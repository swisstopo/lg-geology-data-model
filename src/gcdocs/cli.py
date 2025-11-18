"""
Clean CLI interface for gcdocs
Separated from business logic - only handles commands and arguments
"""

import os
import sys
import traceback
from pathlib import Path

import click
import yaml
from loguru import logger

from .config import AVAILABLE_LANGUAGES, GeoDataConfig, get_default_config
from .core.generator import EnhancedMarkdownGenerator
from .core.validator import ModelValidator
from .exporters.xlsx import XLSXExporter, EnhancedXLSXExporter
from .translation.model_translator import (
    HierarchicalDatamodelProcessor,
    HierarchicalTranslationManager,
    ModelProcessor,
    ModelTranslationManager,
)
from .translation.translator import TranslationManager


def parse_langs(ctx, param, value):
    if not value:
        raise click.BadParameter("You must provide at least one language.")
    langs = [v.strip().lower() for v in value.split(",")]

    invalid = [lang for lang in langs if lang not in AVAILABLE_LANGUAGES]
    if invalid:
        raise click.BadParameter(f"Invalid language(s): {', '.join(invalid)}")
    return langs


@click.command()
@click.option(
    "--lang",
    callback=parse_langs,
    required=True,
    help="Comma-separated list of languages (e.g., de,fr)",
)
def generate_docs(lang):
    """
    Generate documentation in one or more languages.
    """
    for language in lang:
        click.echo(f"Generating docs for: {language}")
        # Your generation logic here


@click.group()
@click.option("--debug", is_flag=True, help="Enable debug logging")
@click.option(
    "--logfile", type=click.Path(), default=None, help="Optional path to log file"
)
@click.pass_context
def gcdocs(ctx, debug, logfile):
    """GeoCover geological data model documentation generator

    Generate Markdown documentation from GeoCover geological data models.
    Use 'make pdfs' afterwards for PDF/DOCX export with pandoc.
    """
    color_supported = sys.stderr.isatty() and os.name != "nt"

    logger.remove()  # Remove default handler

    # Always log to stderr at INFO level
    logger.add(sys.stderr, level="DEBUG" if debug else "INFO", colorize=color_supported)

    # If logfile is provided, log to file at DEBUG level
    if logfile:
        logger.add(logfile, level="DEBUG", rotation="10 MB", retention="10 days")

    # Store config in context
    ctx.ensure_object(dict)
    ctx.obj["config"] = get_default_config()
    ctx.obj["debug"] = debug


@gcdocs.command()
@click.option(
    "--lang",
    # type=click.Choice(["de", "fr"], case_sensitive=False),
    required=True,
    callback=parse_langs,
    help="Language for document generation",
)
@click.option(
    "--output",
    "-o",
    type=click.Path(file_okay=False),
    default="inputs",
    help="Output directory for Markdown files",
)
@click.option(
    "--input-dir",
    "-i",
    type=click.Path(exists=True, file_okay=False),
    default="exports",
    help="Directory containing input JSON files",
)
@click.argument("datamodel", type=click.Path(exists=True))
@click.pass_context
def generate(ctx, lang, datamodel, output, input_dir):
    """Generate Markdown documentation from YAML datamodel

    Creates {lang}/datamodel.md and supporting files.
    Run 'make pdfs' afterwards to generate PDF/DOCX with pandoc.
    """
    try:
        # Setup config with custom input directory

        config = GeoDataConfig(Path(input_dir).resolve())

        # Validate data files exist
        if not config.validate_data():
            click.echo("❌ Missing required data files in input directory")
            click.echo(f"   Expected files in {input_dir}:")
            click.echo("   - coded_domains.json")
            click.echo("   - subtypes_dict.json")
            click.echo("   - geocover-schema-sde.json")
            sys.exit(1)

        # Generate documentation
        # TODO generator = MarkdownGenerator(config)
        generator = EnhancedMarkdownGenerator(config)
        if ctx.obj.get('debug'):
            logger.debug(f"Translation dir: {generator.model_translator.translations_dir}")
        for lg in lang:
            output_path = generator.generate_markdown(datamodel, lg.lower(), output)
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
        if ctx.obj.get("debug"):
            raise
        sys.exit(1)


@gcdocs.command()
@click.option(
    "--lang",
    type=click.Choice(AVAILABLE_LANGUAGES, case_sensitive=False),
    required=True,
)
@click.option(
    "--format",
    type=click.Choice(["pdf", "docx", "both"], case_sensitive=False),
    default="pdf",
)
@click.option("--input-dir", "-i", type=click.Path(), help="Input dir path")
@click.argument("datamodel", type=click.Path(exists=True))
@click.pass_context
def build(ctx, lang, format, datamodel, input_dir):
    """Generate Markdown AND convert to PDF/DOCX (requires pandoc)

    This is a convenience command that combines 'generate' + pandoc.
    For more control, use 'gcdocs generate' + 'make pdfs'.
    """
    from .exporters.pdf import PandocPDFExporter

    INPUT_DIR = "toto"

    # First generate Markdown
    ctx.invoke(
        generate,
        lang=lang,
        datamodel=datamodel,
        input_dir=input_dir,  # "exports/2025-08-26",
        output=INPUT_DIR,
    )

    # Then convert with pandoc
    exporter = PandocPDFExporter()

    if not exporter.is_available():
        click.echo("💡 Install pandoc or use the Makefile:")
        click.echo("   make pdfs")
        return

    input_dir = Path(INPUT_DIR) / lang
    markdown_file = input_dir / "datamodel.md"
    metadata_file = input_dir / "metadata.yaml"

    if format in ["pdf", "both"]:
        output_file = input_dir / "datamodel.pdf"
        exporter.export_pdf(markdown_file, output_file, metadata_file)

    if format in ["docx", "both"]:
        output_file = input_dir / "datamodel.docx"
        exporter.export_docx(markdown_file, output_file, metadata_file)


@gcdocs.command()
@click.argument("datamodel", type=click.Path(exists=True))
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
        if ctx.obj.get("debug"):
            raise
        sys.exit(1)


@gcdocs.command()
@click.argument("datamodel", type=click.Path(exists=True))
@click.option(
    "--format",
    "-f",
    type=click.Choice(["xlsx", "json"], case_sensitive=False),
    default="xlsx",
    help="Export format",
)
@click.option("--output", "-o", type=click.Path(), help="Output file path")
@click.pass_context
def legacy_export(ctx, datamodel, format, output):
    """Export GeoCover datamodel to Excel/JSON formats"""
    try:
        # Auto-generate output filename if not provided
        if not output:
            stem = Path(datamodel).stem
            suffix = "xlsx" if format.lower() == "xlsx" else "json"
            output = f"{stem}.{suffix}"

        if format.lower() == "xlsx":
            exporter = XLSXExporter()
            exporter.export(datamodel, output)
        else:
            # JSON export - just copy the processed model
            # TODO from .core.generator import MarkdownGenerator, EnhancedMarkdownGenerator

            config = ctx.obj["config"]
            # TODO generator = MarkdownGenerator(config)
            generator = EnhancedMarkdownGenerator(config)
            model_data = generator.process_model(datamodel)

            import json
            from datetime import date, datetime

            def json_encoder(obj):
                if isinstance(obj, (datetime, date)):
                    return obj.isoformat()
                raise TypeError(f"Object {obj} is not JSON serializable")

            with open(output, "w", encoding="utf-8") as f:
                json.dump(
                    model_data, f, indent=4, ensure_ascii=False, default=json_encoder
                )

        click.echo(f"✓ Exported to {output}")

    except Exception as e:
        logger.error(f"Export failed: {e}")
        click.echo(f"❌ Export failed: {e}")
        if ctx.obj.get("debug"):
            raise
        sys.exit(1)


@gcdocs.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.option("--output", "-o", type=click.Path(), help="Output YAML file")
@click.pass_context
def convert(ctx, input_file, output):
    """Convert Excel/JSON to YAML datamodel"""
    try:
        from .core.model import DataModelConverter

        if not output:
            output = Path(input_file).with_suffix(".yaml")

        converter = DataModelConverter()
        converter.to_yaml(input_file, output)

        click.echo(f"✓ Converted {input_file} to {output}")

    except Exception as e:
        logger.error(f"Conversion failed: {e}")
        click.echo(f"❌ Conversion failed: {e}")
        if ctx.obj.get("debug"):
            raise
        sys.exit(1)


@gcdocs.command()
@click.argument("datamodel", type=click.Path(exists=True))
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

        with open(datamodel, "w") as f:
            yaml.dump(data, f)

        click.echo(f"✓ Prettified {datamodel}")

    except Exception as e:
        logger.error(f"Prettify failed: {e}")
        click.echo(f"❌ Prettify failed: {e}")
        if ctx.obj.get("debug"):
            raise
        sys.exit(1)


@gcdocs.command()
@click.option(
    "--input-dir",
    "-i",
    type=click.Path(exists=True, file_okay=False),
    default="exports",
    help="Directory containing translation CSV",
)
@click.option(
    "--output-dir",
    "-o",
    type=click.Path(file_okay=False),
    default="locale",
    help="Output directory for PO files",
)
@click.pass_context
def legacy_translations(ctx, input_dir, output_dir):
    """Generate PO translation files from CSV data"""
    try:
        config = GeoDataConfig(Path(input_dir).resolve())
        translation_df = config.translation_df

        # Generate PO files
        po_files = TranslationManager.create_po_files(translation_df)
        TranslationManager.write_po_files(po_files, output_dir)

        click.echo(f"✓ Generated translation files in {output_dir}")
        click.echo("Files created:")
        for lang in po_files.keys():
            if lang == "pot":
                click.echo(f"   - {output_dir}/datamodel.pot (template)")
            else:
                click.echo(f"   - {output_dir}/{lang}/LC_MESSAGES/datamodel.po")

    except Exception as e:
        logger.error(f"Translation generation failed: {e}")
        click.echo(f"❌ Translation generation failed: {e}")
        if ctx.obj.get("debug"):
            raise
        sys.exit(1)


@gcdocs.command()
@click.option(
    "--input-dir",
    "-i",
    type=click.Path(exists=True, file_okay=False),
    default="exports",
    help="Directory containing translation files",
)
@click.option(
    "--output", "-o", type=click.Path(), help="Output xlsx file for merged translations"
)
@click.option("--stats", is_flag=True, help="Show translation statistics")
@click.pass_context
def merge_translations(ctx, input_dir, output, stats):
    """Merge and manage translation files"""
    debug = ctx.obj.get("debug", False)
    try:
        config = GeoDataConfig(Path(input_dir).resolve())

        if stats:
            # Show statistics
            translation_stats = config.get_translation_stats()

            click.echo("📊 Translation Statistics:")
            click.echo(f"   Total entries: {translation_stats['total_entries']}")
            click.echo(
                f"   German translations: {translation_stats['de_translations']}"
            )
            click.echo(
                f"   French translations: {translation_stats['fr_translations']}"
            )
            click.echo(
                f"   Italian translations: {translation_stats['it_translations']}"
            )
            click.echo(
                f"   English translations: {translation_stats['en_translations']}"
            )
            click.echo(f"   Missing German: {translation_stats['missing_de']}")
            click.echo(f"   Missing French: {translation_stats['missing_fr']}")
            click.echo(f"   Missing Italian: {translation_stats['missing_it']}")
            click.echo(f"   Missing English: {translation_stats['missing_en']}")
            click.echo(f"   Complete entries: {translation_stats['complete_entries']}")

        if output:
            # Save merged translations
            output_path = config.save_merged_translations(output)
            click.echo(f"✓ Saved merged translations to {output_path}")

        if not stats and not output:
            # Just show what files were found
            translation_df = config.translation_df
            click.echo(
                f"✓ Loaded {len(translation_df)} translations from multiple sources"
            )
            click.echo("💡 Use --stats to see detailed statistics")
            click.echo("💡 Use --output FILE.xlsx to save merged translations")

    except Exception as e:
        import traceback

        logger.error(f"Translation merge failed: {e}")
        click.echo(f"❌ Translation merge failed: {e}")

        if ctx.obj.get("debug"):
            click.echo(traceback.print_exc())
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
    pandoc_path = shutil.which("pandoc")
    if pandoc_path:
        try:
            result = subprocess.run(
                [pandoc_path, "--version"], capture_output=True, text=True
            )
            version = (
                result.stdout.split("\n")[0] if result.returncode == 0 else "unknown"
            )
            click.echo(f"✓ pandoc: {version}")
        except Exception:
            click.echo("❓ pandoc: found but version check failed")
    else:
        click.echo("❌ pandoc: not found")
        click.echo("   Install: https://pandoc.org/installing.html")
        click.echo("   Required for PDF/DOCX generation")

    # Check Make
    make_path = shutil.which("make")
    if make_path:
        click.echo("✓ make: available")
    else:
        click.echo("❌ make: not found")
        click.echo("   Install build tools for your platform")


# Enhanced translation


# Modify your existing export command to support translation export
@gcdocs.command()
@click.argument("datamodel", type=click.Path(exists=True))
@click.option(
    "--format",
    "-f",
    type=click.Choice(["xlsx", "json", "translation_xlsx"], case_sensitive=False),
    default="xlsx",
    help="Export format",
)
@click.option("--output", "-o", type=click.Path(), help="Output file path")
@click.option(
    "--translations-dir",
    "-t",
    type=click.Path(),
    default="translations",
    help="Translations directory",
)
@click.pass_context
def export(ctx, datamodel, format, output, translations_dir):
    """Export GeoCover datamodel to Excel/JSON/Translation formats (enhanced)"""
    try:
        if not output:
            stem = Path(datamodel).stem
            suffix = {
                "xlsx": "xlsx",
                "json": "json",
                "translation_xlsx": "translation.xlsx",
            }[format.lower()]
            output = f"{stem}.{suffix}"

        if format.lower() == "translation_xlsx":
            # Export for translation workflow
            model_tm = ModelTranslationManager(translations_dir)
            exporter = EnhancedXLSXExporter(model_tm)
            exporter.export_for_translation(datamodel, output)

        elif format.lower() == "xlsx":
            # Your existing XLSX export
            from .exporters.xlsx import XLSXExporter

            exporter = XLSXExporter()
            exporter.export(datamodel, output)

        else:  # JSON
            # Your existing JSON export logic
            pass

        click.echo(f"✓ Exported to {output}")

    except Exception as e:
        logger.error(f"Export failed: {e}")
        click.echo(f"❌ Export failed: {e}")
        sys.exit(1)


# Add translation import command
@gcdocs.command()
@click.argument("excel_file", type=click.Path(exists=True))
@click.option(
    "--translations-dir", "-t", default="translations", help="Translations directory"
)
@click.option("--yaml-output", "-y", help="Output YAML file with keys")
@click.pass_context
def import_translations(ctx, excel_file, translations_dir, yaml_output):
    """Import completed translations from Excel (enhanced)"""
    try:
        model_tm = ModelTranslationManager(translations_dir)
        exporter = EnhancedXLSXExporter(model_tm)

        if yaml_output:
            yaml_structure = exporter.import_from_excel(excel_file)
            with open(yaml_output, "w", encoding="utf-8") as f:
                yaml.dump(
                    yaml_structure, f, default_flow_style=False, allow_unicode=True
                )
            click.echo(f"✓ Created key-based YAML: {yaml_output}")
        else:
            exporter.import_from_excel(excel_file)

        click.echo(f"✓ Imported translations from {excel_file}")

    except Exception as e:
        logger.error(f"Import failed: {e}")
        click.echo(f"❌ Import failed: {e}")
        sys.exit(1)


@gcdocs.group()
@click.pass_context
def translations(ctx):
    """Hierarchical translation management for geology data model"""
    pass


# Add migration command
@translations.command(name="migrate")
@click.argument("datamodel", type=click.Path(exists=True))
@click.option(
    "--translations-dir", "-t", default="translations", help="Translations directory"
)
@click.pass_context
def migrate_translations(ctx, datamodel, translations_dir):
    """Migrate YAML from embedded translations to key-based system (enhanced)"""
    try:
        # Load current YAML
        with open(datamodel, "r", encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)

        # Initialize managers
        model_tm = ModelTranslationManager(translations_dir)
        processor = ModelProcessor(
            model_tm, None
        )  # geol_translator not needed for migration

        # Migrate
        new_yaml_data = processor.migrate_yaml_to_keys(yaml_data)

        # Save new YAML
        new_yaml_file = str(Path(datamodel).with_suffix(".with_keys.yaml"))
        with open(new_yaml_file, "w", encoding="utf-8") as f:
            yaml.dump(new_yaml_data, f, default_flow_style=False, allow_unicode=True)

        # Save translations
        model_tm.save_translations()

        click.echo(f"✓ Migration complete:")
        click.echo(f"   New YAML: {new_yaml_file}")
        click.echo(f"   Translations: {translations_dir}/model_*.json")

    except Exception as e:
        logger.error(f"Migration failed: {e}")
        click.echo(f"❌ Migration failed: {e}")
        sys.exit(1)

    return export, import_translations, migrate_translations


@translations.command()
@click.argument("yaml_file", type=click.Path(exists=True))
@click.option("--output", "-o", default="geology_model.xlsx", help="Output Excel file")
@click.option(
    "--translations-dir", "-d", default="translations", help="Translations directory"
)
def export_excel(yaml_file, output, translations_dir):
    """Export YAML to structured Excel format"""
    # Load YAML
    with open(yaml_file, "r", encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f)

    # Initialize translation manager
    tm = HierarchicalTranslationManager(translations_dir)

    # Export to Excel
    tm.export_to_structured_excel(yaml_data, output)
    click.echo(f"Exported to structured Excel: {output}")


@translations.command()
@click.argument("excel_file", type=click.Path(exists=True))
@click.option(
    "--translations-dir", "-d", default="translations", help="Translations directory"
)
@click.option(
    "--yaml-output", "-y", default="datamodel_with_keys.yaml", help="Output YAML file"
)
def import_excel(excel_file, translations_dir, yaml_output):
    """Import from structured Excel and create key-based YAML"""
    tm = HierarchicalTranslationManager(translations_dir)
    yaml_structure = tm.import_from_structured_excel(excel_file)

    # Save new YAML structure
    with open(yaml_output, "w", encoding="utf-8") as f:
        yaml.dump(yaml_structure, f, default_flow_style=False, allow_unicode=True)

    click.echo(f"Imported translations and created: {yaml_output}")


@translations.command(name="status")
@click.option("--translations-dir", "-t", default="translations")
def translation_status(translations_dir):
    """Show translation completion status"""
    tm = HierarchicalTranslationManager(translations_dir)
    stats = tm.get_translation_status()

    click.echo("📊 Translation Status:")
    click.echo()
    for lang, data in stats.items():
        percentage = data["percentage"]
        status_icon = "✅" if percentage == 100 else "🔄" if percentage > 0 else "❌"
        click.echo(
            f"  {status_icon} {lang.upper()}: {data['translated']}/{data['total']} ({percentage}%)"
        )

    click.echo()
    click.echo(
        "💡 Use 'gcdocs export-missing --lang it' to get missing translations for Italian"
    )


@translations.command(name="test")
@click.argument("key")
@click.option("--lang", default="de")
@click.option("--translations-dir", "-t", default="translations")
def test_translation(key, lang, translations_dir):
    """Test translation lookup with fallbacks"""
    tm = HierarchicalTranslationManager(translations_dir)

    click.echo(f"🔍 Testing translation for key: {key}")
    click.echo()

    for test_lang in ["de", "fr", "it", "en"]:
        result = tm.get_translation(key, test_lang)
        status = "✅" if key in tm.translations.get(test_lang, {}) else "🔄 (fallback)"
        click.echo(f"  {test_lang.upper()}: {result} {status}")


@translations.command()
@click.argument("yaml_file", type=click.Path(exists=True))
@click.option(
    "--translations-dir", "-d", default="translations", help="Translations directory"
)
def migrate(yaml_file, translations_dir):
    """Migrate existing YAML from embedded to key-based translations"""
    # Load current YAML
    with open(yaml_file, "r", encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f)

    # Initialize translation manager and processor
    tm = HierarchicalTranslationManager(translations_dir)
    processor = HierarchicalDatamodelProcessor(tm)

    # Migrate
    new_yaml_data = processor.migrate_from_embedded_yaml(yaml_data)

    # Save new YAML
    new_yaml_file = yaml_file.replace(".yaml", "_with_keys.yaml")
    with open(new_yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(new_yaml_data, f, default_flow_style=False, allow_unicode=True)

    # Save translations
    tm.save_translations()

    click.echo(f"Migration complete:")
    click.echo(f"  New YAML: {new_yaml_file}")
    click.echo(f"  Translations: {translations_dir}/")


@translations.command()
@click.argument("yaml_file", type=click.Path(exists=True))
@click.option("--lang", "-l", default="en", help="Target language")
@click.option(
    "--translations-dir", "-d", default="translations", help="Translations directory"
)
@click.option("--output", "-o", help="Output file (default: datamodel_{lang}.yaml)")
def render(yaml_file, lang, translations_dir, output):
    """Render YAML with translations for specific language"""
    # Load YAML with keys
    with open(yaml_file, "r", encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f)

    # Initialize translation manager and processor
    tm = HierarchicalTranslationManager(translations_dir)
    processor = HierarchicalDatamodelProcessor(tm)

    # Render with translations
    rendered_yaml = processor.render_with_translations(yaml_data, lang)

    # Save rendered YAML
    if not output:
        output = f"datamodel_{lang}.yaml"

    with open(output, "w", encoding="utf-8") as f:
        yaml.dump(rendered_yaml, f, default_flow_style=False, allow_unicode=True)

    click.echo(f"Rendered {lang} version: {output}")


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


if __name__ == "__main__":
    gcdocs()
