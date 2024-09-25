LANGUAGES = de fr
FORMATS = pdf odt docx html

INPUT_DIR = inputs
OUTPUT_DIR = outputs

PANDOC=/usr/bin/pandoc
RM=/bin/rm
CP=/usr/bin/cp

CSS = datamodel.css

# Define targets for each language and format
OUTPUTS = $(foreach lang,$(LANGUAGES),$(foreach fmt,$(FORMATS),$(OUTPUT_DIR)/$(lang)/datamodel.$(fmt)))

# Options for all doc format
PANDOC_OPTIONS=--standalone \
         -V papersize:a4   \
         --number-sections \
         --shift-heading-level-by=-1  \
         --variable mainfont="DejaVu Sans" \
         -V colorlinks=true \
         -V linkcolor=teal \
         -V urlcolor=teal \
         -V toccolor=gray


# Define language-specific options
OPTIONS_de = --metadata lang=de  --metadata-file=$(INPUT_DIR)/de/metadata.yaml -V lang=de
OPTIONS_fr = --metadata lang=fr  --metadata-file=$(INPUT_DIR)/fr/metadata.yaml -V lang=fr

# format specific options
PANDOC_HTML_OPTIONS=--to html5 --toc  --css $(CSS)
PANDOC_PDF_OPTIONS=--pdf-engine=xelatex
PANDOC_DOCX_OPTIONS=
PANDOC_ODT_OPTIONS=

assets:
	mkdir -p $(OUTPUT_DIR)
	$(CP) assets/$(CSS) $(OUTPUT_DIR)
	$(CP) assets/geocover.png $(OUTPUT_DIR)
	$(CP) assets/geocover.png .

babel:
	pybabel compile --domain=app --directory=locale --use-fuzzy
	pybabel compile --domain=datamodel --directory=locale --use-fuzzy

markdown: babel
	python datamodel.py --lang=de
	python datamodel.py --lang=fr

diagram:
	python create_gv.py



OUTPUTS = $(foreach lang,$(LANGUAGES),$(foreach fmt,$(FORMATS),$(OUTPUT_DIR)/$(lang)/datamodel.$(fmt)))

.PHONY: all
all: $(OUTPUTS)

# Define individual rules for each format and language
define build_rule
$(INPUT_DIR)/$(1)/metadata.yaml:
	mkdir -p $$(@D)
	python datamodel.py --lang=$(1)

$(INPUT_DIR)/$(1)/datamodel.md:
	mkdir -p $$(@D)
	python datamodel.py --lang=$(1)

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
.PHONY: pdfs odts htmls
pdfs: $(foreach lang,$(LANGUAGES),$(OUTPUT_DIR)/$(lang)/datamodel.pdf)
odts: $(foreach lang,$(LANGUAGES),$(OUTPUT_DIR)/$(lang)/datamodel.odt)
htmls: $(foreach lang,$(LANGUAGES),$(OUTPUT_DIR)/$(lang)/datamodel.html)


# Targets for building specific languages
.PHONY: de fr it
de: $(foreach fmt,$(FORMATS),$(OUTPUT_DIR)/de/datamodel.$(fmt))
fr: $(foreach fmt,$(FORMATS),$(OUTPUT_DIR)/fr/datamodel.$(fmt))
it: $(foreach fmt,$(FORMATS),$(OUTPUT_DIR)/it/datamodel.$(fmt))

# Clean up
.PHONY: clean
clean:
	rm -rf $(OUTPUT_DIR)/*
