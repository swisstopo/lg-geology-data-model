Datenmodell
===========


    python datamodel.py > datamodel.md

    pandoc -s --pdf-engine=xelatex   --variable mainfont="DejaVu Sans" -o datamodel.pdf datamodel.md


Adding PDF metadata and A4 paper

    pandoc -s --pdf-engine=xelatex  -V papersize:a4  --metadata-file=metadata.yaml --variable mainfont="DejaVu Sans" -o datamodel.pdf datamodel.md


Adding chapter numbering

    pandoc -s --pdf-engine=xelatex  -V papersize:a4  --number-sections --shift-heading-level-by=-1  --metadata-file=metadata.yaml --variable mainfont="DejaVu Sans" -o datamodel.pdf datamodel.md



