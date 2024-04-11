Datenmodell
===========


    python datamodel.py > datamodel.md

    pandoc -s --pdf-engine=xelatex   --variable mainfont="DejaVu Sans" -o datamodel.pdf datamodel.md


Adding PDF metadata and A4 paper

    pandoc -s --pdf-engine=xelatex  -V papersize:a4  --metadata-file=metadata.yaml --variable mainfont="DejaVu Sans" -o datamodel.pdf datamodel.md


Adding chapter numbering

    pandoc -s --pdf-engine=xelatex  -V papersize:a4  --number-sections --shift-heading-level-by=-1  --metadata-file=metadata.yaml --variable mainfont="DejaVu Sans" -o datamodel.pdf datamodel.md


    
    pandoc 2.5
Compiled with pandoc-types 1.17.5.4, texmath 0.11.2.2, skylighting 0.7.7

 pandoc -s --pdf-engine=xelatex  -V linkcolor:teal -V monofont="DejaVu Sans Mono"   -V papersize:a4  --number-sections --base-header-level=1  --metadata-file=metadata.yaml --variable mainfont="DejaVu Sans" -o datamodel.pdf datamodel.md
