Modèle de données géologiques
=============================

Le but de ces outils est de créer de manière plus au moins automatique le [modèle de données géologiques](https://www.geologieportal.ch/fr/connaissance/consulter/modeles-de-donnees/modele-de-donnees-geologiques.html), en
particulier la liste des valeurs attributaires possibles, et le modèle physique issu de ESRI ArcSDE.

Les exports de la base de données ArcSDE sont dans `exports`, les fichiers intermédiaires `markdown` dans `inputs`
et les différents formats du modèle final dans `outputs`.

* Pour l'instant, le modèle est disponible en allemand et en français.
* Plusieurs formats sont disponbiles : `datamodel.pdf`, ainsi que sous forme de fichier `.docx`, `.html` et `.odt`.
* Le dump des informations de ESRI ArcSDE dans `exports`
* Le schéma ER de la base `ER-GCOVER.svg`, généré à partir d'un fichier `PlantUML`.



# Installation

L'outil est disponbile comme paquets sur `anaconda.org` et `pypi.org`. La génération des fichiers finaux à partir des `exports`
est possible dans n'importe quel environnement, mais l'export des données nécessite `arcpy`et un accès à la base ESRI ArcSDE.
base de données ESRI ArcSDE n'est bien entendu pas possible.

## Windows

Open a Python Command Prompt windows and clone the default ESRI ArcGis `conda` environnement

    (arcgispro-py3) C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3>conda create --clone arcgispro-py3 --prefix C:\LegacySW\envs\arcgispro-py3_clone

Deactivate the default environment

    (arcgispro-py3) C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3> deactivate

Activate the newly created cloned environment

    C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3> activate C:\LegacySW\envs\arcgispro-py3_clone

Install the package

    (arcgispro-py3) C:\LegacySW\envs\arcgispro-py3_clone> conda install swisstopo::geocover

To generate de final documents from the `markdown` sources, you need `pandoc`. As _pandoc.exe_ is a standalone binary on
Windows, simply download it and unzip it into _C:\LegacySW_ (see the latest available version on  [Pandoc](https://github.com/jgm/pandoc/releases) ).

Pour tester l'installation (le numéro de version peut être différent):

    C:\LegacySW\pandoc-3.1.13\pandoc.exe --version
    
## Linux

You need `pandoc` and a fully-fledge `XeLaTeX` installation. Install it with `apt-get`, `yum`, etc.

Create a `conda` environement as normal and install the package:

    conda install swisstopo::geocover

The subcommand of `geocover` requiring `arcpy` are not available on Linux. The 
Le script `datamodel` qui génère le fichier _markdown_ n'a besoin que des libraries de base sus-mentionnées.


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

Le script _datamodel_ combine les informations de la configuration _datamodel.yaml_  avec _coded_domains.json_ , _subtypes.json_ et le fichier de traduction.
Le résultat est le fichier _Marcdown_ _fr/datamodel.md_ ou _de/datamodel.md_

    datamodel --lang de  datamodel.yaml

## Génération des différents formats

simply use the latest https://github.com/swisstopo/lg-geology-data-model/releases

### Linux

Use `make`

    make pdfs # or all

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
         -o de/datamodel.pdf de/datamodel.md

Idem, mais pour un fichier Microsoft Word (.docx)

     C:\LegacySW\pandoc-3.1.13\pandoc.exe -s -V papersize:a4 --number-sections --shift-heading-level-by=-1
     --metadata-file=metadata.yaml  --variable mainfont="DejaVu Sans"  -o datamodel.docx datamodel.md

For HTML

Sur Linux...

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

    geocover rules -l INFO

## Compter les features dans un périmètre donné

With an arbitrary polyon (GeoJSON or ESRI Shapefile)

    geocover filter --geometry san_bernardino.geojson  --gdb-path  I:\backup\GCOVER\daily\20240425_0300_2030-12-31.gdb  -s san_bernardino.json


Or with a bounding box:


    geocover filter --bbox 2760000,1146000,2777500,1158000  --gdb-path  I:\backup\GCOVER\daily\20240425_0300_2030-12-31.gdb  -s san_bernardino.xlsx
