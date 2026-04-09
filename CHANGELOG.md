# Changelog


## [4.3.3] - 2026-04-26
### Added
- Improved `Geology Mapping Tools` (mapping code between input data and this model)
- Improved minor version management on AWS S3
- Added the `HOWTO_REALEASE.md`

## [4.3.2] - 2026-04-04
### Fixed
- Deprecated GitHub Action runners
### Added
- CD Bund header for PDF documents (model, schema diff, release notes)
- Tracking changes in `CHANGELOG.md`, `SCHEMA_VERSION.yaml` and `DATA_RELEASE.yaml`
- Release on merge to `master`
- generate the model schema diff doc and reports (incorporated into artefacts)


## [4.3.1] - 2026-03-25
### Fixed
- Double column rendering in German PDF output (#181)
### Added
- Italian and English translations (attributes and code)

## [4.3.0] - 2026-02-16
### Added
- PDF custom metadata (Model Revision, Git Hash, Language)
- CLI to export all coded domains from SDE JSON
- Creating a new `gcodcs` python module

## [4.2.0] - 2025-11-27
### Added
- Italian and English language scaffolding (draft)
- Replacing `babel` by a simple translation class

## [4.1.0] - 2025-07-30
### Added
- Kartiereinheiten (KE) as domain source for Bedrock
- PDF metadata validation via exiftool

## [4.0.0] - 2024-11-25
### First published automated publish version of de datamodel and model changes from SDE export