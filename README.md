Modèle de donnée géologie
=========================

Le but de ces outils est de créer de manière plus au moins automatique le _modèle de donnée géologie_ GeoCover, en
particulier la liste des valeurs attributaires possibles.


# Installation

    conda install jinja2 pyyaml pandas

Uniquement des librairies de base pour _datamodel.py_ . Evidemment, _coded_domain.py_ et _subtype.py_ doivent être 
excécuté dans un projet ESRI ArcGis Pro avec une connection sur la base SDE GCOVER.


# Utilisation

Creation des fichiers JSON contenant les _coded domains_ et la liste des _subtypes_

Dans ue fenêtre Python ou un notebook _Jupyter_ exécuter les deux scripts _coded_domains.py_ et
_subtypes.py_ . Le résultat sont deux fichiers JSON _coded_domains.json_ et _subtypes.json_

Creation des fichiers _markdown_ et JSON

    python datamodel.py


Creation d'un fichier PDF

    pandoc -s --pdf-engine=xelatex  \
         -V papersize:a4  \
         --number-sections \
         --shift-heading-level-by=-1  \
         --metadata-file=metadata.yaml \
         --variable mainfont="DejaVu Sans" \
         -V colorlinks=true \
         -V linkcolor=teal \
         -V urlcolor=teal \
         -V toccolor=gray \
         -o datamodel.pdf datamodel.md

Idem, mais pour un fichier Microsoft Word

    pandoc -s   -V papersize:a4  \
                  --number-sections   \
                  --shift-heading-level-by=-1 \
                  --metadata-file=metadata.yaml  \
                  --variable mainfont="DejaVu Sans" \
                  -o datamodel.docx datamodel.md


Pour HTML

        pandoc -s  --toc \
                  --number-sections   \
                  --shift-heading-level-by=-1 \
                  --css datamodel.css \
                  --metadata-file=metadata.yaml  \
                  --variable mainfont="Sans" \
                  -o datamodel.html datamodel.md
