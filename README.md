Modèle de données géologiques
=============================

Le but de ces outils est de créer de manière plus au moins automatique le [modèle de données géologiques](https://www.geologieportal.ch/fr/connaissance/consulter/modeles-de-donnees/modele-de-donnees-geologiques.html), en
particulier la liste des valeurs attributaires possibles, et le modèle physique issu de ESRI ArcSDE.

Les fichiers d'intérêts sont dans le répertoire `outputs`:

* Pour l'instante, le modèle est disponible en allemand et en français.
* Plusieurs formats sont disponbiles : `datamodel.pdf`, ainsi que sous forme de fichier `.docx`, `.html` et `.odt`.
* le dump des informations de ESRI ArcSDE 
* Le schéma ER de la base `ER-GCOVER.svg`, généré à partir d'un fichier `PlantUML`.



# Installation

Les scripts ne fonctionnent qu'avec Python3 et sont disponible comme paquet `conda`. Sur BURAUT, il faut cloner l'environnement par defaut
pour pouvoir le modifier. Sous Linux, il est possible de générer les fichiers finaux, mais l'extraction des données à partir de la
base de données ESRI ArcSDE n'est bien entendu pas possible.

## Windows

Open a Python Command Prompt windows and clone the default ESRI ArcGis  `conda` environnement

    (arcgispro-py3) C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3>conda create --clone arcgispro-py3 --prefix C:\LegacySW\envs\arcgispro-py3_clone

Deactivate

    (arcgispro-py3) C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3> deactivate

Activate

    C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3> activate C:\LegacySW\envs\arcgispro-py3_clone


    (arcgispro-py3) C:\LegacySW\envs\arcgispro-py3_clone> conda install swisstopo::geocover

Comme _pandoc.exe_ est un fichier unique, il peut être facilement téléchargé et installé dans _C:\LegacySW_ . Télécharger
la dernière version Windows disponible sur [Pandoc](https://github.com/jgm/pandoc/releases) et dézipper dans _C:>LegacySW_

Pour tester l'installation (le numéro de version peut être différent):

    C:\LegacySW\pandoc-3.1.13\pandoc.exe --version
    
## Linux

    conda install swisstopo::geocover


Les scripts, _coded_domain.py_ et _subtype.py_ doivent être excécuté dans un projet ESRI ArcGis Pro avec une connection
sur la base SDE GCOVER.

Le script `datamodel` qui génère le fichier _MarkDown_ n'a besoin que des libraries de base sus-mentionnées.


# Utilisation

## Extraction des données

1. Creation des fichiers JSON/YAML contenant les _coded domains_ et la liste des _subtypes_ directement depuis
   la base de donnée ArcSDE

Dans un prompt Python, en utilisant l'environnement `conda` par défaut `arcgis-py3` :

    (arcgispro-py3-clone)> cd H:\code\lg-geology-data-model

    (arcgispro-py3-clone)lg-geology-data-model>geocover  export  -w D:\connections\GCOVERP@osa.sde -l DEBUG -o ../exports


2. Export de la structure Oracle : 

Dans ArcGis Pro, charger et exécuter le script : `export_oracle_tables.py`

3. Export des champs obligatoires :

    python export_mandatory.py

## Traductions

1. Extraction des chaînes de caractères  pour traduction :

    pybabel extract -F babel.cfg -o locale/app.pot .

2. Fusion des catalogues (`app` et `datamodel`):

    pybabel update -i locale/app.pot -d locale -D app
    pybabel update -i locale/datamodel.pot -d locale -D datamodel

3. Edition des fichiers .po dans `PoEdit` par exemple
    

4. Compiler les catalogues (`app` et `datamodel`) :
    
    pybabel compile --domain=app --directory=locale --use-fuzzy


## Création du fichier Markdown source

Le script _datamodel.py_ combine les informations de la configuration _datamodel.yaml_  avec _coded_domains.json_ , _subtypes.json_ et le fichier de traduction.
Le résultat est le fichier _Marcdown_ _datamodel_fr.md_ ou _datamodel_de.md_

    datamodel --lang de  datamodel.yaml

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


# Génération du schema ER de la base de donnée SDE

Générer le fichier `PlantUML`  avec :

    python create_gv.py 
    
Convertir en fichier SVG avec p.ex. https://www.planttext.com/

Convertir en image :

    convert  ER-GCOVER.svg ER-GCOVER.png

Convertir en PDF (A3)

    cairosvg  -o ER-GCOVER.pdf    --background '#EEEEFF' --output-width   4191   --output-height 2972 ER-GCOVER.svg

# Autres fonctions

## Extraire les règles des layerfiles

    python geocover.py rules -l INFO

## Compter les features dans un périmètre

With an arbitrary polyon (GeoJSON or ESRI Shapefile)

    python geocover.py filter --geometry san_bernardino.geojson  --gdb-path  I:\backup\GCOVER\daily\20240425_0300_2030-12-31.gdb  -s san_bernardino.json


Or with a bounding box:


    python geocover.py filter --bbox 2760000,1146000,2777500,1158000  --gdb-path  I:\backup\GCOVER\daily\20240425_0300_2030-12-31.gdb  -s san_bernardino.xlsx
