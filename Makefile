LANGUAGES = de fr
FORMATS = pdf odt docx html

INPUT_DIR = inputs
OUTPUT_DIR = outputs
LOCALE_DIR = locale

PANDOC=/usr/bin/pandoc
RM=/bin/rm
CP=/usr/bin/cp

CSS = datamodel.css

# Define targets for each language and format
OUTPUTS = $(foreach lang,$(LANGUAGES),$(foreach fmt,$(FORMATS),$(OUTPUT_DIR)/$(lang)/datamodel.$(fmt)))
# Define the list of required .mo files for each language
MO_FILES = $(foreach lang,$(LANGUAGES),$(LOCALE_DIR)/$(lang)/LC_MESSAGES/datamodel.mo $(LOCALE_DIR)/$(lang)/LC_MESSAGES/app.mo)
INPUTS = $(foreach lang,$(LANGUAGES),$(foreach fmt,$(FORMATS),$(INPUT_DIR)/$(lang)/datamodel.md))



# Options for all doc format
# Unknown --shift-heading-level-by=-1  \
PANDOC_OPTIONS=--standalone \
         -V papersize:a4   \
         --number-sections \
         --variable mainfont="DejaVu Sans" \
         -V colorlinks=true \
         -V linkcolor=teal \
         -V urlcolor=teal \
         -V toccolor=gray


# Define language-specific options
OPTIONS_de = --metadata lang=de  --metadata-file=$(INPUT_DIR)/de/metadata.yaml -V lang=de
OPTIONS_fr = --metadata lang=fr  --metadata-file=$(INPUT_DIR)/fr/metadata.yaml -V lang=fr

# format specific options
PANDOC_HTML_OPTIONS=--to html5 --toc-depth=2 --shift-heading-level-by=-1  --toc --standalone --include-after-body=assets/sortable.html  --css $(CSS)
PANDOC_PDF_OPTIONS=--pdf-engine=xelatex
PANDOC_DOCX_OPTIONS=
PANDOC_ODT_OPTIONS=

# Help target
help:
	@echo "Usage:"
	@echo "  make all      - Generate all files (PDF, DOCX, HTML and ODT for all languages)"
	@echo "  make pdfs     - Generate only PDF files for all languages"
	@echo "  make docxs    - Generate only DOCX files for all languages"
	@echo "  make odts     - Generate only ODT files for all languages"
	@echo "  make htmls    - Generate only HTML files for all languages"
	@echo "  make mds      - Generate only Markdown files for all languages"
	@echo "  make de       - Generate all files (PDF, DOCX, HTML and ODT) for German"
	@echo "  make fr       - Generate all files (PDF, DOCX, HTML and ODT) for French"
	@echo "  make babel    - Generate .mo translation files"
	@echo "  make markdown - Generate markdown files"
	@echo "  make diagram  - Generate ER diagram"
	@echo "  make validate - Validate the datamodel against the schema"
	@echo "  make clean    - Remove all generated files"
	@echo "  make help     - Display this help message"

.PHONY: assets
assets:
	mkdir -p $(OUTPUT_DIR)/de
	mkdir -p $(OUTPUT_DIR)/fr
	$(CP) assets/$(CSS) $(OUTPUT_DIR)/de
	$(CP) assets/$(CSS) $(OUTPUT_DIR)/fr
	$(CP) assets/geocover.png $(OUTPUT_DIR)/de
	$(CP) assets/geocover.png $(OUTPUT_DIR)/fr
	$(CP) assets/geocover.png .
	$(CP) assets/model.png $(OUTPUT_DIR)/de
	$(CP) assets/model.png $(OUTPUT_DIR)/fr
	$(CP) assets/model.png .

babel: $(MO_FILES)


# Rule to compile .mo files if missing
$(LOCALE_DIR)/%/LC_MESSAGES/datamodel.mo: $(LOCALE_DIR)/%/LC_MESSAGES/datamodel.po
	mkdir -p $(@D)
	pybabel compile --domain=datamodel --directory=locale --use-fuzzy

$(LOCALE_DIR)/%/LC_MESSAGES/app.mo: $(LOCALE_DIR)/%/LC_MESSAGES/app.po
	mkdir -p $(@D)
	pybabel compile --domain=app --directory=locale --use-fuzzy

markdown: $(MO_FILES) $(INPUTS)


diagram: assets
	python create_gv.py
	
$(INPUT_DIR)/datamodel.xlsx:
	datamodel  export datamodel.yaml  -o $@


.PHONY: all
all: $(MO_FILES) $(INPUTS)  $(OUTPUTS) diagram $(INPUT_DIR)/datamodel.xlsx

# Define individual rules for each format and language
define build_rule
$(INPUT_DIR)/$(1)/metadata.yaml: assets $(MO_FILES)
	mkdir -p $$(@D)
	datamodel generate --lang=$(1)  -o $(INPUT_DIR) datamodel.yaml

$(INPUT_DIR)/$(1)/datamodel.md: assets $(MO_FILES)
	mkdir -p $$(@D)
	datamodel generate --lang=$(1) -o $(INPUT_DIR) datamodel.yaml

$(OUTPUT_DIR)/$(1)/datamodel.pdf: $(INPUT_DIR)/$(1)/datamodel.md $(INPUT_DIR)/$(1)/metadata.yaml
	mkdir -p $$(@D)
	$(PANDOC) $(PANDOC_OPTIONS) $(OPTIONS_$1) $(PANDOC_PDF_OPTIONS) -o $$@ $$<

$(OUTPUT_DIR)/$(1)/datamodel.docx: $(INPUT_DIR)/$(1)/datamodel.md $(INPUT_DIR)/$(1)/metadata.yaml
	mkdir -p $$(@D)
	$(PANDOC) $(PANDOC_OPTIONS) $(OPTIONS_$1) $(PANDOC_DOCX_OPTIONS) -o $$@ $$<

$(OUTPUT_DIR)/$(1)/datamodel.odt: $(INPUT_DIR)/$(1)/datamodel.md $(INPUT_DIR)/$(1)/metadata.yaml
	mkdir -p $$(@D)
	$(PANDOC) $(PANDOC_OPTIONS) $(OPTIONS_$1) $(PANDOC_ODT_OPTIONS) -o $$@ $$<

$(OUTPUT_DIR)/$(1)/datamodel.html: $(INPUT_DIR)/$(1)/datamodel.md $(INPUT_DIR)/$(1)/metadata.yaml
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
.PHONY: de fr it
de: $(foreach fmt,$(FORMATS),$(OUTPUT_DIR)/de/datamodel.$(fmt))
fr: $(foreach fmt,$(FORMATS),$(OUTPUT_DIR)/fr/datamodel.$(fmt))

.PHONY: validate
validate:
	 datamodel validate datamodel.yaml

# Clean up
# Clean up all generated files
.PHONY: clean cleanall
cleanall: clean cleaninputs cleanpdf cleanodt cleanhtml cleandocx

clean:
	rm -rf $(OUTPUT_DIR)/*
	find $(LOCALE_DIR) -name "*.mo" -delete

# Clean up only generated PDF files
.PHONY: cleanpdf
cleanpdf:
	find $(OUTPUT_DIR) -name "*.pdf" -delete

# Clean up only generated ODT files
.PHONY: cleanodt
cleanodt:
	find $(OUTPUT_DIR) -name "*.odt" -delete

# Clean up only generated DOCX files
.PHONY: cleandocx
cleandocx:
	find $(OUTPUT_DIR) -name "*.docx" -delete

# Clean up only generated HTML, CSS, and image files
.PHONY: cleanhtml
cleanhtml:
	find $(OUTPUT_DIR) -type f \( -name "*.html" -o -name "*.css" -o -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" \) -delete

.PHONY: cleaninputs
cleaninputs:
	rm -rf $(INPUT_DIR)/de/*
	rm -rf $(INPUT_DIR)/fr/*
