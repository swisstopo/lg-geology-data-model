# Makefile
# 
# Converts Markdown to other formats (HTML, PDF, DOCX, RTF, ODT, EPUB) using Pandoc
# <http://johnmacfarlane.net/pandoc/>
#
# Run "make" (or "make all") to convert to all other formats
#
# Run "make clean" to delete converted files

# Convert all files in this directory that have a .md suffix
SOURCE_DOCS := $(wildcard *.md)

EXPORTED_DOCS=\
 $(SOURCE_DOCS:.md=.html) \
 $(SOURCE_DOCS:.md=.pdf) \
 $(SOURCE_DOCS:.md=.docx) \
 $(SOURCE_DOCS:.md=.odt) 


RM=/bin/rm

$(info $$LANG  is [${LANG}])

PANDOC=/usr/bin/pandoc

PANDOC_OPTIONS=--standalone -V papersize:a4   --number-sections \
         --shift-heading-level-by=-1  \
         --metadata-file=metadata_${LANG}.yaml \
         --variable mainfont="DejaVu Sans" \
         -V colorlinks=true \
         -V linkcolor=teal \
         -V urlcolor=teal \
         -V toccolor=gray \
         -V lang=${LANG}

PANDOC_HTML_OPTIONS=--to html5
PANDOC_PDF_OPTIONS=--pdf-engine=xelatex 
PANDOC_DOCX_OPTIONS=
PANDOC_ODT_OPTIONS=


$(info $$PANDOC_OPTIONS  is [${PANDOC_OPTIONS}])

# Pattern-matching Rules

outdir/%_${LANG}.html : %_${LANG}.md
	$(PANDOC) $(PANDOC_OPTIONS) $(PANDOC_HTML_OPTIONS) -o $@ $<

outdir/%_${LANG}.pdf : %_${LANG}.md
	$(PANDOC) $(PANDOC_OPTIONS) $(PANDOC_PDF_OPTIONS) -o $@ $<
	
outdir/%_${LANG}.docx : %_${LANG}.md
	$(PANDOC) $(PANDOC_OPTIONS) $(PANDOC_DOCX_OPTIONS) -o $@ $<

outdir/%_${LANG}.odt : %_${LANG}.md
	$(PANDOC) $(PANDOC_OPTIONS) $(PANDOC_ODT_OPTIONS) -o $@ $<



# Targets and dependencies

.PHONY: all clean

all : $(EXPORTED_DOCS)

clean:
	- $(RM) $(EXPORTED_DOCS)
