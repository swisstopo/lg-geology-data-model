LANGUAGES = de fr it en
FORMATS = pdf odt docx html

# Define the directories
EXPORT_DIR ?= sources
INPUT_DIR ?= inputs
OUTPUT_DIR ?= outputs


PANDOC := $(shell which pandoc)
GCDOCS=gcdocs
GCOVER=gcover
RM=/bin/rm
CP=/usr/bin/cp

CSS = datamodel.css

# Define targets for each language and format
OUTPUTS = $(foreach lang,$(LANGUAGES),$(foreach fmt,$(FORMATS),$(OUTPUT_DIR)/$(lang)/datamodel.$(fmt)))
INPUTS = $(foreach lang,$(LANGUAGES),$(foreach fmt,$(FORMATS),$(INPUT_DIR)/$(lang)/datamodel.md))
CLEAN_PDFS = $(shell find outputs -name "*.pdf" -not -name "ER-GCOVER.pdf")
LOGO := Logo_RGB_farbig_positiv.png


# regex: 4 digits, dash, 2 digits, dash, 2 digits
DATE_PATTERN := ^[0-9]{4}-[0-9]{2}-[0-9]{2}$$

# 1. ls -1: List files
# 2. grep -E: Filter only those matching the date pattern
# 3. sort: Put them in chronological order
# 4. tail -n 2: Get the last two
LAST_TWO := $(shell ls -1 $(EXPORT_DIR) | grep -E '$(DATE_PATTERN)' | sort | tail -n 2)

V1 ?= $(word 1, $(LAST_TWO))
V2 ?= $(word 2, $(LAST_TWO))


# $(info clean pdfs = $(CLEAN_PDFS))

# Options for all doc format
# Unknown --shift-heading-level-by=-1  \

PANDOC_OPTIONS := --standalone \
                 --resource-path=.:assets


# Define language-specific options
OPTIONS_de = --metadata lang=de  --metadata-file=$(INPUT_DIR)/de/metadata.yaml -V lang=de --number-sections
OPTIONS_fr = --metadata lang=fr  --metadata-file=$(INPUT_DIR)/fr/metadata.yaml -V lang=fr --number-sections
OPTIONS_it = --metadata lang=it  --metadata-file=$(INPUT_DIR)/it/metadata.yaml -V lang=it --number-sections
OPTIONS_en = --metadata lang=en  --metadata-file=$(INPUT_DIR)/en/metadata.yaml -V lang=en --number-sections

# format specific options
PANDOC_HTML_OPTIONS=  --to html5 --toc  --toc-depth=3  --include-in-header=$(INPUT_DIR)/de/headers.html  --include-after-body=assets/sortable.html  --css $(CSS)
PANDOC_PDF_OPTIONS=--pdf-engine=xelatex  --pdf-engine-opt=--halt-on-error
PANDOC_DOCX_OPTIONS=
PANDOC_ODT_OPTIONS=

# Help target
help:
	@echo "Usage:"
	@echo "  make all                - Generate all files (PDF, DOCX, HTML and ODT for all languages)"
	@echo "  make pdfs               - Generate only PDF files for all languages"
	@echo "  make docxs              - Generate only DOCX files for all languages"
	@echo "  make odts               - Generate only ODT files for all languages"
	@echo "  make htmls              - Generate only HTML files for all languages"
	@echo "  make mds                - Generate only Markdown files for all languages"
	@echo "  make de                 - Generate all files (PDF, DOCX, HTML and ODT) for German"
	@echo "  make fr                 - Generate all files (PDF, DOCX, HTML and ODT) for French"
	@echo "  make it                 - Generate all files (PDF, DOCX, HTML and ODT) for Italian"
	@echo "  make en                 - Generate all files (PDF, DOCX, HTML and ODT) for English"
	@echo "  make markdown           - Generate markdown files"
	@echo "  make release-notes      - Gemerate release notes"
	@echo "  make diagram            - Generate ER diagram"
	@echo "  make validate           - Validate the datamodel against the schema"
	@echo "  make check-metadata     - Check the model metadata"
	@echo "  make validate-metadata  - Validate the datamodel metadata"
	@echo "  make cleanall           - Remove all generated files"
	@echo "  make help               - Display this help message"
	@echo ""
	@echo "VARIABLES:"
	@echo "  pandoc=$(PANDOC)"
	@echo "  V1=$(V1)"
	@echo "  V2=$(V2)"

.PHONY: assets
assets:
	@mkdir -p $(OUTPUT_DIR)/de
	@mkdir -p $(OUTPUT_DIR)/fr
	@mkdir -p $(OUTPUT_DIR)/it
	@mkdir -p $(OUTPUT_DIR)/en
	@mkdir -p $(INPUT_DIR)/de
	@mkdir -p $(INPUT_DIR)/fr
	@mkdir -p $(INPUT_DIR)/it
	@mkdir -p $(INPUT_DIR)/en
	@$(CP) assets/$(CSS) $(OUTPUT_DIR)/de
	@$(CP) assets/$(CSS) $(OUTPUT_DIR)/fr
	@$(CP) assets/$(CSS) $(OUTPUT_DIR)/it
	@$(CP) assets/$(CSS) $(OUTPUT_DIR)/en
	@$(CP) assets/geocover.png $(OUTPUT_DIR)/de
	@$(CP) assets/geocover.png $(OUTPUT_DIR)/fr
	@$(CP) assets/geocover.png $(OUTPUT_DIR)/it
	@$(CP) assets/geocover.png $(OUTPUT_DIR)/en
	@$(CP) assets/geocover.png .
	@$(CP) assets/model.png $(OUTPUT_DIR)/de
	@$(CP) assets/model.png $(OUTPUT_DIR)/fr
	@$(CP) assets/model.png $(OUTPUT_DIR)/it
	@$(CP) assets/model.png $(OUTPUT_DIR)/en
	@$(CP) assets/model.png .
	@$(CP) -f assets/$(LOGO) $(INPUT_DIR)/en/
	@$(CP) -f assets/$(LOGO)  $(INPUT_DIR)/de/
	@$(CP) -f assets/$(LOGO)  $(INPUT_DIR)/fr/
	@$(CP) -f assets/$(LOGO)  $(INPUT_DIR)/it/

$(OUTPUT_DIR):
	@mkdir -p $(OUTPUT_DIR)

$(OUTPUT_DIR)/%: assets


$(OUTPUT_DIR)/%: assets


markdown: $(MO_FILES) $(INPUTS)


diagram: assets
	rm -rf $(OUTPUT_DIR)/ER-GCOVER.*
	python create_gv.py

$(INPUT_DIR)/datamodel.xlsx:
	$(GCDOCS)  export datamodel.yaml  -o $@


.PHONY: all
all:  $(OUTPUT_DIR) $(INPUTS)  $(OUTPUTS)
# TODO readd  $(INPUT_DIR)/datamodel.xlsx

# Define individual rules for each format and language
define build_rule
$(INPUT_DIR)/$(1)/headers.html: assets
	mkdir -p $$(@D)
	$(GCDOCS)  generate --lang=$(1)  -i $(EXPORT_DIR) -o $(INPUT_DIR) datamodel.yaml

$(INPUT_DIR)/$(1)/metadata.yaml: assets
	mkdir -p $$(@D)
	$(GCDOCS)  generate --lang=$(1)  -i $(EXPORT_DIR) -o $(INPUT_DIR) datamodel.yaml

$(INPUT_DIR)/$(1)/datamodel.md: assets extract-subtypes extract-domains
	mkdir -p $$(@D)
	$(GCDOCS)  generate --lang=$(1) -i $(EXPORT_DIR) -o $(INPUT_DIR) datamodel.yaml

$(OUTPUT_DIR)/$(1)/datamodel.pdf: $(INPUT_DIR)/$(1)/datamodel.md $(INPUT_DIR)/$(1)/metadata.yaml
	mkdir -p $$(@D)
	$(PANDOC) $(PANDOC_OPTIONS) $(OPTIONS_$1) $(PANDOC_PDF_OPTIONS) --include-in-header=$(INPUT_DIR)/$(1)/cd-header.tex --resource-path=.:assets  -o $$@ $$<

$(OUTPUT_DIR)/$(1)/datamodel.docx: $(INPUT_DIR)/$(1)/datamodel.md $(INPUT_DIR)/$(1)/metadata.yaml
	mkdir -p $$(@D)
	$(PANDOC) $(PANDOC_OPTIONS) $(OPTIONS_$1) $(PANDOC_DOCX_OPTIONS) -o $$@ $$<

$(OUTPUT_DIR)/$(1)/datamodel.odt: $(INPUT_DIR)/$(1)/datamodel.md $(INPUT_DIR)/$(1)/metadata.yaml
	mkdir -p $$(@D)
	$(PANDOC) $(PANDOC_OPTIONS) $(OPTIONS_$1) $(PANDOC_ODT_OPTIONS) -o $$@ $$<

$(OUTPUT_DIR)/$(1)/datamodel.html: $(INPUT_DIR)/$(1)/datamodel.md $(INPUT_DIR)/$(1)/metadata.yaml $(INPUT_DIR)/$(1)/headers.html
	mkdir -p $$(@D)
	$(PANDOC) $(PANDOC_OPTIONS) $(OPTIONS_$1) $(PANDOC_HTML_OPTIONS) -o $$@ $$<
endef

# Apply the build_rule for each language
$(foreach lang,$(LANGUAGES),$(eval $(call build_rule,$(lang))))



# Targets for building specific formats
.PHONY: pdfs odts htmls docxs mds
pdfs: $(foreach lang,$(LANGUAGES),$(OUTPUT_DIR)/$(lang)/datamodel.pdf)
odts: $(foreach lang,$(LANGUAGES),$(OUTPUT_DIR)/$(lang)/datamodel.odt)
htmls: $(foreach lang,$(LANGUAGES),$(OUTPUT_DIR)/$(lang)/datamodel.html)
docxs: $(foreach lang,$(LANGUAGES),$(OUTPUT_DIR)/$(lang)/datamodel.docx)
mds: $(foreach lang,$(LANGUAGES),$(INPUT_DIR)/$(lang)/datamodel.md)


# Targets for building specific languages
.PHONY: de fr it en
de: $(foreach fmt,$(FORMATS),$(OUTPUT_DIR)/de/datamodel.$(fmt))
fr: $(foreach fmt,$(FORMATS),$(OUTPUT_DIR)/fr/datamodel.$(fmt))
it: $(foreach fmt,$(FORMATS),$(OUTPUT_DIR)/it/datamodel.$(fmt))
en: $(foreach fmt,$(FORMATS),$(OUTPUT_DIR)/en/datamodel.$(fmt))



#.PHONY: cover-image

cover-image:
	@python ./scripts/generate_cover_image.py

.PHONY: schema-changes-md schema-changes-pdf data-releases-md data-releases-pdf release-notes clean-releases  validate-release-files release-notes

# High-level targets
schema-changes-md: $(OUTPUT_DIR)/SCHEMA_CHANGES.md
schema-changes-pdf: $(OUTPUT_DIR)/SCHEMA_CHANGES.pdf
data-releases-md: $(OUTPUT_DIR)/DATA_RELEASES.md
data-releases-pdf: $(OUTPUT_DIR)/DATA_RELEASES.pdf
release-notes: schema-changes-pdf data-releases-pdf

# Rule for Schema Markdown
$(OUTPUT_DIR)/SCHEMA_CHANGES.md:
	python scripts/geocover_release_notes.py schema \
		--template-dir scripts/templates \
		--output $@ --schema-file SCHEMA_CHANGES.yaml --data-file DATA_RELEASES.yaml

# Rule for Schema PDF
$(OUTPUT_DIR)/SCHEMA_CHANGES.pdf: $(OUTPUT_DIR)/SCHEMA_CHANGES.md $(INPUT_DIR)/en/cd-header.tex
	$(PANDOC) $(PANDOC_OPTIONS) $(PANDOC_PDF_OPTIONS) \
		--include-in-header=$(INPUT_DIR)/en/cd-header.tex -o $@ $<

# Rule for Data Release Markdown
$(OUTPUT_DIR)/DATA_RELEASES.md:
	python scripts/geocover_release_notes.py data \
		--template-dir scripts/templates \
		--output $@

# Rule for Data Release PDF
$(OUTPUT_DIR)/DATA_RELEASES.pdf: $(OUTPUT_DIR)/DATA_RELEASES.md $(INPUT_DIR)/en/cd-header.tex
	$(PANDOC) $(PANDOC_OPTIONS) $(PANDOC_PDF_OPTIONS) \
		--include-in-header=$(INPUT_DIR)/en/cd-header.tex -o $@ $<

release-notes: schema-changes-pdf data-releases-pdf

excel-mapping: $(OUTPUT_DIR)/geology_mapping_tool.xlsx

$(OUTPUT_DIR)/geology_mapping_tool.xlsx:
	python ./scripts/geology_mapping_tool.py

validate-release-files:
	python scripts/geocover_release_notes.py both --validate

clean-releases:
	rm -f $(OUTPUT_DIR)/DATA_RELEASES.pdf
	rm -f $(OUTPUT_DIR)/DATA_RELEASES.md
	rm -f $(OUTPUT_DIR)/SCHEMA_CHANGES.pdf
	rm -f $(OUTPUT_DIR)/SCHEMA_CHANGES.md


.PHONY: diff diff-pdf diff-docx diff-reports

diff: $(OUTPUT_DIR) $(OUTPUT_DIR)/$(V1)_$(V2).md $(OUTPUT_DIR)/$(V1)_$(V2).html

diff-reports: $(OUTPUT_DIR)   $(OUTPUT_DIR)/$(V1)_$(V2).pdf $(OUTPUT_DIR)/$(V1)_$(V2).docx $(OUTPUT_DIR)/$(V1)_$(V2).html

$(INPUT_DIR)/en/cd-header.tex:


.PHONE: schema-simple extract-subtypes extract-domains

schema-simple: $(EXPORT_DIR)/$(V2)/gcover-schema-simple.json

extract-subtypes: $(EXPORT_DIR)/$(V2)/subtypes_dict.json

extract-domains: $(EXPORT_DIR)/$(V2)/coded_domains.json


$(EXPORT_DIR)/$(V2)/gcover-schema-simple.json:
	$(GCOVER) schema transform --pretty --show-summary --output $@  sources/$(V2)/geocover-schema-sde.json

$(EXPORT_DIR)/$(V2)/subtypes_dict.json:
	$(GCDOCS) extract --mode subtypes -f json -o $@  sources/$(V2)/geocover-schema-sde.json

$(EXPORT_DIR)/$(V2)/coded_domains.json:
	$(GCDOCS) extract --mode domains -f json -o $@  sources/$(V2)/geocover-schema-sde.json



$(OUTPUT_DIR)/$(V1)_$(V2).html:
	@echo "Comparing $(V1) against $(V2)..."
	gcover  schema diff \
		-o $(OUTPUT_DIR)/$(V1)_$(V2).html \
		--format html \
		--old-schema-version $(V1) \
		--new-schema-version $(V2) \
		$(EXPORT_DIR)/$(V1)/geocover-schema-sde.json \
		$(EXPORT_DIR)/$(V2)/geocover-schema-sde.json

$(OUTPUT_DIR)/$(V1)_$(V2).md:
	@echo "Comparing $(V1) against $(V2)..."
	gcover  schema diff \
		-o $(OUTPUT_DIR)/$(V1)_$(V2).md \
		--format markdown \
		--old-schema-version $(V1) \
		--new-schema-version $(V2) \
		$(EXPORT_DIR)/$(V1)/geocover-schema-sde.json \
		$(EXPORT_DIR)/$(V2)/geocover-schema-sde.json

$(OUTPUT_DIR)/$(V1)_$(V2).pdf: $(OUTPUT_DIR)/$(V1)_$(V2).md
	$(PANDOC) $(PANDOC_OPTIONS)  $(PANDOC_PDF_OPTIONS)  -V documentclass=extarticle -V fontsize=8pt \
  --metadata-file=assets/diff_metadata.yaml  --include-in-header=$(INPUT_DIR)/en/cd-header.tex  -o $(OUTPUT_DIR)/$(V1)_$(V2).pdf $(OUTPUT_DIR)/$(V1)_$(V2).md

$(OUTPUT_DIR)/$(V1)_$(V2).docx: $(OUTPUT_DIR)/$(V1)_$(V2).md
	$(PANDOC) $(PANDOC_OPTIONS)  $(PANDOC_DOCX_OPTIONS)  -o $(OUTPUT_DIR)/$(V1)_$(V2).docx $(OUTPUT_DIR)/$(V1)_$(V2).md




.PHONY: validate test
validate:
	 $(GCDOCS)  validate datamodel.yaml

test:
	python -m pytest tests/test_gcdocs_smoke.py -v --no-cov 2>&1

# Check metadata in all generated PDFs
.PHONY: check-metadata
check-metadata:
	@echo "=== PDF Metadata Check ==="
	@for pdf in $(CLEAN_PDFS); do \
		if [ -f "$$pdf" ]; then \
			echo; \
			echo "$$(basename $$pdf)"; \
			pdfinfo -custom "$$pdf" | grep -E "(ModelRevision|GitHash|GitTag|BuildDate|BuildContext):" | sed 's/^/  /' || echo "  No custom metadata found"; \
		fi; \
	done

.PHONY: validate-metadata
validate-metadata:
	@echo "=== Metadata Validation ==="
	@missing=0; \
	for pdf in $(CLEAN_PDFS); do \
		if [ -f "$$pdf" ]; then \
			echo -n "Checking $$(basename $$pdf)... "; \
			if pdfinfo -custom "$$pdf" | grep -q "ModelRevision:"; then \
				echo "✓"; \
			else \
				echo "✗ Missing ModelRevision"; \
				missing=$$((missing + 1)); \
			fi; \
		fi; \
	done; \
	if [ $$missing -eq 0 ]; then \
		echo "All PDFs have required metadata ✓"; \
	else \
		echo "$$missing PDFs missing metadata ✗"; \
		exit 1; \
	fi

# Clean up
# Clean up all generated files
.PHONY:  cleanall
cleanall: cleaninputs cleanpdf cleanodt cleanhtml cleandocx


# Clean up only generated PDF files
.PHONY: cleanpdf
cleanpdf:
	@echo "Deleting all PDFs except ER-GCOVER.pdf..."
	@if [ -n "$(CLEAN_PDFS)" ]; then \
		rm $(CLEAN_PDFS); \
	else \
		echo "No other PDFs to delete."; \
	fi



# Clean up only generated ODT files
.PHONY: cleanodt
cleanodt: $(OUTPUT_DIR)
	find $(OUTPUT_DIR) -name "*.odt" -delete

# Clean up only generated DOCX files
.PHONY: cleandocx
cleandocx: $(OUTPUT_DIR)
	find $(OUTPUT_DIR) -name "*.docx" -delete

# Clean up only generated HTML, CSS, and image files
.PHONY: cleanhtml
cleanhtml: $(OUTPUT_DIR)
	find $(OUTPUT_DIR) -type f \( -name "*.html" -o -name "*.css" -o -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" \) -delete

.PHONY: cleaninputs
cleaninputs:
	rm -rf $(INPUT_DIR)/de/*
	rm -rf $(INPUT_DIR)/fr/*
	rm -rf $(INPUT_DIR)/it/*
	rm -rf $(INPUT_DIR)/en/*
