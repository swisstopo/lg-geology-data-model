#!/usr/bin/env python3
"""
Script to generate an HTML index page for available datamodel versions in S3 bucket.

Versioning convention:
  x.y   = schema version  (what users and geologists care about)
  x.y.z = tooling/patch version  (what gets physically stored in S3)

The index groups all x.y.z patches under their x.y parent and displays
files from the latest patch — similar to a symlink from x.y → x.y.z.
"""

import boto3
import sys
import json
import os
import click
from collections import defaultdict, OrderedDict
from datetime import datetime
from typing import List, Dict, Any, Tuple


def get_s3_client(profile_name: str = None):
    """Create S3 client with optional profile"""
    session = (
        boto3.Session(profile_name=profile_name) if profile_name else boto3.Session()
    )
    return session.client("s3")


def parse_version(version_str: str) -> tuple:
    """Parse version string into comparable tuple for sorting"""
    import re

    parts = re.findall(r"\d+|\D+", version_str)
    result = []
    for part in parts:
        if part.isdigit():
            result.append((0, int(part)))
        else:
            result.append((1, part))
    return tuple(result)


def list_versions(s3_client, bucket_name: str, prefix: str = "datamodel/") -> List[str]:
    """List all version directories in the S3 bucket (returns full x.y.z versions)"""
    versions = []

    try:
        paginator = s3_client.get_paginator("list_objects_v2")
        page_iterator = paginator.paginate(
            Bucket=bucket_name, Prefix=prefix, Delimiter="/"
        )

        for page in page_iterator:
            if "CommonPrefixes" in page:
                for prefix_info in page["CommonPrefixes"]:
                    version = prefix_info["Prefix"].replace(prefix, "").rstrip("/")
                    if version:
                        versions.append(version)

        # Sort newest first
        versions.sort(key=parse_version, reverse=True)

    except Exception as e:
        print(f"Error listing versions: {e}")
        sys.exit(1)

    return versions


def group_versions_by_minor(versions: List[str]) -> "OrderedDict[str, List[str]]":
    """
    Group x.y.z patch versions under their x.y schema version key.

    Input  (already sorted newest-first): ["1.3.1", "1.3.0", "1.2.4", "1.2.3"]
    Output (OrderedDict, insertion order = newest schema first):
        {
            "1.3": ["1.3.1", "1.3.0"],
            "1.2": ["1.2.4", "1.2.3"],
        }

    Versions that don't follow x.y.z (e.g. legacy "x.y" keys still in S3)
    are kept as-is under their own key so nothing is silently dropped.
    """
    groups: OrderedDict = OrderedDict()
    for v in versions:
        parts = v.split(".")
        minor_key = ".".join(parts[:2]) if len(parts) >= 3 else v
        groups.setdefault(minor_key, []).append(v)
    return groups


def get_files_for_version(
    s3_client, bucket_name: str, version: str, prefix: str = "datamodel/"
) -> Dict[str, List[Dict[str, Any]]]:
    """Get list of files for a specific version, organised by language"""
    version_prefix = f"{prefix}{version}/"
    files_by_lang = {"root": [], "de": [], "fr": [], "it": [], "en": []}

    excluded_extensions = {".css", ".map"}

    try:
        paginator = s3_client.get_paginator("list_objects_v2")
        page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=version_prefix)

        for page in page_iterator:
            if "Contents" in page:
                for obj in page["Contents"]:
                    key = obj["Key"]
                    filename = key.split("/")[-1]

                    if (
                        key.endswith("/")
                        or filename.startswith(".")
                        or any(filename.lower().endswith(ext) for ext in excluded_extensions)
                    ):
                        continue

                    path_parts = key.replace(version_prefix, "").split("/")
                    lang = "root"
                    if len(path_parts) > 1 and path_parts[0] in ("de", "fr", "it", "en"):
                        lang = path_parts[0]

                    files_by_lang[lang].append({
                        "name": filename,
                        "key": key,
                        "size": obj["Size"],
                        "last_modified": obj["LastModified"],
                        "lang": lang,
                        "path": "/".join(path_parts),
                    })

        for lang in files_by_lang:
            files_by_lang[lang].sort(key=lambda x: x["name"])

    except Exception as e:
        print(f"Error listing files for version {version}: {e}")

    return files_by_lang


def format_file_size(size_bytes: int) -> str:
    """Format file size in human-readable form"""
    if size_bytes == 0:
        return "0 B"
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    return f"{size_bytes:.1f} {size_names[i]}"


def get_file_type_icon(filename: str) -> str:
    """Return an emoji icon for the file type"""
    ext = filename.lower().split(".")[-1] if "." in filename else ""
    icons = {
        "pdf": "📄",
        "docx": "📝",
        "html": "🌐",
        "odt": "📄",
        "md": "📋",
        "json": "🔧",
        "yaml": "⚙️",
        "yml": "⚙️",
    }
    return icons.get(ext, "📎")


def generate_html(
    versions: List[str],
    version_files: Dict[str, Dict[str, List[Dict]]],
    bucket_name: str,
    cloudfront_domain: str = "dubious.cloud",
) -> str:
    """
    Generate the HTML index page.

    `versions` is the flat sorted list of x.y.z strings.
    `version_files` is keyed by x.y.z (full patch version).

    Versions are displayed grouped by x.y schema version; files are served
    from the latest x.y.z patch in each group.
    """
    base_url = (
        f"https://{cloudfront_domain}"
        if cloudfront_domain
        else f"https://{bucket_name}.s3.amazonaws.com"
    )

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modèle de données géologiques - Versions disponibles</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
        }}

        .header {{
            background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
            color: white;
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            text-align: center;
        }}

        .header h1 {{
            margin: 0 0 0.5rem 0;
            font-size: 2.5rem;
        }}

        .header p {{
            margin: 0;
            opacity: 0.9;
            font-size: 1.1rem;
        }}

        .version-card {{
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
            overflow: hidden;
        }}

        .version-header {{
            background: #34495e;
            color: white;
            padding: 1rem 1.5rem;
            font-size: 1.3rem;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            flex-wrap: wrap;
        }}

        .latest-badge {{
            background: #e74c3c;
            color: white;
            padding: 0.2rem 0.6rem;
            border-radius: 12px;
            font-size: 0.8rem;
        }}

        .draft-badge {{
            background: #ff9900;
            color: white;
            padding: 0.2rem 0.6rem;
            border-radius: 12px;
            font-size: 0.8rem;
            margin-left: 1rem;
        }}

        /* Patch pill — pushed to the right */
        .patch-info {{
            margin-left: auto;
            font-size: 0.75rem;
            font-weight: normal;
            font-family: monospace;
            opacity: 0.80;
            white-space: nowrap;
        }}

        .patch-info summary {{
            cursor: pointer;
            list-style: none;
            padding: 0.15rem 0.5rem;
            border: 1px solid rgba(255,255,255,0.35);
            border-radius: 10px;
            user-select: none;
        }}

        .patch-info summary::-webkit-details-marker {{ display: none; }}

        .patch-info[open] summary {{
            border-bottom-left-radius: 0;
            border-bottom-right-radius: 0;
        }}

        .patch-list {{
            position: absolute;
            right: 1.5rem;
            background: #2c3e50;
            border: 1px solid rgba(255,255,255,0.35);
            border-top: none;
            border-radius: 0 0 8px 8px;
            padding: 0.4rem 0.6rem;
            z-index: 10;
        }}

        .patch-list li {{
            list-style: none;
            padding: 0.1rem 0;
        }}

        .patch-wrapper {{
            position: relative;
        }}

        .language-section {{
            padding: 1rem 1.5rem;
            border-bottom: 1px solid #eee;
        }}

        .language-section:last-child {{
            border-bottom: none;
        }}

        .language-header {{
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 1rem;
            color: #2c3e50;
            display: flex;
            align-items: center;
        }}

        .language-code {{
            background: #3498db;
            color: white;
            padding: 0.3rem 0.6rem;
            border-radius: 4px;
            font-size: 0.9rem;
            font-weight: bold;
            margin-right: 0.8rem;
            min-width: 2rem;
            text-align: center;
        }}

        .files-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1rem;
        }}

        .file-item {{
            display: flex;
            align-items: center;
            padding: 0.8rem;
            background: #f8f9fa;
            border-radius: 6px;
            text-decoration: none;
            color: #333;
            transition: all 0.3s ease;
        }}

        .file-item:hover {{
            background: #e9ecef;
            transform: translateY(-2px);
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        }}

        .file-icon {{
            font-size: 1.5rem;
            margin-right: 0.8rem;
        }}

        .file-info {{
            flex: 1;
        }}

        .file-name {{
            font-weight: 500;
            margin-bottom: 0.2rem;
        }}

        .file-details {{
            font-size: 0.85rem;
            color: #666;
        }}

        .no-files {{
            text-align: center;
            padding: 2rem;
            color: #666;
            font-style: italic;
        }}

        .footer {{
            text-align: center;
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid #ddd;
            color: #666;
        }}

        .github-link {{
            display: inline-block;
            margin-top: 1rem;
            padding: 0.5rem 1rem;
            background: #333;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: background 0.3s ease;
        }}

        .github-link:hover {{
            background: #555;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🗺️ Modèle de données géologiques</h1>
        <p>Versions disponibles du modèle de données géologiques suisse</p>
    </div>

    <main>
"""

    lang_config = {
        "de":   {"name": "Deutsch",         "code": "DE"},
        "fr":   {"name": "Français",         "code": "FR"},
        "it":   {"name": "Italiano",         "code": "IT", "status": "draft"},
        "en":   {"name": "English",          "code": "EN", "status": "draft"},
        "root": {"name": "Fichiers communs", "code": "📄"},
    }

    if not versions:
        html += """
        <div class="version-card">
            <div class="no-files">Aucune version disponible pour le moment.</div>
        </div>
        """
    else:
        groups = group_versions_by_minor(versions)

        for i, (minor_version, patches) in enumerate(groups.items()):
            # Files always come from the latest patch in this schema group
            latest_patch = patches[0]
            files_by_lang = version_files.get(latest_patch, {})

            latest_badge = '<span class="latest-badge">DERNIÈRE</span>' if i == 0 else ""

            # Build the patch pill (collapsible <details> when multiple patches exist)
            if len(patches) == 1:
                patch_html = (
                    f'<span class="patch-info" title="Version de déploiement">🔧 {patches[0]}</span>'
                )
            else:
                items = "".join(f"<li>{p}</li>" for p in patches)
                patch_html = f"""
                    <div class="patch-wrapper">
                        <details class="patch-info">
                            <summary>🔧 {patches[0]} (+{len(patches) - 1})</summary>
                            <ul class="patch-list">{items}</ul>
                        </details>
                    </div>"""

            html += f"""
        <div class="version-card">
            <div class="version-header">
                Version {minor_version}
                {latest_badge}
                {patch_html}
            </div>
            """

            total_files = sum(len(f) for f in files_by_lang.values())

            if total_files == 0:
                html += '<div class="no-files">Aucun fichier disponible pour cette version.</div>'
            else:
                for lang, files in files_by_lang.items():
                    if not files:
                        continue

                    lang_info = lang_config.get(lang, {"name": lang.title(), "code": lang.upper()})
                    draft_badge = (
                        '<span class="draft-badge">DRAFT</span>'
                        if lang_info.get("status") == "draft"
                        else ""
                    )

                    html += f"""
            <div class="language-section">
                <div class="language-header">
                    <span class="language-code">{lang_info["code"]}</span>
                    {lang_info["name"]} {draft_badge}
                </div>
                <div class="files-grid">
                    """

                    for file_info in files:
                        icon = get_file_type_icon(file_info["name"])
                        size = format_file_size(file_info["size"])
                        file_url = f"{base_url}/{file_info['key']}"
                        html += f"""
                    <a href="{file_url}" class="file-item" target="_blank">
                        <div class="file-icon">{icon}</div>
                        <div class="file-info">
                            <div class="file-name">{file_info["name"]}</div>
                            <div class="file-details">{size}</div>
                        </div>
                    </a>
                        """

                    html += """
                </div>
            </div>
                    """

            html += "</div>"  # end version-card

    html += f"""
    </main>

    <footer class="footer">
        <p>Généré automatiquement le {datetime.now().strftime("%d/%m/%Y à %H:%M")} UTC</p>
        <a href="https://github.com/swisstopo/lg-geology-data-model" class="github-link">
            📂 Voir le code source sur GitHub
        </a>
    </footer>
</body>
</html>"""

    return html


def upload_to_s3(
    s3_client, bucket_name: str, html_content: str, key: str = "datamodel/index.html"
):
    """Upload HTML content to S3"""
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=key,
            Body=html_content.encode("utf-8"),
            ContentType="text/html",
            CacheControl="max-age=300",  # 5 minutes
        )
        print(f"✅ Successfully uploaded {key} to s3://{bucket_name}/{key}")
    except Exception as e:
        print(f"❌ Error uploading to S3: {e}")
        sys.exit(1)


@click.command("process")
@click.option("--no-upload", is_flag=True, help="Write index.html locally instead of uploading")
def main(no_upload):
    """Generate and upload the version index page."""

    bucket_name = os.getenv("S3_BUCKET")
    if not bucket_name:
        print("No bucket found. Set variable `S3_BUCKET`. Exiting.")
        sys.exit(2)

    profile_name = os.getenv("AWS_PROFILE")
    cloudfront_domain = os.getenv("CLOUDFRONT_DOMAIN", "dubious.cloud")
    prefix = os.getenv("S3_PREFIX", "datamodel/")

    if cloudfront_domain in ("", "none", "None"):
        cloudfront_domain = None

    if os.getenv("CI"):
        profile_name = None

    print(f"🔍 Scanning bucket: {bucket_name}")
    print(f"📁 Prefix: {prefix}")

    s3_client = get_s3_client(profile_name)

    # --- list all x.y.z directories ---
    print("📋 Listing versions...")
    versions = list_versions(s3_client, bucket_name, prefix)
    print(f"✅ Found {len(versions)} patch version(s): {', '.join(versions)}")

    groups = group_versions_by_minor(versions)
    print(f"📐 Schema versions (x.y): {', '.join(groups.keys())}")

    # --- fetch file listings for every x.y.z (needed for the latest-patch display) ---
    print("📂 Scanning files for each patch version...")
    version_files: Dict[str, Dict] = {}
    for version in versions:
        files_by_lang = get_files_for_version(s3_client, bucket_name, version, prefix)
        version_files[version] = files_by_lang

        total = sum(len(f) for f in files_by_lang.values())
        lang_summary = [f"{l}: {len(f)}" for l, f in files_by_lang.items() if f]
        print(f"  📋 {version}: {total} files ({', '.join(lang_summary)})")

    # --- generate ---
    print("🎨 Generating HTML...")
    html_content = generate_html(versions, version_files, bucket_name, cloudfront_domain)

    # --- upload or write locally ---
    if not no_upload:
        index_key = f"{prefix}index.html"
        print("⬆️  Uploading index page...")
        upload_to_s3(s3_client, bucket_name, html_content, index_key)
        print("🎉 Done!")
        target = (
            f"https://{cloudfront_domain}/{index_key}"
            if cloudfront_domain
            else f"https://{bucket_name}.s3.amazonaws.com/{index_key}"
        )
        print(f"🌐 {target}")
    else:
        out = "index.html"
        with open(out, "w") as f:
            f.write(html_content)
        print(f"💾 Written locally to {out}")


if __name__ == "__main__":
    main()
