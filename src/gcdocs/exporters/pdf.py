# gcdocs/exporters/pdf.py
"""
Optional PDF exporter that wraps pandoc calls
Provides convenience for users who don't want to use Make
"""

import subprocess
import shutil
from pathlib import Path
import click
from typing import Optional, List


class PandocPDFExporter:
    """Simple wrapper around pandoc for PDF generation"""

    def __init__(self):
        self.pandoc_path = self._find_pandoc()

    def _find_pandoc(self) -> Optional[str]:
        """Find pandoc executable"""
        return shutil.which('pandoc')

    def is_available(self) -> bool:
        """Check if pandoc is available"""
        return self.pandoc_path is not None

    def export_pdf(self, markdown_file: Path, output_file: Path,
                   metadata_file: Optional[Path] = None) -> bool:
        """
        Export markdown to PDF using pandoc
        Simplified version of your Makefile commands
        """
        if not self.is_available():
            click.echo("❌ pandoc not found. Please install pandoc or use 'make pdfs'")
            return False

        # Basic pandoc command (simplified from your Makefile)
        cmd = [
            self.pandoc_path,
            '-s',  # standalone
            '--pdf-engine=xelatex',
            '-V', 'papersize:a4',
            '--number-sections',
            '--shift-heading-level-by=-1',
            '--variable', 'mainfont=DejaVu Sans',
            '-V', 'colorlinks=true',
            '-V', 'linkcolor=teal',
            '-V', 'urlcolor=teal',
            '-V', 'toccolor=gray',
        ]

        # Add metadata if provided
        if metadata_file and metadata_file.exists():
            cmd.extend(['--metadata-file', str(metadata_file)])

        # Add input and output
        cmd.extend(['-o', str(output_file), str(markdown_file)])

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            click.echo(f"✓ Generated {output_file}")
            return True
        except subprocess.CalledProcessError as e:
            click.echo(f"❌ pandoc failed: {e.stderr}")
            return False
        except Exception as e:
            click.echo(f"❌ Error: {e}")
            return False

    def export_docx(self, markdown_file: Path, output_file: Path,
                    metadata_file: Optional[Path] = None) -> bool:
        """Export to DOCX format"""
        if not self.is_available():
            click.echo("❌ pandoc not found. Please install pandoc or use 'make docx'")
            return False

        cmd = [
            self.pandoc_path,
            '-s',
            '-V', 'papersize:a4',
            '--number-sections',
            '--shift-heading-level-by=-1',
        ]

        if metadata_file and metadata_file.exists():
            cmd.extend(['--metadata-file', str(metadata_file)])

        cmd.extend(['-o', str(output_file), str(markdown_file)])

        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            click.echo(f"✓ Generated {output_file}")
            return True
        except subprocess.CalledProcessError as e:
            click.echo(f"❌ pandoc failed: {e.stderr}")
            return False