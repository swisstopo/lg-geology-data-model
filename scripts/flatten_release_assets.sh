#!/usr/bin/env bash
# Flattens a `gh run download` artifact tree into a flat directory suitable
# for `gh release create`/`gh release upload` (which don't accept nested paths).
#
# Usage:
#   gh run download <RUN-ID> -D release-assets
#   scripts/flatten_release_assets.sh [release-assets]
#
# The build workflow (.github/workflows/build.yaml) uploads one artifact named
# `geology-data-model-<revision>`; `gh run download` nests it as
# <DEST>/geology-data-model-<revision>/... . This script finds that folder,
# copies the relevant files up to <DEST> (renaming per-language datamodel.pdf/
# .docx to datamodel-<lang>.<ext> so they don't collide), and removes it.
set -euo pipefail

DEST="${1:-release-assets}"

ART_DIR=$(find "$DEST" -mindepth 1 -maxdepth 1 -type d -name 'geology-data-model-*' | head -n1)
if [ -z "$ART_DIR" ]; then
  echo "No geology-data-model-* artifact folder found under $DEST — already flat?" >&2
  exit 1
fi

for f in "$ART_DIR"/outputs/*/datamodel.pdf "$ART_DIR"/outputs/*/datamodel.docx; do
  [ -f "$f" ] || continue
  lang=$(basename "$(dirname "$f")")
  cp "$f" "$DEST/datamodel-${lang}.${f##*.}"
done

cp "$ART_DIR"/outputs/DATA_RELEASES.pdf \
   "$ART_DIR"/outputs/SCHEMA_CHANGES.pdf \
   "$ART_DIR"/outputs/diagram.pdf \
   "$ART_DIR"/outputs/geology_mapping_tool.xlsx \
   "$ART_DIR"/outputs/all_geolcode.xlsx \
   "$DEST"/

# Schema diff report: outputs/<V1>_<V2>.pdf — name varies per release.
for f in "$ART_DIR"/outputs/*_*.pdf; do
  case "$(basename "$f")" in
    DATA_RELEASES.pdf|SCHEMA_CHANGES.pdf) continue ;;
  esac
  cp "$f" "$DEST"/
done

cp "$ART_DIR"/sources/*/gcover-schema-simple.json "$DEST"/

rm -rf "$ART_DIR"

echo "Flattened into $DEST:"
ls -la "$DEST"
