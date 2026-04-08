# HOWTO — GeoCover Datamodel Release

This document describes the full procedure for publishing a new GeoCover 2D datamodel release.
It covers both a **schema release** (model version bump, e.g. `4.1 → 4.2`) and a **data-only release**
(new map sheets, same schema, e.g. `R14 → R15`).

> **Versioning rule:**
> - `x.y.0` — schema changed → entry required in `SCHEMA_CHANGES.yaml`
> - `x.y.z` — code/tooling fixes only → entry in `CHANGELOG.md` only, no schema entry

---

## Overview

```
Step 1  Create exports directory and extract data from SDE    (Windows / ArcGIS Pro)
Step 2  Update release metadata files                          (any machine)
Step 3  Edit documentation files                               (any machine)
Step 4  Generate PDFs, diff reports, release notes             (Linux / CI)
Step 5  Validate output                                        (any machine)
Step 6  Open PR → merge to master → GitHub Actions publishes   (GitHub)
```

---

## Step 1 — Export data from SDE (Windows, requires `arcpy`)

All export commands run on Windows with ArcGIS Pro. The target directory uses the SDE export date,
not the publication date.

### 1.1 Create the export directory

```bash
mkdir -p exports/<RELEASE-DIR>
# Example:
mkdir -p exports/2026-02-16
```

### 1.2 Install `gcover` (if not already installed)

```bash
# In the ArcGIS Pro conda environment:
conda install swisstopo::gcover

# Or with pip (non-arcpy environment):
pip install gcover
```

### 1.3 Extract the full SDE schema

```bash
gcover schema extract \
  --filter-prefix "GC_" \
  --output exports/<RELEASE-DIR>/geocover-schema-sde.json \
  "D:\connections\GCOVERP@osa.sde"
```

### 1.4 Transform to simplified schema

```bash
gcover schema transform-simple \
  exports/<RELEASE-DIR>/geocover-schema-sde.json \
  -o exports/<RELEASE-DIR>/gcoverp_export_simple.json
```

> **Note:** Check whether `gcoverp_export_simple.json` is still required by the current pipeline
> or superseded by the coded domains extraction below.

### 1.5 Export annex tables

```bash
gcover schema export-tables \
  -w "H:/connections/GCOVERP@osa.sde" \
  -o exports/<RELEASE-DIR> \
  --all-tables
```

Generates:

```
exports/<RELEASE-DIR>/
  Geol_Mapping_Unit_Att.json
  Geol_Mapping_Unit.json
  Correlation.json
  Admixture.json
  Composit.json
  Charcat.json
  System.json
```

### 1.6 Extract coded domains and subtypes

```bash
# Combined coded domains (replaces all_codes_dict.json)
gcdocs extract \
  --mode combined \
  -f json \
  -o exports/<RELEASE-DIR>/coded_domains.json \
  exports/<RELEASE-DIR>/geocover-schema-sde.json

# Subtypes
gcdocs extract \
  --mode subtypes \
  -f json \
  -o exports/<RELEASE-DIR>/subtypes_dict.json \
  exports/<RELEASE-DIR>/geocover-schema-sde.json
```

### 1.7 Add static supporting files

Copy the following files into `exports/<RELEASE-DIR>/` (these will be automated in a future release):

```
geolcode_chrono.csv
GeolCodeText_Trad_230317.csv
```

> `all_codes_dict.json` — generate with `gcdocs extract --mode combined` (see 1.6 above).

### 1.8 Generate cover images

Change the PDF cover image with every big release (easier to identify each release)

```bash
python scripts/generate_cover_image.py
```

---

## Step 2 — Update release metadata files

These files are the source of truth for the release. Edit them in order.

### 2.1 `release.yaml` — current build config

Update the three fields that change with every release:

```yaml
model:
  revision: '4.3.1'            # ← bump according to versioning rule above
  revision_date: "2026-02-16"  # ← SDE export date (= exports/<RELEASE-DIR>)
  sources_dir: "exports/2026-02-16"

geodata:
  release: "R16"               # ← geodata release identifier
  publication_date: "2026-03-30"
```

### 2.2 `DATA_RELEASES.yaml` — append a new entry at the top

```yaml
releases:
  - release: "R16"
    publication_date: "2026-03-30"
    schema_version: "4.3.1"          # must match revision in release.yaml
    schema_export_date: "2026-02-16"
    new_data:
      - { name: "Winterthur", sheet: 140 }
      - { name: "Nesslau",    sheet: 141 }
      # ... all updated map sheets
    release_notes: ~                  # or a short note if relevant
```

### 2.3 `SCHEMA_CHANGES.yaml` — append only if model version is `x.y.0`

If this is a patch release (`x.y.z`), skip this file entirely.

If schema changed, prepend a new entry:

```yaml
schema_versions:
  - version: "4.3.0"          # must match revision in release.yaml
    git_tag: "v4.3.0"
    date: "2026-02-16"
    model_transition: "4.2 -> 4.3"   # only if major/minor bump
    changes:
      - class: "GC_LINEAR_OBJECTS"
        attribute: "KIND"
        type: "value_added"
        values:
          - { de: "...", fr: "..." }
        motivation: >
          Why this change was made.
```

See the change type reference at the bottom of `SCHEMA_CHANGES.md` for valid `type` values.

---

## Step 3 — Edit documentation files

| File | When to edit |
|------|-------------|
| `CHANGELOG.md` | Every release — add entry under new version heading |
| `SCHEMA_CHANGES.yaml` | Schema releases only (`x.y.0`) |
| `DATA_RELEASES.yaml` | Every release |
| `release.yaml` | Every release |
| `datamodel.yaml` | Only if model structure code changes |

`CHANGELOG.md` entry format:

```markdown
## [4.3.1] - 2026-03-25
### Fixed
- Double column rendering in German PDF output (#181)
### Added
- Italian and English draft translations
```

---

## Step 4 — Generate output files

Run all generation steps on Linux (or let CI handle them after merge).

```bash
# Generate PDFs (all languages)
make pdfs

# Generate schema diff reports (PDF + DOCX)
make diff-reports

# Generate SCHEMA_CHANGES.md and DATA_RELEASES.md from YAML sources
make release-notes
```

Individual targets if needed:

```bash
# Schema changelog only
python scripts/geocover_release_notes.py schema

# Data release log only
python scripts/geocover_release_notes.py data

# Latest release only (for announcements)
python scripts/geocover_release_notes.py data --latest --stdout
python scripts/geocover_release_notes.py schema --latest --stdout
```

---

## Step 5 — Validate output

### 5.1 Validate YAML files

```bash
python scripts/geocover_release_notes.py both --validate
```

### 5.2 Check PDF metadata

```bash
exiftool outputs/fr/datamodel.pdf
```

Expected fields:

```
Language                : fr
Title                   : Modèle de donnée géologique 2D (GeoCover), Révision 4.3
Author                  : Service géologique national — Office fédéral de topographie swisstopo
Model Revision          : 4.3.1
Model Short Revision    : 4.3
Git Hash                : <short hash>
Create Date             : 2026:03:25 ...
```

### 5.3 Check generated Markdown

```bash
# Quick visual check of the latest release block
python scripts/geocover_release_notes.py data --latest --stdout --no-summary
```

---

## Step 6 — Open PR and publish

```bash
# Stage everything
git add exports/<RELEASE-DIR>/
git add release.yaml DATA_RELEASES.yaml SCHEMA_CHANGES.yaml CHANGELOG.md
git add SCHEMA_CHANGES.md DATA_RELEASES.md   # generated files

git commit -m "release: R16 / model v4.3.1"
git push origin release/r16
```

Open a PR against `master`. The GitHub Actions workflow triggers on PR to build and validate.
On merge to `master`, the release workflow:

1. Reads `release.yaml` to get `model.revision`
2. Checks that a Git tag `v<revision>` does not already exist
3. Builds all PDFs and diff reports
4. Creates the GitHub Release with tag `v4.3.1` and attaches all artifacts
5. Updates the package on `anaconda.org` / `pypi.org`

> **RC workflow:** if you need a release candidate before merging, push a tag manually:
> ```bash
> git tag v4.3.1-rc.1 && git push origin v4.3.1-rc.1
> ```
> RC tags trigger a build but do **not** update `DATA_RELEASES.yaml` or `SCHEMA_CHANGES.yaml`
> and are not considered by `--latest`.

---

## Quick checklist

```
[ ] exports/<RELEASE-DIR>/ populated and committed
[ ] release.yaml updated (revision, revision_date, sources_dir, geodata.release)
[ ] DATA_RELEASES.yaml — new entry prepended
[ ] SCHEMA_CHANGES.yaml — new entry prepended (schema releases only)
[ ] CHANGELOG.md — new entry added
[ ] make pdfs         → outputs/*/datamodel.pdf generated
[ ] make diff-reports → outputs/*_*.pdf/.docx generated
[ ] make release-notes → SCHEMA_CHANGES.md / DATA_RELEASES.md regenerated
[ ] exiftool check passes
[ ] python scripts/geocover_release_notes.py both --validate passes
[ ] PR opened, CI green, reviewed
[ ] Merged to master → GitHub Release created automatically
```
