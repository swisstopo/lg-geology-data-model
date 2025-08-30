Modèle de données géologiques
=============================

Le but de ces outils est de créer de manière plus au moins automatique le [modèle de données géologiques](https://www.swisstopo.admin.ch/fr/modele-geologique-2d-geocover), en
particulier la liste des valeurs attributaires possibles, et le modèle physique issu de ESRI ArcSDE.

Les exports de la base de données ArcSDE sont dans `exports`, les fichiers intermédiaires nécessaires pour la génération
des documents finaux, comme `markdown` dans `inputs` et les différents formats du modèle final dans `outputs`.

* Pour l'instant, le modèle est disponible en allemand et en français.
* Plusieurs formats sont disponbiles : `datamodel.pdf`, ainsi que sous forme de fichier `.docx`, `.html` et `.odt`.
* Le dump des informations de ESRI ArcSDE dans `exports`
* Le schéma ER de la base `ER-GCOVER.svg`, généré à partir d'un fichier `PlantUML`.



# Installation

Les outils `gcdocs` (génération de la documentation) et `gcover` (exports à partir de ESRI ArcSDE, mais pas que) sont
disponbiles comme paquets sur `anaconda.org` et `pypi.org`. La génération des fichiers finaux à partir des `exports`
est possible dans n'importe quel environnement, mais l'export des données à partir de l'ESRI Enterprise Database (SDE)
nécessite `arcpy` et un accès à cette même base (donc exclusivement Windows. Il est toutefois possible de générer cet
export à partir d'une FileGDB (backup).


## Windows

Créez un nouvel environnement `conda` en clonant `arcgispro-py3` si vous devez exporter des données depuis ArcSDE (évident).  
Pour générer les modèles, vous n'avez pas besoin de `arcpy`.

Installez le paquet :

    (arcgispro-py3) D:\conda\envs\arcgispro-py3_clone> conda install -c swisstopo gcover gcdocs

Pour générer les documents finaux à partir des sources `markdown`, vous avez besoin de `pandoc`.  
Comme _pandoc.exe_ est un binaire autonome sous Windows, téléchargez-le simplement et décompressez-le dans _C:\LegacySW_  
(voir la dernière version disponible sur [Pandoc](https://github.com/jgm/pandoc/releases)).

Pour tester l'installation (le numéro de version peut varier) :

    C:\LegacySW\pandoc-3.1.13\pandoc.exe --version

## Linux

Vous avez besoin de `pandoc` et d'une installation complète de `XeLaTeX`.  
Installez-la avec `apt-get`, `yum`, etc.

Créez un environnement `conda` comme d'habitude et installez le paquet :

    conda install -c gcover gcdocs

Les sous-commandes de `gcover` nécessitant `arcpy` ne sont évidemment pas disponibles sous Linux.


# Utilisation

Ce guide décrit les étapes nécessaires pour générer une nouvelle version du modèle de données géologiques en utilisant
les outils `gcover` et `geocover`

## Préparation

### 1. Création du répertoire de données

Créez un nouveau répertoire pour stocker les exports de la version :

```bash
mkdir -p exports/<RELEASE-DIR>
```

**Exemple :** `mkdir -p exports/2025-08-26`

### 2. Configuration du modèle

Modifiez le fichier `datamodel.yaml` pour spécifier la nouvelle version et le répertoire source :

```yaml
# Le numéro de révision du modèle doit être modifié lorsque des attributs sont ajoutés, supprimés ou modifiés
model:
  revision: '4.1.1'
  revision_date: "2025-08-26"
  sources_dir: "exports/2025-08-26"
```

### 3. Installation de l'outil

Si ce n'est pas déjà fait, installez des outils `gcdocs` et `gcover` :

**Avec conda (recommandé) :**
```bash
conda install -c swisstopo gcdocs  gcover
```

**Avec pip :**
```bash
pip install gcdocs gcover
```

## Export des données

### 1. Export du schéma de données

Exportez le schéma complet depuis la base de données ArcSDE :

```bash
gcover schema extract \
  --filter-prefix "GC_" \
  --output exports/<RELEASE-DIR>/GCOVERP.json \
  "D:\connections\GCOVERP@osa.sde"
```

### 2. Transformation en version simplifiée

Convertissez le schéma complet ESRI en version simplifiée :

```bash
gcover schema transform-simple \
  exports/<RELEASE-DIR>/GCOVERP.json \
  -o exports/<RELEASE-DIR>/gcoverp_export_simple.json
```

### 3. Export des tables annexes

Exportez toutes les tables de référence nécessaires :

```bash
gcover schema export-tables \
  -w "H:/connections/GCOVERP@osa.sde" \
  -o exports/<RELEASE-DIR> \
  --all-tables
```

**Cette commande génère les fichiers suivants :**
- `Geol_Mapping_Unit_Att.json`
- `Geol_Mapping_Unit.json` 
- `Correlation.json`
- `Admixture.json`
- `Composit.json`
- `Charcat.json`
- `System.json`

### 4. Ajout des fichiers statiques

Copiez manuellement les fichiers statiques suivants dans le répertoire `exports/<RELEASE-DIR>/` :

> **Note :** Ces fichiers seront bientôt intégrés automatiquement dans le processus

- `geolcode_chrono.csv`
- `GeolCodeText_Trad_2025.xlsx`
- `SCHEMA_CHANGES_4.0-4.1.json`

## Génération des documents

### Génération du fichier Markdown

```commandline
 gcdocs generate -i exports/2025-08-26/  -o inputs --lang fr,de  datamodel.yaml
```

### Génération des PDF

Une fois tous les exports terminés, générez les documents finaux :

```bash
make pdfs
```
or
```commandline
gcdocs build --lang de --format pdf --input-dir inputs
```

Cette commande produit les fichiers PDF dans les langues configurées (français, allemand).

## Vérification de la qualité

### Validation des métadonnées PDF

Vérifiez que les métadonnées du PDF généré sont correctes :

```bash
exiftool outputs/fr/datamodel.pdf
```

**Sortie attendue :**
```
ExifTool Version Number         : 12.40
File Name                       : datamodel.pdf
Language                        : fr
Page Count                      : 425
Title                           : Modèle de donnée géologique 2D (GeoCover), Révision 4.1
Subject                         : Levé géologique de la Suisse
Author                          : Service géologique national — Office fédéral de topographie swisstopo
Keywords                        : GeoCover, Metadata, Model, GIS, Vector data, Geology, Switzerland, development
Model Revision                  : 4.1.1
Model Short Revision            : 4.1
Git Hash                        : a858a3b
Create Date                     : 2025:08:27 21:41:58+03:00
```

## Notes importantes

- **Pré-requis :** L'export des données nécessite un accès à la base de données ArcSDE et l'environnement ArcGIS Pro avec `arcpy`
- **Durée :** Le processus complet peut prendre plusieurs minutes selon la taille de la base de données
- **Sauvegarde :** Il est recommandé de sauvegarder les exports précédents avant de générer une nouvelle version
- **Validation :** Vérifiez toujours les fichiers générés avant de les publier

## Résolution de problèmes

### Erreurs communes

1. **Connexion à la base de données impossible :**
   - Vérifiez la chaîne de connexion ArcSDE
   - Assurez-vous que l'environnement ArcGIS Pro est actif

2. **Fichiers manquants :**
   - Vérifiez que tous les fichiers statiques ont été copiés
   - Contrôlez les permissions sur le répertoire de sortie

3. **Erreur lors de la génération PDF :**
   - Vérifiez que `pandoc` et XeLaTeX sont installés
   - Contrôlez la syntaxe du fichier `datamodel.yaml`

### Contact

En cas de problème, consultez la documentation technique ou contactez l'équipe de développement (geocover@swisstopo.ch).



