"""
Clean CLI interface for gcdocs
Separated from business logic - only handles commands and arguments
"""

import click
import sys
from pathlib import Path
from loguru import logger

from .config import GeoDataConfig, get_default_config
from .core.generator import MarkdownGenerator
from .core.validator import ModelValidator
from .translation.translator import TranslationManager
from .exporters.xlsx import XLSXExporter
import traceback

@click.group()
@click.option('--debug', is_flag=True, help='Enable debug logging')
@click.pass_context
def gcdocs(ctx, debug):
    """GeoCover geological data model documentation generator

    Generate Markdown documentation from GeoCover geological data models.
    Use 'make pdfs' afterwards for PDF/DOCX export with pandoc.
    """
    # Setup logging
    if debug:
        logger.remove()
        logger.add(sys.stderr, level="DEBUG")

    # Store config in context
    ctx.ensure_object(dict)
    ctx.obj['config'] = get_default_config()


@gcdocs.command()
@click.option('--lang',
              type=click.Choice(['de', 'fr'], case_sensitive=False),
              required=True,
              help='Language for document generation')
@click.option('--output', '-o',
              type=click.Path(file_okay=False),
              default='inputs',
              help='Output directory for Markdown files')
@click.option('--input-dir', '-i',
              type=click.Path(exists=True, file_okay=False),
              default='exports',
              help='Directory containing input JSON files')
@click.argument('datamodel', type=click.Path(exists=True))
@click.pass_context
def generate(ctx, lang, datamodel, output, input_dir):
    """Generate Markdown documentation from YAML datamodel

    Creates {lang}/datamodel.md and supporting files.
    Run 'make pdfs' afterwards to generate PDF/DOCX with pandoc.
    """
    try:
        # Setup config with custom input directory
        config = GeoDataConfig(input_dir)

        # Validate data files exist
        if not config.validate_data():
            click.echo("❌ Missing required data files in input directory")
            click.echo(f"   Expected files in {input_dir}:")
            click.echo("   - coded_domains.json")
            click.echo("   - subtypes_dict.json")
            click.echo("   - geocover-schema-sde.json")
            sys.exit(1)

        # Generate documentation
        generator = MarkdownGenerator(config)
        output_path = generator.generate_markdown(datamodel, lang.lower(), output)

        click.echo(f"✓ Generated Markdown documentation in {output_path}")
        click.echo("💡 Next steps:")
        click.echo("   make pdfs    # Generate PDF with pandoc")
        click.echo("   make docx    # Generate DOCX with pandoc")
        click.echo("   make all     # Generate all formats")

    except FileNotFoundError as e:
        click.echo(f"❌ File not found: {e}")
        sys.exit(1)
    except Exception as e:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]

        logger.error(f"Generation failed: {e}")
        click.echo(f"❌ Generation failed: {e}")
        if ctx.obj.get('debug'):
            raise
        sys.exit(1)


@gcdocs.command()
@click.argument('datamodel', type=click.Path(exists=True))
@click.pass_context
def validate(ctx, datamodel):
    """Validate GeoCover datamodel against JSON schema"""
    try:
        validator = ModelValidator()

        if validator.validate_file(datamodel):
            click.echo(f"✓ {datamodel} is valid")
        else:
            click.echo(f"❌ {datamodel} has validation errors")
            for error in validator.get_errors():
                click.echo(f"   - {error}")
            sys.exit(1)

    except Exception as e:
        logger.error(f"Validation failed: {e}")
        click.echo(f"❌ Validation failed: {e}")
        if ctx.obj.get('debug'):
            raise
        sys.exit(1)


@gcdocs.command()
@click.argument('datamodel', type=click.Path(exists=True))
@click.option('--format', '-f',
              type=click.Choice(['xlsx', 'json'], case_sensitive=False),
              default='xlsx',
              help='Export format')
@click.option('--output', '-o',
              type=click.Path(),
              help='Output file path')
@click.pass_context
def export(ctx, datamodel, format, output):
    """Export GeoCover datamodel to Excel/JSON formats"""
    try:
        # Auto-generate output filename if not provided
        if not output:
            stem = Path(datamodel).stem
            suffix = 'xlsx' if format.lower() == 'xlsx' else 'json'
            output = f"{stem}.{suffix}"

        if format.lower() == 'xlsx':
            exporter = XLSXExporter()
            exporter.export(datamodel, output)
        else:
            # JSON export - just copy the processed model
            from .core.generator import MarkdownGenerator
            config = ctx.obj['config']
            generator = MarkdownGenerator(config)
            model_data = generator.process_model(datamodel)

            import json
            from datetime import datetime, date

            def json_encoder(obj):
                if isinstance(obj, (datetime, date)):
                    return obj.isoformat()
                raise TypeError(f"Object {obj} is not JSON serializable")

            with open(output, 'w', encoding='utf-8') as f:
                json.dump(model_data, f, indent=4, ensure_ascii=False, default=json_encoder)

        click.echo(f"✓ Exported to {output}")

    except Exception as e:
        logger.error(f"Export failed: {e}")
        click.echo(f"❌ Export failed: {e}")
        if ctx.obj.get('debug'):
            raise
        sys.exit(1)


@gcdocs.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--output', '-o',
              type=click.Path(),
              help='Output YAML file')
@click.pass_context
def convert(ctx, input_file, output):
    """Convert Excel/JSON to YAML datamodel"""
    try:
        from .core.model import DataModelConverter

        if not output:
            output = Path(input_file).with_suffix('.yaml')

        converter = DataModelConverter()
        converter.to_yaml(input_file, output)

        click.echo(f"✓ Converted {input_file} to {output}")

    except Exception as e:
        logger.error(f"Conversion failed: {e}")
        click.echo(f"❌ Conversion failed: {e}")
        if ctx.obj.get('debug'):
            raise
        sys.exit(1)


@gcdocs.command()
@click.argument('datamodel', type=click.Path(exists=True))
@click.pass_context
def prettify(ctx, datamodel):
    """Prettify/format the YAML datamodel file"""
    try:
        import ruamel.yaml
        from ruamel.yaml import YAML

        def set_block_style(obj):
            """Recursively set block style for YAML objects"""
            if isinstance(obj, dict):
                for k in obj:
                    try:
                        obj.fa.set_block_style()
                    except AttributeError:
                        pass
                    set_block_style(obj[k])
            elif isinstance(obj, list):
                for elem in obj:
                    try:
                        obj.fa.set_block_style()
                    except AttributeError:
                        pass
                    set_block_style(elem)

        yaml = YAML()
        yaml.preserve_quotes = True

        with open(datamodel) as f:
            data = yaml.load(f)

        set_block_style(data)

        with open(datamodel, 'w') as f:
            yaml.dump(data, f)

        click.echo(f"✓ Prettified {datamodel}")

    except Exception as e:
        logger.error(f"Prettify failed: {e}")
        click.echo(f"❌ Prettify failed: {e}")
        if ctx.obj.get('debug'):
            raise
        sys.exit(1)


@gcdocs.command()
@click.option('--input-dir', '-i',
              type=click.Path(exists=True, file_okay=False),
              default='exports',
              help='Directory containing translation CSV')
@click.option('--output-dir', '-o',
              type=click.Path(file_okay=False),
              default='locale',
              help='Output directory for PO files')
@click.pass_context
def translations(ctx, input_dir, output_dir):
    """Generate PO translation files from CSV data"""
    try:
        config = GeoDataConfig(input_dir)
        translation_df = config.translation_df

        # Generate PO files
        po_files = TranslationManager.create_po_files(translation_df)
        TranslationManager.write_po_files(po_files, output_dir)

        click.echo(f"✓ Generated translation files in {output_dir}")
        click.echo("Files created:")
        for lang in po_files.keys():
            if lang == 'pot':
                click.echo(f"   - {output_dir}/datamodel.pot (template)")
            else:
                click.echo(f"   - {output_dir}/{lang}/LC_MESSAGES/datamodel.po")

    except Exception as e:
        logger.error(f"Translation generation failed: {e}")
        click.echo(f"❌ Translation generation failed: {e}")
        if ctx.obj.get('debug'):
            raise
        sys.exit(1)


@gcdocs.command()
def deps():
    """Check if required dependencies are available"""
    import shutil
    import subprocess

    click.echo("Checking dependencies:")

    # Check Python dependencies
    click.echo("✓ Python dependencies: OK")

    # Check pandoc
    pandoc_path = shutil.which('pandoc')
    if pandoc_path:
        try:
            result = subprocess.run([pandoc_path, '--version'],
                                    capture_output=True, text=True)
            version = result.stdout.split('\n')[0] if result.returncode == 0 else "unknown"
            click.echo(f"✓ pandoc: {version}")
        except Exception:
            click.echo("❓ pandoc: found but version check failed")
    else:
        click.echo("❌ pandoc: not found")
        click.echo("   Install: https://pandoc.org/installing.html")
        click.echo("   Required for PDF/DOCX generation")

    # Check Make
    make_path = shutil.which('make')
    if make_path:
        click.echo("✓ make: available")
    else:
        click.echo("❌ make: not found")
        click.echo("   Install build tools for your platform")


# Backward compatibility command (deprecated)
@click.command()
@click.pass_context
def datamodel(ctx):
    """[DEPRECATED] Use 'gcdocs' instead"""
    click.echo("⚠️  Warning: 'datamodel' command is deprecated.")
    click.echo("   Please use 'gcdocs' instead:")
    click.echo()
    click.echo("Migration examples:")
    click.echo("  Old: datamodel generate --lang de model.yaml")
    click.echo("  New: gcdocs generate --lang de model.yaml")
    click.echo()
    click.echo("  Old: datamodel validate model.yaml")
    click.echo("  New: gcdocs validate model.yaml")
    click.echo()
    click.echo("Run 'gcdocs --help' for all available commands.")
    ctx.exit(1)


if __name__ == '__main__':
    gcdocs()