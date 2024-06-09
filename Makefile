# Makefile
# 
# Help target
help:
	@echo "Usage:"
	@echo "  make docs     - Generate all files (PDF, DOCX, HTML and ODT for all languages)"
	@echo "  make pdf      - Generate only PDF files for all languages"
	@echo "  make docx     - Generate only PDF files for all languages"
	@echo "  make de       - Generate all files (PDF, DOCX, HTML and ODT) for German"
	@echo "  make fr       - Generate all files (PDF, DOCX, HTML and ODT) for French"
	@echo "  make babel    - Generate .mo translation files"
	@echo "  make markdown - Generate markdown files"
	@echo "  make diagram  - Generate ER diagram"
	@echo "  make clean    - Remove all generated files"
	@echo "  make help     - Display this help message"
	
	
INPUT_DIR = input
OUTPUT_DIR = output
SOURCES = $(wildcard $(INPUT_DIR)/datamodel_*.md)
FORMATS = pdf docx odt html
CSS = datamodel.css

# Extract base names and languages from sources
BASENAMES = $(basename $(notdir $(SOURCES)))
LANGUAGES = $(patsubst datamodel_%, %, $(BASENAMES))

PANDOC=/usr/bin/pandoc
RM=/bin/rm
CP=/usr/bin/cp

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
OPTIONS_de = --metadata lang=de  --metadata-file=$(INPUT_DIR)/metadata_de.yaml -V lang=de
OPTIONS_fr = --metadata lang=fr  --metadata-file=$(INPUT_DIR)/metadata_fr.yaml -V lang=fr

# format specific options
PANDOC_HTML_OPTIONS=--to html5 --toc  --css $(CSS)
PANDOC_PDF_OPTIONS=--pdf-engine=xelatex 
PANDOC_DOCX_OPTIONS=
PANDOC_ODT_OPTIONS=

# Define target files
TARGETS = $(foreach lang, $(LANGUAGES), \
            $(foreach format, $(FORMATS), \
              $(OUTPUT_DIR)/datamodel_$(lang).$(format)))
              
# Define PDF target files
PDF_TARGETS = $(foreach lang, $(LANGUAGES), \
                $(OUTPUT_DIR)/datamodel_$(lang).pdf)
                
# Define Microsoft .docx target files
DOCX_TARGETS = $(foreach lang, $(LANGUAGES), \
                $(OUTPUT_DIR)/datamodel_$(lang).docx)
                
# Define LibreOffice .odt target files
ODT_TARGETS = $(foreach lang, $(LANGUAGES), \
                $(OUTPUT_DIR)/datamodel_$(lang).odt)
                
# Define HTML target files
HTML_TARGETS = $(foreach lang, $(LANGUAGES), \
                $(OUTPUT_DIR)/datamodel_$(lang).html)
                
# Define language-specific target files
DE_TARGETS = $(foreach format, $(FORMATS), $(OUTPUT_DIR)/datamodel_de.$(format))
FR_TARGETS = $(foreach format, $(FORMATS), $(OUTPUT_DIR)/datamodel_fr.$(format))

              


# $(info $$TARGETS  is [${TARGETS}])



# Default target
docs: babel assets $(TARGETS)

# Target to generate only PDF files
pdf: assets $(PDF_TARGETS)

# Target to generate only docx files
docx: assets $(DOCX_TARGETS)

# Target to generate only docx files
odt: assets $(ODT_TARGETS)

# Target to generate only html files
html: assets $(HTML_TARGETS)

assets:
	$(CP) assets/$(CSS) $(OUTPUT_DIR)
	$(CP) assets/geocover.png $(OUTPUT_DIR)
	$(CP) assets/geocover.png .

de: assets $(DE_TARGETS)
fr: assets $(FR_TARGETS)

all: markdown diagram docs

# Phony targets
.PHONY: all clean de fr help assets

babel:
	pybabel compile --domain=app --directory=locale --use-fuzzy
	pybabel compile --domain=datamodel --directory=locale --use-fuzzy

markdown: babel
	python datamodel.py --lang=de
	python datamodel.py --lang=fr

diagram:
	python create_gv.py

# Pattern rule for conversion
$(OUTPUT_DIR)/datamodel_%.pdf: $(INPUT_DIR)/datamodel_%.md
	$(PANDOC) $(PANDOC_OPTIONS)  $(OPTIONS_$*) $(PANDOC_PDF_OPTIONS) -o $@ $<
	

$(OUTPUT_DIR)/datamodel_%.docx: $(INPUT_DIR)/datamodel_%.md
	$(PANDOC) $(PANDOC_OPTIONS)  $(OPTIONS_$*) $(PANDOC_DOCX_OPTIONS) -o $@ $<
	
$(OUTPUT_DIR)/datamodel_%.html: $(INPUT_DIR)/datamodel_%.md
	$(PANDOC) $(PANDOC_OPTIONS)  $(OPTIONS_$*) $(PANDOC_HTML_OPTIONS) -o $@ $<
	
$(OUTPUT_DIR)/datamodel_%.odt: $(INPUT_DIR)/datamodel_%.md
	$(PANDOC) $(PANDOC_OPTIONS) $(OPTIONS_$*) $(PANDOC_ODT_OPTIONS) -o $@ $<

# Clean generated files
clean:
	rm -f $(TARGETS)
	
cleanall: clean
	find . -name '*.mo' -exec rm -f {} \;
	rm -f $(OUTPUT_DIR)/*.css

# Ensure the output directory exists
$(OUTPUT_DIR):
	mkdir -p $(OUTPUT_DIR)

# Phony targets
.PHONY: all clean babel

# Ensure the output directory is created before generating files
$(TARGETS): | $(OUTPUT_DIR)
$(PDF_TARGETS): | $(OUTPUT_DIR)
$(DE_TARGETS): | $(OUTPUT_DIR)
$(FR_TARGETS): | $(OUTPUT_DIR)





