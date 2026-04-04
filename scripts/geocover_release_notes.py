#!/usr/bin/env python3
"""
geocover_release_notes.py

Generate Markdown release notes from SCHEMA_CHANGES.yaml and DATA_RELEASES.yaml.

Commands:
    schema    Render schema version changelog
    data      Render data release log
    both      Render both documents

Options applying to all commands:
    --latest          Only render the most recent entry
    --stdout          Print to stdout instead of writing a file
    --validate        Validate YAML only, no rendering
    --no-summary      Skip the Rich summary table

Examples:
    python geocover_release_notes.py schema
    python geocover_release_notes.py data --latest --stdout
    python geocover_release_notes.py both
    python geocover_release_notes.py schema --version 4.1 --stdout
    python geocover_release_notes.py data --release R16 --stdout
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import click
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined, TemplateNotFound
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console(stderr=True)

# ── Change type display metadata ────────────────────────────────────────────

CHANGE_TYPES: dict[str, tuple[str, str]] = {
    "value_added":           ("green",  "➕"),
    "value_removed":         ("red",    "➖"),
    "attribute_added":       ("green",  "➕"),
    "attribute_removed":     ("red",    "➖"),
    "class_added":           ("green",  "🆕"),
    "class_removed":         ("red",    "🗑️ "),
    "domain_source_changed": ("yellow", "🔄"),
    "hierarchy_changed":     ("yellow", "🔀"),
    "content_cleared":       ("yellow", "🧹"),
    "class_content_removed": ("red",    "✂️ "),
    "data_fill":             ("cyan",   "🔲"),
    "attribute_relinked":    ("yellow", "🔗"),
}
KNOWN_TYPES = set(CHANGE_TYPES)


# ── YAML loading ─────────────────────────────────────────────────────────────

def load_yaml(path: Path) -> dict:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        console.print(Panel(str(exc), title=f"[red]YAML error: {path}[/red]", border_style="red"))
        sys.exit(1)
    if not isinstance(data, dict):
        console.print(f"[red]YAML root must be a mapping: {path}[/red]")
        sys.exit(1)
    return data


# ── Cross-reference ──────────────────────────────────────────────────────────

def cross_reference(schema_data: dict, release_data: dict) -> tuple[list, list]:
    """
    Enrich schema_versions with _used_by list of release numbers.
    Enrich releases with _schema_info (the matching schema_version entry).
    Returns (schema_versions, releases).
    """
    schema_versions: list[dict] = schema_data.get("schema_versions", [])
    releases: list[dict] = release_data.get("releases", [])

    # Index schema by version string
    schema_index = {sv.get("version"): sv for sv in schema_versions}

    for sv in schema_versions:
        sv["_used_by"] = []

    for r in releases:
        sv_key = r.get("schema_version")
        r["_schema_info"] = schema_index.get(sv_key)
        if sv_key and sv_key in schema_index:
            schema_index[sv_key]["_used_by"].append(r.get("release", "?"))

    return schema_versions, releases


# ── Validation ───────────────────────────────────────────────────────────────

def validate_schema(data: dict) -> list[str]:
    errors = []
    versions = data.get("schema_versions", [])
    seen = set()
    for i, sv in enumerate(versions):
        loc = f"schema_versions[{i}] ({sv.get('version', '?')})"
        v = sv.get("version")
        if not v:
            errors.append(f"{loc}: missing 'version'")
        elif v in seen:
            errors.append(f"{loc}: duplicate version '{v}'")
        else:
            seen.add(v)
        for j, ch in enumerate(sv.get("changes") or []):
            cloc = f"{loc}.changes[{j}]"
            if not ch.get("note"):
              if not ch.get("class"):
                errors.append(f"{cloc}: missing 'class'")
              t = ch.get("type")
              if not t:
                errors.append(f"{cloc}: missing 'type'")
              elif t not in KNOWN_TYPES:
                errors.append(f"{cloc}: unknown type '{t}'")
              if t == "value_added" and not ch.get("values"):
                errors.append(f"{cloc}: 'value_added' requires a 'values' list")
              if t == "domain_source_changed":
                for field in ("from", "to"):
                    if not ch.get(field):
                        errors.append(f"{cloc}: 'domain_source_changed' requires '{field}'")
    return errors


def validate_releases(data: dict) -> list[str]:
    errors = []
    releases = data.get("releases", [])
    seen = set()
    for i, r in enumerate(releases):
        loc = f"releases[{i}] ({r.get('release', '?')})"
        rel = r.get("release")
        if not rel:
            errors.append(f"{loc}: missing 'release'")
        elif rel in seen:
            errors.append(f"{loc}: duplicate release '{rel}'")
        else:
            seen.add(rel)
    return errors


def report_validation(errors: list[str], label: str) -> bool:
    """Print validation result. Returns True if valid."""
    if errors:
        console.print(Panel(
            "\n".join(f"[red]✗[/red] {e}" for e in errors),
            title=f"[red bold]Validation errors — {label}[/red bold]",
            border_style="red",
        ))
        return False
    console.print(f"[green]✓[/green] {label} validation passed")
    return True


# ── Rich summary tables ──────────────────────────────────────────────────────

def print_schema_summary(schema_versions: list[dict]) -> None:
    table = Table(
        box=box.ROUNDED, header_style="bold cyan",
        title="[bold]Schema Versions[/bold]",
    )
    table.add_column("Version",  style="bold white", no_wrap=True)
    table.add_column("Date",     style="dim")
    table.add_column("Git tag",  style="dim")
    table.add_column("Changes",  justify="right")
    table.add_column("Used by",  style="yellow")
    table.add_column("Types")

    for sv in schema_versions:
        changes = sv.get("changes") or []
        type_counts: dict[str, int] = {}
        for ch in changes:
            t = ch.get("type", "?")
            type_counts[t] = type_counts.get(t, 0) + 1

        type_parts = []
        for t, count in type_counts.items():
            color, icon = CHANGE_TYPES.get(t, ("white", "?"))
            suffix = f"×{count}" if count > 1 else ""
            type_parts.append(f"[{color}]{icon} {t}{suffix}[/{color}]")

        table.add_row(
            sv.get("version", "?"),
            str(sv.get("date", "—")),
            sv.get("git_tag") or "—",
            str(len(changes)) if changes else "[dim]—[/dim]",
            ", ".join(sv.get("_used_by") or []) or "[dim]—[/dim]",
            "\n".join(type_parts) or "[dim]none[/dim]",
        )

    console.print()
    console.print(table)
    console.print()


def print_release_summary(releases: list[dict]) -> None:
    table = Table(
        box=box.ROUNDED, header_style="bold cyan",
        title="[bold]Data Releases[/bold]",
    )
    table.add_column("Release",    style="bold white", no_wrap=True)
    table.add_column("Published",  style="dim")
    table.add_column("Schema v",   style="yellow")
    table.add_column("SDE export", style="dim")
    table.add_column("New data",   justify="right")
    table.add_column("Schema Δ",   justify="right")

    for r in releases:
        sv_key    = r.get("schema_version") or "—"
        new_data  = r.get("new_data") or []
        si        = r.get("_schema_info")
        n_changes = len(si.get("changes") or []) if si else 0

        table.add_row(
            r.get("release", "?"),
            str(r.get("publication_date", "?")),
            sv_key,
            str(r.get("schema_export_date") or "—"),
            str(len(new_data)) if new_data else "[dim]—[/dim]",
            f"[yellow]{n_changes}[/yellow]" if n_changes else "[dim]—[/dim]",
        )

    console.print()
    console.print(table)
    console.print()


# ── Rendering ────────────────────────────────────────────────────────────────

def render(template_path: Path, **context) -> str:
    env = Environment(
        loader=FileSystemLoader(str(template_path.parent)),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    env.filters["selectattr"] = lambda seq, attr: [x for x in seq if x.get(attr)]
    env.filters["rejectattr"] = lambda seq, attr: [x for x in seq if not x.get(attr)]

    try:
        tmpl = env.get_template(template_path.name)
    except TemplateNotFound:
        console.print(f"[red]Template not found:[/red] {template_path}")
        sys.exit(1)
    return tmpl.render(**context)


def write_or_print(content: str, output_path: Path, to_stdout: bool) -> None:
    if to_stdout:
        click.echo(content)
    else:
        output_path.write_text(content, encoding="utf-8")
        lines = content.count("\n")
        console.print(
            f"[green]✓[/green] Written [bold]{output_path}[/bold] [dim]({lines} lines)[/dim]"
        )


# ── Shared options ────────────────────────────────────────────────────────────

def shared_options(f):
    """Decorator that adds common options to a command."""
    for decorator in reversed([
        click.option("--schema-file", "schema_path",
            type=click.Path(exists=True, path_type=Path),
            default="SCHEMA_CHANGES.yaml", show_default=True),
        click.option("--data-file", "release_path",
            type=click.Path(exists=True, path_type=Path),
            default="DATA_RELEASES.yaml", show_default=True),
        click.option("--template-dir", "tmpl_dir",
            type=click.Path(exists=True, file_okay=False, path_type=Path),
            default=None,
            help="Directory containing .j2 templates (default: same dir as this script)."),
        click.option("--latest", is_flag=True, default=False,
            help="Render only the most recent entry."),
        click.option("--stdout", is_flag=True, default=False,
            help="Print to stdout instead of writing a file."),
        click.option("--validate", "validate_only", is_flag=True, default=False,
            help="Validate YAML and exit."),
        click.option("--no-summary", is_flag=True, default=False,
            help="Skip the Rich summary table."),
    ]):
        f = decorator(f)
    return f


def resolve_tmpl_dir(tmpl_dir: Path | None) -> Path:
    return tmpl_dir or Path(__file__).parent


# ── Commands ──────────────────────────────────────────────────────────────────

@click.group()
def cli():
    """GeoCover release notes generator."""


@cli.command()
@shared_options
@click.option("--version", "filter_version", default=None, metavar="X.Y.Z",
    help="Render a specific schema version only.")
@click.option("-o", "--output", "output_path",
    type=click.Path(path_type=Path),
    default="SCHEMA_CHANGES.md", show_default=True)
def schema(schema_path, release_path, tmpl_dir, latest, stdout,
           validate_only, no_summary, filter_version, output_path):
    """Render schema version changelog from SCHEMA_CHANGES.yaml."""

    console.rule("[bold cyan]Schema changes[/bold cyan]")
    schema_data  = load_yaml(schema_path)
    release_data = load_yaml(release_path)

    ok = report_validation(validate_schema(schema_data),   "SCHEMA_CHANGES.yaml")
    ok = report_validation(validate_releases(release_data), "DATA_RELEASES.yaml") and ok
    if validate_only:
        sys.exit(0 if ok else 1)
    if not ok and not click.confirm("Continue despite errors?", default=False):
        sys.exit(1)

    schema_versions, _ = cross_reference(schema_data, release_data)

    if filter_version:
        schema_versions = [sv for sv in schema_versions if sv.get("version") == filter_version]
        if not schema_versions:
            console.print(f"[red]Version '{filter_version}' not found.[/red]")
            sys.exit(1)
    elif latest:
        schema_versions = schema_versions[:1]

    if not no_summary:
        print_schema_summary(schema_versions)

    tmpl = resolve_tmpl_dir(tmpl_dir) / "schema_changes.md.j2"
    content = render(tmpl, schema_versions=schema_versions)
    write_or_print(content, output_path, stdout)


@cli.command()
@shared_options
@click.option("--release", "filter_release", default=None, metavar="RXX",
    help="Render a specific release only (e.g. R16).")
@click.option("-o", "--output", "output_path",
    type=click.Path(path_type=Path),
    default="DATA_RELEASES.md", show_default=True)
def data(schema_path, release_path, tmpl_dir, latest, stdout,
         validate_only, no_summary, filter_release, output_path):
    """Render data release log from DATA_RELEASES.yaml."""

    console.rule("[bold cyan]Data releases[/bold cyan]")
    schema_data  = load_yaml(schema_path)
    release_data = load_yaml(release_path)

    ok = report_validation(validate_schema(schema_data),   "SCHEMA_CHANGES.yaml")
    ok = report_validation(validate_releases(release_data), "DATA_RELEASES.yaml") and ok
    if validate_only:
        sys.exit(0 if ok else 1)
    if not ok and not click.confirm("Continue despite errors?", default=False):
        sys.exit(1)

    _, releases = cross_reference(schema_data, release_data)

    if filter_release:
        releases = [r for r in releases if r.get("release") == filter_release]
        if not releases:
            available = ", ".join(r.get("release", "?") for r in release_data.get("releases", []))
            console.print(f"[red]Release '{filter_release}' not found.[/red] Available: {available}")
            sys.exit(1)
    elif latest:
        from datetime import date
        today = date.today().isoformat()
        filled = [r for r in releases
                  if r.get("publication_date") and str(r["publication_date"]) <= today
                  and r.get("schema_version")]
        releases = filled[:1]

    if not no_summary:
        print_release_summary(releases)

    tmpl = resolve_tmpl_dir(tmpl_dir) / "data_releases.md.j2"
    content = render(tmpl, releases=releases)
    write_or_print(content, output_path, stdout)


@cli.command()
@shared_options
@click.option("--schema-output", type=click.Path(path_type=Path),
    default="SCHEMA_CHANGES.md", show_default=True)
@click.option("--data-output", type=click.Path(path_type=Path),
    default="DATA_RELEASES.md", show_default=True)
def both(schema_path, release_path, tmpl_dir, latest, stdout,
         validate_only, no_summary, schema_output, data_output):
    """Render both schema changelog and data release log."""

    console.rule("[bold cyan]Schema changes + Data releases[/bold cyan]")
    schema_data  = load_yaml(schema_path)
    release_data = load_yaml(release_path)

    ok = report_validation(validate_schema(schema_data),    "SCHEMA_CHANGES.yaml")
    ok = report_validation(validate_releases(release_data), "DATA_RELEASES.yaml") and ok
    if validate_only:
        sys.exit(0 if ok else 1)
    if not ok and not click.confirm("Continue despite errors?", default=False):
        sys.exit(1)

    schema_versions, releases = cross_reference(schema_data, release_data)

    if latest:
        schema_versions = schema_versions[:1]
        filled = [r for r in releases if r.get("publication_date")]
        releases = filled[:1]

    if not no_summary:
        print_schema_summary(schema_versions)
        print_release_summary(releases)

    td = resolve_tmpl_dir(tmpl_dir)

    schema_content = render(td / "schema_changes.md.j2", schema_versions=schema_versions)
    data_content   = render(td / "data_releases.md.j2",  releases=releases)

    if stdout:
        click.echo(schema_content)
        click.echo("\n---\n")
        click.echo(data_content)
    else:
        schema_output.write_text(schema_content, encoding="utf-8")
        data_output.write_text(data_content,   encoding="utf-8")
        console.print(f"[green]✓[/green] Written [bold]{schema_output}[/bold]")
        console.print(f"[green]✓[/green] Written [bold]{data_output}[/bold]")


if __name__ == "__main__":
    cli()
