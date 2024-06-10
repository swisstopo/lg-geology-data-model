Modèle de donnée géologie
=========================

Le but de ces outils est de créer de manière plus au moins automatique le _modèle de donnée géologie_ GeoCover, en
particulier la liste des valeurs attributaires possibles, et le modèle physique issu de ESRI ArcSDE.

Les fichiers d'intérêts sont dans le répertoire `output`

* Le modèle de donnée géologique : `datamodel_de.pdf` et `datamodel_fr.pdf` (des fichiers `.docx`, `.html` et `.odt` sont
  également disponibles)
* le dump des informations de ESRI ArcSDE 
* Le schéma ER de la base `ER-GCOVER.svg`, généré à partir d'un fichier `PlantUML`.



# Installation

Les scripts ne fonctionnent qu'avec Python3 (on est en 2024). Sur BURAUT, on peut utiliser l'installation _conda_ par 
defaut de _ESRI ArcGis Pro_ (_argispro-py3_) qui contient les modules nécessaires. Sur Linux, il faut au moins :

    conda install jinja2 pyyaml pandas click loguru --yes

ou simplement (l'environement créé est `DATAMODEL`):

    conda env create -f environment.yml

En cas d'ajout de dépendances, recréer la liste des paquets avec :

    conda env export environment.yml

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

1. Creation des fichiers JSON/YAML contenant les _coded domains_ et la liste des _subtypes_ directement depuis
   la base de donnée ArcSDE

Dans un prompt Python, en utilisant l'environnement `conda` par défaut `arcgis-py3` :

     ./geocover.py  export  -w D:\connections\GCOVERP@osa.sde -l DEBUG -o ../exports


2. Export de la structure Oracle : 

Dans ArcGis Pro, charger et exécuter le script : `export_oracle_tables.py`

3. Export des champs obligatoires :


    python export_mandatory.py

## Traductions

1. Extraction des chaînes de caractères  pour traduction :

    pybabel extract -F babel.cfg -o locale/app.pot .

2. Edition des fichiers .po dans `PoEdit` par exemple
    
3. Fusion des catalogues (`app` et `datamodel`):

    pybabel update -i locale/app.pot   -d app
    
4. Compiler les catalogues (`app` et `datamodel`) :
    
    pybabel compile --domain=app --directory=locale --use-fuzzy



## Création du fichier Markdown source

Le script _datamodel.py_ combine les informations de la configuration _datamodel.yaml_  avec _coded_domains.json_ , _subtypes.json_ et le fichier de traduction.
Le résultat est le fichier _Marcdown_ _datamodel_fr.md_ ou _datamodel_de.md_

    python3 datamodel.py --lang de  # ou fr

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
