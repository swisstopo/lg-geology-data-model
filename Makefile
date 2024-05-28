# Makefile
# 
# Help target
help:
	@echo "Usage:"
	@echo "  make all    - Generate all files (PDF, DOCX, HTML and ODT for all languages)"
	@echo "  make pdf    - Generate only PDF files for all languages"
	@echo "  make docx    - Generate only PDF files for all languages"
	@echo "  make de     - Generate all files (PDF, DOCX, HTML and ODT) for German"
	@echo "  make fr     - Generate all files (PDF, DOCX, HTML and ODT) for French"
	@echo "  make clean  - Remove all generated files"
	@echo "  make help   - Display this help message"
	
	
INPUT_DIR = input
OUTPUT_DIR = output
SOURCES = $(wildcard $(INPUT_DIR)/datamodel_*.md)
FORMATS = pdf docx odt html

# Extract base names and languages from sources
BASENAMES = $(basename $(notdir $(SOURCES)))
LANGUAGES = $(patsubst datamodel_%, %, $(BASENAMES))

PANDOC=/usr/bin/pandoc

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
OPTIONS_de = --metadata lang=de  --metadata-file=metadata_de.yaml -V lang=de
OPTIONS_fr = --metadata lang=fr  --metadata-file=metadata_fr.yaml -V lang=fr

PANDOC_HTML_OPTIONS=--to html5
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
                
# Define PDF target files
DOCX_TARGETS = $(foreach lang, $(LANGUAGES), \
                $(OUTPUT_DIR)/datamodel_$(lang).docx)
                
# Define language-specific target files
DE_TARGETS = $(foreach format, $(FORMATS), $(OUTPUT_DIR)/datamodel_de.$(format))
FR_TARGETS = $(foreach format, $(FORMATS), $(OUTPUT_DIR)/datamodel_fr.$(format))

              
RM=/bin/rm

# $(info $$TARGETS  is [${TARGETS}])



# Default target
all: babel $(TARGETS)

# Target to generate only PDF files
pdf: $(PDF_TARGETS)

# Target to generate only docx files
docx: $(DOCX_TARGETS)

de: $(DE_TARGETS)
fr: $(FR_TARGETS)



# Phony targets
.PHONY: all pdf clean de fr help

babel:
	pybabel compile --domain=app --directory=locale --use-fuzzy
	pybabel compile --domain=datamodel --directory=locale --use-fuzzy

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
	find . -name '*.mo' -exec rm -i {} \;

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





