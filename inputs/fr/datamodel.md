






![Extrait de GeoCover et exemple de représentation](geocover.png "Figure alt text")





\pagebreak





# Thème ROCK_BODIES

## Classe Unconsolidated_Deposits_PT (Runc){#unconsolidated-deposits-pt}
La classe [Unconsolidated_Deposits_PT](#unconsolidated-deposits-pt) comprend les volumes
rocheux individualisés (de taille variable, des galets aux
blocs) qui ont été transportés par des processus
gravitaires, glaciaires ou anthropogéniques jusqu’à leur
position actuelle, ou dégagés sur place par dégradation de
la roche sous-jacente.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**STATUS**                 | [CD](#unconsolidated-deposits-pt-status)  | État du type d&#39;objet | [1]
**ROCK_TYPE**                 | [CD](#unconsolidated-deposits-pt-rock-type)  | Type de roche | [0..1]
**ROCK_SPE**                 | [CD](#unconsolidated-deposits-pt-rock-spe)  | Description de la roche repère | [0..1]
**MAT_TYPE**                 | [ Table ](#gc-litho-unco-cd)  | Description du matériel (unité lithologique) | [0..1]
**ORIG_DESCR**                 | string                  | Description selon la carte géologique originale | [0..1]
**PROTECTED**                 | boolean                  | Objet géologique protégé (oui / non)? | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14401001 | erratischer Block | bloc erratique     |
|14401002 | Schwarm erratischer Blöcke | accumulation de blocs erratiques     |
|14401003 | anthropogene Ansammlung von erratischen Blöcken | amas anthropique de blocs erratiques     |
|14401004 | Wanderblock | bloc laboureur     |
|14401005 | Geschiebe | cailloutis glaciaire     |
|14401006 | Sturzblock | bloc éboulé     |
|14401007 | Lesesteinhaufen | dépôt d&#39;épierrage     |
|14401008 | Verwitterungsrückstände (Gerölle und/oder Konkretionen) | éléments résiduels (galets et/ou rognons)     |




#### Attribut  STATUS {#unconsolidated-deposits-pt-status}
_État du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14402001 | versetzt | déplacé artificiellement     |
|14402002 | zerstört | détruit     |
|14402003 | in Situ | in situ     |
|14402004 | umgelagert | déplacé naturellement     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  ROCK_TYPE {#unconsolidated-deposits-pt-rock-type}
_Type de roche_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14403001 | Kristallingestein | roche cristalline     |
|14403002 | Sedimentgestein | roche sédimentaire     |
|14403003 | Basisches / Ultrabasisches Gestein | roche basique / ultrabasique     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  ROCK_SPE {#unconsolidated-deposits-pt-rock-spe}
_Description de la roche repère_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14404001 | Vallorcine-Konglomerat | 14404001     |
|14404002 | Allalin-Gabbro | 14404002     |
|14404003 | Mont-Blanc-Granit | 14404003     |
|14404004 | Serpentinit | 14404004     |
|14404005 | Niesen-Brekzie | 14404005     |
|14404006 | Hohgant-Sandstein | 14404006     |
|14404007 | Grindelwald-Marmor | 14404007     |
|14404008 | Aare-Granit | 14404008     |
|14404009 | Gastern-Granit | 14404009     |
|14404010 | Habkern-Granit | 14404010     |
|14404011 | Windgällen-Porphyr | 14404011     |
|14404012 | Glarner Verrucano | 14404012     |
|14404013 | Kalknagelfluh des Speer- und Stockberggebietes | 14404013     |
|14404014 | Ilanz-Verrucano | 14404014     |
|14404015 | Mels-Sandstein | 14404015     |
|14404016 | Taspinit-Brekzie | 14404016     |
|14404017 | Albula-Granit | 14404017     |
|14404018 | Punteglias-Granit | 14404018     |
|14404019 | Rofna-Porphyr | 14404019     |
|14404020 | Degersheim-Kalknagelfluh | 14404020     |
|14404021 | Taveyannaz-Sandstein | 14404021     |
|14404022 | Muschelsandstein | 14404022     |
|14404023 | Karbon-Brekzie | 14404023     |
|14404024 | Alpines Sedimentgestein | 14404024     |
|14404025 | Molassegestein | 14404025     |
|14404026 | Gruontal-Konglomerat | 14404026     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  MAT_TYPE
_Description du matériel (unité lithologique)_

Voir [GC_LITHO_UNCO_CD](#gc-litho-unco-cd) dans l'annexe





#### Attribut  ORIG_DESCR
_Description selon la carte géologique originale_

_Type de donnée :  string_





#### Attribut  PROTECTED
_Objet géologique protégé (oui / non)?_

_Type de donnée :  boolean_





## Classe Unconsolidated_Deposits_PLG (Runc){#unconsolidated-deposits-plg}
La classe [Unconsolidated_Deposits_PLG](#unconsolidated-deposits-plg) contient toutes les
dépôts de roches meubles.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**LITSTRAT**                 | [ Table ](#gc-litstrat-unco-cd)  | Description lithostratigraphique | [1]
**LITHO**                 | [ Table ](#gc-litho-cd)  | Description lithologique | [1]
**CHRONO_T**                 | [ Table ](#gc-chrono-cd)  | Attribution chronostratigraphique du toit de la formation  (top) | [1]
**CHRONO_B**                 | [ Table ](#gc-chrono-cd)  | Attribution chronostratigraphique de la base de la  formation (basis) | [1]
**MAT_TYPE**                 | [ Table ](#lithostratigraphic-units-litho)  | Description du matériel (unité lithologique) | [0..3]
**BURIED_OUT**                 | boolean                  | Est-ce que la roche consolidée est recouvert (oui / non)? | [1]
**COMPOSIT**                 | table                  | Composition de la roche meuble | [0..3]
**ADMIXTURE**                 | table                  | Incorporation | [0..2]
**STRUCTUR**                 | [CD](#unconsolidated-deposits-plg-structur)  | Struccture de la roche meuble | [0..1]
**CHARACT**                 | table                  | Charactéristique spécifique | [0..3]
**MORPHOLO**                 | [CD](#unconsolidated-deposits-plg-morpholo)  | Morphologie de l’unité de roche meuble | [0..1]
**GLAC_TYPE**                 | [CD](#unconsolidated-deposits-plg-glac-type)  | Type de glacier auquel le type d’objet est associé. Cet  attribut n’est valable que pour des moraines | [0..1]
**REF_YEAR**                 | string                  | Information de temps ou période. Par ex. &#34;1940-1943: année de référence de l’ancienne ligne de rivage&#34; | [0..1]
**THIN_COVER**                 | [CD](#unconsolidated-deposits-plg-thin-cover)  | Type de couverture meuble pelliculaire | [0..1]
**ORIG_DESCR**                 | string                  | Description selon la légende de la carte géologique originale | [1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14517001 | Lockergestein | roche meuble     |




#### Attribut  LITSTRAT
_Description lithostratigraphique_

Voir [GC_LITSTRAT_UNCO_CD](#gc-litstrat-unco-cd) dans l'annexe





#### Attribut  LITHO
_Description lithologique_

Voir [GC_LITHO_CD](#gc-litho-cd) dans l'annexe





#### Attribut  CHRONO_T
_Attribution chronostratigraphique du toit de la formation  (top)_

Voir [GC_CHRONO_CD](#gc-chrono-cd) dans l'annexe





#### Attribut  CHRONO_B
_Attribution chronostratigraphique de la base de la  formation (basis)_

Voir [GC_CHRONO_CD](#gc-chrono-cd) dans l'annexe





#### Attribut  MAT_TYPE
_Description du matériel (unité lithologique)_

Voir [Lithostratigraphic_Units_Litho](#lithostratigraphic-units-litho) dans l'annexe





#### Attribut  BURIED_OUT
_Est-ce que la roche consolidée est recouvert (oui / non)?_

_Type de donnée :  boolean_





#### Attribut  COMPOSIT
_Composition de la roche meuble_

_Type de donnée :  table_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14508004 | sandig | sableux     |
|14508002 | lehmig | limoneux     |
|14508001 | tonig | argileux     |
|14508006 | geröllreich | riche en galets     |
|14508007 | torfig | tourbeux     |
|14508003 | siltig | silteux     |
|14508005 | kiesig | graveleux     |




#### Attribut  ADMIXTURE
_Incorporation_

_Type de donnée :  table_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14509008 | mit Hangschutt vermischt | mélangé à des éboulis     |
|14509010 | mit Torf | avec tourbe     |
|14509004 | mit Blöcken | avec blocs     |
|14509013 | mit Schieferkohle | 14509013     |
|14509002 | mit Lösslehm | avec loess argileux     |
|14509011 | mit jurassischen Geröllen | avec galets jurassiens     |
|14509012 | mit Geröllen aus Vogesen / Schwarzwald | avec galets des Vosges / de la Forêt Noire     |
|14509001 | mit Löss | avec loess     |
|14509006 | mit Block- und Geschiebestreu | parsemé de blocs     |
|14509007 | mit Blockschutt vermischt | mélangé à des dépôts d&#39;éboulement     |
|14509003 | mit Seekreide | avec craie lacustre     |
|14509005 | mit alpinen Geröllen | avec galets alpins     |
|14509009 | mit Verwitterungsschutt vermischt | mélangé à des résidus d&#39;altération     |




#### Attribut  STRUCTUR {#unconsolidated-deposits-plg-structur}
_Struccture de la roche meuble_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14510001 | texturlos | sans structure     |
|14510002 | geschichtet | stratifié     |
|14510003 | schräg-/kreuzgeschichtet | stratification oblique/entrecroisée     |
|14510004 | grossmassstäbliche Schrägschichtung (z.B. Deltaschichtung) | stratification oblique à grande échelle (p.ex. stratification deltaïque)     |
|14510005 | glaziale Überprägung (Glazitektonik) | soumis à des déformations glaciotectoniques     |
|14510006 | periglazial gestörte Schichtung (Diapir, Eiskeil, etc.) | affecté par la cryoturbation (diapir, coin de glace, etc.)     |
|14510007 | laminiert | laminé     |
|14510008 | mit Warven | varvé     |
|14510009 | normal gradiert | granoclassement normal     |
|14510010 | invers gradiert | granoclassement inverse     |
|14510011 | bioturbiert | bioturbé     |
|14510012 | pedogen überprägt | pédogénétisé     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  CHARACT
_Charactéristique spécifique_

_Type de donnée :  table_





#### Attribut  MORPHOLO {#unconsolidated-deposits-plg-morpholo}
_Morphologie de l’unité de roche meuble_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14512001 | Kegel / Fächer | cône     |
|14512002 | Schleier | voile     |
|14512003 | Düne | dune     |
|14512004 | Wall | vallum     |
|14512005 | Terrasse | terrasse     |
|14512006 | Sander | sandur     |
|14512007 | Os | esker     |
|14512008 | Bastion | bastion     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  GLAC_TYPE {#unconsolidated-deposits-plg-glac-type}
_Type de glacier auquel le type d’objet est associé. Cet  attribut n’est valable que pour des moraines._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14513001 | Lokalgletscher | glacier local     |
|14513002 | grosse Tal- und Vorlandgletscher | grands glaciers de vallées et de piedmont     |
|14513003 | Bündner Gletscher | glacier des Grisons     |
|14513004 | Bodensee-Rheingletscher | glacier du Bodensee-Rhein     |
|14513005 | Linth-Rheingletscher | glacier de la Linth-Rhein     |
|14513006 | Reussgletscher | glacier de la Reuss     |
|14513007 | Waldemme- und Entlegletscher | glaciers de la Waldemme et de l’Entle     |
|14513008 | Walliser Gletscher | glacier Valaisan     |
|14513009 | Aaregletscher | glacier de l‘Aar     |
|14513010 | Saanegletscher | glacier de la Sarine     |
|14513011 | Schlierengletscher | glacier des Schlieren     |
|14513012 | Engelberger Gletscher | glacier d&#39;Engelberg     |
|14513013 | Brünig-Aaregletscher | glacier du Brünig-Aar     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  REF_YEAR
_Information de temps ou période. Par ex. &#34;1940-1943: année de référence de l’ancienne ligne de rivage&#34;._

_Type de donnée :  string_





#### Attribut  THIN_COVER {#unconsolidated-deposits-plg-thin-cover}
_Type de couverture meuble pelliculaire_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14515001 | geringmächtige Lockergesteinsbedeckung, undifferenziert | couverture de roches meubles peu épaisse, indifférenciée     |
|14515002 | geringmächtige Moränenbedeckung | couverture morainique peu épaisse     |
|14515003 | geringmächtige Schotterbedeckung | couverture de graviers peu épaisse     |
|14515004 | geringmächtige Schwemmlehmbedeckung | couverture de colluvions peu épaisse     |
|14515005 | geringmächtige Löss- oder Lösslehmbedeckung | couverture de loess ou de loess argileux peu épaisse     |
|14515006 | tiefgründige Verwitterungsdecke | sol d&#39;altération profonde     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  ORIG_DESCR
_Description selon la légende de la carte géologique originale_

_Type de donnée :  string_





## Classe Bedrock_PLG (Rbed){#bedrock-plg}
La classe [Bedrock_PLG](#bedrock-plg) regroupe toutes les unités lithostratigraphiques de roches consolidées.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**TECTO**                 | [ Table ](#gc-tecto-cd)  | Attribution tectonique | [1]
**GEOL_MAPPING_UNIT_ATT**                 | [ Table ](#gc-geol-mapping-unit-att)  | Unités cartographique | [1]
**LITSTRAT_FORMATION_BANK**                 | [ Table ](#gc-litstrat-formation-bank-cd)  | Formation lithostratigraphique | [1]
**CHRONO_TOP**                 | [ Table ](#gc-chrono-cd)  | Attribution chronostratigraphique du toit de la  formation (top) | [1]
**CHRONO_BASE**                 | [ Table ](#gc-chrono-cd)  | Attribution chronostratigraphique de la base de la formation | [1]
**LITHO_MAIN**                 | [ Table ](#gc-litho-cd)  | Description lithologique principale | [1]
**LITHO_SEC**                 | [ Table ](#gc-litho-cd)  | Description lithologique secondaire | [1]
**LITHO_TER**                 | [ Table ](#gc-litho-cd)  | Description lithologique tertiaire | [1]
**CORRELATION**                 | [ Table ](#gc-correlation-cd)  | Correlation | [1]
**DESCRIPTION**                 | string                  | Description selon la légende de la carte géologique originale | [1]
**EXOTIC_ELE**                 | boolean                  | S’agit-il d’un élément exotique (oui / non)? | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14334001 | Festgestein | roche consolidée     |




#### Attribut  TECTO
_Attribution tectonique_

Voir [GC_TECTO_CD](#gc-tecto-cd) dans l'annexe





#### Attribut  GEOL_MAPPING_UNIT_ATT
_Unités cartographique_

Voir [GC_GEOL_MAPPING_UNIT_ATT](#gc-geol-mapping-unit-att) dans l'annexe





#### Attribut  LITSTRAT_FORMATION_BANK
_Formation lithostratigraphique_

Voir [GC_LITSTRAT_FORMATION_BANK_CD](#gc-litstrat-formation-bank-cd) dans l'annexe





#### Attribut  CHRONO_TOP
_Attribution chronostratigraphique du toit de la  formation (top)_

Voir [GC_CHRONO_CD](#gc-chrono-cd) dans l'annexe





#### Attribut  CHRONO_BASE
_Attribution chronostratigraphique de la base de la formation_

Voir [GC_CHRONO_CD](#gc-chrono-cd) dans l'annexe





#### Attribut  LITHO_MAIN
_Description lithologique principale_

Voir [GC_LITHO_CD](#gc-litho-cd) dans l'annexe





#### Attribut  LITHO_SEC
_Description lithologique secondaire_

Voir [GC_LITHO_CD](#gc-litho-cd) dans l'annexe





#### Attribut  LITHO_TER
_Description lithologique tertiaire_

Voir [GC_LITHO_CD](#gc-litho-cd) dans l'annexe





#### Attribut  CORRELATION
_Correlation_

Voir [GC_CORRELATION_CD](#gc-correlation-cd) dans l'annexe





#### Attribut  DESCRIPTION
_Description selon la légende de la carte géologique originale_

_Type de donnée :  string_





#### Attribut  EXOTIC_ELE
_S’agit-il d’un élément exotique (oui / non)?_

_Type de donnée :  boolean_









# Thème GEOMORPHOLOGY

## Classe Instability_Structures_PT (Gins){#instability-structures-pt}
La classe [Instability_Structures_PT](#instability-structures-pt) contient des indications
sur des instabilités de pentes (glissements) observés
localement, qui ne peuvent pas être délimités spatialement.
Cependant, lorsque cela est possible, les masses de roches
instables doivent être saisies comme polygones (classe
Instabilities_PLG).




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11601001 | Hinweis auf Hanginstabilität | indice d&#39;instabilité     |




## Classe Instability_Structures_L (Gins){#instability-structures-l}
La classe [Instability_Structures_L](#instability-structures-l) comprend les morphologies
linéaires qui se sont formées en surface à la suite
d&#39;instabilités de pente.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11701001 | Stauchwulst | bourrelet de glissement     |
|11701002 | Nackentälchen, Zerrstruktur | limite de contrepente     |
|11701003 | Abrissrand | niche d´arrachement     |
|11701004 | offene Spalte | fissure ouverte     |




## Classe Instabilities_PLG (Gins){#instabilities-plg}
La classe [Instabilities_PLG](#instabilities-plg) contient tous les polygones qui
délimitent les zones de roches solides ou meubles instables.
Cette classe délimite les espaces de processus des
différents types de processus de mouvements de masse; les
corps rocheux ou les dépôts de roche meuble proprement dits,
qui ont été affectés ou formés par des processus de
mouvement de masse, sont décrits dans les classes
Bedrock_PLG et/ou Unconsolidated_Deposits_PLG.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**MAIN_MOV**                 | [CD](#instabilities-plg-main-mov)  | Phase de mouvement principale | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15801001 | Sackungsgebiet | zone de tassement     |
|15801002 | Gebiet mit Hakenwurf | zone de fauchage     |
|15801003 | Rutschgebiet | zone de glissement     |
|15801004 | Gebiet mit Solifluktion | zone de solifluxion     |




#### Attribut  MAIN_MOV {#instabilities-plg-main-mov}
_Phase de mouvement principale_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11502001 | Hauptbewegungsphase vor dem letzteiszeitlichen Maximum | phase principale du mouvement avant le Dernier Maximum Glaciaire     |
|11502002 | Hauptbewegungsphase nach dem letzteiszeitlichen Maximum | phase principale du mouvement après le Dernier Maximum Glaciaire     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




## Classe Glacial_Structures_PT (Ggla){#glacial-structures-pt}
La classe [Glacial_Structures_PT](#glacial-structures-pt) contient des types d’objets
qui montrent ponctuellement la présence dans le passé d’un
glacier (les stries glaciaires sont des objets orientés et
se trouvent en conséquence dans la classe Lineation_PT.)




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11201002 | Gletschermühle, Strudelloch | marmite glaciaire, cavité d´érosion     |
|11201001 | glazitektonische Deformation | déformation glaciotectonique     |




## Classe Glacial_and_Periglacial_Structures_L (Ggla){#glacial-and-periglacial-structures-l}
La classe [Glacial_and_Periglacial_Structures_L](#glacial-and-periglacial-structures-l) contient des
structures linéaires qui indiquent un milieu de formation
glaciaire ou périglaciaire.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**MORAI_MO**                 | [CD](#glacial-and-periglacial-structures-l-morai-mo)  | Morphologie de la moraine | [0..1]
**GLAC_TYP**                 | [CD](#glacial-and-periglacial-structures-l-glac-typ)  | Type de glacier auquel le type d’objet est associé | [0..1]
**ICE_M_P**                 | [CD](#glacial-and-periglacial-structures-l-ice-m-p)  | Stade glaciaire | [0..1]
**QUAT_STR**                 | [CD](#glacial-and-periglacial-structures-l-quat-str)  | Attribution chronostratigraphique du vallum morainique au sein du Quaternaire | [0..1]
**REF_YEAR**                 | integer                  | Année de référence | [0..1]
**SOURCE**                 | string                  | Source des données déduites à partir de données historiques | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11301001 | Moränenwall | vallum morainique     |
|11301002 | Moränenwall auf Gletscher oder auf Toteis | cordon morainique sur glacier ou sur glace morte     |
|11301003 | Kameterrassenkante | bord de terrasse de kame     |
|11301004 | älterer Gletscherstand, basierend auf historischen Daten | ancien stade glaciaire, déduit de données historiques     |
|11301005 | Schliffgrenze | limite supérieure de l&#39;érosion glaciaire (trimline)     |
|11301006 | Protalus Rampart Wulst | bourrelet de protalus rampart     |
|11301007 | Blockwulst im Blockgletscher | bourrelet de glacier rocheux     |
|11301008 | Schneehaldenmoränenwall | vallum de moraine de névé     |
|11301009 | Verbreitungsgrenze von Geschiebe | limite de l&#39;étendue des blocs     |
|11301010 | periglazialer Wulst im Allg. | 11301010     |




#### Attribut  MORAI_MO {#glacial-and-periglacial-structures-l-morai-mo}
_Morphologie de la moraine_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11302001 | symmetrisch | symétrique     |
|11302002 | einseitig abfallend | unilatéral     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  GLAC_TYP {#glacial-and-periglacial-structures-l-glac-typ}
_Type de glacier auquel le type d’objet est associé_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11303001 | Lokalgletscher | glacier local     |
|11303002 | grosse Tal- und Vorlandgletscher | grands glaciers de vallées et de piedmont     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  ICE_M_P {#glacial-and-periglacial-structures-l-ice-m-p}
_Stade glaciaire_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11304001 | Maximalstand, undifferenziert | stade maximal, indifférencié     |
|11304002 | Bern | Berne     |
|11304003 | Bremgarten, undifferenziert | Bremgarten, indifferencié     |
|11304004 | Konstanz | Constance     |
|11304005 | Feuerthalen, undifferenziert | Feuerthalen, indifferencié     |
|11304006 | Gurten | Gurten     |
|11304007 | Hurden | Hurden     |
|11304008 | Killwangen | Killwangen     |
|11304009 | Mellingen | Mellingen     |
|11304010 | Muri | Muri     |
|11304011 | Rotkreuz | Rotkreuz     |
|11304012 | Schaffhausen, undifferenziert | Schaffhouse, indifferencié     |
|11304013 | Schlieren, undifferenziert | Schlieren, indifferencié     |
|11304014 | Schosshalde | Schosshalde     |
|11304015 | Seftigschwand | Seftigschwand     |
|11304016 | Solothurn | Soleure     |
|11304017 | Spreitenbach | Spreitenbach     |
|11304018 | Spreitenbach-Killwangen | Spreitenbach-Killwangen     |
|11304019 | Stein am Rhein, undifferenziert | Stein am Rhein, indifferencié     |
|11304020 | Stetten, undifferenziert | Stetten     |
|11304021 | Wangen I | Wangen I     |
|11304022 | Wangen II | Wangen II     |
|11304023 | Wittigkofen | Wittigkofen     |
|11304024 | Zürich, undifferenziert | Zurich, indifferencié     |
|11304025 | Stein-am-Rhein I | Stein am Rhein I     |
|11304026 | Stein-am-Rhein II | Stein am Rhein II     |
|11304027 | Stein-am-Rhein III | Stein am Rhein III     |
|11304028 | Feuerthalen I | Feuerthalen I     |
|11304029 | Feuerthalen II | Feuerthalen II     |
|11304030 | Schaffausen I | Schaffhouse I     |
|11304031 | Schaffausen II | Schaffhouse II     |
|11304035 | Küblis | Küblis     |
|11304036 | Lunden | Lunden     |
|11304037 | Chur | Coire     |
|11304038 | Sargans | Sargans     |
|11304039 | Koblach | Koblach     |
|11304040 | Fideris | Fideris     |
|11304041 | Serneus | Serneus     |
|11304042 | Wangen, undifferenziert | Wangen, indifferencié     |
|11304043 | Sursee | Sursee     |
|11304044 | Triengen | Triengen     |
|11304045 | Staffelbach-Stand | 11304045     |
|11304046 | Zürich I | 11304046     |
|11304047 | Zürich II | 11304047     |
|11304048 | Schlieren I | 11304048     |
|11304049 | Schlieren II | 11304049     |
|11304050 | Bremgarten I | Bremgarten I     |
|11304051 | Bremgarten II | Bremgarten II     |
|11304052 | Bülach I | Bülach I     |
|11304053 | Bülach II | Bülach II     |
|11304054 | Bülach, undifferenziert | Bülach, indifferencié     |
|11304055 | Dättikon | Dättikon     |
|11304056 | Regensdorf | Regensdorf     |
|11304057 | Seeb | Seeb     |
|11304058 | Stetten I | Stetten I     |
|11304059 | Stetten II | Stetten II     |
|11304060 | Würenlos I | Würenlos I     |
|11304061 | Würenlos II | Würenlos II     |
|11304062 | Würenlos, undifferenziert | Würenlos, indifferencié     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  QUAT_STR {#glacial-and-periglacial-structures-l-quat-str}
_Attribution chronostratigraphique du vallum morainique au sein du Quaternaire_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11305001 | 1. Vergletscherung der letzten Eiszeit (MIS 5d) | 1ère glaciation de la Dernière Période glaciaire (MIS 5d)     |
|11305002 | 2. Vergletscherung der letzten Eiszeit (MIS 4) | 2ème glaciation de la Dernière Période glaciaire (MIS 4)     |
|11305003 | 3. Vergletscherung der letzten Eiszeit (LGM, MIS 2) | 3ème glaciation de la Dernière Période glaciaire (LGM, MIS 2)     |
|11305004 | Gschnitz | Gschnitz     |
|11305005 | Clavadel | Clavadel     |
|11305006 | Daun | Daun     |
|11305007 | Egesen | Egesen     |
|11305008 | Mittleres Pleistozän | Pléistocène moyen     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  REF_YEAR
_Année de référence._

_Type de donnée :  integer_





#### Attribut  SOURCE
_Source des données déduites à partir de données historiques_

_Type de donnée :  string_





## Classe Glacial_Structures_PLG (Ggla){#glacial-structures-plg}
La classe [Glacial_Structures_PLG](#glacial-structures-plg) regroupe les formes du
paysage d’origine glaciaire qui se sont formées par
écoulement basal de la glace du glacier ou par sa fonte.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11401001 | Drumlin, drumlinartige Kieskuppe | drumlin, croupe graveleuse en forme de drumlin     |
|11401003 | Rundhöcker | roches moutonnées     |
|11401004 | Toteisloch, Soll | doline glaciaire, soll     |
|11401005 | Kame | 11401005     |




## Classe Erosional_Structures_PT (Gero){#erosional-structures-pt}
La classe [Erosional_Structures_PT](#erosional-structures-pt) contient des éléments
locaux du paysage qui se sont formés au cours du temps sous
l’influence de processus érosifs.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11001001 | Erdpyramide | demoiselle coiffée     |




## Classe Erosional_Structures_L (Gero){#erosional-structures-l}
La classe [Erosional_Structures_L](#erosional-structures-l) contient des formes
érosives linéaires telles que les bords d&#39;érosion en général
ou les bords de terrasses.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11101001 | Erosionsrand | bord d´érosion     |
|11101002 | Terrassenkante | bord de terrasse     |
|11101003 | Schichtstufenkante | escarpement en tête de banc     |




## Classe Karstic_Structures_PT (Gkar){#karstic-structures-pt}
La classe [Karstic_Structures_PT](#karstic-structures-pt) regroupe les phénomènes
karstiques qui sont représentés par des formes ponctuelles.
Elle contient entre autres le ponor ou l’entrée d’une
grotte.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**ICE_CAVE**                 | boolean                  | S’agit-il d’une glacière (oui / non) | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11301001 | Moränenwall | vallum morainique     |
|11301002 | Moränenwall auf Gletscher oder auf Toteis | cordon morainique sur glacier ou sur glace morte     |
|11301003 | Kameterrassenkante | bord de terrasse de kame     |
|11301004 | älterer Gletscherstand, basierend auf historischen Daten | ancien stade glaciaire, déduit de données historiques     |
|11301005 | Schliffgrenze | limite supérieure de l&#39;érosion glaciaire (trimline)     |
|11301006 | Protalus Rampart Wulst | bourrelet de protalus rampart     |
|11301007 | Blockwulst im Blockgletscher | bourrelet de glacier rocheux     |
|11301008 | Schneehaldenmoränenwall | vallum de moraine de névé     |
|11301009 | Verbreitungsgrenze von Geschiebe | limite de l&#39;étendue des blocs     |
|11301010 | periglazialer Wulst im Allg. | 11301010     |




#### Attribut  ICE_CAVE
_S’agit-il d’une glacière (oui / non)_

_Type de donnée :  boolean_





## Classe Karstic_Structures_PLG (Gkar){#karstic-structures-plg}
La classe [Karstic_Structures_PLG](#karstic-structures-plg) comprend les formes
karstiques surfaciques telles que les dolines ou les poljés.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12001001 | Senke ohne oberirdischen Abfluss | dépression sans exutoire superficiel     |
|12001002 | Doline | doline     |
|12001003 | Karrenfeld | lapiez     |
|12001004 | Polje | poljé     |




## Classe Alluvial_and_Lacustrine_Structures_L (Gall){#alluvial-and-lacustrine-structures-l}
La classe [Alluvial_and_Lacustrine_Structures_L](#alluvial-and-lacustrine-structures-l) contient les
morphologies linéaires d’origine fluviatile ou lacustre.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**AGE**                 | [CD](#alluvial-and-lacustrine-structures-l-age)  | Âge du type d&#39;obje | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10901001 | Strandwall | cordon littoral     |
|10901002 | Achse einer Murgangrinne | axe d&#39;un chenal de lave torrentielle     |




#### Attribut  AGE {#alluvial-and-lacustrine-structures-l-age}
_Âge du type d&#39;obje_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10902001 | fossil | fossile     |
|10902002 | rezent | récent     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |








# Thème TECTONICS

## Classe Deformation_Structures_PT (Tdef){#deformation-structures-pt}
La classe [Deformation_Structures_PT](#deformation-structures-pt) contient des structures de déformation tectonique observées ponctuellement, telles que des endroits localement très plissés (plissotement) ou des endroits avec une fissuration marquée. Cette classe contient également des points construits, tels que l&#39;orientation de la surface de l&#39;axe des plis.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**AZIMUTH**                 | integer                  | Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles  d&#39;une montre | [0..1]
**DIP**                 | integer                  | Valeur du plongement du type d&#39;&#39;objet (valeur en degrés, mesurée de l’horizontale
(0°) vers le bas jusqu’à la verticale (90°)) | [0..1]
**FOLD_TYP**                 | [CD](#deformation-structures-pt-fold-typ)  | Caractéristique du type d&#39;objet | [0..1]
**FOLD_FOR**                 | [CD](#deformation-structures-pt-fold-for)  | Forme du type d&#39;objet | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14601001 | punktuell beobachtete tektonische Brekzie | brèche tectonique observée ponctuellement     |
|14601002 | ausgeprägte Klüftung | diaclases bien marquées     |
|14601003 | tektonische Diskordanz | discordance tectonique     |
|14601004 | Orientierung der Faltenachsenfläche | orientation de la surface axiale d&#39;un pli     |
|14601005 | Fältelung | plissotement (plis)     |
|14601006 | Darstellung der Spur einer Achsenfläche | représentation de la trace d&#39;une surface axiale     |
|14601007 | Chevron-Falte, Kink Fold | plis en chevron, Kink Fold     |




#### Attribut  AZIMUTH
_Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles  d&#39;une montre_

_Type de donnée :  integer_





#### Attribut  DIP
_Valeur du plongement du type d&#39;&#39;objet (valeur en degrés, mesurée de l’horizontale
(0°) vers le bas jusqu’à la verticale (90°))_

_Type de donnée :  integer_





#### Attribut  FOLD_TYP {#deformation-structures-pt-fold-typ}
_Caractéristique du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14604001 | Antiklinale | anticlinal     |
|14604002 | Synklinale | synclinal     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  FOLD_FOR {#deformation-structures-pt-fold-for}
_Forme du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14605001 | Antiform | antiforme     |
|14605002 | Synform | synforme     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




## Classe Deformation_Structures_L (Tdef){#deformation-structures-l}
La classe [Deformation_Structures_L](#deformation-structures-l) regroupe les structures
linéaires de déformations tectoniques comme le tracé d’une
charnière de pli.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14701001 | Faltenscharnier | charnière de pli     |




## Classe Deformation_Structures_PLG (Tdef){#deformation-structures-plg}
Dans la classe [Deformation_Structures_PLG](#deformation-structures-plg) se trouvent les
régions marquées par des structures tectoniques à grande
échelle comme les zones tectonisées ou les zones diaclasées.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**TYPE**                 | [CD](#deformation-structures-plg-type)  | Caractéristique du type d&#39;objet | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14801001 | Kluftzone | zone diaclasée     |
|14801002 | tektonisierte Zone | zone tectonisée     |




#### Attribut  TYPE {#deformation-structures-plg-type}
_Caractéristique du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14802001 | kataklastisch | cataclastique     |
|14802002 | kakiritisch | kakiritique     |
|14802003 | mylonitisch | mylonitique     |
|14802004 | pseudotachylitisch | pseudotachylitique     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




## Classe Tectonic_Boundaries_L (Ttec){#tectonic-boundaries-l}
La classe [Tectonic_Boundaries_L](#tectonic-boundaries-l) comprend toutes les
accidents tectoniques.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**FAULT_MO**                 | [CD](#tectonic-boundaries-l-fault-mo)  | Mouvement de la faille | [0..1]
**VERTI_MO**                 | [CD](#tectonic-boundaries-l-verti-mo)  | Mouvement parallèle au pendage du plan de faille | [0..1]
**HORIZ_MO**                 | [CD](#tectonic-boundaries-l-horiz-mo)  | Mouvement parallèle à la direction du plan de faille ou de cisaillement | [0..1]
**LIM_TYP**                 | [CD](#tectonic-boundaries-l-lim-typ)  | Type de limite tectonique | [1]
**HIERA**                 | [CD](#tectonic-boundaries-l-hiera)  | Hiérarchie de l&#39;accident tectonique | [1]
**STATUS**                 | [CD](#tectonic-boundaries-l-status)  | État du type d&#39;objet | [1]
**META_STA**                 | [CD](#tectonic-boundaries-l-meta-sta)  | Chronologie tecto-métamorphique du type d’objet | [0..1]
**NAME**                 | string                  | Nom du type de l&#39;objet | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14901001 | Überschiebung | chevauchement     |
|14901002 | Abschiebung | détachement (faille normale de grande extension et faible pendage)     |
|14901004 | Bruch | faille     |
|14901005 | Aufschiebung | faille inverse     |
|14901006 | Blattverschiebung | décrochement     |
|14901007 | komplexe Störung | accident tectonique complexe     |
|14901008 | Störung i. Allg. | accident tectonique en général     |
|14901009 | neotektonischer Bruch | 14901009     |




#### Attribut  FAULT_MO {#tectonic-boundaries-l-fault-mo}
_Mouvement de la faille_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14902001 | schrägverschiebend (oblique slip) | oblique (oblique slip)     |
|14902002 | parallel zur Streichrichtung (Horizontalverschiebung) | parallèle à la direction     |
|14902003 | parallel zur Fallrichtung (strike slip) | parallèle au pendage (strike slip)     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  VERTI_MO {#tectonic-boundaries-l-verti-mo}
_Mouvement parallèle au pendage du plan de faille_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14903001 | aufschiebend | 14903001     |
|14903002 | abschiebend | 14903002     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  HORIZ_MO {#tectonic-boundaries-l-horiz-mo}
_Mouvement parallèle à la direction du plan de faille ou de cisaillement_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14904001 | dextral | dextre     |
|14904002 | sinistral | sénestre     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  LIM_TYP {#tectonic-boundaries-l-lim-typ}
_Type de limite tectonique_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14910001 | Decken trennend | délimitant des nappes     |
|14910002 | Schuppen trennend | délimitant des écailles     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  HIERA {#tectonic-boundaries-l-hiera}
_Hiérarchie de l&#39;accident tectonique_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14911001 | Störung | 14911001     |
|14911002 | Teilstörungssystem | système tectonique partiel     |
|14911003 | Grossstörungssystem | grand système tectonique     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  STATUS {#tectonic-boundaries-l-status}
_État du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14906001 | gesichert, im Allgemeinen | certain, en général     |
|14906002 | gesichert, unter Tage festgestellt | certain, mis en évidence dans des travaux souterrains     |
|14906003 | vermutet | probable     |
|14906004 | aus Seismikdaten interpretiert | interprété de données sismiques     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  META_STA {#tectonic-boundaries-l-meta-sta}
_Chronologie tecto-métamorphique du type d’objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14908001 | vor der Platznahme der Decken | anté-nappe     |
|14908002 | während der Platznahme der Decken | syn-nappe     |
|14908003 | nach der Platznahme der Decken | post-nappe     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  NAME
_Nom du type de l&#39;objet_

_Type de donnée :  string_









# Thème MEASUREMENTS_SPATIAL_ORIENTATION

## Classe Folds_PT (Mfol){#folds-pt}
La classe [Folds_PT](#folds-pt) contient les objets qui décrivent la
position spatiale d’objets géologiques plissés (par des
mesures prises directement sur le terrain).




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**FOLD_TYP**                 | [CD](#folds-pt-fold-typ)  | Type de pli | [0..1]
**FOLD_FOR**                 | [CD](#folds-pt-fold-for)  | Forme du type de pli | [0..1]
**PHASE**                 | [CD](#folds-pt-phase)  | Phase de déformation | [0..1]
**PHASE_REF**                 | string                  | Référence pour les données concernant la phase de déformation | [0..1]
**AZIMUTH**                 | integer                  | Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles  d&#39;une montre | [1]
**DIP**                 | integer                  | Valeur du plongement du type d&#39;objet (en degrés), mesurée de l’horizontale (0°) vers le bas jusqu’à la  verticale (90°) | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13601001 | Orientierung der Faltenachse | orientation d&#39;un axe de pli     |
|13601002 | Orientierung der Scheitellinie | orientation d&#39;une ligne de crête     |
|13601003 | Orientierung der Muldenlinie | orientation d&#39;une ligne de creux     |




#### Attribut  FOLD_TYP {#folds-pt-fold-typ}
_Type de pli_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13602001 | Antiklinale | anticlinal     |
|13602002 | Synklinale | synclinal     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  FOLD_FOR {#folds-pt-fold-for}
_Forme du type de pli_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|




#### Attribut  PHASE {#folds-pt-phase}
_Phase de déformation_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13604001 | F1 (1. Phase) | F1 (1ère phase)     |
|13604002 | F2 (2. Phase) | F2 (2ème phase)     |
|13604003 | F3 (3. Phase) | F3 (3ème phase)     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  PHASE_REF
_Référence pour les données concernant la phase de déformation_

_Type de donnée :  string_





#### Attribut  AZIMUTH
_Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles  d&#39;une montre._

_Type de donnée :  integer_





#### Attribut  DIP
_Valeur du plongement du type d&#39;objet (en degrés), mesurée de l’horizontale (0°) vers le bas jusqu’à la  verticale (90°)_

_Type de donnée :  integer_





## Classe Lineation_PT (Mlin){#lineation-pt}
La classe [Lineation_PT](#lineation-pt) contient des structures linéaires
dont la position spatiale est décrite par des mesures
directes sur le terrain. La position dans l’espace, entre
autre de stries glaciaires et de tectoglyphes, fait aussi
partie de cette classe tout comme l’orientation de la
linéation d’intersection ou de linéation d’étirement.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**AZIMUTH**                 | integer                  | Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles  d&#39;une montre | [1]
**DIP**                 | integer                  | Valeur du plongement du type d&#39;objet (en degrés), mesurée de l’horizontale (0°) vers le bas jusqu’à la  verticale (90°) | []





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13701001 | Orientierung der Intersektionslineation | orientation de la linéation d´intersection     |
|13701002 | Orientierung der Streckungslineation | orientation de la linéation d&#39;étirement     |
|13701003 | Orientierung von Rutschharnischen | orientation des tectoglyphes     |
|13701004 | Orientierung von Gletscherschliffen | orientation des stries glaciaires     |




#### Attribut  AZIMUTH
_Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles  d&#39;une montre_

_Type de donnée :  integer_





#### Attribut  DIP
_Valeur du plongement du type d&#39;objet (en degrés), mesurée de l’horizontale (0°) vers le bas jusqu’à la  verticale (90°)_

_Type de donnée :  integer_





## Classe Planar_Structures_PT (Mpla){#planar-structures-pt}
La classe [Planar_Structures_PT](#planar-structures-pt) contient des types d&#39;objets
qui décrivent la position des structures planaires avec des
mesures directes sur le terrain.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**POLARITY**                 | [CD](#planar-structures-pt-polarity)  | Polarité du type d&#39;objet dans l&#39;espace | [0..1]
**PHASE**                 | [CD](#planar-structures-pt-phase)  | Phase de déformation | [0..1]
**PHASE_REF**                 | string                  | Référence pour les données concernant la phase de déformation | [0..1]
**OB_DIP_SLO**                 | boolean                  | Dip slope (oui / non)? | [0..1]
**AZIMUTH**                 | integer                  | Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles  d&#39;une montre | [1]
**DIP**                 | integer                  | Valeur du plongement du type d&#39;objet (en degrés), mesurée de l’horizontale (0°) vers le bas jusqu’à la  verticale (90°) | []





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13801002 | Orientierung eines Ganges | orientation d&#39;un filon     |
|13801003 | Orientierung einer Bruchfläche | orientation d&#39;un plan de faille     |
|13801004 | Orientierung der Schieferung | orientation d&#39;une schistosité     |
|13801005 | Orientierung einer Schichtung oder Schieferung | orientation d&#39;une couche ou d&#39;une schistosité     |
|13801001 | Orientierung der Schichten | orientation des couches     |
|13801006 | Schüttungsrichtung | direction de transport sédimentaire     |




#### Attribut  POLARITY {#planar-structures-pt-polarity}
_Polarité du type d&#39;objet dans l&#39;espace_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13802001 | normal | normale     |
|13802002 | überkippt | renversée     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  PHASE {#planar-structures-pt-phase}
_Phase de déformation_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13803001 | S1 (1. Phase) | S1 (1ère phase)     |
|13803002 | S2 (2. Phase) | S2 (2ème phase)     |
|13803003 | S3 (3. Phase) | S3 (3ème phase)     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  PHASE_REF
_Référence pour les données concernant la phase de déformation_

_Type de donnée :  string_





#### Attribut  OB_DIP_SLO
_Dip slope (oui / non)?_

_Type de donnée :  boolean_





#### Attribut  AZIMUTH
_Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles  d&#39;une montre_

_Type de donnée :  integer_





#### Attribut  DIP
_Valeur du plongement du type d&#39;objet (en degrés), mesurée de l’horizontale (0°) vers le bas jusqu’à la  verticale (90°)_

_Type de donnée :  integer_









# Thème LOCAL_ADDITIONAL_INFORMATION

## Classe Anomalies_PT (Lano){#anomalies-pt}
La classe [Anomalies_PT](#anomalies-pt) contient des anomalies observées et /
ou mesurées localement.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**TYPE**                 | [CD](#anomalies-pt-type)  | Caractéristique du type d&#39;objet | []





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12801001 | gemessene Anomalie | anomalie mesurée     |
|12801002 | Fulgurit | fulgurite     |




#### Attribut  TYPE {#anomalies-pt-type}
_Caractéristique du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|




## Classe Fossils_PT (Lfos){#fossils-pt}
La classe [Fossils_PT](#fossils-pt) contient tous les gisements.
fossilifères




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**DIVISION**                 | [CD](#fossils-pt-division)  | Catégorie de fossile à laquelle appartient l&#39;objet | [0..1]
**SYSTEM**                 | table                  | Groupe de fossiles | [0..5]
**DAT_METH**                 | [CD](#fossils-pt-dat-meth)  | Méthode de datation | [0..1]
**STATUS**                 | [CD](#fossils-pt-status)  | État du type d&#39;objet | [0..1]
**PROTECTED**                 | boolean                  | Objet géologique protégé (oui / non)? | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12901001 | Fossilfundstelle | gisement fossilifère     |




#### Attribut  DIVISION {#fossils-pt-division}
_Catégorie de fossile à laquelle appartient l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12902001 | Tierreste | faune     |
|12902002 | Pflanzen- und Tierreste | faune et flore     |
|12902003 | Pflanzenreste | flore     |
|12902004 | Spuren | traces     |
|12902006 | Einzeller | unicellulaires     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  SYSTEM
_Groupe de fossiles_

_Type de donnée :  table_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12903008 | Holz | bois     |
|12903010 | Schwämme | éponges     |
|12903018 | Reptilien | reptiles     |
|12903004 | Foraminiferen | foraminifères     |
|12903013 | Mollusken | mollusques     |
|12903002 | Ostrakoden | ostracodes     |
|12903015 | Bivalven | bivalves     |
|12903021 | Palynomorphe | palynomorphes     |
|12903011 | Korallen | coraux     |
|12903012 | Brachiopoden | brachiopodes     |
|12903001 | Vertebraten | vertébrés     |
|12903019 | Säugetiere | mammifères     |
|12903006 | Blätter | feuilles     |
|12903007 | Gräser | graminées     |
|12903016 | Echinodermen | échinodermes     |
|12903003 | Gastropoden | gastéropodes     |
|12903005 | Algen | algues     |
|12903009 | Ammoniten | ammonites     |
|12903014 | Cephalopoden | céphalopodes     |
|12903017 | Fische | poissons     |




#### Attribut  DAT_METH {#fossils-pt-dat-meth}
_Méthode de datation_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12904001 | radiometrisch datiert | daté radiométriquement     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  STATUS {#fossils-pt-status}
_État du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12905001 | aufgeschlossen | affleurant     |
|12905002 | wieder verdeckt | recouvert     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  PROTECTED
_Objet géologique protégé (oui / non)?_

_Type de donnée :  boolean_





## Classe Indication_of_Resources_PT (Lres){#indication-of-resources-pt}
La classe [Indication_of_Resources_PT](#indication-of-resources-pt) regroupe les gisements
de minéraux, de gaz, d’hydrocarbures et de matériel
volcanique




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**STATUS**                 | [CD](#indication-of-resources-pt-status)  | Etat du type d&#39;objet | [0..1]
**MATERIAL**                 | [CD](#indication-of-resources-pt-material)  | Matériau associé au type d&#39;objet | [0..1]
**CHEMISTRY**                 | string                  | Composant(s) chimique(s) caractérisant la nature du type d&#39;objet | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13201001 | Mineralfundstelle | gisement de minéraux     |
|13201002 | Gasquelle | source de gaz naturel     |
|13201003 | Anzeichen auf Öl | indices de pétrole     |
|13201006 | Fundstelle vulkanischer Auswürflinge (Tephra) | gisement de projections volcaniques (tephra)     |
|13201007 | Fundstelle von Ries-Auswürflingen | gisement de projections du Ries     |
|13201008 | Asphalt, vereinzeltes Vorkommen | asphalte, gisement isolé     |
|13201005 | Fundstelle von vulkanischem Tuffit | gisement de tuffite volcanique     |
|13201004 | Tasche, Karsttasche, Kluft, mit Füllung von siderolithischem Sediment | poche, poche karstique, fissure, remplie de matériel sidérolithique     |
|13201009 | Meteoritenfundstelle | gisement de météorite     |




#### Attribut  STATUS {#indication-of-resources-pt-status}
_Etat du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13202001 | aufgeschlossen | affleurant     |
|13202002 | wieder verdeckt | recouvert     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  MATERIAL {#indication-of-resources-pt-material}
_Matériau associé au type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13203001 | Boluston | argile à bolus     |
|13203002 | Huppererde | hupper     |
|13203003 | Bohnerz | pisolites ferrugineuses     |
|13203004 | Glas- / Quarzsand | sable vitrifiable     |
|13203005 | Walkerde | terre à foulon     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  CHEMISTRY
_Composant(s) chimique(s) caractérisant la nature du type d&#39;objet_

_Type de donnée :  string_





## Classe Mineralised_Zone_L (Lmin){#mineralised-zone-l}
La classe [Mineralised_Zone_L](#mineralised-zone-l) contient les zones
minéralisées.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**CHEMISTRY**                 | string                  | Composant(s) chimique(s) caractérisant la nature du type d&#39;objet | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13301001 | Vererzungszone | zone minéralisée     |




#### Attribut  CHEMISTRY
_Composant(s) chimique(s) caractérisant la nature du type d&#39;objet._

_Type de donnée :  string_





## Classe Sedimentary_Structures_PT (Lsed){#sedimentary-structures-pt}
La classe [Sedimentary_Structures_PT](#sedimentary-structures-pt) contient la description
des structures sédimentaires observées.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**AZIMUTH**                 | integer                  | Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles  d&#39;une montre | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13401001 | Sedimentstrukturen | structures sédimentaires     |
|13401002 | Riffstrukturen | structures récifales     |
|13401003 | Erosions- oder Omissionsfläche, Hartgrund, Kondensationshorizont | surface d´érosion ou lacune stratigraphique, surface durcie, niveau de condensation     |
|13401004 | stratigraphische Lage (Polarität) einer Schichtserie | position stratigraphique (polarité) d´une couche sédimentaire     |
|13401005 | Winkeldiskordanz | discordance angulaire     |
|13401006 | Entwässerungstrichter (blow-out structure) | cratère d&#39;échappement d&#39;eau     |




#### Attribut  AZIMUTH
_Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles  d&#39;une montre._

_Type de donnée :  integer_





## Classe Type_Localities_PT (Ltyp){#type-localities-pt}
La classe [Type_Localities_PT](#type-localities-pt) regroupe les types d’objets qui
décrivent les profiles-types ou les affleurements
géologiques importants.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**STRATI**                 | [CD](#type-localities-pt-strati)  | Complément lithostratigraphique du type d&#39;objet | [0..1]
**NAME**                 | string                  | Nom de la localité-type. Description de l’affleurement géologique important | [0..1]
**ACCESSIBIL**                 | boolean                  | Est-ce que le type d’objet était accessible au moment du levé de la carte (oui / non)? | [0..1]
**PROTECTED**                 | boolean                  | Objet géologique protégé (oui / non)? | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13501001 | geologisch relevanter Aufschluss | affleurement géologique important     |
|13501003 | Typusprofil | coupe-type     |




#### Attribut  STRATI {#type-localities-pt-strati}
_Complément lithostratigraphique du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13502001 | Gruppe | groupe     |
|13502002 | Subgruppe | sous-groupe     |
|13502003 | Formation | formation     |
|13502004 | Member | membre     |
|13502005 | Bank | banc     |
|13502006 | Stufe | étage     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  NAME
_Nom de la localité-type. Description de l’affleurement géologique important_

_Type de donnée :  string_





#### Attribut  ACCESSIBIL
_Est-ce que le type d’objet était accessible au moment du levé de la carte (oui / non)?_

_Type de donnée :  boolean_





#### Attribut  PROTECTED
_Objet géologique protégé (oui / non)?_

_Type de donnée :  boolean_





## Classe Prominent_Lithological_Features_L (Lpro){#prominent-lithological-features-l}
La classe [Prominent_Lithological_Features_L](#prominent-lithological-features-l) contient des
horizons rocheux linéaires. Ces horizons rocheux n&#39;ont qu&#39;un
caractère indicatif (par ex. « banc de grès marquant » au
sein de d&#39;alternances de grès et de marnes) et sont séparés
des horizons directeurs (par ex. &#34;calcaire spathique dans le
Hauptrogenstein&#34;). Les horizons marqueurs se trouvent dans
le thème Rock Bodies.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**CONG_SPE**                 | [CD](#prominent-lithological-features-l-cong-spe)  | Caractérisation des conglomérats selon la nature des clastes | [0..1]
**NAME_HORIZ**                 | [ Table ](#gc-geol-mapping-unit-cd)  | Nom de l&#39;horizon repère | [0..1]
**ORIG_DESCR**                 | string                  | Description selon la légende de la carte géologique originale | [0..1]
**LITHO**                 | [ Table ](#gc-litho-cd)  | Description du  matériel (unité lithologique) | [1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13101001 | Gesteinshorizont | horizon de roche     |




#### Attribut  CONG_SPE {#prominent-lithological-features-l-cong-spe}
_Caractérisation des conglomérats selon la nature des clastes_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13102001 | kristallinfreie bis -arme (Kalk-)Nagelfluh | poudingue (calcaire) dépourvu ou pauvre en éléments cristallins     |
|13102002 | kristallinführende (Kalk-)Nagelfluh | poudingue (calcaire) à éléments cristallins     |
|13102003 | bunte bis polygene Nagelfluh | poudingue polygénique     |
|13102004 | Flyschsandstein-Nagelfluh, Riesenkonglomerat | poudingue à éléments de grès de flysch, Riesenkonglomerat     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  NAME_HORIZ
_Nom de l&#39;horizon repère_

Voir [GC_GEOL_MAPPING_UNIT_CD](#gc-geol-mapping-unit-cd) dans l'annexe





#### Attribut  ORIG_DESCR
_Description selon la légende de la carte géologique originale_

_Type de donnée :  string_





#### Attribut  LITHO
_Description du  matériel (unité lithologique)_

Voir [GC_LITHO_CD](#gc-litho-cd) dans l'annexe





## Classe Miscellaneous_PT (Lmis){#miscellaneous-pt}
La classe [Miscellaneous_PT](#miscellaneous-pt) est réservée aux objets locaux
très particuliers qui ne sont pas pertinents pour l’ensemble
des données géologiques. Par conséquent ils ne sont pas
standardisés dans le Modèle de données géologiques.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**ORIG_NAME**                 | string                  | Description originale de l&#39;objet | [1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15501001 | Diverse | divers     |




#### Attribut  ORIG_NAME
_Description originale de l&#39;objet_

_Type de donnée :  string_





## Classe Geological_Outlines_L (Lgeo){#geological-outlines-l}
La classe [Geological_Outlines_L](#geological-outlines-l) contient les contours
géologiques.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**STATUS**                 | [CD](#geological-outlines-l-status)  | État du type d&#39;objet | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13001001 | geologische Kontur | contour géologique     |




#### Attribut  STATUS {#geological-outlines-l-status}
_État du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13002001 | im Allgemeinen | en général     |
|13002002 | vermutet | probable     |
|13002003 | künstlich | artificiel     |
|13002004 | gesichert, tektonisch überprägt | certain, tectonisé     |
|13002005 | vermutet, tektonisch überprägt | probable, tectonisé     |
|13002006 | Gewässerlinie | ligne d&#39;un cours d&#39;eau     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |








# Thème PARAMETER_AND_MODELLING

## Classe Slope_Bedrock_PT (Pslo){#slope-bedrock-pt}
La classe [Slope_Bedrock_PT](#slope-bedrock-pt) contient des informations
ponctuelles provenant de la modélisation de l’orientation
d’horizons lithologiques des roches consolidées dans le
sous-sol ou de surfaces d’érosion.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**TYPE**                 | [CD](#slope-bedrock-pt-type)  | Surface de référence | [1]
**AZIMUTH**                 | integer                  | Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles d&#39;une montre | [0..1]
**DIP**                 | integer                  | Valeur du plongement du type d&#39;objet (en degrés), mesurée de l’horizontale (0°) vers le bas jusqu’à la  verticale (90°) | [0..1]
**FORMATIO**                 | [ Table ](#gc-geol-mapping-unit-cd)  | Unité lithostratigraphique de l’horizon modélisé | [1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14201001 | Neigungsrichtung | direction de plongement     |




#### Attribut  TYPE {#slope-bedrock-pt-type}
_Surface de référence_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14202001 | Felsoberfläche | surface du substratum rocheux     |
|14202002 | Obergrenze einer gegebenen Formation | surface du toit d&#39;une formation donnée     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  AZIMUTH
_Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles d&#39;une montre_

_Type de donnée :  integer_





#### Attribut  DIP
_Valeur du plongement du type d&#39;objet (en degrés), mesurée de l’horizontale (0°) vers le bas jusqu’à la  verticale (90°)_

_Type de donnée :  integer_





#### Attribut  FORMATIO
_Unité lithostratigraphique de l’horizon modélisé_

Voir [GC_GEOL_MAPPING_UNIT_CD](#gc-geol-mapping-unit-cd) dans l'annexe





## Classe Contour_Lines_Bedrock_L (Pcob){#contour-lines-bedrock-l}
La classe [Contour_Lines_Bedrock_L](#contour-lines-bedrock-l) contient les isohypses qui
décrivent la géométrie des roches consolidées dans le sous-
sol et sont le résultat d’une modélisation. Dans cette
classe se trouvent entre autres les isohypses de la surface
du substratum rocheux.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**TYPE**                 | [CD](#contour-lines-bedrock-l-type)  | Surface de référence | [1]
**ALTITUDE**                 | float                  | Valeur altimétrique des isohypses | [1]
**LITSTRAT**                 | [ Table ](#gc-geol-mapping-unit-cd)  | Unité lithostratigraphique de la formation modelisée | [1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13901001 | Isohypse | isohypse     |




#### Attribut  TYPE {#contour-lines-bedrock-l-type}
_Surface de référence_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13902001 | Felsoberfläche | surface du substratum rocheux     |
|13902002 | Obergrenze einer gegebenen Formation | surface du toit d&#39;une formation donnée     |
|13902003 | Untergrenze einer gegebenen Formation | surface de la base d&#39;une formation donnée     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  ALTITUDE
_Valeur altimétrique des isohypses_

_Type de donnée :  float_





#### Attribut  LITSTRAT
_Unité lithostratigraphique de la formation modelisée_

Voir [GC_GEOL_MAPPING_UNIT_CD](#gc-geol-mapping-unit-cd) dans l'annexe





## Classe Modelled_Water_Table_PT (Pmod){#modelled-water-table-pt}
La classe [Modelled_Water_Table_PT](#modelled-water-table-pt) contient des informations
ponctuelles provenant de la modélisation du niveau
piézométrique d’une nappe libre.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**AZIMUTH**                 | integer                  | Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles  d&#39;une montre | [0..1]
**DIP**                 | integer                  | Valeur du plongement du type d&#39;objet (en degrés), mesurée de l’horizontale (0°) vers le bas jusqu’à la  verticale (90°) | [0..1]
**HEIGHT**                 | float                  | Cote de la nappe phréatique | [0..1]
**MEA_PERIOD**                 | range                  | Période de mesure de la profondeur du niveau hydrostatique | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14101001 | Grundwasserfliessrichtung | direction d&#39;écoulement     |
|14101002 | mittlere Höhe des Grundwasserspiegels | niveau moyen de la nappe phréatique     |




#### Attribut  AZIMUTH
_Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles  d&#39;une montre_

_Type de donnée :  integer_





#### Attribut  DIP
_Valeur du plongement du type d&#39;objet (en degrés), mesurée de l’horizontale (0°) vers le bas jusqu’à la  verticale (90°)_

_Type de donnée :  integer_





#### Attribut  HEIGHT
_Cote de la nappe phréatique_

_Type de donnée :  float_





#### Attribut  MEA_PERIOD
_Période de mesure de la profondeur du niveau hydrostatique_

_Type de donnée :  range_





## Classe Contour_Lines_Hydro_L (Pcoh){#contour-lines-hydro-l}
Dans la classe [Contour_Lines_Hydro_L](#contour-lines-hydro-l) se trouvent les
isohypses qui décrivent la surface d’une nappe d’eau
souterraine.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**CONFINE**                 | [CD](#contour-lines-hydro-l-confine)  | État de la pression dans l’aquifère | [0..1]
**ALTITUDE**                 | float                  | Valeur altimétrique des isohypses | [1]
**WA_TABLE**                 | [CD](#contour-lines-hydro-l-wa-table)  | Niveau des eaux | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14001001 | Isohypse des Grundwasserspiegels | isohypse de la surface piézométrique     |




#### Attribut  CONFINE {#contour-lines-hydro-l-confine}
_État de la pression dans l’aquifère_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14002001 | frei | libre     |
|14002002 | gespannt | captive     |
|14002003 | artesisch | artésienne     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  ALTITUDE
_Valeur altimétrique des isohypses_

_Type de donnée :  float_





#### Attribut  WA_TABLE {#contour-lines-hydro-l-wa-table}
_Niveau des eaux_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14004001 | mittlere Höhe des Niedrigwasserstands | altitude moyenne des basses eaux     |
|14004002 | mittlere Höhe des Hochwasserstands | altitude moyenne des hautes eaux     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |








# Thème ANTHROPOGENIC_FEATURES

## Classe Archaeology_PT (Aarc){#archaeology-pt}
La classe [Archaeology_PT](#archaeology-pt) regroupe les sites archéologiques.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | []
**EPOCH**                 | [CD](#archaeology-pt-epoch)  | Époque archéologique du type d&#39;objet | [0..1]
**PERIOD**                 | [CD](#archaeology-pt-period)  | Période archéologique du type d&#39;objet | [0..1]
**AGE**                 | [CD](#archaeology-pt-age)  | Âge archéologique du type d&#39;objet | [0..1]
**TYPE**                 | [CD](#archaeology-pt-type)  | Type de mégalithe | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10101001 | archäologische Fundstelle, Anlage, Siedlungsreste | site archéologique, station, vestiges d&#39;établissement     |
|10101005 | Gräber, Gräberfeld | tombe, site mortuaire     |
|10101007 | Grabhügel, Dolmengrab | tumulus, dolmen funéraire     |
|10101008 | Kultstein | mégalithe     |
|10101009 | Kalkofen | four à chaux     |
|10101010 | Felsenkeller | cave dans la roche     |
|10101011 | Schlackenhalde | crassier     |
|10101012 | Glashütte | verrerie     |
|10101013 | Schmelzofen | four à fer     |
|10101004 | Burgstelle, Burghügel, Wachtturm | motte, emplacement d´un ancien château, d´une fortification, d&#39;un château-fort     |
|10101002 | Höhlensiedlung, Abri | grotte, abri sous roche     |
|10101003 | Pfahlbauten | palafitte     |
|10101006 | Steinplattengrab | sépulture     |
|10101015 | Abbaustelle | exploitation     |




#### Attribut  EPOCH {#archaeology-pt-epoch}
_Époque archéologique du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10002001 | historisch | historique     |
|10002002 | prähistorisch | préhistorique     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  PERIOD {#archaeology-pt-period}
_Période archéologique du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10003001 | Neuzeit | époque moderne     |
|10003002 | Mittelalter | Moyen Âge     |
|10003003 | Römerzeit | époque romaine     |
|10003004 | Eisenzeit | âge du fer     |
|10003005 | Bronzezeit | âge du bronze     |
|10003006 | Steinzeit | âge de la pierre     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  AGE {#archaeology-pt-age}
_Âge archéologique du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10004001 | Latènezeit | La Tène     |
|10004002 | Hallstattzeit | Hallstatt     |
|10004003 | Jungbronzezeit | bronze tardif     |
|10004004 | Mittelbronzezeit | bronze moyen     |
|10004005 | Altbronzezeit | bronze précoce     |
|10004006 | Neolithikum | néolithique     |
|10004007 | Mesolithikum | mésolithique     |
|10004008 | Paläolithikum | paléolithique     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  TYPE {#archaeology-pt-type}
_Type de mégalithe_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10105001 | Menhir | menhir     |
|10105002 | Schalenstein | pierre à cupules     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




## Classe Archaeology_L (Aarc){#archaeology-l}
La classe [Archaeology_L](#archaeology-l) contient les éléments archéologiques
de forme linéaire. Les routes historiques, les chemins creux
et les fossés de fortification font partie de cette classe.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | []
**EPOCH**                 | [CD](#archaeology-l-epoch)  | Époque archéologique du type d&#39;objet | [0..1]
**PERIOD**                 | [CD](#archaeology-l-period)  | Période archéologique du type d&#39;objet | [0..1]
**AGE**                 | [CD](#archaeology-l-age)  | Âge archéologique du type d&#39;objet | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10201001 | Verkehrsweg | voie de communication     |
|10201002 | Hohlweg | chemin creux     |
|10201003 | künstlicher Graben, Befestigungsgraben | fossé artificiel, fossé de fortification     |
|10201004 | künstlicher Erdwall | levée de terre artificielle     |
|10201005 | Wasserleitung | aqueduc     |
|10201006 | Steinreihe | alignement mégalithique     |
|10201007 | Schützengraben | tranchée     |




#### Attribut  EPOCH {#archaeology-l-epoch}
_Époque archéologique du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10002001 | historisch | historique     |
|10002002 | prähistorisch | préhistorique     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  PERIOD {#archaeology-l-period}
_Période archéologique du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10003001 | Neuzeit | époque moderne     |
|10003002 | Mittelalter | Moyen Âge     |
|10003003 | Römerzeit | époque romaine     |
|10003004 | Eisenzeit | âge du fer     |
|10003005 | Bronzezeit | âge du bronze     |
|10003006 | Steinzeit | âge de la pierre     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  AGE {#archaeology-l-age}
_Âge archéologique du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10004001 | Latènezeit | La Tène     |
|10004002 | Hallstattzeit | Hallstatt     |
|10004003 | Jungbronzezeit | bronze tardif     |
|10004004 | Mittelbronzezeit | bronze moyen     |
|10004005 | Altbronzezeit | bronze précoce     |
|10004006 | Neolithikum | néolithique     |
|10004007 | Mesolithikum | mésolithique     |
|10004008 | Paläolithikum | paléolithique     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




## Classe Archaeology_PLG (Aarc){#archaeology-plg}
Dans la classe [Archaeology_PLG](#archaeology-plg) se trouvent les vestiges
archéologiques (p.ex. le Castrum romain) qui recouvrent une
surface importante.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | []
**EPOCH**                 | [CD](#archaeology-plg-epoch)  | Époque archéologique du type d&#39;objet | [0..1]
**PERIOD**                 | [CD](#archaeology-plg-period)  | Période archéologique du type d&#39;objet | [0..1]
**AGE**                 | [CD](#archaeology-plg-age)  | Âge archéologique du type d&#39;objet | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10301001 | Castrum | castrum     |
|10301002 | Refugium, Höhensiedlung, Erdwerk | refugium, oppidum, fortification     |




#### Attribut  EPOCH {#archaeology-plg-epoch}
_Époque archéologique du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10002001 | historisch | historique     |
|10002002 | prähistorisch | préhistorique     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  PERIOD {#archaeology-plg-period}
_Période archéologique du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10003001 | Neuzeit | époque moderne     |
|10003002 | Mittelalter | Moyen Âge     |
|10003003 | Römerzeit | époque romaine     |
|10003004 | Eisenzeit | âge du fer     |
|10003005 | Bronzezeit | âge du bronze     |
|10003006 | Steinzeit | âge de la pierre     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  AGE {#archaeology-plg-age}
_Âge archéologique du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10004001 | Latènezeit | La Tène     |
|10004002 | Hallstattzeit | Hallstatt     |
|10004003 | Jungbronzezeit | bronze tardif     |
|10004004 | Mittelbronzezeit | bronze moyen     |
|10004005 | Altbronzezeit | bronze précoce     |
|10004006 | Neolithikum | néolithique     |
|10004007 | Mesolithikum | mésolithique     |
|10004008 | Paläolithikum | paléolithique     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




## Classe Exploitation_Geomaterials_PT (Aexp){#exploitation-geomaterials-pt}
La classe [Exploitation_Geomaterials_PT](#exploitation-geomaterials-pt) contient des
informations ponctuelles sur les sites d’exploitation de
matériaux géologiques.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | []
**EXP_UNIT**                 | [ Table ](#gc-geol-mapping-unit-cd)  | Unité lithostratigraphique exploitée | [0..*]
**STATUS**                 | [CD](#exploitation-geomaterials-pt-status)  | État de l&#39;exploitation | [0..1]
**DEPTH_TOT**                 | float                  | Profondeur totale du type d&#39;objet (en mètres depuis la surface) | [0..1]
**TARG_MAT**                 | [CD](#exploitation-geomaterials-pt-targ-mat)  | Matériau exploité | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10601001 | Bergwerk, Untertageabbau | mine, exploitation souterraine     |
|10601002 | Stolleneingang | entrée de galerie     |
|10601003 | Schacht | puits de mine     |
|10601004 | Pinge (dolinenartiger Stolleneinbruch) | fontis (effondrement de surface lié à des travaux souterrains)     |
|10601005 | Schürfloch | trace d´exploitation en surface     |
|10601006 | ausgeräumte Bohnerztasche | poche sidérolithique vidée     |




#### Attribut  EXP_UNIT
_Unité lithostratigraphique exploitée_

Voir [GC_GEOL_MAPPING_UNIT_CD](#gc-geol-mapping-unit-cd) dans l'annexe





#### Attribut  STATUS {#exploitation-geomaterials-pt-status}
_État de l&#39;exploitation_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10603001 | in Betrieb | en exploitation     |
|10603002 | stillgelegt | abandonné     |
|10603003 | aufgefüllt | comblé     |
|10603004 | verfallen | effondré     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  DEPTH_TOT
_Profondeur totale du type d&#39;objet (en mètres depuis la surface)._

_Type de donnée :  float_





#### Attribut  TARG_MAT {#exploitation-geomaterials-pt-targ-mat}
_Matériau exploité._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10605001 | Erze allgemein | minerais en général     |
|10605002 | Gold | or     |
|10605003 | Silber | argent     |
|10605004 | Kupfer, z.T. mit Silber, Wismut und Arsen | cuivre, partiellement avec argent, bismuth et arsenic     |
|10605005 | Eisen / Eisenoolith | fer / oolite ferrugineuse     |
|10605006 | Blei-Zink | plomb-zinc     |
|10605007 | Chrom-Nickel, z.T. mit Kobalt | chrome-nickel, partiellement avec cobalt     |
|10605008 | Mangan | manganèse     |
|10605009 | Molybdän und Wolfram | molybdène et tungstène     |
|10605010 | Antimon | antimoine     |
|10605011 | Baryt | barytine     |
|10605012 | Kalzit | calcite     |
|10605013 | Fluorit | fluorite     |
|10605014 | Quarz | quartz     |
|10605015 | Kaolin | kaolin     |
|10605016 | Magnesit | magnésite     |
|10605017 | Magnesium | magnésium     |
|10605018 | Phosphorit, Apatit | phosphorite, apatite     |
|10605019 | Talk | talc     |
|10605020 | Schwefel | soufre     |
|10605021 | Uran | uranium     |
|10605022 | Bohnerz | pisolites ferrugineuses     |
|10605023 | Asbest | asbeste / amiante     |
|10605024 | Kohle allgemein | charbon en général     |
|10605025 | Steinkohle / Anthrazit | houille / anthracite     |
|10605026 | Lignit | lignite     |
|10605027 | Graphit | graphite     |
|10605028 | Ölschiefer | schiste bitumineux     |
|10605029 | Asphalt / Bitumen | asphalte / bitume     |
|10605030 | Hartgestein | roche dure     |
|10605031 | Dachschiefer / Tafelschiefer | ardoise, schiste ardoisier     |
|10605032 | Serpentin | serpentine     |
|10605033 | Speckstein | stéatite     |
|10605034 | Gips | gypse     |
|10605035 | Salz / Steinsalz | sel / halite     |
|10605036 | Ton / Ton und Silt (Lehm) | argile / argile et silt (limon)     |
|10605037 | Sand | sable     |
|10605038 | Sand und Kies | sable et gravier     |
|10605039 | Pyrit | pyrite     |
|10605040 | Kies | gravier     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




## Classe Exploitation_Geomaterials_L (Aexp){#exploitation-geomaterials-l}
La classe [Exploitation_Geomaterials_L](#exploitation-geomaterials-l) contient les objets de
forme linéaire liés aux sites d’exploitation de matériaux
géologiques (p.ex. le front de taille).




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | []
**STATUS**                 | [CD](#exploitation-geomaterials-l-status)  | État de l&#39;exploitation | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10701001 | Abbaufront | front d&#39;exploitation     |
|10701002 | Bergwerksstollen | galerie de mine     |




#### Attribut  STATUS {#exploitation-geomaterials-l-status}
_État de l&#39;exploitation_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10702001 | in Betrieb | en exploitation     |
|10702002 | stillgelegt | abandonné     |
|10702003 | aufgefüllt | comblé     |
|10702004 | verfallen | effondré     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




## Classe Exploitation_Geomaterials_PLG (Aexp){#exploitation-geomaterials-plg}
La classe [Exploitation_Geomaterials_PLG](#exploitation-geomaterials-plg) contient les
surfaces d’exploitation de géomatériaux, telles qu’elles
étaient au moment du levé de la carte géologique.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | []
**EXP_UNIT**                 | [ Table ](#gc-geol-mapping-unit-cd)  | Unité lithostratigraphique exploitée | [1..*]
**STATUS**                 | [CD](#exploitation-geomaterials-plg-status)  | État de l&#39;exploitation | [0..1]
**DEPTH_TOT**                 | float                  | Profondeur totale du type d&#39;objet (en mètres depuis la surface) | [0..1]
**TARG_MAT**                 | [CD](#exploitation-geomaterials-plg-targ-mat)  | Matériel exploité | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10801001 | Steinbruch | carrière     |
|10801002 | Grube (Lockergesteinsabbau) | exploitation de matériaux meubles     |




#### Attribut  EXP_UNIT
_Unité lithostratigraphique exploitée_

Voir [GC_GEOL_MAPPING_UNIT_CD](#gc-geol-mapping-unit-cd) dans l'annexe





#### Attribut  STATUS {#exploitation-geomaterials-plg-status}
_État de l&#39;exploitation_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10802001 | in Betrieb | en exploitation     |
|10802002 | stillgelegt | abandonné     |
|10802003 | aufgefüllt | comblé     |
|10802004 | verfallen | effondré     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  DEPTH_TOT
_Profondeur totale du type d&#39;objet (en mètres depuis la surface)_

_Type de donnée :  float_





#### Attribut  TARG_MAT {#exploitation-geomaterials-plg-targ-mat}
_Matériel exploité._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10804001 | Ton / Ton und Silt (Lehm) | argile / argile et silt (limon)     |
|10804002 | Sand | sable     |
|10804003 | Sand und Kies | sable et gravier     |
|10804004 | Hartgestein | roche dure     |
|10804005 | Dachschiefer / Tafelschiefer | ardoise, schiste ardoisier     |
|10804006 | Gips | gypse     |
|10804007 | Serpentin | serpentine     |
|10804008 | Speckstein | stéatite     |
|10804009 | Talk | talc     |
|10804010 | Baryt | barite     |
|10804011 | Kalzit / Kalk | calcite / calcaire     |
|10804012 | Eisen / Eisenoolithe | fer / oolite ferrugineuse     |
|10804013 | Kaolin | kaolin     |
|10804014 | Quarz / Quarzit | quartz / quartzite     |
|10804015 | Asbest | asbeste / amiante     |
|10804016 | Bohnerz | pisolites ferrugineuses     |
|10804017 | Torf | tourbe     |
|10804018 | Mergel | marne     |
|10804019 | Kohle | charbon     |
|10804020 | Salz / Steinsalz | sel     |
|10804021 | Kies | gravier     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




## Classe Boreholes_PT (Abor){#boreholes-pt}
La classe [Boreholes_PT](#boreholes-pt) regroupe les forages et les sondages. (Sur les anciennes cartes imprimées, le genre d’objet n’était pas toujours distingué. D’ailleurs, il se peut que sur les anciennes cartes, les sondages par carottier battu aient été classés en tant que forages.)




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | []
**DEPTH_BEDR**                 | float                  | Profondeur de la roche en place (en mètres depuis la surface). Si l’ouvrage n’atteint pas la roche en place,  par exemple forage interrompu dans la couverture quaternaire, la valeur est  999, au cas où le forage commence déjà dans la roche en place la valeur est 0. Si la roche solide a été atteinte, mais qu&#39;il n&#39;est pas clair qu&#39;il s&#39;agit de la surface de la roche, la valeur est 888 | [0..1]
**D_C_UNDERG**                 | boolean                  | Forage réalisé à partir d’une galerie (oui / non)? | [1]
**MAIN_TAR**                 | [CD](#boreholes-pt-main-tar)  | But principal du sondage | [0..1]
**TARG_MAT**                 | [CD](#boreholes-pt-targ-mat)  | Matériau cible du sondage | [0..1]
**DEPTH_TOT**                 | float                  | Profondeur totale du type d&#39;objet (en mètres depuis la surface) | [0..1]
**DEPTH_FM_A**                 | [ Table ](#gc-geol-mapping-unit-cd)  | Profondeur relative à la formation A atteinte (en mètres depuis la surface) | [0..1]
**DEPTH_FM_B**                 | float                  | Profondeur de la formation B atteinte (en mètres depuis  la surface) | [0..1]
**FM_A**                 | [ Table ](#gc-geol-mapping-unit-cd)  | Unité lithostratigraphique de la formation A atteinte | [0..1]
**DEPTH_FM_B**                 | float                  | Profondeur de la formation B atteinte (en mètres depuis  la surface) | [0..1]
**DEPTH_WT**                 | float                  | Profondeur (m depuis la surface) de la nappe phréatique (valeur moyenne) | [0..1]
**AZIMUTH**                 | integer                  | Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le nord en degré de 0° à 359° dans le sens des aiguilles d&#39;une montre | [0..1]
**DIP**                 | integer                  | Valeur du plongement du type d&#39;objet (en degrés), mesurée de l’horizontale (0°) vers le bas jusqu’à la  verticale (90°) | [0..1]
**REF_NUMBER**                 | integer                  | Numéro de référence du type d&#39;objet dans un  document annexé (notice explicative,…) | [0..1]
**LITHO**                 | [ Table ](#gc-litho-unco-cd)  | Unité lithologique atteinte (dans le cas de forage atteignant le quaternaire) | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10501001 | Bohrung | forage     |
|10501002 | Sondierschlitz | fouille ou tranchée de reconnaissance     |
|10501003 | Handsondierung | sondage à la tarière     |
|10501004 | Rammsondierung | sondage au pénétromètre     |
|10501005 | Rammkernsondierung | sondage par carottier battu     |




#### Attribut  DEPTH_BEDR
_Profondeur de la roche en place (en mètres depuis la surface). Si l’ouvrage n’atteint pas la roche en place,  par exemple forage interrompu dans la couverture quaternaire, la valeur est  999, au cas où le forage commence déjà dans la roche en place la valeur est 0. Si la roche solide a été atteinte, mais qu&#39;il n&#39;est pas clair qu&#39;il s&#39;agit de la surface de la roche, la valeur est 888._

_Type de donnée :  float_





#### Attribut  D_C_UNDERG
_Forage réalisé à partir d’une galerie (oui / non)?_

_Type de donnée :  boolean_





#### Attribut  MAIN_TAR {#boreholes-pt-main-tar}
_But principal du sondage_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10505001 | Geotechnik | géotechnique     |
|10505002 | Hydrogeologie | hydrogéologique     |
|10505004 | mineralische Rohstoffe | matières premières minérales     |
|10505005 | Kohlenwasserstoffe | hydrocarbures     |
|10505006 | belasteter Standort | site pollué     |
|10505007 | Seismik | sismique     |
|10505008 | Geothermie | géothermique     |
|10505012 | Forschung | recherche     |
|10505013 | Naturgefahren | dangers naturels     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  TARG_MAT {#boreholes-pt-targ-mat}
_Matériau cible du sondage_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10506001 | Salz / Steinsalz | sel / halite     |
|10506002 | Erdöl | pétrole     |
|10506003 | Erdgas | gaz naturel     |
|10506004 | Erdwärme | energie géothermique     |
|10506005 | Thermalwasser | eau thermale     |
|10506006 | Grundwasser | eau souterraine     |
|10506007 | Mineralwasser | eau minérale     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  DEPTH_TOT
_Profondeur totale du type d&#39;objet (en mètres depuis la surface)_

_Type de donnée :  float_





#### Attribut  DEPTH_FM_A
_Profondeur relative à la formation A atteinte (en mètres depuis la surface)_

Voir [GC_GEOL_MAPPING_UNIT_CD](#gc-geol-mapping-unit-cd) dans l'annexe





#### Attribut  DEPTH_FM_B
_Profondeur de la formation B atteinte (en mètres depuis  la surface)_

_Type de donnée :  float_





#### Attribut  FM_A
_Unité lithostratigraphique de la formation A atteinte_

Voir [GC_GEOL_MAPPING_UNIT_CD](#gc-geol-mapping-unit-cd) dans l'annexe





#### Attribut  DEPTH_FM_B
_Profondeur de la formation B atteinte (en mètres depuis  la surface)_

_Type de donnée :  float_





#### Attribut  DEPTH_WT
_Profondeur (m depuis la surface) de la nappe phréatique (valeur moyenne)_

_Type de donnée :  float_





#### Attribut  AZIMUTH
_Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le nord en degré de 0° à 359° dans le sens des aiguilles d&#39;une montre._

_Type de donnée :  integer_





#### Attribut  DIP
_Valeur du plongement du type d&#39;objet (en degrés), mesurée de l’horizontale (0°) vers le bas jusqu’à la  verticale (90°)_

_Type de donnée :  integer_





#### Attribut  REF_NUMBER
_Numéro de référence du type d&#39;objet dans un  document annexé (notice explicative,…)_

_Type de donnée :  integer_





#### Attribut  LITHO
_Unité lithologique atteinte (dans le cas de forage atteignant le quaternaire)_

Voir [GC_LITHO_UNCO_CD](#gc-litho-unco-cd) dans l'annexe





## Classe Artificial_Surface_Modifications_PLG (Aart){#artificial-surface-modifications-plg}
La classe [Artificial_Surface_Modifications_PLG](#artificial-surface-modifications-plg) contient des
modifications artificielles importantes du terrain (terrain
de golf, domaine skiable, etc.) qui ont pour conséquence que
le relief original n&#39;est plus reconnaissable, ce qui
pourrait conduire à des conclusions erronées lors d&#39;une
interprétation géomorphologique.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10401001 | künstlich verändertes Gelände | terrain modelé artificiellement     |
|10401002 | künstliche Ablagerung, undifferenziert | dépôts artificiels, indifférenciés     |
|10401003 | Aufschüttung, Damm | remblai, digue     |
|10401004 | Auffüllung | remplissage     |
|10401005 | Deponie | décharge     |
|10401006 | Halde | terril     |








# Thème HYDROGEOLOGY

## Classe Construction_PT (Hcon){#construction-pt}
Dans la classe [Construction_PT](#construction-pt) se trouvent les constructions
hydriques, comme les captages dans la nappe phréatique et
les citernes. Les instruments de mesure comme les
piézomètres et les limnigraphes appartiennent également à
cette classe.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**STATUS**                 | [CD](#construction-pt-status)  | État du type d&#39;objet | [0..1]
**EPOCH**                 | [CD](#construction-pt-epoch)  | Époque de construction du type d&#39;objet | [0..1]
**DEPTH**                 | float                  | Profondeur du type d&#39;objet | [0..1]
**DEPTH_WT**                 | float                  | Profondeur (m depuis la surface) de la nappe phréatique (valeur moyenne) | [0..1]
**MEA_PERIOD**                 | range                  | Période de mesure de la profondeur du niveau hydrostatique | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12101001 | Grundwasserfassung | captage dans la nappe phréatique     |
|12101002 | Zisterne | citerne     |
|12101003 | laufender Brunnen (in wasserarmem Gebiet) | fontaine (en région sèche)     |
|12101004 | Sodbrunnen | puits     |
|12101005 | Versickerungsschacht | puits d´infiltration     |
|12101006 | Limnigraph | limnigraphe     |
|12101007 | Piezometer | piézomètre     |




#### Attribut  STATUS {#construction-pt-status}
_État du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12102001 | in Betrieb | en activité     |
|12102002 | stillgelegt | abandonné     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  EPOCH {#construction-pt-epoch}
_Époque de construction du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12103001 | Mittelalter | Moyen Âge     |
|12103002 | Römerzeit | époque romaine     |
|12103003 | prähistorisch | préhistorique     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  DEPTH
_Profondeur du type d&#39;objet_

_Type de donnée :  float_





#### Attribut  DEPTH_WT
_Profondeur (m depuis la surface) de la nappe phréatique (valeur moyenne)_

_Type de donnée :  float_





#### Attribut  MEA_PERIOD
_Période de mesure de la profondeur du niveau hydrostatique_

_Type de donnée :  range_





## Classe Construction_L (Hcon){#construction-l}
Dans la classe [Construction_L](#construction-l) se trouvent les constructions
hydriques de forme linéaire comme les galeries de captage
d’eau, qui peuvent être combinées avec les types d’objets de
la classe Surface_Water_PT.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**COMBI**                 | [CD](#construction-l-combi)  | Type d’objet d&#39;une autre classe avec lequel le type d’objet peut être combiné | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12201001 | Wasserfassungsstollen | galerie de captage d´eau     |
|12201002 | künstlicher Gewässerlauf | écoulement artificiel     |




#### Attribut  COMBI {#construction-l-combi}
_Type d’objet d&#39;une autre classe avec lequel le type d’objet peut être combiné_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12202001 | mit Quellfassung (orientiert) in Stollen | avec captage (orienté) en galerie     |
|12202002 | mit gefasster Mineralquelle (orientiert) in Stollen | avec source minérale (orientée) captée en galerie     |
|12202003 | mit gefasster Thermalquelle (orientiert) in Stollen | avec source thermale (orientée) captée en galerie     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




## Classe Palaeohydrology_L (Hpal){#palaeohydrology-l}
La classe [Palaeohydrology_L](#palaeohydrology-l) contient tous les types d’objets
de forme linéaire, indiquant le tracé d’un cours d’eau dans
le passé.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**REL_AGE**                 | [CD](#palaeohydrology-l-rel-age)  | Age relatif du type d&#39;objet | [0..1]
**CHRONO**                 | [ Table ](#gc-chrono-cd)  | Attribution chronostratigraphique | [0..1]
**REF_YEAR**                 | integer                  | Année de référence de l’ancienne ligne de rivage | [1]
**SOURCE**                 | string                  | Source des données déduites à partir de données historiques | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12301001 | Paläotal | axe de paléovallée     |
|12301002 | ehemalige Entwässerungsrinne | ancien chenal     |
|12301004 | Trockental | vallée sèche     |
|12301005 | ehemaliges Bachbett | ancien lit de cours d&#39;eau (ruisseau)     |
|12301006 | Ufer eines ehemaligen Flussbetts | rive d&#39;un ancien lit de cours d&#39;eau     |
|12301007 | ehemalige Uferlinie | ancienne ligne de rivage     |
|12301003 | ehemalige glaziale Abflussrinne | axe d&#39;un ancien effluent glaciaire     |




#### Attribut  REL_AGE {#palaeohydrology-l-rel-age}
_Age relatif du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12302001 | die Jüngste oder Einzige | la plus récente ou la seule     |
|12302002 | älter als die Jüngste | plus ancienne que la plus récente     |
|12302003 | älter als die Zweitjüngste | plus ancienne que la deuxième plus récente     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  CHRONO
_Attribution chronostratigraphique_

Voir [GC_CHRONO_CD](#gc-chrono-cd) dans l'annexe





#### Attribut  REF_YEAR
_Année de référence de l’ancienne ligne de rivage._

_Type de donnée :  integer_





#### Attribut  SOURCE
_Source des données déduites à partir de données historiques_

_Type de donnée :  string_





## Classe Subsurface_Water_L (Hsub){#subsurface-water-l}
Dans la classe [Subsurface_Water_L](#subsurface-water-l) se trouvent les objets de
forme linéaire qui représentent les cours d’eau souterrains.
Le parcours exact des cours d’eau souterrains est presque
toujours supposé. Il est déduit à partir de quelques données
d’études de systèmes de captage. Les essais de traçage
seront mentionnées dans la notice explicative, lorsqu’elle
existe. Les cours d’eau souterrains peuvent être combinés
avec les objets de la classe Surface_Water_PT.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**COMBI**                 | [CD](#subsurface-water-l-combi)  | Type d’objet d&#39;une autre classe avec lequel le type d’objet peut être combiné | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12401001 | unterirdischer Gewässerlauf | écoulement souterrain     |




#### Attribut  COMBI {#subsurface-water-l-combi}
_Type d’objet d&#39;une autre classe avec lequel le type d’objet peut être combiné_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12402001 | mit Versickerungsstelle eines Baches | avec perte d&#39;un cours d&#39;eau     |
|12402002 | mit Wiederaustritt eines unterirdischen Bachlaufes | avec résurgence d&#39;une rivière souterraine     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




## Classe Surface_Water_PT (Hsur){#surface-water-pt}
La classe [Surface_Water_PT](#surface-water-pt) comprend les eaux de surface
locales (ponctuelles) comme les sources et les pertes d’un
cours d’eau. On y trouve également des types d’objets
particuliers comme les cascades et les rapides, lesquels
marquent des positions spécifiques du cours d’eau qui sont à
relier avec la géologie sous-jacente. Une source est décrite
comme «source thermale» lorsque l’eau y atteint une
température annuelle moyenne ≥ 20°C. L’attribut «Temp» est
associé à ce type de source et se limite en règle générale à
la température moyenne de l’eau. Par conséquent aucune
donnée d’analyse chimique n’est indiquée pour cet attribut.
Par «source minérale», on entend une source avec une
concentration minérale dans l’eau ≥ 1g / l ou une
concentration en CO2 ≥ 250 mg / l. L’attribut «Chemistry»
est associé à ce type de source. Il indique l’élément
caractéristique principal de l’eau minérale et non le
chimisme complet de l’eau




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**STATUS**                 | [CD](#surface-water-pt-status)  | État du type d&#39;objet | [0..1]
**FLOW_CON**                 | [CD](#surface-water-pt-flow-con)  | Condition d’écoulement | [0..1]
**TYPE**                 | [CD](#surface-water-pt-type)  | Caractéristique du type d&#39;objet | [0..1]
**DIS_LOCA**                 | [CD](#surface-water-pt-dis-loca)  | Lieu d’écoulement | [0..1]
**COMBI**                 | [CD](#surface-water-pt-combi)  | Type d’objet d&#39;une autre classe avec lequel le type  d’objet peut être combiné | [0..1]
**TEMP**                 | integer                  | Température moyenne (°C) de l&#39;eau | [0..1]
**CHEMISTRY**                 | string                  | Element chimique caractéristique dans l’eau minérale | [0..1]
**AZIMUTH**                 | integer                  | Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles  d&#39;une montre | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12501001 | Quelle | source     |
|12501002 | diffuse Quelle | source diffuse     |
|12501003 | Wiederaustritt eines unterirdischen Bachlaufes | résurgence d&#39;une rivière souterraine     |
|12501004 | Versickerungsstelle eines Baches | perte d´un cours d´eau     |
|12501005 | Steilstufe in Bachrinne, Wasserfall | rapide d&#39;un cours d&#39;eau, cascade     |
|12501006 | Grundwasseraufstoss | résurgence des eaux souterraines     |




#### Attribut  STATUS {#surface-water-pt-status}
_État du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12502001 | gefasst | captée     |
|12502002 | nicht gefasst | non captée     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  FLOW_CON {#surface-water-pt-flow-con}
_Condition d’écoulement_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12503001 | perennierend | pérenne     |
|12503002 | temporär | temporaire     |
|12503003 | versiegt | tarie     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  TYPE {#surface-water-pt-type}
_Caractéristique du type d&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12504001 | Karstquelle | karstique     |
|12504002 | Mineralquelle | minérale     |
|12504003 | Thermalquelle | thermale     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  DIS_LOCA {#surface-water-pt-dis-loca}
_Lieu d’écoulement_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12505002 | in Stollen | en galerie     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  COMBI {#surface-water-pt-combi}
_Type d’objet d&#39;une autre classe avec lequel le type  d’objet peut être combiné_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12506001 | mit Wasserfassungsstollen | avec galerie de captage d&#39;eau     |
|12506002 | mit unterirdischem Gewässerlauf | avec écoulement souterrain     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  TEMP
_Température moyenne (°C) de l&#39;eau_

_Type de donnée :  integer_





#### Attribut  CHEMISTRY
_Element chimique caractéristique dans l’eau minérale_

_Type de donnée :  string_





#### Attribut  AZIMUTH
_Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles  d&#39;une montre_

_Type de donnée :  integer_





## Classe Surface_Water_L (Hsur){#surface-water-l}
Dans la classe [Surface_Water_L](#surface-water-l) sont décrit les niveaux de
sources (de forme linéaire)




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12601001 | Quellhorizont | niveau de sources, déversement de la nappe phréatique     |
|12601002 | Bachlauf | ruisseau     |




## Classe Surface_Water_PLG (Hsur){#surface-water-plg}
La classe [Surface_Water_PLG](#surface-water-plg) regroupe toutes les
accumulations d’eaux superficielles comme les glaciers, les
lacs et les rivières qui masquent les unités géologiques
sous-jacentes. Le modèle complet du réseau hydrique ne fait
pas partie du Modèle de données géologiques.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12701001 | Gletscher | glacier     |
|12701002 | See | lac     |
|12701003 | Fluss | rivière     |





# Annexes


\blandscape


## Annexe  GC_GEOL_MAPPING_UNIT_ATT {#gc-geol-mapping-unit-att}
Unités de cartographie



| Code    |  GMU      |Litho main | Litho sec | Litho ter |  Formation | Chrono top | Chrono base | Correlation |
|---------|-----------|-----------|-----------|------------|------------|-------------|-------------|
|15202091 |Formation de l&#39;Öhrli | Kalkstein: Bioklasten-Ooide  | Kalkstein: sandig   | Mergelstein |  Öhrli-Formation |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202092 |Formation de Palfris | Mergelstein: schiefrig  | Tonstein: schiefrig   | Kalkstein: Bioklasten |  Palfris-Formation |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202093 |Formation du Zementstein | Mergelstein  | Kalkstein: mergelig   | Kalkstein: mikritisch |  15253121 |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202094 |Membre du Graspass | Brekzie: kalkig  | Brekzie: dolomitisch   | Mergelstein |  Graspass-Member |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202095 |Calcaire du Gassen(stock) | Kalkstein: arenitisch-spätig  | Kalkstein: mikritisch   | – |  Gassen-Kalk |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202096 |Malm de l&#39;Helvétique | Kalkstein  | Mergelstein   | – |  – |  Berriasien     | Callovien   | Malm  |
|15202097 |Formation de Quinten | Kalkstein: mikritisch  | –   | – |  Quinten-Formation |  Berriasien     | Oxfordien   | Malm  |
|15202098 |Calcaire de Tros | Kalkstein: Korallen  | Kalkstein: Ooide   | – |  Tros-Kalk |  Berriasien     | Tithonien   | Malm  |
|15202099 |Mergelband (Fm. de Quinten) | Mergelstein  | Kalkstein: mergelig   | – |  «Mergelband» (Quinten-Fm.) |  Kimméridgien     | Kimméridgien   | Malm  |
|15202100 |Formation du Schilt | Kalkstein  | Mergelstein   | – |  Schilt-Formation |  Oxfordien     | Callovien   | Malm  |
|15202101 |Membre de Mürtschen | Mergelstein: schiefrig  | Kalkstein: mikritisch   | – |  Mürtschen-Member |  Oxfordien     | Oxfordien   | Malm  |
|15202102 |Marne du Schilt | Mergelstein: schiefrig  | Mergelstein: kalkig   | – |  Schilt-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15202103 |Calcaire du Schilt | Kalkstein  | –   | – |  Schilt-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15202104 |Membre du Seeztal | Siltstein: mergelig  | Kalkstein: spätig: Bioklasten   | – |  Seeztal-Member |  Oxfordien     | Callovien   | Malm  |
|15202105 |Membre des Windgällen | Kalkstein: mergelig  | Tonstein   | – |  Windgällen-Member |  Oxfordien     | Oxfordien   | Malm  |
|15202106 |Dogger de l&#39;Helvétique | Kalkstein  | Mergelstein   | Sandstein |  – |  Oxfordien     | Toarcien   | Syn-Rift  |
|15202107 |Formation de l&#39;Erzegg | Tonstein: schiefrig  | Mergelstein: schiefrig   | – |  Erzegg-Formation |  Oxfordien     | Bajocien   | Lias-Dogger in pelagischer Fazies  |
|15202108 |Formation de la Reischiben | Kalkstein: spätig: Bioklasten-Chert  | Kalkstein: sandig   | Kalkstein: mergelig |  Reischiben-Formation |  Bathonien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15202109 |Oolite ferrugineuse de la Blegi | Kalkstein: Eisenooide  | –   | – |  Blegi-Eisenoolith |  Callovien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15202110 |Conglomérat de la Bannalp | Mergelstein: dolomitisch  | Konglomerat   | – |  Bannalp-Konglomerat |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15202111 |Horizon fossilifère de Guppen | Kalkstein: Bioklasten  | –   | – |  Guppen-Fossilhorizont |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15202112 |Horizon fossilifère du Gursbach | Kalkstein: Bioklasten  | –   | – |  Gursbach-Fossilhorizont |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15202113 |Formation du Hochstollen | Kalkstein: sandig-spätig  | Mergelstein: sandig   | – |  Hochstollen-Formation |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15202114 |Membre du Schwarzhorn | Kalkstein: sandig-kieselig  | Mergelstein   | Kalkstein: spätig: Bioklasten |  Schwarzhorn-Member |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15202115 |Membre du Bietenhorn | Mergelstein: siltig  | Tonstein: schiefrig   | Kalkstein: sandig |  Bietenhorn-Member |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15202116 |Formation du Bommerstein | Sandstein: Quarz  | Kalkstein: spätig: Bioklasten   | Tonstein: schiefrig |  Bommerstein-Formation |  Aalénien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15202117 |Membre de Mols | Tonstein: schiefrig  | Kalkstein: spätig: Bioklasten   | – |  Mols-Member |  Aalénien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15202118 |Formation de Dugny | Tonstein: siltig: Glimmer  | Siltstein   | – |  Dugny-Formation |  Aalénien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15202119 |Formation du Coroi | Tonstein: schiefrig  | Siltstein   | Sandstein |  Coroi-Formation |  Aalénien     | Aalénien   | Syn-Rift  |
|15202120 |Lias de l&#39;Helvétique | Mergelstein  | Kalkstein   | Sandstein |  – |  Aalénien     | Rhétien   | Lias-Dogger in neritischer Fazies  |
|15202121 |Formation du Brunnistock | Kalkstein: sandig-spätig  | Tonstein   | – |  Brunnistock-Formation |  Toarcien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202122 |Formation d&#39;Inferno | Kalkstein: mergelig-schiefrig  | Tonstein: schiefrig   | Kalkstein: spätig: Bioklasten |  Inferno-Formation |  Toarcien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202123 |Formation des Monts Rosset | Mergelstein  | Kalkstein: spätig: Bioklasten   | – |  Monts-Rosset-Formation |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15202124 |Membre de la Torrentalp | Sandstein: kalkig-kieselig  | Kalkstein: mergelig   | Tonstein |  Torrentalp-Member |  Aalénien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202125 |Formation du Sexmor | Kalkstein: spätig: Bioklasten  | Mergelstein   | Kalkstein: kieselig |  Sexmor-Formation |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202126 |Formation du Mont Joly | Kalkstein: kieselig  | Kalkstein: spätig: Bioklasten   | Kalkstein: sandig-tonig |  Mont-Joly-Formation |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202127 |Membre de Galm | Sandstein: kalkig-kieselig  | Kalkstein: sandig-spätig   | – |  Galm-Member |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202128 |Formation du Spitzmeilen | Kalkstein: sandig  | Sandstein: kalkig   | Mergelstein |  Spitzmeilen-Formation |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202129 |Formation des Tierces | Mergelstein  | Kalkstein: mikritisch   | Kalkstein: sandig-spätig |  Tierces-Formation |  Sinémurien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15202130 |Formation de la Bachalp | Mergelstein: kalkig  | Kalkstein: spätig   | – |  Bachalp-Formation |  Sinémurien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15202131 |Formation du Prodkamm | Tonstein  | Mergelstein   | Sandstein: kalkig |  Prodkamm-Formation |  Sinémurien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15202132 |Membre à Cardinia | Tonstein: schiefrig  | Sandstein: kalkig   | Kalkstein: Bioklasten |  «Cardinia-Member» |  Sinémurien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15202133 |Formation du Stgir | Kalkstein: sandig  | Tonstein: schiefrig   | Sandstein: Quarz |  Stgir-Formation |  Sinémurien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15202134 |Trias de l&#39;Helvétique | Dolomitstein  | Sandstein   | Gestein: pelitisch |  – |  Rhétien     | Olénékien   | Prä-Rift  |
|15202135 |Formation des Besoëns | Sandstein: Quarz  | Kalkstein: sandig: Bioklasten   | Tonstein: schiefrig |  Besoëns-Formation |  Rhétien     | Rhétien   | «Rhät»  |
|15202136 |Formation de Quarten | Tonstein: schiefrig  | Siltstein: schiefrig   | Dolomitstein |  Quarten-Formation |  Trias tardif     | Trias tardif   | Keuper  |
|15202137 |Formation des Arandellys | Kalkstein: dolomitisch  | Dolomitstein   | Rauwacke |  Arandellys-Formation |  Trias tardif     | Trias moyen   | Muschelkalk  |
|15202138 |Membre de la Griaz | Evaporit: Gips  | Rauwacke   | – |  Griaz-Member |  Trias tardif     | Trias tardif   | Muschelkalk  |
|15202139 |Formation de la Röti | Dolomitstein  | Rauwacke   | Tonstein: dolomitisch |  Röti-Formation |  Carnien     | Anisien   | Muschelkalk  |
|15202140 |Formation du Vieux Emosson | Sandstein: Quarz  | Sandstein: Feldspat   | Tonstein |  Vieux-Emosson-Formation |  Anisien     | Olénékien   | Buntsandstein  |
|15202141 |Formation de Mels | Sandstein: Quarz  | Tonstein: schiefrig   | Dolomitstein |  Mels-Formation |  Anisien     | Olénékien   | Buntsandstein  |
|15202142 |Permo-Carbonifère de l&#39;Helvétique | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Permien     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15202143 |Groupe du Verrucano | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15202144 |Verrucano de Glaris | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Lopingien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202145 |Formation de Schönbüel | Tonstein: sandig-schiefrig  | Sandstein: Quarz   | – |  Schönbühl-Formation |  Lopingien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202146 |Quartzite de Schönbüel | Sandstein: Quarz  | –   | – |  Schönbühl-Formation |  Lopingien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202147 |Formation du Kärpf | Konglomerat  | Sandstein   | Tonstein: siltig-schiefrig |  Kärpf-Formation |  Lopingien     | Guadalupien   | Spät- bis postvariszisches Grundgebirge  |
|15202148 |Formation du Karrenstock | Tonstein: sandig-schiefrig  | Gestein: vulkanisch   | Sandstein: konglomeratisch |  Karrenstock-Formation |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202149 |Membre de la Chartegg | Tonstein: siltig-schiefrig  | –   | – |  Chartegg-Member |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202150 |Membre du Fuggstock | Konglomerat  | –   | – |  Fuggstock-Member |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202151 |Formation de la Mären(egg) | Tonstein: siltig-schiefrig  | Brekzie   | Sandstein |  Mären-Formation |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202217 |Granite du Montenvers | Granit  | Granit: mylonitisch   | – |  Montenvers-Granit |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202218 |Orthogneiss de Lognan | Gneis: augig  | Gneis: gebändert   | – |  Lognan-Orthogneis |  Ordovicien     | Ordovicien   | Prävariszisches Grundgebirge  |
|15202219 |Orthogneiss des Pétoudes | Gneis: magmatisch  | –   | – |  Pétoudes-Orthogneis |  Ordovicien     | Ordovicien   | Prävariszisches Grundgebirge  |
|15202220 |Groupe de Pesciora | Gestein: plutonisch  | –   | – |  – |  Cisuralien     | Cisuralien   | Postvariszisches Grundgebirge  |
|15202221 |Granite du Rotondo | Granit: Biotit-Granat  | –   | – |  Rotondo-Granit |  Sakmarien     | Sakmarien   | Postvariszisches Grundgebirge  |
|15202222 |Granite de la Cacciola | Granit: Biotit-Muskovit  | –   | – |  Cacciola-Granit |  Cisuralien     | Cisuralien   | Postvariszisches Grundgebirge  |
|15202223 |Diorite du Sädelhorn | Diorit  | –   | – |  Sädelhorn-Diorit |  Cisuralien     | Cisuralien   | Postvariszisches Grundgebirge  |
|15202224 |Granite du Winterhorn | Granit: aplitisch: Granat  | –   | – |  Winterhorn-Granit |  Cisuralien     | Cisuralien   | Postvariszisches Grundgebirge  |
|15202225 |Groupe du Val Lavaz | Gestein: plutonisch  | –   | – |  – |  Cisuralien     | Pennsylvanien   | Spätvariszisches Grundgebirge  |
|15202226 |Granite de Medel | Granit: porphyrisch  | Gneis: granitisch   | – |  Medel-Granit |  Cisuralien     | Cisuralien   | Spätvariszisches Grundgebirge  |
|15202227 |Granodiorite de Cristallina | Granodiorit  | –   | – |  Cristallina-Granodiorit |  Cisuralien     | Pennsylvanien   | Spätvariszisches Grundgebirge  |
|15202228 |Granite du Gamsboden | Granit: Biotit-Muskovit  | Gneis: augig   | – |  Gamsboden-Granit |  Cisuralien     | Pennsylvanien   | Spätvariszisches Grundgebirge  |
|15202229 |Diorite du Val Uffiern | Diorit: Biotit-Hornblende  | –   | – |  Uffiern-Diorit |  Cisuralien     | Pennsylvanien   | Spätvariszisches Grundgebirge  |
|15202230 |Granite de la Fibbia | Granit: Biotit-Muskovit  | Gneis: augig   | – |  Fibbia-Granit |  Cisuralien     | Pennsylvanien   | Spätvariszisches Grundgebirge  |
|15202231 |Groupe du Val Rondadura | Gneis: sedimentär  | Schiefer   | – |  – |  Paléozoïque     | Paléozoïque   | Prä- bis frühvariszisches Grundgebirge  |
|15202232 |Complexe gneissique du Piz Borel | Schiefer: Glimmer-Hornblende  | –   | – |  Borel-Gneiskomplex |  Paléozoïque     | Paléozoïque   | Prä- bis frühvariszisches Grundgebirge  |
|15202233 |Complexe gneissique du Piz Tenelin | Schiefer: Hornblende  | Gneis: Hornblende   | Amphibolit: Granat |  Tenelin-Gneiskomplex |  Paléozoïque     | Paléozoïque   | Prä- bis frühvariszisches Grundgebirge  |
|15202234 |Complexe gneissique des Laiets | Gneis  | Schiefer: Glimmer   | – |  Laiets-Gneiskomplex |  Paléozoïque     | Paléozoïque   | Prä- bis frühvariszisches Grundgebirge  |
|15202235 |Complexe gneissique de la Tremola | Gneis: Hornblende  | Schiefer: Hornblende-Granat   | Amphibolit |  Tremola-Gneiskomplex |  Paléozoïque     | Paléozoïque   | Prä- bis frühvariszisches Grundgebirge  |
|15202236 |Complexe gneissique de Pontino | Schiefer: Glimmer-Hornblende  | Gneis: schiefrig: Hornblende   | Amphibolit |  Pontino-Gneiskomplex |  Paléozoïque     | Paléozoïque   | Prä- bis frühvariszisches Grundgebirge  |
|15202237 |Complexe gneissique de Nelva | Gneis  | Schiefer: Glimmer-Granat   | Schiefer: Hornblende |  Nelva-Gneiskomplex |  Paléozoïque     | Paléozoïque   | Prä- bis frühvariszisches Grundgebirge  |
|15202238 |Complexe gneissique du Sasso Rosso | Schiefer: Glimmer  | Gneis: schiefrig: Chlorit   | Schiefer: Hornblende |  Sasso-Rosso-Gneiskomplex |  Paléozoïque     | Paléozoïque   | Prä- bis frühvariszisches Grundgebirge  |
|15202239 |Complexe gneissique de Prüsfa | Gneis: Granat  | Quarzit   | Rhyolith |  Prüsfa-Gneiskomplex |  Paléozoïque     | Paléozoïque   | Prä- bis frühvariszisches Grundgebirge  |
|15202240 |Complexe du Streifengneiss | Gneis: granitisch  | Gneis: Biotit-Muskovit   | – |  Streifengneis-Komplex |  Llandoveryien     | Spätes Ordovizium   | Prävariszisches Grundgebirge  |
|15202241 |Métagabbro du Chastelhorn | Amphibolit: Granat  | Gabbro   | – |  Chastelhorn-Metagabbro |  Mittleres Ordovizium     | Frühes Ordovizium   | Prävariszisches Grundgebirge  |
|15202242 |Gneiss de la Gurschen(alp) | Gneis  | Schiefer   | Gneis: migmatitisch |  Gurschen-Gneis |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202243 |Gneiss de la Guspis | Gneis  | Schiefer   | Gneis: migmatitisch |  Guspis-Gneis |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202244 |Gneiss de Sorescia | Gneis  | Gneis: migmatitisch   | – |  Sorescia-Gneis |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202246 |roches granitiques | Granit  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15202247 |roches volcaniques et subvolcaniques acides | Gestein: saur-vulkanisch  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15202255 |Cristallin à altération permienne | Gestein: residual  | Gneis   | – |  – |  Permien     | Permien   | Grundgebirge  |
|15202256 |Formation de Goltschenried | Schiefer: Graphit  | Gneis   | – |  Goltschenried-Formation |  Cisuralien     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202263 |Granite d&#39;Engi | Granit: porphyrisch  | –   | – |  Engi-Granit |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202264 |Complexe gneissique de Calmut | Gneis: migmatitisch  | –   | – |  Calmut-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202265 |Complexe gneissique du Val Pigniu | Gneis  | –   | – |  Val-Pigniu-Gneiskomplex |  Protérozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202266 |Permo-Carbonifère de la zone d&#39;Urseren-Garvera | Sandstein  | Konglomerat   | Gestein: pelitisch |  – |  Permien     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15202267 |Complexe gneissique de Goms | Gneis  | Migmatit   | Amphibolit |  Goms-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202271 |Granite du (Monte) Prosa | Granit: Biotit-Granat  | –   | – |  Prosa-Granit |  Cisuralien     | Cisuralien   | Postvariszisches Grundgebirge  |
|15202272 |Granite du Val Tremola | Granit: aplitisch  | –   | – |  Val-Tremola-Granit |  Cisuralien     | Cisuralien   | Postvariszisches Grundgebirge  |
|15202273 |Gneiss de la Leventina | Gneis: Biotit-Muskovit  | Granit: porphyrisch   | – |  Leventina-Gneis |  Cisuralien     | Mississippien   | Grundgebirge  |
|15202274 |Orthogneiss de la nappe du Lukmanier | Gneis: magmatisch  | –   | – |  – |  Cisuralien     | Carbonifère   | Grundgebirge  |
|15202275 |Paragneiss de la nappe du Lukmanier | Gneis: sedimentär  | –   | – |  – |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15202276 |Marbre du Val Stgira | Kalkstein: Korallen  | –   | – |  Val-Stgira-Riffmarmor |  Jurassique précoce     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15202277 |Fossilmarmor | Marmor: sandig: Bioklasten  | –   | – |  – |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202278 |Trias de Fanee | Dolomitstein  | Kalkstein   | Sandstein: Quarz |  – |  Trias tardif     | Trias précoce   | Sedimentbedeckung  |
|15202279 |Unités de flysch ultrahelvétiques | Sandstein  | Mergelstein   | Kalkstein |  – |  Eocène     | Eocène   | Flysch  |
|15202281 |Formation de Martinsmad | Mergelstein: kalkig  | Kalkstein: kieselig   | Sandstein: Quarz |  Martinsmad-Formation |  Yprésien     | Maastrichtien   | Flysch  |
|15202282 |Obere Flyschabfolge (Sardona) | Kalkstein: sandig: Bioklasten  | Sandstein: kalkig   | Tonstein: schiefrig |  «Supraquarzitischer Flysch» (Martinsmad-Fm.) |  Bartonien     | Lutétien   | Flysch  |
|15202283 |Quartzite du Sardona | Sandstein: Quarz  | –   | – |  Sardona-Member |  Yprésien     | Thanétien   | Flysch  |
|15202284 |Untere Flyschabfolge (Sardona) | Kalkstein: sandig: Glimmer  | Kalkstein: mergelig   | Tonstein: schiefrig |  «Infraquarzitischer Flysch» (Martinsmad-Fm.) |  Danien     | Maastrichtien   | Flysch  |
|15202285 |Formation du Meilleret | Konglomerat  | Tonstein: schiefrig   | Kalkstein: Bioklasten |  Meilleret-Formation |  Priabonien     | Lutétien   | Flysch  |
|15202286 |Grès de Lavtina | Sandstein: kalkig: Glimmer  | Tonstein: schiefrig   | – |  Lavtina-Sandstein |  Priabonien     | Eocène moyen   | Flysch  |
|15202287 |Grès du Blattengrat | Sandstein: Glimmer  | Mergelstein: schiefrig   | Kalkstein: kieselig |  Blattengrat-Sandstein |  Priabonien     | Priabonien   | Flysch  |
|15202288 |Grès de Burg | Kalkstein: sandig  | Sandstein: kalkig   | Mergelstein |  Burg-Sandstein |  Priabonien     | Priabonien   | Flysch  |
|15202289 |Grès du Val-d&#39;Illiez | Sandstein: tonig  | –   | – |  Val-d&#39;Illiez-Sandstein |  Rupélien     | Priabonien   | Flysch  |
|15202290 |Formation du Muot da Rubi | Mergelstein: siltig-schiefrig  | Sandstein: tonig   | – |  Muot-da-Rubi-Formation |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202291 |Membre du Ahornen | Sandstein: tonig: Lithoklasten  | Mergelstein   | – |  Ahornen-Member |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202292 |Membre du Kistenstöckli | Konglomerat  | Kalkstein: sandig: Glimmer   | Mergelstein: sandig |  Kistenstöckli-Member |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202293 |Membre du Ghölzwald | Kalkstein: sandig: Glimmer  | Sandstein: kalkig: Glimmer   | – |  Ghölzwald-Member |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202294 |Membre du Malor | Mergelstein  | Sandstein: Glimmer   | – |  Malor-Member |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202295 |Membre du Südelbach | Mergelstein  | Kalkstein: siltig   | Brekzie: polymikt |  Südelgrabe-Melange |  Priabonien     | Priabonien   | Mélange  |
|15202296 |Conglomérat du Kleintal | Konglomerat: kalkig  | –   | – |  Kleintal-Konglomerat |  Priabonien     | Lutétien   | Syn-Kollision  |
|15202297 |Conglomérat de Rütenen | Konglomerat  | Mergelstein   | – |  Rütenen-Konglomerat |  Priabonien     | Lutétien   | Syn-Kollision  |
|15202298 |Jurassique de l&#39;Helvétique | Kalkstein  | Mergelstein   | Sandstein |  – |  Berriasien     | Rhétien   | Sedimentbedeckung  |
|15202299 |Brèche de Wang | Brekzie  | –   | – |  «Wang-Brekzie» |  Maastrichtien     | Maastrichtien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202300 |«Oberer Schrattenkalk» | Kalkstein: mikritisch: Bioklasten  | –   | – |  «Oberer Schrattenkalk» |  Aptien     | Aptien   | «Urgonien»  |
|15202301 |«Unterer Schrattenkalk» | Kalkstein: mikritisch: Bioklasten  | –   | – |  «Unterer Schrattenkalk» |  Aptien     | Barrémien   | «Urgonien»  |
|15202302 |«Oberer Quinten-Kalk» | Kalkstein: mikritisch  | –   | – |  «Oberer Quintner Kalk» |  Berriasien     | Tithonien   | Malm  |
|15202303 |«Unterer Quinten-Kalk» | Kalkstein: mikritisch: Chert  | –   | – |  «Unterer Quintner Kalk» |  Kimméridgien     | Oxfordien   | Malm  |
|15202304 |Oolite ferrugineuse de la Planplatte | Kalkstein: Eisenooide  | –   | – |  Planplatte-Eisenoolith |  Callovien     | Callovien   | Lias-Dogger in pelagischer Fazies  |
|15202305 |Conglomérat du Geissbach | Konglomerat  | –   | – |  Geissbach-Konglomerat |  Aalénien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15202306 |Grès de Stöckli | Sandstein: Quarz  | Brekzie: dolomitisch   | – |  Stöckli-Sandstein |  Aalénien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15202307 |Mélange Infrapréalpin | Tonstein  | Sandstein   | Kalkstein |  «Infrapräalpines Melange» |  Priabonien     | Priabonien   | Mélange  |
|15202308 |Mélange d&#39;Iberg | Mergelstein  | Tonstein   | – |  Iberg-Melange |  Eocène     | Eocène   | Mélange  |
|15202309 |Flysch de Surbrunnen | Tonstein  | Sandstein: tonig: Lithoklasten   | – |  Surbrunnen-Flysch |  Thanétien     | Danien   | Flysch  |
|15202310 |Complexe de la Roggenegg | Mergelstein  | Kalkstein   | – |  Roggenegg-Komplex |  Yprésien     | Trias   | Mélange  |
|15202311 |Complexe de l&#39;Isentobel | Siltstein  | Mergelstein   | – |  Isentobel-Komplex |  Eocène     | Crétacé tardif   | Mélange  |
|15202312 |Flysch der Serhalten | Tonstein  | Mergelstein   | – |  Serhalten-Flysch |  Eocène     | Eocène   | Mélange  |
|15202313 |Flysch de Gwürz | Tonstein  | Sandstein: tonig   | – |  Gwürz-Flysch |  Paléogène     | Paléogène   | Flysch  |
|15202314 |Flysch de Ruestel | Sandstein: tonig  | Tonstein: schiefrig   | – |  Ruestel-Flysch |  Yprésien     | Paléocène   | Flysch  |
|15202315 |Flysch de la Scheidegg | Mergelstein  | Siltstein   | Sandstein: Glaukonit |  Scheidegg-Flysch |  Paléogène     | Paléogène   | Flysch  |
|15202316 |Granite de Habkern | Granit  | –   | – |  Habkern-Granit |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15202317 |Mélange du Gros Plané | Tonstein  | Sandstein   | – |  Gros-Plané-Melange |  Rupélien     | Rupélien   | Mélange  |
|15202318 |Mélange de la Bodevena | Tonstein  | Sandstein   | – |  Bodevena-Melange |  Priabonien     | Crétacé tardif   | Mélange  |
|15202319 |Flysch Subalpin | Tonstein  | Sandstein: Quarz   | – |  «Subalpiner Flysch» |  Rupélien     | Priabonien   | Flysch  |
|15202320 |Formation du Torrenthorn | Sandstein: kalkig-kieselig  | Kalkstein: sandig-spätig   | Tonstein |  Torrenthorn-Formation |  Toarcien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202321 |Banc du Weissgandstöckli | Sandstein: kalkig: Glimmer  | –   | – |  Weissgandstöckli-Bank |  Sinémurien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15202322 |Membre du (Piz) Grisch | Tonstein: siltig-schiefrig  | Kalkstein   | – |  Grisch-Member |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202323 |Membre du Foostock | Tonstein: siltig-schiefrig  | –   | – |  Foostock-Member |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202324 |Formation du Murgtal | Brekzie  | Sandstein   | Tonstein: siltig-schiefrig |  Murgtal-Formation |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202325 |Membre du Dzéman | Konglomerat  | Sandstein   | Tonstein |  Dzéman-Member |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15202326 |Faciès de bordure aplitique du Granite Central de l&#39;Aar | Granit: aplitisch  | –   | – |  Zentraler Aare-Granit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202327 |Rhyolithe de la Chli Windgällen | Rhyolith: ignimbritisch  | –   | – |  Windgällen-Formation |  Assélien     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202328 |Complexe gneissique de la Bäregg | Gneis  | Gneis: mylonitisch   | Granodiorit |  Bäregg-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202329 |Complexe gneissique du Gärsthorn | Gneis: augig  | –   | – |  Gärsthorn-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202330 |Complexe gneissique de Sogn Placi | Gneis  | Schiefer: Glimmer   | Schiefer: tonig |  Sogn-Placi-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202331 |Complexe gneissique de la Massa | Gneis: migmatitisch  | Migmatit   | Amphibolit |  Massa-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202332 |Roches plutoniques éo-varisques du massif des Aiguilles Rouges | Gestein: plutonisch  | –   | – |  – |  Pennsylvanien     | Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202333 |Roches plutoniques éo-varisques du massif des Aiguilles Rouges | Gestein: plutonisch  | –   | – |  – |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15202334 |Socle polycyclique anté-varisque du massif des Aiguilles Rouges | Gneis  | Schiefer   | Amphibolit |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202335 |Gneiss des Chéserys | Gneis: Kyanit  | –   | – |  Chéserys-Gneis |  Dévonien     | Paléozoïque   | Prävariszisches Grundgebirge  |
|15202336 |Roches plutoniques tardi- à post-varisques du massif du Mont Blanc | Gestein: plutonisch  | –   | – |  – |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202337 |Socle polycyclique anté-varisque du massif du Mont Blanc | Gneis  | Schiefer   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202338 |Complexe gneissique de l&#39;Alp Cavradi | Gneis  | Schiefer: tonig   | Schiefer: Graphit |  Alp-Cavradi-Gneiskomplex |  Paléozoïque     | Paléozoïque   | Prä- bis frühvariszisches Grundgebirge  |
|15202339 |Complexe gneissique de Giubine | Gneis  | Schiefer: Glimmer   | – |  Giubine-Gneiskomplex |  Paléozoïque     | Paléozoïque   | Prä- bis frühvariszisches Grundgebirge  |
|15202340 |Socle polycyclique anté-varisque de la nappe du Gotthard | Gneis  | Schiefer   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202341 |Gneiss d&#39;Unterwassern | Gneis  | –   | – |  Unterwassern-Gneis |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202343 |Gneiss oeillé du Sassina | Gneis: granitisch-augig  | –   | – |  Sassina-Spans-Augengneis |  Paléozoïque     | Paléozoïque   | Prävariszisches Grundgebirge  |
|15202344 |Gneiss granitique de l&#39;Alp Ramosa | Gneis: granitisch  | –   | – |  Alp-Ramosa-Granitgneis |  Paléozoïque     | Paléozoïque   | Prävariszisches Grundgebirge  |
|15202346 |Complexe gneissique du Val Nalps | Gneis  | Amphibolit: Granat   | Gestein: ultramafisch |  Val-Nalps-Gneiskomplex |  Cambrien     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202347 |Gneiss de Prato | Gneis  | Schiefer: Glimmer   | Amphibolit |  Prato-Gneis |  Cambrien     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202348 |Gneiss du Distelgrat | Gneis: sedimentär  | –   | – |  Distelgrat-Gneis |  Cambrien     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202349 |Gneiss oeillé du Val Gronda | Gneis: migmatitisch-augig  | –   | – |  Val-Gronda-Augengneis |  Cambrien     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202350 |Serpentinite de la Fuorcla Paradis | Serpentinit  | –   | – |  Fuorcla-Paradis-Serpentinit |  Cambrien     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202351 |Complexe gneissique du (Piz) Paradis | Gneis: migmatitisch  | –   | – |  Paradis-Gneiskomplex |  Cambrien     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202352 |Gneiss d&#39;Oberstafel | Gneis: Biotit-Plagioklas  | –   | – |  Oberstafel-Gneis |  Mittleres Ordovizium     | Frühes Ordovizium   | Prävariszisches Grundgebirge  |
|15202353 |Gneiss du (Piz) Ganneretsch | Gneis: migmatitisch  | –   | – |  Ganneretsch-Gneis |  Cambrien     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202354 |Amphibolite de Corandoni | Amphibolit  | Schiefer: Hornblende   | Gneis |  Corandoni-Amphibolit |  Cambrien     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202355 |Socle polycyclique anté-varisque de la nappe du Tavetsch | Gneis  | Migmatit   | Amphibolit |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202356 |Complexe gneissique de Rueras | Gneis: Muskovit  | –   | – |  Rueras-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202357 |Roches sédimentaires et volcaniques éo-varisques du massif des Aiguilles Rouges | Gestein: sedimentär  | Gestein: vulkanisch   | – |  – |  Mississippien     | Mississippien   | Prä- bis frühvariszisches Grundgebirge  |
|15202358 |Schistes de l&#39;Au d&#39;Arbignon | Tonstein: schiefrig: Anthrazit  | –   | – |  Au-d&#39;Arbignon-Schiefer |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202359 |Conglomérat de Dorénaz | Konglomerat  | –   | – |  Dorénaz-Konglomerat |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202360 |Wildflysch | Tonstein  | –   | – |  – |  Paléogène     | Paléogène   | Mélange  |
|15205032 |Maiolica Lombarda | Kalkstein: mikritisch: Chert  | Tonstein   | – |  «Maiolica Lombarda» |  Barrémien     | Tithonien   | Maiolica / Aptychenkalk  |
|15205033 |Groupe de la Radiolarite Lombarde | Gestein: kieselig: Radiolarien  | Kalkstein: mergelig   | – |  «Selcifero Lombardo» |  Tithonien     | Bajocien   | Radiolarit  |
|15205034 |Rosso ad Aptici | Mergelstein  | Kalkstein: mergelig: Chert   | – |  «Rosso ad Aptici» |  Tithonien     | Kimméridgien   | Radiolarit  |
|15205035 |Calcari a bivalvi planctonici | 15111227  | Mergelstein   | – |  «Calcare a bivalvi planctonici» |  Bajocien     | Aalénien   | Lias-Dogger in pelagischer Fazies  |
|15205036 |Rosso Ammonitico Lombardo | Kalkstein: mergelig: Bioklasten  | Mergelstein   | – |  «Rosso Ammonitico Lombardo» |  Aalénien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15205037 |Lumachelle à Posidonia alpina (Grenzposidonienschichten) | Mergelstein: Bioklasten  | –   | – |  «Grenzposidonienschichten» |  Toarcien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15205038 |Formation de Morbio | Kalkstein: mikritisch  | Mergelstein   | – |  Morbio-Formation |  Toarcien     | Pliensbachien   | Lias-Dogger in pelagischer Fazies  |
|15205039 |Calcaire de Besazio | Kalkstein: Bioklasten  | –   | – |  Besazio-Kalk |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15205040 |Formation de Moltrasio | Kalkstein: kieselig  | Mergelstein   | Brekzie |  Moltrasio-Formation |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15205041 |Membre du Molino | Kalkstein: kieselig  | Mergelstein   | – |  Molino-Member |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15205042 |Formation de Saltrio | Kalkstein: arenitisch: Bioklasten  | –   | – |  Saltrio-Formation |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15205043 |Macchia Vecchia | Brekzie  | –   | – |  «Macchia Vecchia» |  Pliensbachien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15205044 |Broccatello d&#39;Arzo | Kalkstein: Bioklasten  | Brekzie   | – |  Broccatello d&#39;Arzo |  Sinémurien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15205045 |Formation de l&#39;Albenza | Kalkstein: dolomitisch  | Dolomitstein: kalkig   | Kalkstein: Ooide |  Albenza-Formation |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15205046 |Calcaire de Zu | Kalkstein: Bioklasten  | Kalkstein: mergelig   | Mergelstein |  Zu-Kalk |  Rhétien     | Norien   | Pelitische Trias  |
|15205047 |Formation de Tremona | 15111193  | Mergelstein   | Dolomitstein |  Tremona-Formation |  Rhétien     | Rhétien   | Pelitische Trias  |
|15205048 |Brecce Retiche | Brekzie  | –   | – |  «Brecce Retiche» |  Rhétien     | Rhétien   | Pelitische Trias  |
|15205049 |Argilite de Riva di Solto | Tonstein  | Mergelstein   | Kalkstein: mergelig |  Riva-di-Solto-Tonstein |  Norien     | Norien   | Pelitische Trias  |
|15205050 |Dolomia Principale | Dolomitstein  | Dolomitstein: stromatolithisch   | – |  «Dolomia Principale» |  Norien     | Norien   | Hauptdolomit  |
|15205051 |Marne du (Monte) Pizzella | Mergelstein  | Mergelstein: Bitumen   | Kalkstein |  Pizzella-Mergel |  Carnien     | Carnien   | Raibl  |
|15205052 |Formation de Cunardo | Kalkstein: Chert  | –   | – |  Cunardo-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205053 |Formation de Meride | Kalkstein: tonig  | Tonstein: schiefrig: Bitumen   | Dolomitstein |  Meride-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205054 |Kalkschieferzone (Fm. de Meride) | Schiefer: kalkig  | Kalkstein: mikritisch   | Mergelstein |  «Kalkschieferzone» (Meride-Fm.) |  Carnien     | Ladinien   | Karbonatische Trias  |
|15205055 |Banc de Cassina | Tonstein: schiefrig: Bitumen  | Kalkstein   | Tuffit |  Cassina-Bank |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205056 |Cava Superiore | Tonstein: schiefrig: Bitumen  | –   | – |  «Cava Superiore» |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205057 |Cava Inferiore | Tonstein: schiefrig: Bitumen  | –   | – |  «Cava Inferiore» |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205058 |Dolomie du (Monte) San Giorgio | 15111281  | –   | – |  San-Giorgio-Dolomit |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205059 |Tuffite du Val Serrata | Tuffit  | –   | – |  Val-Serrata-Tuffite |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205060 |Formation de Besano | 15111288  | Tonstein: schiefrig: Bitumen   | – |  Besano-Formation |  Ladinien     | Anisien   | Karbonatische Trias  |
|15205061 |Dolomie du (Monte) San Salvatore | Dolomitstein  | –   | – |  San-Salvatore-Dolomit |  Ladinien     | Anisien   | Karbonatische Trias  |
|15205062 |Formation de Bellano | Konglomerat  | Sandstein   | – |  Bellano-Formation |  Anisien     | Trias précoce   | Detritische Trias  |
|15205063 |Servino | Sandstein  | Tonstein   | – |  «Servino» |  Trias précoce     | Permien   | Detritische Trias  |
|15205064 |Verrucano Lombardo | Konglomerat  | Sandstein   | Tonstein |  – |  Changhsingien     | Changhsingien   | Spät- bis postvariszisches Grundgebirge  |
|15205065 |Roches volcanique permienne du Sudalpin | Gestein: vulkanisch  | –   | – |  – |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15205066 |Granophyre permien du Sudalpin | Granophyr  | –   | – |  – |  Kungurien     | Kungurien   | Spät- bis postvariszisches Grundgebirge  |
|15205067 |Andésite et dacite permiennes du Sudalpin | Andesit  | Dazit   | – |  – |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15205068 |Basalte permien du Sudalpin | Basalt  | –   | – |  – |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15205069 |Tuf basal permien du Sudalpin | Tuffit  | –   | – |  – |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15205070 |Formation de Manno | Konglomerat  | Sandstein   | Schiefer: tonig: Anthrazit |  Manno-Formation |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15205071 |Südalpin: Paläogen-Neogen | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Tertiaire     | Tertiaire   | Sedimentbedeckung  |
|15205072 |Südalpin: Kreide | Sandstein  | Gestein: pelitisch   | Kalkstein |  – |  Crétacé     | Crétacé   | Sedimentbedeckung  |
|15205073 |Südalpin: Radiolarit-Aptychenkalk | Gestein: kieselig: Radiolarien  | Kalkstein: mergelig   | – |  – |  Jurassique tardif     | Jurassique tardif   | Radiolarit  |
|15205074 |Südalpin: Dogger | 15111227  | Mergelstein   | – |  – |  Jurassique moyen     | Jurassique moyen   | Lias-Dogger in pelagischer Fazies  |
|15205075 |Südalpin: Lias | Kalkstein  | Mergelstein   | Brekzie |  – |  Jurassique précoce     | Jurassique précoce   | Syn-Rift  |
|15205076 |Südalpin: Trias | Dolomitstein  | Gestein: pelitisch   | Kalkstein |  – |  Trias     | Trias   | Prä-Rift  |
|15205077 |Südalpin: Permo-Karbon | Konglomerat  | Sandstein   | Gestein: vulkanisch |  – |  Permien     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15205078 |Südalpin: Grundgebirge | Gneis  | Amphibolit   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15205079 |roches intrusives varisques du Sudalpin | Gestein: plutonisch  | –   | – |  – |  Paléozoïque     | Paléozoïque   | Variszisches Grundgebirge  |
|15205080 |San-Bernardo-Gneis | Gneis  | –   | – |  San-Bernardo-Gneis |  Silurien     | Ordovicien   | Grundgebirge  |
|15205081 |métasédiments anté-varisques du Sudalpin | Gneis: sedimentär  | Schiefer: Glimmer   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15205082 |Stabbiello-Gneis | 15111554  | –   | – |  Stabbiello-Gneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15205083 |Giumello-Gneis | 15111513  | –   | – |  Giumello-Gneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15205084 |Ceneri-Gneis | Gneis: Granat  | –   | – |  Ceneri-Gneis |  Spätes Ordovizium     | Spätes Ordovizium   | Grundgebirge  |
|15205085 |Südalpin: Proterozoische und paläozoische mafische und ultramafische Gesteine | Gestein: mafisch  | Gestein: ultramafisch   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15205086 |Mont-Morion-Granit | Granit: porphyrisch  | –   | – |  Mont-Morion-Granit |  Permien     | Permien   | Variszisches Grundgebirge  |
|15205087 |Pointe-d&#39;Otemma-Granodiorit | 15111412  | Gneis: granodioritisch   | – |  Pointe-d&#39;Otemma-Granodiorit |  Permien     | Permien   | Variszisches Grundgebirge  |
|15205088 |Bouquetins-Quarzdiorit | 15111439  | Gneis: dioritisch   | – |  Bouquetins-Quarzdiorit |  Permien     | Permien   | Variszisches Grundgebirge  |
|15205089 |Tête-de-Valpelline-Phyllit | Schiefer: tonig: Graphit  | –   | – |  Tête-de-Valpelline-Phyllit |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15205090 |Arolla-Einheit: Série rubanée | Gneis: gebändert  | Gneis: granitisch   | Gneis: dioritisch |  «Série Rubanée» |  Paléozoïque     | Paléozoïque   | Variszisches Grundgebirge  |
|15205091 |Sassa-Metagabbro | Gabbro  | Diorit   | Gestein: ultramafisch |  Sassa-Metagabbro |  Permien     | Permien   | Variszisches Grundgebirge  |
|15205092 |Maia-Metagabbro | Gabbro: Hornblende  | –   | – |  Maia-Metagabbro |  Permien     | Permien   | Variszisches Grundgebirge  |
|15205093 |Losone-Schiefer | Schiefer: Serizit-Chlorit  | Gneis   | – |  Losone-Schiefer |  Mésozoïque     | Protérozoïque   | Grundgebirge  |
|15205094 |Pizzo-Leone-Gneis | Gneis: Chlorit  | –   | – |  Pizzo-Leone-Gneis |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203562 |Klippen-Flysch | Sandstein  | Mergelstein   | – |  – |  Eocène     | Eocène   | Flysch  |
|15203559 |Simano-D.: Ultramafitit | Gestein: ultramafisch  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203560 |Schistes de l&#39;Alpbach | Schiefer: tonig  | Sandstein   | Kalkstein |  Alpbach-Schiefer |  Crétacé     | Crétacé   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203561 |Arosa-D.: Gabbro | Gabbro  | –   | – |  – |  Jurassique moyen     | Jurassique moyen   | Ophiolithische Abfolge  |
|15203563 |Couches-Rouges de klippes de Suisse centrale | Kalkstein: mergelig  | Kalkstein: mikritisch   | Mergelstein |  – |  Maastrichtien     | Albien   | Couches Rouges  |
|15203564 |Flysch du Wägital: partie supérieure (Paléogène) | Brekzie: polymikt  | Sandstein   | Kalkstein: siltig-tonig |  Wägital-Flysch |  Yprésien     | Yprésien   | Flysch  |
|15203565 |Flysch du Wägital: partie inférieure (Crétacé) | Brekzie: polymikt  | Mergelstein   | Kalkstein: mikritisch |  Wägital-Flysch |  Maastrichtien     | Santonien   | Flysch  |
|15203566 |Flysch du Wägital: partie basale, tectonisée | Sandstein  | Mergelstein   | Kalkstein: siltig-tonig |  Wägital-Flysch |  Maastrichtien     | Santonien   | Flysch  |
|15203567 |Formations de Gibel et de Griggeli | Kalkstein: sandig  | –   | – |  – |  Oxfordien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15203568 |Dolomie des Préalpes Médianes | Dolomitstein  | –   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15203569 |Dolomie et calcaire des Préalpes Médianes | Dolomitstein  | Kalkstein   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15203570 |Dolomie schisteuse et cornieule des Préalpes Médianes | Dolomitstein: schiefrig  | Rauwacke   | – |  – |  Trias     | Trias   | Prä-Rift  |
|15203571 |Cornieule des Préalpes Médianes | Rauwacke  | –   | – |  – |  Trias     | Trias   | Prä-Rift  |
|15203572 |Marne gypseuse et grès des Préalpes Médianes | Mergelstein: Gips  | Sandstein   | – |  – |  Trias     | Trias   | Prä-Rift  |
|15203573 |Grès des Schlieren, tectonisé au Paléogène | Sandstein  | Siltstein   | Tonstein |  Schlieren-Sandstein |  Paléogène     | Paléogène   | Flysch  |
|15203574 |Couches de la Leimern | Kalkstein: mergelig  | Mergelstein: kalkig   | – |  Leimern-Schichten |  Santonien     | Coniacien   | Couches Rouges  |
|15203575 |Cornieule et grès quartzitique des Préalpes Médianes (Trias basal) | Rauwacke  | Sandstein: Quarz   | – |  – |  Trias moyen     | Trias précoce   | Prä-Rift  |
|15203576 |Flysch des Schlieren: masse principale (Paléogène) | Sandstein  | Siltstein   | – |  – |  Yprésien     | Yprésien   | Flysch  |
|15203577 |Lias moyen des Préalpes | Kalkstein: sandig  | Kalkstein: spätig   | – |  – |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15203579 |Schistes argileux de la Nolla: grès quartzitique | Sandstein: Quarz  | –   | – |  Nolla-Tonschiefer |  Albien     | Aptien   | Sedimentbedeckung  |
|15203580 |Formation du Bärenhorn: grès quartzitique | Sandstein: Quarz  | –   | – |  Bärenhorn-Formation |  Barrémien     | Berriasien   | Sedimentbedeckung  |
|15203581 |Schiste argilo-calcaire de la nappe de la Grava | Schiefer: kalkig  | –   | – |  – |  Crétacé     | Crétacé   | Sedimentbedeckung  |
|15203582 |Schiste calcaréo-argileux de la nappe de la Grava | Schiefer: tonig  | –   | – |  – |  Crétacé     | Crétacé   | Sedimentbedeckung  |
|15203583 |Trias de la nappe de la Grava, indifférencié | Schiefer: Serizit  | –   | – |  – |  Trias     | Trias   | Prä-Rift  |
|15203584 |Soladier- und Verdy-Mb. | Mergelstein  | Kalkstein   | – |  Staldengraben-Formation |  Bajocien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15203585 |Col-de-Tompey- und Bois-de-Luan-Mb. | Mergelstein  | Sandstein: kalkig   | Kalkstein: mikritisch |  – |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15203586 |Heiti- und Rossinière-Fm. | Mergelstein  | Kalkstein: kieselig   | Kalkstein: spätig |  – |  Bajocien     | Sinémurien   | Syn-Rift  |
|15203587 |Coulaytes-Melange und Cuvigne-Derrey-Fm. | Tonstein  | Kalkstein   | Sandstein: tonig: Lithoklasten |  – |  Priabonien     | Eocène moyen   | Syn-Kollision  |
|15203588 |Langel- und Col-de-Cordon-Mb. | Kalkstein: Ooide  | Kalkstein: arenitisch   | – |  – |  Callovien     | Bajocien   | Syn-Rift  |
|15203589 |Grande-Bonavau-Fm. und Fm. spathique | Kalkstein: spätig  | Kalkstein: mikritisch   | Dolomitstein |  – |  Aalénien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15203590 |Col-de-Tompey- und Agreblierai-Mb. | Mergelstein  | Sandstein: kalkig   | Kalkstein: Ooide |  – |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15203591 |Chavanette- und Rubli-Mb. | Brekzie  | Mergelstein   | Kalkstein |  – |  Callovien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15203592 |Barrhorn-Einheit: Flysch | Sandstein  | Gestein: pelitisch   | – |  – |  Lutétien     | Lutétien   | Flysch  |
|15203593 |Barrhorn-Einheit: Couches-Rouges | Kalkstein: mergelig  | Mergelstein   | – |  – |  Maastrichtien     | Cénomanien   | Couches Rouges  |
|15203594 |Barrhorn-Einheit: Malm | Kalkstein  | Mergelstein   | – |  – |  Berriasien     | Oxfordien   | Malm  |
|15203595 |Barrhorn-Einheit: Dogger | Sandstein  | Mergelstein   | Kalkstein: Ooide |  – |  Callovien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15203596 |St-Triphon- und Wiriehorn-Fm. | Kalkstein  | Dolomitstein   | – |  – |  Anisien     | Olénékien   | Karbonatische Trias  |
|15203597 |Printse-Fm. | Sandstein  | Schiefer: tonig: Anthrazit   | – |  Printse-Formation |  Carbonifère     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15203598 |Métailler-Fm.: Louvie-Gabbro | Gabbro  | –   | – |  Louvie-Gabbro |  Spätes Ordovizium     | Mittleres Ordovizium   | Grundgebirge  |
|15203599 |Distulberg-Fm.: Graphitschiefer | Schiefer: Graphit  | –   | – |  Distulberg-Formation |  Cambrien     | Cambrien   | Grundgebirge  |
|15203600 |Lirec-Fm.: Amphibolit | Amphibolit  | –   | – |  Lirec-Formation |  Cambrien     | Cambrien   | Grundgebirge  |
|15203601 |Ergischhorn-Komplex: Brändjispitz-Gabbro | Gabbro  | –   | – |  Brändjispitz-Metagabbro |  Cambrien     | Cambrien   | Grundgebirge  |
|15203602 |Ergischhorn-Komplex: Eklogit | Eklogit  | –   | – |  Ergischhorn-Komplex |  Protérozoïque     | Protérozoïque   | Grundgebirge  |
|15203603 |Südegg-Komplex: Prasinit | Prasinit  | Basalt   | – |  Südegg-Komplex |  Mésozoïque     | Mésozoïque   | Mélange  |
|15203604 |Südegg-Komplex: Talk-Chloritschiefer | Schiefer: Chlorit-Talk  | –   | – |  Südegg-Komplex |  Mésozoïque     | Mésozoïque   | Mélange  |
|15203605 |Gurnigel-Decke: Flysch-3 | Mergelstein  | Sandstein: kalkig   | – |  «Flysch 3» |  Thanétien     | Danien   | Flysch  |
|15203606 |Gurnigel-Decke: Flysch-2 | Sandstein  | Tonstein   | – |  «Flysch 2» |  Yprésien     | Yprésien   | Flysch  |
|15203607 |Hellstätt-Fm. und Flysch 2a | Tonstein  | Sandstein   | Kalkstein: siltig-tonig |  – |  Danien     | Maastrichtien   | Flysch  |
|15203608 |Aroley-, Marmontains- und St-Chritophe-Fm. | Schiefer  | Marmor   | Quarzit |  – |  Paléogène     | Crétacé   | Sedimentbedeckung  |
|15203609 |Südegg-Komplex: Schwarzer Schiefer | Schiefer: tonig  | –   | – |  Südegg-Komplex |  Carbonifère     | Carbonifère   | Mélange  |
|15203610 |Südegg-Komplex: Serpentinit | Serpentinit  | –   | – |  Südegg-Komplex |  Permien     | Carbonifère   | Mélange  |
|15203611 |Südegg-Komplex: Albitgneis | Gneis: Albit  | –   | – |  Südegg-Komplex |  Permien     | Permien   | Mélange  |
|15203612 |Südegg-Komplex: Marmor | Marmor: kalkig  | Marmor: dolomitisch   | Brekzie: dolomitisch |  Südegg-Komplex |  Trias tardif     | Trias moyen   | Mélange  |
|15203613 |Südegg-Komplex: Brekzie | Brekzie  | –   | – |  Südegg-Komplex |  Jurassique     | Jurassique   | Mélange  |
|15203614 |Südegg-Komplex: Gips | Evaporit: Gips  | –   | – |  Südegg-Komplex |  Trias tardif     | Trias moyen   | Mélange  |
|15203615 |Monte-Leone-Decke: Sedimentbedeckung | Schiefer  | Marmor   | Konglomerat |  – |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15203616 |Monte-Leone-Decke: Dogger-Malm | Konglomerat: polymikt  | Marmor   | Schiefer: Glimmer |  – |  Jurassique tardif     | Jurassique moyen   | Post-Rift  |
|15203617 |Monte-Leone-Decke: Dogger-Malm: Glimmerschiefer | Schiefer: Glimmer  | –   | – |  – |  Jurassique tardif     | Jurassique moyen   | Post-Rift  |
|15203618 |Monte-Leone-Decke: Dogger-Malm: Marmor | Marmor  | –   | – |  – |  Jurassique tardif     | Jurassique moyen   | Post-Rift  |
|15203619 |Monte-Leone-Decke: Dogger: Konglomerat | Konglomerat  | Sandstein   | – |  – |  Jurassique tardif     | Jurassique moyen   | Syn-Rift  |
|15203620 |Monte-Leone-Decke: Lias | Konglomerat  | Marmor   | Schiefer |  – |  Jurassique moyen     | Jurassique précoce   | Syn-Rift  |
|15203621 |Monte-Leone-Decke: Lias: Sandstein | Sandstein  | –   | – |  – |  Jurassique moyen     | Jurassique précoce   | Lias-Dogger in detritischer Fazies  |
|15203622 |Monte-Leone-Decke: Lias: Konglomerat | Konglomerat  | Sandstein   | – |  – |  Jurassique moyen     | Jurassique précoce   | Lias-Dogger in detritischer Fazies  |
|15205095 |Fornale-Gabbro | Gabbro: Hornblende  | –   | – |  Fornale-Gabbro |  Permien     | Permien   | Variszisches Grundgebirge  |
|15205096 |Matterhorn-Gabbro | Gabbro  | –   | – |  Matterhorn-Gabbro |  Permien     | Permien   | Ophiolithische Abfolge  |
|15205097 |Berrio-Gabbro | Gabbro  | –   | – |  Berrio-Gabbro |  Permien     | Permien   | Variszisches Grundgebirge  |
|15205098 |Grand-Dolin-Brekzie | Brekzie: polymikt  | –   | – |  Grand-Dolin-Brekzie |  Jurassique tardif     | Jurassique moyen   | Lias-Dogger in neritischer Fazies  |
|15205099 |Partie supérieure du Calcaire de Meride | Kalkstein: Bitumen  | Mergelstein   | Kalkstein: mergelig |  Meride-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205100 |Partie inférieure du Calcaire de Meride | Kalkstein  | Mergelstein: schiefrig: Bitumen   | – |  Meride-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205101 |Dolomit-Band (Fm. de Meride) | Dolomitstein  | –   | – |  «Dolomitband» (Meride-Fm.) |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205102 |Calcaire du Groupe du Dolin | Kalkstein: spätig: Bioklasten  | –   | – |  – |  Jurassique précoce     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15205103 |Dolomie du Groupe du Dolin | Dolomitstein  | Kalkstein   | – |  – |  Norien     | Norien   | Karbonatische Trias  |
|15205104 |Cornieule du Groupe du Dolin | Rauwacke  | –   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15205105 |Quartzite du Groupe du Dolin | Sandstein: Quarz  | Konglomerat: Quarz   | – |  – |  Trias     | Trias   | Detritische Trias  |
|15205106 |Orthogneiss du Groupe d&#39;Arolla, leucocrate | Gneis: granitisch  | –   | – |  Arolla-Orthogneis |  Permien     | Permien   | Variszisches Grundgebirge  |
|15205107 |Orthogneiss du Groupe d&#39;Arolla, oeillé | Gneis: granitisch-augig  | Gneis   | – |  Arolla-Orthogneis |  Permien     | Permien   | Variszisches Grundgebirge  |
|15205108 |Orthogneiss du Groupe d&#39;Arolla, mylonitique | Gneis: mylonitisch  | –   | – |  Arolla-Orthogneis |  Permien     | Permien   | Variszisches Grundgebirge  |
|15205109 |Gneiss du Groupe d&#39;Arolla, mylonitique | Gneis: mylonitisch  | –   | – |  «Série Rubanée» |  Paléozoïque     | Protérozoïque   | Variszisches Grundgebirge  |
|15205110 |Gneiss du Groupe d&#39;Arolla, micro-oeillé | Gneis: augig  | –   | – |  «Série Rubanée» |  Paléozoïque     | Protérozoïque   | Variszisches Grundgebirge  |
|15205111 |Métagranitoïde du Groupe d&#39;Arolla | Gneis: granitisch-augig  | –   | – |  Arolla-Orthogneis |  Permien     | Permien   | Variszisches Grundgebirge  |
|15205112 |Métaroche basique du Groupe d&#39;Arolla | Diorit  | Gabbro: Hornblende   | – |  – |  Paléozoïque     | Protérozoïque   | Variszisches Grundgebirge  |
|15205113 |Métaroche basique du Groupe d&#39;Arolla, mylonitique | 15111448  | Schiefer: Zoisit-Fuchsit   | – |  – |  Paléozoïque     | Protérozoïque   | Variszisches Grundgebirge  |
|15205114 |Prasinite du Groupe d&#39;Arolla | Prasinit  | –   | – |  – |  Mésozoïque     | Protérozoïque   | Grundgebirge  |
|15205115 |Gabbro à horneblende du Groupe d&#39;Arolla | Gabbro: Hornblende  | Diorit   | – |  – |  Permien     | Permien   | Grundgebirge  |
|15205116 |Roche ultramafique du Groupe d&#39;Arolla | Gestein: ultramafisch  | Serpentinit   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15205117 |Paragneiss du Groupe d&#39;Arolla | Gneis: sedimentär  | Gneis: Amphibol   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15205118 |Micaschiste du Groupe d&#39;Arolla | Schiefer: Glimmer-Granat  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15205119 |Mylonite du Groupe de Valpelline | Mylonit  | Schiefer: Chlorit-Epidot   | Gneis: Albit |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15205120 |Amphibolite du Groupe de Valpelline | Amphibolit  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15205121 |Marbre du Groupe de Valpelline | Marmor: kalkig  | Marmor: Kalksilikat   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15205122 |Migmatite du Groupe de Valpelline | Gneis: migmatitisch  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15205123 |Marbre de Roisan | Marmor: kalkig  | Marmor: dolomitisch   | Schiefer: kalkig: Glimmer |  – |  Trias moyen     | Permien   | Sedimentbedeckung  |
|15205124 |Granite de Musella | Granit: porphyrisch: Hornblende  | –   | – |  Musella-Granit |  Carbonifère     | Carbonifère   | Grundgebirge  |
|15205125 |Granodiorite de la Sella | 15111412  | –   | – |  Sella-Granodiorit |  Carbonifère     | Carbonifère   | Grundgebirge  |
|15205126 |Formation de Marinelli | 15111580  | Schiefer: tonig: Graphit   | Amphibolit |  Marinelli-Formation |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15205127 |socle cristallin de la nappe de la Margna-Sella | Gneis  | Amphibolit   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15205128 |roches intrusives de la nappe de la Margna-Sella | Granit  | Granodiorit   | – |  – |  Permien     | Carbonifère   | Variszisches Grundgebirge  |
|15205129 |socle polycyclique anté-varisque de la nappe de la Margna-Sella | Gneis  | Schiefer   | Amphibolit |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15205130 |Métaarkose, orthogneiss anté-varisque | Gneis  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15205131 |orthogneiss de la nappe de Sesia | Gneis: magmatisch  | –   | – |  – |  Permien     | Carbonifère   | Grundgebirge  |
|15205132 |micaschiste de la nappe de Sesia | Schiefer: Glimmer  | Eklogit   | Marmor |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15205133 |Péridotite de Finero | Peridotit  | –   | – |  Finero-Peridotit |  Permien     | Permien   | Variszisches Grundgebirge  |
|15205134 |Complexe Mafique d&#39;Ivrée | Gabbro  | Diorit   | – |  – |  Permien     | Permien   | Variszisches Grundgebirge  |
|15205135 |Zona Dioritico-Kinzigitica | Gneis: granulitisch  | Gestein: basisch   | Marmor |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15205136 |orthogneiss anté-varisques du Sudalpin | Gneis: magmatisch  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15205137 |Formation de Pontida | Sandstein  | Tonstein   | – |  Pontida-Formation |  Coniacien     | Turonien   | Flysch  |
|15205138 |Arolla-Einheit: Metagranit | Granit  | –   | – |  – |  Permien     | Permien   | Variszisches Grundgebirge  |
|15205139 |Arolla-Einheit: Leukokrater Granitgneis | Gneis: granitisch  | –   | – |  – |  Permien     | Permien   | Variszisches Grundgebirge  |
|15206001 |roches volcaniques cénozoïques péri-adriatiques | Gestein: vulkanisch  | –   | – |  – |  Paléogène     | Paléogène   | Periadriatisches Vulkanismus  |
|15206002 |Intrusion de Novate | Granit  | –   | – |  – |  Miocène précoce     | Chattien   | Novate-Intrusion  |
|15206003 |Intrusion du Bergell | Granodiorit  | Tonalit   | Granit |  – |  Oligocène     | Oligocène   | Bregaglia-Intrusion  |
|15206004 |Intrusion de l&#39;Adamello | Granodiorit  | Tonalit   | Granit |  – |  Rupélien     | Priabonien   | Adamello-Intrusion  |
|15206005 |Melirolo-Augengneis | Gneis: augig  | –   | – |  Melirolo-Augengneis |  Rupélien     | Rupélien   | Bregaglia-Intrusion  |
|15206006 |Bergell-Intrusiva: Granodioritische Fazies | Granodiorit  | –   | – |  – |  Rupélien     | Rupélien   | Bregaglia-Intrusion  |
|15206007 |Bergell-Intrusiva: Tonalitische Fazies | Tonalit  | –   | – |  – |  Rupélien     | Rupélien   | Bregaglia-Intrusion  |
|15206008 |Monte-Bassetta-Quarzdiorit | Diorit: Quarz  | –   | – |  Monte-Bassetta-Quarzdiorit |  Rupélien     | Rupélien   | Bregaglia-Intrusion  |
|15206009 |Sorico-Tonalit | Tonalit  | –   | – |  Sorico-Tonalit |  Rupélien     | Rupélien   | Bregaglia-Intrusion  |
|15206010 |Jorio-Tonalit | Tonalit  | –   | – |  Jorio-Tonalit |  Rupélien     | Rupélien   | Bregaglia-Intrusion  |
|15206011 |Val-Masino-Granodiorit | Granodiorit  | –   | – |  Val-Masino-Granodiorit |  Rupélien     | Rupélien   | Bregaglia-Intrusion  |
|15206012 |Alpe-Cameraccio-Granodiorit | Granodiorit  | –   | – |  Alpe-Cameraccio-Granodiorit |  Rupélien     | Rupélien   | Bregaglia-Intrusion  |
|15206013 |Monte-Rosso-Mikrogranit | Granit: mikrokristallin  | –   | – |  Monte-Rosso-Mikrogranit |  Oligocène     | Oligocène   | Bregaglia-Intrusion  |
|15206014 |Zocca-Aplit | Aplit  | –   | – |  Zocca-Aplit |  Oligocène     | Oligocène   | Bregaglia-Intrusion  |
|15206015 |San-Fedelino-Granit | Granit  | –   | – |  San-Fedelino-Granit |  Chattien     | Chattien   | Novate-Intrusion  |
|15206016 |Undifferenzierte Einheit | Gestein  | –   | – |  – |  Cénozoïque     | Protérozoïque   | –  |
|15206017 |Undifferenzierte lithologische Einheit: Tektonische Brekzie | Brekzie: tektonisch  | –   | – |  – |  Holocène     | Protérozoïque   | –  |
|15206018 |Lochsiten-Kalk | 15111475  | –   | – |  Lochsiten-Kalk |  Tertiaire     | Mésozoïque   | Sedimentbedeckung  |
|15206019 |Salleren-Brekzie | Brekzie: tektonisch  | –   | – |  Salleren-Brekzie |  Tertiaire     | Mésozoïque   | Sedimentbedeckung  |
|15206020 |Undifferenzierte lithologische Einheit | Gestein  | –   | – |  – |  Cénozoïque     | Protérozoïque   | –  |
|15202364 |Kiental-Melange | Tonstein  | Sandstein   | – |  Kiental-Melange |  Crétacé tardif     | Crétacé tardif   | Mélange  |
|15202361 |Plaine-Morte-Melange | Mergelstein  | Sandstein   | – |  Plaine-Morte-Melange |  Tertiaire     | Crétacé tardif   | Mélange  |
|15202362 |Mättental-Melange | Tonstein  | Mergelstein   | Sandstein |  Mättental-Melange |  Rupélien     | Priabonien   | Mélange  |
|15202363 |Meilleret-Fm.: Höchst-Flysch | Sandstein  | –   | – |  Höchst-Flysch |  Priabonien     | Eocène moyen   | Flysch  |
|15202365 |Termen-Zone: Tonschiefer | Schiefer: Glimmer-Granat  | –   | – |  – |  Toarcien     | Pliensbachien   | Sedimentbedeckung  |
|15202366 |Termen-Zone: Kalkschiefer | Schiefer: kalkig  | Marmor: kalkig   | – |  – |  Pliensbachien     | Rhétien   | Sedimentbedeckung  |
|15202367 |Nufenen-Zone: Knotenschiefer | Schiefer: kalkig: Zoisit  | Marmor: kalkig   | – |  – |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202368 |Nufenen-Zone: Sandstein | Sandstein: Quarz  | Schiefer: tonig-kalkig   | – |  – |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202369 |Nufenen-Zone: Granatschiefer | Schiefer: Glimmer-Granat  | –   | – |  – |  Sinémurien     | Rhétien   | Lias-Dogger in neritischer Fazies  |
|15202370 |Stgir-Fm.: Unterer Teil | Tonstein: schiefrig  | Kalkstein: Bioklasten   | Kalkstein: sandig |  Stgir-Formation |  Sinémurien     | Rhétien   | Lias-Dogger in neritischer Fazies  |
|15202371 |Stgir-Fm.: Oberer Teil | Sandstein: Quarz  | Kalkstein: sandig-spätig   | Tonstein: schiefrig |  Stgir-Formation |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202372 |Inferno-Fm.: Oberer Teil: Runcaleida-Sch. | Sandstein: Quarz  | Kalkstein: Bioklasten   | Tonstein: schiefrig |  Runcaldeida-Schichten |  Toarcien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202373 |Inferno-Fm.: Unterer Teil: Riein-Sch. | Kalkstein: sandig  | –   | – |  Riein-Schichten |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202374 |Meierhof-Phyllit | Phyllit  | Schiefer: Serizit   | – |  Meierhof-Phyllit |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15202375 |Waltensburg-Verrucano | Rhyolith  | Sandstein   | Konglomerat |  Waltensburg-Verrucano |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15202376 |Ruinas Sandstein | Sandstein  | Rhyolith   | Tonstein |  Ruinas-Sandstein |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15202377 |Niederhorn-Fm.: Hohgant-Sandstein: Berglikehle-Bk. | Kalkstein: Bitumen  | Mergelstein: Kohle   | – |  Berglikehle-Bank |  Priabonien     | Priabonien   | «Nummulitikum»  |
|15202378 |Rossplatten-Diorit | Diorit  | Granit   | – |  Rossplatten-Diorit |  Pennsylvanien     | Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202379 |Schöllenen-Diorit | Diorit  | –   | – |  Schöllenen-Diorit |  Pennsylvanien tardif     | Pennsylvanien moyen   | Mittelvariszisches Grundgebirge  |
|15202380 |Amden-Fm.: Leist-Mergel: Grotzen-Austernbank | Kalkstein: siltig: Bioklasten  | –   | – |  Grotzen-Austernbank |  Campanien     | Santonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202381 |Tierwis-Fm.: Hurst-Mergel | Mergelstein  | Kalkstein: mergelig   | – |  Hurst-Mergel |  Barrémien     | Barrémien   | «Urgonien»  |
|15202382 |Helvetischer Kieselkalk: Palis-Bk. | Kalkstein: spätig: Echinodermen  | Kalkstein: kieselig   | – |  Palis-Bank |  Hauterivien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202383 |Öhrli-Fm.: Oberer-Öhrlikalk | Kalkstein: Bioklasten-Ooide  | Kalkstein: spätig   | – |  «Oberer Öhrlikalk» |  Valanginien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202384 |Öhrli-Fm.: Oberer-Öhrlimergel | Mergelstein: kalkig: Bioklasten  | –   | – |  «Oberer Öhrlimergel» |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202385 |Öhrli-Fm.: Unterer-Öhrlikalk | Kalkstein: sandig  | –   | – |  «Unterer Öhrlikalk» |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202386 |Spitzmeilen-Fm.: Oberer Teil | Kalkstein: sandig-spätig  | Kalkstein: kieselig   | Sandstein: kalkig |  Spitzmeilen-Formation |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202387 |Spitzmeilen-Fm.: Unterer Teil | Sandstein: Quarz  | Sandstein: kalkig   | Kalkstein: sandig: Eisenooide |  Spitzmeilen-Formation |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202388 |Spitzmeilen-Fm.: Basaler Teil | Sandstein: Quarz  | Tonstein: schiefrig   | – |  Spitzmeilen-Formation |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202389 |Prodkamm-Fm.: Oberer Teil | Tonstein: schiefrig  | Sandstein: kalkig   | Sandstein: Quarz |  Prodkamm-Formation |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202390 |Prodkamm-Fm.: Mittlerer Teil | Tonstein: schiefrig  | Sandstein: kalkig   | Kalkstein: sandig |  Prodkamm-Formation |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202391 |Prodkamm-Fm.: Unterer Teil | Kalkstein: Ooide  | Mergelstein   | Kalkstein: Bioklasten |  Prodkamm-Formation |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202392 |Sandpass-Fm. | Schiefer  | Phyllit   | – |  Sandpass-Formation |  Artinskien     | Artinskien   | Spät- bis postvariszisches Grundgebirge  |
|15202393 |Sanetsch-Fm.: Diablerets-Mb.: Roc-Champion-Konglomerat | Konglomerat  | –   | – |  Roc-Champion-Konglomerat |  Priabonien     | Priabonien   | «Nummulitikum»  |
|15202394 |Membre du Spirstock | Sandstein: Quarz  | Mergelstein   | – |  Spirstock-Member |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202395 |«Roter Seewenkalk» | Kalkstein: mikritisch  | –   | – |  «Roter Seewenkalk» |  Turonien     | Turonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202396 |Banc de Götzis inférieur | Sandstein: Glaukonit  | –   | – |  Untere Götzis-Bank |  Turonien     | Cénomanien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202397 |Banc du Col de la Plaine Morte | Sandstein: mergelig: Glaukonit  | –   | – |  Col-de-la-Plaine-Morte-Bank |  Aptien     | Aptien   | «Gault»  |
|15202398 |«Oberer Betliskalk» | Kalkstein: Bioklasten-Chert  | –   | – |  «Oberer Betliskalk» |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202399 |«Unterer Betliskalk» | Kalkstein: sandig: Bioklasten  | Kalkstein: spätig   | – |  «Unterer Betliskalk» |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202400 |Brèche fossilifère de Vättis | Kalkstein: spätig: Bioklasten  | Kalkstein: Glaukonit   | – |  Vättis-Fossilbrekzie |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15202401 |Formation d&#39;Inferno, partie supérieure | Schiefer: kalkig: Zoisit  | Kalkstein: spätig: Echinodermen   | – |  Inferno-Formation |  Toarcien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202402 |Formation d&#39;Inferno, partie moyenne | Schiefer: Zoisit  | Mergelstein: Bioklasten   | – |  Inferno-Formation |  Toarcien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202403 |Formation d&#39;Inferno, partie inférieure | Kalkstein  | Schiefer: Zoisit   | Mergelstein: Bioklasten |  Inferno-Formation |  Toarcien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202404 |Formation du Sexmor, partie supérieure | Kalkstein: kieselig  | Kalkstein: spätig   | Kalkstein: sandig |  Sexmor-Formation |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202405 |Formation du Sexmor, partie inférieure | Mergelstein: kalkig  | Kalkstein: kieselig   | Kalkstein: spätig: Bioklasten |  Sexmor-Formation |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202406 |«Leitoolith» | Kalkstein: Bioklasten-Ooide  | –   | – |  «Leitoolith» (Prodkamm-Fm.) |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202411 |Brèche de la Lochegg | Brekzie: kalkig: Bioklasten  | –   | – |  Lochegg-Brekzie |  Eocène     | Eocène   | Syn-Kollision  |
|15202412 |«Obere Zementsteinschichten» | Mergelstein: schiefrig  | Kalkstein: mikritisch   | – |  15253121 |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202413 |«Untere Zementsteinschichten» | Mergelstein  | Kalkstein: mergelig   | – |  15253121 |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202414 |«Rote Echinodermenbrekzie» | Kalkstein: spätig: Bioklasten  | –   | – |  «Rote Echinodermenbrekzie» (Bommerstein-Fm.) |  Bajocien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15202415 |«Obere Tonschiefer» (Fm. du Bommerstein) | Tonstein: schiefrig  | Mergelstein: siltig-schiefrig   | – |  «Obere Tonschiefer» (Bommerstein-Fm.) |  Bajocien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15202416 |Membre du Glockhaus | Sandstein: Quarz  | Kalkstein: sandig: Bioklasten   | Tonstein |  Glockhaus-Member |  Bajocien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15202417 |«Quartzite de base» (Fm. du Coroi) | Sandstein: Quarz  | –   | – |  «Basaler Quarzit» (Coroi-Fm.) |  Aalénien     | Aalénien   | Syn-Rift  |
|15202418 |Cornieule (Fm. de la Röti) | Rauwacke  | –   | – |  Röti-Formation |  Carnien     | Anisien   | Muschelkalk  |
|15202419 |Membre du Col du Jorat | Tonstein  | Sandstein   | Dolomitstein |  Col-du-Jorat-Member |  Anisien     | Anisien   | Buntsandstein  |
|15202420 |«Equisetenschiefer» | Tonstein: schiefrig  | Siltstein: schiefrig   | – |  Quarten-Formation |  Trias tardif     | Trias tardif   | Keuper  |
|15202421 |Marne du Leist | Mergelstein  | –   | – |  Leist-Mergel |  Campanien     | Santonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202422 |Marne du Leiboden | Mergelstein: Bioklasten  | –   | – |  Leiboden-Mergel |  Santonien     | Coniacien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202423 |Formation des Covayes | Mergelstein  | Kalkstein: mikritisch   | – |  Covayes-Formation |  Turonien     | Turonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202424 |Formation du Javrex | Kalkstein: arenitisch  | Kalkstein: sandig: Glaukonit   | – |  Javrex-Formation |  Albien     | Aptien   | «Gault»  |
|15202425 |«Marnes noires pyriteuses» | Mergelstein  | –   | – |  Javrex-Formation |  Albien     | Aptien   | «Gault»  |
|15202426 |«Calcaires gréso-glauconieux» | Kalkstein: sandig: Glaukonit  | Mergelstein: siltig: Glaukonit   | – |  Javrex-Formation |  Aptien     | Aptien   | «Gault»  |
|15203626 |Pizzo-del-Vallone-Decke: Dogger-Malm | Sandstein  | Schiefer: Glimmer   | Marmor |  – |  Jurassique tardif     | Jurassique moyen   | Sedimentbedeckung  |
|15203623 |Monte-Leone-Decke: Trias | Quarzit  | Marmor   | Rauwacke |  – |  Trias     | Trias   | Prä-Rift  |
|15203624 |Monte-Leone-Decke: Quarzitische Trias | Quarzit  | –   | – |  – |  Trias     | Trias   | Prä-Rift  |
|15203625 |Pizzo-del-Vallone-Decke: Sedimentbedeckung | Schiefer  | Marmor   | Sandstein |  – |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15203627 |Pizzo-del-Vallone-Decke: Dogger-Malm: Marmor | Marmor  | –   | – |  – |  Jurassique tardif     | Jurassique moyen   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15203628 |Pizzo-del-Vallone-Decke: Dogger-Malm: Glimmerschiefer | Schiefer: Glimmer  | –   | – |  – |  Jurassique tardif     | Jurassique moyen   | Post-Rift Mesozoikum in detritischer Fazies  |
|15203629 |Pizzo-del-Vallone-Decke: Dogger-Malm: Vulkanit | Gestein: vulkanisch  | –   | – |  – |  Jurassique tardif     | Jurassique moyen   | Sedimentbedeckung  |
|15203630 |Pizzo-del-Vallone-Decke: Lias | Konglomerat  | Quarzit   | Schiefer: Glimmer |  – |  Aalénien     | Jurassique précoce   | Syn-Rift  |
|15203631 |Pizzo-del-Vallone-Decke: Trias | Rauwacke  | Marmor   | Evaporit: Gips |  – |  Trias     | Trias   | Prä-Rift  |
|15203632 |Mont-Fort-Decke: Sedimentbedeckung | Brekzie  | Marmor   | Rauwacke |  – |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15203633 |Mont-Fort-Decke: Trias | Marmor: dolomitisch  | Marmor: kalkig   | Rauwacke |  – |  Trias     | Trias   | Sedimentbedeckung  |
|15203634 |Mont-Fort-Decke: Trias: Rauwacke | Rauwacke  | –   | – |  – |  Trias     | Trias   | Sedimentbedeckung  |
|15203635 |Métailler-Fm.: Quarzit | Quarzit  | –   | – |  – |  Ordovicien     | Ordovicien   | Grundgebirge  |
|15203636 |Métailler-Fm.: Glimmerschiefer | Schiefer: Glimmer  | –   | – |  – |  Ordovicien     | Ordovicien   | Grundgebirge  |
|15203637 |Métailler-Fm.: Chloritoid-Glimmerschiefer | Schiefer: Glimmer-Chloritoid  | –   | – |  – |  Ordovicien     | Ordovicien   | Grundgebirge  |
|15203638 |Distulberg-Fm.: Schiefer | Schiefer  | –   | – |  – |  Cambrien     | Cambrien   | Grundgebirge  |
|15203639 |Distulberg-Fm.: Albitgneis | Gneis: Albit  | –   | – |  – |  Cambrien     | Cambrien   | Grundgebirge  |
|15203640 |Barrhorn-Einheit: Trias | Dolomitstein  | Rauwacke   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15203641 |Siviez-Mischabel-Decke: Aplit | Aplit  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203642 |Siviez-Mischabel-Decke: Pegmatit | Pegmatit  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203643 |Lirec-Fm.: Leukokrater Mikroklingneis | Gneis: Mikroklin  | –   | – |  Lirec-Formation |  Cambrien     | Cambrien   | Grundgebirge  |
|15203644 |Adlerflüe-Fm.: Leukokrater Gneiss | Gneis  | –   | – |  Adlerflüe-Formation |  Cambrien     | Protérozoïque   | Grundgebirge  |
|15203645 |Ergischhorn-Komplex: Leukokrater aplitischer Gneis | Gneis: aplitisch  | –   | – |  Ergischhorn-Komplex |  Protérozoïque     | Protérozoïque   | Grundgebirge  |
|15203646 |Stalden-Gneiskomplex | Gneis  | –   | – |  Stalden-Gneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203647 |Stalden-Gneiskomplex: Ahorn-Augengneis | Gneis: augig  | –   | – |  Ahorn-Augengneiss |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203648 |Stalden-Gneiskomplex: Amphibolit | Amphibolit  | –   | – |  Stalden-Gneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203649 |Printse-Fm.: Konglomerat | Konglomerat  | –   | – |  Printse-Formation |  Permien     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15203650 |Printse-Fm.: Graphitschiefer | Schiefer: Graphit  | Schiefer: tonig: Anthrazit   | – |  Printse-Formation |  Permien     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15203651 |Portjengrat-Decke: Kalzitmarmor | Marmor: kalkig  | –   | – |  – |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15203652 |Portjengrat-Decke: Dolomitmarmor | Marmor: dolomitisch  | –   | – |  – |  Trias     | Trias   | Sedimentbedeckung  |
|15203653 |Portjengrat-Decke: Arkose | Sandstein: Feldspat  | –   | – |  – |  Trias     | Trias   | Prä-Rift  |
|15203654 |Portjengrat-Decke: Grundgebirge | Gneis: migmatitisch  | Gneis   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203655 |Gornergrat-Decke: Kalkschiefer, sandiger Marmor, Brekzie | Schiefer: kalkig  | Marmor: sandig   | Brekzie |  – |  Mésozoïque     | Mésozoïque   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203656 |Gornergrat-Decke: Trias | Marmor: dolomitisch  | Marmor: kalkig   | Rauwacke |  – |  Trias     | Trias   | Karbonatische Trias  |
|15203657 |Gornergrat-Decke: Phengit-Albitgneis | Gneis: Albit  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203658 |Gornergrat-Decke: Basisches Ganggestein | Gestein: basisch-gangartig  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203659 |Gornergrat-Decke: Granat-Muskovit-Schiefer | Schiefer: Glimmer-Granat  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203660 |Frilihorn-Decke: Trias | Marmor: dolomitisch  | Marmor: kalkig   | Rauwacke |  – |  Trias     | Trias   | Karbonatische Trias  |
|15203661 |Frilihorn-Decke: Trias: Rauwacke | Rauwacke  | –   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15203662 |Garda-Bordon-Fm.: Série feuilletée | Schiefer: tonig: Bitumen  | –   | – |  Garda-Bordon-Formation |  Crétacé     | Crétacé   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203663 |Garda-Bordon-Fm.: Quarzschiefer | Schiefer: Quarz  | –   | – |  Garda-Bordon-Formation |  Crétacé     | Crétacé   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203664 |Serra-Neire-Serpentinit | Serpentinit  | –   | – |  Serra-Neire-Serpentinit |  Jurassique     | Jurassique   | Ophiolithische Abfolge  |
|15203665 |Zermatt-Saas-Decke: Eklogit | Eklogit  | –   | – |  – |  Jurassique     | Jurassique   | Ophiolithische Abfolge  |
|15203666 |Zermatt-Saas-Decke: Metapyroxenit | 15111466  | –   | – |  – |  Jurassique     | Jurassique   | Ophiolithische Abfolge  |
|15203667 |Zermatt-Saas-Decke: Metagabbro | Gabbro  | –   | – |  – |  Jurassique     | Jurassique   | Ophiolithische Abfolge  |
|15203668 |Zermatt-Saas-Decke: Rodingit | Rodingit  | –   | – |  – |  Jurassique     | Jurassique   | Ophiolithische Abfolge  |
|15203669 |Zermatt-Saas-Decke: Talkschiefer | Schiefer: Talk  | –   | – |  – |  Jurassique     | Jurassique   | Ophiolithische Abfolge  |
|15203670 |Lengenbach-Dolomitmarmor | Marmor: dolomitisch  | –   | – |  Lengenbach-Dolomitmarmor |  Trias     | Trias   | Prä-Rift  |
|15204001 |Flysch du God Drosa | Tonstein: kieselig  | Sandstein: Feldspat   | Kalkstein: arenitisch |  God-Drosa-Flysch |  Turonien     | Cénomanien   | Flysch  |
|15204002 |Formation de Chanèls | Kalkstein: mergelig-schiefrig  | Tonstein: kalkig: Glaukonit   | – |  Chanèls-Formation |  Turonien     | Aptien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15204003 |Formation de Lech | Gestein: pelitisch  | Gestein: pelitisch   | – |  Lech-Formation |  Cénomanien     | Crétacé précoce   | Flysch  |
|15204004 |Formation d&#39;Emmat | Tonstein: kieselig  | Mergelstein   | Kalkstein: mikritisch |  Emmat-Formation |  Albien     | Aptien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15204005 |Formation du (Munt) Russenna | Kalkstein: mikritisch: Chert  | Tonstein   | Kalkstein: spätig: Bioklasten |  Russenna-Formation |  Aptien     | Tithonien   | Maiolica / Aptychenkalk  |
|15204006 |Formation d&#39;Ammergau | Kalkstein: mikritisch: Aptychen  | –   | – |  Ammergau-Formation |  Crétacé précoce     | Jurassique tardif   | Maiolica / Aptychenkalk  |
|15204007 |Formation du Blais | Gestein: kieselig: Radiolarien  | Tonstein: kieselig   | Kalkstein: mikritisch: Bioklasten |  Blais-Radiolarit |  Tithonien     | Callovien   | Radiolarit  |
|15204008 |Membre de Plattas | Kalkstein: mikritisch: Bioklasten-Chert  | –   | – |  Plattas-Member |  Tithonien     | Tithonien   | Radiolarit  |
|15204009 |Formation de Ruhpolding | 15111108  | –   | – |  Ruhpolding-Formation |  Tithonien     | Oxfordien   | Radiolarit  |
|15204010 |Groupe du (Piz) Saluver | Brekzie: polymikt  | Sandstein   | Tonstein |  – |  Callovien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15204011 |Formation du (Piz) Saluver | Brekzie: polymikt  | Sandstein   | Tonstein: schiefrig |  Saluver-Formation |  Jurassique moyen     | Jurassique moyen   | Lias-Dogger in neritischer Fazies  |
|15204012 |Formation de Bardella | 15111108  | Kalkstein: sandig   | Brekzie: polymikt |  Bardella-Formation |  Jurassique moyen     | Jurassique moyen   | Sedimentbedeckung  |
|15204013 |Formation du (Piz) Salteras | 15111108  | Sandstein: Glimmer   | Brekzie: polymikt |  Salteras-Formation |  Jurassique moyen     | Jurassique moyen   | Sedimentbedeckung  |
|15204014 |Brèche de Salamun | 15111009  | –   | – |  Salamun-Brekzie |  Jurassique moyen     | Jurassique moyen   | Sedimentbedeckung  |
|15204015 |Brèche d&#39;Err | 15111009  | –   | – |  Err-Brekzie |  Jurassique moyen     | Jurassique moyen   | Sedimentbedeckung  |
|15204016 |Formation de l&#39;Allgäu | Mergelstein  | Kalkstein: tonig   | Kalkstein: arenitisch |  Allgäu-Formation |  Callovien     | Hettangien   | Syn-Rift  |
|15206024 |Undifferenzierte lithologische Einheit: Ganggestein | Gestein: gangartig  | –   | – |  – |  Cénozoïque     | Protérozoïque   | –  |
|15206021 |Undifferenzierte lithologische Einheit: Gips | Evaporit: Gips  | –   | – |  – |  Trias     | Trias   | Sedimentbedeckung  |
|15206022 |Undifferenzierte lithologische Einheit: Rauwacke | Rauwacke  | –   | – |  – |  Trias     | Trias   | Sedimentbedeckung  |
|15206023 |Undifferenzierte lithologische Einheit: Dolomitmarmor | Dolomitstein  | –   | – |  – |  Trias     | Trias   | Sedimentbedeckung  |
|15206025 |Lias, indifférencié | Kalkstein  | Gestein: pelitisch   | – |  – |  Jurassique précoce     | Jurassique précoce   | Sedimentbedeckung  |
|15206026 |Dogger, indifférencié | Mergelstein  | Kalkstein   | Sandstein |  – |  Jurassique moyen     | Jurassique moyen   | Sedimentbedeckung  |
|15206027 |Malm, indifférencié | Kalkstein  | Mergelstein   | – |  – |  Jurassique tardif     | Jurassique tardif   | Sedimentbedeckung  |
|15206028 |Crétacé, indifférencié | Kalkstein  | Mergelstein   | Sandstein |  – |  Crétacé     | Crétacé   | Sedimentbedeckung  |
|15206029 |Trias, indifférencié | Dolomitstein  | Evaporit   | Gestein: klastisch |  – |  Trias     | Trias   | Prä-Rift  |
|15206030 |roche sédimentaire, indifférenciée | Gestein: sedimentär  | –   | – |  – |  Cénozoïque     | Protérozoïque   | –  |
|15206031 |roche cristalline, indifférenciée | Gestein: kristallin  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15206032 |granite, indifférencié | Granit  | –   | – |  – |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15206033 |unité stratigraphique indifférenciée | Gestein  | –   | – |  – |  Cénozoïque     | Paléozoïque   | –  |
|15206034 |Mésozoïque, indifférencié | Gestein  | –   | – |  – |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15206035 |rhyolite, indifférenciée | Rhyolith  | –   | – |  – |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15206036 |roche verte, indifférenciée | Amphibolit  | Prasinit   | – |  – |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15206037 |amphibolite, indifférenciée | Amphibolit  | –   | – |  – |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15206038 |filon de quartz | Gestein: gangartig: Quarz  | –   | – |  – |  Cénozoïque     | Protérozoïque   | –  |
|15206039 |aplite | Aplit  | –   | – |  – |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15206040 |pegmatite | Pegmatit  | –   | – |  – |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15206041 |prasinite, indifférenciée | Prasinit  | –   | – |  – |  Cénozoïque     | Protérozoïque   | –  |
|15206042 |serpentinite, indifférenciée | Serpentinit  | –   | – |  – |  Cénozoïque     | Protérozoïque   | –  |
|15206043 |filon minéralisé | Gestein: gangartig  | –   | – |  – |  Cénozoïque     | Protérozoïque   | –  |
|15206044 |microgranite | Granit: mikrokristallin  | –   | – |  – |  Cénozoïque     | Protérozoïque   | Grundgebirge  |
|15206045 |Rhétien, indifférencié | Kalkstein  | Gestein: pelitisch   | Dolomitstein |  – |  Hettangien     | Rhétien   | «Rhät»  |
|15206046 |calcaire biogène (Éocène) | Kalkstein: Bioklasten  | –   | – |  – |  Priabonien     | Lutétien   | «Nummulitikum»  |
|15206047 |rodingite | Rodingit  | –   | – |  – |  Cénozoïque     | Protérozoïque   | Ophiolithische Abfolge  |
|15206048 |filon acide | Gestein: saur-gangartig  | –   | – |  – |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15206049 |filon basique | Gestein: basisch-gangartig  | –   | – |  – |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15206050 |éclogite, indifférenciée | Eklogit  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15206051 |mylonite, indifférenciée | Mylonit  | –   | – |  – |  Cénozoïque     | Protérozoïque   | –  |
|15206052 |roche calcsilicatée | Granofels: Kalksilikat  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15206053 |marbre, indifférencié | Marmor  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15206054 |brèche sédimentaire, indifférenciée | Brekzie: sedimentär  | –   | – |  – |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15206055 |Paléozoïque, indifférencié | Gestein: sedimentär  | Gestein: magmatisch   | Gestein: metamorph |  – |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15206056 |Cénozoïque, indifférencié | Gestein  | –   | – |  – |  Cénozoïque     | Cénozoïque   | Sedimentbedeckung  |
|15206057 |roche ultramafique | Gestein: ultramafisch  | –   | – |  – |  Cénozoïque     | Protérozoïque   | –  |
|15206058 |roche altérée, indifférenciée | Gestein: residual  | –   | – |  – |  Holocène     | Paléozoïque   | –  |
|15206059 |ophicalcite, indifférenciée | Serpentinit: brekziös: Karbonat  | –   | – |  – |  Mésozoïque     | Mésozoïque   | Ophiolithische Abfolge  |
|15206060 |talcschiste, indifférencié | Schiefer: Talk  | –   | – |  – |  Phanérozoïque     | Phanérozoïque   | Sedimentbedeckung  |
|15206061 |microdiorite, indifférenciée | Diorit: mikrokristallin  | –   | – |  – |  Phanérozoïque     | Phanérozoïque   | –  |
|15206062 |quartzite, indifférenciée | Quarzit  | –   | – |  – |  Phanérozoïque     | Phanérozoïque   | –  |
|15206063 |schiste à zoïsite et fuchsite, indifférencié | Schiefer: Zoisit-Fuchsit  | –   | – |  – |  Phanérozoïque     | Phanérozoïque   | –  |
|15206064 |conglomérat, indifférencié | Konglomerat  | –   | – |  – |  Phanérozoïque     | Phanérozoïque   | Sedimentbedeckung  |
|15206065 |schiste à glaucophane, indifférencié | Schiefer: Glaukophan  | –   | – |  – |  Phanérozoïque     | Phanérozoïque   | –  |
|15206066 |Bündnerschiefer, indifférencié | Schiefer: kalkig  | Schiefer: Glimmer   | – |  – |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15206067 |gneiss oeillé, indifférencié | Gneis: augig  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15206068 |micaschistes à grenat, indifférencié | Schiefer: Glimmer-Granat  | –   | – |  – |  Phanérozoïque     | Phanérozoïque   | –  |
|15206069 |schiste à muscovite et albite, indifférencié | Schiefer: Muskovit-Albit  | –   | – |  – |  Phanérozoïque     | Phanérozoïque   | –  |
|15206070 |gneiss, indifférencié | Gneis  | –   | – |  – |  Phanérozoïque     | Phanérozoïque   | Grundgebirge  |
|15206071 |schiste graphiteux, indifférencié | Schiefer: Graphit  | –   | – |  – |  Phanérozoïque     | Phanérozoïque   | –  |
|15206072 |micaschistes, indifférencié | Schiefer: Glimmer  | –   | – |  – |  Mésozoïque     | Protérozoïque   | –  |
|15206073 |Garbenschiefer, indifférencié | Schiefer  | –   | – |  – |  Mésozoïque     | Protérozoïque   | –  |
|15206074 |diorite, indifférenciée | Diorit  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15206075 |gabbro, indifférencié | Gabbro  | –   | – |  – |  Mésozoïque     | Protérozoïque   | –  |
|15206076 |orthogneiss, indifférencié | Gneis: magmatisch  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15206077 |paragneiss, indifférencié | Gneis: sedimentär  | –   | – |  – |  Mésozoïque     | Protérozoïque   | –  |
|15206078 |roche volcanique, indifférenciée | Gestein: vulkanisch  | –   | – |  – |  Cénozoïque     | Protérozoïque   | –  |
|15206079 |basalte, indifférencié | Basalt  | –   | – |  – |  Cénozoïque     | Protérozoïque   | –  |
|15206080 |Carbonifère, indifférencié | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Carbonifère     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15206081 |schiste chloriteux, indifférencié | Schiefer: Chlorit  | –   | – |  – |  Mésozoïque     | Protérozoïque   | –  |
|15206082 |phyllite, indifférenciée | Phyllit  | –   | – |  – |  Mésozoïque     | Protérozoïque   | –  |
|15206083 |quartzphyllite, indifférenciée | Phyllit: Quarz  | –   | – |  – |  Mésozoïque     | Protérozoïque   | –  |
|15206084 |Bündnerschiefer calcaires | Schiefer: kalkig  | –   | – |  – |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15206085 |Bündnerschiefer argileux | Schiefer: tonig  | –   | – |  – |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15206086 |migmatite, indifférenciée | Migmatit  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15206087 |tonalite, indifférenciée | Tonalit  | –   | – |  – |  Cénozoïque     | Paléozoïque   | –  |
|15206088 |syénite, indifférenciée | Syenit  | –   | – |  – |  Paléozoïque     | Paléozoïque   | –  |
|15202431 |Membre de Riondouneire | Kalkstein: mikritisch  | Mergelstein   | Kalkstein: arenitisch |  Riondouneire-Member |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202427 |«Calcarénites beiges oolitiques» | Kalkstein: arenitisch: Bioklasten  | –   | – |  Montsalvens-Kalkarenit |  Barrémien     | Barrémien   | «Urgonien»  |
|15202429 |Formation de Villarbeney | Kalkstein: mikritisch  | Mergelstein   | – |  Villarbeney-Formation |  Aptien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202430 |Membre de la Veveyse de Châtel | Kalkstein: mikritisch  | Mergelstein   | Kalkstein: kieselig |  Veveyse-de-Châtel-Member |  Barrémien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202432 |Formation de la Jogne | Kalkstein: mikritisch  | Mergelstein   | – |  Jogne-Formation |  Tithonien     | Oxfordien   | Malm  |
|15202433 |«Calcaires bréchiques» | Brekzie: kalkig  | –   | – |  Jogne-Formation |  Tithonien     | Tithonien   | Malm  |
|15202434 |Membre des Vuavres | Kalkstein: mikritisch: Chert  | Mergelstein   | – |  Vuavres-Member |  Tithonien     | Kimméridgien   | Malm  |
|15202435 |Membre de la Planière | Kalkstein: mikritisch  | Mergelstein   | – |  Planière-Member |  Oxfordien     | Oxfordien   | Malm  |
|15202436 |Formation de Bifé | Tonstein: schiefrig  | Mergelstein   | Kalkstein: tonig |  Bifé-Formation |  Oxfordien     | Callovien   | Lias-Dogger in pelagischer Fazies  |
|15202437 |«Calcaire à ciment» (Fm. de Bifé) | Kalkstein  | –   | – |  Bifé-Formation |  Oxfordien     | Oxfordien   | Lias-Dogger in pelagischer Fazies  |
|15202438 |Membre de Joux Galez | Mergelstein: Glimmer  | –   | – |  Joux-Galez-Member |  Oxfordien     | Callovien   | Lias-Dogger in pelagischer Fazies  |
|15202439 |Formation de la Pereyre | Kalkstein: spätig: Bioklasten  | Kalkstein: Ooide   | Kalkstein: sandig: Glaukonit |  Pereyres-Formation |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15202440 |Formation de Praz Couquain | Kalkstein: tonig  | Mergelstein: schiefrig   | Kalkstein: sandig: Bioklasten |  Praz-Couquain-Formation |  Bajocien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15202442 |Formation de la Gryonne | Mergelstein: schiefrig  | Kalkstein: mergelig   | Kalkstein: kieselig |  Gryonne-Formation |  Jurassique précoce     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15202443 |Membre du Taffon | Mergelstein: schiefrig  | Kalkstein   | – |  Taffon-Member |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15202444 |Membre des Saix | Sandstein  | Mergelstein: Glimmer   | Kalkstein |  Saix-Member |  Aalénien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15202445 |Membre du Cergnement | Kalkstein: mikritisch  | Mergelstein   | – |  Cergnement-Member |  Barrémien     | Barrémien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202446 |Flysch de la nappe d&#39;Arveyes | Mergelstein  | Sandstein: kalkig: Glimmer   | – |  Arveyes-Flysch |  Eocène     | Eocène   | Flysch  |
|15202447 |Flysch de la nappe du Sex Mort | Mergelstein  | Sandstein: kalkig: Bioklasten   | – |  Sex-Mort-Flysch |  Priabonien     | Priabonien   | Flysch  |
|15202448 |Méta-andésite du Maasplanggstock | Andesit  | –   | – |  Maasplanggstock-Metaandesit |  Cisuralien     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202449 |Diorite du Dammagletscher | Diorit  | –   | – |  Dammagletscher-Diorit |  Pennsylvanien tardif     | Pennsylvanien tardif   | Mittelvariszisches Grundgebirge  |
|15202450 |Lias des Mines schisteux | Mergelstein: schiefrig  | –   | – |  Gryonne-Formation |  Toarcien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202451 |Lias des Mines calcaire | Kalkstein: kieselig  | Mergelstein   | – |  Gryonne-Formation |  Pliensbachien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15202452 |Lias des Mines basal | Kalkstein: Bioklasten  | Mergelstein: sandig: Glimmer   | – |  Gryonne-Formation |  Hettangien     | Rhétien   | «Rhät»  |
|15202453 |base tectonisée du Verrucano de Glaris («Plagioklasgneis») | Schiefer: konglomeratisch  | Gneis: mylonitisch   | – |  – |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202454 |Migmatite du Chrüzlistock | Migmatit  | Gneis: migmatitisch   | – |  Chrüzlistock-Migmatit |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202455 |Complexe gneissique du Piz Cuolmet | Gneis: migmatitisch  | Gneis: gebändert   | Schiefer: Serizit-Chlorit |  Piz-Cuolmet-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202456 |Pulanera-Gneiskomplex | Gneis  | Schiefer   | – |  Pulanera-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202465 |Permo-Carbonifère du massif des Aiguilles Rouges | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Permien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202467 |Variszisches Kristallin des Helvetikums | Gneis  | Schiefer   | Gestein: magmatisch |  – |  Paléozoïque     | Protérozoïque   | Variszisches Grundgebirge  |
|15202468 |Socle polycyclique anté-varisque de l&#39;Helvétique | Gneis  | Schiefer   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202469 |Socle cristallin indifférencié de l&#39;Helvétique | Gneis  | Schiefer   | Gestein: magmatisch |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15202472 |Complexe gneissique du Catogne | Migmatit  | Gneis: migmatitisch   | Amphibolit |  Catogne-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202473 |Leucogranite des Grépillons | Granit: mikrokristallin-porphyrisch  | –   | – |  Grépillons-Leukogranit |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202474 |Leucogranite d&#39;Arpette | Granit: mikrokristallin  | –   | – |  Arpette-Leukogranit |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202475 |Gneiss oeillé de Bitschji | Gneis: augig  | –   | – |  Bitschji-Augengneis |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202476 |Gneiss oeillé de Geimen | Gneis: augig  | –   | – |  Geimen-Augengneis |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202477 |Socle polycyclique anté-varisque du massif du Mont Blanc, migmatitique | Migmatit  | Gneis   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202478 |Socle polycyclique anté-varisque du massif du Mont Blanc, riche en amphibolites | Gneis: migmatitisch  | Amphibolit   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202479 |Socle polycyclique anté-varisque du massif du Mont Blanc, mylonitique | Gneis: mylonitisch  | Mylonit   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202480 |Microgranite de Morcles | Granit: mikrokristallin  | –   | – |  Morcles-Mikrogranit |  Pennsylvanien tardif     | Pennsylvanien tardif   | Mittelvariszisches Grundgebirge  |
|15202481 |Socle polycyclique anté-varisque du massif des Aiguilles Rouges, migmatitique | Migmatit  | Gneis   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202482 |Complexe gneissique de Fully | Migmatit  | –   | – |  Fully-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202483 |Granite d&#39;Hinterbalm | Granit  | –   | – |  Hinterbalm-Granit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202484 |Granite de la Balmenegg | Granit: porphyrisch: Biotit  | –   | – |  Balmenegg-Granit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202485 |faciès d&#39;Unter-der-Flue | Granit: aplitisch  | –   | – |  Unter-der-Flue-Granit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202486 |Granite du (Piz) Pardatschas | Granit  | Granit: mylonitisch   | – |  Pardatschas-Granit |  Mississippien tardif     | Mississippien tardif   | Frühvariszisches Grundgebirge  |
|15202487 |Diorite du Rossbodenstock | Diorit: Quarz-Biotit  | –   | – |  Rossbodenstock-Diorit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202488 |Diorite du Val da Surplattas | Diorit  | –   | – |  Val-da-Surplattas-Diorit |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15202489 |Microgranite de Rinderbiel | Granit: mikrokristallin-porphyrisch  | –   | – |  Rinderbiel-Mikrogranit |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202490 |Dachquarzit (Leventina) | Quarzit  | –   | – |  – |  Trias     | Trias   | Detritische Trias  |
|15202491 |Formation de Kapfen | Konglomerat  | Sandstein   | – |  Kapfen-Formation |  Lopingien     | Guadalupien   | Spät- bis postvariszisches Grundgebirge  |
|15202492 |Grès de Kapfen | Sandstein  | –   | – |  Kapfen-Formation |  Lopingien     | Guadalupien   | Spät- bis postvariszisches Grundgebirge  |
|15202493 |Sernifite du Kärpfgipfel | Konglomerat  | –   | – |  Kärpfgipfel-Sernifit |  Lopingien     | Guadalupien   | Spät- bis postvariszisches Grundgebirge  |
|15202494 |Formation du Fulen | Tonstein: sandig-schiefrig  | –   | – |  Fulen-Formation |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15202495 |Membre de Glattmatt | Tonstein  | Sandstein   | Brekzie |  Glattmatt-Member |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202496 |Kératophyre du Hahnenstock | Trachyt  | –   | – |  Hahnenstock-Keratophyr |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202497 |Horizons du Sonnenberg | Sandstein: Feldspat  | Kalkstein   | Tonstein: siltig-schiefrig |  Sonnenberg-Horizonte |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202498 |Conglomérat du Chamseeli | Konglomerat  | –   | – |  Chamseeli-Konglomerat |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202499 |Grès du Rotberg | Sandstein  | –   | – |  Rotberg-Sandstein |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202500 |Membre de Seez | Konglomerat  | –   | – |  Seez-Member |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202501 |Membre de la Gufelialp | Brekzie: siltig  | Tonstein   | Siltstein |  Gufelialp-Member |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202505 |Microgranite de la Windgällenlücke | Granit: mikrokristallin-porphyrisch  | –   | – |  Windgällen-Formation |  Pennsylvanien tardif     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15204020 |Formation d&#39;Agnelli | Kalkstein: kieselig  | Kalkstein: spätig: Bioklasten   | – |  Agnelli-Formation |  Toarcien     | Sinémurien   | Syn-Rift  |
|15204017 |Membre du (Piz) Mezzaun | Kalkstein: kieselig  | Mergelstein   | – |  Mezzaun-Member |  Callovien     | Aalénien   | Syn-Rift  |
|15204018 |Membre du (Piz) Blaisun | Mergelstein: schiefrig  | Kalkstein: kieselig   | – |  Blaisun-Member |  Toarcien     | Toarcien   | Syn-Rift  |
|15204019 |Membre du (Val) Trupchun | Kalkstein: siltig  | Kalkstein: kieselig   | Brekzie: kalkig |  Trupchun-Member |  Pliensbachien     | Sinémurien   | Syn-Rift  |
|15204021 |Calcaire d&#39;Adnet | Kalkstein  | Mergelstein   | – |  Agnelli-Formation |  Toarcien     | Sinémurien   | Syn-Rift  |
|15204022 |Calcaire de Hierlatz | Kalkstein: spätig: Echinodermen  | –   | – |  Agnelli-Formation |  Pliensbachien     | Sinémurien   | Syn-Rift  |
|15204023 |Brèche d&#39;Alv | Brekzie: kalkig-dolomitisch  | –   | – |  Alv-Brekzie |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15204024 |Formation de Kössen | Tonstein  | Kalkstein: Bioklasten   | – |  Kössen-Formation |  Rhétien     | Norien   | «Rhät»  |
|15204025 |Calcaire du Zirmenkopf | Kalkstein: Korallen  | Mergelstein   | – |  Zirmenkopf-Kalk |  Rhétien     | Norien   | «Rhät»  |
|15204026 |Membre du (Piz) Mitgel | Kalkstein  | Dolomitstein: kalkig   | Mergelstein: siltig |  Mitgel-Member |  Rhétien     | Norien   | «Rhät»  |
|15204027 |Membre de Ramoz | Mergelstein  | Kalkstein   | – |  Ramoz-Member |  Rhétien     | Norien   | «Rhät»  |
|15204028 |Membre du Schesaplana | 15111272  | Kalkstein: Korallen   | – |  Schesaplana-Member |  Rhétien     | Norien   | «Rhät»  |
|15204029 |Membre de l&#39;Alplihorn | Tonstein: schiefrig  | Kalkstein: mergelig-schiefrig   | Kalkstein |  Alplihorn-Member |  Rhétien     | Norien   | «Rhät»  |
|15204030 |Hauptdolomit-Gruppe | Dolomitstein  | Brekzie   | – |  – |  Norien     | Norien   | Hauptdolomit  |
|15204031 |Calcaire plaqueté du (Piz) Murtèr | Kalkstein: mikritisch: Bioklasten-Chert  | Kalkstein: mergelig   | Tonstein |  Murtèr-Plattenkalk |  Norien     | Norien   | Hauptdolomit  |
|15204032 |Dolomie du Murteret | Dolomitstein  | –   | – |  Murteret-Dolomit |  Norien     | Norien   | Hauptdolomit  |
|15204033 |Formation du (Piz dal) Diavel | Kalkstein: kieselig  | Mergelstein   | – |  Diavel-Formation |  Norien     | Norien   | Hauptdolomit  |
|15204034 |Formation du (Piz) Quattervals | 15111227  | Brekzie   | Kalkstein: Bioklasten |  Quattervals-Formation |  Norien     | Norien   | Hauptdolomit  |
|15204035 |Marne de la Crappa Mala | Mergelstein  | Tonstein   | Kalkstein: tonig |  Crappa-Mala-Mergel |  Norien     | Norien   | Hauptdolomit  |
|15204036 |Membre de Pra Grata | Kalkstein: spätig: Chert  | Dolomitstein   | Brekzie |  Pra-Grata-Member |  Norien     | Norien   | Hauptdolomit  |
|15204037 |Dolomie du (Val) Müschauns | Dolomitstein: spätig  | –   | – |  Müschauns-Dolomit |  Norien     | Norien   | Hauptdolomit  |
|15204038 |Groupe de Raibl | Evaporit: Gips  | Dolomitstein   | Rauwacke |  – |  Carnien     | Ladinien   | Raibl  |
|15204039 |Formation de Fanez | Sandstein  | Tonstein: schiefrig   | Dolomitstein: stromatolithisch |  Fanez-Formation |  Carnien     | Carnien   | Raibl  |
|15204040 |Membre de la Valbella | Brekzie: polymikt  | –   | – |  Valbella-Member |  Carnien     | Carnien   | Raibl  |
|15204041 |Dolomie de Fanez | Dolomitstein  | –   | – |  Fanez-Formation |  Carnien     | Carnien   | Raibl  |
|15204042 |Membre du (Piz) Mezdi | Tonstein  | Kalkstein: Bioklasten-Ooide   | – |  Mezdi-Member |  Carnien     | Carnien   | Raibl  |
|15204043 |Membre du Val Cluozza | Sandstein: Feldspat  | Siltstein   | Dolomitstein |  Cluozza-Member |  Carnien     | Carnien   | Raibl  |
|15204044 |Membre de Stugl | Evaporit: Gips  | –   | – |  Stugl-Gips |  Carnien     | Carnien   | Raibl  |
|15204045 |Formation du Val Mingèr | Dolomitstein  | Rauwacke   | – |  Minger-Formation |  Carnien     | Ladinien   | Raibl  |
|15204046 |Dolomie du Val Mingèr | Dolomitstein  | –   | – |  Minger-Formation |  Carnien     | Ladinien   | Raibl  |
|15204047 |Membre du Val Mora | Rauwacke  | Tonstein: schiefrig   | Dolomitstein |  Mora-Member |  Carnien     | Ladinien   | Raibl  |
|15204048 |Formation du (Monte) Garone | Rauwacke  | Tonstein   | Dolomitstein |  Garone-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204049 |Formation de l&#39;Arlberg | Kalkstein  | Tonstein   | Dolomitstein |  Arlberg-Formation |  Carnien     | Ladinien   | Karbonatische Trias  |
|15204050 |Formation de la Partnach | Mergelstein: schiefrig  | Tonstein: kieselig   | – |  Partnach-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204051 |Formation de l&#39;Altein | Dolomitstein  | Kalkstein: Chert   | Tonstein |  Altein-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204052 |Membre de la Parai Alba | 15111282  | Tonstein   | Tuff: vulkanisch |  Parai-Alba-Member |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204053 |Formation du (Piz) Prosanto | Kalkstein: Bitumen  | Dolomitstein   | Tonstein |  Prosanto-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204054 |Formation du (Piz) Vallatscha | Dolomitstein: stromatolithisch  | Brekzie: dolomitisch   | – |  Vallatscha-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204055 |Brèche du Tiaun | Brekzie  | –   | – |  Tiaun-Brekzie |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204056 |Membre du (Piz) Vallatscha | Dolomitstein  | –   | – |  Vallatscha-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204057 |Membre du (Piz) Turettas | 15111279  | Dolomitstein: Ooide   | Rauwacke |  Turettas-Member |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204058 |Membre de la Landwasser | Dolomitstein  | –   | – |  Landwasser-Member |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204059 |Formation de S-charl | Dolomitstein  | Kalkstein   | – |  S-charl-Formation |  Ladinien     | Anisien   | Karbonatische Trias  |
|15204060 |Membre du Sertig | Kalkstein  | Kalkstein: Ooide   | – |  Sertig-Member |  Ladinien     | Anisien   | Karbonatische Trias  |
|15204061 |Membre de Ravais-ch | Dolomitstein  | Sandstein   | Rauwacke |  Ravais-ch-Member |  Ladinien     | Anisien   | Karbonatische Trias  |
|15204062 |Formation de Reiflingen | Kalkstein: mikritisch  | Kalkstein: spätig: Bioklasten   | Tuffit |  Reiflingen-Formation |  Ladinien     | Anisien   | Karbonatische Trias  |
|15204063 |Formation du (Piz) Ducan | Dolomitstein  | Dolomitstein: sandig   | Sandstein |  Ducan-Formation |  Anisien     | Anisien   | Karbonatische Trias  |
|15204064 |Trochitendolomit-Member | 15111293  | –   | – |  «Trochitendolomit-Member» |  Anisien     | Anisien   | Karbonatische Trias  |
|15204065 |Brachiopodenkalk-Member | Kalkstein: Bioklasten-Chert  | Kalkstein: siltig-tonig   | – |  «Brachiopodenkalk-Member» |  Anisien     | Anisien   | Karbonatische Trias  |
|15204066 |Eisendolomit-Member | Dolomitstein: Bioklasten  | –   | – |  «Eisendolomit-Member» |  Anisien     | Anisien   | Karbonatische Trias  |
|15204067 |Gracilis-Member | 15111286  | Dolomitstein: stromatolithisch   | – |  «Gracilis-Member» |  Anisien     | Anisien   | Karbonatische Trias  |
|15204068 |Formation de Gutenstein | Kalkstein  | Dolomitstein: spätig   | – |  Gutenstein-Formation |  Ladinien     | Anisien   | Karbonatische Trias  |
|15204069 |Formation de Reichenhall | 15111298  | Dolomitstein   | Brekzie: dolomitisch |  Reichenhall-Formation |  Anisien     | Olénékien   | Karbonatische Trias  |
|15204070 |Formation du Fuorn | Sandstein: Quarz  | Siltstein   | Dolomitstein |  Fuorn-Formation |  Anisien     | Trias précoce   | Detritische Trias  |
|15204071 |Membre de Punt la Drossa | Sandstein: kalkig  | Dolomitstein   | Rauwacke |  Punt-la-Drossa-Member |  Anisien     | Trias précoce   | Detritische Trias  |
|15204072 |Pflanzenquarzit (Fm. du Fuorn) | Sandstein: Quarz  | –   | – |  «Pflanzenquarzit» |  Anisien     | Trias précoce   | Detritische Trias  |
|15204073 |Membre inférieur de la Fm. du Fuorn | Sandstein: kalkig  | Siltstein   | – |  Fuorn-Formation |  Trias précoce     | Trias précoce   | Detritische Trias  |
|15204074 |Groupe du Val Müstair | Konglomerat  | Sandstein   | Rhyolith |  – |  Trias précoce     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15204075 |Formation de Chazforà | Konglomerat  | Sandstein   | Siltstein |  Chazforà-Formation |  Trias précoce     | Lopingien   | Spät- bis postvariszisches Grundgebirge  |
|15204076 |Membre du (Val) Tuors | Sandstein  | Konglomerat: Quarz   | – |  Tuors-Member |  Trias précoce     | Trias précoce   | Spät- bis postvariszisches Grundgebirge  |
|15204077 |Membre du Val Püra | Brekzie  | –   | – |  Val-Püra-Member |  Lopingien     | Lopingien   | Spät- bis postvariszisches Grundgebirge  |
|15206089 |tectonite, indifférenciée | Gestein: tektonisch  | –   | – |  – |  Cénozoïque     | Protérozoïque   | –  |
|15206090 |cornéenne, indifférenciée | Hornfels  | –   | – |  – |  Cénozoïque     | Protérozoïque   | –  |
|15206091 |gneiss à hornblende, indifférencié | Gneis: Hornblende  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15206092 |gneiss à biotite et plagioclase, indifférencié | Gneis: Biotit-Plagioklas  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15206093 |gneiss rubané, indifférencié | Gneis: gebändert  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15206094 |gneiss à deux micas, indifférencié | Gneis: Biotit-Muskovit  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15206095 |gneiss phyllitique, indifférencié | Gneis: phyllitisch  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15206096 |péridotite, indifférencié | Peridotit  | –   | – |  – |  Mésozoïque     | Protérozoïque   | –  |
|15206097 |amphibolite rubanée et à blocs, indifférencié | Amphibolit  | –   | – |  – |  Mésozoïque     | Protérozoïque   | Grundgebirge  |
|15206098 |amphibolite à grenat, indifférencié | Amphibolit: Granat  | –   | – |  – |  Mésozoïque     | Protérozoïque   | Grundgebirge  |
|15206099 |filon diabasique, indifférencié | Basalt  | –   | – |  – |  Mésozoïque     | Protérozoïque   | –  |
|15206100 |Permien, indifférencié | Sandstein  | Konglomerat   | Gestein: vulkanisch |  – |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15206101 |marbre calcaire, indifférencié | Marmor: kalkig  | –   | – |  – |  Mésozoïque     | Paléozoïque   | –  |
|15206103 |Permo-Carbonifère, indifférencié | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Permien     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15206104 |calcschiste, indifférencié | Schiefer: kalkig  | –   | – |  – |  Cénozoïque     | Paléozoïque   | –  |
|15206105 |grès, indifférencié | Sandstein  | –   | – |  – |  Cénozoïque     | Paléozoïque   | Sedimentbedeckung  |
|15206106 |schiste argileux, indifférencié | Schiefer: tonig  | –   | – |  – |  Mésozoïque     | Protérozoïque   | –  |
|15206107 |radiolarite, indifférenciée | Gestein: kieselig: Radiolarien  | –   | – |  – |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15206108 |calcaire, indifférencié | Kalkstein  | –   | – |  – |  Cénozoïque     | Paléozoïque   | Sedimentbedeckung  |
|15206109 |gneiss conglomératique, indifférencié | Gneis: psephitisch  | –   | – |  – |  Mésozoïque     | Protérozoïque   | –  |
|15206110 |socle polycyclique anté-varisque, indifférencié | Gneis  | Schiefer   | Amphibolit |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15206111 |schiste, indifférencié | Schiefer  | –   | – |  – |  Mésozoïque     | Protérozoïque   | –  |
|15206112 |gneiss aplitique, indifférencié | Gneis: aplitisch  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15206113 |Undifferenzierte lithologische Einheit: Süsswasserkalk | Kalkstein  | –   | – |  – |  Tertiaire     | Tertiaire   | Sedimentbedeckung  |
|15206114 |mélange tectonique | Tonstein: schiefrig  | –   | – |  – |  Néogène     | Paléogène   | Mélange  |
|15206115 |Flysch, indifférencié | Sandstein  | Gestein: pelitisch   | – |  – |  Paléogène     | Crétacé tardif   | Flysch  |
|15206116 |Calcaire à aptychus, indiff. | Kalkstein: mikritisch: Aptychen  | –   | – |  – |  Crétacé précoce     | Jurassique tardif   | Sedimentbedeckung  |
|15206117 |Grès quartzitique, indiff. | Sandstein: Quarz  | –   | – |  – |  Trias     | Trias   | Sedimentbedeckung  |
|15206118 |Undifferenzierte lithologische Einheit: Mergelstein | Mergelstein  | –   | – |  – |  Cénozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15206119 |Undifferenzierte lithologische Einheit: Basisches Gestein | Gestein: basisch  | –   | – |  – |  Cénozoïque     | Präkambrium   | –  |
|15200001 |Formation du Twannbach | Kalkstein: mikritisch  | Dolomitstein   | Kalkstein: stromatolithisch |  Twannbach-Formation |  Tithonien     | Kimméridgien   | Malm  |
|15200002 |Formation de Reuchenette | Kalkstein: mikritisch  | Kalkstein: Bioklasten   | Mergelstein |  Reuchenette-Formation |  Kimméridgien     | Kimméridgien   | Malm  |
|15200003 |Formation de Courgenay | Kalkstein: mikritisch  | Kalkstein: kreidig   | – |  Courgenay-Formation |  Kimméridgien     | Oxfordien   | Malm  |
|15200004 |Formation de Vellerat | Kalkstein: mergelig  | Kalkstein: mikritisch   | Mergelstein |  Vellerat-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15200005 |Formation de St-Ursanne | Kalkstein: Korallen  | Kalkstein: Ooide   | Kalkstein: arenitisch: Bioklasten |  St-Ursanne-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15200006 |Formation de Bärschwil | Tonstein: mergelig  | Mergelstein   | Kalkstein: Chert |  Bärschwil-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15200007 |Formation d&#39;Ifenthal | Mergelstein  | Kalkstein: Eisenooide   | Mergelstein: Bioklasten |  Ifenthal-Formation |  Callovien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200008 |Hauptrogenstein | Kalkstein: Ooide  | Kalkstein: Bioklasten   | Mergelstein |  Hauptrogenstein |  Bathonien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200009 |Formation du Passwang | Tonstein  | Mergelstein: Eisenooide   | Kalkstein: sandig: Bioklasten |  Passwang-Formation |  Bathonien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15200010 |Argile à Opalinus | Tonstein  | Mergelstein: siltig   | Siltstein: Glimmer |  Opalinus-Ton |  Aalénien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15200011 |Formation de la Staffelegg | Mergelstein  | Kalkstein   | Sandstein: kalkig |  Staffelegg-Formation |  Toarcien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15200012 |Malm du Jura | Kalkstein  | Mergelstein   | – |  – |  Tithonien     | Oxfordien   | Malm  |
|15200013 |Membre de Vouglans | Kalkstein: mikritisch  | Dolomitstein   | – |  Vouglans-Member |  Tithonien     | Tithonien   | Malm  |
|15200014 |Membre du Chailley | Dolomitstein  | Kalkstein: stromatolithisch   | Kalkstein: Bioklasten |  Chailley-Member |  Tithonien     | Kimméridgien   | Malm  |
|15200015 |Marnes à Virgula supérieures | Mergelstein: Bioklasten  | –   | – |  «Oberer Virgula-Mergel» |  Kimméridgien     | Kimméridgien   | Malm  |
|15200016 |Banc à Nérinées du sommet | Kalkstein: Bioklasten  | –   | – |  «Grenznerineen-Bank» |  Kimméridgien     | Kimméridgien   | Malm  |
|15200017 |Calcaire à Cladocoropsis | Kalkstein: Bioklasten  | –   | – |  «Cladocoropsis-Kalk» |  Kimméridgien     | Kimméridgien   | Malm  |
|15200018 |Marnes à Virgula inférieures | Mergelstein: Bioklasten  | –   | – |  «Unterer Virgula-Mergel» |  Kimméridgien     | Kimméridgien   | Malm  |
|15200019 |Membre de Courtedoux | Kalkstein: Bioklasten  | –   | – |  Courtedoux-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200020 |Membre du Banné | Mergelstein: Bioklasten  | Kalkstein: mergelig   | – |  Banné-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200021 |Membre de Vabenau | Kalkstein: mikritisch  | Kalkstein: mergelig   | – |  Vabenau-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200022 |Couches du Creugenat | Mergelstein: Bioklasten  | Kalkstein: mergelig   | – |  Creugenat-Schichten |  Kimméridgien     | Kimméridgien   | Malm  |
|15200023 |Formation des Etiollets | Kalkstein: mikritisch  | Kalkstein: Korallen   | Mergelstein |  Etiollets-Formation |  Kimméridgien     | Kimméridgien   | Malm  |
|15200024 |Complexe récifal (Fm. des Etiollets) | Kalkstein: Korallen  | Kalkstein: mikritisch   | Kalkstein: arenitisch |  «Complexe récifal» |  Kimméridgien     | Kimméridgien   | Malm  |
|15200025 |Membre du Couvaloup | Mergelstein  | Kalkstein: mikritisch   | – |  Couvaloup-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200026 |Membre de Porrentruy | Kalkstein: kreidig  | Kalkstein: arenitisch   | – |  Porrentruy-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200027 |Membre de la May | Kalkstein: mikritisch  | –   | – |  La-May-Member |  Kimméridgien     | Oxfordien   | Malm  |
|15200028 |Membre de l&#39;Oolithe rousse | Kalkstein: Ooide  | –   | – |  «Oolithe-Rousse-Member» |  Oxfordien     | Oxfordien   | Malm  |
|15200029 |Membre de Bure | Mergelstein: kalkig  | –   | – |  Bure-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200030 |Membre du Hauptmumienbank (Oolithe nuciforme) | Kalkstein: mikritisch: Onkoide  | –   | – |  «Hauptmumienbank-Member» |  Oxfordien     | Oxfordien   | Malm  |
|15200031 |Membre de Röschenz | Kalkstein: mergelig: Bioklasten  | Kalkstein: Bioklasten   | – |  Röschenz-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200032 |Membre du Vorbourg | Kalkstein: mikritisch  | –   | – |  Vorbourg-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200033 |Membre du Tiergarten | Kalkstein: Ooide  | Kalkstein: Korallen   | – |  Tiergarten-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200034 |Membre de Buix | Kalkstein: kreidig: Chert  | Kalkstein: Korallen   | – |  Buix-Member |  Oxfordien     | Oxfordien   | Malm  |
|15202509 |Grès du Guschakopf | Sandstein: Quarz  | –   | – |  Guschakopf-Sandstein |  Paléogène     | Paléogène   | «Nummulitikum»  |
|15202506 |Rhyolithe de la Sandalp | Rhyolith  | –   | – |  Sandalp-Rhyolith |  Assélien     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202507 |Tuffitisches Member (Tscharren) | Tuffit  | –   | – |  Tscharren-Formation |  Pennsylvanien tardif     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202508 |Ignimbritisches Member (Tscharren) | Ignimbrit  | –   | – |  Tscharren-Formation |  Pennsylvanien tardif     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202510 |Horizon du Gonzen | Kalkstein: Eisenooide  | –   | – |  Gonzen-Eisenerzhorizont |  Kimméridgien     | Oxfordien   | Malm  |
|15202511 |Schabell-Melange | Tonstein  | Mergelstein   | Sandstein |  Schabell-Melange |  Rupélien     | Priabonien   | Mélange  |
|15202512 |Taveyannaz-Fm.: Dachschiefer-Fazies | Tonstein: schiefrig  | Sandstein: tonig   | – |  Taveyannaz-Formation |  Rupélien     | Priabonien   | Flysch  |
|15202513 |Helvetischer Kieselkalk: Oberer Teil | Kalkstein: kieselig: Bioklasten  | Kalkstein: spätig: Bioklasten   | Mergelstein |  15253100 |  Hauterivien     | Hauterivien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202514 |Helvetischer Kieselkalk: Unterer Teil | Kalkstein: kieselig: Bioklasten  | Kalkstein: spätig: Bioklasten   | Mergelstein |  15253100 |  Hauterivien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202515 |Helvetischer Kieselkalk: Basisschiefer | Mergelstein: kieselig  | –   | – |  15253100 |  Hauterivien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202516 |Torrenthorn-Fm.: Torrentalp-Mb.: Schiefer-Fazies | Tonstein  | Kalkstein: mergelig   | – |  Torrentalp-Member |  Aalénien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15202517 |Torrenthorn-Fm.: Torrentalp-Mb.: Spatkalk-Fazies | Kalkstein: spätig  | –   | – |  Torrentalp-Member |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15202518 |Torrenthorn-Fm.: Torrentalp-Mb.: Sandstein-Fazies | Sandstein: kalkig-kieselig  | –   | – |  Torrentalp-Member |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202519 |Torrenthorn-Fm.: Galm-Mb.: Spatkalk-Fazies | Kalkstein: sandig-spätig  | –   | – |  Galm-Member |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202520 |Torrenthorn-Fm.: Galm-Mb.: Sandstein-Fazies | Sandstein: kalkig-kieselig  | –   | – |  Galm-Member |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202521 |Meilleret-Fm.: Iserin-Konglomerat | Konglomerat: polymikt  | –   | – |  Iserin-Konglomerat |  Priabonien     | Lutétien   | Flysch  |
|15202522 |Meilleret-Fm.: Biodetritischer Kalkstein | Kalkstein: arenitisch: Bioklasten  | –   | – |  Meilleret-Formation |  Priabonien     | Lutétien   | Flysch  |
|15202523 |Meilleret-Fm.: Arkose | Sandstein: Feldspat  | Sandstein: Quarz   | – |  Meilleret-Formation |  Priabonien     | Lutétien   | Flysch  |
|15202524 |Meilleret-Fm.: Basales Konglomerat | Konglomerat  | –   | – |  Meilleret-Formation |  Priabonien     | Lutétien   | Flysch  |
|15202525 |Bommerstein-Fm.: Glockhaus-Mb.: Grenzquarzit | Sandstein: Quarz  | Kalkstein: sandig-spätig   | – |  «Grenzquarzit» (Bommerstein-Fm.) |  Bajocien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15202526 |Telltistock-Granit | Granit: Biotit  | Granit: mylonitisch   | – |  Telltistock-Granit |  Pennsylvanien tardif     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202527 |Formation de l&#39;Öhrli, à infiltrations de Sidérolithique | Kalkstein  | Gestein: residual: Eisenmineralien   | – |  Öhrli-Formation |  Eocène     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202528 |faciès de Beesten | Granit: porphyrisch  | –   | – |  Beesten-Granit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202529 |Diorite de Garwiidi | Diorit: Quarz-Hornblende  | –   | – |  Garwiidi-Diorit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202530 |Granite de l&#39;Alp Crap Ner | Granit  | –   | – |  Alp-Crap-Ner-Granit |  Mississippien moyen     | Mississippien moyen   | Frühvariszisches Grundgebirge  |
|15202531 |Migmatite d&#39;Innertkirchen, à altération permienne | Gestein: residual  | Migmatit   | Gneis |  Innertkirchen-Migmatit |  Permien     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202532 |Complexe gneissique d&#39;Erstfeld, à altération permienne | Gestein: residual  | Gneis   | – |  Erstfeld-Gneiskomplex |  Permien     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202533 |Flysch du Suren | Sandstein: tonig  | Tonstein: schiefrig   | – |  Suren-Flysch |  Eocène moyen     | Yprésien   | Flysch  |
|15202534 |Obere Sandsteine (Spirstock) | Sandstein: kalkig: Quarz  | Konglomerat: polymikt   | – |  Spirstock-Member |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202535 |Blockmergel (Spirstock) | Mergelstein: konglomeratisch  | –   | – |  Spirstock-Member |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202536 |Untere Sandsteine (Spirstock) | Sandstein: Feldspat  | Mergelstein: schiefrig   | – |  Spirstock-Member |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202537 |Couches de Ringgenberg | Kalkstein: mikritisch  | Mergelstein: schiefrig   | – |  Ringgenberg-Schichten |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202538 |Brèche du Malm | Brekzie: kalkig  | Brekzie: dolomitisch   | – |  Quinten-Formation |  Tithonien     | Kimméridgien   | Malm  |
|15202539 |Calcaire marneux du Schattwald | Kalkstein: mergelig  | Kalkstein: mikritisch   | – |  Schattwald-Mergelkalk |  Crétacé précoce     | Tithonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202540 |Formations d&#39;Elm et de Matt, indifférenciées | Sandstein: Quarz  | Sandstein: tonig   | Tonstein |  – |  Rupélien     | Priabonien   | Flysch  |
|15202541 |Formations d&#39;Elm et de Matt: grès quartzitique | Sandstein: Quarz  | –   | – |  – |  Rupélien     | Priabonien   | Flysch  |
|15202542 |Formations d&#39;Elm et de Matt: argillite schisteuse | Tonstein: schiefrig  | –   | – |  – |  Rupélien     | Priabonien   | Flysch  |
|15202543 |Schistes de la Schwalmern | Mergelstein: schiefrig  | –   | – |  Tierwis-Formation |  Barrémien     | Barrémien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202544 |Calcaire de la Schwalmern | Mergelstein: kalkig-kieselig  | Kalkstein: spätig: Bioklasten   | Kalkstein: sandig |  Tierwis-Formation |  Barrémien     | Barrémien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202545 |Membre du Glockhaus: grès ferrugineux schisteux | Sandstein: Eisenmineralien  | –   | – |  Glockhaus-Member |  Bajocien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15202546 |Dolomie du Trias helvétique | Dolomitstein  | –   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15202547 |Cornieule du Trias helvétique | Rauwacke  | –   | – |  – |  Trias     | Trias   | Prä-Rift  |
|15202548 |Gypse du Trias helvétique | Evaporit: Gips  | –   | – |  – |  Trias     | Trias   | Prä-Rift  |
|15202549 |Granodiorite de Baltschieder: tonalite à biotite | Tonalit: Biotit  | –   | – |  Baltschieder-Granodiorit |  Mississippien     | Mississippien   | Prävariszisches Grundgebirge  |
|15202550 |Granodiorite de Baltschieder: tonalite à biotite et horneblende | Tonalit: Biotit-Hornblende  | –   | – |  Baltschieder-Granodiorit |  Mississippien     | Mississippien   | Prävariszisches Grundgebirge  |
|15202551 |Complexe gneissique d&#39;Erstfeld: gneiss à plagioclase et biotite | Gneis: migmatitisch  | Migmatit   | – |  Erstfeld-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202552 |Complexe gneissique d&#39;Erstfeld: orthogneiss | Gneis: granitisch  | –   | – |  Erstfeld-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202553 |Complexe gneissique d&#39;Erstfeld: migmatite | Migmatit  | –   | – |  Erstfeld-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202554 |Complexe gneissique de Guttannnen: paragneiss | Gneis: sedimentär  | –   | – |  Guttannen-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202555 |Complexe gneissique de Guttannnen: orthogneiss | Gneis: magmatisch  | –   | – |  Guttannen-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202556 |Complexe gneissique de Guttannnen: schiste à chlorite et biotite | Schiefer  | Gneis   | – |  Guttannen-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202557 |Complexe gneissique de Guttannnen: schiste à séricite et chlorite | Schiefer  | Gneis   | – |  Guttannen-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202558 |Complexe gneissique du Lötschental: gneiss à muscovite | Gneis: Muskovit  | –   | – |  Lötschental-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202559 |Complexe gneissique du Lötschental: gneiss à biotite migmatitique | Gneis: migmatitisch  | –   | – |  Lötschental-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202560 |Complexe gneissique du Lötschental: schiste à chlorite | Schiefer: Chlorit  | –   | – |  Lötschental-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202561 |Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: gneiss rubané à plagioclase et biotite | Gneis: gebändert  | Migmatit   | – |  Ofenhorn-Stampfhorn-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202562 |Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: migmatite | Migmatit  | Gneis   | – |  Ofenhorn-Stampfhorn-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202563 |Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: gneiss à biotite | Gneis: Biotit  | –   | – |  Ofenhorn-Stampfhorn-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202564 |Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: orthogneiss | Gneis: magmatisch  | –   | – |  Ofenhorn-Stampfhorn-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202565 |Complexe gneissique de la Bäregg: orthogneiss mylonitique | Gneis: mylonitisch  | –   | – |  Bäregg-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202566 |Complexe gneissique de la Bäregg: paragneiss mylonitique | Gneis: mylonitisch  | –   | – |  Bäregg-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202567 |Complexe gneissique de la Bäregg: métavulcanite | Gestein: vulkanisch  | –   | – |  Bäregg-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202568 |Granodiorite du Grimsel: faciès aplitique de bordure | Granit: aplitisch  | –   | – |  Grimsel-Granodiorit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15204081 |Membre de Bellaluna | Rhyolith  | Dazit: rhyolithisch   | – |  Bellaluna-Member |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15204078 |Formation de Präbichl | Konglomerat: polymikt  | Sandstein: tonig: Lithoklasten   | Tonstein: schiefrig |  Präbichl-Formation |  Trias précoce     | Permien   | Grundgebirge  |
|15204079 |Formation de la Ruina | Rhyolith  | Dazit: rhyolithisch   | Tuff: vulkanisch |  Ruina-Formation |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15204080 |Membre du Sandhubel | Ignimbrit  | Tuff: vulkanisch   | – |  Sandhubel-Member |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15204082 |Gneiss oeillé de la Mönchalp | 15111535  | –   | – |  Mönchalp-Augengneis |  Cambrien     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15204083 |Gneiss oeillé de Tschuggen | Gneis: augig  | –   | – |  Tschuggen-Augengneis |  Ordovicien     | Ordovicien   | Prävariszisches Grundgebirge  |
|15204084 |Gneiss de la Güstizia | Gneis: Muskovit  | –   | – |  Güstizia-Gneis |  Ordovicien     | Ordovicien   | Prävariszisches Grundgebirge  |
|15204085 |Gneiss oeillé de Plasseggen | Gneis: augig  | Granit   | Diorit: Quarz |  Plasseggen-Augengneis |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15204086 |Trias de l&#39;Austroalpin | Dolomitstein  | Rauwacke   | Gestein: pelitisch |  – |  Trias     | Trias   | Prä-Rift  |
|15204087 |Ostalpin: Dogger | Brekzie: polymikt  | Sandstein   | Tonstein |  – |  Jurassique moyen     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15204088 |Ostalpin: Radiolarit-Aptychenkalk | Gestein: kieselig: Radiolarien  | Kalkstein: mikritisch: Aptychen   | – |  – |  Jurassique tardif     | Jurassique moyen   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15204089 |Ostalpin: Kreide | Kalkstein  | Gestein: pelitisch   | Brekzie |  – |  Crétacé     | Crétacé   | Sedimentbedeckung  |
|15204090 |Ostalpin: Lias | Kalkstein  | Sandstein   | Mergelstein |  – |  Permien     | Carbonifère   | Syn-Rift  |
|15204091 |Ostalpin: Grundgebirge | Gneis  | Schiefer   | Amphibolit |  – |  Permien     | Protérozoïque   | Grundgebirge  |
|15204092 |Nair-Porphyroid | Rhyolith  | Dazit: rhyolithisch   | – |  Nair-Porphyroid |  Carbonifère     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15204093 |Nair-Porphyroid: Lavatèra-Brekzie | 15111021  | –   | – |  Lavatèra-Brekzie |  Mésozoïque     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15204094 |Varaina-Schiefer | Andesit  | Schiefer: Chlorit   | – |  Varaina-Schiefer |  Carbonifère     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15204095 |Sprenkel-Schiefer | Dazit: rhyolithisch  | Tuffit   | – |  «Sprenkelschiefer» |  Carbonifère     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15204096 |Complexe gneissique de Fedoz | 15111525  | Schiefer   | Marmor: kalkig |  Fedoz-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15204097 |Fedoz-Metagabbro | Gabbro  | Schiefer: Chlorit   | – |  Fedoz-Metagabbro |  Guadalupien     | Guadalupien   | Grundgebirge  |
|15204098 |Maloja-Orthogneis | Gneis: magmatisch  | –   | – |  Maloja-Orthogneis |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15204099 |Complexe gneissique du Maloja | Schiefer: Glimmer-Chloritoid  | Schiefer: Glimmer-Granat   | Gneis: Amphibol |  Maloja-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15204100 |Ur-Brekzie | Brekzie: tektonisch  | Serpentinit: brekziös: Karbonat   | – |  Ur-Brekzie |  Mésozoïque     | Paléozoïque   | Ophiolithische Abfolge  |
|15204101 |Tschima-da-Flix-Granit | Granit: porphyrisch  | –   | – |  Tschima-da-Flix-Granit |  Carbonifère     | Carbonifère   | Variszisches Grundgebirge  |
|15204102 |Granodiorite d&#39;Err | Granodiorit  | –   | – |  Err-Granodiorit |  Permien     | Carbonifère   | Grundgebirge  |
|15204103 |Filons de diabase postvarisques | 15111445  | –   | – |  – |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15204104 |Gneiss oeillé de la Flüela | Gneis: augig  | Granit: porphyrisch   | – |  Flüela-Augengneis |  Ordovicien     | Ordovicien   | Prävariszisches Grundgebirge  |
|15204105 |Gneiss du Dorfberg | Gneis  | –   | – |  Dorfberg-Gneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15204106 |Brèche du Piz Chaschauna | Brekzie: kalkig: Bioklasten  | –   | – |  Chaschauna-Brekzie |  Jurassique précoce     | Jurassique précoce   | Syn-Rift  |
|15204107 |Gneiss oeillé de la Sesvenna | Gneis: granitisch-augig  | –   | – |  Sesvenna-Augengneis |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15204108 |Granodiorite de Vaüglia | Granodiorit  | –   | – |  Vaüglia-Granodiorit |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15204109 |Roches volcanique du Döss Radond | 15111445  | Tuff: vulkanisch   | – |  Döss-Radond-Vulkanite |  Carnien     | Ladinien   | Raibl  |
|15204110 |Brèche de l&#39;Augsten | Brekzie: polymikt  | Tonstein   | – |  Augsten-Brekzie |  Crétacé tardif     | Crétacé tardif   | Sedimentbedeckung  |
|15204111 |Métarhyolite du Piz Trovat | Rhyolith  | –   | – |  Piz-Trovat-Metarhyolit |  Sakmarien     | Sakmarien   | Spät- bis postvariszisches Grundgebirge  |
|15204112 |Métarhyolite du Sass Queder | Rhyolith  | –   | – |  Sass-Queder-Metarhyolith |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15204113 |Orthogneiss de la Rösa | Gneis: magmatisch  | –   | – |  La-Rösa-Orthogneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15204114 |Schistes du Carale | 15111580  | Schiefer: Quarz-Glimmer   | Gneis |  Carale-Schiefer |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15204115 |Groupe de Gosau | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Eocène     | Crétacé tardif   | Post-Kollision  |
|15204116 |Serpentinite du Morteratsch | Serpentinit  | –   | – |  Morteratsch-Serpentinit |  Carbonifère     | Carbonifère   | Grundgebirge  |
|15204117 |Gneiss oeillé du Forun | Gneis: augig  | –   | – |  Forun-Augengneis |  Spätes Ordovizium     | Spätes Ordovizium   | Prävariszisches Grundgebirge  |
|15204118 |Gneiss oeillé du Piz Kesch | Gneis: augig  | Gneis: gebändert   | – |  Kesch-Augengneis |  Ordovicien     | Ordovicien   | Prävariszisches Grundgebirge  |
|15204119 |socle polycyclique anté-varisque de l&#39;Austroalpin | Gneis  | Schiefer   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15204120 |«Jüngere Orthogneise» | Gneis: magmatisch  | –   | – |  – |  Spätes Ordovizium     | Spätes Ordovizium   | Prävariszisches Grundgebirge  |
|15204121 |«Ältere Orthogneise» | Gneis: magmatisch  | –   | – |  – |  Cambrien     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15204122 |Orthogneiss du Val Rude | Gneis: augig  | –   | – |  Val-Rude-Orthogneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15204123 |Granodiorite du Corvatsch | Granodiorit  | –   | – |  Corvatsch-Granodiorit |  Carbonifère     | Carbonifère   | Grundgebirge  |
|15204124 |Granodiorite du Julier | Granodiorit  | –   | – |  Julier-Granodiorit |  Carbonifère     | Carbonifère   | Grundgebirge  |
|15204125 |Granodiorite du Sasso Rosso | Granodiorit  | –   | – |  Sasso-Rosso-Granodiorit |  Carbonifère     | Carbonifère   | Grundgebirge  |
|15204126 |Brèche du Piz Lavinèr | Brekzie: dolomitisch  | –   | – |  Lavinèr-Brekzie |  Trias     | Trias   | Karbonatische Trias  |
|15204127 |Brèche de l&#39;Haupter | Brekzie: polymikt  | –   | – |  Haupter-Brekzie |  Jurassique moyen     | Jurassique précoce   | Syn-Rift  |
|15204130 |Groupe de Buffalora | Dolomitstein  | Kalkstein   | Mergelstein |  – |  Ladinien     | Anisien   | Karbonatische Trias  |
|15204132 |roches intrusives varisques de l&#39;Austroalpin | Granit  | Granodiorit   | Gabbro |  – |  Permien     | Carbonifère   | Variszisches Grundgebirge  |
|15204135 |orthogneiss anté-varisques de l&#39;Austroalpin | Gneis: magmatisch  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15204136 |paragneiss anté-varisques de l&#39;Austroalpin | Gneis: sedimentär  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15204137 |roches vertes anté-varisques de l&#39;Austroalpin | Prasinit  | Serpentinit   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15204138 |Calcaire d&#39;Uglix | Kalkstein: dolomitisch  | Tuffit   | – |  Uglix-Plattenkalk |  Norien     | Norien   | Hauptdolomit  |
|15204139 |Granite du Parait Chavagl | Granit  | –   | – |  Parait-Chavagl-Granit |  Permien     | Pennsylvanien   | Variszisches Grundgebirge  |
|15204140 |Brèche de Clavadatsch | Brekzie  | –   | – |  Clavadatsch-Brekzie |  Cénomanien     | Cénomanien   | Flysch  |
|15204141 |Granodiorite du Corno di Campo | Granodiorit  | Syenit   | Gabbro |  Corno-di-Campo-Granodiorit |  Permien     | Carbonifère   | Grundgebirge  |
|15204142 |Gabbro de Campocologno | Gabbro  | Diorit   | – |  Campocologno-Gabbro |  Permien     | Carbonifère   | Grundgebirge  |
|15200035 |Membre du Chestel | Kalkstein: arenitisch: Bioklasten  | Kalkstein: Korallen   | Kalkstein: Ooide |  Chestel-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200036 |Pisolite de la Caquerelle | Kalkstein: Onkoide  | –   | – |  15251130 |  Oxfordien     | Oxfordien   | Malm  |
|15200037 |Membre de Grellingen | Kalkstein: mikritisch  | Kalkstein: Korallen   | – |  Grellingen-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200039 |Formation du Pichoux | Kalkstein: mikritisch  | Kalkstein: mergelig   | – |  Pichoux-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15200040 |Membre de Liesberg | Mergelstein  | Kalkstein: Chert   | – |  Liesberg-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200041 |Membre de Sornetan | Tonstein: mergelig  | Kalkstein   | – |  Sornetan-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200042 |Membre à Renggeri | Tonstein: mergelig  | Kalkstein   | – |  «Renggeri-Member» |  Oxfordien     | Oxfordien   | Malm  |
|15200043 |Membre du Graitery | Mergelstein  | Kalkstein: mergelig   | – |  Graitery-Member |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15200044 |Membre de Herznach | Kalkstein: Eisenooide  | Mergelstein: Eisenooide   | – |  Herznach-Member |  Oxfordien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15200045 |Banc du Schellenbrücke | Kalkstein: Eisenooide  | –   | – |  Schellenbrücke-Bank |  Oxfordien     | Oxfordien   | Lias-Dogger in neritischer Fazies  |
|15200046 |Membre de Bollement | Kalkstein: spätig: Bioklasten  | Kalkstein: arenitisch: Bioklasten-Chert   | – |  Bollement-Member |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15200047 |Membre d&#39;Ängistein | Kalkstein: spätig: Bioklasten  | Kalkstein: arenitisch: Bioklasten   | – |  Ängistein-Member |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15200048 |Banc d&#39;Unter Erli | Kalkstein: Bioklasten  | –   | – |  Unter-Erli-Bank |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15200049 |Membre de Bözen | Mergelstein  | Kalkstein: mergelig   | – |  Bözen-Member |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15200050 |Membre de Saulcy | Mergelstein: tonig  | –   | – |  Saulcy-Member |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15200051 |Membre du Schelmenloch | Mergelstein  | Kalkstein: mergelig   | – |  Schelmenloch-Member |  Callovien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200052 |Banc d&#39;Anwil | Kalkstein: Eisenooide  | –   | – |  Anwil-Bank |  Callovien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200053 |Membre de Châtillon | Mergelstein  | Kalkstein: Bioklasten   | – |  Châtillon-Member |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15200054 |Membre de St-Braix | Kalkstein: Bioklasten-Ooide  | Mergelstein: sandig   | – |  St-Brais-Member |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200055 |Dogger du Jura | Kalkstein  | Mergelstein   | Tonstein |  – |  Oxfordien     | Toarcien   | Syn-Rift  |
|15200056 |Lias du Jura | Mergelstein  | Kalkstein   | Tonstein |  – |  Toarcien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15200057 |Spatkalk (Hauptrogenstein) | Kalkstein: spätig: Bioklasten  | –   | – |  «Spatkalk» (Hauptrogenstein) |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200058 |Pierre Blanche (Hauptrogenstein) | Kalkstein: mikritisch: Ooide  | –   | – |  «Pierre Blanche» (Hauptrogenstein) |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200059 |Couches de Movelier | Mergelstein: Bioklasten  | Mergelstein: kalkig   | – |  Movelier-Schichten |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200060 |Série oolitique supérieure (Grande Oolithe) | Kalkstein: Ooide  | Kalkstein: spätig: Bioklasten   | – |  15251167 |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200061 |Couches à Acuminata supérieures | Mergelstein: Bioklasten  | Kalkstein: spätig   | – |  «Obere Acuminata-Schichten» |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200062 |Série oolitique inférieure (Oolithe Subcompacte) | Kalkstein: Bioklasten-Ooide  | Kalkstein: mikritisch   | – |  «Oolithe Subcompacte» (Hauptrogenstein) |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200063 |Membre du Grenchenberg | Kalkstein: siltig: Bioklasten  | Mergelstein   | – |  Grenchenberg-Member |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200064 |Membre de la Rothenfluh | Mergelstein: sandig: Bioklasten  | Kalkstein: sandig   | – |  Rothenfluh-Member |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200065 |Membre de Brüggli | Kalkstein: sandig  | Kalkstein: Bioklasten   | Mergelstein: Eisenooide |  Brüggli-Member |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200066 |Couches à Humphriesi | Kalkstein: Bioklasten  | Mergelstein: Eisenooide   | – |  «Humphriesi-Schichten» (Brüggli-Mb.) |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200067 |Membre de Waldenburg | Tonstein  | Mergelstein   | Mergelstein: Eisenooide |  Waldenburg-Member |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200068 |Membre du Hirnichopf | Tonstein  | Kalkstein: sandig   | Mergelstein: Eisenooide |  Hirnichopf-Member |  Bajocien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15200069 |Membre de Hauenstein | Tonstein  | Kalkstein: sandig   | – |  Hauenstein-Member |  Aalénien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15200070 |Membre de Sissach | Kalkstein: sandig: Glimmer  | Kalkstein: Bioklasten   | Mergelstein: Eisenooide |  Sissach-Member |  Aalénien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15200071 |Membre du Gross Wolf | Mergelstein: Bioklasten  | Kalkstein: mergelig   | – |  Gross-Wolf-Member |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15200072 |Banc d&#39;Eriwis | Kalkstein: Bioklasten  | –   | – |  Eriwis-Bank |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15200073 |Banc d&#39;Erlimoos | Mergelstein: Glaukonit-Bioklasten  | –   | – |  Erlimoos-Bank |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15200074 |Banc de Gipf | Mergelstein: Bioklasten  | Kalkstein: Eisenooide   | – |  Gipf-Bank |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15200075 |Membre de Rietheim | Mergelstein: tonig: Bitumen  | –   | – |  Rietheim-Member |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15200076 |Unterer Stein (Fm. de la Staffelegg) | Kalkstein: Bitumen  | –   | – |  «Unterer Stein» (Staffelegg-Fm.) |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15200077 |Membre de Rickenbach | Mergelstein: kalkig: Glaukonit  | –   | – |  Rickenbach-Member |  Toarcien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15200078 |Banc de la Müsenegg | Mergelstein  | Kalkstein: mergelig   | – |  Müsenegg-Bank |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15200079 |Membre de Breitenmatt | Mergelstein: kalkig: Bioklasten  | Kalkstein   | – |  Breitenmatt-Member |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15200080 |Banc de Trasadingen | Mergelstein: kalkig  | –   | – |  Trasadingen-Bank |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15200081 |Membre du Grünschholz | Mergelstein: kalkig: Glaukonit  | Kalkstein   | – |  Grünschholz-Member |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15200082 |Membre de Frick | Tonstein  | Siltstein: Glimmer   | – |  Frick-Member |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15200083 |Membre du Mont Terri | Mergelstein: Glimmer  | Kalkstein: mergelig   | – |  Mont-Terri-Member |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15200084 |Membre de Fasiswald | Kalkstein: sandig  | Tonstein: siltig   | – |  Fasiswald-Member |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15200085 |Membre du Weissenstein | Kalkstein: sandig  | Sandstein: kalkig   | – |  Weissenstein-Member |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15200086 |Membre de Beggingen | Kalkstein: arenitisch-spätig  | Tonstein   | Siltstein |  Beggingen-Member |  Sinémurien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15200087 |Banc de Gächlingen | Kalkstein: Eisenooide  | Kalkstein: Bioklasten   | – |  Gächlingen-Bank |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15200088 |Banc de Schleitheim | Kalkstein: Eisenooide  | Kalkstein: Bioklasten   | – |  Schleitheim-Bank |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15200089 |Membre du Schambelen | Tonstein: mergelig: Bitumen  | Tonstein: siltig   | – |  Schambelen-Member |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15200090 |Banc de Hallau | Tonstein: Bitumen  | Kalkstein: sandig: Glaukonit   | – |  Hallau-Bank |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15200091 |Sidérolithique du Jura | Gestein: residual: Eisenmineralien  | –   | – |  – |  Bartonien     | Lutétien   | Siderolithikum  |
|15200092 |Formations des Gorges de l&#39;Orbe et de Vallorbe, indifférenciées | Kalkstein: Bioklasten  | Kalkstein: Ooide   | Mergelstein |  – |  Barrémien     | Hauterivien   | «Urgonien»  |
|15200093 |Formation de Vallorbe | Kalkstein: Bioklasten  | –   | – |  Vallorbe-Member |  Barrémien     | Hauterivien   | «Urgonien»  |
|15200094 |Membre de la Rivière | Kalkstein: mergelig  | Mergelstein   | – |  La-Rivière-Member |  Barrémien     | Barrémien   | «Urgonien»  |
|15200096 |Formation des Gorges de l&#39;Orbe | Kalkstein: Ooide  | Kalkstein: Bioklasten   | Mergelstein |  Gorges-de-l&#39;Orbe-Formation |  Hauterivien     | Hauterivien   | «Urgonien»  |
|15200097 |Formations de Pierre-Châtel, de Vions et de la Chambotte, indifférenciées | Kalkstein: mikritisch  | Kalkstein: Bioklasten-Ooide   | Mergelstein |  – |  Valanginien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200098 |Formation de la Chambotte | Kalkstein: mikritisch: Bioklasten  | –   | – |  Chambotte-Formation |  Valanginien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202572 |Complexe gneissique de la Tamina: mylonitique | Gneis: mylonitisch  | –   | – |  Tamina-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202569 |Granite de la Voralp: faciès acide de bordure | Granit: aplitisch  | –   | – |  Voralp-Granit |  Pennsylvanien     | Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202570 |Complexe gneissique de la Tamina | Gneis: migmatitisch  | –   | – |  Tamina-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202571 |Complexe gneissique de la Tamina: gneiss schisteux à biotite | Gneis: schiefrig: Biotit  | –   | – |  Tamina-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202573 |Migmatite d&#39;Innertkirchen: marbre | Marmor  | –   | – |  Innertkirchen-Migmatit |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202574 |Complexe gneissique de Guttannnen: migmatite | Migmatit  | –   | – |  Guttannen-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202575 |Complexe gneissique de Guttannnen: avec amphibolite | Gneis: migmatitisch  | Amphibolit   | – |  Guttannen-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202576 |Complexe gneissique de Guttannnen: granite aplitique | Granit: aplitisch  | –   | – |  Guttannen-Gneiskomplex |  Carbonifère     | Carbonifère   | Prävariszisches Grundgebirge  |
|15202577 |Complexe gneissique de Guttannnen: marbre | Marmor  | –   | – |  Guttannen-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202578 |Complexe gneissique de Guttannnen: roche ultramafique | Gestein: ultramafisch  | –   | – |  Guttannen-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202579 |Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: avec amphibolite à blocs | Gneis: migmatitisch  | Amphibolit: migmatitisch   | – |  Ofenhorn-Stampfhorn-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202580 |Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: granite aplitique | Granit: aplitisch  | –   | – |  Ofenhorn-Stampfhorn-Gneiskomplex |  Carbonifère     | Carbonifère   | Prävariszisches Grundgebirge  |
|15202581 |Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: amphibolite à blocs | Amphibolit: migmatitisch  | –   | – |  Ofenhorn-Stampfhorn-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202582 |Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: roche ultramafique | Gestein: ultramafisch  | –   | – |  Ofenhorn-Stampfhorn-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202583 |Formations de Bommerstein et de Reischiben, indifférenciées | Tonstein  | Kalkstein: spätig   | Mergelstein |  – |  Bathonien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15202584 |Formations de Mels et de Röti, indifférenciées | Dolomitstein  | Sandstein   | – |  – |  Carnien     | Trias précoce   | Prä-Rift  |
|15202585 |Complexe gneissique de Guttannnen: gneiss schisteux à biotite, chlorite, séricite | Gneis  | Schiefer   | – |  Guttannen-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202586 |Mélange de la Zettenalp-Trochematt | Mergelstein: schiefrig  | Sandstein   | Brekzie: kalkig: Bioklasten |  Zettenalp-Trochematt-Melange |  Eocène     | Eocène   | Mélange  |
|15202587 |Flysch du Laubersmad | Brekzie: kristallin  | –   | – |  Laubersmad-Flysch |  Priabonien     | Eocène moyen   | Flysch  |
|15202588 |Formation de Stad, «Jüngerer Quarzsandstein» | Sandstein: Quarz  | –   | – |  Stad-Formation |  Priabonien     | Eocène moyen   | «Nummulitikum»  |
|15202589 |Membre d&#39;Einsiedeln, «Älterer Quarzsandstein» | Sandstein: Quarz  | –   | – |  Einsiedeln-Member |  Eocène moyen     | Yprésien   | «Nummulitikum»  |
|15202590 |Formation du Schrattenkalk, devenant marneuse | Kalkstein: mergelig  | Mergelstein   | – |  Schrattenkalk-Formation |  Aptien     | Aptien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202591 |Calcaire de Wängen, faciès calcaire à Lithothamnies | Kalkstein: Bioklasten  | –   | – |  Wängen-Kalk |  Priabonien     | Eocène moyen   | «Nummulitikum»  |
|15202592 |Membre d&#39;Einsiedeln, faciès calcaire à Alvéolines | Kalkstein: Nummuliten  | –   | – |  Einsiedeln-Member |  Eocène moyen     | Yprésien   | «Nummulitikum»  |
|15202593 |Grès du Hohgant, calcaire gréseux et calcaire | Kalkstein: sandig  | Kalkstein   | – |  Hohgant-Sandstein |  Priabonien     | Bartonien   | «Nummulitikum»  |
|15202594 |Mélange tectonique des écailles internes d&#39;Einsiedeln | Mergelstein  | –   | – |  – |  Eocène     | Eocène   | Mélange  |
|15202595 |Formations du Bürgen et d&#39;Euthal, indiff. | Kalkstein  | Sandstein   | Mergelstein |  – |  Priabonien     | Lutétien   | «Nummulitikum»  |
|15202596 |Formation de l&#39;Euthal et Membre du Steinbach, indiff. | Kalkstein: Nummuliten  | Sandstein: Glaukonit   | – |  – |  Yprésien     | Thanétien   | «Nummulitikum»  |
|15202597 |Formation de Stad (e6) | Tonstein  | –   | – |  Stad-Formation |  Priabonien     | Priabonien   | «Nummulitikum»  |
|15202598 |Formations du Stgir et d&#39;Inferno, indifférenciées | Schiefer: tonig  | Schiefer: kalkig   | Quarzit |  – |  Jurassique précoce     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15202599 |Oberer Quintner Kalk: calcaire à coraux | Kalkstein: Korallen  | –   | – |  «Oberer Quintner Kalk» |  Tithonien     | Tithonien   | Malm  |
|15202600 |Oberer Quintner Kalk: Unterer Kalk | Kalkstein: mikritisch  | –   | – |  «Oberer Quintner Kalk» |  Tithonien     | Tithonien   | Malm  |
|15202601 |Formation du Prodkamm à Formation du Sexmor, indifférenciées | Gestein: pelitisch  | Kalkstein   | Sandstein |  – |  Jurassique précoce     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15202602 |Formation du Plattazüg | Schiefer: Chlorit  | Phyllit   | Dazit |  Plattenzüg-Formation |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15202603 |Formation du Zementstein à Formation de Garschella, indifférenciées | Kalkstein  | Mergelstein   | Sandstein |  – |  Crétacé précoce     | Crétacé précoce   | Post-Rift  |
|15202604 |Formation d&#39;Euthal: faciès argilo-schisteux noir | Tonstein: schiefrig  | Konglomerat   | Sandstein: Quarz |  Vasanachopf-Member |  Paléocène     | Paléocène   | «Nummulitikum»  |
|15202605 |Pfäfers-Fm. | Mergelstein  | Kalkstein: kieselig   | Sandstein: Glimmer |  Pfäfers-Formation |  Eocène     | Maastrichtien   | Flysch  |
|15202606 |Euthal- und Bürgen-Fm. | Kalkstein  | Sandstein   | – |  – |  Lutétien     | Sélandien   | «Nummulitikum»  |
|15202607 |Amden- und Wang-Fm. | Mergelstein  | Kalkstein: sandig   | – |  – |  Maastrichtien     | Santonien   | Post-Rift  |
|15202608 |Seewen- und Amden-Fm. | Mergelstein  | Kalkstein: mikritisch   | – |  – |  Campanien     | Cénomanien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202609 |Betlis- bis Schrattenkalk-Fm. | Kalkstein  | Mergelstein   | – |  – |  Albien     | Valanginien   | Post-Rift  |
|15202610 |Öhrli- bis Schrattenkalk-Fm. | Kalkstein  | Mergelstein   | – |  – |  Crétacé précoce     | Crétacé précoce   | Post-Rift  |
|15202611 |Bommerstein-Fm.: Basisbildungen | Brekzie  | Sandstein   | Kalkstein: spätig |  Bommerstein-Formation |  Aalénien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15202612 |Öhrli- und Betlis-Fm. | Kalkstein: Bioklasten  | Mergelstein   | – |  – |  Valanginien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202613 |Erzegg-Fm.: Grenzschicht | Kalkstein: mikritisch: Bioklasten  | Kalkstein: spätig: Glaukonit   | – |  «Grenzschicht» (Erzegg-Fm.) |  Callovien     | Bajocien   | Lias-Dogger in pelagischer Fazies  |
|15202614 |Spitzmeilen-Fm.: Bränd-Brekzie | Brekzie: dolomitisch  | –   | – |  Bränd-Brekzie |  Jurassique précoce     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15202615 |Infralias-Sandstein | Sandstein: Quarz  | Mergelstein: sandig: Bioklasten   | Tonstein: schiefrig |  «Infralias-Sandstein» |  Hettangien     | Rhétien   | «Rhät»  |
|15202616 |Nufenen-Zone: Phyllitische Trias | Phyllit  | Schiefer   | – |  – |  Trias     | Trias   | Pelitische Trias  |
|15202617 |Nufenen-Zone: Karbonatische Trias | Marmor: kalkig  | Rauwacke   | Dolomitstein |  – |  Trias     | Trias   | Karbonatische Trias  |
|15202618 |Nufenen-Zone: Karbonatische Trias: Kalkmarmor | Marmor: kalkig  | –   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15202619 |Nufenen-Zone: Karbonatische Trias: Dolomit | Dolomitstein  | –   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15202620 |Nufenen-Zone: Karbonatische Trias: Rauwacke | Rauwacke  | –   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15202621 |Nufenen-Zone: Quarzitische Trias | Quarzit  | –   | – |  – |  Trias     | Trias   | Detritische Trias  |
|15202622 |Urseren-Garvera-Zone: Malm | Schiefer: tonig  | –   | – |  – |  Jurassique tardif     | Jurassique tardif   | Malm  |
|15202623 |Urseren-Garvera-Zone: Dogger | Schiefer: tonig  | –   | – |  – |  Jurassique moyen     | Jurassique moyen   | Lias-Dogger in neritischer Fazies  |
|15202624 |Urseren-Garvera-Zone: Lias | Schiefer: tonig  | –   | – |  – |  Jurassique précoce     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15202625 |Urseren-Garvera-Zone: Oberer Lias | Schiefer: kalkig  | –   | – |  – |  Jurassique précoce     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15202626 |Urseren-Garvera-Zone: Mittlerer Lias | Schiefer: kalkig: Zoisit  | –   | – |  – |  Jurassique précoce     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15202627 |Urseren-Garvera-Zone: Unterer Lias | Sandstein: Quarz  | –   | – |  – |  Jurassique précoce     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15202628 |Urseren-Garvera-Zone: Phyllitische Trias | Phyllit  | Schiefer   | – |  – |  Trias     | Trias   | Pelitische Trias  |
|15202629 |Urseren-Garvera-Zone: Karbonatische Trias | Marmor: kalkig  | Rauwacke   | Dolomitstein |  – |  Trias     | Trias   | Karbonatische Trias  |
|15202630 |Urseren-Garvera-Zone: Permo-Karbon: Psephit- und Psammitgneis | Gneis: psammitisch  | Gneis: psephitisch   | – |  – |  Permien     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15202631 |Urseren-Garvera-Zone: Permo-Karbon: Metarhyolith | Rhyolith  | –   | – |  – |  Permien     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15202632 |Urseren-Garvera-Zone: Permo-Karbon: Chloritschiefer | Schiefer: Chlorit  | –   | – |  – |  Permien     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15204143 |Orthogneiss de Celerina | Gneis: magmatisch  | –   | – |  Celerina-Orthogneis |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15204144 |Schistes du Tonale | Schiefer: Glimmer-Granat  | Gneis: Granat   | – |  Tonale-Schiefer |  Paléozoïque     | Protérozoïque   | Sedimentbedeckung  |
|15204145 |Gypse du Groupe de Raibl | Evaporit: Gips  | –   | – |  – |  Carnien     | Ladinien   | Raibl  |
|15204146 |Cornieule du Groupe de Raibl | Rauwacke  | –   | – |  – |  Carnien     | Ladinien   | Raibl  |
|15204147 |faciès récifal de la Formation de l&#39;Arlberg | Kalkstein: Korallen  | –   | – |  Arlberg-Formation |  Carnien     | Ladinien   | Karbonatische Trias  |
|15204148 |Alpiner Muschelkalk | Kalkstein  | Dolomitstein   | – |  – |  Anisien     | Anisien   | Karbonatische Trias  |
|15204149 |Groupe de Raible: dolomite | Dolomitstein  | –   | – |  – |  Carnien     | Carnien   | Raibl  |
|15204150 |Groupe de la Hauptdolomite: brèche dolomitique bitumineuse | 15111279  | –   | – |  – |  Norien     | Norien   | Hauptdolomit  |
|15204151 |Groupe de Raibl des klippes de Suisse centrale | Rauwacke  | Dolomitstein   | Rauwacke |  – |  Carnien     | Carnien   | Raibl  |
|15200099 |Membre du Guiers | Mergelstein: Bioklasten  | Kalkstein: mergelig   | – |  Guiers-Member |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200100 |Formation de Vions | Kalkstein: arenitisch: Quarz  | Mergelstein   | – |  Vions-Formation |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200101 |Formation de Pierre-Châtel | Kalkstein: mikritisch  | Kalkstein: Bioklasten-Ooide   | Mergelstein |  Pierre-Châtel-Formation |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200102 |Formation du Burghorn | Kalkstein: mikritisch  | Mergelstein   | – |  Burghorn-Formation |  Kimméridgien     | Kimméridgien   | Malm  |
|15200103 |Membre de Wettingen | Kalkstein: mikritisch  | Kalkstein: Chert   | – |  Wettingen-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200104 |Membre de Baden | Kalkstein: mikritisch: Glaukonit  | Mergelstein   | – |  Baden-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200105 |Formation de Villigen | Kalkstein: mikritisch  | Mergelstein   | – |  Villigen-Formation |  Kimméridgien     | Oxfordien   | Malm  |
|15200106 |Membre du Wangental | Kalkstein: mikritisch  | Mergelstein   | – |  Wangental-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200107 |Membre du Letzi | Kalkstein: mikritisch  | –   | – |  Letzi-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200108 |Knollen-Bank (Fm. de Villigen) | Kalkstein: mergelig: Glaukonit  | –   | – |  «Knollen-Bank» |  Kimméridgien     | Oxfordien   | Malm  |
|15200109 |Membre de la Küssaburg | Kalkstein: spätig: Bioklasten  | Kalkstein: mikritisch   | – |  Küssaburg-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200110 |Membre de Wangen | Kalkstein: mikritisch  | Kalkstein: kreidig   | – |  Wangen-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200111 |Membre du Hornbuck | Kalkstein: mergelig: Chert  | Mergelstein   | – |  Hornbuck-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200112 |Membre à Crenularis | Kalkstein: Glaukonit-Bioklasten  | –   | – |  «Crenularis-Member» |  Oxfordien     | Oxfordien   | Malm  |
|15200113 |Membre du Geissberg | Kalkstein: mikritisch  | Mergelstein   | – |  Geissberg-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200114 |Formation de Wildegg | Mergelstein  | Kalkstein: mergelig   | Kalkstein: mikritisch |  Wildegg-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15200115 |Membre d&#39;Effingen | Mergelstein  | Mergelstein: kalkig   | – |  Effingen-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200116 |Banc du Gerstenhübel | Kalkstein: mikritisch  | Kalkstein: mergelig   | – |  Gerstenhübel-Bank |  Oxfordien     | Oxfordien   | Malm  |
|15200117 |Membre de Birmenstorf | Kalkstein: mikritisch: Glaukonit  | Kalkstein: mergelig   | – |  Birmenstorf-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200118 |Formation de Günsberg | Kalkstein: Korallen  | Kalkstein: Ooide   | Mergelstein |  Günsberg-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15200119 |Calcaire à coraux de Moutier | Kalkstein: Korallen  | Mergelstein   | – |  Moutier-Korallenkalk |  Oxfordien     | Oxfordien   | Malm  |
|15200120 |Formation de Klingnau | Mergelstein  | Kalkstein: Bioklasten   | Kalkstein: Ooide |  Klingnau-Formation |  Bathonien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200121 |Argile à Knorri | Tonstein  | Kalkstein: mergelig   | – |  «Knorri-Ton» |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200122 |Couches à Wuerttembergica | Mergelstein  | Kalkstein: Bioklasten   | – |  «Wuerttembergica-Schichten» |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200123 |Banc à Subfurcatum | Mergelstein: Bioklasten  | –   | – |  «Subfurcatum-Bank» |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200124 |Couches à Blagdeni | Kalkstein: sandig  | Mergelstein   | – |  «Blagdeni-Schichten» (Klingnau-Fm.) |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200125 |Groupe du Keuper | Sandstein  | Gestein: pelitisch   | Evaporit |  – |  Rhétien     | Ladinien   | Keuper  |
|15200126 |Formation du Klettgau | Mergelstein  | Sandstein   | Dolomitstein |  Klettgau-Formation |  Rhétien     | Carnien   | Keuper  |
|15200127 |Membre du Belchen | Sandstein: Quarz  | Tonstein   | – |  Belchen-Member |  Rhétien     | Rhétien   | Keuper  |
|15200128 |Formation du Bänkerjoch | Tonstein  | Evaporit: Sulfat   | Evaporit: Halit |  Bänkerjoch-Formation |  Carnien     | Ladinien   | Keuper  |
|15200129 |Groupe du Muschelkalk | Dolomitstein  | Kalkstein   | Evaporit |  – |  Ladinien     | Anisien   | Muschelkalk  |
|15200130 |Formation de Schinznach | Dolomitstein  | Kalkstein: Bioklasten   | Mergelstein |  Schinznach-Formation |  Ladinien     | Anisien   | Muschelkalk  |
|15200131 |Membre d&#39;Asp | Tonstein: siltig  | Mergelstein: dolomitisch   | Dolomitstein |  Asp-Member |  Ladinien     | Ladinien   | Muschelkalk  |
|15200132 |Membre du Stamberg | Dolomitstein  | Dolomitstein: Ooide   | Dolomitstein: Bioklasten |  Stamberg-Member |  Ladinien     | Ladinien   | Muschelkalk  |
|15200133 |Membre de Liedertswil | Kalkstein: mikritisch  | Dolomitstein   | – |  Liedertswil-Member |  Ladinien     | Ladinien   | Muschelkalk  |
|15200134 |Membre de Kienberg | Kalkstein: spätig: Bioklasten  | –   | – |  Kienberg-Member |  Ladinien     | Ladinien   | Muschelkalk  |
|15200135 |Formation de Zeglingen | Evaporit: Anhydrit  | Mergelstein   | Dolomitstein |  Zeglingen-Formation |  Anisien     | Anisien   | Muschelkalk  |
|15200136 |Obere Sufatzone (Fm. de Zeglingen) | Evaporit: Anhydrit  | Mergelstein   | – |  «Obere Sufatzone» (Zeglingen-Fm.) |  Anisien     | Anisien   | Muschelkalk  |
|15200137 |Salzlager (Fm. de Zeglingen) | Evaporit: Halit  | –   | – |  «Salzlager» (Zeglingen-Fm.) |  Anisien     | Anisien   | Muschelkalk  |
|15200138 |Untere Sulfatzone (Fm. de Zeglingen) | Evaporit: Anhydrit  | Dolomitstein   | Mergelstein |  «Untere Sulfatzone» (Zeglingen-Fm.) |  Anisien     | Anisien   | Muschelkalk  |
|15200139 |Formation de Kaiseraugst | Dolomitstein  | Kalkstein: mergelig   | Mergelstein: Glimmer |  Kaiseraugst-Formation |  Anisien     | Anisien   | Muschelkalk  |
|15200140 |Marne à Orbicularis | Mergelstein: kalkig: Bitumen  | Evaporit: Anhydrit   | – |  «Orbicularis-Mergel» |  Anisien     | Anisien   | Muschelkalk  |
|15200141 |Wellenkalk / Wellenmergel | Kalkstein: mergelig  | Mergelstein   | – |  «Wellenkalk / Wellenmergel» |  Anisien     | Anisien   | Muschelkalk  |
|15200142 |Wellendolomit | Dolomitstein  | Kalkstein   | Mergelstein |  «Wellendolomit» |  Anisien     | Anisien   | Muschelkalk  |
|15200143 |Groupe du Buntsandstein | Sandstein  | Tonstein   | – |  – |  Anisien     | Olénékien   | Buntsandstein  |
|15200144 |Formation du Dinkelberg | Sandstein: Glimmer  | Tonstein   | – |  Dinkelberg-Formation |  Anisien     | Olénékien   | Buntsandstein  |
|15200145 |Rhötton | Tonstein: siltig: Glimmer  | –   | – |  «Rhötton» |  Anisien     | Anisien   | Buntsandstein  |
|15200146 |Plattensandstein (Fm. du Dinkelberg) | Sandstein: Glimmer  | –   | – |  «Plattensandstein» (Dinkelberg-Fm.) |  Anisien     | Olénékien   | Buntsandstein  |
|15200147 |Karneol-Horizont (Fm. du Dinkelberg) | Sandstein: kieselig  | –   | – |  «Karneol-Horizont» (Dinkelberg-Fm.) |  Olénékien     | Olénékien   | Buntsandstein  |
|15200148 |Formation de Narlay | Kalkstein: kreidig: Chert  | Kalkstein: mergelig   | – |  Narlay-Formation |  Coniacien     | Cénomanien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15200149 |Formation de la Perte-du-Rhône | Sandstein: Glaukonit  | Kalkstein: mergelig   | Tonstein |  Perte-du-Rhône-Formation |  Cénomanien     | Aptien   | «Gault»  |
|15200150 |Formation du Grand Essert | Kalkstein: spätig: Bioklasten-Glaukonit  | Kalkstein: Ooide   | Mergelstein: Bioklasten |  Grand-Essert-Formation |  Hauterivien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200151 |Membre de Neuchâtel | Kalkstein: spätig: Bioklasten-Glaukonit  | Kalkstein: Ooide   | – |  Neuchâtel-Member |  Hauterivien     | Hauterivien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200152 |Membre d&#39;Hauterive | Mergelstein: Bioklasten  | Kalkstein: spätig: Bioklasten-Glaukonit   | Mergelstein: kalkig |  Hauterive-Member |  Hauterivien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200153 |Formation du Vuache | Kalkstein: spätig: Bioklasten-Ooide  | Mergelstein   | – |  Vuache-Formation |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200154 |Calcaire à Alectyonia rectangularis | Kalkstein: spätig: Bioklasten  | –   | – |  «Alectryonia-Kalk» |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200155 |Marne d&#39;Arzier | Mergelstein: Bioklasten  | Kalkstein: mergelig   | – |  Arzier-Mergel |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200156 |Formation du Goldberg | Mergelstein  | Kalkstein   | Brekzie: polymikt |  Goldberg-Formation |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in detritischer Fazies  |
|15200157 |Formation du Wiesental | Sandstein: Feldspat  | Sandstein: dolomitisch   | – |  Wiesental-Formation |  Lopingien     | Lopingien   | Spät- bis postvariszisches Grundgebirge  |
|15200158 |Formation de Weitenau | Sandstein: Feldspat  | Konglomerat   | – |  Weitenau-Formation |  Lopingien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15200159 |Formation de Weiach | Sandstein: Feldspat  | Konglomerat   | Tonstein |  Weiach-Formation |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200160 |Formations de Günsberg, Vellerat, Villigen, Balsthal et Courgenay, indifférenciées | Kalkstein: mikritisch  | Kalkstein: Ooide   | Mergelstein |  – |  Kimméridgien     | Oxfordien   | Malm  |
|15202636 |Gotthard-Decke: Prävariszischer Paragneis | Gneis: sedimentär  | –   | – |  – |  Paléozoïque     | Präkambrium   | Prävariszisches Grundgebirge  |
|15202633 |Urseren-Garvera-Zone: Permo-Karbon: Graphitschiefer | Schiefer: Graphit  | –   | – |  – |  Permien     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15202634 |Gotthard-Decke: Prävariszischer Orthogneis | Gneis: magmatisch  | –   | – |  – |  Paléozoïque     | Präkambrium   | Prävariszisches Grundgebirge  |
|15202635 |Gotthard-Decke: Prävariszischer Augengneis | Gneis: augig  | –   | – |  – |  Paléozoïque     | Präkambrium   | Prävariszisches Grundgebirge  |
|15202637 |Camosci-Decke: Paragneis | Gneis: sedimentär  | –   | – |  – |  Jurassique moyen     | Jurassique moyen   | Sedimentbedeckung  |
|15202638 |Camosci-Decke: Lias-Dogger | Schiefer: Glimmer  | Schiefer: kalkig   | – |  – |  Aalénien     | Toarcien   | Syn-Rift  |
|15202639 |Camosci-Decke: Lias-Dogger: Kalkglimmerschiefer | Schiefer: kalkig: Glimmer  | –   | – |  – |  Aalénien     | Toarcien   | Syn-Rift  |
|15202640 |Camosci-Decke: Lias-Dogger: Granatglimmerschiefer | Schiefer: Glimmer-Granat  | –   | – |  – |  Aalénien     | Toarcien   | Syn-Rift  |
|15202641 |Camosci-Decke: Lias | Marmor  | Quarzit   | – |  – |  Jurassique précoce     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15202642 |Camosci-Decke: Trias | Marmor: dolomitisch  | Rauwacke   | Schiefer: Glimmer |  – |  Trias     | Trias   | Prä-Rift  |
|15202643 |Camosci-Decke: Sandige Trias | Sandstein  | –   | – |  – |  Trias     | Trias   | Detritische Trias  |
|15202644 |Camosci-Decke: Karbonatische Trias | Dolomitstein  | Rauwacke   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15202645 |Urseren-Garvera-Zone | Marmor  | Schiefer   | Rauwacke |  – |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15202646 |Urseren-Garvera-Zone: Trias | Rauwacke  | Phyllit   | Marmor |  – |  Trias     | Trias   | Prä-Rift  |
|15202647 |Nufenen-Zone: Trias | Rauwacke  | Phyllit   | Quarzit |  – |  Trias     | Trias   | Prä-Rift  |
|15202648 |Nufenen-Zone: Lias | Schiefer: tonig  | Quarzit   | Schiefer: kalkig |  – |  Jurassique précoce     | Rhétien   | Lias-Dogger in neritischer Fazies  |
|15203001 |Flysch du Niesen | Konglomerat  | Sandstein   | Tonstein: schiefrig |  – |  Lutétien     | Maastrichtien   | Flysch  |
|15203002 |Formation du Chesselbach | Sandstein  | Tonstein: schiefrig   | – |  Chesselbach-Formation |  Lutétien     | Paléocène   | Flysch  |
|15203003 |Formation de Seron | Konglomerat: polymikt  | Kalkstein: sandig: Bioklasten   | – |  Seron-Formation |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203004 |Formation du Niesenkulm | Konglomerat  | Brekzie: kalkig   | Kalkstein: mikritisch |  Niesenkulm-Formation |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203005 |Formation de Frutigen | Konglomerat  | Sandstein: tonig-kalkig   | Tonstein: schiefrig |  Frutigen-Formation |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203006 |Formation de la Grande Eau | Tonstein  | Sandstein: kalkig   | Konglomerat: polymikt |  Grande-Eau-Formation |  Bathonien     | Aalénien   | Syn-Rift  |
|15203007 |Membre de Langy | Sandstein: kalkig  | Tonstein   | Konglomerat |  Langy-Member |  Bathonien     | Bathonien   | Syn-Rift  |
|15203008 |Membre de la Forclaz | Sandstein: kalkig  | Mergelstein: Bioklasten   | – |  Forclaz-Member |  Bathonien     | Bathonien   | Syn-Rift  |
|15203009 |Membre des Grès de Passage | Sandstein  | –   | – |  «Grès de Passage» |  Bathonien     | Bathonien   | Syn-Rift  |
|15203010 |Membre de la Leyderry | Konglomerat: polymikt  | –   | – |  Leyderry-Member |  Bathonien     | Bathonien   | Syn-Rift  |
|15203011 |Membre de la Raverette | Konglomerat: kalkig  | Mergelstein: Glimmer   | Sandstein: kalkig |  Raverette-Member |  Bajocien     | Bajocien   | Syn-Rift  |
|15203012 |Membre des Schistes à Miches | Tonstein: siltig: Glimmer  | –   | – |  «Schistes à Miches» |  Aalénien     | Aalénien   | Syn-Rift  |
|15203013 |Calcaire de Murgaz | Kalkstein: kieselig-spätig  | Tonstein: schiefrig   | – |  Murgaz-Kalk |  Sinémurien     | Sinémurien   | Syn-Rift  |
|15203014 |Trias de la nappe du Niesen | Sandstein  | Kalkstein: dolomitisch   | Rauwacke |  – |  Trias     | Trias   | Prä-Rift  |
|15203015 |Formation de Chlussli | Schiefer: Chlorit  | Gneis   | – |  Chlussli-Formation |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203016 |Mélange des Coulaytes | Tonstein  | –   | – |  Coulaytes-Melange |  Priabonien     | Eocène moyen   | Mélange  |
|15203017 |Formation de Cuvigne Derrey | Sandstein  | Mergelstein   | – |  Cuvigne-Derrey-Formation |  Lutétien     | Lutétien   | Flysch  |
|15203018 |Groupe des Couches Rouges | Kalkstein: mergelig  | Kalkstein: mikritisch   | Mergelstein |  – |  Maastrichtien     | Cénomanien   | Couches Rouges  |
|15203019 |Formation des Chenaux Rouges | Kalkstein: mergelig  | Mergelstein   | – |  Chenaux-Rouges-Formation |  Yprésien     | Sélandien   | Couches Rouges  |
|15203020 |Calcarénite de la Hochmatt | Kalkstein: arenitisch  | –   | – |  Hochmatt-Kalkarenit |  Yprésien     | Sélandien   | Couches Rouges  |
|15203021 |Croûte minéralisée des Chenaux Rouges | Kalkstein: stromatolithisch: Eisenmineralien-Phosphorit  | Konglomerat   | – |  Chenaux-Rouges-Mineralkruste |  Yprésien     | Paléocène   | Couches Rouges  |
|15203022 |Formation des Forclettes | Kalkstein: mikritisch  | Mergelstein   | – |  Forclettes-Formation |  Maastrichtien     | Maastrichtien   | Couches Rouges  |
|15203023 |Hartground de Roter Sattel | Kalkstein: stromatolithisch: Eisenmineralien-Phosphorit  | –   | – |  Roter-Sattel-Hartgrund |  Sélandien     | Maastrichtien   | Couches Rouges  |
|15203024 |Conglomérat de Beaumont | Konglomerat  | –   | – |  Beaumont-Konglomerat |  Maastrichtien     | Maastrichtien   | Couches Rouges  |
|15203025 |Calcaire des Rayes | Kalkstein: Bioklasten  | –   | – |  Rayes-Kalk |  Maastrichtien     | Maastrichtien   | Couches Rouges  |
|15203026 |Membre du Pissot | Kalkstein  | Tonstein   | – |  Pissot-Member |  Maastrichtien     | Maastrichtien   | Couches Rouges  |
|15203027 |Formation de Rote Platte | Kalkstein: mikritisch  | Kalkstein: mergelig   | – |  Rote-Platte-Formation |  Santonien     | Turonien   | Couches Rouges  |
|15203028 |Membre du Wildenbach | Kalkstein  | Kalkstein: tonig   | Mergelstein: schiefrig |  Wildenbach-Member |  Santonien     | Santonien   | Couches Rouges  |
|15203029 |Hardground de Pra du Pont | Kalkstein: Glaukonit  | –   | – |  Pra-du-Pont-Hartgrund |  Santonien     | Santonien   | Couches Rouges  |
|15203030 |Membre des Rontins | Kalkstein  | Kalkstein: tonig   | Tonstein |  Rontins-Member |  Santonien     | Turonien   | Couches Rouges  |
|15203031 |Membre d&#39;Allières | Kalkstein: tonig  | Mergelstein   | – |  Allières-Member |  Turonien     | Turonien   | Couches Rouges  |
|15203032 |Calcaire de Gérignoz | Kalkstein  | –   | – |  Gérignoz-Kalk |  Turonien     | Turonien   | Couches Rouges  |
|15203033 |Calcarénite de la Plagersflue | Kalkstein: arenitisch  | –   | – |  Plagersflue-Kalkarenit |  Turonien     | Turonien   | Couches Rouges  |
|15203034 |Formation de l&#39;Intyamon | Kalkstein: tonig  | Mergelstein: Bitumen   | – |  Intyamon-Formation |  Turonien     | Aptien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203035 |Membre du Chällihorn | Kalkstein: mikritisch  | Mergelstein   | – |  Chällihorn-Member |  Turonien     | Cénomanien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203036 |Membre de la Comba d&#39;Avau | Mergelstein  | Kalkstein: mergelig: Pyrit   | Kalkstein: kieselig |  Comba-d&#39;Avau-Member |  Albien     | Aptien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203037 |Membre de Rodosex | Kalkstein: stromatolithisch  | Mergelstein: Bioklasten   | Kalkstein: arenitisch: Glaukonit |  Rodosex-Member |  Aptien     | Aptien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203038 |Formation des Sciernes d&#39;Albeuve | Kalkstein: mikritisch: Chert  | Mergelstein   | – |  Sciernes-d&#39;Albeuve-Formation |  Barrémien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203039 |Formation du Moléson | Kalkstein: mikritisch  | Kalkstein: Onkoide   | Kalkstein: Bioklasten |  Moléson-Formation |  Berriasien     | Kimméridgien   | Malm  |
|15203040 |Formation du Torrent de Lessoc | Kalkstein: tonig  | Kalkstein: kieselig   | Mergelstein |  Torrent-de-Lessoc-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15203041 |Formation du Staldengraben | Kalkstein: mergelig  | Mergelstein: schiefrig   | – |  Staldengraben-Formation |  Callovien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15203042 |Membre du Col de Lys | Kalkstein: sandig-kieselig  | Kalkstein: spätig: Glaukonit   | Mergelstein |  Col-de-Lys-Member |  Callovien     | Callovien   | Lias-Dogger in pelagischer Fazies  |
|15203043 |Membre du Vanil Carré | Mergelstein  | Kalkstein: sandig-spätig   | Kalkstein: Ooide |  Vanil-Carré-Member |  Bathonien     | Bajocien   | Lias-Dogger in pelagischer Fazies  |
|15203044 |Membre du Verdy | Kalkstein: tonig  | Mergelstein: schiefrig   | – |  Verdy-Member |  Bajocien     | Bajocien   | Lias-Dogger in pelagischer Fazies  |
|15203045 |Membre de Soladier | Mergelstein: schiefrig  | Kalkstein: tonig   | – |  Soladier-Member |  Aalénien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15203046 |Formation de Sommant | Kalkstein: mikritisch  | Kalkstein: sandig: Bioklasten   | Kalkstein: Ooide |  Sommant-Formation |  Bathonien     | Bajocien   | Syn-Rift  |
|15200175 |Argile à pisolites ferrugineuses | Gestein: residual-tonig: Eisenpisoide  | –   | – |  – |  Rupélien     | Lutétien   | Siderolithikum  |
|15200161 |Crétacé du Jura | Kalkstein  | Mergelstein   | Sandstein: kalkig |  – |  Coniacien     | Berriasien   | Post-Rift  |
|15200162 |Jurassique du Jura | Kalkstein  | Mergelstein   | Tonstein |  – |  Tithonien     | Hettangien   | Sedimentbedeckung  |
|15200163 |Trias du Jura | Dolomitstein  | Mergelstein   | Evaporit |  – |  Rhétien     | Olénékien   | Prä-Rift  |
|15200176 |Argile à bolus | Gestein: residual-tonig: Limonit  | –   | – |  – |  Priabonien     | Bartonien   | Siderolithikum  |
|15200177 |Hupper | Gestein: residual-sandig: Quarz  | Gestein: residual-tonig: Kaolinit   | – |  – |  Priabonien     | Eocène moyen   | Siderolithikum  |
|15200178 |Marne à Homomyes | Mergelstein: Bioklasten  | Kalkstein: spätig   | – |  «Homomya-Mergel» |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200179 |Grès des Vosges | Sandstein  | –   | – |  Vogesen-Sandstein |  Olénékien     | Olénékien   | Buntsandstein  |
|15200180 |Sable siliceux vitrifiable | Gestein: residual-sandig: Quarz  | –   | – |  – |  Priabonien     | Eocène moyen   | Siderolithikum  |
|15200181 |Membre de Mussel | Sandstein: Glaukonit  | –   | – |  Mussel-Member |  Albien     | Aptien   | «Gault»  |
|15200182 |Membre de la Fulie | Kalkstein: mergelig  | Mergelstein   | – |  Fulie-Member |  Albien     | Aptien   | «Gault»  |
|15200183 |Marne des Uttins | Mergelstein: Bioklasten  | Mergelstein: kalkig   | – |  Les-Uttins-Mergel |  Hauterivien     | Hauterivien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200184 |Zone marno-calcaire (Fm. du Grand Essert) | Mergelstein: Bioklasten  | Kalkstein: spätig: Glaukonit-Chert   | – |  L&#39;Ecluse-Mergelkalk |  Hauterivien     | Hauterivien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200185 |Marne à Bryozoaires | Mergelstein: Bioklasten  | –   | – |  «Bryozoen-Mergel» |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200186 |Calcaire saccharoïde | Kalkstein: kristallin  | Dolomitstein   | Rauwacke |  Twannbach-Formation |  Tithonien     | Tithonien   | Malm  |
|15200187 |Membre de Chevenez | Kalkstein: Bioklasten  | Mergelstein: Bioklasten   | – |  Chevenez-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200188 |Formation de Balsthal | Kalkstein: Ooide  | Kalkstein: Onkoide   | Kalkstein: mikritisch |  Balsthal-Formation |  Kimméridgien     | Oxfordien   | Malm  |
|15200189 |Membre de Ste-Vérène | Kalkstein: arenitisch: Bioklasten  | Kalkstein: kreidig   | – |  Verena-Member |  Kimméridgien     | Oxfordien   | Malm  |
|15200190 |Membre de la Holzflue | Kalkstein: Ooide  | Kalkstein: mikritisch   | – |  Holzflue-Member |  Kimméridgien     | Oxfordien   | Malm  |
|15200191 |Membre de Laufon | Kalkstein: mikritisch  | Kalkstein: Ooide   | Kalkstein: Onkoide |  Laufen-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200192 |Membre d&#39;Olten | Kalkstein: mikritisch: Chert  | Kalkstein: Korallen   | – |  Olten-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200193 |Membre du Steinibach | Kalkstein: Ooide  | –   | – |  Steinibach-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200194 |Grüne Mumienbank | Kalkstein: mikritisch: Onkoide  | –   | – |  «Grüne Mumienbank» |  Oxfordien     | Oxfordien   | Malm  |
|15200195 |Banc à Pecten (Fm. de Wildegg) | Kalkstein: mergelig: Bioklasten  | Kalkstein: mikritisch   | – |  «Pecten-Bank» |  Oxfordien     | Oxfordien   | Malm  |
|15200196 |Oolite à Ferrugineus | Mergelstein: Bioklasten-Ooide  | Mergelstein: kalkig   | – |  «Ferrugineus-Oolith» |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200197 |Calcaire à coraux de Wittnau | Kalkstein: Korallen  | –   | – |  Wittnau-Korallenkalk |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200198 |Marne du Furcil | Mergelstein  | Kalkstein: mergelig   | – |  Furcil-Mergel |  Bathonien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200199 |Couches à Maeandrina | Mergelstein: Bioklasten-Ooide  | –   | – |  «Maeandrina-Schichten» |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200200 |Calcaire à coraux de la Gisliflue | Kalkstein: Korallen  | Kalkstein: Bioklasten   | – |  Gisliflue-Korallenkalk |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200201 |Couches à Acuminata inférieures | Kalkstein: Bioklasten  | Kalkstein: Ooide   | Mergelstein |  «Untere Acuminata-Schichten» |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200202 |Couches à Parkinsoni | Mergelstein  | Kalkstein: Bioklasten   | – |  «Parkinsoni-Schichten» (Klingnau-Fm.) |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200203 |Couches à Pecten dewalquei | Kalkstein  | Kalkstein: mergelig: Bioklasten   | – |  «Couches à Pecten dewalquei» |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200204 |Couches de Brot | Mergelstein: kalkig: Bioklasten  | –   | – |  Brot-Schichten |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200205 |Banc à Comptum | Kalkstein: Eisenooide  | Kalkstein: spätig   | – |  «Comptum-Bank» (Passwang-Fm.) |  Aalénien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15200206 |Membre de Seebi | Sandstein: dolomitisch  | Dolomitstein   | Tonstein |  Seebi-Member |  Norien     | Norien   | Keuper  |
|15200207 |Membre de la Gruhalde | Mergelstein: dolomitisch  | –   | – |  Gruhalde-Member |  Norien     | Carnien   | Keuper  |
|15200208 |Membre de Berlingen | Sandstein: kalkig  | –   | – |  Berlingen-Member |  Carnien     | Carnien   | Keuper  |
|15200209 |Membre de Gansingen | Dolomitstein: stromatolithisch  | Mergelstein: dolomitisch   | Evaporit: Sulfat |  Gansingen-Member |  Carnien     | Carnien   | Keuper  |
|15200210 |Membre de l&#39;Ergolz | Mergelstein: siltig-dolomitisch  | Dolomitstein   | Sandstein |  Ergolz-Member |  Carnien     | Carnien   | Keuper  |
|15200211 |Banc de Kaisten | Dolomitstein: Ooide  | –   | – |  Kaisten-Bank |  Ladinien     | Ladinien   | Muschelkalk  |
|15200212 |Banc d&#39;Eptingen | Dolomitstein: Ooide-Chert  | Kalkstein: Ooide   | – |  Eptingen-Bank |  Ladinien     | Ladinien   | Muschelkalk  |
|15200213 |Banc du Dünnlenberg | Mergelstein  | –   | – |  Dünnlenberg-Bank |  Anisien     | Anisien   | Muschelkalk  |
|15200214 |Banc de Saalhof | Kalkstein: Bioklasten  | –   | – |  Saalhof-Bank |  Anisien     | Anisien   | Muschelkalk  |
|15200215 |Banc de Fützen | Kalkstein: Ooide-Chert  | –   | – |  Fützen-Bank |  Anisien     | Anisien   | Muschelkalk  |
|15200216 |Dolomitzone (Fm. de Zeglingen) | Dolomitstein: stromatolithisch: Chert  | –   | – |  «Dolomitzone» (Zeglingen-Fm.) |  Anisien     | Anisien   | Muschelkalk  |
|15200217 |Oberer Schuttfächer (Fm. de Weitenau) | Sandstein: Feldspat  | Konglomerat   | – |  «Oberer Schuttfächer» (Weitenau-Fm.) |  Lopingien     | Guadalupien   | Spät- bis postvariszisches Grundgebirge  |
|15200218 |Playa-Serie (Fm. de Weitenau) | Sandstein: tonig: Glimmer  | Sandstein: tonig: Feldspat   | – |  «Playa-Serie» (Weitenau-Fm.) |  Lopingien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15200219 |Unterer Schuttfächer (Fm. de Weitenau) | Sandstein: Feldspat  | Konglomerat   | Tonstein |  «Unterer Schuttfächer» (Weitenau-Fm.) |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15200220 |Roches plutoniques tardi- à postvarisques de la Forêt Noire | Gestein: plutonisch  | –   | – |  – |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200221 |Permo-Carbonifère du NW de la Suisse | Sandstein  | Konglomerat   | Tonstein |  – |  Permien     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15200222 |Quarzporphyre du Stockberg | Rhyolith  | –   | – |  Stockberg-Rhyolith |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200223 |Granite de la Bärhalde | Granit: Biotit-Muskovit  | –   | – |  Bärhalde-Granit |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200224 |Granite du Schluchsee | Granit: Biotit-Muskovit  | –   | – |  Schluchsee-Granit |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200225 |Granite de Säckingen | Granit: aplitisch  | –   | – |  Säckingen-Granit |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200226 |Jüngere Flussablagerungen (Fm. de Weiach) | Sandstein: Feldspat  | –   | – |  «Jüngere Flussablagerungen» (Weiach-Fm.) |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15200227 |Seeablagerungen (Fm. de Weiach) | Tonstein  | –   | – |  «Seeablagerungen» (Weiach-Fm.) |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15200228 |Ältere Flussablagerungen (Fm. de Weiach) | Sandstein: Feldspat  | Tonstein   | Konglomerat |  «Ältere Flussablagerungen» (Weiach-Fm.) |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200229 |Kohle-Serie (Fm. de Weiach) | Sandstein  | Tonstein: Kohle   | – |  «Kohle-Serie» (Weiach-Fm.) |  Pennsylvanien tardif     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15200230 |Roches plutoniques éo-variques de la Forêt Noire | Gestein: plutonisch  | –   | – |  – |  Mississippien     | Dévonien tardif   | Frühvariszisches Grundgebirge  |
|15200231 |Granite de l&#39;Albtal | Granit: porphyrisch: Biotit  | –   | – |  Albtal-Granit |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15200232 |Granite de Malsburg | Granit: Biotit  | –   | – |  Malsburg-Granit |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15200233 |Granite du Blauen | Granit: Biotit  | –   | – |  Blauen-Granit |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15200234 |Granite du Klemmbach | Granit: Biotit-Muskovit  | –   | – |  Klemmbach-Granit |  Mississippien     | Dévonien tardif   | Frühvariszisches Grundgebirge  |
|15203050 |Membre des Chevalets | Kalkstein: kieselig  | Mergelstein: Glaukonit   | – |  Chevalets-Schichten |  Toarcien     | Toarcien   | Syn-Rift  |
|15203047 |Formation de Rossinière | Kalkstein: spätig: Glaukonit  | –   | – |  Rossinière-Formation |  Aalénien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15203048 |Formation de Heiti | Mergelstein  | Kalkstein: kieselig   | – |  Heiti-Formation |  Bajocien     | Sinémurien   | Lias-Dogger in pelagischer Fazies  |
|15203049 |Formation de la Combe du Pissot | Tonstein: schiefrig: Bitumen  | Kalkstein: kieselig   | Mergelstein: Glaukonit |  Combe-du-Pissot-Formation |  Toarcien     | Toarcien   | Syn-Rift  |
|15203051 |Membre du Creux-de-l&#39;Ours | Mergelstein: Bitumen  | Kalkstein   | – |  Creux-de-l&#39;Ours-Schichten |  Toarcien     | Toarcien   | Syn-Rift  |
|15203052 |Formation du Petit Liençon | Kalkstein: kieselig  | Mergelstein: schiefrig   | – |  Petit-Liençon-Formation |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15203053 |Formation d&#39;Arvel | Kalkstein: spätig: Bioklasten  | Mergelstein: schiefrig   | – |  Arvel-Formation |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15203054 |Formation de la Grande Bonavau | Kalkstein: spätig: Glaukonit  | Kalkstein: dolomitisch: Bioklasten   | – |  Grande-Bonavau-Formation |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15203055 |Formation du Chauderon | Kalkstein: kieselig-spätig  | Mergelstein: schiefrig   | – |  Chauderon-Formation |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15203056 |Formation de la Vudalla | Kalkstein: mikritisch  | Kalkstein: Ooide   | – |  Vudalla-Formation |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15203057 |Membre du Bois de Luan | Kalkstein: mikritisch  | Kalkstein: sandig: Bioklasten   | Mergelstein |  Bois-de-Luan-Member |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15203058 |Membre d&#39;Agreblierai | Kalkstein: Ooide  | –   | – |  Agreblierai-Member |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15203059 |Formation du Col de Tompey | Mergelstein: dolomitisch  | Sandstein: kalkig: Glaukonit   | – |  Col-de-Tompey-Formation |  Hettangien     | Rhétien   | «Rhät»  |
|15203060 |Formation de Plan Falcon | Mergelstein: schiefrig  | Kalkstein: mergelig-dolomitisch   | Kalkstein: Bioklasten-Ooide |  Plan-Falcon-Formation |  Rhétien     | Rhétien   | «Rhät»  |
|15203061 |Dolomies Blondes | Dolomitstein  | Tonstein   | Mergelstein: dolomitisch |  «Dolomies Blondes» |  Norien     | Norien   | Hauptdolomit  |
|15203062 |Formation de Clôt la Cime | Dolomitstein  | Evaporit: Gips   | Brekzie |  Clôt-la-Cime-Formation |  Carnien     | Carnien   | Raibl  |
|15203066 |Formation du Griggeli | Kalkstein: kieselig  | Mergelstein   | – |  Griggeli-Formation |  Oxfordien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15203067 |Calcaire siliceux des Mythen | Kalkstein: kieselig  | Mergelstein   | Kalkstein: spätig |  Mythen-Kieselkalk |  Oxfordien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15203068 |Banc du Griggeli | Kalkstein: spätig: Bioklasten  | –   | – |  «Griggeli-Bank» |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15203069 |Formation de Gibel | Kalkstein: kieselig-spätig  | –   | – |  Gibel-Formation |  Callovien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15203070 |Membre de Rämsi | Brekzie: dolomitisch  | Kalkstein: Korallen   | – |  Rämsi-Member |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15203071 |Membre de Gibel | Kalkstein: sandig: Bioklasten  | Konglomerat   | Kalkstein: spätig: Bioklasten |  «Gibel-Member» |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15203072 |Conglomérat du Steinberg | Konglomerat  | –   | – |  Steinberg-Konglomerat |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15203073 |Membre de la Musenalp | Kalkstein: spätig: Chert  | Kalkstein: Ooide   | – |  Musenalp-Member |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15203074 |Formation du Stanserhorn | Mergelstein  | Kalkstein: kieselig   | – |  Stanserhorn-Formation |  Bajocien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15203075 |Couches à Zoophycos (Fm. du Stanserhorn) | Mergelstein  | Kalkstein: kieselig   | – |  «Zoophycos-Schichten» (Stanserhorn-Fm.) |  Bajocien     | Aalénien   | Lias-Dogger in pelagischer Fazies  |
|15203076 |Calcaire de la Spis | Kalkstein: Onkoide  | Kalkstein: Bioklasten   | Kalkstein: Eisenmineralien |  Spis-Kalk |  Toarcien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15203077 |Schistes à Posidonies (Fm. du Stanserhorn) | Tonstein: schiefrig: Bitumen  | Mergelstein   | Kalkstein |  «Posidonienschiefer» (Stanserhorn-Fm.) |  Toarcien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15203078 |Formation de la Obflue | Kalkstein: kieselig  | Mergelstein: Glaukonit   | – |  Obflue-Formation |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15203079 |Formation de Brand | Kalkstein: spätig: Bioklasten-Chert  | Mergelstein   | – |  Brand-Formation |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15203080 |Formation du Horngraben | Kalkstein: sandig  | Mergelstein: Bioklasten   | Brekzie |  Horngraben-Formation |  Hettangien     | Hettangien   | «Rhät»  |
|15203081 |Formation du Lückengraben | Kalkstein: dolomitisch  | Kalkstein: spätig   | Mergelstein |  Lückengraben-Formation |  Rhétien     | Rhétien   | «Rhät»  |
|15203082 |Formation de la Dorfflüe | Kalkstein: mikritisch  | –   | – |  Dorfflüe-Formation |  Berriasien     | Oxfordien   | Malm  |
|15203083 |Microfaciès de la Gummfluh | Kalkstein: arenitisch: Bioklasten  | –   | – |  Gummfluh-Mikrofazies |  Jurassique tardif     | Jurassique tardif   | Malm  |
|15203084 |Microfaciès de Pfad | Kalkstein: Bioklasten  | –   | – |  Pfad-Mikrofazies |  Jurassique tardif     | Jurassique tardif   | Malm  |
|15203085 |Microfaciès à oncolithes (Fm. de la Dorfflüe) | Kalkstein: Onkoide  | –   | – |  Rindenkorn-Mikrofazies |  Jurassique tardif     | Jurassique tardif   | Malm  |
|15203086 |Oolite des Gastlosen | Kalkstein: Ooide  | –   | – |  Gastlosen-Oolith |  Jurassique tardif     | Jurassique tardif   | Malm  |
|15203087 |Microfaciès de la Wandfluh | Kalkstein: mikritisch: Bioklasten  | Kalkstein: Ooide   | – |  Wandfluh-Mikrofazies |  Jurassique tardif     | Jurassique tardif   | Malm  |
|15203088 |Couches à Mytilus | Mergelstein: sandig: Kohle  | Kalkstein: sandig: Bioklasten   | Konglomerat |  Mytilus-Schichten |  Callovien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15203089 |Membre du Col de Cordon | Kalkstein: sandig  | Kalkstein: arenitisch   | Konglomerat |  Col-de-Cordon-Member |  Callovien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15203090 |Conglomérat de la Klus | Kalkstein: sandig: Bioklasten  | –   | – |  Klus-Konglomerat |  Callovien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15203092 |Membre du Rubli | Kalkstein: mergelig: Bioklasten  | Kalkstein: mikritisch: Onkoide   | – |  Rubli-Member |  Callovien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15203093 |Membre de Chavanette | Konglomerat  | Mergelstein: sandig: Kohle   | – |  Chavanette-Member |  Bajocien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15203094 |Membre des Erpilles | Dolomitstein  | Brekzie: dolomitisch   | Mergelstein: schiefrig |  Erpilles-Member |  Ladinien     | Ladinien   | Raibl  |
|15203095 |Formation du Wiriehorn | Kalkstein  | Dolomitstein   | – |  Wiriehorn-Formation |  Anisien     | Anisien   | Karbonatische Trias  |
|15203096 |Formation de St-Triphon | Kalkstein  | Dolomitstein   | Tonstein |  St-Triphon-Formation |  Anisien     | Olénékien   | Karbonatische Trias  |
|15203097 |Membre des Andonces | Kalkstein  | Kalkstein: stromatolithisch   | Tonstein |  Andonces-Member |  Anisien     | Anisien   | Karbonatische Trias  |
|15203098 |Membre du Lessus | Kalkstein  | –   | – |  Lessus-Member |  Anisien     | Anisien   | Karbonatische Trias  |
|15203099 |Membre de Dorchaux | Dolomitstein: stromatolithisch  | Tonstein   | – |  Dorchaux-Member |  Anisien     | Olénékien   | Karbonatische Trias  |
|15203100 |Mélange des Mattes | Tonstein  | Siltstein   | Sandstein |  Mattes-Melange |  Priabonien     | Priabonien   | Mélange  |
|15203101 |Formation de la Chumi | Mergelstein: kalkig  | Sandstein   | Brekzie: polymikt |  Chumi-Formation |  Eocène moyen     | Yprésien   | Flysch  |
|15203102 |Formation de la Joux Verte | Mergelstein  | Kalkstein: kieselig: Glaukonit   | – |  Joux-Verte-Formation |  Turonien     | Barrémien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203103 |Formation de Bonave | Kalkstein: mikritisch: Chert  | Kalkstein: arenitisch   | Brekzie |  Bonave-Formation |  Valanginien     | Tithonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203104 |Brèche Supérieure | Kalkstein: mikritisch  | Brekzie: kalkig   | – |  «Obere Brekzie» (Brekzien-Decke) |  Tithonien     | Kimméridgien   | Lias-Dogger in neritischer Fazies  |
|15203105 |Schistes Ardoisiers | Tonstein: kieselig  | Kalkstein: arenitisch   | – |  «Obere Schiefer» (Brekzien-Decke) |  Oxfordien     | Callovien   | Lias-Dogger in pelagischer Fazies  |
|15203106 |Brèche Inférieure | Brekzie: polymikt  | Brekzie: dolomitisch   | – |  «Untere Brekzie» (Brekzien-Decke) |  Callovien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15203107 |Schistes Inférieurs | Tonstein: sandig-schiefrig  | Kalkstein: spätig   | Brekzie |  «Untere Schiefer» (Brekzien-Decke) |  Aalénien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15203108 |Calcaires Inférieurs | Kalkstein: spätig: Chert  | –   | – |  «Untere Kalke» (Brekzien-Decke) |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15203109 |Trias de la nappe de la Brèche | Dolomitstein  | Gestein: pelitisch   | Kalkstein: Bioklasten |  – |  Trias tardif     | Trias tardif   | Prä-Rift  |
|15203110 |Flysch du Gurnigel | Sandstein  | Mergelstein   | – |  – |  Paléocène     | Maastrichtien   | Flysch  |
|15203111 |Flysch 4 à turbidites silteuses | Mergelstein: tonig  | Sandstein: kalkig   | Sandstein: kieselig |  «Flysch 4 mit siltigen Turbiditen» |  Lutétien     | Lutétien   | Flysch  |
|15200238 |Granite de St-Blasien | Granit: Biotit  | –   | – |  St.-Blasien-Granit |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15200235 |Randgranit | Granit: Biotit-Muskovit  | –   | – |  «Randgranit» |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15200236 |Granite des Münsterhalden | Granit  | –   | – |  Münsterhalden-Granit |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15200237 |Granite de Schönau-Herrenschwand | Granit  | –   | – |  Schönau-Herrenschwand-Granit |  Mississippien     | Dévonien tardif   | Frühvariszisches Grundgebirge  |
|15200239 |Granite de Mambach | Granit  | Granodiorit   | – |  Mambach-Granit |  Mississippien     | Dévonien tardif   | Frühvariszisches Grundgebirge  |
|15200240 |Granite de Lenzkirch-Steina | Granit: Biotit  | –   | – |  Lenzkirch-Steina-Granit |  Mississippien     | Dévonien tardif   | Frühvariszisches Grundgebirge  |
|15200241 |Granite du Hauenstein | Granit  | –   | – |  Hauenstein-Granit |  Mississippien     | Dévonien tardif   | Frühvariszisches Grundgebirge  |
|15200242 |Granite de Böttstein | Granit: porphyrisch: Biotit  | –   | – |  Böttstein-Granit |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15200243 |Roches sédimentaires et volcaniques anté- à éo-varisques de la Forêt Noire | Gestein: sedimentär  | –   | – |  – |  Mississippien     | Dévonien   | Prä- bis frühvariszisches Grundgebirge  |
|15200245 |Socle polycyclique anté-varisque de la Forêt Noire | Gneis: migmatitisch  | Gneis: magmatisch   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15200246 |Orthogneiss de la Forêt Noire | Gneis: magmatisch  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15200247 |Complexe gneissique de Todtmoos-Horbach | Gneis: migmatitisch  | Gneis: Hornblende   | – |  Todtmoos-Horbach-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15200248 |Complexe gneissique du Murgtal | Gneis: migmatitisch: Cordierit  | –   | – |  Murgtal-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15200249 |Complexe gneissique de Laufenburg | Gneis: migmatitisch  | –   | – |  Laufenburg-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15200250 |Migmatites de la Forêt Noire | Gneis: migmatitisch  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15200251 |Complexe du Wiesental-Wehratal | Gneis: migmatitisch  | –   | – |  Wiesen-Wehratal-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15200252 |Syénite du Wehratal | Syenit  | –   | – |  Wehratal-Syenit |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15200253 |Roches vertes de la Forêt Noire | Amphibolit  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15200254 |Molasse | Sandstein  | Mergelstein   | Konglomerat |  – |  Serravallien     | Rupélien   | Molasse  |
|15200255 |Molasse d&#39;eau douce supérieure (OSM) | Mergelstein  | Sandstein   | Konglomerat |  – |  Serravallien     | Burdigalien   | OSM  |
|15200256 |Couches de Tannenberg | Sandstein  | Konglomerat   | – |  Tannenberg-Schichten |  Tortonien     | Serravallien   | Molasse  |
|15200257 |Couches du Pfänder | Konglomerat  | Sandstein   | Mergelstein: tonig |  Pfänder-Formation |  Serravallien     | Burdigalien tardif   | Molasse  |
|15200258 |Formation du Napf | Konglomerat: polymikt: Quarz  | Sandstein: Feldspat   | Mergelstein |  Napf-Formation |  Langhien     | Burdigalien   | OSM  |
|15200259 |Niveau charbonneux du Blapbach | Mergelstein: Kohle  | –   | – |  Blapbach-Kohleflöz |  Burdigalien     | Burdigalien   | OSM  |
|15200260 |Membre d&#39;Eimätteli | Mergelstein: Glimmer  | Konglomerat: ophiolithisch   | Siltstein: tonig |  Eimätteli-Member |  Burdigalien     | Burdigalien   | OSM  |
|15200261 |Poudingue de la Schüpferegg | Konglomerat: polymikt: Quarz  | Sandstein   | Mergelstein |  Schüpferegg-Nagelfluh |  Burdigalien     | Burdigalien   | Molasse  |
|15200262 |OSM-II | Konglomerat  | Sandstein   | – |  – |  Tortonien     | Langhien   | OSM  |
|15200263 |Roches volcaniques du Hegau | Gestein: vulkanisch  | –   | – |  – |  Messinien     | Langhien   | Hegau-Vulkanismus  |
|15200264 |Basalte du Hegau | Basalt  | –   | – |  Höwenegg-Basalt |  Messinien     | Messinien   | Hegau-Vulkanismus  |
|15200265 |Phonolite du Hegau | 15111372  | –   | – |  Hohenwiel-Phonolith |  Tortonien     | Tortonien   | Hegau-Vulkanismus  |
|15200266 |Tuffite du Hegau | Tuffit  | –   | – |  Hegau-Tuffit |  Serravallien     | Langhien   | Hegau-Vulkanismus  |
|15200267 |Poudingue du Hörnligipfel | Konglomerat  | Mergelstein   | Sandstein |  Hörnligipfel-Nagelfluh |  Tortonien     | Tortonien   | OSM  |
|15200268 |Brèche de la Höchegg | Brekzie: sandig  | –   | – |  Höchegg-Brekzie |  Serravallien     | Serravallien   | OSM  |
|15200269 |Marne du Hörnligubel | Mergelstein  | Sandstein: mergelig   | Konglomerat |  Hörnligubel-Mergel |  Tortonien     | Serravallien   | OSM  |
|15200270 |Couches du Tösswald | Konglomerat: kalkig-dolomitisch  | Mergelstein   | Sandstein |  Tösswald-Member |  Serravallien     | Langhien   | OSM  |
|15200271 |Bentonite de Bischofszell | Bentonit  | –   | – |  Bischofzell-Bentonit |  Langhien     | Langhien   | OSM  |
|15200272 |Zone d&#39;Öhningen de la région du Hörnli | Mergelstein  | Siltstein: Kohle   | Sandstein |  Hörnli-Formation |  Langhien     | Langhien   | OSM  |
|15200273 |Couches de Krinau | Konglomerat  | Mergelstein: Kohle   | Sandstein: Glimmer |  Krinau-Member |  Langhien     | Langhien   | OSM  |
|15200274 |Formation du Glimmersand | Sandstein: Quarz-Glimmer  | –   | – |  – |  Tortonien     | Langhien   | OSM  |
|15200275 |Calcaire d&#39;eau douce du Fellitobel | Kalkstein  | –   | – |  Fellitobel-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200276 |Couches de l&#39;Üetliberg | Konglomerat: kalkig-dolomitisch  | Mergelstein   | – |  Uetliberg-Formation |  Serravallien     | Serravallien   | OSM  |
|15200277 |Poudingue de l&#39;Üetliberggipfel | Konglomerat: kalkig-dolomitisch  | –   | – |  Uetliberggipfel-Nagelfluh |  Serravallien     | Serravallien   | OSM  |
|15200278 |Poudingue de l&#39;Üetliberg | Mergelstein  | –   | – |  Uetliberg-Mergel |  Serravallien     | Serravallien   | OSM  |
|15200279 |Marne de la Falätschen | Mergelstein  | –   | – |  Falätschen-Mergel |  Langhien     | Langhien   | OSM  |
|15200280 |Couches du Pfannenstiel | Mergelstein  | Sandstein   | – |  Pfannenstiel-Formation |  Serravallien     | Serravallien   | OSM  |
|15200281 |Couches de Zürich | Mergelstein  | Kalkstein   | – |  Zürich-Formation |  Langhien     | Langhien   | OSM  |
|15200282 |Bentonite de Leimbach | Bentonit  | –   | – |  Leimbach-Bentonit |  Langhien     | Langhien   | OSM  |
|15200283 |Calcaire d&#39;eau douce du Rütschlibach-Riedhof | Kalkstein  | –   | – |  Rütschlibach-Riedhof-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200284 |Bentonite de Winterthur | Bentonit  | –   | – |  Winterthur-Bentonit |  Langhien     | Langhien   | OSM  |
|15200285 |Bentonite de l&#39;Aeugstertal | Bentonit  | –   | – |  Aeugstertal-Bentonit |  Langhien     | Langhien   | OSM  |
|15200286 |Calcaire d&#39;eau douce de l&#39;Äntlisberg-Doldertobel | Kalkstein: Bitumen  | –   | – |  Äntlisberg-Doldertobel-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200287 |Calcaire d&#39;eau douce du Wehrenbach-Höckler | Kalkstein  | Mergelstein: Bitumen   | – |  Wehrenbach-Höckler-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200288 |Bentonite de Küsnacht | Bentonit  | –   | – |  Küsnacht-Bentonit |  Langhien     | Langhien   | OSM  |
|15200289 |Bentonite d&#39;Urdorf | Bentonit  | –   | – |  Urdorf-Bentonit |  Langhien     | Langhien   | OSM  |
|15200290 |Niveau repère de l&#39;Appenzellergranit | Konglomerat  | Sandstein: kalkig   | Siltstein: kalkig |  «Appenzellergranit-Leitniveau» |  Langhien     | Langhien   | OSM  |
|15200291 |Conglomérat d&#39;Abtwil | Konglomerat  | –   | – |  Abtwil-Konglomerat |  Langhien     | Langhien   | OSM  |
|15200292 |Conglomérat d&#39;Hüllistein | Konglomerat: kalkig-dolomitisch  | Brekzie   | – |  Hüllistein-Konglomerat |  Langhien     | Langhien   | OSM  |
|15200293 |Conglomérat de Degersheim | Konglomerat  | Brekzie   | Kalkstein |  Degersheim-Kalknagelfluh |  Langhien     | Langhien   | OSM  |
|15200294 |Calcaire de Meilen | Siltstein: kalkig  | Sandstein: siltig-kalkig   | Kalkstein: arenitisch |  Meilen-Kalk |  Langhien     | Langhien   | OSM  |
|15200295 |OSM-I | Konglomerat  | Sandstein   | Mergelstein |  – |  Langhien     | Burdigalien   | OSM  |
|15200296 |Formation de Lichtensteig | Konglomerat: polymikt  | Sandstein   | Mergelstein |  Lichtensteig-Formation |  Langhien     | Burdigalien tardif   | OSM  |
|15200297 |Formation du Hörnli | Konglomerat  | Sandstein   | Mergelstein |  Hörnli-Formation |  Tortonien     | Langhien   | OSM  |
|15200298 |Formation du Guggershorn | Konglomerat: kalkig-dolomitisch  | Sandstein   | Mergelstein |  Guggershorn-Formation |  Langhien     | Burdigalien tardif   | OSM  |
|15203115 |Flysch 2a argilo-gréseux | Tonstein  | Sandstein: Glaukonit   | – |  «Flysch 2a tonig-sandig» |  Danien     | Danien   | Flysch  |
|15203112 |Flysch 3b à turbidites bioclastiques | Mergelstein  | Sandstein: kalkig: Bioklasten   | – |  «Flysch 3b mit bioklastischen Turbiditen» |  Yprésien     | Yprésien   | Flysch  |
|15203113 |Flysch 3a marno-gréseux | Mergelstein  | Sandstein: kalkig   | – |  «Flysch 3a mergelig-sandig» |  Yprésien     | Yprésien   | Flysch  |
|15203114 |Flysch 2b à turbidites siliceuses | Sandstein: kieselig  | Sandstein: Glaukonit   | Mergelstein |  «Flysch 2b mit sandigen Turbiditen» |  Thanétien     | Thanétien   | Flysch  |
|15203116 |Formation de Hellstätt | Tonstein  | Kalkstein: siltig-tonig   | Sandstein |  Hellstätt-Formation |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203117 |Flysch des Schlieren | Sandstein  | Siltstein   | – |  – |  Yprésien     | Maastrichtien   | Flysch  |
|15203118 |Grès des Schlieren | Sandstein: kalkig: Nummuliten  | Siltstein   | Tonstein |  Schlieren-Sandstein |  Yprésien     | Yprésien   | Flysch  |
|15203119 |Grès de la Schoni | Sandstein: kalkig: Nummuliten  | Siltstein   | Tonstein |  Schoni-Sandstein |  Yprésien     | Yprésien   | Flysch  |
|15203120 |Obere Tonsteinschichten (Flysch des Schlieren) | Tonstein  | Siltstein   | – |  «Obere Tonsteinschichten» (Schlieren-Flysch) |  Yprésien     | Yprésien   | Flysch  |
|15203121 |Grès de Guber | Sandstein  | Siltstein   | – |  Guber-Sandstein |  Thanétien     | Thanétien   | Flysch  |
|15203122 |Untere Tonsteinschichten (Flysch des Schlieren) | Tonstein  | Sandstein: Quarz   | – |  «Untere Tonsteinschichten» (Schlieren-Flysch) |  Paléocène     | Paléocène   | Flysch  |
|15203123 |Flysch basal des Schlieren | Sandstein  | Siltstein   | Kalkstein: mergelig |  – |  Maastrichtien     | Campanien   | Flysch  |
|15203124 |Flysch d&#39;Estavannens | Sandstein: kalkig  | Mergelstein   | Tonstein |  Estavannens-Flysch |  Thanétien     | Danien   | Flysch  |
|15203125 |Formation de Reidigen | Sandstein: Glimmer  | Tonstein   | Kalkstein: mikritisch |  Reidigen-Formation |  Danien     | Maastrichtien   | Flysch  |
|15203126 |Formation du Biot | Sandstein: kalkig  | Kalkstein: mikritisch   | – |  Biot-Formation |  Maastrichtien     | Campanien   | Flysch  |
|15203127 |Formation de Chétillon | Tonstein  | Siltstein   | Sandstein |  Chétillon-Formation |  Santonien     | Coniacien   | Flysch  |
|15203128 |Formation des Rodomonts | Sandstein  | Mergelstein: schiefrig   | Konglomerat: polymikt |  Rodomonts-Formation |  Coniacien     | Turonien   | Flysch  |
|15203129 |Poudingue de la Mocausa | Sandstein  | Konglomerat: polymikt   | – |  Mocausa-Nagelfluh |  Coniacien     | Turonien   | Flysch  |
|15203130 |Mélange de la Tissota | Tonstein  | Mergelstein   | – |  Tissota-Melange |  Santonien     | Santonien   | Mélange  |
|15203131 |Complexe de la Gueyraz | Kalkstein  | Mergelstein   | – |  Gueyraz-Komplex |  Crétacé tardif     | Jurassique précoce   | Mélange  |
|15203132 |Flysch de la Weissenburg | Konglomerat: kalkig  | Sandstein: kalkig-dolomitisch   | Mergelstein |  Weissenburg-Flysch |  Santonien     | Turonien   | Flysch  |
|15203133 |Formation de la Manche | Sandstein: siltig-kalkig  | Mergelstein   | – |  Manche-Formation |  Santonien     | Turonien   | Flysch  |
|15203134 |Formation du Fouyet | Tonstein  | Kalkstein: tonig-schiefrig   | Kalkstein: sandig |  Fouyet-Formation |  Turonien     | Albien   | Flysch  |
|15203135 |Couches à foraminifères | Kalkstein: tonig-schiefrig  | Mergelstein: schiefrig   | – |  «Foraminiferenschichten» (Tissota-Melange) |  Cénomanien     | Barrémien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203136 |Calcaires à Aptychus | Kalkstein: mikritisch: Aptychen  | –   | – |  «Aptychenkalk» (Tissota-Melange) |  Barrémien     | Tithonien   | Maiolica / Aptychenkalk  |
|15203137 |Radiolarites | Gestein: kieselig: Radiolarien  | –   | – |  «Radiolarit» (Tissota-Melange) |  Kimméridgien     | Bathonien   | Radiolarit  |
|15203138 |Calcaires à filaments | Kalkstein: Bioklasten  | Mergelstein   | – |  «Filamentkalk» (Tissota-Melange) |  Callovien     | Aalénien   | Lias-Dogger in pelagischer Fazies  |
|15203139 |Calcaires spathiques | Kalkstein: spätig  | –   | – |  «Spatkalk» (Tissota-Melange) |  Jurassique précoce     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15203140 |Formation du Hundsrügg | Sandstein: Glimmer  | Konglomerat   | – |  Hundsrügg-Formation |  Campanien     | Coniacien   | Flysch  |
|15203141 |Formation des Perrières | Tonstein  | Kalkstein: mikritisch   | Sandstein |  Perrières-Formation |  Coniacien     | Turonien   | Flysch  |
|15203142 |Flysch Rhénodanubien | Sandstein  | Gestein: pelitisch   | – |  – |  Crétacé tardif     | Crétacé précoce   | Flysch  |
|15203143 |Flysch du Vorarlberg | Sandstein  | Gestein: pelitisch   | Kalkstein |  – |  Crétacé tardif     | Crétacé tardif   | Flysch  |
|15203144 |Formation de Fanola | Tonstein: sandig-mergelig  | Brekzie: polymikt   | Sandstein: Quarz |  Fanola-Formation |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203145 |Formation de Planknerbrücke | Sandstein  | Tonstein   | Kalkstein: mikritisch |  Planknerbrücke-Formation |  Maastrichtien     | Campanien   | Flysch  |
|15203146 |Formation de Planken | Kalkstein: mikritisch  | Kalkstein: siltig   | Mergelstein |  Planken-Formation |  Santonien     | Coniacien   | Flysch  |
|15203147 |Formation du Reiselsberg | Sandstein  | Tonstein   | – |  Reiselsberg-Formation |  Turonien     | Turonien   | Flysch  |
|15203148 |Série basale (Fm. du Reiselsberg) | Kalkstein: mergelig  | Tonstein   | Sandstein: Glimmer |  Reiselsberg-Formation |  Turonien     | Turonien   | Flysch  |
|15203149 |Flysch du Liechtenstein | Kalkstein: kieselig: Glaukonit  | Tonstein   | – |  – |  Paléogène     | Crétacé précoce   | Flysch  |
|15203150 |Flysch de Triesen | Kalkstein: kieselig  | Tonstein   | Brekzie: polymikt |  Triesen-Formation |  Yprésien     | Maastrichtien   | Flysch  |
|15203151 |Flysch de Vaduz | Kalkstein: kieselig: Glaukonit  | Mergelstein   | Sandstein |  – |  Maastrichtien     | Turonien   | Flysch  |
|15203152 |Formation de l&#39;Eichholztobel | Kalkstein: kieselig: Glaukonit  | Mergelstein   | – |  Eichholztobel-Formation |  Santonien     | Coniacien   | Flysch  |
|15203153 |Formation de Schloss | Sandstein: Glaukonit  | Kalkstein: kieselig: Glaukonit   | – |  Schloss-Formation |  Turonien     | Turonien   | Flysch  |
|15203154 |Formation de Gaschlo | Sandstein: Quarz  | Kalkstein: kieselig: Glaukonit   | Mergelstein |  Gaschlo-Formation |  Maastrichtien     | Coniacien   | Flysch  |
|15203155 |Calcaire de la Leimern | Kalkstein: mikritisch  | Mergelstein: kalkig   | – |  Leimern-Schichten |  Santonien     | Coniacien   | Couches Rouges  |
|15203156 |Mélange de la Pierre Avoi | Schiefer  | Kalkstein: mergelig   | Brekzie |  Pierre-Avoi-Melange |  Rupélien     | Eocène moyen   | Mélange  |
|15203157 |Formation de St-Christophe | Kalkstein: sandig: Glimmer  | Schiefer: kalkig   | – |  St-Christophe-Formation |  Crétacé tardif     | Crétacé tardif   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203158 |Formation des Marmontains | Schiefer: tonig-kieselig: Bitumen  | Quarzit   | – |  Marmontains-Formation |  Cénomanien     | Aptien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203159 |Formation de l&#39;Aroley | Kalkstein: sandig  | Brekzie: kalkig   | – |  Aroley-Formation |  Aptien     | Barrémien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203160 |Couches de la Peula | Quarzit  | Sandstein: kalkig   | Schiefer: tonig |  Peula-Schichten |  Crétacé précoce     | Crétacé précoce   | Sedimentbedeckung  |
|15203161 |Couches du Versoyen | Basalt  | Gabbro   | Schiefer |  Versoyen-Schichten |  Crétacé     | Crétacé   | Sedimentbedeckung  |
|15203162 |Schistes du Prättigau | Schiefer  | –   | – |  – |  Yprésien     | Valanginien   | Sedimentbedeckung  |
|15203163 |Formation du Ruchberg | Sandstein: Feldspat  | Schiefer: tonig   | Brekzie: polymikt |  Ruchberg-Formation |  Yprésien     | Yprésien   | Sedimentbedeckung  |
|15203164 |Formation de l&#39;Oberälpli | Tonstein: schiefrig  | Kalkstein: sandig-kieselig   | Sandstein: Quarz-Glaukonit |  Oberälpli-Formation |  Thanétien     | Danien   | Sedimentbedeckung  |
|15203165 |Formation de l&#39;Eggberg | Kalkstein: mergelig-schiefrig  | Brekzie: polymikt   | Kalkstein: sandig |  Eggberg-Formation |  Maastrichtien     | Maastrichtien   | Sedimentbedeckung  |
|15203166 |Formation du Gyrenspitz | Brekzie: polymikt  | Kalkstein: sandig-kieselig   | Mergelstein: schiefrig |  Gyrenspitz-Formation |  Maastrichtien     | Campanien   | Sedimentbedeckung  |
|15203167 |Formation de la Fadura | Kalkstein: mergelig-schiefrig  | Kalkstein: sandig-kieselig   | Brekzie |  Fadura-Formation |  Santonien     | Coniacien   | Sedimentbedeckung  |
|15203168 |Formation du Pfävigrat | Kalkstein: sandig-kieselig  | Mergelstein   | Brekzie: polymikt |  Pfävigrat-Formation |  Turonien     | Turonien   | Sedimentbedeckung  |
|15203169 |Formation de la Sassauna | Kalkstein: sandig-kieselig  | Tonstein: schiefrig   | Mergelstein: schiefrig |  Sassauna-Formation |  Cénomanien     | Cénomanien   | Sedimentbedeckung  |
|15203170 |Formation de Valzeina | Tonstein: schiefrig  | Kalkstein: sandig   | – |  Valzeina-Formation |  Albien     | Aptien   | Sedimentbedeckung  |
|15203171 |Formation de la Klus | Kalkstein: sandig-kieselig  | Kalkstein: spätig   | Tonstein: schiefrig |  Klus-Formation |  Barrémien     | Valanginien   | Sedimentbedeckung  |
|15203172 |Flysch du Tomül | Schiefer: sandig-kalkig  | Schiefer: tonig   | – |  Stätzerhorn-Formation |  Eocène     | Crétacé tardif   | Flysch  |
|15200302 |Juranagelfluh (OSM-J) | Konglomerat: kalkig  | –   | – |  – |  Tortonien     | Aquitanien   | OSM  |
|15200299 |Calcaire d&#39;eau douce de Horgen-Käpfnach | Kalkstein  | Gestein: organisch: Kohle   | – |  Horgen-Käpfnach-Süsswasserkalk |  Burdigalien     | Burdigalien   | OSM  |
|15200300 |OSM-J | Sandstein  | Kalkstein: kreidig   | Konglomerat: kalkig |  – |  Langhien     | Burdigalien tardif   | OSM  |
|15200301 |Formation du Bois de Raube | Konglomerat  | Sandstein   | Mergelstein |  Bois-de-Raube-Formation |  Tortonien     | Serravallien   | OSM  |
|15200304 |Bentonite de la Combe Girard | Bentonit  | –   | – |  Combe-Girard-Bentonit |  Langhien     | Langhien   | OSM  |
|15200305 |Calcaire d&#39;eau douce de Vermes | Kalkstein: mikritisch: Bioklasten  | Kalkstein: Onkoide   | Mergelstein |  Vermes-Süsswasserkalk |  Langhien     | Burdigalien   | OSM  |
|15200306 |Gompholite du Locle | Konglomerat: kalkig  | –   | – |  Crêt-du-Locle-Formation |  Langhien     | Langhien   | Molasse  |
|15200307 |Molasse marine supérieure (OMM) | Sandstein  | Mergelstein   | Konglomerat |  – |  Burdigalien     | Aquitanien   | OMM  |
|15200308 |OMM-II | Sandstein  | Konglomerat   | Mergelstein |  – |  Burdigalien     | Burdigalien   | OMM  |
|15200309 |Formation de St-Gall | Sandstein: Glaukonit  | Mergelstein   | Konglomerat |  St.-Gallen-Formation |  Burdigalien tardif     | Burdigalien   | OMM  |
|15200310 |Grès grossier de Staffelbach | Sandstein  | –   | – |  Staffelbach-Grobsandstein |  Burdigalien     | Burdigalien   | OMM  |
|15200311 |OMM-I | Sandstein  | Konglomerat   | Mergelstein |  – |  Burdigalien     | Aquitanien   | OMM  |
|15200312 |Formation de Lucerne | Sandstein: Glaukonit  | Mergelstein   | Konglomerat |  Luzern-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200313 |Grès coquillier de Safenwil | Sandstein: kalkig: Muscheln  | –   | – |  Safenwil-Muschelsandstein |  Burdigalien     | Burdigalien   | OMM  |
|15200314 |Molasse d&#39;eau douce inférieure (USM) | Sandstein  | Konglomerat   | Mergelstein |  – |  Aquitanien     | Rupélien   | USM  |
|15200315 |Poudingue des Höhronen | Konglomerat  | Sandstein   | Siltstein |  Höhronen-Nagelfluh |  Aquitanien     | Aquitanien   | USM  |
|15200316 |Poudingue du Kronberg | Konglomerat: polymikt  | –   | – |  Kronberg-Nagelfluh |  Aquitanien     | Aquitanien   | USM  |
|15200317 |Grès de la Cornalle | Sandstein: kalkig  | Mergelstein: siltig   | – |  Cornalle-Sandstein |  Chattien tardif     | Chattien tardif   | USM  |
|15200318 |Poudingue du Mont Pèlerin | Konglomerat: kalkig  | Mergelstein: siltig   | Sandstein: tonig |  Mont-Pèlerin-Nagelfluh |  Chattien tardif     | Chattien précoce   | USM  |
|15200319 |Formation du Speer | Konglomerat: kalkig  | Mergelstein   | Sandstein: kalkig |  Speer-Formation |  Chattien     | Rupélien   | USM  |
|15200320 |Formation de Thoune | Konglomerat  | Sandstein   | Mergelstein |  Thun-Formation |  Chattien tardif     | Chattien précoce   | USM  |
|15200321 |Poudingue quartzitique de Gunten | Konglomerat: Quarz  | Sandstein   | Mergelstein |  Gunten-Nagelfluh |  Chattien     | Chattien   | USM  |
|15200322 |Formation du Rigi | Konglomerat  | Tonstein: siltig   | – |  Rigi-Formation |  Chattien     | Chattien   | USM  |
|15200323 |Poudingue de la Rigi-Scheidegg | Konglomerat: kalkig  | Mergelstein   | – |  Scheidegg-Nagelfluh |  Chattien     | Chattien   | USM  |
|15200324 |Bunte Rigi-Nagelfluh | Konglomerat: kalkig-dolomitisch  | Sandstein   | Mergelstein |  «Bunte Rigi-Nagelfluh» |  Chattien     | Chattien   | USM  |
|15200325 |Radiolaritreiche Nagelfluh (Fm. du Rigi) | Konglomerat: kalkig  | Sandstein   | Mergelstein |  «Radiolaritreiche Nagelfluh» (Rigi-Fm.) |  Chattien     | Chattien   | USM  |
|15200326 |USM-III | Konglomerat  | Mergelstein   | – |  – |  Burdigalien     | Burdigalien   | USM  |
|15200327 |Poudingue du Sommersberg | Konglomerat  | Mergelstein   | Sandstein: kalkig |  Sommersberg-Nagelfluh |  Burdigalien     | Burdigalien   | USM  |
|15200328 |Poudingue du Brendenbach | Mergelstein  | –   | – |  Brendenbach-Mergel |  Burdigalien     | Burdigalien   | USM  |
|15200329 |USM-II | Sandstein  | Mergelstein   | Konglomerat |  – |  Burdigalien     | Aquitanien   | USM  |
|15200330 |Formation de la Molasse granitique | Sandstein: Feldspat  | Mergelstein   | Konglomerat: polymikt |  «Formation der Granitischen Molasse» |  Aquitanien     | Chattien tardif   | USM  |
|15200331 |Oberaquitane Mergelzone | Mergelstein  | Sandstein: mergelig   | Sandstein: kalkig |  «Oberaquitane Mergelzone» |  Aquitanien     | Aquitanien   | USM  |
|15200332 |Molasse Grise de Lausanne | Sandstein: tonig-kalkig  | Mergelstein: siltig   | – |  «Molasse Grise de Lausanne» |  Aquitanien     | Aquitanien   | USM  |
|15200333 |Bentonite de Bois-Genoud | Bentonit  | –   | – |  Bois-Genoud-Bentonit |  Aquitanien     | Aquitanien   | USM  |
|15200334 |Grès de Cuarny | Sandstein  | –   | – |  Cuarny-Sandstein |  Aquitanien     | Aquitanien   | USM  |
|15200335 |USM-I | Mergelstein  | Sandstein   | Konglomerat |  – |  Chattien     | Rupélien   | USM  |
|15200336 |Grès et Marnes Gris à Gypse | Mergelstein: Gips  | Sandstein   | Kalkstein |  «Grès et Marnes Gris à Gypse» |  Chattien     | Chattien   | USM  |
|15200337 |Molasse à Charbon | Sandstein: kalkig  | Mergelstein: sandig   | Tonstein: Kohle |  «Molasse à Charbon» |  Chattien     | Chattien   | USM  |
|15200338 |Molasse Rouge | Mergelstein  | Siltstein   | Sandstein: kalkig |  – |  Chattien     | Rupélien   | USM  |
|15200339 |Poudingue de Heuboden-Äschitannen | Konglomerat  | Mergelstein   | – |  Heuboden-Äschitannen-Nagelfluh |  Chattien     | Rupélien   | USM  |
|15200340 |Formation de la Beichlen | Konglomerat: kalkig  | Sandstein   | Mergelstein |  Beichlen-Formation |  Rupélien     | Rupélien   | USM  |
|15200341 |USM-J | Sandstein  | Mergelstein   | – |  – |  Chattien     | Chattien   | USM  |
|15200342 |Calcaire d&#39;eau douce de La Chaux | Kalkstein: kreidig: Pisoide  | –   | – |  La-Chaux-Süsswasserkalk |  Aquitanien     | Aquitanien   | USM  |
|15200343 |Molasse alsacienne s.s. | Mergelstein  | Siltstein   | Sandstein: Glimmer |  «Elsässer-Molasse» |  Chattien     | Chattien   | USM  |
|15200344 |Calcaire d&#39;eau douce de Delémont | Kalkstein: mikritisch  | –   | – |  Delémont-Süsswasserkalk |  Chattien     | Chattien   | USM  |
|15200345 |Calcaire d&#39;eau douce de Matzendorf | Kalkstein  | –   | – |  Matzendorf-Süsswasserkalk |  Chattien     | Chattien   | USM  |
|15200346 |Calcaire d&#39;eau douce d&#39;Oensingen | Kalkstein  | –   | – |  Oensingen-Süsswasserkalk |  Chattien     | Chattien   | USM  |
|15200347 |Calcaire d&#39;eau douce de Wynau | Kalkstein  | –   | – |  Wynau-Süsswasserkalk |  Chattien précoce     | Rupélien   | USM  |
|15200348 |Molasse marine inférieure (UMM) | Mergelstein  | Sandstein   | – |  – |  Rupélien     | Rupélien   | UMM  |
|15200349 |UMM-III | Sandstein: kalkig: Glimmer  | Mergelstein   | – |  – |  Rupélien     | Rupélien   | UMM  |
|15200350 |Grès d&#39;Horw | Sandstein: kalkig: Glimmer  | Mergelstein   | – |  Horw-Sandstein |  Rupélien     | Rupélien   | UMM  |
|15200351 |UMM-II | Mergelstein  | Sandstein: kalkig: Glimmer   | – |  – |  Rupélien     | Rupélien   | UMM  |
|15200352 |Marne de Grisigen | Mergelstein  | Sandstein: kalkig: Glimmer   | – |  Grisigen-Mergel |  Rupélien     | Rupélien   | UMM  |
|15200353 |UMM-I | Mergelstein: tonig  | Siltstein   | Sandstein: tonig: Lithoklasten |  – |  Rupélien     | Rupélien   | UMM  |
|15200354 |Sous-formation de Cucloz | Sandstein: Glimmer  | Mergelstein   | Siltstein |  Cucloz-Formation |  Rupélien     | Rupélien   | UMM  |
|15200355 |Grès de Cucloz | Sandstein: Glimmer  | Brekzie: polymikt   | – |  Cucloz-Sandstein |  Rupélien     | Rupélien   | UMM  |
|15200356 |Marnes gris-souris | Mergelstein  | Siltstein   | – |  «Marnes gris-souris» (Cucloz-Fm.) |  Rupélien     | Rupélien   | UMM  |
|15200357 |Schistes marno-micacés | Mergelstein: siltig: Glimmer  | Sandstein   | – |  «Schistes marno-micacés» (Cucloz-Fm.) |  Rupélien     | Rupélien   | UMM  |
|15200358 |Formation de la Hilfern | Mergelstein: tonig  | Siltstein   | Sandstein |  Hilfern-Formation |  Rupélien     | Rupélien   | UMM  |
|15200359 |Sous-formation de Rietbad | Sandstein  | Mergelstein   | Konglomerat |  Rietbad-Formation |  Rupélien     | Rupélien   | UMM  |
|15200360 |Marne du Jordisboden | Mergelstein: Glimmer  | Sandstein   | – |  Jordisboden-Mergel |  Rupélien     | Rupélien   | UMM  |
|15200361 |Grès de la Goldegg | Sandstein: Glimmer  | Konglomerat: polymikt   | – |  Goldegg-Sandstein |  Rupélien     | Rupélien   | UMM  |
|15203176 |Calcaire de la Nolla | Schiefer: sandig-kalkig  | Schiefer: tonig   | – |  Nolla-Kalkschiefer |  Cénomanien     | Cénomanien   | Sedimentbedeckung  |
|15203173 |Hauptkonglomerat (Flysch du Tomül) | Konglomerat: kalkig  | –   | – |  «Hauptkonglomerat» |  Coniacien     | Coniacien   | Flysch  |
|15203174 |Formation du Carnusa(horn) | Sandstein: kalkig: Quarz  | Schiefer: tonig   | Konglomerat |  Carnusa-Formation |  Turonien     | Turonien   | Sedimentbedeckung  |
|15203175 |Calcaire de Safien | Kalkstein: sandig  | –   | – |  Safien-Kalk |  Turonien     | Turonien   | Sedimentbedeckung  |
|15203177 |Argillite de la Nolla | Schiefer: tonig: Bitumen  | Kalkstein: sandig   | – |  Nolla-Tonschiefer |  Albien     | Aptien   | Sedimentbedeckung  |
|15203178 |Formation du Bärenhorn | Schiefer: sandig-tonig  | Schiefer: kalkig   | Prasinit |  Bärenhorn-Formation |  Barrémien     | Berriasien   | Sedimentbedeckung  |
|15203179 |Roches vertes (Grava/Tomül) | Prasinit  | Basalt   | – |  – |  Jurassique tardif     | Jurassique tardif   | Sedimentbedeckung  |
|15203180 |Mélange du Tomül | Brekzie  | Quarzit   | Amphibolit |  – |  Mésozoïque     | Mésozoïque   | Mélange  |
|15203181 |Série du Tounô | Marmor  | Schiefer: tonig   | Schiefer: sandig-kalkig |  – |  Eocène     | Trias moyen   | Sedimentbedeckung  |
|15203182 |Série du Barrhorn | Schiefer: kalkig  | Marmor   | Dolomitstein |  – |  Eocène     | Mésozoïque   | Sedimentbedeckung  |
|15203183 |Formation du Bruneggjoch | Quarzit  | Konglomerat: Quarz   | – |  Bruneggjoch-Formation |  Trias précoce     | Lopingien   | Detritische Trias  |
|15203184 |Membre de Sous le Rocher | Quarzit  | Konglomerat: Quarz   | Sandstein: kalkig |  Sous-le-Rocher-Member |  Trias précoce     | Lopingien   | Detritische Trias  |
|15203185 |Gneiss oeillé de Randa | Granit: porphyrisch  | Gneis: augig   | – |  Randa-Augengneis |  Guadalupien     | Cisuralien   | Variszisches Grundgebirge  |
|15203186 |Formation du Col de Chassoure | Schiefer: Quarz-Serizit  | Quarzit   | Gestein: vulkanisch |  Col-de-Chassoure-Formation |  Lopingien     | Cisuralien   | Grundgebirge  |
|15203187 |Membre de la Gouille Verte | Schiefer: Quarz-Serizit  | Schiefer: Serizit-Chlorit   | – |  Gouille-Verte-Member |  Lopingien     | Lopingien   | Grundgebirge  |
|15203188 |Membre de la Matse | Schiefer: Serizit  | Gestein: vulkanisch   | Dolomitstein |  Matse-Member |  Lopingien     | Lopingien   | Grundgebirge  |
|15203189 |Membre de la Dent de Nendaz | Konglomerat: polymikt  | Sandstein   | Schiefer: tonig |  Dent-de-Nendaz-Member |  Lopingien     | Cisuralien   | Grundgebirge  |
|15203190 |Membre du Goli d&#39;Aget | Konglomerat  | Sandstein: Feldspat   | Schiefer: Chlorit |  Goli-d&#39;Aget-Member |  Guadalupien     | Cisuralien   | Grundgebirge  |
|15203191 |Membre de la Mondra | Schiefer: Quarz-Chlorit  | Schiefer: Anthrazit   | – |  Mondra-Member |  Cisuralien     | Cisuralien   | Grundgebirge  |
|15203192 |Membre de Cleuson | Rhyolith  | Konglomerat   | Schiefer: Quarz |  Cleuson-Member |  Cisuralien     | Cisuralien   | Grundgebirge  |
|15203193 |Formation du Métailler | Gneis: Chlorit  | Schiefer: Chlorit   | Prasinit |  Métailler-Formation |  Frühes Ordovizium     | Cambrien   | Grundgebirge  |
|15203194 |Formation du Distulberg | Schiefer: Glimmer  | Prasinit: Albit-Chlorit   | Gneis |  Distulberg-Formation |  Cambrien     | Cambrien   | Grundgebirge  |
|15203195 |Métagranophyre de Thyon | Granophyr  | –   | – |  Thyon-Metagranophyr |  Cambrien     | Cambrien   | Grundgebirge  |
|15203196 |Métagranite du Mont Rogneux | Granit: Biotit  | –   | – |  Mont-Rogneux-Metagranit |  Cambrien     | Cambrien   | Grundgebirge  |
|15203197 |Formation de Lirec | Gneis: augig  | Gneis: gebändert   | Gestein: vulkanisch |  Lirec-Formation |  Cambrien     | Cambrien   | Grundgebirge  |
|15203198 |Formation de l&#39;Adlerflüe | Amphibolit: gebändert  | Gneis   | Schiefer: augig: Glimmer |  Adlerflüe-Formation |  Cambrien     | Protérozoïque   | Grundgebirge  |
|15203199 |Complexe de l&#39;Ergischhorn | Gneis  | Amphibolit   | – |  Ergischhorn-Komplex |  Protérozoïque     | Protérozoïque   | Grundgebirge  |
|15203200 |Flysch du Gelbhorn | Tonstein: schiefrig  | Marmor: kalkig: Serizit   | – |  Gelbhorn-Flysch |  Eocène     | Crétacé   | Flysch  |
|15203201 |Groupe de l&#39;Obrist | Marmor: kalkig: Serizit  | Quarzit   | Schiefer: tonig |  Obrist-Formation |  Crétacé     | Jurassique tardif   | Sedimentbedeckung  |
|15203202 |Brèche du Vizan | Brekzie: dolomitisch  | Sandstein: Feldspat   | – |  Vizan-Brekzie |  Albien     | Toarcien   | Sedimentbedeckung  |
|15203203 |Marbre de la Tschera | Marmor: kalkig  | –   | – |  Tschera-Marmor |  Tithonien     | Oxfordien   | Sedimentbedeckung  |
|15203204 |Brèche du Wissberg | Brekzie: kalkig-dolomitisch  | Marmor: kalkig   | – |  Wissberg-Brekzie |  Tithonien     | Oxfordien   | Sedimentbedeckung  |
|15203205 |Groupe de Nisellas | Schiefer: tonig  | Schiefer: sandig-kalkig   | Brekzie: kalkig-dolomitisch |  Nisellas-Formation |  Callovien     | Aalénien   | Sedimentbedeckung  |
|15203206 |Groupe de la Tumpriv | Rauwacke  | Evaporit: Gips   | Dolomitstein |  Tumpriv-Formation |  Toarcien     | Carnien   | Sedimentbedeckung  |
|15203207 |Groupe du Kalkberg | Dolomitstein  | Kalkstein   | – |  Kalkberg-Formation |  Ladinien     | Anisien   | Sedimentbedeckung  |
|15203208 |Groupe de Bavugls | Dolomitstein  | Quarzit   | Konglomerat |  Bavugls-Formation |  Trias moyen     | Carbonifère   | Sedimentbedeckung  |
|15203209 |Socle cristallin du Nolla | Gneis: schiefrig  | –   | – |  – |  Carbonifère     | Carbonifère   | Grundgebirge  |
|15203210 |Flysch de la nappe du Falknis | Kalkstein: sandig-kieselig  | Sandstein: Quarz   | Tonstein |  – |  Lutétien     | Yprésien   | Flysch  |
|15203211 |Globorotalien-Schichten | Sandstein: kalkig  | Kalkstein: mergelig   | Tonstein: schiefrig |  «Globorotalien-Schichten» |  Thanétien     | Danien   | Sedimentbedeckung  |
|15203212 |Quarzsandstein-Flysch (Gault) | Sandstein: Quarz-Glaukonit  | Kalkstein: sandig   | Konglomerat: polymikt |  «Quarzsandstein-Flysch» |  Cénomanien     | Aptien   | «Gault»  |
|15203213 |Formation de Tristel | Kalkstein: sandig  | Brekzie: kalkig-dolomitisch   | Tonstein |  Tristel-Formation |  Aptien     | Barrémien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203214 |Fleckenkalk-Flysch (Neokom) | Kalkstein: mergelig  | Kalkstein: kieselig   | Tonstein: sandig |  «Fleckenkalk-Flysch» |  Barrémien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203215 |Formation de la Jes | Kalkstein: mikritisch: Chert  | Brekzie: kalkig-dolomitisch   | Mergelstein |  Jes-Formation |  Berriasien     | Tithonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203216 |Brèche du Falknis | Brekzie: polymikt  | Sandstein: kalkig   | Kalkstein: kieselig |  Falknis-Brekzie |  Tithonien     | Kimméridgien   | Post-Rift Mesozoikum in detritischer Fazies  |
|15203217 |Formation de Sanalada | Mergelstein  | Kalkstein: mergelig   | Kalkstein: arenitisch |  Sanalada-Formation |  Kimméridgien     | Oxfordien   | Post-Rift Mesozoikum in detritischer Fazies  |
|15203218 |Formation de Panier | Mergelstein: schiefrig  | Tonstein   | Brekzie: polymikt |  Panier-Formation |  Oxfordien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15203219 |Flysch de la nappe de la Suzfluh | Tonstein: schiefrig  | Sandstein   | Kalkstein: kieselig |  – |  Yprésien     | Thanétien   | Flysch  |
|15203220 |Calcaire de la Sulzfluh | Kalkstein: mikritisch  | Kalkstein: Ooide   | Kalkstein: arenitisch |  Sulzfluh-Kalk |  Tithonien     | Tithonien   | Malm  |
|15203221 |Granite de la nappe de la Suzfluh | Granit  | –   | – |  – |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203222 |Flysch de la nappe de la Tasna | Tonstein  | Sandstein   | – |  – |  Yprésien     | Yprésien   | Flysch  |
|15203223 |Calcaire du Steinsberg | Kalkstein: spätig: Bioklasten  | Kalkstein: sandig: Bioklasten   | – |  Steinsberg-Kalk |  Jurassique précoce     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15203224 |Granite de la nappe de la Tasna | Granit  | –   | – |  Plattamala-Granit |  Paléozoïque     | Protérozoïque   | Variszisches Grundgebirge  |
|15203225 |Série Rousse | Marmor: sandig  | Marmor: tonig-schiefrig   | Konglomerat |  «Série-Rousse» |  Crétacé tardif     | Cénomanien   | Couches Rouges  |
|15203226 |Série Grise | Schiefer: kalkig  | Marmor   | Prasinit |  «Série Grise» |  Crétacé tardif     | Cénomanien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203227 |Série de la Garde de Bordon | Schiefer: tonig: Bitumen  | Schiefer: kalkig   | – |  Garda-Bordon-Formation |  Crétacé tardif     | Crétacé précoce   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203228 |Flysch de la Fêta d&#39;Août | Schiefer: tonig  | Marmor: kalkig   | – |  Fêta-d&#39;Août-Formation |  Crétacé tardif     | Crétacé précoce   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203229 |Gabbro de l&#39;Allalin | Gabbro  | Gabbro: Omphazit   | – |  Allalin-Gabbro |  Oxfordien     | Bathonien   | Ophiolithische Abfolge  |
|15203230 |Mélange d&#39;Arosa | Gestein: pelitisch  | Sandstein: tonig: Lithoklasten   | – |  – |  Paléogène     | Crétacé tardif   | Mélange  |
|15203231 |Formation de la Verspala | Sandstein: tonig  | Mergelstein   | – |  Verspala-Formation |  Coniacien     | Cénomanien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203232 |Formation de Lavagna | Schiefer: kieselig  | –   | – |  Lavagna-Formation |  Albien     | Aptien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203233 |Formation à Palombini | Schiefer: tonig-kieselig  | Marmor: kalkig-kieselig   | – |  «Palombini-Formation» |  Barrémien     | Tithonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15200365 |Marnes à Foraminifères (Foraminiferenmergel) | Mergelstein: sandig: Glimmer  | –   | – |  «Foraminiferenmergel» (UMM-J) |  Rupélien     | Rupélien   | UMM  |
|15200362 |UMM-J | Sandstein: kalkig  | Mergelstein   | Tonstein |  – |  Chattien     | Rupélien   | UMM  |
|15200363 |Argile à Septaria (Septarienton) | Tonstein: mergelig: Glimmer  | Sandstein   | – |  «Septarienton» (UMM-J) |  Chattien     | Rupélien   | UMM  |
|15200364 |Schistes à Poissons (Fischschiefer) | Tonstein: siltig  | Tonstein: mergelig   | – |  «Fischschiefer» (UMM-J) |  Rupélien     | Rupélien   | UMM  |
|15200366 |Meeressand | Sandstein: kalkig: Quarz  | Konglomerat: kalkig   | – |  «Meeressand» (UMM-J) |  Chattien     | Rupélien   | UMM  |
|15200368 |Banc à Cyathula (bassin de Laufon) | Mergelstein  | –   | – |  «Cyathulabank» (UMM-J) |  Rupélien     | Priabonien   | UMM  |
|15200369 |Marne à Cyrènes | Mergelstein  | Sandstein: Glimmer   | – |  «Cyrenenmergel» (UMM-J) |  Chattien     | Chattien   | UMM  |
|15200370 |Conglomérat de Porrentruy | Konglomerat: kalkig  | –   | – |  Porrentruy-Konglomerat |  Rupélien     | Priabonien   | USM  |
|15200371 |Raitsche | Kalkstein  | –   | – |  Rossemaison-Formation |  Rupélien     | Priabonien   | Siderolithikum  |
|15200373 |Gompholite d&#39;Ajoie | Brekzie: kalkig  | –   | – |  Ajoie-Gompholit |  Rupélien     | Rupélien   | UMM  |
|15200378 |Calcaire d&#39;eau douce de Tüllingen | Kalkstein: mikritisch  | Mergelstein   | – |  Tüllingen-Süsswasserkalk |  Chattien tardif     | Chattien tardif   | USM  |
|15200380 |Partie supérieure du Hauptrogenstein | Kalkstein: Ooide  | Mergelstein   | – |  Hauptrogenstein |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200382 |Partie inférieure du Hauptrogenstein | Kalkstein: Ooide  | Mergelstein   | – |  Hauptrogenstein |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200383 |Calcaire roux marneux | Kalkstein: mergelig: Bioklasten  | –   | – |  «Calcaire roux marneux» (Hauptrogenstein) |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200384 |Membre d&#39;Ajoie | Sandstein  | Mergelstein   | Konglomerat |  Ajoie-Member |  Miocène tardif     | Miocène tardif   | OSM  |
|15200385 |Membre du Bois de Raube | Konglomerat  | Sandstein   | Mergelstein |  Bois-de-Raube-Member |  Serravallien     | Serravallien   | OSM  |
|15200386 |Membre du Montchaibeux | Sandstein  | Mergelstein   | – |  Montchaibeux-Member |  Serravallien     | Serravallien   | OSM  |
|15200387 |Conglomérat de Daubrée | Konglomerat: kalkig-residual: Eisenpisoide  | –   | – |  «Daubrée-Konglomerat» |  Priabonien     | Eocène moyen   | Siderolithikum  |
|15200388 |Dépôts de blocs pérégrins (Wanderblock-Bildungen) | Gestein: residual  | –   | – |  – |  Pliocène     | Miocène tardif   | Post-Messinien  |
|15200389 |Sables à galets (OMM) | Sandstein: konglomeratisch  | –   | – |  – |  Burdigalien     | Burdigalien   | OMM  |
|15200390 |Poudingue polygénique (OMM) | Konglomerat: polymikt  | –   | – |  – |  Burdigalien     | Burdigalien   | OMM  |
|15200391 |Zone du grès coquillier (OMM) | Sandstein: kalkig: Muscheln  | –   | – |  – |  Burdigalien     | Burdigalien   | OMM  |
|15200392 |Molasse Grise (OMM) | Sandstein: Glimmer  | Sandstein: kalkig: Muscheln   | – |  – |  Burdigalien     | Burdigalien   | OMM  |
|15200393 |Calcaire de Daubrée | Kalkstein: Eisenooide  | –   | – |  «Daubrée-Konglomerat» |  Eocène moyen     | Eocène moyen   | Siderolithikum  |
|15200394 |Formations de la base de l&#39;USM-J | Kalkstein  | Gestein: residual: Eisenmineralien   | – |  – |  Rupélien     | Priabonien   | USM  |
|15200395 |Juranagelfluh de Laufon | Konglomerat: kalkig  | –   | – |  Laufen-Juranagelfluh |  Tortonien     | Langhien   | OSM  |
|15200396 |Juranagelfluh du Jura bâlois | Konglomerat: kalkig  | Sandstein   | Mergelstein |  Basler Juranagelfluh |  Langhien     | Langhien   | OSM  |
|15200397 |Juranagelfluh d&#39;Argovie | Konglomerat: kalkig  | –   | – |  Aargauer Juranagelfluh |  Tortonien     | Langhien   | OSM  |
|15200399 |Couches du Jensberg | Sandstein: Glaukonit  | Mergelstein   | – |  Jensberg-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200400 |Couches du Rebhubel | Sandstein: mergelig: Glimmer  | Sandstein: konglomeratisch   | Konglomerat |  Rebhubel-Schichten |  Burdigalien tardif     | Burdigalien tardif   | OMM  |
|15200401 |Formation de Niedermatt | Sandstein  | Konglomerat: polymikt   | – |  Niedermatt-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200402 |Formation du Belpberg | Sandstein  | Mergelstein   | Konglomerat |  Belpberg-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200403 |Poudingue de la Pfadflüe | Konglomerat: kalkig  | Mergelstein   | Sandstein |  Pfadflüe-Member |  Burdigalien     | Burdigalien   | Molasse  |
|15200404 |Poudingue calcaire de Sädel | Konglomerat: kalkig  | –   | – |  Sädel-Kalknagelfluh |  Burdigalien     | Burdigalien   | OMM  |
|15200405 |Grès coquillier d&#39;Utzigen | Sandstein: kalkig: Muscheln  | –   | – |  Utzigen-Muschelsandstein |  Burdigalien     | Burdigalien   | OMM  |
|15200406 |Poudingue quarzitique d&#39;Ulmiz | Konglomerat: Quarz  | –   | – |  Ulmiz-Quarzitnagelfluh |  Burdigalien     | Burdigalien   | OMM  |
|15200407 |Poudingue du Bütschelbach | Konglomerat  | –   | – |  Bütschelbach-Nagelfluh |  Burdigalien     | Burdigalien   | OMM  |
|15200408 |Formation de Kalchstätten | Konglomerat: kalkig  | Sandstein   | Mergelstein |  Kalchstätten-Formation |  Langhien     | Burdigalien   | Molasse  |
|15200409 |Poudingue du Freudenberg | Konglomerat: kalkig  | –   | – |  Freudenberg-Nagelfluh |  Burdigalien     | Burdigalien   | OMM  |
|15200410 |Couches de Goldbrunnen | Mergelstein  | Sandstein   | – |  Goldbrunnen-Schichten |  Burdigalien     | Burdigalien   | OMM  |
|15200411 |Poudingue de Dreilinden | Konglomerat  | –   | – |  Dreilinden-Nagelfluh |  Burdigalien     | Burdigalien   | OMM  |
|15200412 |Obere Grenznagelfluh (Fm. de Saint-Gall) | Konglomerat  | –   | – |  «Obere Grenznagelfluh» |  Burdigalien     | Burdigalien   | OMM  |
|15200413 |Formation de Kirchberg | Tonstein  | Mergelstein   | – |  Kirchberg-Formation |  Burdigalien tardif     | Burdigalien tardif   | Molasse  |
|15200414 |Formation de Grimmelfingen | Tonstein  | Mergelstein   | Sandstein |  Grimmelfingen-Formation |  Burdigalien tardif     | Burdigalien tardif   | Molasse  |
|15200415 |Couches de la Chnebelburg | Sandstein: Glaukonit  | Sandstein: kalkig: Muscheln   | Mergelstein |  Chnebelburg-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200416 |Grès coquillier de Meinisberg | Sandstein: kalkig: Muscheln  | –   | – |  Meinisberg-Muschelsandstein |  Burdigalien     | Burdigalien   | OMM  |
|15200417 |Poudingue coquillier de Brüttelen | Sandstein: konglomeratisch-kalkig: Muscheln  | –   | – |  Brüttelen-Grobsandstein |  Burdigalien     | Burdigalien   | OMM  |
|15200418 |Formation de la Singine | Sandstein: Glaukonit  | Siltstein   | Mergelstein |  Sense-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200419 |Couches de Montécu | Mergelstein: siltig  | –   | – |  Montécu-Schichten |  Burdigalien     | Burdigalien   | OMM  |
|15200420 |Grès coquillier de la Molière | Sandstein: kalkig: Muscheln  | –   | – |  Molière-Muschelsandstein |  Burdigalien     | Burdigalien   | OMM  |
|15200421 |Poudingue quartzitique du Scherli(grabe) | Konglomerat: Quarz  | –   | – |  Scherli-Quarzitnagelfluh |  Burdigalien     | Burdigalien   | OMM  |
|15200422 |Calcaire d&#39;eau douce de Grilly | Kalkstein  | –   | – |  Grilly-Süsswasserkalk |  Rupélien     | Rupélien   | USM  |
|15200423 |Calcaire d&#39;eau douce d&#39;Orbe | Kalkstein: Bitumen-Bioklasten  | –   | – |  Orbe-Süsswasserkalk |  Rupélien     | Priabonien   | USM  |
|15200424 |Calcaire concrétionné (USM) | Kalkstein: pedogen-verkrustet  | –   | – |  – |  Rupélien     | Priabonien   | USM  |
|15200425 |Formation de Gümmenen | Sandstein  | Mergelstein: siltig   | – |  Gümmenen-Formation |  Aquitanien     | Chattien tardif   | USM  |
|15200429 |Molasse bariolée supérieure | Mergelstein: siltig  | Sandstein   | Sandstein: kalkig |  «Obere Bunte Molasse» (USM-II) |  Aquitanien     | Aquitanien   | USM  |
|15200430 |Calcaire d&#39;eau douce d&#39;Oberdorf | Kalkstein: kreidig  | Mergelstein   | – |  Oberdorf-Süsswasserkalk |  Rupélien     | Rupélien   | Siderolithikum  |
|15200431 |Horizon limnique (OMM-II) | Mergelstein: siltig  | Kalkstein   | – |  St.-Gallen-Formation |  Burdigalien tardif     | Burdigalien tardif   | OMM  |
|15200432 |Poudingue quartzitique (Fm. de Saint-Gall) | Konglomerat: Quarz  | Konglomerat: kalkig: Muscheln   | – |  – |  Burdigalien     | Burdigalien   | OMM  |
|15200433 |Conglomérat basal (Fm. de Lucerne) | Konglomerat: polymikt  | –   | – |  Luzern-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200436 |Membre de Poncin | Sandstein: Glimmer-Glaukonit  | –   | – |  Poncin-Member |  Cénomanien     | Cénomanien   | «Gault»  |
|15200437 |Grès de la Vraconne | Sandstein: Glaukonit  | Mergelstein: sandig   | – |  Vraconne-Sandstein |  Albien     | Albien   | «Gault»  |
|15203238 |Conglomérat de Buufal | Konglomerat: dolomitisch  | –   | – |  Buufal-Konglomerat |  Priabonien     | Eocène moyen   | Mélange  |
|15203234 |Calcaire à Calpionelles de la zone d&#39;Arosa | Kalkstein: mikritisch: Aptychen  | –   | – |  – |  Tithonien     | Tithonien   | Maiolica / Aptychenkalk  |
|15203235 |Radiolarite de la zone d&#39;Arosa | Gestein: kieselig: Radiolarien  | Schiefer: kieselig   | – |  – |  Kimméridgien     | Oxfordien   | Radiolarit  |
|15203236 |Ophiolite de la zone d&#39;Arosa | Serpentinit  | Gabbro   | Basalt |  – |  Oxfordien     | Bathonien   | Ophiolithische Abfolge  |
|15203239 |Membre de Langel | Kalkstein: Ooide  | Kalkstein: Onkoide   | – |  Langel-Member |  Bathonien     | Bajocien   | Syn-Rift  |
|15203240 |Cornieule Supérieure | Rauwacke  | –   | – |  «Obere Rauhwacke» (Pralet-Fm.) |  Carnien     | Carnien   | Raibl  |
|15203241 |Gypse de la nappe des Préalpes Médianes | Evaporit: Gips  | –   | – |  Clôt-la-Cime-Formation |  Trias     | Trias   | Raibl  |
|15203242 |Couches Rouges de la nappe de la Brèche | Kalkstein: tonig  | Brekzie   | – |  – |  Thanétien     | Campanien   | Couches Rouges  |
|15203243 |Cornieule de la nappe de la Brèche | Rauwacke  | –   | – |  – |  Trias     | Trias   | Prä-Rift  |
|15203244 |Grès du Lamperehubel | Sandstein: kalkig  | –   | – |  Lamperehubel-Sandstein |  Albien     | Albien   | Flysch  |
|15203245 |Ophiolite des Gets | Serpentinit  | Gabbro   | Basalt |  Gets-Ophiolith |  Bathonien     | Bathonien   | Ophiolithische Abfolge  |
|15203246 |Obere Kalk- und Tonschiefer (Grava/Tomül) | Schiefer: kalkig: Glimmer  | Schiefer: tonig   | – |  – |  Jurassique moyen     | Jurassique moyen   | Sedimentbedeckung  |
|15203247 |Quarzit und quarzitische Schiefer (Grava/Tomül) | Quarzit: kalkig  | Schiefer: kalkig: Glimmer   | – |  – |  Jurassique moyen     | Jurassique moyen   | Sedimentbedeckung  |
|15203248 |Untere Kalk- und Tonschiefer (Grava/Tomül) | Schiefer: tonig  | Schiefer: kalkig   | Schiefer: sandig |  – |  Jurassique précoce     | Jurassique précoce   | Sedimentbedeckung  |
|15203249 |Marbre du Piz Aul | Marmor  | –   | – |  Aul-Marmor |  Tithonien     | Oxfordien   | Sedimentbedeckung  |
|15203250 |Brèche (Grava/Tomül) | Brekzie: dolomitisch  | –   | – |  – |  Jurassique précoce     | Jurassique précoce   | Sedimentbedeckung  |
|15203251 |Gryphäenkalk | Kalkstein: sandig: Bioklasten  | –   | – |  – |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15203252 |Trias nord-pennique | Quarzit  | Marmor: dolomitisch   | Sandstein: Feldspat |  – |  Trias     | Trias   | Prä-Rift  |
|15203253 |Orthogneiss de Zervreila | Gneis: granitisch-augig  | –   | – |  Zervreila-Orthogneis |  Cisuralien     | Cisuralien   | Grundgebirge  |
|15203254 |Gneiss oeillé du Garenstock | Gneis: augig  | –   | – |  Garenstock-Augengneis |  Ordovicien     | Ordovicien   | Grundgebirge  |
|15203255 |Adula-D.: Glimmerschiefer und Paragneis | Schiefer: Glimmer  | Gneis   | – |  Salahorn-Formation |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203256 |Adula-D.: Amphibolit | Amphibolit  | –   | – |  – |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203257 |Mélange Submédian | Evaporit: Gips  | Tonstein   | – |  – |  Paléogène     | Crétacé tardif   | Mélange  |
|15203258 |Brèche de la Truche | Brekzie: polymikt  | –   | – |  Truche-Brekzie |  Eocène     | Eocène   | Mélange  |
|15203259 |Brèche de Trom | Brekzie: polymikt  | Kalkstein: mikritisch   | – |  Trom-Brekzie |  Tertiaire     | Crétacé tardif   | Mélange  |
|15203260 |Brèche d&#39;Exergillod | Brekzie  | Brekzie: kalkig: Bioklasten   | – |  Exergillod-Brekzie |  Jurassique tardif     | Jurassique précoce   | Mélange  |
|15203261 |Calcaire du Troublon | Kalkstein: mikritisch: Bioklasten  | Sandstein: mergelig   | – |  Troublon-Kalk |  Jurassique tardif     | Jurassique tardif   | Mélange  |
|15203262 |Calcaire noduleux de la Zünegg | Kalkstein: mergelig  | –   | – |  Zünegg-Knollenkalk |  Jurassique tardif     | Jurassique tardif   | Mélange  |
|15203263 |Formation de Hauta-Crêtaz | Kalkstein: spätig: Bioklasten  | Brekzie: kalkig   | – |  Hauta-Crêtaz-Formation |  Jurassique tardif     | Jurassique précoce   | Mélange  |
|15203264 |Brèche de la Pointe de l&#39;Au | Brekzie: kalkig  | –   | – |  Pointe-de-l&#39;Au-Brekzie |  Bathonien     | Bathonien   | Mélange  |
|15203265 |Calcaire de Bonaveau | Kalkstein: sandig  | Kalkstein: sandig   | – |  Bonaveau-Kalk |  Toarcien     | Toarcien   | Mélange  |
|15203266 |Calcaire du Sex du Tronc | Kalkstein: spätig: Bioklasten  | –   | – |  Sex-du-Tronc-Kalk |  Sinémurien     | Sinémurien   | Mélange  |
|15203267 |Calcaire du Sex de Grand-Herba | Kalkstein  | –   | – |  Grand-Herba-Kalk |  Sinémurien     | Sinémurien   | Mélange  |
|15203268 |Formation d&#39;Oudiou | Kalkstein: Bioklasten  | Kalkstein: kieselig-spätig   | – |  Oudiou-Formation |  Aalénien     | Rhétien   | Syn-Rift  |
|15203269 |Malm de la nappe des Préalpes Médianes | Kalkstein  | Mergelstein   | – |  – |  Berriasien     | Oxfordien   | Malm  |
|15203270 |Série d&#39;Albeuve | Mergelstein: Glaukonit-Bioklasten  | –   | – |  Albeuve-Serie |  Kimméridgien     | Kimméridgien   | Malm  |
|15203271 |Couches de la Kummli | Kalkstein: mikritisch  | –   | – |  Kummli-Schichten |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203272 |Dogger de la nappe des Préalpes Médianes | Kalkstein  | Mergelstein   | – |  – |  Callovien     | Bajocien   | Syn-Rift  |
|15203273 |Calcaire de la Stockenflue | Kalkstein: sandig: Bioklasten  | –   | – |  Stockenflue-Kalk |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15203274 |Membre de Mieussy | Kalkstein: arenitisch  | Kalkstein: Bioklasten   | Kalkstein: mikritisch |  Mieussy-Member |  Bathonien     | Bajocien   | Syn-Rift  |
|15203275 |Lias de la nappe des Préalpes Médianes | Mergelstein  | Kalkstein: spätig   | Kalkstein: kieselig |  – |  Bajocien     | Rhétien   | Syn-Rift  |
|15203276 |Trias de la nappe des Préalpes Médianes | Dolomitstein  | Kalkstein: Bioklasten   | Gestein: pelitisch |  – |  Ladinien     | Olénékien   | Prä-Rift  |
|15203277 |Formation du Pralet | Dolomitstein  | Kalkstein: spätig: Bioklasten   | Tonstein |  Pralet-Formation |  Ladinien     | Ladinien   | Raibl  |
|15203278 |Membre du Balmi | Dolomitstein  | Kalkstein: arenitisch   | Kalkstein: spätig: Echinodermen |  Balmi-Member |  Ladinien     | Ladinien   | Raibl  |
|15203279 |Membre de la Bodeflue | Dolomitstein  | –   | – |  Bodeflue-Member |  Anisien     | Anisien   | Karbonatische Trias  |
|15203280 |Membre du Wildgrimmi | Kalkstein  | Dolomitstein   | – |  Wildgrimmi-Member |  Anisien     | Anisien   | Karbonatische Trias  |
|15203281 |Cornieule Inférieure | Rauwacke  | –   | – |  «Untere Rauhwacke» (St-Triphon-Fm.) |  Anisien     | Trias précoce   | Karbonatische Trias  |
|15203282 |Mélange infra-brèche | Gestein: pelitisch  | Brekzie   | – |  «Infrabrèche-Melange» |  Paléogène     | Crétacé tardif   | Mélange  |
|15203283 |Flysch du Wägital | Sandstein  | Brekzie: polymikt   | Tonstein |  Wägital-Flysch |  Yprésien     | Campanien   | Flysch  |
|15203284 |Flysch 5 à microconglomérats siliceux | Konglomerat  | Sandstein: kieselig   | – |  «Flysch 5, mit kieseligen Mikrokonglomeraten» |  Lutétien     | Lutétien   | Flysch  |
|15203285 |Flysch des Voirons | Sandstein  | Konglomerat   | Mergelstein |  – |  Rupélien     | Eocène moyen   | Flysch  |
|15203286 |Marne de Boëge | Mergelstein  | Sandstein   | – |  Boëge-Mergel |  Rupélien     | Priabonien   | Flysch  |
|15203287 |Conglomérat du Vouan | Konglomerat  | Sandstein   | Mergelstein |  Vouan-Konglomerat |  Rupélien     | Priabonien   | Flysch  |
|15203288 |Grès des Voirons | Sandstein  | Mergelstein   | – |  Voirons-Sandstein |  Priabonien     | Eocène moyen   | Flysch  |
|15203291 |Couches Rouges de la nappe des Préalpes Médianes, indifférenciées | Kalkstein: mergelig  | Kalkstein: mikritisch   | Mergelstein |  – |  Yprésien     | Turonien   | Couches Rouges  |
|15203292 |Flysch de la Simme, indifférencié | Sandstein  | Gestein: pelitisch   | Konglomerat |  – |  Santonien     | Albien   | Flysch  |
|15203293 |Flysch de Trepsen | Brekzie: polymikt  | Sandstein   | Tonstein |  Trepsen-Flysch |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203294 |Cocco-Gneis | Gneis: granodioritisch  | –   | – |  Cocco-Gneis |  Pennsylvanien     | Pennsylvanien   | Variszisches Grundgebirge  |
|15203295 |Verzasca-Gneis | Gneis: Biotit-Muskovit  | –   | – |  Verzasca-Gneis |  Cisuralien     | Pennsylvanien   | Grundgebirge  |
|15203296 |Vogorno-Gneis | Gneis: Biotit-Muskovit  | –   | – |  Vogorno-Gneis |  Cisuralien     | Pennsylvanien   | Grundgebirge  |
|15203297 |Ruscada-Gneis | Gneis  | –   | – |  Ruscada-Gneis |  Paléozoïque     | Paléozoïque   | Variszisches Grundgebirge  |
|15203298 |Mergoscia-Gneis | Gneis: Biotit  | Gneis: migmatitisch   | – |  Mergoscia-Gneis |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203299 |Monte-Rosa-Orthogneis | Gneis: granodioritisch  | Granodiorit   | – |  Monte-Rosa-Orthogneis  |  Carbonifère     | Carbonifère   | Grundgebirge  |
|15200441 |Grès de Scie Besse | Sandstein: Glaukonit  | –   | – |  Scie-Besse-Sandstein |  Aptien     | Aptien   | «Gault»  |
|15200438 |Argile de la Presta | Tonstein: sandig  | –   | – |  La-Presta-Mergel |  Albien     | Albien   | «Gault»  |
|15200439 |Grès des Vernettes | Sandstein: Glaukonit  | –   | – |  Vernettes-Sandstein |  Albien     | Albien   | «Gault»  |
|15200440 |Banc du Ponthoud | Kalkstein: Bioklasten  | –   | – |  Ponthoud-Bank |  Aptien     | Aptien   | «Gault»  |
|15200442 |Marne du Mortier | Mergelstein  | –   | – |  Mortier-Mergel |  Aptien     | Aptien   | «Gault»  |
|15200443 |Couches de Vauglène | Mergelstein: kalkig  | –   | – |  Vauglène-Bänke |  Aptien     | Aptien   | «Gault»  |
|15200444 |Banc du Poet | Kalkstein: mergelig: Bioklasten  | –   | – |  Poet-Bank |  Aptien     | Aptien   | «Gault»  |
|15200445 |Calcaire d&#39;eau douce de Courcelon | Kalkstein  | –   | – |  Courcelon-Süsswasserkalk |  Rupélien     | Priabonien   | Siderolithikum  |
|15200446 |Calcaire concrétionné de la Erzmatt | Kalkstein: Limonit  | –   | – |  Erzmatt-Krustenkalk |  Rupélien     | Priabonien   | Siderolithikum  |
|15200447 |Calcaire d&#39;eau douce de Diegten | Kalkstein: Bioklasten  | –   | – |  Diegten-Süsswasserkalk |  Rupélien     | Eocène moyen   | Siderolithikum  |
|15200448 |Calcaire d&#39;eau douce de la Verrerie | Kalkstein: kreidig  | Mergelstein   | – |  La-Verrerie-Süsswasserkalk |  Rupélien     | Priabonien   | Siderolithikum  |
|15200449 |Calcaire d&#39;eau douce de la Charrue | Kalkstein  | Mergelstein   | – |  La-Charrue-Süsswasserkalk |  Rupélien     | Priabonien   | Siderolithikum  |
|15200450 |Marne à Astieria | Mergelstein: Bioklasten  | –   | – |  «Astieria-Mergel» |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200451 |Couches de Villers | Mergelstein  | –   | – |  Villers-Schichten |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200452 |Unité Moyenne Calcaire (UMC) | Kalkstein: mikritisch  | –   | – |  «Unité Moyenne Calcaire» |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200453 |Unité Inférieure Oolithique (UIO) | Kalkstein: Bioklasten-Ooide  | Mergelstein   | – |  «Unité Inférieure Oolithique» |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200456 |Calcaire de Landaize | Kalkstein: Bioklasten  | –   | – |  Landaize-Kalk |  Kimméridgien     | Kimméridgien   | Malm  |
|15200457 |Oolite du Balmberg | Kalkstein: Ooide  | –   | – |  Balmberg-Oolith |  Kimméridgien     | Oxfordien   | Malm  |
|15200458 |Calcaire algaire des Hautes Roches | Kalkstein: mikritisch: Onkoide  | Kalkstein: dolomitisch   | – |  Hautes-Roches-Algenkalk |  Oxfordien     | Oxfordien   | Malm  |
|15200459 |Bancs accessoires à momies | Kalkstein: Onkoide  | –   | – |  Akzessorische Mumienbänke |  Oxfordien     | Oxfordien   | Malm  |
|15200460 |Brauner Oolith | Kalkstein: Ooide  | –   | – |  «Brauner Oolith» |  Oxfordien     | Oxfordien   | Malm  |
|15200461 |Bleiglanzbank (Fm. de Kaiseraugst) | Dolomitstein  | –   | – |  «Bleiglanzbank» (Kaiseraugst-Fm.) |  Anisien     | Anisien   | Muschelkalk  |
|15200462 |Banc à Arenicolites | Kalkstein  | –   | – |  «Arenicolites-Bank» |  Anisien     | Anisien   | Buntsandstein  |
|15200463 |Diagonalschichtiger Sandstein (Fm. du Dinkelberg) | Sandstein: tonig: Glimmer  | –   | – |  «Diagonalschichtiger Sandstein» (Dinkelberg-Fm.) |  Olénékien     | Olénékien   | Buntsandstein  |
|15200464 |Membre du Leutschenberg | Kalkstein: dolomitisch  | Kalkstein: Bioklasten   | – |  Leutschenberg-Member |  Anisien     | Anisien   | Muschelkalk  |
|15200465 |Granite de Schlächtenhaus | Granit: Biotit-Muskovit  | –   | – |  Schlächtenhaus-Granit |  Mississippien     | Dévonien tardif   | Frühvariszisches Grundgebirge  |
|15200466 |Complexe gneissique du Steinatal | Gneis: migmatitisch  | Amphibolit   | – |  Steinatal-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15200467 |Grenzdolomit (Fm. de Schinznach) | Dolomitstein  | –   | – |  «Grenzdolomit» (Schinznach-Fm.) |  Ladinien     | Ladinien   | Muschelkalk  |
|15200468 |Couches à Estheria (Fm. de Schinznach) | Mergelstein: Bitumen  | –   | – |  «Estherien-Schichten» |  Ladinien     | Ladinien   | Muschelkalk  |
|15200469 |Hangende-Bankkalke-Formation | Kalkstein: mikritisch  | –   | – |  Hangende-Bankkalke-Formation |  Tithonien     | Tithonien   | Malm  |
|15200470 |Zementmergel-Formation | Mergelstein  | Kalkstein   | – |  Zementmergel-Formation |  Tithonien     | Kimméridgien   | Malm  |
|15200471 |Liegende-Bankkalke-Formation | Kalkstein: Bioklasten  | Mergelstein   | – |  Liegende-Bankkalke-Formation |  Kimméridgien     | Kimméridgien   | Malm  |
|15200472 |Obere-Felsenkalke-Formation | Kalkstein: mikritisch  | –   | – |  Obere-Felsenkalke-Formation |  Kimméridgien     | Kimméridgien   | Malm  |
|15200473 |Untere-Felsenkalke-Formation | Kalkstein  | Mergelstein   | – |  Untere-Felsenkalke-Formation |  Kimméridgien     | Kimméridgien   | Malm  |
|15200474 |Lacunosamergel-Formation | Mergelstein  | Kalkstein: mergelig   | – |  Lacunosamergel-Formation |  Kimméridgien     | Kimméridgien   | Malm  |
|15200475 |Oberjura-Massenkalk-Formation | Kalkstein: Schwämme  | –   | – |  Oberjura-Massenkalk-Formation |  Tithonien     | Kimméridgien   | Malm  |
|15200476 |Lochen-Subformation | Kalkstein: Schwämme  | –   | – |  Lochen-Subformation |  Kimméridgien     | Oxfordien   | Malm  |
|15200477 |Wohlgeschichtete-Kalke-Formation | Kalkstein: mikritisch  | –   | – |  Wohlgeschichtete-Kalke-Formation |  Kimméridgien     | Oxfordien   | Malm  |
|15200478 |Impressamergel-Formation | Mergelstein: tonig  | Kalkstein: mergelig   | – |  Impressamergel-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15200479 |Ornatenton-Formation | Tonstein  | Mergelstein: tonig   | Kalkstein: Eisenooide |  Ornatenton-Formation |  Oxfordien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200480 |Glaukonitsandmergel-Subformation | Mergelstein: sandig-tonig: Glaukonit  | –   | – |  Glaukonitsandmergel-Subformation |  Oxfordien     | Oxfordien   | Lias-Dogger in neritischer Fazies  |
|15200481 |Grenzkalk | Mergelstein: kalkig: Ooide  | –   | – |  Grenzkalk |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15200482 |Macrocephalenoolith-Subformation | Tonstein: Eisenooide  | –   | – |  Macrocephalenoolith-Subformation |  Callovien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200483 |Wutach-Formation | Mergelstein: kalkig: Eisenooide  | –   | – |  Wutach-Formation |  Callovien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200484 |Variansmergel-Formation | Mergelstein  | Kalkstein   | – |  Variansmergel-Formation |  Bathonien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200485 |Dentalienton-Formation | Mergelstein: tonig  | –   | – |  Dentalienton-Formation |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200486 |Hamitenton-Formation | Mergelstein: tonig  | –   | – |  Hamitenton-Formation |  Bathonien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200487 |Parkinsonioolith-Subformation | Kalkstein: Eisenooide  | Mergelstein: tonig   | – |  Parkinsonioolith-Subformation |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200488 |Gosheim-Formation | Kalkstein: Eisenooide  | Mergelstein   | – |  Gosheim-Formation |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200489 |Blagdeni-Subformation | Mergelstein  | Kalkstein   | – |  Blagdeni-Subformation |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200490 |Humphriesioolith-Subformation | Mergelstein: Eisenooide  | –   | – |  Humphriesioolith-Subformation |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200491 |Wedelsandstein-Formation | Mergelstein  | Kalkstein   | – |  Wedelsandstein-Formation |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200492 |Blaukalk-Subformation | Kalkstein  | Mergelstein   | – |  Blaukalk-Subformation |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200493 |Murchisonaeoolith-Formation | Kalkstein: sandig  | Sandstein: kalkig   | Sandstein: Eisenooide |  Murchisonaeoolith-Formation |  Aalénien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15200494 |Achdorf-Formation | Tonstein: sandig: Glimmer  | Kalkstein: Ooide   | Kalkstein: Bioklasten |  Achdorf-Formation |  Aalénien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15200495 |Couches du Tannenwald | Konglomerat  | Sandstein   | – |  Tannenwald-Schichten |  Serravallien     | Serravallien   | Molasse  |
|15200496 |Couches de la Gabelspitz | Konglomerat: polymikt: Quarz  | Sandstein   | Mergelstein |  Gabelspitz-Schichten |  Burdigalien     | Burdigalien   | Molasse  |
|15200497 |Marne du Schallenberg | Mergelstein  | Sandstein   | Konglomerat: polymikt |  Schallenberg-Member |  Burdigalien     | Burdigalien   | Molasse  |
|15200498 |Poudingue de Seli | Konglomerat: polymikt: Quarz  | –   | – |  Seli-Nagelfluh |  Burdigalien     | Burdigalien   | Molasse  |
|15200499 |Tuffite du Brand-Herrentisch | Tuffit  | –   | – |  Brand-Herrentisch-Tuffit |  Tortonien     | Langhien   | Hegau-Vulkanismus  |
|15200500 |Tuffite de Wangen | Tuffit  | –   | – |  Wangen-Tuffit |  Serravallien     | Langhien   | Hegau-Vulkanismus  |
|15200501 |Tuffite du Hohenolber | Tuffit  | –   | – |  Hohenolber-Tuffit |  Serravallien     | Serravallien   | Hegau-Vulkanismus  |
|15200502 |Tuffite d&#39;Eichbol | Tuffit  | –   | – |  Eichbol-Tuffit |  Langhien     | Langhien   | Hegau-Vulkanismus  |
|15203303 |Spegnas-Fm. | Sandstein  | Schiefer   | Kalkstein: sandig |  Spegnas-Formation |  Paléocène     | Paléocène   | Sedimentbedeckung  |
|15203300 |Arblatsch-Flysch | Sandstein  | Schiefer: tonig-kalkig   | Konglomerat |  Arblatsch-Flysch |  Yprésien     | Maastrichtien   | Flysch  |
|15203301 |Arblatsch-Flysch: Sandstein-dominierte Fazies | Sandstein  | –   | – |  Arblatsch-Flysch |  Yprésien     | Yprésien   | Flysch  |
|15203302 |Arblatsch-Flysch: Konglomerat-dominierte Fazies | Konglomerat  | –   | – |  Arblatsch-Flysch |  Yprésien     | Yprésien   | Flysch  |
|15203304 |Rudnal-Fm. | Kalkstein: mergelig  | Tonstein: schiefrig   | Sandstein |  Rudnal-Formation |  Maastrichtien     | Maastrichtien   | Sedimentbedeckung  |
|15203305 |Savognin-Fm. | Rauwacke  | Evaporit: Gips   | Brekzie |  Savognin-Formation |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15203306 |Stätzerhorn-Fm.: Bleis-Pintgas-Mb. | Kalkstein: sandig  | Schiefer: tonig   | – |  Bleis-Pintgas-Member |  Maastrichtien     | Santonien   | Flysch  |
|15203307 |Stätzerhorn-Fm.: Parnegl-Mb. | Kalkstein: sandig  | Schiefer: tonig   | – |  Parnegl-Member |  Maastrichtien     | Santonien   | Flysch  |
|15203308 |Stätzerhorn-Fm.: Danis-Mb. | Kalkstein: sandig  | –   | – |  Danis-Member |  Maastrichtien     | Santonien   | Flysch  |
|15203309 |Stätzerhorn-Fm.: Raschil-Mb. | Kalkstein: sandig  | Schiefer: tonig   | – |  Raschil-Member |  Maastrichtien     | Santonien   | Flysch  |
|15203310 |Bruneggjoch-Fm.: Embd-Mb. | Quarzit  | Konglomerat: Quarz   | – |  Embd-Member |  Lopingien     | Lopingien   | Detritische Trias  |
|15203311 |Randa-Augengneis: Bonigersee-Augengneis | Granit: porphyrisch  | Gneis: augig   | – |  Bonigersee-Augengneis |  Ordovicien     | Ordovicien   | Variszisches Grundgebirge  |
|15203312 |Törbel-Gneis | Gneis  | –   | – |  Törbel-Gneis |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203313 |Lodano-Gneis | Gneis: gebändert  | –   | – |  Lodano-Gneis |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203314 |Vergeletto-Gneis | Gneis  | –   | – |  Vergeletto-Gneis |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203315 |Cortascia-Gneis | Gneis: Biotit-Muskovit  | –   | – |  Cortascia-Gneis |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203316 |Forcoletta-Gneis | Gneis: Biotit-Muskovit  | –   | – |  Forcoletta-Gneis |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203317 |Matorello-Gneis | Gneis  | Granodiorit   | – |  Matorello-Gneis |  Assélien     | Pennsylvanien tardif   | Variszisches Grundgebirge  |
|15203318 |Complexe gneissique du Lebendun | Gneis: psephitisch  | Marmor   | Schiefer: Glimmer |  Lebendun-Komplex |  Mésozoïque     | Paléozoïque   | Grundgebirge  |
|15203319 |Sabbione-Sandstein | Sandstein  | Gestein: vulkanisch   | – |  Sabbione-Sandstein |  Bathonien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15203320 |Socle cristallin de la nappe du Monte Leone | Gneis: augig  | Gneis   | – |  – |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203321 |Ganter-Gneis | Gneis: augig  | –   | – |  Ganter-Gneis |  Paléozoïque     | Paléozoïque   | Variszisches Grundgebirge  |
|15203322 |Ritter-Gneis | Gneis  | –   | – |  Ritter-Gneis |  Paléozoïque     | Paléozoïque   | Variszisches Grundgebirge  |
|15203323 |Geisspfad-Serpentinit | Serpentinit  | Peridotit   | Granofels: Pyroxen |  Geisspfad-Serpentinit |  Mésozoïque     | Paléozoïque   | Grundgebirge  |
|15203325 |Calcschistes de l&#39;Holzerspitz | Schiefer: kalkig  | –   | – |  Holzerspitz-Kalkschiefer |  Mésozoïque     | Mésozoïque   | Post-Rift  |
|15203327 |Rinderbach-Fm. | Tonstein  | Sandstein: Quarz   | – |  Rinderbach-Formation |  Danien     | Danien   | Flysch  |
|15203328 |Langenegg-Fm. | Sandstein: kalkig  | Mergelstein   | – |  Langenegg-Formation |  Turonien     | Cénomanien   | Flysch  |
|15203329 |Rombach-Fm. | Brekzie: polymikt  | Mergelstein   | – |  Rombach-Formation |  Santonien     | Coniacien   | Flysch  |
|15203330 |Roffna-Gneis | Gneis: granitisch  | Gneis: granitisch   | – |  Roffna-Gneis |  Mississippien     | Mississippien   | Variszisches Grundgebirge  |
|15203331 |Roffna-Gneis: Porphyrische Fazies | Granit: porphyrisch  | –   | – |  Roffna-Gneis |  Mississippien     | Mississippien   | Variszisches Grundgebirge  |
|15203332 |Burgruinen-Gneis | Gneis  | Pegmatit   | – |  Burgruinen-Gneis |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203333 |Taspegn-Gneis | Gneis: psephitisch  | –   | – |  Taspegn-Gneis |  Permien     | Carbonifère   | Sedimentbedeckung  |
|15203334 |Aigremont-Brekzie | Brekzie: polymikt  | Siltstein: schiefrig   | – |  Aigremont-Brekzie |  Crétacé tardif     | Crétacé tardif   | Flysch  |
|15203335 |Sulzgrabe-Fm. | Mergelstein: kalkig  | Sandstein   | Kalkstein |  Sulzgrabe-Formation |  Crétacé précoce     | Jurassique tardif   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203336 |Brekzien-Decke: Rhät | Schiefer: kalkig  | –   | – |  – |  Rhétien     | Rhétien   | «Rhät»  |
|15203337 |Klippen-Decke: Siderolithischer Dogger | Tonstein  | Gestein: residual: Eisenmineralien   | Brekzie: dolomitisch |  – |  Jurassique moyen     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15203338 |St-Triphon-Fm.: Andonces-Mb.: Silex-Niveau | Kalkstein: Chert  | –   | – |  «Silex-Niveau» (St-Triphon-Fm.) |  Anisien     | Anisien   | Karbonatische Trias  |
|15203339 |St-Triphon-Fm.: Andonces-Mb.: Mittlere Rauwacke | Rauwacke  | Dolomitstein   | Mergelstein |  «Mittlere Rauhwacke» (St-Triphon-Fm.) |  Ladinien     | Anisien   | Karbonatische Trias  |
|15203340 |Timun-Gneiskomplex | Schiefer: Serizit-Chlorit  | Gneis   | Amphibolit |  Timun-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15203341 |Malenco-Serpentinit | Serpentinit  | Schiefer: Antigorit   | – |  Malenco-Serpentinit |  Bathonien     | Bajocien   | Ophiolithische Abfolge  |
|15203342 |Forno-Amphibolit | Amphibolit: gebändert  | Basalt   | Brekzie: pyroklastisch |  Forno-Amphibolit |  Tithonien     | Callovien   | Ophiolithische Abfolge  |
|15203343 |Muretto-Quarzit | Quarzit  | Schiefer: Quarz   | – |  Muretto-Quarzit |  Crétacé tardif     | Crétacé tardif   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203344 |Biot-Fm.: Colerin-Konglomerat | Konglomerat  | –   | – |  Colerin-Konglomerat |  Maastrichtien     | Campanien   | Flysch  |
|15203345 |Pierre-Avoi-Melange: Brekzie | Brekzie: polymikt  | –   | – |  Pierre-Avoi-Brekzie |  Mésozoïque     | Mésozoïque   | Mélange  |
|15203346 |Dréveneuse-Bauxit | Gestein: residual  | –   | – |  Dréveneuse-Bauxit |  Jurassique moyen     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15203347 |Barrhorn-Einheit: Metabauxit | Schiefer: Chloritoid-Kyanit  | –   | – |  Brunnegjoch-Metabauxit |  Jurassique moyen     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15203349 |Schistes du (Piz) Terri | Schiefer: kalkig  | Schiefer: tonig   | Marmor |  Terri-Schiefer |  Jurassique moyen     | Jurassique précoce   | Sedimentbedeckung  |
|15203350 |Wildflysch de Robièi | Siltstein  | Sandstein: kalkig: Glimmer   | Schiefer: Glimmer-Granat |  Robiei-Wildflysch |  Priabonien     | Eocène moyen   | Mélange  |
|15203351 |Wildflysch du Pizzo Castello | Gneis  | Sandstein: kalkig   | Marmor |  Pizzo-Castello-Wildflysch |  Priabonien     | Eocène moyen   | Mélange  |
|15203352 |Wildflysch de Tamier-Zött | Gneis  | Gestein: basisch   | – |  Tamier-Zött-Wildflysch |  Priabonien     | Eocène moyen   | Mélange  |
|15203353 |Wildflysch de l&#39;Alpe Tamia-Campo | Marmor: kalkig  | –   | – |  Alpe-Tamia-Campo-Wildflysch |  Priabonien     | Eocène moyen   | Mélange  |
|15203354 |Calcschistes du Teggiolo | Schiefer: kalkig  | –   | – |  Teggiolo-Kalkschiefer |  Eocène moyen     | Crétacé tardif   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203355 |Quartzite du Mèdola | Quarzit  | Sandstein: kalkig   | Schiefer: Glimmer |  Medola-Quarzit |  Eocène moyen     | Crétacé tardif   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203356 |Calcschiste de Pianasciom | Schiefer: kalkig  | Sandstein   | Kalkstein |  Pianasciom-Kalkschiefer |  Eocène moyen     | Crétacé tardif   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203357 |Grès du Piano delle Creste | Sandstein: Quarz  | Sandstein: kalkig   | – |  Piano-delle-Creste-Sandstein |  Eocène moyen     | Crétacé tardif   | Post-Rift Mesozoikum in detritischer Fazies  |
|15203358 |Groupe d&#39;Antabia | Marmor  | Sandstein   | Konglomerat |  – |  Berriasien     | Jurassique précoce   | Sedimentbedeckung  |
|15203359 |Formation des Vanis | Marmor  | Schiefer: kalkig   | – |  Vanis-Formation |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203360 |Marbre de Sevinèra | Marmor: kalkig  | –   | – |  Sevinera-Marmor |  Tithonien     | Oxfordien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15203361 |Grès de Sevinèra | Sandstein: kalkig  | –   | – |  Sevinera-Sandstein |  Callovien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15203362 |Conglomérat du Ri d&#39;Antabia | Konglomerat  | –   | – |  Ri-d&#39;Antabia-Konglomerat |  Jurassique moyen     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15203363 |Scisti bruni (Lebendun) | Schiefer: Glimmer  | –   | – |  «Scisti bruni» (Lebendun) |  Mésozoïque     | Paléozoïque   | Grundgebirge  |
|15203364 |Gneiss basale (Lebendun) | Gneis: augig  | –   | – |  Lebendun-Komplex |  Mésozoïque     | Paléozoïque   | Grundgebirge  |
|15200506 |Tuffite du Seerücken | Tuffit  | –   | – |  Seerücken-Tuffit |  Serravallien     | Serravallien   | OSM  |
|15200503 |Formation d&#39;Öhningen | Mergelstein  | Gestein: vulkanisch   | – |  Öhningen-Formation |  Langhien     | Langhien   | OSM  |
|15200504 |Calcaire d&#39;eau douce d&#39;Öhningen | Kalkstein  | Tonstein   | Gestein: vulkanisch |  Öhningen-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200505 |Poudingue de la Ramschwag | Konglomerat: kalkig-dolomitisch  | –   | – |  Ramschwag-Nagelfluh |  Langhien     | Langhien   | OSM  |
|15200507 |Couches de Meilen | Mergelstein  | –   | – |  Meilen-Formation |  Langhien     | Langhien   | OSM  |
|15200508 |Rotzone Wulp | Bentonit  | –   | – |  «Wulp-Rotzone» |  Langhien     | Langhien   | OSM  |
|15200509 |Formation de Käpfnach | Mergelstein  | Gestein: organisch: Kohle   | – |  Kapfnach-Formation |  Langhien     | Burdigalien tardif   | OSM  |
|15200510 |Juranagelfluh-Mergel | Mergelstein  | –   | – |  – |  Tortonien     | Langhien   | OSM  |
|15200511 |Calcaire d&#39;eau douce du Golat | Kalkstein: kreidig: Bitumen  | Mergelstein   | Sandstein |  Golat-Süsswasserkalk |  Miocène moyen     | Miocène moyen   | OSM  |
|15200512 |Petrefaktenlager (Fm. du Belpberg) | Mergelstein: Bioklasten  | Sandstein: mergelig   | – |  Belpberg-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200513 |Formation du Hombach | Sandstein: Feldspat  | Mergelstein   | Konglomerat |  Hombach-Member |  Chattien tardif     | Chattien tardif   | USM  |
|15200514 |Membre de Homberg | Sandstein: Feldspat  | Siltstein   | Mergelstein |  Homberg-Formation |  Chattien précoce     | Chattien précoce   | USM  |
|15200515 |Poudingue du Gäbris | Konglomerat  | Sandstein   | – |  Gäbris-Nagelfluh |  Aquitanien     | Aquitanien   | USM  |
|15200516 |Membre du Gstaldenbach | Mergelstein  | Konglomerat   | – |  Gstaldenbach-Member |  Aquitanien     | Aquitanien   | USM  |
|15200517 |Membre de Heiden | Sandstein: kalkig  | –   | – |  Heiden-Member |  Aquitanien     | Aquitanien   | USM  |
|15200518 |Membre du Klusbach | Konglomerat  | –   | – |  Klusbach-Member |  Aquitanien     | Aquitanien   | USM  |
|15200519 |Membre de l&#39;Eggen | Sandstein  | –   | – |  Eggen-Member |  Aquitanien     | Aquitanien   | USM  |
|15200520 |Membre de Sulzbach | Sandstein: Feldspat  | Sandstein: kalkig   | Konglomerat: kalkig |  Sulzbach-Member |  Aquitanien     | Aquitanien   | USM  |
|15200521 |Poudingue de Sulzbach | Konglomerat: kalkig  | –   | – |  Sulzbach-Member |  Aquitanien     | Aquitanien   | USM  |
|15200522 |Membre du Pfingstboden | Konglomerat: polymikt  | –   | – |  Pfingstboden-Member |  Aquitanien     | Aquitanien   | USM  |
|15200523 |Membre de la Hochfläschli | Konglomerat  | Mergelstein   | – |  Hochfläschli-Member |  Aquitanien     | Aquitanien   | USM  |
|15200524 |Membre d&#39;Ennetbühl | Konglomerat  | Mergelstein   | – |  Ennetbühl-Member |  Aquitanien     | Aquitanien   | USM  |
|15200525 |Membre de la Hochalp | Konglomerat: kalkig-dolomitisch  | Mergelstein   | – |  Hochalp-Member |  Aquitanien     | Aquitanien   | USM  |
|15200526 |Membre de Krummenau | Mergelstein  | Konglomerat: kalkig   | Sandstein: kalkig |  Krummenau-Member |  Aquitanien     | Aquitanien   | USM  |
|15200527 |Ältere Juranagelfluh | Konglomerat: kalkig  | Mergelstein   | – |  «Ältere Juranagelfluh» |  Aquitanien     | Aquitanien   | USM  |
|15200528 |Poudingue de la Gitzischöpf | Konglomerat  | Sandstein   | Tonstein |  Gitzschöpf-Nagelfluh |  Chattien tardif     | Chattien tardif   | USM  |
|15200529 |Marne de la Honegg | Mergelstein: sandig  | Konglomerat   | – |  Honegg-Mergel |  Aquitanien     | Chattien tardif   | USM  |
|15200530 |Poudingue du Kaltbach | Konglomerat  | –   | – |  Kaltbach-Nagelfluh |  Aquitanien     | Chattien tardif   | USM  |
|15200531 |Poudingue de Hünibach | Konglomerat  | Sandstein   | Mergelstein |  Hünibach-Nagelfluh |  Chattien     | Chattien   | USM  |
|15200532 |Formation de la Losenegg | Konglomerat: polymikt  | Sandstein   | Siltstein |  Losenegg-Formation |  Chattien     | Chattien   | USM  |
|15200533 |Poudingue de Schwändibach | Konglomerat  | Sandstein   | Mergelstein |  Schwändibach-Nagelfluh |  Chattien précoce     | Chattien précoce   | USM  |
|15200534 |Formation d&#39;Uerscheli | Sandstein  | Siltstein   | Konglomerat: polymikt |  Uerscheli-Formation |  Chattien précoce     | Chattien précoce   | USM  |
|15200535 |Poudingue de Bumbach | Konglomerat  | Siltstein   | – |  Bumbach-Nagelfluh |  Chattien précoce     | Chattien précoce   | USM  |
|15200536 |Kalksandstein-Serie | Sandstein: kalkig: Glimmer  | Mergelstein: sandig   | – |  «Untere Bunte Molasse» (USM-I) |  Chattien     | Chattien   | USM  |
|15200537 |Couches du Gérignoz | Mergelstein  | Sandstein: Glimmer   | Tonstein: Kohle |  Gérignoz-Formation |  Aquitanien     | Chattien tardif   | USM  |
|15200538 |Poudingue du Leuenfall | Konglomerat: kalkig  | –   | – |  Leuenfall-Nagelfluh |  Chattien     | Rupélien   | USM  |
|15200539 |Membre du Wintersberg | Mergelstein  | Sandstein: kalkig   | Konglomerat |  Wintersberg-Member |  Chattien     | Chattien   | USM  |
|15200540 |Grès d&#39;Ebnat | Mergelstein  | Sandstein: mergelig   | Sandstein: kalkig |  Ebnat-Member |  Chattien     | Rupélien   | USM  |
|15200541 |Grès calcaire de Rütiberg | Sandstein: kalkig  | –   | – |  Rütiberg-Kalksandstein |  Chattien     | Rupélien   | USM  |
|15200542 |Poudingue de la Pfiffegg | Konglomerat: kalkig-dolomitisch  | Sandstein   | – |  Pfiffegg-Nagelfluh |  Chattien     | Chattien   | USM  |
|15200543 |Formation de Weggis | Konglomerat: kalkig-dolomitisch  | Sandstein   | Mergelstein |  Weggis-Formation |  Chattien précoce     | Rupélien   | USM  |
|15200544 |Poudingue de la Kännelegg | Konglomerat: kalkig  | –   | – |  Kännelegg-Nagelfluh |  Chattien précoce     | Rupélien   | USM  |
|15200545 |Molasse Rouge du Pied-du-Jura | Mergelstein: sandig  | Sandstein: Glimmer   | Konglomerat: kalkig |  «Molasse Rouge des Jurasüdfusses» |  Chattien tardif     | Rupélien   | USM  |
|15200546 |Grès de Mathod | Sandstein  | –   | – |  Mathod-Sandstein |  Chattien tardif     | Chattien tardif   | USM  |
|15200547 |Grès de Goumoëns | Sandstein  | Konglomerat: kalkig   | – |  Goumoëns-Sandstein |  Chattien précoce     | Chattien précoce   | USM  |
|15200548 |Molasse Rouge de Vevey | Mergelstein: siltig: Glimmer  | Sandstein: mergelig   | – |  «Molasse Rouge de Vevey» |  Chattien     | Chattien   | USM  |
|15200549 |Molasse Rouge de Monthey | Schiefer  | Sandstein   | – |  «Molasse Rouge de Monthey» |  Chattien     | Chattien   | USM  |
|15200550 |Formation de la Grindelegg | Mergelstein  | Sandstein: kalkig: Glimmer   | Konglomerat: kalkig |  Grindelegg-Formation |  Chattien     | Chattien   | USM  |
|15200551 |Couches de Tillerée | Mergelstein: tonig: Kohle  | Mergelstein: siltig   | – |  Tillerée-Schichten |  Aquitanien     | Chattien tardif   | USM  |
|15200552 |Série des calcaires d&#39;eau douce et dolomie (GMGG) | Kalkstein  | Dolomitstein   | – |  «Grès et Marnes Gris à Gypse» |  Chattien tardif     | Chattien tardif   | USM  |
|15200553 |Calcarénite d&#39;Oltingue | Kalkstein: arenitisch  | –   | – |  Oltingue-Kalkarenit |  Rupélien     | Rupélien   | UMM  |
|15200554 |Formation de Vaulruz (UMM-II+III indiff.) | Sandstein: kalkig: Glimmer  | Mergelstein   | – |  Vaulruz-Formation |  Rupélien     | Rupélien   | UMM  |
|15200555 |Poudingue d&#39;Unter Lochsitli | Konglomerat  | –   | – |  Unter-Lochsiti-Nagelfluh |  Rupélien     | Rupélien   | UMM  |
|15200556 |Poudingue de Flühli | Konglomerat  | –   | – |  Flühli-Nagelfluh |  Rupélien     | Rupélien   | UMM  |
|15200557 |Zone der Schiefermergel (Fm. de Saint-Gall) | Mergelstein: Bioklasten  | –   | – |  St.-Gallen-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200558 |Membre de Marbach | Sandstein: Glimmer  | Mergelstein   | – |  Marbach-Member |  Aquitanien     | Aquitanien   | USM  |
|15200560 |Molasse bariolée inférieure | Mergelstein: siltig  | Sandstein   | – |  «Untere Bunte Molasse» (USM-I) |  Chattien tardif     | Chattien tardif   | USM  |
|15200562 |Mittlere Juranagelfluh | Konglomerat  | –   | – |  Mittlere Juranagelfluh |  Langhien     | Burdigalien   | OSM  |
|15200563 |Albstein | Kalkstein  | –   | – |  Albstein |  Burdigalien     | Burdigalien   | OSM  |
|15200564 |Graupensand | Sandstein  | –   | – |  Grimmelfingen-Formation |  Burdigalien     | Burdigalien   | Molasse  |
|15200565 |Marne à Hélicidés | Mergelstein: Bioklasten  | Tonstein   | – |  «Heliciden-Mergel» (OSM-J) |  Tortonien     | Langhien   | OSM  |
|15200566 |Marne de Haldenhof | Mergelstein  | Sandstein   | – |  Haldenhof-Mergel |  Langhien     | Burdigalien tardif   | OSM  |
|15203368 |Série schisto-quartzitique (Pierre Avoi) | Schiefer: tonig  | Quarzit   | Schiefer: kalkig |  Pierre-Avoi-Melange |  Rupélien     | Eocène moyen   | Mélange  |
|15203365 |Orthogneiss d&#39;Antigorio | Gneis: magmatisch  | –   | – |  Antigorio-Orthogneis |  Cisuralien     | Cisuralien   | Grundgebirge  |
|15203366 |Couches-Rouges (Falknis, Sulzfluh, Tasna) | Kalkstein: mergelig  | Mergelstein   | Brekzie |  – |  Maastrichtien     | Albien   | Couches Rouges  |
|15203367 |Lagensandkalk | Schiefer: tonig-kalkig  | Quarzit: Chlorit   | – |  – |  Jurassique précoce     | Jurassique précoce   | Sedimentbedeckung  |
|15203369 |Série conglomératique (Pierre Avoi) | Konglomerat  | –   | – |  Pierre-Avoi-Melange |  Rupélien     | Eocène moyen   | Mélange  |
|15203370 |Compexe de Südegg | Schiefer  | Gestein: metamorph   | – |  Südegg-Komplex |  Mésozoïque     | Paléozoïque   | Mélange  |
|15203371 |Complexe de la Punta Rossa | Gneis  | Serpentinit   | Konglomerat |  Punta-Rossa-Komplex |  Mésozoïque     | Paléozoïque   | Mélange  |
|15203372 |Schistes de Ferret | Schiefer: tonig  | Schiefer: kieselig   | Kalkstein |  Ferret-Schiefer |  Crétacé tardif     | Crétacé précoce   | Sedimentbedeckung  |
|15203373 |Schistes basaux du (Piz) Terri | Schiefer: sandig-tonig  | –   | – |  – |  Jurassique précoce     | Jurassique précoce   | Sedimentbedeckung  |
|15203374 |Schistes du Val Lumnezia | Schiefer  | –   | – |  – |  Crétacé     | Crétacé   | Sedimentbedeckung  |
|15203376 |Konglomeratgneis (Terri) | Gneis: psephitisch  | –   | – |  – |  Trias précoce     | Permien   | Sedimentbedeckung  |
|15203377 |Brèche de Garzott | Brekzie  | Kalkstein: sandig   | Quarzit |  Garzott-Brekzie |  Jurassique moyen     | Jurassique précoce   | Sedimentbedeckung  |
|15203378 |Mélange d&#39;Areua-Bruschghorn | Gneis  | Brekzie   | – |  Areua-Bruschghorn-Melange |  Cénozoïque     | Paléozoïque   | Mélange  |
|15203379 |Albitquarzit (Grava) | Quarzit: Albit  | –   | – |  – |  Jurassique moyen     | Jurassique moyen   | Sedimentbedeckung  |
|15203380 |Basale Tonschiefer (Grava) | Schiefer: tonig  | –   | – |  – |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15203381 |Phengitgneis (Grava) | Gneis: augig: Phengit  | –   | – |  – |  Paléozoïque     | Paléozoïque   | Sedimentbedeckung  |
|15203382 |Formation de la Haute Pointe | Kalkstein: kieselig: Bioklasten-Chert  | Kalkstein: mergelig-schiefrig   | – |  Haute-Pointe-Formation |  Oxfordien     | Callovien   | Syn-Rift  |
|15203383 |Formation des Brasses | Kalkstein: kieselig  | Kalkstein: spätig: Bioklasten   | Kalkstein: mergelig-schiefrig |  Brasses-Formation |  Bajocien     | Pliensbachien   | Syn-Rift  |
|15203385 |Gneiss oeillé de Macugnaga | Gneis: augig  | –   | – |  Macugnaga-Augengneis |  Pennsylvanien     | Pennsylvanien   | Grundgebirge  |
|15203386 |Permien de la Zone Houillère | Schiefer: Quarz  | Konglomerat   | Sandstein |  – |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15203387 |Permien quarzoschisteux de la Zone Houillère | Schiefer: Quarz  | Gneis   | – |  – |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15203388 |Rhyolite de Ricard | Rhyolith  | –   | – |  Ricard-Rhyolit |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15203389 |Permien conglomératique de la Zone Houillère | Konglomerat  | –   | – |  – |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15203390 |Série schisto-gréseuse supérieure | Schiefer: sandig  | –   | – |  Printse-Formation |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15203391 |Série schisteuse moyenne | Schiefer: tonig  | –   | – |  Printse-Formation |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15203392 |Grès de Chandoline | Sandstein  | Sandstein: konglomeratisch   | – |  Chandoline-Sandstein |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15203393 |Gneiss de Gälmji | Gneis  | Schiefer: Glimmer-Granat   | Amphibolit |  Gälmji-Gneis |  Permien     | Carbonifère   | Grundgebirge  |
|15203394 |Gabbro du Scherbadung | Gabbro  | –   | – |  Scherbadung-Gabbro |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203395 |Gneiss oeillé des Lacerandes | Gneis: augig  | –   | – |  Lacerandes-Augengneis |  Spätes Ordovizium     | Mittleres Ordovizium   | Grundgebirge  |
|15203396 |Métapélites du Mont Mort | Schiefer: Glimmer-Granat  | Amphibolit   | – |  Mont-Mort-Metapelit |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203397 |Schistes noirs (Pierre Avoi) | Schiefer: tonig  | –   | – |  Pierre-Avoi-Melange |  Mésozoïque     | Paléozoïque   | Mélange  |
|15203398 |Calcaire albitisé de la Dotse | Kalkstein: Albit  | –   | – |  La-Dotse-Albitkalk |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15203399 |Gneiss de Ginals | Gneis: augig  | –   | – |  Ginals-Gneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203400 |Socle cristallin de la nappe de Berisal | Gneis: Granat  | Schiefer: Glimmer-Granat   | Amphibolit |  Berisal-Gneiskomplex |  Permien     | Ordovicien   | Grundgebirge  |
|15203401 |Gneiss oeillé de la nappe de Berisal | Gneis: augig  | –   | – |  Berisal-Gneiskomplex |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203402 |Socle cristallin de la nappe du Ruitor | Gneis: augig  | Schiefer: Glimmer-Granat   | Amphibolit |  Ruitor-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203403 |Gneiss du Corno | Gneis: psammitisch  | Gneis: psephitisch: Phengit   | – |  Corno-Gneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203404 |Quartzite du Trias nord-pennique | Quarzit  | –   | – |  – |  Trias     | Trias   | Detritische Trias  |
|15203405 |Socle cristallin du Briançonnais | Gneis  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203406 |Permo-Carbonifère de la nappe du Ruitor | Quarzit  | Schiefer: Quarz-Glimmer   | – |  Mont-Brûlé-Quarzit |  Permien     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15203407 |Permo-Carbonifère conglomératique de la nappe du Ruitor | Konglomerat  | –   | – |  Plan-Palasuit-Konglomerat |  Permien     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15203408 |Schistes lustrés du Piémontais | 15111591  | Schiefer: tonig   | – |  – |  Mésozoïque     | Mésozoïque   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203409 |Métasédiments de la nappe du Tsaté | Gestein: sedimentär  | –   | – |  – |  Mésozoïque     | Mésozoïque   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203410 |Marbre de la nappe du Tsaté | Marmor  | Brekzie   | – |  – |  Jurassique tardif     | Jurassique tardif   | Maiolica / Aptychenkalk  |
|15203411 |Métaradiolarite de la nappe du Tsaté | Gestein: kieselig: Radiolarien  | Schiefer: kieselig   | – |  Chanrion-Radiolarit |  Jurassique tardif     | Jurassique moyen   | Radiolarit  |
|15203412 |Métasédiments de la nappe de Zermatt-Saas | Gestein: sedimentär  | –   | – |  – |  Mésozoïque     | Mésozoïque   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203413 |Ophiolite du Piémontais | Serpentinit  | Gabbro   | Basalt |  – |  Jurassique tardif     | Jurassique moyen   | Ophiolithische Abfolge  |
|15203414 |Ophiolite de la nappe du Tsaté | Serpentinit  | Gabbro   | Basalt |  – |  Jurassique tardif     | Jurassique moyen   | Ophiolithische Abfolge  |
|15203415 |Métabasalte du Mont des Ritzes | Basalt  | Prasinit   | – |  Mont-des-Ritzes-Metabasalt |  Jurassique tardif     | Jurassique moyen   | Ophiolithische Abfolge  |
|15203416 |Métagabbro des Aiguilles Rouges d&#39;Arolla | Gabbro  | –   | – |  Aiguilles-Rouges-d&#39;Arolla-Metagabbro |  Jurassique tardif     | Jurassique moyen   | Ophiolithische Abfolge  |
|15203417 |Brèche de Torrembey | Brekzie: kalkig  | –   | – |  Torrembey-Brekzie |  Trias     | Trias   | Prä-Rift  |
|15203418 |Marbre de la nappe de Zermatt-Saas | Marmor  | –   | – |  – |  Jurassique tardif     | Jurassique tardif   | Maiolica / Aptychenkalk  |
|15203419 |Quartzite de la nappe de Zermatt-Saas | Quarzit  | Gestein: kieselig: Radiolarien   | – |  – |  Jurassique tardif     | Jurassique moyen   | Radiolarit  |
|15203420 |Mélange du Riffelberg | Eklogit  | Schiefer   | – |  Riffelberg-Melange |  Mésozoïque     | Mésozoïque   | Mélange  |
|15203421 |Schistes lustrés de la nappe de Zermatt-Saas | 15111591  | Schiefer: tonig   | – |  – |  Mésozoïque     | Mésozoïque   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203422 |Ophiolite de la nappe de Zermatt-Saas | Serpentinit  | Gabbro   | Basalt |  – |  Jurassique tardif     | Jurassique moyen   | Ophiolithische Abfolge  |
|15203423 |Métabasalte du Pfulwe | Basalt  | Prasinit   | – |  Pfulwe-Metabasalt |  Jurassique tardif     | Jurassique moyen   | Ophiolithische Abfolge  |
|15203424 |Ophiolite de la nappe d&#39;Antrona | Serpentinit  | Gabbro   | Basalt |  – |  Jurassique tardif     | Jurassique moyen   | Ophiolithische Abfolge  |
|15203425 |Gneiss du Böshorn | Gneis  | Granit   | – |  Böshorn-Gneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203426 |Orthogneiss de la nappe du Monte Leone | Gneis: magmatisch  | –   | – |  – |  Permien     | Carbonifère   | Grundgebirge  |
|15203427 |Leucogneiss de la nappe du Monte Leone | Gneis  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203428 |Hyperaugengneiss de la nappe du Monte Leone | Gneis: augig  | –   | – |  – |  Ordovicien     | Ordovicien   | Grundgebirge  |
|15203429 |Paragneiss de la nappe du Monte Leone | Gneis: sedimentär  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15200567 |OMM-J | Sandstein  | Mergelstein   | Konglomerat |  – |  Burdigalien     | Burdigalien   | OMM  |
|15200568 |Poudingue coquillier de Tenniken | Sandstein: kalkig: Muscheln  | Konglomerat: kalkig: Muscheln   | – |  Tenniken-Muschelagglomerat |  Burdigalien     | Burdigalien   | OMM  |
|15200569 |Calcaire à Turritelles | Kalkstein: sandig: Bioklasten  | –   | – |  – |  Burdigalien     | Burdigalien   | OMM  |
|15200570 |Calcaire grossier du Randen | Kalkstein: sandig: Bioklasten  | –   | – |  Randen-Grobkalk |  Burdigalien     | Burdigalien   | OMM  |
|15200571 |Sable à galets de Péry | Sandstein: konglomeratisch  | –   | – |  Péry-Sandstein |  Burdigalien     | Burdigalien   | OMM  |
|15200572 |Gompholite des Bayards | Brekzie: kalkig  | –   | – |  Les-Bayards-Juranagelfluh |  Pliocène     | Miocène   | OSM  |
|15200573 |Formation de Günsberg et de Vellerat, indifférenciées | Kalkstein  | Mergelstein   | – |  – |  Oxfordien     | Oxfordien   | Malm  |
|15200574 |Ornatenton-Fm.: Ancepsoolith-Sbf. | Tonstein: Eisenooide  | –   | – |  Ancepsoolith-Subformation |  Callovien     | Callovien   | Malm  |
|15200575 |Jurensismergel-Fm. | Mergelstein  | Kalkstein: mergelig   | – |  Jurensismergel-Formation |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15200576 |Posidonienschiefer-Fm. | Mergelstein: Bitumen  | Kalkstein   | – |  Posidonienschiefer-Formation |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15200577 |Amaltheenton-Fm. | Tonstein: Pyrit  | Mergelstein: kalkig   | – |  Amaltheenton-Formation |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15200578 |Numismalismergel-Fm. | Mergelstein  | Kalkstein: mergelig   | – |  Numismalismergel-Formation |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15200579 |Obtususton-Fm. | Tonstein: Pyrit  | –   | – |  Obtususton-Formation |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15200580 |Arietenkalk-Fm. | Kalkstein: Bioklasten  | Mergelstein   | – |  Arietenkalk-Formation |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15200581 |Angulatenton-Fm. | Tonstein  | Mergelstein: Bitumen   | – |  Angulatenton-Formation |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15200582 |Psilonotenton-Fm. | Tonstein  | Kalkstein   | – |  Psilonotenton-Formation |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15200584 |Etiollets-Fm.: Tabalcon-Kalk | Kalkstein: Bioklasten  | –   | – |  Tabalcon-Kalk |  Kimméridgien     | Kimméridgien   | Malm  |
|15200585 |Bonneville-Sandstein | Sandstein: Glimmer  | Konglomerat: polymikt   | – |  Bonneville-Sandstein |  Rupélien     | Rupélien   | UMM  |
|15200586 |Montauban-Mergel | Mergelstein: Glimmer  | –   | – |  Montauban-Mergel |  Rupélien     | Rupélien   | UMM  |
|15200588 |Mornex-Nagelfluh | Konglomerat: kalkig  | Sandstein   | – |  Mornex-Nagelfluh |  Rupélien     | Rupélien   | UMM  |
|15200589 |USM-III bis OSM-I | Konglomerat  | Mergelstein   | – |  – |  Langhien     | Burdigalien   | Molasse  |
|15200590 |Uetliberg-Fm.: Loorenkopf-Nagelfluh | Konglomerat: kalkig-dolomitisch  | –   | – |  Loorenkopf-Nagelfluh |  Serravallien     | Serravallien   | OSM  |
|15200591 |Grand-Essert-Fm: Neuchâtel-Mb.: Oberer Teil | Kalkstein: spätig: Bioklasten-Glaukonit  | Kalkstein: Ooide   | – |  «Pierre Jaune Supérieure» |  Hauterivien     | Hauterivien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200592 |Grand-Essert-Fm: Neuchâtel-Mb.: Unterer Teil | Kalkstein: spätig: Bioklasten-Glaukonit  | Mergelstein   | – |  «Pierre Jaune Inférieure» |  Hauterivien     | Hauterivien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200593 |Chambotte-Fm.: Oberer Teil | Kalkstein: mikritisch: Bioklasten  | –   | – |  Chambotte-Formation |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200594 |Chambotte-Fm.: Unterer Teil | Kalkstein: mikritisch: Bioklasten  | –   | – |  Chambotte-Formation |  Valanginien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200602 |Helvetikum: Siderolithikum | Gestein: residual: Eisenmineralien  | –   | – |  – |  Bartonien     | Lutétien   | Siderolithikum  |
|15200616 |Schwarzwald-Massiv: Grundgebirge | Gestein: metamorph  | Gestein: plutonisch   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15200617 |Schwarzwald-Massiv: Variszische Intrusiva | Gestein: plutonisch  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Variszisches Grundgebirge  |
|15200618 |Calcaire d&#39;eau douce de Mümliswil | Kalkstein  | –   | – |  Mümliswil-Süsswasserkalk |  Chattien précoce     | Chattien précoce   | USM  |
|15200619 |Horizon limnique (OMM-I) | Mergelstein  | Gestein: organisch: Kohle   | – |  Luzern-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200620 |Grès de Dardagny | Sandstein: Bitumen  | –   | – |  Dardagny-Sandstein |  Chattien précoce     | Chattien précoce   | USM  |
|15200621 |Napf-Fm.: Konglomerat-dominierte Fazies | Konglomerat: polymikt: Quarz  | Sandstein: Feldspat   | – |  Napf-Formation |  Langhien     | Burdigalien   | OSM  |
|15200622 |Napf-Fm.: Sandstein-Mergelstein-dominierte Fazies | Sandstein: Feldspat  | Mergelstein   | – |  Napf-Formation |  Langhien     | Burdigalien   | OSM  |
|15200623 |Le-Locle-Fm. | Kalkstein: kreidig  | Mergelstein: Lignit   | Tonstein |  Le-Locle-Formation |  Serravallien     | Langhien   | OSM  |
|15200624 |Le-Locle-Fm.: Le-Verger Mb. | Kalkstein: kreidig  | Mergelstein: Lignit   | – |  Le-Verger-Member |  Serravallien     | Langhien   | OSM  |
|15200625 |Le-Locle-Fm.: Combe-Girard Mb. | Kalkstein: kreidig  | –   | – |  Combe-Girard-Member |  Serravallien     | Langhien   | OSM  |
|15200626 |Crêt-du-Locle-Fm. | Mergelstein  | Konglomerat: kalkig   | – |  Crêt-du-Locle-Formation |  Serravallien     | Langhien   | Molasse  |
|15200627 |Crêt-du-Locle-Fm.: Mergelfazies | Mergelstein  | –   | – |  Crêt-du-Locle-Formation |  Serravallien     | Langhien   | Molasse  |
|15200628 |St.-Gallen-Fm.: Gitzigrabe-Grobsandstein | Sandstein  | –   | – |  Gitzigrabe-Grobsandstein |  Burdigalien     | Burdigalien   | OMM  |
|15200629 |Trois-Rods-Süsswasserkalk | Kalkstein: Bioklasten  | –   | – |  Trois-Rods-Süsswasserkalk |  Chattien précoce     | Chattien précoce   | USM  |
|15200630 |Champ-Vuillerat-Süsswasserkalk | Kalkstein  | –   | – |  Champ-Vuillerat-Süsswasserkalk |  Rupélien     | Priabonien   | Siderolithikum  |
|15200631 |Bentonite de Wholusen | Bentonit  | –   | – |  Wolhusen-Bentonit |  Langhien     | Burdigalien   | OSM  |
|15200632 |Clacaire d&#39;eau douce du Gitzitobel | Kalkstein  | –   | – |  Gitzitobel-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200633 |Calcaire d&#39;eau douce du Wissenbach | Kalkstein  | –   | – |  Wissenbach-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200634 |Calcaire d&#39;eau douce de l&#39;Altbach | Kalkstein  | –   | – |  Altbach-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200635 |Calcaire d&#39;eau douce de Tröleten | Kalkstein  | –   | – |  Tröleten-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200636 |Calcaire d&#39;eau douce du Tschöplihof | Kalkstein  | –   | – |  Tschöplihof-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200637 |Formation du Lienegg | Konglomerat: kalkig  | Sandstein   | Mergelstein |  Lienegg-Formation |  Aquitanien     | Chattien   | USM  |
|15200638 |Formation de l&#39;Öligraben | Konglomerat: polymikt  | Sandstein   | Mergelstein: Kohle |  Öligraben-Formation |  Chattien     | Chattien   | USM  |
|15200639 |Formation du Studweid | Sandstein  | Mergelstein   | Konglomerat: polymikt |  Studweid-Formation |  Aquitanien     | Aquitanien   | USM  |
|15200640 |Formation de Rossemaison | Mergelstein: siltig  | Gestein: residual   | – |  Rossemaison-Formation |  Rupélien     | Priabonien   | Siderolithikum  |
|15200641 |Rhyolithe de Schwaningen-Merenbach | Rhyolith  | –   | – |  Schwaningen-Merenbach-Rhyolith |  Permien     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15200642 |Granite de Schwaningen-Weizen | Granit  | –   | – |  Schwaningen-Weizen-Granit |  Permien     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15200643 |Granite d&#39;Etzgen | Granit  | –   | – |  Etzgen-Granit |  Permien     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15200645 |Karbonatreiche Molasse: Kalk-Dolomit-Nagelfluh | Konglomerat: kalkig-dolomitisch  | –   | – |  – |  Chattien     | Rupélien   | USM  |
|15200646 |Mélange de Hornbüel | Sandstein  | Mergelstein   | Konglomerat |  Hornbüel-Melange |  Chattien     | Rupélien   | Mélange  |
|15200647 |Formation du Kalter Wangen | Konglomerat: kalkig  | Sandstein   | Mergelstein |  Kalter-Wangen-Formation |  Tortonien     | Langhien   | OSM  |
|15200648 |Poudingue de Baltersweil | Konglomerat: polymikt: Bioklasten  | –   | – |  Baltersweil-Nagelfluh |  Burdigalien     | Burdigalien   | OMM  |
|15200649 |Poudingue du Netzbachtal | Konglomerat  | –   | – |  Netzbachtal-Nagelfluh |  Burdigalien     | Burdigalien   | OMM  |
|15200650 |Formation du Rocher des Hirondelles | Kalkstein: Bioklasten  | Mergelstein   | – |  Rocher-des-Hirondelles-Formation |  Barrémien     | Hauterivien   | «Urgonien»  |
|15200651 |Membre du Fort de l&#39;Ecluse | Kalkstein: Bioklasten  | Kalkstein: Ooide   | – |  Fort-de-l&#39;Écluse-Member |  Barrémien     | Hauterivien   | «Urgonien»  |
|15200652 |Membre de Bôle | Mergelstein: Bioklasten  | Kalkstein: mergelig   | – |  Bôle-Member |  Barrémien     | Barrémien   | «Urgonien»  |
|15203433 |Socle cristallin de la nappe de Ruginenta | Gneis  | Gestein: ultramafisch   | Schiefer: Glimmer-Granat |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203430 |Gneiss du Lebendun, arkosique | Sandstein: Feldspat  | –   | – |  Lebendun-Komplex |  Mésozoïque     | Permien   | Grundgebirge  |
|15203431 |Gneiss du Lebendun, conglomératique | Konglomerat  | –   | – |  Lebendun-Komplex |  Mésozoïque     | Permien   | Grundgebirge  |
|15203432 |Série du (Passo) Salarioli | Kalkstein  | Dolomitstein   | Serpentinit |  – |  Trias     | Pennsylvanien   | Sedimentbedeckung  |
|15203434 |Schistes de la nappe de Ruginenta | Schiefer: Glimmer-Granat  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203435 |Paragneiss de la nappe de Ruginenta | Gneis: sedimentär  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203436 |Formation de la Preja | Quarzit  | Rauwacke   | Marmor |  Preja-Formation |  Jurassique tardif     | Trias   | Sedimentbedeckung  |
|15203437 |Formation des Cavalli | Sandstein: tonig  | Sandstein: Quarz   | Schiefer: Glimmer |  Cavalli-Formation |  Permien     | Permien   | Sedimentbedeckung  |
|15203438 |Série de Furgg | Sandstein: Feldspat  | Quarzit   | Marmor |  – |  Mésozoïque     | Permien   | Sedimentbedeckung  |
|15203439 |Granite de Mezzalama | Granit: porphyrisch  | –   | – |  Mezzalama-Granit |  Guadalupien     | Cisuralien   | Grundgebirge  |
|15203440 |Orthogneiss du Mont Rose, à grain grossier | Gneis: magmatisch  | –   | – |  Monte-Rosa-Orthogneis  |  Carbonifère     | Carbonifère   | Grundgebirge  |
|15203441 |Migmatite du Rottal | Migmatit  | –   | – |  Rottal-Migmatit |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203442 |Orthogneiss du Mont Rose, mylonitique | Gneis: mylonitisch  | –   | – |  Monte-Rosa-Orthogneis  |  Carbonifère     | Carbonifère   | Grundgebirge  |
|15203443 |Paragneiss de la nappe du Mont Rose | Gneis: sedimentär  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203444 |Gneiss à biotite de la nappe du Mont Rose | Gneis: Biotit  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203445 |Gneiss rubané de la nappe du Mont Rose | Gneis: gebändert  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203446 |Micaschiste de la nappe du Mont Rose | Schiefer: Glimmer  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203447 |Série du Grundberg | Marmor  | Marmor   | Dolomitstein |  – |  Crétacé tardif     | Trias   | Sedimentbedeckung  |
|15203449 |Orthogneiss de la nappe du Protjengrat | Gneis: magmatisch  | –   | – |  Portjengrat-Orthogneis |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203450 |Gneiss oeillé de Saas Fee | Gneis: augig  | –   | – |  Saas-Fee-Augengneis |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203451 |Migmatite de l&#39;Almagelhorn | Migmatit  | –   | – |  Almagelhorn-Migmatit |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203452 |Paragneiss du Weissmies | Gneis: sedimentär  | Gneis: migmatitisch   | – |  Weissmies-Paragneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203453 |Orthogneiss du Mont Rose, à grain moyen | Gneis: magmatisch  | –   | – |  Monte-Rosa-Orthogneis  |  Carbonifère     | Carbonifère   | Grundgebirge  |
|15203454 |Mylonite du Stellihorn | Gneis: mylonitisch  | –   | – |  Stellihorn-Mylonit |  Cénozoïque     | Paléozoïque   | Grundgebirge  |
|15203455 |Calcschistes de la Série du Fäldbach | Schiefer: kalkig  | Schiefer: Glimmer   | – |  – |  Mésozoïque     | Mésozoïque   | Post-Rift  |
|15203456 |Dogger nord-pennique | Schiefer  | –   | – |  – |  Jurassique moyen     | Jurassique moyen   | Lias-Dogger in detritischer Fazies  |
|15203457 |Lias nord-pennique | Kalkstein  | –   | – |  – |  Aalénien     | Jurassique précoce   | Lias-Dogger in detritischer Fazies  |
|15203458 |Dolomie du Trias nord-pennique | Marmor: dolomitisch  | –   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15203459 |Paragneiss de Vagrande | Gneis: sedimentär  | Gneis: Biotit-Muskovit   | Schiefer: Glimmer |  Valgrande-Paragneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203460 |Roches intrusives varisques du Briançonnais | Gneis: magmatisch  | –   | – |  – |  Permien     | Carbonifère   | Variszisches Grundgebirge  |
|15203461 |Socle cristallin anté-varisque du Briançonnais | Gneis  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15203462 |Péridotite du Moncucco | Peridotit  | –   | – |  Moncucco-Peridotit |  Mésozoïque     | Paléozoïque   | Grundgebirge  |
|15203463 |Schistes oeillés à porphyroblastes d&#39;albite (SOPA) de la Formation de l&#39;Adlerflüe | Schiefer: augig: Glimmer  | –   | – |  Adlerflüe-Formation |  Cambrien     | Protérozoïque   | Grundgebirge  |
|15203464 |Amphibolite rubanée de la Formation de l&#39;Adlerflüe | Amphibolit: gebändert  | –   | – |  Adlerflüe-Formation |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203465 |Éclogite du Minugrat | Eklogit  | –   | – |  Minugrat-Eklogit |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203466 |Amphibolite du Complexe gneissique de l&#39;Ergischhorn | Amphibolit  | –   | – |  Ergischhorn-Komplex |  Protérozoïque     | Protérozoïque   | Grundgebirge  |
|15203467 |Roches vertes de la Formation du Distulberg | Gestein: mafisch  | –   | – |  Distulberg-Formation |  Cambrien     | Cambrien   | Grundgebirge  |
|15203468 |Prasinites de la Formation du Métailler | Prasinit  | –   | – |  Métailler-Formation |  Rupélien     | Cambrien   | Grundgebirge  |
|15203469 |Roches ultramafiques de la Formation du Métailler | Gestein: ultramafisch  | –   | – |  Métailler-Formation |  Rupélien     | Cambrien   | Grundgebirge  |
|15203470 |Gneiss albitique d&#39;Oberems | Gneis: Albit  | Rhyolith   | – |  Oberems-Albitgneis |  Permien     | Permien   | Variszisches Grundgebirge  |
|15203471 |Permo-Carbonifère de la nappe de la Maggia | Schiefer  | Konglomerat   | – |  – |  Permien     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15203472 |Permien de la nappe de la Maggia | Schiefer: Quarz-Glimmer  | –   | – |  – |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15203473 |Carbonifère de la nappe de la Maggia | Schiefer: Glimmer-Graphit  | –   | – |  – |  Carbonifère     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15203474 |Roches intrusives varisques de la nappe de la Maggia | Gestein: plutonisch  | –   | – |  – |  Permien     | Carbonifère   | Variszisches Grundgebirge  |
|15203475 |Socle cristallin anté-varisque de la nappe de la Maggia | Gneis  | Amphibolit   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15203476 |Maggia-D.: Paragneis | Gneis: sedimentär  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15203477 |Gneiss rubané de la nappe de la Maggia | Gneis: gebändert  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15203478 |Gneiss oeillé de la nappe de la Maggia | Gneis: augig  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15203479 |Gneiss d&#39;Alpigia | Gneis: migmatitisch  | Amphibolit: migmatitisch   | – |  Alpigia-Gneis |  Permien     | Permien   | Grundgebirge  |
|15203480 |zone de Gresso-Someo | Quarzit  | Marmor: kalkig   | – |  – |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15203481 |zone de Pertusio | Quarzit  | Marmor: kalkig   | – |  – |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15203482 |zone du Passo di Cristallina | Marmor  | Quarzit   | Schiefer: Glimmer-Granat |  – |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15203483 |Formation du Lago Scuro | Marmor: konglomeratisch  | Brekzie: kalkig   | – |  Lago-Scuro-Formation |  Jurassique tardif     | Jurassique moyen   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15203484 |Formation du Val Sabbia | Quarzit  | –   | – |  Val-Sabbia-Formation |  Sinémurien     | Sinémurien   | Lias-Dogger in detritischer Fazies  |
|15203485 |Formation du (Pizzo) Massari | Sandstein  | Kalkstein: sandig   | – |  Massari-Formation |  Pliensbachien     | Hettangien   | Lias-Dogger in detritischer Fazies  |
|15203486 |Formation du Narèt | Schiefer: Quarz-Glimmer  | Schiefer: Glimmer-Graphit   | Marmor |  Naret-Formation |  Hettangien     | Rhétien   | Lias-Dogger in detritischer Fazies  |
|15203487 |Serpentinite du Breithorn | Serpentinit  | –   | – |  Breithorn-Serpentinit |  Jurassique tardif     | Jurassique moyen   | Ophiolithische Abfolge  |
|15203488 |Amphibolite de Loranco | Amphibolit  | –   | – |  Loranco-Amphibolit |  Jurassique tardif     | Jurassique moyen   | Ophiolithische Abfolge  |
|15203489 |Éclogite d&#39;Andolla | Eklogit  | –   | – |  Andolla-Eklogit |  Jurassique tardif     | Jurassique moyen   | Ophiolithische Abfolge  |
|15203490 |Schistes du Roz | Schiefer: sandig-kalkig  | Schiefer: sandig   | Schiefer: tonig |  Roz-Schiefer |  Paléogène     | Crétacé tardif   | Sedimentbedeckung  |
|15203491 |Ophiolite de la zone de Ramosch | Serpentinit  | Amphibolit   | – |  – |  Crétacé précoce     | Jurassique   | Ophiolithische Abfolge  |
|15203492 |Métasédiments de la nappe d&#39;Arosa | Schiefer  | Marmor   | Sandstein |  – |  Crétacé tardif     | Jurassique tardif   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203493 |Serpentinite de la Totalp | Serpentinit  | –   | – |  Totalp-Serpentinit |  Oxfordien     | Bathonien   | Ophiolithische Abfolge  |
|15203494 |Brèche de Maran | Brekzie: polymikt  | Schiefer: tonig-kieselig   | – |  Maran-Brekzie |  Jurassique tardif     | Jurassique tardif   | Syn-Rift  |
|15200659 |Membres de Wangen et du Letzi, indifférenciés | Kalkstein: mikritisch  | –   | – |  Villigen-Formation |  Kimméridgien     | Oxfordien   | Malm  |
|15200653 |Membre de Montcherand | Mergelstein  | Kalkstein: Bioklasten   | – |  Montcherand-Member |  Barrémien     | Hauterivien   | «Urgonien»  |
|15200654 |Calcaire Roux | Kalkstein: spätig: Ooide  | –   | – |  Vuache-Formation |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200658 |Couches du Schwarzbach | Kalkstein: mergelig: Bioklasten  | Mergelstein   | – |  Schwarzbach-Formation |  Kimméridgien     | Kimméridgien   | Malm  |
|15200660 |Grand-Essert- bis Narlay-Fm. | Kalkstein  | Mergelstein   | Sandstein: Glaukonit |  – |  Pléistocène     | Valanginien   | Post-Rift  |
|15200661 |Goldberg- bis Vuache-Fm. | Kalkstein  | Mergelstein   | – |  – |  Valanginien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200662 |Rocher-des-Hirondelles-Fm.: Bellegarde-Bk. | Kalkstein: Bioklasten  | Mergelstein: konglomeratisch   | – |  Bellegarde-Bänke |  Barrémien     | Barrémien   | «Urgonien»  |
|15200663 |Rocher-des-Hirondelles-Fm.: Serrières-Bk. | Kalkstein: Bioklasten  | –   | – |  Serrières-Bank |  Barrémien     | Barrémien   | «Urgonien»  |
|15200664 |Gorges-de-l&#39;Orbe-Fm.: Morteau-Kalk | Kalkstein: Bioklasten  | Kalkstein: Ooide   | – |  Morteau-Kalk |  Barrémien     | Barrémien   | «Urgonien»  |
|15200665 |Gorges-de-l&#39;Orbe-Fm.: Montcherand-Mb.: La-Vaux-Bk. | Kalkstein: Ooide  | –   | – |  La-Vaux-Bänke |  Barrémien     | Barrémien   | «Urgonien»  |
|15200666 |Gorges-de-l&#39;Orbe-Fm.: Montcherand-Mb.: Cul-du-Nozon-Bk. | Mergelstein  | –   | – |  Cul-du-Nozon-Bänke |  Hauterivien     | Hauterivien   | «Urgonien»  |
|15200667 |Gorges-de-l&#39;Orbe-Fm.: Montcherand-Mb.: Pont-des-Pierres-Bk. | Kalkstein: mergelig: Glaukonit  | –   | – |  Pont-des-Pierres-Bänke |  Hauterivien     | Hauterivien   | «Urgonien»  |
|15200668 |Grand-Essert-Fm: Hauterive-Mb.: Censeau-Mergel | Mergelstein: Korallen  | –   | – |  Censeau-Mergel |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200669 |Grand-Essert-Fm: Hauterive-Mb.: Morteau-Mergel | Mergelstein: tonig  | –   | – |  Morteau-Mergel |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200670 |Chambotte-Fm.: Guiers-Mb.: Grande-Varappe-Bk. | Mergelstein: konglomeratisch  | –   | – |  Grande-Varappe-Bank |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200671 |Le-Coin-Fm. | Kalkstein: mikritisch: Chert  | Kalkstein: dolomitisch   | – |  Le-Coin-Formation |  Kimméridgien     | Kimméridgien   | Malm  |
|15200672 |Bärschwil-, St-Ursanne- und Pichoux-Fm. | Kalkstein  | Mergelstein   | Tonstein |  – |  Oxfordien     | Oxfordien   | Malm  |
|15200673 |Passwang- bis Ifenthal-Fm. | Kalkstein  | Mergelstein   | Tonstein |  – |  Oxfordien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15200674 |Calcaire à Entroques | Kalkstein: spätig: Bioklasten  | –   | – |  «Calcaire à Entroques» |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200675 |Staffelegg-Fm. und Opalinus-Ton | Mergelstein  | Tonstein   | – |  – |  Aalénien     | Hettangien   | Syn-Rift  |
|15200676 |Schafisheim-Syenit | Syenit  | Granit   | Diorit |  Schafisheim-Syenit |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200677 |Pfaffnau-Granit | Granit: Biotit  | Diorit   | Syenit |  Pfaffnau-Granit |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200678 |Zurzach-Granit | Granit: Biotit-Cordierit  | –   | – |  Zurzach-Granit |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200679 |Siblingen-Granit | Granit: Biotit-Cordierit  | –   | – |  Siblingen-Granit |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200680 |Lindau-Granit | Granit: Biotit-Cordierit  | –   | – |  Lindau-Granit |  Mississippien     | Dévonien   | Frühvariszisches Grundgebirge  |
|15200681 |Kreuzlingen-Granit | Granit: Biotit-Cordierit  | –   | – |  Kreuzlingen-Granit |  Mississippien     | Dévonien   | Frühvariszisches Grundgebirge  |
|15200682 |Schlächtenhaus-Schiefer | Sandstein: tonig  | Schiefer: tonig   | – |  Schlächtenhaus-Schiefer |  Mississippien     | Dévonien tardif   | Prä- bis frühvariszisches Grundgebirge  |
|15200683 |Gersbach-Schiefer | Schiefer: Hornblende  | –   | – |  Gersbach-Schiefer |  Ordovicien     | Ordovicien   | Prä- bis frühvariszisches Grundgebirge  |
|15200685 |Courgenay- Balsthal- und VilligenFm. | Kalkstein  | Mergelstein   | – |  – |  Kimméridgien     | Oxfordien   | Malm  |
|15200686 |Pichoux-Fm.: Korallenfazies | Kalkstein: Korallen  | Kalkstein: mergelig   | – |  Pichoux-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15200687 |Pichoux-Fm.: Schwammfazies | Kalkstein: Schwämme  | Kalkstein: mergelig   | Mergelstein |  Pichoux-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15200688 |Kalter-Wangen-Fm.: Konglomerat-dominierte Fazies | Konglomerat: kalkig  | Sandstein   | Mergelstein |  Kalter-Wangen-Formation |  Tortonien     | Langhien   | OSM  |
|15200689 |Kalter-Wangen-Fm.: Sandstein-Mergelstein-dominierte Fazies | Sandstein  | Mergelstein   | Konglomerat: kalkig |  Kalter-Wangen-Formation |  Tortonien     | Langhien   | OSM  |
|15200690 |Kalter-Wangen-Fm.: Heilsberg-Bentonit | Bentonit  | –   | – |  Heilsberg-Bentonit |  Tortonien     | Langhien   | OSM  |
|15200691 |OSM: Humlikon-Bentonit | Bentonit  | –   | – |  Humlikon-Bentonit |  Tortonien     | Langhien   | OSM  |
|15200684 |Herdern-Streifengneis | Gneis: Biotit  | –   | – |  Herdern-Streifengneis |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202001 |Mélange de Habkern | Mergelstein  | Tonstein   | – |  Habkern-Melange |  Eocène     | Crétacé tardif   | Mélange  |
|15202002 |Mélange de Sörenberg | Mergelstein  | Tonstein   | – |  Sörenberg-Melange |  Priabonien     | Priabonien   | Mélange  |
|15202003 |Mélange de Wildhaus | Mergelstein  | –   | – |  Wildhaus-Melange |  Eocène     | Eocène   | Mélange  |
|15202004 |Unités de flysch sud-helvétiques | Mergelstein  | Sandstein: kalkig   | Kalkstein: Nummuliten |  – |  Priabonien     | Lutétien   | Flysch  |
|15202005 |Groupe du Flysch nord-helvétique | Sandstein: tonig  | Tonstein   | – |  – |  Rupélien     | Priabonien   | Flysch  |
|15202006 |Formation de Matt | Sandstein: Quarz  | Tonstein: schiefrig   | Konglomerat: polymikt |  Matt-Formation |  Rupélien     | Rupélien   | Flysch  |
|15202007 |Schistes ardoisiers d&#39;Engi | Tonstein: schiefrig  | Sandstein: Quarz   | – |  Engi-Dachschiefer |  Rupélien     | Rupélien   | Flysch  |
|15202008 |Conglomérat du Gruontal | Konglomerat: polymikt  | Brekzie   | – |  Gruontal-Konglomerat |  Rupélien     | Rupélien   | Flysch  |
|15202009 |Formation d&#39;Elm | Tonstein: schiefrig  | Sandstein: tonig   | – |  Elm-Formation |  Rupélien     | Priabonien   | Flysch  |
|15202010 |Banc du Rüschenweid | Sandstein  | –   | – |  Rüschenweid-Bank |  Rupélien     | Rupélien   | Flysch  |
|15202011 |Formation de Taveyannaz | Sandstein: tonig  | Tonstein: schiefrig   | – |  Taveyannaz-Formation |  Rupélien     | Priabonien   | Flysch  |
|15202012 |Paléogène de l&#39;Helvétique | Kalkstein: Bioklasten  | Sandstein   | Mergelstein |  – |  Paléogène     | Paléogène   | Sedimentbedeckung  |
|15202013 |Formation de Stad | Mergelstein: siltig  | –   | – |  Stad-Formation |  Priabonien     | Lutétien   | «Nummulitikum»  |
|15202014 |Calcaire de Wängen | Kalkstein: Bioklasten  | –   | – |  Wängen-Kalk |  Priabonien     | Lutétien   | «Nummulitikum»  |
|15202015 |Conglomérat du Jochstock | Konglomerat: kalkig  | Brekzie: kalkig   | Mergelstein: sandig-kalkig |  Jochstock-Konglomerat |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202016 |Formation du Sanetsch | Kalkstein: sandig: Bioklasten  | Sandstein: kalkig   | – |  Sanetsch-Formation |  Rupélien     | Priabonien   | «Nummulitikum»  |
|15202017 |Calcaire de Pierredar | Kalkstein: Bioklasten  | –   | – |  Pierredar-Kalk |  Rupélien     | Priabonien   | «Nummulitikum»  |
|15202018 |Membre de Tsanfleuron | Sandstein: kalkig: Bioklasten  | Kalkstein: arenitisch   | – |  Tsanfleuron-Member |  Priabonien     | Priabonien   | «Nummulitikum»  |
|15202019 |Membre des Diablerets | Kalkstein: sandig  | Mergelstein: Kohle   | – |  Diablerets-Member |  Priabonien précoce     | Priabonien précoce   | «Nummulitikum»  |
|15202020 |Formation du Niederhorn | Sandstein: kalkig: Quarz  | Kalkstein: Bioklasten   | – |  Niederhorn-Formation |  Priabonien     | Bartonien   | «Nummulitikum»  |
|15202021 |Calcaire de la Gemmenalp | Kalkstein: Bioklasten  | –   | – |  Gemmenalp-Kalk |  Priabonien     | Bartonien   | «Nummulitikum»  |
|15202022 |Grès du Hohgant | Sandstein: kalkig: Quarz  | Sandstein: kalkig: Bioklasten   | – |  Hohgant-Sandstein |  Priabonien     | Bartonien   | «Nummulitikum»  |
|15202023 |Couches du Wagenmoos | Sandstein: Quarz  | –   | – |  Wagenmoos-Bänke |  Priabonien     | Priabonien   | «Nummulitikum»  |
|15202024 |Formation du Wildstrubel | Mergelstein: sandig-kalkig  | Sandstein: Glaukonit   | – |  Wildstrubel-Formation |  Priabonien     | Bartonien   | «Nummulitikum»  |
|15202025 |Membre du Schimberg | Mergelstein: sandig  | Sandstein: Quarz   | Konglomerat |  Schimberg-Member |  Priabonien     | Priabonien   | «Nummulitikum»  |
|15202026 |Membre du Tierberg | Sandstein: Glaukonit  | Mergelstein: sandig   | – |  Tierberg-Member |  Bartonien     | Bartonien   | «Nummulitikum»  |
|15202027 |Membre du Küblibad | Sandstein: Glaukonit  | –   | – |  Küblibad-Member |  Bartonien     | Bartonien   | «Nummulitikum»  |
|15203498 |Calcaire à calpionelles de la nappe du Platta | 15111233  | Mergelstein   | – |  – |  Jurassique     | Jurassique   | Maiolica / Aptychenkalk  |
|15203495 |Calcaire de Solis | Kalkstein: tonig: Chert  | –   | – |  Solis-Kalk |  Jurassique tardif     | Jurassique précoce   | Sedimentbedeckung  |
|15203496 |Métasédiments de la nappe du Platta | Gestein: sedimentär  | –   | – |  – |  Cénozoïque     | Jurassique   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203497 |Schistes de Flix | Schiefer: tonig  | Schiefer: kieselig   | – |  Flix-Schichten |  Albien     | Aptien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203499 |Radiolarite de la nappe du Platta | Gestein: kieselig: Radiolarien  | Schiefer: tonig-kieselig   | Brekzie |  Falotta-Radiolarit |  Jurassique     | Jurassique   | Radiolarit  |
|15203500 |Ophiolite de la nappe du Platta | Serpentinit  | Gabbro   | Basalt |  – |  Jurassique tardif     | Jurassique moyen   | Ophiolithische Abfolge  |
|15203501 |Gneiss de Vignone | Gneis  | –   | – |  Vignun-Gneis |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203502 |Métasédiments de la nappe de l&#39;Avers | Gestein: sedimentär  | –   | – |  – |  Cénozoïque     | Jurassique   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203503 |Ophiolite de la nappe de l&#39;Avers | Serpentinit  | Gabbro   | Basalt |  – |  Jurassique tardif     | Jurassique moyen   | Ophiolithische Abfolge  |
|15203504 |Brekzie-Formation | Brekzie  | –   | – |  – |  Crétacé tardif     | Albien   | Couches Rouges  |
|15203505 |Brèche du Minschun | Brekzie: polymikt  | –   | – |  Minschun-Brekzie (Tasna) |  Aptien     | Barrémien   | Couches Rouges  |
|15203506 |Socle cristallin de la nappe de la Tasna | Gneis: sedimentär  | Schiefer   | Migmatit |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15203507 |Gneiss du Piz del Palo | Gneis: augig  | Gneis: gebändert   | – |  Piz-del-Palo-Gneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203508 |Granite de Truzzo | Granit  | Gneis: augig   | – |  Truzzo-Granit |  Permien     | Carbonifère   | Variszisches Grundgebirge  |
|15203509 |Gneiss de Rebi | Gneis  | Granit   | – |  Rebi-Gneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203510 |Gabbro de Brione | Gabbro  | –   | – |  Brione-Gabbro |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203511 |Migmatite du Gruf | Gneis: migmatitisch  | –   | – |  Gruf-Migmatit |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203512 |Adula-D.: Basaler Gneis | Gneis: Biotit-Muskovit  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203513 |Gneiss du Val Chironico | Gneis: Biotit-Hornblende  | –   | – |  Val-Chironico-Gneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203514 |Gneiss de Ganna | Gneis: schiefrig-augig  | –   | – |  Ganna-Gneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203515 |Adula-D.: Albit-Oligoklasgneis | Gneis: Albit-Oligoklas  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203516 |Gneiss de Sivigia | Gneis  | Schiefer: Glimmer-Granat   | – |  Sivigia-Gneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203517 |Complexe gneissique d&#39;Aula-Spruga | Gneis: Biotit  | Gneis: Hornblende   | – |  Aula-Spruga-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203518 |Schistes verts du Lizun | 15111629  | Gabbro   | – |  Lizun-Prasinit |  Jurassique tardif     | Jurassique moyen   | Ophiolithische Abfolge  |
|15203519 |Formation des Rossi | Schiefer: Glimmer-Granat  | –   | – |  Rossi-Formation |  Crétacé     | Jurassique tardif   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203520 |Gneiss de Bosco | Gneis  | –   | – |  Bosco-Gneis |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203521 |Gneiss du Batnall | Gneis: augig  | –   | – |  Batnall-Gneis |  Paléozoïque     | Paléozoïque   | Grundgebirge  |
|15203522 |Seron-Fm.: Sandig-kalkige Fazies | Kalkstein: sandig: Bioklasten  | –   | – |  Seron-Formation |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203523 |Seron-Fm.: Konglomerat-dominierte Fazies | Konglomerat: polymikt  | –   | – |  Seron-Formation |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203524 |Frutigen-Fm.: Konglomerat-dominierte Fazies | Konglomerat: polymikt  | Sandstein   | – |  Frutigen-Formation |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203525 |Frutigen-Fm.: Schiefrige Fazies | Tonstein: schiefrig  | Sandstein: kalkig   | Sandstein: tonig |  Frutigen-Formation |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203526 |Gypse de la Zone Submédiane | Evaporit: Gips  | –   | – |  – |  Trias     | Trias   | Mélange  |
|15203527 |Karpatischer Keuper | Kalkstein: Korallen  | Tonstein   | – |  – |  Trias tardif     | Trias tardif   | Pelitische Trias  |
|15203528 |Marne de Zwischenmythen | Mergelstein: sandig: Glimmer  | –   | – |  Zwischenmythen-Mergel |  Trias tardif     | Trias tardif   | Pelitische Trias  |
|15203529 |Cenomanbrekzien-Serie | Brekzie  | Tonstein: schiefrig   | Mergelstein |  «Cenomanbrekzien-Serie» |  Cénomanien     | Cénomanien   | Post-Rift Mesozoikum in detritischer Fazies  |
|15203530 |Brèche du Bettlerjoch | Brekzie  | –   | – |  Bettlerjoch-Brekzie |  Mésozoïque     | Mésozoïque   | Post-Rift Mesozoikum in detritischer Fazies  |
|15203531 |Brèche de Bargella | Brekzie  | –   | – |  Bargella-Brekzie |  Cénomanien     | Cénomanien   | Post-Rift Mesozoikum in detritischer Fazies  |
|15203532 |Adula-D.: Kalkschiefer und Marmor | Schiefer: kalkig  | Marmor: kalkig   | – |  – |  Mésozoïque     | Mésozoïque   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203533 |Formation du Salahorn: métaplutonite | Gestein: plutonisch  | –   | – |  Salahorn-Formation |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203534 |Formation du Salahorn: paragneiss | Gneis: sedimentär  | –   | – |  Salahorn-Formation |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203535 |Adula-D.: Ultramafitit | Gestein: ultramafisch  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203536 |Cima-Lunga-D.: Kalkschiefer und Marmor | Schiefer: kalkig  | Marmor: kalkig   | – |  – |  Mésozoïque     | Mésozoïque   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203537 |Cima-Lunga-D.: Dolomitmarmor | Marmor: dolomitisch  | –   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15203538 |Cima-Lunga-D.: Paragneis | Gneis: sedimentär  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203539 |Gneiss de Vacarisc | Gneis  | –   | – |  Vacarisc-Gneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203540 |Gneiss de Rognoi | Gneis  | –   | – |  Rognoi-Gneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203541 |Cima-Lunga-D.: Granatit | Granofels: Granat  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203542 |Cima-Lunga-D.: Amphibolit | Amphibolit  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203543 |Cima-Lunga-D.: Eklogit | Eklogit  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203544 |Cima-Lunga-D.: Ultramafitit | Gestein: ultramafisch  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203545 |Gneiss de Personico | Gneis  | Granit   | – |  Personico-Gneis |  Permien     | Carbonifère   | Grundgebirge  |
|15203546 |Gneiss de la Leventina: partie supérieure | Gneis: Biotit-Muskovit  | Granit   | – |  Leventina-Gneis |  Permien     | Carbonifère   | Grundgebirge  |
|15203547 |Gneiss de la Leventina: partie inférieure | Gneis  | Granit   | – |  Leventina-Gneis |  Permien     | Carbonifère   | Grundgebirge  |
|15203548 |Leventina-D.: Kalksilikatfels | Granofels: Kalksilikat  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203549 |Leventina-D.: Leukogneis | Gneis  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203550 |Leventina-D.: Paragneis | Gneis: sedimentär  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203551 |Leventina-D.: Amphibolit | Amphibolit  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203552 |Maggia-D.: Amphibolit | Amphibolit  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15203553 |Simano-D.: Kalkmarmor | Marmor: kalkig  | –   | – |  – |  Mésozoïque     | Mésozoïque   | Grundgebirge  |
|15203554 |Simano-D.: Dolomitmarmor | Marmor: dolomitisch  | –   | – |  – |  Trias     | Trias   | Grundgebirge  |
|15203555 |Simano-D.: Paragneis | Gneis: sedimentär  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203556 |Gneiss de Renten | Gneis  | –   | – |  Renten-Gneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203557 |Gneiss de Legiuna | Gneis: augig  | –   | – |  Legiuna-Gneis |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15203558 |Simano-D.: Amphibolit | Amphibolit  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Grundgebirge  |
|15204129 |Ostalpin: Jura | Gestein: kieselig: Radiolarien  | Kalkstein: mikritisch: Bioklasten   | Tonstein |  – |  Jurassique     | Jurassique   | Sedimentbedeckung  |
|15202441 |Bretaye-Fm. | Tonstein: siltig: Glimmer  | –   | – |  Formation de Bretaye |  Aalénien     | Aalénien   | Syn-Rift  |
|15203091 |Unité du Holzerhorn | Mergelstein: sandig: Kohle  | Kalkstein: sandig: Bioklasten   | Konglomerat |  Holzerhorn-Einheit |  Callovien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15204128 |Permo-Carbonifère de l&#39;Austroalpin | Gestein: vulkanisch  | Gestein: sedimentär   | – |  – |  Permien     | Carbonifère   | Spät- bis postvariszisches Grundgebirge  |
|15202342 |Gneiss de l&#39;Hüenerstock | Gneis: granitisch  | –   | – |  Hüenerstock-Gneis |  Paléozoïque     | Paléozoïque   | Prävariszisches Grundgebirge  |
|15202345 |Migmatite du Val Camadra | Gneis: migmatitisch  | –   | – |  Val-Camadra-Migmatit |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202502 |Verrucano d&#39;Ilanz s.s. | Sandstein  | Konglomerat   | – |  – |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15202503 |Buntgefleckte Schiefer (Ilanz) | Schiefer  | Phyllit   | – |  – |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15202504 |Permien de la nappe du Tavetsch (Val Acla Mulin) | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15202254 |Sédiments permiens de la zone d&#39;Ilanz | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15202257 |zone de l&#39;Oberaar-Furka | Gneis  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202258 |zone d&#39;Ausserberg-Avat | Gneis  | Migmatit   | Schiefer |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15200596 |Helvetischer Flysch | Sandstein  | Tonstein   | – |  – |  Rupélien     | Lutétien   | Flysch  |
|15200597 |Euthal- bis Stad-Fm. | Kalkstein: Bioklasten  | Sandstein   | Mergelstein |  – |  Priabonien     | Sélandien   | «Nummulitikum»  |
|15200598 |Stad- und Muot-da-Rubi-Fm. | Mergelstein  | Sandstein   | – |  – |  Priabonien     | Lutétien   | Sedimentbedeckung  |
|15200599 |Euthal- bis Sanetsch-Fm. | Kalkstein: Bioklasten  | Sandstein   | Mergelstein |  – |  Rupélien     | Sélandien   | «Nummulitikum»  |
|15202260 |Gneiss granitique de la zone d&#39;Ausserberg-Avat | Gneis: granitisch  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202261 |Paragneiss de la zone d&#39;Ausserberg-Avat | Gneis: sedimentär  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202262 |zone de Clavaniev | Gestein: tektonisch  | –   | – |  – |  Paléozoïque     | Protérozoïque   | Spät- bis postvariszisches Grundgebirge  |
|15202649 |Nufenen-Zone | Schiefer: tonig  | Schiefer: kalkig   | Quarzit |  – |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15202268 |zone d&#39;Ausserbinn-Piz Cavel | Gneis  | Amphibolit   | Schiefer |  – |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202650 |Termen-Zone | Schiefer: tonig  | Schiefer: kalkig   | – |  – |  Mésozoïque     | Mésozoïque   | Sedimentbedeckung  |
|15203671 |Salahorn-Fm. | Schiefer: Glimmer  | Gneis: sedimentär   | – |  Salahorn-Formation |  Cambrien     | Cambrien   | Grundgebirge  |
|15200607 |Etiollets- Reuchenette- und Twannbach-Fm. | Kalkstein: mikritisch  | Mergelstein   | – |  – |  Tithonien     | Kimméridgien   | Malm  |
|15200608 |Bärschwil-, St-Ursanne-, Pichoux- und Wildegg-Fm. | Mergelstein  | Kalkstein   | Tonstein |  – |  Oxfordien     | Oxfordien   | Malm  |
|15203672 |Col-de-Tompey- und Vudalla-Fm. | Mergelstein  | Kalkstein   | Sandstein: kalkig |  – |  Hettangien     | Rhétien   | Lias-Dogger in neritischer Fazies  |
|15202407 |Punteglias-Granit: Posta-Biala-Granit | Granit  | –   | – |  Posta-Biala-Granit |  Mississippien moyen     | Mississippien moyen   | Prävariszisches Grundgebirge  |
|15202280 |Mélange du Sardona | Mergelstein  | Sandstein   | – |  – |  Tertiaire     | Crétacé tardif   | Mélange  |
|15202409 |Punteglias-Granit: Val-Punteglias-Diorit | Diorit: Biotit-Hornblende  | Diorit: monzonitisch   | Monzonit: Quarz |  Val-Punteglias-Diorit |  Viséen     | Viséen   | Prävariszisches Grundgebirge  |
|15200379 |Molasse alsacienne s.l. | Mergelstein  | Siltstein   | Sandstein: Glimmer |  «Elsässer-Molasse» |  Chattien     | Chattien   | USM  |
|15200381 |Hauptogenstein: Mittlerer Teil | Mergelstein  | Kalkstein: mergelig   | – |  Hauptrogenstein |  Bathonien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15205001 |Groupe du Dolin | Brekzie  | Dolomitstein   | Sandstein |  – |  Jurassique moyen     | Trias   | Sedimentbedeckung  |
|15205002 |Brèche calcaire du Dolin | Brekzie: kalkig-dolomitisch  | –   | – |  Petit-Dolin-Kalkbrekzie |  Jurassique moyen     | Jurassique précoce   | Lias-Dogger in neritischer Fazies  |
|15205003 |zone de Roisan | Marmor  | Schiefer   | – |  – |  Trias moyen     | Permien   | Sedimentbedeckung  |
|15205004 |Série d&#39;Arolla | Gneis: gebändert  | Schiefer: Glimmer   | – |  – |  Cisuralien     | Cisuralien   | Grundgebirge  |
|15205005 |Complexe du Mont Collon | 15111449  | –   | – |  Mont-Collon-Gabbro |  Cisuralien     | Cisuralien   | Variszisches Grundgebirge  |
|15205006 |orthogneiss du Groupe d&#39;Arolla | Gneis: granitisch  | –   | – |  Arolla-Orthogneis |  Permien     | Permien   | Variszisches Grundgebirge  |
|15205007 |Série de Valpelline | 15111557  | Gneis: granulitisch   | – |  – |  Paléogène     | Protérozoïque   | Grundgebirge  |
|15205008 |Argile de Castel di Sotto | Tonstein  | Mergelstein   | Siltstein |  Castel-di-Sotto-Ton |  Zancléen     | Zancléen   | Post-Messinien  |
|15205009 |Conglomérat de Pontegana | Konglomerat: kalkig  | Sandstein   | – |  Pontegana-Konglomerat |  Messinien     | Messinien   | Post-Kollision  |
|15205010 |Groupe de la Gompholite Lombarde | Konglomerat  | Sandstein   | Tonstein |  – |  Langhien     | Chattien   | Lombardischer Gompholit  |
|15205011 |Conglomérat de Lucino | Konglomerat  | Sandstein   | Tonstein |  Lucino-Konglomerat |  Langhien     | Burdigalien   | Lombardischer Gompholit  |
|15205012 |Grès de Cagno | Sandstein  | Konglomerat   | – |  Cagno-Sandstein |  Langhien     | Burdigalien   | Lombardischer Gompholit  |
|15205013 |Grès du Val Grande | Sandstein  | Sandstein: konglomeratisch   | Tonstein |  Val-Grande-Sandstein |  Burdigalien     | Burdigalien   | Lombardischer Gompholit  |
|15205014 |Pélite de Prestino | Tonstein  | Siltstein   | Sandstein |  Prestino-Pelite |  Aquitanien     | Aquitanien   | Lombardischer Gompholit  |
|15205015 |Conglomérat de Como | Konglomerat: polymikt  | Sandstein   | Tonstein |  Como-Konglomerat |  Burdigalien     | Chattien   | Lombardischer Gompholit  |
|15205016 |Grès de Malnate | Sandstein  | Sandstein: konglomeratisch   | Tonstein |  Malnate-Sandstein |  Burdigalien     | Burdigalien   | Lombardischer Gompholit  |
|15205017 |Pélite du Rio dei Gioghi | Tonstein  | Siltstein   | Sandstein |  Rio-dei-Gioghi-Pelite |  Aquitanien     | Aquitanien   | Lombardischer Gompholit  |
|15205018 |Formation de Chiasso | Tonstein  | Sandstein   | Konglomerat |  Chiasso-Formation |  Chattien     | Chattien   | Lombardischer Gompholit  |
|15205019 |Conglomérat de Villa Olmo | Konglomerat: polymikt  | Sandstein   | Tonstein |  Villa-Olmo-Konglomerat |  Chattien     | Chattien   | Lombardischer Gompholit  |
|15205020 |Formation de Ternate | Kalkstein: arenitisch: Bioklasten  | Mergelstein   | – |  Ternate-Formation |  Priabonien     | Priabonien   | Post-Kollision in pelagischer Fazies  |
|15205021 |Formation de Brenno | Kalkstein: mikritisch  | Kalkstein: arenitisch   | – |  Brenno-Formation |  Maastrichtien     | Campanien   | Post-Kollision in pelagischer Fazies  |
|15205022 |Conglomérat de Prella | Konglomerat: polymikt  | Kalkstein: arenitisch   | Kalkstein: mikritisch |  Prella-Konglomerat |  Campanien     | Campanien   | Post-Kollision in pelagischer Fazies  |
|15205023 |Groupe du Flysch Lombard | Sandstein  | Konglomerat: polymikt   | Kalkstein |  – |  Campanien     | Cénomanien   | Flysch  |
|15205024 |Flysch de Bergamo | Tonstein  | Kalkstein: arenitisch   | – |  Bergamo-Flysch |  Campanien     | Santonien   | Flysch  |
|15205025 |Flysch de Coldrerio | Sandstein  | Siltstein   | Mergelstein |  Coldrerio-Flysch |  Campanien     | Santonien   | Flysch  |
|15205026 |Conglomérat de Torre | Konglomerat: polymikt  | Sandstein   | – |  Torre-Konglomerat |  Santonien     | Santonien   | Flysch  |
|15205027 |Flysch du Varesotto | Sandstein  | Siltstein   | Mergelstein |  Varesotto-Flysch |  Santonien     | Cénomanien   | Flysch  |
|15205028 |Groupe de la Scaglia Lombarda | Kalkstein: mergelig  | Mergelstein   | – |  – |  Cénomanien     | Aptien   | Scaglia  |
|15205029 |Scaglia Rossa Lombarda | Kalkstein: mergelig  | Mergelstein   | – |  «Scaglia Rossa Lombarda» |  Cénomanien     | Cénomanien   | Scaglia  |
|15205030 |Scaglia Bianca Lombarda | Kalkstein: mergelig  | Mergelstein   | Tonstein: schiefrig: Bitumen |  «Scaglia Bianca Lombarda» |  Albien     | Albien   | Scaglia  |
|15205031 |Scaglia Variegata Lombarda | Kalkstein: mergelig  | Mergelstein   | Tonstein: schiefrig: Bitumen |  «Scaglia Variegata Lombarda» |  Albien     | Aptien   | Scaglia  |
|15202031 |Membre de Fräkmünt | Sandstein: Quarz-Glaukonit  | Kalkstein: mikritisch   | Sandstein: kalkig: Bioklasten |  Fräkmünt-Member |  Bartonien     | Lutétien   | «Nummulitikum»  |
|15202028 |Formation du Klimsenhorn | Sandstein: Quarz  | Kalkstein: sandig   | Kalkstein: mikritisch |  Klimsenhorn-Formation |  Bartonien     | Lutétien   | «Nummulitikum»  |
|15202029 |Membre du Fruttli | Kalkstein: mikritisch  | Sandstein: kalkig: Bioklasten   | Kalkstein: sandig: Bioklasten |  Fruttli-Member |  Lutétien     | Lutétien   | «Nummulitikum»  |
|15202030 |Membre du Bandweg | Sandstein: Quarz  | Sandstein: kalkig   | Kalkstein |  Band-Member |  Bartonien     | Lutétien   | «Nummulitikum»  |
|15202032 |Membre du Bürgen(stock) | Kalkstein: mikritisch  | Kalkstein: sandig: Glaukonit   | Mergelstein: Bioklasten |  Bürgen-Formation |  Lutétien     | Lutétien   | «Nummulitikum»  |
|15202033 |Membre du Foribach | Kalkstein: sandig: Glaukonit  | Kalkstein: mikritisch: Bioklasten   | – |  Foribach-Member |  Lutétien     | Lutétien   | «Nummulitikum»  |
|15202034 |Membre du Mattgrat | Kalkstein: mikritisch: Bioklasten  | –   | – |  Mattgrat-Member |  Lutétien     | Lutétien   | «Nummulitikum»  |
|15202035 |Membre de Scharti | Sandstein: kalkig: Glaukonit  | Kalkstein: sandig: Bioklasten   | Mergelstein |  Scharti-Member |  Lutétien     | Lutétien   | «Nummulitikum»  |
|15202036 |Formation d&#39;Euthal | Kalkstein: Nummuliten  | Sandstein: Quarz-Glaukonit   | – |  Euthal-Formation |  Lutétien     | Sélandien   | «Nummulitikum»  |
|15202037 |Membre du Steinbach | Sandstein: Glaukonit  | Kalkstein: Bioklasten   | – |  Steinbach-Member |  Lutétien     | Lutétien   | «Nummulitikum»  |
|15202038 |Membre d&#39;Einsiedeln | Kalkstein: Nummuliten  | Sandstein: kalkig: Glaukonit   | – |  Einsiedeln-Member |  Lutétien     | Yprésien   | «Nummulitikum»  |
|15202039 |Membre de la Batöni | Sandstein: Quarz-Glaukonit  | –   | – |  Batöni-Member |  Yprésien     | Thanétien   | «Nummulitikum»  |
|15202040 |Membre de la Chruteren | Sandstein: Glaukonit  | Kalkstein: spätig: Bioklasten   | Kalkstein: Algen |  Chruteren-Member |  Yprésien     | Thanétien   | «Nummulitikum»  |
|15202041 |Membre du Fliegenspitz | Mergelstein: sandig  | –   | – |  Fliegenspitz-Member |  Thanétien     | Sélandien   | «Nummulitikum»  |
|15202043 |Marbre de Grindelwald | Brekzie: kalkig  | –   | – |  Grindelwald-Marmor |  Eocène moyen     | Eocène moyen   | Siderolithikum  |
|15202044 |Brèche de Mürren | Brekzie: kalkig: Bioklasten  | –   | – |  Mürren-Brekzie |  Priabonien     | Priabonien   | «Nummulitikum»  |
|15202045 |Conglomérat de la Dünden | Konglomerat: kalkig-residual: Eisenpisoide  | –   | – |  Dünden-Konglomerat |  Eocène moyen     | Eocène moyen   | Siderolithikum  |
|15202046 |Marbre de Rosenlaui | Brekzie: kalkig  | –   | – |  Rosenlaui-Marmor |  Eocène moyen     | Eocène moyen   | Siderolithikum  |
|15202047 |Crétacé de l&#39;Helvétique | Kalkstein  | Mergelstein   | Sandstein |  – |  Crétacé     | Crétacé   | Post-Rift  |
|15202048 |Formation de Wang | Kalkstein: sandig-kieselig  | Mergelstein   | – |  Wang-Formation |  Maastrichtien     | Campanien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202049 |Marne d&#39;Amden | Mergelstein: Bioklasten  | Siltstein: kalkig   | – |  Amden-Mergel |  Campanien     | Santonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202050 |Formation de Seewen | Kalkstein: mikritisch  | Mergelstein   | – |  Seewen-Formation |  Santonien     | Cénomanien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202051 |Membre du Choltal | Mergelstein: kalkig  | Kalkstein: mikritisch   | – |  Choltal-Member |  Santonien     | Santonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202052 |Formation de Garschella | Sandstein: Glaukonit  | Kalkstein: spätig: Bioklasten   | Mergelstein: sandig |  Garschella-Formation |  Cénomanien     | Aptien   | «Gault»  |
|15202053 |Membre de Selun | Sandstein: Glaukonit  | Kalkstein: sandig-tonig   | Kalkstein: sandig: Bioklasten |  Selun-Member |  Cénomanien     | Aptien   | «Gault»  |
|15202054 |Banc du Kamm | Kalkstein: mikritisch: Bioklasten  | Kalkstein: spätig: Bioklasten   | – |  Kamm-Bank |  Cénomanien     | Albien   | «Gault»  |
|15202055 |Couches de l&#39;Aubrig | Kalkstein: sandig: Glaukonit  | Sandstein: Quarz-Glaukonit   | – |  Aubrig-Schichten |  Cénomanien     | Albien   | «Gault»  |
|15202056 |Banc de la Wannenalp | Sandstein: Glaukonit  | –   | – |  Wannenalp-Bank |  Albien     | Albien   | «Gault»  |
|15202057 |Couches de la Sellamatt | Kalkstein: spätig: Glaukonit  | Kalkstein: mergelig   | Siltstein: kalkig |  Sellamatt-Schichten |  Albien     | Albien   | «Gault»  |
|15202058 |Banc du Plattenwald | Kalkstein: mikritisch: Bioklasten  | –   | – |  Plattenwald-Bank |  Albien     | Aptien   | «Gault»  |
|15202059 |Banc de la Durschlägi | Sandstein: Glaukonit  | –   | – |  Durschlägi-Bank |  Albien     | Albien   | «Gault»  |
|15202060 |Couches de la Niederi | Sandstein: Glaukonit  | –   | – |  Niederi-Schichten |  Albien     | Albien   | «Gault»  |
|15202061 |Banc du Twäriberg | Sandstein: Quarz-Glaukonit  | –   | – |  Twäriberg-Bank |  Albien     | Aptien   | «Gault»  |
|15202062 |Banc de Klaus | Sandstein: Glaukonit  | Kalkstein: mikritisch   | – |  Klaus-Bank |  Albien     | Aptien   | «Gault»  |
|15202063 |Membre de Rankweil | Sandstein: Glaukonit  | –   | – |  Rankweil-Member |  Albien     | Aptien   | «Gault»  |
|15202064 |Membre de la Brisi | Sandstein: Quarz-Glaukonit  | Kalkstein: sandig: Bioklasten   | – |  Brisi-Member |  Aptien     | Aptien   | «Gault»  |
|15202065 |Calcaire de la Brisi | Kalkstein: sandig: Bioklasten  | Kalkstein: spätig: Bioklasten   | – |  Brisi-Member |  Aptien     | Aptien   | «Gault»  |
|15202066 |Grès de la Brisi | Sandstein: Quarz-Glaukonit  | –   | – |  Brisi-Member |  Aptien     | Aptien   | «Gault»  |
|15202067 |Couches du Gams | Sandstein: tonig: Glaukonit  | Mergelstein: kalkig-schiefrig   | – |  Gams-Schichten |  Aptien     | Aptien   | «Gault»  |
|15202068 |Banc de la Luitere | Sandstein: mergelig: Glaukonit  | –   | – |  Luitere-Bank |  Aptien     | Aptien   | «Gault»  |
|15202069 |Membre du Freschen | Tonstein: mergelig  | Sandstein   | Kalkstein |  Freschen-Member |  Albien     | Albien   | «Gault»  |
|15202070 |Couches du Hochkugel | Kalkstein: kieselig  | Tonstein: mergelig   | – |  Hochkugel-Schichten |  Aptien     | Aptien   | «Gault»  |
|15202071 |Membre du Grünten | Mergelstein: sandig: Glaukonit  | Kalkstein: sandig   | Kalkstein: spätig: Bioklasten |  Grünten-Member |  Aptien     | Aptien   | «Gault»  |
|15202072 |Banc du Rohrbachstein | Kalkstein: arenitisch: Glaukonit  | –   | – |  Rohrbachstein-Bank |  Aptien     | Aptien   | «Gault»  |
|15202073 |Formation du Schrattenkalk | Kalkstein: Bioklasten  | –   | – |  Schrattenkalk-Formation |  Aptien     | Barrémien   | «Urgonien»  |
|15202074 |Membre du Rawil | Kalkstein: mergelig: Bioklasten  | Mergelstein   | – |  Rawil-Member |  Aptien     | Aptien   | «Urgonien»  |
|15202075 |Formation de Tierwis | Mergelstein: Glaukonit  | Kalkstein: kieselig   | – |  Tierwis-Formation |  Barrémien     | Hauterivien   | «Urgonien»  |
|15202076 |Banc du Chopf | Kalkstein: sandig  | Mergelstein: Glaukonit-Bioklasten   | – |  Chopf-Bank |  Barrémien     | Barrémien   | «Urgonien»  |
|15202077 |Membre du Drusberg | Mergelstein  | Kalkstein: kieselig   | – |  Drusberg-Member |  Barrémien     | Barrémien   | «Urgonien»  |
|15202078 |Membre de l&#39;Altmann | Mergelstein: sandig: Glaukonit  | Kalkstein: sandig   | – |  Altmann-Member |  Barrémien     | Hauterivien   | «Urgonien»  |
|15202079 |Kieselkalk Helvétique | Kalkstein: kieselig: Bioklasten  | Mergelstein: kieselig   | – |  15253100 |  Hauterivien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202080 |Calcaire échinodermique du Chriesiloch | Kalkstein: spätig: Bioklasten  | –   | – |  Chriesiloch-Echinodermenkalk |  Hauterivien     | Hauterivien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202081 |Membre de la Lidernen | Kalkstein: sandig: Glaukonit  | Mergelstein   | – |  Lidernen-Member |  Hauterivien     | Hauterivien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202082 |Banc du Gemsmättli | Kalkstein: mikritisch: Glaukonit  | Kalkstein: sandig: Bioklasten   | – |  Gemsmättli-Bank |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202083 |Membre du Rahberg | Kalkstein: sandig: Glaukonit  | –   | – |  Rahberg-Bank |  Hauterivien     | Hauterivien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202084 |Formation de Betlis | Kalkstein: spätig: Bioklasten-Chert  | Mergelstein   | – |  Betlis-Formation |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202085 |Membre à Pygurus | Kalkstein: sandig-spätig  | –   | – |  «Pygurus-Member» |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202086 |Membre de la Spitzeren | Kalkstein  | Mergelstein   | – |  Spitzern-Member |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202087 |Banc de Büls | Kalkstein: sandig: Glaukonit  | Mergelstein   | – |  Büls-Bank |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202088 |Calcaire de la Sichel | Kalkstein: mikritisch: Bioklasten-Chert  | –   | – |  Sichel-Kalk |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202089 |Calcaire à Diphyoides | Kalkstein: mikritisch  | –   | – |  15253114 |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202090 |Marne de Vitznau | Mergelstein  | Kalkstein: mikritisch: Bioklasten   | – |  Vitznau-Mergel |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202155 |Membre de Salvan | Sandstein  | –   | – |  Salvan-Member |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202152 |Formation de l&#39;Üblital | Brekzie  | Tonstein   | Gestein: basisch-vulkanisch |  Üblital-Formation |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202153 |Verrucano d&#39;Ilanz | Schiefer  | Gneis   | – |  – |  Permien     | Permien   | Spät- bis postvariszisches Grundgebirge  |
|15202154 |Formation de Vernayaz | Sandstein  | Tonstein   | Konglomerat |  Vernayaz-Formation |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202156 |Conglomérat de Vallorcine | Konglomerat  | –   | – |  Vallorcine-Konglomerat |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202157 |Groupe du Haslital | Gestein: plutonisch  | –   | – |  – |  Assélien     | Assélien   | Spät- bis postvariszisches Grundgebirge  |
|15202158 |Granite de Gastern | Granit: Biotit  | –   | – |  Gastern-Granit |  Assélien     | Pennsylvanien tardif   | Frühvariszisches Grundgebirge  |
|15202159 |Granite de la Mittagflue | Granit: Biotit  | Granit: mylonitisch   | – |  Mittagfluh-Granit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202160 |Granite central de l&#39;Aar | Granit: Biotit  | Granit: schiefrig   | – |  Zentraler Aare-Granit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202161 |Granodiorite du Grimsel | Granodiorit: porphyrisch  | Granit: Biotit   | Gneis: augig |  Grimsel-Granodiorit |  Pennsylvanien tardif     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202162 |Granite sud-occidental de l&#39;Aar | Granit  | Granit: schiefrig   | – |  «Südwestlicher Aare-Granit» |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202163 |Granodiorite de Bugnei | Granodiorit  | –   | – |  Bugnei-Granodiorit |  Pennsylvanien moyen     | Pennsylvanien moyen   | Mittelvariszisches Grundgebirge  |
|15202164 |Roches sédimentaires et volcaniques tardi- à post-varisques du massif de l&#39;Aar | Gestein: sedimentär  | Gestein: vulkanisch   | – |  – |  Cisuralien     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202165 |Formation du Wendenjoch | Schiefer: tonig: Graphit  | Sandstein   | Konglomerat |  Wendenjoch-Formation |  Cisuralien     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202166 |Formation des Windgällen | Granit: mikrokristallin-porphyrisch  | Rhyolith: ignimbritisch   | Schiefer: tonig |  Windgällen-Formation |  Cisuralien     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202167 |Formation du Trift | Schiefer: tonig  | Konglomerat   | Gestein: pyroklastisch |  Trift-Formation |  Cisuralien     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202168 |Formation d&#39;Intschi | Rhyolith  | Ignimbrit   | Schiefer: tonig: Graphit |  Intschi-Formation |  Cisuralien     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202169 |Formation du Bifertengrätli | Konglomerat  | Sandstein: Feldspat   | Schiefer: tonig: Graphit |  Bifertengrätli-Formation |  Cisuralien     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202170 |Membre lacustre (Fm. du Bifertengrätli) | Sandstein  | Siltstein: schiefrig   | Tonstein |  «Lakustrisches Member» (Bifertengrätli-Fm.) |  Cisuralien     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202171 |Membre estuarien (Fm. du Bifertengrätli) | Konglomerat  | Sandstein   | Tonstein: Anthrazit |  «Estuarisches Member» (Bifertengrätli-Fm.) |  Cisuralien     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202172 |Conglomérat basal (Fm. du Bifertengrätli) | Konglomerat  | –   | – |  «Basales Konglomerat» (Bifertengrätli-Fm.) |  Cisuralien     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202173 |Membre volcanique (Fm. du Bifertengrätli) | Konglomerat  | Sandstein: Quarz   | Tuffit |  Grünhorn-Member |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202174 |Formation du Diechtergletscher | Schiefer: tonig  | Gestein: pyroklastisch   | – |  Diechtergletscher-Formation |  Cisuralien     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202175 |Formation de la Tscharren | Ignimbrit  | Tuffit   | Konglomerat |  Tscharren-Formation |  Cisuralien     | Pennsylvanien tardif   | Spät- bis postvariszisches Grundgebirge  |
|15202177 |Groupe du Fruttstock | Gestein: plutonisch  | –   | – |  – |  Pennsylvanien moyen     | Pennsylvanien moyen   | Mittelvariszisches Grundgebirge  |
|15202178 |Granite de la Brunni | Granit  | –   | – |  Brunni-Granit |  Pennsylvanien moyen     | Pennsylvanien moyen   | Mittelvariszisches Grundgebirge  |
|15202179 |Diorite du Düssi | Diorit  | Aplit   | Pegmatit |  Düssi-Diorit |  Pennsylvanien moyen     | Pennsylvanien moyen   | Mittelvariszisches Grundgebirge  |
|15202180 |Granite du Munt Dado | Granit  | –   | – |  Munt-Dado-Granit |  Pennsylvanien moyen     | Pennsylvanien moyen   | Mittelvariszisches Grundgebirge  |
|15202181 |Diorite de Russein | Diorit  | –   | – |  Russein-Diorit |  Pennsylvanien moyen     | Pennsylvanien précoce   | Frühvariszisches Grundgebirge  |
|15202182 |Granite de la Voralp | Granit: Biotit  | –   | – |  Voralp-Granit |  Pennsylvanien     | Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202183 |Groupe du Rötifirn | Gestein: plutonisch  | –   | – |  – |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15202184 |Granite de Punteglias | Granit: porphyrisch: Hornblende  | –   | – |  Punteglias-Granit |  Mississippien moyen     | Mississippien moyen   | Prävariszisches Grundgebirge  |
|15202185 |Granite du Tödi | Granit  | Granit: Hornblende   | – |  Tödi-Granit |  Mississippien moyen     | Mississippien moyen   | Frühvariszisches Grundgebirge  |
|15202186 |Granite du (Val) Strem | Granit  | Granit: mylonitisch   | – |  Strem-Granit |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202187 |Granodiorite de Baltschieder | Granodiorit  | –   | – |  Baltschieder-Granodiorit |  Mississippien     | Mississippien   | Prävariszisches Grundgebirge  |
|15202188 |Syénite du (Piz) Giuv | Syenit: porphyrisch: Quarz  | Monzonit: porphyrisch: Quarz   | – |  Giuv-Syenit |  Mississippien moyen     | Mississippien moyen   | Frühvariszisches Grundgebirge  |
|15202189 |Monzodiorite du (Piz) Curtin | Monzonit: Quarz  | Syenit: Quarz   | – |  Curtin-Monzodiorit |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15202190 |Syénite du Bristenstock | Syenit: Quarz-Hornblende  | –   | – |  Bristenstock-Syenit |  Mississippien moyen     | Mississippien moyen   | Mittelvariszisches Grundgebirge  |
|15202191 |Groupe de Cavardiras | Gestein: sedimentär  | –   | – |  – |  Mississippien     | Paléozoïque   | Frühvariszisches Grundgebirge  |
|15202192 |Formation du Val Gliems | Ignimbrit  | Tuffit   | Konglomerat |  Val-Gliems-Formation |  Mississippien     | Paléozoïque   | Frühvariszisches Grundgebirge  |
|15202193 |Formation du Bifertenfirn | Schiefer: tonig: Anthrazit  | Gneis   | – |  Bifertenfirn-Formation |  Mississippien     | Paléozoïque   | Frühvariszisches Grundgebirge  |
|15202194 |Socle métamorphique polycyclique anté-varisque du massif de l&#39;Aar | Gneis  | Schiefer   | – |  – |  Dévonien     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202195 |Migmatite d&#39;Innertkirchen | Migmatit: Cordierit  | Gneis: migmatitisch   | Amphibolit |  Innertkirchen-Migmatit |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202196 |Gneiss du Zäsenberg | Gneis  | –   | – |  Zäsenberg-Gneis |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202197 |Complexe gneissique d&#39;Erstfeld | Gneis: migmatitisch  | Gneis: granitisch   | Schiefer |  Erstfeld-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202198 |Complexe gneissique de Guttannen | Gneis: migmatitisch  | Migmatit   | Granofels: Kalksilikat |  Guttannen-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202199 |Complexe gneissique du Straligenstöckli | Granit: porphyrisch: Biotit  | Granodiorit: aplitisch   | – |  Straligenstöckli-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202200 |Complexe gneissique du Lötschental | Gneis: migmatitisch  | Schiefer: Chlorit   | – |  Lötschental-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202201 |Complexe gneissique de l&#39;Ofenhorn-Stampfhorn | Gneis  | Migmatit   | Schiefer |  Ofenhorn-Stampfhorn-Gneiskomplex |  Carbonifère     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202202 |Granodiorite de Fully | Granodiorit  | Migmatit: Cordierit   | – |  Fully-Granodiorit |  Pennsylvanien     | Pennsylvanien   | Prävariszisches Grundgebirge  |
|15202203 |Rhyodacite de Plex-Aboyeu | Dazit: rhyolithisch  | –   | – |  Plex-Aboyeu-Rhyolith |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202204 |Granite de Vallorcine | Granit: Biotit-Cordierit  | –   | – |  Vallorcine-Granit |  Pennsylvanien     | Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202205 |Mylonite de Miéville | Granit: mylonitisch  | Mylonit   | – |  Miéville-Mylonit |  Pennsylvanien     | Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202206 |Granite des Montées-Pélissiers | Granit  | –   | – |  Montées-Pélissiers-Granit |  Mississippien moyen     | Mississippien moyen   | Frühvariszisches Grundgebirge  |
|15202207 |Granite de Pormenaz | Granit  | –   | – |  Pormenaz-Granit |  Mississippien moyen     | Mississippien moyen   | Frühvariszisches Grundgebirge  |
|15202210 |Micaschistes d&#39;Emosson | Gneis: schiefrig: Biotit  | Schiefer: Glimmer   | Gneis: migmatitisch |  Emosson-Gneiskomplex |  Paléozoïque     | Protérozoïque   | Prävariszisches Grundgebirge  |
|15202211 |Orthogneiss du Luisin | Gneis: granodioritisch  | Granodiorit   | – |  Luisin-Orthogneis |  Ordovicien     | Ordovicien   | Prävariszisches Grundgebirge  |
|15202212 |Complexe gneissique du Val Bérard | Gneis: magmatisch  | –   | – |  Val-Bérard-Gneiskomplex |  Ordovicien     | Ordovicien   | Prävariszisches Grundgebirge  |
|15202213 |Éclogite du Lac Cornu | Eklogit  | –   | – |  Lac-Cornu-Eklogit |  Ordovicien     | Ordovicien   | Prävariszisches Grundgebirge  |
|15202214 |Orthogneiss des Perrons | Gneis: granodioritisch  | Granodiorit   | – |  Perrons-Orthogneis |  Ordovicien     | Ordovicien   | Prävariszisches Grundgebirge  |
|15202215 |Rhyolithe de la Breya | Rhyolith  | –   | – |  Breya-Rhyolith |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202216 |Granite du Mont Blanc | Granit  | –   | – |  Mont-Blanc-Granit |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |

\elandscape






## Annexe  GC_GEOL_MAPPING_UNIT_CD {#gc-geol-mapping-unit-cd}
Unités de cartographie

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15200199 | Hauptrogenstein: Maeandrina-Sch. | Couches à Maeandrina     |
|15200200 | Hauptrogenstein: Gisliflue-Korallenkalk | Calcaire à coraux de la Gisliflue     |
|15200201 | Hauptrogenstein: Untere Acuminata-Sch. | Couches à Acuminata inférieures     |
|15200202 | Klingnau-Fm.: Parkinsoni-Sch. | Couches à Parkinsoni     |
|15200203 | Dewalquei-Kalk | Couches à Pecten dewalquei     |
|15200204 | Brot-Sch. | Couches de Brot     |
|15200205 | Passwang-Fm.: Sissach-Mb.: Comptum-Bk. | Banc à Comptum     |
|15200206 | Klettgau-Fm.: Seebi-Mb. | Membre de Seebi     |
|15200207 | Klettgau-Fm.: Gruhalde-Mb. | Membre de la Gruhalde     |
|15200208 | Klettgau-Fm.: Berlingen-Mb. | Membre de Berlingen     |
|15200209 | Klettgau-Fm.: Gansingen-Mb. | Membre de Gansingen     |
|15200210 | Klettgau-Fm.: Ergolz-Mb. | Membre de l&#39;Ergolz     |
|15200211 | Schinznach-Fm.: Stamberg-Mb.: Kaisten-Bk. | Banc de Kaisten     |
|15200212 | Schinznach-Fm.: Eptingen-Bk. | Banc d&#39;Eptingen     |
|15200213 | Schinznach-Fm.: Dünnlenberg-Bk. | Banc du Dünnlenberg     |
|15200214 | Schinznach-Fm.: Kienberg-Mb.: Saalhof-Bk. | Banc de Saalhof     |
|15200215 | Schinznach-Fm.: Leutschenberg-Mb.: Fützen-Bk. | Banc de Fützen     |
|15200216 | Zeglingen-Fm.: Dolomitzone | Dolomitzone (Fm. de Zeglingen)     |
|15200217 | Weitenau-Fm.: Oberer Schuttfächer | Oberer Schuttfächer (Fm. de Weitenau)     |
|15200218 | Weitenau-Fm.: Playa-Serie | Playa-Serie (Fm. de Weitenau)     |
|15200219 | Weitenau-Fm.: Unterer Schuttfächer | Unterer Schuttfächer (Fm. de Weitenau)     |
|15200220 | Schwarzwald-Massiv: Spät- bis postvariszische Intrusiva | Roches plutoniques tardi- à postvarisques de la Forêt Noire     |
|15200221 | Nordalpines Vorland: Spät- bis postvariszische Sedimente und Vulkanite | Permo-Carbonifère du NW de la Suisse     |
|15200222 | Stockberg-Quarzporphyr | Quarzporphyre du Stockberg     |
|15200223 | Bärhalde-Granit | Granite de la Bärhalde     |
|15200224 | Schluchsee-Granit | Granite du Schluchsee     |
|15200225 | Säckingen-Granit | Granite de Säckingen     |
|15200226 | Weiach-Fm.: Jüngere Flussablagerungen | Jüngere Flussablagerungen (Fm. de Weiach)     |
|15200227 | Weiach-Fm.: Seeablagerungen | Seeablagerungen (Fm. de Weiach)     |
|15200228 | Weiach-Fm.: Ältere Flussablagerungen | Ältere Flussablagerungen (Fm. de Weiach)     |
|15200229 | Weiach-Fm.: Ältere Flussablagerungen: Kohle-Serie | Kohle-Serie (Fm. de Weiach)     |
|15200230 | Schwarzwald-Massiv: Früh- bis mittelvariszische Intrusiva | Roches plutoniques éo-variques de la Forêt Noire     |
|15200231 | Albtal-Granit | Granite de l&#39;Albtal     |
|15200232 | Malsburg-Granit | Granite de Malsburg     |
|15200233 | Blauen-Granit | Granite du Blauen     |
|15200234 | Klemmbach-Granit | Granite du Klemmbach     |
|15200235 | Randgranit | Randgranit     |
|15200236 | Münsterhalden-Granit | Granite des Münsterhalden     |
|15200237 | Schönau-Herrenschwand-Granit | Granite de Schönau-Herrenschwand     |
|15200238 | St.-Blasien-Granit | Granite de St-Blasien     |
|15200239 | Mambach-Granit | Granite de Mambach     |
|15200240 | Lenzkirch-Steina-Granit | Granite de Lenzkirch-Steina     |
|15200241 | Hauenstein-Granit | Granite du Hauenstein     |
|15200242 | Böttstein-Granit | Granite de Böttstein     |
|15200243 | Schwarzwald-Massiv: Früh- bis mittelvariszische Sedimente | Roches sédimentaires et volcaniques anté- à éo-varisques de la Forêt Noire     |
|15200245 | Schwarzwald-Massiv: Prävariszisches polyzyklisches Grundgebirge | Socle polycyclique anté-varisque de la Forêt Noire     |
|15200246 | Schwarzwald-Massiv: Prävariszische Orthogneise | Orthogneiss de la Forêt Noire     |
|15200247 | Todtmoos-Gneiskomplex | Complexe gneissique de Todtmoos-Horbach     |
|15200248 | Murgtal-Gneiskomplex | Complexe gneissique du Murgtal     |
|15200249 | Laufenburg-Gneiskomplex | Complexe gneissique de Laufenburg     |
|15200250 | Schwarzwald-Massiv: Prävariszische Migmatite | Migmatites de la Forêt Noire     |
|15200251 | Wiesen-Wehratal-Gneiskomplex | Complexe du Wiesental-Wehratal     |
|15200252 | Wiesen-Wehratal-Gneiskomplex: Wehratal-Syenit | Syénite du Wehratal     |
|15200253 | Schwarzwald-Massiv: Prävariszische Grüngesteine | Roches vertes de la Forêt Noire     |
|15200254 | Molasse | Molasse     |
|15200255 | OSM (Obere Süsswassermolasse) | Molasse d&#39;eau douce supérieure (OSM)     |
|15200256 | Pfänder-Fm.: Tannenberg-Sch. | Couches de Tannenberg     |
|15200257 | Pfänder-Fm. | Couches du Pfänder     |
|15200258 | Napf-Fm. | Formation du Napf     |
|15200259 | Napf-Fm.: Eimätteli-Mb.: Blapbach-Kohlehorizont | Niveau charbonneux du Blapbach     |
|15200260 | Napf-Fm.: Eimätteli-Mb. | Membre d&#39;Eimätteli     |
|15200261 | Schüpferegg-Nagelfluh | Poudingue de la Schüpferegg     |
|15200262 | OSM-II | OSM-II     |
|15200263 | Hegau-Vulkanite | Roches volcaniques du Hegau     |
|15200264 | Höwenegg-Basalt | Basalte du Hegau     |
|15200265 | Hohenwiel-Phonolith | Phonolite du Hegau     |
|15200266 | Hegau-Tuffit | Tuffite du Hegau     |
|15200267 | Hörnli-Fm.: Hörnligipfel-Nagelfluh | Poudingue du Hörnligipfel     |
|15200268 | Hörnli-Fm.: Hörnligubel-Mergel: Höchegg-Brekzie | Brèche de la Höchegg     |
|15200269 | Hörnli-Fm.: Hörnligubel-Mergel | Marne du Hörnligubel     |
|15200270 | Hörnli-Fm.: Tösswald-Mb. | Couches du Tösswald     |
|15200271 | Öhningen-Fm.: Bischofszell-Bentonit | Bentonite de Bischofszell     |
|15200272 | Hörnli-Fm.: Mergelstein-dominierte Fazies | Zone d&#39;Öhningen de la région du Hörnli     |
|15200273 | Hörnli-Fm.: Krinau-Mb. | Couches de Krinau     |
|15200274 | OSM-II: Glimmersand-Fazies | Formation du Glimmersand     |
|15200275 | Zürich-Fm.: Fellitobel-Süsswasserkalk | Calcaire d&#39;eau douce du Fellitobel     |
|15200276 | Uetliberg-Fm. | Couches de l&#39;Üetliberg     |
|15200277 | Uetliberg-Fm.: Uetliberggipfel-Nagelfluh | Poudingue de l&#39;Üetliberggipfel     |
|15200278 | Uetliberg-Fm.: Uetliberg-Mergel | Poudingue de l&#39;Üetliberg     |
|15200279 | Pfannenstiel-Fm.: Falätschen-Mergel | Marne de la Falätschen     |
|15200280 | Pfannenstiel-Fm. | Couches du Pfannenstiel     |
|15200281 | Zürich-Fm. | Couches de Zürich     |
|15200282 | Zürich-Fm.: Leimbach-Bentonit | Bentonite de Leimbach     |
|15200283 | Zürich-Fm.: Rütschlibach-Riedhof-Süsswasserkalk | Calcaire d&#39;eau douce du Rütschlibach-Riedhof     |
|15200284 | Zürich-Fm.: Winterthur-Bentonit | Bentonite de Winterthur     |
|15200285 | Zürich-Fm.: Aeugstertal-Bentonit | Bentonite de l&#39;Aeugstertal     |
|15200286 | Zürich-Fm.: Äntlisberg-Doldertobel-Süsswasserkalk | Calcaire d&#39;eau douce de l&#39;Äntlisberg-Doldertobel     |
|15200287 | Zürich-Fm.: Wehrenbach-Höckler-Süsswasserkalk | Calcaire d&#39;eau douce du Wehrenbach-Höckler     |
|15200288 | Meilen-Fm.: Küsnacht-Bentonit | Bentonite de Küsnacht     |
|15200289 | Meilen-Fm.: Urdorf-Bentonit | Bentonite d&#39;Urdorf     |
|15200290 | Appenzellergranit-Leitniveau | Niveau repère de l&#39;Appenzellergranit     |
|15200291 | Appenzellergranit-Leitniveau: Abtwil-Konglomerat | Conglomérat d&#39;Abtwil     |
|15200292 | Appenzellergranit-Leitniveau: Hüllistein-Konglomerat | Conglomérat d&#39;Hüllistein     |
|15200293 | Appenzellergranit-Leitniveau: Degersheim-Kalknagelfluh | Conglomérat de Degersheim     |
|15200294 | Appenzellergranit-Leitniveau: Meilen-Kalk | Calcaire de Meilen     |
|15200295 | OSM-I | OSM-I     |
|15200296 | Lichtensteig-Fm. | Formation de Lichtensteig     |
|15200297 | Hörnli-Fm. | Formation du Hörnli     |
|15200298 | Guggershorn-Fm. | Formation du Guggershorn     |
|15200299 | Käpfnach-Fm.: Horgen-Süsswasserkalk | Calcaire d&#39;eau douce de Horgen-Käpfnach     |
|15200300 | OSM-J | OSM-J     |
|15200301 | Bois-de-Raube-Fm. | Formation du Bois de Raube     |
|15200302 | OSM-J: Juranagelfluh | Juranagelfluh (OSM-J)     |
|15200304 | Le-Locle-Fm.: Combe-Girard Mb.: Combe-Girard-Bentonit | Bentonite de la Combe Girard     |
|15200305 | Vermes-Süsswasserkalk | Calcaire d&#39;eau douce de Vermes     |
|15200306 | Crêt-du-Locle-Fm.: Gompholitfazies | Gompholite du Locle     |
|15200307 | OMM (Obere Meeresmolasse) | Molasse marine supérieure (OMM)     |
|15200308 | OMM-II | OMM-II     |
|15200309 | St.-Gallen-Fm. | Formation de St-Gall     |
|15200310 | St.-Gallen-Fm.: Staffelbach-Grobsandstein | Grès grossier de Staffelbach     |
|15200311 | OMM-I | OMM-I     |
|15200312 | Luzern-Fm. | Formation de Lucerne     |
|15200313 | Luzern-Fm.: Safenwil-Muschelsandstein | Grès coquillier de Safenwil     |
|15200314 | USM (Untere Süsswassermolasse) | Molasse d&#39;eau douce inférieure (USM)     |
|15200315 | Höhronen-Nagelfluh | Poudingue des Höhronen     |
|15200316 | Kronberg-Nagelfluh | Poudingue du Kronberg     |
|15200317 | Cornalle-Sandstein | Grès de la Cornalle     |
|15200318 | Mont-Pèlerin-Nagelfluh | Poudingue du Mont Pèlerin     |
|15200319 | Speer-Fm. | Formation du Speer     |
|15200320 | Thun-Fm. | Formation de Thoune     |
|15200321 | Thun-Fm.: Gunten-Quarzitnagelfluh | Poudingue quartzitique de Gunten     |
|15200322 | Rigi-Fm. | Formation du Rigi     |
|15200323 | Rigi-Fm.: Scheidegg-Nagelfluh | Poudingue de la Rigi-Scheidegg     |
|15200324 | Rigi-Fm.: Bunte Rigi-Nagelfluh | Bunte Rigi-Nagelfluh     |
|15200325 | Rigi-Fm.: Radiolaritreiche Nagelfluh | Radiolaritreiche Nagelfluh (Fm. du Rigi)     |
|15200326 | USM-III | USM-III     |
|15200327 | Sommersberg-Nagelfluh | Poudingue du Sommersberg     |
|15200328 | Sommersberg-Nagelfluh: Brendenbach-Mergel | Poudingue du Brendenbach     |
|15200329 | USM-II | USM-II     |
|15200001 | Twannbach-Fm. | Formation du Twannbach     |
|15200002 | Reuchenette-Fm. | Formation de Reuchenette     |
|15200003 | Courgenay-Fm. | Formation de Courgenay     |
|15200004 | Vellerat-Fm. | Formation de Vellerat     |
|15200005 | St-Ursanne-Fm. | Formation de St-Ursanne     |
|15200006 | Bärschwil-Fm. | Formation de Bärschwil     |
|15200007 | Ifenthal-Fm. | Formation d&#39;Ifenthal     |
|15200008 | Hauptrogenstein | Hauptrogenstein     |
|15200009 | Passwang-Fm. | Formation du Passwang     |
|15200010 | Opalinus-Ton | Argile à Opalinus     |
|15200011 | Staffelegg-Fm. | Formation de la Staffelegg     |
|15200012 | Juragebirge: Malm | Malm du Jura     |
|15200013 | Twannbach-Fm.: Vouglans-Mb. | Membre de Vouglans     |
|15200014 | Twannbach-Fm.: Chailley-Mb. | Membre du Chailley     |
|15200015 | Twannbach-Fm.: Oberer Virgula-Mergel | Marnes à Virgula supérieures     |
|15200016 | Reuchenette-Fm.: Chevenez-Mb.: Grenznerineen-Bk. | Banc à Nérinées du sommet     |
|15200017 | Reuchenette-Fm.: Chevenez-Mb.: Cladocoropsis-Kalk | Calcaire à Cladocoropsis     |
|15200018 | Reuchenette-Fm.: Chevenez-Mb.: Unterer Virgula-Mergel | Marnes à Virgula inférieures     |
|15200019 | Reuchenette-Fm.: Courtedoux-Mb. | Membre de Courtedoux     |
|15200020 | Reuchenette-Fm.: Banné-Mb. | Membre du Banné     |
|15200021 | Reuchenette-Fm.: Vabenau-Mb. | Membre de Vabenau     |
|15200022 | Reuchenette-Fm.: Vabenau-Mb.: Creugenat-Sch. | Couches du Creugenat     |
|15200023 | Etiollets-Fm. | Formation des Etiollets     |
|15200024 | Etiollets-Fm.: Complexe récifal | Complexe récifal (Fm. des Etiollets)     |
|15200025 | Etiollets-Fm.: Couvaloup-Mb. | Membre du Couvaloup     |
|15200026 | Courgenay-Fm.: Porrentruy-Mb. | Membre de Porrentruy     |
|15200027 | Courgenay-Fm.: La-May-Mb. | Membre de la May     |
|15200028 | Vellerat-Fm.: Oolithe-Rousse-Mb. | Membre de l&#39;Oolithe rousse     |
|15200029 | Vellerat-Fm.: Bure-Mb. | Membre de Bure     |
|15200030 | Vellerat-Fm.: Hauptmumienbank-Mb. | Membre du Hauptmumienbank (Oolithe nuciforme)     |
|15200031 | Vellerat-Fm.: Röschenz-Mb. | Membre de Röschenz     |
|15200032 | Vellerat-Fm.: Vorbourg-Mb. | Membre du Vorbourg     |
|15200033 | St-Ursanne-Fm.: Tiergarten-Mb. | Membre du Tiergarten     |
|15200034 | St-Ursanne-Fm.: Buix-Mb. | Membre de Buix     |
|15200035 | St-Ursanne-Fm.: Chestel-Mb. | Membre du Chestel     |
|15200036 | St-Ursanne-Fm.: Chestel-Mb.: Caquerelle-Pisolith | Pisolite de la Caquerelle     |
|15200037 | St-Ursanne-Fm.: Grellingen-Mb. | Membre de Grellingen     |
|15200039 | Pichoux-Fm. | Formation du Pichoux     |
|15200040 | Bärschwil-Fm.: Liesberg-Mb. | Membre de Liesberg     |
|15200041 | Bärschwil-Fm.: Sornetan-Mb. | Membre de Sornetan     |
|15200042 | Bärschwil-Fm.: Renggeri-Mb. | Membre à Renggeri     |
|15200043 | Ifenthal-Fm.: Graitery-Mb. | Membre du Graitery     |
|15200044 | Ifenthal-Fm.: Herznach-Mb. | Membre de Herznach     |
|15200045 | Ifenthal-Fm.: Herznach-Mb.: Schellenbrücke-Bk. | Banc du Schellenbrücke     |
|15200046 | Ifenthal-Fm.: Bollement-Mb. | Membre de Bollement     |
|15200047 | Ifenthal-Fm.: Ängistein-Mb. | Membre d&#39;Ängistein     |
|15200048 | Ifenthal-Fm.: Ängistein-Mb.: Unter-Erli-Bk. | Banc d&#39;Unter Erli     |
|15200049 | Ifenthal-Fm.: Bözen-Mb. | Membre de Bözen     |
|15200050 | Ifenthal-Fm.: Saulcy-Mb. | Membre de Saulcy     |
|15200051 | Ifenthal-Fm.: Schelmenloch-Mb. | Membre du Schelmenloch     |
|15200052 | Ifenthal-Fm.: Schelmenloch-Mb.: Anwil-Bk. | Banc d&#39;Anwil     |
|15200053 | Ifenthal-Fm.: Châtillon-Mb. | Membre de Châtillon     |
|15200054 | Ifenthal-Fm.: St-Brais-Mb. | Membre de St-Braix     |
|15200055 | Juragebirge: Dogger | Dogger du Jura     |
|15200056 | Juragebirge: Lias | Lias du Jura     |
|15200057 | Hauptrogenstein: Spatkalk | Spatkalk (Hauptrogenstein)     |
|15200058 | Hauptrogenstein: Pierre-Blanche | Pierre Blanche (Hauptrogenstein)     |
|15200059 | Hauptrogenstein: Movelier-Sch. | Couches de Movelier     |
|15200060 | Hauptrogenstein: Grande Oolithe | Série oolitique supérieure (Grande Oolithe)     |
|15200061 | Hauptrogenstein: Obere Acuminata-Sch. | Couches à Acuminata supérieures     |
|15200062 | Hauptrogenstein: Oolithe Subcompacte | Série oolitique inférieure (Oolithe Subcompacte)     |
|15200063 | Passwang-Fm.: Grenchenberg-Mb. | Membre du Grenchenberg     |
|15200064 | Passwang-Fm.: Rothenfluh-Mb. | Membre de la Rothenfluh     |
|15200065 | Passwang-Fm.: Brüggli-Mb. | Membre de Brüggli     |
|15200066 | Passwang-Fm.: Brüggli-Mb.: Humphriesi-Sch. | Couches à Humphriesi     |
|15200067 | Passwang-Fm.: Waldenburg-Mb. | Membre de Waldenburg     |
|15200068 | Passwang-Fm.: Hirnichopf-Mb. | Membre du Hirnichopf     |
|15200069 | Passwang-Fm.: Hauenstein-Mb. | Membre de Hauenstein     |
|15200070 | Passwang-Fm.: Sissach-Mb. | Membre de Sissach     |
|15200071 | Staffelegg-Fm.: Gross-Wolf-Mb. | Membre du Gross Wolf     |
|15200072 | Staffelegg-Fm.: Gross-Wolf-Mb.: Eriwis-Bk. | Banc d&#39;Eriwis     |
|15200073 | Staffelegg-Fm.: Gross-Wolf-Mb.: Erlimoos-Bk. | Banc d&#39;Erlimoos     |
|15200074 | Staffelegg-Fm.: Gross-Wolf-Mb.: Gipf-Bk. | Banc de Gipf     |
|15200075 | Staffelegg-Fm.: Rietheim-Mb. | Membre de Rietheim     |
|15200076 | Staffelegg-Fm.: Rietheim-Mb.: Unterer Stein | Unterer Stein (Fm. de la Staffelegg)     |
|15200077 | Staffelegg-Fm.: Rickenbach-Mb. | Membre de Rickenbach     |
|15200078 | Staffelegg-Fm.: Rickenbach-Mb.: Müsenegg-Bk. | Banc de la Müsenegg     |
|15200079 | Staffelegg-Fm.: Breitenmatt-Mb. | Membre de Breitenmatt     |
|15200080 | Staffelegg-Fm.: Breitenmatt-Mb.: Trasadingen-Bk. | Banc de Trasadingen     |
|15200081 | Staffelegg-Fm.: Grünschholz-Mb. | Membre du Grünschholz     |
|15200082 | Staffelegg-Fm.: Frick-Mb. | Membre de Frick     |
|15200083 | Staffelegg-Fm.: Mont-Terri-Mb. | Membre du Mont Terri     |
|15200084 | Staffelegg-Fm.: Fasiswald-Mb. | Membre de Fasiswald     |
|15200085 | Staffelegg-Fm.: Weissenstein-Mb. | Membre du Weissenstein     |
|15200086 | Staffelegg-Fm.: Beggingen-Mb. | Membre de Beggingen     |
|15200087 | Staffelegg-Fm.: Beggingen-Mb.: Gächlingen-Bk. | Banc de Gächlingen     |
|15200088 | Staffelegg-Fm.: Beggingen-Mb.: Schleitheim-Bk. | Banc de Schleitheim     |
|15200089 | Staffelegg-Fm.: Schambelen-Mb. | Membre du Schambelen     |
|15200090 | Staffelegg-Fm.: Schambelen-Mb.: Hallau-Bk. | Banc de Hallau     |
|15200091 | Juragebirge: Siderolithikum | Sidérolithique du Jura     |
|15200092 | Gorges-de-l&#39;Orbe- und Vallorbe-Mb. | Formations des Gorges de l&#39;Orbe et de Vallorbe, indifférenciées     |
|15200093 | Rocher-des-Hirondelles-Fm.: Vallorbe-Mb. | Formation de Vallorbe     |
|15200094 | Rocher-des-Hirondelles-Fm.: Rivière-Mb. | Membre de la Rivière     |
|15200096 | Gorges-de-l&#39;Orbe-Fm. | Formation des Gorges de l&#39;Orbe     |
|15200097 | Pierre-Châtel- Vions- und Chambotte-Fm. | Formations de Pierre-Châtel, de Vions et de la Chambotte, indifférenciées     |
|15200098 | Chambotte-Fm. | Formation de la Chambotte     |
|15200099 | Chambotte-Fm.: Guiers-Mb. | Membre du Guiers     |
|15200100 | Vions-Fm. | Formation de Vions     |
|15200101 | Pierre-Châtel-Fm. | Formation de Pierre-Châtel     |
|15200102 | Burghorn-Fm. | Formation du Burghorn     |
|15200103 | Burghorn-Fm.: Wettingen-Mb. | Membre de Wettingen     |
|15200104 | Burghorn-Fm.: Baden-Mb. | Membre de Baden     |
|15200105 | Villigen-Fm. | Formation de Villigen     |
|15200106 | Villigen-Fm.: Wangental-Mb. | Membre du Wangental     |
|15200107 | Villigen-Fm.: Letzi-Mb. | Membre du Letzi     |
|15200108 | Villigen-Fm.: Knollen-Bk. | Knollen-Bank (Fm. de Villigen)     |
|15200109 | Villigen-Fm.: Küssaburg-Mb. | Membre de la Küssaburg     |
|15200110 | Villigen-Fm.: Wangen-Mb. | Membre de Wangen     |
|15200111 | Villigen-Fm.: Hornbuck-Mb. | Membre du Hornbuck     |
|15200112 | Villigen-Fm.: Crenularis-Mb. | Membre à Crenularis     |
|15200113 | Villigen-Fm.: Geissberg-Mb. | Membre du Geissberg     |
|15200114 | Wildegg-Fm. | Formation de Wildegg     |
|15200115 | Wildegg-Fm.: Effingen-Mb. | Membre d&#39;Effingen     |
|15200116 | Wildegg-Fm.: Effingen-Mb.: Gerstenhübel-Bk. | Banc du Gerstenhübel     |
|15200117 | Wildegg-Fm.: Birmenstorf-Mb. | Membre de Birmenstorf     |
|15200118 | Günsberg-Fm. | Formation de Günsberg     |
|15200119 | Günsberg-Fm.: Moutier-Korallenkalk | Calcaire à coraux de Moutier     |
|15200120 | Klingnau-Fm. | Formation de Klingnau     |
|15200121 | Klingnau-Fm.: Knorri-Ton | Argile à Knorri     |
|15200122 | Klingnau-Fm.: Wuerttembergica-Sch. | Couches à Wuerttembergica     |
|15200123 | Klingnau-Fm.: Parkinsoni-Sch.: Subfurcatum-Bk. | Banc à Subfurcatum     |
|15200124 | Klingnau-Fm.: Blagdeni-Sch. | Couches à Blagdeni     |
|15200125 | Juragebirge: Keuper | Groupe du Keuper     |
|15200126 | Klettgau-Fm. | Formation du Klettgau     |
|15200127 | Klettgau-Fm.: Belchen-Mb. | Membre du Belchen     |
|15200128 | Bänkerjoch-Fm. | Formation du Bänkerjoch     |
|15200129 | Juragebirge: Muschelkalk | Groupe du Muschelkalk     |
|15200130 | Schinznach-Fm. | Formation de Schinznach     |
|15200131 | Schinznach-Fm.: Asp-Mb. | Membre d&#39;Asp     |
|15200132 | Schinznach-Fm.: Stamberg-Mb. | Membre du Stamberg     |
|15200133 | Schinznach-Fm.: Liedertswil-Mb. | Membre de Liedertswil     |
|15200134 | Schinznach-Fm.: Kienberg-Mb. | Membre de Kienberg     |
|15200135 | Zeglingen-Fm. | Formation de Zeglingen     |
|15200136 | Zeglingen-Fm.: Obere Sufatzone | Obere Sufatzone (Fm. de Zeglingen)     |
|15200137 | Zeglingen-Fm.: Salzlager | Salzlager (Fm. de Zeglingen)     |
|15200138 | Zeglingen-Fm.: Untere Sulfatzone | Untere Sulfatzone (Fm. de Zeglingen)     |
|15200139 | Kaiseraugst-Fm. | Formation de Kaiseraugst     |
|15200140 | Kaiseraugst-Fm.: Orbicularis-Mergel | Marne à Orbicularis     |
|15200141 | Kaiseraugst-Fm.: Wellenkalk / Wellenmergel | Wellenkalk / Wellenmergel     |
|15200142 | Kaiseraugst-Fm.: Wellendolomit | Wellendolomit     |
|15200143 | Juragebirge: Buntsandstein | Groupe du Buntsandstein     |
|15200144 | Dinkelberg-Fm. | Formation du Dinkelberg     |
|15200145 | Dinkelberg-Fm.: Rötton | Rhötton     |
|15200146 | Dinkelberg-Fm.: Plattensandstein | Plattensandstein (Fm. du Dinkelberg)     |
|15200147 | Dinkelberg-Fm.: Karneolhorizont | Karneol-Horizont (Fm. du Dinkelberg)     |
|15200148 | Narlay-Fm. | Formation de Narlay     |
|15200149 | Perte-du-Rhône-Fm. | Formation de la Perte-du-Rhône     |
|15200150 | Grand-Essert-Fm. | Formation du Grand Essert     |
|15200151 | Grand-Essert-Fm: Neuchâtel-Mb. | Membre de Neuchâtel     |
|15200152 | Grand-Essert-Fm: Hauterive-Mb. | Membre d&#39;Hauterive     |
|15200153 | Vuache-Fm. | Formation du Vuache     |
|15200154 | Vuache-Fm.: Alectryonia-Kalk | Calcaire à Alectyonia rectangularis     |
|15200155 | Vuache-Fm.: Arzier-Mergel | Marne d&#39;Arzier     |
|15200156 | Goldberg-Fm. | Formation du Goldberg     |
|15200157 | Wiesental-Fm. | Formation du Wiesental     |
|15200158 | Weitenau-Fm. | Formation de Weitenau     |
|15200159 | Weiach-Fm. | Formation de Weiach     |
|15200160 | Günsberg- Vellerat- Villigen- Balsthal- und Courgenay-Fm. | Formations de Günsberg, Vellerat, Villigen, Balsthal et Courgenay, indifférenciées     |
|15200161 | Juragebirge: Kreide | Crétacé du Jura     |
|15200162 | Juragebirge: Jura | Jurassique du Jura     |
|15200163 | Juragebirge: Trias | Trias du Jura     |
|15200175 | Siderolithikum: Bohnerzton | Argile à pisolites ferrugineuses     |
|15200176 | Siderolithikum: Boluston | Argile à bolus     |
|15200177 | Siderolithikum: Huppererde | Hupper     |
|15200178 | Hauptrogenstein: Homomyenmergel | Marne à Homomyes     |
|15200179 | Dinkelberg-Fm.: Vogesen-Sandstein | Grès des Vosges     |
|15200180 | Siderolithikum: Quarzsand | Sable siliceux vitrifiable     |
|15200181 | Perte-du-Rhône-Fm.: Mussel-Mb. | Membre de Mussel     |
|15200182 | Perte-du-Rhône-Fm.: Fulie-Mb. | Membre de la Fulie     |
|15200183 | Grand-Essert-Fm: Neuchâtel-Mb.: Uttins-Mergel | Marne des Uttins     |
|15200184 | Grand-Essert-Fm: Hauterive-Mb.: Ecluse-Mergelkalk | Zone marno-calcaire (Fm. du Grand Essert)     |
|15200185 | Vuache-Fm.: Bryozoen-Mergel | Marne à Bryozoaires     |
|15200186 | Twannbach-Fm.: Zuckerkörniger Kalk | Calcaire saccharoïde     |
|15200187 | Reuchenette-Fm.: Chevenez-Mb. | Membre de Chevenez     |
|15200188 | Balsthal-Fm. | Formation de Balsthal     |
|15200189 | Balsthal-Fm.: Verena-Mb. | Membre de Ste-Vérène     |
|15200190 | Balsthal-Fm.: Holzflue-Mb. | Membre de la Holzflue     |
|15200191 | Balsthal-Fm.: Laufen-Mb. | Membre de Laufon     |
|15200192 | Balsthal-Fm.: Olten-Mb. | Membre d&#39;Olten     |
|15200193 | Balsthal-Fm.: Steinibach-Mb. | Membre du Steinibach     |
|15200194 | Vellerat-Fm.: Röschenz-Mb.: Grüne Mumienbank | Grüne Mumienbank     |
|15200195 | Wildegg-Fm.: Effingen-Mb.: Pecten-Bk. | Banc à Pecten (Fm. de Wildegg)     |
|15200196 | Hauptrogenstein: Ferrugineus-Oolith | Oolite à Ferrugineus     |
|15200197 | Hauptrogenstein: Wittnau-Korallenkalk | Calcaire à coraux de Wittnau     |
|15200198 | Hauptrogenstein: Furcil-Mergel | Marne du Furcil     |
|15203329 | Rombach-Fm. | Rombach-Fm.     |
|15203330 | Roffna-Gneis | Roffna-Gneis     |
|15203331 | Roffna-Gneis: Porphyrische Fazies | Roffna-Gneis: Porphyrische Fazies     |
|15203332 | Burgruinen-Gneis | Burgruinen-Gneis     |
|15203333 | Taspegn-Gneis | Taspegn-Gneis     |
|15203334 | Aigremont-Brekzie | Aigremont-Brekzie     |
|15203335 | Sulzgrabe-Fm. | Sulzgrabe-Fm.     |
|15203336 | Brekzien-Decke: Rhät | Brekzien-Decke: Rhät     |
|15203337 | Klippen-Decke: Siderolithischer Dogger | Klippen-Decke: Siderolithischer Dogger     |
|15203338 | St-Triphon-Fm.: Andonces-Mb.: Silex-Niveau | St-Triphon-Fm.: Andonces-Mb.: Silex-Niveau     |
|15203339 | St-Triphon-Fm.: Andonces-Mb.: Mittlere Rauwacke | St-Triphon-Fm.: Andonces-Mb.: Mittlere Rauwacke     |
|15203340 | Timun-Gneiskomplex | Timun-Gneiskomplex     |
|15203341 | Malenco-Serpentinit | Malenco-Serpentinit     |
|15203342 | Forno-Amphibolit | Forno-Amphibolit     |
|15203343 | Muretto-Quarzit | Muretto-Quarzit     |
|15203344 | Biot-Fm.: Colerin-Konglomerat | Biot-Fm.: Colerin-Konglomerat     |
|15203345 | Pierre-Avoi-Melange: Brekzie | Pierre-Avoi-Melange: Brekzie     |
|15203346 | Dréveneuse-Bauxit | Dréveneuse-Bauxit     |
|15203347 | Barrhorn-Einheit: Metabauxit | Barrhorn-Einheit: Metabauxit     |
|15203349 | Terri-Schiefer | Schistes du (Piz) Terri     |
|15203350 | Robiei-Wildflysch | Wildflysch de Robièi     |
|15203351 | Robiei-Wildflysch: Pizzo-Castello-Wildflysch | Wildflysch du Pizzo Castello     |
|15203352 | Robiei-Wildflysch: Tamier-Zött-Wildflysch | Wildflysch de Tamier-Zött     |
|15203353 | Robiei-Wildflysch: Alpe-Tamia-Campo-Wildflysch | Wildflysch de l&#39;Alpe Tamia-Campo     |
|15203354 | Teggiolo-Kalkschiefer | Calcschistes du Teggiolo     |
|15203355 | Teggiolo-Kalkschiefer: Medola-Quarzit | Quartzite du Mèdola     |
|15203356 | Teggiolo-Kalkschiefer: Pianasciom-Kalkschiefer | Calcschiste de Pianasciom     |
|15203357 | Teggiolo-Kalkschiefer: Piano-delle-Creste-Sandstein | Grès du Piano delle Creste     |
|15203358 | Antabia-Gr. | Groupe d&#39;Antabia     |
|15203359 | Vanis-Fm. | Formation des Vanis     |
|15203360 | Sevinera-Marmor | Marbre de Sevinèra     |
|15203361 | Sevinera-Sandstein | Grès de Sevinèra     |
|15203362 | Ri-d&#39;Antabia-Konglomerat | Conglomérat du Ri d&#39;Antabia     |
|15203363 | Lebendun-Komplex: Scisti bruni | Scisti bruni (Lebendun)     |
|15203364 | Lebendun-Komplex: Basaler Gneis | Gneiss basale (Lebendun)     |
|15203365 | Antigorio-Orthogneis | Orthogneiss d&#39;Antigorio     |
|15203366 | Falknis-, Sulzfluh- und Tasna-Decke: Couches Rouges | Couches-Rouges (Falknis, Sulzfluh, Tasna)     |
|15203367 | Piz-Terri-Lunschania: Lagensandkalk | Lagensandkalk     |
|15203368 | Pierre-Avoi-Melange: Quarzschiefer-dominierte Fazies | Série schisto-quartzitique (Pierre Avoi)     |
|15203369 | Pierre-Avoi-Melange: Konglomerat-dominierte Fazies | Série conglomératique (Pierre Avoi)     |
|15203370 | Südegg-Komplex | Compexe de Südegg     |
|15203371 | Punta-Rossa-Komplex | Complexe de la Punta Rossa     |
|15203372 | Ferret-Schiefer | Schistes de Ferret     |
|15203373 | Piz-Terri-Lunschania: Basale Tonschiefer | Schistes basaux du (Piz) Terri     |
|15203374 | Grava-Decke: Kalk- und Tonschiefer | Schistes du Val Lumnezia     |
|15203376 | Piz-Terri-Lunschania: Konglomeratgneis | Konglomeratgneis (Terri)     |
|15203377 | Garzott-Brekzie | Brèche de Garzott     |
|15203378 | Areua-Bruschghorn-Melange | Mélange d&#39;Areua-Bruschghorn     |
|15203379 | Grava-Decke: Albitquarzit | Albitquarzit (Grava)     |
|15203380 | Grava-Decke: Basale Tonschiefer | Basale Tonschiefer (Grava)     |
|15203381 | Aul-Decke: Phengitgneis | Phengitgneis (Grava)     |
|15203382 | Haute-Pointe-Fm. | Formation de la Haute Pointe     |
|15203383 | Brasses-Fm. | Formation des Brasses     |
|15203385 | Macugnaga-Augengneis | Gneiss oeillé de Macugnaga     |
|15203386 | Zone Houillère: Perm | Permien de la Zone Houillère     |
|15203387 | Zone Houillère: Perm: Quarzschiefer | Permien quarzoschisteux de la Zone Houillère     |
|15203388 | Ricard-Rhyolit | Rhyolite de Ricard     |
|15203389 | Zone Houillère: Perm: Konglomerat | Permien conglomératique de la Zone Houillère     |
|15203390 | Printse-Fm.: Sandig-schiefrige Fazies | Série schisto-gréseuse supérieure     |
|15203391 | Printse-Fm.: Tonige Fazies | Série schisteuse moyenne     |
|15203392 | Printse-Fm.: Chandoline-Sandstein | Grès de Chandoline     |
|15203393 | Gälmji-Gneis | Gneiss de Gälmji     |
|15203394 | Scherbadung-Gabbro | Gabbro du Scherbadung     |
|15203395 | Lacerandes-Augengneis | Gneiss oeillé des Lacerandes     |
|15203396 | Mont-Mort-Metapelit | Métapélites du Mont Mort     |
|15203397 | Pierre-Avoi-Melange: Schwarze Schiefer | Schistes noirs (Pierre Avoi)     |
|15203398 | Ferret-Schiefer: La-Dotse-Albitkalk | Calcaire albitisé de la Dotse     |
|15203399 | Ergischhorn-Komplex-Fm.: Ginals-Gneis | Gneiss de Ginals     |
|15203400 | Berisal-Gneiskomplex | Socle cristallin de la nappe de Berisal     |
|15203401 | Berisal-Gneiskomplex: Augengneis | Gneiss oeillé de la nappe de Berisal     |
|15203402 | Ruitor-Gneiskomplex | Socle cristallin de la nappe du Ruitor     |
|15203403 | Corno-Gneis | Gneiss du Corno     |
|15203404 | Unterpenninikum: Trias: Quarzit | Quartzite du Trias nord-pennique     |
|15203405 | Mittelpenninikum: Grundgebirge | Socle cristallin du Briançonnais     |
|15203406 | Mont-Brûlé-Quarzit | Permo-Carbonifère de la nappe du Ruitor     |
|15203407 | Mont-Brûlé-Quarzit: Plan-Palasuit-Konglomerat | Permo-Carbonifère conglomératique de la nappe du Ruitor     |
|15203408 | Oberpenninikum: Metasedimente | Schistes lustrés du Piémontais     |
|15203409 | Tsaté-Decke: Metasedimente | Métasédiments de la nappe du Tsaté     |
|15203410 | Tsaté-Decke: Marmor | Marbre de la nappe du Tsaté     |
|15203411 | Tsaté-Decke: Radiolarit | Métaradiolarite de la nappe du Tsaté     |
|15203412 | Zermatt-Saas-Decke: Metasedimente | Métasédiments de la nappe de Zermatt-Saas     |
|15203413 | Oberpenninikum: Ophiolith | Ophiolite du Piémontais     |
|15203414 | Tsaté-Decke: Ophiolith | Ophiolite de la nappe du Tsaté     |
|15203415 | Mont-des-Ritzes-Metabasalt | Métabasalte du Mont des Ritzes     |
|15203416 | Aiguilles-Rouges-d&#39;Arolla-Metagabbro | Métagabbro des Aiguilles Rouges d&#39;Arolla     |
|15203417 | Torrembey-Brekzie | Brèche de Torrembey     |
|15203418 | Zermatt-Saas-Decke: Marmor | Marbre de la nappe de Zermatt-Saas     |
|15203419 | Zermatt-Saas-Decke: Quarzit | Quartzite de la nappe de Zermatt-Saas     |
|15203420 | Riffelberg-Melange | Mélange du Riffelberg     |
|15203421 | Zermatt-Saas-Decke: Schiefer | Schistes lustrés de la nappe de Zermatt-Saas     |
|15203422 | Zermatt-Saas-Decke: Ophiolith | Ophiolite de la nappe de Zermatt-Saas     |
|15203423 | Pfulwe-Metabasalt | Métabasalte du Pfulwe     |
|15203424 | Antrona-Decke: Ophiolith | Ophiolite de la nappe d&#39;Antrona     |
|15203425 | Ergischhorn-Komplex-Fm.: Böshorn-Gneis | Gneiss du Böshorn     |
|15203426 | Monte-Leone-Decke: Orthogneis | Orthogneiss de la nappe du Monte Leone     |
|15203427 | Monte-Leone-Decke: Leukogneis | Leucogneiss de la nappe du Monte Leone     |
|15203428 | Monte-Leone-Decke: Hyperaugengneis | Hyperaugengneiss de la nappe du Monte Leone     |
|15203429 | Monte-Leone-Decke: Paragneis | Paragneiss de la nappe du Monte Leone     |
|15203430 | Lebendun-Komplex: Arkose | Gneiss du Lebendun, arkosique     |
|15203431 | Lebendun-Komplex: Konglomerat | Gneiss du Lebendun, conglomératique     |
|15203432 | Ruginenta-Decke: Sedimentbedeckung | Série du (Passo) Salarioli     |
|15203433 | Ruginenta-Decke: Grundgebirge | Socle cristallin de la nappe de Ruginenta     |
|15203434 | Ruginenta-Decke: Glimmerschiefer | Schistes de la nappe de Ruginenta     |
|15203435 | Ruginenta-Decke: Paragneis | Paragneiss de la nappe de Ruginenta     |
|15203436 | Preja-Fm. | Formation de la Preja     |
|15203437 | Cavalli-Fm. | Formation des Cavalli     |
|15203438 | Monte-Rosa-Decke: Sedimentbedeckung | Série de Furgg     |
|15203439 | Mezzalama-Granit | Granite de Mezzalama     |
|15203440 | Monte-Rosa-Orthogneis: Grobkörnige Fazies | Orthogneiss du Mont Rose, à grain grossier     |
|15203441 | Rottal-Migmatit | Migmatite du Rottal     |
|15203442 | Monte-Rosa-Orthogneis: Mylonitische Fazies | Orthogneiss du Mont Rose, mylonitique     |
|15203443 | Monte-Rosa-Decke: Paragneis | Paragneiss de la nappe du Mont Rose     |
|15203444 | Monte-Rosa-Decke: Biotitgneis | Gneiss à biotite de la nappe du Mont Rose     |
|15203445 | Monte-Rosa-Decke: Bändergneis | Gneiss rubané de la nappe du Mont Rose     |
|15203446 | Monte-Rosa-Decke: Glimmerschiefer | Micaschiste de la nappe du Mont Rose     |
|15203447 | Portjengrat-Decke: Sedimentbedeckung | Série du Grundberg     |
|15203449 | Portjengrat-Orthogneis | Orthogneiss de la nappe du Protjengrat     |
|15203164 | Oberälpli-Fm. | Formation de l&#39;Oberälpli     |
|15203165 | Eggberg-Fm. | Formation de l&#39;Eggberg     |
|15203166 | Gyrenspitz-Fm. | Formation du Gyrenspitz     |
|15203167 | Fadura-Fm. | Formation de la Fadura     |
|15203168 | Pfävigrat-Fm. | Formation du Pfävigrat     |
|15203169 | Sassauna-Fm. | Formation de la Sassauna     |
|15203170 | Valzeina-Fm. | Formation de Valzeina     |
|15203171 | Klus-Fm. | Formation de la Klus     |
|15203172 | Stätzerhorn-Fm. | Flysch du Tomül     |
|15203173 | Stätzerhorn-Fm.: Basaler Konglomerat | Hauptkonglomerat (Flysch du Tomül)     |
|15203174 | Carnusa-Fm. | Formation du Carnusa(horn)     |
|15203175 | Nolla-Kalkschiefer: Safien-Kalk | Calcaire de Safien     |
|15203176 | Nolla-Kalkschiefer | Calcaire de la Nolla     |
|15203177 | Nolla-Tonschiefer | Argillite de la Nolla     |
|15203178 | Bärenhorn-Fm. | Formation du Bärenhorn     |
|15203179 | Tomül-Decke: Grüngesteine | Roches vertes (Grava/Tomül)     |
|15203180 | Tomül-Decke: Mélange | Mélange du Tomül     |
|15203181 | Touno-Einheit | Série du Tounô     |
|15203182 | Barrhorn-Einheit | Série du Barrhorn     |
|15203183 | Bruneggjoch-Fm. | Formation du Bruneggjoch     |
|15203184 | Bruneggjoch-Fm.: Sous-le-Rocher-Mb. | Membre de Sous le Rocher     |
|15203185 | Randa-Augengneis | Gneiss oeillé de Randa     |
|15201182 | Juraschotter | Juraschotter     |
|15201183 | Alte Doubsschotter | Gravier ancien du Doubs     |
|15201184 | Wutach-Schotter | Gravier de la Wutach     |
|15201185 | Merenbach-Schotter | Gravier du Merenbach     |
|15201186 | Malmkalk-Schotter der Randen-Täler | Malmkalk-Schotter (vallée du Randen)     |
|15201002 | Niederterrasse | Niederterrasse     |
|15201006 | Birrfeld-Eiszeit (Letzte Eiszeit) | Période glaciaire du Birrfeld (Dernière Période glaciaire)     |
|15201008 | LGM-Rückzug | Phase de retrait du LGM     |
|15201187 | Solothurn-Stadium | stade de Soleure     |
|15201129 | Zürich-Stein-Bremgarten-Stadien | stade glaciaire de Zürich-Stein-Bremgarten     |
|15201130 | Untere Singen-Terrasse | terrasse inférieure de Singen     |
|15201131 | Schlieren-Diessenhofen-Stetten-Stadien | stade de Schlieren-Diessenhofen-Stetten     |
|15201132 | Obere Singen-Terrasse | terrasse supérieure de Singen     |
|15201133 | Rheinau-Terrasse | terrasse de Rheinau     |
|15201134 | Nohl-Terrasse | terrasse de Nohl     |
|15201135 | Altenburg-Fulach-Terrasse | terrasse d&#39;Altenburg-Fulach     |
|15201136 | Aare-Schotter | Gravier de l&#39;Aar     |
|15201137 | Schüss-Schotter | Gravier de la Suze     |
|15201138 | Orvin-Schotter | Gravier d&#39;Orvin     |
|15201139 | Seeablagerungen von Frinvillier und Rondchâtel | Dépôts lacustres de Frinvillier et Rondchâtel     |
|15201140 | Stauschotter von Diessbach | Gravier de retenue de Diessbach     |
|15201141 | Mély-Formation | Formation de Mély     |
|15201007 | Last Glacial Maximum (LGM), undiff. | Dernier Maximum Glaciaire (LGM), indifférencié     |
|15201142 | Kiessande von Madretsch | Sable à gravier de Madretsch     |
|15201143 | Seeland-Schotter | Gravier du Seeland     |
|15201144 | Emme-Schotter | Gravier de l&#39;Emme     |
|15201145 | Gäu-Schotter | Gravier du Gäu     |
|15201146 | Flumenthal-Lehm | Limon du Flumenthal     |
|15201147 | Killwangen-Schaffhausen-Mellingen-Stadium | stade de Killwangen-Schaffhouse-Mellingen     |
|15201148 | Munot-Terrasse | terrasse du Munot     |
|15201149 | Stokar-Terrasse | terrasse de Stokar     |
|15201150 | Breite-Terrasse | terrasse de la Breite     |
|15201151 | Maximalstand (Kilwangen-Schaffhausen-Stadium) | stade maximal (Kilwangen-Schaffhouse)     |
|15201009 | Birmenstorf-Vergletscherung (2. LGM-Vorstoss) | Glaciation de Birmenstorf     |
|15201010 | Wettingen-Vorstoss | Avancée glaciaire de Wettingen     |
|15201011 | Flüefeld-Schotter | Gravier du Flüefeld     |
|15201012 | Altberg-Till | Till de l&#39;Altberg     |
|15203186 | Col-de-Chassoure-Fm. | Formation du Col de Chassoure     |
|15203187 | Col-de-Chassoure-Fm.: Gouille-Verte-Mb. | Membre de la Gouille Verte     |
|15203188 | Col-de-Chassoure-Fm.: Matse-Mb. | Membre de la Matse     |
|15203189 | Col-de-Chassoure-Fm.: Dent-de-Nendaz-Mb. | Membre de la Dent de Nendaz     |
|15203190 | Col-de-Chassoure-Fm.: Goli-d&#39;Aget-Mb. | Membre du Goli d&#39;Aget     |
|15203191 | Col-de-Chassoure-Fm.: Mondra-Mb. | Membre de la Mondra     |
|15203192 | Col-de-Chassoure-Fm.: Cleuson-Mb. | Membre de Cleuson     |
|15203193 | Métailler-Fm. | Formation du Métailler     |
|15203194 | Distulberg-Fm. | Formation du Distulberg     |
|15203195 | Thyon-Metagranophyr | Métagranophyre de Thyon     |
|15203196 | Mont-Rogneux-Metagranit | Métagranite du Mont Rogneux     |
|15203197 | Lirec-Fm. undiff | Formation de Lirec     |
|15203198 | Adlerflüe-Fm. | Formation de l&#39;Adlerflüe     |
|15203199 | Ergischhorn-Komplex | Complexe de l&#39;Ergischhorn     |
|15203200 | Gelbhorn-Flysch | Flysch du Gelbhorn     |
|15203201 | Obrist-Fm. | Groupe de l&#39;Obrist     |
|15203202 | Vizan-Brekzie | Brèche du Vizan     |
|15203203 | Tschera-Marmor | Marbre de la Tschera     |
|15203204 | Tschera-Marmor: Wissberg-Brekzie | Brèche du Wissberg     |
|15203205 | Nisellas-Fm. | Groupe de Nisellas     |
|15201013 | Birmenstorf-Vorstoss | Avancée glaciaire de Birmenstorf     |
|15201014 | Birr-Schotter | Gravier de Birr     |
|15201015 | Oberhard-Till | Till d&#39;Oberhard     |
|15201152 | Wehntal-Schotter | Gravier du Wehntal     |
|15201016 | Seon-Vorstoss | Avancée glaciaire de Seon     |
|15201017 | Berg-Schotter | Gravier de Berg     |
|15201018 | Fornholz-Till | Till de Fornholz     |
|15201153 | Bick-Till | Till du Bick(acher)     |
|15201154 | Flüe-Till | Till de Flüe     |
|15201155 | Wettingen-Schotter | Gravier de Wettingen     |
|15201019 | Gontenschwil-Vorstoss | Avancée glaciaire de Gontenschwil     |
|15201020 | Gontenschwil-Till | Till de Gontenschwil     |
|15201021 | Staffelbach-Vorstoss | Avancée glaciaire de Staffelbach     |
|15201022 | Staffelbach-Schotter | Gravier de Staffelbach     |
|15201023 | Staffelbach-Till | Till de Staffelbach     |
|15201024 | Lindmühle-Vergletscherung (1. LGM-Vorstoss) | Glaciation de Lindmühle     |
|15201025 | Otelfingen-Vorstoss | Avancée glaciaire d&#39;Otelfingen     |
|15201026 | Tägerhard-Schotter | Gravier de Tägerhard     |
|15201027 | Lindmühle-Vorstoss | Avancée glaciaire du Lindmühle     |
|15201028 | Ämmert-Schotter | Gravier d&#39;Ämmert     |
|15201029 | Ämmert-Till | Till d&#39;Ämmert     |
|15201030 | Emmet-Vorstoss | Avancée glaciaire d&#39;Emmet     |
|15201031 | Gündelmoos-Lehm | Limon de Gündelmoos     |
|15201032 | Igliste-Schotter | Gravier d&#39;Igliste     |
|15201033 | Niderholz-Till | Till du Niderholz     |
|15201034 | Zetzwil-Vorstoss | Avancée glaciaire de Zetzwil     |
|15201035 | Zetzwil-Till | Till de Zetzwil     |
|15201036 | Kirchleerau-Vorstoss | Avancée glaciaire de Kirchleerau     |
|15201037 | Kirchleerau-Till | Till de Kirchleerau     |
|15201038 | Gossau-Interstadial | Interstade de Gossau     |
|15201039 | Mülligen-Paläoboden | Paléosol de Mülligen     |
|15201040 | Niederweningen-Formation | Formation de Niederweningen     |
|15201041 | Hombrechtikon-Vergletscherung (Frühletzteiszeitliche Vergl.) | Glaciation de Hombrechtikon     |
|15201042 | Mülligen-Schotter | Gravier de Mülligen     |
|15201043 | 2. letzteiszeitlischs Vorstoss | 2ème avancée glaciaire de la Dernière Période glaciaire     |
|15201044 | 1. letzteiszeitlischs Vorstoss | 1ère avancée glaciaire de la Dernière Période glaciaire     |
|15201001 | Ältere Ablagerungen, undifferenziert | Dépôts indifférenciés précédant le Dernier Maximum Glaciaire     |
|15201156 | Bersturzmasse von Selzach | Dépôt d&#39;écroulement de Selzach     |
|15203206 | Tumpriv-Fm. | Groupe de la Tumpriv     |
|15203207 | Kalkberg-Fm. | Groupe du Kalkberg     |
|15203208 | Bavugls-Fm. | Groupe de Bavugls     |
|15203209 | Nolla-Kristallin | Socle cristallin du Nolla     |
|15203210 | Falknis-Decke: Flysch | Flysch de la nappe du Falknis     |
|15203211 | Globorotalien-Sch. | Globorotalien-Schichten     |
|15203212 | Quarzsandstein-Flysch | Quarzsandstein-Flysch (Gault)     |
|15203213 | Tristel-Fm. | Formation de Tristel     |
|15203214 | Fleckenkalk-Flysch | Fleckenkalk-Flysch (Neokom)     |
|15203215 | Jes-Fm. | Formation de la Jes     |
|15203216 | Falknis-Brekzie | Brèche du Falknis     |
|15203217 | Sanalada-Fm. | Formation de Sanalada     |
|15203218 | Panier-Fm. | Formation de Panier     |
|15203219 | Sulzfluh-Decke: Flysch | Flysch de la nappe de la Suzfluh     |
|15203220 | Sulzfluh-Kalk | Calcaire de la Sulzfluh     |
|15203221 | Sulzfluh-Decke: Granit | Granite de la nappe de la Suzfluh     |
|15203222 | Tasna-Decke: Flysch | Flysch de la nappe de la Tasna     |
|15203223 | Steinsberg-Kalk | Calcaire du Steinsberg     |
|15203224 | Plattamala-Granit | Granite de la nappe de la Tasna     |
|15203225 | Série Rousse | Série Rousse     |
|15203226 | Série Grise | Série Grise     |
|15203227 | Garda-Bordon-Fm. | Série de la Garde de Bordon     |
|15203228 | Fêta-d&#39;Août-Fm. | Flysch de la Fêta d&#39;Août     |
|15203229 | Allalin-Metagabbro | Gabbro de l&#39;Allalin     |
|15203230 | Arosa-Decke: Melange | Mélange d&#39;Arosa     |
|15203231 | Verspala-Fm. | Formation de la Verspala     |
|15203232 | Lavagna-Fm. | Formation de Lavagna     |
|15203233 | Palombini-Fm. | Formation à Palombini     |
|15203234 | Arosa-Decke: Calpionellenkalk | Calcaire à Calpionelles de la zone d&#39;Arosa     |
|15203235 | Arosa-Decke: Radiolarit | Radiolarite de la zone d&#39;Arosa     |
|15203236 | Arosa-Decke: Ophiolith | Ophiolite de la zone d&#39;Arosa     |
|15203238 | Coulaytes-Melange: Buufal-Konglomerat | Conglomérat de Buufal     |
|15203239 | Sommant-Fm.: Langel-Mb. | Membre de Langel     |
|15203240 | Pralet-Fm.: Obere Rauwacke | Cornieule Supérieure     |
|15203241 | Clôt-la-Cime-Fm.: Gips | Gypse de la nappe des Préalpes Médianes     |
|15203242 | Brekzien-Decke: Couches-Rouges | Couches Rouges de la nappe de la Brèche     |
|15203243 | Brekzien-Decke: Trias: Rauwacke | Cornieule de la nappe de la Brèche     |
|15203244 | Manche-Fm.: Lamperehubel-Sandstein | Grès du Lamperehubel     |
|15203245 | Perrières-Fm.: Gets-Ophiolith | Ophiolite des Gets     |
|15203246 | Piz-Terri-Lunschania: Obere Kalk- und Tonschiefer | Obere Kalk- und Tonschiefer (Grava/Tomül)     |
|15203247 | Piz-Terri-Lunschania: Gneisquarzit | Quarzit und quarzitische Schiefer (Grava/Tomül)     |
|15203248 | Piz-Terri-Lunschania: Untere Kalk- und Tonschiefer | Untere Kalk- und Tonschiefer (Grava/Tomül)     |
|15203249 | Aul-Marmor | Marbre du Piz Aul     |
|15203250 | Piz-Terri-Lunschania: Dolomitbrekzie | Brèche (Grava/Tomül)     |
|15203251 | Grava-Decke: Gryphäenkalk | Gryphäenkalk     |
|15203252 | Unterpenninikum: Trias | Trias nord-pennique     |
|15203253 | Zervreila-Granitgneis | Orthogneiss de Zervreila     |
|15203254 | Garenstock-Augengneis | Gneiss oeillé du Garenstock     |
|15203255 | Salahorn-Fm.: Glimmerschiefer und Paragneis | Adula-D.: Glimmerschiefer und Paragneis     |
|15203256 | Adula-Decke: Amphibolit | Adula-D.: Amphibolit     |
|15203257 | Zone Submédiane: Melange | Mélange Submédian     |
|15203258 | Zone Submédiane: Truche-Brekzie | Brèche de la Truche     |
|15203259 | Zone Submédiane: Trom-Brekzie | Brèche de Trom     |
|15203260 | Zone Submédiane: Exergillod-Brekzie | Brèche d&#39;Exergillod     |
|15203261 | Zone Submédiane: Troublon-Kalk | Calcaire du Troublon     |
|15203262 | Zone Submédiane: Zünegg-Knollenkalk | Calcaire noduleux de la Zünegg     |
|15203263 | Zone Submédiane: Hauta-Crêtaz-Fm. | Formation de Hauta-Crêtaz     |
|15203264 | Zone Submédiane: Pointe-de-l&#39;Au-Brekzie | Brèche de la Pointe de l&#39;Au     |
|15203265 | Zone Submédiane: Bonaveau-Kalk | Calcaire de Bonaveau     |
|15203266 | Zone Submédiane: Sex-du-Tronc-Kalk | Calcaire du Sex du Tronc     |
|15203267 | Zone Submédiane: Grand-Herba-Kalk | Calcaire du Sex de Grand-Herba     |
|15203268 | Oudiou-Fm. | Formation d&#39;Oudiou     |
|15203269 | Klippen-Decke: Malm | Malm de la nappe des Préalpes Médianes     |
|15203270 | Moléson-Fm.: Albeuve-Serie | Série d&#39;Albeuve     |
|15203271 | Sciernes-d&#39;Albeuve-Fm.: Kummli-Sch. | Couches de la Kummli     |
|15203272 | Klippen-Decke: Dogger | Dogger de la nappe des Préalpes Médianes     |
|15203273 | Mytilus-Sch.: Col-de-Cordon-Mb.: Stockenflue-Kalk | Calcaire de la Stockenflue     |
|15203274 | Sommant-Fm.: Mieussy-Mb. | Membre de Mieussy     |
|15203275 | Klippen-Decke: Lias | Lias de la nappe des Préalpes Médianes     |
|15203276 | Klippen-Decke: Trias | Trias de la nappe des Préalpes Médianes     |
|15203277 | Pralet-Fm. | Formation du Pralet     |
|15203278 | Pralet-Fm.: Balmi-Mb. | Membre du Balmi     |
|15203279 | Wiriehorn-Fm.: Bodeflue-Mb. | Membre de la Bodeflue     |
|15203280 | Wiriehorn-Fm.: Wildgrimmi-Mb. | Membre du Wildgrimmi     |
|15203281 | St-Triphon-Fm.: Dorchaux-Mb.: Untere Rauwacke | Cornieule Inférieure     |
|15203282 | Infrabrèche-Melange | Mélange infra-brèche     |
|15203283 | Wägital-Decke: Flysch | Flysch du Wägital     |
|15203284 | Gurnigel-Decke: Flysch-5 | Flysch 5 à microconglomérats siliceux     |
|15203285 | Voirons-Decke: Flysch | Flysch des Voirons     |
|15203286 | Boëge-Mergel | Marne de Boëge     |
|15203287 | Vouan-Konglomerat | Conglomérat du Vouan     |
|15203288 | Voirons-Sandstein | Grès des Voirons     |
|15203291 | Klippen-Decke: Couches-Rouges | Couches Rouges de la nappe des Préalpes Médianes, indifférenciées     |
|15203292 | Simmen-Decke: Flysch | Flysch de la Simme, indifférencié     |
|15203293 | Trepsen-Flysch | Flysch de Trepsen     |
|15203294 | Cocco-Gneis | Cocco-Gneis     |
|15203295 | Verzasca-Gneis | Verzasca-Gneis     |
|15203296 | Vogorno-Gneis | Vogorno-Gneis     |
|15203297 | Ruscada-Gneis | Ruscada-Gneis     |
|15203298 | Mergoscia-Gneis | Mergoscia-Gneis     |
|15203299 | Monte-Rosa-Orthogneis | Monte-Rosa-Orthogneis     |
|15203300 | Arblatsch-Flysch | Arblatsch-Flysch     |
|15203301 | Arblatsch-Flysch: Sandstein-dominierte Fazies | Arblatsch-Flysch: Sandstein-dominierte Fazies     |
|15203302 | Arblatsch-Flysch: Konglomerat-dominierte Fazies | Arblatsch-Flysch: Konglomerat-dominierte Fazies     |
|15203303 | Spegnas-Fm. | Spegnas-Fm.     |
|15203304 | Rudnal-Fm. | Rudnal-Fm.     |
|15203305 | Savognin-Fm. | Savognin-Fm.     |
|15201181 | Rhein- und Aareschotter | Gravier du Rhin et de l&#39;Aar     |
|15203306 | Stätzerhorn-Fm.: Bleis-Pintgas-Mb. | Stätzerhorn-Fm.: Bleis-Pintgas-Mb.     |
|15203307 | Stätzerhorn-Fm.: Parnegl-Mb. | Stätzerhorn-Fm.: Parnegl-Mb.     |
|15203308 | Stätzerhorn-Fm.: Danis-Mb. | Stätzerhorn-Fm.: Danis-Mb.     |
|15203309 | Stätzerhorn-Fm.: Raschil-Mb. | Stätzerhorn-Fm.: Raschil-Mb.     |
|15203310 | Bruneggjoch-Fm.: Embd-Mb. | Bruneggjoch-Fm.: Embd-Mb.     |
|15203311 | Randa-Augengneis: Bonigersee-Augengneis | Randa-Augengneis: Bonigersee-Augengneis     |
|15203312 | Törbel-Gneis | Törbel-Gneis     |
|15203313 | Lodano-Gneis | Lodano-Gneis     |
|15203314 | Vergeletto-Gneis | Vergeletto-Gneis     |
|15203315 | Cortascia-Gneis | Cortascia-Gneis     |
|15203316 | Forcoletta-Gneis | Forcoletta-Gneis     |
|15203317 | Matorello-Gneis | Matorello-Gneis     |
|15203318 | Lebendun-Komplex | Complexe gneissique du Lebendun     |
|15203319 | Sabbione-Sandstein | Sabbione-Sandstein     |
|15203320 | Monte-Leone-Decke: Grundgebirge | Socle cristallin de la nappe du Monte Leone     |
|15203321 | Ganter-Gneis | Ganter-Gneis     |
|15203322 | Ritter-Gneis | Ritter-Gneis     |
|15203323 | Geisspfad-Serpentinit | Geisspfad-Serpentinit     |
|15203325 | Holzerspitz-Kalkschiefer | Calcschistes de l&#39;Holzerspitz     |
|15203327 | Rinderbach-Fm. | Rinderbach-Fm.     |
|15203328 | Langenegg-Fm. | Langenegg-Fm.     |
|15201536 | Niederterrassenschotter, oberste Terrasse | Niederterrasse, premier niveau graveleux le plus élevé     |
|15201537 | Tiefere Deckenschotter, unteres Niveau | Tiefere Deckenschotter, niveau inférieur     |
|15201538 | Tiefere Deckenschotter, oberes Niveau | Tiefere Deckenschotter, niveau supérieur     |
|15201539 | Kunkels-Formation | Formation de Kunkels     |
|15201540 | Alluvion von Ransun | Alluvion de Ransun     |
|15201541 | Rüdlingen-Till | Till de Rüdlingen     |
|15201542 | Niklaushalden-Formation | Formation de Niklaushalden     |
|15201556 | Saxegrabe-Schotter | Gravier du Saxegrabe     |
|15201557 | Zweidlen-Schotter | Gravier de Zweidlen     |
|15201558 | Burgacher-Schotter | Gravier de Burgacher     |
|15201559 | Chatzenstig-Schotter | Gravier du Chatzenstig     |
|15201560 | Wasterkingen-Schotter | Gravier de Wasterkingen     |
|15203563 | Zentralschweizerische Klippen: Couches-Rouges | Couches-Rouges de klippes de Suisse centrale     |
|15203564 | Wägital-Flysch: Oberer Teil (Paläogen) | Flysch du Wägital: partie supérieure (Paléogène)     |
|15203565 | Wägital-Flysch: Unterer Teil (Kreide) | Flysch du Wägital: partie inférieure (Crétacé)     |
|15203566 | Wägital-Flysch: Basaler tektonisierter Teil | Flysch du Wägital: partie basale, tectonisée     |
|15203567 | Gibel- und Griggeli-Fm. | Formations de Gibel et de Griggeli     |
|15203568 | Mittelpenninikum: Trias: Dolomit | Dolomie des Préalpes Médianes     |
|15203569 | Mittelpenninikum: Trias: Dolomit und Kalk | Dolomie et calcaire des Préalpes Médianes     |
|15203570 | Mittelpenninikum: Trias: Dolomit und Rauwacke | Dolomie schisteuse et cornieule des Préalpes Médianes     |
|15203571 | Mittelpenninikum: Trias: Rauwacke | Cornieule des Préalpes Médianes     |
|15203572 | Mittelpenninikum: Trias: Gipsmergel und Sandstein | Marne gypseuse et grès des Préalpes Médianes     |
|15203573 | Schlieren-Sandstein: Im Paläogen tektonisch überprägt | Grès des Schlieren, tectonisé au Paléogène     |
|15203574 | Leimern-Sch. | Couches de la Leimern     |
|15203575 | Mittelpenninikum: Trias: Rauwacke und Sandstein | Cornieule et grès quartzitique des Préalpes Médianes (Trias basal)     |
|15203576 | Guber- Schoni- und Schlieren-Sandstein | Flysch des Schlieren: masse principale (Paléogène)     |
|15203577 | Zentralschweizerische Klippen: Mittellias | Lias moyen des Préalpes     |
|15203579 | Nolla-Tonschiefer: Quarzsandstein | Schistes argileux de la Nolla: grès quartzitique     |
|15204026 | Kössen-Fm.: Mitgel-Mb. | Membre du (Piz) Mitgel     |
|15204027 | Kössen-Fm.: Ramoz-Mb. | Membre de Ramoz     |
|15204028 | Kössen-Fm.: Schesaplana-Mb. | Membre du Schesaplana     |
|15204029 | Kössen-Fm.: Alplihorn-Mb. | Membre de l&#39;Alplihorn     |
|15204030 | Ostalpin: Hauptdolomit-Gr. | Hauptdolomit-Gruppe     |
|15204031 | Murtèr-Plattenkalk | Calcaire plaqueté du (Piz) Murtèr     |
|15204032 | Murteret-Dolomit | Dolomie du Murteret     |
|15204033 | Diavel-Fm. | Formation du (Piz dal) Diavel     |
|15204034 | Quattervals-Fm. | Formation du (Piz) Quattervals     |
|15204035 | Quattervals-Fm.: Crappa-Mala-Mb. | Marne de la Crappa Mala     |
|15204036 | Quattervals-Fm.: Pra-Grata-Mb. | Membre de Pra Grata     |
|15204037 | Müschauns-Dolomit | Dolomie du (Val) Müschauns     |
|15204038 | Ostalpin: Raibl-Gr. | Groupe de Raibl     |
|15204039 | Fanez-Fm. | Formation de Fanez     |
|15204040 | Fanez-Fm.: Valbella-Mb. | Membre de la Valbella     |
|15204041 | Fanez-Fm.: Dolomit | Dolomie de Fanez     |
|15204042 | Fanez-Fm.: Mezdi-Mb. | Membre du (Piz) Mezdi     |
|15204043 | Fanez-Fm.: Cluozza-Mb. | Membre du Val Cluozza     |
|15204044 | Fanez-Fm.: Stugl-Gips | Membre de Stugl     |
|15204045 | Minger-Fm. | Formation du Val Mingèr     |
|15204046 | Minger-Fm.: Dolomit | Dolomie du Val Mingèr     |
|15204047 | Mingèr-Fm.: Mora-Mb. | Membre du Val Mora     |
|15201562 | Tubeschwanz-Schotter | Gravier de Tubeschwanz     |
|15201563 | Weisweil-Schotter | Gravier de Weisweil     |
|15201561 | Paradiesgärtli-Schotter | Gravier du Paradiesgärtli     |
|15201565 | Stetten-Schotter | Gravier de Stetten     |
|15201544 | Volken-Lehm | Limon de Volken     |
|15201549 | Weiach-Schotter | Gravier de Weiach     |
|15201545 | Rheinau-Till | Till de Rheinau     |
|15201546 | Ellikerholz-Formation | Formation de l&#39;Ellikerholz     |
|15201547 | Eggholz-Formation | Formation de l&#39;Eggholz     |
|15201548 | Bannhalden-Schotter | Gravier de Bannhalden     |
|15201550 | Balm-Schotter | Gravier de Balm     |
|15201551 | Windlach-Till | Till de Windlach     |
|15201552 | Südranden-Till | Gravier du Südranden     |
|15201553 | Schlossbuck-Schotter | Gravier de Schlossbuck     |
|15201554 | Risibüel-Schotter | Gravier de Risibüel     |
|15201555 | Schmerlet- und Toktri-Formation, undifferenziert | Formations de Schmerlet et Toktri, indifférenciées     |
|15201534 | Niederterrassenschotter, tiefere Niveaus | Niederterrasse, niveaux graveleux inférieurs     |
|15201564 | Hasli-Formation | Formation de Hasli     |
|15201532 | Bergsturzablagerung von Bargis | dépôt d&#39;éboulement de Bargis     |
|15201533 | Bergsturzablagerung von Fidaz | dépôt d&#39;éboulement de Fidaz     |
|15201543 | Stadel-Till | Till de Stadel     |
|15201535 | Niederterrassenschotter, zweitoberste Terrasse | Niederterrasse, deuxième niveau graveleux le plus élevé     |
|15206026 | Undifferenzierte stratigraphische Einheit: Dogger | Dogger, indifférencié     |
|15206027 | Undifferenzierte stratigraphische Einheit: Malm | Malm, indifférencié     |
|15206028 | Undifferenzierte stratigraphische Einheit: Kreide | Crétacé, indifférencié     |
|15206029 | Undifferenzierte stratigraphische Einheit: Trias | Trias, indifférencié     |
|15206030 | Undifferenzierte lithologische Einheit: Sedimentgestein | roche sédimentaire, indifférenciée     |
|15206031 | Undifferenzierte lithologische Einheit: Kristallingestein | roche cristalline, indifférenciée     |
|15206032 | Undifferenzierte lithologische Einheit: Granit | granite, indifférencié     |
|15206033 | Undifferenzierte stratigraphische Einheit | unité stratigraphique indifférenciée     |
|15206034 | Undifferenzierte stratigraphische Einheit: Mesozoikum | Mésozoïque, indifférencié     |
|15206035 | Undifferenzierte lithologische Einheit: Rhyolith | rhyolite, indifférenciée     |
|15206036 | Undifferenzierte lithologische Einheit: Grüngestein | roche verte, indifférenciée     |
|15206037 | Undifferenzierte lithologische Einheit: Amphibolit | amphibolite, indifférenciée     |
|15206038 | Undifferenzierte lithologische Einheit: Quarzgang | filon de quartz     |
|15206039 | Undifferenzierte lithologische Einheit: Aplit | aplite     |
|15206040 | Undifferenzierte lithologische Einheit: Pegmatit | pegmatite     |
|15204048 | Garone-Fm. | Formation du (Monte) Garone     |
|15204049 | Arlberg-Fm. | Formation de l&#39;Arlberg     |
|15204050 | Partnach-Fm. | Formation de la Partnach     |
|15204051 | Altein-Fm. | Formation de l&#39;Altein     |
|15204052 | Altein-Fm.: Parai-Alba-Mb. | Membre de la Parai Alba     |
|15204053 | Prosanto-Fm. | Formation du (Piz) Prosanto     |
|15204054 | Vallatscha-Fm. | Formation du (Piz) Vallatscha     |
|15204055 | Vallatscha-Fm.: Tiaun-Brekzie | Brèche du Tiaun     |
|15204056 | Vallatscha-Fm.: Dolomit | Membre du (Piz) Vallatscha     |
|15204057 | Vallatscha-Fm.: Turettas-Mb. | Membre du (Piz) Turettas     |
|15204058 | Vallatscha-Fm.: Landwasser-Mb. | Membre de la Landwasser     |
|15204059 | S-charl-Fm. | Formation de S-charl     |
|15204060 | S-charl-Fm.: Sertig-Mb. | Membre du Sertig     |
|15204061 | S-charl-Fm.: Ravais-ch-Mb. | Membre de Ravais-ch     |
|15204062 | Reiflingen-Fm. | Formation de Reiflingen     |
|15204063 | Ducan-Fm. | Formation du (Piz) Ducan     |
|15204064 | Ducan-Fm.: Trochitendolomit | Trochitendolomit-Member     |
|15204065 | Ducan-Fm.: Brachiopodenkalk | Brachiopodenkalk-Member     |
|15204066 | Ducan-Fm.: Eisendolomit-Mb. | Eisendolomit-Member     |
|15204067 | Ducan-Fm.: Gracilis-Mb. | Gracilis-Member     |
|15204068 | Gutenstein-Fm. | Formation de Gutenstein     |
|15204069 | Reichenhall-Fm. | Formation de Reichenhall     |
|15204070 | Fuorn-Fm. | Formation du Fuorn     |
|15204071 | Fuorn-Fm.: Punt-la-Drossa-Mb. | Membre de Punt la Drossa     |
|15204072 | Fuorn-Fm.: Pflanzenquarzit | Pflanzenquarzit (Fm. du Fuorn)     |
|15204073 | Fuorn-Fm.: Unterer Teil | Membre inférieur de la Fm. du Fuorn     |
|15204074 | Ruina- und Chazfora-Fm. | Groupe du Val Müstair     |
|15204075 | Chazforà-Fm. | Formation de Chazforà     |
|15204076 | Chazforà-Fm.: Tuors-Mb. | Membre du (Val) Tuors     |
|15204077 | Chazforà-Fm.: Val-Püra-Mb. | Membre du Val Püra     |
|15204078 | Präbichl-Fm. | Formation de Präbichl     |
|15204079 | Ruina-Fm. | Formation de la Ruina     |
|15204080 | Ruina-Fm.: Sandhubel-Mb. | Membre du Sandhubel     |
|15204081 | Ruina-Fm.: Bellaluna-Mb. | Membre de Bellaluna     |
|15204082 | Mönchalp-Augengneis | Gneiss oeillé de la Mönchalp     |
|15204083 | Tschuggen-Augengneis | Gneiss oeillé de Tschuggen     |
|15204084 | Güstizia-Gneis | Gneiss de la Güstizia     |
|15204085 | Plasseggen-Augengneis | Gneiss oeillé de Plasseggen     |
|15204086 | Ostalpin: Trias | Trias de l&#39;Austroalpin     |
|15204087 | Ostalpin: Dogger | Ostalpin: Dogger     |
|15204088 | Ostalpin: Radiolarit-Aptychenkalk | Ostalpin: Radiolarit-Aptychenkalk     |
|15204089 | Ostalpin: Kreide | Ostalpin: Kreide     |
|15204090 | Ostalpin: Lias | Ostalpin: Lias     |
|15204091 | Ostalpin: Grundgebirge | Ostalpin: Grundgebirge     |
|15204092 | Nair-Porphyroid | Nair-Porphyroid     |
|15201566 | Plaffeien-Seetone | Plaffeien-Seetone     |
|15201567 | Plasselb-Stauschotter | Plasselb-Stauschotter     |
|15206041 | Undifferenzierte lithologische Einheit: Prasinit | prasinite, indifférenciée     |
|15206042 | Undifferenzierte lithologische Einheit: Serpentinit | serpentinite, indifférenciée     |
|15206043 | Undifferenzierte lithologische Einheit: Mineralisierter Gang | filon minéralisé     |
|15206044 | Undifferenzierte lithologische Einheit: Mikrogranit | microgranite     |
|15206045 | Undifferenzierte stratigraphische Einheit: Rhät | Rhétien, indifférencié     |
|15206046 | Undifferenzierte lithologische Einheit: Biogener Kalkstein | calcaire biogène (Éocène)     |
|15206047 | Undifferenzierte lithologische Einheit: Rodingit | rodingite     |
|15206048 | Undifferenzierte lithologische Einheit: Saures Ganggestein | filon acide     |
|15206049 | Undifferenzierte lithologische Einheit: Basisches Ganggestein | filon basique     |
|15206050 | Undifferenzierte lithologische Einheit: Eklogit | éclogite, indifférenciée     |
|15206051 | Undifferenzierte lithologische Einheit: Mylonit | mylonite, indifférenciée     |
|15206052 | Undifferenzierte lithologische Einheit: Kalksilikatfels | roche calcsilicatée     |
|15206053 | Undifferenzierte lithologische Einheit: Marmor | marbre, indifférencié     |
|15206054 | Undifferenzierte lithologische Einheit: Sedimentäre Brekzie | brèche sédimentaire, indifférenciée     |
|15206055 | Undifferenzierte stratigraphische Einheit: Paläozoikum | Paléozoïque, indifférencié     |
|15201259 | Ofenloch-Karstfüllung | Ofenloch-Karstfüllung     |
|15201260 | Wurmsbach-Deltaablagerungen | Wurmsbach-Deltaablagerungen     |
|15201261 | Oeschinensee-Bergsturzablagerungen | Oeschinensee-Bergsturzablagerungen     |
|15201262 | Fisistock-Bergsturzablagerungen | Fisistock-Bergsturzablagerungen     |
|15201263 | Bire-Bergsturzablagerungen | Bire-Bergsturzablagerungen     |
|15201264 | Hasle-Schotter | Hasle-Schotter     |
|15201265 | Fankhusgrabe-Schotter | Fankhusgrabe-Schotter     |
|15201266 | Rossgaden-Schotter | Rossgaden-Schotter     |
|15201267 | Grundtal-Schotter | Grundtal-Schotter     |
|15201268 | Murg-Schieferkohle | Murg-Schieferkohle     |
|15201269 | Oberricken-Schotter | Oberricken-Schotter     |
|15201270 | Haslentobel-Schotter | Haslentobel-Schotter     |
|15201271 | Aatal-Seebodenlehm | Aatal-Seebodenlehm     |
|15201272 | Eschenbach-Formation | Eschenbach-Formation     |
|15201273 | Oberkirch-Seebodenlehm | Oberkirch-Seebodenlehm     |
|15201274 | Günterstall-Schotter | Günterstall-Schotter     |
|15201275 | Gublen-Schotter | Gublen-Schotter     |
|15201276 | Unter-Buechwald-Schotter | Unter-Buechwald-Schotter     |
|15201277 | Regelstein-Till | Regelstein-Till     |
|15201278 | Halden-Seeablagerungen | Halden-Seeablagerungen     |
|15201279 | Schafbüel-Formation | Schafbüel-Formation     |
|15201280 | Unteres-Huttenbüel-Schotter | Unteres-Huttenbüel-Schotter     |
|15201281 | Winden-Schieferkohle | Winden-Schieferkohle     |
|15201282 | Tiefenwinkel-Seebodensedimente | Tiefenwinkel-Seebodensedimente     |
|15201283 | Uznach-Schieferkohle | Uznach-Schieferkohle     |
|15201284 | Embrach-Seeablagerungen | Embrach-Seeablagerungen     |
|15201458 | Ceppo | Ceppo     |
|15201459 | Novazzano-Sand | Sable de Novazzano     |
|15201444 | Löss, undifferenziert | Loess, indifférencié     |
|15201707 | Humbel-Schotter | Humbel-Schotter     |
|15201623 | Hochterrasse, unteres Niveau | Hochterrasse, unteres Niveau     |
|15201712 | Birlibänz-Schotter | Birlibänz-Schotter     |
|15201714 | Wentzwiller-Schotter | Wentzwiller-Schotter     |
|15201629 | Zurzach-Formation | Zurzach-Formation     |
|15201715 | Bellevue-Schotter | Bellevue-Schotter     |
|15201713 | Schönenbuch-Schotter | Schönenbuch-Schotter     |
|15206056 | Undifferenzierte stratigraphische Einheit: Känozoikum | Cénozoïque, indifférencié     |
|15206057 | Undifferenzierte lithologische Einheit: Ultramafisches Gestein | roche ultramafique     |
|15206058 | Undifferenzierte lithologische Einheit: Verwitterter Fels | roche altérée, indifférenciée     |
|15206059 | Undifferenzierte lithologische Einheit: Ophikalzit | ophicalcite, indifférenciée     |
|15206060 | Undifferenzierte lithologische Einheit: Talkschiefer | talcschiste, indifférencié     |
|15206061 | Undifferenzierte lithologische Einheit: Mirkodiorit | microdiorite, indifférenciée     |
|15206062 | Undifferenzierte lithologische Einheit: Quarzit | quartzite, indifférenciée     |
|15206063 | Undifferenzierte lithologische Einheit: Fuchsit-Zoisitschiefer | schiste à zoïsite et fuchsite, indifférencié     |
|15206064 | Undifferenzierte lithologische Einheit: Konglomerat | conglomérat, indifférencié     |
|15206065 | Undifferenzierte lithologische Einheit: Glaukophanschiefer | schiste à glaucophane, indifférencié     |
|15206066 | Bündnerschiefer | Bündnerschiefer, indifférencié     |
|15206067 | Undifferenzierte lithologische Einheit: Augengneis | gneiss oeillé, indifférencié     |
|15206068 | Undifferenzierte lithologische Einheit: Granat-Glimmerschiefer | micaschistes à grenat, indifférencié     |
|15206069 | Undifferenzierte lithologische Einheit: Albit-Muskowitschiefer | schiste à muscovite et albite, indifférencié     |
|15206070 | Undifferenzierte lithologische Einheit: Gneis | gneiss, indifférencié     |
|15201460 | Bergsturzablagerungen vom Stützwald | dépôt d&#39;écroulement du Stützwald     |
|15204093 | Nair-Porphyroid: Lavatèra-Brekzie | Nair-Porphyroid: Lavatèra-Brekzie     |
|15204094 | Varaina-Schiefer | Varaina-Schiefer     |
|15204095 | Sprenkel-Schiefer | Sprenkel-Schiefer     |
|15204096 | Fedoz-Gneiskomplex | Complexe gneissique de Fedoz     |
|15204097 | Fedoz-Metagabbro | Fedoz-Metagabbro     |
|15204098 | Maloja-Orthogneis | Maloja-Orthogneis     |
|15204099 | Maloja-Gneiskomplex | Complexe gneissique du Maloja     |
|15204100 | Ur-Brekzie | Ur-Brekzie     |
|15204101 | Tschima-da-Flix-Granit | Tschima-da-Flix-Granit     |
|15204102 | Err-Granodiorit | Granodiorite d&#39;Err     |
|15204103 | Ostalpin: Postvariszische Diabasgänge | Filons de diabase postvarisques     |
|15204104 | Flüela-Augengneis | Gneiss oeillé de la Flüela     |
|15204105 | Dorfberg-Gneis | Gneiss du Dorfberg     |
|15204106 | Allgäu-Fm.: Alpisella-Mb.: Chaschauna-Brekzie | Brèche du Piz Chaschauna     |
|15204107 | Sesvenna-Augengneis | Gneiss oeillé de la Sesvenna     |
|15204108 | Vaüglia-Granodiorit | Granodiorite de Vaüglia     |
|15204109 | Mingèr-Fm.: Mora-Mb.: Döss-Radond-Vulkanite | Roches volcanique du Döss Radond     |
|15204110 | Augsten-Brekzie | Brèche de l&#39;Augsten     |
|15204111 | Piz-Trovat-Metarhyolith | Métarhyolite du Piz Trovat     |
|15204112 | Sass-Queder-Metarhyolith | Métarhyolite du Sass Queder     |
|15204113 | La-Rösa-Orthogneis | Orthogneiss de la Rösa     |
|15201665 | Schlüsselgraben-Schotter | Schlüsselgraben-Schotter     |
|15201568 | Uetliberg-Lehm | Uetliberg-Lehm     |
|15201569 | Schotter der Thur | Schotter der Thur     |
|15201570 | Schwarzwald-Schotter | Schwarzwald-Schotter     |
|15201571 | Neuenburg-Formation | Neuenburg-Formation     |
|15201572 | Hartheim-Member | Hartheim-Member     |
|15201573 | Nambsheim-Member | Nambsheim-Member     |
|15201574 | Breisgau-Formation | Breisgau-Formation     |
|15201575 | Balgau-Member | Balgau-Member     |
|15201576 | Weinstetten-Member | Weinstetten-Member     |
|15201577 | Iffezheim-Formation | Iffezheim-Formation     |
|15201578 | Mannheim-Formation | Mannheim-Formation     |
|15201579 | Etzgen-Formation | Etzgen-Formation     |
|15201580 | Niederuster-Schotter | Niederuster-Schotter     |
|15201581 | Pfungen-Formation | Pfungen-Formation     |
|15201582 | Dättlikon-Stadium | Dättlikon-Stadium     |
|15201583 | Dübendorf-Stadium | Dübendorf-Stadium     |
|15201584 | Gfenn-Stadium | Gfenn-Stadium     |
|15201585 | Regensdorf-Stadium | Regensdorf-Stadium     |
|15206071 | Undifferenzierte lithologische Einheit: Graphitschiefer | schiste graphiteux, indifférencié     |
|15206072 | Undifferenzierte lithologische Einheit: Glimmerschiefer | micaschistes, indifférencié     |
|15206073 | Undifferenzierte lithologische Einheit: Garbenschiefer | Garbenschiefer, indifférencié     |
|15206074 | Undifferenzierte lithologische Einheit: Diorit | diorite, indifférenciée     |
|15206075 | Undifferenzierte lithologische Einheit: Gabbro | gabbro, indifférencié     |
|15206076 | Undifferenzierte lithologische Einheit: Orthogneis | orthogneiss, indifférencié     |
|15206077 | Undifferenzierte lithologische Einheit: Paragneis | paragneiss, indifférencié     |
|15206078 | Undifferenzierte lithologische Einheit: Vulkanisches Gestein | roche volcanique, indifférenciée     |
|15206079 | Undifferenzierte lithologische Einheit: Basalt | basalte, indifférencié     |
|15206080 | Undifferenzierte stratigraphische Einheit: Karbon | Carbonifère, indifférencié     |
|15206081 | Undifferenzierte lithologische Einheit: Chloritschiefer | schiste chloriteux, indifférencié     |
|15206082 | Undifferenzierte lithologische Einheit: Phyllit | phyllite, indifférenciée     |
|15206083 | Undifferenzierte lithologische Einheit: Quarzphyllit | quartzphyllite, indifférenciée     |
|15206084 | Bündnerschiefer: Kalkschiefer | Bündnerschiefer calcaires     |
|15206085 | Bündnerschiefer: Tonschiefer | Bündnerschiefer argileux     |
|15204114 | Carale-Schiefer | Schistes du Carale     |
|15204115 | Gosau-Gruppe | Groupe de Gosau     |
|15204116 | Morteratsch-Serpentinit | Serpentinite du Morteratsch     |
|15204117 | Forun-Augengneis | Gneiss oeillé du Forun     |
|15204118 | Kesch-Augengneis | Gneiss oeillé du Piz Kesch     |
|15204119 | Ostalpin: Prävariszisches polyzyklisches Grundgebirge | socle polycyclique anté-varisque de l&#39;Austroalpin     |
|15204120 | Silvretta-Decke: Jüngere Orthogneise | «Jüngere Orthogneise»     |
|15204121 | Silvretta-Decke: Ältere Orthogneise | «Ältere Orthogneise»     |
|15204122 | Val-Rude-Orthogneis | Orthogneiss du Val Rude     |
|15204123 | Corvatsch-Granitkomplex: Corvatsch-Granodiorit | Granodiorite du Corvatsch     |
|15204124 | Julier-Granodiorit | Granodiorite du Julier     |
|15204125 | Sasso-Rosso-Granodiorit | Granodiorite du Sasso Rosso     |
|15204126 | Vallatscha-Fm.: Lavinèr-Brekzie | Brèche du Piz Lavinèr     |
|15204127 | Haupter-Brekzie | Brèche de l&#39;Haupter     |
|15204128 | Ostalpin: Postvariszische Vulkanite und Sedimente | Permo-Carbonifère de l&#39;Austroalpin     |
|15204130 | Garone-, Vallatscha-,Prosanto- und Altein-Fm. | Groupe de Buffalora     |
|15204132 | Ostalpin: Variszische Intrusiva | roches intrusives varisques de l&#39;Austroalpin     |
|15204135 | Ostalpin: Prävariszischer Orthogneis | orthogneiss anté-varisques de l&#39;Austroalpin     |
|15201653 | Lei-Schotter | Lei-Schotter     |
|15201683 | Tannboden-Schotter | Tannboden-Schotter     |
|15206086 | Undifferenzierte lithologische Einheit: Migmatit | migmatite, indifférenciée     |
|15206087 | Undifferenzierte lithologische Einheit: Tonalit | tonalite, indifférenciée     |
|15206088 | Undifferenzierte lithologische Einheit: Syenit | syénite, indifférenciée     |
|15206089 | Undifferenzierte lithologische Einheit: Tektonit | tectonite, indifférenciée     |
|15206090 | Undifferenzierte lithologische Einheit: Hornfels | cornéenne, indifférenciée     |
|15206091 | Undifferenzierte lithologische Einheit: Hornblendegneis | gneiss à hornblende, indifférencié     |
|15206092 | Undifferenzierte lithologische Einheit: Biotit-Plagioklasgneis | gneiss à biotite et plagioclase, indifférencié     |
|15206093 | Undifferenzierte lithologische Einheit: Bändergneis | gneiss rubané, indifférencié     |
|15206094 | Undifferenzierte lithologische Einheit: Zweiglimmergneis | gneiss à deux micas, indifférencié     |
|15206095 | Undifferenzierte lithologische Einheit: Phyllitgneis | gneiss phyllitique, indifférencié     |
|15206096 | Undifferenzierte lithologische Einheit: Peridotit | péridotite, indifférencié     |
|15206097 | Undifferenzierte lithologische Einheit: Bänder- und Schollenamphibolit | amphibolite rubanée et à blocs, indifférencié     |
|15206098 | Undifferenzierte lithologische Einheit: Granatamphibolit | amphibolite à grenat, indifférencié     |
|15206099 | Undifferenzierte lithologische Einheit: Diabasgang | filon diabasique, indifférencié     |
|15206100 | Undifferenzierte stratigraphische Einheit: Perm | Permien, indifférencié     |
|15204136 | Ostalpin: Prävariszischer Paragneis | paragneiss anté-varisques de l&#39;Austroalpin     |
|15204137 | Ostalpin: Prävariszische Grüngesteine | roches vertes anté-varisques de l&#39;Austroalpin     |
|15204138 | Uglix-Plattenkalk | Calcaire d&#39;Uglix     |
|15204139 | Parait-Chavagl-Granit | Granite du Parait Chavagl     |
|15204140 | God-Drosa-Flysch: Clavadatsch-Brekzie | Brèche de Clavadatsch     |
|15204141 | Corno-di-Campo-Granodiorit | Granodiorite du Corno di Campo     |
|15204142 | Campocologno-Gabbro | Gabbro de Campocologno     |
|15204143 | Celerina-Orthogneis | Orthogneiss de Celerina     |
|15204144 | Tonale-Schiefer | Schistes du Tonale     |
|15204145 | Ostalpin: Raibl-Gr.: Gips | Gypse du Groupe de Raibl     |
|15204146 | Ostalpin: Raibl-Gr.: Rauwacke | Cornieule du Groupe de Raibl     |
|15204147 | Arlberg-Fm.: Rifffazies | faciès récifal de la Formation de l&#39;Arlberg     |
|15204148 | Ducan- und S-charl-Fm. | Alpiner Muschelkalk     |
|15204149 | Ostalpin: Raibl-Gr.: Dolomit | Groupe de Raible: dolomite     |
|15204150 | Ostalpin: Hauptdolomit-Gr.: bituminöser Dolomit | Groupe de la Hauptdolomite: brèche dolomitique bitumineuse     |
|15204151 | Zentralschweizerische Klippen: Raibl-Gr. | Groupe de Raibl des klippes de Suisse centrale     |
|15205001 | Dent-Blanche-Decke: Sedimentbedeckung | Groupe du Dolin     |
|15205002 | Petit-Dolin-Kalkbrekzie | Brèche calcaire du Dolin     |
|15201064 | Löhningen-Engiwald-Vergletscherung | Glaciation de Löhningen-Engiwald     |
|15201065 | Engiwald-Vorstoss | Avancée glaciaire de l&#39;Engiwald     |
|15201066 | Rüfenach-Vorstoss | Avancée glaciaire de Rüfenach     |
|15201175 | Reusstal-Sand | Sable du Reusstal     |
|15201176 | Reusstal-Lehm | Limon du Reusstal     |
|15201067 | Löhningen-Vorstoss | Avancée glaciaire de Löhningen     |
|15201068 | Remigen-Vorstoss | Avancée glaciaire de Remingen     |
|15201177 | Hausen-Lehm | Limon de Hausen     |
|15201178 | Hausen-Moräne | Till de Hausen     |
|15201069 | Remigen-Schotter | Gravier de Remingen     |
|15201070 | Meikirch-Interglazial | Interglaciaire de Meikirch     |
|15201071 | Ältere Beckenfüllungen | Anciens remplissages de bassin     |
|15201072 | Hagenholz-Eiszeit | Période glaciaire du Hagenholz     |
|15201179 | Ruckfeld-Schotter | Gravier du Ruckfeld     |
|15201073 | Hagenholz-Vergletscherung | Glaciation du Hagenholz     |
|15201074 | Hagenholz-Vorstoss | Avancée glaciaire du Hagenholz     |
|15201075 | Aathal-Schotter | Gravier de l&#39;Aathal     |
|15201076 | Pfyn-Vorstoss | Avancée glaciaire de Pfyn     |
|15201077 | Ittingen-Schotter | Gravier d&#39;Ittingen     |
|15201078 | Ryhirt-Formation | Formation du Ryhirt     |
|15201079 | Geisslingen-Schotter | Gravier de Geisslingen     |
|15201080 | Habsburg-Hagenholz-Interglazial | Interglaciaire Habsburg-Hagenholz     |
|15201081 | Möhlinerfeld-Paläoboden | Paléosol du Möhlinerfeld     |
|15201082 | Habsburg-Eiszeit | Période glaciaire de Habsburg     |
|15201083 | Gränichen-Schotter | Gravier de Gränichen     |
|15201084 | Roggehuse-Schotter | Gravier de Roggehuse     |
|15201085 | Buerfeld-Schotter | Gravier du Buerfeld     |
|15201086 | Habsburg-Vergletscherung | Glaciation de Habsburg     |
|15201087 | Habsburg-Vorstoss | Avancée glaciaire de Habsburg     |
|15201088 | Habsburg-Schotter | Gravier de Habsburg     |
|15201180 | Endingen-Schotter | Gravier d&#39;Endingen     |
|15201089 | Unterschlatt-Vorstoss | Avancée glaciaire d&#39;Unterschlatt     |
|15201090 | Thalgut-Interglazial | Interglaciaire de Thalgut     |
|15201091 | Möhlin-Eiszeit (Grösste Eiszeit) | Période glaciaire de Möhlin     |
|15201092 | Möhlin-Vergletscherung | Glaciation de Möhlin     |
|15201093 | Möhlin-Vorstoss | Avancée glaciaire de Möhlin     |
|15201094 | Bünten-Till | Till de Bünten     |
|15201095 | Schleitheim-Vorstoss | Avancée glaciaire de Schleitheim     |
|15201004 | Tiefere Deckenschotter | Tiefere Deckenschotter     |
|15206101 | Undifferenzierte lithologische Einheit: Kalkmarmor | marbre calcaire, indifférencié     |
|15206103 | Undifferenzierte stratigraphische Einheit: Permo-Karbon | Permo-Carbonifère, indifférencié     |
|15206104 | Undifferenzierte lithologische Einheit: Kalkschiefer | calcschiste, indifférencié     |
|15206105 | Undifferenzierte lithologische Einheit: Sandstein | grès, indifférencié     |
|15206106 | Undifferenzierte lithologische Einheit: Tonschiefer | schiste argileux, indifférencié     |
|15206107 | Undifferenzierte lithologische Einheit: Radiolarit | radiolarite, indifférenciée     |
|15206108 | Undifferenzierte lithologische Einheit: Kalkstein | calcaire, indifférencié     |
|15206109 | Undifferenzierte lithologische Einheit: Konglomeratgneis | gneiss conglomératique, indifférencié     |
|15206110 | Undifferenzierte stratigraphische Einheit: Prävariszisches polyzyklisches Grundgebirge | socle polycyclique anté-varisque, indifférencié     |
|15206111 | Undifferenzierte lithologische Einheit: Schiefer | schiste, indifférencié     |
|15206112 | Undifferenzierte lithologische Einheit: Aplitgneis | gneiss aplitique, indifférencié     |
|15206113 | Undifferenzierte lithologische Einheit: Süsswasserkalk | Undifferenzierte lithologische Einheit: Süsswasserkalk     |
|15206114 | Undifferenzierte stratigraphische Einheit: Tektonisches Melange | mélange tectonique     |
|15201499 | Untergrabehüsli-Schotter | Untergrabehüsli-Schotter     |
|15205003 | Roisan-Cignana-Zone | zone de Roisan     |
|15205004 | Arolla-Einheit | Série d&#39;Arolla     |
|15205005 | Mont-Collon-Gabbro | Complexe du Mont Collon     |
|15205006 | Arolla-Orthogneis | orthogneiss du Groupe d&#39;Arolla     |
|15205007 | Valpelline-Einheit | Série de Valpelline     |
|15205008 | Castel-di-Sotto-Ton | Argile de Castel di Sotto     |
|15205009 | Pontegana-Konglomerat | Conglomérat de Pontegana     |
|15205010 | Lombardischer Gompholith | Groupe de la Gompholite Lombarde     |
|15205011 | Lucino-Konglomerat | Conglomérat de Lucino     |
|15205012 | Lucino-Konglomerat: Cagno-Sandstein | Grès de Cagno     |
|15205013 | Como-Konglomerat: Val-Grande-Sandstein | Grès du Val Grande     |
|15205014 | Como-Konglomerat: Prestino-Pelite | Pélite de Prestino     |
|15205015 | Como-Konglomerat | Conglomérat de Como     |
|15205016 | Como-Konglomerat: Malnate-Sandstein | Grès de Malnate     |
|15205017 | Como-Konglomerat: Rio-dei-Gioghi-Pelite | Pélite du Rio dei Gioghi     |
|15205018 | Chiasso-Fm. | Formation de Chiasso     |
|15205019 | Chiasso-Fm: Villa-Olmo-Konglomerat | Conglomérat de Villa Olmo     |
|15205020 | Ternate-Fm. | Formation de Ternate     |
|15205021 | Brenno-Fm. | Formation de Brenno     |
|15205022 | Prella-Konglomerat | Conglomérat de Prella     |
|15205023 | Südalpin: Flysch | Groupe du Flysch Lombard     |
|15205024 | Bergamo-Flysch | Flysch de Bergamo     |
|15201096 | Fisibach-Schotter | Gravier de Fisibach     |
|15201097 | Bärengraben-Schotter und -Till | Gravier et Till du Bärengraben     |
|15201098 | Iberig-Schotterkomplex | Gravier de l&#39;Iberig     |
|15201099 | Obere Iberigschotter | Gravier supérieur de l&#39;Iberig     |
|15201100 | Oberer Till | Oberer Till (Iberig)     |
|15201101 | Mittlere Iberigschotter | Gravier moyen de l&#39;Iberig     |
|15201102 | Untere Iberigschotter | Gravier inférieur de l&#39;Iberig     |
|15201103 | Unterer Till | Unterer Till (Iberig)     |
|15201104 | Wolfacher-Schotter und -Till | Gravier et Till de Wolfacher     |
|15201105 | Fornech-Schotter | Gravier de la Fornech     |
|15201005 | Höhere Deckenschotter | Höhere Deckenschotter     |
|15201106 | Forenirchel-Schotter | Gravier du Forenirchel     |
|15201107 | Steig-Schotter | Gravier du Steig     |
|15201108 | Irchel-Schotterkomplex | Gravier de l&#39;Irchel     |
|15201109 | Obere Irchelschotter | Gravier supérieur de l&#39;Irchel     |
|15201111 | Irchel-Dolomitschotter | Gravier dolomitique de l&#39;Irchel     |
|15201112 | Mittlere Irchelschotter | Gravier moyen de l&#39;Irchel     |
|15201113 | Untere Irchelschotter | Gravier inférieur de l&#39;Irchel     |
|15201114 | Langacher-Schotter | Gravier du Langacher     |
|15201115 | Dürn-Formation | Formation du Dürn     |
|15201116 | Degermoos-Schotter | Gravier de Degermoos     |
|15201117 | Ebnet-Schotter | Gravier de l&#39;Ebnet     |
|15201118 | Wannen-Schotter | Gravier du Wannen(buck)     |
|15201119 | Egghalden-Schotter | Gravier de l&#39;Egghalden     |
|15201120 | Buechen-Formation | Formation de Buechen     |
|15201121 | Feusi-Schotter | Gravier du Feusi     |
|15201122 | Lindenhau-Schotter | Gravier du Lindenhau     |
|15201123 | Egg-Schotter | Gravier de l&#39;Egg     |
|15201124 | Sundgau-Schotter | Gravier du Sundgau     |
|15201125 | Mischschotter | Mischschotter (Sundgau)     |
|15201126 | Weisse Serie | Weisse Serie (Sundgau)     |
|15206115 | Undifferenzierte stratigraphische Einheit: Flysch | Flysch, indifférencié     |
|15206116 | Undifferenzierte lithologische Einheit: Aptychenkalk | Calcaire à aptychus, indiff.     |
|15206117 | Undifferenzierte lithologische Einheit: Quarzsandstein | Grès quartzitique, indiff.     |
|15206118 | Undifferenzierte lithologische Einheit: Mergelstein | Undifferenzierte lithologische Einheit: Mergelstein     |
|15206119 | Undifferenzierte lithologische Einheit: Basisches Gestein | Undifferenzierte lithologische Einheit: Basisches Gestein     |
|15201505 | Reuss-Schotterkomplex | Reuss-Schotterkomplex     |
|15201490 | Rufswil-Schotter | Rufswil-Schotter     |
|15201491 | Rütimatt-Schotter | Rütimatt-Schotter     |
|15201511 | Mooretal-Schotter | Mooretal-Schotter     |
|15201462 | Birkenhof-Formation | Birkenhof-Formation     |
|15201463 | Zeiningen-Till | Zeiningen-Till     |
|15201464 | Höhenschotter | Höhenschotter     |
|15201465 | Böschmatt-Schotter | Böschmatt-Schotter     |
|15201466 | Bramegg-Schotter | Bramegg-Schotter     |
|15201467 | Kaltenegg-Schotter | Kaltenegg-Schotter     |
|15201468 | Steinhuserberg-Schotter | Steinhuserberg-Schotter     |
|15201469 | Büelm-Schotter | Büelm-Schotter     |
|15201470 | Büel-Schotter | Büel-Schotter     |
|15205025 | Coldrerio-Flysch | Flysch de Coldrerio     |
|15205026 | Torre-Konglomerat | Conglomérat de Torre     |
|15205027 | Varesotto-Flysch | Flysch du Varesotto     |
|15205028 | Scaglia Lombarda | Groupe de la Scaglia Lombarda     |
|15205029 | Scaglia Rossa Lombarda | Scaglia Rossa Lombarda     |
|15205030 | Scaglia Bianca Lombarda | Scaglia Bianca Lombarda     |
|15205031 | Scaglia Variegata Lombarda | Scaglia Variegata Lombarda     |
|15205032 | Maiolica Lombarda | Maiolica Lombarda     |
|15205033 | Selcifero Lombardo | Groupe de la Radiolarite Lombarde     |
|15205034 | Selcifero Lombardo: Rosso ad Aptici | Rosso ad Aptici     |
|15205035 | Calcare a bivalvi planctonici | Calcari a bivalvi planctonici     |
|15205036 | Rosso Ammonitico Lombardo | Rosso Ammonitico Lombardo     |
|15205037 | Rosso Ammonitico Lombardo: Grenzposidonienschichten | Lumachelle à Posidonia alpina (Grenzposidonienschichten)     |
|15205038 | Morbio-Fm. | Formation de Morbio     |
|15205039 | Besazio-Kalk | Calcaire de Besazio     |
|15205040 | Moltrasio-Fm. | Formation de Moltrasio     |
|15205041 | Moltrasio-Fm.: Molino-Mb. | Membre du Molino     |
|15205042 | Saltrio-Fm. | Formation de Saltrio     |
|15205043 | Macchia Vecchia | Macchia Vecchia     |
|15205044 | Broccatello d&#39;Arzo | Broccatello d&#39;Arzo     |
|15205045 | Albenza-Fm. | Formation de l&#39;Albenza     |
|15205046 | Zu-Kalk | Calcaire de Zu     |
|15203450 | Saas-Fee-Augengneis | Gneiss oeillé de Saas Fee     |
|15203451 | Almagelhorn-Migmatit | Migmatite de l&#39;Almagelhorn     |
|15203452 | Weissmies-Paragneis | Paragneiss du Weissmies     |
|15203453 | Monte-Rosa-Orthogneis: Mittelkörnige Fazies | Orthogneiss du Mont Rose, à grain moyen     |
|15203454 | Stellihorn-Mylonit | Mylonite du Stellihorn     |
|15203455 | Pizzo-del-Vallone-Decke: Kalkschiefer | Calcschistes de la Série du Fäldbach     |
|15203456 | Unterpenninikum: Dogger | Dogger nord-pennique     |
|15203457 | Unterpenninikum: Lias | Lias nord-pennique     |
|15203458 | Unterpenninikum: Trias: Dolomit | Dolomie du Trias nord-pennique     |
|15203459 | Valgrande-Paragneis | Paragneiss de Vagrande     |
|15203460 | Mittelpenninikum: Variszische Intrusiva | Roches intrusives varisques du Briançonnais     |
|15203461 | Mittelpenninikum: Prävariszisches Grundgebirge | Socle cristallin anté-varisque du Briançonnais     |
|15203462 | Moncucco-Peridotit | Péridotite du Moncucco     |
|15203463 | Adlerflüe-Fm.: Albitaugenschiefer | Schistes oeillés à porphyroblastes d&#39;albite (SOPA) de la Formation de l&#39;Adlerflüe     |
|15203464 | Adlerflüe-Fm.: Bänderamphibolit | Amphibolite rubanée de la Formation de l&#39;Adlerflüe     |
|15203465 | Adlerflüe-Fm.: Minugrat-Eklogit | Éclogite du Minugrat     |
|15203466 | Ergischhorn-Komplex: Amphibolit | Amphibolite du Complexe gneissique de l&#39;Ergischhorn     |
|15203467 | Distulberg-Fm.: Grüngesteine | Roches vertes de la Formation du Distulberg     |
|15201286 | Bergsturzablagerungen von Sierre | dépôt d&#39;écroulement de Sierre     |
|15201287 | Bergsturzablagerungen von Chiètres | dépôt d&#39;écroulement de Chiètres     |
|15201288 | Bergsturzablagerungen von Chessel-Noville | dépôt d&#39;écroulement de Chessel-Noville     |
|15201289 | Bergsturzablagerungen von Novalles-Vugelles | dépôt d&#39;écroulement de Novalles-Vugelles     |
|15201290 | Bergsturzablagerungen von Gwelber-Laui-Weid | dépôt d&#39;écroulement de Gwelber-Laui-Weid     |
|15201291 | Bergsturzablagerungen von Castasegna | dépôt d&#39;écroulement de Castasegna     |
|15201292 | Bergsturzablagerungen von Sogno | dépôt d&#39;écroulement de Sogno     |
|15201293 | Bergsturzablagerungen von Prapan | dépôt d&#39;écroulement de Prapan     |
|15201294 | Bergsturzablagerungen von Schaingels | dépôt d&#39;écroulement de Schaingels     |
|15201295 | Bergsturzablagerungen von Mutta | dépôt d&#39;écroulement de Mutta     |
|15201296 | Bergsturzablagerungen von Brienz | dépôt d&#39;écroulement de Brienz     |
|15201297 | Bergsturzablagerungen von Flims | dépôt d&#39;écroulement de Flims     |
|15201298 | Bergsturzablagerungen von Brüsis | dépôt d&#39;écroulement de Brüsis     |
|15201299 | Bergsturzablagerungen vom Chapf | dépôt d&#39;écroulement de Chapf     |
|15201300 | Bergsturzablagerungen von Derborence | Bergsturzablagerungen von Derborence     |
|15201301 | Bergsturzablagerungen vom Drussetschawald | dépôt d&#39;écroulement du Drussetschawald     |
|15201302 | Bergsturzablagerungen vom Delenwald | dépôt d&#39;écroulement du Delenwald     |
|15201303 | Bergsturzablagerungen von Elm | dépôt d&#39;écroulement d&#39;Elm     |
|15201304 | Bergsturzablagerungen von Goldau | dépôt d&#39;écroulement de Goldau     |
|15201305 | Bergsturzablagerungen von Iragell | dépôt d&#39;écroulement d&#39;Iragell     |
|15201306 | Bergsturzablagerungen vom Kernwald | dépôt d&#39;écroulement du Kernwald     |
|15201307 | Bergsturzablagerungen von Triesenberg | dépôt d&#39;écroulement de Triesenberg     |
|15201308 | Bonaduz-Formation | Formation de Bonaduz     |
|15201309 | Bonfol-Ton | Argile de Bonfol     |
|15201310 | Bergsturzablagerungen von Tamins | dépôt d&#39;écroulement de Tamins     |
|15201311 | Informell benannte Bergsturzablagerungen | dépôts d&#39;écroulement nommés informellement     |
|15203580 | Bärenhorn-Fm.: Quarzsandstein | Formation du Bärenhorn: grès quartzitique     |
|15203581 | Grava-Decke: Kalkschiefer | Schiste argilo-calcaire de la nappe de la Grava     |
|15203582 | Grava-Decke: Tonschiefer | Schiste calcaréo-argileux de la nappe de la Grava     |
|15203583 | Grava-Decke: Trias | Trias de la nappe de la Grava, indifférencié     |
|15203584 | Soladier- und Verdy-Mb. | Soladier- und Verdy-Mb.     |
|15203585 | Col-de-Tompey- und Bois-de-Luan-Mb. | Col-de-Tompey- und Bois-de-Luan-Mb.     |
|15203586 | Heiti- und Rossinière-Fm. | Heiti- und Rossinière-Fm.     |
|15203587 | Coulaytes-Melange und Cuvigne-Derrey-Fm. | Coulaytes-Melange und Cuvigne-Derrey-Fm.     |
|15203588 | Langel- und Col-de-Cordon-Mb. | Langel- und Col-de-Cordon-Mb.     |
|15203589 | Grande-Bonavau-Fm. und Fm. spathique | Grande-Bonavau-Fm. und Fm. spathique     |
|15203590 | Col-de-Tompey- und Agreblierai-Mb. | Col-de-Tompey- und Agreblierai-Mb.     |
|15203591 | Chavanette- und Rubli-Mb. | Chavanette- und Rubli-Mb.     |
|15203592 | Barrhorn-Einheit: Flysch | Barrhorn-Einheit: Flysch     |
|15203593 | Barrhorn-Einheit: Couches-Rouges | Barrhorn-Einheit: Couches-Rouges     |
|15203594 | Barrhorn-Einheit: Malm | Barrhorn-Einheit: Malm     |
|15203595 | Barrhorn-Einheit: Dogger | Barrhorn-Einheit: Dogger     |
|15203596 | St-Triphon- und Wiriehorn-Fm. | St-Triphon- und Wiriehorn-Fm.     |
|15203597 | Printse-Fm. | Printse-Fm.     |
|15203598 | Métailler-Fm.: Louvie-Gabbro | Métailler-Fm.: Louvie-Gabbro     |
|15203599 | Distulberg-Fm.: Graphitschiefer | Distulberg-Fm.: Graphitschiefer     |
|15201471 | Bünten-Schotter | Bünten-Schotter     |
|15201472 | Durnagel-Schotter | Durnagel-Schotter     |
|15201473 | Dürrenroth-Schotter | Dürrenroth-Schotter     |
|15201474 | Egghüsli-Schotter | Egghüsli-Schotter     |
|15201475 | Emmental-Schotter | Emmental-Schotter     |
|15201476 | Ergolztal-Schotter | Ergolztal-Schotter     |
|15201477 | Gammenthal-Schotter | Gammenthal-Schotter     |
|15201478 | Gondiswil-Formation | Gondiswil-Formation     |
|15201479 | Hasewald-Schotter | Hasewald-Schotter     |
|15201480 | Hirzmatt-Schotter | Hirzmatt-Schotter     |
|15201481 | Mettlen-Schotter | Mettlen-Schotter     |
|15201482 | Möhlinerfeld-Schotter | Möhlinerfeld-Schotter     |
|15201483 | Muttenfeld-Schotter | Muttenfeld-Schotter     |
|15201484 | Nidfurn-Schotter | Nidfurn-Schotter     |
|15201485 | Oberhöhe-Grundmoräne | Oberhöhe-Grundmoräne     |
|15201486 | Obermoos-Schotter | Obermoos-Schotter     |
|15201492 | Schwanderholzwald-Schotter | Schwanderholzwald-Schotter     |
|15201493 | Schwande-Seebodensedimente | Schwande-Seebodensedimente     |
|15201494 | Soppensee-Seebodensedimente | Soppensee-Seebodensedimente     |
|15201495 | Speicherboden-Lokalmoräne | Speicherboden-Lokalmoräne     |
|15201496 | terrasse lémanique de 10 m | terrasse lémanique de 10 m     |
|15201497 | terrasse lémanique de 3 m | terrasse lémanique de 3 m     |
|15201498 | Untere Zeller Schotter | Untere Zeller Schotter     |
|15201487 | Öflingen-Schotter | Öflingen-Schotter     |
|15201500 | Untertreie-Schotter | Untertreie-Schotter     |
|15201501 | Wallbach-Schotter | Wallbach-Schotter     |
|15201502 | Werthenstein-Schotter | Werthenstein-Schotter     |
|15201503 | Willburg-Formation | Willburg-Formation     |
|15201504 | Wilzigen-Seebodensedimente | Wilzigen-Seebodensedimente     |
|15201488 | Rottal-Schotter | Rottal-Schotter     |
|15201506 | Hagnau-Niveau | Hagnau-Niveau     |
|15205047 | Tremona-Fm. | Formation de Tremona     |
|15205048 | Brecce Retiche | Brecce Retiche     |
|15205049 | Riva-di-Solto-Tonstein | Argilite de Riva di Solto     |
|15205050 | Dolomia Principale | Dolomia Principale     |
|15205051 | Pizzella-Mergel | Marne du (Monte) Pizzella     |
|15205052 | Cunardo-Fm. | Formation de Cunardo     |
|15205053 | Meride-Fm. | Formation de Meride     |
|15205054 | Meride-Fm.: Kalkschieferzone | Kalkschieferzone (Fm. de Meride)     |
|15205055 | Meride-Fm.: Unterer Kalk: Cassina-Bk. | Banc de Cassina     |
|15205056 | Meride-Fm.: Unterer Kalk: Cava Superiore | Cava Superiore     |
|15205057 | Meride-Fm.: Unterer Kalk: Cava Inferiore | Cava Inferiore     |
|15205058 | San-Giorgio-Dolomit | Dolomie du (Monte) San Giorgio     |
|15205059 | San-Giorgio-Dolomit: Val-Serrata-Tuffite | Tuffite du Val Serrata     |
|15205060 | Besano-Fm. | Formation de Besano     |
|15205061 | San-Salvatore-Dolomit | Dolomie du (Monte) San Salvatore     |
|15205062 | Bellano-Fm. | Formation de Bellano     |
|15205063 | Servino | Servino     |
|15205064 | Verrucano Lombardo | Verrucano Lombardo     |
|15205065 | Morcote-Vulkanite | Roches volcanique permienne du Sudalpin     |
|15205066 | Morcote-Vulkanite: Granophyr | Granophyre permien du Sudalpin     |
|15205067 | Morcote-Vulkanite: Andesit und Dazit | Andésite et dacite permiennes du Sudalpin     |
|15203468 | Métailler-Fm.: Prasinit | Prasinites de la Formation du Métailler     |
|15203469 | Métailler-Fm.: Ultramafisches Gestein | Roches ultramafiques de la Formation du Métailler     |
|15203470 | Randa-Augengneis: Oberems-Albitgneis | Gneiss albitique d&#39;Oberems     |
|15203471 | Maggia-Decke: Permo-Karbon | Permo-Carbonifère de la nappe de la Maggia     |
|15203472 | Maggia-Decke: Quarz-Glimmerschiefer | Permien de la nappe de la Maggia     |
|15203473 | Maggia-Decke: Muskovit-Graphitschiefer | Carbonifère de la nappe de la Maggia     |
|15203474 | Maggia-Decke: Variszische Intrusive | Roches intrusives varisques de la nappe de la Maggia     |
|15203475 | Maggia-Decke: Prävariszisches Grundgebirge | Socle cristallin anté-varisque de la nappe de la Maggia     |
|15203476 | Maggia-Decke: Paragneis | Maggia-D.: Paragneis     |
|15203477 | Maggia-Decke: Bändergneis | Gneiss rubané de la nappe de la Maggia     |
|15203478 | Maggia-Decke: Augengneis | Gneiss oeillé de la nappe de la Maggia     |
|15203479 | Alpigia-Gneis | Gneiss d&#39;Alpigia     |
|15203480 | Gresso-Someo-Zone | zone de Gresso-Someo     |
|15203481 | Pertusio-Zone | zone de Pertusio     |
|15203482 | Passo-di-Cristallina-Zone | zone du Passo di Cristallina     |
|15203483 | Lago-Scuro-Fm. | Formation du Lago Scuro     |
|15203484 | Val-Sabbia-Fm. | Formation du Val Sabbia     |
|15203485 | Massari-Fm. | Formation du (Pizzo) Massari     |
|15203486 | Naret-Fm. | Formation du Narèt     |
|15201188 | Münsingen-Schotterkomplex | Complexe graveleux de Münsingen     |
|15201189 | Alterswil-Schotter | Gravier d&#39;Alterswil     |
|15201190 | Karlsruhe-Schotter | Gravier de Karlsruhe     |
|15201191 | Chisetal-Schotter | Gravier du Chisetal     |
|15201192 | Grauholz-Schotter | Gravier du Grauholz     |
|15201193 | Trachslau-Schotter | Gravier de Trachslau     |
|15201194 | Bennau-Schotter | Gravier de Bennau     |
|15201195 | Hütten-Schotter | Gravier de Hütten     |
|15201196 | Schnabelsberg-Stauchotter | Gravier de Schnabelsberg     |
|15201197 | Einsiedeln-Lehm | Limon d&#39;Einsiedeln     |
|15201312 | Informell benannte künstliche Ablagerungen | dépôts artificiels nommés informellement     |
|15201313 | Künstliche Ablagerungen des Bahnhofs Brig | dépôts artificiels de la gare de Brigue     |
|15201314 | Künstliche Ablagerungen Golar | dépôts artificiels Golar     |
|15201315 | Künstliche Ablagerungen der Gamsenried-Deponie | dépôts artificiels de la décharge de la Lonza     |
|15201316 | Künstliche Ablagerungen des Riedertals | dépôts artificiels du Riedertal     |
|15201317 | Informell benannte Sackungsmassen | masses tassées nommées informellement     |
|15201318 | Sackungsmasse des Heinzenbergs | masse tassée du Heinzenberg     |
|15201319 | Informell benannte fluviatile Schotter | graviers fluviatiles nommés informellement     |
|15201320 | Schotter und Sand der Rhône | graviers et sables du Rhône     |
|15201321 | Schotter und Sand der Vispa | graviers et sables de la Viège     |
|15201322 | Informell benannter Bachschutt | dépôts torrentiels nommés informellement     |
|15201323 | Bachschutt des Baltschiederbachs | dépôts torrentiels du Baltschiedertal     |
|15201324 | Bachschutt des Bietschbachs | dépôts torrentiels du Bietschbach     |
|15201325 | Bachschutt des Chelchbachs | dépôts torrentiels du Chelchbach     |
|15201326 | Bachschutt der Gamsa | dépôts torrentiels de la Gamsa     |
|15201327 | Bachschutt des Jolibachs | dépôts torrentiels du Jolibach     |
|15201328 | Bachschutt der Lonza | dépôts torrentiels de la Lonza     |
|15201329 | Bachschutt der Saltina | dépôts torrentiels de la Saltina     |
|15201330 | Bachschutt der Vispa | dépôts torrentiels de la Viège     |
|15201331 | Bachschutt der Gürbe | dépôts torrentiels de la Gürbe     |
|15201332 | Bachschutt des Lombachs | dépôts torrentiels du Lombach     |
|15201333 | Pliozäne Ablagerungen | dépôts pliocènes     |
|15201334 | Stockesee-Sediment | Sédiments du Stockesee     |
|15201335 | Strätligen-Till | Till de Strätligen     |
|15201336 | Bärenholz-Till | Till du Bärenholz     |
|15201337 | Wässerifluh-Formation | Formation de la Wässerlifluh     |
|15201338 | Schlyffi-Till | Till de la Schlyffi     |
|15201339 | Brüggstutz-Schotter | Gravier du Brüggstutz     |
|15201340 | Guntelsei-Till | Till de la Guntelsei     |
|15201341 | Guntelsei-Schotter | Gravier de la Guntelsei     |
|15201342 | Steghalden-Schotter | Gravier de la Steghalden     |
|15201343 | Glütschtal-Formation | Formation du Glütschtal     |
|15201344 | Hahni-Schotter | Gravier de Hahni     |
|15203600 | Lirec-Fm.: Amphibolit | Lirec-Fm.: Amphibolit     |
|15203601 | Ergischhorn-Komplex: Brändjispitz-Gabbro | Ergischhorn-Komplex: Brändjispitz-Gabbro     |
|15203602 | Ergischhorn-Komplex: Eklogit | Ergischhorn-Komplex: Eklogit     |
|15203603 | Südegg-Komplex: Prasinit | Südegg-Komplex: Prasinit     |
|15203604 | Südegg-Komplex: Talk-Chloritschiefer | Südegg-Komplex: Talk-Chloritschiefer     |
|15203605 | Gurnigel-Decke: Flysch-3 | Gurnigel-Decke: Flysch-3     |
|15203606 | Gurnigel-Decke: Flysch-2 | Gurnigel-Decke: Flysch-2     |
|15203607 | Hellstätt-Fm. und Flysch 2a | Hellstätt-Fm. und Flysch 2a     |
|15203608 | Aroley-, Marmontains- und St-Chritophe-Fm. | Aroley-, Marmontains- und St-Chritophe-Fm.     |
|15203609 | Südegg-Komplex: Schwarzer Schiefer | Südegg-Komplex: Schwarzer Schiefer     |
|15203610 | Südegg-Komplex: Serpentinit | Südegg-Komplex: Serpentinit     |
|15203611 | Südegg-Komplex: Albitgneis | Südegg-Komplex: Albitgneis     |
|15203612 | Südegg-Komplex: Marmor | Südegg-Komplex: Marmor     |
|15203613 | Südegg-Komplex: Brekzie | Südegg-Komplex: Brekzie     |
|15203614 | Südegg-Komplex: Gips | Südegg-Komplex: Gips     |
|15203615 | Monte-Leone-Decke: Sedimentbedeckung | Monte-Leone-Decke: Sedimentbedeckung     |
|15203616 | Monte-Leone-Decke: Dogger-Malm | Monte-Leone-Decke: Dogger-Malm     |
|15203617 | Monte-Leone-Decke: Dogger-Malm: Glimmerschiefer | Monte-Leone-Decke: Dogger-Malm: Glimmerschiefer     |
|15201507 | Reusstal-Seebodensediment | Reusstal-Seebodensediment     |
|15201508 | Wyna-Schotter | Wyna-Schotter     |
|15201509 | Rickenbach-Schotter | Rickenbach-Schotter     |
|15201510 | Ermensee-Schotter | Ermensee-Schotter     |
|15201489 | Rüdelwald-Schotter | Rüdelwald-Schotter     |
|15201512 | Ämmet-Schotter | Ämmet-Schotter     |
|15201513 | Homberg-Till | Homberg-Till     |
|15201514 | Lindenberg-Till | Lindenberg-Till     |
|15201515 | Heubeerihübel-Schotter | Heubeerihübel-Schotter     |
|15201516 | Ritzhans-Schotter | Ritzhans-Schotter     |
|15201517 | Unterdorf-Schotter | Unterdorf-Schotter     |
|15201518 | Schönegg-Formation | Schönegg-Formation     |
|15201519 | Säckingen-Schotter | Säckingen-Schotter     |
|15201520 | Bruderhäusle-Schotter | Bruderhäusle-Schotter     |
|15201521 | Mumpf-Schotter | Mumpf-Schotter     |
|15201522 | Riedmatt-Schotter | Riedmatt-Schotter     |
|15201523 | Beuggen-Schotter | Beuggen-Schotter     |
|15201524 | Feldhof-Schotter | Feldhof-Schotter     |
|15201525 | Spärgacher-Schotter | Spärgacher-Schotter     |
|15205068 | Morcote-Vulkanite: Basalt | Basalte permien du Sudalpin     |
|15205069 | Morcote-Vulkanite: Basaler Tuf | Tuf basal permien du Sudalpin     |
|15205070 | Manno-Fm. | Formation de Manno     |
|15205071 | Südalpin: Paläogen-Neogen | Südalpin: Paläogen-Neogen     |
|15205072 | Südalpin: Kreide | Südalpin: Kreide     |
|15205073 | Südalpin: Radiolarit-Aptychenkalk | Südalpin: Radiolarit-Aptychenkalk     |
|15205074 | Südalpin: Dogger | Südalpin: Dogger     |
|15205075 | Südalpin: Lias | Südalpin: Lias     |
|15205076 | Südalpin: Trias | Südalpin: Trias     |
|15205077 | Südalpin: Permo-Karbon | Südalpin: Permo-Karbon     |
|15205078 | Südalpin: Grundgebirge | Südalpin: Grundgebirge     |
|15205079 | Südalpin: Variszische Intrusiva | roches intrusives varisques du Sudalpin     |
|15205080 | San-Bernardo-Gneis | San-Bernardo-Gneis     |
|15205081 | Südalpin: Prävariszische Metasedimente | métasédiments anté-varisques du Sudalpin     |
|15205082 | Stabbiello-Gneis | Stabbiello-Gneis     |
|15205083 | Giumello-Gneis | Giumello-Gneis     |
|15205084 | Ceneri-Gneis | Ceneri-Gneis     |
|15205085 | Südalpin: Proterozoische und paläozoische mafische und ultramafische Gesteine | Südalpin: Proterozoische und paläozoische mafische und ultramafische Gesteine     |
|15205086 | Mont-Morion-Granit | Mont-Morion-Granit     |
|15203487 | Breithorn-Serpentinit | Serpentinite du Breithorn     |
|15203488 | Loranco-Amphibolit | Amphibolite de Loranco     |
|15203489 | Andolla-Eklogit | Éclogite d&#39;Andolla     |
|15203490 | Roz-Schiefer | Schistes du Roz     |
|15203491 | Ramosch-Zone: Ophiolith | Ophiolite de la zone de Ramosch     |
|15203492 | Arosa-Decke: Metasedimente | Métasédiments de la nappe d&#39;Arosa     |
|15203493 | Totalp-Serpentinit | Serpentinite de la Totalp     |
|15203494 | Maran-Brekzie | Brèche de Maran     |
|15203495 | Tumpriv-Fm.: Solis-Kalk | Calcaire de Solis     |
|15203496 | Platta-Decke: Metasedimente | Métasédiments de la nappe du Platta     |
|15203497 | Flix-Sch. | Schistes de Flix     |
|15203498 | Platta-Decke: Calpionellenkalk | Calcaire à calpionelles de la nappe du Platta     |
|15203499 | Falotta-Radiolarit | Radiolarite de la nappe du Platta     |
|15203500 | Platta-Decke: Ophiolith | Ophiolite de la nappe du Platta     |
|15203501 | Vignun-Gneis | Gneiss de Vignone     |
|15203502 | Avers-Decke: Metasedimente | Métasédiments de la nappe de l&#39;Avers     |
|15203503 | Avers-Decke: Ophiolith | Ophiolite de la nappe de l&#39;Avers     |
|15203504 | Tasna-Decke: Couches Rouges | Brekzie-Formation     |
|15203505 | Tasna-Decke: Tristel-Fm.: Minschun-Brekzie | Brèche du Minschun     |
|15201198 | Willisau-Schotter | Gravier de Willisau     |
|15201199 | Wolhusen-Schotter | Gravier de Wolhusen     |
|15201200 | Wiggen-Schotter | Gravier de la Wigger     |
|15201201 | Menzingen-Schotter | Gravier de Menzingen     |
|15201202 | La-Tuffière-Schotter | Gravier de la Tuffière     |
|15201203 | Gontenschwil-Lehm | Limon de Gontenschwil     |
|15201204 | Mooslerau-Lehm | Limon du Mooslerau     |
|15201205 | Triengen-Schotter | Gravier de Triengen     |
|15201206 | Triengen-Lehm | Limon de Triengen     |
|15201207 | Sihl-Schotter | Gravier de la Sihl     |
|15201208 | Haselbach-Schotter | Gravier du Haselbach     |
|15201209 | Jonen-Schotter | Gravier de Jonen     |
|15201210 | Aabach-Schotter | Gravier de l&#39;Aabach     |
|15201211 | Starrberg-Schotter | Gravier de Starrberg     |
|15201212 | Port-Stauschotter | Gravier de Port     |
|15201213 | Rempen-Stauschotter | Gravier de Rempen     |
|15201214 | Dagmersellen-Vorstoss | Avancée glaciaire de Dagmersellen     |
|15201215 | Oftringen-Schotter | Gravier d&#39;Oftringen     |
|15201216 | Zelg-Schotter | Gravier de Zelg     |
|15201217 | Forst-Schotter | Gravier du Forst     |
|15201218 | Raintal-Deltaschotter | Gravier du Raintal     |
|15201219 | Kleinhöchstetten-Kies-Sand-Komplex | Complexe sablo-graveleux de Kleinhöchstetten     |
|15201220 | Krauchthal-Schotter | Gravier du Krauchthal     |
|15201221 | Brandflue-Schotter | Gravier de la Brandflue     |
|15201222 | Küsnacht-Schotter | Gravier de Küsnacht     |
|15201223 | Chatzenstrick-Schotter | Gravier du Chatzenstrick     |
|15201224 | Rabennest-Schotter | Gravier du Rabennest     |
|15201225 | Ratengütsch-Schotter | Gravier du Ratengütsch     |
|15201226 | Scherenspitz-Schotter | Gravier du Scherenspitz     |
|15201227 | Walsenhaus-Schotter | Gravier de Walsenhaus     |
|15201228 | Richterswil-Seeton | Argile lacustre de Richterswil     |
|15201229 | Schwanden-Schotter | Gravier de Schwanden     |
|15201230 | Reidbach-Schotter | Gravier du Reidbach     |
|15201231 | Zell-Schotterkomplex | Gravier de Zell     |
|15201232 | Gubel-Schotter | Gravier de Gubel     |
|15201233 | Chälen-Schotter | Gravier de Chälen     |
|15201234 | Chälen-Till | Till de Chälen     |
|15201235 | Sihlsprung-Schotter | Gravier du Sihlsprung     |
|15201236 | Kollbrunn-Schotter | Gravier de Kollbrunn     |
|15201237 | Walenberg-Schotter | Gravier de Walenberg     |
|15203618 | Monte-Leone-Decke: Dogger-Malm: Marmor | Monte-Leone-Decke: Dogger-Malm: Marmor     |
|15203619 | Monte-Leone-Decke: Dogger: Konglomerat | Monte-Leone-Decke: Dogger: Konglomerat     |
|15203620 | Monte-Leone-Decke: Lias | Monte-Leone-Decke: Lias     |
|15203621 | Monte-Leone-Decke: Lias: Sandstein | Monte-Leone-Decke: Lias: Sandstein     |
|15203622 | Monte-Leone-Decke: Lias: Konglomerat | Monte-Leone-Decke: Lias: Konglomerat     |
|15203623 | Monte-Leone-Decke: Trias | Monte-Leone-Decke: Trias     |
|15203624 | Monte-Leone-Decke: Quarzitische Trias | Monte-Leone-Decke: Quarzitische Trias     |
|15203625 | Pizzo-del-Vallone-Decke: Sedimentbedeckung | Pizzo-del-Vallone-Decke: Sedimentbedeckung     |
|15203626 | Pizzo-del-Vallone-Decke: Dogger-Malm | Pizzo-del-Vallone-Decke: Dogger-Malm     |
|15203627 | Pizzo-del-Vallone-Decke: Dogger-Malm: Marmor | Pizzo-del-Vallone-Decke: Dogger-Malm: Marmor     |
|15203628 | Pizzo-del-Vallone-Decke: Dogger-Malm: Glimmerschiefer | Pizzo-del-Vallone-Decke: Dogger-Malm: Glimmerschiefer     |
|15203629 | Pizzo-del-Vallone-Decke: Dogger-Malm: Vulkanit | Pizzo-del-Vallone-Decke: Dogger-Malm: Vulkanit     |
|15203630 | Pizzo-del-Vallone-Decke: Lias | Pizzo-del-Vallone-Decke: Lias     |
|15203631 | Pizzo-del-Vallone-Decke: Trias | Pizzo-del-Vallone-Decke: Trias     |
|15203632 | Mont-Fort-Decke: Sedimentbedeckung | Mont-Fort-Decke: Sedimentbedeckung     |
|15203633 | Mont-Fort-Decke: Trias | Mont-Fort-Decke: Trias     |
|15203634 | Mont-Fort-Decke: Trias: Rauwacke | Mont-Fort-Decke: Trias: Rauwacke     |
|15201526 | Wagenmoos-Till | Till du Wagenmoos     |
|15201527 | Niderstalden-Schotter | Gravier de Niderstalden     |
|15201528 | Zulgtal-Schotter | Gravier du Zulgtal     |
|15201529 | Spiez-Schotter | Gravier de Spiez     |
|15201530 | Hahni-Till | Till de Hahni     |
|15201531 | Bergsturzablagerung von Ralligen (im Thunersee) | Dépôt d&#39;écroulement de Ralligen (dans le lac de Thoune)     |
|15205087 | Pointe-d&#39;Otemma-Granodiorit | Pointe-d&#39;Otemma-Granodiorit     |
|15205088 | Bouquetins-Quarzdiorit | Bouquetins-Quarzdiorit     |
|15205089 | Tête-de-Valpelline-Phyllit | Tête-de-Valpelline-Phyllit     |
|15205090 | Arolla-Einheit: Série rubanée | Arolla-Einheit: Série rubanée     |
|15205091 | Sassa-Metagabbro | Sassa-Metagabbro     |
|15205092 | Maia-Metagabbro | Maia-Metagabbro     |
|15205093 | Losone-Schiefer | Losone-Schiefer     |
|15205094 | Pizzo-Leone-Gneis | Pizzo-Leone-Gneis     |
|15205095 | Fornale-Gabbro | Fornale-Gabbro     |
|15205096 | Matterhorn-Gabbro | Matterhorn-Gabbro     |
|15205097 | Berrio-Gabbro | Berrio-Gabbro     |
|15205098 | Grand-Dolin-Brekzie | Grand-Dolin-Brekzie     |
|15205099 | Meride-Fm.: Oberer Kalk | Partie supérieure du Calcaire de Meride     |
|15205100 | Meride-Fm.: Unterer Kalk | Partie inférieure du Calcaire de Meride     |
|15205101 | Meride-Fm.: Dolomit-Band | Dolomit-Band (Fm. de Meride)     |
|15205102 | Dent-Blanche-Decke: Lias: Kalkstein | Calcaire du Groupe du Dolin     |
|15205103 | Dent-Blanche-Decke: Trias: Dolomit | Dolomie du Groupe du Dolin     |
|15205104 | Dent-Blanche-Decke: Trias: Rauwacke | Cornieule du Groupe du Dolin     |
|15205105 | Dent-Blanche-Decke: Trias: Quarzit | Quartzite du Groupe du Dolin     |
|15205106 | Arolla-Orthogneis: Leukokrater Gneis | Orthogneiss du Groupe d&#39;Arolla, leucocrate     |
|15205107 | Arolla-Orthogneis: Augengneis | Orthogneiss du Groupe d&#39;Arolla, oeillé     |
|15203506 | Tasna-Decke: Prävariszisches Grundgebrige | Socle cristallin de la nappe de la Tasna     |
|15203507 | Piz-del-Palo-Gneis | Gneiss du Piz del Palo     |
|15203508 | Truzzo-Granit | Granite de Truzzo     |
|15203509 | Rebi-Gneis | Gneiss de Rebi     |
|15203510 | Brione-Gabbro | Gabbro de Brione     |
|15203511 | Gruf-Migmatit | Migmatite du Gruf     |
|15203512 | Adula-Decke: Basaler Gneis | Adula-D.: Basaler Gneis     |
|15203513 | Val-Chironico-Gneis | Gneiss du Val Chironico     |
|15203514 | Ganna-Gneis | Gneiss de Ganna     |
|15203515 | Adula-Decke: Albit-Oligoklasgneis | Adula-D.: Albit-Oligoklasgneis     |
|15203516 | Sivigia-Gneis | Gneiss de Sivigia     |
|15203517 | Aula-Spruga-Gneiskomplex | Complexe gneissique d&#39;Aula-Spruga     |
|15203518 | Lizun-Grünschiefer | Schistes verts du Lizun     |
|15203519 | Rossi-Fm. | Formation des Rossi     |
|15203520 | Bosco-Gneis | Gneiss de Bosco     |
|15203521 | Batnall-Gneis | Gneiss du Batnall     |
|15203522 | Seron-Fm.: Sandig-kalkige Fazies | Seron-Fm.: Sandig-kalkige Fazies     |
|15203523 | Seron-Fm.: Konglomerat-dominierte Fazies | Seron-Fm.: Konglomerat-dominierte Fazies     |
|15203524 | Frutigen-Fm.: Konglomerat-dominierte Fazies | Frutigen-Fm.: Konglomerat-dominierte Fazies     |
|15201238 | Ritteren-Schotterkomplex | Complexe graveleux de Ritteren     |
|15201239 | Vorholz-Schotter | Gravier du Vorholz     |
|15201240 | Gutsch-Schotter | Gravier du Gutsch     |
|15201241 | Junkerenwald-Schotter | Gravier du Junkerenwald     |
|15201242 | Chräjeloch-Schotter | Gravier du Chräjeloch     |
|15201243 | Butteberg-Schotter | Gravier du Butteberg     |
|15201244 | Höchi-Schotter | Gravier du Höchi     |
|15201245 | Heitere-Schotter | Gravier deHeitere     |
|15201246 | Holziken-Schotter | Gravier de Holziken     |
|15201247 | Ruedertal-Schotter | Gravier du Ruedertal     |
|15201248 | Bänkel-Schotter | Gravier de Bänkel     |
|15201249 | Quartär, undifferenziert | Quaternaire, indifférencié     |
|15201250 | Deckenschotter, undifferenziert | Deckenschotter, indifférencié     |
|15201251 | Girenbad-Schotter | Gravier du Girenbad     |
|15201252 | Sagenbach-Schotter | Gravbier du Sagenbach     |
|15201253 | Schrotzburg-Schotter | Gravier de la Schrotzburg     |
|15201254 | Schrotzburg-Till | Till de la Schrotzburg     |
|15201255 | Bohlingen-Schotter | Gravier de Bohlingen     |
|15201256 | Bannholz-Schotter | Gravier du Bannholz     |
|15201257 | Hungerbol-Schotter | Gravier d&#39;Hungerbol     |
|15201258 | Chilchstapfen-Schotter | Gravier de la Chilchstapfen     |
|15203635 | Métailler-Fm.: Quarzit | Métailler-Fm.: Quarzit     |
|15203636 | Métailler-Fm.: Glimmerschiefer | Métailler-Fm.: Glimmerschiefer     |
|15203637 | Métailler-Fm.: Chloritoid-Glimmerschiefer | Métailler-Fm.: Chloritoid-Glimmerschiefer     |
|15203638 | Distulberg-Fm.: Schiefer | Distulberg-Fm.: Schiefer     |
|15203639 | Distulberg-Fm.: Albitgneis | Distulberg-Fm.: Albitgneis     |
|15203640 | Barrhorn-Einheit: Trias | Barrhorn-Einheit: Trias     |
|15203641 | Siviez-Mischabel-Decke: Aplit | Siviez-Mischabel-Decke: Aplit     |
|15203642 | Siviez-Mischabel-Decke: Pegmatit | Siviez-Mischabel-Decke: Pegmatit     |
|15203643 | Lirec-Fm.: Leukokrater Mikroklingneis | Lirec-Fm.: Leukokrater Mikroklingneis     |
|15203644 | Adlerflüe-Fm.: Leukokrater Gneiss | Adlerflüe-Fm.: Leukokrater Gneiss     |
|15203645 | Ergischhorn-Komplex: Leukokrater aplitischer Gneis | Ergischhorn-Komplex: Leukokrater aplitischer Gneis     |
|15203646 | Stalden-Gneiskomplex | Stalden-Gneiskomplex     |
|15203647 | Stalden-Gneiskomplex: Ahorn-Augengneis | Stalden-Gneiskomplex: Ahorn-Augengneis     |
|15203648 | Stalden-Gneiskomplex: Amphibolit | Stalden-Gneiskomplex: Amphibolit     |
|15203649 | Printse-Fm.: Konglomerat | Printse-Fm.: Konglomerat     |
|15203650 | Printse-Fm.: Graphitschiefer | Printse-Fm.: Graphitschiefer     |
|15203651 | Portjengrat-Decke: Kalzitmarmor | Portjengrat-Decke: Kalzitmarmor     |
|15203652 | Portjengrat-Decke: Dolomitmarmor | Portjengrat-Decke: Dolomitmarmor     |
|15205108 | Arolla-Orthogneis: Mylonit | Orthogneiss du Groupe d&#39;Arolla, mylonitique     |
|15205109 | Arolla-Einheit: Série rubanée: Mylonit | Gneiss du Groupe d&#39;Arolla, mylonitique     |
|15205110 | Arolla-Einheit: Série rubanée: Mikroaugengneis | Gneiss du Groupe d&#39;Arolla, micro-oeillé     |
|15205111 | Arolla-Orthogneis: Granitoid | Métagranitoïde du Groupe d&#39;Arolla     |
|15205112 | Arolla-Einheit: Basisches Gestein | Métaroche basique du Groupe d&#39;Arolla     |
|15205113 | Arolla-Einheit: Basisches Gestein: Mylonitisch | Métaroche basique du Groupe d&#39;Arolla, mylonitique     |
|15205114 | Arolla-Einheit: Prasinit | Prasinite du Groupe d&#39;Arolla     |
|15205115 | Arolla-Einheit: Hornblendegabbro | Gabbro à horneblende du Groupe d&#39;Arolla     |
|15205116 | Arolla-Einheit: Ultramafisches Gestein | Roche ultramafique du Groupe d&#39;Arolla     |
|15205117 | Arolla-Einheit: Paragneis | Paragneiss du Groupe d&#39;Arolla     |
|15205118 | Arolla-Einheit: Glimmerschiefer | Micaschiste du Groupe d&#39;Arolla     |
|15205119 | Valpelline-Einheit: Mylonit | Mylonite du Groupe de Valpelline     |
|15205120 | Valpelline-Einheit: Amphibolit | Amphibolite du Groupe de Valpelline     |
|15205121 | Valpelline-Einheit: Marmor | Marbre du Groupe de Valpelline     |
|15205122 | Valpelline-Einheit: Migmatit | Migmatite du Groupe de Valpelline     |
|15205123 | Roisan-Cignana-Zone: Marmor | Marbre de Roisan     |
|15205124 | Musella-Granit | Granite de Musella     |
|15205125 | Sella-Granodiorit | Granodiorite de la Sella     |
|15205126 | Marinelli-Fm. | Formation de Marinelli     |
|15205127 | Margna- und Sella-Decke: Grundgebirge | socle cristallin de la nappe de la Margna-Sella     |
|15203525 | Frutigen-Fm.: Schiefrige Fazies | Frutigen-Fm.: Schiefrige Fazies     |
|15203526 | Zone Submédiane: Gips | Gypse de la Zone Submédiane     |
|15203527 | Zentralschweizerische Klippen: Keuper | Karpatischer Keuper     |
|15203528 | Zwischenmythen-Mergel | Marne de Zwischenmythen     |
|15203529 | Arosa-Decke: Cenomanbrekzien-Serie | Cenomanbrekzien-Serie     |
|15203530 | Arosa-Decke: Bettlerjoch-Brekzie | Brèche du Bettlerjoch     |
|15203531 | Arosa-Decke: Bargella-Brekzie | Brèche de Bargella     |
|15203532 | Adula-Decke: Kalkschiefer und Marmor | Adula-D.: Kalkschiefer und Marmor     |
|15203533 | Salahorn-Fm.: Metaplutonit | Formation du Salahorn: métaplutonite     |
|15203534 | Salahorn-Fm.: Paragneis | Formation du Salahorn: paragneiss     |
|15203535 | Adula-Decke: Ultramafisches Gestein | Adula-D.: Ultramafitit     |
|15203536 | Cima-Lunga-Decke: Kalkschiefer und Marmor | Cima-Lunga-D.: Kalkschiefer und Marmor     |
|15203537 | Cima-Lunga-Decke: Dolomitmarmor | Cima-Lunga-D.: Dolomitmarmor     |
|15203538 | Cima-Lunga-Decke: Paragneis | Cima-Lunga-D.: Paragneis     |
|15203539 | Vacarisc-Gneis | Gneiss de Vacarisc     |
|15203540 | Rognoi-Gneis | Gneiss de Rognoi     |
|15203541 | Cima-Lunga-Decke: Granatit | Cima-Lunga-D.: Granatit     |
|15203542 | Cima-Lunga-Decke: Amphibolit | Cima-Lunga-D.: Amphibolit     |
|15203543 | Cima-Lunga-Decke: Eklogit | Cima-Lunga-D.: Eklogit     |
|15203653 | Portjengrat-Decke: Arkose | Portjengrat-Decke: Arkose     |
|15203654 | Portjengrat-Decke: Grundgebirge | Portjengrat-Decke: Grundgebirge     |
|15203655 | Gornergrat-Decke: Kalkschiefer, sandiger Marmor, Brekzie | Gornergrat-Decke: Kalkschiefer, sandiger Marmor, Brekzie     |
|15203656 | Gornergrat-Decke: Trias | Gornergrat-Decke: Trias     |
|15203657 | Gornergrat-Decke: Phengit-Albitgneis | Gornergrat-Decke: Phengit-Albitgneis     |
|15203658 | Gornergrat-Decke: Basisches Ganggestein | Gornergrat-Decke: Basisches Ganggestein     |
|15203659 | Gornergrat-Decke: Granat-Muskovit-Schiefer | Gornergrat-Decke: Granat-Muskovit-Schiefer     |
|15203660 | Frilihorn-Decke: Trias | Frilihorn-Decke: Trias     |
|15203661 | Frilihorn-Decke: Trias: Rauwacke | Frilihorn-Decke: Trias: Rauwacke     |
|15203662 | Garda-Bordon-Fm.: Série feuilletée | Garda-Bordon-Fm.: Série feuilletée     |
|15203663 | Garda-Bordon-Fm.: Quarzschiefer | Garda-Bordon-Fm.: Quarzschiefer     |
|15203664 | Serra-Neire-Serpentinit | Serra-Neire-Serpentinit     |
|15203665 | Zermatt-Saas-Decke: Eklogit | Zermatt-Saas-Decke: Eklogit     |
|15203666 | Zermatt-Saas-Decke: Metapyroxenit | Zermatt-Saas-Decke: Metapyroxenit     |
|15203667 | Zermatt-Saas-Decke: Metagabbro | Zermatt-Saas-Decke: Metagabbro     |
|15203668 | Zermatt-Saas-Decke: Rodingit | Zermatt-Saas-Decke: Rodingit     |
|15203669 | Zermatt-Saas-Decke: Talkschiefer | Zermatt-Saas-Decke: Talkschiefer     |
|15203670 | Lengenbach-Dolomitmarmor | Lengenbach-Dolomitmarmor     |
|15204001 | God-Drosa-Flysch | Flysch du God Drosa     |
|15205128 | Margna- und Sella-Decke: Variszische Intrusiva | roches intrusives de la nappe de la Margna-Sella     |
|15205129 | Margna- und Sella-Decke: Prävariszisches Grundgebirge | socle polycyclique anté-varisque de la nappe de la Margna-Sella     |
|15205130 | Margna-Decke: Metaarkose, Orthogneise | Métaarkose, orthogneiss anté-varisque     |
|15205131 | Sesia-Decke: Orthogneis | orthogneiss de la nappe de Sesia     |
|15205132 | Sesia-Decke: Micascisti Eclogitici | micaschiste de la nappe de Sesia     |
|15205133 | Finero-Peridotit | Péridotite de Finero     |
|15205134 | Ivrea Mafischer Komplex | Complexe Mafique d&#39;Ivrée     |
|15205135 | Sesia-Decke: Zona Dioritico-Kinzigitica | Zona Dioritico-Kinzigitica     |
|15205136 | Südalpin: Prävariszischer Orthogneis | orthogneiss anté-varisques du Sudalpin     |
|15205137 | Pontida-Fm. | Formation de Pontida     |
|15205138 | Arolla-Einheit: Metagranit | Arolla-Einheit: Metagranit     |
|15205139 | Arolla-Einheit: Leukokrater Granitgneis | Arolla-Einheit: Leukokrater Granitgneis     |
|15206001 | Periadriatische Vulkanite | roches volcaniques cénozoïques péri-adriatiques     |
|15206002 | Novate-Intrusiva | Intrusion de Novate     |
|15206003 | Bergell-Intrusiva | Intrusion du Bergell     |
|15206004 | Adamello-Intrusiva | Intrusion de l&#39;Adamello     |
|15206005 | Melirolo-Augengneis | Melirolo-Augengneis     |
|15206006 | Bergell-Intrusiva: Granodioritische Fazies | Bergell-Intrusiva: Granodioritische Fazies     |
|15206007 | Bergell-Intrusiva: Tonalitische Fazies | Bergell-Intrusiva: Tonalitische Fazies     |
|15203544 | Cima-Lunga-Decke: Ultramafisches Gestein | Cima-Lunga-D.: Ultramafitit     |
|15203545 | Personico-Gneis | Gneiss de Personico     |
|15203546 | Leventina-Gneis: Oberer Teil | Gneiss de la Leventina: partie supérieure     |
|15203547 | Leventina-Gneis: Unterer Teil | Gneiss de la Leventina: partie inférieure     |
|15203548 | Leventina-Decke: Kalksilikatfels | Leventina-D.: Kalksilikatfels     |
|15203549 | Leventina-Decke: Leukogneis | Leventina-D.: Leukogneis     |
|15203550 | Leventina-Decke: Paragneis | Leventina-D.: Paragneis     |
|15203551 | Leventina-Decke: Amphibolit | Leventina-D.: Amphibolit     |
|15203552 | Maggia-Decke: Amphibolit | Maggia-D.: Amphibolit     |
|15203553 | Simano-Decke: Kalkmarmor | Simano-D.: Kalkmarmor     |
|15203554 | Simano-Decke: Dolomitmarmor | Simano-D.: Dolomitmarmor     |
|15203555 | Simano-Decke: Paragneis | Simano-D.: Paragneis     |
|15203556 | Renten-Gneis | Gneiss de Renten     |
|15203557 | Legiuna-Gneis | Gneiss de Legiuna     |
|15203558 | Simano-Decke: Amphibolit | Simano-D.: Amphibolit     |
|15203559 | Simano-Decke: Ultramafisches Gestein | Simano-D.: Ultramafitit     |
|15203560 | Alpbach-Schiefer | Schistes de l&#39;Alpbach     |
|15203561 | Arosa-Decke: Gabbro | Arosa-D.: Gabbro     |
|15203562 | Zentralschweizerische Klippen: Flysch | Klippen-Flysch     |
|15204002 | Chanèls-Fm. | Formation de Chanèls     |
|15204003 | Lech-Fm. | Formation de Lech     |
|15204004 | Emmat-Fm. | Formation d&#39;Emmat     |
|15204005 | Russenna-Fm. | Formation du (Munt) Russenna     |
|15204006 | Ammergau-Fm. | Formation d&#39;Ammergau     |
|15204007 | Blais-Fm. | Formation du Blais     |
|15204008 | Blais-Fm.: Plattas-Mb. | Membre de Plattas     |
|15204009 | Ruhpolding-Fm. | Formation de Ruhpolding     |
|15204010 | Ostalpin: Dogger | Groupe du (Piz) Saluver     |
|15204011 | Saluver-Fm. | Formation du (Piz) Saluver     |
|15204012 | Bardella-Fm. | Formation de Bardella     |
|15204013 | Salteras-Fm. | Formation du (Piz) Salteras     |
|15204014 | Salamun-Brekzie | Brèche de Salamun     |
|15204015 | Err-Brekzie | Brèche d&#39;Err     |
|15204016 | Allgäu-Fm. | Formation de l&#39;Allgäu     |
|15204017 | Allgäu-Fm.: Mezzaun-Mb. | Membre du (Piz) Mezzaun     |
|15204018 | Allgäu-Fm.: Blaisun-Mb. | Membre du (Piz) Blaisun     |
|15204019 | Allgäu-Fm.: Trupchun-Mb. | Membre du (Val) Trupchun     |
|15204020 | Agnelli-Fm. | Formation d&#39;Agnelli     |
|15204021 | Agnelli-Fm.: Knollenkalk-Fazies | Calcaire d&#39;Adnet     |
|15204022 | Agnelli-Fm.: Echinodermenkalk-Fazies | Calcaire de Hierlatz     |
|15204023 | Alv-Brekzie | Brèche d&#39;Alv     |
|15204024 | Kössen-Fm. | Formation de Kössen     |
|15204025 | Kössen-Fm.: Zirmenkopf-Mb. | Calcaire du Zirmenkopf     |
|15206008 | Monte-Bassetta-Quarzdiorit | Monte-Bassetta-Quarzdiorit     |
|15206009 | Sorico-Tonalit | Sorico-Tonalit     |
|15206010 | Jorio-Tonalit | Jorio-Tonalit     |
|15206011 | Val-Masino-Granodiorit | Val-Masino-Granodiorit     |
|15206012 | Alpe-Cameraccio-Granodiorit | Alpe-Cameraccio-Granodiorit     |
|15206013 | Monte-Rosso-Mikrogranit | Monte-Rosso-Mikrogranit     |
|15206014 | Zocca-Aplit | Zocca-Aplit     |
|15206015 | San-Fedelino-Granit | San-Fedelino-Granit     |
|15206016 | Undifferenzierte Einheit | Undifferenzierte Einheit     |
|15206017 | Undifferenzierte lithologische Einheit: Tektonische Brekzie | Undifferenzierte lithologische Einheit: Tektonische Brekzie     |
|15206018 | Lochsiten-Kalk | Lochsiten-Kalk     |
|15206019 | Salleren-Brekzie | Salleren-Brekzie     |
|15206020 | Undifferenzierte lithologische Einheit | Undifferenzierte lithologische Einheit     |
|15206021 | Undifferenzierte lithologische Einheit: Gips | Undifferenzierte lithologische Einheit: Gips     |
|15206022 | Undifferenzierte lithologische Einheit: Rauwacke | Undifferenzierte lithologische Einheit: Rauwacke     |
|15206023 | Undifferenzierte lithologische Einheit: Dolomitmarmor | Undifferenzierte lithologische Einheit: Dolomitmarmor     |
|15206024 | Undifferenzierte lithologische Einheit: Ganggestein | Undifferenzierte lithologische Einheit: Ganggestein     |
|15206025 | Undifferenzierte stratigraphische Einheit: Lias | Lias, indifférencié     |
|15203055 | Chauderon-Fm. | Formation du Chauderon     |
|15203056 | Vudalla-Fm. | Formation de la Vudalla     |
|15203057 | Vudalla-Fm.: Bois-de-Luan-Mb. | Membre du Bois de Luan     |
|15203058 | Vudalla-Fm.: Agreblierai-Mb. | Membre d&#39;Agreblierai     |
|15203059 | Col-de-Tompey-Fm. | Formation du Col de Tompey     |
|15203060 | Plan-Falcon-Fm. | Formation de Plan Falcon     |
|15203061 | Dolomies Blondes | Dolomies Blondes     |
|15203062 | Clôt-la-Cime-Fm. | Formation de Clôt la Cime     |
|15203066 | Griggeli-Fm. | Formation du Griggeli     |
|15203067 | Griggeli-Fm.: Mythen-Kieselkalk | Calcaire siliceux des Mythen     |
|15203068 | Griggeli-Fm.: Griggeli-Bk. | Banc du Griggeli     |
|15203069 | Gibel-Fm. | Formation de Gibel     |
|15203070 | Gibel-Fm.: Rämsi-Mb. | Membre de Rämsi     |
|15203071 | Gibel-Fm.: Gibel-Mb. | Membre de Gibel     |
|15203072 | Gibel-Fm.: Steinberg-Konglomerat | Conglomérat du Steinberg     |
|15203073 | Gibel-Fm.: Musenalp-Mb. | Membre de la Musenalp     |
|15203074 | Stanserhorn-Fm. | Formation du Stanserhorn     |
|15203075 | Stanserhorn-Fm.: Zoophycos-Sch. | Couches à Zoophycos (Fm. du Stanserhorn)     |
|15203076 | Stanserhorn-Fm.: Spis-Kalk | Calcaire de la Spis     |
|15203077 | Stanserhorn-Fm.: Posidonienschiefer | Schistes à Posidonies (Fm. du Stanserhorn)     |
|15200503 | Öhningen-Fm. | Formation d&#39;Öhningen     |
|15200504 | Öhningen-Fm.: Öhningen-Süsswasserkalk | Calcaire d&#39;eau douce d&#39;Öhningen     |
|15200505 | Öhningen-Fm.: Ramschwag-Nagelfluh | Poudingue de la Ramschwag     |
|15200506 | Hörnli-Fm.: Seerücken-Tuffit | Tuffite du Seerücken     |
|15200507 | Meilen-Fm. | Couches de Meilen     |
|15200508 | Meilen-Fm.: Wulp-Rotzone | Rotzone Wulp     |
|15200509 | Käpfnach-Fm. | Formation de Käpfnach     |
|15200510 | OSM-J: Juranagelfluh: Mergel-dominierte Fazies | Juranagelfluh-Mergel     |
|15200511 | Golat-Süsswasserkalk | Calcaire d&#39;eau douce du Golat     |
|15200512 | Belpberg-Fm.: Fossilreicher Horizont | Petrefaktenlager (Fm. du Belpberg)     |
|15200513 | Fm. der Granitischen Molasse: Hombach-Mb. | Formation du Hombach     |
|15200514 | Homberg-Fm. | Membre de Homberg     |
|15200515 | Gäbris-Nagelfluh | Poudingue du Gäbris     |
|15200516 | Gäbris-Nagelfluh: Gstaldenbach-Mb. | Membre du Gstaldenbach     |
|15200517 | Gäbris-Nagelfluh: Heiden-Mb. | Membre de Heiden     |
|15200518 | Gäbris-Nagelfluh: Klusbach-Mb. | Membre du Klusbach     |
|15200519 | Gäbris-Nagelfluh: Eggen-Mb. | Membre de l&#39;Eggen     |
|15200520 | Gäbris-Sulzbach: Sulzbach-Mb. | Membre de Sulzbach     |
|15200521 | Gäbris-Sulzbach: Sulzbach-Mb.: Kalknagelfluh | Poudingue de Sulzbach     |
|15200522 | Kronberg-Nagelfluh: Pfingstboden-Mb. | Membre du Pfingstboden     |
|15202140 | Vieux-Emosson-Fm. | Formation du Vieux Emosson     |
|15202141 | Mels-Fm. | Formation de Mels     |
|15202142 | Helvetikum: Spät- bis postvariszische Sedimente und Vulkanite | Permo-Carbonifère de l&#39;Helvétique     |
|15202143 | Helvetikum: Verrucano | Groupe du Verrucano     |
|15202144 | Glarner Verrucano | Verrucano de Glaris     |
|15202145 | Schönbühl-Fm. | Formation de Schönbüel     |
|15202146 | Schönbühl-Fm.: Quarzit | Quartzite de Schönbüel     |
|15202147 | Kärpf-Fm. | Formation du Kärpf     |
|15202148 | Karrenstock-Fm. | Formation du Karrenstock     |
|15202149 | Murgtal-Fm.: Chartegg-Mb. | Membre de la Chartegg     |
|15202150 | Karrenstock-Fm.: Fuggstock-Mb. | Membre du Fuggstock     |
|15202151 | Mären-Fm. | Formation de la Mären(egg)     |
|15202152 | Üblital-Fm. | Formation de l&#39;Üblital     |
|15202153 | Ilanz-Verrucano | Verrucano d&#39;Ilanz     |
|15202154 | Vernayaz-Fm. | Formation de Vernayaz     |
|15202155 | Vernayaz-Fm.: Salvan-Mb. | Membre de Salvan     |
|15202156 | Vernayaz-Fm.: Salvan-Mb.: Vallorcine-Konglomerat | Conglomérat de Vallorcine     |
|15202157 | Aar-Massiv: Spät- bis postvariszische Intrusiva | Groupe du Haslital     |
|15202158 | Gastern-Granit | Granite de Gastern     |
|15202159 | Mittagflue-Granit | Granite de la Mittagflue     |
|15202423 | Covayes-Fm. | Formation des Covayes     |
|15202424 | Javrex-Fm. | Formation du Javrex     |
|15202425 | Javrex-Fm.: Mergelstein-Fazies | «Marnes noires pyriteuses»     |
|15202426 | Javrex-Fm.: Kalksandstein-Fazies | «Calcaires gréso-glauconieux»     |
|15202427 | Montsalvens-Kalkarenit | «Calcarénites beiges oolitiques»     |
|15202429 | Villarbeney-Fm. | Formation de Villarbeney     |
|15202430 | Villarbeney-Fm.: Veveyse-de-Châtel-Mb. | Membre de la Veveyse de Châtel     |
|15202431 | Villarbeney-Fm.: Riondouneire-Mb. | Membre de Riondouneire     |
|15202432 | Jogne-Fm. | Formation de la Jogne     |
|15202433 | Jogne-Fm.: Kalkbrekzie | «Calcaires bréchiques»     |
|15202434 | Jogne-Fm.: Vuavres-Mb. | Membre des Vuavres     |
|15202435 | Jogne-Fm.: Planière-Mb. | Membre de la Planière     |
|15202436 | Bifé-Fm. | Formation de Bifé     |
|15202437 | Bifé-Fm.: Zementkalk | «Calcaire à ciment» (Fm. de Bifé)     |
|15202438 | Bifé-Fm.: Joux-Galez-Mb. | Membre de Joux Galez     |
|15202439 | Pereyre-Fm. | Formation de la Pereyre     |
|15202440 | Praz-Couquain-Fm. | Formation de Praz Couquain     |
|15202442 | Gryonne-Fm. | Formation de la Gryonne     |
|15202443 | Praz-Couquain-Fm.: Taffon-Mb. | Membre du Taffon     |
|15202444 | Praz-Couquain-Fm.: Saix-Mb. | Membre des Saix     |
|15200523 | Kronberg-Nagelfluh: Hochfläschli-Mb. | Membre de la Hochfläschli     |
|15200524 | Kronberg-Nagelfluh: Ennetbühl-Mb. | Membre d&#39;Ennetbühl     |
|15200525 | Kronberg-Nagelfluh: Hochalp-Mb. | Membre de la Hochalp     |
|15200526 | Kronberg-Nagelfluh: Krummenau-Mb. | Membre de Krummenau     |
|15200527 | USM-J: Ältere Juranagelfluh | Ältere Juranagelfluh     |
|15200528 | Gitzischöpf-Nagelfluh | Poudingue de la Gitzischöpf     |
|15200529 | Honegg-Mergel | Marne de la Honegg     |
|15200530 | Honegg-Mergel: Kaltbach-Nagelfluh | Poudingue du Kaltbach     |
|15200531 | Thun-Fm.: Hünibach-Nagelfluh | Poudingue de Hünibach     |
|15200532 | Losenegg-Fm. | Formation de la Losenegg     |
|15200533 | Homberg-Fm.: Schwändibach-Nagelfluh | Poudingue de Schwändibach     |
|15200534 | Uerscheli-Fm. | Formation d&#39;Uerscheli     |
|15200535 | Uerscheli-Fm.: Bumbach-Nagelfluh | Poudingue de Bumbach     |
|15200536 | USM-I: Untere Bunte Molasse: Kalksandstein | Kalksandstein-Serie     |
|15200537 | Gérignoz-Fm. | Couches du Gérignoz     |
|15200538 | Speer-Fm.: Leuenfall-Nagelfluh | Poudingue du Leuenfall     |
|15200539 | Speer-Fm.: Wintersberg-Mb. | Membre du Wintersberg     |
|15200540 | Speer-Fm.: Ebnat-Mb. | Grès d&#39;Ebnat     |
|15200541 | Speer-Fm.: Ebnat-Mb.: Rütiberg-Kalksandstein | Grès calcaire de Rütiberg     |
|15200542 | Rigi-Fm.: Bunte Rigi-Nagelfluh: Pfiffegg-Nagelfluh | Poudingue de la Pfiffegg     |
|15202160 | Zentraler Aare-Granit | Granite central de l&#39;Aar     |
|15202161 | Grimsel-Granodiorit | Granodiorite du Grimsel     |
|15202162 | Südwestlicher Aare-Granit | Granite sud-occidental de l&#39;Aar     |
|15202163 | Bugnei-Granodiorit | Granodiorite de Bugnei     |
|15202164 | Aar-Massiv: Spät- bis postvariszische Sedimente und Vulkanite | Roches sédimentaires et volcaniques tardi- à post-varisques du massif de l&#39;Aar     |
|15202165 | Wendenjoch-Fm. | Formation du Wendenjoch     |
|15202166 | Windgällen-Fm. | Formation des Windgällen     |
|15202167 | Trift-Fm. | Formation du Trift     |
|15202168 | Intschi-Fm. | Formation d&#39;Intschi     |
|15202169 | Bifertengrätli-Fm. | Formation du Bifertengrätli     |
|15202170 | Bifertengrätli-Fm.: Lakustrisches Mb. | Membre lacustre (Fm. du Bifertengrätli)     |
|15202171 | Bifertengrätli-Fm.: Estuarisches Mb. | Membre estuarien (Fm. du Bifertengrätli)     |
|15202172 | Bifertengrätli-Fm.: Grünhorn-Mb.: Basales Konglomerat | Conglomérat basal (Fm. du Bifertengrätli)     |
|15202173 | Bifertengrätli-Fm.: Grünhorn-Mb. | Membre volcanique (Fm. du Bifertengrätli)     |
|15202174 | Diechtergletscher-Fm. | Formation du Diechtergletscher     |
|15202175 | Tscharren-Fm. | Formation de la Tscharren     |
|15202177 | Aar-Massiv: Mittelvariszische Intrusiva | Groupe du Fruttstock     |
|15202178 | Brunni-Granit | Granite de la Brunni     |
|15202179 | Düssi-Diorit | Diorite du Düssi     |
|15202180 | Munt-Dado-Granit | Granite du Munt Dado     |
|15203078 | Obflue-Fm. | Formation de la Obflue     |
|15203079 | Brand-Fm. | Formation de Brand     |
|15203080 | Horngraben-Fm. | Formation du Horngraben     |
|15203081 | Lückengraben-Fm. | Formation du Lückengraben     |
|15203082 | Dorfflüe-Fm. | Formation de la Dorfflüe     |
|15203083 | Dorfflüe-Fm.: Gummfluh-Mikrofazies | Microfaciès de la Gummfluh     |
|15203084 | Dorfflüe-Fm.: Pfad-Mikrofazies | Microfaciès de Pfad     |
|15203085 | Dorfflüe-Fm.: Rindenkorn-Mikrofazies | Microfaciès à oncolithes (Fm. de la Dorfflüe)     |
|15203086 | Dorfflüe-Fm.: Gastlosen-Oolith | Oolite des Gastlosen     |
|15203087 | Dorfflüe-Fm.: Wandfluh-Mikrofazies | Microfaciès de la Wandfluh     |
|15203088 | Mytilus-Sch. | Couches à Mytilus     |
|15203089 | Mytilus-Sch.: Col-de-Cordon-Mb. | Membre du Col de Cordon     |
|15203090 | Mytilus-Sch.: Col-de-Cordon-Mb.: Klus-Konglomerat | Conglomérat de la Klus     |
|15203091 | Mytilus-Sch.: Col-de-Cordon-Mb.: Holzerhorn-Einheit | Unité du Holzerhorn     |
|15203092 | Mytilus-Sch.: Rubli-Mb. | Membre du Rubli     |
|15203093 | Mytilus-Sch.: Chavanette-Mb. | Membre de Chavanette     |
|15203094 | Pralet-Fm.: Erpilles-Mb. | Membre des Erpilles     |
|15203095 | Wiriehorn-Fm. | Formation du Wiriehorn     |
|15203096 | St-Triphon-Fm. | Formation de St-Triphon     |
|15203097 | St-Triphon-Fm.: Andonces-Mb. | Membre des Andonces     |
|15203098 | St-Triphon-Fm.: Lessus-Mb. | Membre du Lessus     |
|15200543 | Weggis-Fm. | Formation de Weggis     |
|15200544 | Weggis-Fm.: Kännelegg-Nagelfluh | Poudingue de la Kännelegg     |
|15200545 | Molasse Rouge des Jurasüdfusses | Molasse Rouge du Pied-du-Jura     |
|15200546 | Molasse Rouge des Jurasüdfusses: Mathod-Sandstein | Grès de Mathod     |
|15200547 | Molasse Rouge des Jurasüdfusses: Goumoëns-Sandstein | Grès de Goumoëns     |
|15200548 | Molasse Rouge de Vevey | Molasse Rouge de Vevey     |
|15200549 | Molasse Rouge de Monthey | Molasse Rouge de Monthey     |
|15200550 | Grindelegg-Fm. | Formation de la Grindelegg     |
|15200551 | Grès et Marnes Gris à Gypse: Tillerée-Sch. | Couches de Tillerée     |
|15200552 | Grès et Marnes Gris à Gypse: Süsswasserkalke und Dolomite | Série des calcaires d&#39;eau douce et dolomie (GMGG)     |
|15200553 | Oltingue-Kalkarenit | Calcarénite d&#39;Oltingue     |
|15200554 | Vaulruz-Fm. | Formation de Vaulruz (UMM-II+III indiff.)     |
|15200555 | Hilfern-Fm.: Unter-Lochsiti-Nagelfluh | Poudingue d&#39;Unter Lochsitli     |
|15200556 | Hilfern-Fm.: Flühli-Nagelfluh | Poudingue de Flühli     |
|15200557 | St.-Gallen-Fm.: Mergelstein-dominierte Fazies | Zone der Schiefermergel (Fm. de Saint-Gall)     |
|15200558 | Fm. der Granitischen Molasse: Marbach-Mb. | Membre de Marbach     |
|15200560 | USM-I: Untere Bunte Molasse | Molasse bariolée inférieure     |
|15200562 | OSM-J: Mittlere Juranagelfluh | Mittlere Juranagelfluh     |
|15200563 | OSM-J: Albstein | Albstein     |
|15202181 | Russein-Diorit | Diorite de Russein     |
|15202182 | Voralp-Granit | Granite de la Voralp     |
|15202183 | Aar-Massiv: Frühvariszische Intrusiva | Groupe du Rötifirn     |
|15202184 | Punteglias-Granit | Granite de Punteglias     |
|15202185 | Tödi-Granit | Granite du Tödi     |
|15202186 | Strem-Granit | Granite du (Val) Strem     |
|15202187 | Baltschieder-Granodiorit | Granodiorite de Baltschieder     |
|15202188 | Giuv-Syenit | Syénite du (Piz) Giuv     |
|15202189 | Curtin-Monzodiorit | Monzodiorite du (Piz) Curtin     |
|15202190 | Bristenstock-Syenit | Syénite du Bristenstock     |
|15202191 | Aar-Massiv: Frühvariszische Sedimente | Groupe de Cavardiras     |
|15202192 | Val-Gliems-Fm. | Formation du Val Gliems     |
|15202193 | Bifertenfirn-Fm. | Formation du Bifertenfirn     |
|15202194 | Aar-Massiv: Prävariszisches polyzyklisches Grundgebirge | Socle métamorphique polycyclique anté-varisque du massif de l&#39;Aar     |
|15202195 | Innertkirchen-Migmatit | Migmatite d&#39;Innertkirchen     |
|15202196 | Innertkirchen-Migmatit: Zäsenberg-Gneis | Gneiss du Zäsenberg     |
|15202197 | Erstfeld-Gneiskomplex | Complexe gneissique d&#39;Erstfeld     |
|15202198 | Guttannen-Gneiskomplex | Complexe gneissique de Guttannen     |
|15202199 | Straligenstöckli-Gneiskomplex | Complexe gneissique du Straligenstöckli     |
|15202200 | Lötschental-Gneiskomplex | Complexe gneissique du Lötschental     |
|15202445 | Villarbeney-Fm.: Cergnement-Mb. | Membre du Cergnement     |
|15202446 | Arveyes-Flysch | Flysch de la nappe d&#39;Arveyes     |
|15202447 | Sex-Mort-Flysch | Flysch de la nappe du Sex Mort     |
|15202448 | Diechtergletscher-Fm.: Maasplanggstock-Metaandesit | Méta-andésite du Maasplanggstock     |
|15202449 | Dammagletscher-Diorit | Diorite du Dammagletscher     |
|15202450 | Gryonne-Fm.: Schiefrige Fazies | Lias des Mines schisteux     |
|15202451 | Gryonne-Fm.: Kalkige Fazies | Lias des Mines calcaire     |
|15202452 | Gryonne-Fm.: Basaler Teil | Lias des Mines basal     |
|15202453 | Glarner-Verrucano: Tektonisierte Basis | base tectonisée du Verrucano de Glaris («Plagioklasgneis»)     |
|15202454 | Chrüzlistock-Migmatit | Migmatite du Chrüzlistock     |
|15202455 | Piz-Cuolmet-Gneiskomplex | Complexe gneissique du Piz Cuolmet     |
|15202456 | Pulanera-Gneiskomplex | Pulanera-Gneiskomplex     |
|15202465 | Aiguilles-Rouges-Massiv: Spät- bis postvariszische Sedimente und Vulkanite | Permo-Carbonifère du massif des Aiguilles Rouges     |
|15202467 | Helvetikum: Variszisches Kristallin | Variszisches Kristallin des Helvetikums     |
|15202468 | Helvetikum: Prävariszisches polyzyklisches Grundgebirge | Socle polycyclique anté-varisque de l&#39;Helvétique     |
|15202469 | Helvetikum: Grundgebirge | Socle cristallin indifférencié de l&#39;Helvétique     |
|15202472 | Catogne-Gneiskomplex | Complexe gneissique du Catogne     |
|15202473 | Grépillons-Leukogranit | Leucogranite des Grépillons     |
|15203099 | St-Triphon-Fm.: Dorchaux-Mb. | Membre de Dorchaux     |
|15203100 | Mattes-Melange | Mélange des Mattes     |
|15203101 | Chumi-Fm. | Formation de la Chumi     |
|15203102 | Joux-Verte-Fm. | Formation de la Joux Verte     |
|15203103 | Bonave-Fm. | Formation de Bonave     |
|15203104 | Obere Brekzie | Brèche Supérieure     |
|15203105 | Obere Schiefer | Schistes Ardoisiers     |
|15203106 | Untere Brekzie | Brèche Inférieure     |
|15203107 | Untere Schiefer | Schistes Inférieurs     |
|15203108 | Untere Schiefer: Untere Kalke | Calcaires Inférieurs     |
|15203109 | Brekzien-Decke:Trias | Trias de la nappe de la Brèche     |
|15203110 | Gurnigel-Decke: Flysch | Flysch du Gurnigel     |
|15203111 | Gurnigel-Decke: Flysch-4 | Flysch 4 à turbidites silteuses     |
|15203112 | Gurnigel-Decke: Flysch-3b | Flysch 3b à turbidites bioclastiques     |
|15203113 | Gurnigel-Decke: Flysch-3a | Flysch 3a marno-gréseux     |
|15203114 | Gurnigel-Decke: Flysch-2b | Flysch 2b à turbidites siliceuses     |
|15203115 | Gurnigel-Decke: Flysch-2a | Flysch 2a argilo-gréseux     |
|15203116 | Hellstätt-Fm. | Formation de Hellstätt     |
|15203117 | Schlieren-Decke: Flysch | Flysch des Schlieren     |
|15203118 | Schlieren-Sandstein | Grès des Schlieren     |
|15203119 | Schoni-Sandstein | Grès de la Schoni     |
|15203120 | Schoni-Sandstein: Oberer Tonstein | Obere Tonsteinschichten (Flysch des Schlieren)     |
|15200564 | Grimmelfingen-Fm.: Graupensand-Fazies | Graupensand     |
|15200565 | OSM-J: Heliciden-Mergel | Marne à Hélicidés     |
|15200566 | Haldenhof-Mergel | Marne de Haldenhof     |
|15200567 | OMM-J | OMM-J     |
|15200568 | Tenniken-Muschelagglomerat | Poudingue coquillier de Tenniken     |
|15200569 | OMM-II: Turritellen-Kalk | Calcaire à Turritelles     |
|15200570 | Randen-Grobkalk | Calcaire grossier du Randen     |
|15200571 | Péry-Sandstein | Sable à galets de Péry     |
|15200572 | Les-Bayards-Juranagelfluh | Gompholite des Bayards     |
|15200573 | Günsberg- und Vellerat-Fm. | Formation de Günsberg et de Vellerat, indifférenciées     |
|15200574 | Ornatenton-Fm.: Ancepsoolith-Sbf. | Ornatenton-Fm.: Ancepsoolith-Sbf.     |
|15200575 | Jurensismergel-Fm. | Jurensismergel-Fm.     |
|15200576 | Posidonienschiefer-Fm. | Posidonienschiefer-Fm.     |
|15200577 | Amaltheenton-Fm. | Amaltheenton-Fm.     |
|15200578 | Numismalismergel-Fm. | Numismalismergel-Fm.     |
|15200579 | Obtususton-Fm. | Obtususton-Fm.     |
|15200580 | Arietenkalk-Fm. | Arietenkalk-Fm.     |
|15200581 | Angulatenton-Fm. | Angulatenton-Fm.     |
|15200582 | Psilonotenton-Fm. | Psilonotenton-Fm.     |
|15200584 | Etiollets-Fm.: Tabalcon-Kalk | Etiollets-Fm.: Tabalcon-Kalk     |
|15200585 | Bonneville-Sandstein | Bonneville-Sandstein     |
|15200586 | Montauban-Mergel | Montauban-Mergel     |
|15200588 | Mornex-Nagelfluh | Mornex-Nagelfluh     |
|15202201 | Ofenhorn-Stampfhorn-Gneiskomplex | Complexe gneissique de l&#39;Ofenhorn-Stampfhorn     |
|15202202 | Fully-Granodiorit | Granodiorite de Fully     |
|15202203 | Vernayaz-Fm.: Salvan-Mb.: Plex-Aboyeu-Rhyolith | Rhyodacite de Plex-Aboyeu     |
|15202204 | Vallorcine-Granit | Granite de Vallorcine     |
|15202205 | Vallorcine-Granit: Miéville-Mylonit | Mylonite de Miéville     |
|15202206 | Montées-Pélissiers-Granit | Granite des Montées-Pélissiers     |
|15202207 | Pormenaz-Granit | Granite de Pormenaz     |
|15202210 | Emosson-Gneiskomplex | Micaschistes d&#39;Emosson     |
|15202211 | Luisin-Orthogneis | Orthogneiss du Luisin     |
|15202212 | Val-Bérard-Gneiskomplex | Complexe gneissique du Val Bérard     |
|15202213 | Lac-Cornu-Eklogit | Éclogite du Lac Cornu     |
|15202214 | Perrons-Orthogneis | Orthogneiss des Perrons     |
|15202215 | Breya-Rhyolith | Rhyolithe de la Breya     |
|15202216 | Mont-Blanc-Granit | Granite du Mont Blanc     |
|15202217 | Montenvers-Granit | Granite du Montenvers     |
|15202218 | Lognan-Orthogneis | Orthogneiss de Lognan     |
|15202219 | Pétoudes-Orthogneis | Orthogneiss des Pétoudes     |
|15202220 | Gotthard-Decke: Postvariszische Intrusiva | Groupe de Pesciora     |
|15202221 | Rotondo-Granit | Granite du Rotondo     |
|15202222 | Cacciola-Granit | Granite de la Cacciola     |
|15202474 | Arpette-Leukogranit | Leucogranite d&#39;Arpette     |
|15202475 | Gärsthorn-Gneiskomplex: Bitschji-Augengneis | Gneiss oeillé de Bitschji     |
|15202476 | Gärsthorn-Gneiskomplex: Geimen-Augengneis | Gneiss oeillé de Geimen     |
|15202477 | Mont-Blanc-Massiv: Prävariszische Migmatite | Socle polycyclique anté-varisque du massif du Mont Blanc, migmatitique     |
|15202478 | Mont-Blanc-Massiv: Prävariszisches Grundgebirge: Amphibolit-reiche Fazies | Socle polycyclique anté-varisque du massif du Mont Blanc, riche en amphibolites     |
|15202479 | Mont-Blanc-Massiv: Prävariszisches Grundgebirge: Mylonit | Socle polycyclique anté-varisque du massif du Mont Blanc, mylonitique     |
|15202480 | Morcles-Mikrogranit | Microgranite de Morcles     |
|15202481 | Aiguilles-Rouges-Massiv: Prävariszisches Migmatite | Socle polycyclique anté-varisque du massif des Aiguilles Rouges, migmatitique     |
|15202482 | Fully-Gneiskomplex | Complexe gneissique de Fully     |
|15202483 | Hinterbalm-Granit | Granite d&#39;Hinterbalm     |
|15202484 | Balmenegg-Granit | Granite de la Balmenegg     |
|15202485 | Zentraler-Aare-Granit: Unter-der-Flue-Varietät | faciès d&#39;Unter-der-Flue     |
|15202486 | Pardatschas-Granit | Granite du (Piz) Pardatschas     |
|15202487 | Rossbodenstock-Diorit | Diorite du Rossbodenstock     |
|15202488 | Val-da-Surplattas-Diorit | Diorite du Val da Surplattas     |
|15202489 | Tscharren-Fm.: Rinderbiel-Mikrogranit | Microgranite de Rinderbiel     |
|15203121 | Guber-Sandstein | Grès de Guber     |
|15203122 | Guber-Sandstein: Unterer Tonstein | Untere Tonsteinschichten (Flysch des Schlieren)     |
|15203123 | Schlieren-Decke: Basaler Flysch | Flysch basal des Schlieren     |
|15203124 | Estavannens-Fm. | Flysch d&#39;Estavannens     |
|15203125 | Reidigen-Fm. | Formation de Reidigen     |
|15203126 | Biot-Fm. | Formation du Biot     |
|15203127 | Chétillon-Fm. | Formation de Chétillon     |
|15203128 | Rodomonts-Fm. | Formation des Rodomonts     |
|15203129 | Rodomonts-Fm.: Mocausa-Nagelfluh | Poudingue de la Mocausa     |
|15203130 | Tissota-Melange | Mélange de la Tissota     |
|15203131 | Tissota-Melange: Gueyraz-Komplex | Complexe de la Gueyraz     |
|15203132 | Manche-Fm.: Weissenburg-Flysch | Flysch de la Weissenburg     |
|15203133 | Manche-Fm. | Formation de la Manche     |
|15203134 | Fouyet-Fm. | Formation du Fouyet     |
|15203135 | Tissota-Melange: Gueyraz-Komplex: Foraminiferenschichten | Couches à foraminifères     |
|15203136 | Tissota-Melange: Gueyraz-Komplex: Aptychenkalk | Calcaires à Aptychus     |
|15203137 | Tissota-Melange: Gueyraz-Komplex: Radiolarit | Radiolarites     |
|15203138 | Tissota-Melange: Gueyraz-Komplex: Filamentkalk | Calcaires à filaments     |
|15203139 | Tissota-Melange: Gueyraz-Komplex: Spatkalk | Calcaires spathiques     |
|15203140 | Hundsrügg-Fm. | Formation du Hundsrügg     |
|15200589 | USM-III bis OSM-I | USM-III bis OSM-I     |
|15200590 | Uetliberg-Fm.: Loorenkopf-Nagelfluh | Uetliberg-Fm.: Loorenkopf-Nagelfluh     |
|15200591 | Grand-Essert-Fm: Neuchâtel-Mb.: Oberer Teil | Grand-Essert-Fm: Neuchâtel-Mb.: Oberer Teil     |
|15200592 | Grand-Essert-Fm: Neuchâtel-Mb.: Unterer Teil | Grand-Essert-Fm: Neuchâtel-Mb.: Unterer Teil     |
|15200593 | Chambotte-Fm.: Oberer Teil | Chambotte-Fm.: Oberer Teil     |
|15200594 | Chambotte-Fm.: Unterer Teil | Chambotte-Fm.: Unterer Teil     |
|15200616 | Schwarzwald-Massiv: Grundgebirge | Schwarzwald-Massiv: Grundgebirge     |
|15200617 | Schwarzwald-Massiv: Variszische Intrusiva | Schwarzwald-Massiv: Variszische Intrusiva     |
|15200618 | USM-I: Untere Bunte Molasse: Mümliswil-Süsswasserkalk | Calcaire d&#39;eau douce de Mümliswil     |
|15200619 | Luzern-Fm.: Limnischer Horizont | Horizon limnique (OMM-I)     |
|15200620 | Molasse Rouge des Jurasüdfusses: Dardagny-Sandstein | Grès de Dardagny     |
|15200621 | Napf-Fm.: Konglomerat-dominierte Fazies | Napf-Fm.: Konglomerat-dominierte Fazies     |
|15200622 | Napf-Fm.: Sandstein-Mergelstein-dominierte Fazies | Napf-Fm.: Sandstein-Mergelstein-dominierte Fazies     |
|15200623 | Le-Locle-Fm. | Le-Locle-Fm.     |
|15200624 | Le-Locle-Fm.: Le-Verger Mb. | Le-Locle-Fm.: Le-Verger Mb.     |
|15200625 | Le-Locle-Fm.: Combe-Girard Mb. | Le-Locle-Fm.: Combe-Girard Mb.     |
|15200626 | Crêt-du-Locle-Fm. | Crêt-du-Locle-Fm.     |
|15200627 | Crêt-du-Locle-Fm.: Mergelfazies | Crêt-du-Locle-Fm.: Mergelfazies     |
|15200628 | St.-Gallen-Fm.: Gitzigrabe-Grobsandstein | St.-Gallen-Fm.: Gitzigrabe-Grobsandstein     |
|15202223 | Sädelhorn-Diorit | Diorite du Sädelhorn     |
|15202224 | Winterhorn-Granit | Granite du Winterhorn     |
|15202225 | Gotthard-Decke: Spätvariszische Intrusiva | Groupe du Val Lavaz     |
|15202226 | Medel-Granit | Granite de Medel     |
|15202227 | Cristallina-Granodiorit | Granodiorite de Cristallina     |
|15202228 | Gamsboden-Granit | Granite du Gamsboden     |
|15202229 | Uffiern-Diorit | Diorite du Val Uffiern     |
|15202230 | Fibbia-Granit | Granite de la Fibbia     |
|15202231 | Gotthard-Decke: Prä- und frühvariszische Metasedimentgesteine und Vulkanoklastika | Groupe du Val Rondadura     |
|15202232 | Borel-Gneiskomplex | Complexe gneissique du Piz Borel     |
|15202233 | Tenelin-Gneiskomplex | Complexe gneissique du Piz Tenelin     |
|15202234 | Laiets-Gneiskomplex | Complexe gneissique des Laiets     |
|15202235 | Tremola-Gneiskomplex | Complexe gneissique de la Tremola     |
|15202236 | Tremola-Gneiskomplex: Pontino-Schiefer | Complexe gneissique de Pontino     |
|15202237 | Tremola-Gneiskomplex: Nelva-Gneis | Complexe gneissique de Nelva     |
|15202238 | Tremola-Gneiskomplex: Sasso-Rosso-Schiefer | Complexe gneissique du Sasso Rosso     |
|15202239 | Prüsfa-Gneiskomplex | Complexe gneissique de Prüsfa     |
|15202240 | Streifengneis-Komplex | Complexe du Streifengneiss     |
|15202241 | Chastelhorn-Metagabbro | Métagabbro du Chastelhorn     |
|15202490 | Leventina-Lucomagno-Decke: Trias: Quarzit | Dachquarzit (Leventina)     |
|15202491 | Kapfen-Fm. | Formation de Kapfen     |
|15202492 | Kapfen-Fm.: Sandstein-dominierte Fazies | Grès de Kapfen     |
|15202493 | Kärpf-Fm.: Kärpfgipfel-Sernifit | Sernifite du Kärpfgipfel     |
|15202494 | Fulen-Fm. | Formation du Fulen     |
|15202495 | Karrenstock-Fm.: Glattmatt-Mb. | Membre de Glattmatt     |
|15202496 | Mären-Fm.: Grisch-Mb.: Hanenstock-Keratophyr | Kératophyre du Hahnenstock     |
|15202497 | Mären-Fm.: Grisch-Mb.: Sonnenberg-Horizonte | Horizons du Sonnenberg     |
|15202498 | Mären-Fm.: Grisch-Mb.: Chamseeli-Konglomerat | Conglomérat du Chamseeli     |
|15202499 | Murgtal-Fm.: Chartegg-Mb.: Rotberg-Sandstein | Grès du Rotberg     |
|15202500 | Murgtal-Fm.: Seez-Mb. | Membre de Seez     |
|15202501 | Murgtal-Fm.: Gufelialp-Mb. | Membre de la Gufelialp     |
|15202502 | Ilanz-Verrucano s.s. | Verrucano d&#39;Ilanz s.s.     |
|15202503 | Ilanz-Verrucano: Buntgefleckte Schiefer | Buntgefleckte Schiefer (Ilanz)     |
|15202504 | Tavetsch-Decke: Perm | Permien de la nappe du Tavetsch (Val Acla Mulin)     |
|15202505 | Windgällen-Fm.: Mikrogranit | Microgranite de la Windgällenlücke     |
|15202506 | Bifertengrätli-Fm.: Sandalp-Rhyolith | Rhyolithe de la Sandalp     |
|15202507 | Tscharren-Fm.: Tuffitische Fazies | Tuffitisches Member (Tscharren)     |
|15200629 | Trois-Rods-Süsswasserkalk | Trois-Rods-Süsswasserkalk     |
|15200630 | Champ-Vuillerat-Süsswasserkalk | Champ-Vuillerat-Süsswasserkalk     |
|15200631 | Napf-Fm.: Wolhusen-Bentonit | Bentonite de Wholusen     |
|15200632 | OSM-II: Gitzitobel-Süsswasserkalk | Clacaire d&#39;eau douce du Gitzitobel     |
|15200633 | OSM-II: Wissenbach-Süsswasserkalk | Calcaire d&#39;eau douce du Wissenbach     |
|15200634 | OSM-II: Altbach-Süsswasserkalk | Calcaire d&#39;eau douce de l&#39;Altbach     |
|15200635 | OSM-II: Tröleten-Süsswasserkalk | Calcaire d&#39;eau douce de Tröleten     |
|15200636 | OSM-II: Tschöplihof-Süsswasserkalk | Calcaire d&#39;eau douce du Tschöplihof     |
|15200637 | Lienegg-Fm. | Formation du Lienegg     |
|15200638 | Öligraben-Fm. | Formation de l&#39;Öligraben     |
|15200639 | Studweid-Fm. | Formation du Studweid     |
|15200640 | Rossemaison-Fm. | Formation de Rossemaison     |
|15200641 | Schwaningen-Merenbach-Rhyolith | Rhyolithe de Schwaningen-Merenbach     |
|15200642 | Schwaningen-Weizen-Granit | Granite de Schwaningen-Weizen     |
|15200643 | Etzgen-Granit | Granite d&#39;Etzgen     |
|15200645 | USM-I: Kalk-Dolomit-Nagelfluh | Karbonatreiche Molasse: Kalk-Dolomit-Nagelfluh     |
|15200646 | Hornbüel-Melange | Mélange de Hornbüel     |
|15200647 | Kalter-Wangen-Fm. | Formation du Kalter Wangen     |
|15200648 | Baltersweil-Nagelfluh | Poudingue de Baltersweil     |
|15200649 | Netzbachtal-Nagelfluh | Poudingue du Netzbachtal     |
|15200650 | Rocher-des-Hirondelles-Fm. | Formation du Rocher des Hirondelles     |
|15202242 | Val-Nalps-Gneiskomplex: Gurschen-Gneis | Gneiss de la Gurschen(alp)     |
|15202243 | Val-Nalps-Gneiskomplex: Guspis-Gneis | Gneiss de la Guspis     |
|15202244 | Paradis-Gneiskomplex: Sorescia-Gneis | Gneiss de Sorescia     |
|15202246 | Helvetikum: Grundgebirge: Granit | roches granitiques     |
|15202247 | Helvetikum: Grundgebirge: Saures vulkanisches Gestein | roches volcaniques et subvolcaniques acides     |
|15202254 | Ilanz-Zone: Permische Sedimente | Sédiments permiens de la zone d&#39;Ilanz     |
|15202255 | Helvetikum: Grundgebirge: Permisch verwittertes Kristallin | Cristallin à altération permienne     |
|15202256 | Goltschenried-Fm. | Formation de Goltschenried     |
|15202257 | Oberaar-Furka Zone | zone de l&#39;Oberaar-Furka     |
|15202258 | Ausserberg-Avat-Zone | zone d&#39;Ausserberg-Avat     |
|15202260 | Ausserberg-Avat-Zone: Granitischer Gneis | Gneiss granitique de la zone d&#39;Ausserberg-Avat     |
|15202261 | Ausserberg-Avat-Zone: Paragneis | Paragneiss de la zone d&#39;Ausserberg-Avat     |
|15202262 | Clavaniev-Zone | zone de Clavaniev     |
|15202263 | Gärsthorn-Gneiskomplex: Engi-Granit | Granite d&#39;Engi     |
|15202264 | Calmut-Gneiskomplex | Complexe gneissique de Calmut     |
|15202265 | Val-Pigniu-Gneiskomplex | Complexe gneissique du Val Pigniu     |
|15202266 | Urseren-Garvera-Zone: Permo-Karbon | Permo-Carbonifère de la zone d&#39;Urseren-Garvera     |
|15202267 | Goms-Gneiskomplex | Complexe gneissique de Goms     |
|15202508 | Tscharren-Fm.: Ignimbritische Fazies | Ignimbritisches Member (Tscharren)     |
|15202509 | Euthal-Fm.: Guschakopf-Sandstein | Grès du Guschakopf     |
|15202510 | Quinten-Fm.: Gonzen-Eisenerzhorizont | Horizon du Gonzen     |
|15202511 | Schabell-Melange | Schabell-Melange     |
|15202512 | Taveyannaz-Fm.: Dachschiefer-Fazies | Taveyannaz-Fm.: Dachschiefer-Fazies     |
|15202513 | Helvetischer Kieselkalk: Oberer Teil | Helvetischer Kieselkalk: Oberer Teil     |
|15202514 | Helvetischer Kieselkalk: Unterer Teil | Helvetischer Kieselkalk: Unterer Teil     |
|15202515 | Helvetischer Kieselkalk: Basisschiefer | Helvetischer Kieselkalk: Basisschiefer     |
|15202516 | Torrenthorn-Fm.: Torrentalp-Mb.: Schiefer-Fazies | Torrenthorn-Fm.: Torrentalp-Mb.: Schiefer-Fazies     |
|15202517 | Torrenthorn-Fm.: Torrentalp-Mb.: Spatkalk-Fazies | Torrenthorn-Fm.: Torrentalp-Mb.: Spatkalk-Fazies     |
|15202518 | Torrenthorn-Fm.: Torrentalp-Mb.: Sandstein-Fazies | Torrenthorn-Fm.: Torrentalp-Mb.: Sandstein-Fazies     |
|15202519 | Torrenthorn-Fm.: Galm-Mb.: Spatkalk-Fazies | Torrenthorn-Fm.: Galm-Mb.: Spatkalk-Fazies     |
|15202520 | Torrenthorn-Fm.: Galm-Mb.: Sandstein-Fazies | Torrenthorn-Fm.: Galm-Mb.: Sandstein-Fazies     |
|15202521 | Meilleret-Fm.: Iserin-Konglomerat | Meilleret-Fm.: Iserin-Konglomerat     |
|15202522 | Meilleret-Fm.: Biodetritischer Kalkstein | Meilleret-Fm.: Biodetritischer Kalkstein     |
|15202523 | Meilleret-Fm.: Arkose | Meilleret-Fm.: Arkose     |
|15202524 | Meilleret-Fm.: Basales Konglomerat | Meilleret-Fm.: Basales Konglomerat     |
|15200651 | Rocher-des-Hirondelles-Fm.: Fort-de-l&#39;Ecluse-Mb. | Membre du Fort de l&#39;Ecluse     |
|15200652 | Gorges-de-l&#39;Orbe-Fm.: Bôle-Mb. | Membre de Bôle     |
|15200653 | Gorges-de-l&#39;Orbe-Fm.: Montcherand-Mb. | Membre de Montcherand     |
|15200654 | Vuache-Fm.: Calcaire roux s.s. | Calcaire Roux     |
|15200658 | Schwarzbach-Fm. | Couches du Schwarzbach     |
|15200659 | Wangen- und Letzi-Mb. | Membres de Wangen et du Letzi, indifférenciés     |
|15200660 | Grand-Essert- bis Narlay-Fm. | Grand-Essert- bis Narlay-Fm.     |
|15200661 | Goldberg- bis Vuache-Fm. | Goldberg- bis Vuache-Fm.     |
|15200662 | Rocher-des-Hirondelles-Fm.: Bellegarde-Bk. | Rocher-des-Hirondelles-Fm.: Bellegarde-Bk.     |
|15200663 | Rocher-des-Hirondelles-Fm.: Serrières-Bk. | Rocher-des-Hirondelles-Fm.: Serrières-Bk.     |
|15200664 | Gorges-de-l&#39;Orbe-Fm.: Morteau-Kalk | Gorges-de-l&#39;Orbe-Fm.: Morteau-Kalk     |
|15200665 | Gorges-de-l&#39;Orbe-Fm.: Montcherand-Mb.: La-Vaux-Bk. | Gorges-de-l&#39;Orbe-Fm.: Montcherand-Mb.: La-Vaux-Bk.     |
|15200666 | Gorges-de-l&#39;Orbe-Fm.: Montcherand-Mb.: Cul-du-Nozon-Bk. | Gorges-de-l&#39;Orbe-Fm.: Montcherand-Mb.: Cul-du-Nozon-Bk.     |
|15200667 | Gorges-de-l&#39;Orbe-Fm.: Montcherand-Mb.: Pont-des-Pierres-Bk. | Gorges-de-l&#39;Orbe-Fm.: Montcherand-Mb.: Pont-des-Pierres-Bk.     |
|15200668 | Grand-Essert-Fm: Hauterive-Mb.: Censeau-Mergel | Grand-Essert-Fm: Hauterive-Mb.: Censeau-Mergel     |
|15200669 | Grand-Essert-Fm: Hauterive-Mb.: Morteau-Mergel | Grand-Essert-Fm: Hauterive-Mb.: Morteau-Mergel     |
|15200670 | Chambotte-Fm.: Guiers-Mb.: Grande-Varappe-Bk. | Chambotte-Fm.: Guiers-Mb.: Grande-Varappe-Bk.     |
|15201157 | Plateauschotter | Plateauschotter     |
|15201158 | La-Côte-Schotter | Alluvions de la Côte     |
|15201003 | Hochterrasse | Hochterrasse     |
|15201050 | Gondiswil-Interglazial (Letztes Interglazial) | Interglaciaire de Gondiswil (Dernier Interglaciaire)     |
|15201051 | Flurlingen-Quelltuff | Tuf calcaire de Flurlingen     |
|15201052 | Birrfeld- und Klettgau-Paläoböden | Paléosols du Birrfeld et du Klettgau     |
|15201045 | Klettgau-Schotter | Gravier du Klettgau     |
|15201046 | Obere Klettgauschotter | Gravier supérieur du Klettgau     |
|15201047 | Glazi-lakustrische Serie | Série glaciolacustre (Gravier du Klettgau)     |
|15201048 | Mittlere Klettgauschotter | Gravier moyen du Klettgau     |
|15201049 | Untere Klettgauschotter | Gravier inférieur du Klettgau     |
|15201159 | Enge-Schotter | Gravier de l&#39;Enge     |
|15201160 | Attiswil-Schotter | Gravier d&#39;Attiswil     |
|15201161 | Lommiswil-Schotter | Gravier de Lommiswil     |
|15201162 | Oensingen-Moos-Lehm | Limon d&#39;Oensingen-Moos     |
|15201163 | Berken-Schotter | Gravier de Berken     |
|15201164 | Berken-Sand | Sable de Berken     |
|15201165 | Schwarzhäusern-Lehm | Limon de Schwarzhäusern     |
|15201166 | Käppelihof-Schotter | Gravier du Käppelihof     |
|15201167 | Aarburg-Schotter | Gravier d&#39;Aarburg     |
|15201168 | Tuileries-Formation | Formation des Tuileries     |
|15201169 | Grandson-Formation | Formation de Grandson     |
|15201170 | Poissine-Formation | Formation de la Poissine     |
|15201053 | Beringen-Eiszeit | Période glaciaire de Beringen (Avant-dernière Période glaciaire)     |
|15201171 | Surbtal-Lehm | Limon du Surbtal     |
|15201172 | Surbtal-Till | Till du Surbtal     |
|15201173 | Surbtal-Schotter | Gravier du Surbtal     |
|15201174 | Fislisbach-Schotter | Gravier de Fislisbach     |
|15201054 | Entfelden-Schotter | Gravier d&#39;Entfelden     |
|15201055 | Aarau-Schotter | Gravier d&#39;Aarau     |
|15201056 | Suhr-Schotter | Gravier de Suhr     |
|15201057 | Veltheim-Schotter | Gravier de Veltheim     |
|15201058 | Stüsslingen-Schotter | Gravier de Stüsslingen     |
|15201059 | Langwiesen-Vergletscherung | Glaciation de Langwiesen     |
|15201060 | Langwiesen-Vorstoss | Avancée glaciaire de Langwiesen     |
|15201061 | Schaffhausen-Schotter | Gravier de Schaffhouse     |
|15201062 | Reuenthal-Vorstoss | Avancée glaciaire de Reuenthal     |
|15201063 | Lupfig-Schotter | Gravier de Lupfig     |
|15202525 | Bommerstein-Fm.: Glockhaus-Mb.: Grenzquarzit | Bommerstein-Fm.: Glockhaus-Mb.: Grenzquarzit     |
|15202526 | Telltistock-Granit | Telltistock-Granit     |
|15202527 | Öhrli-Fm.: von Siderolithikum durchsetzt | Formation de l&#39;Öhrli, à infiltrations de Sidérolithique     |
|15202528 | Zentraler-Aare-Granit: Beesten-Varietät | faciès de Beesten     |
|15202529 | Diechtergletscher-Fm.: Garwiidi-Diorit | Diorite de Garwiidi     |
|15202530 | Alp-Crap-Ner-Granit | Granite de l&#39;Alp Crap Ner     |
|15202531 | Innertkirchen-Migmatit: Permisch verwittert | Migmatite d&#39;Innertkirchen, à altération permienne     |
|15202532 | Erstfeld-Gneiskomplex: Permisch verwittert | Complexe gneissique d&#39;Erstfeld, à altération permienne     |
|15202533 | Martinsmad-Fm.: Supraquarzitischer Flysch: Suren-Flysch | Flysch du Suren     |
|15202534 | Stad-Fm.: Spirstock-Mb.: Obere Sandsteine | Obere Sandsteine (Spirstock)     |
|15202535 | Stad-Fm.: Spirstock-Mb.: Blockmergel | Blockmergel (Spirstock)     |
|15202536 | Stad-Fm.: Spirstock-Mb.: Untere Sandsteine | Untere Sandsteine (Spirstock)     |
|15202537 | Helvetischer Kieselkalk: Ringgenberg-Sch. | Couches de Ringgenberg     |
|15202538 | Quinten-Fm.: Brekziöse Fazies | Brèche du Malm     |
|15202539 | Schattwald-Mergelkalk | Calcaire marneux du Schattwald     |
|15202540 | Elm- und Matt-Fm. | Formations d&#39;Elm et de Matt, indifférenciées     |
|15202541 | Elm- und Matt-Fm.: Quarzsandstein | Formations d&#39;Elm et de Matt: grès quartzitique     |
|15203141 | Perrières-Fm. | Formation des Perrières     |
|15203142 | Rhenodanubischer Flysch | Flysch Rhénodanubien     |
|15203143 | Vorarlberg-Flysch | Flysch du Vorarlberg     |
|15203144 | Fanola-Fm. | Formation de Fanola     |
|15203145 | Planknerbrücke-Fm. | Formation de Planknerbrücke     |
|15203146 | Planken-Fm. | Formation de Planken     |
|15203147 | Reiselsberg-Fm. | Formation du Reiselsberg     |
|15203148 | Reiselsberg-Fm.: Basaler Teil | Série basale (Fm. du Reiselsberg)     |
|15203149 | Liechtenstein-Flysch | Flysch du Liechtenstein     |
|15203150 | Triesen-Fm. | Flysch de Triesen     |
|15203151 | Vaduz-Flysch | Flysch de Vaduz     |
|15203152 | Eichholztobel-Fm. | Formation de l&#39;Eichholztobel     |
|15203153 | Schloss-Fm. | Formation de Schloss     |
|15203154 | Gaschlo-Fm. | Formation de Gaschlo     |
|15203155 | Leimern-Sch.: Kalkige-Fazies | Calcaire de la Leimern     |
|15203156 | Pierre-Avoi-Melange | Mélange de la Pierre Avoi     |
|15203157 | St-Christophe-Fm. | Formation de St-Christophe     |
|15203158 | Marmontains-Fm. | Formation des Marmontains     |
|15203159 | Aroley-Fm. | Formation de l&#39;Aroley     |
|15203160 | Ferret-Schiefer: Peula-Sch. | Couches de la Peula     |
|15203161 | Versoyen-Sch. | Couches du Versoyen     |
|15203162 | Prättigau-Schiefer | Schistes du Prättigau     |
|15203163 | Ruchberg-Fm. | Formation du Ruchberg     |
|15200671 | Le-Coin-Fm. | Le-Coin-Fm.     |
|15200672 | Bärschwil-, St-Ursanne- und Pichoux-Fm. | Bärschwil-, St-Ursanne- und Pichoux-Fm.     |
|15200673 | Passwang- bis Ifenthal-Fm. | Passwang- bis Ifenthal-Fm.     |
|15200674 | Calcaire à Entroques | Calcaire à Entroques     |
|15200675 | Staffelegg-Fm. und Opalinus-Ton | Staffelegg-Fm. und Opalinus-Ton     |
|15200676 | Schafisheim-Syenit | Schafisheim-Syenit     |
|15200677 | Pfaffnau-Granit | Pfaffnau-Granit     |
|15200678 | Zurzach-Granit | Zurzach-Granit     |
|15200679 | Siblingen-Granit | Siblingen-Granit     |
|15200680 | Lindau-Granit | Lindau-Granit     |
|15200681 | Kreuzlingen-Granit | Kreuzlingen-Granit     |
|15200682 | Schlächtenhaus-Schiefer | Schlächtenhaus-Schiefer     |
|15200683 | Gersbach-Schiefer | Gersbach-Schiefer     |
|15200684 | Herdern-Streifengneis | Herdern-Streifengneis     |
|15200685 | Courgenay- Balsthal- und VilligenFm. | Courgenay- Balsthal- und VilligenFm.     |
|15200686 | Pichoux-Fm.: Korallenfazies | Pichoux-Fm.: Korallenfazies     |
|15200687 | Pichoux-Fm.: Schwammfazies | Pichoux-Fm.: Schwammfazies     |
|15200688 | Kalter-Wangen-Fm.: Konglomerat-dominierte Fazies | Kalter-Wangen-Fm.: Konglomerat-dominierte Fazies     |
|15200689 | Kalter-Wangen-Fm.: Sandstein-Mergelstein-dominierte Fazies | Kalter-Wangen-Fm.: Sandstein-Mergelstein-dominierte Fazies     |
|15200690 | Kalter-Wangen-Fm.: Heilsberg-Bentonit | Kalter-Wangen-Fm.: Heilsberg-Bentonit     |
|15201586 | Seeb-Stadium | Seeb-Stadium     |
|15201587 | Würenlos-Stadium | Würenlos-Stadium     |
|15201588 | Würenlos-Stand-I | Würenlos-Stand-I     |
|15201589 | Würenlos-Stand-II | Würenlos-Stand-II     |
|15201590 | Bülach-Stadium | Bülach-Stadium     |
|15201591 | Bülach-Stand-I | Bülach-Stand-I     |
|15201592 | Bülach-Stand-II | Bülach-Stand-II     |
|15201595 | Stein-am-Rhein-Stand-II | Stein-am-Rhein-Stand-II     |
|15201596 | Stein-am-Rhein-Stand-III | Stein-am-Rhein-Stand-III     |
|15201597 | Zürich-Stadium | Zürich-Stadium     |
|15201599 | Zürich-Stand-II | Zürich-Stand-II     |
|15201601 | Bremgarten-I | Bremgarten-I     |
|15201602 | Bremgarten-II | Bremgarten-II     |
|15201604 | Feuerthalen-Stadium | Feuerthalen-Stadium     |
|15201605 | Feuerthalen-Stand-I | Feuerthalen-Stand-I     |
|15201609 | Hittnau-Seeablagerung | Hittnau-Seeablagerung     |
|15201610 | Russikon-Seeablagerung | Russikon-Seeablagerung     |
|15201611 | Stetten-Stadium | Stetten-Stadium     |
|15201612 | Stetten-Stand-I | Stetten-Stand-I     |
|15201613 | Stetten-Stand-II | Stetten-Stand-II     |
|15201614 | Diessenhofen-Stadium | Diessenhofen-Stadium     |
|15201615 | Mellingen-Stand | Mellingen-Stand     |
|15201616 | Schaffhausen-Stadium | Schaffhausen-Stadium     |
|15201617 | Schaffhausen-Stand-I | Schaffhausen-Stand-I     |
|15201618 | Schaffhausen-Stand-II | Schaffhausen-Stand-II     |
|15201619 | Killwangen-Stadium | Killwangen-Stadium     |
|15201620 | Lottstetten-, Kohlschwärze- und Zelgli-Vorstoss | Lottstetten-, Kohlschwärze- und Zelgli-Vorstoss     |
|15202268 | Ausserbinn-Piz-Cavel-Zone | zone d&#39;Ausserbinn-Piz Cavel     |
|15202271 | Prosa-Granit | Granite du (Monte) Prosa     |
|15202272 | Val-Tremola-Granit | Granite du Val Tremola     |
|15202273 | Leventina-Gneis | Gneiss de la Leventina     |
|15202274 | Lucomagno-Decke: Prävariszischer Orthogneis | Orthogneiss de la nappe du Lukmanier     |
|15202275 | Lucomagno-Decke: Prävariszischer Paragneis | Paragneiss de la nappe du Lukmanier     |
|15202276 | Val-Stgira-Riffmarmor | Marbre du Val Stgira     |
|15202277 | Piz-Terri-Lunschania: Fossilmarmor | Fossilmarmor     |
|15202278 | Piz-Terri-Lunschania: Trias | Trias de Fanee     |
|15202279 | Ultrahelvetischer Flysch | Unités de flysch ultrahelvétiques     |
|15202280 | Sardona-Decke: Melange | Mélange du Sardona     |
|15202281 | Martinsmad-Fm. | Formation de Martinsmad     |
|15202282 | Martinsmad-Fm.: Supraquarzitischer Flysch | Obere Flyschabfolge (Sardona)     |
|15202283 | Martinsmad-Fm.: Sardona-Mb. | Quartzite du Sardona     |
|15202284 | Martinsmad-Fm.: Infraquarzitischer Flysch | Untere Flyschabfolge (Sardona)     |
|15202285 | Meilleret-Fm. | Formation du Meilleret     |
|15202286 | Lavtina-Sandstein | Grès de Lavtina     |
|15202287 | Blattengrat-Sandstein | Grès du Blattengrat     |
|15202288 | Burg-Sandstein | Grès de Burg     |
|15202289 | Elm-Fm.: Val-d&#39;Illiez-Sandstein | Grès du Val-d&#39;Illiez     |
|15202542 | Nordhelvetische Flysch-Gr.: Schiefriger Tonstein | Formations d&#39;Elm et de Matt: argillite schisteuse     |
|15202543 | Tierwis-Fm.: Schiefrige Fazies | Schistes de la Schwalmern     |
|15202544 | Tierwis-Fm.: Kalkige Fazies | Calcaire de la Schwalmern     |
|15202545 | Bommerstein-Fm.: Glockhaus-Mb.: Schiefriger Eisensandstein | Membre du Glockhaus: grès ferrugineux schisteux     |
|15202546 | Helvetikum: Trias: Dolomit | Dolomie du Trias helvétique     |
|15202547 | Helvetikum: Trias: Rauwacke | Cornieule du Trias helvétique     |
|15202548 | Helvetikum: Trias: Gips | Gypse du Trias helvétique     |
|15202549 | Baltschieder-Granodiorit: Biotittonalit | Granodiorite de Baltschieder: tonalite à biotite     |
|15202550 | Baltschieder-Granodiorit: Hornblende Biotittonalit | Granodiorite de Baltschieder: tonalite à biotite et horneblende     |
|15202551 | Erstfeld-Gneiskomplex: Biotit-Plagioklasgneis | Complexe gneissique d&#39;Erstfeld: gneiss à plagioclase et biotite     |
|15202552 | Erstfeld-Gneiskomplex: Orthogneis | Complexe gneissique d&#39;Erstfeld: orthogneiss     |
|15202553 | Erstfeld-Gneiskomplex: Migmatit | Complexe gneissique d&#39;Erstfeld: migmatite     |
|15202554 | Guttannen-Gneiskomplex: Paragneis | Complexe gneissique de Guttannnen: paragneiss     |
|15202555 | Guttannen-Gneiskomplex: Orthogneis | Complexe gneissique de Guttannnen: orthogneiss     |
|15202556 | Guttannen-Gneiskomplex: Biotit-Chloritschiefer | Complexe gneissique de Guttannnen: schiste à chlorite et biotite     |
|15202557 | Guttannen-Gneiskomplex: Chlorit-Serizitschiefer | Complexe gneissique de Guttannnen: schiste à séricite et chlorite     |
|15202558 | Lötschental-Gneiskomplex: Muskovitgneis | Complexe gneissique du Lötschental: gneiss à muscovite     |
|15200330 | Fm. der Granitischen Molasse | Formation de la Molasse granitique     |
|15200331 | Fm. der Granitischen Molasse: Oberaquitane Mergelzone | Oberaquitane Mergelzone     |
|15200332 | Lausanne-Fm. | Molasse Grise de Lausanne     |
|15200333 | Lausanne-Fm.: Bois-Genoud-Bentonit | Bentonite de Bois-Genoud     |
|15200334 | Lausanne-Fm.: Cuarny-Sandstein | Grès de Cuarny     |
|15200335 | USM-I | USM-I     |
|15200336 | Grès et Marnes Gris à Gypse | Grès et Marnes Gris à Gypse     |
|15200337 | Molasse à Charbon | Molasse à Charbon     |
|15200338 | Molasse Rouge | Molasse Rouge     |
|15200339 | Heuboden-Äschitannen-Nagelfluh | Poudingue de Heuboden-Äschitannen     |
|15200340 | Beichlen-Fm. | Formation de la Beichlen     |
|15200341 | USM-J | USM-J     |
|15200342 | USM-J: La-Chaux-Süsswasserkalk | Calcaire d&#39;eau douce de La Chaux     |
|15200343 | Elsässer Molasse | Molasse alsacienne s.s.     |
|15200344 | Elsässer Molasse: Delémont-Süsswasserkalk | Calcaire d&#39;eau douce de Delémont     |
|15200345 | Elsässer Molasse: Matzendorf-Süsswasserkalk | Calcaire d&#39;eau douce de Matzendorf     |
|15200346 | Elsässer Molasse: Oensingen-Süsswasserkalk | Calcaire d&#39;eau douce d&#39;Oensingen     |
|15200347 | Elsässer Molasse: Wynau-Süsswasserkalk | Calcaire d&#39;eau douce de Wynau     |
|15200348 | UMM (Untere Meeresmolasse) | Molasse marine inférieure (UMM)     |
|15200349 | UMM-III | UMM-III     |
|15200691 | OSM: Humlikon-Bentonit | OSM: Humlikon-Bentonit     |
|15202001 | Habkern-Melange | Mélange de Habkern     |
|15202002 | Sörenberg-Melange | Mélange de Sörenberg     |
|15202003 | Wildhaus-Melange | Mélange de Wildhaus     |
|15202004 | Südhelvetischer Flysch | Unités de flysch sud-helvétiques     |
|15202005 | Nordhelvetische Flysch-Gr. | Groupe du Flysch nord-helvétique     |
|15202006 | Matt-Fm. | Formation de Matt     |
|15202007 | Matt-Fm.: Engi-Dachschiefer | Schistes ardoisiers d&#39;Engi     |
|15202008 | Matt-Fm.: Gruontal-Konglomerat | Conglomérat du Gruontal     |
|15202009 | Elm-Fm. | Formation d&#39;Elm     |
|15202010 | Matt-Fm.: Gruontal-Konglomerat: Rüschenweid-Bk. | Banc du Rüschenweid     |
|15202011 | Taveyannaz-Fm. | Formation de Taveyannaz     |
|15202012 | Helvetikum: Paläogen | Paléogène de l&#39;Helvétique     |
|15202013 | Stad-Fm. | Formation de Stad     |
|15202014 | Stad-Fm.: Wängen-Kalk | Calcaire de Wängen     |
|15202015 | Stad-Fm.: Jochstock-Konglomerat | Conglomérat du Jochstock     |
|15202016 | Sanetsch-Fm. | Formation du Sanetsch     |
|15202017 | Sanetsch-Fm.: Pierredar-Kalk | Calcaire de Pierredar     |
|15202018 | Sanetsch-Fm.: Tsanfleuron-Mb. | Membre de Tsanfleuron     |
|15202019 | Sanetsch-Fm.: Diablerets-Mb. | Membre des Diablerets     |
|15202020 | Niederhorn-Fm. | Formation du Niederhorn     |
|15201621 | Grafschaft-Schotter | Grafschaft-Schotter     |
|15201622 | &#34;Mittelterrasse&#34; | &#34;Mittelterrasse&#34;     |
|15201593 | Stein-am-Rhein-Stadium | Stein-am-Rhein-Stadium     |
|15201624 | Hochterrasse, mittleres Niveau | Hochterrasse, mittleres Niveau     |
|15201625 | Hochterrasse, oberes Niveau | Hochterrasse, oberes Niveau     |
|15201626 | First-Schotter | First-Schotter     |
|15201627 | Helltobel-Schotter | Helltobel-Schotter     |
|15201628 | Lettenberg-Seesedimente | Lettenberg-Seesedimente     |
|15201594 | Stein-am-Rhein-Stand-I | Stein-am-Rhein-Stand-I     |
|15201630 | Ursplen-Till | Ursplen-Till     |
|15201631 | Äntschberg-Schotter | Äntschberg-Schotter     |
|15201632 | Oberrüti-Schotter | Oberrüti-Schotter     |
|15201633 | Neerach-Schotter | Neerach-Schotter     |
|15201634 | Bachs-Schotter | Bachs-Schotter     |
|15201635 | Steighalden-Schotter | Steighalden-Schotter     |
|15201636 | Mühlbach-Formation | Mühlbach-Formation     |
|15201637 | Chilchberg-Schotter | Chilchberg-Schotter     |
|15201638 | Frenkendorf-Schotter | Frenkendorf-Schotter     |
|15201639 | Birstal-Schotter | Birstal-Schotter     |
|15201640 | Schlatt-Formation | Schlatt-Formation     |
|15201641 | Illmensee-Formation | Illmensee-Formation     |
|15201642 | Dietmanns-Formation | Dietmanns-Formation     |
|15201643 | Hasenweiler-Formation | Hasenweiler-Formation     |
|15201644 | Haseltal-Formation | Haseltal-Formation     |
|15201645 | Birndorf-, Laufenburg- und Zeiningen-Vorstoss | Birndorf-, Laufenburg- und Zeiningen-Vorstoss     |
|15201646 | Chäppeli-Schotter | Chäppeli-Schotter     |
|15201647 | Leuggern-Schotter | Leuggern-Schotter     |
|15201648 | Zelgli-Schotter | Zelgli-Schotter     |
|15201649 | Leibstadt-Schotter | Leibstadt-Schotter     |
|15201650 | Dogern-Schotter | Dogern-Schotter     |
|15201651 | Haldenacher-Schotter | Haldenacher-Schotter     |
|15201652 | Allmendwald-Schotter | Allmendwald-Schotter     |
|15201598 | Zürich-Stand-I | Zürich-Stand-I     |
|15201654 | Obersäckingen-Schotter | Obersäckingen-Schotter     |
|15201655 | Schulerholz-Formation | Schulerholz-Formation     |
|15201656 | Schachen-Formation | Schachen-Formation     |
|15201657 | Schmerlet-Formation | Schmerlet-Formation     |
|15201658 | Toktri-Formation | Toktri-Formation     |
|15202290 | Muot-da-Rubi-Fm. | Formation du Muot da Rubi     |
|15202291 | Muot-da-Rubi-Fm.: Ahornen-Mb. | Membre du Ahornen     |
|15202292 | Muot-da-Rubi-Fm.: Kistenstöckli-Mb. | Membre du Kistenstöckli     |
|15202293 | Muot-da-Rubi-Fm.: Ghölzwald-Mb. | Membre du Ghölzwald     |
|15202294 | Muot-da-Rubi-Fm.: Malor-Mb. | Membre du Malor     |
|15202295 | Südelgrabe-Melange | Membre du Südelbach     |
|15202296 | Stad-Fm.: Kleintal-Konglomerat | Conglomérat du Kleintal     |
|15202297 | Stad-Fm.: Rütenen-Konglomerat | Conglomérat de Rütenen     |
|15202298 | Helvetikum: Jura | Jurassique de l&#39;Helvétique     |
|15202299 | Wang-Fm.: Brekzie | Brèche de Wang     |
|15202300 | Schrattenkalk-Fm.: Oberer Teil | «Oberer Schrattenkalk»     |
|15202301 | Schrattenkalk-Fm.: Unterer Teil | «Unterer Schrattenkalk»     |
|15202302 | Quinten-Fm.: Oberer Quintner Kalk | «Oberer Quinten-Kalk»     |
|15202303 | Quinten-Fm.: Unterer Quintner Kalk | «Unterer Quinten-Kalk»     |
|15202304 | Erzegg-Fm.: Planplatte-Eisenoolith | Oolite ferrugineuse de la Planplatte     |
|15202305 | Bommerstein-Fm.: Geissbach-Konglomerat | Conglomérat du Geissbach     |
|15202306 | Bommerstein-Fm.: Stöckli-Sandstein | Grès de Stöckli     |
|15202307 | Infrapräalpines Melange | Mélange Infrapréalpin     |
|15202308 | Iberg-Melange | Mélange d&#39;Iberg     |
|15202559 | Lötschental-Gneiskomplex: Migmatitischer Biotitgneis | Complexe gneissique du Lötschental: gneiss à biotite migmatitique     |
|15202560 | Lötschental-Gneiskomplex: Chloritschiefer | Complexe gneissique du Lötschental: schiste à chlorite     |
|15202561 | Ofenhorn-Stampfhorn-Gneiskomplex: Gebänderter Biotitgneis | Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: gneiss rubané à plagioclase et biotite     |
|15202562 | Ofenhorn-Stampfhorn-Gneiskomplex: Migmatit | Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: migmatite     |
|15202563 | Ofenhorn-Stampfhorn-Gneiskomplex: Biotitgneis | Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: gneiss à biotite     |
|15202564 | Ofenhorn-Stampfhorn-Gneiskomplex: Orthogneis | Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: orthogneiss     |
|15202565 | Bäregg-Gneiskomplex: Mylonitischer Orthogneis | Complexe gneissique de la Bäregg: orthogneiss mylonitique     |
|15202566 | Bäregg-Gneiskomplex: Mylonitischer Paragneis | Complexe gneissique de la Bäregg: paragneiss mylonitique     |
|15202567 | Bäregg-Gneiskomplex: Metavulkanite | Complexe gneissique de la Bäregg: métavulcanite     |
|15202568 | Grimsel-Granodiorit: Aplitische Randfazies | Granodiorite du Grimsel: faciès aplitique de bordure     |
|15202569 | Voralp-Granit: Saure Randfazies | Granite de la Voralp: faciès acide de bordure     |
|15202570 | Tamina-Gneiskomplex | Complexe gneissique de la Tamina     |
|15202571 | Tamina-Gneiskomplex: Schiefriger Biotitgneis | Complexe gneissique de la Tamina: gneiss schisteux à biotite     |
|15202572 | Tamina-Gneiskomplex: Mylonit | Complexe gneissique de la Tamina: mylonitique     |
|15202573 | Innertkirchen-Migmatit: Marmor | Migmatite d&#39;Innertkirchen: marbre     |
|15202574 | Guttannen-Gneiskomplex: Migmatit | Complexe gneissique de Guttannnen: migmatite     |
|15202575 | Guttannen-Gneiskomplex: Amphibolit-reiche Fazies | Complexe gneissique de Guttannnen: avec amphibolite     |
|15200350 | Horw-Sandstein | Grès d&#39;Horw     |
|15200351 | UMM-II | UMM-II     |
|15200352 | Grisigen-Mergel | Marne de Grisigen     |
|15200353 | UMM-I | UMM-I     |
|15200354 | Cucloz-Fm. | Sous-formation de Cucloz     |
|15200355 | Cucloz-Fm.: Cucloz-Sandstein | Grès de Cucloz     |
|15200356 | Cucloz-Fm.: Marnes gris-souris | Marnes gris-souris     |
|15200357 | Cucloz-Fm.: Schistes marno-micacés | Schistes marno-micacés     |
|15200358 | Hilfern-Fm. | Formation de la Hilfern     |
|15200359 | Rietbad-Fm. | Sous-formation de Rietbad     |
|15200360 | Jordisboden-Mergel | Marne du Jordisboden     |
|15200361 | Goldegg-Sandstein | Grès de la Goldegg     |
|15200362 | UMM-J | UMM-J     |
|15200363 | UMM-J: Septarienton | Argile à Septaria (Septarienton)     |
|15200364 | UMM-J: Fischschiefer | Schistes à Poissons (Fischschiefer)     |
|15200365 | UMM-J: Foraminiferenmergel | Marnes à Foraminifères (Foraminiferenmergel)     |
|15200366 | UMM-J: Meeressand | Meeressand     |
|15200368 | UMM-J: Cyathulabank | Banc à Cyathula (bassin de Laufon)     |
|15200369 | UMM-J: Cyrenenmergel | Marne à Cyrènes     |
|15200370 | Porrentruy-Konglomerat | Conglomérat de Porrentruy     |
|15200371 | Rossemaison-Fm.: Süsswasserkalk | Raitsche     |
|15202021 | Niederhorn-Fm.: Gemmenalp-Kalk | Calcaire de la Gemmenalp     |
|15202022 | Niederhorn-Fm.: Hohgant-Sandstein | Grès du Hohgant     |
|15202023 | Niederhorn-Fm.: Hohgant-Sandstein: Wagenmoos-Bk. | Couches du Wagenmoos     |
|15202024 | Wildstrubel-Fm. | Formation du Wildstrubel     |
|15202025 | Wildstrubel-Fm.: Schimberg-Mb. | Membre du Schimberg     |
|15202026 | Wildstrubel-Fm.: Tierberg-Mb. | Membre du Tierberg     |
|15202027 | Wildstrubel-Fm.: Küblibad-Mb. | Membre du Küblibad     |
|15202028 | Klimsenhorn-Fm. | Formation du Klimsenhorn     |
|15202029 | Klimsenhorn-Fm.: Fruttli-Mb. | Membre du Fruttli     |
|15202030 | Klimsenhorn-Fm.: Band-Mb. | Membre du Bandweg     |
|15202031 | Klimsenhorn-Fm.: Fräkmünt-Mb. | Membre de Fräkmünt     |
|15202032 | Bürgen-Fm. | Membre du Bürgen(stock)     |
|15202033 | Bürgen-Fm.: Foribach-Mb. | Membre du Foribach     |
|15202034 | Bürgen-Fm.: Mattgrat-Mb. | Membre du Mattgrat     |
|15202035 | Bürgen-Fm.: Scharti-Mb. | Membre de Scharti     |
|15202036 | Euthal-Fm. | Formation d&#39;Euthal     |
|15202037 | Bürgen-Fm.: Steinbach-Mb. | Membre du Steinbach     |
|15202038 | Euthal-Fm.: Einsiedeln-Mb. | Membre d&#39;Einsiedeln     |
|15202039 | Euthal-Fm.: Batöni-Mb. | Membre de la Batöni     |
|15202040 | Euthal-Fm.: Chruteren-Mb. | Membre de la Chruteren     |
|15201659 | Buchholz-Till | Buchholz-Till     |
|15201660 | Birndorf-Till | Birndorf-Till     |
|15201661 | Geissäcker-Schotter | Geissäcker-Schotter     |
|15201662 | Bürgerwald-Schotter | Bürgerwald-Schotter     |
|15201663 | Hettenschwil-Schotter | Hettenschwil-Schotter     |
|15201664 | Moos-Schotter | Moos-Schotter     |
|15201600 | Bremgarten-Stadium | Bremgarten-Stadium     |
|15201666 | Hundsbel-Schotter | Hundsbel-Schotter     |
|15201667 | Laufenburg-Schotter | Laufenburg-Schotter     |
|15201668 | Eilez-Schotter | Eilez-Schotter     |
|15201669 | St.-Margarethen-Schotter | St.-Margarethen-Schotter     |
|15201670 | Hegenheim-Schotter | Hegenheim-Schotter     |
|15201671 | Blotzheim-Schotter | Blotzheim-Schotter     |
|15201672 | Hardwald-Schotter | Hardwald-Schotter     |
|15201673 | Homberg-Schotter | Homberg-Schotter     |
|15201674 | Rümlang-Schotter | Rümlang-Schotter     |
|15201675 | Äpelöö-Schotter | Äpelöö-Schotter     |
|15201676 | Fehrental-Schotter | Fehrental-Schotter     |
|15201677 | Challeren-Schotter | Challeren-Schotter     |
|15201678 | Ausserberg-Schotter | Ausserberg-Schotter     |
|15201679 | Leibstadt-Till | Leibstadt-Till     |
|15201680 | Buechli-Schotter | Buechli-Schotter     |
|15201681 | Bächemoos-Schotter | Bächemoos-Schotter     |
|15201682 | Aarberg-Schotter | Aarberg-Schotter     |
|15201603 | Singen-Stadium | Singen-Stadium     |
|15201684 | Etzwil-Schotter | Etzwil-Schotter     |
|15201685 | Ellenbühl-Schotter | Ellenbühl-Schotter     |
|15201686 | Kegelplatz-Schotter | Kegelplatz-Schotter     |
|15201687 | Einschlag-Schotter | Einschlag-Schotter     |
|15201688 | Lehacker-Schotter | Lehacker-Schotter     |
|15201689 | Letten-Schotter | Letten-Schotter     |
|15201690 | Schwörstadt-Schotter | Schwörstadt-Schotter     |
|15201691 | Steppberg-Schotter | Steppberg-Schotter     |
|15201692 | Bloseberg-Schotter | Bloseberg-Schotter     |
|15201693 | Steinebol-Schotter | Steinebol-Schotter     |
|15201694 | Giebenach-Schotter | Giebenach-Schotter     |
|15201695 | Blözen-Schotter | Blözen-Schotter     |
|15201696 | Rütihard-Schotter | Rütihard-Schotter     |
|15201697 | Bruederholz-Schotter | Bruederholz-Schotter     |
|15201698 | Binningen-Schotter | Binningen-Schotter     |
|15202309 | Iberg-Melange: Surbrunnen-Flysch | Flysch de Surbrunnen     |
|15202310 | Iberg-Melange: Roggenegg-Komplex | Complexe de la Roggenegg     |
|15202311 | Iberg-Melange: Isentobel-Komplex | Complexe de l&#39;Isentobel     |
|15202312 | Serhalten-Melange | Flysch der Serhalten     |
|15202313 | Iberg-Melange: Gwürz-Flysch | Flysch de Gwürz     |
|15202314 | Ruestel-Flysch | Flysch de Ruestel     |
|15202315 | Iberg-Melange: Scheidegg-Flysch | Flysch de la Scheidegg     |
|15202316 | Habkern-Granit | Granite de Habkern     |
|15202317 | Infrapräalpines Melange: Gros-Plané-Melange | Mélange du Gros Plané     |
|15202318 | Infrapräalpines Melange: Bodevena-Melange | Mélange de la Bodevena     |
|15202319 | Subalpiner Flysch | Flysch Subalpin     |
|15202320 | Torrenthorn-Fm. | Formation du Torrenthorn     |
|15202321 | Prodkamm-Fm.: Cardinien-Mb.: Weissgandstöckli-Bk. | Banc du Weissgandstöckli     |
|15202322 | Mären-Fm.: Grisch-Mb. | Membre du (Piz) Grisch     |
|15202323 | Mären-Fm.: Foostock-Mb. | Membre du Foostock     |
|15202324 | Murgtal-Fm. | Formation du Murgtal     |
|15202325 | Vernayaz-Fm.: Dzéman-Mb. | Membre du Dzéman     |
|15202326 | Zentraler-Aare-Granit: Aplitische Randfazies | Faciès de bordure aplitique du Granite Central de l&#39;Aar     |
|15202576 | Guttannen-Gneiskomplex: Aplitischer Granit | Complexe gneissique de Guttannnen: granite aplitique     |
|15202577 | Guttannen-Gneiskomplex: Marmor | Complexe gneissique de Guttannnen: marbre     |
|15202578 | Guttannen-Gneiskomplex: Ultramafisches Gestein | Complexe gneissique de Guttannnen: roche ultramafique     |
|15202579 | Ofenhorn-Stampfhorn-Gneiskomplex: Schollenamphibolit-reiche Fazies | Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: avec amphibolite à blocs     |
|15202580 | Ofenhorn-Stampfhorn-Gneiskomplex: Aplitischer Granit | Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: granite aplitique     |
|15202581 | Ofenhorn-Stampfhorn-Gneiskomplex: Schollenamphibolit | Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: amphibolite à blocs     |
|15202582 | Ofenhorn-Stampfhorn-Gneiskomplex: Ultramafisches Gestein | Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: roche ultramafique     |
|15202583 | Bommerstein- und Reischiben-Fm. | Formations de Bommerstein et de Reischiben, indifférenciées     |
|15202584 | Mels- und Röti-Fm. | Formations de Mels et de Röti, indifférenciées     |
|15202585 | Guttannen-Gneiskomplex: Schierfriger Biotit-Chlorit-Serizit-Gneis | Complexe gneissique de Guttannnen: gneiss schisteux à biotite, chlorite, séricite     |
|15202586 | Zettenalp-Trochematt-Melange | Mélange de la Zettenalp-Trochematt     |
|15202587 | Laubersmad-Flysch | Flysch du Laubersmad     |
|15202588 | Stad-Fm.: Quarzsandstein | Formation de Stad, «Jüngerer Quarzsandstein»     |
|15202589 | Euthal-Fm.: Einsiedeln-Mb.: Quarzsandstein | Membre d&#39;Einsiedeln, «Älterer Quarzsandstein»     |
|15202590 | Schrattenkalk-Fm.: vermergelt | Formation du Schrattenkalk, devenant marneuse     |
|15202591 | Stad-Fm.: Wängen-Kalk: Lithothamnienkalk-Fazies | Calcaire de Wängen, faciès calcaire à Lithothamnies     |
|15200373 | Ajoie-Gompholit | Gompholite d&#39;Ajoie     |
|15200378 | Tüllingen-Süsswasserkalk | Calcaire d&#39;eau douce de Tüllingen     |
|15200380 | Hauptogenstein: Oberer Teil | Partie supérieure du Hauptrogenstein     |
|15200382 | Hauptogenstein: Unterer Teil | Partie inférieure du Hauptrogenstein     |
|15200383 | Hauptrogenstein: Calcaire roux marneux | Calcaire roux marneux     |
|15200384 | Bois-de-Raube-Fm.: Ajoie-Mb. | Membre d&#39;Ajoie     |
|15200385 | Bois-de-Raube-Fm.: Bois-de-Raube-Mb. | Membre du Bois de Raube     |
|15200386 | Bois-de-Raube-Fm.: Montchaibeux-Mb. | Membre du Montchaibeux     |
|15200387 | Daubrée-Konglomerat | Conglomérat de Daubrée     |
|15200388 | Wanderblock-Bildungen | Dépôts de blocs pérégrins (Wanderblock-Bildungen)     |
|15200389 | OMM-II: Geröllsande | Sables à galets (OMM)     |
|15200390 | OMM-II: Polymikte Nagelfluh | Poudingue polygénique (OMM)     |
|15200391 | OMM-I: Muschelsandstein | Zone du grès coquillier (OMM)     |
|15200392 | OMM-I: Graue Molasse | Molasse Grise (OMM)     |
|15200393 | Daubrée-Konglomerat: Süsswasserkalk | Calcaire de Daubrée     |
|15200394 | USM: Basale Süsswassermolasse | Formations de la base de l&#39;USM-J     |
|15200395 | Laufen-Juranagelfluh | Juranagelfluh de Laufon     |
|15200396 | Basler Juranagelfluh | Juranagelfluh du Jura bâlois     |
|15200397 | Aargauer Juranagelfluh | Juranagelfluh d&#39;Argovie     |
|15200399 | Jensberg-Fm. | Couches du Jensberg     |
|15202041 | Euthal-Fm.: Fliegenspitz-Mb. | Membre du Fliegenspitz     |
|15202043 | Siderolithikum: Grindelwald-Marmor | Marbre de Grindelwald     |
|15202044 | Niederhorn-Fm.: Hohgant-Sandstein: Mürren-Brekzie | Brèche de Mürren     |
|15202045 | Siderolithikum: Dünden-Konglomerat | Conglomérat de la Dünden     |
|15202046 | Siderolithikum: Rosenlaui-Marmor | Marbre de Rosenlaui     |
|15202047 | Helvetikum: Kreide | Crétacé de l&#39;Helvétique     |
|15202048 | Wang-Fm. | Formation de Wang     |
|15202049 | Amden-Fm. | Marne d&#39;Amden     |
|15202050 | Seewen Fm. | Formation de Seewen     |
|15202051 | Seewen-Fm.: Choltal-Mb. | Membre du Choltal     |
|15202052 | Garschella-Fm. | Formation de Garschella     |
|15202053 | Garschella-Fm.: Selun-Mb. | Membre de Selun     |
|15202054 | Garschella-Fm.: Selun-Mb.: Kamm-Bk. | Banc du Kamm     |
|15202055 | Garschella-Fm.: Selun-Mb.: Aubrig-Sch. | Couches de l&#39;Aubrig     |
|15202056 | Garschella-Fm.: Selun-Mb.: Wannenalp-Bk. | Banc de la Wannenalp     |
|15202057 | Garschella-Fm.: Selun-Mb.: Sellamatt-Sch. | Couches de la Sellamatt     |
|15202058 | Garschella-Fm.: Selun-Mb.: Plattenwald-Bk. | Banc du Plattenwald     |
|15202059 | Garschella-Fm.: Selun-Mb.: Durschlägi-Bk. | Banc de la Durschlägi     |
|15202060 | Garschella-Fm.: Selun-Mb.: Niederi-Sch. | Couches de la Niederi     |
|15201699 | Allschwil-Schotter | Allschwil-Schotter     |
|15201700 | Buschwiller-Schotter | Buschwiller-Schotter     |
|15201606 | Feuerthalen-Stand-II | Feuerthalen-Stand-II     |
|15201702 | Hörndli-Schotter | Hörndli-Schotter     |
|15201703 | Acheberg-Schotter | Acheberg-Schotter     |
|15201704 | Mühleberg-Schotter | Mühleberg-Schotter     |
|15201705 | Mandach-Schotter | Mandach-Schotter     |
|15201706 | Duttenberg-Schotter | Duttenberg-Schotter     |
|15201607 | Schlieren-Stadium | Schlieren-Stadium     |
|15201708 | Frauewald-Schotter | Frauewald-Schotter     |
|15201709 | Bolderen-Schotter | Bolderen-Schotter     |
|15201710 | Seiglisten-Schotter | Seiglisten-Schotter     |
|15201711 | Geispel-Schotter | Geispel-Schotter     |
|15201608 | Bäretswil-Seeablagerung | Bäretswil-Seeablagerung     |
|15202327 | Windgällen-Fm.: Rhyolith | Rhyolithe de la Chli Windgällen     |
|15202328 | Bäregg-Gneiskomplex | Complexe gneissique de la Bäregg     |
|15202329 | Gärsthorn-Gneiskomplex | Complexe gneissique du Gärsthorn     |
|15202330 | Sogn-Placi-Gneiskomplex | Complexe gneissique de Sogn Placi     |
|15202331 | Massa-Gneiskomplex | Complexe gneissique de la Massa     |
|15202332 | Aiguilles-Rouges-Massiv: Mittelvariszische Intrusiva | Roches plutoniques éo-varisques du massif des Aiguilles Rouges     |
|15202333 | Aiguilles-Rouges-Massiv: Frühvariszische Intrusiva | Roches plutoniques éo-varisques du massif des Aiguilles Rouges     |
|15202334 | Aiguilles-Rouges-Massiv: Prävariszisches Grundgebirge | Socle polycyclique anté-varisque du massif des Aiguilles Rouges     |
|15202335 | Chéserys-Gneis | Gneiss des Chéserys     |
|15202336 | Mont-Blanc-Massiv: Spät- bis postvariszische Intrusiva | Roches plutoniques tardi- à post-varisques du massif du Mont Blanc     |
|15202337 | Mont-Blanc-Massiv: Prävariszisches Grundgebirge | Socle polycyclique anté-varisque du massif du Mont Blanc     |
|15202338 | Alp-Cavradi-Gneiskomplex | Complexe gneissique de l&#39;Alp Cavradi     |
|15202339 | Giubine-Gneiskomplex | Complexe gneissique de Giubine     |
|15202340 | Gotthardt-Decke: Prävariszisches polyzyklisches Grundgebirge | Socle polycyclique anté-varisque de la nappe du Gotthard     |
|15202341 | Goms-Gneiskomplex: Unterwassern-Gneis | Gneiss d&#39;Unterwassern     |
|15202343 | Streifengneis-Komplex: Sassina-Augengneis | Gneiss oeillé du Sassina     |
|15202344 | Streifengneis-Komplex: Alp-Ramosa-Granitgneis | Gneiss granitique de l&#39;Alp Ramosa     |
|15202346 | Val-Nalps-Gneiskomplex | Complexe gneissique du Val Nalps     |
|15202592 | Euthal-Fm.: Einsiedeln-Mb.: Alveolinenkalk-Fazies | Membre d&#39;Einsiedeln, faciès calcaire à Alvéolines     |
|15202593 | Niederhorn-Fm.: Hohgant-Sandstein: Sandkalk und Kalk | Grès du Hohgant, calcaire gréseux et calcaire     |
|15202594 | Interne Einsiedeln-Schuppen: Tektonisches Melange | Mélange tectonique des écailles internes d&#39;Einsiedeln     |
|15202595 | Bürgen- und Wildstrubel-Fm. | Formations du Bürgen et d&#39;Euthal, indiff.     |
|15202596 | Einsiedeln- und Steinbach-Mb. | Formation de l&#39;Euthal et Membre du Steinbach, indiff.     |
|15202597 | Stad-Fm.: e6 | Formation de Stad (e6)     |
|15202598 | Stgir- und Inferno-Fm. | Formations du Stgir et d&#39;Inferno, indifférenciées     |
|15202599 | Quinten-Fm.: Oberer Quintner Kalk: Korallenkalk | Oberer Quintner Kalk: calcaire à coraux     |
|15202600 | Quinten-Fm.: Oberer Quintner Kalk: Unterer Kalk | Oberer Quintner Kalk: Unterer Kalk     |
|15202601 | Prodkamm- bis Sexmor-Fm. | Formation du Prodkamm à Formation du Sexmor, indifférenciées     |
|15202602 | Plattenzüg-Fm. | Formation du Plattazüg     |
|15202603 | Zemenstein- bis Garschella Fm. | Formation du Zementstein à Formation de Garschella, indifférenciées     |
|15202604 | Euthal-Fm.: Vasanachopf-Mb | Formation d&#39;Euthal: faciès argilo-schisteux noir     |
|15202605 | Pfäfers-Fm. | Pfäfers-Fm.     |
|15202606 | Euthal- und Bürgen-Fm. | Euthal- und Bürgen-Fm.     |
|15202607 | Amden- und Wang-Fm. | Amden- und Wang-Fm.     |
|15202608 | Seewen- und Amden-Fm. | Seewen- und Amden-Fm.     |
|15202609 | Betlis- bis Schrattenkalk-Fm. | Betlis- bis Schrattenkalk-Fm.     |
|15200400 | Jensberg-Fm.: Rebhubel-Sch. | Couches du Rebhubel     |
|15200401 | Niedermatt-Fm. | Formation de Niedermatt     |
|15200402 | Belpberg-Fm. | Formation du Belpberg     |
|15200403 | Kalchstätten-Fm.: Pfadflüe-Nagelfluh | Poudingue de la Pfadflüe     |
|15200404 | Belpberg-Fm.: Sädel-Kalknagelfluh | Poudingue calcaire de Sädel     |
|15200405 | Belpberg-Fm.: Utzigen-Muschelsandstein | Grès coquillier d&#39;Utzigen     |
|15200406 | Belpberg-Fm.: Ulmiz-Quarzitnagelfluh | Poudingue quarzitique d&#39;Ulmiz     |
|15200407 | Belpberg-Fm.: Bütschelbach-Nagelfluh | Poudingue du Bütschelbach     |
|15200408 | Kalchstätten-Fm. | Formation de Kalchstätten     |
|15200409 | St.-Gallen-Fm.: Freudenberg-Nagelfluh | Poudingue du Freudenberg     |
|15200410 | St.-Gallen-Fm.: Goldbrunnen-Sch. | Couches de Goldbrunnen     |
|15200411 | St.-Gallen-Fm.: Dreilinden-Nagelfluh | Poudingue de Dreilinden     |
|15200412 | St.-Gallen-Fm.: Obere Grenznagelfluh | Obere Grenznagelfluh (Fm. de Saint-Gall)     |
|15200413 | Kirchberg-Fm. | Formation de Kirchberg     |
|15200414 | Grimmelfingen-Fm. | Formation de Grimmelfingen     |
|15200415 | Chnebelburg-Fm. | Couches de la Chnebelburg     |
|15200416 | Chnebelburg-Fm.: Meinisberg-Muschelsandstein | Grès coquillier de Meinisberg     |
|15200417 | Chnebelburg-Fm.: Brüttelen-Grobsandstein | Poudingue coquillier de Brüttelen     |
|15200418 | Sense-Fm. | Formation de la Singine     |
|15202061 | Garschella-Fm.: Selun-Mb.: Twäriberg-Bk. | Banc du Twäriberg     |
|15202062 | Garschella-Fm.: Selun-Mb.: Klaus-Bk. | Banc de Klaus     |
|15202063 | Garschella-Fm.: Rankweil-Mb. | Membre de Rankweil     |
|15202064 | Garschella-Fm.: Brisi-Mb. | Membre de la Brisi     |
|15202065 | Garschella-Fm.: Brisi-Mb.: Kalkige Fazies | Calcaire de la Brisi     |
|15202066 | Garschella-Fm.: Brisi-Mb.: Sandige Fazies | Grès de la Brisi     |
|15202067 | Garschella-Fm.: Brisi-Mb.: Gams-Sch. | Couches du Gams     |
|15202068 | Garschella-Fm.: Brisi-Mb.: Luitere-Bk. | Banc de la Luitere     |
|15202069 | Garschella-Fm.: Freschen-Mb. | Membre du Freschen     |
|15202070 | Garschella-Fm.: Freschen-Mb.: Hochkugel-Sch. | Couches du Hochkugel     |
|15202071 | Garschella-Fm.: Grünten-Mb. | Membre du Grünten     |
|15202072 | Garschella-Fm.: Grünten-Mb.: Rohrbachstein-Bk. | Banc du Rohrbachstein     |
|15202073 | Schrattenkalk-Fm. | Formation du Schrattenkalk     |
|15202074 | Schrattenkalk-Fm.: Rawil-Mb. | Membre du Rawil     |
|15202075 | Tierwis-Fm. | Formation de Tierwis     |
|15202076 | Tierwis-Fm.: Chopf-Bk. | Banc du Chopf     |
|15202077 | Tierwis-Fm.: Drusberg-Mb. | Membre du Drusberg     |
|15202078 | Tierwis-Fm.: Altmann-Mb. | Membre de l&#39;Altmann     |
|15201701 | Berchenwald-Schotter | Berchenwald-Schotter     |
|15202610 | Öhrli- bis Schrattenkalk-Fm. | Öhrli- bis Schrattenkalk-Fm.     |
|15202611 | Bommerstein-Fm.: Basisbildungen | Bommerstein-Fm.: Basisbildungen     |
|15202612 | Öhrli- und Betlis-Fm. | Öhrli- und Betlis-Fm.     |
|15202613 | Erzegg-Fm.: Grenzschicht | Erzegg-Fm.: Grenzschicht     |
|15202614 | Spitzmeilen-Fm.: Bränd-Brekzie | Spitzmeilen-Fm.: Bränd-Brekzie     |
|15202615 | Infralias-Sandstein | Infralias-Sandstein     |
|15202616 | Nufenen-Zone: Phyllitische Trias | Nufenen-Zone: Phyllitische Trias     |
|15202617 | Nufenen-Zone: Karbonatische Trias | Nufenen-Zone: Karbonatische Trias     |
|15202618 | Nufenen-Zone: Karbonatische Trias: Kalkmarmor | Nufenen-Zone: Karbonatische Trias: Kalkmarmor     |
|15202619 | Nufenen-Zone: Karbonatische Trias: Dolomit | Nufenen-Zone: Karbonatische Trias: Dolomit     |
|15202620 | Nufenen-Zone: Karbonatische Trias: Rauwacke | Nufenen-Zone: Karbonatische Trias: Rauwacke     |
|15202621 | Nufenen-Zone: Quarzitische Trias | Nufenen-Zone: Quarzitische Trias     |
|15202622 | Urseren-Garvera-Zone: Malm | Urseren-Garvera-Zone: Malm     |
|15202623 | Urseren-Garvera-Zone: Dogger | Urseren-Garvera-Zone: Dogger     |
|15202624 | Urseren-Garvera-Zone: Lias | Urseren-Garvera-Zone: Lias     |
|15202625 | Urseren-Garvera-Zone: Oberer Lias | Urseren-Garvera-Zone: Oberer Lias     |
|15202626 | Urseren-Garvera-Zone: Mittlerer Lias | Urseren-Garvera-Zone: Mittlerer Lias     |
|15202627 | Urseren-Garvera-Zone: Unterer Lias | Urseren-Garvera-Zone: Unterer Lias     |
|15200419 | Sense-Fm.: Montécu-Sch. | Couches de Montécu     |
|15200420 | Sense-Fm.: Molière-Muschelsandstein | Grès coquillier de la Molière     |
|15200421 | Sense-Fm.: Scherli-Nagelfluh | Poudingue quartzitique du Scherli(grabe)     |
|15200422 | Grilly-Süsswasserkalk | Calcaire d&#39;eau douce de Grilly     |
|15200423 | Orbe-Süsswasserkalk | Calcaire d&#39;eau douce d&#39;Orbe     |
|15200424 | USM: Basale Süsswassermolasse: Krustenkalk | Calcaire concrétionné (USM)     |
|15200425 | Gümmenen-Fm. | Formation de Gümmenen     |
|15200429 | USM-II: Obere Bunte Molasse | Molasse bariolée supérieure     |
|15200430 | Oberdorf-Süsswasserkalk | Calcaire d&#39;eau douce d&#39;Oberdorf     |
|15200431 | St.-Gallen-Fm.: Limnischer Horizont | Horizon limnique (OMM-II)     |
|15200432 | OMM-II: Quarzitnagelfluh | Poudingue quartzitique (Fm. de Saint-Gall)     |
|15200433 | Luzern-Fm.: Basales Konglomerat | Conglomérat basal (Fm. de Lucerne)     |
|15200436 | Perte-du-Rhône-Fm.: Poncin-Mb. | Membre de Poncin     |
|15200437 | Perte-du-Rhône-Fm.: Mussel-Mb.: Vraconne-Sandstein | Grès de la Vraconne     |
|15200438 | Perte-du-Rhône-Fm.: Mussel-Mb.: La-Presta-Mergel | Argile de la Presta     |
|15200439 | Perte-du-Rhône-Fm.: Mussel-Mb.: Vernettes-Sandstein | Grès des Vernettes     |
|15200440 | Perte-du-Rhône-Fm.: Mussel-Mb.: Ponthoud-Bk. | Banc du Ponthoud     |
|15200441 | Perte-du-Rhône-Fm.: Mussel-Mb.: Scie-Besse-Sandstein | Grès de Scie Besse     |
|15200442 | Perte-du-Rhône-Fm.: Fulie-Mb.: Mortier-Mergel | Marne du Mortier     |
|15200443 | Perte-du-Rhône-Fm.: Fulie-Mb.: Vauglène-Bk. | Couches de Vauglène     |
|15202079 | Helvetischer Kieselkalk | Kieselkalk Helvétique     |
|15202080 | Helvetischer Kieselkalk: Chriesiloch-Echinodermenkalk | Calcaire échinodermique du Chriesiloch     |
|15202081 | Helvetischer Kieselkalk: Lidernen-Mb. | Membre de la Lidernen     |
|15202082 | Helvetischer Kieselkalk: Gemsmättli-Bk. | Banc du Gemsmättli     |
|15202083 | Helvetischer Kieselkalk: Rahberg-Bk. | Membre du Rahberg     |
|15202084 | Betlis-Fm. | Formation de Betlis     |
|15202085 | Betlis-Fm.: Pygurus-Mb. | Membre à Pygurus     |
|15202086 | Betlis-Fm.: Spitzern-Mb. | Membre de la Spitzeren     |
|15202087 | Betlis-Fm.: Büls-Bk. | Banc de Büls     |
|15202088 | Sichel-Kalk | Calcaire de la Sichel     |
|15202089 | Diphyoides-Kalk | Calcaire à Diphyoides     |
|15202090 | Vitznau-Mergel | Marne de Vitznau     |
|15202091 | Öhrli-Fm. | Formation de l&#39;Öhrli     |
|15202092 | Palfris-Fm. | Formation de Palfris     |
|15202093 | Zementstein-Fm. | Formation du Zementstein     |
|15202094 | Zementstein-Fm.: Grasspass-Mb. | Membre du Graspass     |
|15202095 | Zementstein-Fm.: Gassen-Kalk | Calcaire du Gassen(stock)     |
|15202096 | Helvetikum: Malm | Malm de l&#39;Helvétique     |
|15202097 | Quinten-Fm. | Formation de Quinten     |
|15202098 | Quinten-Fm.: Tros-Kalk | Calcaire de Tros     |
|15202347 | Val-Nalps-Gneiskomplex: Prato-Gneis | Gneiss de Prato     |
|15202348 | Val-Nalps-Gneiskomplex: Distelgrat-Gneis | Gneiss du Distelgrat     |
|15202349 | Paradis-Gneiskomplex: Val-Gronda-Augengneis | Gneiss oeillé du Val Gronda     |
|15202350 | Val-Nalps-Gneiskomplex: Fuorcla-Paradis-Serpentinit | Serpentinite de la Fuorcla Paradis     |
|15202351 | Paradis-Gneiskomplex | Complexe gneissique du (Piz) Paradis     |
|15202352 | Paradis-Gneiskomplex: Oberstafel-Gneis | Gneiss d&#39;Oberstafel     |
|15202353 | Paradis-Gneiskomplex: Ganneretsch-Gneis | Gneiss du (Piz) Ganneretsch     |
|15202354 | Paradis-Gneiskomplex: Corandoni-Amphibolit | Amphibolite de Corandoni     |
|15202355 | Tavetsch-Decke: Prävariszisches polyzyklisches Grundgebirge | Socle polycyclique anté-varisque de la nappe du Tavetsch     |
|15202356 | Rueras-Gneiskomplex | Complexe gneissique de Rueras     |
|15202357 | Aiguilles-Rouges-Massiv: Prä- und frühvariszische Sedimente und Vulkanite | Roches sédimentaires et volcaniques éo-varisques du massif des Aiguilles Rouges     |
|15202358 | Vernayaz-Fm.: Salvan-Mb.: Au-d&#39;Arbignon-Schiefer | Schistes de l&#39;Au d&#39;Arbignon     |
|15202359 | Vernayaz-Fm.: Salvan-Mb.: Dorénaz-Konglomerat | Conglomérat de Dorénaz     |
|15202360 | Wildflysch | Wildflysch     |
|15202361 | Plaine-Morte-Melange | Plaine-Morte-Melange     |
|15202362 | Mättental-Melange | Mättental-Melange     |
|15202363 | Meilleret-Fm.: Höchst-Flysch | Meilleret-Fm.: Höchst-Flysch     |
|15202628 | Urseren-Garvera-Zone: Phyllitische Trias | Urseren-Garvera-Zone: Phyllitische Trias     |
|15202629 | Urseren-Garvera-Zone: Karbonatische Trias | Urseren-Garvera-Zone: Karbonatische Trias     |
|15202630 | Urseren-Garvera-Zone: Permo-Karbon: Psephit- und Psammitgneis | Urseren-Garvera-Zone: Permo-Karbon: Psephit- und Psammitgneis     |
|15202631 | Urseren-Garvera-Zone: Permo-Karbon: Metarhyolith | Urseren-Garvera-Zone: Permo-Karbon: Metarhyolith     |
|15202632 | Urseren-Garvera-Zone: Permo-Karbon: Chloritschiefer | Urseren-Garvera-Zone: Permo-Karbon: Chloritschiefer     |
|15202633 | Urseren-Garvera-Zone: Permo-Karbon: Graphitschiefer | Urseren-Garvera-Zone: Permo-Karbon: Graphitschiefer     |
|15202634 | Gotthard-Decke: Prävariszischer Orthogneis | Gotthard-Decke: Prävariszischer Orthogneis     |
|15202635 | Gotthard-Decke: Prävariszischer Augengneis | Gotthard-Decke: Prävariszischer Augengneis     |
|15202636 | Gotthard-Decke: Prävariszischer Paragneis | Gotthard-Decke: Prävariszischer Paragneis     |
|15202637 | Camosci-Decke: Paragneis | Camosci-Decke: Paragneis     |
|15202638 | Camosci-Decke: Lias-Dogger | Camosci-Decke: Lias-Dogger     |
|15202639 | Camosci-Decke: Lias-Dogger: Kalkglimmerschiefer | Camosci-Decke: Lias-Dogger: Kalkglimmerschiefer     |
|15202640 | Camosci-Decke: Lias-Dogger: Granatglimmerschiefer | Camosci-Decke: Lias-Dogger: Granatglimmerschiefer     |
|15202641 | Camosci-Decke: Lias | Camosci-Decke: Lias     |
|15202642 | Camosci-Decke: Trias | Camosci-Decke: Trias     |
|15202643 | Camosci-Decke: Sandige Trias | Camosci-Decke: Sandige Trias     |
|15200444 | Perte-du-Rhône-Fm.: Fulie-Mb.: Poet-Bk. | Banc du Poet     |
|15200445 | Rossemaison-Fm.: Courcelon-Süsswasserkalk | Calcaire d&#39;eau douce de Courcelon     |
|15200446 | Erzmatt-Krustenkalk | Calcaire concrétionné de la Erzmatt     |
|15200447 | Diegten-Süsswasserkalk | Calcaire d&#39;eau douce de Diegten     |
|15200448 | La-Verrerie-Süsswasserkalk | Calcaire d&#39;eau douce de la Verrerie     |
|15200449 | La-Charrue-Süsswasserkalk | Calcaire d&#39;eau douce de la Charrue     |
|15200450 | Vuache-Fm.: Astieria-Mergel | Marne à Astieria     |
|15200451 | Vuache-Fm.: Villers-Sch. | Couches de Villers     |
|15200452 | Pierre-Châtel-Fm.: Unité Moyenne Calcaire | Unité Moyenne Calcaire (UMC)     |
|15200453 | Pierre-Châtel-Fm.: Unité Inférieure Oolithique | Unité Inférieure Oolithique (UIO)     |
|15200456 | Etiollets-Fm.: Complexe récifal: Landaize-Kalk | Calcaire de Landaize     |
|15200457 | Balsthal-Fm.: Holzflue-Mb.: Balmberg-Oolith | Oolite du Balmberg     |
|15200458 | Balsthal-Fm.: Laufen-Mb.: Hautes-Roches-Algenkalk | Calcaire algaire des Hautes Roches     |
|15200459 | Balsthal-Fm.: Laufen-Mb.: Akzessorische Mumienbänke | Bancs accessoires à momies     |
|15200460 | Vellerat-Fm.: Röschenz-Mb.: Brauner Oolith | Brauner Oolith     |
|15200461 | Kaiseraugst-Fm.: Wellendolomit: Bleiglanz-Bk. | Bleiglanzbank (Fm. de Kaiseraugst)     |
|15200462 | Dinkelberg-Fm.: Rötton: Arenicolites-Bk. | Banc à Arenicolites     |
|15202364 | Kiental-Melange | Kiental-Melange     |
|15202365 | Termen-Zone: Tonschiefer | Termen-Zone: Tonschiefer     |
|15202366 | Termen-Zone: Kalkschiefer | Termen-Zone: Kalkschiefer     |
|15202367 | Nufenen-Zone: Knotenschiefer | Nufenen-Zone: Knotenschiefer     |
|15202368 | Nufenen-Zone: Sandstein | Nufenen-Zone: Sandstein     |
|15202369 | Nufenen-Zone: Granatschiefer | Nufenen-Zone: Granatschiefer     |
|15202370 | Stgir-Fm.: Unterer Teil | Stgir-Fm.: Unterer Teil     |
|15202371 | Stgir-Fm.: Oberer Teil | Stgir-Fm.: Oberer Teil     |
|15202372 | Inferno-Fm.: Oberer Teil: Runcaleida-Sch. | Inferno-Fm.: Oberer Teil: Runcaleida-Sch.     |
|15202373 | Inferno-Fm.: Unterer Teil: Riein-Sch. | Inferno-Fm.: Unterer Teil: Riein-Sch.     |
|15202374 | Meierhof-Phyllit | Meierhof-Phyllit     |
|15202375 | Waltensburg-Verrucano | Waltensburg-Verrucano     |
|15202376 | Ruinas Sandstein | Ruinas Sandstein     |
|15202377 | Niederhorn-Fm.: Hohgant-Sandstein: Berglikehle-Bk. | Niederhorn-Fm.: Hohgant-Sandstein: Berglikehle-Bk.     |
|15202378 | Rossplatten-Diorit | Rossplatten-Diorit     |
|15202379 | Schöllenen-Diorit | Schöllenen-Diorit     |
|15202380 | Amden-Fm.: Leist-Mergel: Grotzen-Austernbank | Amden-Fm.: Leist-Mergel: Grotzen-Austernbank     |
|15202381 | Tierwis-Fm.: Hurst-Mergel | Tierwis-Fm.: Hurst-Mergel     |
|15202382 | Helvetischer Kieselkalk: Palis-Bk. | Helvetischer Kieselkalk: Palis-Bk.     |
|15202644 | Camosci-Decke: Karbonatische Trias | Camosci-Decke: Karbonatische Trias     |
|15202645 | Urseren-Garvera-Zone | Urseren-Garvera-Zone     |
|15202646 | Urseren-Garvera-Zone: Trias | Urseren-Garvera-Zone: Trias     |
|15202647 | Nufenen-Zone: Trias | Nufenen-Zone: Trias     |
|15202648 | Nufenen-Zone: Lias | Nufenen-Zone: Lias     |
|15203001 | Niesen-Decke: Flysch | Flysch du Niesen     |
|15203002 | Chesselbach-Fm. | Formation du Chesselbach     |
|15203003 | Seron-Fm. | Formation de Seron     |
|15203004 | Niesenkulm-Fm. | Formation du Niesenkulm     |
|15203005 | Frutigen-Fm. | Formation de Frutigen     |
|15203006 | Grande-Eau-Fm. | Formation de la Grande Eau     |
|15203007 | Grande-Eau-Fm.: Langy-Mb. | Membre de Langy     |
|15203008 | Grande-Eau-Fm.: Forclaz-Mb. | Membre de la Forclaz     |
|15203009 | Grande-Eau-Fm.: Grès de Passage | Membre des Grès de Passage     |
|15203010 | Grande-Eau-Fm.: Leyderry-Mb. | Membre de la Leyderry     |
|15203011 | Grande-Eau-Fm.: Raverette-Mb. | Membre de la Raverette     |
|15203012 | Grande-Eau-Fm.: Schistes à miches | Membre des Schistes à Miches     |
|15203013 | Murgaz-Kalk | Calcaire de Murgaz     |
|15203014 | Niesen-Decke: Trias | Trias de la nappe du Niesen     |
|15203015 | Chlussli-Fm. | Formation de Chlussli     |
|15200463 | Dinkelberg-Fm.: Diagonalschichtiger Sandstein | Diagonalschichtiger Sandstein (Fm. du Dinkelberg)     |
|15200464 | Schinznach-Fm.: Leutschenberg-Mb. | Membre du Leutschenberg     |
|15200465 | Schlächtenhaus-Granit | Granite de Schlächtenhaus     |
|15200466 | Steinatal-Gneiskomplex | Complexe gneissique du Steinatal     |
|15200467 | Schinznach-Fm.: Asp-Mb.: Grenzdolomit | Grenzdolomit (Fm. de Schinznach)     |
|15200468 | Schinznach-Fm.: Asp-Mb.: Estherien-Sch. | Couches à Estheria (Fm. de Schinznach)     |
|15200469 | Hangende-Bankkalke-Fm. | Hangende-Bankkalke-Formation     |
|15200470 | Zementmergel-Fm. | Zementmergel-Formation     |
|15200471 | Liegende-Bankkalke-Fm. | Liegende-Bankkalke-Formation     |
|15200472 | Obere-Felsenkalke-Fm. | Obere-Felsenkalke-Formation     |
|15200473 | Untere-Felsenkalke-Fm. | Untere-Felsenkalke-Formation     |
|15200474 | Lacunosamergel-Fm. | Lacunosamergel-Formation     |
|15200475 | Oberjura-Massenkalk-Fm. | Oberjura-Massenkalk-Formation     |
|15200476 | Oberjura-Massenkalk-Fm.: Lochen-Sbf. | Lochen-Subformation     |
|15200477 | Wohlgeschichtete-Kalke-Fm. | Wohlgeschichtete-Kalke-Formation     |
|15200478 | Impressamergel-Fm. | Impressamergel-Formation     |
|15200479 | Ornatenton-Fm. | Ornatenton-Formation     |
|15200480 | Ornatenton-Fm.: Glaukonitsandmergel-Sbf. | Glaukonitsandmergel-Subformation     |
|15200481 | Ornatenton-Fm.: Glaukonitsandmergel-Sbf.: Grenzkalk | Grenzkalk     |
|15202099 | Quinten-Fm.: Mergelband | Mergelband (Fm. de Quinten)     |
|15202100 | Schilt-Fm. | Formation du Schilt     |
|15202101 | Schilt-Fm.: Mürtschen-Mb. | Membre de Mürtschen     |
|15202102 | Schilt-Fm.: Mergelstein-dominierte Fazies | Marne du Schilt     |
|15202103 | Schilt-Fm.: Kalkstein-dominierte Fazies | Calcaire du Schilt     |
|15202104 | Schilt-Fm.: Seeztal-Mb. | Membre du Seeztal     |
|15202105 | Schilt-Fm.: Windgällen-Mb. | Membre des Windgällen     |
|15202106 | Helvetikum: Dogger | Dogger de l&#39;Helvétique     |
|15202107 | Erzegg-Fm. | Formation de l&#39;Erzegg     |
|15202108 | Reischiben-Fm. | Formation de la Reischiben     |
|15202109 | Reischiben-Fm.: Blegi-Eisenoolith | Oolite ferrugineuse de la Blegi     |
|15202110 | Reischiben-Fm.: Bannalp-Konglomerat | Conglomérat de la Bannalp     |
|15202111 | Reischiben-Fm.: Guppen-Fossilhorizont | Horizon fossilifère de Guppen     |
|15202112 | Reischiben-Fm.: Gursbach-Fossilhorizont | Horizon fossilifère du Gursbach     |
|15202113 | Hochstollen-Fm. | Formation du Hochstollen     |
|15202114 | Hochstollen-Fm.: Schwarzhorn-Mb. | Membre du Schwarzhorn     |
|15202115 | Hochstollen-Fm.: Bietenhorn-Mb. | Membre du Bietenhorn     |
|15202116 | Bommerstein-Fm. | Formation du Bommerstein     |
|15202117 | Bommerstein-Fm.: Mols-Mb. | Membre de Mols     |
|15202383 | Öhrli-Fm.: Oberer-Öhrlikalk | Öhrli-Fm.: Oberer-Öhrlikalk     |
|15202384 | Öhrli-Fm.: Oberer-Öhrlimergel | Öhrli-Fm.: Oberer-Öhrlimergel     |
|15202385 | Öhrli-Fm.: Unterer-Öhrlikalk | Öhrli-Fm.: Unterer-Öhrlikalk     |
|15202386 | Spitzmeilen-Fm.: Oberer Teil | Spitzmeilen-Fm.: Oberer Teil     |
|15202387 | Spitzmeilen-Fm.: Unterer Teil | Spitzmeilen-Fm.: Unterer Teil     |
|15202388 | Spitzmeilen-Fm.: Basaler Teil | Spitzmeilen-Fm.: Basaler Teil     |
|15202389 | Prodkamm-Fm.: Oberer Teil | Prodkamm-Fm.: Oberer Teil     |
|15202390 | Prodkamm-Fm.: Mittlerer Teil | Prodkamm-Fm.: Mittlerer Teil     |
|15202391 | Prodkamm-Fm.: Unterer Teil | Prodkamm-Fm.: Unterer Teil     |
|15202392 | Sandpass-Fm. | Sandpass-Fm.     |
|15202393 | Sanetsch-Fm.: Diablerets-Mb.: Roc-Champion-Konglomerat | Sanetsch-Fm.: Diablerets-Mb.: Roc-Champion-Konglomerat     |
|15202394 | Stad-Fm.: Spirstock-Mb. | Membre du Spirstock     |
|15202395 | Seewen-Fm.: Roter-Seewer-Kalk | «Roter Seewenkalk»     |
|15202396 | Seewen-Fm.: Untere Götzis-Bk. | Banc de Götzis inférieur     |
|15202397 | Garschella-Fm.: Grünten-Mb.: Col-de-la-Plaine-Morte-Bk. | Banc du Col de la Plaine Morte     |
|15202398 | Betlis-Fm.: Oberer Teil | «Oberer Betliskalk»     |
|15202399 | Betlis-Fm.: Unterer Teil | «Unterer Betliskalk»     |
|15202400 | Bommerstein-Fm.: Vättis-Brekzie | Brèche fossilifère de Vättis     |
|15203016 | Coulaytes-Melange | Mélange des Coulaytes     |
|15203017 | Cuvigne-Derrey-Fm. | Formation de Cuvigne Derrey     |
|15203018 | Couches-Rouges | Groupe des Couches Rouges     |
|15203019 | Chenaux-Rouges-Fm. | Formation des Chenaux Rouges     |
|15203020 | Chenaux-Rouges-Fm.: Hochmatt-Kalkarenit | Calcarénite de la Hochmatt     |
|15203021 | Chenaux-Rouges-Fm.: Chenaux-Rouges-Mineralkruste | Croûte minéralisée des Chenaux Rouges     |
|15203022 | Forclettes-Fm. | Formation des Forclettes     |
|15203023 | Forclettes-Fm.: Roter-Sattel-Hartgrund | Hartground de Roter Sattel     |
|15203024 | Forclettes-Fm.: Beaumont-Konglomerat | Conglomérat de Beaumont     |
|15203025 | Forclettes-Fm.: Rayes-Kalk | Calcaire des Rayes     |
|15203026 | Forclettes-Fm.: Pissot-Mb. | Membre du Pissot     |
|15203027 | Rote-Platte-Fm. | Formation de Rote Platte     |
|15203028 | Rote-Platte-Fm.: Wildenbach-Mb. | Membre du Wildenbach     |
|15203029 | Rote-Platte-Fm.: Pra-du-Pont-Hartgrund | Hardground de Pra du Pont     |
|15203030 | Rote-Platte-Fm.: Rontins-Mb. | Membre des Rontins     |
|15203031 | Rote-Platte-Fm.: Allières-Mb. | Membre d&#39;Allières     |
|15203032 | Rote-Platte-Fm.: Gérignoz-Kalk | Calcaire de Gérignoz     |
|15203033 | Rote-Platte-Fm.: Plagersflue-Kalkarenit | Calcarénite de la Plagersflue     |
|15203034 | Intyamon-Fm. | Formation de l&#39;Intyamon     |
|15200482 | Ornatenton-Fm.: Macrocephalenoolith-Sbf. | Macrocephalenoolith-Subformation     |
|15200483 | Wutach-Fm. | Wutach-Formation     |
|15200484 | Variansmergel-Fm. | Variansmergel-Formation     |
|15200485 | Dentalienton-Fm. | Dentalienton-Formation     |
|15200486 | Hamitenton-Fm. | Hamitenton-Formation     |
|15200487 | Hamitenton-Fm.: Parkinsonioolith-Sbf. | Parkinsonioolith-Subformation     |
|15200488 | Gosheim-Fm. | Gosheim-Formation     |
|15200489 | Gosheim-Fm.: Blagdeni-Sbf. | Blagdeni-Subformation     |
|15200490 | Gosheim-Fm.: Humphriesioolith-Sbf. | Humphriesioolith-Subformation     |
|15200491 | Wedelsandstein-Fm. | Wedelsandstein-Formation     |
|15200492 | Wedelsandstein-Fm.: Blaukalk-Sbf. | Blaukalk-Subformation     |
|15200493 | Murchisonaeoolith-Fm. | Murchisonaeoolith-Formation     |
|15200494 | Achdorf-Fm. | Achdorf-Formation     |
|15200495 | Tannenwald-Sch. | Couches du Tannenwald     |
|15200496 | Schüpferegg-Nagelfluh: Gabelspitz-Sch. | Couches de la Gabelspitz     |
|15200497 | Schüpferegg-Nagelfluh: Schallenberg-Mergel | Marne du Schallenberg     |
|15200498 | Schüpferegg-Nagelfluh: Seli-Nagelfluh | Poudingue de Seli     |
|15200499 | Brand-Herrentisch-Tuffit | Tuffite du Brand-Herrentisch     |
|15200500 | Wangen-Tuffit | Tuffite de Wangen     |
|15200501 | Hohenolber-Tuffit | Tuffite du Hohenolber     |
|15200502 | Eichbol-Tuffit | Tuffite d&#39;Eichbol     |
|15202118 | Dugny-Fm. | Formation de Dugny     |
|15202119 | Coroi-Fm. | Formation du Coroi     |
|15202120 | Helvetikum: Lias | Lias de l&#39;Helvétique     |
|15202121 | Brunnistock-Fm. | Formation du Brunnistock     |
|15202122 | Inferno-Fm. | Formation d&#39;Inferno     |
|15202123 | Monts-Rosset-Fm. | Formation des Monts Rosset     |
|15202124 | Torrenthorn-Fm.: Torrentalp-Mb. | Membre de la Torrentalp     |
|15202125 | Sexmor-Fm. | Formation du Sexmor     |
|15202126 | Mont-Joly-Fm. | Formation du Mont Joly     |
|15202127 | Torrenthorn-Fm.: Galm-Mb. | Membre de Galm     |
|15202128 | Spitzmeilen-Fm. | Formation du Spitzmeilen     |
|15202129 | Tierces-Fm. | Formation des Tierces     |
|15202130 | Bachalp-Fm. | Formation de la Bachalp     |
|15202131 | Prodkamm-Fm. | Formation du Prodkamm     |
|15202132 | Prodkamm-Fm.: Cardinien-Mb. | Membre à Cardinia     |
|15202133 | Stgir-Fm. | Formation du Stgir     |
|15202134 | Helvetikum: Trias | Trias de l&#39;Helvétique     |
|15202135 | Besoëns-Fm. | Formation des Besoëns     |
|15202136 | Quarten-Fm. | Formation de Quarten     |
|15202137 | Arandellys-Fm. | Formation des Arandellys     |
|15202138 | Arandellys-Fm.: Griaz-Mb. | Membre de la Griaz     |
|15202139 | Röti-Fm. | Formation de la Röti     |
|15202401 | Inferno-Fm.: Oberer Teil | Formation d&#39;Inferno, partie supérieure     |
|15202402 | Inferno-Fm.: Mittlerer Teil | Formation d&#39;Inferno, partie moyenne     |
|15202403 | Inferno-Fm.: Unterer Teil | Formation d&#39;Inferno, partie inférieure     |
|15202404 | Sexmor-Fm.: Oberer Teil | Formation du Sexmor, partie supérieure     |
|15202405 | Sexmor-Fm.: Unterer Teil | Formation du Sexmor, partie inférieure     |
|15202406 | Prodkamm-Fm.: Unterer Teil: Leitoolith | «Leitoolith»     |
|15202411 | Stad-Fm.: Lochegg-Brekzie | Brèche de la Lochegg     |
|15202412 | Zementstein-Fm.: Oberer Teil | «Obere Zementsteinschichten»     |
|15202413 | Zementstein-Fm.: Unterer Teil | «Untere Zementsteinschichten»     |
|15202414 | Bommerstein-Fm.: Glockhaus-Mb.: Roter Echinodermenkalk | «Rote Echinodermenbrekzie»     |
|15202415 | Bommerstein-Fm.: Glockhaus-Mb.: Obere Tonschiefer | «Obere Tonschiefer» (Fm. du Bommerstein)     |
|15202416 | Bommerstein-Fm.: Glockhaus-Mb. | Membre du Glockhaus     |
|15202417 | Coroi-Fm.: Basaler Quarzit | «Quartzite de base» (Fm. du Coroi)     |
|15202418 | Röti-Fm.: Rauwacke | Cornieule (Fm. de la Röti)     |
|15202419 | Vieux-Emosson-Fm.: Col-du-Jorat-Mb. | Membre du Col du Jorat     |
|15202420 | Quarten-Fm.: Equisetenschiefer | «Equisetenschiefer»     |
|15202421 | Amden-Fm.: Leist-Mergel | Marne du Leist     |
|15202422 | Amden Fm.: Leiboden-Mergel | Marne du Leiboden     |
|15203035 | Intyamon-Fm.: Chällihorn-Mb. | Membre du Chällihorn     |
|15203036 | Intyamon-Fm.: Comba-d&#39;Avau-Mb. | Membre de la Comba d&#39;Avau     |
|15203037 | Intyamon-Fm.: Rodosex-Mb. | Membre de Rodosex     |
|15203038 | Sciernes-d&#39;Albeuve-Fm. | Formation des Sciernes d&#39;Albeuve     |
|15203039 | Moléson-Fm. | Formation du Moléson     |
|15203040 | Torrent-de-Lessoc-Fm. | Formation du Torrent de Lessoc     |
|15203041 | Staldengraben-Fm. | Formation du Staldengraben     |
|15203042 | Staldengraben-Fm.: Col-de-Lys-Mb. | Membre du Col de Lys     |
|15203043 | Staldengraben-Fm.: Vanil-Carré-Mb. | Membre du Vanil Carré     |
|15203044 | Staldengraben-Fm.: Verdy-Mb. | Membre du Verdy     |
|15203045 | Staldengraben-Fm.: Soladier-Mb. | Membre de Soladier     |
|15203046 | Sommant-Fm. | Formation de Sommant     |
|15203047 | Rossinière-Fm. | Formation de Rossinière     |
|15203048 | Heiti-Fm. | Formation de Heiti     |
|15203049 | Combe-du-Pissot-Fm. | Formation de la Combe du Pissot     |
|15203050 | Combe-du-Pissot-Fm.: Chevalets-Mb. | Membre des Chevalets     |
|15203051 | Combe-du-Pissot-Fm.: Creux-de-l&#39;Ours-Mb. | Membre du Creux-de-l&#39;Ours     |
|15203052 | Petit-Liençon-Fm. | Formation du Petit Liençon     |
|15203053 | Arvel-Fm. | Formation d&#39;Arvel     |
|15203054 | Grande-Bonavau-Fm. | Formation de la Grande Bonavau     |









## Annexe  GC_CORRELATION_CD {#gc-correlation-cd}
Correlation

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15283007 | Bregaglia-Intrusion | Bregaglia-Intrusion     |
|15285015 | USM-II | USM-II     |
|15285043 | Lias-Dogger in neritischer Fazies | Lias-Dogger in neritischer Fazies     |
|15285001 | Sedimentbedeckung | Sedimentbedeckung     |
|15285032 | Scaglia | Scaglia     |
|15285009 | USM-III bis OSM-I | USM-III bis OSM-I     |
|15285027 | «Nummulitikum» | «Nummulitikum»     |
|15285045 | Prä-Rift | Prä-Rift     |
|15287001 | Grundgebirge | Grundgebirge     |
|15287003 | Spät- bis postvariszisches Grundgebirge | Spät- bis postvariszisches Grundgebirge     |
|15285019 | UMM-III | UMM-III     |
|15285035 | Post-Rift Mesozoikum in detritischer Fazies | Post-Rift Mesozoikum in detritischer Fazies     |
|15285006 | OSM-II | OSM-II     |
|15285012 | OMM-I | OMM-I     |
|15285038 | «Urgonien» | «Urgonien»     |
|15285044 | Lias-Dogger in detritischer Fazies | Lias-Dogger in detritischer Fazies     |
|15287005 | Spätvariszisches Grundgebirge | Spätvariszisches Grundgebirge     |
|15283003 | Hegau-Vulkanismus | Hegau-Vulkanismus     |
|15285004 | Molasse | Molasse     |
|15285021 | UMM-I | UMM-I     |
|15285029 | Post-Rift | Post-Rift     |
|15283001 | Alpines Magmatismus | Alpines Magmatismus     |
|15285034 | Radiolarit | Radiolarit     |
|15285048 | Keuper | Keuper     |
|15285002 | Post-Kollision | Post-Kollision     |
|15285047 | «Rhät» | «Rhät»     |
|15285003 | Lombardischer Gompholit | Lombardischer Gompholit     |
|15285013 | USM | USM     |
|15285037 | Post-Rift Mesozoikum in Plattform-Fazies | Post-Rift Mesozoikum in Plattform-Fazies     |
|15285049 | Karbonatische Trias | Karbonatische Trias     |
|15285022 | Post-Kollision in pelagischer Fazies | Post-Kollision in pelagischer Fazies     |
|15287006 | Mittelvariszisches Grundgebirge | Mittelvariszisches Grundgebirge     |
|15285031 | Couches Rouges | Couches Rouges     |
|15285026 | Prä-Kollision | Prä-Kollision     |
|15285041 | Ophiolithische Abfolge | Ophiolithische Abfolge     |
|15287009 | Prävariszisches Grundgebirge | Prävariszisches Grundgebirge     |
|15285030 | Post-Rift Mesozoikum in pelagischer Fazies | Post-Rift Mesozoikum in pelagischer Fazies     |
|15285050 | Muschelkalk | Muschelkalk     |
|15285054 | Buntsandstein | Buntsandstein     |
|15287004 | Postvariszisches Grundgebirge | Postvariszisches Grundgebirge     |
|15281001 | Post-Messinien | Post-Messinien     |
|15285010 | OMM | OMM     |
|15285042 | Lias-Dogger in pelagischer Fazies | Lias-Dogger in pelagischer Fazies     |
|15285051 | Hauptdolomit | Hauptdolomit     |
|15285018 | UMM | UMM     |
|15283005 | Alpine Intrusion | Alpine Intrusion     |
|15283006 | Novate-Intrusion | Novate-Intrusion     |
|15285039 | Malm | Malm     |
|15287008 | Frühvariszisches Grundgebirge | Frühvariszisches Grundgebirge     |
|15285007 | Appenzellergranit-Leitniveau | Appenzellergranit-Leitniveau     |
|15285011 | OMM-II | OMM-II     |
|15285014 | USM-III | USM-III     |
|15285036 | «Gault» | «Gault»     |
|15283002 | Alpines Vulkanismus | Alpines Vulkanismus     |
|15285020 | UMM-II | UMM-II     |
|15285028 | Siderolithikum | Siderolithikum     |
|15285023 | Syn-Kollision | Syn-Kollision     |
|15287007 | Prä- bis frühvariszisches Grundgebirge | Prä- bis frühvariszisches Grundgebirge     |
|15285024 | Mélange | Mélange     |
|15285046 | Pelitische Trias | Pelitische Trias     |
|15283004 | Periadriatisches Vulkanismus | Periadriatisches Vulkanismus     |
|15285016 | USM-I | USM-I     |
|15285017 | Basisbildungen der USM | Basisbildungen der USM     |
|15283008 | Adamello-Intrusion | Adamello-Intrusion     |
|15285052 | Raibl | Raibl     |
|15285025 | Flysch | Flysch     |
|15287002 | Variszisches Grundgebirge | Variszisches Grundgebirge     |
|15285005 | OSM | OSM     |
|15285008 | OSM-I | OSM-I     |
|15285033 | Maiolica / Aptychenkalk | Maiolica / Aptychenkalk     |
|15285040 | Syn-Rift | Syn-Rift     |
|15285053 | Detritische Trias | Detritische Trias     |









## Annexe  GC_LITSTRAT_FORMATION_BANK_CD {#gc-litstrat-formation-bank-cd}
blabla

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15251231 | Numismalismergel-Formation | Numismalismergel-Formation     |
|15251232 | Obtususton-Formation | Obtususton-Formation     |
|15251233 | Arietenkalk-Formation | Arietenkalk-Formation     |
|15251234 | Angulatenton-Formation | Angulatenton-Formation     |
|15251235 | Psilonotenton-Formation | Psilonotenton-Formation     |
|15251236 | Klettgau-Formation | Klettgau-Formation     |
|15251237 | Belchen-Member | Belchen-Member     |
|15251238 | Seebi-Member | Seebi-Member     |
|15251239 | Gruhalde-Member | Gruhalde-Member     |
|15251240 | Berlingen-Member | Berlingen-Member     |
|15251241 | Gansingen-Member | Gansingen-Member     |
|15251242 | Ergolz-Member | Ergolz-Member     |
|15251243 | Bänkerjoch-Formation | Bänkerjoch-Formation     |
|15251244 | Schinznach-Formation | Schinznach-Formation     |
|15251245 | Asp-Member | Asp-Member     |
|15251246 | «Grenzdolomit» (Schinznach-Fm.) | «Grenzdolomit» (Schinznach-Fm.)     |
|15251247 | «Estherien-Schichten» | «Estherien-Schichten»     |
|15251248 | Stamberg-Member | Stamberg-Member     |
|15251249 | Kaisten-Bank | Kaisten-Bank     |
|15251250 | Eptingen-Bank | Eptingen-Bank     |
|15251251 | Liedertswil-Member | Liedertswil-Member     |
|15251252 | Dünnlenberg-Bank | Dünnlenberg-Bank     |
|15251253 | Kienberg-Member | Kienberg-Member     |
|15251254 | Saalhof-Bank | Saalhof-Bank     |
|15251255 | Leutschenberg-Member | Leutschenberg-Member     |
|15251256 | Fützen-Bank | Fützen-Bank     |
|15251257 | Zeglingen-Formation | Zeglingen-Formation     |
|15251258 | «Dolomitzone» (Zeglingen-Fm.) | «Dolomitzone» (Zeglingen-Fm.)     |
|15251259 | «Obere Sufatzone» (Zeglingen-Fm.) | «Obere Sufatzone» (Zeglingen-Fm.)     |
|15251260 | «Salzlager» (Zeglingen-Fm.) | «Salzlager» (Zeglingen-Fm.)     |
|15251261 | «Untere Sulfatzone» (Zeglingen-Fm.) | «Untere Sulfatzone» (Zeglingen-Fm.)     |
|15251262 | Kaiseraugst-Formation | Kaiseraugst-Formation     |
|15251263 | «Orbicularis-Mergel» | «Orbicularis-Mergel»     |
|15251264 | «Wellenkalk / Wellenmergel» | «Wellenkalk / Wellenmergel»     |
|15251265 | «Wellendolomit» | «Wellendolomit»     |
|15251266 | «Bleiglanzbank» (Kaiseraugst-Fm.) | «Bleiglanzbank» (Kaiseraugst-Fm.)     |
|15251267 | Dinkelberg-Formation | Dinkelberg-Formation     |
|15251268 | «Rhötton» | «Rhötton»     |
|15251269 | «Arenicolites-Bank» | «Arenicolites-Bank»     |
|15251270 | «Plattensandstein» (Dinkelberg-Fm.) | «Plattensandstein» (Dinkelberg-Fm.)     |
|15251271 | «Karneol-Horizont» (Dinkelberg-Fm.) | «Karneol-Horizont» (Dinkelberg-Fm.)     |
|15251272 | «Diagonalschichtiger Sandstein» (Dinkelberg-Fm.) | «Diagonalschichtiger Sandstein» (Dinkelberg-Fm.)     |
|15251273 | Vogesen-Sandstein | Vogesen-Sandstein     |
|15251274 | Wiesental-Formation | Wiesental-Formation     |
|15251275 | Weitenau-Formation | Weitenau-Formation     |
|15251276 | «Oberer Schuttfächer» (Weitenau-Fm.) | «Oberer Schuttfächer» (Weitenau-Fm.)     |
|15251277 | «Playa-Serie» (Weitenau-Fm.) | «Playa-Serie» (Weitenau-Fm.)     |
|15251278 | «Unterer Schuttfächer» (Weitenau-Fm.) | «Unterer Schuttfächer» (Weitenau-Fm.)     |
|15251279 | Weiach-Formation | Weiach-Formation     |
|15251280 | «Jüngere Flussablagerungen» (Weiach-Fm.) | «Jüngere Flussablagerungen» (Weiach-Fm.)     |
|15251281 | «Seeablagerungen» (Weiach-Fm.) | «Seeablagerungen» (Weiach-Fm.)     |
|15251282 | «Ältere Flussablagerungen» (Weiach-Fm.) | «Ältere Flussablagerungen» (Weiach-Fm.)     |
|15251283 | «Kohle-Serie» (Weiach-Fm.) | «Kohle-Serie» (Weiach-Fm.)     |
|15251284 | Schwaningen-Merenbach-Rhyolith | Schwaningen-Merenbach-Rhyolith     |
|15251285 | Schwaningen-Weizen-Granit | Schwaningen-Weizen-Granit     |
|15251001 | Rossemaison-Formation | Rossemaison-Formation     |
|15251002 | Courcelon-Süsswasserkalk | Courcelon-Süsswasserkalk     |
|15251003 | Erzmatt-Krustenkalk | Erzmatt-Krustenkalk     |
|15251004 | Oberdorf-Süsswasserkalk | Oberdorf-Süsswasserkalk     |
|15251005 | Diegten-Süsswasserkalk | Diegten-Süsswasserkalk     |
|15251006 | La-Charrue-Süsswasserkalk | La-Charrue-Süsswasserkalk     |
|15251007 | Champ-Vuillerat-Süsswasserkalk | Champ-Vuillerat-Süsswasserkalk     |
|15251008 | La-Verrerie-Süsswasserkalk | La-Verrerie-Süsswasserkalk     |
|15251009 | «Daubrée-Konglomerat» | «Daubrée-Konglomerat»     |
|15251010 | Narlay-Formation | Narlay-Formation     |
|15251011 | Perte-du-Rhône-Formation | Perte-du-Rhône-Formation     |
|15251012 | Poncin-Member | Poncin-Member     |
|15251013 | Mussel-Member | Mussel-Member     |
|15251014 | Vraconne-Sandstein | Vraconne-Sandstein     |
|15251015 | La-Presta-Mergel | La-Presta-Mergel     |
|15251016 | Vernettes-Sandstein | Vernettes-Sandstein     |
|15251017 | Ponthoud-Bank | Ponthoud-Bank     |
|15251018 | Scie-Besse-Sandstein | Scie-Besse-Sandstein     |
|15251019 | Fulie-Member | Fulie-Member     |
|15251020 | Mortier-Mergel | Mortier-Mergel     |
|15251021 | Vauglène-Bänke | Vauglène-Bänke     |
|15251022 | Poet-Bank | Poet-Bank     |
|15251023 | Rocher-des-Hirondelles-Formation | Rocher-des-Hirondelles-Formation     |
|15251024 | Vallorbe-Member | Vallorbe-Member     |
|15251025 | Bellegarde-Bänke | Bellegarde-Bänke     |
|15251026 | Serrières-Bank | Serrières-Bank     |
|15251027 | La-Rivière-Member | La-Rivière-Member     |
|15251028 | Fort-de-l&#39;Écluse-Member | Fort-de-l&#39;Écluse-Member     |
|15251029 | Gorges-de-l&#39;Orbe-Formation | Gorges-de-l&#39;Orbe-Formation     |
|15251030 | Morteau-Kalk | Morteau-Kalk     |
|15251031 | Bôle-Member | Bôle-Member     |
|15251032 | Montcherand-Member | Montcherand-Member     |
|15251033 | La-Vaux-Bänke | La-Vaux-Bänke     |
|15251034 | Cul-du-Nozon-Bänke | Cul-du-Nozon-Bänke     |
|15251035 | Pont-des-Pierres-Bänke | Pont-des-Pierres-Bänke     |
|15251036 | Grand-Essert-Formation | Grand-Essert-Formation     |
|15251037 | Neuchâtel-Member | Neuchâtel-Member     |
|15251038 | «Pierre Jaune Supérieure» | «Pierre Jaune Supérieure»     |
|15251039 | Les-Uttins-Mergel | Les-Uttins-Mergel     |
|15251040 | «Pierre Jaune Inférieure» | «Pierre Jaune Inférieure»     |
|15251041 | Hauterive-Member | Hauterive-Member     |
|15251042 | L&#39;Ecluse-Mergelkalk | L&#39;Ecluse-Mergelkalk     |
|15251043 | Censeau-Mergel | Censeau-Mergel     |
|15251044 | Morteau-Mergel | Morteau-Mergel     |
|15251045 | Vuache-Formation | Vuache-Formation     |
|15251046 | «Bryozoen-Mergel» | «Bryozoen-Mergel»     |
|15251047 | «Astieria-Mergel» | «Astieria-Mergel»     |
|15251048 | Villers-Schichten | Villers-Schichten     |
|15251049 | «Alectryonia-Kalk» | «Alectryonia-Kalk»     |
|15251050 | Arzier-Mergel | Arzier-Mergel     |
|15251051 | Chambotte-Formation | Chambotte-Formation     |
|15251052 | Guiers-Member | Guiers-Member     |
|15251053 | Grande-Varappe-Bank | Grande-Varappe-Bank     |
|15251054 | Vions-Formation | Vions-Formation     |
|15251055 | Pierre-Châtel-Formation | Pierre-Châtel-Formation     |
|15251056 | «Unité Moyenne Calcaire» | «Unité Moyenne Calcaire»     |
|15251057 | «Unité Inférieure Oolithique» | «Unité Inférieure Oolithique»     |
|15251058 | Goldberg-Formation | Goldberg-Formation     |
|15251059 | Twannbach-Formation | Twannbach-Formation     |
|15251060 | Vouglans-Member | Vouglans-Member     |
|15251061 | Chailley-Member | Chailley-Member     |
|15251062 | «Oberer Virgula-Mergel» | «Oberer Virgula-Mergel»     |
|15251063 | Reuchenette-Formation | Reuchenette-Formation     |
|15251064 | Chevenez-Member | Chevenez-Member     |
|15251065 | «Grenznerineen-Bank» | «Grenznerineen-Bank»     |
|15251066 | «Cladocoropsis-Kalk» | «Cladocoropsis-Kalk»     |
|15251067 | «Unterer Virgula-Mergel» | «Unterer Virgula-Mergel»     |
|15251068 | Courtedoux-Member | Courtedoux-Member     |
|15251069 | Banné-Member | Banné-Member     |
|15251070 | Vabenau-Member | Vabenau-Member     |
|15251071 | Creugenat-Schichten | Creugenat-Schichten     |
|15251072 | Etiollets-Formation | Etiollets-Formation     |
|15251073 | «Complexe récifal» | «Complexe récifal»     |
|15251074 | Landaize-Kalk | Landaize-Kalk     |
|15251075 | Tabalcon-Kalk | Tabalcon-Kalk     |
|15251076 | Couvaloup-Member | Couvaloup-Member     |
|15251077 | Le-Coin-Formation | Le-Coin-Formation     |
|15251078 | Hangende-Bankkalke-Formation | Hangende-Bankkalke-Formation     |
|15251079 | Hohentengen-Formation | Hohentengen-Formation     |
|15251080 | Zementmergel-Formation | Zementmergel-Formation     |
|15251081 | Liegende-Bankkalke-Formation | Liegende-Bankkalke-Formation     |
|15251082 | Obere-Felsenkalke-Formation | Obere-Felsenkalke-Formation     |
|15251083 | Untere-Felsenkalke-Formation | Untere-Felsenkalke-Formation     |
|15251084 | Lacunosamergel-Formation | Lacunosamergel-Formation     |
|15251085 | Weilergraben-Formation | Weilergraben-Formation     |
|15251086 | Gugenmühle-Member | Gugenmühle-Member     |
|15251087 | Schwarzbach-Formation | Schwarzbach-Formation     |
|15251088 | Burghorn-Formation | Burghorn-Formation     |
|15251089 | Wettingen-Member | Wettingen-Member     |
|15251090 | Baden-Member | Baden-Member     |
|15251091 | Oberjura-Massenkalk-Formation | Oberjura-Massenkalk-Formation     |
|15251092 | Lochen-Subformation | Lochen-Subformation     |
|15251093 | Courgenay-Formation | Courgenay-Formation     |
|15251094 | Porrentruy-Member | Porrentruy-Member     |
|15251095 | La-May-Member | La-May-Member     |
|15251096 | Balsthal-Formation | Balsthal-Formation     |
|15251097 | Verena-Member | Verena-Member     |
|15251098 | Holzflue-Member | Holzflue-Member     |
|15251099 | Balmberg-Oolith | Balmberg-Oolith     |
|15251100 | Laufen-Member | Laufen-Member     |
|15251101 | Hautes-Roches-Algenkalk | Hautes-Roches-Algenkalk     |
|15251102 | Akzessorische Mumienbänke | Akzessorische Mumienbänke     |
|15251103 | Olten-Member | Olten-Member     |
|15251104 | Steinibach-Member | Steinibach-Member     |
|15251105 | Wohlgeschichtete-Kalke-Formation | Wohlgeschichtete-Kalke-Formation     |
|15251106 | Villigen-Formation | Villigen-Formation     |
|15251107 | Wangental-Member | Wangental-Member     |
|15251108 | Letzi-Member | Letzi-Member     |
|15251109 | «Knollen-Bank» | «Knollen-Bank»     |
|15251110 | Küssaburg-Member | Küssaburg-Member     |
|15251111 | Wangen-Member | Wangen-Member     |
|15251112 | Hornbuck-Member | Hornbuck-Member     |
|15251113 | «Crenularis-Member» | «Crenularis-Member»     |
|15251114 | Geissberg-Member | Geissberg-Member     |
|15251116 | Vellerat-Formation | Vellerat-Formation     |
|15251117 | Bure-Member | Bure-Member     |
|15251118 | «Oolithe-Rousse-Member» | «Oolithe-Rousse-Member»     |
|15251119 | «Hauptmumienbank-Member» | «Hauptmumienbank-Member»     |
|15251120 | Röschenz-Member | Röschenz-Member     |
|15251121 | «Brauner Oolith» | «Brauner Oolith»     |
|15251122 | «Grüne Mumienbank» | «Grüne Mumienbank»     |
|15251123 | Vorbourg-Member | Vorbourg-Member     |
|15251124 | Günsberg-Formation | Günsberg-Formation     |
|15251125 | Moutier-Korallenkalk | Moutier-Korallenkalk     |
|15251126 | St-Ursanne-Formation | St-Ursanne-Formation     |
|15251127 | Tiergarten-Member | Tiergarten-Member     |
|15251128 | Buix-Member | Buix-Member     |
|15251129 | Chestel-Member | Chestel-Member     |
|15251130 | Caquerelle-Pisolith | Caquerelle-Pisolith     |
|15251131 | Grellingen-Member | Grellingen-Member     |
|15251132 | Pichoux-Formation | Pichoux-Formation     |
|15251133 | Impressamergel-Formation | Impressamergel-Formation     |
|15251134 | Wildegg-Formation | Wildegg-Formation     |
|15251135 | Effingen-Member | Effingen-Member     |
|15251136 | Gerstenhübel-Bank | Gerstenhübel-Bank     |
|15251137 | «Pecten-Bank» | «Pecten-Bank»     |
|15251138 | Birmenstorf-Member | Birmenstorf-Member     |
|15251139 | Bärschwil-Formation | Bärschwil-Formation     |
|15251140 | Liesberg-Member | Liesberg-Member     |
|15251141 | Sornetan-Member | Sornetan-Member     |
|15251142 | «Renggeri-Member» | «Renggeri-Member»     |
|15251143 | Ornatenton-Formation | Ornatenton-Formation     |
|15251144 | Glaukonitsandmergel-Subformation | Glaukonitsandmergel-Subformation     |
|15251145 | Grenzkalk | Grenzkalk     |
|15251115 | Ancepsoolith-Subformation | Ancepsoolith-Subformation     |
|15251146 | Macrocephalenoolith-Subformation | Macrocephalenoolith-Subformation     |
|15251147 | Wutach-Formation | Wutach-Formation     |
|15251148 | Ifenthal-Formation | Ifenthal-Formation     |
|15251149 | Graitery-Member | Graitery-Member     |
|15251150 | Herznach-Member | Herznach-Member     |
|15251151 | Schellenbrücke-Bank | Schellenbrücke-Bank     |
|15251152 | Bollement-Member | Bollement-Member     |
|15251153 | Ängistein-Member | Ängistein-Member     |
|15251154 | Unter-Erli-Bank | Unter-Erli-Bank     |
|15251155 | Bözen-Member | Bözen-Member     |
|15251156 | Saulcy-Member | Saulcy-Member     |
|15251157 | Châtillon-Member | Châtillon-Member     |
|15251158 | St-Brais-Member | St-Brais-Member     |
|15251159 | Schelmenloch-Member | Schelmenloch-Member     |
|15251160 | Anwil-Bank | Anwil-Bank     |
|15251161 | Variansmergel-Formation | Variansmergel-Formation     |
|15251162 | Hauptrogenstein | Hauptrogenstein     |
|15251163 | «Spatkalk» (Hauptrogenstein) | «Spatkalk» (Hauptrogenstein)     |
|15251164 | «Ferrugineus-Oolith» | «Ferrugineus-Oolith»     |
|15251165 | «Pierre Blanche» (Hauptrogenstein) | «Pierre Blanche» (Hauptrogenstein)     |
|15251166 | Movelier-Schichten | Movelier-Schichten     |
|15251167 | «Grande Oolithe» (Hauptrogenstein) | «Grande Oolithe» (Hauptrogenstein)     |
|15251168 | Wittnau-Korallenkalk | Wittnau-Korallenkalk     |
|15251169 | Furcil-Mergel | Furcil-Mergel     |
|15251170 | «Calcaire roux marneux» (Hauptrogenstein) | «Calcaire roux marneux» (Hauptrogenstein)     |
|15251171 | «Homomya-Mergel» | «Homomya-Mergel»     |
|15251172 | «Obere Acuminata-Schichten» | «Obere Acuminata-Schichten»     |
|15251173 | «Oolithe Subcompacte» (Hauptrogenstein) | «Oolithe Subcompacte» (Hauptrogenstein)     |
|15251174 | «Maeandrina-Schichten» | «Maeandrina-Schichten»     |
|15251175 | «Untere Acuminata-Schichten» | «Untere Acuminata-Schichten»     |
|15251176 | Gisliflue-Korallenkalk | Gisliflue-Korallenkalk     |
|15251177 | Klingnau-Formation | Klingnau-Formation     |
|15251178 | «Knorri-Ton» | «Knorri-Ton»     |
|15251179 | «Wuerttembergica-Schichten» | «Wuerttembergica-Schichten»     |
|15251180 | «Parkinsoni-Schichten» (Klingnau-Fm.) | «Parkinsoni-Schichten» (Klingnau-Fm.)     |
|15251181 | «Subfurcatum-Bank» | «Subfurcatum-Bank»     |
|15251182 | «Blagdeni-Schichten» (Klingnau-Fm.) | «Blagdeni-Schichten» (Klingnau-Fm.)     |
|15251183 | Dentalienton-Formation | Dentalienton-Formation     |
|15251184 | Hamitenton-Formation | Hamitenton-Formation     |
|15251185 | Parkinsonioolith-Subformation | Parkinsonioolith-Subformation     |
|15251186 | Gosheim-Formation | Gosheim-Formation     |
|15251187 | Blagdeni-Subformation | Blagdeni-Subformation     |
|15251188 | Humphriesioolith-Subformation | Humphriesioolith-Subformation     |
|15251189 | «Calcaire à Entroques» | «Calcaire à Entroques»     |
|15251190 | Passwang-Formation | Passwang-Formation     |
|15251191 | Grenchenberg-Member | Grenchenberg-Member     |
|15251192 | Rothenfluh-Member | Rothenfluh-Member     |
|15251193 | Brüggli-Member | Brüggli-Member     |
|15251194 | «Humphriesi-Schichten» (Brüggli-Mb.) | «Humphriesi-Schichten» (Brüggli-Mb.)     |
|15251195 | Waldenburg-Member | Waldenburg-Member     |
|15251196 | Hirnichopf-Member | Hirnichopf-Member     |
|15251197 | Hauenstein-Member | Hauenstein-Member     |
|15251198 | Sissach-Member | Sissach-Member     |
|15251199 | «Comptum-Bank» (Passwang-Fm.) | «Comptum-Bank» (Passwang-Fm.)     |
|15251200 | «Couches à Pecten dewalquei» | «Couches à Pecten dewalquei»     |
|15251201 | Brot-Schichten | Brot-Schichten     |
|15251202 | Wedelsandstein-Formation | Wedelsandstein-Formation     |
|15251203 | Blaukalk-Subformation | Blaukalk-Subformation     |
|15251204 | Murchisonaeoolith-Formation | Murchisonaeoolith-Formation     |
|15251205 | Achdorf-Formation | Achdorf-Formation     |
|15251206 | Opalinus-Ton | Opalinus-Ton     |
|15251207 | Staffelegg-Formation | Staffelegg-Formation     |
|15251208 | Gross-Wolf-Member | Gross-Wolf-Member     |
|15251209 | Eriwis-Bank | Eriwis-Bank     |
|15251210 | Erlimoos-Bank | Erlimoos-Bank     |
|15251211 | Gipf-Bank | Gipf-Bank     |
|15251212 | Rietheim-Member | Rietheim-Member     |
|15251213 | «Unterer Stein» (Staffelegg-Fm.) | «Unterer Stein» (Staffelegg-Fm.)     |
|15251214 | Rickenbach-Member | Rickenbach-Member     |
|15251215 | Müsenegg-Bank | Müsenegg-Bank     |
|15251216 | Breitenmatt-Member | Breitenmatt-Member     |
|15251217 | Trasadingen-Bank | Trasadingen-Bank     |
|15251218 | Grünschholz-Member | Grünschholz-Member     |
|15251219 | Frick-Member | Frick-Member     |
|15251220 | Mont-Terri-Member | Mont-Terri-Member     |
|15251221 | Fasiswald-Member | Fasiswald-Member     |
|15251222 | Weissenstein-Member | Weissenstein-Member     |
|15251223 | Beggingen-Member | Beggingen-Member     |
|15251224 | Gächlingen-Bank | Gächlingen-Bank     |
|15251225 | Schleitheim-Bank | Schleitheim-Bank     |
|15251226 | Schambelen-Member | Schambelen-Member     |
|15251227 | Hallau-Bank | Hallau-Bank     |
|15251228 | Jurensismergel-Formation | Jurensismergel-Formation     |
|15251229 | Posidonienschiefer-Formation | Posidonienschiefer-Formation     |
|15251230 | Amaltheenton-Formation | Amaltheenton-Formation     |
|15251286 | Etzgen-Granit | Etzgen-Granit     |
|15251287 | Stockberg-Rhyolith | Stockberg-Rhyolith     |
|15251288 | Schafisheim-Syenit | Schafisheim-Syenit     |
|15251289 | Pfaffnau-Granit | Pfaffnau-Granit     |
|15251290 | Bärhalde-Granit | Bärhalde-Granit     |
|15251291 | Schluchsee-Granit | Schluchsee-Granit     |
|15251292 | Säckingen-Granit | Säckingen-Granit     |
|15251293 | Zurzach-Granit | Zurzach-Granit     |
|15251294 | Siblingen-Granit | Siblingen-Granit     |
|15251295 | Albtal-Granit | Albtal-Granit     |
|15251296 | Malsburg-Granit | Malsburg-Granit     |
|15251297 | Blauen-Granit | Blauen-Granit     |
|15251298 | Klemmbach-Granit | Klemmbach-Granit     |
|15251299 | Schlächtenhaus-Granit | Schlächtenhaus-Granit     |
|15251300 | «Randgranit» | «Randgranit»     |
|15251301 | Münsterhalden-Granit | Münsterhalden-Granit     |
|15251302 | Schönau-Herrenschwand-Granit | Schönau-Herrenschwand-Granit     |
|15251303 | St.-Blasien-Granit | St.-Blasien-Granit     |
|15251304 | Mambach-Granit | Mambach-Granit     |
|15251305 | Lenzkirch-Steina-Granit | Lenzkirch-Steina-Granit     |
|15251306 | Lindau-Granit | Lindau-Granit     |
|15251307 | Kreuzlingen-Granit | Kreuzlingen-Granit     |
|15251308 | Hauenstein-Granit | Hauenstein-Granit     |
|15251309 | Böttstein-Granit | Böttstein-Granit     |
|15251310 | Schlächtenhaus-Schiefer | Schlächtenhaus-Schiefer     |
|15251311 | Gersbach-Schiefer | Gersbach-Schiefer     |
|15251312 | Herdern-Streifengneis | Herdern-Streifengneis     |
|15251313 | Todtmoos-Horbach-Gneiskomplex | Todtmoos-Horbach-Gneiskomplex     |
|15251314 | Steinatal-Gneiskomplex | Steinatal-Gneiskomplex     |
|15251315 | Murgtal-Gneiskomplex | Murgtal-Gneiskomplex     |
|15251316 | Laufenburg-Gneiskomplex | Laufenburg-Gneiskomplex     |
|15251317 | Wiesen-Wehratal-Gneiskomplex | Wiesen-Wehratal-Gneiskomplex     |
|15251318 | Wehratal-Syenit | Wehratal-Syenit     |
|15252001 | Bois-de-Raube-Formation | Bois-de-Raube-Formation     |
|15252002 | Ajoie-Member | Ajoie-Member     |
|15252003 | Bois-de-Raube-Member | Bois-de-Raube-Member     |
|15252004 | Montchaibeux-Member | Montchaibeux-Member     |
|15252005 | Kalter-Wangen-Formation | Kalter-Wangen-Formation     |
|15252006 | Heilsberg-Bentonit | Heilsberg-Bentonit     |
|15252007 | Humlikon-Bentonit | Humlikon-Bentonit     |
|15252008 | Aargauer Juranagelfluh | Aargauer Juranagelfluh     |
|15252009 | Basler Juranagelfluh | Basler Juranagelfluh     |
|15252010 | Laufen-Juranagelfluh | Laufen-Juranagelfluh     |
|15252011 | Vermes-Süsswasserkalk | Vermes-Süsswasserkalk     |
|15252012 | Golat-Süsswasserkalk | Golat-Süsswasserkalk     |
|15252013 | Le-Locle-Formation | Le-Locle-Formation     |
|15252014 | Le-Verger-Member | Le-Verger-Member     |
|15252015 | Combe-Girard-Member | Combe-Girard-Member     |
|15252016 | Combe-Girard-Bentonit | Combe-Girard-Bentonit     |
|15252017 | «Heliciden-Mergel» (OSM-J) | «Heliciden-Mergel» (OSM-J)     |
|15252018 | Les-Bayards-Juranagelfluh | Les-Bayards-Juranagelfluh     |
|15252019 | Mittlere Juranagelfluh | Mittlere Juranagelfluh     |
|15252020 | Albstein | Albstein     |
|15252021 | Napf-Formation | Napf-Formation     |
|15252022 | Wolhusen-Bentonit | Wolhusen-Bentonit     |
|15252023 | Eimätteli-Member | Eimätteli-Member     |
|15252024 | Blapbach-Kohleflöz | Blapbach-Kohleflöz     |
|15252025 | Gitzitobel-Süsswasserkalk | Gitzitobel-Süsswasserkalk     |
|15252026 | Wissenbach-Süsswasserkalk | Wissenbach-Süsswasserkalk     |
|15252139 | «Cyathulabank» (UMM-J) | «Cyathulabank» (UMM-J)     |
|15252140 | «Cyrenenmergel» (UMM-J) | «Cyrenenmergel» (UMM-J)     |
|15252141 | «Septarienton» (UMM-J) | «Septarienton» (UMM-J)     |
|15252142 | «Fischschiefer» (UMM-J) | «Fischschiefer» (UMM-J)     |
|15252143 | «Foraminiferenmergel» (UMM-J) | «Foraminiferenmergel» (UMM-J)     |
|15252144 | «Meeressand» (UMM-J) | «Meeressand» (UMM-J)     |
|15252145 | Ajoie-Gompholit | Ajoie-Gompholit     |
|15252146 | Oltingue-Kalkarenit | Oltingue-Kalkarenit     |
|15252147 | Bonneville-Sandstein | Bonneville-Sandstein     |
|15252148 | Montauban-Mergel | Montauban-Mergel     |
|15252149 | Cucloz-Formation | Cucloz-Formation     |
|15252150 | Cucloz-Sandstein | Cucloz-Sandstein     |
|15252151 | «Marnes gris-souris» (Cucloz-Fm.) | «Marnes gris-souris» (Cucloz-Fm.)     |
|15252152 | «Schistes marno-micacés» (Cucloz-Fm.) | «Schistes marno-micacés» (Cucloz-Fm.)     |
|15252153 | Goldegg-Sandstein | Goldegg-Sandstein     |
|15252154 | Jordisboden-Mergel | Jordisboden-Mergel     |
|15252155 | Vaulruz-Formation | Vaulruz-Formation     |
|15252156 | «Molasse Rouge de Vevey» | «Molasse Rouge de Vevey»     |
|15252157 | Mont-Pèlerin-Nagelfluh | Mont-Pèlerin-Nagelfluh     |
|15252158 | Cornalle-Sandstein | Cornalle-Sandstein     |
|15252159 | «Molasse à Charbon» | «Molasse à Charbon»     |
|15252160 | Gérignoz-Formation | Gérignoz-Formation     |
|15252161 | Studweid-Formation | Studweid-Formation     |
|15252162 | Heuboden-Äschitannen-Nagelfluh | Heuboden-Äschitannen-Nagelfluh     |
|15252163 | Horw-Sandstein | Horw-Sandstein     |
|15252164 | Grisigen-Mergel | Grisigen-Mergel     |
|15252165 | Hilfern-Formation | Hilfern-Formation     |
|15252166 | Unter-Lochsiti-Nagelfluh | Unter-Lochsiti-Nagelfluh     |
|15252167 | Flühli-Nagelfluh | Flühli-Nagelfluh     |
|15252168 | Gitzschöpf-Nagelfluh | Gitzschöpf-Nagelfluh     |
|15252169 | Honegg-Mergel | Honegg-Mergel     |
|15252170 | Kaltbach-Nagelfluh | Kaltbach-Nagelfluh     |
|15252171 | Thun-Formation | Thun-Formation     |
|15252172 | Gunten-Nagelfluh | Gunten-Nagelfluh     |
|15252173 | Hünibach-Nagelfluh | Hünibach-Nagelfluh     |
|15252174 | Losenegg-Formation | Losenegg-Formation     |
|15252175 | Homberg-Formation | Homberg-Formation     |
|15252176 | Schwändibach-Nagelfluh | Schwändibach-Nagelfluh     |
|15252177 | Uerscheli-Formation | Uerscheli-Formation     |
|15252178 | Bumbach-Nagelfluh | Bumbach-Nagelfluh     |
|15252179 | Beichlen-Formation | Beichlen-Formation     |
|15252180 | Lienegg-Formation | Lienegg-Formation     |
|15252181 | Öligraben-Formation | Öligraben-Formation     |
|15252182 | Hornbüel-Melange | Hornbüel-Melange     |
|15252183 | Hombach-Member | Hombach-Member     |
|15252184 | Rigi-Formation | Rigi-Formation     |
|15252185 | Scheidegg-Nagelfluh | Scheidegg-Nagelfluh     |
|15252186 | «Bunte Rigi-Nagelfluh» | «Bunte Rigi-Nagelfluh»     |
|15252187 | Pfiffegg-Nagelfluh | Pfiffegg-Nagelfluh     |
|15252188 | «Radiolaritreiche Nagelfluh» (Rigi-Fm.) | «Radiolaritreiche Nagelfluh» (Rigi-Fm.)     |
|15252189 | Weggis-Formation | Weggis-Formation     |
|15252190 | Kännelegg-Nagelfluh | Kännelegg-Nagelfluh     |
|15252191 | Grindelegg-Formation | Grindelegg-Formation     |
|15252192 | Höhronen-Nagelfluh | Höhronen-Nagelfluh     |
|15252193 | Speer-Formation | Speer-Formation     |
|15252194 | Wintersberg-member | Wintersberg-Member     |
|15252195 | Ebnat-Member | Ebnat-Member     |
|15252196 | Rütiberg-Kalksandstein | Rütiberg-Kalksandstein     |
|15252197 | Leuenfall-Nagelfluh | Leuenfall-Nagelfluh     |
|15252198 | Rietbad-Formation | Rietbad-Formation     |
|15252199 | Kronberg-Nagelfluh | Kronberg-Nagelfluh     |
|15252200 | Pfingstboden-Member | Pfingstboden-Member     |
|15252201 | Hochfläschli-Member | Hochfläschli-Member     |
|15252202 | Ennetbühl-Member | Ennetbühl-Member     |
|15252203 | Hochalp-Member | Hochalp-Member     |
|15252204 | Krummenau-Member | Krummenau-Member     |
|15252205 | Sommersberg-Nagelfluh | Sommersberg-Nagelfluh     |
|15252206 | Brendenbach-Mergel | Brendenbach-Mergel     |
|15252207 | Gäbris-Nagelfluh | Gäbris-Nagelfluh     |
|15252208 | Gstaldenbach-Member | Gstaldenbach-Member     |
|15252209 | Heiden-Member | Heiden-Member     |
|15252210 | Klusbach-Member | Klusbach-Member     |
|15252211 | Eggen-Member | Eggen-Member     |
|15252212 | Sulzbach-Member | Sulzbach-Member     |
|15252213 | Marbach-Member | Marbach-Member     |
|15253001 | Zettenalp-Trochematt-Melange | Zettenalp-Trochematt-Melange     |
|15253002 | Laubersmad-Flysch | Laubersmad-Flysch     |
|15253003 | Serhalten-Flysch | Serhalten-Flysch     |
|15253004 | Ruestel-Flysch | Ruestel-Flysch     |
|15253005 | Matt-Formation | Matt-Formation     |
|15253006 | Engi-Dachschiefer | Engi-Dachschiefer     |
|15253007 | Gruontal-Konglomerat | Gruontal-Konglomerat     |
|15253008 | Rüschenweid-Bank | Rüschenweid-Bank     |
|15253009 | Elm-Formation | Elm-Formation     |
|15253010 | Val-d&#39;Illiez-Sandstein | Val-d&#39;Illiez-Sandstein     |
|15253011 | Taveyannaz-Formation | Taveyannaz-Formation     |
|15253012 | Lavtina-Sandstein | Lavtina-Sandstein     |
|15253013 | Burg-Sandstein | Burg-Sandstein     |
|15253014 | Muot-da-Rubi-Formation | Muot-da-Rubi-Formation     |
|15253015 | Ahornen-Member | Ahornen-Member     |
|15253016 | Kistenstöckli-Member | Kistenstöckli-Member     |
|15253017 | Ghölzwald-Member | Ghölzwald-Member     |
|15253018 | Malor-Member | Malor-Member     |
|15253019 | Südelgrabe-Melange | Südelgrabe-Melange     |
|15253020 | Stad-Formation | Stad-Formation     |
|15253021 | Wängen-Kalk | Wängen-Kalk     |
|15253022 | Jochstock-Konglomerat | Jochstock-Konglomerat     |
|15253023 | Rütenen-Konglomerat | Rütenen-Konglomerat     |
|15253024 | Kleintal-Konglomerat | Kleintal-Konglomerat     |
|15253025 | Lochegg-Brekzie | Lochegg-Brekzie     |
|15253026 | Spirstock-Member | Spirstock-Member     |
|15253027 | Sanetsch-Formation | Sanetsch-Formation     |
|15253028 | Pierredar-Kalk | Pierredar-Kalk     |
|15253029 | Tsanfleuron-Member | Tsanfleuron-Member     |
|15253030 | Diablerets-Member | Diablerets-Member     |
|15253031 | Roc-Champion-Konglomerat | Roc-Champion-Konglomerat     |
|15253032 | Niederhorn-Formation | Niederhorn-Formation     |
|15253033 | Gemmenalp-Kalk | Gemmenalp-Kalk     |
|15253034 | Hohgant-Sandstein | Hohgant-Sandstein     |
|15253035 | Wagenmoos-Bänke | Wagenmoos-Bänke     |
|15253036 | Berglikehle-Bank | Berglikehle-Bank     |
|15253037 | Mürren-Brekzie | Mürren-Brekzie     |
|15253038 | Wildstrubel-Formation | Wildstrubel-Formation     |
|15253039 | Schimberg-Member | Schimberg-Member     |
|15253040 | Tierberg-Member | Tierberg-Member     |
|15253041 | Küblibad-Member | Küblibad-Member     |
|15253042 | Klimsenhorn-Formation | Klimsenhorn-Formation     |
|15253161 | Tierces-Formation | Tierces-Formation     |
|15253162 | Prodkamm-Formation | Prodkamm-Formation     |
|15253163 | «Leitoolith» (Prodkamm-Fm.) | «Leitoolith» (Prodkamm-Fm.)     |
|15253164 | «Cardinia-Member» | «Cardinia-Member»     |
|15253165 | Weissgandstöckli-Bank | Weissgandstöckli-Bank     |
|15253166 | «Infralias-Sandstein» | «Infralias-Sandstein»     |
|15253167 | Besoëns-Formation | Besoëns-Formation     |
|15253168 | Quarten-Formation | Quarten-Formation     |
|15253169 | Arandellys-Formation | Arandellys-Formation     |
|15253170 | Griaz-Member | Griaz-Member     |
|15253171 | Röti-Formation | Röti-Formation     |
|15253172 | Vieux-Emosson-Formation | Vieux-Emosson-Formation     |
|15253173 | Col-du-Jorat-Member | Col-du-Jorat-Member     |
|15253174 | Mels-Formation | Mels-Formation     |
|15253175 | «Subalpiner Flysch» | «Subalpiner Flysch»     |
|15253176 | Vernayaz-Formation | Vernayaz-Formation     |
|15253177 | Dzéman-Member | Dzéman-Member     |
|15253178 | Salvan-Member | Salvan-Member     |
|15253179 | Au-d&#39;Arbignon-Schiefer | Au-d&#39;Arbignon-Schiefer     |
|15253180 | Vallorcine-Konglomerat | Vallorcine-Konglomerat     |
|15253181 | Dorénaz-Konglomerat | Dorénaz-Konglomerat     |
|15253182 | Plex-Aboyeu-Rhyolith | Plex-Aboyeu-Rhyolith     |
|15253183 | Morcles-Mikrogranit | Morcles-Mikrogranit     |
|15253184 | Vallorcine-Granit | Vallorcine-Granit     |
|15253185 | Miéville-Mylonit | Miéville-Mylonit     |
|15253186 | Montées-Pélissiers-Granit | Montées-Pélissiers-Granit     |
|15253187 | Pormenaz-Granit | Pormenaz-Granit     |
|15253188 | Luisin-Orthogneis | Luisin-Orthogneis     |
|15253189 | Perrons-Orthogneis | Perrons-Orthogneis     |
|15253190 | Emosson-Gneiskomplex | Emosson-Gneiskomplex     |
|15253191 | Chéserys-Gneis | Chéserys-Gneis     |
|15253192 | Val-Bérard-Gneiskomplex | Val-Bérard-Gneiskomplex     |
|15253193 | Lac-Cornu-Eklogit | Lac-Cornu-Eklogit     |
|15253194 | Fully-Granodiorit | Fully-Granodiorit     |
|15253195 | Fully-Gneiskomplex | Fully-Gneiskomplex     |
|15253196 | Breya-Rhyolith | Breya-Rhyolith     |
|15253197 | Grépillons-Leukogranit | Grépillons-Leukogranit     |
|15253198 | Arpette-Leukogranit | Arpette-Leukogranit     |
|15253199 | Mont-Blanc-Granit | Mont-Blanc-Granit     |
|15253200 | Montenvers-Granit | Montenvers-Granit     |
|15253201 | Lognan-Orthogneis | Lognan-Orthogneis     |
|15253202 | Pétoudes-Orthogneis | Pétoudes-Orthogneis     |
|15253203 | Catogne-Gneiskomplex | Catogne-Gneiskomplex     |
|15253204 | Sandpass-Formation | Sandpass-Formation     |
|15253205 | Plattenzüg-Formation | Plattenzüg-Formation     |
|15253206 | Mittagfluh-Granit | Mittagfluh-Granit     |
|15253207 | Hinterbalm-Granit | Hinterbalm-Granit     |
|15253208 | Balmenegg-Granit | Balmenegg-Granit     |
|15253209 | Zentraler Aare-Granit | Zentraler Aare-Granit     |
|15253210 | Unter-der-Flue-Granit | Unter-der-Flue-Granit     |
|15253211 | Beesten-Granit | Beesten-Granit     |
|15253212 | Telltistock-Granit | Telltistock-Granit     |
|15253213 | «Südwestlicher Aare-Granit» | «Südwestlicher Aare-Granit»     |
|15253214 | Strem-Granit | Strem-Granit     |
|15253215 | Grimsel-Granodiorit | Grimsel-Granodiorit     |
|15253216 | Rossbodenstock-Diorit | Rossbodenstock-Diorit     |
|15253217 | Wendenjoch-Formation | Wendenjoch-Formation     |
|15253218 | Goltschenried-Formation | Goltschenried-Formation     |
|15253219 | Trift-Formation | Trift-Formation     |
|15253043 | Fruttli-Member | Fruttli-Member     |
|15253044 | Band-Member | Band-Member     |
|15253045 | Fräkmünt-Member | Fräkmünt-Member     |
|15253046 | Bürgen-Formation | Bürgen-Formation     |
|15253047 | Foribach-Member | Foribach-Member     |
|15253048 | Mattgrat-Member | Mattgrat-Member     |
|15253049 | Scharti-Member | Scharti-Member     |
|15253050 | Steinbach-Member | Steinbach-Member     |
|15253051 | Euthal-Formation | Euthal-Formation     |
|15253052 | Einsiedeln-Member | Einsiedeln-Member     |
|15253053 | Chruteren-Member | Chruteren-Member     |
|15253054 | Batöni-Member | Batöni-Member     |
|15253055 | Guschakopf-Sandstein | Guschakopf-Sandstein     |
|15253056 | Vasanachopf-Member | Vasanachopf-Member     |
|15253057 | Fliegenspitz-Member | Fliegenspitz-Member     |
|15253058 | Grindelwald-Marmor | Grindelwald-Marmor     |
|15253059 | Dünden-Konglomerat | Dünden-Konglomerat     |
|15253060 | Rosenlaui-Marmor | Rosenlaui-Marmor     |
|15253061 | Wang-Formation | Wang-Formation     |
|15253062 | «Wang-Brekzie» | «Wang-Brekzie»     |
|15253063 | Amden-Mergel | Amden-Mergel     |
|15253064 | Leist-Mergel | Leist-Mergel     |
|15253065 | Grotzen-Austernbank | Grotzen-Austernbank     |
|15253066 | Leiboden-Mergel | Leiboden-Mergel     |
|15253067 | Seewen-Formation | Seewen-Formation     |
|15253068 | Choltal-Member | Choltal-Member     |
|15253069 | «Roter Seewenkalk» | «Roter Seewenkalk»     |
|15253070 | Untere Götzis-Bank | Untere Götzis-Bank     |
|15253071 | Garschella-Formation | Garschella-Formation     |
|15253072 | Selun-Member | Selun-Member     |
|15253073 | Kamm-Bank | Kamm-Bank     |
|15253074 | Aubrig-Schichten | Aubrig-Schichten     |
|15253075 | Wannenalp-Bank | Wannenalp-Bank     |
|15253076 | Sellamatt-Schichten | Sellamatt-Schichten     |
|15253077 | Plattenwald-Bank | Plattenwald-Bank     |
|15253078 | Durschlägi-Bank | Durschlägi-Bank     |
|15253079 | Niederi-Schichten | Niederi-Schichten     |
|15253080 | Klaus-Bank | Klaus-Bank     |
|15253081 | Twäriberg-Bank | Twäriberg-Bank     |
|15253082 | Rankweil-Member | Rankweil-Member     |
|15253083 | Brisi-Member | Brisi-Member     |
|15253084 | Gams-Schichten | Gams-Schichten     |
|15253085 | Luitere-Bank | Luitere-Bank     |
|15253086 | Freschen-Member | Freschen-Member     |
|15253087 | Hochkugel-Schichten | Hochkugel-Schichten     |
|15253088 | Grünten-Member | Grünten-Member     |
|15253089 | Col-de-la-Plaine-Morte-Bank | Col-de-la-Plaine-Morte-Bank     |
|15253090 | Rohrbachstein-Bank | Rohrbachstein-Bank     |
|15253091 | Schrattenkalk-Formation | Schrattenkalk-Formation     |
|15253092 | «Oberer Schrattenkalk» | «Oberer Schrattenkalk»     |
|15253093 | Rawil-Member | Rawil-Member     |
|15253094 | «Unterer Schrattenkalk» | «Unterer Schrattenkalk»     |
|15253095 | Tierwis-Formation | Tierwis-Formation     |
|15253096 | Hurst-Mergel | Hurst-Mergel     |
|15253097 | Chopf-Bank | Chopf-Bank     |
|15253098 | Drusberg-Member | Drusberg-Member     |
|15253099 | Altmann-Member | Altmann-Member     |
|15253100 | Helvetischer Kieselkalk | Helvetischer Kieselkalk     |
|15253101 | Chriesiloch-Echinodermenkalk | Chriesiloch-Echinodermenkalk     |
|15253102 | Lidernen-Member | Lidernen-Member     |
|15253103 | Ringgenberg-Schichten | Ringgenberg-Schichten     |
|15253104 | Rahberg-Bank | Rahberg-Bank     |
|15253105 | Palis-Bank | Palis-Bank     |
|15253106 | Gemsmättli-Bank | Gemsmättli-Bank     |
|15253107 | Betlis-Formation | Betlis-Formation     |
|15253108 | «Pygurus-Member» | «Pygurus-Member»     |
|15253109 | «Oberer Betliskalk» | «Oberer Betliskalk»     |
|15253110 | Büls-Bank | Büls-Bank     |
|15253111 | «Unterer Betliskalk» | «Unterer Betliskalk»     |
|15253112 | Spitzern-Member | Spitzern-Member     |
|15253113 | Sichel-Kalk | Sichel-Kalk     |
|15253114 | Diphyoides-Kalk | Diphyoides-Kalk     |
|15253115 | Vitznau-Mergel | Vitznau-Mergel     |
|15253116 | Öhrli-Formation | Öhrli-Formation     |
|15253117 | «Oberer Öhrlikalk» | «Oberer Öhrlikalk»     |
|15253118 | «Oberer Öhrlimergel» | «Oberer Öhrlimergel»     |
|15253119 | «Unterer Öhrlikalk» | «Unterer Öhrlikalk»     |
|15253120 | Palfris-Formation | Palfris-Formation     |
|15253121 | Zementstein-Formation | Zementstein-Formation     |
|15253122 | Graspass-Member | Graspass-Member     |
|15253123 | Gassen-Kalk | Gassen-Kalk     |
|15253124 | Quinten-Formation | Quinten-Formation     |
|15253125 | Tros-Kalk | Tros-Kalk     |
|15253126 | «Oberer Quintner Kalk» | «Oberer Quintner Kalk»     |
|15253127 | «Mergelband» (Quinten-Fm.) | «Mergelband» (Quinten-Fm.)     |
|15253128 | «Unterer Quintner Kalk» | «Unterer Quintner Kalk»     |
|15253129 | Gonzen-Eisenerzhorizont | Gonzen-Eisenerzhorizont     |
|15253130 | Schilt-Formation | Schilt-Formation     |
|15253131 | Mürtschen-Member | Mürtschen-Member     |
|15253132 | Seeztal-Member | Seeztal-Member     |
|15253133 | Windgällen-Member | Windgällen-Member     |
|15253134 | Erzegg-Formation | Erzegg-Formation     |
|15253135 | Planplatte-Eisenoolith | Planplatte-Eisenoolith     |
|15253136 | «Grenzschicht» (Erzegg-Fm.) | «Grenzschicht» (Erzegg-Fm.)     |
|15253137 | Reischiben-Formation | Reischiben-Formation     |
|15253138 | Blegi-Eisenoolith | Blegi-Eisenoolith     |
|15253139 | Bannalp-Konglomerat | Bannalp-Konglomerat     |
|15253140 | Guppen-Fossilhorizont | Guppen-Fossilhorizont     |
|15253141 | Gursbach-Fossilhorizont | Gursbach-Fossilhorizont     |
|15253142 | Hochstollen-Formation | Hochstollen-Formation     |
|15253143 | Schwarzhorn-Member | Schwarzhorn-Member     |
|15253144 | Bietenhorn-Member | Bietenhorn-Member     |
|15253145 | Bommerstein-Formation | Bommerstein-Formation     |
|15253146 | Glockhaus-Member | Glockhaus-Member     |
|15253147 | «Grenzquarzit» (Bommerstein-Fm.) | «Grenzquarzit» (Bommerstein-Fm.)     |
|15253148 | «Obere Tonschiefer» (Bommerstein-Fm.) | «Obere Tonschiefer» (Bommerstein-Fm.)     |
|15253149 | «Rote Echinodermenbrekzie» (Bommerstein-Fm.) | «Rote Echinodermenbrekzie» (Bommerstein-Fm.)     |
|15253150 | Mols-Member | Mols-Member     |
|15253151 | Geissbach-Konglomerat | Geissbach-Konglomerat     |
|15253152 | Stöckli-Sandstein | Stöckli-Sandstein     |
|15253153 | Vättis-Fossilbrekzie | Vättis-Fossilbrekzie     |
|15253154 | Dugny-Formation | Dugny-Formation     |
|15253155 | Brunnistock-Formation | Brunnistock-Formation     |
|15253156 | Monts-Rosset-Formation | Monts-Rosset-Formation     |
|15253157 | Sexmor-Formation | Sexmor-Formation     |
|15253158 | Mont-Joly-Formation | Mont-Joly-Formation     |
|15253159 | Spitzmeilen-Formation | Spitzmeilen-Formation     |
|15253160 | Bränd-Brekzie | Bränd-Brekzie     |
|15252027 | Altbach-Süsswasserkalk | Altbach-Süsswasserkalk     |
|15252028 | Tröleten-Süsswasserkalk | Tröleten-Süsswasserkalk     |
|15252029 | Tschöplihof-Süsswasserkalk | Tschöplihof-Süsswasserkalk     |
|15252030 | Öhningen-Formation | Öhningen-Formation     |
|15252031 | Öhningen-Süsswasserkalk | Öhningen-Süsswasserkalk     |
|15252032 | Bischofzell-Bentonit | Bischofzell-Bentonit     |
|15252033 | Ramschwag-Nagelfluh | Ramschwag-Nagelfluh     |
|15252034 | Hörnli-Formation | Hörnli-Formation     |
|15252035 | Hörnligipfel-Nagelfluh | Hörnligipfel-Nagelfluh     |
|15252036 | Hörnligubel-Mergel | Hörnligubel-Mergel     |
|15252037 | Höchegg-Brekzie | Höchegg-Brekzie     |
|15252038 | Tösswald-Member | Tösswald-Member     |
|15252039 | Seerücken-Tuffit | Seerücken-Tuffit     |
|15252040 | Krinau-Member | Krinau-Member     |
|15252041 | Uetliberg-Formation | Uetliberg-Formation     |
|15252042 | Uetliberggipfel-Nagelfluh | Uetliberggipfel-Nagelfluh     |
|15252043 | Uetliberg-Mergel | Uetliberg-Mergel     |
|15252044 | Loorenkopf-Nagelfluh | Loorenkopf-Nagelfluh     |
|15252045 | Pfannenstiel-Formation | Pfannenstiel-Formation     |
|15252046 | Falätschen-Mergel | Falätschen-Mergel     |
|15252047 | Zürich-Formation | Zürich-Formation     |
|15252048 | Fellitobel-Süsswasserkalk | Fellitobel-Süsswasserkalk     |
|15252049 | Leimbach-Bentonit | Leimbach-Bentonit     |
|15252050 | Rütschlibach-Riedhof-Süsswasserkalk | Rütschlibach-Riedhof-Süsswasserkalk     |
|15252051 | Winterthur-Bentonit | Winterthur-Bentonit     |
|15252052 | Aeugstertal-Bentonit | Aeugstertal-Bentonit     |
|15252053 | Äntlisberg-Doldertobel-Süsswasserkalk | Äntlisberg-Doldertobel-Süsswasserkalk     |
|15252054 | Wehrenbach-Höckler-Süsswasserkalk | Wehrenbach-Höckler-Süsswasserkalk     |
|15252055 | Meilen-Formation | Meilen-Formation     |
|15252056 | Küsnacht-Bentonit | Küsnacht-Bentonit     |
|15252057 | «Wulp-Rotzone» | «Wulp-Rotzone»     |
|15252058 | Urdorf-Bentonit | Urdorf-Bentonit     |
|15252059 | «Appenzellergranit-Leitniveau» | «Appenzellergranit-Leitniveau»     |
|15252060 | Degersheim-Kalknagelfluh | Degersheim-Kalknagelfluh     |
|15252061 | Abtwil-Konglomerat | Abtwil-Konglomerat     |
|15252062 | Meilen-Kalk | Meilen-Kalk     |
|15252063 | Hüllistein-Konglomerat | Hüllistein-Konglomerat     |
|15252064 | Haldenhof-Mergel | Haldenhof-Mergel     |
|15252065 | Lichtensteig-Formation | Lichtensteig-Formation     |
|15252066 | Kapfnach-Formation | Kapfnach-Formation     |
|15252067 | Horgen-Käpfnach-Süsswasserkalk | Horgen-Käpfnach-Süsswasserkalk     |
|15252068 | Guggershorn-Formation | Guggershorn-Formation     |
|15252069 | Kirchberg-Formation | Kirchberg-Formation     |
|15252070 | Grimmelfingen-Formation | Grimmelfingen-Formation     |
|15252071 | Pfänder-Formation | Pfänder-Formation     |
|15252072 | Tannenwald-Schichten | Tannenwald-Schichten     |
|15252073 | Tannenberg-Schichten | Tannenberg-Schichten     |
|15252074 | Schüpferegg-Nagelfluh | Schüpferegg-Nagelfluh     |
|15252075 | Gabelspitz-Schichten | Gabelspitz-Schichten     |
|15252076 | Schallenberg-Member | Schallenberg-Member     |
|15252077 | Seli-Nagelfluh | Seli-Nagelfluh     |
|15252078 | Kalchstätten-Formation | Kalchstätten-Formation     |
|15252079 | Pfadflüe-Member | Pfadflüe-Member     |
|15252080 | Crêt-du-Locle-Formation | Crêt-du-Locle-Formation     |
|15252081 | Baltersweil-Nagelfluh | Baltersweil-Nagelfluh     |
|15252082 | St.-Gallen-Formation | St.-Gallen-Formation     |
|15252083 | «Obere Grenznagelfluh» | «Obere Grenznagelfluh»     |
|15252084 | Goldbrunnen-Schichten | Goldbrunnen-Schichten     |
|15252085 | Dreilinden-Nagelfluh | Dreilinden-Nagelfluh     |
|15252086 | Freudenberg-Nagelfluh | Freudenberg-Nagelfluh     |
|15252087 | Staffelbach-Grobsandstein | Staffelbach-Grobsandstein     |
|15252088 | Gitzigrabe-Grobsandstein | Gitzigrabe-Grobsandstein     |
|15252089 | Niedermatt-Formation | Niedermatt-Formation     |
|15252090 | Belpberg-Formation | Belpberg-Formation     |
|15252091 | Sädel-Kalknagelfluh | Sädel-Kalknagelfluh     |
|15252092 | Utzigen-Muschelsandstein | Utzigen-Muschelsandstein     |
|15252093 | Ulmiz-Quarzitnagelfluh | Ulmiz-Quarzitnagelfluh     |
|15252094 | Bütschelbach-Nagelfluh | Bütschelbach-Nagelfluh     |
|15252095 | Jensberg-Formation | Jensberg-Formation     |
|15252096 | Rebhubel-Schichten | Rebhubel-Schichten     |
|15252097 | Netzbachtal-Nagelfluh | Netzbachtal-Nagelfluh     |
|15252098 | Randen-Grobkalk | Randen-Grobkalk     |
|15252099 | Tenniken-Muschelagglomerat | Tenniken-Muschelagglomerat     |
|15252100 | Péry-Sandstein | Péry-Sandstein     |
|15252101 | Luzern-Formation | Luzern-Formation     |
|15252102 | Safenwil-Muschelsandstein | Safenwil-Muschelsandstein     |
|15252103 | Sense-Formation | Sense-Formation     |
|15252104 | Molière-Muschelsandstein | Molière-Muschelsandstein     |
|15252105 | Montécu-Schichten | Montécu-Schichten     |
|15252106 | Scherli-Quarzitnagelfluh | Scherli-Quarzitnagelfluh     |
|15252107 | Chnebelburg-Formation | Chnebelburg-Formation     |
|15252108 | Meinisberg-Muschelsandstein | Meinisberg-Muschelsandstein     |
|15252109 | Brüttelen-Grobsandstein | Brüttelen-Grobsandstein     |
|15252110 | «Formation der Granitischen Molasse» | «Formation der Granitischen Molasse»     |
|15252111 | «Oberaquitane Mergelzone» | «Oberaquitane Mergelzone»     |
|15252112 | «Molasse Grise de Lausanne» | «Molasse Grise de Lausanne»     |
|15252113 | Bois-Genoud-Bentonit | Bois-Genoud-Bentonit     |
|15252114 | Cuarny-Sandstein | Cuarny-Sandstein     |
|15252115 | Gümmenen-Formation | Gümmenen-Formation     |
|15252116 | «Obere Bunte Molasse» (USM-II) | «Obere Bunte Molasse» (USM-II)     |
|15252117 | «Grès et Marnes Gris à Gypse» | «Grès et Marnes Gris à Gypse»     |
|15252118 | Tillerée-Schichten | Tillerée-Schichten     |
|15252119 | «Untere Bunte Molasse» (USM-I) | «Untere Bunte Molasse» (USM-I)     |
|15252120 | Mümliswil-Süsswasserkalk | Mümliswil-Süsswasserkalk     |
|15252121 | «Molasse Rouge de Monthey» | «Molasse Rouge de Monthey»     |
|15252122 | «Molasse Rouge des Jurasüdfusses» | «Molasse Rouge des Jurasüdfusses»     |
|15252123 | Mathod-Sandstein | Mathod-Sandstein     |
|15252124 | Goumoëns-Sandstein | Goumoëns-Sandstein     |
|15252125 | Dardagny-Sandstein | Dardagny-Sandstein     |
|15252126 | La-Chaux-Süsswasserkalk | La-Chaux-Süsswasserkalk     |
|15252127 | «Ältere Juranagelfluh» | «Ältere Juranagelfluh»     |
|15252128 | Tüllingen-Süsswasserkalk | Tüllingen-Süsswasserkalk     |
|15252129 | «Elsässer-Molasse» | «Elsässer-Molasse»     |
|15252130 | Delémont-Süsswasserkalk | Delémont-Süsswasserkalk     |
|15252131 | Matzendorf-Süsswasserkalk | Matzendorf-Süsswasserkalk     |
|15252132 | Wynau-Süsswasserkalk | Wynau-Süsswasserkalk     |
|15252133 | Oensingen-Süsswasserkalk | Oensingen-Süsswasserkalk     |
|15252134 | Trois-Rods-Süsswasserkalk | Trois-Rods-Süsswasserkalk     |
|15252135 | Orbe-Süsswasserkalk | Orbe-Süsswasserkalk     |
|15252136 | Grilly-Süsswasserkalk | Grilly-Süsswasserkalk     |
|15252137 | Porrentruy-Konglomerat | Porrentruy-Konglomerat     |
|15252138 | Mornex-Nagelfluh | Mornex-Nagelfluh     |
|15253336 | Goms-Gneiskomplex | Goms-Gneiskomplex     |
|15253337 | Unterwassern-Gneis | Unterwassern-Gneis     |
|15253338 | Streifengneis-Komplex | Streifengneis-Komplex     |
|15253339 | Hüenerstock-Gneis | Hüenerstock-Gneis     |
|15253340 | Sassina-Spans-Augengneis | Sassina-Spans-Augengneis     |
|15253341 | Alp-Ramosa-Granitgneis | Alp-Ramosa-Granitgneis     |
|15253342 | Chastelhorn-Metagabbro | Chastelhorn-Metagabbro     |
|15253343 | Val-Nalps-Gneiskomplex | Val-Nalps-Gneiskomplex     |
|15253344 | Prato-Gneis | Prato-Gneis     |
|15253345 | Distelgrat-Gneis | Distelgrat-Gneis     |
|15253346 | Guspis-Gneis | Guspis-Gneis     |
|15253347 | Gurschen-Gneis | Gurschen-Gneis     |
|15253348 | Fuorcla-Paradis-Serpentinit | Fuorcla-Paradis-Serpentinit     |
|15253349 | Paradis-Gneiskomplex | Paradis-Gneiskomplex     |
|15253350 | Oberstafel-Gneis | Oberstafel-Gneis     |
|15253351 | Ganneretsch-Gneis | Ganneretsch-Gneis     |
|15253352 | Sorescia-Gneis | Sorescia-Gneis     |
|15253353 | Val-Camadra-Migmatit | Val-Camadra-Migmatit     |
|15253354 | Val-Gronda-Augengneis | Val-Gronda-Augengneis     |
|15253355 | Corandoni-Amphibolit | Corandoni-Amphibolit     |
|15253356 | Coroi-Formation | Coroi-Formation     |
|15253357 | «Basaler Quarzit» (Coroi-Fm.) | «Basaler Quarzit» (Coroi-Fm.)     |
|15253358 | Inferno-Formation | Inferno-Formation     |
|15253359 | Runcaldeida-Schichten | Runcaldeida-Schichten     |
|15253360 | Riein-Schichten | Riein-Schichten     |
|15253361 | Stgir-Formation | Stgir-Formation     |
|15253362 | Habkern-Melange | Habkern-Melange     |
|15253363 | Habkern-Granit | Habkern-Granit     |
|15253364 | Leimern-Schichten | Leimern-Schichten     |
|15253365 | Schattwald-Mergelkalk | Schattwald-Mergelkalk     |
|15253366 | Sörenberg-Melange | Sörenberg-Melange     |
|15253367 | Iberg-Melange | Iberg-Melange     |
|15253368 | Surbrunnen-Flysch | Surbrunnen-Flysch     |
|15253369 | Roggenegg-Komplex | Roggenegg-Komplex     |
|15253370 | Isentobel-Komplex | Isentobel-Komplex     |
|15253371 | Gwürz-Flysch | Gwürz-Flysch     |
|15253372 | Scheidegg-Flysch | Scheidegg-Flysch     |
|15253373 | Wildhaus-Melange | Wildhaus-Melange     |
|15253374 | Plaine-Morte-Melange | Plaine-Morte-Melange     |
|15253375 | Sex-Mort-Flysch | Sex-Mort-Flysch     |
|15253376 | Arveyes-Flysch | Arveyes-Flysch     |
|15253377 | Gryonne-Formation | Gryonne-Formation     |
|15253378 | Meilleret-Formation | Meilleret-Formation     |
|15253379 | Höchst-Flysch | Höchst-Flysch     |
|15253380 | Iserin-Konglomerat | Iserin-Konglomerat     |
|15253381 | «Infrapräalpines Melange» | «Infrapräalpines Melange»     |
|15253382 | Gros-Plané-Melange | Gros-Plané-Melange     |
|15253383 | Bodevena-Melange | Bodevena-Melange     |
|15253384 | Covayes-Formation | Covayes-Formation     |
|15253385 | Javrex-Formation | Javrex-Formation     |
|15253386 | Montsalvens-Kalkarenit | Montsalvens-Kalkarenit     |
|15253387 | Villarbeney-Formation | Villarbeney-Formation     |
|15253388 | Cergnement-Member | Cergnement-Member     |
|15253389 | Veveyse-de-Châtel-Member | Veveyse-de-Châtel-Member     |
|15253390 | Riondouneire-Member | Riondouneire-Member     |
|15253391 | Jogne-Formation | Jogne-Formation     |
|15253392 | Vuavres-Member | Vuavres-Member     |
|15253393 | Planière-Member | Planière-Member     |
|15253394 | Bifé-Formation | Bifé-Formation     |
|15253395 | Joux-Galez-Member | Joux-Galez-Member     |
|15253396 | Pereyres-Formation | Pereyres-Formation     |
|15253397 | Praz-Couquain-Formation | Praz-Couquain-Formation     |
|15253398 | Taffon-Member | Taffon-Member     |
|15253399 | Saix-Member | Saix-Member     |
|15253400 | Lochsiten-Kalk | Lochsiten-Kalk     |
|15253401 | Salleren-Brekzie | Salleren-Brekzie     |
|15254001 | Robiei-Wildflysch | Robiei-Wildflysch     |
|15254002 | Pizzo-Castello-Wildflysch | Pizzo-Castello-Wildflysch     |
|15254003 | Tamier-Zött-Wildflysch | Tamier-Zött-Wildflysch     |
|15254004 | Alpe-Tamia-Campo-Wildflysch | Alpe-Tamia-Campo-Wildflysch     |
|15254005 | Teggiolo-Kalkschiefer | Teggiolo-Kalkschiefer     |
|15254006 | Medola-Quarzit | Medola-Quarzit     |
|15254007 | Pianasciom-Kalkschiefer | Pianasciom-Kalkschiefer     |
|15254008 | Piano-delle-Creste-Sandstein | Piano-delle-Creste-Sandstein     |
|15254009 | Vanis-Formation | Vanis-Formation     |
|15254010 | Sevinera-Marmor | Sevinera-Marmor     |
|15254011 | Sevinera-Sandstein | Sevinera-Sandstein     |
|15254012 | Ri-d&#39;Antabia-Konglomerat | Ri-d&#39;Antabia-Konglomerat     |
|15254013 | Antigorio-Orthogneis | Antigorio-Orthogneis     |
|15254014 | Alpigia-Gneis | Alpigia-Gneis     |
|15254015 | Forcoletta-Gneis | Forcoletta-Gneis     |
|15254016 | Aula-Spruga-Gneiskomplex | Aula-Spruga-Gneiskomplex     |
|15254017 | Mergoscia-Gneis | Mergoscia-Gneis     |
|15254018 | Lebendun-Komplex | Lebendun-Komplex     |
|15254019 | «Scisti bruni» (Lebendun) | «Scisti bruni» (Lebendun)     |
|15254020 | Holzerspitz-Kalkschiefer | Holzerspitz-Kalkschiefer     |
|15254021 | Lengenbach-Dolomitmarmor | Lengenbach-Dolomitmarmor     |
|15254022 | Ganter-Gneis | Ganter-Gneis     |
|15254023 | Ritter-Gneis | Ritter-Gneis     |
|15254024 | Geisspfad-Serpentinit | Geisspfad-Serpentinit     |
|15254025 | Sabbione-Sandstein | Sabbione-Sandstein     |
|15254026 | Valgrande-Paragneis | Valgrande-Paragneis     |
|15254027 | Bosco-Gneis | Bosco-Gneis     |
|15254028 | Batnall-Gneis | Batnall-Gneis     |
|15254029 | Cocco-Gneis | Cocco-Gneis     |
|15254030 | Ruscada-Gneis | Ruscada-Gneis     |
|15254031 | Lodano-Gneis | Lodano-Gneis     |
|15254032 | Vergeletto-Gneis | Vergeletto-Gneis     |
|15254033 | Cortascia-Gneis | Cortascia-Gneis     |
|15254034 | Lago-Scuro-Formation | Lago-Scuro-Formation     |
|15254035 | Val-Sabbia-Formation | Val-Sabbia-Formation     |
|15254036 | Massari-Formation | Massari-Formation     |
|15254037 | Naret-Formation | Naret-Formation     |
|15254038 | Matorello-Gneis | Matorello-Gneis     |
|15254039 | Leventina-Gneis | Leventina-Gneis     |
|15254040 | Personico-Gneis | Personico-Gneis     |
|15254041 | Verzasca-Gneis | Verzasca-Gneis     |
|15254042 | Renten-Gneis | Renten-Gneis     |
|15254043 | Rebi-Gneis | Rebi-Gneis     |
|15254044 | Brione-Gabbro | Brione-Gabbro     |
|15254045 | Legiuna-Gneis | Legiuna-Gneis     |
|15254046 | Val-Chironico-Gneis | Val-Chironico-Gneis     |
|15254047 | Ganna-Gneis | Ganna-Gneis     |
|15254048 | Vogorno-Gneis | Vogorno-Gneis     |
|15254049 | Vacarisc-Gneis | Vacarisc-Gneis     |
|15254050 | Rognoi-Gneis | Rognoi-Gneis     |
|15254051 | Zervreila-Orthogneis | Zervreila-Orthogneis     |
|15254052 | Garenstock-Augengneis | Garenstock-Augengneis     |
|15254053 | Salahorn-Formation | Salahorn-Formation     |
|15255116 | Plagersflue-Kalkarenit | Plagersflue-Kalkarenit     |
|15255117 | Intyamon-Formation | Intyamon-Formation     |
|15255118 | Chällihorn-Member | Chällihorn-Member     |
|15255119 | Comba-d&#39;Avau-Member | Comba-d&#39;Avau-Member     |
|15255120 | Rodosex-Member | Rodosex-Member     |
|15255121 | Sciernes-d&#39;Albeuve-Formation | Sciernes-d&#39;Albeuve-Formation     |
|15255122 | Kummli-Schichten | Kummli-Schichten     |
|15255123 | Dorfflüe-Formation | Dorfflüe-Formation     |
|15255124 | Wandfluh-Mikrofazies | Wandfluh-Mikrofazies     |
|15255125 | Gummfluh-Mikrofazies | Gummfluh-Mikrofazies     |
|15255126 | Gastlosen-Oolith | Gastlosen-Oolith     |
|15255127 | Rindenkorn-Mikrofazies | Rindenkorn-Mikrofazies     |
|15255128 | Pfad-Mikrofazies | Pfad-Mikrofazies     |
|15255129 | Moléson-Formation | Moléson-Formation     |
|15255130 | Albeuve-Serie | Albeuve-Serie     |
|15255131 | Torrent-de-Lessoc-Formation | Torrent-de-Lessoc-Formation     |
|15255132 | Dréveneuse-Bauxit | Dréveneuse-Bauxit     |
|15255133 | Mytilus-Schichten | Mytilus-Schichten     |
|15255134 | Col-de-Cordon-Member | Col-de-Cordon-Member     |
|15255135 | Stockenflue-Kalk | Stockenflue-Kalk     |
|15255136 | Klus-Konglomerat | Klus-Konglomerat     |
|15255137 | Holzerhorn-Einheit | Holzerhorn-Einheit     |
|15255138 | Rubli-Member | Rubli-Member     |
|15255139 | Chavanette-Member | Chavanette-Member     |
|15255140 | Staldengraben-Formation | Staldengraben-Formation     |
|15255141 | Col-de-Lys-Member | Col-de-Lys-Member     |
|15255142 | Vanil-Carré-Member | Vanil-Carré-Member     |
|15255143 | Verdy-Member | Verdy-Member     |
|15255144 | Soladier-Member | Soladier-Member     |
|15255145 | Sommant-Formation | Sommant-Formation     |
|15255146 | Langel-Member | Langel-Member     |
|15255147 | Mieussy-Member | Mieussy-Member     |
|15255148 | Haute-Pointe-Formation | Haute-Pointe-Formation     |
|15255149 | Brasses-Formation | Brasses-Formation     |
|15255150 | Rossinière-Formation | Rossinière-Formation     |
|15255151 | Heiti-Formation | Heiti-Formation     |
|15255152 | Combe-du-Pissot-Formation | Combe-du-Pissot-Formation     |
|15255153 | Chevalets-Schichten | Chevalets-Schichten     |
|15255154 | Creux-de-l&#39;Ours-Schichten | Creux-de-l&#39;Ours-Schichten     |
|15255155 | Petit-Liençon-Formation | Petit-Liençon-Formation     |
|15255156 | Arvel-Formation | Arvel-Formation     |
|15255157 | Grande-Bonavau-Formation | Grande-Bonavau-Formation     |
|15255158 | Chauderon-Formation | Chauderon-Formation     |
|15255159 | Vudalla-Formation | Vudalla-Formation     |
|15255160 | Agreblierai-Member | Agreblierai-Member     |
|15255161 | Bois-de-Luan-Member | Bois-de-Luan-Member     |
|15255162 | Col-de-Tompey-Formation | Col-de-Tompey-Formation     |
|15255163 | Plan-Falcon-Formation | Plan-Falcon-Formation     |
|15255164 | «Dolomies Blondes» | «Dolomies Blondes»     |
|15255165 | Clôt-la-Cime-Formation | Clôt-la-Cime-Formation     |
|15255166 | Pralet-Formation | Pralet-Formation     |
|15255167 | «Obere Rauhwacke» (Pralet-Fm.) | «Obere Rauhwacke» (Pralet-Fm.)     |
|15255168 | Erpilles-Member | Erpilles-Member     |
|15255169 | Balmi-Member | Balmi-Member     |
|15255170 | Wiriehorn-Formation | Wiriehorn-Formation     |
|15255171 | Bodeflue-Member | Bodeflue-Member     |
|15255172 | Wildgrimmi-Member | Wildgrimmi-Member     |
|15255173 | St-Triphon-Formation | St-Triphon-Formation     |
|15254054 | Piz-del-Palo-Gneis | Piz-del-Palo-Gneis     |
|15254055 | Gruf-Migmatit | Gruf-Migmatit     |
|15254056 | Sivigia-Gneis | Sivigia-Gneis     |
|15255001 | Garzott-Brekzie | Garzott-Brekzie     |
|15255002 | Terri-Schiefer | Terri-Schiefer     |
|15255003 | Val-Stgira-Riffmarmor | Val-Stgira-Riffmarmor     |
|15255004 | Chesselbach-Formation | Chesselbach-Formation     |
|15255005 | Seron-Formation | Seron-Formation     |
|15255006 | Niesenkulm-Formation | Niesenkulm-Formation     |
|15255007 | Frutigen-Formation | Frutigen-Formation     |
|15255008 | Aigremont-Brekzie | Aigremont-Brekzie     |
|15255009 | Sulzgrabe-Formation | Sulzgrabe-Formation     |
|15255010 | Grande-Eau-Formation | Grande-Eau-Formation     |
|15255011 | Langy-Member | Langy-Member     |
|15255012 | Forclaz-Member | Forclaz-Member     |
|15255013 | «Grès de Passage» | «Grès de Passage»     |
|15255014 | Leyderry-Member | Leyderry-Member     |
|15255015 | Raverette-Member | Raverette-Member     |
|15255016 | «Schistes à Miches» | «Schistes à Miches»     |
|15255017 | Chlussli-Formation | Chlussli-Formation     |
|15255018 | Murgaz-Kalk | Murgaz-Kalk     |
|15255019 | Formation de Bretaye | Formation de Bretaye     |
|15255020 | Oudiou-Formation | Oudiou-Formation     |
|15255021 | Kiental-Melange | Kiental-Melange     |
|15255022 | Boëge-Mergel | Boëge-Mergel     |
|15255023 | Vouan-Konglomerat | Vouan-Konglomerat     |
|15255024 | Voirons-Sandstein | Voirons-Sandstein     |
|15255025 | «Flysch 5, mit kieseligen Mikrokonglomeraten» | «Flysch 5, mit kieseligen Mikrokonglomeraten»     |
|15255026 | «Flysch 4 mit siltigen Turbiditen» | «Flysch 4 mit siltigen Turbiditen»     |
|15255027 | «Flysch 3» | «Flysch 3»     |
|15255028 | «Flysch 3b mit bioklastischen Turbiditen» | «Flysch 3b mit bioklastischen Turbiditen»     |
|15255029 | «Flysch 3a mergelig-sandig» | «Flysch 3a mergelig-sandig»     |
|15255030 | «Flysch 2» | «Flysch 2»     |
|15255031 | «Flysch 2b mit sandigen Turbiditen» | «Flysch 2b mit sandigen Turbiditen»     |
|15255032 | «Flysch 2a tonig-sandig» | «Flysch 2a tonig-sandig»     |
|15255033 | Hellstätt-Formation | Hellstätt-Formation     |
|15255034 | Schlieren-Sandstein | Schlieren-Sandstein     |
|15255035 | Schoni-Sandstein | Schoni-Sandstein     |
|15255036 | «Obere Tonsteinschichten» (Schlieren-Flysch) | «Obere Tonsteinschichten» (Schlieren-Flysch)     |
|15255037 | Guber-Sandstein | Guber-Sandstein     |
|15255038 | «Untere Tonsteinschichten» (Schlieren-Flysch) | «Untere Tonsteinschichten» (Schlieren-Flysch)     |
|15255039 | Wägital-Flysch | Wägital-Flysch     |
|15255040 | Trepsen-Flysch | Trepsen-Flysch     |
|15255041 | Fanola-Formation | Fanola-Formation     |
|15255042 | Planknerbrücke-Formation | Planknerbrücke-Formation     |
|15255043 | Planken-Formation | Planken-Formation     |
|15255044 | Reiselsberg-Formation | Reiselsberg-Formation     |
|15255045 | Rombach-Formation | Rombach-Formation     |
|15255046 | Langenegg-Formation | Langenegg-Formation     |
|15255047 | Rinderbach-Formation | Rinderbach-Formation     |
|15255048 | Triesen-Formation | Triesen-Formation     |
|15255049 | Eichholztobel-Formation | Eichholztobel-Formation     |
|15255050 | Schloss-Formation | Schloss-Formation     |
|15255051 | Gaschlo-Formation | Gaschlo-Formation     |
|15255052 | St-Christophe-Formation | St-Christophe-Formation     |
|15255053 | Marmontains-Formation | Marmontains-Formation     |
|15255054 | Aroley-Formation | Aroley-Formation     |
|15255055 | Südegg-Komplex | Südegg-Komplex     |
|15255056 | Punta-Rossa-Komplex | Punta-Rossa-Komplex     |
|15255057 | Ferret-Schiefer | Ferret-Schiefer     |
|15255058 | Peula-Schichten | Peula-Schichten     |
|15255059 | La-Dotse-Albitkalk | La-Dotse-Albitkalk     |
|15255060 | Pierre-Avoi-Melange | Pierre-Avoi-Melange     |
|15255061 | Pierre-Avoi-Brekzie | Pierre-Avoi-Brekzie     |
|15255062 | Versoyen-Schichten | Versoyen-Schichten     |
|15255063 | Aul-Marmor | Aul-Marmor     |
|15255064 | Stätzerhorn-Formation | Stätzerhorn-Formation     |
|15255065 | Bleis-Pintgas-Member | Bleis-Pintgas-Member     |
|15255066 | Parnegl-Member | Parnegl-Member     |
|15255067 | Danis-Member | Danis-Member     |
|15255068 | Raschil-Member | Raschil-Member     |
|15255069 | «Hauptkonglomerat» | «Hauptkonglomerat»     |
|15255070 | Carnusa-Formation | Carnusa-Formation     |
|15255071 | Nolla-Kalkschiefer | Nolla-Kalkschiefer     |
|15255072 | Safien-Kalk | Safien-Kalk     |
|15255073 | Nolla-Tonschiefer | Nolla-Tonschiefer     |
|15255074 | Bärenhorn-Formation | Bärenhorn-Formation     |
|15255075 | Ruchberg-Formation | Ruchberg-Formation     |
|15255076 | Oberälpli-Formation | Oberälpli-Formation     |
|15255077 | Eggberg-Formation | Eggberg-Formation     |
|15255078 | Gyrenspitz-Formation | Gyrenspitz-Formation     |
|15255079 | Fadura-Formation | Fadura-Formation     |
|15255080 | Pfävigrat-Formation | Pfävigrat-Formation     |
|15255081 | Sassauna-Formation | Sassauna-Formation     |
|15255082 | Valzeina-Formation | Valzeina-Formation     |
|15255083 | Klus-Formation | Klus-Formation     |
|15255084 | Arblatsch-Flysch | Arblatsch-Flysch     |
|15255085 | Spegnas-Formation | Spegnas-Formation     |
|15255086 | Rudnal-Formation | Rudnal-Formation     |
|15255087 | Savognin-Formation | Savognin-Formation     |
|15255088 | Roz-Schiefer | Roz-Schiefer     |
|15255089 | Truche-Brekzie | Truche-Brekzie     |
|15255090 | Trom-Brekzie | Trom-Brekzie     |
|15255091 | Exergillod-Brekzie | Exergillod-Brekzie     |
|15255092 | Troublon-Kalk | Troublon-Kalk     |
|15255093 | Zünegg-Knollenkalk | Zünegg-Knollenkalk     |
|15255094 | Hauta-Crêtaz-Formation | Hauta-Crêtaz-Formation     |
|15255095 | Pointe-de-l&#39;Au-Brekzie | Pointe-de-l&#39;Au-Brekzie     |
|15255096 | Bonaveau-Kalk | Bonaveau-Kalk     |
|15255097 | Sex-du-Tronc-Kalk | Sex-du-Tronc-Kalk     |
|15255098 | Grand-Herba-Kalk | Grand-Herba-Kalk     |
|15255099 | Coulaytes-Melange | Coulaytes-Melange     |
|15255100 | Buufal-Konglomerat | Buufal-Konglomerat     |
|15255101 | Cuvigne-Derrey-Formation | Cuvigne-Derrey-Formation     |
|15255102 | Chenaux-Rouges-Formation | Chenaux-Rouges-Formation     |
|15255103 | Hochmatt-Kalkarenit | Hochmatt-Kalkarenit     |
|15255104 | Chenaux-Rouges-Mineralkruste | Chenaux-Rouges-Mineralkruste     |
|15255105 | Forclettes-Formation | Forclettes-Formation     |
|15255106 | Roter-Sattel-Hartgrund | Roter-Sattel-Hartgrund     |
|15255107 | Beaumont-Konglomerat | Beaumont-Konglomerat     |
|15255108 | Rayes-Kalk | Rayes-Kalk     |
|15255109 | Pissot-Member | Pissot-Member     |
|15255110 | Rote-Platte-Formation | Rote-Platte-Formation     |
|15255111 | Wildenbach-Member | Wildenbach-Member     |
|15255112 | Pra-du-Pont-Hartgrund | Pra-du-Pont-Hartgrund     |
|15255113 | Rontins-Member | Rontins-Member     |
|15255114 | Allières-Member | Allières-Member     |
|15255115 | Gérignoz-Kalk | Gérignoz-Kalk     |
|15253220 | Intschi-Formation | Intschi-Formation     |
|15253221 | Windgällen-Formation | Windgällen-Formation     |
|15253222 | Bifertengrätli-Formation | Bifertengrätli-Formation     |
|15253223 | Sandalp-Rhyolith | Sandalp-Rhyolith     |
|15253224 | «Lakustrisches Member» (Bifertengrätli-Fm.) | «Lakustrisches Member» (Bifertengrätli-Fm.)     |
|15253225 | «Estuarisches Member» (Bifertengrätli-Fm.) | «Estuarisches Member» (Bifertengrätli-Fm.)     |
|15253226 | Grünhorn-Member | Grünhorn-Member     |
|15253227 | «Basales Konglomerat» (Bifertengrätli-Fm.) | «Basales Konglomerat» (Bifertengrätli-Fm.)     |
|15253228 | Diechtergletscher-Formation | Diechtergletscher-Formation     |
|15253229 | Maasplanggstock-Metaandesit | Maasplanggstock-Metaandesit     |
|15253230 | Garwiidi-Diorit | Garwiidi-Diorit     |
|15253231 | Tscharren-Formation | Tscharren-Formation     |
|15253232 | Rinderbiel-Mikrogranit | Rinderbiel-Mikrogranit     |
|15253233 | Voralp-Granit | Voralp-Granit     |
|15253234 | Brunni-Granit | Brunni-Granit     |
|15253235 | Munt-Dado-Granit | Munt-Dado-Granit     |
|15253236 | Bugnei-Granodiorit | Bugnei-Granodiorit     |
|15253237 | Düssi-Diorit | Düssi-Diorit     |
|15253238 | Schöllenen-Diorit | Schöllenen-Diorit     |
|15253239 | Rossplatten-Diorit | Rossplatten-Diorit     |
|15253240 | Dammagletscher-Diorit | Dammagletscher-Diorit     |
|15253241 | Bristenstock-Syenit | Bristenstock-Syenit     |
|15253242 | Tödi-Granit | Tödi-Granit     |
|15253243 | Pardatschas-Granit | Pardatschas-Granit     |
|15253244 | Giuv-Syenit | Giuv-Syenit     |
|15253245 | Curtin-Monzodiorit | Curtin-Monzodiorit     |
|15253246 | Val-da-Surplattas-Diorit | Val-da-Surplattas-Diorit     |
|15253247 | Alp-Crap-Ner-Granit | Alp-Crap-Ner-Granit     |
|15253248 | Russein-Diorit | Russein-Diorit     |
|15253249 | Val-Gliems-Formation | Val-Gliems-Formation     |
|15253250 | Bifertenfirn-Formation | Bifertenfirn-Formation     |
|15253251 | Gastern-Granit | Gastern-Granit     |
|15253252 | Innertkirchen-Migmatit | Innertkirchen-Migmatit     |
|15253253 | Zäsenberg-Gneis | Zäsenberg-Gneis     |
|15253254 | Erstfeld-Gneiskomplex | Erstfeld-Gneiskomplex     |
|15253255 | Guttannen-Gneiskomplex | Guttannen-Gneiskomplex     |
|15253256 | Lötschental-Gneiskomplex | Lötschental-Gneiskomplex     |
|15253257 | Ofenhorn-Stampfhorn-Gneiskomplex | Ofenhorn-Stampfhorn-Gneiskomplex     |
|15253258 | Straligenstöckli-Gneiskomplex | Straligenstöckli-Gneiskomplex     |
|15253259 | Chrüzlistock-Migmatit | Chrüzlistock-Migmatit     |
|15253260 | Piz-Cuolmet-Gneiskomplex | Piz-Cuolmet-Gneiskomplex     |
|15253261 | Tamina-Gneiskomplex | Tamina-Gneiskomplex     |
|15253262 | Bäregg-Gneiskomplex | Bäregg-Gneiskomplex     |
|15253263 | Baltschieder-Granodiorit | Baltschieder-Granodiorit     |
|15253264 | Gärsthorn-Gneiskomplex | Gärsthorn-Gneiskomplex     |
|15253265 | Bitschji-Augengneis | Bitschji-Augengneis     |
|15253266 | Geimen-Augengneis | Geimen-Augengneis     |
|15253267 | Engi-Granit | Engi-Granit     |
|15253268 | Massa-Gneiskomplex | Massa-Gneiskomplex     |
|15253269 | Sogn-Placi-Gneiskomplex | Sogn-Placi-Gneiskomplex     |
|15253270 | Pulanera-Gneiskomplex | Pulanera-Gneiskomplex     |
|15253271 | Punteglias-Granit | Punteglias-Granit     |
|15253272 | Posta-Biala-Granit | Posta-Biala-Granit     |
|15253273 | Val-Punteglias-Diorit | Val-Punteglias-Diorit     |
|15253274 | Piz-Ner-Granit | Piz-Ner-Granit     |
|15253275 | Torrenthorn-Formation | Torrenthorn-Formation     |
|15253276 | Torrentalp-Member | Torrentalp-Member     |
|15253277 | Galm-Member | Galm-Member     |
|15253278 | Bachalp-Formation | Bachalp-Formation     |
|15253279 | Mättental-Melange | Mättental-Melange     |
|15253280 | Schabell-Melange | Schabell-Melange     |
|15253281 | Blattengrat-Sandstein | Blattengrat-Sandstein     |
|15253282 | Martinsmad-Formation | Martinsmad-Formation     |
|15253283 | «Supraquarzitischer Flysch» (Martinsmad-Fm.) | «Supraquarzitischer Flysch» (Martinsmad-Fm.)     |
|15253284 | Suren-Flysch | Suren-Flysch     |
|15253285 | Sardona-Member | Sardona-Member     |
|15253286 | «Infraquarzitischer Flysch» (Martinsmad-Fm.) | «Infraquarzitischer Flysch» (Martinsmad-Fm.)     |
|15253287 | Pfäfers-Formation | Pfäfers-Formation     |
|15253288 | Kapfen-Formation | Kapfen-Formation     |
|15253289 | Schönbühl-Formation | Schönbühl-Formation     |
|15253290 | Kärpf-Formation | Kärpf-Formation     |
|15253291 | Kärpfgipfel-Sernifit | Kärpfgipfel-Sernifit     |
|15253292 | Fulen-Formation | Fulen-Formation     |
|15253293 | Karrenstock-Formation | Karrenstock-Formation     |
|15253294 | Glattmatt-Member | Glattmatt-Member     |
|15253295 | Fuggstock-Member | Fuggstock-Member     |
|15253296 | Murgtal-Formation | Murgtal-Formation     |
|15253297 | Chartegg-Member | Chartegg-Member     |
|15253298 | Rotberg-Sandstein | Rotberg-Sandstein     |
|15253299 | Seez-Member | Seez-Member     |
|15253300 | Gufelialp-Member | Gufelialp-Member     |
|15253301 | Mären-Formation | Mären-Formation     |
|15253302 | Grisch-Member | Grisch-Member     |
|15253303 | Hahnenstock-Keratophyr | Hahnenstock-Keratophyr     |
|15253304 | Sonnenberg-Horizonte | Sonnenberg-Horizonte     |
|15253305 | Chamseeli-Konglomerat | Chamseeli-Konglomerat     |
|15253306 | Foostock-Member | Foostock-Member     |
|15253307 | Üblital-Formation | Üblital-Formation     |
|15253308 | Val-Pigniu-Gneiskomplex | Val-Pigniu-Gneiskomplex     |
|15253309 | Calmut-Gneiskomplex | Calmut-Gneiskomplex     |
|15253310 | Rueras-Gneiskomplex | Rueras-Gneiskomplex     |
|15253311 | Meierhof-Phyllit | Meierhof-Phyllit     |
|15253312 | Waltensburg-Verrucano | Waltensburg-Verrucano     |
|15253313 | Ruinas-Sandstein | Ruinas-Sandstein     |
|15253314 | Corno-Gneis | Corno-Gneis     |
|15253315 | Winterhorn-Granit | Winterhorn-Granit     |
|15253316 | Cacciola-Granit | Cacciola-Granit     |
|15253317 | Rotondo-Granit | Rotondo-Granit     |
|15253318 | Prosa-Granit | Prosa-Granit     |
|15253319 | Val-Tremola-Granit | Val-Tremola-Granit     |
|15253320 | Sädelhorn-Diorit | Sädelhorn-Diorit     |
|15253321 | Gamsboden-Granit | Gamsboden-Granit     |
|15253322 | Fibbia-Granit | Fibbia-Granit     |
|15253323 | Medel-Granit | Medel-Granit     |
|15253324 | Cristallina-Granodiorit | Cristallina-Granodiorit     |
|15253325 | Uffiern-Diorit | Uffiern-Diorit     |
|15253326 | Alp-Cavradi-Gneiskomplex | Alp-Cavradi-Gneiskomplex     |
|15253327 | Borel-Gneiskomplex | Borel-Gneiskomplex     |
|15253328 | Tenelin-Gneiskomplex | Tenelin-Gneiskomplex     |
|15253329 | Laiets-Gneiskomplex | Laiets-Gneiskomplex     |
|15253330 | Giubine-Gneiskomplex | Giubine-Gneiskomplex     |
|15253331 | Tremola-Gneiskomplex | Tremola-Gneiskomplex     |
|15253332 | Pontino-Gneiskomplex | Pontino-Gneiskomplex     |
|15253333 | Nelva-Gneiskomplex | Nelva-Gneiskomplex     |
|15253334 | Sasso-Rosso-Gneiskomplex | Sasso-Rosso-Gneiskomplex     |
|15253335 | Prüsfa-Gneiskomplex | Prüsfa-Gneiskomplex     |
|15255174 | Andonces-Member | Andonces-Member     |
|15255175 | «Mittlere Rauhwacke» (St-Triphon-Fm.) | «Mittlere Rauhwacke» (St-Triphon-Fm.)     |
|15255176 | «Silex-Niveau» (St-Triphon-Fm.) | «Silex-Niveau» (St-Triphon-Fm.)     |
|15255177 | Lessus-Member | Lessus-Member     |
|15255178 | Dorchaux-Member | Dorchaux-Member     |
|15255179 | «Untere Rauhwacke» (St-Triphon-Fm.) | «Untere Rauhwacke» (St-Triphon-Fm.)     |
|15255180 | Griggeli-Formation | Griggeli-Formation     |
|15255181 | Mythen-Kieselkalk | Mythen-Kieselkalk     |
|15255182 | «Griggeli-Bank» | «Griggeli-Bank»     |
|15255183 | Gibel-Formation | Gibel-Formation     |
|15255184 | Rämsi-Member | Rämsi-Member     |
|15255185 | «Gibel-Member» | «Gibel-Member»     |
|15255186 | Steinberg-Konglomerat | Steinberg-Konglomerat     |
|15255187 | Musenalp-Member | Musenalp-Member     |
|15255188 | Stanserhorn-Formation | Stanserhorn-Formation     |
|15255189 | «Zoophycos-Schichten» (Stanserhorn-Fm.) | «Zoophycos-Schichten» (Stanserhorn-Fm.)     |
|15255190 | Spis-Kalk | Spis-Kalk     |
|15255191 | «Posidonienschiefer» (Stanserhorn-Fm.) | «Posidonienschiefer» (Stanserhorn-Fm.)     |
|15255192 | Obflue-Formation | Obflue-Formation     |
|15255193 | Brand-Formation | Brand-Formation     |
|15255194 | Horngraben-Formation | Horngraben-Formation     |
|15255195 | Lückengraben-Formation | Lückengraben-Formation     |
|15255196 | Zwischenmythen-Mergel | Zwischenmythen-Mergel     |
|15255197 | Mattes-Melange | Mattes-Melange     |
|15255198 | Chumi-Formation | Chumi-Formation     |
|15255199 | Joux-Verte-Formation | Joux-Verte-Formation     |
|15255200 | Bonave-Formation | Bonave-Formation     |
|15255201 | «Obere Brekzie» (Brekzien-Decke) | «Obere Brekzie» (Brekzien-Decke)     |
|15255202 | «Obere Schiefer» (Brekzien-Decke) | «Obere Schiefer» (Brekzien-Decke)     |
|15255203 | «Untere Brekzie» (Brekzien-Decke) | «Untere Brekzie» (Brekzien-Decke)     |
|15255204 | «Untere Schiefer» (Brekzien-Decke) | «Untere Schiefer» (Brekzien-Decke)     |
|15255205 | «Untere Kalke» (Brekzien-Decke) | «Untere Kalke» (Brekzien-Decke)     |
|15255206 | «Infrabrèche-Melange» | «Infrabrèche-Melange»     |
|15255207 | Ricard-Rhyolit | Ricard-Rhyolit     |
|15255208 | Printse-Formation | Printse-Formation     |
|15255209 | Chandoline-Sandstein | Chandoline-Sandstein     |
|15255210 | Gälmji-Gneis | Gälmji-Gneis     |
|15255211 | Scherbadung-Gabbro | Scherbadung-Gabbro     |
|15255212 | Moncucco-Peridotit | Moncucco-Peridotit     |
|15255213 | Mont-Brûlé-Quarzit | Mont-Brûlé-Quarzit     |
|15255214 | Plan-Palasuit-Konglomerat | Plan-Palasuit-Konglomerat     |
|15255215 | Ruitor-Gneiskomplex | Ruitor-Gneiskomplex     |
|15255216 | Lacerandes-Augengneis | Lacerandes-Augengneis     |
|15255217 | Mont-Mort-Metapelit | Mont-Mort-Metapelit     |
|15255218 | Törbel-Gneis | Törbel-Gneis     |
|15255219 | Stalden-Gneis | Stalden-Gneis     |
|15255220 | Ahorn-Augengneiss | Ahorn-Augengneiss     |
|15255221 | Berisal-Gneiskomplex | Berisal-Gneiskomplex     |
|15255222 | Brunnegjoch-Metabauxit | Brunnegjoch-Metabauxit     |
|15255223 | Bruneggjoch-Formation | Bruneggjoch-Formation     |
|15255224 | Sous-le-Rocher-Member | Sous-le-Rocher-Member     |
|15255225 | Embd-Member | Embd-Member     |
|15255226 | Randa-Augengneis | Randa-Augengneis     |
|15255227 | Oberems-Albitgneis | Oberems-Albitgneis     |
|15255228 | Bonigersee-Augengneis | Bonigersee-Augengneis     |
|15255229 | Col-de-Chassoure-Formation | Col-de-Chassoure-Formation     |
|15255230 | Gouille-Verte-Member | Gouille-Verte-Member     |
|15256008 | «Série Rubanée» | «Série Rubanée»     |
|15256009 | Mont-Collon-Gabbro | Mont-Collon-Gabbro     |
|15256010 | Sassa-Metagabbro | Sassa-Metagabbro     |
|15256011 | Berrio-Gabbro | Berrio-Gabbro     |
|15256012 | Tête-de-Valpelline-Phyllit | Tête-de-Valpelline-Phyllit     |
|15256013 | Maia-Metagabbro | Maia-Metagabbro     |
|15256014 | Losone-Schiefer | Losone-Schiefer     |
|15256015 | Maloja-Orthogneis | Maloja-Orthogneis     |
|15256016 | Fedoz-Metagabbro | Fedoz-Metagabbro     |
|15256017 | Maloja-Gneiskomplex | Maloja-Gneiskomplex     |
|15256018 | Fedoz-Gneiskomplex | Fedoz-Gneiskomplex     |
|15256019 | Musella-Granit | Musella-Granit     |
|15256020 | Sella-Granodiorit | Sella-Granodiorit     |
|15256021 | Marinelli-Formation | Marinelli-Formation     |
|15257001 | God-Drosa-Flysch | God-Drosa-Flysch     |
|15257002 | Clavadatsch-Brekzie | Clavadatsch-Brekzie     |
|15257003 | Chanèls-Formation | Chanèls-Formation     |
|15257004 | Emmat-Formation | Emmat-Formation     |
|15257005 | Russenna-Formation | Russenna-Formation     |
|15257006 | Blais-Radiolarit | Blais-Radiolarit     |
|15257007 | Plattas-Member | Plattas-Member     |
|15257008 | Saluver-Formation | Saluver-Formation     |
|15257009 | Allgäu-Formation | Allgäu-Formation     |
|15257010 | Mezzaun-Member | Mezzaun-Member     |
|15257011 | Blaisun-Member | Blaisun-Member     |
|15257012 | Trupchun-Member | Trupchun-Member     |
|15257013 | Chaschauna-Brekzie | Chaschauna-Brekzie     |
|15257014 | Agnelli-Formation | Agnelli-Formation     |
|15257015 | Alv-Brekzie | Alv-Brekzie     |
|15257016 | Kössen-Formation | Kössen-Formation     |
|15257017 | Zirmenkopf-Kalk | Zirmenkopf-Kalk     |
|15257018 | Mitgel-Member | Mitgel-Member     |
|15257019 | Ramoz-Member | Ramoz-Member     |
|15257020 | Schesaplana-Member | Schesaplana-Member     |
|15257021 | Alplihorn-Member | Alplihorn-Member     |
|15257022 | Murtèr-Plattenkalk | Murtèr-Plattenkalk     |
|15257023 | Uglix-Plattenkalk | Uglix-Plattenkalk     |
|15257024 | Murteret-Dolomit | Murteret-Dolomit     |
|15257025 | Diavel-Formation | Diavel-Formation     |
|15257026 | Quattervals-Formation | Quattervals-Formation     |
|15257027 | Crappa-Mala-Mergel | Crappa-Mala-Mergel     |
|15257028 | Pra-Grata-Member | Pra-Grata-Member     |
|15257029 | Müschauns-Dolomit | Müschauns-Dolomit     |
|15257030 | Fanez-Formation | Fanez-Formation     |
|15257031 | Valbella-Member | Valbella-Member     |
|15257032 | Stugl-Gips | Stugl-Gips     |
|15257033 | Mezdi-Member | Mezdi-Member     |
|15257034 | Cluozza-Member | Cluozza-Member     |
|15257035 | Minger-Formation | Minger-Formation     |
|15257036 | Mora-Member | Mora-Member     |
|15257037 | Döss-Radond-Vulkanite | Döss-Radond-Vulkanite     |
|15257038 | Altein-Formation | Altein-Formation     |
|15257039 | Parai-Alba-Member | Parai-Alba-Member     |
|15257040 | Prosanto-Formation | Prosanto-Formation     |
|15257041 | Vallatscha-Formation | Vallatscha-Formation     |
|15257042 | Tiaun-Brekzie | Tiaun-Brekzie     |
|15257043 | Turettas-Member | Turettas-Member     |
|15257044 | Landwasser-Member | Landwasser-Member     |
|15257045 | Lavinèr-Brekzie | Lavinèr-Brekzie     |
|15257046 | Garone-Formation | Garone-Formation     |
|15257047 | S-charl-Formation | S-charl-Formation     |
|15257048 | Sertig-Member | Sertig-Member     |
|15257049 | Ravais-ch-Member | Ravais-ch-Member     |
|15257050 | Ducan-Formation | Ducan-Formation     |
|15257051 | «Trochitendolomit-Member» | «Trochitendolomit-Member»     |
|15257052 | «Brachiopodenkalk-Member» | «Brachiopodenkalk-Member»     |
|15257053 | «Eisendolomit-Member» | «Eisendolomit-Member»     |
|15257054 | «Gracilis-Member» | «Gracilis-Member»     |
|15257055 | Fuorn-Formation | Fuorn-Formation     |
|15257056 | Punt-la-Drossa-Member | Punt-la-Drossa-Member     |
|15257057 | «Pflanzenquarzit» | «Pflanzenquarzit»     |
|15257058 | Chazforà-Formation | Chazforà-Formation     |
|15257059 | Tuors-Member | Tuors-Member     |
|15257060 | Val-Püra-Member | Val-Püra-Member     |
|15257061 | Ruina-Formation | Ruina-Formation     |
|15257062 | Sandhubel-Member | Sandhubel-Member     |
|15257063 | Bellaluna-Member | Bellaluna-Member     |
|15257064 | Piz-Trovat-Metarhyolit | Piz-Trovat-Metarhyolit     |
|15257065 | Sass-Queder-Metarhyolith | Sass-Queder-Metarhyolith     |
|15257066 | Nair-Porphyroid | Nair-Porphyroid     |
|15257067 | Lavatèra-Brekzie | Lavatèra-Brekzie     |
|15257068 | Varaina-Schiefer | Varaina-Schiefer     |
|15257069 | «Sprenkelschiefer» | «Sprenkelschiefer»     |
|15257070 | Tschima-da-Flix-Granit | Tschima-da-Flix-Granit     |
|15257071 | Parait-Chavagl-Granit | Parait-Chavagl-Granit     |
|15257072 | Celerina-Orthogneis | Celerina-Orthogneis     |
|15257073 | Plasseggen-Augengneis | Plasseggen-Augengneis     |
|15257074 | Dorfberg-Gneis | Dorfberg-Gneis     |
|15257075 | Augsten-Brekzie | Augsten-Brekzie     |
|15257076 | Sasso-Rosso-Granodiorit | Sasso-Rosso-Granodiorit     |
|15257077 | Morteratsch-Serpentinit | Morteratsch-Serpentinit     |
|15257078 | La-Rösa-Orthogneis | La-Rösa-Orthogneis     |
|15257079 | Val-Rude-Orthogneis | Val-Rude-Orthogneis     |
|15257080 | Carale-Schiefer | Carale-Schiefer     |
|15257081 | Julier-Granodiorit | Julier-Granodiorit     |
|15257082 | Err-Brekzie | Err-Brekzie     |
|15257083 | Salamun-Brekzie | Salamun-Brekzie     |
|15257084 | Vaüglia-Granodiorit | Vaüglia-Granodiorit     |
|15257085 | Err-Granodiorit | Err-Granodiorit     |
|15257086 | Salteras-Formation | Salteras-Formation     |
|15257087 | Corvatsch-Granodiorit | Corvatsch-Granodiorit     |
|15257088 | Bardella-Formation | Bardella-Formation     |
|15257089 | Corno-di-Campo-Granodiorit | Corno-di-Campo-Granodiorit     |
|15257090 | Campocologno-Gabbro | Campocologno-Gabbro     |
|15257091 | Tonale-Schiefer | Tonale-Schiefer     |
|15257092 | Lech-Formation | Lech-Formation     |
|15257093 | Ammergau-Formation | Ammergau-Formation     |
|15257094 | Ruhpolding-Formation | Ruhpolding-Formation     |
|15257095 | Arlberg-Formation | Arlberg-Formation     |
|15257096 | Partnach-Formation | Partnach-Formation     |
|15257097 | Reiflingen-Formation | Reiflingen-Formation     |
|15257098 | Gutenstein-Formation | Gutenstein-Formation     |
|15257099 | Reichenhall-Formation | Reichenhall-Formation     |
|15257100 | Präbichl-Formation | Präbichl-Formation     |
|15257101 | Flüela-Augengneis | Flüela-Augengneis     |
|15257102 | Tschuggen-Augengneis | Tschuggen-Augengneis     |
|15257103 | Forun-Augengneis | Forun-Augengneis     |
|15257104 | Kesch-Augengneis | Kesch-Augengneis     |
|15257105 | Güstizia-Gneis | Güstizia-Gneis     |
|15257106 | Mönchalp-Augengneis | Mönchalp-Augengneis     |
|15257107 | Sesvenna-Augengneis | Sesvenna-Augengneis     |
|15258001 | Castel-di-Sotto-Ton | Castel-di-Sotto-Ton     |
|15258002 | Pontegana-Konglomerat | Pontegana-Konglomerat     |
|15258003 | Lucino-Konglomerat | Lucino-Konglomerat     |
|15258004 | Cagno-Sandstein | Cagno-Sandstein     |
|15258005 | Como-Konglomerat | Como-Konglomerat     |
|15258006 | Malnate-Sandstein | Malnate-Sandstein     |
|15258007 | Val-Grande-Sandstein | Val-Grande-Sandstein     |
|15258008 | Rio-dei-Gioghi-Pelite | Rio-dei-Gioghi-Pelite     |
|15258009 | Prestino-Pelite | Prestino-Pelite     |
|15258010 | Chiasso-Formation | Chiasso-Formation     |
|15258011 | Villa-Olmo-Konglomerat | Villa-Olmo-Konglomerat     |
|15258012 | Ternate-Formation | Ternate-Formation     |
|15258013 | Brenno-Formation | Brenno-Formation     |
|15258014 | Prella-Konglomerat | Prella-Konglomerat     |
|15258015 | Bergamo-Flysch | Bergamo-Flysch     |
|15258016 | Coldrerio-Flysch | Coldrerio-Flysch     |
|15258017 | Torre-Konglomerat | Torre-Konglomerat     |
|15258018 | Varesotto-Flysch | Varesotto-Flysch     |
|15258019 | Pontida-Formation | Pontida-Formation     |
|15258020 | «Scaglia Rossa Lombarda» | «Scaglia Rossa Lombarda»     |
|15258021 | «Scaglia Bianca Lombarda» | «Scaglia Bianca Lombarda»     |
|15258022 | «Scaglia Variegata Lombarda» | «Scaglia Variegata Lombarda»     |
|15258023 | «Maiolica Lombarda» | «Maiolica Lombarda»     |
|15258024 | «Selcifero Lombardo» | «Selcifero Lombardo»     |
|15258025 | «Rosso ad Aptici» | «Rosso ad Aptici»     |
|15258026 | «Calcare a bivalvi planctonici» | «Calcare a bivalvi planctonici»     |
|15258027 | «Rosso Ammonitico Lombardo» | «Rosso Ammonitico Lombardo»     |
|15258028 | «Grenzposidonienschichten» | «Grenzposidonienschichten»     |
|15258029 | Morbio-Formation | Morbio-Formation     |
|15258030 | Besazio-Kalk | Besazio-Kalk     |
|15258031 | Moltrasio-Formation | Moltrasio-Formation     |
|15258032 | Molino-Member | Molino-Member     |
|15258033 | Saltrio-Formation | Saltrio-Formation     |
|15258034 | «Macchia Vecchia» | «Macchia Vecchia»     |
|15258035 | Broccatello d&#39;Arzo | Broccatello d&#39;Arzo     |
|15258036 | Albenza-Formation | Albenza-Formation     |
|15258037 | Zu-Kalk | Zu-Kalk     |
|15258038 | Tremona-Formation | Tremona-Formation     |
|15258039 | «Brecce Retiche» | «Brecce Retiche»     |
|15258040 | Riva-di-Solto-Tonstein | Riva-di-Solto-Tonstein     |
|15258041 | «Dolomia Principale» | «Dolomia Principale»     |
|15258042 | Pizzella-Mergel | Pizzella-Mergel     |
|15258043 | Cunardo-Formation | Cunardo-Formation     |
|15258044 | Meride-Formation | Meride-Formation     |
|15258045 | «Kalkschieferzone» (Meride-Fm.) | «Kalkschieferzone» (Meride-Fm.)     |
|15258046 | «Dolomitband» (Meride-Fm.) | «Dolomitband» (Meride-Fm.)     |
|15258047 | Cassina-Bank | Cassina-Bank     |
|15258048 | «Cava Superiore» | «Cava Superiore»     |
|15258049 | «Cava Inferiore» | «Cava Inferiore»     |
|15258050 | San-Giorgio-Dolomit | San-Giorgio-Dolomit     |
|15258051 | Val-Serrata-Tuffite | Val-Serrata-Tuffite     |
|15258052 | Besano-Formation | Besano-Formation     |
|15258053 | San-Salvatore-Dolomit | San-Salvatore-Dolomit     |
|15258054 | Bellano-Formation | Bellano-Formation     |
|15258055 | «Servino» | «Servino»     |
|15258056 | Manno-Formation | Manno-Formation     |
|15258057 | Fornale-Gabbro | Fornale-Gabbro     |
|15258058 | Finero-Peridotit | Finero-Peridotit     |
|15258059 | Pizzo-Leone-Gneis | Pizzo-Leone-Gneis     |
|15258060 | San-Bernardo-Gneis | San-Bernardo-Gneis     |
|15258061 | Stabbiello-Gneis | Stabbiello-Gneis     |
|15258062 | Giumello-Gneis | Giumello-Gneis     |
|15258063 | Ceneri-Gneis | Ceneri-Gneis     |
|15259001 | Höwenegg-Basalt | Höwenegg-Basalt     |
|15259002 | Hohenwiel-Phonolith | Hohenwiel-Phonolith     |
|15259003 | Hegau-Tuffit | Hegau-Tuffit     |
|15259004 | Brand-Herrentisch-Tuffit | Brand-Herrentisch-Tuffit     |
|15259005 | Wangen-Tuffit | Wangen-Tuffit     |
|15259006 | Hohenolber-Tuffit | Hohenolber-Tuffit     |
|15259007 | Eichbol-Tuffit | Eichbol-Tuffit     |
|15259008 | Zocca-Aplit | Zocca-Aplit     |
|15259009 | Monte-Rosso-Mikrogranit | Monte-Rosso-Mikrogranit     |
|15259010 | Alpe-Cameraccio-Granodiorit | Alpe-Cameraccio-Granodiorit     |
|15259011 | Val-Masino-Granodiorit | Val-Masino-Granodiorit     |
|15259012 | Melirolo-Augengneis | Melirolo-Augengneis     |
|15259013 | Monte-Bassetta-Quarzdiorit | Monte-Bassetta-Quarzdiorit     |
|15259014 | Sorico-Tonalit | Sorico-Tonalit     |
|15259015 | Jorio-Tonalit | Jorio-Tonalit     |
|15259016 | San-Fedelino-Granit | San-Fedelino-Granit     |
|15255231 | Matse-Member | Matse-Member     |
|15255232 | Dent-de-Nendaz-Member | Dent-de-Nendaz-Member     |
|15255233 | Goli-d&#39;Aget-Member | Goli-d&#39;Aget-Member     |
|15255234 | Mondra-Member | Mondra-Member     |
|15255235 | Cleuson-Member | Cleuson-Member     |
|15255236 | Métailler-Formation | Métailler-Formation     |
|15255237 | Louvie-Gabbro | Louvie-Gabbro     |
|15255238 | Distulberg-Formation | Distulberg-Formation     |
|15255239 | Thyon-Metagranophyr | Thyon-Metagranophyr     |
|15255240 | Mont-Rogneux-Metagranit | Mont-Rogneux-Metagranit     |
|15255241 | Lirec-Formation | Lirec-Formation     |
|15255242 | Adlerflüe-Formation | Adlerflüe-Formation     |
|15255243 | Minugrat-Eklogit | Minugrat-Eklogit     |
|15255244 | Ergischhorn-Komplex | Ergischhorn-Komplex     |
|15255245 | Brändjispitz-Metagabbro | Brändjispitz-Metagabbro     |
|15255246 | Ginals-Gneis | Ginals-Gneis     |
|15255247 | Böshorn-Gneis | Böshorn-Gneis     |
|15255248 | «Série-Rousse» | «Série-Rousse»     |
|15255249 | Portjengrat-Orthogneis | Portjengrat-Orthogneis     |
|15255250 | Saas-Fee-Augengneis | Saas-Fee-Augengneis     |
|15255251 | Almagelhorn-Migmatit | Almagelhorn-Migmatit     |
|15255252 | Weissmies-Paragneis | Weissmies-Paragneis     |
|15255253 | Preja-Formation | Preja-Formation     |
|15255254 | Cavalli-Formation | Cavalli-Formation     |
|15255255 | Mezzalama-Granit | Mezzalama-Granit     |
|15255256 | Monte-Rosa-Orthogneis  | Monte-Rosa-Orthogneis      |
|15255257 | Macugnaga-Augengneis | Macugnaga-Augengneis     |
|15255258 | Rottal-Migmatit | Rottal-Migmatit     |
|15255259 | Stellihorn-Mylonit | Stellihorn-Mylonit     |
|15255260 | Truzzo-Granit | Truzzo-Granit     |
|15255261 | Roffna-Gneis | Roffna-Gneis     |
|15255262 | Timun-Gneiskomplex | Timun-Gneiskomplex     |
|15255263 | Gelbhorn-Flysch | Gelbhorn-Flysch     |
|15255264 | Obrist-Formation | Obrist-Formation     |
|15255265 | Vizan-Brekzie | Vizan-Brekzie     |
|15255266 | Tschera-Marmor | Tschera-Marmor     |
|15255267 | Wissberg-Brekzie | Wissberg-Brekzie     |
|15255268 | Nisellas-Formation | Nisellas-Formation     |
|15255269 | Tumpriv-Formation | Tumpriv-Formation     |
|15255270 | Solis-Kalk | Solis-Kalk     |
|15255271 | Kalkberg-Formation | Kalkberg-Formation     |
|15255272 | Bavugls-Formation | Bavugls-Formation     |
|15255273 | Taspegn-Gneis | Taspegn-Gneis     |
|15255274 | Burgruinen-Gneis | Burgruinen-Gneis     |
|15255275 | Vignun-Gneis | Vignun-Gneis     |
|15255276 | Areua-Bruschghorn-Melange | Areua-Bruschghorn-Melange     |
|15255277 | «Globorotalien-Schichten» | «Globorotalien-Schichten»     |
|15255278 | «Quarzsandstein-Flysch» | «Quarzsandstein-Flysch»     |
|15255279 | Tristel-Formation | Tristel-Formation     |
|15255280 | «Fleckenkalk-Flysch» | «Fleckenkalk-Flysch»     |
|15255281 | Jes-Formation | Jes-Formation     |
|15255282 | Falknis-Brekzie | Falknis-Brekzie     |
|15255283 | Sanalada-Formation | Sanalada-Formation     |
|15255284 | Panier-Formation | Panier-Formation     |
|15255285 | Sulzfluh-Kalk | Sulzfluh-Kalk     |
|15255286 | Minschun-Brekzie (Tasna) | Minschun-Brekzie (Tasna)     |
|15255287 | Steinsberg-Kalk | Steinsberg-Kalk     |
|15255288 | Plattamala-Granit | Plattamala-Granit     |
|15255289 | Hundsrügg-Formation | Hundsrügg-Formation     |
|15255290 | Perrières-Formation | Perrières-Formation     |
|15255291 | Gets-Ophiolith | Gets-Ophiolith     |
|15255292 | Rodomonts-Formation | Rodomonts-Formation     |
|15255293 | Mocausa-Nagelfluh | Mocausa-Nagelfluh     |
|15255294 | Tissota-Melange | Tissota-Melange     |
|15255295 | Gueyraz-Komplex | Gueyraz-Komplex     |
|15255296 | «Foraminiferenschichten» (Tissota-Melange) | «Foraminiferenschichten» (Tissota-Melange)     |
|15255297 | «Aptychenkalk» (Tissota-Melange) | «Aptychenkalk» (Tissota-Melange)     |
|15255298 | «Radiolarit» (Tissota-Melange) | «Radiolarit» (Tissota-Melange)     |
|15255299 | «Filamentkalk» (Tissota-Melange) | «Filamentkalk» (Tissota-Melange)     |
|15255300 | «Spatkalk» (Tissota-Melange) | «Spatkalk» (Tissota-Melange)     |
|15255301 | Manche-Formation | Manche-Formation     |
|15255302 | Weissenburg-Flysch | Weissenburg-Flysch     |
|15255303 | Lamperehubel-Sandstein | Lamperehubel-Sandstein     |
|15255304 | Fouyet-Formation | Fouyet-Formation     |
|15255305 | Biot-Formation | Biot-Formation     |
|15255306 | Colerin-Konglomerat | Colerin-Konglomerat     |
|15255307 | Chétillon-Formation | Chétillon-Formation     |
|15255308 | Estavannens-Flysch | Estavannens-Flysch     |
|15255309 | Reidigen-Formation | Reidigen-Formation     |
|15255310 | Loranco-Amphibolit | Loranco-Amphibolit     |
|15255311 | Andolla-Eklogit | Andolla-Eklogit     |
|15255312 | Riffelberg-Melange | Riffelberg-Melange     |
|15255313 | Pfulwe-Metabasalt | Pfulwe-Metabasalt     |
|15255314 | Allalin-Gabbro | Allalin-Gabbro     |
|15255315 | Breithorn-Serpentinit | Breithorn-Serpentinit     |
|15255316 | «Série Grise» | «Série Grise»     |
|15255317 | Garda-Bordon-Formation | Garda-Bordon-Formation     |
|15255318 | Fêta-d&#39;Août-Formation | Fêta-d&#39;Août-Formation     |
|15255319 | Chanrion-Radiolarit | Chanrion-Radiolarit     |
|15255320 | Mont-des-Ritzes-Metabasalt | Mont-des-Ritzes-Metabasalt     |
|15255321 | Aiguilles-Rouges-d&#39;Arolla-Metagabbro | Aiguilles-Rouges-d&#39;Arolla-Metagabbro     |
|15255322 | Serra-Neire-Serpentinit | Serra-Neire-Serpentinit     |
|15255323 | Torrembey-Brekzie | Torrembey-Brekzie     |
|15255324 | Muretto-Quarzit | Muretto-Quarzit     |
|15255325 | Rossi-Formation | Rossi-Formation     |
|15255326 | Lizun-Prasinit | Lizun-Prasinit     |
|15255327 | Forno-Amphibolit | Forno-Amphibolit     |
|15255328 | Ur-Brekzie | Ur-Brekzie     |
|15255329 | Malenco-Serpentinit | Malenco-Serpentinit     |
|15255330 | Flix-Schichten | Flix-Schichten     |
|15255331 | Falotta-Radiolarit | Falotta-Radiolarit     |
|15255332 | «Cenomanbrekzien-Serie» | «Cenomanbrekzien-Serie»     |
|15255333 | Bettlerjoch-Brekzie | Bettlerjoch-Brekzie     |
|15255334 | Bargella-Brekzie | Bargella-Brekzie     |
|15255335 | Verspala-Formation | Verspala-Formation     |
|15255336 | Alpbach-Schiefer | Alpbach-Schiefer     |
|15255337 | Lavagna-Formation | Lavagna-Formation     |
|15255338 | «Palombini-Formation» | «Palombini-Formation»     |
|15255339 | Maran-Brekzie | Maran-Brekzie     |
|15255340 | Haupter-Brekzie | Haupter-Brekzie     |
|15255341 | Totalp-Serpentinit | Totalp-Serpentinit     |
|15256001 | Matterhorn-Gabbro | Matterhorn-Gabbro     |
|15256002 | Grand-Dolin-Brekzie | Grand-Dolin-Brekzie     |
|15256003 | Petit-Dolin-Kalkbrekzie | Petit-Dolin-Kalkbrekzie     |
|15256004 | Mont-Morion-Granit | Mont-Morion-Granit     |
|15256005 | Pointe-d&#39;Otemma-Granodiorit | Pointe-d&#39;Otemma-Granodiorit     |
|15256006 | Bouquetins-Quarzdiorit | Bouquetins-Quarzdiorit     |
|15256007 | Arolla-Orthogneis | Arolla-Orthogneis     |









## Annexe  GC_LITSTRAT_UNCO_CD {#gc-litstrat-unco-cd}
Table des valeurs des unités lithostratigraphiques

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15201001 | Ältere Ablagerungen, undifferenziert | Dépôts indifférenciés précédant le Dernier Maximum Glaciaire     |
|15201002 | Niederterrasse | Niederterrasse     |
|15201003 | Hochterrasse | Hochterrasse     |
|15201004 | Tiefere Deckenschotter | Tiefere Deckenschotter     |
|15201005 | Höhere Deckenschotter | Höhere Deckenschotter     |
|15201006 | Birrfeld-Eiszeit (Letzte Eiszeit) | Période glaciaire du Birrfeld (Dernière Période glaciaire)     |
|15201007 | Last Glacial Maximum (LGM), undiff. | Dernier Maximum Glaciaire (LGM), indifférencié     |
|15201008 | LGM-Rückzug | Phase de retrait du LGM     |
|15201009 | Birmenstorf-Vergletscherung (2. LGM-Vorstoss) | Glaciation de Birmenstorf     |
|15201010 | Wettingen-Vorstoss | Avancée glaciaire de Wettingen     |
|15201011 | Flüefeld-Schotter | Gravier du Flüefeld     |
|15201012 | Altberg-Till | Till de l&#39;Altberg     |
|15201013 | Birmenstorf-Vorstoss | Avancée glaciaire de Birmenstorf     |
|15201014 | Birr-Schotter | Gravier de Birr     |
|15201015 | Oberhard-Till | Till d&#39;Oberhard     |
|15201016 | Seon-Vorstoss | Avancée glaciaire de Seon     |
|15201017 | Berg-Schotter | Gravier de Berg     |
|15201018 | Fornholz-Till | Till de Fornholz     |
|15201019 | Gontenschwil-Vorstoss | Avancée glaciaire de Gontenschwil     |
|15201020 | Gontenschwil-Till | Till de Gontenschwil     |
|15201021 | Staffelbach-Vorstoss | Avancée glaciaire de Staffelbach     |
|15201022 | Staffelbach-Schotter | Gravier de Staffelbach     |
|15201023 | Staffelbach-Till | Till de Staffelbach     |
|15201024 | Lindmühle-Vergletscherung (1. LGM-Vorstoss) | Glaciation de Lindmühle     |
|15201025 | Otelfingen-Vorstoss | Avancée glaciaire d&#39;Otelfingen     |
|15201026 | Tägerhard-Schotter | Gravier de Tägerhard     |
|15201027 | Lindmühle-Vorstoss | Avancée glaciaire du Lindmühle     |
|15201028 | Ämmert-Schotter | Gravier d&#39;Ämmert     |
|15201029 | Ämmert-Till | Till d&#39;Ämmert     |
|15201030 | Emmet-Vorstoss | Avancée glaciaire d&#39;Emmet     |
|15201031 | Gündelmoos-Lehm | Limon de Gündelmoos     |
|15201032 | Igliste-Schotter | Gravier d&#39;Igliste     |
|15201033 | Niderholz-Till | Till du Niderholz     |
|15201034 | Zetzwil-Vorstoss | Avancée glaciaire de Zetzwil     |
|15201035 | Zetzwil-Till | Till de Zetzwil     |
|15201036 | Kirchleerau-Vorstoss | Avancée glaciaire de Kirchleerau     |
|15201037 | Kirchleerau-Till | Till de Kirchleerau     |
|15201038 | Gossau-Interstadial | Interstade de Gossau     |
|15201039 | Mülligen-Paläoboden | Paléosol de Mülligen     |
|15201040 | Niederweningen-Formation | Formation de Niederweningen     |
|15201041 | Hombrechtikon-Vergletscherung (Frühletzteiszeitliche Vergl.) | Glaciation de Hombrechtikon     |
|15201042 | Mülligen-Schotter | Gravier de Mülligen     |
|15201043 | 2. letzteiszeitlischs Vorstoss | 2ème avancée glaciaire de la Dernière Période glaciaire     |
|15201044 | 1. letzteiszeitlischs Vorstoss | 1ère avancée glaciaire de la Dernière Période glaciaire     |
|15201045 | Klettgau-Schotter | Gravier du Klettgau     |
|15201046 | Obere Klettgauschotter | Gravier supérieur du Klettgau     |
|15201047 | Glazi-lakustrische Serie | Série glaciolacustre (Gravier du Klettgau)     |
|15201048 | Mittlere Klettgauschotter | Gravier moyen du Klettgau     |
|15201049 | Untere Klettgauschotter | Gravier inférieur du Klettgau     |
|15201050 | Gondiswil-Interglazial (Letztes Interglazial) | Interglaciaire de Gondiswil (Dernier Interglaciaire)     |
|15201051 | Flurlingen-Quelltuff | Tuf calcaire de Flurlingen     |
|15201052 | Birrfeld- und Klettgau-Paläoböden | Paléosols du Birrfeld et du Klettgau     |
|15201053 | Beringen-Eiszeit | Période glaciaire de Beringen (Avant-dernière Période glaciaire)     |
|15201054 | Entfelden-Schotter | Gravier d&#39;Entfelden     |
|15201055 | Aarau-Schotter | Gravier d&#39;Aarau     |
|15201056 | Suhr-Schotter | Gravier de Suhr     |
|15201057 | Veltheim-Schotter | Gravier de Veltheim     |
|15201058 | Stüsslingen-Schotter | Gravier de Stüsslingen     |
|15201059 | Langwiesen-Vergletscherung | Glaciation de Langwiesen     |
|15201060 | Langwiesen-Vorstoss | Avancée glaciaire de Langwiesen     |
|15201061 | Schaffhausen-Schotter | Gravier de Schaffhouse     |
|15201062 | Reuenthal-Vorstoss | Avancée glaciaire de Reuenthal     |
|15201063 | Lupfig-Schotter | Gravier de Lupfig     |
|15201064 | Löhningen-Engiwald-Vergletscherung | Glaciation de Löhningen-Engiwald     |
|15201065 | Engiwald-Vorstoss | Avancée glaciaire de l&#39;Engiwald     |
|15201066 | Rüfenach-Vorstoss | Avancée glaciaire de Rüfenach     |
|15201067 | Löhningen-Vorstoss | Avancée glaciaire de Löhningen     |
|15201068 | Remigen-Vorstoss | Avancée glaciaire de Remingen     |
|15201069 | Remigen-Schotter | Gravier de Remingen     |
|15201070 | Meikirch-Interglazial | Interglaciaire de Meikirch     |
|15201071 | Ältere Beckenfüllungen | Anciens remplissages de bassin     |
|15201072 | Hagenholz-Eiszeit | Période glaciaire du Hagenholz     |
|15201073 | Hagenholz-Vergletscherung | Glaciation du Hagenholz     |
|15201074 | Hagenholz-Vorstoss | Avancée glaciaire du Hagenholz     |
|15201075 | Aathal-Schotter | Gravier de l&#39;Aathal     |
|15201076 | Pfyn-Vorstoss | Avancée glaciaire de Pfyn     |
|15201077 | Ittingen-Schotter | Gravier d&#39;Ittingen     |
|15201078 | Ryhirt-Formation | Formation du Ryhirt     |
|15201079 | Geisslingen-Schotter | Gravier de Geisslingen     |
|15201080 | Habsburg-Hagenholz-Interglazial | Interglaciaire Habsburg-Hagenholz     |
|15201081 | Möhlinerfeld-Paläoboden | Paléosol du Möhlinerfeld     |
|15201082 | Habsburg-Eiszeit | Période glaciaire de Habsburg     |
|15201083 | Gränichen-Schotter | Gravier de Gränichen     |
|15201084 | Roggehuse-Schotter | Gravier de Roggehuse     |
|15201085 | Buerfeld-Schotter | Gravier du Buerfeld     |
|15201086 | Habsburg-Vergletscherung | Glaciation de Habsburg     |
|15201087 | Habsburg-Vorstoss | Avancée glaciaire de Habsburg     |
|15201088 | Habsburg-Schotter | Gravier de Habsburg     |
|15201089 | Unterschlatt-Vorstoss | Avancée glaciaire d&#39;Unterschlatt     |
|15201090 | Thalgut-Interglazial | Interglaciaire de Thalgut     |
|15201091 | Möhlin-Eiszeit (Grösste Eiszeit) | Période glaciaire de Möhlin     |
|15201092 | Möhlin-Vergletscherung | Glaciation de Möhlin     |
|15201093 | Möhlin-Vorstoss | Avancée glaciaire de Möhlin     |
|15201094 | Bünten-Till | Till de Bünten     |
|15201095 | Schleitheim-Vorstoss | Avancée glaciaire de Schleitheim     |
|15201096 | Fisibach-Schotter | Gravier de Fisibach     |
|15201097 | Bärengraben-Schotter und -Till | Gravier et Till du Bärengraben     |
|15201098 | Iberig-Schotterkomplex | Gravier de l&#39;Iberig     |
|15201099 | Obere Iberigschotter | Gravier supérieur de l&#39;Iberig     |
|15201100 | Oberer Till | Oberer Till (Iberig)     |
|15201101 | Mittlere Iberigschotter | Gravier moyen de l&#39;Iberig     |
|15201102 | Untere Iberigschotter | Gravier inférieur de l&#39;Iberig     |
|15201103 | Unterer Till | Unterer Till (Iberig)     |
|15201104 | Wolfacher-Schotter und -Till | Gravier et Till de Wolfacher     |
|15201105 | Fornech-Schotter | Gravier de la Fornech     |
|15201106 | Forenirchel-Schotter | Gravier du Forenirchel     |
|15201107 | Steig-Schotter | Gravier du Steig     |
|15201108 | Irchel-Schotterkomplex | Gravier de l&#39;Irchel     |
|15201109 | Obere Irchelschotter | Gravier supérieur de l&#39;Irchel     |
|15201111 | Irchel-Dolomitschotter | Gravier dolomitique de l&#39;Irchel     |
|15201112 | Mittlere Irchelschotter | Gravier moyen de l&#39;Irchel     |
|15201113 | Untere Irchelschotter | Gravier inférieur de l&#39;Irchel     |
|15201114 | Langacher-Schotter | Gravier du Langacher     |
|15201115 | Dürn-Formation | Formation du Dürn     |
|15201116 | Degermoos-Schotter | Gravier de Degermoos     |
|15201117 | Ebnet-Schotter | Gravier de l&#39;Ebnet     |
|15201118 | Wannen-Schotter | Gravier du Wannen(buck)     |
|15201119 | Egghalden-Schotter | Gravier de l&#39;Egghalden     |
|15201120 | Buechen-Formation | Formation de Buechen     |
|15201121 | Feusi-Schotter | Gravier du Feusi     |
|15201122 | Lindenhau-Schotter | Gravier du Lindenhau     |
|15201123 | Egg-Schotter | Gravier de l&#39;Egg     |
|15201124 | Sundgau-Schotter | Gravier du Sundgau     |
|15201125 | Mischschotter | Mischschotter (Sundgau)     |
|15201126 | Weisse Serie | Weisse Serie (Sundgau)     |
|15201129 | Zürich-Stein-Bremgarten-Stadien | stade glaciaire de Zürich-Stein-Bremgarten     |
|15201130 | Untere Singen-Terrasse | terrasse inférieure de Singen     |
|15201131 | Schlieren-Diessenhofen-Stetten-Stadien | stade de Schlieren-Diessenhofen-Stetten     |
|15201132 | Obere Singen-Terrasse | terrasse supérieure de Singen     |
|15201133 | Rheinau-Terrasse | terrasse de Rheinau     |
|15201134 | Nohl-Terrasse | terrasse de Nohl     |
|15201135 | Altenburg-Fulach-Terrasse | terrasse d&#39;Altenburg-Fulach     |
|15201136 | Aare-Schotter | Gravier de l&#39;Aar     |
|15201137 | Schüss-Schotter | Gravier de la Suze     |
|15201138 | Orvin-Schotter | Gravier d&#39;Orvin     |
|15201139 | Seeablagerungen von Frinvillier und Rondchâtel | Dépôts lacustres de Frinvillier et Rondchâtel     |
|15201140 | Stauschotter von Diessbach | Gravier de retenue de Diessbach     |
|15201141 | Mély-Formation | Formation de Mély     |
|15201142 | Kiessande von Madretsch | Sable à gravier de Madretsch     |
|15201143 | Seeland-Schotter | Gravier du Seeland     |
|15201144 | Emme-Schotter | Gravier de l&#39;Emme     |
|15201145 | Gäu-Schotter | Gravier du Gäu     |
|15201146 | Flumenthal-Lehm | Limon du Flumenthal     |
|15201147 | Killwangen-Schaffhausen-Mellingen-Stadium | stade de Killwangen-Schaffhouse-Mellingen     |
|15201148 | Munot-Terrasse | terrasse du Munot     |
|15201149 | Stokar-Terrasse | terrasse de Stokar     |
|15201150 | Breite-Terrasse | terrasse de la Breite     |
|15201151 | Maximalstand (Kilwangen-Schaffhausen-Stadium) | stade maximal (Kilwangen-Schaffhouse)     |
|15201152 | Wehntal-Schotter | Gravier du Wehntal     |
|15201153 | Bick-Till | Till du Bick(acher)     |
|15201154 | Flüe-Till | Till de Flüe     |
|15201155 | Wettingen-Schotter | Gravier de Wettingen     |
|15201156 | Bersturzmasse von Selzach | Dépôt d&#39;écroulement de Selzach     |
|15201157 | Plateauschotter | Plateauschotter     |
|15201158 | La-Côte-Schotter | Alluvions de la Côte     |
|15201159 | Enge-Schotter | Gravier de l&#39;Enge     |
|15201160 | Attiswil-Schotter | Gravier d&#39;Attiswil     |
|15201161 | Lommiswil-Schotter | Gravier de Lommiswil     |
|15201162 | Oensingen-Moos-Lehm | Limon d&#39;Oensingen-Moos     |
|15201163 | Berken-Schotter | Gravier de Berken     |
|15201164 | Berken-Sand | Sable de Berken     |
|15201165 | Schwarzhäusern-Lehm | Limon de Schwarzhäusern     |
|15201166 | Käppelihof-Schotter | Gravier du Käppelihof     |
|15201167 | Aarburg-Schotter | Gravier d&#39;Aarburg     |
|15201168 | Tuileries-Formation | Formation des Tuileries     |
|15201169 | Grandson-Formation | Formation de Grandson     |
|15201170 | Poissine-Formation | Formation de la Poissine     |
|15201171 | Surbtal-Lehm | Limon du Surbtal     |
|15201172 | Surbtal-Till | Till du Surbtal     |
|15201173 | Surbtal-Schotter | Gravier du Surbtal     |
|15201174 | Fislisbach-Schotter | Gravier de Fislisbach     |
|15201175 | Reusstal-Sand | Sable du Reusstal     |
|15201176 | Reusstal-Lehm | Limon du Reusstal     |
|15201177 | Hausen-Lehm | Limon de Hausen     |
|15201178 | Hausen-Moräne | Till de Hausen     |
|15201179 | Ruckfeld-Schotter | Gravier du Ruckfeld     |
|15201180 | Endingen-Schotter | Gravier d&#39;Endingen     |
|15201181 | Rhein- und Aareschotter | Gravier du Rhin et de l&#39;Aar     |
|15201182 | Juraschotter | Juraschotter     |
|15201183 | Alte Doubsschotter | Gravier ancien du Doubs     |
|15201184 | Wutach-Schotter | Gravier de la Wutach     |
|15201185 | Merenbach-Schotter | Gravier du Merenbach     |
|15201186 | Malmkalk-Schotter der Randen-Täler | Malmkalk-Schotter (vallée du Randen)     |
|15201187 | Solothurn-Stadium | stade de Soleure     |
|15201188 | Münsingen-Schotterkomplex | Complexe graveleux de Münsingen     |
|15201189 | Alterswil-Schotter | Gravier d&#39;Alterswil     |
|15201190 | Karlsruhe-Schotter | Gravier de Karlsruhe     |
|15201191 | Chisetal-Schotter | Gravier du Chisetal     |
|15201192 | Grauholz-Schotter | Gravier du Grauholz     |
|15201193 | Trachslau-Schotter | Gravier de Trachslau     |
|15201194 | Bennau-Schotter | Gravier de Bennau     |
|15201195 | Hütten-Schotter | Gravier de Hütten     |
|15201196 | Schnabelsberg-Stauchotter | Gravier de Schnabelsberg     |
|15201197 | Einsiedeln-Lehm | Limon d&#39;Einsiedeln     |
|15201198 | Willisau-Schotter | Gravier de Willisau     |
|15201199 | Wolhusen-Schotter | Gravier de Wolhusen     |
|15201200 | Wiggen-Schotter | Gravier de la Wigger     |
|15201201 | Menzingen-Schotter | Gravier de Menzingen     |
|15201202 | La-Tuffière-Schotter | Gravier de la Tuffière     |
|15201203 | Gontenschwil-Lehm | Limon de Gontenschwil     |
|15201204 | Mooslerau-Lehm | Limon du Mooslerau     |
|15201205 | Triengen-Schotter | Gravier de Triengen     |
|15201206 | Triengen-Lehm | Limon de Triengen     |
|15201207 | Sihl-Schotter | Gravier de la Sihl     |
|15201208 | Haselbach-Schotter | Gravier du Haselbach     |
|15201209 | Jonen-Schotter | Gravier de Jonen     |
|15201210 | Aabach-Schotter | Gravier de l&#39;Aabach     |
|15201211 | Starrberg-Schotter | Gravier de Starrberg     |
|15201212 | Port-Stauschotter | Gravier de Port     |
|15201213 | Rempen-Stauschotter | Gravier de Rempen     |
|15201214 | Dagmersellen-Vorstoss | Avancée glaciaire de Dagmersellen     |
|15201215 | Oftringen-Schotter | Gravier d&#39;Oftringen     |
|15201216 | Zelg-Schotter | Gravier de Zelg     |
|15201217 | Forst-Schotter | Gravier du Forst     |
|15201218 | Raintal-Deltaschotter | Gravier du Raintal     |
|15201219 | Kleinhöchstetten-Kies-Sand-Komplex | Complexe sablo-graveleux de Kleinhöchstetten     |
|15201220 | Krauchthal-Schotter | Gravier du Krauchthal     |
|15201221 | Brandflue-Schotter | Gravier de la Brandflue     |
|15201222 | Küsnacht-Schotter | Gravier de Küsnacht     |
|15201223 | Chatzenstrick-Schotter | Gravier du Chatzenstrick     |
|15201224 | Rabennest-Schotter | Gravier du Rabennest     |
|15201225 | Ratengütsch-Schotter | Gravier du Ratengütsch     |
|15201226 | Scherenspitz-Schotter | Gravier du Scherenspitz     |
|15201227 | Walsenhaus-Schotter | Gravier de Walsenhaus     |
|15201228 | Richterswil-Seeton | Argile lacustre de Richterswil     |
|15201229 | Schwanden-Schotter | Gravier de Schwanden     |
|15201230 | Reidbach-Schotter | Gravier du Reidbach     |
|15201231 | Zell-Schotterkomplex | Gravier de Zell     |
|15201232 | Gubel-Schotter | Gravier de Gubel     |
|15201233 | Chälen-Schotter | Gravier de Chälen     |
|15201234 | Chälen-Till | Till de Chälen     |
|15201235 | Sihlsprung-Schotter | Gravier du Sihlsprung     |
|15201236 | Kollbrunn-Schotter | Gravier de Kollbrunn     |
|15201237 | Walenberg-Schotter | Gravier de Walenberg     |
|15201238 | Ritteren-Schotterkomplex | Complexe graveleux de Ritteren     |
|15201239 | Vorholz-Schotter | Gravier du Vorholz     |
|15201240 | Gutsch-Schotter | Gravier du Gutsch     |
|15201241 | Junkerenwald-Schotter | Gravier du Junkerenwald     |
|15201242 | Chräjeloch-Schotter | Gravier du Chräjeloch     |
|15201243 | Butteberg-Schotter | Gravier du Butteberg     |
|15201244 | Höchi-Schotter | Gravier du Höchi     |
|15201245 | Heitere-Schotter | Gravier deHeitere     |
|15201246 | Holziken-Schotter | Gravier de Holziken     |
|15201247 | Ruedertal-Schotter | Gravier du Ruedertal     |
|15201248 | Bänkel-Schotter | Gravier de Bänkel     |
|15201249 | Quartär, undifferenziert | Quaternaire, indifférencié     |
|15201250 | Deckenschotter, undifferenziert | Deckenschotter, indifférencié     |
|15201251 | Girenbad-Schotter | Gravier du Girenbad     |
|15201252 | Sagenbach-Schotter | Gravbier du Sagenbach     |
|15201253 | Schrotzburg-Schotter | Gravier de la Schrotzburg     |
|15201254 | Schrotzburg-Till | Till de la Schrotzburg     |
|15201255 | Bohlingen-Schotter | Gravier de Bohlingen     |
|15201256 | Bannholz-Schotter | Gravier du Bannholz     |
|15201257 | Hungerbol-Schotter | Gravier d&#39;Hungerbol     |
|15201258 | Chilchstapfen-Schotter | Gravier de la Chilchstapfen     |
|15201259 | Ofenloch-Karstfüllung | Ofenloch-Karstfüllung     |
|15201260 | Wurmsbach-Deltaablagerungen | Wurmsbach-Deltaablagerungen     |
|15201261 | Oeschinensee-Bergsturzablagerungen | Oeschinensee-Bergsturzablagerungen     |
|15201262 | Fisistock-Bergsturzablagerungen | Fisistock-Bergsturzablagerungen     |
|15201263 | Bire-Bergsturzablagerungen | Bire-Bergsturzablagerungen     |
|15201264 | Hasle-Schotter | Hasle-Schotter     |
|15201265 | Fankhusgrabe-Schotter | Fankhusgrabe-Schotter     |
|15201266 | Rossgaden-Schotter | Rossgaden-Schotter     |
|15201267 | Grundtal-Schotter | Grundtal-Schotter     |
|15201268 | Murg-Schieferkohle | Murg-Schieferkohle     |
|15201269 | Oberricken-Schotter | Oberricken-Schotter     |
|15201270 | Haslentobel-Schotter | Haslentobel-Schotter     |
|15201271 | Aatal-Seebodenlehm | Aatal-Seebodenlehm     |
|15201272 | Eschenbach-Formation | Eschenbach-Formation     |
|15201273 | Oberkirch-Seebodenlehm | Oberkirch-Seebodenlehm     |
|15201274 | Günterstall-Schotter | Günterstall-Schotter     |
|15201275 | Gublen-Schotter | Gublen-Schotter     |
|15201276 | Unter-Buechwald-Schotter | Unter-Buechwald-Schotter     |
|15201277 | Regelstein-Till | Regelstein-Till     |
|15201278 | Halden-Seeablagerungen | Halden-Seeablagerungen     |
|15201279 | Schafbüel-Formation | Schafbüel-Formation     |
|15201280 | Unteres-Huttenbüel-Schotter | Unteres-Huttenbüel-Schotter     |
|15201281 | Winden-Schieferkohle | Winden-Schieferkohle     |
|15201282 | Tiefenwinkel-Seebodensedimente | Tiefenwinkel-Seebodensedimente     |
|15201283 | Uznach-Schieferkohle | Uznach-Schieferkohle     |
|15201284 | Embrach-Seeablagerungen | Embrach-Seeablagerungen     |
|15201286 | Bergsturzablagerungen von Sierre | dépôt d&#39;écroulement de Sierre     |
|15201287 | Bergsturzablagerungen von Chiètres | dépôt d&#39;écroulement de Chiètres     |
|15201288 | Bergsturzablagerungen von Chessel-Noville | dépôt d&#39;écroulement de Chessel-Noville     |
|15201289 | Bergsturzablagerungen von Novalles-Vugelles | dépôt d&#39;écroulement de Novalles-Vugelles     |
|15201290 | Bergsturzablagerungen von Gwelber-Laui-Weid | dépôt d&#39;écroulement de Gwelber-Laui-Weid     |
|15201291 | Bergsturzablagerungen von Castasegna | dépôt d&#39;écroulement de Castasegna     |
|15201292 | Bergsturzablagerungen von Sogno | dépôt d&#39;écroulement de Sogno     |
|15201293 | Bergsturzablagerungen von Prapan | dépôt d&#39;écroulement de Prapan     |
|15201294 | Bergsturzablagerungen von Schaingels | dépôt d&#39;écroulement de Schaingels     |
|15201295 | Bergsturzablagerungen von Mutta | dépôt d&#39;écroulement de Mutta     |
|15201296 | Bergsturzablagerungen von Brienz | dépôt d&#39;écroulement de Brienz     |
|15201297 | Bergsturzablagerungen von Flims | dépôt d&#39;écroulement de Flims     |
|15201298 | Bergsturzablagerungen von Brüsis | dépôt d&#39;écroulement de Brüsis     |
|15201299 | Bergsturzablagerungen vom Chapf | dépôt d&#39;écroulement de Chapf     |
|15201300 | Bergsturzablagerungen von Derborence | Bergsturzablagerungen von Derborence     |
|15201301 | Bergsturzablagerungen vom Drussetschawald | dépôt d&#39;écroulement du Drussetschawald     |
|15201302 | Bergsturzablagerungen vom Delenwald | dépôt d&#39;écroulement du Delenwald     |
|15201303 | Bergsturzablagerungen von Elm | dépôt d&#39;écroulement d&#39;Elm     |
|15201304 | Bergsturzablagerungen von Goldau | dépôt d&#39;écroulement de Goldau     |
|15201305 | Bergsturzablagerungen von Iragell | dépôt d&#39;écroulement d&#39;Iragell     |
|15201306 | Bergsturzablagerungen vom Kernwald | dépôt d&#39;écroulement du Kernwald     |
|15201307 | Bergsturzablagerungen von Triesenberg | dépôt d&#39;écroulement de Triesenberg     |
|15201308 | Bonaduz-Formation | Formation de Bonaduz     |
|15201309 | Bonfol-Ton | Argile de Bonfol     |
|15201310 | Bergsturzablagerungen von Tamins | dépôt d&#39;écroulement de Tamins     |
|15201311 | Informell benannte Bergsturzablagerungen | dépôts d&#39;écroulement nommés informellement     |
|15201312 | Informell benannte künstliche Ablagerungen | dépôts artificiels nommés informellement     |
|15201313 | Künstliche Ablagerungen des Bahnhofs Brig | dépôts artificiels de la gare de Brigue     |
|15201314 | Künstliche Ablagerungen Golar | dépôts artificiels Golar     |
|15201315 | Künstliche Ablagerungen der Gamsenried-Deponie | dépôts artificiels de la décharge de la Lonza     |
|15201316 | Künstliche Ablagerungen des Riedertals | dépôts artificiels du Riedertal     |
|15201317 | Informell benannte Sackungsmassen | masses tassées nommées informellement     |
|15201318 | Sackungsmasse des Heinzenbergs | masse tassée du Heinzenberg     |
|15201319 | Informell benannte fluviatile Schotter | graviers fluviatiles nommés informellement     |
|15201320 | Schotter und Sand der Rhône | graviers et sables du Rhône     |
|15201321 | Schotter und Sand der Vispa | graviers et sables de la Viège     |
|15201322 | Informell benannter Bachschutt | dépôts torrentiels nommés informellement     |
|15201323 | Bachschutt des Baltschiederbachs | dépôts torrentiels du Baltschiedertal     |
|15201324 | Bachschutt des Bietschbachs | dépôts torrentiels du Bietschbach     |
|15201325 | Bachschutt des Chelchbachs | dépôts torrentiels du Chelchbach     |
|15201326 | Bachschutt der Gamsa | dépôts torrentiels de la Gamsa     |
|15201327 | Bachschutt des Jolibachs | dépôts torrentiels du Jolibach     |
|15201328 | Bachschutt der Lonza | dépôts torrentiels de la Lonza     |
|15201329 | Bachschutt der Saltina | dépôts torrentiels de la Saltina     |
|15201330 | Bachschutt der Vispa | dépôts torrentiels de la Viège     |
|15201331 | Bachschutt der Gürbe | dépôts torrentiels de la Gürbe     |
|15201332 | Bachschutt des Lombachs | dépôts torrentiels du Lombach     |
|15201333 | Pliozäne Ablagerungen | dépôts pliocènes     |
|15201334 | Stockesee-Sediment | Sédiments du Stockesee     |
|15201335 | Strätligen-Till | Till de Strätligen     |
|15201336 | Bärenholz-Till | Till du Bärenholz     |
|15201337 | Wässerifluh-Formation | Formation de la Wässerlifluh     |
|15201338 | Schlyffi-Till | Till de la Schlyffi     |
|15201339 | Brüggstutz-Schotter | Gravier du Brüggstutz     |
|15201340 | Guntelsei-Till | Till de la Guntelsei     |
|15201341 | Guntelsei-Schotter | Gravier de la Guntelsei     |
|15201342 | Steghalden-Schotter | Gravier de la Steghalden     |
|15201343 | Glütschtal-Formation | Formation du Glütschtal     |
|15201344 | Hahni-Schotter | Gravier de Hahni     |
|15201444 | Löss, undifferenziert | Loess, indifférencié     |
|15201458 | Ceppo | Ceppo     |
|15201459 | Novazzano-Sand | Sable de Novazzano     |
|15201460 | Bergsturzablagerungen vom Stützwald | dépôt d&#39;écroulement du Stützwald     |
|15201462 | Birkenhof-Formation | Birkenhof-Formation     |
|15201463 | Zeiningen-Till | Zeiningen-Till     |
|15201464 | Höhenschotter | Höhenschotter     |
|15201465 | Böschmatt-Schotter | Böschmatt-Schotter     |
|15201466 | Bramegg-Schotter | Bramegg-Schotter     |
|15201467 | Kaltenegg-Schotter | Kaltenegg-Schotter     |
|15201468 | Steinhuserberg-Schotter | Steinhuserberg-Schotter     |
|15201469 | Büelm-Schotter | Büelm-Schotter     |
|15201470 | Büel-Schotter | Büel-Schotter     |
|15201471 | Bünten-Schotter | Bünten-Schotter     |
|15201472 | Durnagel-Schotter | Durnagel-Schotter     |
|15201473 | Dürrenroth-Schotter | Dürrenroth-Schotter     |
|15201474 | Egghüsli-Schotter | Egghüsli-Schotter     |
|15201475 | Emmental-Schotter | Emmental-Schotter     |
|15201476 | Ergolztal-Schotter | Ergolztal-Schotter     |
|15201477 | Gammenthal-Schotter | Gammenthal-Schotter     |
|15201478 | Gondiswil-Formation | Gondiswil-Formation     |
|15201479 | Hasewald-Schotter | Hasewald-Schotter     |
|15201480 | Hirzmatt-Schotter | Hirzmatt-Schotter     |
|15201481 | Mettlen-Schotter | Mettlen-Schotter     |
|15201482 | Möhlinerfeld-Schotter | Möhlinerfeld-Schotter     |
|15201483 | Muttenfeld-Schotter | Muttenfeld-Schotter     |
|15201484 | Nidfurn-Schotter | Nidfurn-Schotter     |
|15201485 | Oberhöhe-Grundmoräne | Oberhöhe-Grundmoräne     |
|15201486 | Obermoos-Schotter | Obermoos-Schotter     |
|15201487 | Öflingen-Schotter | Öflingen-Schotter     |
|15201488 | Rottal-Schotter | Rottal-Schotter     |
|15201489 | Rüdelwald-Schotter | Rüdelwald-Schotter     |
|15201490 | Rufswil-Schotter | Rufswil-Schotter     |
|15201491 | Rütimatt-Schotter | Rütimatt-Schotter     |
|15201492 | Schwanderholzwald-Schotter | Schwanderholzwald-Schotter     |
|15201493 | Schwande-Seebodensedimente | Schwande-Seebodensedimente     |
|15201494 | Soppensee-Seebodensedimente | Soppensee-Seebodensedimente     |
|15201495 | Speicherboden-Lokalmoräne | Speicherboden-Lokalmoräne     |
|15201496 | terrasse lémanique de 10 m | terrasse lémanique de 10 m     |
|15201497 | terrasse lémanique de 3 m | terrasse lémanique de 3 m     |
|15201498 | Untere Zeller Schotter | Untere Zeller Schotter     |
|15201499 | Untergrabehüsli-Schotter | Untergrabehüsli-Schotter     |
|15201500 | Untertreie-Schotter | Untertreie-Schotter     |
|15201501 | Wallbach-Schotter | Wallbach-Schotter     |
|15201502 | Werthenstein-Schotter | Werthenstein-Schotter     |
|15201503 | Willburg-Formation | Willburg-Formation     |
|15201504 | Wilzigen-Seebodensedimente | Wilzigen-Seebodensedimente     |
|15201505 | Reuss-Schotterkomplex | Reuss-Schotterkomplex     |
|15201506 | Hagnau-Niveau | Hagnau-Niveau     |
|15201507 | Reusstal-Seebodensediment | Reusstal-Seebodensediment     |
|15201508 | Wyna-Schotter | Wyna-Schotter     |
|15201509 | Rickenbach-Schotter | Rickenbach-Schotter     |
|15201510 | Ermensee-Schotter | Ermensee-Schotter     |
|15201511 | Mooretal-Schotter | Mooretal-Schotter     |
|15201512 | Ämmet-Schotter | Ämmet-Schotter     |
|15201513 | Homberg-Till | Homberg-Till     |
|15201514 | Lindenberg-Till | Lindenberg-Till     |
|15201515 | Heubeerihübel-Schotter | Heubeerihübel-Schotter     |
|15201516 | Ritzhans-Schotter | Ritzhans-Schotter     |
|15201517 | Unterdorf-Schotter | Unterdorf-Schotter     |
|15201518 | Schönegg-Formation | Schönegg-Formation     |
|15201519 | Säckingen-Schotter | Säckingen-Schotter     |
|15201520 | Bruderhäusle-Schotter | Bruderhäusle-Schotter     |
|15201521 | Mumpf-Schotter | Mumpf-Schotter     |
|15201522 | Riedmatt-Schotter | Riedmatt-Schotter     |
|15201523 | Beuggen-Schotter | Beuggen-Schotter     |
|15201524 | Feldhof-Schotter | Feldhof-Schotter     |
|15201525 | Spärgacher-Schotter | Spärgacher-Schotter     |
|15201526 | Wagenmoos-Till | Till du Wagenmoos     |
|15201527 | Niderstalden-Schotter | Gravier de Niderstalden     |
|15201528 | Zulgtal-Schotter | Gravier du Zulgtal     |
|15201529 | Spiez-Schotter | Gravier de Spiez     |
|15201530 | Hahni-Till | Till de Hahni     |
|15201531 | Bergsturzablagerung von Ralligen (im Thunersee) | Dépôt d&#39;écroulement de Ralligen (dans le lac de Thoune)     |
|15201532 | Bergsturzablagerung von Bargis | dépôt d&#39;éboulement de Bargis     |
|15201533 | Bergsturzablagerung von Fidaz | dépôt d&#39;éboulement de Fidaz     |
|15201534 | Niederterrassenschotter, tiefere Niveaus | Niederterrasse, niveaux graveleux inférieurs     |
|15201535 | Niederterrassenschotter, zweitoberste Terrasse | Niederterrasse, deuxième niveau graveleux le plus élevé     |
|15201536 | Niederterrassenschotter, oberste Terrasse | Niederterrasse, premier niveau graveleux le plus élevé     |
|15201537 | Tiefere Deckenschotter, unteres Niveau | Tiefere Deckenschotter, niveau inférieur     |
|15201538 | Tiefere Deckenschotter, oberes Niveau | Tiefere Deckenschotter, niveau supérieur     |
|15201539 | Kunkels-Formation | Formation de Kunkels     |
|15201540 | Alluvion von Ransun | Alluvion de Ransun     |
|15201541 | Rüdlingen-Till | Till de Rüdlingen     |
|15201542 | Niklaushalden-Formation | Formation de Niklaushalden     |
|15201543 | Stadel-Till | Till de Stadel     |
|15201544 | Volken-Lehm | Limon de Volken     |
|15201545 | Rheinau-Till | Till de Rheinau     |
|15201546 | Ellikerholz-Formation | Formation de l&#39;Ellikerholz     |
|15201547 | Eggholz-Formation | Formation de l&#39;Eggholz     |
|15201548 | Bannhalden-Schotter | Gravier de Bannhalden     |
|15201549 | Weiach-Schotter | Gravier de Weiach     |
|15201550 | Balm-Schotter | Gravier de Balm     |
|15201551 | Windlach-Till | Till de Windlach     |
|15201552 | Südranden-Till | Gravier du Südranden     |
|15201553 | Schlossbuck-Schotter | Gravier de Schlossbuck     |
|15201554 | Risibüel-Schotter | Gravier de Risibüel     |
|15201555 | Schmerlet- und Toktri-Formation, undifferenziert | Formations de Schmerlet et Toktri, indifférenciées     |
|15201556 | Saxegrabe-Schotter | Gravier du Saxegrabe     |
|15201557 | Zweidlen-Schotter | Gravier de Zweidlen     |
|15201558 | Burgacher-Schotter | Gravier de Burgacher     |
|15201559 | Chatzenstig-Schotter | Gravier du Chatzenstig     |
|15201560 | Wasterkingen-Schotter | Gravier de Wasterkingen     |
|15201561 | Paradiesgärtli-Schotter | Gravier du Paradiesgärtli     |
|15201562 | Tubeschwanz-Schotter | Gravier de Tubeschwanz     |
|15201563 | Weisweil-Schotter | Gravier de Weisweil     |
|15201564 | Hasli-Formation | Formation de Hasli     |
|15201565 | Stetten-Schotter | Gravier de Stetten     |
|15201566 | Plaffeien-Seetone | Plaffeien-Seetone     |
|15201567 | Plasselb-Stauschotter | Plasselb-Stauschotter     |
|15201568 | Uetliberg-Lehm | Uetliberg-Lehm     |
|15201569 | Schotter der Thur | Schotter der Thur     |
|15201570 | Schwarzwald-Schotter | Schwarzwald-Schotter     |
|15201571 | Neuenburg-Formation | Neuenburg-Formation     |
|15201572 | Hartheim-Member | Hartheim-Member     |
|15201573 | Nambsheim-Member | Nambsheim-Member     |
|15201574 | Breisgau-Formation | Breisgau-Formation     |
|15201575 | Balgau-Member | Balgau-Member     |
|15201576 | Weinstetten-Member | Weinstetten-Member     |
|15201577 | Iffezheim-Formation | Iffezheim-Formation     |
|15201578 | Mannheim-Formation | Mannheim-Formation     |
|15201579 | Etzgen-Formation | Etzgen-Formation     |
|15201580 | Niederuster-Schotter | Niederuster-Schotter     |
|15201581 | Pfungen-Formation | Pfungen-Formation     |
|15201582 | Dättlikon-Stadium | Dättlikon-Stadium     |
|15201583 | Dübendorf-Stadium | Dübendorf-Stadium     |
|15201584 | Gfenn-Stadium | Gfenn-Stadium     |
|15201585 | Regensdorf-Stadium | Regensdorf-Stadium     |
|15201586 | Seeb-Stadium | Seeb-Stadium     |
|15201587 | Würenlos-Stadium | Würenlos-Stadium     |
|15201588 | Würenlos-Stand-I | Würenlos-Stand-I     |
|15201589 | Würenlos-Stand-II | Würenlos-Stand-II     |
|15201590 | Bülach-Stadium | Bülach-Stadium     |
|15201591 | Bülach-Stand-I | Bülach-Stand-I     |
|15201592 | Bülach-Stand-II | Bülach-Stand-II     |
|15201593 | Stein-am-Rhein-Stadium | Stein-am-Rhein-Stadium     |
|15201594 | Stein-am-Rhein-Stand-I | Stein-am-Rhein-Stand-I     |
|15201595 | Stein-am-Rhein-Stand-II | Stein-am-Rhein-Stand-II     |
|15201596 | Stein-am-Rhein-Stand-III | Stein-am-Rhein-Stand-III     |
|15201597 | Zürich-Stadium | Zürich-Stadium     |
|15201598 | Zürich-Stand-I | Zürich-Stand-I     |
|15201599 | Zürich-Stand-II | Zürich-Stand-II     |
|15201600 | Bremgarten-Stadium | Bremgarten-Stadium     |
|15201601 | Bremgarten-I | Bremgarten-I     |
|15201602 | Bremgarten-II | Bremgarten-II     |
|15201603 | Singen-Stadium | Singen-Stadium     |
|15201604 | Feuerthalen-Stadium | Feuerthalen-Stadium     |
|15201605 | Feuerthalen-Stand-I | Feuerthalen-Stand-I     |
|15201606 | Feuerthalen-Stand-II | Feuerthalen-Stand-II     |
|15201607 | Schlieren-Stadium | Schlieren-Stadium     |
|15201608 | Bäretswil-Seeablagerung | Bäretswil-Seeablagerung     |
|15201609 | Hittnau-Seeablagerung | Hittnau-Seeablagerung     |
|15201610 | Russikon-Seeablagerung | Russikon-Seeablagerung     |
|15201611 | Stetten-Stadium | Stetten-Stadium     |
|15201612 | Stetten-Stand-I | Stetten-Stand-I     |
|15201613 | Stetten-Stand-II | Stetten-Stand-II     |
|15201614 | Diessenhofen-Stadium | Diessenhofen-Stadium     |
|15201615 | Mellingen-Stand | Mellingen-Stand     |
|15201616 | Schaffhausen-Stadium | Schaffhausen-Stadium     |
|15201617 | Schaffhausen-Stand-I | Schaffhausen-Stand-I     |
|15201618 | Schaffhausen-Stand-II | Schaffhausen-Stand-II     |
|15201619 | Killwangen-Stadium | Killwangen-Stadium     |
|15201620 | Lottstetten-, Kohlschwärze- und Zelgli-Vorstoss | Lottstetten-, Kohlschwärze- und Zelgli-Vorstoss     |
|15201621 | Grafschaft-Schotter | Grafschaft-Schotter     |
|15201622 | &#34;Mittelterrasse&#34; | &#34;Mittelterrasse&#34;     |
|15201623 | Hochterrasse, unteres Niveau | Hochterrasse, unteres Niveau     |
|15201624 | Hochterrasse, mittleres Niveau | Hochterrasse, mittleres Niveau     |
|15201625 | Hochterrasse, oberes Niveau | Hochterrasse, oberes Niveau     |
|15201626 | First-Schotter | First-Schotter     |
|15201627 | Helltobel-Schotter | Helltobel-Schotter     |
|15201628 | Lettenberg-Seesedimente | Lettenberg-Seesedimente     |
|15201629 | Zurzach-Formation | Zurzach-Formation     |
|15201630 | Ursplen-Till | Ursplen-Till     |
|15201631 | Äntschberg-Schotter | Äntschberg-Schotter     |
|15201632 | Oberrüti-Schotter | Oberrüti-Schotter     |
|15201633 | Neerach-Schotter | Neerach-Schotter     |
|15201634 | Bachs-Schotter | Bachs-Schotter     |
|15201635 | Steighalden-Schotter | Steighalden-Schotter     |
|15201636 | Mühlbach-Formation | Mühlbach-Formation     |
|15201637 | Chilchberg-Schotter | Chilchberg-Schotter     |
|15201638 | Frenkendorf-Schotter | Frenkendorf-Schotter     |
|15201639 | Birstal-Schotter | Birstal-Schotter     |
|15201640 | Schlatt-Formation | Schlatt-Formation     |
|15201641 | Illmensee-Formation | Illmensee-Formation     |
|15201642 | Dietmanns-Formation | Dietmanns-Formation     |
|15201643 | Hasenweiler-Formation | Hasenweiler-Formation     |
|15201644 | Haseltal-Formation | Haseltal-Formation     |
|15201645 | Birndorf-, Laufenburg- und Zeiningen-Vorstoss | Birndorf-, Laufenburg- und Zeiningen-Vorstoss     |
|15201646 | Chäppeli-Schotter | Chäppeli-Schotter     |
|15201647 | Leuggern-Schotter | Leuggern-Schotter     |
|15201648 | Zelgli-Schotter | Zelgli-Schotter     |
|15201649 | Leibstadt-Schotter | Leibstadt-Schotter     |
|15201650 | Dogern-Schotter | Dogern-Schotter     |
|15201651 | Haldenacher-Schotter | Haldenacher-Schotter     |
|15201652 | Allmendwald-Schotter | Allmendwald-Schotter     |
|15201653 | Lei-Schotter | Lei-Schotter     |
|15201654 | Obersäckingen-Schotter | Obersäckingen-Schotter     |
|15201655 | Schulerholz-Formation | Schulerholz-Formation     |
|15201656 | Schachen-Formation | Schachen-Formation     |
|15201657 | Schmerlet-Formation | Schmerlet-Formation     |
|15201658 | Toktri-Formation | Toktri-Formation     |
|15201659 | Buchholz-Till | Buchholz-Till     |
|15201660 | Birndorf-Till | Birndorf-Till     |
|15201661 | Geissäcker-Schotter | Geissäcker-Schotter     |
|15201662 | Bürgerwald-Schotter | Bürgerwald-Schotter     |
|15201663 | Hettenschwil-Schotter | Hettenschwil-Schotter     |
|15201664 | Moos-Schotter | Moos-Schotter     |
|15201665 | Schlüsselgraben-Schotter | Schlüsselgraben-Schotter     |
|15201666 | Hundsbel-Schotter | Hundsbel-Schotter     |
|15201667 | Laufenburg-Schotter | Laufenburg-Schotter     |
|15201668 | Eilez-Schotter | Eilez-Schotter     |
|15201669 | St.-Margarethen-Schotter | St.-Margarethen-Schotter     |
|15201670 | Hegenheim-Schotter | Hegenheim-Schotter     |
|15201671 | Blotzheim-Schotter | Blotzheim-Schotter     |
|15201672 | Hardwald-Schotter | Hardwald-Schotter     |
|15201673 | Homberg-Schotter | Homberg-Schotter     |
|15201674 | Rümlang-Schotter | Rümlang-Schotter     |
|15201675 | Äpelöö-Schotter | Äpelöö-Schotter     |
|15201676 | Fehrental-Schotter | Fehrental-Schotter     |
|15201677 | Challeren-Schotter | Challeren-Schotter     |
|15201678 | Ausserberg-Schotter | Ausserberg-Schotter     |
|15201679 | Leibstadt-Till | Leibstadt-Till     |
|15201680 | Buechli-Schotter | Buechli-Schotter     |
|15201681 | Bächemoos-Schotter | Bächemoos-Schotter     |
|15201682 | Aarberg-Schotter | Aarberg-Schotter     |
|15201683 | Tannboden-Schotter | Tannboden-Schotter     |
|15201684 | Etzwil-Schotter | Etzwil-Schotter     |
|15201685 | Ellenbühl-Schotter | Ellenbühl-Schotter     |
|15201686 | Kegelplatz-Schotter | Kegelplatz-Schotter     |
|15201687 | Einschlag-Schotter | Einschlag-Schotter     |
|15201688 | Lehacker-Schotter | Lehacker-Schotter     |
|15201689 | Letten-Schotter | Letten-Schotter     |
|15201690 | Schwörstadt-Schotter | Schwörstadt-Schotter     |
|15201691 | Steppberg-Schotter | Steppberg-Schotter     |
|15201692 | Bloseberg-Schotter | Bloseberg-Schotter     |
|15201693 | Steinebol-Schotter | Steinebol-Schotter     |
|15201694 | Giebenach-Schotter | Giebenach-Schotter     |
|15201695 | Blözen-Schotter | Blözen-Schotter     |
|15201696 | Rütihard-Schotter | Rütihard-Schotter     |
|15201697 | Bruederholz-Schotter | Bruederholz-Schotter     |
|15201698 | Binningen-Schotter | Binningen-Schotter     |
|15201699 | Allschwil-Schotter | Allschwil-Schotter     |
|15201700 | Buschwiller-Schotter | Buschwiller-Schotter     |
|15201701 | Berchenwald-Schotter | Berchenwald-Schotter     |
|15201702 | Hörndli-Schotter | Hörndli-Schotter     |
|15201703 | Acheberg-Schotter | Acheberg-Schotter     |
|15201704 | Mühleberg-Schotter | Mühleberg-Schotter     |
|15201705 | Mandach-Schotter | Mandach-Schotter     |
|15201706 | Duttenberg-Schotter | Duttenberg-Schotter     |
|15201707 | Humbel-Schotter | Humbel-Schotter     |
|15201708 | Frauewald-Schotter | Frauewald-Schotter     |
|15201709 | Bolderen-Schotter | Bolderen-Schotter     |
|15201710 | Seiglisten-Schotter | Seiglisten-Schotter     |
|15201711 | Geispel-Schotter | Geispel-Schotter     |
|15201712 | Birlibänz-Schotter | Birlibänz-Schotter     |
|15201713 | Schönenbuch-Schotter | Schönenbuch-Schotter     |
|15201714 | Wentzwiller-Schotter | Wentzwiller-Schotter     |
|15201715 | Bellevue-Schotter | Bellevue-Schotter     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |









## Annexe  GC_LITHO_CD {#gc-litho-cd}
Tables des valeurs de la description lithologique

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15101001 | Lockergestein | roche meuble     |
|15101003 | gravitative Sedimente und Verwitterungsbildungen, undifferenziert | dépôts gravitaires et d&#39;altération, indifférenciés     |
|15101005 | Sturzablagerung, undifferenziert | dépôts d&#39;écroulement, d&#39;éboulement, indifférenciés     |
|15101006 | Bergsturzablagerung | dépôt d&#39;écroulement     |
|15101007 | Felssturzablagerung | dépôt d&#39;éboulement     |
|15101008 | Lawinenschutt | dépôts d&#39;avalanche     |
|15101009 | Hangschutt | éboulis     |
|15101010 | Blockschutt | amas de blocs éboulés     |
|15101012 | Verwitterungslehm, undifferenziert | limons d&#39;altération, indifférenciés     |
|15101013 | Plateaulehm | limons de plateau, éluvions     |
|15101014 | Hanglehm, Schwemmlehm | limons de pente, colluvions     |
|15101015 | Blockgletscher | glacier rocheux     |
|15101016 | zerrüttete Sackungsmasse | masse de roche tassée et disloquée     |
|15101017 | Rutschmasse | masse glissée     |
|15101019 | glazigenes Sediment, undifferenziert | sédiments glaciaires, indifférenciés     |
|15101021 | Moräne (Till), undifferenziert | moraine (till), indifférenciée     |
|15101024 | Moräne auf Gletscher oder Toteis (Glacier or Dead Ice covered by Till) | moraine sur glacier ou glace morte (glacier or dead ice covered by till)     |
|15101026 | fluviatiles Sediment, undifferenziert | sédiments fluviatiles, indifférenciés     |
|15101028 | glazifluviatiles Sediment, undifferenziert | sédiments fluvioglaciaires, indifférenciés     |
|15101030 | randglazialer Schotter | graviers de bordure glaciaire     |
|15101031 | glazifluviatiler Schotter | graviers fluvioglaciaires     |
|15101032 | Vorstossschotter | graviers de progression     |
|15101033 | Rückzugsschotter | graviers de retrait     |
|15101034 | Stauschotter | graviers de retenue     |
|15101035 | gemischter Schutt | dépôts mixtes     |
|15101037 | Murgangablagerung | dépôts de laves torrentielles     |
|15101039 | Alluvion, undifferenziert | alluvions, indifférenciés     |
|15101040 | fluviatiler Schotter | graviers fluviatiles     |
|15101041 | Bachschutt | dépôts torrentiels     |
|15101042 | Überschwemmungssediment | dépôts d&#39;inondation     |
|15101044 | lakustrisches Sediment, undifferenziert | sédiments lacustres, indifférenciés     |
|15101046 | glazilakustrisches Sediment, undifferenziert | dépôts glaciolacustres, indifférenciés     |
|15101047 | glazilakustrisches Deltasediment | dépôts deltaïques glaciolacustres     |
|15101048 | subaquatisch abgelagerte Moräne (Waterlaid Till) | moraine aquatique (waterlaid till)     |
|15101049 | detritische Verlandungsbildung | dépôts d&#39;atterrissement détritiques     |
|15101050 | palustrisches Sediment | sédiments palustres     |
|15101051 | palustrisches Sediment, undifferenziert | sédiments palustres, indifférenciés     |
|15101052 | Sumpf | dépôts paludéens     |
|15101053 | Torfmoor, Torf | dépôts de tourbière, tourbe     |
|15101054 | Lignit (palustrisches Sediment) | lignite (sédiment palustre)     |
|15101056 | Strandablagerungen | dépôts de terrasses lacustres     |
|15101057 | lakustrisches Deltasediment | dépôts deltaïques lacustres     |
|15101058 | Seebodensediment | sédiments de fond lacustre     |
|15101059 | Seekreide | craie lacustre     |
|15101061 | äolisches Sediment, undifferenziert | sédiments éoliens, indifférenciés     |
|15101062 | äolischer Sand, Flugsand | sable éolien     |
|15101063 | Löss, Lösslehm | loess, loess argileux     |
|15101065 | vulkanische Asche | cendres volcaniques     |
|15101067 | anthropogene Elemente, undifferenziert | éléments anthropiques, indifférenciés     |
|15101069 | künstliche Ablagerung, undifferenziert | dépôts artificiels, indifférenciés     |
|15101070 | Aufschüttung, Damm | remblai, digue     |
|15101071 | Auffüllung | comblement     |
|15101072 | Deponie | décharge     |
|15101073 | Halde | terril     |
|15101075 | dünne Lockermaterialbedeckung | couverture meuble pelliculaire     |
|15101076 | geringmächtige Lockergesteinsbedeckung | couverture de roches meubles peu épaisse     |
|15101078 | tiefgründige Verwitterungsdecke | sol d&#39;altération profonde     |
|15101079 | Gyttja | gyttja     |
|15101080 | Quelltuff (Kalksinter, Lockergestein) | tuf calcaire (dépôt non consolidé)     |
|15101081 | hydrochemische Bildungen (Kalksinter) | dépôts hydrochimiques     |
|15101082 | Travertin (Kalksinter, Lockergestein) | travertin (dépôt non consolidé)     |
|15101083 | In-situ-Verwitterungsschutt | dépôt d&#39;altération in situ     |
|15101084 | strukturierter Hangschutt | éboulis structuré     |
|15101085 | Tsunamiablagerung | dépôt de tsunami     |
|15101086 | Entwässerungssediment | sédiment formé par échappement d&#39;eau     |
|15101087 | Sedimentärer Gang (clastic dike) | filon sédimentaire     |
|15111001 | Gestein | Gestein     |
|15111002 | Gestein: sedimentär | Gestein: sedimentär     |
|15111003 | Gestein: klastisch | Gestein: klastisch     |
|15111004 | Gestein: psephitisch | Gestein: psephitisch     |
|15111005 | Brekzie | Brekzie     |
|15111006 | Brekzie: sedimentär | Brekzie: sedimentär     |
|15111007 | Brekzie: dolomitisch | Brekzie: dolomitisch     |
|15111008 | Brekzie: dolomitisch: Bitumen | Brekzie: dolomitisch: Bitumen     |
|15111009 | Brekzie: dolomitisch-polymikt | Brekzie: dolomitisch-polymikt     |
|15111010 | Brekzie: kalkig | Brekzie: kalkig     |
|15111011 | Brekzie: kalkig: Bioklasten | Brekzie: kalkig: Bioklasten     |
|15111012 | Brekzie: kalkig-dolomitisch | Brekzie: kalkig-dolomitisch     |
|15111013 | Brekzie: kalkig-polymikt | Brekzie: kalkig-polymikt     |
|15111014 | Brekzie: kristallin | Brekzie: kristallin     |
|15111015 | Brekzie: kristallin: polymikt | Brekzie: kristallin: polymikt     |
|15111016 | Brekzie: monomikt | Brekzie: monomikt     |
|15111017 | Brekzie: polymikt | Brekzie: polymikt     |
|15111018 | Brekzie: sandig | Brekzie: sandig     |
|15111019 | Brekzie: siltig | Brekzie: siltig     |
|15111020 | Brekzie: pyroklastisch | Brekzie: pyroklastisch     |
|15111021 | Brekzie: rhyolithisch | Brekzie: rhyolithisch     |
|15111022 | Brekzie: tuffitisch | Brekzie: tuffitisch     |
|15111023 | Brekzie: tektonisch | Brekzie: tektonisch     |
|15111024 | Brekzie: kakiritisch | Brekzie: kakiritisch     |
|15111025 | Brekzie: kataklastisch | Brekzie: kataklastisch     |
|15111026 | Brekzie: kataklastisch-dolomitisch | Brekzie: kataklastisch-dolomitisch     |
|15111027 | Brekzie: kataklastisch-kalkig | Brekzie: kataklastisch-kalkig     |
|15111028 | Konglomerat | Konglomerat     |
|15111029 | Konglomerat: dolomitisch | Konglomerat: dolomitisch     |
|15111030 | Konglomerat: kalkig | Konglomerat: kalkig     |
|15111031 | Konglomerat: kalkig: Muscheln | Konglomerat: kalkig: Muscheln     |
|15111032 | Konglomerat: kalkig-dolomitisch | Konglomerat: kalkig-dolomitisch     |
|15111033 | Konglomerat: kalkig-residual: Eisenpisoide | Konglomerat: kalkig-residual: Eisenpisoide     |
|15111034 | Konglomerat: kristallin | Konglomerat: kristallin     |
|15111035 | Konglomerat: monomikt | Konglomerat: monomikt     |
|15111036 | Konglomerat: ophiolithisch | Konglomerat: ophiolithisch     |
|15111037 | Konglomerat: polymikt | Konglomerat: polymikt     |
|15111038 | Konglomerat: polymikt: Bioklasten | Konglomerat: polymikt: Bioklasten     |
|15111039 | Konglomerat: polymikt: Quarz | Konglomerat: polymikt: Quarz     |
|15111040 | Konglomerat: Quarz | Konglomerat: Quarz     |
|15111041 | Konglomerat: pyroklastisch | Konglomerat: pyroklastisch     |
|15111042 | Konglomerat: tuffitisch | Konglomerat: tuffitisch     |
|15111043 | Gestein: psammitisch | Gestein: psammitisch     |
|15111044 | Sandstein | Sandstein     |
|15111045 | Sandstein: Anthrazit | Sandstein: Anthrazit     |
|15111046 | Sandstein: Bioklasten | Sandstein: Bioklasten     |
|15111047 | Sandstein: Bitumen | Sandstein: Bitumen     |
|15111048 | Sandstein: dolomitisch | Sandstein: dolomitisch     |
|15111049 | Sandstein: Eisenmineralien | Sandstein: Eisenmineralien     |
|15111050 | Sandstein: Eisenooide | Sandstein: Eisenooide     |
|15111051 | Sandstein: Feldspat | Sandstein: Feldspat     |
|15111052 | Sandstein: Glaukonit | Sandstein: Glaukonit     |
|15111053 | Sandstein: Glimmer | Sandstein: Glimmer     |
|15111054 | Sandstein: Glimmer-Glaukonit | Sandstein: Glimmer-Glaukonit     |
|15111055 | Sandstein: Gips | Sandstein: Gips     |
|15111056 | Sandstein: kalkig | Sandstein: kalkig     |
|15111057 | Sandstein: kalkig: Bioklasten | Sandstein: kalkig: Bioklasten     |
|15111058 | Sandstein: kalkig: Glaukonit | Sandstein: kalkig: Glaukonit     |
|15111059 | Sandstein: kalkig: Glimmer | Sandstein: kalkig: Glimmer     |
|15111060 | Sandstein: kalkig: Kohle | Sandstein: kalkig: Kohle     |
|15111061 | Sandstein: kalkig: Muscheln | Sandstein: kalkig: Muscheln     |
|15111062 | Sandstein: kalkig: Nummuliten | Sandstein: kalkig: Nummuliten     |
|15111063 | Sandstein: kalkig: Quarz | Sandstein: kalkig: Quarz     |
|15111064 | Sandstein: kalkig-dolomitisch | Sandstein: kalkig-dolomitisch     |
|15111065 | Sandstein: kalkig-kieselig | Sandstein: kalkig-kieselig     |
|15111066 | Sandstein: kieselig | Sandstein: kieselig     |
|15111067 | Sandstein: Kohle | Sandstein: Kohle     |
|15111068 | Sandstein: konglomeratisch | Sandstein: konglomeratisch     |
|15111069 | Sandstein: konglomeratisch-kalkig: Muscheln | Sandstein: konglomeratisch-kalkig: Muscheln     |
|15111070 | Sandstein: mergelig | Sandstein: mergelig     |
|15111071 | Sandstein: mergelig: Glaukonit | Sandstein: mergelig: Glaukonit     |
|15111072 | Sandstein: mergelig: Glimmer | Sandstein: mergelig: Glimmer     |
|15111073 | Sandstein: Phosphorit | Sandstein: Phosphorit     |
|15111074 | Sandstein: Quarz | Sandstein: Quarz     |
|15111075 | Sandstein: Quarz-Glaukonit | Sandstein: Quarz-Glaukonit     |
|15111076 | Sandstein: Quarz-Glimmer | Sandstein: Quarz-Glimmer     |
|15111077 | Sandstein: siltig | Sandstein: siltig     |
|15111078 | Sandstein: siltig-kalkig | Sandstein: siltig-kalkig     |
|15111079 | Sandstein: tonig | Sandstein: tonig     |
|15111080 | Sandstein: tonig: Feldspat | Sandstein: tonig: Feldspat     |
|15111081 | Sandstein: tonig: Glaukonit | Sandstein: tonig: Glaukonit     |
|15111082 | Sandstein: tonig: Glimmer | Sandstein: tonig: Glimmer     |
|15111083 | Sandstein: tonig: Kohle | Sandstein: tonig: Kohle     |
|15111084 | Sandstein: tonig: Lithoklasten | Sandstein: tonig: Lithoklasten     |
|15111085 | Sandstein: tonig-dolomitisch | Sandstein: tonig-dolomitisch     |
|15111086 | Sandstein: tonig-kalkig | Sandstein: tonig-kalkig     |
|15111087 | Sandstein: tonig-kalkig: Kohle | Sandstein: tonig-kalkig: Kohle     |
|15111088 | Sandstein: tuffitisch | Sandstein: tuffitisch     |
|15111089 | Gestein: pelitisch | Gestein: pelitisch     |
|15111090 | Siltstein | Siltstein     |
|15111091 | Siltstein: dolomitisch | Siltstein: dolomitisch     |
|15111092 | Siltstein: Glimmer | Siltstein: Glimmer     |
|15111093 | Siltstein: kalkig | Siltstein: kalkig     |
|15111094 | Siltstein: Kohle | Siltstein: Kohle     |
|15111095 | Siltstein: mergelig | Siltstein: mergelig     |
|15111096 | Siltstein: sandig | Siltstein: sandig     |
|15111097 | Siltstein: schiefrig | Siltstein: schiefrig     |
|15111098 | Siltstein: tonig | Siltstein: tonig     |
|15111099 | Siltstein: tonig-dolomitisch | Siltstein: tonig-dolomitisch     |
|15111100 | Siltstein: tonig-kalkig | Siltstein: tonig-kalkig     |
|15111101 | Siltstein: tuffitisch | Siltstein: tuffitisch     |
|15111102 | Tonstein | Tonstein     |
|15111103 | Tonstein: Anthrazit | Tonstein: Anthrazit     |
|15111104 | Tonstein: Bitumen | Tonstein: Bitumen     |
|15111105 | Tonstein: dolomitisch | Tonstein: dolomitisch     |
|15111106 | Tonstein: Eisenooide | Tonstein: Eisenooide     |
|15111107 | Tonstein: Glaukonit | Tonstein: Glaukonit     |
|15111108 | Tonstein: kalkig | Tonstein: kalkig     |
|15111109 | Tonstein: kalkig: Glaukonit | Tonstein: kalkig: Glaukonit     |
|15111110 | Tonstein: kieselig | Tonstein: kieselig     |
|15111111 | Tonstein: Kohle | Tonstein: Kohle     |
|15111112 | Tonstein: mergelig | Tonstein: mergelig     |
|15111113 | Tonstein: mergelig: Bitumen | Tonstein: mergelig: Bitumen     |
|15111114 | Tonstein: mergelig: Glimmer | Tonstein: mergelig: Glimmer     |
|15111115 | Tonstein: Pyrit | Tonstein: Pyrit     |
|15111116 | Tonstein: sandig | Tonstein: sandig     |
|15111117 | Tonstein: sandig: Glimmer | Tonstein: sandig: Glimmer     |
|15111118 | Tonstein: sandig: Kohle | Tonstein: sandig: Kohle     |
|15111119 | Tonstein: sandig-dolomitisch | Tonstein: sandig-dolomitisch     |
|15111120 | Tonstein: sandig-kalkig | Tonstein: sandig-kalkig     |
|15111121 | Tonstein: sandig-mergelig | Tonstein: sandig-mergelig     |
|15111122 | Tonstein: sandig-schiefrig | Tonstein: sandig-schiefrig     |
|15111123 | Tonstein: schiefrig | Tonstein: schiefrig     |
|15111124 | Tonstein: schiefrig: Anthrazit | Tonstein: schiefrig: Anthrazit     |
|15111125 | Tonstein: schiefrig: Bitumen | Tonstein: schiefrig: Bitumen     |
|15111126 | Tonstein: siltig | Tonstein: siltig     |
|15111127 | Tonstein: siltig: Glimmer | Tonstein: siltig: Glimmer     |
|15111128 | Tonstein: siltig-dolomitisch | Tonstein: siltig-dolomitisch     |
|15111129 | Tonstein: siltig-kalkig | Tonstein: siltig-kalkig     |
|15111130 | Tonstein: siltig-schiefrig | Tonstein: siltig-schiefrig     |
|15111131 | Tonstein: tuffitisch | Tonstein: tuffitisch     |
|15111132 | Mergelstein | Mergelstein     |
|15111133 | Mergelstein: Bioklasten | Mergelstein: Bioklasten     |
|15111134 | Mergelstein: Bioklasten-Ooide | Mergelstein: Bioklasten-Ooide     |
|15111135 | Mergelstein: Bitumen | Mergelstein: Bitumen     |
|15111136 | Mergelstein: dolomitisch | Mergelstein: dolomitisch     |
|15111137 | Mergelstein: Eisenooide | Mergelstein: Eisenooide     |
|15111138 | Mergelstein: Gips | Mergelstein: Gips     |
|15111139 | Mergelstein: Glaukonit | Mergelstein: Glaukonit     |
|15111140 | Mergelstein: Glaukonit-Bioklasten | Mergelstein: Glaukonit-Bioklasten     |
|15111141 | Mergelstein: Glimmer | Mergelstein: Glimmer     |
|15111142 | Mergelstein: kalkig | Mergelstein: kalkig     |
|15111143 | Mergelstein: kalkig: Bioklasten | Mergelstein: kalkig: Bioklasten     |
|15111144 | Mergelstein: kalkig: Bitumen | Mergelstein: kalkig: Bitumen     |
|15111145 | Mergelstein: kalkig-dolomitisch | Mergelstein: kalkig-dolomitisch     |
|15111146 | Mergelstein: kalkig: Eisenooide | Mergelstein: kalkig: Eisenooide     |
|15111147 | Mergelstein: kalkig: Glaukonit | Mergelstein: kalkig: Glaukonit     |
|15111148 | Mergelstein: kalkig: Ooide | Mergelstein: kalkig: Ooide     |
|15111149 | Mergelstein: kalkig-kieselig | Mergelstein: kalkig-kieselig     |
|15111150 | Mergelstein: kalkig-schiefrig | Mergelstein: kalkig-schiefrig     |
|15111151 | Mergelstein: kieselig | Mergelstein: kieselig     |
|15111152 | Mergelstein: Kohle | Mergelstein: Kohle     |
|15111153 | Mergelstein: konglomeratisch | Mergelstein: konglomeratisch     |
|15111154 | Mergelstein: Korallen | Mergelstein: Korallen     |
|15111155 | Mergelstein: Lignit | Mergelstein: Lignit     |
|15111156 | Mergelstein: Ooide | Mergelstein: Ooide     |
|15111157 | Mergelstein: Phosphorit | Mergelstein: Phosphorit     |
|15111158 | Mergelstein: sandig | Mergelstein: sandig     |
|15111159 | Mergelstein: sandig: Bioklasten | Mergelstein: sandig: Bioklasten     |
|15111160 | Mergelstein: sandig-dolomitisch | Mergelstein: sandig-dolomitisch     |
|15111161 | Mergelstein: sandig: Glaukonit | Mergelstein: sandig: Glaukonit     |
|15111162 | Mergelstein: sandig: Glimmer | Mergelstein: sandig: Glimmer     |
|15111163 | Mergelstein: sandig: Kohle | Mergelstein: sandig: Kohle     |
|15111164 | Mergelstein: sandig-kalkig | Mergelstein: sandig-kalkig     |
|15111165 | Mergelstein: sandig-siltig | Mergelstein: sandig-siltig     |
|15111166 | Mergelstein: sandig-tonig | Mergelstein: sandig-tonig     |
|15111167 | Mergelstein: sandig-tonig: Glaukonit | Mergelstein: sandig-tonig: Glaukonit     |
|15111168 | Mergelstein: schiefrig | Mergelstein: schiefrig     |
|15111169 | Mergelstein: schiefrig: Bitumen | Mergelstein: schiefrig: Bitumen     |
|15111170 | Mergelstein: siltig | Mergelstein: siltig     |
|15111171 | Mergelstein: siltig: Glaukonit | Mergelstein: siltig: Glaukonit     |
|15111172 | Mergelstein: siltig: Glimmer | Mergelstein: siltig: Glimmer     |
|15111173 | Mergelstein: siltig-dolomitisch | Mergelstein: siltig-dolomitisch     |
|15111174 | Mergelstein: siltig-kalkig | Mergelstein: siltig-kalkig     |
|15111175 | Mergelstein: siltig-schiefrig | Mergelstein: siltig-schiefrig     |
|15111176 | Mergelstein: siltig-tonig | Mergelstein: siltig-tonig     |
|15111177 | Mergelstein: tonig | Mergelstein: tonig     |
|15111178 | Mergelstein: tonig: Bitumen | Mergelstein: tonig: Bitumen     |
|15111179 | Mergelstein: tonig: Kohle | Mergelstein: tonig: Kohle     |
|15111180 | Gestein: Karbonat | Gestein: Karbonat     |
|15111181 | Gestein: sedimentär: Karbonat | Gestein: sedimentär: Karbonat     |
|15111182 | Gestein: pedogen: Karbonat | Gestein: pedogen: Karbonat     |
|15111183 | Gestein: pedogen-verkrustet: Karbonat | Gestein: pedogen-verkrustet: Karbonat     |
|15111184 | Gestein: vulkanisch: Karbonat | Gestein: vulkanisch: Karbonat     |
|15111185 | Gestein: metamorph: Karbonat | Gestein: metamorph: Karbonat     |
|15111186 | Kalkstein | Kalkstein     |
|15111187 | Kalkstein: Albit | Kalkstein: Albit     |
|15111188 | Kalkstein: Algen | Kalkstein: Algen     |
|15111189 | Kalkstein: arenitisch | Kalkstein: arenitisch     |
|15111190 | Kalkstein: arenitisch: Bioklasten | Kalkstein: arenitisch: Bioklasten     |
|15111191 | Kalkstein: arenitisch: Bioklasten-Chert | Kalkstein: arenitisch: Bioklasten-Chert     |
|15111192 | Kalkstein: arenitisch: Glaukonit | Kalkstein: arenitisch: Glaukonit     |
|15111193 | Kalkstein: arenitisch: Ooide | Kalkstein: arenitisch: Ooide     |
|15111194 | Kalkstein: arenitisch: Quarz | Kalkstein: arenitisch: Quarz     |
|15111195 | Kalkstein: arenitisch-spätig | Kalkstein: arenitisch-spätig     |
|15111196 | Kalkstein: Bioklasten | Kalkstein: Bioklasten     |
|15111197 | Kalkstein: Bioklasten-Chert | Kalkstein: Bioklasten-Chert     |
|15111198 | Kalkstein: Bioklasten-Ooide | Kalkstein: Bioklasten-Ooide     |
|15111199 | Kalkstein: Bitumen | Kalkstein: Bitumen     |
|15111200 | Kalkstein: Bitumen-Bioklasten | Kalkstein: Bitumen-Bioklasten     |
|15111201 | Kalkstein: brekziös | Kalkstein: brekziös     |
|15111202 | Kalkstein: Chert | Kalkstein: Chert     |
|15111203 | Kalkstein: dolomitisch | Kalkstein: dolomitisch     |
|15111204 | Kalkstein: dolomitisch: Bioklasten | Kalkstein: dolomitisch: Bioklasten     |
|15111205 | Kalkstein: Eisenmineralien | Kalkstein: Eisenmineralien     |
|15111206 | Kalkstein: Eisenooide | Kalkstein: Eisenooide     |
|15111207 | Kalkstein: Glaukonit | Kalkstein: Glaukonit     |
|15111208 | Kalkstein: Glaukonit-Bioklasten | Kalkstein: Glaukonit-Bioklasten     |
|15111209 | Kalkstein: kieselig | Kalkstein: kieselig     |
|15111210 | Kalkstein: kieselig: Bioklasten | Kalkstein: kieselig: Bioklasten     |
|15111211 | Kalkstein: kieselig: Bioklasten-Chert | Kalkstein: kieselig: Bioklasten-Chert     |
|15111212 | Kalkstein: kieselig: Glaukonit | Kalkstein: kieselig: Glaukonit     |
|15111213 | Kalkstein: kieselig-spätig | Kalkstein: kieselig-spätig     |
|15111214 | Kalkstein: Korallen | Kalkstein: Korallen     |
|15111215 | Kalkstein: kreidig | Kalkstein: kreidig     |
|15111216 | Kalkstein: kreidig: Bitumen | Kalkstein: kreidig: Bitumen     |
|15111217 | Kalkstein: kreidig: Chert | Kalkstein: kreidig: Chert     |
|15111218 | Kalkstein: kreidig: Pisoide | Kalkstein: kreidig: Pisoide     |
|15111219 | Kalkstein: kristallin | Kalkstein: kristallin     |
|15111220 | Kalkstein: Limonit | Kalkstein: Limonit     |
|15111221 | Kalkstein: mergelig | Kalkstein: mergelig     |
|15111222 | Kalkstein: mergelig: Bioklasten | Kalkstein: mergelig: Bioklasten     |
|15111223 | Kalkstein: mergelig: Chert | Kalkstein: mergelig: Chert     |
|15111224 | Kalkstein: mergelig: Glaukonit | Kalkstein: mergelig: Glaukonit     |
|15111225 | Kalkstein: mergelig: Pyrit | Kalkstein: mergelig: Pyrit     |
|15111226 | Kalkstein: mergelig-dolomitisch | Kalkstein: mergelig-dolomitisch     |
|15111227 | Kalkstein: mergelig-kieselig | Kalkstein: mergelig-kieselig     |
|15111228 | Kalkstein: mergelig-schiefrig | Kalkstein: mergelig-schiefrig     |
|15111229 | Kalkstein: mikritisch | Kalkstein: mikritisch     |
|15111230 | Kalkstein: mikritisch: Aptychen | Kalkstein: mikritisch: Aptychen     |
|15111231 | Kalkstein: mikritisch: Bioklasten | Kalkstein: mikritisch: Bioklasten     |
|15111232 | Kalkstein: mikritisch: Bioklasten-Chert | Kalkstein: mikritisch: Bioklasten-Chert     |
|15111233 | Kalkstein: mikritisch: Calpionellen | Kalkstein: mikritisch: Calpionellen     |
|15111234 | Kalkstein: mikritisch: Chert | Kalkstein: mikritisch: Chert     |
|15111235 | Kalkstein: mikritisch: Glaukonit | Kalkstein: mikritisch: Glaukonit     |
|15111236 | Kalkstein: mikritisch: Onkoide | Kalkstein: mikritisch: Onkoide     |
|15111237 | Kalkstein: mikritisch: Ooide | Kalkstein: mikritisch: Ooide     |
|15111238 | Kalkstein: Nummuliten | Kalkstein: Nummuliten     |
|15111239 | Kalkstein: Onkoide | Kalkstein: Onkoide     |
|15111240 | Kalkstein: Ooide | Kalkstein: Ooide     |
|15111241 | Kalkstein: Ooide-Chert | Kalkstein: Ooide-Chert     |
|15111242 | Kalkstein: pedogen-verkrustet | Kalkstein: pedogen-verkrustet     |
|15111243 | Kalkstein: Phosphorit | Kalkstein: Phosphorit     |
|15111244 | Kalkstein: Pisoide | Kalkstein: Pisoide     |
|15111245 | Kalkstein: ruditisch | Kalkstein: ruditisch     |
|15111246 | Kalkstein: ruditisch: Korallen | Kalkstein: ruditisch: Korallen     |
|15111247 | Kalkstein: sandig | Kalkstein: sandig     |
|15111248 | Kalkstein: sandig: Bioklasten | Kalkstein: sandig: Bioklasten     |
|15111249 | Kalkstein: sandig: Eisenooide | Kalkstein: sandig: Eisenooide     |
|15111250 | Kalkstein: sandig: Glaukonit | Kalkstein: sandig: Glaukonit     |
|15111251 | Kalkstein: sandig: Glimmer | Kalkstein: sandig: Glimmer     |
|15111252 | Kalkstein: sandig-kieselig | Kalkstein: sandig-kieselig     |
|15111253 | Kalkstein: sandig-spätig | Kalkstein: sandig-spätig     |
|15111254 | Kalkstein: sandig-tonig | Kalkstein: sandig-tonig     |
|15111255 | Kalkstein: Schwämme | Kalkstein: Schwämme     |
|15111256 | Kalkstein: siltig | Kalkstein: siltig     |
|15111257 | Kalkstein: siltig: Bioklasten | Kalkstein: siltig: Bioklasten     |
|15111258 | Kalkstein: siltig-tonig | Kalkstein: siltig-tonig     |
|15111259 | Kalkstein: spätig | Kalkstein: spätig     |
|15111260 | Kalkstein: spätig: Bioklasten | Kalkstein: spätig: Bioklasten     |
|15111261 | Kalkstein: spätig: Bioklasten-Chert | Kalkstein: spätig: Bioklasten-Chert     |
|15111262 | Kalkstein: spätig: Bioklasten-Glaukonit | Kalkstein: spätig: Bioklasten-Glaukonit     |
|15111263 | Kalkstein: spätig: Bioklasten-Ooide | Kalkstein: spätig: Bioklasten-Ooide     |
|15111264 | Kalkstein: spätig: Chert | Kalkstein: spätig: Chert     |
|15111265 | Kalkstein: spätig: Echinodermen | Kalkstein: spätig: Echinodermen     |
|15111266 | Kalkstein: spätig: Glaukonit | Kalkstein: spätig: Glaukonit     |
|15111267 | Kalkstein: spätig: Glaukonit-Chert | Kalkstein: spätig: Glaukonit-Chert     |
|15111268 | Kalkstein: spätig: Ooide | Kalkstein: spätig: Ooide     |
|15111269 | Kalkstein: stromatolithisch | Kalkstein: stromatolithisch     |
|15111270 | Kalkstein: stromatolithisch: Eisenmineralien-Phosphorit | Kalkstein: stromatolithisch: Eisenmineralien-Phosphorit     |
|15111271 | Kalkstein: tonig | Kalkstein: tonig     |
|15111272 | Kalkstein: tonig: Bioklasten | Kalkstein: tonig: Bioklasten     |
|15111273 | Kalkstein: tonig: Chert | Kalkstein: tonig: Chert     |
|15111274 | Kalkstein: tonig-schiefrig | Kalkstein: tonig-schiefrig     |
|15111275 | Kalkstein: tufig | Kalkstein: tufig     |
|15111276 | Tuff: kalkig | Tuff: kalkig     |
|15111277 | Dolomitstein | Dolomitstein     |
|15111278 | Dolomitstein: Bioklasten | Dolomitstein: Bioklasten     |
|15111279 | Dolomitstein: Bitumen | Dolomitstein: Bitumen     |
|15111280 | Dolomitstein: kalkig | Dolomitstein: kalkig     |
|15111281 | Dolomitstein: kieselig | Dolomitstein: kieselig     |
|15111282 | Dolomitstein: mikritisch | Dolomitstein: mikritisch     |
|15111283 | Dolomitstein: Ooide | Dolomitstein: Ooide     |
|15111284 | Dolomitstein: Ooide-Chert | Dolomitstein: Ooide-Chert     |
|15111285 | Dolomitstein: sandig | Dolomitstein: sandig     |
|15111286 | Dolomitstein: sandig-siltig | Dolomitstein: sandig-siltig     |
|15111287 | Dolomitstein: sandig-tonig | Dolomitstein: sandig-tonig     |
|15111288 | Dolomitstein: sandig-tonig: Bitumen | Dolomitstein: sandig-tonig: Bitumen     |
|15111289 | Dolomitstein: schiefrig | Dolomitstein: schiefrig     |
|15111290 | Dolomitstein: siltig | Dolomitstein: siltig     |
|15111291 | Dolomitstein: siltig-tonig | Dolomitstein: siltig-tonig     |
|15111292 | Dolomitstein: spätig | Dolomitstein: spätig     |
|15111293 | Dolomitstein: spätig: Bioklasten | Dolomitstein: spätig: Bioklasten     |
|15111294 | Dolomitstein: stromatolithisch | Dolomitstein: stromatolithisch     |
|15111295 | Dolomitstein: stromatolithisch: Chert | Dolomitstein: stromatolithisch: Chert     |
|15111296 | Dolomitstein: tonig | Dolomitstein: tonig     |
|15111297 | Rauwacke | Rauwacke     |
|15111298 | Rauwacke: sandig | Rauwacke: sandig     |
|15111299 | Rauwacke: sedimentär | Rauwacke: sedimentär     |
|15111300 | Rauwacke: kataklastisch | Rauwacke: kataklastisch     |
|15111301 | Evaporit | Evaporit     |
|15111302 | Evaporit: Anhydrit | Evaporit: Anhydrit     |
|15111303 | Evaporit: Gips | Evaporit: Gips     |
|15111304 | Evaporit: Halit | Evaporit: Halit     |
|15111305 | Evaporit: Sulfat | Evaporit: Sulfat     |
|15111306 | Evaporit: tonig | Evaporit: tonig     |
|15111307 | Evaporit: tonig: Anhydrit | Evaporit: tonig: Anhydrit     |
|15111308 | Evaporit: tonig: Gips | Evaporit: tonig: Gips     |
|15111309 | Gestein: kieselig | Gestein: kieselig     |
|15111310 | Gestein: kieselig-sedimentär | Gestein: kieselig-sedimentär     |
|15111311 | Gestein: kieselig-kryptokristallin | Gestein: kieselig-kryptokristallin     |
|15111312 | Gestein: kieselig-pedogen | Gestein: kieselig-pedogen     |
|15111313 | Gestein: kieselig: Radiolarien | Gestein: kieselig: Radiolarien     |
|15111314 | Gestein: kieselig: Schwämme | Gestein: kieselig: Schwämme     |
|15111315 | Gestein: kieselig-metamorph | Gestein: kieselig-metamorph     |
|15111316 | Gestein: Phosphorit | Gestein: Phosphorit     |
|15111317 | Gestein: organisch | Gestein: organisch     |
|15111318 | Gestein: organisch: Anthrazit | Gestein: organisch: Anthrazit     |
|15111319 | Gestein: organisch: Kohle | Gestein: organisch: Kohle     |
|15111320 | Gestein: organisch: Lignit | Gestein: organisch: Lignit     |
|15111321 | Gestein: pedogen | Gestein: pedogen     |
|15111322 | Gestein: residual | Gestein: residual     |
|15111323 | Gestein: residual: Eisenmineralien | Gestein: residual: Eisenmineralien     |
|15111324 | Gestein: residual: Silikat | Gestein: residual: Silikat     |
|15111325 | Gestein: residual: Silikat-Eisenmineralien | Gestein: residual: Silikat-Eisenmineralien     |
|15111326 | Gestein: residual-sandig | Gestein: residual-sandig     |
|15111327 | Gestein: residual-sandig: Quarz | Gestein: residual-sandig: Quarz     |
|15111328 | Gestein: residual-siltig | Gestein: residual-siltig     |
|15111329 | Gestein: residual-tonig | Gestein: residual-tonig     |
|15111330 | Gestein: residual-tonig: Eisenpisoide | Gestein: residual-tonig: Eisenpisoide     |
|15111331 | Gestein: residual-tonig: Kaolinit | Gestein: residual-tonig: Kaolinit     |
|15111332 | Gestein: residual-tonig: Limonit | Gestein: residual-tonig: Limonit     |
|15111333 | Gestein: Eisenmineralien | Gestein: Eisenmineralien     |
|15111334 | Gestein: Eisenooide | Gestein: Eisenooide     |
|15111335 | Gestein: Eisenpisoide | Gestein: Eisenpisoide     |
|15111336 | Gestein: pyroklastisch | Gestein: pyroklastisch     |
|15111337 | Ignimbrit | Ignimbrit     |
|15111338 | Tuff | Tuff     |
|15111339 | Tuff: vulkanisch | Tuff: vulkanisch     |
|15111340 | Tuff: vulkanisch: Asche | Tuff: vulkanisch: Asche     |
|15111341 | Tuff: vulkanisch: Kristalle | Tuff: vulkanisch: Kristalle     |
|15111342 | Tuff: vulkanisch: Lapilli | Tuff: vulkanisch: Lapilli     |
|15111343 | Bentonit | Bentonit     |
|15111344 | Gestein: kristallin | Gestein: kristallin     |
|15111345 | Gestein: saur | Gestein: saur     |
|15111346 | Gestein: basisch | Gestein: basisch     |
|15111347 | Gestein: magmatisch | Gestein: magmatisch     |
|15111348 | Gestein: vulkanisch | Gestein: vulkanisch     |
|15111349 | Gestein: vulkanisch: Karbonat | Gestein: vulkanisch: Karbonat     |
|15111350 | Gestein: saur-vulkanisch | Gestein: saur-vulkanisch     |
|15111351 | Gestein: rhyolithisch | Gestein: rhyolithisch     |
|15111352 | Rhyolith | Rhyolith     |
|15111353 | Rhyolith: Alkalifeldspat | Rhyolith: Alkalifeldspat     |
|15111354 | Rhyolith: ignimbritisch | Rhyolith: ignimbritisch     |
|15111355 | Rhyolith: porphyrisch | Rhyolith: porphyrisch     |
|15111356 | Gestein: dazitisch | Gestein: dazitisch     |
|15111357 | Dazit | Dazit     |
|15111358 | Dazit: rhyolithisch | Dazit: rhyolithisch     |
|15111359 | Gestein: latitisch | Gestein: latitisch     |
|15111360 | Latit | Latit     |
|15111361 | Gestein: trachytisch | Gestein: trachytisch     |
|15111362 | Trachyt | Trachyt     |
|15111363 | Trachyt: Alkalifeldspat | Trachyt: Alkalifeldspat     |
|15111364 | Gestein: andesitisch | Gestein: andesitisch     |
|15111365 | Andesit | Andesit     |
|15111366 | Gestein: basisch-vulkanisch | Gestein: basisch-vulkanisch     |
|15111367 | Gestein: basaltisch | Gestein: basaltisch     |
|15111368 | Basalt | Basalt     |
|15111369 | Basalt: Olivin | Basalt: Olivin     |
|15111370 | Basalt: verwittert: Albit | Basalt: verwittert: Albit     |
|15111371 | Gestein: phonolithisch | Gestein: phonolithisch     |
|15111372 | Phonolith | Phonolith     |
|15111373 | Phonolith: tephritisch | Phonolith: tephritisch     |
|15111374 | Gestein: tephritisch | Gestein: tephritisch     |
|15111375 | Tephrit | Tephrit     |
|15111376 | Tephrit: phonolithisch | Tephrit: phonolithisch     |
|15111377 | Basanit | Basanit     |
|15111378 | Gestein: foiditisch | Gestein: foiditisch     |
|15111379 | Foidit | Foidit     |
|15111380 | Tuffit | Tuffit     |
|15111381 | Gestein: gangartig | Gestein: gangartig     |
|15111382 | Gestein: gangartig: Quarz | Gestein: gangartig: Quarz     |
|15111383 | Gestein: saur-gangartig | Gestein: saur-gangartig     |
|15111384 | Aplit | Aplit     |
|15111385 | Pegmatit | Pegmatit     |
|15111386 | Granophyr | Granophyr     |
|15111387 | Gestein: basisch-gangartig | Gestein: basisch-gangartig     |
|15111388 | Rodingit | Rodingit     |
|15111389 | Gestein: plutonisch | Gestein: plutonisch     |
|15111390 | Gestein: granitisch | Gestein: granitisch     |
|15111391 | Granit | Granit     |
|15111392 | Granit: Alkalifeldspat | Granit: Alkalifeldspat     |
|15111393 | Granit: aplitisch | Granit: aplitisch     |
|15111394 | Granit: aplitisch: Granat | Granit: aplitisch: Granat     |
|15111395 | Granit: Biotit | Granit: Biotit     |
|15111396 | Granit: Biotit-Cordierit | Granit: Biotit-Cordierit     |
|15111397 | Granit: Biotit-Granat | Granit: Biotit-Granat     |
|15111398 | Granit: Biotit-Muskovit | Granit: Biotit-Muskovit     |
|15111399 | Granit: Hornblende | Granit: Hornblende     |
|15111400 | Granit: metasomatisch | Granit: metasomatisch     |
|15111401 | Granit: mikrokristallin | Granit: mikrokristallin     |
|15111402 | Granit: mikrokristallin-porphyrisch | Granit: mikrokristallin-porphyrisch     |
|15111403 | Granit: monzonitisch | Granit: monzonitisch     |
|15111404 | Granit: mylonitisch | Granit: mylonitisch     |
|15111405 | Granit: porphyrisch | Granit: porphyrisch     |
|15111406 | Granit: porphyrisch: Biotit | Granit: porphyrisch: Biotit     |
|15111407 | Granit: porphyrisch: Hornblende | Granit: porphyrisch: Hornblende     |
|15111408 | Granit: schiefrig | Granit: schiefrig     |
|15111409 | Granit: syenitisch | Granit: syenitisch     |
|15111410 | Granodiorit | Granodiorit     |
|15111411 | Granodiorit: aplitisch | Granodiorit: aplitisch     |
|15111412 | Granodiorit: Hornblende | Granodiorit: Hornblende     |
|15111413 | Granodiorit: porphyrisch | Granodiorit: porphyrisch     |
|15111414 | Granodiorit: schiefrig | Granodiorit: schiefrig     |
|15111415 | Monzonit | Monzonit     |
|15111416 | Monzonit: Feldspatoid | Monzonit: Feldspatoid     |
|15111417 | Monzonit: porphyrisch: Quarz | Monzonit: porphyrisch: Quarz     |
|15111418 | Monzonit: Quarz | Monzonit: Quarz     |
|15111419 | Tonalit | Tonalit     |
|15111420 | Tonalit: Biotit | Tonalit: Biotit     |
|15111421 | Tonalit: Biotit-Hornblende | Tonalit: Biotit-Hornblende     |
|15111422 | Gestein: syenitisch | Gestein: syenitisch     |
|15111423 | Syenit | Syenit     |
|15111424 | Syenit: Alkalifeldspat | Syenit: Alkalifeldspat     |
|15111425 | Syenit: Feldspatoid | Syenit: Feldspatoid     |
|15111426 | Syenit: Nephelin | Syenit: Nephelin     |
|15111427 | Syenit: porphyrisch: Quarz | Syenit: porphyrisch: Quarz     |
|15111428 | Syenit: Quarz | Syenit: Quarz     |
|15111429 | Syenit: Quarz-Hornblende | Syenit: Quarz-Hornblende     |
|15111430 | Gestein: dioritisch | Gestein: dioritisch     |
|15111431 | Diorit | Diorit     |
|15111432 | Diorit: Biotit-Hornblende | Diorit: Biotit-Hornblende     |
|15111433 | Diorit: migmatitisch | Diorit: migmatitisch     |
|15111434 | Diorit: mikrokristallin | Diorit: mikrokristallin     |
|15111435 | Diorit: monzonitisch | Diorit: monzonitisch     |
|15111436 | Diorit: porphyrisch | Diorit: porphyrisch     |
|15111437 | Diorit: Quarz | Diorit: Quarz     |
|15111438 | Diorit: Quarz-Biotit | Diorit: Quarz-Biotit     |
|15111439 | Diorit: Quarz-Epidot | Diorit: Quarz-Epidot     |
|15111440 | Diorit: Quarz-Hornblende | Diorit: Quarz-Hornblende     |
|15111441 | Diorit: schiefrig | Diorit: schiefrig     |
|15111442 | Gestein: gabbroisch | Gestein: gabbroisch     |
|15111443 | Gabbro | Gabbro     |
|15111444 | Gabbro: Hornblende | Gabbro: Hornblende     |
|15111445 | Gabbro: mikrokristallin | Gabbro: mikrokristallin     |
|15111446 | Gabbro: monzonitisch | Gabbro: monzonitisch     |
|15111447 | Gabbro: monzonitisch: Nephelin | Gabbro: monzonitisch: Nephelin     |
|15111448 | Gabbro: mylonitisch | Gabbro: mylonitisch     |
|15111449 | Gabbro: Olivin | Gabbro: Olivin     |
|15111450 | Gabbro: Omphazit | Gabbro: Omphazit     |
|15111451 | Gabbro: Orthopyroxen | Gabbro: Orthopyroxen     |
|15111452 | Gabbro: Quarz | Gabbro: Quarz     |
|15111453 | Gestein: foidolitisch | Gestein: foidolitisch     |
|15111454 | Foidolit | Foidolit     |
|15111455 | Gestein: ultramafisch | Gestein: ultramafisch     |
|15111456 | Peridotit | Peridotit     |
|15111457 | Peridotit: plutonisch | Peridotit: plutonisch     |
|15111458 | Peridotit: plutonisch: Klinopyroxen-Orthopyroxen | Peridotit: plutonisch: Klinopyroxen-Orthopyroxen     |
|15111459 | Peridotit: plutonisch: Olivin | Peridotit: plutonisch: Olivin     |
|15111460 | Peridotit: plutonisch: Olivin-Klinopyroxen | Peridotit: plutonisch: Olivin-Klinopyroxen     |
|15111461 | Peridotit: plutonisch: Olivin-Orthopyroxen | Peridotit: plutonisch: Olivin-Orthopyroxen     |
|15111462 | Peridotit: metamorph | Peridotit: metamorph     |
|15111463 | Peridotit: metamorph: Hornblende | Peridotit: metamorph: Hornblende     |
|15111464 | Peridotit: metamorph: Phlogopit | Peridotit: metamorph: Phlogopit     |
|15111465 | Peridotit: metamorph: Serpentin | Peridotit: metamorph: Serpentin     |
|15111466 | Pyroxenit | Pyroxenit     |
|15111467 | Pyroxenit: plutonisch | Pyroxenit: plutonisch     |
|15111468 | Gestein: metamorph | Gestein: metamorph     |
|15111469 | Gestein: metasomatisch | Gestein: metasomatisch     |
|15111470 | Gestein: tektonisch | Gestein: tektonisch     |
|15111471 | Kakirit | Kakirit     |
|15111472 | Kakirit: tonig | Kakirit: tonig     |
|15111473 | Kataklastit | Kataklastit     |
|15111474 | Mylonit | Mylonit     |
|15111475 | Mylonit: kalkig | Mylonit: kalkig     |
|15111476 | Mylonit: phyllitisch | Mylonit: phyllitisch     |
|15111477 | Pseudotachyllit | Pseudotachyllit     |
|15111478 | Hornfels | Hornfels     |
|15111479 | Granofels | Granofels     |
|15111480 | Granofels: Albit | Granofels: Albit     |
|15111481 | Granofels: Granat | Granofels: Granat     |
|15111482 | Granofels: Kalksilikat | Granofels: Kalksilikat     |
|15111483 | Granofels: Olivin | Granofels: Olivin     |
|15111484 | Granofels: Pyroxen | Granofels: Pyroxen     |
|15111485 | Granofels: Silikat-Karbonat | Granofels: Silikat-Karbonat     |
|15111486 | Marmor | Marmor     |
|15111487 | Marmor: dolomitisch | Marmor: dolomitisch     |
|15111488 | Marmor: dolomitisch-schiefrig | Marmor: dolomitisch-schiefrig     |
|15111489 | Marmor: kalkig | Marmor: kalkig     |
|15111490 | Marmor: kalkig: Chlorit | Marmor: kalkig: Chlorit     |
|15111491 | Marmor: kalkig: Serizit | Marmor: kalkig: Serizit     |
|15111492 | Marmor: kalkig-kieselig | Marmor: kalkig-kieselig     |
|15111493 | Marmor: Kalksilikat | Marmor: Kalksilikat     |
|15111494 | Marmor: kieselig | Marmor: kieselig     |
|15111495 | Marmor: konglomeratisch | Marmor: konglomeratisch     |
|15111496 | Marmor: konglomeratisch-kalkig | Marmor: konglomeratisch-kalkig     |
|15111497 | Marmor: metasomatisch | Marmor: metasomatisch     |
|15111498 | Marmor: sandig | Marmor: sandig     |
|15111499 | Marmor: sandig: Bioklasten | Marmor: sandig: Bioklasten     |
|15111500 | Marmor: schiefrig | Marmor: schiefrig     |
|15111501 | Marmor: Serizit | Marmor: Serizit     |
|15111502 | Marmor: Silikat | Marmor: Silikat     |
|15111503 | Marmor: tonig | Marmor: tonig     |
|15111504 | Marmor: tonig-schiefrig | Marmor: tonig-schiefrig     |
|15111505 | Quarzit | Quarzit     |
|15111506 | Quarzit: Albit | Quarzit: Albit     |
|15111507 | Quarzit: Chlorit | Quarzit: Chlorit     |
|15111508 | Quarzit: kalkig | Quarzit: kalkig     |
|15111509 | Quarzit: Serizit | Quarzit: Serizit     |
|15111510 | Gneis | Gneis     |
|15111511 | Gneis: Albit | Gneis: Albit     |
|15111512 | Gneis: Albit-Oligoklas | Gneis: Albit-Oligoklas     |
|15111513 | Gneis: Aluminosilikat | Gneis: Aluminosilikat     |
|15111514 | Gneis: Amphibol | Gneis: Amphibol     |
|15111515 | Gneis: aplitisch | Gneis: aplitisch     |
|15111516 | Gneis: augig | Gneis: augig     |
|15111517 | Gneis: augig: Phengit | Gneis: augig: Phengit     |
|15111518 | Gneis: Biotit | Gneis: Biotit     |
|15111519 | Gneis: Biotit-Hornblende | Gneis: Biotit-Hornblende     |
|15111520 | Gneis: Biotit-Muskovit | Gneis: Biotit-Muskovit     |
|15111521 | Gneis: Biotit-Plagioklas | Gneis: Biotit-Plagioklas     |
|15111522 | Gneis: Chlorit | Gneis: Chlorit     |
|15111523 | Gneis: dioritisch | Gneis: dioritisch     |
|15111524 | Gneis: gebändert | Gneis: gebändert     |
|15111525 | Gneis: gebändert: Granat | Gneis: gebändert: Granat     |
|15111526 | Gneis: Granat | Gneis: Granat     |
|15111527 | Gneis: granitisch | Gneis: granitisch     |
|15111528 | Gneis: granitisch-augig | Gneis: granitisch-augig     |
|15111529 | Gneis: granodioritisch | Gneis: granodioritisch     |
|15111530 | Gneis: granulitisch | Gneis: granulitisch     |
|15111531 | Gneis: Hornblende | Gneis: Hornblende     |
|15111532 | Gneis: Kyanit | Gneis: Kyanit     |
|15111533 | Gneis: magmatisch | Gneis: magmatisch     |
|15111534 | Gneis: magmatisch-augig | Gneis: magmatisch-augig     |
|15111535 | Gneis: magmatisch-augig: Cordierit | Gneis: magmatisch-augig: Cordierit     |
|15111536 | Gneis: metasomatisch | Gneis: metasomatisch     |
|15111537 | Gneis: migmatitisch | Gneis: migmatitisch     |
|15111538 | Gneis: migmatitisch: Cordierit | Gneis: migmatitisch: Cordierit     |
|15111539 | Gneis: migmatitisch-augig | Gneis: migmatitisch-augig     |
|15111540 | Gneis: Mikroklin | Gneis: Mikroklin     |
|15111541 | Gneis: Muskovit | Gneis: Muskovit     |
|15111542 | Gneis: mylonitisch | Gneis: mylonitisch     |
|15111543 | Gneis: Phengit | Gneis: Phengit     |
|15111544 | Gneis: phyllitisch | Gneis: phyllitisch     |
|15111545 | Gneis: psammitisch | Gneis: psammitisch     |
|15111546 | Gneis: psephitisch | Gneis: psephitisch     |
|15111547 | Gneis: psephitisch: Phengit | Gneis: psephitisch: Phengit     |
|15111548 | Gneis: schiefrig | Gneis: schiefrig     |
|15111549 | Gneis: schiefrig: Biotit | Gneis: schiefrig: Biotit     |
|15111550 | Gneis: schiefrig: Chlorit | Gneis: schiefrig: Chlorit     |
|15111551 | Gneis: schiefrig: Hornblende | Gneis: schiefrig: Hornblende     |
|15111552 | Gneis: schiefrig-augig | Gneis: schiefrig-augig     |
|15111553 | Gneis: sedimentär | Gneis: sedimentär     |
|15111554 | Gneis: Serizit | Gneis: Serizit     |
|15111555 | Gneis: Serizit-Granat | Gneis: Serizit-Granat     |
|15111556 | Granulit | Granulit     |
|15111557 | Granulit: Biotit-Granat | Granulit: Biotit-Granat     |
|15111558 | Granulit: Feldspat-Granat | Granulit: Feldspat-Granat     |
|15111559 | Migmatit | Migmatit     |
|15111560 | Migmatit: Cordierit | Migmatit: Cordierit     |
|15111561 | Phyllit | Phyllit     |
|15111562 | Phyllit: Graphit | Phyllit: Graphit     |
|15111563 | Phyllit: kalkig | Phyllit: kalkig     |
|15111564 | Phyllit: Quarz | Phyllit: Quarz     |
|15111565 | Schiefer | Schiefer     |
|15111566 | Schiefer: Aktinolith | Schiefer: Aktinolith     |
|15111567 | Schiefer: Amphibol | Schiefer: Amphibol     |
|15111568 | Schiefer: Anthrazit | Schiefer: Anthrazit     |
|15111569 | Schiefer: Antigorit | Schiefer: Antigorit     |
|15111570 | Schiefer: augig: Glimmer | Schiefer: augig: Glimmer     |
|15111571 | Schiefer: Biotit | Schiefer: Biotit     |
|15111572 | Schiefer: Biotit-Apatit | Schiefer: Biotit-Apatit     |
|15111573 | Schiefer: Chlorit | Schiefer: Chlorit     |
|15111574 | Schiefer: Chlorit-Epidot | Schiefer: Chlorit-Epidot     |
|15111575 | Schiefer: Chlorit-Talk | Schiefer: Chlorit-Talk     |
|15111576 | Schiefer: Chloritoid | Schiefer: Chloritoid     |
|15111577 | Schiefer: Chloritoid-Kyanit | Schiefer: Chloritoid-Kyanit     |
|15111578 | Schiefer: Glaukophan | Schiefer: Glaukophan     |
|15111579 | Schiefer: Glimmer | Schiefer: Glimmer     |
|15111580 | Schiefer: Glimmer-Chlorit | Schiefer: Glimmer-Chlorit     |
|15111581 | Schiefer: Glimmer-Chloritoid | Schiefer: Glimmer-Chloritoid     |
|15111582 | Schiefer: Glimmer-Granat | Schiefer: Glimmer-Granat     |
|15111583 | Schiefer: Glimmer-Graphit | Schiefer: Glimmer-Graphit     |
|15111584 | Schiefer: Glimmer-Hornblende | Schiefer: Glimmer-Hornblende     |
|15111585 | Schiefer: Granat | Schiefer: Granat     |
|15111586 | Schiefer: Graphit | Schiefer: Graphit     |
|15111587 | Schiefer: Hornblende | Schiefer: Hornblende     |
|15111588 | Schiefer: Hornblende-Granat | Schiefer: Hornblende-Granat     |
|15111589 | Schiefer: kalkig | Schiefer: kalkig     |
|15111590 | Schiefer: kalkig: Glimmer | Schiefer: kalkig: Glimmer     |
|15111591 | Schiefer: kalkig: Serizit | Schiefer: kalkig: Serizit     |
|15111592 | Schiefer: kalkig: Zoisit | Schiefer: kalkig: Zoisit     |
|15111593 | Schiefer: kieselig | Schiefer: kieselig     |
|15111594 | Schiefer: Kohle | Schiefer: Kohle     |
|15111595 | Schiefer: konglomeratisch | Schiefer: konglomeratisch     |
|15111596 | Schiefer: konglomeratisch-kalkig | Schiefer: konglomeratisch-kalkig     |
|15111597 | Schiefer: Kyanit | Schiefer: Kyanit     |
|15111598 | Schiefer: mergelig | Schiefer: mergelig     |
|15111599 | Schiefer: Muskovit-Albit | Schiefer: Muskovit-Albit     |
|15111600 | Schiefer: Quarz | Schiefer: Quarz     |
|15111601 | Schiefer: Quarz-Chlorit | Schiefer: Quarz-Chlorit     |
|15111602 | Schiefer: Quarz-Glimmer | Schiefer: Quarz-Glimmer     |
|15111603 | Schiefer: Quarz-Serizit | Schiefer: Quarz-Serizit     |
|15111604 | Schiefer: sandig | Schiefer: sandig     |
|15111605 | Schiefer: sandig-kalkig | Schiefer: sandig-kalkig     |
|15111606 | Schiefer: sandig-tonig | Schiefer: sandig-tonig     |
|15111607 | Schiefer: Serizit | Schiefer: Serizit     |
|15111608 | Schiefer: Serizit-Chlorit | Schiefer: Serizit-Chlorit     |
|15111609 | Schiefer: Serizit-Staurolith | Schiefer: Serizit-Staurolith     |
|15111610 | Schiefer: Talk | Schiefer: Talk     |
|15111611 | Schiefer: Talk-Kyanit | Schiefer: Talk-Kyanit     |
|15111612 | Schiefer: Talk-Serpentin | Schiefer: Talk-Serpentin     |
|15111613 | Schiefer: Talk-Tremolit | Schiefer: Talk-Tremolit     |
|15111614 | Schiefer: tonig | Schiefer: tonig     |
|15111615 | Schiefer: tonig: Anthrazit | Schiefer: tonig: Anthrazit     |
|15111616 | Schiefer: tonig: Bitumen | Schiefer: tonig: Bitumen     |
|15111617 | Schiefer: tonig: Graphit | Schiefer: tonig: Graphit     |
|15111618 | Schiefer: tonig-kalkig | Schiefer: tonig-kalkig     |
|15111619 | Schiefer: tonig-kieselig | Schiefer: tonig-kieselig     |
|15111620 | Schiefer: tonig-kieselig: Bitumen | Schiefer: tonig-kieselig: Bitumen     |
|15111621 | Schiefer: Tremolit | Schiefer: Tremolit     |
|15111622 | Schiefer: Turmalin | Schiefer: Turmalin     |
|15111623 | Schiefer: Zoisit | Schiefer: Zoisit     |
|15111624 | Schiefer: Zoisit-Fuchsit | Schiefer: Zoisit-Fuchsit     |
|15111625 | Gestein: mafisch | Gestein: mafisch     |
|15111626 | Prasinit | Prasinit     |
|15111627 | Prasinit: Albit-Chlorit | Prasinit: Albit-Chlorit     |
|15111628 | Prasinit: Chlorit | Prasinit: Chlorit     |
|15111629 | Prasinit: schiefrig | Prasinit: schiefrig     |
|15111630 | Amphibolit | Amphibolit     |
|15111631 | Amphibolit: gebändert | Amphibolit: gebändert     |
|15111632 | Amphibolit: Granat | Amphibolit: Granat     |
|15111633 | Amphibolit: Hornblende | Amphibolit: Hornblende     |
|15111634 | Amphibolit: migmatitisch | Amphibolit: migmatitisch     |
|15111635 | Eklogit | Eklogit     |
|15111636 | Serpentinit | Serpentinit     |
|15111637 | Serpentinit: Antigorit | Serpentinit: Antigorit     |
|15111638 | Serpentinit: brekziös: Karbonat | Serpentinit: brekziös: Karbonat     |
|15111639 | Serpentinit: Chrysotil | Serpentinit: Chrysotil     |
|999998 | nicht anwendbar | non applicable     |
|999997 | unbekannt | inconnu     |









## Annexe  GC_LITHO_UNCO_CD {#gc-litho-unco-cd}
Tables des valeurs de la description lithologique (roches meubles)

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15101001 | Lockergestein | roche meuble     |
|15101003 | gravitative Sedimente und Verwitterungsbildungen, undifferenziert | dépôts gravitaires et d&#39;altération, indifférenciés     |
|15101005 | Sturzablagerung, undifferenziert | dépôts d&#39;écroulement, d&#39;éboulement, indifférenciés     |
|15101006 | Bergsturzablagerung | dépôt d&#39;écroulement     |
|15101007 | Felssturzablagerung | dépôt d&#39;éboulement     |
|15101008 | Lawinenschutt | dépôts d&#39;avalanche     |
|15101009 | Hangschutt | éboulis     |
|15101010 | Blockschutt | amas de blocs éboulés     |
|15101012 | Verwitterungslehm, undifferenziert | limons d&#39;altération, indifférenciés     |
|15101013 | Plateaulehm | limons de plateau, éluvions     |
|15101014 | Hanglehm, Schwemmlehm | limons de pente, colluvions     |
|15101015 | Blockgletscher | glacier rocheux     |
|15101016 | zerrüttete Sackungsmasse | masse de roche tassée et disloquée     |
|15101017 | Rutschmasse | masse glissée     |
|15101019 | glazigenes Sediment, undifferenziert | sédiments glaciaires, indifférenciés     |
|15101021 | Moräne (Till), undifferenziert | moraine (till), indifférenciée     |
|15101024 | Moräne auf Gletscher oder Toteis (Glacier or Dead Ice covered by Till) | moraine sur glacier ou glace morte (glacier or dead ice covered by till)     |
|15101026 | fluviatiles Sediment, undifferenziert | sédiments fluviatiles, indifférenciés     |
|15101028 | glazifluviatiles Sediment, undifferenziert | sédiments fluvioglaciaires, indifférenciés     |
|15101030 | randglazialer Schotter | graviers de bordure glaciaire     |
|15101031 | glazifluviatiler Schotter | graviers fluvioglaciaires     |
|15101032 | Vorstossschotter | graviers de progression     |
|15101033 | Rückzugsschotter | graviers de retrait     |
|15101034 | Stauschotter | graviers de retenue     |
|15101035 | gemischter Schutt | dépôts mixtes     |
|15101037 | Murgangablagerung | dépôts de laves torrentielles     |
|15101039 | Alluvion, undifferenziert | alluvions, indifférenciés     |
|15101040 | fluviatiler Schotter | graviers fluviatiles     |
|15101041 | Bachschutt | dépôts torrentiels     |
|15101042 | Überschwemmungssediment | dépôts d&#39;inondation     |
|15101044 | lakustrisches Sediment, undifferenziert | sédiments lacustres, indifférenciés     |
|15101046 | glazilakustrisches Sediment, undifferenziert | dépôts glaciolacustres, indifférenciés     |
|15101047 | glazilakustrisches Deltasediment | dépôts deltaïques glaciolacustres     |
|15101048 | subaquatisch abgelagerte Moräne (Waterlaid Till) | moraine aquatique (waterlaid till)     |
|15101049 | detritische Verlandungsbildung | dépôts d&#39;atterrissement détritiques     |
|15101050 | palustrisches Sediment | sédiments palustres     |
|15101051 | palustrisches Sediment, undifferenziert | sédiments palustres, indifférenciés     |
|15101052 | Sumpf | dépôts paludéens     |
|15101053 | Torfmoor, Torf | dépôts de tourbière, tourbe     |
|15101054 | Lignit (palustrisches Sediment) | lignite (sédiment palustre)     |
|15101056 | Strandablagerungen | dépôts de terrasses lacustres     |
|15101057 | lakustrisches Deltasediment | dépôts deltaïques lacustres     |
|15101058 | Seebodensediment | sédiments de fond lacustre     |
|15101059 | Seekreide | craie lacustre     |
|15101061 | äolisches Sediment, undifferenziert | sédiments éoliens, indifférenciés     |
|15101062 | äolischer Sand, Flugsand | sable éolien     |
|15101063 | Löss, Lösslehm | loess, loess argileux     |
|15101065 | vulkanische Asche | cendres volcaniques     |
|15101067 | anthropogene Elemente, undifferenziert | éléments anthropiques, indifférenciés     |
|15101069 | künstliche Ablagerung, undifferenziert | dépôts artificiels, indifférenciés     |
|15101070 | Aufschüttung, Damm | remblai, digue     |
|15101071 | Auffüllung | comblement     |
|15101072 | Deponie | décharge     |
|15101073 | Halde | terril     |
|15101075 | dünne Lockermaterialbedeckung | couverture meuble pelliculaire     |
|15101076 | geringmächtige Lockergesteinsbedeckung | couverture de roches meubles peu épaisse     |
|15101078 | tiefgründige Verwitterungsdecke | sol d&#39;altération profonde     |
|15101079 | Gyttja | gyttja     |
|15101080 | Quelltuff (Kalksinter, Lockergestein) | tuf calcaire (dépôt non consolidé)     |
|15101081 | hydrochemische Bildungen (Kalksinter) | dépôts hydrochimiques     |
|15101082 | Travertin (Kalksinter, Lockergestein) | travertin (dépôt non consolidé)     |
|15101083 | In-situ-Verwitterungsschutt | dépôt d&#39;altération in situ     |
|15101084 | strukturierter Hangschutt | éboulis structuré     |
|15101085 | Tsunamiablagerung | dépôt de tsunami     |
|15101086 | Entwässerungssediment | sédiment formé par échappement d&#39;eau     |
|15101087 | Sedimentärer Gang (clastic dike) | filon sédimentaire     |
|999998 | nicht anwendbar | non applicable     |
|999997 | unbekannt | inconnu     |









## Annexe  GC_CHRONO_CD {#gc-chrono-cd}
Table des valeurs des unités chronostratigraphiques

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15001001 | Phanerozoikum | Phanérozoïque     |
|15001002 | Känozoikum | Cénozoïque     |
|15001003 | Quartär | Quaternaire     |
|15001004 | Holozän | Holocène     |
|15001005 | Pleistozän | Pléistocène     |
|15001006 | Spätes Pleistozän | Pléistocène tardif     |
|15001007 | Mittleres Pleistozän | Pléistocène moyen     |
|15001009 | Frühes Pleistozän | Pléistocène précoce     |
|15001010 | Calabrien | Calabrien     |
|15001011 | Gélasien | Gélasien     |
|15001012 | Tertiär | Tertiaire     |
|15001013 | Neogen | Néogène     |
|15001014 | Pliozän | Pliocène     |
|15001015 | Plaisancien | Plaisancien     |
|15001016 | Zancléen | Zancléen     |
|15001017 | Miozän | Miocène     |
|15001018 | Spätes Miozän | Miocène tardif     |
|15001019 | Messinien | Messinien     |
|15001020 | Tortonien | Tortonien     |
|15001021 | Mittleres Miozän | Miocène moyen     |
|15001022 | Serravallien | Serravallien     |
|15001023 | Langhien | Langhien     |
|15001024 | Frühes Miozän | Miocène précoce     |
|15001025 | Burdigalien | Burdigalien     |
|15001026 | spätes Burdigalien | Burdigalien tardif     |
|15001027 | frühes Burdigalien | Burdigalien précoce     |
|15001028 | Aquitanien | Aquitanien     |
|15001029 | Paläogen | Paléogène     |
|15001030 | Oligozän | Oligocène     |
|15001031 | Chattien | Chattien     |
|15001032 | spätes Chattien | Chattien tardif     |
|15001033 | frühes Chattien | Chattien précoce     |
|15001034 | Rupélien | Rupélien     |
|15001035 | Eozän | Eocène     |
|15001036 | Spätes Eozän | Eocène tardif     |
|15001037 | Priabonien | Priabonien     |
|15001038 | spätes Priabonien | Priabonien tardif / Latdorfien     |
|15001039 | frühes Priabonien | Priabonien précoce     |
|15001040 | Mittleres Eozän | Eocène moyen     |
|15001041 | Bartonien | Bartonien     |
|15001042 | Lutétien | Lutétien     |
|15001043 | Frühes Eozän | Eocène précoce     |
|15001044 | Yprésien | Yprésien     |
|15001045 | Paleozän | Paléocène     |
|15001046 | Thanétien | Thanétien     |
|15001047 | Sélandien | Sélandien     |
|15001048 | Danien | Danien     |
|15001049 | Mesozoikum | Mésozoïque     |
|15001050 | Kreide | Crétacé     |
|15001051 | Späte Kreide | Crétacé tardif     |
|15001052 | Maastrichtien | Maastrichtien     |
|15001053 | Campanien | Campanien     |
|15001054 | Santonien | Santonien     |
|15001055 | Coniacien | Coniacien     |
|15001056 | Turonien | Turonien     |
|15001057 | Cénomanien | Cénomanien     |
|15001058 | Frühe Kreide | Crétacé précoce     |
|15001059 | Albien | Albien     |
|15001060 | Aptien | Aptien     |
|15001061 | Barrémien | Barrémien     |
|15001062 | Hauterivien | Hauterivien     |
|15001063 | Valanginien | Valanginien     |
|15001064 | Berriasien | Berriasien     |
|15001065 | Jura | Jurassique     |
|15001066 | Später Jura | Jurassique tardif     |
|15001067 | Tithonien | Tithonien     |
|15001068 | Kimméridgien | Kimméridgien     |
|15001069 | Oxfordien | Oxfordien     |
|15001070 | Mittlerer Jura | Jurassique moyen     |
|15001071 | Callovien | Callovien     |
|15001072 | Bathonien | Bathonien     |
|15001073 | Bajocien | Bajocien     |
|15001074 | Aalénien | Aalénien     |
|15001075 | Früher Jura | Jurassique précoce     |
|15001076 | Toarcien | Toarcien     |
|15001077 | Pliensbachien | Pliensbachien     |
|15001078 | Sinémurien | Sinémurien     |
|15001079 | Hettangien | Hettangien     |
|15001080 | Trias | Trias     |
|15001081 | Späte Trias | Trias tardif     |
|15001082 | Rhät | Rhétien     |
|15001083 | Norien | Norien     |
|15001084 | Carnien | Carnien     |
|15001085 | Mittlere Trias | Trias moyen     |
|15001086 | Ladinien | Ladinien     |
|15001087 | Anisien | Anisien     |
|15001088 | Frühe Trias | Trias précoce     |
|15001089 | Olénékien | Olénékien     |
|15001090 | Indusien | Indusien     |
|15001091 | Paläozoikum | Paléozoïque     |
|15001093 | Perm | Permien     |
|15001095 | Lopingien | Lopingien     |
|15001096 | Changhsingien | Changhsingien     |
|15001098 | Wuchiapingien | Wuchiapingien     |
|15001101 | Guadalupien | Guadalupien     |
|15001102 | Capitanien | Capitanien     |
|15001106 | Wordien | Wordien     |
|15001108 | Roadien | Roadien     |
|15001110 | Cisuralien | Cisuralien     |
|15001111 | Kungurien | Kungurien     |
|15001113 | Artinskien | Artinskien     |
|15001115 | Sakmarien | Sakmarien     |
|15001117 | Asselien | Assélien     |
|15001119 | Karbon | Carbonifère     |
|15001120 | Pennsylvanien | Pennsylvanien     |
|15001121 | Spätes Pennsylvanien | Pennsylvanien tardif     |
|15001122 | Mittleres Pennsylvanien | Pennsylvanien moyen     |
|15001123 | Frühes Pennsylvanien | Pennsylvanien précoce     |
|15001124 | Mississippien | Mississippien     |
|15001125 | Spätes Mississippien | Mississippien tardif     |
|15001126 | Mittleres Mississippien | Mississippien moyen     |
|15001127 | Frühes Mississippien | Mississippien précoce     |
|15001128 | Devon | Dévonien     |
|15001129 | Frühes Devon | Dévonien tardif     |
|15001130 | Mittleres Devon | Dévonien moyen     |
|15001131 | Spätes Devon | Dévonien tardif     |
|15001133 | Silur | Silurien     |
|15001134 | Ordovizium | Ordovicien     |
|15001135 | Kambrium | Cambrien     |
|15001136 | Proterozoikum | Protérozoïque     |
|15001137 | Gzhélien | Gzhélien     |
|15001138 | Kasimovien | Kasimovien     |
|15001139 | Moscovien | Moscovien     |
|15001140 | Bashkirien | Bashkirien     |
|15001141 | Serpukhovien | Serpukhovien     |
|15001142 | Viséen | Viséen     |
|15001143 | Tournaisien | Tournaisien     |
|15001144 | Pridoli | Pridolien     |
|15001145 | Ludlow | Ludlowien     |
|15001146 | Wenlock | Wenlockien     |
|15001147 | Llandovery | Llandoveryien     |
|15001148 | Spätes Ordovizium | Spätes Ordovizium     |
|15001149 | Mittleres Ordovizium | Mittleres Ordovizium     |
|15001150 | Frühes Ordovizium | Frühes Ordovizium     |
|15001151 | Chibanien | Chibanien     |
|15001152 | Präkambrium | Präkambrium     |
|15001153 | Archaikum | Archaikum     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |









## Annexe  GC_TECTO_CD {#gc-tecto-cd}
Table des valeurs des unités tectoniques

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15309001 | Autochthones Nordalpines Vorland | Autochthones Nordalpines Vorland     |
|15309002 | Bresse-Graben | Bresse-Graben     |
|15309003 | Haute-Saône-Tafel | Haute-Saône-Tafel     |
|15309004 | Oberrhein-Graben | Oberrhein-Graben     |
|15309005 | Süddeutsche Tafel | Süddeutsche Tafel     |
|15309006 | Hegau-Bodensee-Graben | Hegau-Bodensee-Graben     |
|15309007 | Übergangszone zwischen Abgeschertem und Autochthonem Vorlandplateau | Übergangszone zwischen Abgeschertem und Autochthonem Vorlandplateau     |
|15309008 | Abgeschertes Nordalpines Vorland | Abgeschertes Nordalpines Vorland     |
|15309009 | Externer Faltenjura | Externer Faltenjura     |
|15309010 | Faisceaux | Faisceaux     |
|15309011 | Plateaux | Plateaux     |
|15309012 | Interner Faltenjura und Vorlandplateau | Interner Faltenjura und Vorlandplateau     |
|15309013 | Subalpine Molasse | Subalpine Molasse     |
|15309014 | Marbach-Berneck-Dreieckzone | Marbach-Berneck-Dreieckzone     |
|15309015 | Subalpiner Schuppenkomplex | Subalpiner Schuppenkomplex     |
|15309016 | Belmont-Schuppe | Belmont-Schuppe     |
|15309017 | Lutry-Thonon-Schuppe | Lutry-Thonon-Schuppe     |
|15309018 | Brécorens-Lucinges-Schuppe | Brécorens-Lucinges-Schuppe     |
|15309019 | Cully-Schuppe | Cully-Schuppe     |
|15309020 | Lavaux-Schuppe | Lavaux-Schuppe     |
|15309021 | Mont-Pèlerin-Schuppe | Mont-Pèlerin-Schuppe     |
|15309022 | Vevey-Evian-Schuppe | Vevey-Evian-Schuppe     |
|15309023 | Gérignoz-La-Roche-Schuppe | Gérignoz-La-Roche-Schuppe     |
|15309024 | Vaulruz-Schuppe | Vaulruz-Schuppe     |
|15309025 | Champotey-Ramsera-Schuppe | Champotey-Ramsera-Schuppe     |
|15309026 | La-Pattaz-La-Holena-Schuppe | La-Pattaz-La-Holena-Schuppe     |
|15309027 | Villarvolard-Schuppe | Villarvolard-Schuppe     |
|15309028 | Seftigschwand-Schuppe | Seftigschwand-Schuppe     |
|15309029 | Giebelegg-Schuppe | Giebelegg-Schuppe     |
|15309030 | Steffisburg-Schuppe | Steffisburg-Schuppe     |
|15309031 | Schangnau-Schuppe | Schangnau-Schuppe     |
|15309032 | Hornbüel-Schuppenzone | Hornbüel-Schuppenzone     |
|15309033 | Blueme-Beichle-Schuppe | Blueme-Beichle-Schuppe     |
|15309034 | Wolfsegg-Schuppe | Wolfsegg-Schuppe     |
|15309035 | Ralligen-Schuppenzone | Ralligen-Schuppenzone     |
|15309036 | Hilfern-Schuppe | Hilfern-Schuppe     |
|15309037 | Höhronen-Schuppe | Höhronen-Schuppe     |
|15309038 | St.-Jost-Schuppe | St.-Jost-Schuppe     |
|15309039 | Rigi-Rossberg-Schuppe | Rigi-Rossberg-Schuppe     |
|15309040 | Gäbris-Schuppe | Gäbris-Schuppe     |
|15309041 | Kronberg-Schuppe | Kronberg-Schuppe     |
|15309042 | «Zone Kronberg-Süd» | «Zone Kronberg-Süd»     |
|15309043 | Schorhüttenberg-Schuppe | Schorhüttenberg-Schuppe     |
|15309044 | Speer-Stockberg-Schuppe | Speer-Stockberg-Schuppe     |
|15309045 | Chräzerli-Schuppe | Chräzerli-Schuppe     |
|15309046 | Hirschberg-Schuppe | Hirschberg-Schuppe     |
|15309047 | Hölzliberg-Schuppe | Hölzliberg-Schuppe     |
|15309048 | Eichberg-Schuppe | Eichberg-Schuppe     |
|15309049 | Helvetikum | Helvetikum     |
|15309050 | Unterhelvetikum | Unterhelvetikum     |
|15309051 | Subalpine Flysch-Zone | Subalpine Flysch-Zone     |
|15309052 | Externe Einsiedeln-Schuppen | Externe Einsiedeln-Schuppen     |
|15309053 | Belledonne-Massiv | Belledonne-Massiv     |
|15309054 | Externes Belledonne-Massiv | Externes Belledonne-Massiv     |
|15309055 | Mittleres Belledonne-Massiv | Mittleres Belledonne-Massiv     |
|15309056 | Internes Belledonne-Massiv | Internes Belledonne-Massiv     |
|15309057 | Aiguilles-Rouges-Massiv | Aiguilles-Rouges-Massiv     |
|15309058 | Mont-Blanc-Massiv | Mont-Blanc-Massiv     |
|15309059 | Externes Mont-Blanc-Massiv | Externes Mont-Blanc-Massiv     |
|15309060 | Internes Mont-Blanc-Massiv | Internes Mont-Blanc-Massiv     |
|15309061 | Aar-Massiv | Aar-Massiv     |
|15309062 | Externes Aar-Massiv | Externes Aar-Massiv     |
|15309063 | Gastern-Teilmassiv | Gastern-Teilmassiv     |
|15309064 | Internes Aar-Massiv | Internes Aar-Massiv     |
|15309065 | Baltschieder-Gletsch-Teilmassiv | Baltschieder-Gletsch-Teilmassiv     |
|15309066 | Trun-Punteglias-Teilmassiv | Trun-Punteglias-Teilmassiv     |
|15309067 | Kaminspitz-Schuppe | Kaminspitz-Schuppe     |
|15309068 | Stelli-Schuppe | Stelli-Schuppe     |
|15309069 | Orglen-Schuppen (Aar-Massiv-Anteil) | Orglen-Schuppen (Aar-Massiv-Anteil)     |
|15309070 | Calanda-Schuppe (Aar-Massiv-Anteil) | Calanda-Schuppe (Aar-Massiv-Anteil)     |
|15309071 | Mirutta-Schuppen (Aar-Massiv-Anteil) | Mirutta-Schuppen (Aar-Massiv-Anteil)     |
|15309072 | Tschep-Schuppe | Tschep-Schuppe     |
|15309073 | Maliens-Schuppe | Maliens-Schuppe     |
|15309074 | Piz-d&#39;Artgas-Schuppe | Piz-d&#39;Artgas-Schuppe     |
|15309075 | Hoch-Fulen-Schuppe | Hoch-Fulen-Schuppe     |
|15309076 | Chaines-Subalpines-Decke | Chaines-Subalpines-Decke     |
|15309077 | Morcles-Decke | Morcles-Decke     |
|15309078 | Ardon-Decke | Ardon-Decke     |
|15309079 | Doldenhorn-Decke | Doldenhorn-Decke     |
|15309080 | Gellihorn-Decke | Gellihorn-Decke     |
|15309081 | Plammis-Decke | Plammis-Decke     |
|15309082 | Jägerchrüz-Decke | Jägerchrüz-Decke     |
|15309083 | Kammlistock-Decke | Kammlistock-Decke     |
|15309084 | Griessstock-Decke | Griessstock-Decke     |
|15309085 | Clariden-Schuppenkomplex | Clariden-Schuppenkomplex     |
|15309086 | Klausenpass-Schuppen | Klausenpass-Schuppen     |
|15309087 | Chamerstock-Schuppe | Chamerstock-Schuppe     |
|15309088 | Geisstritt-Schuppe | Geisstritt-Schuppe     |
|15309089 | Stichplatten-Schuppe | Stichplatten-Schuppe     |
|15309090 | Gemsfairen-Schuppe | Gemsfairen-Schuppe     |
|15309091 | Rotstock-Schuppe | Rotstock-Schuppe     |
|15309092 | Langfirn-Schuppe | Langfirn-Schuppe     |
|15309093 | Fiseten-Orthalden-Schuppen | Fiseten-Orthalden-Schuppen     |
|15309094 | Cavistrau-Decke | Cavistrau-Decke     |
|15309095 | Chropfsberg-Pizalun-Schuppen | Chropfsberg-Pizalun-Schuppen     |
|15309096 | Chropfsberg-Schuppe | Chropfsberg-Schuppe     |
|15309097 | Pizalun-Schuppe | Pizalun-Schuppe     |
|15309098 | Gaffia-Schuppe | Gaffia-Schuppe     |
|15309099 | Logsbach-Schuppe | Logsbach-Schuppe     |
|15309100 | Mättental-Melange | Mättental-Melange     |
|15309101 | Schabell-Melange | Schabell-Melange     |
|15309102 | Tschingelhörner-Schuppen | Tschingelhörner-Schuppen     |
|15309103 | Blattengrat-Decke | Blattengrat-Decke     |
|15309104 | Marchegghorn-Schuppe (Blattengrat-Anteil) | Marchegghorn-Schuppe (Blattengrat-Anteil)     |
|15309105 | Calanda-Schuppe (Blattengrat-Anteil) | Calanda-Schuppe (Blattengrat-Anteil)     |
|15309106 | Mirutta-Schuppe (Blattengrat-Anteil) | Mirutta-Schuppe (Blattengrat-Anteil)     |
|15309107 | Sardona-Decke | Sardona-Decke     |
|15309108 | Marchegghorn-Schuppe (Sardona-Anteil) | Marchegghorn-Schuppe (Sardona-Anteil)     |
|15309109 | Orglen-Schuppen (Sardona-Anteil) | Orglen-Schuppen (Sardona-Anteil)     |
|15309110 | Calanda-Schuppe (Sardona-Anteil) | Calanda-Schuppe (Sardona-Anteil)     |
|15309111 | Mirutta-Schuppe (Sardona-Anteil) | Mirutta-Schuppe (Sardona-Anteil)     |
|15309112 | Bad-Ragaz-Decke | Bad-Ragaz-Decke     |
|15309113 | Calanda-Schuppe (undifferenziert) | Calanda-Schuppe (undifferenziert)     |
|15309114 | Marchegghorn-Schuppe (undifferenziert) | Marchegghorn-Schuppe (undifferenziert)     |
|15309115 | Mirutta-Schuppe (undifferenziert) | Mirutta-Schuppe (undifferenziert)     |
|15309116 | Orglen-Schuppe (undifferenziert) | Orglen-Schuppe (undifferenziert)     |
|15309117 | Oberhelvetikum | Oberhelvetikum     |
|15309118 | Mont-Chétif-Decke | Mont-Chétif-Decke     |
|15309119 | Roselette-Decke | Roselette-Decke     |
|15309120 | Wildhorn-Deckenkomplex | Wildhorn-Deckenkomplex     |
|15309121 | Diablerets-Decke | Diablerets-Decke     |
|15309122 | Mont-Gond-Decke | Mont-Gond-Decke     |
|15309123 | Sublage-Decke | Sublage-Decke     |
|15309124 | Glarner Deckenkomplex | Glarner Deckenkomplex     |
|15309125 | Wageten-Schuppe | Wageten-Schuppe     |
|15309126 | Gonzen-Walenstadt-Schuppen | Gonzen-Walenstadt-Schuppen     |
|15309127 | Mürtschen-Decke | Mürtschen-Decke     |
|15309128 | Axen-Decke | Axen-Decke     |
|15309129 | Toralp-Schuppe | Toralp-Schuppe     |
|15309130 | Silberen-Schuppen | Silberen-Schuppen     |
|15309131 | Bächistock-Schuppe | Bächistock-Schuppe     |
|15309132 | Axen-Südschuppe | Axen-Südschuppe     |
|15309133 | Axen-Nordschuppe | Axen-Nordschuppe     |
|15309134 | Wissberg-Schuppe | Wissberg-Schuppe     |
|15309135 | Schächentaler Windgällen-Schuppen | Schächentaler Windgällen-Schuppen     |
|15309136 | Höch-Turm-Schuppen | Höch-Turm-Schuppen     |
|15309137 | Friteren-Schuppe | Friteren-Schuppe     |
|15309138 | Drusberg-Decke | Drusberg-Decke     |
|15309139 | Wissenwand-Schuppe | Wissenwand-Schuppe     |
|15309140 | Niederhorn-Pilatus-Schuppe | Niederhorn-Pilatus-Schuppe     |
|15309141 | Bürgenstock-Urmiberg-Schuppe | Bürgenstock-Urmiberg-Schuppe     |
|15309142 | Hochflue-Schuppe | Hochflue-Schuppe     |
|15309143 | Maisander-Schuppe | Maisander-Schuppe     |
|15309144 | Aubrig-Schuppe | Aubrig-Schuppe     |
|15309145 | Säntis-Decke | Säntis-Decke     |
|15309146 | Hohenems-Decke | Hohenems-Decke     |
|15309147 | Tavetsch-Decke | Tavetsch-Decke     |
|15309148 | Ilanz-Decke | Ilanz-Decke     |
|15309149 | Gotthard-Decke | Gotthard-Decke     |
|15309150 | Camosci-Decke | Camosci-Decke     |
|15309151 | Scopi-Decke | Scopi-Decke     |
|15309152 | Piora-Peiden-Schuppenkomplex | Piora-Peiden-Schuppenkomplex     |
|15309153 | Habkern-Melangezone | Habkern-Melangezone     |
|15309154 | Iberg-Melange | Iberg-Melange     |
|15309155 | Interne Einsiedeln-Schuppen | Interne Einsiedeln-Schuppen     |
|15309156 | Wildhaus-Melange | Wildhaus-Melange     |
|15309157 | Liebenstein-Decke | Liebenstein-Decke     |
|15309158 | Fläscherberg-Decke | Fläscherberg-Decke     |
|15309159 | Pillon-Melangezone | Pillon-Melangezone     |
|15309160 | Plaine-Morte-Melange | Plaine-Morte-Melange     |
|15309161 | Anzeinde-type slivers | Anzeinde-type slivers     |
|15309162 | Sex-Mort-type slivers | Sex-Mort-type slivers     |
|15309163 | Arveyes-type slivers | Arveyes-type slivers     |
|15309164 | Bex-Laubhorn-type slivers | Bex-Laubhorn-type slivers     |
|15309165 | Meilleret-type slivers | Meilleret-type slivers     |
|15309166 | Bulle-Melangezone | Bulle-Melangezone     |
|15309167 | Infrapräalpines Melange | Infrapräalpines Melange     |
|15309168 | Montsalvens-Schuppe | Montsalvens-Schuppe     |
|15309169 | Les-Pléiades-Schuppe | Les-Pléiades-Schuppe     |
|15309170 | Bois-de-Bouleyres-Schuppe | Bois-de-Bouleyres-Schuppe     |
|15309171 | Faucigny-Schuppen | Faucigny-Schuppen     |
|15309172 | Lepontikum | Lepontikum     |
|15309173 | Verampio-Decke | Verampio-Decke     |
|15309174 | Antigorio-Deckenkomplex | Antigorio-Deckenkomplex     |
|15309175 | Antigorio-Decke | Antigorio-Decke     |
|15309176 | Mergoscia-Zone | Mergoscia-Zone     |
|15309177 | Lebendun-Decke | Lebendun-Decke     |
|15309178 | Monte-Leone-Decke | Monte-Leone-Decke     |
|15309179 | Moncucco-Decke | Moncucco-Decke     |
|15309180 | Pizzo-del-Vallone-Decke | Pizzo-del-Vallone-Decke     |
|15309181 | Isorno-Zone | Isorno-Zone     |
|15309182 | Orselina-Bellinzona-Zone | Orselina-Bellinzona-Zone     |
|15309183 | Bosco-Zone | Bosco-Zone     |
|15309184 | Bombogno-Zone | Bombogno-Zone     |
|15309185 | Maggia-Decke | Maggia-Decke     |
|15309186 | Sambuco-Decke | Sambuco-Decke     |
|15309187 | San-Giorgio-Schuppe | San-Giorgio-Schuppe     |
|15309188 | Leventina-Lucomagno-Decke | Leventina-Lucomagno-Decke     |
|15309189 | Simano-Decke | Simano-Decke     |
|15309190 | Cima-Lunga-Decke | Cima-Lunga-Decke     |
|15309191 | Adula-Decke | Adula-Decke     |
|15309192 | Gruf-Komplex | Gruf-Komplex     |
|15309193 | Soja-Decke | Soja-Decke     |
|15309194 | Garzott-Schuppen | Garzott-Schuppen     |
|15309195 | Piz-Terri-Lunschania-Decke | Piz-Terri-Lunschania-Decke     |
|15309196 | Terri-Schuppe | Terri-Schuppe     |
|15309197 | Güida-Alpettas-Schuppen | Güida-Alpettas-Schuppen     |
|15309198 | Darlun-Schuppe | Darlun-Schuppe     |
|15309199 | Penninikum | Penninikum     |
|15309200 | Unterpenninikum | Unterpenninikum     |
|15309201 | Niesen-Decke | Niesen-Decke     |
|15309202 | Infraniesen-Melange | Infraniesen-Melange     |
|15309203 | Voirons-Decke | Voirons-Decke     |
|15309204 | Gurnigel-Decke | Gurnigel-Decke     |
|15309205 | Schlieren-Decke | Schlieren-Decke     |
|15309206 | Wägital-Decke | Wägital-Decke     |
|15309207 | Üntschen-Decke | Üntschen-Decke     |
|15309208 | Sigiswang-Decke | Sigiswang-Decke     |
|15309209 | Triesenberg-Schuppenkomplex | Triesenberg-Schuppenkomplex     |
|15309210 | Oberstdorf-Decke | Oberstdorf-Decke     |
|15309211 | Sion-Courmayeur-Decke | Sion-Courmayeur-Decke     |
|15309212 | Rosswald-Schuppe | Rosswald-Schuppe     |
|15309213 | Ferret-Schuppe | Ferret-Schuppe     |
|15309214 | Moûtiers-Schuppe | Moûtiers-Schuppe     |
|15309215 | Roignais-Versoyen-Schuppe | Roignais-Versoyen-Schuppe     |
|15309216 | Pierre-Avoi-Schuppe | Pierre-Avoi-Schuppe     |
|15309217 | Petit-St-Bernard-Schuppe | Petit-St-Bernard-Schuppe     |
|15309218 | Chiavenna-Decke | Chiavenna-Decke     |
|15309219 | Vals-Schuppen | Vals-Schuppen     |
|15309220 | Aul-Decke | Aul-Decke     |
|15309221 | Grava-Decke | Grava-Decke     |
|15309222 | Tomül-Decke | Tomül-Decke     |
|15309223 | Forbesch-Schuppe | Forbesch-Schuppe     |
|15309224 | Roz-Champatsch-Melange | Roz-Champatsch-Melange     |
|15309225 | Ramosch-Zone | Ramosch-Zone     |
|15309226 | Pfunds-Decke | Pfunds-Decke     |
|15309227 | Mittelpenninikum | Mittelpenninikum     |
|15309228 | Zone Submédiane | Zone Submédiane     |
|15309229 | Klippen-Decke | Klippen-Decke     |
|15309230 | Préalpes Médianes Plastiques | Préalpes Médianes Plastiques     |
|15309231 | Préalpes Médianes Rigides | Préalpes Médianes Rigides     |
|15309232 | Mythen-Roggenegg-Schuppe | Mythen-Roggenegg-Schuppe     |
|15309233 | Obere Rotenflue-Schuppe | Obere Rotenflue-Schuppe     |
|15309234 | Stäglerenegg-Brünnelistock-Schuppen  | Stäglerenegg-Brünnelistock-Schuppen      |
|15309235 | Brekzien-Decke | Brekzien-Decke     |
|15309236 | Zone Houillère | Zone Houillère     |
|15309237 | Zone Houillère externe | Zone Houillère externe     |
|15309238 | Zone Houillère interne | Zone Houillère interne     |
|15309239 | Visperterminen-Schuppe | Visperterminen-Schuppe     |
|15309240 | Untere Stalden-Schuppe | Untere Stalden-Schuppe     |
|15309241 | Gälmji-Zone | Gälmji-Zone     |
|15309242 | Ruginenta-Decke | Ruginenta-Decke     |
|15309243 | Ruitor-Decke | Ruitor-Decke     |
|15309244 | Obere Stalden-Decke | Obere Stalden-Decke     |
|15309245 | Berisal-Decke | Berisal-Decke     |
|15309246 | Camughera-Decke | Camughera-Decke     |
|15309247 | Siviez-Mischabel-Decke | Siviez-Mischabel-Decke     |
|15309248 | Mont-Fort-Decke | Mont-Fort-Decke     |
|15309249 | Portjengrat-Decke | Portjengrat-Decke     |
|15309250 | Stockhorn-Decke | Stockhorn-Decke     |
|15309251 | Monte-Rosa-Decke | Monte-Rosa-Decke     |
|15309252 | Tambo-Decke | Tambo-Decke     |
|15309253 | Suretta-Decke | Suretta-Decke     |
|15309254 | Schams-Deckenkomplex | Schams-Deckenkomplex     |
|15309255 | Gelbhorn-Decke | Gelbhorn-Decke     |
|15309256 | Tschera-Kalkberg-Decke | Tschera-Kalkberg-Decke     |
|15309257 | Knorren-Melange | Knorren-Melange     |
|15309258 | Martegnas-Melange | Martegnas-Melange     |
|15309259 | Areua-Bruschghorn-Melange | Areua-Bruschghorn-Melange     |
|15309260 | Falknis-Decke | Falknis-Decke     |
|15309261 | Tschingel-Schuppe | Tschingel-Schuppe     |
|15309262 | Grauspitz-Schuppe | Grauspitz-Schuppe     |
|15309263 | Glegghorn-Schuppe | Glegghorn-Schuppe     |
|15309264 | Sulzfluh-Decke | Sulzfluh-Decke     |
|15309265 | Fimber-Zone | Fimber-Zone     |
|15309266 | Tasna-Decke | Tasna-Decke     |
|15309267 | Oberpenninikum | Oberpenninikum     |
|15309268 | Gets-Decke | Gets-Decke     |
|15309269 | Simmen-Decke | Simmen-Decke     |
|15309270 | Dranses-Decke | Dranses-Decke     |
|15309271 | Saane-Decke | Saane-Decke     |
|15309272 | Antrona-Decke | Antrona-Decke     |
|15309273 | Zermatt-Saas-Fee-Decke | Zermatt-Saas-Fee-Decke     |
|15309274 | Theodulgletscher-Schuppe | Theodulgletscher-Schuppe     |
|15309275 | Mont-Emilius-Decke | Mont-Emilius-Decke     |
|15309276 | Etirol-Levaz-Schuppe | Etirol-Levaz-Schuppe     |
|15309277 | Châtillon-St-Vincent-Schuppen | Châtillon-St-Vincent-Schuppen     |
|15309278 | Châtillon-Schuppe | Châtillon-Schuppe     |
|15309279 | Pontey-Schuppe | Pontey-Schuppe     |
|15309280 | Grun-Schuppe | Grun-Schuppe     |
|15309281 | Vollon-Schuppe | Vollon-Schuppe     |
|15309282 | Gornergrat-Decke | Gornergrat-Decke     |
|15309283 | Cimes-Blanches-Decke | Cimes-Blanches-Decke     |
|15309284 | Frilihorn-Decke | Frilihorn-Decke     |
|15309285 | Tsaté-Decke | Tsaté-Decke     |
|15309286 | Avers-Decke | Avers-Decke     |
|15309287 | Malenco-Forno-Lizun-Decke | Malenco-Forno-Lizun-Decke     |
|15309288 | Platta-Decke | Platta-Decke     |
|15309289 | Arosa-Zone | Arosa-Zone     |
|15309290 | Haupterhorn-Scholle | Haupterhorn-Scholle     |
|15309291 | Weissfluh-Scholle | Weissfluh-Scholle     |
|15309292 | Gotschnawang-Scholle | Gotschnawang-Scholle     |
|15309293 | Dros-Scholle | Dros-Scholle     |
|15309294 | Totalp-Ophiolithkomplex | Totalp-Ophiolithkomplex     |
|15309295 | Salassikum | Salassikum     |
|15309296 | Mont-Mary-Decke | Mont-Mary-Decke     |
|15309297 | Untere Einheit der Mont-Mary-Decke | Untere Einheit der Mont-Mary-Decke     |
|15309298 | Obere Einheit der Mont-Mary-Decke | Obere Einheit der Mont-Mary-Decke     |
|15309299 | Roisan-Cignana-Scherzone | Roisan-Cignana-Scherzone     |
|15309300 | Dent-Blanche-Decke | Dent-Blanche-Decke     |
|15309301 | Arolla-Einheit | Arolla-Einheit     |
|15309302 | Valpelline-Einheit | Valpelline-Einheit     |
|15309303 | Sesia-Decke | Sesia-Decke     |
|15309304 | Seconda Zona Dioritico-Kinzigitica | Seconda Zona Dioritico-Kinzigitica     |
|15309305 | Gneiss-minuti-Einheit | Gneiss-minuti-Einheit     |
|15309306 | Micascisti-eclogitici-Einheit | Micascisti-eclogitici-Einheit     |
|15309307 | Margna-Decke | Margna-Decke     |
|15309308 | Forcellina-Schuppe | Forcellina-Schuppe     |
|15309309 | Sella-Decke | Sella-Decke     |
|15309310 | Ostalpin | Ostalpin     |
|15309311 | Unterostalpin | Unterostalpin     |
|15309312 | Rothorn-Schwarzhorn-Deckenkomplex | Rothorn-Schwarzhorn-Deckenkomplex     |
|15309313 | Rothorn-Decke | Rothorn-Decke     |
|15309314 | Tschirpen-Decke | Tschirpen-Decke     |
|15309315 | Schafläger-Decke | Schafläger-Decke     |
|15309316 | Dorfberg-Decke | Dorfberg-Decke     |
|15309317 | Grüenhorn-Casanna-Schuppenkomplex | Grüenhorn-Casanna-Schuppenkomplex     |
|15309318 | Grüenhorn-Schuppe | Grüenhorn-Schuppe     |
|15309319 | Casanna-Schuppe | Casanna-Schuppe     |
|15309320 | Stammerspitz-Schuppe | Stammerspitz-Schuppe     |
|15309321 | Bernina-Deckenkomplex | Bernina-Deckenkomplex     |
|15309322 | Ela-Decke | Ela-Decke     |
|15309323 | Bernina-Decke | Bernina-Decke     |
|15309324 | Müsella-Schuppe | Müsella-Schuppe     |
|15309325 | Mezzaun-Schuppe | Mezzaun-Schuppe     |
|15309326 | Madulain-Schuppen | Madulain-Schuppen     |
|15309327 | Schlattain-Clavadatsch-Padella-Schuppen | Schlattain-Clavadatsch-Padella-Schuppen     |
|15309328 | Julier-Decke | Julier-Decke     |
|15309329 | Err-Deckenkomplex | Err-Deckenkomplex     |
|15309330 | Murtiröl-Schuppe | Murtiröl-Schuppe     |
|15309331 | Err-Decke | Err-Decke     |
|15309332 | Carungas-Schuppe | Carungas-Schuppe     |
|15309333 | Corvatsch-Schuppe | Corvatsch-Schuppe     |
|15309334 | Chastelets-Schuppe | Chastelets-Schuppe     |
|15309335 | Bardella-Roccabella-Schuppen | Bardella-Roccabella-Schuppen     |
|15309336 | Oberostalpin | Oberostalpin     |
|15309337 | Campo-Deckenkomplex | Campo-Deckenkomplex     |
|15309338 | Masuccio-Decke | Masuccio-Decke     |
|15309339 | Campo-Decke | Campo-Decke     |
|15309340 | Grosina-Decke | Grosina-Decke     |
|15309341 | Laas-Decke | Laas-Decke     |
|15309342 | Vinschgau-Scherzone | Vinschgau-Scherzone     |
|15309343 | Languard-Decke | Languard-Decke     |
|15309344 | Tonale-Decke | Tonale-Decke     |
|15309345 | Ulten-Einheit | Ulten-Einheit     |
|15309346 | Krabachjoch-Decke | Krabachjoch-Decke     |
|15309347 | Inntal-Decke | Inntal-Decke     |
|15309348 | Roggenstock-Mördergruebi-Decke | Roggenstock-Mördergruebi-Decke     |
|15309349 | Lechtal-Decke | Lechtal-Decke     |
|15309350 | Madrisa-Schuppe | Madrisa-Schuppe     |
|15309351 | Schesaplana-Schuppe | Schesaplana-Schuppe     |
|15309352 | Gorvion-Schuppe | Gorvion-Schuppe     |
|15309353 | Augstenberg-Schuppe | Augstenberg-Schuppe     |
|15309354 | Ochsenkopf-Schuppe | Ochsenkopf-Schuppe     |
|15309355 | Heubühl-Schuppe | Heubühl-Schuppe     |
|15309356 | Drei-Schwestern-Schuppe | Drei-Schwestern-Schuppe     |
|15309357 | Allgäu-Decke | Allgäu-Decke     |
|15309358 | Cenoman-Randschuppe | Cenoman-Randschuppe     |
|15309359 | Schiahorn-Decke | Schiahorn-Decke     |
|15309360 | Silvretta-Decke | Silvretta-Decke     |
|15309361 | S-chanf-Schuppen | S-chanf-Schuppen     |
|15309362 | Phyllitgneiszone | Phyllitgneiszone     |
|15309363 | Ötztal-Deckenkomplex | Ötztal-Deckenkomplex     |
|15309364 | Matsch-Decke | Matsch-Decke     |
|15309365 | Umbrail-Terza-Schuppenkomplex | Umbrail-Terza-Schuppenkomplex     |
|15309366 | Umbrail-Chavalatsch-Schuppen | Umbrail-Chavalatsch-Schuppen     |
|15309367 | Terza-Schuppe | Terza-Schuppe     |
|15309368 | Quattervals-Decke | Quattervals-Decke     |
|15309369 | S-charl-Sesvenna-Decke | S-charl-Sesvenna-Decke     |
|15309370 | Tavrü-Schuppe | Tavrü-Schuppe     |
|15309371 | Ortler-Decke | Ortler-Decke     |
|15309372 | Südalpin | Südalpin     |
|15309373 | Canavese-Zone | Canavese-Zone     |
|15309374 | Ivrea-Ceneri-Komplex | Ivrea-Ceneri-Komplex     |
|15309375 | Ivrea-Zone | Ivrea-Zone     |
|15309376 | Strona-Ceneri-Zone (Ivrea-Ceneri-Anteil) | Strona-Ceneri-Zone (Ivrea-Ceneri-Anteil)     |
|15309377 | Milano-Belt | Milano-Belt     |
|15309378 | Externe Giudicarie-Zone | Externe Giudicarie-Zone     |
|15309379 | Untere Orobische Schuppen | Untere Orobische Schuppen     |
|15309380 | Interne Giudicarie-Zone | Interne Giudicarie-Zone     |
|15309381 | Obere Orobische Decke | Obere Orobische Decke     |
|15309382 | Val-Colla-Zone | Val-Colla-Zone     |
|15309383 | Strona-Ceneri-Zone (Oberer Orobischer Anteil) | Strona-Ceneri-Zone (Oberer Orobischer Anteil)     |
|15309384 | Varesotto-Schuppen | Varesotto-Schuppen     |
|15309385 | Strona-Ceneri-Zone (undifferenziert) | Strona-Ceneri-Zone (undifferenziert)     |
|15309386 | Känozoische magmatische Gesteine | Känozoische magmatische Gesteine     |
|15309387 | Vulkanische Serie des Hegaus | Vulkanische Serie des Hegaus     |
|15309388 | Periadriatische magmatische Provinz | Periadriatische magmatische Provinz     |
|15309389 | Vulkanische Serie von Biella | Vulkanische Serie von Biella     |
|15309390 | Subvulkanischer Körper vom Colle Gallo | Subvulkanischer Körper vom Colle Gallo     |
|15309391 | Subvulkanischer Körper von Gandino | Subvulkanischer Körper von Gandino     |
|15309392 | Bregaglia-Intrusionskörper | Bregaglia-Intrusionskörper     |
|15309393 | Novate-Intrusionskörper | Novate-Intrusionskörper     |
|15309394 | Adamello-Batholith | Adamello-Batholith     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |









## Annexe  GC_MINERAL_CD {#gc-mineral-cd}
Minéral important de la roche métamorphique

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|20401001 | Aktinolith | actinote     |
|20401002 | Albit | albite     |
|20401003 | Allanit | allanite     |
|20401004 | Almandin | almandin     |
|20401005 | Amphibol | amphibole     |
|20401006 | Andalusit | andalousite     |
|20401007 | Ankerit | ankérite     |
|20401008 | Anorthit | anorthite     |
|20401009 | Antigorit | antigorite     |
|20401010 | Biotit | biotite     |
|20401011 | Kalzit | calcite     |
|20401012 | Karbonatmineral | carbonate     |
|20401013 | Karpholith | carpholite     |
|20401014 | Chlorit | chlorite     |
|20401015 | Chloritoid | chloritoïde     |
|20401016 | Klinozoisit | clinozoïsite     |
|20401017 | Coesit | coésite     |
|20401018 | Cordierit | cordiérite     |
|20401019 | Diopsid | diopside     |
|20401020 | Disthen | disthène     |
|20401021 | Dolomit | dolomite     |
|20401022 | Epidot | épidote     |
|20401023 | Feldspat | feldspath     |
|20401024 | Alkalifeldspat | feldspath alcalin     |
|20401026 | Glaukophan | glaucophane     |
|20401027 | Graphit | graphite     |
|20401028 | Granat | grenat     |
|20401029 | Hornblende | hornblende     |
|20401030 | Lawsonit | lawsonite     |
|20401031 | Magnetit | magnétite     |
|20401032 | Glimmer | mica     |
|20401033 | Hellglimmer | mica blanc     |
|20401034 | Mikroklin | microcline     |
|20401035 | Muskovit | muscovite     |
|20401036 | Olivin | olivine     |
|20401037 | Omphazit | omphacite     |
|20401038 | Orthoklas | orthose     |
|20401039 | Paragonit | paragonite     |
|20401040 | Phlogopit | phlogopite     |
|20401041 | Plagioklas | plagioclase     |
|20401042 | Prehnit | préhnite     |
|20401043 | Pyrit | pyrite     |
|20401044 | Pyrop | pyrope     |
|20401045 | Pyrophyllit | pyrophyllite     |
|20401046 | Pyroxen | pyroxène     |
|20401047 | Quarz | quartz     |
|20401049 | Serpentin | serpentine     |
|20401050 | Alumosilikat | silicate d&#39;alumine     |
|20401051 | Sillimanit | sillimanite     |
|20401052 | Staurolith | staurotide     |
|20401053 | Stilpnomelan | stilpnomélane     |
|20401054 | Talk | talc     |
|20401055 | Zoisit | zoïsite     |
|20401056 | Adular | adulaire     |
|20401057 | Aegirin | aegirine     |
|20401058 | Aegirin-Augit | aegirine-augite     |
|20401059 | Andesin | andésine     |
|20401060 | Anhydrit | anhydrite     |
|20401061 | Annit | annite     |
|20401062 | Aragonit | aragonite     |
|20401063 | Augit | augite     |
|20401064 | Chrysotil | chrysotile     |
|20401065 | Grossular | grossulaire     |
|20401066 | Jadeit | jadéite     |
|20401067 | Margarit | margarite     |
|20401068 | Oligoklas | oligoclase     |
|20401069 | Orthopyroxen | orthopyroxène     |
|20401070 | Klinopyroxen | clinopyroxène     |
|20401071 | Phengit | phengite     |
|20401072 | Pumpellyit | pumpellyite     |
|20401073 | Sanidin | sanidine     |
|20401074 | Sapphirin | sapphirine     |
|20401075 | Spessartin | spessartine     |
|20401076 | Spinell | spinelle     |
|20401077 | Titanit | titanite     |
|20401078 | Tremolit | trémolite     |
|20401079 | Turmalin | tourmaline     |
|20401080 | Forsterit | forstérite     |
|20401081 | Fayalit | fayalite     |
|20401082 | Enstatit | enstatite     |
|20401083 | Zeolith | zéolithe     |
|20401084 | Serizit | séricite     |
|20401085 | Fuchsit | fuchsite     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |









## Annexe  GC_ADMIXTURE {#gc-admixture}
Incorporation

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14509008 | mit Hangschutt vermischt | mélangé à des éboulis     |
|14509010 | mit Torf | avec tourbe     |
|14509004 | mit Blöcken | avec blocs     |
|14509013 | mit Schieferkohle | mit Schieferkohle     |
|14509002 | mit Lösslehm | avec loess argileux     |
|14509011 | mit jurassischen Geröllen | avec galets jurassiens     |
|14509012 | mit Geröllen aus Vogesen / Schwarzwald | avec galets des Vosges / de la Forêt Noire     |
|14509001 | mit Löss | avec loess     |
|14509006 | mit Block- und Geschiebestreu | parsemé de blocs     |
|14509007 | mit Blockschutt vermischt | mélangé à des dépôts d&#39;éboulement     |
|14509003 | mit Seekreide | avec craie lacustre     |
|14509005 | mit alpinen Geröllen | avec galets alpins     |
|14509009 | mit Verwitterungsschutt vermischt | mélangé à des résidus d&#39;altération     |









## Annexe  GC_COMPOSIT {#gc-composit}
Composition de la roche meuble

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14508004 | sandig | sableux     |
|14508002 | lehmig | limoneux     |
|14508001 | tonig | argileux     |
|14508006 | geröllreich | riche en galets     |
|14508007 | torfig | tourbeux     |
|14508003 | siltig | silteux     |
|14508005 | kiesig | graveleux     |









## Annexe  GC_CHARCAT {#gc-charcat}
Structure sédimentaire

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14511008 | umgelagert | remanié     |
|14511010 | drainiert | drainé     |
|14511004 | verfestigt (durch Überlast), konsolidiert | consolidé (par surcharge)     |
|14511002 | rezent | récent     |
|14511011 | künstlich bewässert (Wässermatten) | inondé artificiellement (prairies irriguées)     |
|14511001 | fossil | fossile     |
|14511006 | verschwemmt | délavé     |
|14511007 | sumpfig | marécageux     |
|14511003 | verwittert | altéré     |
|14511005 | verkittet (zementiert) | cimenté     |
|14511009 | abgebaut | exploité     |









## Annexe  GC_SYSTEM {#gc-system}
Groupe de fossile

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12903008 | Holz | bois     |
|12903010 | Schwämme | éponges     |
|12903018 | Reptilien | reptiles     |
|12903004 | Foraminiferen | foraminifères     |
|12903013 | Mollusken | mollusques     |
|12903002 | Ostrakoden | ostracodes     |
|12903015 | Bivalven | bivalves     |
|12903021 | Palynomorphe | palynomorphes     |
|12903011 | Korallen | coraux     |
|12903012 | Brachiopoden | brachiopodes     |
|12903001 | Vertebraten | vertébrés     |
|12903019 | Säugetiere | mammifères     |
|12903006 | Blätter | feuilles     |
|12903007 | Gräser | graminées     |
|12903016 | Echinodermen | échinodermes     |
|12903003 | Gastropoden | gastéropodes     |
|12903005 | Algen | algues     |
|12903009 | Ammoniten | ammonites     |
|12903014 | Cephalopoden | céphalopodes     |
|12903017 | Fische | poissons     |









