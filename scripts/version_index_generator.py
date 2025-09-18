#!/usr/bin/env python3
"""
Script to generate an HTML index page for available datamodel versions in S3 bucket
"""

import boto3
import json
import os
import sys
from datetime import datetime
from collections import defaultdict
from typing import List, Dict, Any


def get_s3_client(profile_name: str = None):
    """Create S3 client with optional profile"""
    session = (
        boto3.Session(profile_name=profile_name) if profile_name else boto3.Session()
    )
    return session.client("s3")


def parse_version(version_str: str) -> tuple:
    """Parse version string into comparable tuple"""
    import re

    # Split version into parts (numbers and non-numbers)
    parts = re.findall(r"\d+|\D+", version_str)
    result = []

    for part in parts:
        if part.isdigit():
            result.append((0, int(part)))  # (type, value) - 0 for numbers
        else:
            result.append((1, part))  # (type, value) - 1 for strings

    return tuple(result)


def list_versions(s3_client, bucket_name: str, prefix: str = "datamodel/") -> List[str]:
    """List all version directories in the S3 bucket"""
    versions = []

    try:
        paginator = s3_client.get_paginator("list_objects_v2")
        page_iterator = paginator.paginate(
            Bucket=bucket_name, Prefix=prefix, Delimiter="/"
        )

        for page in page_iterator:
            if "CommonPrefixes" in page:
                for prefix_info in page["CommonPrefixes"]:
                    # Extract version from prefix (remove datamodel/ and trailing /)
                    version = prefix_info["Prefix"].replace(prefix, "").rstrip("/")
                    if version:  # Skip empty strings
                        versions.append(version)

        # Sort versions using semantic versioning (newest first)
        versions.sort(key=parse_version, reverse=True)

    except Exception as e:
        print(f"Error listing versions: {e}")
        sys.exit(1)

    return versions


def get_files_for_version(
    s3_client, bucket_name: str, version: str, prefix: str = "datamodel/"
) -> Dict[str, List[Dict[str, Any]]]:
    """Get list of files for a specific version, organized by language"""
    version_prefix = f"{prefix}{version}/"
    files_by_lang = {"root": [], "de": [], "fr": [], "it": [], "en": []}

    # File extensions to exclude
    excluded_extensions = {".css", ".map"}

    try:
        paginator = s3_client.get_paginator("list_objects_v2")
        page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=version_prefix)

        for page in page_iterator:
            if "Contents" in page:
                for obj in page["Contents"]:
                    key = obj["Key"]
                    filename = key.split("/")[-1]

                    # Skip directory markers, hidden files, and excluded file types
                    if (
                        key.endswith("/")
                        or filename.startswith(".")
                        or any(
                            filename.lower().endswith(ext)
                            for ext in excluded_extensions
                        )
                    ):
                        continue

                    # Determine language from path
                    path_parts = key.replace(version_prefix, "").split("/")
                    lang = "root"  # Default to root

                    if len(path_parts) > 1 and path_parts[0] in [
                        "de",
                        "fr",
                        "it",
                        "en",
                    ]:
                        lang = path_parts[0]

                    file_info = {
                        "name": filename,
                        "key": key,
                        "size": obj["Size"],
                        "last_modified": obj["LastModified"],
                        "lang": lang,
                        "path": "/".join(path_parts),
                    }
                    files_by_lang[lang].append(file_info)

        # Sort files by name for each language
        for lang in files_by_lang:
            files_by_lang[lang].sort(key=lambda x: x["name"])

    except Exception as e:
        print(f"Error listing files for version {version}: {e}")

    return files_by_lang


def format_file_size(size_bytes: int) -> str:
    """Format file size in human readable format"""
    if size_bytes == 0:
        return "0 B"
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    return f"{size_bytes:.1f} {size_names[i]}"


def get_file_type_icon(filename: str) -> str:
    """Get icon/badge for file type"""
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
    """Generate HTML content for the index page"""

    # Use provided domain, default to dubious.cloud, or fallback to S3 if explicitly set to None
    if cloudfront_domain:
        base_url = f"https://{cloudfront_domain}"
    else:
        base_url = f"https://{bucket_name}.s3.amazonaws.com"

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
        }}

        .latest-badge {{
            background: #e74c3c;
            color: white;
            padding: 0.2rem 0.6rem;
            border-radius: 12px;
            font-size: 0.8rem;
            margin-left: 1rem;
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

    # Language configuration
    lang_config = {
        "de": {"name": "Deutsch", "code": "DE"},
        "fr": {"name": "Français", "code": "FR"},
        "it": {"name": "Italiano", "code": "IT"},
        "en": {"name": "English", "code": "EN"},
        "root": {"name": "Fichiers communs", "code": "📄"},
    }

    if not versions:
        html += """
        <div class="version-card">
            <div class="no-files">
                Aucune version disponible pour le moment.
            </div>
        </div>
        """
    else:
        for i, version in enumerate(versions):
            files_by_lang = version_files.get(version, {})
            latest_badge = (
                '<span class="latest-badge">DERNIÈRE</span>' if i == 0 else ""
            )

            html += f"""
        <div class="version-card">
            <div class="version-header">
                Version {version}{latest_badge}
            </div>
            """

            # Check if we have any files
            total_files = sum(len(files) for files in files_by_lang.values())

            if total_files == 0:
                html += '<div class="no-files">Aucun fichier disponible pour cette version.</div>'
            else:
                # Display files by language
                for lang, files in files_by_lang.items():
                    if not files:  # Skip empty language sections
                        continue

                    lang_info = lang_config.get(
                        lang, {"name": lang.title(), "code": lang.upper()}
                    )

                    html += f"""
            <div class="language-section">
                <div class="language-header">
                    <span class="language-code">{lang_info["code"]}</span>
                    {lang_info["name"]}
                </div>
                <div class="files-grid">
                    """

                    for file_info in files:
                        icon = get_file_type_icon(file_info["name"])
                        size = format_file_size(file_info["size"])

                        # Use CloudFront domain if provided
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

            html += "</div>"

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
            CacheControl="max-age=300",  # Cache for 5 minutes
        )
        print(f"✅ Successfully uploaded {key} to s3://{bucket_name}/{key}")
    except Exception as e:
        print(f"❌ Error uploading to S3: {e}")
        sys.exit(1)


def main():
    """Main function"""

    # Configuration - can be overridden by environment variables
    bucket_name = os.getenv("S3_BUCKET")
    profile_name = os.getenv("AWS_PROFILE")  # None for default profile in CI
    cloudfront_domain = os.getenv(
        "CLOUDFRONT_DOMAIN", "dubious.cloud"
    )  # Default to dubious.cloud
    prefix = os.getenv("S3_PREFIX", "datamodel/")

    # Allow disabling CloudFront by setting CLOUDFRONT_DOMAIN to empty string or 'none'
    if cloudfront_domain in ("", "none", "None"):
        cloudfront_domain = None

    # Use profile only if not in CI environment
    if os.getenv("CI"):
        profile_name = None

    print(f"🔍 Scanning bucket: {bucket_name}")
    print(f"📁 Prefix: {prefix}")

    # Initialize S3 client
    s3_client = get_s3_client(profile_name)

    # List all versions
    print("📋 Listing versions...")
    versions = list_versions(s3_client, bucket_name, prefix)
    print(f"✅ Found {len(versions)} versions: {', '.join(versions)}")

    # Get files for each version
    print("📂 Scanning files for each version...")
    version_files = {}
    for version in versions:
        files_by_lang = get_files_for_version(s3_client, bucket_name, version, prefix)
        version_files[version] = files_by_lang

        # Count total files across all languages
        total_files = sum(len(files) for files in files_by_lang.values())
        lang_summary = []
        for lang, files in files_by_lang.items():
            if files:
                lang_summary.append(f"{lang}: {len(files)}")

        print(
            f"  📋 Version {version}: {total_files} files ({', '.join(lang_summary)})"
        )

    # Generate HTML
    print("🎨 Generating HTML...")
    html_content = generate_html(
        versions, version_files, bucket_name, cloudfront_domain
    )

    # Upload to S3
    index_key = f"{prefix}index.html"
    print(f"⬆️  Uploading index page...")
    upload_to_s3(s3_client, bucket_name, html_content, index_key)

    print("🎉 Done!")

    if cloudfront_domain:
        print(
            f"🌐 Index page available at: https://{cloudfront_domain}/{prefix}index.html"
        )
    else:
        print(
            f"🌐 Index page available at: https://{bucket_name}.s3.amazonaws.com/{index_key}"
        )


if __name__ == "__main__":
    main()
