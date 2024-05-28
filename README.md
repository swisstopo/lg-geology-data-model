Modèle de donnée géologie
=========================

Le but de ces outils est de créer de manière plus au moins automatique le _modèle de donnée géologie_ GeoCover, en
particulier la liste des valeurs attributaires possibles.


# Installation

Les scripts ne fonctionnent qu'avec Python3 (on est en 2024). Sur BURAUT, on peut utiliser l'installation _conda_ par 
defaut de _ESRI ArcGis Pro_ (_argispro-py3_) qui contient les modules nécessaires. Sur Linux, il faut au moins :

    conda install jinja2 pyyaml pandas click loguru --yes

Les scripts, _coded_domain.py_ et _subtype.py_ doivent être excécuté dans un projet ESRI ArcGis Pro avec une connection
sur la base SDE GCOVER.

Le script _datamodel.py_  qui génère le fichier _MarkDown_ n'a besoin que des libraries de base sus-mentionnées.
et va combiner



## Windows

Comme _pandoc_ est un fichier unique, il peut être facilement téléchargé et installé dans _C:\LegacySW_ . Téléecahrger
la dernière version Windows disponible sur [Pandoc](https://github.com/jgm/pandoc/releases) et dézipper dans _C:>LegacySW_

Pour tester l'installation (le numéro de version peut être différent):

    C:\LegacySW\pandoc-3.1.13\pandoc.exe --version


# Utilisation

## Extraction des données

1. Creation des fichiers JSON contenant les _coded domains_ et la liste des _subtypes_

Dans une fenêtre Python ou un notebook _Jupyter_ exécuter les deux scripts `export_coded_domains.py` et
`export_subtypes.py` . Le résultat sont deux fichiers JSON _coded_domains.json_ et _subtypes.json_

2. Extraction des tables hiérarchiques : `litho`,  `litstrat`, `chrono` et `tecto`

Dans ArcGis Pro, charger et exécuter le script : `export_tables.py`

3. Export de la structure Oracle : 

Dans ArcGis Pro, charger et exécuter le script : `export_oracle_tables.py`

4. Export des champs obligatoires :


    python export_mandatory.py

## Traductions

Extraction des chaînes de charactères :

    pybabel extract -F babel.cfg -o locale/app.pot .
    
Fusion des catalogues :

    pybabel update -i locale/app.pot   -d app
    
Compiler les catalogues :
    
    pybabel compile --domain=app --directory=locale --use-fuzzy



## Création du fichier Markdown source

Le script _datamodel.py_ combine les informations de la configuration _datamodel.yaml_  avec _coded_domains.json_ , _subtypes.json_ et le fichier de traduction.
Le résultat est le fichier _Marcdown_ _datamodel.md_

    python3 datamodel.py

## Génération des différents formats

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

Idem, mais pour un fichier Microsoft Word (.docx)

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

Pour HTML

Sur Linux...

        pandoc -s  --toc \
                  --number-sections   \
                  --shift-heading-level-by=-1 \
                  --css datamodel.css \
                  --metadata-file=metadata.yaml  \
                  --variable mainfont="Sans" \
                  -o datamodel.html datamodel.md
                  
.. ou Windows

    C:\LegacySW\pandoc-3.1.13\pandoc.exe  --toc --number-sections  --shift-heading-level-by=-1 --css datamodel.css 
                  --metadata-file=metadata.yaml   --variable mainfont="Sans"  -o datamodel.html datamodel.md


# Schema SDE

Générer le fichier `PlantUML  avec :

    python create_gv.py 
    
Convertir en fichier SVG avec p.ex. https://www.planttext.com/

Convertir en image :


    convert  ER-GCOVER.svg ER-GCOVER.png
