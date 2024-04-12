Modèle de donnée géologie
=========================

Le but de ces outils est de créer de manière plus au moins automatique le _modèle de donnée géologie_ GeoCover, en
particulier la liste des valeurs attributaires possibles.


# Installation

Les scripts ne fonctionnent qu'avec Python3 (on est en 2024). Sur BURAUT, on peut utiliser l'installation _conda_ par 
defaut de _ESRI ArcGis Pro_ (_argispro-py3_). Sur Linux, il faut au moins :

    conda install jinja2 pyyaml pandas

Les scripts, _coded_domain.py_ et _subtype.py_ doivent être excécuté dans un projet ESRI ArcGis Pro avec une connection
sur la base SDE GCOVER.

Le script _datamodel.py_  qui génère le fichier _MarkDown_ n'a besoin que des libraries de base sus-mentionnées.

    python3 datamodel.py


## Windows

Comme _pandoc_ est un fichier unique, il peut être facilement téléchargé et installé dans _C:\LegacySW_ . Téléecahrger
la dernière version Windows disponible sur [Pandoc](https://github.com/jgm/pandoc/releases) et dézipper dans _C:>LegacySW_

Pour tester l'installation (le numéro de version peut être différent):

    C:\LegacySW\pandoc-3.1.13\pandoc.exe --version


# Utilisation

Creation des fichiers JSON contenant les _coded domains_ et la liste des _subtypes_

Dans ue fenêtre Python ou un notebook _Jupyter_ exécuter les deux scripts _coded_domains.py_ et
_subtypes.py_ . Le résultat sont deux fichiers JSON _coded_domains.json_ et _subtypes.json_

Creation des fichiers _markdown_ et _JSON_

    python datamodel.py


Creation d'un fichier PDF (possible uniquement avec une installation complète de _LaTeX_)

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

Sur Linux...

    pandoc -s   -V papersize:a4  \
                  --number-sections   \
                  --shift-heading-level-by=-1 \
                  --metadata-file=metadata.yaml  \
                  --variable mainfont="DejaVu Sans" \
                  -o datamodel.docx datamodel.md

..ou sur Windows:

    C:\LegacySW\pandoc-3.1.13\pandoc.exe -s -V papersize:a4 --number-sections --shift-heading-level-by=-1
     --metadata-file=metadata.yaml  --variable mainfont="DejaVu Sans"  -o datamodel.docx datamodel.md
