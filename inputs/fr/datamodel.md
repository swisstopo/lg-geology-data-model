
# Modèle de donnée géologique, Révision 4.0.0-rc.5 #





![Extrait de Geocover et exemple de représentation](geocover.png "Figure alt text")





\pagebreak





## Thème ROCK_BODIES

### Classe Unconsolidated_Deposits_PT (Runc){#unconsolidated-deposits-pt}
La classe [Unconsolidated_Deposits_PT](#unconsolidated-deposits-pt) comprend les volumes
rocheux individualisés (de taille variable, des galets aux
blocs) qui ont été transportés par des processus
gravitaires, glaciaires ou anthropogéniques jusqu’à leur
position actuelle, ou dégagés sur place par dégradation de
la roche sous-jacente.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**STATUS**                 | [CD](#unconsolidated-deposits-pt-status)  | État du type d&#39;objet. | [1]
**ROCK_TYPE**                 | [CD](#unconsolidated-deposits-pt-rock-type)  | Type de roche. | [0..1]
**ROCK_SPE**                 | [CD](#unconsolidated-deposits-pt-rock-spe)  | Description de la roche repère. | [0..1]
**MAT_TYPE**                 | [ Table ](#gc-litho-unco-cd)  | Description du matériel (unité lithologique). | [0..1]
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
|14404001 | Vallorcine-Konglomerat | Vallorcine-Konglomerat     |
|14404002 | Allalin-Gabbro | Allalin-Gabbro     |
|14404003 | Mont-Blanc-Granit | Mont-Blanc-Granit     |
|14404004 | Serpentinit | Serpentinit     |
|14404005 | Niesen-Brekzie | Niesen-Brekzie     |
|14404006 | Hohgant-Sandstein | Hohgant-Sandstein     |
|14404007 | Grindelwald-Marmor | Grindelwald-Marmor     |
|14404008 | Aare-Granit | Aare-Granit     |
|14404009 | Gastern-Granit | Gastern-Granit     |
|14404010 | Habkern-Granit | Habkern-Granit     |
|14404011 | Windgällen-Porphyr | Windgällen-Porphyr     |
|14404012 | Glarner Verrucano | Glarner Verrucano     |
|14404013 | Kalknagelfluh des Speer- und Stockberggebietes | Kalknagelfluh des Speer- und Stockberggebietes     |
|14404014 | Ilanz-Verrucano | Ilanz-Verrucano     |
|14404015 | Mels-Sandstein | Mels-Sandstein     |
|14404016 | Taspinit-Brekzie | Taspinit-Brekzie     |
|14404017 | Albula-Granit | Albula-Granit     |
|14404018 | Punteglias-Granit | Punteglias-Granit     |
|14404019 | Rofna-Porphyr | Rofna-Porphyr     |
|14404020 | Degersheim-Kalknagelfluh | Degersheim-Kalknagelfluh     |
|14404021 | Taveyannaz-Sandstein | Taveyannaz-Sandstein     |
|14404022 | Muschelsandstein | Muschelsandstein     |
|14404023 | Karbon-Brekzie | Karbon-Brekzie     |
|14404024 | Alpines Sedimentgestein | Alpines Sedimentgestein     |
|14404025 | Molassegestein | Molassegestein     |
|14404026 | Gruontal-Konglomerat | Gruontal-Konglomerat     |
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





### Classe Unconsolidated_Deposits_PLG (Runc){#unconsolidated-deposits-plg}
La classe [Unconsolidated_Deposits_PLG](#unconsolidated-deposits-plg) contient toutes les
dépôts de roches meubles.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**LITSTRAT**                 | [ Table ](#gc-litstrat-unco-cd)  | Description lithostratigraphique. | [1]
**LITHO**                 | [ Table ](#gc-litho-cd)  | Description lithologique. | [1..3]
**CHRONO_T**                 | [ Table ](#gc-chrono-cd)  | Attribution chronostratigraphique du toit de la formation  (top). | [1]
**CHRONO_B**                 | [ Table ](#gc-chrono-cd)  | Attribution chronostratigraphique de la base de la  formation (basis). | [1]
**MAT_TYPE**                 | string                  | Description du matériel (unité lithologique) | [0..3]
**BURIED_OUT**                 | boolean                  | Est-ce que la roche consolidée est recouvert (oui / non)? | [1]
**COMPOSIT**                 | [ Table ](#gc-composit)  | Composition de la roche meuble. | [0..3]
**ADMIXTURE**                 | [ Table ](#gc-admixture)  | Incorporation. | [0..2]
**STRUCTUR**                 | [CD](#unconsolidated-deposits-plg-structur)  | Struccture de la roche meuble. | [0..1]
**CHARACT**                 | [ Table ](#gc-charcat)  | Charactéristique spécifique. | [0..3]
**MORPHOLO**                 | [CD](#unconsolidated-deposits-plg-morpholo)  | Morphologie de l’unité de roche meuble. | [0..1]
**GLAC_TYPE**                 | [CD](#unconsolidated-deposits-plg-glac-type)  | Type de glacier auquel le type d’objet est associé. Cet  attribut n’est valable que pour des moraines.. | [0..1]
**REF_YEAR**                 | string                  | Information de temps ou période. Par ex. &#34;1940-1943: année de référence
de l’ancienne ligne de rivage&#34;. | [0..1]
**THIN_COVER**                 | [CD](#unconsolidated-deposits-plg-thin-cover)  | Couverture meuble pelliculaire. | [0..1]
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

_Type de donnée :  string_





#### Attribut  BURIED_OUT
_Est-ce que la roche consolidée est recouvert (oui / non)?_

_Type de donnée :  boolean_





#### Attribut  COMPOSIT
_Composition de la roche meuble_

Voir [gc_composit](#gc-composit) dans l'annexe





#### Attribut  ADMIXTURE
_Incorporation_

Voir [gc_admixture](#gc-admixture) dans l'annexe





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

Voir [gc_charcat](#gc-charcat) dans l'annexe





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
_Information de temps ou période. Par ex. &#34;1940-1943: année de référence
de l’ancienne ligne de rivage&#34;._

_Type de donnée :  string_





#### Attribut  THIN_COVER {#unconsolidated-deposits-plg-thin-cover}
_Couverture meuble pelliculaire_


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





### Classe Bedrock_PLG (Rbed){#bedrock-plg}
La classe [Bedrock_PLG](#bedrock-plg) regroupe toutes les unités
lithostratigraphiques de roches consolidées.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**LITSTRAT**                 | [ Table ](#gc-litstrat-bed-cd)  | Description lithostratigraphique. | [1]
**LITHO**                 | [ Table ](#gc-litho-cd)  | Description lithologique. | [1]
**CHRONO_T**                 | [ Table ](#gc-chrono-cd)  | Attribution chronostratigraphique du toit de la  formation (top). | [1]
**CHRONO_B**                 | [ Table ](#gc-chrono-cd)  | Attribution chronostratigraphique de la base de la  formation (base). | [1]
**TECTO**                 | [ Table ](#gc-tecto-cd)  | Attribution tectonique. | [1]
**ORIG_DESCR**                 | string                  | Description selon la légende de la carte géologique originale | [1]
**EXOTIC_ELE**                 | boolean                  | S’agit-il d’un élément exotique (oui / non)? | [1]
**SEDI_MAIN_COM**                 | [CD](#bedrock-plg-sedi-main-com)  | Composant principal de la roche sédimentaire clastique. | [0..1]
**SEDI_SECO_COM**                 | [CD](#bedrock-plg-sedi-seco-com)  | Composant secondaire de la roche sédimentaire. | [0..2]
**SEDI_BOND_MAT**                 | [CD](#bedrock-plg-sedi-bond-mat)  | Ciment de la roche sédimentaire. | [0..1]
**SEDI_BEDDING**                 | [CD](#bedrock-plg-sedi-bedding)  | Matrice ou ciment de la roche sédimentaire. | [0..2]
**SEDI_STR**                 | [CD](#bedrock-plg-sedi-str)  | Structure sédimentaire de la roche sédimentaire. | [0..2]
**SEDI_TEX**                 | [CD](#bedrock-plg-sedi-tex)  | Texture de la roche sédimentaire. | [0..1]
**IGNE_TEX**                 | [CD](#bedrock-plg-igne-tex)  | Texture de la roche magmatique. | [0..1]
**IGNE_GRAIN_SI**                 | [CD](#bedrock-plg-igne-grain-si)  | Granulométrie de la roche magmatique. | [0..1]
**IGNE_AFFINITY**                 | [CD](#bedrock-plg-igne-affinity)  | Affinité avec une série magmatique. | [0..1]
**META_FULL_NAME**                 | string                  | Description de la roche métamorphique | [0..1]
**META_MINERAL**                 | [ Table ](#gc-mineral-cd)  | Minéral important de la roche métamorphique. | [0..3]
**META_STR**                 | [CD](#bedrock-plg-meta-str)  | Structure de la roche métamorphique. | [0..3]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14334001 | Festgestein | roche consolidée     |




#### Attribut  LITSTRAT
_Description lithostratigraphique_

Voir [GC_LITSTRAT_BED_CD](#gc-litstrat-bed-cd) dans l'annexe





#### Attribut  LITHO
_Description lithologique_

Voir [GC_LITHO_CD](#gc-litho-cd) dans l'annexe





#### Attribut  CHRONO_T
_Attribution chronostratigraphique du toit de la  formation (top)_

Voir [GC_CHRONO_CD](#gc-chrono-cd) dans l'annexe





#### Attribut  CHRONO_B
_Attribution chronostratigraphique de la base de la  formation (base)_

Voir [GC_CHRONO_CD](#gc-chrono-cd) dans l'annexe





#### Attribut  TECTO
_Attribution tectonique_

Voir [GC_TECTO_CD](#gc-tecto-cd) dans l'annexe





#### Attribut  ORIG_DESCR
_Description selon la légende de la carte géologique originale_

_Type de donnée :  string_





#### Attribut  EXOTIC_ELE
_S’agit-il d’un élément exotique (oui / non)?_

_Type de donnée :  boolean_





#### Attribut  SEDI_MAIN_COM {#bedrock-plg-sedi-main-com}
_Composant principal de la roche sédimentaire clastique_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15602001 | Gesteinsbruchstück undifferenziert | fragments de roches indifférenciés     |
|15602002 | kieselige Gesteine (Quarzit, Quarz (Mineralisch), Radiolarit, Kieselkalk, Quarzsandstein, Hornstein) | roches siliceuses (quartzite, quartz (minéral), radiolarite, calcaire siliceux, grès siliceux, silex)     |
|15602003 | Sedimentgestein undifferenziert | roche sédimentaire indifférenciée     |
|15602004 | Tonstein | argilite     |
|15602005 | Kalkstein | roche calcaire     |
|15602006 | Dolomitstein | roche dolomitique     |
|15602007 | Kristallingestein undifferenziert | roche cristalline indifférenciée     |
|15602008 | Vulkanit | roche volcanique     |
|15602009 | Metamorphit | roche métamorphique     |
|15602010 | Mergelstein | marne     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  SEDI_SECO_COM {#bedrock-plg-sedi-seco-com}
_Composant secondaire de la roche sédimentaire_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|20001001 | Gesteinsbruchstück undifferenziert | fragments de roches indifférenciées     |
|20001002 | Sedimentgestein undifferenziert | roche sédimentaire indifférenciée     |
|20001003 | Tonstein | argilite     |
|20001004 | Kalkstein | roche calcaire     |
|20001005 | Dolomitstein | roche dolomitique     |
|20001006 | Kristallingestein undifferenziert | roche cristalline indifférenciée     |
|20001007 | Vulkanit | roche volcanique     |
|20001008 | Metamorphit | roche métamorphique     |
|20001009 | Quarzit | quartzite     |
|20001010 | pyroklastische Komponenten | composants pyroclastiques     |
|20001011 | Quarz | quartz     |
|20001012 | Feldspat | feldspath     |
|20001013 | Glaukonit | glauconite     |
|20001014 | Glimmer | mica     |
|20001015 | intraformationelle Gerölle | galets intraformationnels     |
|20001016 | Kalkkonkretionen | rognons de calcaire     |
|20001017 | Sideritkonkretionen | rognons de sidérite     |
|20001018 | Silexkonkretionen | rognons de silex     |
|20001019 | biogene Komponenten | composants biogènes     |
|20001020 | terrigener Detritus | débris terrigènes     |
|20001021 | Phosphorit | phosphorite     |
|20001022 | Mergelstein | marne     |
|20001023 | Kohle | charbon     |
|20001024 | Bitumen | bitume     |
|20001025 | Evaporit | évaporite     |
|20001026 | Eisenmineralien | minéraux de fer     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  SEDI_BOND_MAT {#bedrock-plg-sedi-bond-mat}
_Ciment de la roche sédimentaire_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14313001 | kalkiger Zement | ciment calcaire     |
|14313002 | dolomitischer Zement | ciment dolomitique     |
|14313003 | kieseliger Zement | ciment siliceux     |
|14313004 | tonige Matrix | matrice argileuse     |
|14313005 | siltige Matrix | matrice silteuse     |
|14313006 | sandige Matrix | matrice sableuse     |
|14313007 | kalkige Matrix | matrice calcaire     |
|14313008 | dolomitische Matrix | matrice dolomitique     |
|14313009 | organische Imprägnierung (Asphalt) | imprégnation de matière organique (asphalte)     |
|14313010 | mineralische Imprägnierung | imprégnation minérale     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  SEDI_BEDDING {#bedrock-plg-sedi-bedding}
_Matrice ou ciment de la roche sédimentaire_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|20101001 | massig | massif     |
|20101002 | gebankt | lité     |
|20101003 | dickbankig (&gt;30cm) | en gros bancs     |
|20101004 | dünnbankig (1-10cm) | en petits bancs     |
|20101005 | blätterig | feuilleté     |
|20101006 | knauerig | concrétionné     |
|20101007 | knollig | noduleux     |
|20101008 | linsenförmig | lenticulaire     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  SEDI_STR {#bedrock-plg-sedi-str}
_Structure sédimentaire de la roche sédimentaire_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|20201001 | texturlos | sans structure     |
|20201002 | geschichtet | stratifié     |
|20201003 | schräg-/kreuzgeschichtet | stratification oblique/entrecroisée     |
|20201004 | laminiert | laminé     |
|20201005 | normal gradiert | granoclassement normal     |
|20201006 | invers gradiert | granoclassement inverse     |
|20201007 | bioturbiert | bioturbé     |
|20201008 | stromatolitisch | stromatolitique     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  SEDI_TEX {#bedrock-plg-sedi-tex}
_Texture de la roche sédimentaire_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|20301001 | monomikt | monomicte     |
|20301002 | polymikt | polymicte     |
|20301003 | mikritisch | micritique     |
|20301004 | spätig | spathique     |
|20301005 | bioklastisch | bioclastique     |
|20301007 | onkolithisch | oncolitique     |
|20301008 | oolithisch | oolitique     |
|20301009 | pelitisch | pélitique     |
|20301010 | pisolithisch | pisolitique     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  IGNE_TEX {#bedrock-plg-igne-tex}
_Texture de la roche magmatique_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14317001 | gleichkörnig | équigranulaire     |
|14317002 | ungleichkörnig | hétérogranulaire     |
|14317003 | porphyrisch | porphyrique     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  IGNE_GRAIN_SI {#bedrock-plg-igne-grain-si}
_Granulométrie de la roche magmatique_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14318001 | grobkörnig | grossière     |
|14318002 | feinkörnig | fine     |
|14318003 | aphanitisch | aphanitique     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  IGNE_AFFINITY {#bedrock-plg-igne-affinity}
_Affinité avec une série magmatique_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15733001 | alkalisch | alcalin     |
|15733002 | kalkalkalisch | calco-alcalin     |
|15733003 | tholeiitisch | tholéitique     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |




#### Attribut  META_FULL_NAME
_Description de la roche métamorphique_

_Type de donnée :  string_





#### Attribut  META_MINERAL
_Minéral important de la roche métamorphique_

Voir [GC_MINERAL_CD](#gc-mineral-cd) dans l'annexe





#### Attribut  META_STR {#bedrock-plg-meta-str}
_Structure de la roche métamorphique_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|20501001 | massig | massif     |
|20501002 | gebändert | rubané     |
|20501003 | augig | oeillé     |
|20501004 | mit Schollen | enclaves     |
|20501005 | schiefrig | schisteux     |
|20501006 | phyllitisch | phylliteux     |
|20501007 | laminiert | laminé     |
|20501008 | lagig | stratifié     |
|20501009 | plattig | plaqueté     |
|20501010 | gebankt | lité     |
|20501011 | gefältelt | plissoté     |
|20501012 | geadert | veiné     |
|20501013 | schlierig | schlieren     |
|20501014 | linsig | lenticulaire     |
|20501015 | flaserig | structure flaser     |
|20501016 | agmatitisch (migmatitisch) | agmatitique     |
|20501017 | brekziös | bréchique     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |








## Thème GEOMORPHOLOGY

### Classe Instability_Structures_PT (Gins){#instability-structures-pt}
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




### Classe Instability_Structures_L (Gins){#instability-structures-l}
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




### Classe Instabilities_PLG (Gins){#instabilities-plg}
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
**MAIN_MOV**                 | [CD](#instabilities-plg-main-mov)  | Phase de mouvement principale. | [0..1]





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




### Classe Glacial_Structures_PT (Ggla){#glacial-structures-pt}
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
|11201001 | glazitektonische Deformation | déformation glaciotectonique     |
|11201002 | Gletschermühle, Strudelloch | marmite glaciaire, cavité d´érosion     |




### Classe Glacial_and_Periglacial_Structures_L (Ggla){#glacial-and-periglacial-structures-l}
La classe [Glacial_and_Periglacial_Structures_L](#glacial-and-periglacial-structures-l) contient des
structures linéaires qui indiquent un milieu de formation
glaciaire ou périglaciaire.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**MORAI_MO**                 | [CD](#glacial-and-periglacial-structures-l-morai-mo)  | Morphologie de la moraine. | [0..1]
**GLAC_TYP**                 | [CD](#glacial-and-periglacial-structures-l-glac-typ)  | Type de glacier auquel le type d’objet est associé. | [0..1]
**ICE_M_P**                 | [CD](#glacial-and-periglacial-structures-l-ice-m-p)  | Stade glaciaire. | [0..1]
**QUAT_STR**                 | [CD](#glacial-and-periglacial-structures-l-quat-str)  | Attribution chronostratigraphique du vallum morainique au sein du Quaternaire. | [0..1]
**REF_YEAR**                 | integer                  | Année de référence. | [0..1]
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
|11304045 | Staffelbach-Stand | Staffelbach-Stand     |
|11304046 | Zürich I | Zürich I     |
|11304047 | Zürich II | Zürich II     |
|11304048 | Schlieren I | Schlieren I     |
|11304049 | Schlieren II | Schlieren II     |
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





### Classe Glacial_Structures_PLG (Ggla){#glacial-structures-plg}
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




### Classe Erosional_Structures_PT (Gero){#erosional-structures-pt}
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




### Classe Erosional_Structures_L (Gero){#erosional-structures-l}
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




### Classe Karstic_Structures_PT (Gkar){#karstic-structures-pt}
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




#### Attribut  ICE_CAVE
_S’agit-il d’une glacière (oui / non)_

_Type de donnée :  boolean_





### Classe Karstic_Structures_PLG (Gkar){#karstic-structures-plg}
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




### Classe Alluvial_and_Lacustrine_Structures_L (Gall){#alluvial-and-lacustrine-structures-l}
La classe [Alluvial_and_Lacustrine_Structures_L](#alluvial-and-lacustrine-structures-l) contient les
morphologies linéaires d’origine fluviatile ou lacustre.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**AGE**                 | [CD](#alluvial-and-lacustrine-structures-l-age)  | Âge du type d&#39;obje. | [0..1]





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








## Thème TECTONICS

### Classe Deformation_Structures_PT (Tdef){#deformation-structures-pt}
La classe [Deformation_Structures_PT](#deformation-structures-pt) contient des structures
de déformation tectonique observées ponctuellement, telles
que des endroits localement très plissés (plissotement) ou
des endroits avec une fissuration marquée. Cette classe
contient également des points construits, tels que
l&#39;orientation de la surface de l&#39;axe des plis.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**AZIMUTH**                 | integer                  | Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles  d&#39;une montre | [0..1]
**DIP**                 | integer                  | Valeur du plongement du type d&#39;&#39;objet (valeur en degrés, mesurée de l’horizontale
(0°) vers le bas jusqu’à la verticale (90°)) | [0..1]
**FOLD_TYP**                 | [CD](#deformation-structures-pt-fold-typ)  | Caractéristique du type d&#39;objet. | [0..1]
**FOLD_FOR**                 | [CD](#deformation-structures-pt-fold-for)  | Forme du type d&#39;objet. | [0..1]





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




### Classe Deformation_Structures_L (Tdef){#deformation-structures-l}
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




### Classe Deformation_Structures_PLG (Tdef){#deformation-structures-plg}
Dans la classe [Deformation_Structures_PLG](#deformation-structures-plg) se trouvent les
régions marquées par des structures tectoniques à grande
échelle comme les zones tectonisées ou les zones diaclasées.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**TYPE**                 | [CD](#deformation-structures-plg-type)  | Caractéristique du type d&#39;objet. | [0..1]





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




### Classe Tectonic_Boundaries_L (Ttec){#tectonic-boundaries-l}
La classe [Tectonic_Boundaries_L](#tectonic-boundaries-l) comprend toutes les
accidents tectoniques.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**FAULT_MO**                 | [CD](#tectonic-boundaries-l-fault-mo)  | Mouvement de la faille. | [0..1]
**VERTI_MO**                 | [CD](#tectonic-boundaries-l-verti-mo)  | Mouvement parallèle au pendage du plan de faille. | [0..1]
**HORIZ_MO**                 | [CD](#tectonic-boundaries-l-horiz-mo)  | Mouvement parallèle à la direction du plan de faille ou de cisaillement. | [0..1]
**LIM_TYP**                 | [CD](#tectonic-boundaries-l-lim-typ)  | Type de limite tectonique. | [1]
**HIERA**                 | [CD](#tectonic-boundaries-l-hiera)  | Hiérarchie de l&#39;accident tectonique. | [1]
**STATUS**                 | [CD](#tectonic-boundaries-l-status)  | État du type d&#39;objet. | [1]
**META_STA**                 | [CD](#tectonic-boundaries-l-meta-sta)  | Chronologie tecto-métamorphique du type d’objet. | [0..1]
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
|14903001 | aufschiebend | aufschiebend     |
|14903002 | abschiebend | abschiebend     |
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
|14911001 | Störung | Störung     |
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









## Thème MEASUREMENTS_SPATIAL_ORIENTATION

### Classe Folds_PT (Mfol){#folds-pt}
La classe [Folds_PT](#folds-pt) contient les objets qui décrivent la
position spatiale d’objets géologiques plissés (par des
mesures prises directement sur le terrain).




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**FOLD_TYP**                 | [CD](#folds-pt-fold-typ)  | Type de pli. | [0..1]
**FOLD_FOR**                 | [CD](#folds-pt-fold-for)  | Forme du type de pli. | [0..1]
**PHASE**                 | [CD](#folds-pt-phase)  | Phase de déformation. | [0..1]
**PHASE_REF**                 | string                  | Référence pour les données concernant la phase de déformation | [0..1]
**AZIMUTH**                 | integer                  | Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles  d&#39;une montre. | [1]
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





### Classe Lineation_PT (Mlin){#lineation-pt}
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





### Classe Planar_Structures_PT (Mpla){#planar-structures-pt}
La classe [Planar_Structures_PT](#planar-structures-pt) contient des types d&#39;objets
qui décrivent la position des structures planaires avec des
mesures directes sur le terrain.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**POLARITY**                 | [CD](#planar-structures-pt-polarity)  | Polarité du type d&#39;objet dans l&#39;espace. | [0..1]
**PHASE**                 | [CD](#planar-structures-pt-phase)  | Phase de déformation. | [0..1]
**PHASE_REF**                 | string                  | Référence pour les données concernant la phase de déformation | [0..1]
**OB_DIP_SLO**                 | boolean                  | Dip slope (oui / non)? | [0..1]
**AZIMUTH**                 | integer                  | Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles  d&#39;une montre | [1]
**DIP**                 | integer                  | Valeur du plongement du type d&#39;objet (en degrés), mesurée de l’horizontale (0°) vers le bas jusqu’à la  verticale (90°) | []





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13801001 | Orientierung der Schichten | orientation des couches     |
|13801002 | Orientierung eines Ganges | orientation d&#39;un filon     |
|13801003 | Orientierung einer Bruchfläche | orientation d&#39;un plan de faille     |
|13801004 | Orientierung der Schieferung | orientation d&#39;une schistosité     |
|13801005 | Orientierung einer Schichtung oder Schieferung | orientation d&#39;une couche ou d&#39;une schistosité     |
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









## Thème LOCAL_ADDITIONAL_INFORMATION

### Classe Anomalies_PT (Lano){#anomalies-pt}
La classe [Anomalies_PT](#anomalies-pt) contient des anomalies observées et /
ou mesurées localement.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**TYPE**                 | [CD](#anomalies-pt-type)  | Caractéristique du type d&#39;objet. | []





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




### Classe Fossils_PT (Lfos){#fossils-pt}
La classe [Fossils_PT](#fossils-pt) contient tous les gisements
fossilifères




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**DIVISION**                 | [CD](#fossils-pt-division)  | Catégorie de fossile à laquelle appartient l&#39;objet. | [0..1]
**SYSTEM**                 | [ Table ](#gc-system)  | Groupe de fossiles. | [0..5]
**DAT_METH**                 | [CD](#fossils-pt-dat-meth)  | Méthode de datation. | [0..1]
**STATUS**                 | [CD](#fossils-pt-status)  | État du type d&#39;objet. | [0..1]
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

Voir [gc_system](#gc-system) dans l'annexe





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





### Classe Indication_of_Resources_PT (Lind){#indication-of-resources-pt}
La classe [Indication_of_Resources_PT](#indication-of-resources-pt) regroupe les gisements
de minéraux, de gaz, d’hydrocarbures et de matériel
volcanique




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**STATUS**                 | [CD](#indication-of-resources-pt-status)  | Etat du type d&#39;objet. | [0..1]
**MATERIAL**                 | [CD](#indication-of-resources-pt-material)  | Matériau associé au type d&#39;objet. | [0..1]
**CHEMISTRY**                 | string                  | Composant(s) chimique(s) caractérisant la nature du type d&#39;objet | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13201001 | Mineralfundstelle | gisement de minéraux     |
|13201002 | Gasquelle | source de gaz naturel     |
|13201003 | Anzeichen auf Öl | indices de pétrole     |
|13201004 | Tasche, Karsttasche, Kluft, mit Füllung von siderolithischem Sediment | poche, poche karstique, fissure, remplie de matériel sidérolithique     |
|13201005 | Fundstelle von vulkanischem Tuffit | gisement de tuffite volcanique     |
|13201006 | Fundstelle vulkanischer Auswürflinge (Tephra) | gisement de projections volcaniques (tephra)     |
|13201007 | Fundstelle von Ries-Auswürflingen | gisement de projections du Ries     |
|13201008 | Asphalt, vereinzeltes Vorkommen | asphalte, gisement isolé     |
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





### Classe Mineralised_Zone_L (Lmin){#mineralised-zone-l}
La classe [Mineralised_Zone_L](#mineralised-zone-l) contient les zones
minéralisées.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**CHEMISTRY**                 | string                  | Composant(s) chimique(s) caractérisant la nature du type d&#39;objet. | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13301001 | Vererzungszone | zone minéralisée     |




#### Attribut  CHEMISTRY
_Composant(s) chimique(s) caractérisant la nature du type d&#39;objet._

_Type de donnée :  string_





### Classe Sedimentary_Structures_PT (Lsed){#sedimentary-structures-pt}
La classe [Sedimentary_Structures_PT](#sedimentary-structures-pt) contient la description
des structures sédimentaires observées.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**AZIMUTH**                 | integer                  | Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles  d&#39;une montre. | [0..1]





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





### Classe Type_Localities_PT (Ltyp){#type-localities-pt}
La classe [Type_Localities_PT](#type-localities-pt) regroupe les types d’objets qui
décrivent les profiles-types ou les affleurements
géologiques importants.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**STRATI**                 | [CD](#type-localities-pt-strati)  | Complément lithostratigraphique du type d&#39;objet. | [0..1]
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





### Classe Prominent_Lithological_Features_L (Lpro){#prominent-lithological-features-l}
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
**CONG_SPE**                 | [CD](#prominent-lithological-features-l-cong-spe)  | Caractérisation des conglomérats selon la nature des clastes. | [0..1]
**NAME_HORIZ**                 | [ Table ](#gc-litstrat-bed-cd)  | Nom du horizon repère. | [0..1]
**ORIG_DESCR**                 | string                  | Description selon la légende de la carte géologique originale | [0..1]
**LITHO**                 | [ Table ](#gc-litho-cd)  | Description du  matériel (unité lithologique). | [1]





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
_Nom du horizon repère_

Voir [GC_LITSTRAT_BED_CD](#gc-litstrat-bed-cd) dans l'annexe





#### Attribut  ORIG_DESCR
_Description selon la légende de la carte géologique originale_

_Type de donnée :  string_





#### Attribut  LITHO
_Description du  matériel (unité lithologique)_

Voir [GC_LITHO_CD](#gc-litho-cd) dans l'annexe





### Classe Miscellaneous_PT (Lmis){#miscellaneous-pt}
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





### Classe Geological_Outlines_L (Lgeo){#geological-outlines-l}
La classe [Geological_Outlines_L](#geological-outlines-l) contient les contours
géologiques.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**STATUS**                 | [CD](#geological-outlines-l-status)  | État du type d&#39;objet. | [0..1]





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








## Thème PARAMETER_AND_MODELLING

### Classe Slope_Bedrock_PT (Pslo){#slope-bedrock-pt}
La classe [Slope_Bedrock_PT](#slope-bedrock-pt) contient des informations
ponctuelles provenant de la modélisation de l’orientation
d’horizons lithologiques des roches consolidées dans le
sous-sol ou de surfaces d’érosion.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**TYPE**                 | [CD](#slope-bedrock-pt-type)  | Surface de référence. | [1]
**AZIMUTH**                 | integer                  | Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le  nord en degré de 0° à 359° dans le sens des aiguilles d&#39;une montre | [0..1]
**DIP**                 | integer                  | Valeur du plongement du type d&#39;objet (en degrés), mesurée de l’horizontale (0°) vers le bas jusqu’à la  verticale (90°) | [0..1]
**FORMATIO**                 | [ Table ](#gc-litstrat-bed-cd)  | Unité lithostratigraphique de l’horizon modélisé. | [1]





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

Voir [GC_LITSTRAT_BED_CD](#gc-litstrat-bed-cd) dans l'annexe





### Classe Contour_Lines_Bedrock_L (Pcon){#contour-lines-bedrock-l}
La classe [Contour_Lines_Bedrock_L](#contour-lines-bedrock-l) contient les isohypses qui
décrivent la géométrie des roches consolidées dans le sous-
sol et sont le résultat d’une modélisation. Dans cette
classe se trouvent entre autres les isohypses de la surface
du substratum rocheux.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**TYPE**                 | [CD](#contour-lines-bedrock-l-type)  | Surface de référence. | [1]
**ALTITUDE**                 | float                  | Valeur altimétrique des isohypses | [1]
**LITSTRAT**                 | [ Table ](#gc-litstrat-bed-cd)  | Unité lithostratigraphique de la formation modelisée. | [1]





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

Voir [GC_LITSTRAT_BED_CD](#gc-litstrat-bed-cd) dans l'annexe





### Classe Modelled_Water_Table_PT (Pmod){#modelled-water-table-pt}
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





### Classe Contour_Lines_Hydro_L (Pcon){#contour-lines-hydro-l}
Dans la classe [Contour_Lines_Hydro_L](#contour-lines-hydro-l) se trouvent les
isohypses qui décrivent la surface d’une nappe d’eau
souterraine.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**CONFINE**                 | [CD](#contour-lines-hydro-l-confine)  | État de la pression dans l’aquifère. | [0..1]
**ALTITUDE**                 | float                  | Valeur altimétrique des isohypses | [1]
**WA_TABLE**                 | [CD](#contour-lines-hydro-l-wa-table)  | Niveau des eaux. | [0..1]





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








## Thème ANTHROPOGENIC_FEATURES

### Classe Archaeology_PT (Aarc){#archaeology-pt}
La classe [Archaeology_PT](#archaeology-pt) regroupe les sites archéologiques.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | []
**EPOCH**                 | [CD](#archaeology-pt-epoch)  | Époque archéologique du type d&#39;objet. | [0..1]
**PERIOD**                 | [CD](#archaeology-pt-period)  | Période archéologique du type d&#39;objet. | [0..1]
**AGE**                 | [CD](#archaeology-pt-age)  | Âge archéologique du type d&#39;objet. | [0..1]
**TYPE**                 | [CD](#archaeology-pt-type)  | Type de mégalithe. | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10101001 | archäologische Fundstelle, Anlage, Siedlungsreste | site archéologique, station, vestiges d&#39;établissement     |
|10101002 | Höhlensiedlung, Abri | grotte, abri sous roche     |
|10101003 | Pfahlbauten | palafitte     |
|10101004 | Burgstelle, Burghügel, Wachtturm | motte, emplacement d´un ancien château, d´une fortification, d&#39;un château-fort     |
|10101005 | Gräber, Gräberfeld | tombe, site mortuaire     |
|10101006 | Steinplattengrab | sépulture     |
|10101007 | Grabhügel, Dolmengrab | tumulus, dolmen funéraire     |
|10101008 | Kultstein | mégalithe     |
|10101009 | Kalkofen | four à chaux     |
|10101010 | Felsenkeller | cave dans la roche     |
|10101011 | Schlackenhalde | crassier     |
|10101012 | Glashütte | verrerie     |
|10101013 | Schmelzofen | four à fer     |
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




### Classe Archaeology_L (Aarc){#archaeology-l}
La classe [Archaeology_L](#archaeology-l) contient les éléments archéologiques
de forme linéaire. Les routes historiques, les chemins creux
et les fossés de fortification font partie de cette classe.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | []
**EPOCH**                 | [CD](#archaeology-l-epoch)  | Époque archéologique du type d&#39;objet. | [0..1]
**PERIOD**                 | [CD](#archaeology-l-period)  | Période archéologique du type d&#39;objet. | [0..1]
**AGE**                 | [CD](#archaeology-l-age)  | Âge archéologique du type d&#39;objet. | [0..1]





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




### Classe Archaeology_PLG (Aarc){#archaeology-plg}
Dans la classe [Archaeology_PLG](#archaeology-plg) se trouvent les vestiges
archéologiques (p.ex. le Castrum romain) qui recouvrent une
surface importante.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | []
**EPOCH**                 | [CD](#archaeology-plg-epoch)  | Époque archéologique du type d&#39;objet. | [0..1]
**PERIOD**                 | [CD](#archaeology-plg-period)  | Période archéologique du type d&#39;objet. | [0..1]
**AGE**                 | [CD](#archaeology-plg-age)  | Âge archéologique du type d&#39;objet. | [0..1]





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




### Classe Exploitation_Geomaterials_PT (Aexp){#exploitation-geomaterials-pt}
La classe [Exploitation_Geomaterials_PT](#exploitation-geomaterials-pt) contient des
informations ponctuelles sur les sites d’exploitation de
matériaux géologiques.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | []
**EXP_UNIT**                 | [ Table ](#gc-litstrat-bed-cd)  | Unité lithostratigraphique exploitée. | [0..*]
**STATUS**                 | [CD](#exploitation-geomaterials-pt-status)  | État de l&#39;exploitation. | [0..1]
**DEPTH_TOT**                 | float                  | Profondeur totale du type d&#39;objet (en mètres depuis la surface). | [0..1]
**TARG_MAT**                 | [CD](#exploitation-geomaterials-pt-targ-mat)  | Matériau exploité.. | [0..1]





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

Voir [GC_LITSTRAT_BED_CD](#gc-litstrat-bed-cd) dans l'annexe





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




### Classe Exploitation_Geomaterials_L (Aexp){#exploitation-geomaterials-l}
La classe [Exploitation_Geomaterials_L](#exploitation-geomaterials-l) contient les objets de
forme linéaire liés aux sites d’exploitation de matériaux
géologiques (p.ex. le front de taille).




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | []
**STATUS**                 | [CD](#exploitation-geomaterials-l-status)  | État de l&#39;exploitation. | [0..1]





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




### Classe Exploitation_Geomaterials_PLG (Aexp){#exploitation-geomaterials-plg}
La classe [Exploitation_Geomaterials_PLG](#exploitation-geomaterials-plg) contient les
surfaces d’exploitation de géomatériaux, telles qu’elles
étaient au moment du levé de la carte géologique.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | []
**EXP_UNIT**                 | [ Table ](#gc-litstrat-bed-cd)  | Unité lithostratigraphique exploitée. | [1..*]
**STATUS**                 | [CD](#exploitation-geomaterials-plg-status)  | État de l&#39;exploitation. | [0..1]
**DEPTH_TOT**                 | float                  | Profondeur totale du type d&#39;objet (en mètres depuis la surface) | [0..1]
**TARG_MAT**                 | [CD](#exploitation-geomaterials-plg-targ-mat)  | Matériel exploité.. | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10801001 | Steinbruch | carrière     |
|10801002 | Grube (Lockergesteinsabbau) | exploitation de matériaux meubles     |




#### Attribut  EXP_UNIT
_Unité lithostratigraphique exploitée_

Voir [GC_LITSTRAT_BED_CD](#gc-litstrat-bed-cd) dans l'annexe





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




### Classe Boreholes_PT (Abor){#boreholes-pt}
La classe [Boreholes_PT](#boreholes-pt) regroupe les forages et les sondages.
(Sur les anciennes cartes imprimées, le genre d’objet
n’était pas toujours distingué. D’ailleurs, il se peut que
sur les anciennes cartes, les sondages par carottier battu
aient été classés en tant que forages.)




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | []
**DEPTH_BEDR**                 | float                  | Profondeur de la roche en place (en mètres depuis la surface). Si l’ouvrage
n’atteint pas la roche en place,  par exemple forage interrompu dans la
couverture quaternaire, la valeur est  999, au cas où le forage commence
déjà dans la roche en place la valeur est 0. Si la roche solide a été atteinte,
mais qu&#39;il n&#39;est pas clair qu&#39;il s&#39;agit de la surface de la roche, la valeur
est 888. | [0..1]
**D_C_UNDERG**                 | boolean                  | Forage réalisé à partir d’une galerie (oui / non)? | [1]
**MAIN_TAR**                 | [CD](#boreholes-pt-main-tar)  | But principal du sondage. | [0..1]
**TARG_MAT**                 | [CD](#boreholes-pt-targ-mat)  | Matériau cible du sondage. | [0..1]
**DEPTH_TOT**                 | float                  | Profondeur totale du type d&#39;objet (en mètres depuis la surface) | [0..1]
**DEPTH_FM_A**                 | [ Table ](#gc-litstrat-bed-cd)  | Profondeur relative à la formation A atteinte (en mètres depuis la surface). | [0..1]
**DEPTH_FM_B**                 | float                  | Profondeur de la formation B atteinte (en mètres depuis  la surface) | [0..1]
**FM_A**                 | [ Table ](#gc-litstrat-bed-cd)  | Unité lithostratigraphique de la formation A atteinte. | [0..1]
**DEPTH_FM_B**                 | float                  | Profondeur de la formation B atteinte (en mètres depuis  la surface) | [0..1]
**DEPTH_WT**                 | float                  | Profondeur (m depuis la surface) de la nappe phréatique (valeur moyenne) | [0..1]
**AZIMUTH**                 | integer                  | Azimut du type d&#39;objet. L&#39;azimut est mesuré depuis le nord en degré de 0° à 359° dans le sens des aiguilles d&#39;une montre. | [0..1]
**DIP**                 | integer                  | Valeur du plongement du type d&#39;objet (en degrés), mesurée de l’horizontale (0°) vers le bas jusqu’à la  verticale (90°) | [0..1]
**REF_NUMBER**                 | integer                  | Numéro de référence du type d&#39;objet dans un  document annexé (notice explicative,…) | [0..1]
**LITHO**                 | [ Table ](#gc-litho-unco-cd)  | Unité lithologique atteinte (dans le cas de forage atteignant le quaternaire). | [0..1]





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
_Profondeur de la roche en place (en mètres depuis la surface). Si l’ouvrage
n’atteint pas la roche en place,  par exemple forage interrompu dans la
couverture quaternaire, la valeur est  999, au cas où le forage commence
déjà dans la roche en place la valeur est 0. Si la roche solide a été atteinte,
mais qu&#39;il n&#39;est pas clair qu&#39;il s&#39;agit de la surface de la roche, la valeur
est 888._

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

Voir [GC_LITSTRAT_BED_CD](#gc-litstrat-bed-cd) dans l'annexe





#### Attribut  DEPTH_FM_B
_Profondeur de la formation B atteinte (en mètres depuis  la surface)_

_Type de donnée :  float_





#### Attribut  FM_A
_Unité lithostratigraphique de la formation A atteinte_

Voir [GC_LITSTRAT_BED_CD](#gc-litstrat-bed-cd) dans l'annexe





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





### Classe Artificial_Surface_Modifications_PLG (Aart){#artificial-surface-modifications-plg}
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








## Thème HYDROGEOLOGY

### Classe Construction_PT (Hcon){#construction-pt}
Dans la classe [Construction_PT](#construction-pt) se trouvent les constructions
hydriques, comme les captages dans la nappe phréatique et
les citernes. Les instruments de mesure comme les
piézomètres et les limnigraphes appartiennent également à
cette classe.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**STATUS**                 | [CD](#construction-pt-status)  | État du type d&#39;objet. | [0..1]
**EPOCH**                 | [CD](#construction-pt-epoch)  | Époque de construction du type d&#39;objet. | [0..1]
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





### Classe Construction_L (Hcon){#construction-l}
Dans la classe [Construction_L](#construction-l) se trouvent les constructions
hydriques de forme linéaire comme les galeries de captage
d’eau, qui peuvent être combinées avec les types d’objets de
la classe Surface_Water_PT.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**COMBI**                 | [CD](#construction-l-combi)  | Type d’objet d&#39;une autre classe avec lequel le type d’objet peut être combiné. | [0..1]





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




### Classe Palaeohydrology_L (Hpal){#palaeohydrology-l}
La classe [Palaeohydrology_L](#palaeohydrology-l) contient tous les types d’objets
de forme linéaire, indiquant le tracé d’un cours d’eau dans
le passé.




Nom             | Type | Description                             |  Card.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Type de l&#39;objet | [1]
**REL_AGE**                 | [CD](#palaeohydrology-l-rel-age)  | Age relatif du type d&#39;objet. | [0..1]
**CHRONO**                 | [ Table ](#gc-chrono-cd)  | Attribution chronostratigraphique. | [0..1]
**REF_YEAR**                 | integer                  | Année de référence de l’ancienne ligne de rivage. | [1]
**SOURCE**                 | string                  | Source des données déduites à partir de données historiques | [0..1]





#### Attribut  KIND
_Type de l&#39;objet_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12301001 | Paläotal | axe de paléovallée     |
|12301002 | ehemalige Entwässerungsrinne | ancien chenal     |
|12301003 | ehemalige glaziale Abflussrinne | axe d&#39;un ancien effluent glaciaire     |
|12301004 | Trockental | vallée sèche     |
|12301005 | ehemaliges Bachbett | ancien lit de cours d&#39;eau (ruisseau)     |
|12301006 | Ufer eines ehemaligen Flussbetts | rive d&#39;un ancien lit de cours d&#39;eau     |
|12301007 | ehemalige Uferlinie | ancienne ligne de rivage     |




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





### Classe Subsurface_Water_L (Hsub){#subsurface-water-l}
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
**COMBI**                 | [CD](#subsurface-water-l-combi)  | Type d’objet d&#39;une autre classe avec lequel le type d’objet peut être combiné. | [0..1]





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




### Classe Surface_Water_PT (Hsur){#surface-water-pt}
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
**STATUS**                 | [CD](#surface-water-pt-status)  | État du type d&#39;objet. | [0..1]
**FLOW_CON**                 | [CD](#surface-water-pt-flow-con)  | Condition d’écoulement. | [0..1]
**TYPE**                 | [CD](#surface-water-pt-type)  | Caractéristique du type d&#39;objet. | [0..1]
**DIS_LOCA**                 | [CD](#surface-water-pt-dis-loca)  | Lieu d’écoulement. | [0..1]
**COMBI**                 | [CD](#surface-water-pt-combi)  | Type d’objet d&#39;une autre classe avec lequel le type  d’objet peut être combiné. | [0..1]
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





### Classe Surface_Water_L (Hsur){#surface-water-l}
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




### Classe Surface_Water_PLG (Hsur){#surface-water-plg}
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









## Annexe  GC_LITSTRAT_BED_CD {#gc-litstrat-bed-cd}
Table des valeurs des unités lithostratigraphiques

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15200001 | Twannbach-Formation | Formation du Twannbach     |
|15200002 | Reuchenette-Formation | Formation de Reuchenette     |
|15200003 | Courgenay-Formation | Formation de Courgenay     |
|15200004 | Vellerat-Formation | Formation de Vellerat     |
|15200005 | St-Ursanne-Formation | Formation de St-Ursanne     |
|15200006 | Bärschwil-Formation | Formation de Bärschwil     |
|15200007 | Ifenthal-Formation | Formation d&#39;Ifenthal     |
|15200008 | Hauptrogenstein | Hauptrogenstein     |
|15200009 | Passwang-Formation | Formation du Passwang     |
|15200010 | Opalinus-Ton | Argile à Opalinus     |
|15200011 | Staffelegg-Formation | Formation de la Staffelegg     |
|15200012 | Malm des Juragebirges | Malm du Jura     |
|15200013 | Vouglans-Member | Membre de Vouglans     |
|15200014 | Chailley-Member | Membre du Chailley     |
|15200015 | Oberer Virgula-Mergel | Marnes à Virgula supérieures     |
|15200016 | Grenznerineen-Bank | Banc à Nérinées du sommet     |
|15200017 | Cladocoropsis-Kalk | Calcaire à Cladocoropsis     |
|15200018 | Unterer Virgula-Mergel | Marnes à Virgula inférieures     |
|15200019 | Courtedoux-Member | Membre de Courtedoux     |
|15200020 | Banné-Member | Membre du Banné     |
|15200021 | Vabenau-Member | Membre de Vabenau     |
|15200022 | Creugenat-Schichten | Couches du Creugenat     |
|15200023 | Etiollets-Formation | Formation des Etiollets     |
|15200024 | Complexe récifal | Complexe récifal (Fm. des Etiollets)     |
|15200025 | Couvaloup-Member | Membre du Couvaloup     |
|15200026 | Porrentruy-Member | Membre de Porrentruy     |
|15200027 | La-May-Member | Membre de la May     |
|15200028 | Oolithe-Rousse-Member | Membre de l&#39;Oolithe rousse     |
|15200029 | Bure-Member | Membre de Bure     |
|15200030 | Hauptmumienbank-Member | Membre du Hauptmumienbank (Oolithe nuciforme)     |
|15200031 | Röschenz-Member | Membre de Röschenz     |
|15200032 | Vorbourg-Member | Membre du Vorbourg     |
|15200033 | Tiergarten-Member | Membre du Tiergarten     |
|15200034 | Buix-Member | Membre de Buix     |
|15200035 | Chestel-Member | Membre du Chestel     |
|15200036 | Caquerelle-Pisolith | Pisolite de la Caquerelle     |
|15200037 | Grellingen-Member | Membre de Grellingen     |
|15200039 | Pichoux-Formation | Formation du Pichoux     |
|15200040 | Liesberg-Member | Membre de Liesberg     |
|15200041 | Sornetan-Member | Membre de Sornetan     |
|15200042 | Renggeri-Member | Membre à Renggeri     |
|15200043 | Graitery-Member | Membre du Graitery     |
|15200044 | Herznach-Member | Membre de Herznach     |
|15200045 | Schellenbrücke-Bank | Banc du Schellenbrücke     |
|15200046 | Bollement-Member | Membre de Bollement     |
|15200047 | Ängistein-Member | Membre d&#39;Ängistein     |
|15200048 | Unter-Erli-Bank | Banc d&#39;Unter Erli     |
|15200049 | Bözen-Member | Membre de Bözen     |
|15200050 | Saulcy-Member | Membre de Saulcy     |
|15200051 | Schelmenloch-Member | Membre du Schelmenloch     |
|15200052 | Anwil-Bank | Banc d&#39;Anwil     |
|15200053 | Châtillon-Member | Membre de Châtillon     |
|15200054 | St-Brais-Member | Membre de St-Braix     |
|15200055 | Dogger des Juragebirges | Dogger du Jura     |
|15200056 | Lias des Juragebirges | Lias du Jura     |
|15200057 | Spatkalk | Spatkalk (Hauptrogenstein)     |
|15200058 | Pierre-Blanche | Pierre Blanche (Hauptrogenstein)     |
|15200059 | Movelier-Schichten | Couches de Movelier     |
|15200060 | Obere Oolithische Serie (Grande Oolithe) | Série oolitique supérieure (Grande Oolithe)     |
|15200061 | Obere Acuminata-Schichten | Couches à Acuminata supérieures     |
|15200062 | Untere Oolithische Serie (Oolithe Subcompacte) | Série oolitique inférieure (Oolithe Subcompacte)     |
|15200063 | Grenchenberg-Member | Membre du Grenchenberg     |
|15200064 | Rothenfluh-Member | Membre de la Rothenfluh     |
|15200065 | Brüggli-Member | Membre de Brüggli     |
|15200066 | Humphriesi-Schichten | Couches à Humphriesi     |
|15200067 | Waldenburg-Member | Membre de Waldenburg     |
|15200068 | Hirnichopf-Member | Membre du Hirnichopf     |
|15200069 | Hauenstein-Member | Membre de Hauenstein     |
|15200070 | Sissach-Member | Membre de Sissach     |
|15200071 | Gross-Wolf-Member | Membre du Gross Wolf     |
|15200072 | Eriwis-Bank | Banc d&#39;Eriwis     |
|15200073 | Erlimoos-Bank | Banc d&#39;Erlimoos     |
|15200074 | Gipf-Bank | Banc de Gipf     |
|15200075 | Rietheim-Member | Membre de Rietheim     |
|15200076 | Unterer Stein | Unterer Stein (Fm. de la Staffelegg)     |
|15200077 | Rickenbach-Member | Membre de Rickenbach     |
|15200078 | Müsenegg-Bank | Banc de la Müsenegg     |
|15200079 | Breitenmatt-Member | Membre de Breitenmatt     |
|15200080 | Trasadingen-Bank | Banc de Trasadingen     |
|15200081 | Grünschholz-Member | Membre du Grünschholz     |
|15200082 | Frick-Member | Membre de Frick     |
|15200083 | Mont-Terri-Member | Membre du Mont Terri     |
|15200084 | Fasiswald-Member | Membre de Fasiswald     |
|15200085 | Weissenstein-Member | Membre du Weissenstein     |
|15200086 | Beggingen-Member | Membre de Beggingen     |
|15200087 | Gächlingen-Bank | Banc de Gächlingen     |
|15200088 | Schleitheim-Bank | Banc de Schleitheim     |
|15200089 | Schambelen-Member | Membre du Schambelen     |
|15200090 | Hallau-Bank | Banc de Hallau     |
|15200091 | Siderolithikum des Juragebirges | Sidérolithique du Jura     |
|15200092 | Gorges-de-l&#39;Orbe- und Vallorbe-Formation, undifferenziert | Formations des Gorges de l&#39;Orbe et de Vallorbe, indifférenciées     |
|15200093 | Vallorbe-Member | Formation de Vallorbe     |
|15200094 | Rivière-Member | Membre de la Rivière     |
|15200095 | Russille-Member | Membre de la Russille     |
|15200096 | Gorges-de-l&#39;Orbe-Formation | Formation des Gorges de l&#39;Orbe     |
|15200097 | Pierre-Châtel-, Vions- und Chambotte-Formation, undifferenziert | Formations de Pierre-Châtel, de Vions et de la Chambotte, indifférenciées     |
|15200098 | Chambotte-Formation | Formation de la Chambotte     |
|15200099 | Guiers-Member | Membre du Guiers     |
|15200100 | Vions-Formation | Formation de Vions     |
|15200101 | Pierre-Châtel-Formation | Formation de Pierre-Châtel     |
|15200102 | Burghorn-Formation | Formation du Burghorn     |
|15200103 | Wettigen-Member | Membre de Wettingen     |
|15200104 | Baden-Member | Membre de Baden     |
|15200105 | Villigen-Formation | Formation de Villigen     |
|15200106 | Wangental-Member | Membre du Wangental     |
|15200107 | Letzi-Member | Membre du Letzi     |
|15200108 | Knollen-Bank | Knollen-Bank (Fm. de Villigen)     |
|15200109 | Küssaburg-Member | Membre de la Küssaburg     |
|15200110 | Wangen-Member | Membre de Wangen     |
|15200111 | Hornbuck-Member | Membre du Hornbuck     |
|15200112 | Crenularis-Member | Membre à Crenularis     |
|15200113 | Geissberg-Member | Membre du Geissberg     |
|15200114 | Wildegg-Formation | Formation de Wildegg     |
|15200115 | Effingen-Member | Membre d&#39;Effingen     |
|15200116 | Gerstenhübel-Bank | Banc du Gerstenhübel     |
|15200117 | Birmenstorf-Member | Membre de Birmenstorf     |
|15200118 | Günsberg-Formation | Formation de Günsberg     |
|15200119 | Moutier-Korallenkalk | Calcaire à coraux de Moutier     |
|15200120 | Klingnau-Formation | Formation de Klingnau     |
|15200121 | Knorri-Ton | Argile à Knorri     |
|15200122 | Wuerttembergica-Schichten | Couches à Wuerttembergica     |
|15200123 | Subfurcatum-Bank | Banc à Subfurcatum     |
|15200124 | Blagdeni-Schichten | Couches à Blagdeni     |
|15200125 | Keuper | Groupe du Keuper     |
|15200126 | Klettgau-Formation | Formation du Klettgau     |
|15200127 | Belchen-Member | Membre du Belchen     |
|15200128 | Bänkerjoch-Formation | Formation du Bänkerjoch     |
|15200129 | Muschelkalk | Groupe du Muschelkalk     |
|15200130 | Schinznach-Formation | Formation de Schinznach     |
|15200131 | Asp-Member | Membre d&#39;Asp     |
|15200132 | Stamberg-Member | Membre du Stamberg     |
|15200133 | Liedertswil-Member | Membre de Liedertswil     |
|15200134 | Kienberg-Member | Membre de Kienberg     |
|15200135 | Zeglingen-Formation | Formation de Zeglingen     |
|15200136 | Obere Sufatzone | Obere Sufatzone (Fm. de Zeglingen)     |
|15200137 | Salzlager | Salzlager (Fm. de Zeglingen)     |
|15200138 | Untere Sulfatzone | Untere Sulfatzone (Fm. de Zeglingen)     |
|15200139 | Kaiseraugst-Formation | Formation de Kaiseraugst     |
|15200140 | Orbicularis-Mergel | Marne à Orbicularis     |
|15200141 | Wellenkalk / Wellenmergel | Wellenkalk / Wellenmergel     |
|15200142 | Wellendolomit | Wellendolomit     |
|15200143 | Buntsandstein | Groupe du Buntsandstein     |
|15200144 | Dinkelberg-Formation | Formation du Dinkelberg     |
|15200145 | Rhötton | Rhötton     |
|15200146 | Plattensandstein | Plattensandstein (Fm. du Dinkelberg)     |
|15200147 | Karneol-Horizont | Karneol-Horizont (Fm. du Dinkelberg)     |
|15200148 | Narlay-Formation | Formation de Narlay     |
|15200149 | Perte-du-Rhône-Formation | Formation de la Perte-du-Rhône     |
|15200150 | Grand-Essert-Formation | Formation du Grand Essert     |
|15200151 | Pierre Jaune de Neuchâtel | Membre de Neuchâtel     |
|15200152 | Hauterive-Mergel | Membre d&#39;Hauterive     |
|15200153 | Vuache-Formation | Formation du Vuache     |
|15200154 | Alectryonia-Kalk | Calcaire à Alectyonia rectangularis     |
|15200155 | Arzier-Mergel | Marne d&#39;Arzier     |
|15200156 | Goldberg-Formation | Formation du Goldberg     |
|15200157 | Wiesental-Formation | Formation du Wiesental     |
|15200158 | Weitenau-Formation | Formation de Weitenau     |
|15200159 | Weiach-Formation | Formation de Weiach     |
|15200160 | Günsberg-, Vellerat-, Villigen-, Balsthal- und Courgenay-Formation, undifferenziert | Formations de Günsberg, Vellerat, Villigen, Balsthal et Courgenay, indifférenciées     |
|15200161 | Kreide des Juragebirges | Crétacé du Jura     |
|15200162 | Jura des Juragebirges | Jurassique du Jura     |
|15200163 | Trias des Juragebirges | Trias du Jura     |
|15200175 | Bohnerzton | Argile à pisolites ferrugineuses     |
|15200176 | Boluston | Argile à bolus     |
|15200177 | Hupper | Hupper     |
|15200178 | Homomya-Mergel | Marne à Homomyes     |
|15200179 | Vogesen-Sandstein | Grès des Vosges     |
|15200180 | Glassand | Sable siliceux vitrifiable     |
|15200181 | Mussel-Member | Membre de Mussel     |
|15200182 | Fulie-Member | Membre de la Fulie     |
|15200183 | Uttins-Mergel | Marne des Uttins     |
|15200184 | Mergelkalk-Zone | Zone marno-calcaire (Fm. du Grand Essert)     |
|15200185 | Bryozoen-Mergel | Marne à Bryozoaires     |
|15200186 | Zuckerkörniger Kalk | Calcaire saccharoïde     |
|15200187 | Chevenez-Member | Membre de Chevenez     |
|15200188 | Balsthal-Formation | Formation de Balsthal     |
|15200189 | Verena-Member | Membre de Ste-Vérène     |
|15200190 | Holzflue-Member | Membre de la Holzflue     |
|15200191 | Laufen-Member | Membre de Laufon     |
|15200192 | Olten-Member | Membre d&#39;Olten     |
|15200193 | Steinibach-Member | Membre du Steinibach     |
|15200194 | Grüne Mumienbank | Grüne Mumienbank     |
|15200195 | Pecten-Bank | Banc à Pecten (Fm. de Wildegg)     |
|15200196 | Ferrugineus-Oolith | Oolite à Ferrugineus     |
|15200197 | Wittnau-Korallenkalk | Calcaire à coraux de Wittnau     |
|15200198 | Furcil-Mergel | Marne du Furcil     |
|15200199 | Maeandrina-Schichten | Couches à Maeandrina     |
|15200200 | Gisliflue-Korallenkalk | Calcaire à coraux de la Gisliflue     |
|15200201 | Untere Acuminata-Schichten | Couches à Acuminata inférieures     |
|15200202 | Parkinsoni-Schichten | Couches à Parkinsoni     |
|15200203 | Dewalquei-Kalk | Couches à Pecten dewalquei     |
|15200204 | Brot-Schichten | Couches de Brot     |
|15200205 | Comptum-Bank | Banc à Comptum     |
|15200206 | Seebi-Member | Membre de Seebi     |
|15200207 | Gruhalde-Member | Membre de la Gruhalde     |
|15200208 | Berlingen-Member | Membre de Berlingen     |
|15200209 | Gansingen-Member | Membre de Gansingen     |
|15200210 | Ergolz-Member | Membre de l&#39;Ergolz     |
|15200211 | Kaisten-Bank | Banc de Kaisten     |
|15200212 | Eptingen-Member | Banc d&#39;Eptingen     |
|15200213 | Dünnlenberg-Bank | Banc du Dünnlenberg     |
|15200214 | Saalhof-Bank | Banc de Saalhof     |
|15200215 | Fützen-Bank | Banc de Fützen     |
|15200216 | Dolomitzone | Dolomitzone (Fm. de Zeglingen)     |
|15200217 | Oberer Schuttfächer | Oberer Schuttfächer (Fm. de Weitenau)     |
|15200218 | Playa-Serie | Playa-Serie (Fm. de Weitenau)     |
|15200219 | Unterer Schuttfächer | Unterer Schuttfächer (Fm. de Weitenau)     |
|15200220 | Spät- bis postvariszische Intrusiva der Nordschweiz | Roches plutoniques tardi- à postvarisques de la Forêt Noire     |
|15200221 | Permo-Karbon der Nordschweiz | Permo-Carbonifère du NW de la Suisse     |
|15200222 | Stockberg-Quarzporphyr | Quarzporphyre du Stockberg     |
|15200223 | Bärhalde-Granit | Granite de la Bärhalde     |
|15200224 | Schluchsee-Granit | Granite du Schluchsee     |
|15200225 | Säckingen-Granit | Granite de Säckingen     |
|15200226 | Jüngere Flussablagerungen | Jüngere Flussablagerungen (Fm. de Weiach)     |
|15200227 | Seeablagerungen | Seeablagerungen (Fm. de Weiach)     |
|15200228 | Ältere Flussablagerungen | Ältere Flussablagerungen (Fm. de Weiach)     |
|15200229 | Kohle-Serie | Kohle-Serie (Fm. de Weiach)     |
|15200230 | Frühvariszische Intrusiva der Nordschweiz | Roches plutoniques éo-variques de la Forêt Noire     |
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
|15200243 | Prä- und frühvariszische Sedimente und Vulkanite der Nordschweiz | Roches sédimentaires et volcaniques anté- à éo-varisques de la Forêt Noire     |
|15200244 | Schiefer und Grauwacken | Schistes et grauwackes de la Forêt Noire     |
|15200245 | Prävariszisches polyzyklisches Grundgebirge der Nordschweiz | Socle polycyclique anté-varisque de la Forêt Noire     |
|15200246 | Prävariszische Orthogneise der Nordschweiz | Orthogneiss de la Forêt Noire     |
|15200247 | Todtmoos-Horbach-Gneiskomplex | Complexe gneissique de Todtmoos-Horbach     |
|15200248 | Murgtal-Gneiskomplex | Complexe gneissique du Murgtal     |
|15200249 | Laufenburg-Gneiskomplex | Complexe gneissique de Laufenburg     |
|15200250 | Prävariszische Migmatite der Nordschweiz | Migmatites de la Forêt Noire     |
|15200251 | Wiesen-Wehratal-Komplex | Complexe du Wiesental-Wehratal     |
|15200252 | Wehratal-Syenit | Syénite du Wehratal     |
|15200253 | Prävariszische Grüngesteine der Nordschweiz | Roches vertes de la Forêt Noire     |
|15200254 | Molasse | Molasse     |
|15200255 | Obere Süsswassermolasse (OSM) | Molasse d&#39;eau douce supérieure (OSM)     |
|15200256 | Tannenberg-Schichten | Couches de Tannenberg     |
|15200257 | Pfänder-Schichten | Couches du Pfänder     |
|15200258 | Napf-Formation | Formation du Napf     |
|15200259 | Blapbach-Kohleflöz | Niveau charbonneux du Blapbach     |
|15200260 | Eimätteli-Member | Membre d&#39;Eimätteli     |
|15200261 | Schüpferegg-Nagelfluh | Poudingue de la Schüpferegg     |
|15200262 | OSM-II | OSM-II     |
|15200263 | Hegau-Vulkanite | Roches volcaniques du Hegau     |
|15200264 | Hegau-Basalt | Basalte du Hegau     |
|15200265 | Hegau-Phonolith | Phonolite du Hegau     |
|15200266 | Hegau-Deckentuffe | Tuffite du Hegau     |
|15200267 | Hörnligipfel-Nagelfluh | Poudingue du Hörnligipfel     |
|15200268 | Höchegg-Brekzie | Brèche de la Höchegg     |
|15200269 | Hörnligubel-Mergel | Marne du Hörnligubel     |
|15200270 | Tösswald-Schichten | Couches du Tösswald     |
|15200271 | Bischofzell-Bentonit | Bentonite de Bischofszell     |
|15200272 | Öhningen-Zone im Hörnligebiet | Zone d&#39;Öhningen de la région du Hörnli     |
|15200273 | Krinau-Schichten | Couches de Krinau     |
|15200274 | Glimmersandstein-Formation | Formation du Glimmersand     |
|15200275 | Fellitobel-Süsswasserkalk | Calcaire d&#39;eau douce du Fellitobel     |
|15200276 | Uetliberg-Schichten | Couches de l&#39;Üetliberg     |
|15200277 | Uetliberggipfel-Nagelfluh | Poudingue de l&#39;Üetliberggipfel     |
|15200278 | Uetliberg-Mergel | Poudingue de l&#39;Üetliberg     |
|15200279 | Falätschen-Mergel | Marne de la Falätschen     |
|15200280 | Pfannenstiel-Schichten | Couches du Pfannenstiel     |
|15200281 | Zürich-Schichten | Couches de Zürich     |
|15200282 | Leimbach-Bentonit | Bentonite de Leimbach     |
|15200283 | Rütschlibach-Riedhof-Süsswasserkalk | Calcaire d&#39;eau douce du Rütschlibach-Riedhof     |
|15200284 | Winterthur-Bentonit | Bentonite de Winterthur     |
|15200285 | Aeugstertal-Bentonit | Bentonite de l&#39;Aeugstertal     |
|15200286 | Äntlisberg-Doldertobel-Süsswasserkalk | Calcaire d&#39;eau douce de l&#39;Äntlisberg-Doldertobel     |
|15200287 | Wehrenbach-Höckler-Süsswasserkalk | Calcaire d&#39;eau douce du Wehrenbach-Höckler     |
|15200288 | Küsnacht-Bentonit | Bentonite de Küsnacht     |
|15200289 | Urdorf-Bentonit | Bentonite d&#39;Urdorf     |
|15200290 | Appenzellergranit-Leitniveau | Niveau repère de l&#39;Appenzellergranit     |
|15200291 | Abtwil-Konglomerat | Conglomérat d&#39;Abtwil     |
|15200292 | Hüllistein-Konglomerat | Conglomérat d&#39;Hüllistein     |
|15200293 | Degersheim-Kalknagelfluh | Conglomérat de Degersheim     |
|15200294 | Meilen-Kalk | Calcaire de Meilen     |
|15200295 | OSM-I | OSM-I     |
|15200296 | Lichtensteig-Schichten | Formation de Lichtensteig     |
|15200297 | Hörnli-Formation | Formation du Hörnli     |
|15200298 | Guggershorn-Formation | Formation du Guggershorn     |
|15200299 | Horgen-Käpfnach-Süsswasserkalk | Calcaire d&#39;eau douce de Horgen-Käpfnach     |
|15200300 | OSM-J | OSM-J     |
|15200301 | Bois-de-Raube-Formation | Formation du Bois de Raube     |
|15200302 | Jura-Nagelfluh | Juranagelfluh (OSM-J)     |
|15200303 | Oehningien des Juragebirges | Oehningien du Jura     |
|15200304 | Combe-Girard-Bentonit | Bentonite de la Combe Girard     |
|15200305 | Vermes-Süsswasserkalk | Calcaire d&#39;eau douce de Vermes     |
|15200306 | Crêt-du-Locle-Formation, Gompholitfazies | Gompholite du Locle     |
|15200307 | Obere Meeresmolasse (OMM) | Molasse marine supérieure (OMM)     |
|15200308 | OMM-II | OMM-II     |
|15200309 | St-Gallen-Formation | Formation de St-Gall     |
|15200310 | Staffelbach-Grobsandstein | Grès grossier de Staffelbach     |
|15200311 | OMM-I | OMM-I     |
|15200312 | Luzern-Formation | Formation de Lucerne     |
|15200313 | Safenwil-Muschelsandstein | Grès coquillier de Safenwil     |
|15200314 | Untere Süsswassermolasse (USM) | Molasse d&#39;eau douce inférieure (USM)     |
|15200315 | Höhronen-Nagelfluh | Poudingue des Höhronen     |
|15200316 | Kronberg-Nagelfluh | Poudingue du Kronberg     |
|15200317 | Cornalle-Sandstein | Grès de la Cornalle     |
|15200318 | Mont-Pèlerin-Nagelfluh | Poudingue du Mont Pèlerin     |
|15200319 | Speer-Formation | Formation du Speer     |
|15200320 | Thun-Formation | Formation de Thoune     |
|15200321 | Gunten-Quarzitnagelfluh | Poudingue quartzitique de Gunten     |
|15200322 | Rigi-Formation | Formation du Rigi     |
|15200323 | Scheidegg-Nagelfluh | Poudingue de la Rigi-Scheidegg     |
|15200324 | Bunte Rigi-Nagelfluh | Bunte Rigi-Nagelfluh     |
|15200325 | Radiolaritreiche Nagelfluh | Radiolaritreiche Nagelfluh (Fm. du Rigi)     |
|15200326 | USM-III | USM-III     |
|15200327 | Sommersberg-Nagelfluh | Poudingue du Sommersberg     |
|15200328 | Brendenbach-Mergel | Poudingue du Brendenbach     |
|15200329 | USM-II | USM-II     |
|15200330 | Formation der Granitischen Molasse | Formation de la Molasse granitique     |
|15200331 | Oberaquitane Mergelzone | Oberaquitane Mergelzone     |
|15200332 | Molasse Grise de Lausanne | Molasse Grise de Lausanne     |
|15200333 | Bois-Genoud-Bentonit | Bentonite de Bois-Genoud     |
|15200334 | Cuarny-Sandstein | Grès de Cuarny     |
|15200335 | USM-I | USM-I     |
|15200336 | Grès et Marnes Gris à Gypse | Grès et Marnes Gris à Gypse     |
|15200337 | Molasse à Charbon | Molasse à Charbon     |
|15200338 | Molasse Rouge | Molasse Rouge     |
|15200339 | Heuboden-Äschitannen-Nagelfluh | Poudingue de Heuboden-Äschitannen     |
|15200340 | Beichlen-Formation | Formation de la Beichlen     |
|15200341 | USM-J | USM-J     |
|15200342 | La-Chaux-Süsswasserkalk | Calcaire d&#39;eau douce de La Chaux     |
|15200343 | Elsässer Molasse s.s. | Molasse alsacienne s.s.     |
|15200344 | Delémont-Süsswasserkalk | Calcaire d&#39;eau douce de Delémont     |
|15200345 | Matzendorf-Süsswasserkalk | Calcaire d&#39;eau douce de Matzendorf     |
|15200346 | Oensingen-Süsswasserkalk | Calcaire d&#39;eau douce d&#39;Oensingen     |
|15200347 | Wynau-Süsswasserkalk | Calcaire d&#39;eau douce de Wynau     |
|15200348 | Untere Meeresmolasse (UMM) | Molasse marine inférieure (UMM)     |
|15200349 | UMM-III | UMM-III     |
|15200350 | Horw-Sandstein | Grès d&#39;Horw     |
|15200351 | UMM-II | UMM-II     |
|15200352 | Grisigen-Mergel | Marne de Grisigen     |
|15200353 | UMM-I | UMM-I     |
|15200354 | Cucloz-Subformation | Sous-formation de Cucloz     |
|15200355 | Cucloz-Sandstein | Grès de Cucloz     |
|15200356 | Marnes gris-souris | Marnes gris-souris     |
|15200357 | Schistes marno-micacés | Schistes marno-micacés     |
|15200358 | Hilfern-Formation | Formation de la Hilfern     |
|15200359 | Rietbad-Subformation | Sous-formation de Rietbad     |
|15200360 | Jordisboden-Mergel | Marne du Jordisboden     |
|15200361 | Goldegg-Sandstein | Grès de la Goldegg     |
|15200362 | UMM-J | UMM-J     |
|15200363 | Septarienton | Argile à Septaria (Septarienton)     |
|15200364 | Fischschiefer | Schistes à Poissons (Fischschiefer)     |
|15200365 | Foraminiferenmergel | Marnes à Foraminifères (Foraminiferenmergel)     |
|15200366 | Meeressand | Meeressand     |
|15200368 | Cyathulabank (Laufen-Becken) | Banc à Cyathula (bassin de Laufon)     |
|15200369 | Cyrenenmergel | Marne à Cyrènes     |
|15200370 | Porrentruy-Konglomerat | Conglomérat de Porrentruy     |
|15200371 | Raitsche | Raitsche     |
|15200373 | Ajoie-Gompholit | Gompholite d&#39;Ajoie     |
|15200378 | Tüllingen-Süsswasserkalk | Calcaire d&#39;eau douce de Tüllingen     |
|15200379 | Elsässer-Molasse s.l. | Molasse alsacienne s.l.     |
|15200380 | Oberer Teil des Hauptrogensteins | Partie supérieure du Hauptrogenstein     |
|15200382 | Unterer Teil des Hauptrogensteins | Partie inférieure du Hauptrogenstein     |
|15200383 | Calcaire roux marneux | Calcaire roux marneux     |
|15200384 | Ajoie-Member | Membre d&#39;Ajoie     |
|15200385 | Bois-de-Raube-Member | Membre du Bois de Raube     |
|15200386 | Montchaibeux-Member | Membre du Montchaibeux     |
|15200387 | Daubrée-Konglomerat | Conglomérat de Daubrée     |
|15200388 | Wanderblock-Bildungen | Dépôts de blocs pérégrins (Wanderblock-Bildungen)     |
|15200389 | Geröllsande | Sables à galets (OMM)     |
|15200390 | Polygene Nagelfluh | Poudingue polygénique (OMM)     |
|15200391 | Muschelsandstein | Zone du grès coquillier (OMM)     |
|15200392 | Graue Molasse | Molasse Grise (OMM)     |
|15200393 | Daubrée-Kalk | Calcaire de Daubrée     |
|15200394 | Basisbildungen der USM-J | Formations de la base de l&#39;USM-J     |
|15200395 | Laufen-Juranagelfluh | Juranagelfluh de Laufon     |
|15200396 | Basler Juranagelfluh | Juranagelfluh du Jura bâlois     |
|15200397 | Aargauer Juranagelfluh | Juranagelfluh d&#39;Argovie     |
|15200398 | Randen-Juranagelfluh | Juranagelfluh du Randen     |
|15200399 | Jensberg-Schichten | Couches du Jensberg     |
|15200400 | Rebhubel-Schichten | Couches du Rebhubel     |
|15200401 | Niedermatt-Formation | Formation de Niedermatt     |
|15200402 | Belpberg-Formation | Formation du Belpberg     |
|15200403 | Pfadflüe-Nagelfluh | Poudingue de la Pfadflüe     |
|15200404 | Sädel-Kalknagelfluh | Poudingue calcaire de Sädel     |
|15200405 | Utzigen-Muschelsandstein | Grès coquillier d&#39;Utzigen     |
|15200406 | Ulmiz-Quarzitnagelfluh | Poudingue quarzitique d&#39;Ulmiz     |
|15200407 | Bütschelbach-Nagelfluh | Poudingue du Bütschelbach     |
|15200408 | Kalchstätten-Formation | Formation de Kalchstätten     |
|15200409 | Freudenberg-Nagelfluh | Poudingue du Freudenberg     |
|15200410 | Goldbrunnen-Schichten | Couches de Goldbrunnen     |
|15200411 | Dreilinden-Nagelfluh | Poudingue de Dreilinden     |
|15200412 | Obere Grenznagelfluh | Obere Grenznagelfluh (Fm. de Saint-Gall)     |
|15200413 | Kirchberg-Formation | Formation de Kirchberg     |
|15200414 | Grimmelfingen-Formation | Formation de Grimmelfingen     |
|15200415 | Chnebelburg-Schichten | Couches de la Chnebelburg     |
|15200416 | Meinisberg-Muschelsandstein | Grès coquillier de Meinisberg     |
|15200417 | Brüttelen-Muschelnagelfluh | Poudingue coquillier de Brüttelen     |
|15200418 | Sense-Formation | Formation de la Singine     |
|15200419 | Montécu-Schichten | Couches de Montécu     |
|15200420 | Molière-Muschelsandstein | Grès coquillier de la Molière     |
|15200421 | Scherli-Quarzitnagelfluh | Poudingue quartzitique du Scherli(grabe)     |
|15200422 | Grilly-Süsswasserkalk | Calcaire d&#39;eau douce de Grilly     |
|15200423 | Orbe-Süsswasserkalk | Calcaire d&#39;eau douce d&#39;Orbe     |
|15200424 | Krustenkalk | Calcaire concrétionné (USM)     |
|15200425 | Gümmenen-Formation | Formation de Gümmenen     |
|15200426 | Solothurner Schildkrötenkalk | Calcaire à tortues de Soleure     |
|15200429 | Obere bunte Molasse | Molasse bariolée supérieure     |
|15200430 | Oberdorf-Süsswasserkalk | Calcaire d&#39;eau douce d&#39;Oberdorf     |
|15200431 | Limnischer Horizont (OMM-II) | Horizon limnique (OMM-II)     |
|15200432 | Quarzitnagelfluh (der St.-Gallen-Fm.) | Poudingue quartzitique (Fm. de Saint-Gall)     |
|15200433 | Basiskonglomerat (der Luzern-Fm.) | Conglomérat basal (Fm. de Lucerne)     |
|15200436 | Poncin-Member | Membre de Poncin     |
|15200437 | Vraconne-Sandstein | Grès de la Vraconne     |
|15200438 | La-Presta-Mergel | Argile de la Presta     |
|15200439 | Vernettes-Sandstein | Grès des Vernettes     |
|15200440 | Ponthoud-Bank | Banc du Ponthoud     |
|15200441 | Scie-Besse-Sandstein | Grès de Scie Besse     |
|15200442 | Mortier-Mergel | Marne du Mortier     |
|15200443 | Vauglène-Bänke | Couches de Vauglène     |
|15200444 | Poet-Bank | Banc du Poet     |
|15200445 | Courcelon-Süsswasserkalk | Calcaire d&#39;eau douce de Courcelon     |
|15200446 | Erzmatt-Krustenkalk | Calcaire concrétionné de la Erzmatt     |
|15200447 | Diegten-Süsswasserkalk | Calcaire d&#39;eau douce de Diegten     |
|15200448 | La-Verrerie-Süsswasserkalk | Calcaire d&#39;eau douce de la Verrerie     |
|15200449 | La-Charrue-Süsswasserkalk | Calcaire d&#39;eau douce de la Charrue     |
|15200450 | Astieria-Mergel | Marne à Astieria     |
|15200451 | Villers-Schichten | Couches de Villers     |
|15200452 | Unité Moyenne Calcaire (UMC) | Unité Moyenne Calcaire (UMC)     |
|15200453 | Unité Inférieure Oolithique (UIO) | Unité Inférieure Oolithique (UIO)     |
|15200454 | Mergel- und Kalkzone (MKZ) | Zone marneuses et calcaire (MKZ)     |
|15200455 | Calcaire âpre | Calcaire âpre     |
|15200456 | Landaize-Kalk | Calcaire de Landaize     |
|15200457 | Balmberg-Oolith | Oolite du Balmberg     |
|15200458 | Hautes-Roches-Algenkalk | Calcaire algaire des Hautes Roches     |
|15200459 | Akzessorische Mumienbänke | Bancs accessoires à momies     |
|15200460 | Brauner Oolith | Brauner Oolith     |
|15200461 | Bleiglanz-Bank | Bleiglanzbank (Fm. de Kaiseraugst)     |
|15200462 | Arenicolites-Bank | Banc à Arenicolites     |
|15200463 | Diagonalschichtiger Sandstein | Diagonalschichtiger Sandstein (Fm. du Dinkelberg)     |
|15200464 | Leutschenberg-Member | Membre du Leutschenberg     |
|15200465 | Schlächtenhaus-Granit | Granite de Schlächtenhaus     |
|15200466 | Steinatal-Gneiskomplex | Complexe gneissique du Steinatal     |
|15200467 | Grenzdolomit | Grenzdolomit (Fm. de Schinznach)     |
|15200468 | Estherien-Schichten | Couches à Estheria (Fm. de Schinznach)     |
|15200469 | Hangende-Bankkalke-Formation | Hangende-Bankkalke-Formation     |
|15200470 | Zementmergel-Formation | Zementmergel-Formation     |
|15200471 | Liegende-Bankkalke-Formation | Liegende-Bankkalke-Formation     |
|15200472 | Obere-Felsenkalke-Formation | Obere-Felsenkalke-Formation     |
|15200473 | Untere-Felsenkalke-Formation | Untere-Felsenkalke-Formation     |
|15200474 | Lacunosamergel-Formation | Lacunosamergel-Formation     |
|15200475 | Oberjura-Massenkalk-Formation | Oberjura-Massenkalk-Formation     |
|15200476 | Lochen-Subformation | Lochen-Subformation     |
|15200477 | Wohlgeschichtete-Kalke-Formation | Wohlgeschichtete-Kalke-Formation     |
|15200478 | Impressamergel-Formation | Impressamergel-Formation     |
|15200479 | Ornatenton-Formation | Ornatenton-Formation     |
|15200480 | Glaukonitsandmergel-Subformation | Glaukonitsandmergel-Subformation     |
|15200481 | Grenzkalk | Grenzkalk     |
|15200482 | Macrocephalenoolith-Subformation | Macrocephalenoolith-Subformation     |
|15200483 | Wutach-Formation | Wutach-Formation     |
|15200484 | Variansmergel-Formation | Variansmergel-Formation     |
|15200485 | Dentalienton-Formation | Dentalienton-Formation     |
|15200486 | Hamitenton-Formation | Hamitenton-Formation     |
|15200487 | Parkinsonioolith-Subformation | Parkinsonioolith-Subformation     |
|15200488 | Gosheim-Formation | Gosheim-Formation     |
|15200489 | Blagdeni-Subformation | Blagdeni-Subformation     |
|15200490 | Humphriesioolith-Subformation | Humphriesioolith-Subformation     |
|15200491 | Wedelsandstein-Formation | Wedelsandstein-Formation     |
|15200492 | Blaukalk-Subformation | Blaukalk-Subformation     |
|15200493 | Murchisonaeoolith-Formation | Murchisonaeoolith-Formation     |
|15200494 | Achdorf-Formation | Achdorf-Formation     |
|15200495 | Tannenwald-Schichten | Couches du Tannenwald     |
|15200496 | Gabelspitz-Schichten | Couches de la Gabelspitz     |
|15200497 | Schallenberg-Member | Marne du Schallenberg     |
|15200498 | Seli-Nagelfluh | Poudingue de Seli     |
|15200499 | Brand-Herrentisch-Tuffit | Tuffite du Brand-Herrentisch     |
|15200500 | Wangen-Tuffit | Tuffite de Wangen     |
|15200501 | Hohenolber-Tuffit | Tuffite du Hohenolber     |
|15200502 | Eichbol-Tuffit | Tuffite d&#39;Eichbol     |
|15200503 | Öhningen-Formation | Formation d&#39;Öhningen     |
|15200504 | Öhningen-Süsswasserkalk | Calcaire d&#39;eau douce d&#39;Öhningen     |
|15200505 | Ramschwag-Nagelfluh | Poudingue de la Ramschwag     |
|15200506 | Seerücken-Tuffit | Tuffite du Seerücken     |
|15200507 | Meilen-Schichten | Couches de Meilen     |
|15200508 | Wulp-Rotzone | Rotzone Wulp     |
|15200509 | Käpfnach-Formation | Formation de Käpfnach     |
|15200510 | «Juranagelfluh-Mergel» | Juranagelfluh-Mergel     |
|15200511 | Golat-Süsswasserkalk | Calcaire d&#39;eau douce du Golat     |
|15200512 | Petrefaktenlager | Petrefaktenlager (Fm. du Belpberg)     |
|15200513 | Hombach-Member | Formation du Hombach     |
|15200514 | Homberg-Formation | Membre de Homberg     |
|15200515 | Gäbris-Nagelfluh | Poudingue du Gäbris     |
|15200516 | Gstaldenbach-Member | Membre du Gstaldenbach     |
|15200517 | Heiden-Member | Membre de Heiden     |
|15200518 | Klusbach-Member | Membre du Klusbach     |
|15200519 | Eggen-Member | Membre de l&#39;Eggen     |
|15200520 | Sulzbach-Member | Membre de Sulzbach     |
|15200521 | Sulzbach-Nagelfluh | Poudingue de Sulzbach     |
|15200522 | Pfingstboden-Member | Membre du Pfingstboden     |
|15200523 | Hochfläschli-Member | Membre de la Hochfläschli     |
|15200524 | Ennetbühl-Member | Membre d&#39;Ennetbühl     |
|15200525 | Hochalp-Member | Membre de la Hochalp     |
|15200526 | Krummenau-Member | Membre de Krummenau     |
|15200527 | Ältere Juranagelfluh | Ältere Juranagelfluh     |
|15200528 | Gitzischöpf-Nagelfluh | Poudingue de la Gitzischöpf     |
|15200529 | Honegg-Mergel | Marne de la Honegg     |
|15200530 | Kaltbach-Nagelfluh | Poudingue du Kaltbach     |
|15200531 | Hünibach-Nagelfluh | Poudingue de Hünibach     |
|15200532 | Losenegg-Formation | Formation de la Losenegg     |
|15200533 | Schwändibach-Naglelfuh | Poudingue de Schwändibach     |
|15200534 | Uerscheli-Formation | Formation d&#39;Uerscheli     |
|15200535 | Bumbach-Nagelfluh | Poudingue de Bumbach     |
|15200536 | Kalksandstein-Serie | Kalksandstein-Serie     |
|15200537 | Gérignoz-Formation | Couches du Gérignoz     |
|15200538 | Leuenfall-Nagelfluh | Poudingue du Leuenfall     |
|15200539 | Wintersberg-Member | Membre du Wintersberg     |
|15200540 | Ebnat-Sandstein | Grès d&#39;Ebnat     |
|15200541 | Rütiberg-Kalksandstein | Grès calcaire de Rütiberg     |
|15200542 | Pfiffegg-Nagelfluh | Poudingue de la Pfiffegg     |
|15200543 | Weggis-Formation | Formation de Weggis     |
|15200544 | Kännelegg-Nagelfluh | Poudingue de la Kännelegg     |
|15200545 | Molasse Rouge des Jurasüdfusses | Molasse Rouge du Pied-du-Jura     |
|15200546 | Mathod-Sandstein | Grès de Mathod     |
|15200547 | Goumoëns-Sandstein | Grès de Goumoëns     |
|15200548 | Molasse Rouge von Vevey | Molasse Rouge de Vevey     |
|15200549 | Molasse Rouge von Monthey | Molasse Rouge de Monthey     |
|15200550 | Grindelegg-Formation | Formation de la Grindelegg     |
|15200551 | Tillerée-Schichten | Couches de Tillerée     |
|15200552 | Serie der Süsswasserkalke und Dolomite | Série des calcaires d&#39;eau douce et dolomie (GMGG)     |
|15200553 | Oltingue-Kalkarenit | Calcarénite d&#39;Oltingue     |
|15200554 | Vaulruz-Formation (UMM-II+III undiff.) | Formation de Vaulruz (UMM-II+III indiff.)     |
|15200555 | Unter-Lochsiti-Nagelfluh | Poudingue d&#39;Unter Lochsitli     |
|15200556 | Flühli-Nagelfluh | Poudingue de Flühli     |
|15200557 | Zone der Schiefermergel (der St.-Gallen-Fm.) | Zone der Schiefermergel (Fm. de Saint-Gall)     |
|15200558 | Marbach-Member | Membre de Marbach     |
|15200559 | Aarwangen-Molasse | Molasse d&#39;Aarwangen     |
|15200560 | Untere Bunte Molasse des Jurasüdfusses | Molasse bariolée inférieure     |
|15200562 | Mittlere Juranagelfluh | Mittlere Juranagelfluh     |
|15200563 | Albstein | Albstein     |
|15200564 | Graupensand | Graupensand     |
|15200565 | Heliciden-Mergel | Marne à Hélicidés     |
|15200566 | Haldenhof-Mergel | Marne de Haldenhof     |
|15200567 | OMM-J | OMM-J     |
|15200568 | Tenniken-Muschelagglomerat | Poudingue coquillier de Tenniken     |
|15200569 | Turritellen-Kalk | Calcaire à Turritelles     |
|15200570 | Randen-Grobkalk | Calcaire grossier du Randen     |
|15200571 | Péry-Geröllsande | Sable à galets de Péry     |
|15200572 | Les-Bayards-Juranagelfluh | Gompholite des Bayards     |
|15200573 | Günsberg- und Vellerat-Formation, undifferenziert | Formation de Günsberg et de Vellerat, indifférenciées     |
|15200574 | Ancepsoolith-Subformation | Ancepsoolith-Subformation     |
|15200575 | Jurensismergel-Formation | Jurensismergel-Formation     |
|15200576 | Posidonienschiefer-Formation | Posidonienschiefer-Formation     |
|15200577 | Amaltheenton-Formation | Amaltheenton-Formation     |
|15200578 | Numismalismergel-Formation | Numismalismergel-Formation     |
|15200579 | Obtususton-Formation | Obtususton-Formation     |
|15200580 | Arietenkalk-Formation | Arietenkalk-Formation     |
|15200581 | Angulatenton-Formation | Angulatenton-Formation     |
|15200582 | Psilonotenton-Formation | Psilonotenton-Formation     |
|15200583 | Bodensee-Nagelfluh | Bodensee-Nagelfluh     |
|15200584 | Tabalcon-Kalk | Tabalcon-Kalk     |
|15200585 | Bonneville-Sandstein | Bonneville-Sandstein     |
|15200586 | Montauban-Mergel | Montauban-Mergel     |
|15200587 | Montauban-Sandstein | Montauban-Sandstein     |
|15200588 | Mornex-Nagelfluh | Mornex-Nagelfluh     |
|15200589 | USM-III bis OSM-I | USM-III bis OSM-I     |
|15200590 | Loorenkopf-Nagelfluh | Loorenkopf-Nagelfluh     |
|15200591 | «Pierre Jaune Supérieure» | «Pierre Jaune Supérieure»     |
|15200592 | «Pierre Jaune Inférieure» | «Pierre Jaune Inférieure»     |
|15200593 | «Formation de la Chambotte Supérieure» | «Formation de la Chambotte Supérieure»     |
|15200594 | «Formation de la Chambotte Inférieure» | «Formation de la Chambotte Inférieure»     |
|15200616 | Kristallin der Nordschweiz | Kristallin der Nordschweiz     |
|15200617 | Variszisches Grundgebirge der Nordschweiz | Variszisches Grundgebirge der Nordschweiz     |
|15200618 | Mümliswil-Süsswasserkalk | Calcaire d&#39;eau douce de Mümliswil     |
|15200619 | Limnischer Horizont (OMM-I) | Horizon limnique (OMM-I)     |
|15200620 | Dardagny-Sandstein | Grès de Dardagny     |
|15200621 | Napf-Formation, proximale Fazies | Napf-Formation, proximale Fazies     |
|15200622 | Napf-Formation, distale Fazies | Napf-Formation, distale Fazies     |
|15200623 | Le-Locle-Formation | Le-Locle-Formation     |
|15200624 | Le-Verger-Member | Le-Verger-Member     |
|15200625 | Combe-Girard-Member | Combe-Girard-Member     |
|15200626 | Crêt-du-Locle-Formation | Crêt-du-Locle-Formation     |
|15200627 | Crêt-du-Locle-Formation, Mergelfazies | Crêt-du-Locle-Formation, Mergelfazies     |
|15200628 | Gitzigrabe-Grobsandstein | Gitzigrabe-Grobsandstein     |
|15200629 | Trois-Rods-Süsswasserkalk | Trois-Rods-Süsswasserkalk     |
|15200630 | Champ-Vuillerat-Süsswasserkalk | Champ-Vuillerat-Süsswasserkalk     |
|15200631 | Wolhusen-Bentonit | Bentonite de Wholusen     |
|15200632 | Gitzitobel-Süsswasserkalk | Clacaire d&#39;eau douce du Gitzitobel     |
|15200633 | Wissenbach-Süsswasserkalk | Calcaire d&#39;eau douce du Wissenbach     |
|15200634 | Altbach-Süsswasserkalk | Calcaire d&#39;eau douce de l&#39;Altbach     |
|15200635 | Tröleten-Süsswasserkalk | Calcaire d&#39;eau douce de Tröleten     |
|15200636 | Tschöplihof-Süsswasserkalk | Calcaire d&#39;eau douce du Tschöplihof     |
|15200637 | Lienegg-Formation | Formation du Lienegg     |
|15200638 | Öligraben-Formation | Formation de l&#39;Öligraben     |
|15200639 | Studweid-Formation | Formation du Studweid     |
|15200640 | Rossemaison-Formation | Formation de Rossemaison     |
|15200641 | Schwaningen-Merenbach-Rhyolith | Rhyolithe de Schwaningen-Merenbach     |
|15200642 | Schwaningen-Weizen-Granit | Granite de Schwaningen-Weizen     |
|15200643 | Etzgen-Granit | Granite d&#39;Etzgen     |
|15200644 | Karbonatreiche Molasse | Karbonatreiche Molasse     |
|15200645 | Karbonatreiche Molasse: Kalk-Dolomit-Nagelfluh | Karbonatreiche Molasse: Kalk-Dolomit-Nagelfluh     |
|15200646 | Hornbüel-Melange | Mélange de Hornbüel     |
|15200647 | Kalter-Wangen-Formation | Formation du Kalter Wangen     |
|15200648 | Baltersweil-Nagelfluh | Poudingue de Baltersweil     |
|15200649 | Netzbachtal-Nagelfluh | Poudingue du Netzbachtal     |
|15200650 | Rocher-des-Hirondelles-Formation | Formation du Rocher des Hirondelles     |
|15200651 | Fort-de-l&#39;Ecluse-Member | Membre du Fort de l&#39;Ecluse     |
|15200652 | Bôle-Member | Membre de Bôle     |
|15200653 | Montcherand-Member | Membre de Montcherand     |
|15200654 | Calcaire Roux | Calcaire Roux     |
|15200655 | Hohentengen-Formation | Formation d&#39;Hohentengen     |
|15200656 | Weilergraben-Formation | Formation du Weilergraben     |
|15200657 | Gugenmühle-Member | Membre du Gugenmühle     |
|15200658 | Schwarzbach-Schichten | Couches du Schwarzbach     |
|15200659 | Wangen- und Letzi-Member, undifferenziert | Membres de Wangen et du Letzi, indifférenciés     |
|15200660 | Grand-Essert- bis Narlay-Formation, undifferenziert | Grand-Essert- bis Narlay-Formation, undifferenziert     |
|15200661 | Goldberg- bis Vuache-Formation, undifferenziert | Goldberg- bis Vuache-Formation, undifferenziert     |
|15200662 | Bellegarde-Bank | Bellegarde-Bank     |
|15200663 | Serrières-Bank | Serrières-Bank     |
|15200664 | Morteau-Bänke | Morteau-Bänke     |
|15200665 | La-Vaux-Bank | La-Vaux-Bank     |
|15200666 | Cul-du-Nozon-Bank | Cul-du-Nozon-Bank     |
|15200667 | Pont-des-Pierres-Bank | Pont-des-Pierres-Bank     |
|15200668 | Censeau-Mergel | Censeau-Mergel     |
|15200669 | Morteau-Mergel | Morteau-Mergel     |
|15200670 | Grande-Varappe-Bank | Grande-Varappe-Bank     |
|15200671 | Le-Coin-Formation | Le-Coin-Formation     |
|15200672 | Bärschwil- bis St-Ursanne-Formation, undifferenziert | Bärschwil- bis St-Ursanne-Formation, undifferenziert     |
|15200673 | Passwang- bis Ifenthal-Formation, undifferenziert | Passwang- bis Ifenthal-Formation, undifferenziert     |
|15200674 | «Calcaires à Entroques» | «Calcaires à Entroques»     |
|15200675 | Staffelegg-Formation und Opalinus-Ton, undifferenziert | Staffelegg-Formation und Opalinus-Ton, undifferenziert     |
|15200676 | Schafisheim-Syenit | Schafisheim-Syenit     |
|15200677 | Pfaffnau-Granit | Pfaffnau-Granit     |
|15200678 | Zurzach-Granit | Zurzach-Granit     |
|15200679 | Siblingen-Granit | Siblingen-Granit     |
|15200680 | Lindau-Granit | Lindau-Granit     |
|15200681 | Kreuzlingen-Granit | Kreuzlingen-Granit     |
|15200682 | Schlächtenhaus-Schiefer | Schlächtenhaus-Schiefer     |
|15200683 | Gersbach-Schiefer | Gersbach-Schiefer     |
|15200684 | Herdern-Streifengneis | Herdern-Streifengneis     |
|15200685 | Courgenay-, Balsthal- und Villigen-Formation, undifferenziert | Courgenay-, Balsthal- und Villigen-Formation, undifferenziert     |
|15200686 | Pichoux-Formation: Korallenfazies | Pichoux-Formation: Korallenfazies     |
|15200687 | Pichoux-Formation: Schwammfazies | Pichoux-Formation: Schwammfazies     |
|15200688 | Kalter-Wangen-Formation: Konglomerat-Fazies | Kalter-Wangen-Formation: Konglomerat-Fazies     |
|15200689 | Kalter-Wangen-Formation: Sandstein-Mergel-Fazies | Kalter-Wangen-Formation: Sandstein-Mergel-Fazies     |
|15200690 | Heilsberg-Bentonit | Heilsberg-Bentonit     |
|15200691 | Humlikon-Bentonit | Humlikon-Bentonit     |
|15202001 | Habkern-Melange | Mélange de Habkern     |
|15202002 | Sörenberg-Melange | Mélange de Sörenberg     |
|15202003 | Wildhaus-Melange | Mélange de Wildhaus     |
|15202004 | Südhelvetische Flyscheinheiten | Unités de flysch sud-helvétiques     |
|15202005 | Nordhelvetische Flysch-Gruppe | Groupe du Flysch nord-helvétique     |
|15202006 | Matt-Formation | Formation de Matt     |
|15202007 | Engi-Dachschiefer | Schistes ardoisiers d&#39;Engi     |
|15202008 | Gruontal-Konglomerat | Conglomérat du Gruontal     |
|15202009 | Elm-Formation | Formation d&#39;Elm     |
|15202010 | Rüschenweid-Bank | Banc du Rüschenweid     |
|15202011 | Taveyannaz-Formation | Formation de Taveyannaz     |
|15202012 | Paläogen des Helvetikums | Paléogène de l&#39;Helvétique     |
|15202013 | Stad-Formation | Formation de Stad     |
|15202014 | Wängen-Kalk | Calcaire de Wängen     |
|15202015 | Jochstock-Konglomerat | Conglomérat du Jochstock     |
|15202016 | Sanetsch-Formation | Formation du Sanetsch     |
|15202017 | Pierredar-Kalk | Calcaire de Pierredar     |
|15202018 | Tsanfleuron-Member | Membre de Tsanfleuron     |
|15202019 | Diablerets-Member | Membre des Diablerets     |
|15202020 | Niederhorn-Formation | Formation du Niederhorn     |
|15202021 | Gemmenalp-Kalk | Calcaire de la Gemmenalp     |
|15202022 | Hohgant-Sandstein | Grès du Hohgant     |
|15202023 | Wagenmoos-Bänke | Couches du Wagenmoos     |
|15202024 | Wildstrubel-Formation | Formation du Wildstrubel     |
|15202025 | Schimberg-Member | Membre du Schimberg     |
|15202026 | Tierberg-Member | Membre du Tierberg     |
|15202027 | Küblibad-Member | Membre du Küblibad     |
|15202028 | Klimsenhorn-Formation | Formation du Klimsenhorn     |
|15202029 | Fruttli-Member | Membre du Fruttli     |
|15202030 | Band-Member | Membre du Bandweg     |
|15202031 | Fräkmünt-Member | Membre de Fräkmünt     |
|15202032 | Bürgen-Formation | Membre du Bürgen(stock)     |
|15202033 | Foribach-Member | Membre du Foribach     |
|15202034 | Mattgrat-Member | Membre du Mattgrat     |
|15202035 | Scharti-Member | Membre de Scharti     |
|15202036 | Euthal-Formation | Formation d&#39;Euthal     |
|15202037 | Steinbach-Member | Membre du Steinbach     |
|15202038 | Einsiedeln-Member | Membre d&#39;Einsiedeln     |
|15202039 | Batöni-Member | Membre de la Batöni     |
|15202040 | Chruteren-Member | Membre de la Chruteren     |
|15202041 | Fliegenspitz-Member | Membre du Fliegenspitz     |
|15202042 | Siderolithikum (des Helvetikums) | Sidérolithique (de l&#39;Helvétique)     |
|15202043 | Grindelwald-Marmor | Marbre de Grindelwald     |
|15202044 | Mürren-Brekzie | Brèche de Mürren     |
|15202045 | Dünden-Konglomerat | Conglomérat de la Dünden     |
|15202046 | Rosenlaui-Marmor | Marbre de Rosenlaui     |
|15202047 | Kreide des Helvetikums | Crétacé de l&#39;Helvétique     |
|15202048 | Wang-Formation | Formation de Wang     |
|15202049 | Amden-Mergel | Marne d&#39;Amden     |
|15202050 | Seewen-Formation | Formation de Seewen     |
|15202051 | Choltal-Member | Membre du Choltal     |
|15202052 | Garschella-Formation | Formation de Garschella     |
|15202053 | Selun-Member | Membre de Selun     |
|15202054 | Kamm-Bank | Banc du Kamm     |
|15202055 | Aubrig-Schichten | Couches de l&#39;Aubrig     |
|15202056 | Wannenalp-Bank | Banc de la Wannenalp     |
|15202057 | Sellamatt-Schichten | Couches de la Sellamatt     |
|15202058 | Plattenwald-Bank | Banc du Plattenwald     |
|15202059 | Durschlägi-Bank | Banc de la Durschlägi     |
|15202060 | Niederi-Schichten | Couches de la Niederi     |
|15202061 | Twäriberg-Bank | Banc du Twäriberg     |
|15202062 | Klaus-Bank | Banc de Klaus     |
|15202063 | Rankweil-Member | Membre de Rankweil     |
|15202064 | Brisi-Member | Membre de la Brisi     |
|15202065 | Brisi-Kalk | Calcaire de la Brisi     |
|15202066 | Brisi-Sandstein | Grès de la Brisi     |
|15202067 | Gams-Schichten | Couches du Gams     |
|15202068 | Luitere-Bank | Banc de la Luitere     |
|15202069 | Freschen-Member | Membre du Freschen     |
|15202070 | Hochkugel-Schichten | Couches du Hochkugel     |
|15202071 | Grünten-Member | Membre du Grünten     |
|15202072 | Rohrbachstein-Bank | Banc du Rohrbachstein     |
|15202073 | Schrattenkalk-Formation | Formation du Schrattenkalk     |
|15202074 | Rawil-Member | Membre du Rawil     |
|15202075 | Tierwis-Formation | Formation de Tierwis     |
|15202076 | Chopf-Bank | Banc du Chopf     |
|15202077 | Drusberg-Member | Membre du Drusberg     |
|15202078 | Altmann-Member | Membre de l&#39;Altmann     |
|15202079 | Helvetischer Kieselkalk | Kieselkalk Helvétique     |
|15202080 | Chriesiloch-Echinodermenkalk | Calcaire échinodermique du Chriesiloch     |
|15202081 | Lidernen-Member | Membre de la Lidernen     |
|15202082 | Gemsmättli-Bank | Banc du Gemsmättli     |
|15202083 | Rahberg-Bank | Membre du Rahberg     |
|15202084 | Betlis-Formation | Formation de Betlis     |
|15202085 | Pygurus-Member | Membre à Pygurus     |
|15202086 | Spitzern-Member | Membre de la Spitzeren     |
|15202087 | Büls-Bank | Banc de Büls     |
|15202088 | Sichel-Kalk | Calcaire de la Sichel     |
|15202089 | Diphyoides-Kalk | Calcaire à Diphyoides     |
|15202090 | Vitznau-Mergel | Marne de Vitznau     |
|15202091 | Öhrli-Formation | Formation de l&#39;Öhrli     |
|15202092 | Palfris-Formation | Formation de Palfris     |
|15202093 | Zementstein-Formation | Formation du Zementstein     |
|15202094 | Graspass-Member | Membre du Graspass     |
|15202095 | Gassen-Kalk | Calcaire du Gassen(stock)     |
|15202096 | Malm des Helvetikums | Malm de l&#39;Helvétique     |
|15202097 | Quinten-Formation | Formation de Quinten     |
|15202098 | Tros-Kalk | Calcaire de Tros     |
|15202099 | «Mergelband» | Mergelband (Fm. de Quinten)     |
|15202100 | Schilt-Formation | Formation du Schilt     |
|15202101 | Mürtschen-Member | Membre de Mürtschen     |
|15202102 | «Schilt-Mergel» | Marne du Schilt     |
|15202103 | «Schilt-Kalk» | Calcaire du Schilt     |
|15202104 | Seeztal-Member | Membre du Seeztal     |
|15202105 | Windgällen-Member | Membre des Windgällen     |
|15202106 | Dogger des Helvetikums | Dogger de l&#39;Helvétique     |
|15202107 | Erzegg-Formation | Formation de l&#39;Erzegg     |
|15202108 | Reischiben-Formation | Formation de la Reischiben     |
|15202109 | Blegi-Eisenoolith | Oolite ferrugineuse de la Blegi     |
|15202110 | Bannalp-Konglomerat | Conglomérat de la Bannalp     |
|15202111 | Guppen-Fossilhorizont | Horizon fossilifère de Guppen     |
|15202112 | Gursbach-Fossilhorizont | Horizon fossilifère du Gursbach     |
|15202113 | Hochstollen-Formation | Formation du Hochstollen     |
|15202114 | Schwarzhorn-Member | Membre du Schwarzhorn     |
|15202115 | Bietenhorn-Member | Membre du Bietenhorn     |
|15202116 | Bommerstein-Formation | Formation du Bommerstein     |
|15202117 | Mols-Member | Membre de Mols     |
|15202118 | Dugny-Formation | Formation de Dugny     |
|15202119 | Coroi-Formation | Formation du Coroi     |
|15202120 | Lias des Helvetikums | Lias de l&#39;Helvétique     |
|15202121 | Brunnistock-Formation | Formation du Brunnistock     |
|15202122 | Inferno-Formation | Formation d&#39;Inferno     |
|15202123 | Monts-Rosset-Formation | Formation des Monts Rosset     |
|15202124 | Torrentalp-Member | Membre de la Torrentalp     |
|15202125 | Sexmor-Formation | Formation du Sexmor     |
|15202126 | Mont-Joly-Formation | Formation du Mont Joly     |
|15202127 | Galm-Member | Membre de Galm     |
|15202128 | Spitzmeilen-Formation | Formation du Spitzmeilen     |
|15202129 | Tierces-Formation | Formation des Tierces     |
|15202130 | Bachalp-Formation | Formation de la Bachalp     |
|15202131 | Prodkamm-Formation | Formation du Prodkamm     |
|15202132 | Cardinia-Member | Membre à Cardinia     |
|15202133 | Stgir-Formation | Formation du Stgir     |
|15202134 | Trias des Helvetikums | Trias de l&#39;Helvétique     |
|15202135 | Besoëns-Formation | Formation des Besoëns     |
|15202136 | Quarten-Formation | Formation de Quarten     |
|15202137 | Arandellys-Formation | Formation des Arandellys     |
|15202138 | Griaz-Member | Membre de la Griaz     |
|15202139 | Röti-Formation | Formation de la Röti     |
|15202140 | Vieux-Emosson-Formation | Formation du Vieux Emosson     |
|15202141 | Mels-Formation | Formation de Mels     |
|15202142 | Permo-Karbon des Helvetikums | Permo-Carbonifère de l&#39;Helvétique     |
|15202143 | Verrucano-Gruppe | Groupe du Verrucano     |
|15202144 | Glarus-Verrucano | Verrucano de Glaris     |
|15202145 | Schönbüel-Formation | Formation de Schönbüel     |
|15202146 | Schönbüel-Quarzit | Quartzite de Schönbüel     |
|15202147 | Kärpf-Formation | Formation du Kärpf     |
|15202148 | Karrenstock-Formation | Formation du Karrenstock     |
|15202149 | Chartegg-Formation | Membre de la Chartegg     |
|15202150 | Fuggstock-Member | Membre du Fuggstock     |
|15202151 | Mären-Formation | Formation de la Mären(egg)     |
|15202152 | Üblital-Formation | Formation de l&#39;Üblital     |
|15202153 | Ilanz-Verrucano | Verrucano d&#39;Ilanz     |
|15202154 | Vernayaz-Formation | Formation de Vernayaz     |
|15202155 | Salvan-Member | Membre de Salvan     |
|15202156 | Vallorcine-Konglomerat | Conglomérat de Vallorcine     |
|15202157 | Haslital-Gruppe | Groupe du Haslital     |
|15202158 | Gastern-Granit | Granite de Gastern     |
|15202159 | Mittagflue-Granit | Granite de la Mittagflue     |
|15202160 | Zentraler Aare-Granit | Granite central de l&#39;Aar     |
|15202161 | Grimsel-Granodiorit | Granodiorite du Grimsel     |
|15202162 | Südwestlicher Aare-Granit | Granite sud-occidental de l&#39;Aar     |
|15202163 | Bugnei-Granodiorit | Granodiorite de Bugnei     |
|15202164 | Spät- bis postvariszische Sedimente und Vulkanite des Aar-Massivs | Roches sédimentaires et volcaniques tardi- à post-varisques du massif de l&#39;Aar     |
|15202165 | Wendenjoch-Formation | Formation du Wendenjoch     |
|15202166 | Windgällen-Formation | Formation des Windgällen     |
|15202167 | Trift-Formation | Formation du Trift     |
|15202168 | Intschi-Formation | Formation d&#39;Intschi     |
|15202169 | Bifertengrätli-Formation | Formation du Bifertengrätli     |
|15202170 | Lakustrisches Member | Membre lacustre (Fm. du Bifertengrätli)     |
|15202171 | Estuarisches Member | Membre estuarien (Fm. du Bifertengrätli)     |
|15202172 | Basales Konglomerat (Bifertengrätli) | Conglomérat basal (Fm. du Bifertengrätli)     |
|15202173 | Grünhorn-Member («Vulkanisches Member») | Membre volcanique (Fm. du Bifertengrätli)     |
|15202174 | Diechtergletscher-Formation | Formation du Diechtergletscher     |
|15202175 | Tscharren-Formation | Formation de la Tscharren     |
|15202177 | Fruttstock-Gruppe | Groupe du Fruttstock     |
|15202178 | Brunni-Granit | Granite de la Brunni     |
|15202179 | Düssi-Diorit | Diorite du Düssi     |
|15202180 | Munt-Dado-Granit | Granite du Munt Dado     |
|15202181 | Russein-Diorit | Diorite de Russein     |
|15202182 | Voralp-Granit | Granite de la Voralp     |
|15202183 | Rötifirn-Gruppe | Groupe du Rötifirn     |
|15202184 | Punteglias-Granit | Granite de Punteglias     |
|15202185 | Tödi-Granit | Granite du Tödi     |
|15202186 | Strem-Granit | Granite du (Val) Strem     |
|15202187 | Baltschieder-Granodiorit | Granodiorite de Baltschieder     |
|15202188 | Giuv-Syenit | Syénite du (Piz) Giuv     |
|15202189 | Curtin-Monzodiorit | Monzodiorite du (Piz) Curtin     |
|15202190 | Bristenstock-Syenit | Syénite du Bristenstock     |
|15202191 | Cavardiras-Gruppe | Groupe de Cavardiras     |
|15202192 | Val-Gliems-Formation | Formation du Val Gliems     |
|15202193 | Bifertenfirn-Formation | Formation du Bifertenfirn     |
|15202194 | Prävariszisches polyzyklisches Grundgebirge des Aar-Massivs | Socle métamorphique polycyclique anté-varisque du massif de l&#39;Aar     |
|15202195 | Innertkirchen-Migmatit | Migmatite d&#39;Innertkirchen     |
|15202196 | Zäsenberg-Gneis | Gneiss du Zäsenberg     |
|15202197 | Erstfeld-Gneiskomplex | Complexe gneissique d&#39;Erstfeld     |
|15202198 | Guttannen-Gneiskomplex | Complexe gneissique de Guttannen     |
|15202199 | Straligenstöckli-Gneiskomplex | Complexe gneissique du Straligenstöckli     |
|15202200 | Lötschental-Gneiskomplex | Complexe gneissique du Lötschental     |
|15202201 | Ofenhorn-Stampfhorn-Gneiskomplex | Complexe gneissique de l&#39;Ofenhorn-Stampfhorn     |
|15202202 | Fully-Granodiorit | Granodiorite de Fully     |
|15202203 | Plex-Aboyeu-Rhyodazit | Rhyodacite de Plex-Aboyeu     |
|15202204 | Vallorcine-Granit | Granite de Vallorcine     |
|15202205 | Miéville-Mylonit | Mylonite de Miéville     |
|15202206 | Montées-Pélissiers-Granit | Granite des Montées-Pélissiers     |
|15202207 | Pormenaz-Granit | Granite de Pormenaz     |
|15202209 | Viséen | Viséen des Aiguilles Rouges     |
|15202210 | Emosson-Glimmerschiefer | Micaschistes d&#39;Emosson     |
|15202211 | Luisin-Orthogneis | Orthogneiss du Luisin     |
|15202212 | Val-Bérard-Gneiskomplex | Complexe gneissique du Val Bérard     |
|15202213 | Lac-Cornu-Eklogit | Éclogite du Lac Cornu     |
|15202214 | Perrons-Orthogneis | Orthogneiss des Perrons     |
|15202215 | Breya-Rhyolith | Rhyolithe de la Breya     |
|15202216 | Mont-Blanc-Granit | Granite du Mont Blanc     |
|15202217 | Montenvers-Granit | Granite du Montenvers     |
|15202218 | Lognan-Orthogneis | Orthogneiss de Lognan     |
|15202219 | Pétoudes-Orthogneis | Orthogneiss des Pétoudes     |
|15202220 | Pesciora-Gruppe | Groupe de Pesciora     |
|15202221 | Rotondo-Granit | Granite du Rotondo     |
|15202222 | Cacciola-Granit | Granite de la Cacciola     |
|15202223 | Sädelhorn-Diorit | Diorite du Sädelhorn     |
|15202224 | Winterhorn-Granit | Granite du Winterhorn     |
|15202225 | Val-Lavaz-Gruppe | Groupe du Val Lavaz     |
|15202226 | Medel-Granit | Granite de Medel     |
|15202227 | Cristallina-Granodiorit | Granodiorite de Cristallina     |
|15202228 | Gamsboden-Granit | Granite du Gamsboden     |
|15202229 | Uffiern-Diorit | Diorite du Val Uffiern     |
|15202230 | Fibbia-Granit | Granite de la Fibbia     |
|15202231 | Val-Rondadura-Gruppe | Groupe du Val Rondadura     |
|15202232 | Borel-Gneiskomplex | Complexe gneissique du Piz Borel     |
|15202233 | Tenelin-Gneiskomplex | Complexe gneissique du Piz Tenelin     |
|15202234 | Laiets-Gneiskomplex | Complexe gneissique des Laiets     |
|15202235 | Tremola-Gneiskomplex | Complexe gneissique de la Tremola     |
|15202236 | Pontino-Gneiskomplex | Complexe gneissique de Pontino     |
|15202237 | Nelva-Gneiskomplex | Complexe gneissique de Nelva     |
|15202238 | Sasso-Rosso-Gneiskomplex | Complexe gneissique du Sasso Rosso     |
|15202239 | Prüsfa-Gneiskomplex | Complexe gneissique de Prüsfa     |
|15202240 | Streifengneis-Komplex | Complexe du Streifengneiss     |
|15202241 | Chastelhorn-Metagabbro | Métagabbro du Chastelhorn     |
|15202242 | Gurschen-Gneis | Gneiss de la Gurschen(alp)     |
|15202243 | Guspis-Gneis | Gneiss de la Guspis     |
|15202244 | Sorescia-Gneis | Gneiss de Sorescia     |
|15202245 | Undifferenzierte Kristallingesteine | roches cristallines indifférenciées     |
|15202246 | Granitartige Gesteine | roches granitiques     |
|15202247 | Saure vulkanische und subvulkanische Gesteine | roches volcaniques et subvolcaniques acides     |
|15202254 | Permische Sedimente der Ilanz-Zone | Sédiments permiens de la zone d&#39;Ilanz     |
|15202255 | Permisch verwittertes Kristallin | Cristallin à altération permienne     |
|15202256 | Goltschenried-Formation | Formation de Goltschenried     |
|15202257 | Oberaar-Furka-Zone | zone de l&#39;Oberaar-Furka     |
|15202258 | Ausserberg-Avat-Zone | zone d&#39;Ausserberg-Avat     |
|15202259 | Migmatit der Ausserberg-Avat-Zone | Migmatite de la zone d&#39;Ausserberg-Avat     |
|15202260 | Granitischer Gneis der Ausserberg-Avat-Zone | Gneiss granitique de la zone d&#39;Ausserberg-Avat     |
|15202261 | Paragneis der Ausserberg-Avat-Zone | Paragneiss de la zone d&#39;Ausserberg-Avat     |
|15202262 | Clavaniev-Zone | zone de Clavaniev     |
|15202263 | Engi-Granit | Granite d&#39;Engi     |
|15202264 | Calmut-Gneiskomplex | Complexe gneissique de Calmut     |
|15202265 | Val-Pigniu-Gneiskomplex | Complexe gneissique du Val Pigniu     |
|15202266 | Permo-Karbon der Urseren-Garvera-Zone | Permo-Carbonifère de la zone d&#39;Urseren-Garvera     |
|15202267 | Goms-Gneiskomplex | Complexe gneissique de Goms     |
|15202268 | Ausserbinn-Piz-Cavel-Zone | zone d&#39;Ausserbinn-Piz Cavel     |
|15202269 | Migmatit der Ausserbinn-Piz-Cavel-Zone | Migmatite de la zone d&#39;Ausserbinn-Piz Cavel     |
|15202270 | Paragneis der Ausserbinn-Piz-Cavel-Zone | Paragneiss de la zone d&#39;Ausserbinn-Piz Cavel     |
|15202271 | Prosa-Granit | Granite du (Monte) Prosa     |
|15202272 | Val-Tremola-Granit | Granite du Val Tremola     |
|15202273 | Leventina-Gneis | Gneiss de la Leventina     |
|15202274 | Orthogneis der Lukmanier-Decke | Orthogneiss de la nappe du Lukmanier     |
|15202275 | Paragneis der Lukmanier-Decke | Paragneiss de la nappe du Lukmanier     |
|15202276 | Val-Stgira-Riffmarmor | Marbre du Val Stgira     |
|15202277 | Fossilmarmor | Fossilmarmor     |
|15202278 | Fanee-Trias | Trias de Fanee     |
|15202279 | Ultrahelvetische Flyscheinheiten | Unités de flysch ultrahelvétiques     |
|15202280 | Sardona-Melange | Mélange du Sardona     |
|15202281 | Martinsmad-Formation | Formation de Martinsmad     |
|15202282 | Obere Flyschabfolge (Sardona) | Obere Flyschabfolge (Sardona)     |
|15202283 | Sardona-Member | Quartzite du Sardona     |
|15202284 | Untere Flyschabfolge (Sardona) | Untere Flyschabfolge (Sardona)     |
|15202285 | Meilleret-Formation | Formation du Meilleret     |
|15202286 | Lavtina-Sandstein | Grès de Lavtina     |
|15202287 | Blattengrat-Sandstein | Grès du Blattengrat     |
|15202288 | Burg-Sandstein | Grès de Burg     |
|15202289 | Val-d&#39;Illiez-Sandstein | Grès du Val-d&#39;Illiez     |
|15202290 | Muot-da-Rubi-Formation | Formation du Muot da Rubi     |
|15202291 | Ahornen-Member | Membre du Ahornen     |
|15202292 | Kistenstöckli-Member | Membre du Kistenstöckli     |
|15202293 | Ghölzwald-Member | Membre du Ghölzwald     |
|15202294 | Malor-Member | Membre du Malor     |
|15202295 | Südelbach-Member | Membre du Südelbach     |
|15202296 | Kleintal-Konglomerat | Conglomérat du Kleintal     |
|15202297 | Rütenen-Konglomerat | Conglomérat de Rütenen     |
|15202298 | Jura des Helvetikums | Jurassique de l&#39;Helvétique     |
|15202299 | Wang-Brekzie | Brèche de Wang     |
|15202300 | «Oberer Schrattenkalk» | «Oberer Schrattenkalk»     |
|15202301 | «Unterer Schrattenkalk» | «Unterer Schrattenkalk»     |
|15202302 | Oberer Quintner Kalk | «Oberer Quinten-Kalk»     |
|15202303 | Unterer Quintner Kalk | «Unterer Quinten-Kalk»     |
|15202304 | Planplatte-Eisenoolith | Oolite ferrugineuse de la Planplatte     |
|15202305 | Geissbach-Konglomerat | Conglomérat du Geissbach     |
|15202306 | Stöcki-Sandstein | Grès de Stöckli     |
|15202307 | Infrapräalpines Melange | Mélange Infrapréalpin     |
|15202308 | Iberg-Melange | Mélange d&#39;Iberg     |
|15202309 | Surbrunnen-Flysch | Flysch de Surbrunnen     |
|15202310 | Roggenegg-Komplex | Complexe de la Roggenegg     |
|15202311 | Isentobel-Komplex | Complexe de l&#39;Isentobel     |
|15202312 | Serhalten-Flysch | Flysch der Serhalten     |
|15202313 | Gwürz-Flysch | Flysch de Gwürz     |
|15202314 | Ruestel-Flysch | Flysch de Ruestel     |
|15202315 | Scheidegg-Flysch | Flysch de la Scheidegg     |
|15202316 | Habkern-Granit | Granite de Habkern     |
|15202317 | Gros-Plané-Melange | Mélange du Gros Plané     |
|15202318 | Bodevena-Melange | Mélange de la Bodevena     |
|15202319 | Subalpiner Flysch | Flysch Subalpin     |
|15202320 | Torrenthorn-Formation | Formation du Torrenthorn     |
|15202321 | Weissgandstöckli-Bank | Banc du Weissgandstöckli     |
|15202322 | Grisch-Member | Membre du (Piz) Grisch     |
|15202323 | Foostock-Member | Membre du Foostock     |
|15202324 | Murgtal-Formation | Formation du Murgtal     |
|15202325 | Dzéman-Member | Membre du Dzéman     |
|15202326 | Aplitische Randfazies des Zentralen Aare-Granits | Faciès de bordure aplitique du Granite Central de l&#39;Aar     |
|15202327 | Windgällen-Formation, Rhyolith | Rhyolithe de la Chli Windgällen     |
|15202328 | Bäregg-Gneiskomplex | Complexe gneissique de la Bäregg     |
|15202329 | Gärsthorn-Gneiskomplex | Complexe gneissique du Gärsthorn     |
|15202330 | Sogn-Placi-Gneiskomplex | Complexe gneissique de Sogn Placi     |
|15202331 | Massa-Gneiskomplex | Complexe gneissique de la Massa     |
|15202332 | Mittelvariszische Intrusiva des Aiguilles-Rouges-Massivs | Roches plutoniques éo-varisques du massif des Aiguilles Rouges     |
|15202333 | Frühvariszische Intrusiva des Aiguilles-Rouges-Massivs | Roches plutoniques éo-varisques du massif des Aiguilles Rouges     |
|15202334 | Prävariszisches polyzyklisches Grundgebirge des Aiguilles-Rouges-Massivs | Socle polycyclique anté-varisque du massif des Aiguilles Rouges     |
|15202335 | Chéserys-Gneis | Gneiss des Chéserys     |
|15202336 | Spät- bis postvariszische Intrusiva des Mont-Blanc-Massivs | Roches plutoniques tardi- à post-varisques du massif du Mont Blanc     |
|15202337 | Prävariszisches polyzyklisches Grundgebirge des Mont-Blanc-Massivs | Socle polycyclique anté-varisque du massif du Mont Blanc     |
|15202338 | Alp-Cavradi-Gneiskomplex | Complexe gneissique de l&#39;Alp Cavradi     |
|15202339 | Giubine-Gneiskomplex | Complexe gneissique de Giubine     |
|15202340 | Prävariszisches polyzyklisches Grundgebirge der Gotthardt-Decke | Socle polycyclique anté-varisque de la nappe du Gotthard     |
|15202341 | Unterwassern-Gneis | Gneiss d&#39;Unterwassern     |
|15202343 | Sassina-Augengneis | Gneiss oeillé du Sassina     |
|15202344 | Alp-Ramosa-Granitgneis | Gneiss granitique de l&#39;Alp Ramosa     |
|15202346 | Val-Nalps-Gneiskomplex | Complexe gneissique du Val Nalps     |
|15202347 | Prato-Gneis | Gneiss de Prato     |
|15202348 | Distelgrat-Gneis | Gneiss du Distelgrat     |
|15202349 | Val-Gronda-Augengneis | Gneiss oeillé du Val Gronda     |
|15202350 | Fuorcla-Paradis-Serpentinit | Serpentinite de la Fuorcla Paradis     |
|15202351 | Paradis-Gneiskomplex | Complexe gneissique du (Piz) Paradis     |
|15202352 | Oberstafel-Gneis | Gneiss d&#39;Oberstafel     |
|15202353 | Ganneretsch-Gneis | Gneiss du (Piz) Ganneretsch     |
|15202354 | Corandoni-Amphibolit | Amphibolite de Corandoni     |
|15202355 | Prävariszisches polyzyklisches Grundgebirge der Tavetsch-Decke | Socle polycyclique anté-varisque de la nappe du Tavetsch     |
|15202356 | Rueras-Gneiskomplex | Complexe gneissique de Rueras     |
|15202357 | Prä- und Frühvariszische Sedimente und Vulkanite des Aiguilles-Rouges-Massivs | Roches sédimentaires et volcaniques éo-varisques du massif des Aiguilles Rouges     |
|15202358 | Au-d&#39;Arbignon-Schiefer | Schistes de l&#39;Au d&#39;Arbignon     |
|15202359 | Dorénaz-Konglomerat | Conglomérat de Dorénaz     |
|15202360 | «Wildflysch», undifferenziert | «Wildflysch», undifferenziert     |
|15202361 | Plaine-Morte-Melange | Plaine-Morte-Melange     |
|15202362 | Mättental-Melange | Mättental-Melange     |
|15202363 | Höchst-Flysch | Höchst-Flysch     |
|15202364 | Kiental-Melange | Kiental-Melange     |
|15202365 | Termen-Tonschiefer | Termen-Tonschiefer     |
|15202366 | Termen-Kalkschiefer | Termen-Kalkschiefer     |
|15202367 | Nufenen-Knotenschiefer | Nufenen-Knotenschiefer     |
|15202368 | Nufenen-Sandstein | Nufenen-Sandstein     |
|15202369 | Nufenen-Granatschiefer | Nufenen-Granatschiefer     |
|15202370 | Stgir-Formation, Unterer Teil | Stgir-Formation, Unterer Teil     |
|15202371 | Stgir-Formation, Oberer Teil | Stgir-Formation, Oberer Teil     |
|15202372 | Runcaleida-Schichten | Runcaleida-Schichten     |
|15202373 | Riein-Schichten | Riein-Schichten     |
|15202374 | Meierhof-Phyllit | Meierhof-Phyllit     |
|15202375 | Waltensburg-Verrucano | Waltensburg-Verrucano     |
|15202376 | Ruinas-Sandstein | Ruinas-Sandstein     |
|15202377 | Berglikehle-Bank | Berglikehle-Bank     |
|15202378 | Rossplatten-Diorit | Rossplatten-Diorit     |
|15202379 | Schöllenen-Diorit | Schöllenen-Diorit     |
|15202380 | Grotzen-Austernbank | Grotzen-Austernbank     |
|15202381 | Hurst-Mergel | Hurst-Mergel     |
|15202382 | Palis-Member | Palis-Member     |
|15202383 | «Oberer Öhrlikalk» | «Oberer Öhrlikalk»     |
|15202384 | «Oberer Öhrlimergel» | «Oberer Öhrlimergel»     |
|15202385 | «Unterer Öhrlikalk» | «Unterer Öhrlikalk»     |
|15202386 | Spitzmeilen-Formation, Oberer Teil | Spitzmeilen-Formation, Oberer Teil     |
|15202387 | Spitzmeilen-Formation, Unterer Teil | Spitzmeilen-Formation, Unterer Teil     |
|15202388 | Spitzmeilen-Formation, Basaler Teil | Spitzmeilen-Formation, Basaler Teil     |
|15202389 | Prodkamm-Formation, Oberer Teil | Prodkamm-Formation, Oberer Teil     |
|15202390 | Prodkamm-Formation, Mittlerer Teil | Prodkamm-Formation, Mittlerer Teil     |
|15202391 | Prodkamm-Formation, Unterer Teil | Prodkamm-Formation, Unterer Teil     |
|15202392 | Sandpass-Formation | Sandpass-Formation     |
|15202393 | Roc-Champion-Konglomerat | Roc-Champion-Konglomerat     |
|15202394 | Spirstock-Member | Membre du Spirstock     |
|15202395 | «Roter Seewenkalk» | «Roter Seewenkalk»     |
|15202396 | Untere Götzis-Bank | Banc de Götzis inférieur     |
|15202397 | Col-de-la-Plaine-Morte-Bank | Banc du Col de la Plaine Morte     |
|15202398 | «Oberer Betliskalk» | «Oberer Betliskalk»     |
|15202399 | «Unterer Betliskalk» | «Unterer Betliskalk»     |
|15202400 | Vättis-Fossilbrekzie | Brèche fossilifère de Vättis     |
|15202401 | Inferno-Formation, Oberer Teil | Formation d&#39;Inferno, partie supérieure     |
|15202402 | Inferno-Formation, Mittlerer Teil | Formation d&#39;Inferno, partie moyenne     |
|15202403 | Inferno-Formation, Unterer Teil | Formation d&#39;Inferno, partie inférieure     |
|15202404 | Sexmor-Formation, Oberer Teil | Formation du Sexmor, partie supérieure     |
|15202405 | Sexmor-Formation, Unterer Teil | Formation du Sexmor, partie inférieure     |
|15202406 | «Leitoolith» | «Leitoolith»     |
|15202411 | Lochegg-Brekzie | Brèche de la Lochegg     |
|15202412 | «Obere Zementsteinschichten» | «Obere Zementsteinschichten»     |
|15202413 | «Untere Zementsteinschichten» | «Untere Zementsteinschichten»     |
|15202414 | «Rote Echinodermenbrekzie» | «Rote Echinodermenbrekzie»     |
|15202415 | «Obere Tonschiefer» (Bommerstein-Fm.) | «Obere Tonschiefer» (Fm. du Bommerstein)     |
|15202416 | Glockhaus-Member | Membre du Glockhaus     |
|15202417 | «Basaler Quarzit» (Coroi-Fm.) | «Quartzite de base» (Fm. du Coroi)     |
|15202418 | Rauwacke (Röti-Fm.) | Cornieule (Fm. de la Röti)     |
|15202419 | Col-du-Jorat-Member | Membre du Col du Jorat     |
|15202420 | «Equisetenschiefer» | «Equisetenschiefer»     |
|15202421 | Leist-Mergel | Marne du Leist     |
|15202422 | Leiboden-Mergel | Marne du Leiboden     |
|15202423 | Covayes-Formation | Formation des Covayes     |
|15202424 | Javrex-Formation | Formation du Javrex     |
|15202425 | «Marnes noires pyriteuses» | «Marnes noires pyriteuses»     |
|15202426 | «Calcaires gréso-glauconieux» | «Calcaires gréso-glauconieux»     |
|15202427 | «Calcarénites beiges oolitiques» | «Calcarénites beiges oolitiques»     |
|15202428 | «Calcaire siliceux brunâtre» | «Calcaire siliceux brunâtre»     |
|15202429 | Villarbeney-Formation | Formation de Villarbeney     |
|15202430 | Veveyse-de-Châtel-Member | Membre de la Veveyse de Châtel     |
|15202431 | Riondouneire-Member | Membre de Riondouneire     |
|15202432 | Jogne-Formation | Formation de la Jogne     |
|15202433 | «Calcaires bréchiques» | «Calcaires bréchiques»     |
|15202434 | Vuavres-Member | Membre des Vuavres     |
|15202435 | Planière-Member | Membre de la Planière     |
|15202436 | Bifé-Formation | Formation de Bifé     |
|15202437 | «Calcaire à ciment» (Bifé-Fm.) | «Calcaire à ciment» (Fm. de Bifé)     |
|15202438 | Joux-Galez-Member | Membre de Joux Galez     |
|15202439 | Pereyres-Formation | Formation de la Pereyre     |
|15202440 | Praz-Couquain-Formation | Formation de Praz Couquain     |
|15202442 | Gryonne-Formation | Formation de la Gryonne     |
|15202443 | Taffon-Member | Membre du Taffon     |
|15202444 | Saix-Member | Membre des Saix     |
|15202445 | Cergnement-Member | Membre du Cergnement     |
|15202446 | Arveyes-Flysch | Flysch de la nappe d&#39;Arveyes     |
|15202447 | Sex-Mort-Flysch | Flysch de la nappe du Sex Mort     |
|15202448 | Maasplanggstock-Metaandesit | Méta-andésite du Maasplanggstock     |
|15202449 | Dammagletscher-Diorit | Diorite du Dammagletscher     |
|15202450 | Schiefriger Mines-Lias | Lias des Mines schisteux     |
|15202451 | Kalkiger Mines-Lias | Lias des Mines calcaire     |
|15202452 | Basaler Mines-Lias | Lias des Mines basal     |
|15202453 | Tektonisierte Basis des Glarner-Verrucano | base tectonisée du Verrucano de Glaris («Plagioklasgneis»)     |
|15202454 | Chrüzlistock-Migmatit | Migmatite du Chrüzlistock     |
|15202455 | Piz-Cuolmet-Gneiskomplex | Complexe gneissique du Piz Cuolmet     |
|15202456 | Pulanera-Gneiskomplex | Pulanera-Gneiskomplex     |
|15202464 | Spät- bis postvariszische Sedimente und Vulkanite des Helvetikums | Roches sédimentaires et volcaniques tardi- à post-varisques de l&#39;Helvétique     |
|15202465 | Permo-Karbon des Aiguilles-Rouges-Massivs | Permo-Carbonifère du massif des Aiguilles Rouges     |
|15202466 | Kristallin des Helvetikums | Socle cristallin de l&#39;Helvétique     |
|15202467 | Variszisches Kristallin des Helvetikums | Variszisches Kristallin des Helvetikums     |
|15202468 | Prävariszisches polyzyklisches Grundgebirge des Helvetikums | Socle polycyclique anté-varisque de l&#39;Helvétique     |
|15202469 | Undifferenziertes Kristallin des Helvetikums | Socle cristallin indifférencié de l&#39;Helvétique     |
|15202472 | Catogne-Gneiskomplex | Complexe gneissique du Catogne     |
|15202473 | Grépillon-Leukogranitporphyr | Leucogranite des Grépillons     |
|15202474 | Arpette-Leukogranit | Leucogranite d&#39;Arpette     |
|15202475 | Bitschji-Augengneis | Gneiss oeillé de Bitschji     |
|15202476 | Geimen-Augengneis | Gneiss oeillé de Geimen     |
|15202477 | Altkristallin des Mont-Blanc-Massivs, migmatitisch | Socle polycyclique anté-varisque du massif du Mont Blanc, migmatitique     |
|15202478 | Altkristallin des Mont-Blanc-Massivs, amphibolitreich | Socle polycyclique anté-varisque du massif du Mont Blanc, riche en amphibolites     |
|15202479 | Altkristallin des Mont-Blanc-Massivs, mylonitisch | Socle polycyclique anté-varisque du massif du Mont Blanc, mylonitique     |
|15202480 | Morcles-Mikrogranit | Microgranite de Morcles     |
|15202481 | Altkristallin des Aiguilles-Rouges-Massivs, migmatitisch | Socle polycyclique anté-varisque du massif des Aiguilles Rouges, migmatitique     |
|15202482 | Fully-Gneiskomplex | Complexe gneissique de Fully     |
|15202483 | Hinterbalm-Granit | Granite d&#39;Hinterbalm     |
|15202484 | Balmenegg-Granit | Granite de la Balmenegg     |
|15202485 | Unter-der-Flue-Fazies | faciès d&#39;Unter-der-Flue     |
|15202486 | Pardatschas-Granit | Granite du (Piz) Pardatschas     |
|15202487 | Rossbodenstock-Diorit | Diorite du Rossbodenstock     |
|15202488 | Val-da-Surplattas-Diorit | Diorite du Val da Surplattas     |
|15202489 | Rinderbiel-Mikrogranit | Microgranite de Rinderbiel     |
|15202490 | Dachquarzit (Leventina) | Dachquarzit (Leventina)     |
|15202491 | Kapfen-Formation | Formation de Kapfen     |
|15202492 | Kapfen-Sandstein | Grès de Kapfen     |
|15202493 | Kärpfgipfel-Sernifit | Sernifite du Kärpfgipfel     |
|15202494 | Fulen-Formation | Formation du Fulen     |
|15202495 | Glattmatt-Member | Membre de Glattmatt     |
|15202496 | Hahnenstock-Keratophyr | Kératophyre du Hahnenstock     |
|15202497 | Sonnenberg-Horizonte | Horizons du Sonnenberg     |
|15202498 | Chamseeli-Konglomerat | Conglomérat du Chamseeli     |
|15202499 | Rotberg-Sandstein | Grès du Rotberg     |
|15202500 | Seez-Member | Membre de Seez     |
|15202501 | Gufelialp-Member | Membre de la Gufelialp     |
|15202502 | Ilanz-Verrucano s.s. | Verrucano d&#39;Ilanz s.s.     |
|15202503 | Buntgefleckte Schiefer | Buntgefleckte Schiefer (Ilanz)     |
|15202504 | Perm der Tavetsch-Decke (Val Acla Mulin) | Permien de la nappe du Tavetsch (Val Acla Mulin)     |
|15202505 | Windgällen-Formation, Mikrogranit | Microgranite de la Windgällenlücke     |
|15202506 | Sandalp-Rhyolith | Rhyolithe de la Sandalp     |
|15202507 | Tuffitisches Member (Tscharren) | Tuffitisches Member (Tscharren)     |
|15202508 | Ignimbritisches Member (Tscharren) | Ignimbritisches Member (Tscharren)     |
|15202509 | Guschakopf-Sandstein | Grès du Guschakopf     |
|15202510 | Gonzen-Eisenerzhorizont | Horizon du Gonzen     |
|15202511 | Schabell-Mélange | Schabell-Mélange     |
|15202512 | Taveyannaz-Sandstein, Dachschiefer vorherrschend | Taveyannaz-Sandstein, Dachschiefer vorherrschend     |
|15202513 | Helvetischer Kieselkalk, Oberer Teil | Helvetischer Kieselkalk, Oberer Teil     |
|15202514 | Helvetischer Kieselkalk, Unterer Teil | Helvetischer Kieselkalk, Unterer Teil     |
|15202515 | Helvetischer Kieselkalk, Basisschiefer | Helvetischer Kieselkalk, Basisschiefer     |
|15202516 | Toarcienschiefer | Toarcienschiefer     |
|15202517 | Toarcienspatkalk | Toarcienspatkalk     |
|15202518 | Domérien-Sandstein | Domérien-Sandstein     |
|15202519 | Pliensbachien-Spatkalk | Pliensbachien-Spatkalk     |
|15202520 | Lotharingien-Sandstein | Lotharingien-Sandstein     |
|15202521 | Iserin-Flysch | Iserin-Flysch     |
|15202522 | Meilleret-Formation, Calcaires organo-détritiques | Meilleret-Formation, Calcaires organo-détritiques     |
|15202523 | Meilleret-Formation, Arkose | Meilleret-Formation, Arkose     |
|15202524 | Meilleret-Formation, Conglomérat basal | Meilleret-Formation, Conglomérat basal     |
|15202525 | Grenzquarzit der Bommerstein-Formation | Grenzquarzit der Bommerstein-Formation     |
|15202526 | Telltistock-Granit | Telltistock-Granit     |
|15202527 | Öhrli-Formation, von Siderolithikum durchsetzt | Formation de l&#39;Öhrli, à infiltrations de Sidérolithique     |
|15202528 | Beesten-Fazies | faciès de Beesten     |
|15202529 | Garwiidi-Diorit | Diorite de Garwiidi     |
|15202530 | Alp-Crap-Ner-Granit | Granite de l&#39;Alp Crap Ner     |
|15202531 | Innertkirchen-Migmatit, permisch verwittert | Migmatite d&#39;Innertkirchen, à altération permienne     |
|15202532 | Erstfeld-Gneiskomplex, permisch verwittert | Complexe gneissique d&#39;Erstfeld, à altération permienne     |
|15202533 | Suren-Flysch | Flysch du Suren     |
|15202534 | Obere Sandsteine (Spirstock) | Obere Sandsteine (Spirstock)     |
|15202535 | Blockmergel (Spirstock) | Blockmergel (Spirstock)     |
|15202536 | Untere Sandsteine (Spirstock) | Untere Sandsteine (Spirstock)     |
|15202537 | Ringgenberg-Schichten | Couches de Ringgenberg     |
|15202538 | Malmbrekzie | Brèche du Malm     |
|15202539 | Schattwald-Mergelkalk | Calcaire marneux du Schattwald     |
|15202540 | Elm- und Matt-Formation, undifferenziert | Formations d&#39;Elm et de Matt, indifférenciées     |
|15202541 | Elm- und Matt-Formation: Quarzsandstein | Formations d&#39;Elm et de Matt: grès quartzitique     |
|15202542 | Nordhelvetische Flysch-Gruppe, vorw. schiefriger Tonstein | Formations d&#39;Elm et de Matt: argillite schisteuse     |
|15202543 | Schwalmern-Schiefer | Schistes de la Schwalmern     |
|15202544 | Schwalmern-Kalk | Calcaire de la Schwalmern     |
|15202545 | Glockhaus-Member: Schiefriger Eisensandstein | Membre du Glockhaus: grès ferrugineux schisteux     |
|15202546 | Dolomit der Helvetische Trias | Dolomie du Trias helvétique     |
|15202547 | Rauwacke der Helvetische Trias | Cornieule du Trias helvétique     |
|15202548 | Gips der Helvetische Trias | Gypse du Trias helvétique     |
|15202549 | Baltschieder-Granodiorit: Biotittonalit | Granodiorite de Baltschieder: tonalite à biotite     |
|15202550 | Baltschieder-Granodiorit: Hornblende Biotittonalit | Granodiorite de Baltschieder: tonalite à biotite et horneblende     |
|15202551 | Erstfeld-Gneiskomplex: Biotit-Plagioklasgneis | Complexe gneissique d&#39;Erstfeld: gneiss à plagioclase et biotite     |
|15202552 | Erstfeld-Gneiskomplex: Orthogneis | Complexe gneissique d&#39;Erstfeld: orthogneiss     |
|15202553 | Erstfeld-Gneiskomplex: Migmatit | Complexe gneissique d&#39;Erstfeld: migmatite     |
|15202554 | Guttannen-Gneiskomplex: Paragneis | Complexe gneissique de Guttannnen: paragneiss     |
|15202555 | Guttannen-Gneiskomplex: Orthogneis | Complexe gneissique de Guttannnen: orthogneiss     |
|15202556 | Guttannen-Gneiskomplex: Biotit-Choritschiefer | Complexe gneissique de Guttannnen: schiste à chlorite et biotite     |
|15202557 | Guttannen-Gneiskomplex: Chlorit-Serizitschiefer | Complexe gneissique de Guttannnen: schiste à séricite et chlorite     |
|15202558 | Lötschental-Gneiskomplex: Muskovitgneis | Complexe gneissique du Lötschental: gneiss à muscovite     |
|15202559 | Lötschental-Gneiskomplex: migmatitischer Biotitgneis | Complexe gneissique du Lötschental: gneiss à biotite migmatitique     |
|15202560 | Lötschental-Gneiskomplex: Chloritschiefer | Complexe gneissique du Lötschental: schiste à chlorite     |
|15202561 | Ofenhorn-Stampfhorn-Gneiskomplex: gebänderter Biotit-Plagioklasgneis | Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: gneiss rubané à plagioclase et biotite     |
|15202562 | Ofenhorn-Stampfhorn-Gneiskomplex: Migmatit | Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: migmatite     |
|15202563 | Ofenhorn-Stampfhorn-Gneiskomplex: Biotitgneis | Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: gneiss à biotite     |
|15202564 | Ofenhorn-Stampfhorn-Gneiskomplex: Orthogneis | Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: orthogneiss     |
|15202565 | Bäregg-Gneiskomplex: mylonitischer Orthogneis | Complexe gneissique de la Bäregg: orthogneiss mylonitique     |
|15202566 | Bäregg-Gneiskomplex: mylonitischer Paragneis | Complexe gneissique de la Bäregg: paragneiss mylonitique     |
|15202567 | Bäregg-Gneiskomplex: Metavulkanite | Complexe gneissique de la Bäregg: métavulcanite     |
|15202568 | Grimsel-Granodiorit: aplitische Randfazies | Granodiorite du Grimsel: faciès aplitique de bordure     |
|15202569 | Voralp-Granit: saure Randfazies | Granite de la Voralp: faciès acide de bordure     |
|15202570 | Tamina-Gneiskomplex | Complexe gneissique de la Tamina     |
|15202571 | Tamina-Gneiskomplex: schiefriger Biotitgneis | Complexe gneissique de la Tamina: gneiss schisteux à biotite     |
|15202572 | Tamina-Gneiskomplex: mylonitisch | Complexe gneissique de la Tamina: mylonitique     |
|15202573 | Innertkirchen-Migmatit: Marmor | Migmatite d&#39;Innertkirchen: marbre     |
|15202574 | Guttannen-Gneiskomplex: Migmatit | Complexe gneissique de Guttannnen: migmatite     |
|15202575 | Guttannen-Gneiskomplex: Amphibolit führend | Complexe gneissique de Guttannnen: avec amphibolite     |
|15202576 | Guttannen-Gneiskomplex: aplitischer Granit | Complexe gneissique de Guttannnen: granite aplitique     |
|15202577 | Guttannen-Gneiskomplex: Marmor | Complexe gneissique de Guttannnen: marbre     |
|15202578 | Guttannen-Gneiskomplex: Ultramafit | Complexe gneissique de Guttannnen: roche ultramafique     |
|15202579 | Ofenhorn-Stampfhorn-Gneiskomplex: mit Schollenamphibolit | Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: avec amphibolite à blocs     |
|15202580 | Ofenhorn-Stampfhorn-Gneiskomplex: aplitischer Granit | Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: granite aplitique     |
|15202581 | Ofenhorn-Stampfhorn-Gneiskomplex: Schollenamphibolit | Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: amphibolite à blocs     |
|15202582 | Ofenhorn-Stampfhorn-Gneiskomplex: Ultramafit | Complexe gneissique de l&#39;Ofenhorn-Stampfhorn: roche ultramafique     |
|15202583 | Bommerstein- und Reischiben-Formation, undifferenziert | Formations de Bommerstein et de Reischiben, indifférenciées     |
|15202584 | Mels- und Röti-Formation, undifferenziert | Formations de Mels et de Röti, indifférenciées     |
|15202585 | Guttannen-Gneiskomplex: schierfriger Biotit-Chlorit-Serizit-Gneis | Complexe gneissique de Guttannnen: gneiss schisteux à biotite, chlorite, séricite     |
|15202586 | Zettenalp-Trochematt-Melange | Mélange de la Zettenalp-Trochematt     |
|15202587 | Laubersmad-Flysch | Flysch du Laubersmad     |
|15202588 | Stad-Formation, «Jüngerer Quarzsandstein» | Formation de Stad, «Jüngerer Quarzsandstein»     |
|15202589 | Einsiedeln-Member, «Älterer Quarzsandstein» | Membre d&#39;Einsiedeln, «Älterer Quarzsandstein»     |
|15202590 | Schrattenkalk-Formation, vermergelt | Formation du Schrattenkalk, devenant marneuse     |
|15202591 | Wängen-Kalk, Lithothamnienkalk-Fazies | Calcaire de Wängen, faciès calcaire à Lithothamnies     |
|15202592 | Einsiedeln-Member, Alveolinenkalk-Fazies | Membre d&#39;Einsiedeln, faciès calcaire à Alvéolines     |
|15202593 | Hohgant-Sandstein, Sandkalk und Kalk | Grès du Hohgant, calcaire gréseux et calcaire     |
|15202594 | Tektonisches Melange der Internen Einsiedeln-Schuppen | Mélange tectonique des écailles internes d&#39;Einsiedeln     |
|15202595 | Bürgen- und Wildstrubel-Formation, undiff. | Formations du Bürgen et d&#39;Euthal, indiff.     |
|15202596 | Einsiedeln- und Steinibach-Member, undifferenziert | Formation de l&#39;Euthal et Membre du Steinbach, indiff.     |
|15202597 | Stad-Formation (e6) | Formation de Stad (e6)     |
|15202598 | Stgir- und Inferno-Formation, undifferenziert | Formations du Stgir et d&#39;Inferno, indifférenciées     |
|15202599 | Oberer Quintner Kalk: Korallenkalk | Oberer Quintner Kalk: calcaire à coraux     |
|15202600 | Oberer Quintner Kalk: Unterer Kalk | Oberer Quintner Kalk: Unterer Kalk     |
|15202601 | Prodkamm- bis Sexmor-Formation, undifferenziert | Formation du Prodkamm à Formation du Sexmor, indifférenciées     |
|15202602 | Plattenzüg-Formation | Formation du Plattazüg     |
|15202603 | Zemenstein- bis Garschella-Formation, undifferenziert | Formation du Zementstein à Formation de Garschella, indifférenciées     |
|15202604 | Vasanachopf-Member | Formation d&#39;Euthal: faciès argilo-schisteux noir     |
|15202605 | Pfäfers-Formation | Pfäfers-Formation     |
|15202606 | Euthal- und Bürgen-Formation, undifferenziert | Euthal- und Bürgen-Formation, undifferenziert     |
|15202607 | Amden- und Wang-Formation, undifferenziert | Amden- und Wang-Formation, undifferenziert     |
|15202608 | Seewen- und Amden-Formation, undifferenziert | Seewen- und Amden-Formation, undifferenziert     |
|15202609 | Betlis- bis Schrattenkalk-Formation, undifferenziert | Betlis- bis Schrattenkalk-Formation, undifferenziert     |
|15202610 | Öhrli- bis Schrattenkalk-Formation, undifferenziert | Öhrli- bis Schrattenkalk-Formation, undifferenziert     |
|15202611 | Mols-Members, Basisbildungen | Mols-Members, Basisbildungen     |
|15202612 | Öhrli- und Betlis-Formation, undifferenziert | Öhrli- und Betlis-Formation, undifferenziert     |
|15202613 | Erzegg-Formation: Grenzschicht | Erzegg-Formation: Grenzschicht     |
|15202614 | Bränd-Brekzie | Bränd-Brekzie     |
|15202615 | Infralias-Sandstein | Infralias-Sandstein     |
|15202616 | Nufenen-Zone: phyllitische Trias | Nufenen-Zone: phyllitische Trias     |
|15202617 | Nufenen-Zone: karbonatische Trias | Nufenen-Zone: karbonatische Trias     |
|15202618 | Nufenen-Zone: karbonatische Trias: Kalkmarmor | Nufenen-Zone: karbonatische Trias: Kalkmarmor     |
|15202619 | Nufenen-Zone: karbonatische Trias: Dolomitmarmor | Nufenen-Zone: karbonatische Trias: Dolomitmarmor     |
|15202620 | Nufenen-Zone: karbonatische Trias: Rauwacke | Nufenen-Zone: karbonatische Trias: Rauwacke     |
|15202621 | Nufenen-Zone: quartzitische Trias | Nufenen-Zone: quartzitische Trias     |
|15202622 | Urseren-Garvera-Zone: Malm | Urseren-Garvera-Zone: Malm     |
|15202623 | Urseren-Garvera-Zone: Dogger | Urseren-Garvera-Zone: Dogger     |
|15202624 | Urseren-Garvera-Zone: Lias undiff. | Urseren-Garvera-Zone: Lias undiff.     |
|15202625 | Urseren-Garvera-Zone: Oberer Lias | Urseren-Garvera-Zone: Oberer Lias     |
|15202626 | Urseren-Garvera-Zone: Mittlerer Lias | Urseren-Garvera-Zone: Mittlerer Lias     |
|15202627 | Urseren-Garvera-Zone: Unterer Lias | Urseren-Garvera-Zone: Unterer Lias     |
|15202628 | Urseren-Garvera-Zone: phyllitische Trias | Urseren-Garvera-Zone: phyllitische Trias     |
|15202629 | Urseren-Garvera-Zone: karbonatische Trias | Urseren-Garvera-Zone: karbonatische Trias     |
|15202630 | Urseren-Garvera-Zone: Permokarbon: Psephit- und Psammitgneis | Urseren-Garvera-Zone: Permokarbon: Psephit- und Psammitgneis     |
|15202631 | Urseren-Garvera-Zone: Permokarbon: Metarhyolith | Urseren-Garvera-Zone: Permokarbon: Metarhyolith     |
|15202632 | Urseren-Garvera-Zone: Permokarbon: Chloritschiefer | Urseren-Garvera-Zone: Permokarbon: Chloritschiefer     |
|15202633 | Urseren-Garvera-Zone: Permokarbon: Graphitschiefer | Urseren-Garvera-Zone: Permokarbon: Graphitschiefer     |
|15202634 | Gotthard-Decke: Prävariszischer Orthogneis | Gotthard-Decke: Prävariszischer Orthogneis     |
|15202635 | Gotthard-Decke: Prävariszischer Augengneis | Gotthard-Decke: Prävariszischer Augengneis     |
|15202636 | Gotthard-Decke: Prävariszischer Paragneis | Gotthard-Decke: Prävariszischer Paragneis     |
|15202637 | Camosci-Decke: Paragneis | Camosci-Decke: Paragneis     |
|15202638 | Camosci-Decke: Lias-Dogger | Camosci-Decke: Lias-Dogger     |
|15202639 | Camosci-Decke: Lias-Dogger: Kalkglimmerschiefer | Camosci-Decke: Lias-Dogger: Kalkglimmerschiefer     |
|15202640 | Camosci-Decke: Lias-Dogger: Granatglimmerschiefer | Camosci-Decke: Lias-Dogger: Granatglimmerschiefer     |
|15202641 | Camosci-Decke: Lias | Camosci-Decke: Lias     |
|15202642 | Camosci-Decke: Trias | Camosci-Decke: Trias     |
|15202643 | Camosci-Decke: sandige Trias | Camosci-Decke: sandige Trias     |
|15202644 | Camosci-Decke: karbonatische Trias | Camosci-Decke: karbonatische Trias     |
|15202645 | Urseren-Garvera-Zone: Mesozoikum undiff. | Urseren-Garvera-Zone: Mesozoikum undiff.     |
|15202646 | Urseren-Garvera-Zone: Trias | Urseren-Garvera-Zone: Trias     |
|15202647 | Nufenen-Zone: Trias | Nufenen-Zone: Trias     |
|15202648 | Nufenen-Zone: Lias undiff. | Nufenen-Zone: Lias undiff.     |
|15203001 | Niesen-Flysch | Flysch du Niesen     |
|15203002 | Chesselbach-Formation | Formation du Chesselbach     |
|15203003 | Seron-Formation | Formation de Seron     |
|15203004 | Niesenkulm-Formation | Formation du Niesenkulm     |
|15203005 | Frutigen-Formation | Formation de Frutigen     |
|15203006 | Grande-Eau-Formation | Formation de la Grande Eau     |
|15203007 | Langy-Member | Membre de Langy     |
|15203008 | Forclaz-Member | Membre de la Forclaz     |
|15203009 | Grès de Passage | Membre des Grès de Passage     |
|15203010 | Leyderry-Member | Membre de la Leyderry     |
|15203011 | Raverette-Member | Membre de la Raverette     |
|15203012 | Schistes à Miches | Membre des Schistes à Miches     |
|15203013 | Murgaz-Kalk | Calcaire de Murgaz     |
|15203014 | Trias der Niesen-Decke | Trias de la nappe du Niesen     |
|15203015 | Chlussli-Formation | Formation de Chlussli     |
|15203016 | Coulaytes-Melange | Mélange des Coulaytes     |
|15203017 | Cuvigne-Derrey-Formation | Formation de Cuvigne Derrey     |
|15203018 | Couches-Rouges-Gruppe | Groupe des Couches Rouges     |
|15203019 | Chenaux-Rouges-Formation | Formation des Chenaux Rouges     |
|15203020 | Hochmatt-Kalkarenit | Calcarénite de la Hochmatt     |
|15203021 | Chenaux-Rouges-Mineralkruste | Croûte minéralisée des Chenaux Rouges     |
|15203022 | Forclettes-Formation | Formation des Forclettes     |
|15203023 | Roter-Sattel-Hartgrund | Hartground de Roter Sattel     |
|15203024 | Beaumont-Konglomerat | Conglomérat de Beaumont     |
|15203025 | Rayes-Kalk | Calcaire des Rayes     |
|15203026 | Pissot-Member | Membre du Pissot     |
|15203027 | Rote-Platte-Formation | Formation de Rote Platte     |
|15203028 | Wildenbach-Member | Membre du Wildenbach     |
|15203029 | Pra-du-Pont-Hartgrund | Hardground de Pra du Pont     |
|15203030 | Rontins-Member | Membre des Rontins     |
|15203031 | Allières-Member | Membre d&#39;Allières     |
|15203032 | Gérignoz-Kalk | Calcaire de Gérignoz     |
|15203033 | Plagersflue-Kalkarenit | Calcarénite de la Plagersflue     |
|15203034 | Intyamon-Formation | Formation de l&#39;Intyamon     |
|15203035 | Chällihorn-Member | Membre du Chällihorn     |
|15203036 | Comba-d&#39;Avau-Member | Membre de la Comba d&#39;Avau     |
|15203037 | Rodosex-Member | Membre de Rodosex     |
|15203038 | Sciernes-d&#39;Albeuve-Formation | Formation des Sciernes d&#39;Albeuve     |
|15203039 | Moléson-Formation | Formation du Moléson     |
|15203040 | Torrent-de-Lessoc-Formation | Formation du Torrent de Lessoc     |
|15203041 | Staldengraben-Formation | Formation du Staldengraben     |
|15203042 | Col-de-Lys-Member | Membre du Col de Lys     |
|15203043 | Vanil-Carré-Member | Membre du Vanil Carré     |
|15203044 | Verdy-Member | Membre du Verdy     |
|15203045 | Soladier-Member | Membre de Soladier     |
|15203046 | Sommant-Formation | Formation de Sommant     |
|15203047 | Rossinière-Formation | Formation de Rossinière     |
|15203048 | Heiti-Formation | Formation de Heiti     |
|15203049 | Combe-du-Pissot-Formation | Formation de la Combe du Pissot     |
|15203050 | Chevalets-Member | Membre des Chevalets     |
|15203051 | Creux-de-l&#39;Ours-Member | Membre du Creux-de-l&#39;Ours     |
|15203052 | Petit-Liençon-Formation | Formation du Petit Liençon     |
|15203053 | Arvel-Formation | Formation d&#39;Arvel     |
|15203054 | Grande-Bonavau-Formation | Formation de la Grande Bonavau     |
|15203055 | Chauderon-Formation | Formation du Chauderon     |
|15203056 | Vudalla-Formation | Formation de la Vudalla     |
|15203057 | Bois-de-Luan-Member | Membre du Bois de Luan     |
|15203058 | Agreblierai-Member | Membre d&#39;Agreblierai     |
|15203059 | Col-de-Tompey-Formation | Formation du Col de Tompey     |
|15203060 | Plan-Falcon-Formation | Formation de Plan Falcon     |
|15203061 | Dolomies Blondes | Dolomies Blondes     |
|15203062 | Clôt-la-Cime-Formation | Formation de Clôt la Cime     |
|15203063 | Neokom | Neokom     |
|15203064 | Malmkalk | Malmkalk     |
|15203065 | Knollenargovien | Knollenargovien     |
|15203066 | Griggeli-Formation | Formation du Griggeli     |
|15203067 | Mythen-Kieselkalk | Calcaire siliceux des Mythen     |
|15203068 | Griggeli-Bank | Banc du Griggeli     |
|15203069 | Gibel-Formation | Formation de Gibel     |
|15203070 | Rämsi-Member | Membre de Rämsi     |
|15203071 | Gibel-Member | Membre de Gibel     |
|15203072 | Steinberg-Konglomerat | Conglomérat du Steinberg     |
|15203073 | Musenalp-Member | Membre de la Musenalp     |
|15203074 | Stanserhorn-Formation | Formation du Stanserhorn     |
|15203075 | Zoophycos-Schichten | Couches à Zoophycos (Fm. du Stanserhorn)     |
|15203076 | Spis-Kalk | Calcaire de la Spis     |
|15203077 | «Posidonienschiefer» (der Stanserhorn-Fm.) | Schistes à Posidonies (Fm. du Stanserhorn)     |
|15203078 | Obflue-Formation | Formation de la Obflue     |
|15203079 | Brand-Formation | Formation de Brand     |
|15203080 | Horngraben-Formation | Formation du Horngraben     |
|15203081 | Lückengraben-Formation | Formation du Lückengraben     |
|15203082 | Dorfflüe-Formation | Formation de la Dorfflüe     |
|15203083 | Gummfluh-Mikrofazies | Microfaciès de la Gummfluh     |
|15203084 | Pfad-Mikrofazies | Microfaciès de Pfad     |
|15203085 | Rindenkorn-Mikrofazies | Microfaciès à oncolithes (Fm. de la Dorfflüe)     |
|15203086 | Gastlosen-Oolith | Oolite des Gastlosen     |
|15203087 | Wandfluh-Mikrofazies | Microfaciès de la Wandfluh     |
|15203088 | Mytilus-Schichten | Couches à Mytilus     |
|15203089 | Col-de-Cordon-Member | Membre du Col de Cordon     |
|15203090 | Klus-Konglomerat | Conglomérat de la Klus     |
|15203091 | Holzerhorn-Einheit | Unité du Holzerhorn     |
|15203092 | Rubli-Member | Membre du Rubli     |
|15203093 | Chavanette-Member | Membre de Chavanette     |
|15203094 | Erpilles-Member | Membre des Erpilles     |
|15203095 | Wiriehorn-Formation | Formation du Wiriehorn     |
|15203096 | St-Triphon-Formation | Formation de St-Triphon     |
|15203097 | Andonces-Member | Membre des Andonces     |
|15203098 | Lessus-Member | Membre du Lessus     |
|15203099 | Dorchaux-Member | Membre de Dorchaux     |
|15203100 | Mattes-Melange | Mélange des Mattes     |
|15203101 | Chumi-Formation | Formation de la Chumi     |
|15203102 | Joux-Verte-Formation | Formation de la Joux Verte     |
|15203103 | Bonave-Formation | Formation de Bonave     |
|15203104 | Obere Brekzie | Brèche Supérieure     |
|15203105 | Obere Schiefer (Schistes Ardoisiers) | Schistes Ardoisiers     |
|15203106 | Untere Brekzie | Brèche Inférieure     |
|15203107 | Untere Schiefer | Schistes Inférieurs     |
|15203108 | Untere Kalke | Calcaires Inférieurs     |
|15203109 | Trias der Brekzien-Decke | Trias de la nappe de la Brèche     |
|15203110 | Gurnigel-Flysch | Flysch du Gurnigel     |
|15203111 | Flysch 4 mit siltigen Turbiditen | Flysch 4 à turbidites silteuses     |
|15203112 | Flysch 3b mit bioklastischen Turbiditen | Flysch 3b à turbidites bioclastiques     |
|15203113 | Flysch 3a mergelig-sandig | Flysch 3a marno-gréseux     |
|15203114 | Flysch 2b mit sandigen Turbiditen | Flysch 2b à turbidites siliceuses     |
|15203115 | Flysch 2a tonig-sandig | Flysch 2a argilo-gréseux     |
|15203116 | Hellstätt-Formation | Formation de Hellstätt     |
|15203117 | Schlieren-Flysch | Flysch des Schlieren     |
|15203118 | Schlieren-Sandstein | Grès des Schlieren     |
|15203119 | Schoni-Sandstein | Grès de la Schoni     |
|15203120 | Obere Tonsteinschichten | Obere Tonsteinschichten (Flysch des Schlieren)     |
|15203121 | Guber-Sandstein | Grès de Guber     |
|15203122 | Untere Tonsteinschichten | Untere Tonsteinschichten (Flysch des Schlieren)     |
|15203123 | Basaler Schlieren-Flysch | Flysch basal des Schlieren     |
|15203124 | Estavannens-Flysch | Flysch d&#39;Estavannens     |
|15203125 | Reidigen-Formation | Formation de Reidigen     |
|15203126 | Biot-Formation | Formation du Biot     |
|15203127 | Chétillon-Formation | Formation de Chétillon     |
|15203128 | Rodomonts-Formation | Formation des Rodomonts     |
|15203129 | Mocausa-Nagelfluh | Poudingue de la Mocausa     |
|15203130 | Tissota-Melange | Mélange de la Tissota     |
|15203131 | Gueyraz-Komplex | Complexe de la Gueyraz     |
|15203132 | Weissenburg-Flysch | Flysch de la Weissenburg     |
|15203133 | Manche-Formation | Formation de la Manche     |
|15203134 | Fouyet-Formation | Formation du Fouyet     |
|15203135 | Foraminiferenschichten | Couches à foraminifères     |
|15203136 | Aptychenkalk | Calcaires à Aptychus     |
|15203137 | Radiolarit | Radiolarites     |
|15203138 | Filamentkalk | Calcaires à filaments     |
|15203139 | Spatkalk (Tissota-Melange) | Calcaires spathiques     |
|15203140 | Hundsrügg-Formation | Formation du Hundsrügg     |
|15203141 | Perrières-Formation | Formation des Perrières     |
|15203142 | Rhenodanubischer Flysch | Flysch Rhénodanubien     |
|15203143 | Vorarlberg-Flysch | Flysch du Vorarlberg     |
|15203144 | Fanola-Formation | Formation de Fanola     |
|15203145 | Planknerbrücke-Formation | Formation de Planknerbrücke     |
|15203146 | Planken-Formation | Formation de Planken     |
|15203147 | Reiselsberg-Formation | Formation du Reiselsberg     |
|15203148 | Basisserie | Série basale (Fm. du Reiselsberg)     |
|15203149 | Liechtenstein-Flysch | Flysch du Liechtenstein     |
|15203150 | Triesen-Formation | Flysch de Triesen     |
|15203151 | Vaduz-Flysch | Flysch de Vaduz     |
|15203152 | Eichholztobel-Formation | Formation de l&#39;Eichholztobel     |
|15203153 | Schloss-Formation | Formation de Schloss     |
|15203154 | Gaschlo-Formation | Formation de Gaschlo     |
|15203155 | Leimern-Kalk | Calcaire de la Leimern     |
|15203156 | Pierre-Avoi-Melange | Mélange de la Pierre Avoi     |
|15203157 | St-Christophe-Schichten | Formation de St-Christophe     |
|15203158 | Marmontains-Schichten | Formation des Marmontains     |
|15203159 | Aroley-Schichten | Formation de l&#39;Aroley     |
|15203160 | Peula-Schichten | Couches de la Peula     |
|15203161 | Versoyen-Schichten | Couches du Versoyen     |
|15203162 | Prättigau-Schiefer | Schistes du Prättigau     |
|15203163 | Ruchberg-Formation | Formation du Ruchberg     |
|15203164 | Oberälpli-Formation | Formation de l&#39;Oberälpli     |
|15203165 | Eggberg-Formation | Formation de l&#39;Eggberg     |
|15203166 | Gyrenspitz-Formation | Formation du Gyrenspitz     |
|15203167 | Fadura-Formation | Formation de la Fadura     |
|15203168 | Pfävigrat-Formation | Formation du Pfävigrat     |
|15203169 | Sassauna-Formation | Formation de la Sassauna     |
|15203170 | Valzeina-Formation | Formation de Valzeina     |
|15203171 | Klus-Formation | Formation de la Klus     |
|15203172 | Stätzerhorn-Gruppe | Flysch du Tomül     |
|15203173 | Basiskonglomerat der Stätzerhorn-Gruppe | Hauptkonglomerat (Flysch du Tomül)     |
|15203174 | Carnusa-Formation | Formation du Carnusa(horn)     |
|15203175 | Safien-Kalk | Calcaire de Safien     |
|15203176 | Nolla-Kalkschiefer | Calcaire de la Nolla     |
|15203177 | Nolla-Tonschiefer | Argillite de la Nolla     |
|15203178 | Bärenhorn-Formation | Formation du Bärenhorn     |
|15203179 | Grüngesteine der Grava- und Tomül-Decke | Roches vertes (Grava/Tomül)     |
|15203180 | Tomül-Mélange | Mélange du Tomül     |
|15203181 | Série du Tounô | Série du Tounô     |
|15203182 | Barrhorn-Serie | Série du Barrhorn     |
|15203183 | Bruneggjoch-Formation | Formation du Bruneggjoch     |
|15203184 | Sous-le-Rocher-Member | Membre de Sous le Rocher     |
|15203185 | Randa-Augengneis | Gneiss oeillé de Randa     |
|15203186 | Col-de-Chassoure-Formation | Formation du Col de Chassoure     |
|15203187 | Gouille-Verte-Member | Membre de la Gouille Verte     |
|15203188 | Matse-Member | Membre de la Matse     |
|15203189 | Dent-de-Nendaz-Member | Membre de la Dent de Nendaz     |
|15203190 | Goli-d&#39;Aget-Member | Membre du Goli d&#39;Aget     |
|15203191 | Mondra-Member | Membre de la Mondra     |
|15203192 | Cleuson-Member | Membre de Cleuson     |
|15203193 | Métailler-Formation | Formation du Métailler     |
|15203194 | Distulberg-Formation | Formation du Distulberg     |
|15203195 | Thyon-Metagranophyr | Métagranophyre de Thyon     |
|15203196 | Mont-Rogneux-Metagranit | Métagranite du Mont Rogneux     |
|15203197 | Lirec-Formation | Formation de Lirec     |
|15203198 | Adlerflüe-Formation | Formation de l&#39;Adlerflüe     |
|15203199 | Ergischhorn-Komplex | Complexe de l&#39;Ergischhorn     |
|15203200 | Gelbhorn-Flysch | Flysch du Gelbhorn     |
|15203201 | Obrist-Gruppe | Groupe de l&#39;Obrist     |
|15203202 | Vizan-Brekzie | Brèche du Vizan     |
|15203203 | Tschera-Marmor | Marbre de la Tschera     |
|15203204 | Wissberg-Brekzie | Brèche du Wissberg     |
|15203205 | Nisellas-Gruppe | Groupe de Nisellas     |
|15203206 | Tumpriv-Gruppe | Groupe de la Tumpriv     |
|15203207 | Kalkberg-Gruppe | Groupe du Kalkberg     |
|15203208 | Bavugls-Gruppe | Groupe de Bavugls     |
|15203209 | Nolla-Kristallin | Socle cristallin du Nolla     |
|15203210 | Falknis-Flysch | Flysch de la nappe du Falknis     |
|15203211 | Globorotalien-Schichten | Globorotalien-Schichten     |
|15203212 | Quarzsandstein-Flysch (Gault) | Quarzsandstein-Flysch (Gault)     |
|15203213 | Tristel-Formation | Formation de Tristel     |
|15203214 | Fleckenkalk-Flysch (Neokom) | Fleckenkalk-Flysch (Neokom)     |
|15203215 | Jes-Formation | Formation de la Jes     |
|15203216 | Falknis-Brekzie | Brèche du Falknis     |
|15203217 | Sanalada-Formation | Formation de Sanalada     |
|15203218 | Panier-Formation | Formation de Panier     |
|15203219 | Sulzfluh-Flysch | Flysch de la nappe de la Suzfluh     |
|15203220 | Sulzfluh-Kalk | Calcaire de la Sulzfluh     |
|15203221 | Sulzfluh-Granit | Granite de la nappe de la Suzfluh     |
|15203222 | Tasna-Flysch | Flysch de la nappe de la Tasna     |
|15203223 | Steinsberg-Kalk | Calcaire du Steinsberg     |
|15203224 | Plattamala-Granit | Granite de la nappe de la Tasna     |
|15203225 | Série Rousse | Série Rousse     |
|15203226 | Série Grise | Série Grise     |
|15203227 | Garde-de-Bordon-Formation | Série de la Garde de Bordon     |
|15203228 | Fêta-d&#39;Août-Formation | Flysch de la Fêta d&#39;Août     |
|15203229 | Allalin-Gabbro | Gabbro de l&#39;Allalin     |
|15203230 | Arosa-Mélange | Mélange d&#39;Arosa     |
|15203231 | Verspala-Formation | Formation de la Verspala     |
|15203232 | Lavagna-Formation | Formation de Lavagna     |
|15203233 | Palombini-Formation | Formation à Palombini     |
|15203234 | Calpionellenkalk der Arosa-Zone | Calcaire à Calpionelles de la zone d&#39;Arosa     |
|15203235 | Radiolarit der Arosa-Zone | Radiolarite de la zone d&#39;Arosa     |
|15203236 | Ophiolith der Arosa-Zone | Ophiolite de la zone d&#39;Arosa     |
|15203238 | Buufal-Konglomerat | Conglomérat de Buufal     |
|15203239 | Langel-Member | Membre de Langel     |
|15203240 | Obere Rauwacke der Klippen-Decke | Cornieule Supérieure     |
|15203241 | Gips der Klippen-Decke | Gypse de la nappe des Préalpes Médianes     |
|15203242 | Couches-Rouges der Brekzien-Decke | Couches Rouges de la nappe de la Brèche     |
|15203243 | Rauwacke der Brekzien-Decke | Cornieule de la nappe de la Brèche     |
|15203244 | Lamperehubel-Sandstein | Grès du Lamperehubel     |
|15203245 | Gets-Ophiolith | Ophiolite des Gets     |
|15203246 | Obere Kalk- und Tonschiefer der Zone Piz Terri - Lunschania | Obere Kalk- und Tonschiefer (Grava/Tomül)     |
|15203247 | Gneisquarzit der Zone Piz Terri - Lunschania | Quarzit und quarzitische Schiefer (Grava/Tomül)     |
|15203248 | Untere Kalk- und Tonschiefer der Zone Piz Terri - Lunschania | Untere Kalk- und Tonschiefer (Grava/Tomül)     |
|15203249 | Aul-Marmor | Marbre du Piz Aul     |
|15203250 | Dolomitbrekzie (Terri) | Brèche (Grava/Tomül)     |
|15203251 | Lias-Kalk (Grava) | Gryphäenkalk     |
|15203252 | Nordpenninische Trias | Trias nord-pennique     |
|15203253 | Zervreila-Granitgneis | Orthogneiss de Zervreila     |
|15203254 | Garenstock-Augengneis | Gneiss oeillé du Garenstock     |
|15203255 | Adula-D.: Glimmerschiefer und Paragneis | Adula-D.: Glimmerschiefer und Paragneis     |
|15203256 | Adula-D.: Amphibolit | Adula-D.: Amphibolit     |
|15203257 | Submédiane-Melange | Mélange Submédian     |
|15203258 | Truche-Brekzie | Brèche de la Truche     |
|15203259 | Trom-Brekzie | Brèche de Trom     |
|15203260 | Exergillod-Brekzie | Brèche d&#39;Exergillod     |
|15203261 | Troublon-Kalk | Calcaire du Troublon     |
|15203262 | Zünegg-Knollenkalk | Calcaire noduleux de la Zünegg     |
|15203263 | Hauta-Crêtaz-Formation | Formation de Hauta-Crêtaz     |
|15203264 | Pointe-de-l&#39;Au-Brekzie | Brèche de la Pointe de l&#39;Au     |
|15203265 | Bonaveau-Kalk | Calcaire de Bonaveau     |
|15203266 | Sex-du-Tronc-Kalk | Calcaire du Sex du Tronc     |
|15203267 | Grand-Herba-Kalk | Calcaire du Sex de Grand-Herba     |
|15203268 | Oudiou-Formation | Formation d&#39;Oudiou     |
|15203269 | Malm der Klippen-Decke | Malm de la nappe des Préalpes Médianes     |
|15203270 | Albeuve-Serie | Série d&#39;Albeuve     |
|15203271 | Kummli-Schichten | Couches de la Kummli     |
|15203272 | Dogger der Klippen-Decke | Dogger de la nappe des Préalpes Médianes     |
|15203273 | Stockenflue-Kalk | Calcaire de la Stockenflue     |
|15203274 | Mieussy-Member | Membre de Mieussy     |
|15203275 | Lias der Klippen-Decke | Lias de la nappe des Préalpes Médianes     |
|15203276 | Trias der Klippen-Decke | Trias de la nappe des Préalpes Médianes     |
|15203277 | Pralet-Formation | Formation du Pralet     |
|15203278 | Balmi-Member | Membre du Balmi     |
|15203279 | Bodeflue-Member | Membre de la Bodeflue     |
|15203280 | Wildgrimmi-Member | Membre du Wildgrimmi     |
|15203281 | Untere Rauwacke der Klippen-Decke | Cornieule Inférieure     |
|15203282 | Infrabrèche-Melange | Mélange infra-brèche     |
|15203283 | Wägital-Flysch | Flysch du Wägital     |
|15203284 | Flysch 5, mit kieseligen Mikrokonglomeraten | Flysch 5 à microconglomérats siliceux     |
|15203285 | Voirons-Flysch | Flysch des Voirons     |
|15203286 | Boëge-Mergel | Marne de Boëge     |
|15203287 | Vouan-Konglomerat | Conglomérat du Vouan     |
|15203288 | Voirons-Sandstein | Grès des Voirons     |
|15203289 | Praz-Serie | Série des Praz     |
|15203290 | Coicon-Serie | Série de Coicon     |
|15203291 | Couches-Rouges der Klippen-Decke, undifferenziert | Couches Rouges de la nappe des Préalpes Médianes, indifférenciées     |
|15203292 | Simmen-Flysch, undifferenziert | Flysch de la Simme, indifférencié     |
|15203293 | Trepsen-Flysch | Flysch de Trepsen     |
|15203294 | Cocco-Gneis | Cocco-Gneis     |
|15203295 | Verzasca-Gneis | Verzasca-Gneis     |
|15203296 | Vogorno-Gneis | Vogorno-Gneis     |
|15203297 | Ruscada-Gneis | Ruscada-Gneis     |
|15203298 | Mergoscia-Gneis | Mergoscia-Gneis     |
|15203299 | Monte-Rosa-Gneis | Monte-Rosa-Gneis     |
|15203300 | «Arblatsch-Flysch» | «Arblatsch-Flysch»     |
|15203301 | Arblatsch-Sandstein | Arblatsch-Sandstein     |
|15203302 | «Arblatsch-Konglomerat» | «Arblatsch-Konglomerat»     |
|15203303 | Spegnas-Formation | Spegnas-Formation     |
|15203304 | Rudnal-Formation | Rudnal-Formation     |
|15203305 | Savognin-Formation | Savognin-Formation     |
|15203306 | Bleis-Pintgas-Formation | Bleis-Pintgas-Formation     |
|15203307 | Parnegl-Formation | Parnegl-Formation     |
|15203308 | Danis-Formation | Danis-Formation     |
|15203309 | Raschil-Formation | Raschil-Formation     |
|15203310 | Embd-Member | Embd-Member     |
|15203311 | Bonigersee-Augengneis | Bonigersee-Augengneis     |
|15203312 | Törbel-Gneis | Törbel-Gneis     |
|15203313 | Lodano-Gneis | Lodano-Gneis     |
|15203314 | Vergeletto-Gneis | Vergeletto-Gneis     |
|15203315 | Cortascia-Gneis | Cortascia-Gneis     |
|15203316 | Forcoletta-Gneis | Forcoletta-Gneis     |
|15203317 | Matorello-Gneis | Matorello-Gneis     |
|15203318 | Lebendun-Gneiskomplex | Complexe gneissique du Lebendun     |
|15203319 | Sabbione-Sandstein | Sabbione-Sandstein     |
|15203320 | Kristallin der Monte-Leone-Decke | Socle cristallin de la nappe du Monte Leone     |
|15203321 | Ganter-Gneis | Ganter-Gneis     |
|15203322 | Ritter-Gneis | Ritter-Gneis     |
|15203323 | Geisspfad-Serpentinit | Geisspfad-Serpentinit     |
|15203324 | Holzerspitz-Gruppe | Holzerspitz-Gruppe     |
|15203325 | Holzerspitz-Kalkschiefer | Calcschistes de l&#39;Holzerspitz     |
|15203326 | Fäldbach-Gruppe | Fäldbach-Gruppe     |
|15203327 | Rinderbach-Formation | Rinderbach-Formation     |
|15203328 | Langenegg-Formation | Langenegg-Formation     |
|15203329 | Rombach-Formation | Rombach-Formation     |
|15203330 | Roffna-Gneis | Roffna-Gneis     |
|15203331 | «Roffna-Porphyr» | «Roffna-Porphyr»     |
|15203332 | Burgruinen-Gneis | Burgruinen-Gneis     |
|15203333 | Taspegn-Gneis | Taspegn-Gneis     |
|15203334 | Aigremont-Brekzie | Aigremont-Brekzie     |
|15203335 | Sulzgrabe-Formation | Sulzgrabe-Formation     |
|15203336 | Rhät der Brekzien-Decke | Rhät der Brekzien-Decke     |
|15203337 | Siderolithisches Dogger der Klippen-Decke | Siderolithisches Dogger der Klippen-Decke     |
|15203338 | «Silex-Niveau» (St-Triphon-Fm.) | «Silex-Niveau» (St-Triphon-Fm.)     |
|15203339 | «Mittlere Rauwacke» (St-Triphon-Fm.) | «Mittlere Rauwacke» (St-Triphon-Fm.)     |
|15203340 | Timun-Komplex | Timun-Komplex     |
|15203341 | Malenco-Serpentinit | Malenco-Serpentinit     |
|15203342 | Forno-Amphibolit | Forno-Amphibolit     |
|15203343 | Muretto-Quarzit | Muretto-Quarzit     |
|15203344 | Colerin-Konglomerat | Colerin-Konglomerat     |
|15203345 | Pierre-Avoi-Brekzie | Pierre-Avoi-Brekzie     |
|15203346 | Dréveneuse-Bauxit | Dréveneuse-Bauxit     |
|15203347 | Bruneggjoch-Metabauxit | Bruneggjoch-Metabauxit     |
|15203348 | Karbon der Zone-Houillère | Carbonifère de la Zone Houillère     |
|15203349 | Terri-Schiefer | Schistes du (Piz) Terri     |
|15203350 | Robiei-Wildflysch | Wildflysch de Robièi     |
|15203351 | Pizzo-Castello-Wildflysch | Wildflysch du Pizzo Castello     |
|15203352 | Tamier-Zött-Wildflysch | Wildflysch de Tamier-Zött     |
|15203353 | Alpe-Tamia-Campo-Wildflysch | Wildflysch de l&#39;Alpe Tamia-Campo     |
|15203354 | Teggiolo-Kalkschiefer | Calcschistes du Teggiolo     |
|15203355 | Medola-Quarzit | Quartzite du Mèdola     |
|15203356 | Pianasciom-Kalkschiefer | Calcschiste de Pianasciom     |
|15203357 | Piano-delle-Creste-Sandstein | Grès du Piano delle Creste     |
|15203358 | Antabia-Gruppe | Groupe d&#39;Antabia     |
|15203359 | Vanis-Formation | Formation des Vanis     |
|15203360 | Sevinera-Marmor | Marbre de Sevinèra     |
|15203361 | Sevinera-Sandstein | Grès de Sevinèra     |
|15203362 | Ri-d&#39;Antabia-Konglomerat | Conglomérat du Ri d&#39;Antabia     |
|15203363 | Scisti bruni (Lebendun) | Scisti bruni (Lebendun)     |
|15203364 | Gneiss basale (Lebendun) | Gneiss basale (Lebendun)     |
|15203365 | Antigorio-Orthogneis | Orthogneiss d&#39;Antigorio     |
|15203366 | Couches-Rouges (Falknis, Sulzfluh, Tasna) | Couches-Rouges (Falknis, Sulzfluh, Tasna)     |
|15203367 | Lagensandkalk | Lagensandkalk     |
|15203368 | Série schisto-quartzitique (Pierre Avoi) | Série schisto-quartzitique (Pierre Avoi)     |
|15203369 | Série conglomératique (Pierre Avoi) | Série conglomératique (Pierre Avoi)     |
|15203370 | Südegg-Komplex | Compexe de Südegg     |
|15203371 | Punta-Rossa-Komplex | Complexe de la Punta Rossa     |
|15203372 | Ferret-Schiefer | Schistes de Ferret     |
|15203373 | Terri-Schiefer_Basale | Schistes basaux du (Piz) Terri     |
|15203374 | Lugnez-Schiefer | Schistes du Val Lumnezia     |
|15203375 | Sosto-Schiefer | Schistes du Sosto     |
|15203376 | Konglomeratgneis (Terri) | Konglomeratgneis (Terri)     |
|15203377 | Garzott-Brekzie | Brèche de Garzott     |
|15203378 | Areua-Bruschghorn-Melange | Mélange d&#39;Areua-Bruschghorn     |
|15203379 | Albitquarzit der Grava- und Tomül-Decke | Albitquarzit (Grava)     |
|15203380 | Basale Tonschiefer der Grava- und Tomül-Decke | Basale Tonschiefer (Grava)     |
|15203381 | Phengitgneis der Aul-Decke | Phengitgneis (Grava)     |
|15203382 | Haute-Pointe-Formation | Formation de la Haute Pointe     |
|15203383 | Brasses-Formation | Formation des Brasses     |
|15203385 | Macugnaga-Augengneis | Gneiss oeillé de Macugnaga     |
|15203386 | Perm der Zone-Houillère | Permien de la Zone Houillère     |
|15203387 | Perm der Zone-Houillère, quarzschiefrig | Permien quarzoschisteux de la Zone Houillère     |
|15203388 | Ricard-Rhyolit | Rhyolite de Ricard     |
|15203389 | Perm der Zone-Houillère, konglomeratisch | Permien conglomératique de la Zone Houillère     |
|15203390 | Série schisto-gréseuse supérieure | Série schisto-gréseuse supérieure     |
|15203391 | Série schisteuse moyenne | Série schisteuse moyenne     |
|15203392 | Chandoline-Sandstein | Grès de Chandoline     |
|15203393 | Gälmji-Gneiss | Gneiss de Gälmji     |
|15203394 | Scherbadung-Gabbro | Gabbro du Scherbadung     |
|15203395 | Lacerandes-Augengneis | Gneiss oeillé des Lacerandes     |
|15203396 | Mont-Mort-Metapelit | Métapélites du Mont Mort     |
|15203397 | Schistes noirs (Pierre Avoi) | Schistes noirs (Pierre Avoi)     |
|15203398 | La-Dotse-Albitkalk | Calcaire albitisé de la Dotse     |
|15203399 | Ginals-Gneis | Gneiss de Ginals     |
|15203400 | Kristallin der Berisal-Decke | Socle cristallin de la nappe de Berisal     |
|15203401 | Augengneis der Berisal-Decke | Gneiss oeillé de la nappe de Berisal     |
|15203402 | Kristallin der Ruitor-Decke | Socle cristallin de la nappe du Ruitor     |
|15203403 | Corno-Gneis | Gneiss du Corno     |
|15203404 | Quarzit der Nordpenninische Trias | Quartzite du Trias nord-pennique     |
|15203405 | Kristallin des Briançonnais | Socle cristallin du Briançonnais     |
|15203406 | Permo-Karbon der Ruitor-Decke | Permo-Carbonifère de la nappe du Ruitor     |
|15203407 | Permo-Karbon der Ruitor-Decke, konglomeratisch | Permo-Carbonifère conglomératique de la nappe du Ruitor     |
|15203408 | Piémont-Glanzschiefer | Schistes lustrés du Piémontais     |
|15203409 | Metasedimente der Tsaté-Decke | Métasédiments de la nappe du Tsaté     |
|15203410 | Marmor der Tsaté-Decke | Marbre de la nappe du Tsaté     |
|15203411 | Metaradiolarit der Tsaté-Decke | Métaradiolarite de la nappe du Tsaté     |
|15203412 | Metasedimente der Zermatt-Saas-Decke | Métasédiments de la nappe de Zermatt-Saas     |
|15203413 | Piémont-Ophiolith | Ophiolite du Piémontais     |
|15203414 | Ophiolith der Tsaté-Decke | Ophiolite de la nappe du Tsaté     |
|15203415 | Mont-des-Ritzes-Metabasalt | Métabasalte du Mont des Ritzes     |
|15203416 | Aiguilles-Rouges-d&#39;Arolla-Metagabbro | Métagabbro des Aiguilles Rouges d&#39;Arolla     |
|15203417 | Torrembey-Brekzie | Brèche de Torrembey     |
|15203418 | Marmor der Zermatt-Saas-Decke | Marbre de la nappe de Zermatt-Saas     |
|15203419 | Quarzit der Zermatt-Saas-Decke | Quartzite de la nappe de Zermatt-Saas     |
|15203420 | Riffelberg-Melange | Mélange du Riffelberg     |
|15203421 | Glanzschiefer der Zermatt-Saas-Decke | Schistes lustrés de la nappe de Zermatt-Saas     |
|15203422 | Ophiolith der Zermatt-Saas-Decke | Ophiolite de la nappe de Zermatt-Saas     |
|15203423 | Pfulwe-Metabasalt | Métabasalte du Pfulwe     |
|15203424 | Ophiolith der Antrona-Decke | Ophiolite de la nappe d&#39;Antrona     |
|15203425 | Böshorn-Gneis | Gneiss du Böshorn     |
|15203426 | Orthogneis der Monte-Leone-Decke | Orthogneiss de la nappe du Monte Leone     |
|15203427 | Leukogneis der Monte-Leone-Decke | Leucogneiss de la nappe du Monte Leone     |
|15203428 | Hyperaugengneis der Monte-Leone-Decke | Hyperaugengneiss de la nappe du Monte Leone     |
|15203429 | Paragneis der Monte-Leone-Decke | Paragneiss de la nappe du Monte Leone     |
|15203430 | Lebendun-Gneis, arkosisch | Gneiss du Lebendun, arkosique     |
|15203431 | Lebendun-Gneis, konglomeratisch | Gneiss du Lebendun, conglomératique     |
|15203432 | Salarioli-Serie | Série du (Passo) Salarioli     |
|15203433 | Kristallin der Ruginenta-Decke | Socle cristallin de la nappe de Ruginenta     |
|15203434 | Schiefer der Ruginenta-Decke | Schistes de la nappe de Ruginenta     |
|15203435 | Paragneis der Ruginenta-Decke | Paragneiss de la nappe de Ruginenta     |
|15203436 | Preja-Formation | Formation de la Preja     |
|15203437 | Cavalli-Formation | Formation des Cavalli     |
|15203438 | Furgg-Serie | Série de Furgg     |
|15203439 | Mezzalama-Granit | Granite de Mezzalama     |
|15203440 | Monte-Rosa-Orthogneis, grobkörnig | Orthogneiss du Mont Rose, à grain grossier     |
|15203441 | Rottal-Migmatit | Migmatite du Rottal     |
|15203442 | Monte-Rosa-Orthogneis, mylonitisch | Orthogneiss du Mont Rose, mylonitique     |
|15203443 | Paragneis der Monte-Rosa-Decke | Paragneiss de la nappe du Mont Rose     |
|15203444 | Biotitgneis der Monte-Rosa-Decke | Gneiss à biotite de la nappe du Mont Rose     |
|15203445 | Bändergneis der Monte-Rosa-Decke | Gneiss rubané de la nappe du Mont Rose     |
|15203446 | Glimmerschiefer der Monte-Rosa-Decke | Micaschiste de la nappe du Mont Rose     |
|15203447 | Grundberg-Serie | Série du Grundberg     |
|15203448 | Kristallin der Portjengrat-Decke | Socle cristallin de la nappe du Protjengrat     |
|15203449 | Orthogneis der Portjengrat-Decke | Orthogneiss de la nappe du Protjengrat     |
|15203450 | Saas-Fee-Augengneis | Gneiss oeillé de Saas Fee     |
|15203451 | Almagelhorn-Migmatit | Migmatite de l&#39;Almagelhorn     |
|15203452 | Weissmies-Paragneis | Paragneiss du Weissmies     |
|15203453 | Monte-Rosa-Orthogneis, mittelkörnig | Orthogneiss du Mont Rose, à grain moyen     |
|15203454 | Stellihorn-Mylonit | Mylonite du Stellihorn     |
|15203455 | Kalkschiefer der Fäldbach-Serie | Calcschistes de la Série du Fäldbach     |
|15203456 | Nordpenninischer Dogger | Dogger nord-pennique     |
|15203457 | Nordpenninischer Lias | Lias nord-pennique     |
|15203458 | Dolomit der Nordpenninische Trias | Dolomie du Trias nord-pennique     |
|15203459 | Valgrande-Paragneis | Paragneiss de Vagrande     |
|15203460 | Variszische Intrusiva des Briançonnais | Roches intrusives varisques du Briançonnais     |
|15203461 | Prävariszisches Grundgebirge des Briançonnais | Socle cristallin anté-varisque du Briançonnais     |
|15203462 | Moncucco-Peridotit | Péridotite du Moncucco     |
|15203463 | Albitaugenschiefer (SOPA) der Adlerflüe-Formation | Schistes oeillés à porphyroblastes d&#39;albite (SOPA) de la Formation de l&#39;Adlerflüe     |
|15203464 | Bänderamphibolit der Adlerflüe-Formation | Amphibolite rubanée de la Formation de l&#39;Adlerflüe     |
|15203465 | Minugrat-Eklogit | Éclogite du Minugrat     |
|15203466 | Ergischhorn-Komplex: Amphibolit | Amphibolite du Complexe gneissique de l&#39;Ergischhorn     |
|15203467 | Grüngesteine der Distulberg-Formation | Roches vertes de la Formation du Distulberg     |
|15203468 | Prasinit der Métailler-Formation | Prasinites de la Formation du Métailler     |
|15203469 | Ultramafit der Métailler-Formation | Roches ultramafiques de la Formation du Métailler     |
|15203470 | Oberems-Albitgneis | Gneiss albitique d&#39;Oberems     |
|15203471 | Permo-Karbon der Maggia-Decke | Permo-Carbonifère de la nappe de la Maggia     |
|15203472 | Perm der Maggia-Decke | Permien de la nappe de la Maggia     |
|15203473 | Karbon der Maggia-Decke | Carbonifère de la nappe de la Maggia     |
|15203474 | Variszische Intrusiva der Maggia-Decke | Roches intrusives varisques de la nappe de la Maggia     |
|15203475 | Prävariszisches Grundgebirge der Maggia-Decke | Socle cristallin anté-varisque de la nappe de la Maggia     |
|15203476 | Maggia-D.: Paragneis | Maggia-D.: Paragneis     |
|15203477 | Bändergneis der Maggia-Decke | Gneiss rubané de la nappe de la Maggia     |
|15203478 | Augengneis der Maggia-Decke | Gneiss oeillé de la nappe de la Maggia     |
|15203479 | Alpigia-Gneis | Gneiss d&#39;Alpigia     |
|15203480 | Gresso-Someo-Zone | zone de Gresso-Someo     |
|15203481 | Pertusio-Zone | zone de Pertusio     |
|15203482 | Passo-di-Cristallina-Zone | zone du Passo di Cristallina     |
|15203483 | Lago-Scuro-Formation | Formation du Lago Scuro     |
|15203484 | Val-Sabbia-Formation | Formation du Val Sabbia     |
|15203485 | Massari-Formation | Formation du (Pizzo) Massari     |
|15203486 | Naret-Formation | Formation du Narèt     |
|15203487 | Breithorn-Serpentinit | Serpentinite du Breithorn     |
|15203488 | Loranco-Amphibolit | Amphibolite de Loranco     |
|15203489 | Andolla-Eklogit | Éclogite d&#39;Andolla     |
|15203490 | Roz-Schiefer | Schistes du Roz     |
|15203491 | Ophiolith der Ramosch-Zone | Ophiolite de la zone de Ramosch     |
|15203492 | Metasedimente der Arosa-Decke | Métasédiments de la nappe d&#39;Arosa     |
|15203493 | Totalp-Serpentinit | Serpentinite de la Totalp     |
|15203494 | Maran-Brekzie | Brèche de Maran     |
|15203495 | Solis-Kalk | Calcaire de Solis     |
|15203496 | Metasedimente der Platta-Decke | Métasédiments de la nappe du Platta     |
|15203497 | Flix-Schichten | Schistes de Flix     |
|15203498 | Calpionellenkalk der Platta-Decke | Calcaire à calpionelles de la nappe du Platta     |
|15203499 | Falotta-Radiolarit | Radiolarite de la nappe du Platta     |
|15203500 | Ophiolith der Platta-Decke | Ophiolite de la nappe du Platta     |
|15203501 | Vignun-Gneis | Gneiss de Vignone     |
|15203502 | Metasedimente der Avers-Decke | Métasédiments de la nappe de l&#39;Avers     |
|15203503 | Ophiolith der Avers-Decke | Ophiolite de la nappe de l&#39;Avers     |
|15203504 | Brekzie-Formation | Brekzie-Formation     |
|15203505 | Minschun-Brekzie | Brèche du Minschun     |
|15203506 | Tasna-Altkristallin | Socle cristallin de la nappe de la Tasna     |
|15203507 | Piz-del-Palo-Gneis | Gneiss du Piz del Palo     |
|15203508 | Truzzo-Granit | Granite de Truzzo     |
|15203509 | Rebi-Gneis | Gneiss de Rebi     |
|15203510 | Brione-Gabbro | Gabbro de Brione     |
|15203511 | Gruf-Migmatit | Migmatite du Gruf     |
|15203512 | Adula-D.: Basaler Gneis | Adula-D.: Basaler Gneis     |
|15203513 | Val-Chironico-Gneis | Gneiss du Val Chironico     |
|15203514 | Ganna-Gneis | Gneiss de Ganna     |
|15203515 | Adula-D.: Albit-Oligoklasgneis | Adula-D.: Albit-Oligoklasgneis     |
|15203516 | Sivigia-Gneis | Gneiss de Sivigia     |
|15203517 | Aula-Spruga-Gneiskomplex | Complexe gneissique d&#39;Aula-Spruga     |
|15203518 | Lizun-Grünschiefer | Schistes verts du Lizun     |
|15203519 | Rossi-Formation | Formation des Rossi     |
|15203520 | Bosco-Gneis | Gneiss de Bosco     |
|15203521 | Batnall-Gneis | Gneiss du Batnall     |
|15203522 | Seron-Formation, Calcschistes zoogènes | Seron-Formation, Calcschistes zoogènes     |
|15203523 | Seron-Formation, Conglomérat moyen | Seron-Formation, Conglomérat moyen     |
|15203524 | Frutigen-Formation, Conglomérat intermédiaire | Frutigen-Formation, Conglomérat intermédiaire     |
|15203525 | Frutigen-Formation, Schistes inférieurs | Frutigen-Formation, Schistes inférieurs     |
|15203526 | Gips der Zone Submédiane | Gypse de la Zone Submédiane     |
|15203527 | Karpatischer Keuper | Karpatischer Keuper     |
|15203528 | Zwischenmythen-Mergel | Marne de Zwischenmythen     |
|15203529 | Cenomanbrekzien-Serie | Cenomanbrekzien-Serie     |
|15203530 | Bettlerjoch-Brekzie | Brèche du Bettlerjoch     |
|15203531 | Bargella-Brekzie | Brèche de Bargella     |
|15203532 | Adula-D.: Kalkschiefer und Marmor | Adula-D.: Kalkschiefer und Marmor     |
|15203533 | Salahorn-Fm.: Metaplutonit | Formation du Salahorn: métaplutonite     |
|15203534 | Salahorn-Fm.: Paragneis | Formation du Salahorn: paragneiss     |
|15203535 | Adula-D.: Ultramafitit | Adula-D.: Ultramafitit     |
|15203536 | Cima-Lunga-D.: Kalkschiefer und Marmor | Cima-Lunga-D.: Kalkschiefer und Marmor     |
|15203537 | Cima-Lunga-D.: Dolomitmarmor | Cima-Lunga-D.: Dolomitmarmor     |
|15203538 | Cima-Lunga-D.: Paragneis | Cima-Lunga-D.: Paragneis     |
|15203539 | Vacarisc-Gneis | Gneiss de Vacarisc     |
|15203540 | Rognoi-Gneis | Gneiss de Rognoi     |
|15203541 | Cima-Lunga-D.: Granatit | Cima-Lunga-D.: Granatit     |
|15203542 | Cima-Lunga-D.: Amphibolit | Cima-Lunga-D.: Amphibolit     |
|15203543 | Cima-Lunga-D.: Eklogit | Cima-Lunga-D.: Eklogit     |
|15203544 | Cima-Lunga-D.: Ultramafitit | Cima-Lunga-D.: Ultramafitit     |
|15203545 | Personico-Gneis | Gneiss de Personico     |
|15203546 | Leventina-Gneis: oberer Teil | Gneiss de la Leventina: partie supérieure     |
|15203547 | Leventina-Gneis: unterer Teil | Gneiss de la Leventina: partie inférieure     |
|15203548 | Leventina-D.: Kalksilikatfels | Leventina-D.: Kalksilikatfels     |
|15203549 | Leventina-D.: Leukogneis | Leventina-D.: Leukogneis     |
|15203550 | Leventina-D.: Paragneis | Leventina-D.: Paragneis     |
|15203551 | Leventina-D.: Amphibolit | Leventina-D.: Amphibolit     |
|15203552 | Maggia-D.: Amphibolit | Maggia-D.: Amphibolit     |
|15203553 | Simano-D.: Kalkmarmor | Simano-D.: Kalkmarmor     |
|15203554 | Simano-D.: Dolomitmarmor | Simano-D.: Dolomitmarmor     |
|15203555 | Simano-D.: Paragneis | Simano-D.: Paragneis     |
|15203556 | Renten-Gneis | Gneiss de Renten     |
|15203557 | Legiuna-Gneis | Gneiss de Legiuna     |
|15203558 | Simano-D.: Amphibolit | Simano-D.: Amphibolit     |
|15203559 | Simano-D.: Ultramafitit | Simano-D.: Ultramafitit     |
|15203560 | Alpbach-Schiefer | Schistes de l&#39;Alpbach     |
|15203561 | Arosa-D.: Gabbro | Arosa-D.: Gabbro     |
|15203562 | Klippen-Flysch | Klippen-Flysch     |
|15203563 | Couches-Rouges der ZSK | Couches-Rouges de klippes de Suisse centrale     |
|15203564 | Wägital-Flysch: oberer Teil (Paläogen) | Flysch du Wägital: partie supérieure (Paléogène)     |
|15203565 | Wägital-Flysch: untererer Teil (Kreide) | Flysch du Wägital: partie inférieure (Crétacé)     |
|15203566 | Wägital-Flysch: basaler, tektonisierter Teil | Flysch du Wägital: partie basale, tectonisée     |
|15203567 | Gibel- und Griggeli-Formation | Formations de Gibel et de Griggeli     |
|15203568 | Dolomit der Klippen-Decke | Dolomie des Préalpes Médianes     |
|15203569 | Dolomit und Kalk der Klippen-Decke | Dolomie et calcaire des Préalpes Médianes     |
|15203570 | Bunter schiefriger Dolomit und Rauwacke der Klippen-Decke | Dolomie schisteuse et cornieule des Préalpes Médianes     |
|15203571 | Rauwacke der Klippen-Decke | Cornieule des Préalpes Médianes     |
|15203572 | Gipsmergel und Sandstein der Klippen-Decke | Marne gypseuse et grès des Préalpes Médianes     |
|15203573 | Schlieren-Sandstein, im Paläogen tektonisch überprägt | Grès des Schlieren, tectonisé au Paléogène     |
|15203574 | Leimern-Schichten | Couches de la Leimern     |
|15203575 | Rauwacke und Quarzsandstein der Klippen-Decke (basale Trias) | Cornieule et grès quartzitique des Préalpes Médianes (Trias basal)     |
|15203576 | Schlieren-Flysch: Hauptmasse (Paläogen) | Flysch des Schlieren: masse principale (Paléogène)     |
|15203577 | Mittellias der Klippen-Decke | Lias moyen des Préalpes     |
|15203578 | Langel-Member der Zentralschweizer Klippen | Membre de Langel des klippes de Suisse centrale     |
|15203579 | Nolla-Tonschiefer: Quarzsandstein | Schistes argileux de la Nolla: grès quartzitique     |
|15203580 | Bärenhorn-Formation: Quarzsandstein | Formation du Bärenhorn: grès quartzitique     |
|15203581 | Kalkiger Tonschiefer der Grava-Decke | Schiste argilo-calcaire de la nappe de la Grava     |
|15203582 | Toniger Kalkschiefer der Grava-Decke | Schiste calcaréo-argileux de la nappe de la Grava     |
|15203583 | Trias der Grava-Decke, undifferenziert | Trias de la nappe de la Grava, indifférencié     |
|15203584 | Soladier- und Verdy-Member, undifferenziert | Soladier- und Verdy-Member, undifferenziert     |
|15203585 | Col-de-Tompey- und Bois-de-Luan-Member, undifferenziert | Col-de-Tompey- und Bois-de-Luan-Member, undifferenziert     |
|15203586 | Heiti- und Rossinière-Formation, undifferenziert | Heiti- und Rossinière-Formation, undifferenziert     |
|15203587 | Coulaytes-Melange und Cuvigne-Derrey-Formation, undifferenziert | Coulaytes-Melange und Cuvigne-Derrey-Formation, undifferenziert     |
|15203588 | Langel- und Col-de-Cordon-Member, undifferenziert | Langel- und Col-de-Cordon-Member, undifferenziert     |
|15203589 | Grande-Bonavau-Formation und Formation spathique, undifferenziert | Grande-Bonavau-Formation und Formation spathique, undifferenziert     |
|15203590 | Col-de-Tompey- und Agreblierai-Member, undifferenziert | Col-de-Tompey- und Agreblierai-Member, undifferenziert     |
|15203591 | Chavanette- und Rubli-Member, undifferenziert | Chavanette- und Rubli-Member, undifferenziert     |
|15203592 | Barrhorn-Einheit: Flysch | Barrhorn-Einheit: Flysch     |
|15203593 | Barrhorn-Einheit: Couches-Rouges | Barrhorn-Einheit: Couches-Rouges     |
|15203594 | Barrhorn-Einheit: Malm | Barrhorn-Einheit: Malm     |
|15203595 | Barrhorn-Einheit: Dogger | Barrhorn-Einheit: Dogger     |
|15203596 | St-Triphon- und Wiriehorn-Fm., undifferenziert | St-Triphon- und Wiriehorn-Fm., undifferenziert     |
|15203597 | Printse-Formation | Printse-Formation     |
|15203598 | Louvie-Gabbro | Louvie-Gabbro     |
|15203599 | Distulberg-Fm.: Graphitschiefer | Distulberg-Fm.: Graphitschiefer     |
|15203600 | Lirec-Fm.: Amphibolit | Lirec-Fm.: Amphibolit     |
|15203601 | Brändjispitz-Gabbro | Brändjispitz-Gabbro     |
|15203602 | Ergischhorn-Komplex: Eklogit | Ergischhorn-Komplex: Eklogit     |
|15203603 | Südegg-Komplex: Prasinit | Südegg-Komplex: Prasinit     |
|15203604 | Südegg-Komplex: Talkschiefer | Südegg-Komplex: Talkschiefer     |
|15203605 | Flysch 2 | Flysch 2     |
|15203606 | Flysch 3 | Flysch 3     |
|15203607 | Hellstätt-Formation und Flysch 2a, undifferenziert | Hellstätt-Formation und Flysch 2a, undifferenziert     |
|15203608 | Walliser-Sedimentabfolge | Walliser-Sedimentabfolge     |
|15203609 | Südegg-Komplex: schwarzer Schiefer | Südegg-Komplex: schwarzer Schiefer     |
|15203610 | Südegg-Komplex: Serpentinit | Südegg-Komplex: Serpentinit     |
|15203611 | Südegg-Komplex: Albitgneis | Südegg-Komplex: Albitgneis     |
|15203612 | Südegg-Komplex: Marmor | Südegg-Komplex: Marmor     |
|15203613 | Südegg-Komplex: Brekzie | Südegg-Komplex: Brekzie     |
|15203614 | Südegg-Komplex: Gips | Südegg-Komplex: Gips     |
|15203615 | Monte-Leone-Decke: Mesozoikum undiff. | Monte-Leone-Decke: Mesozoikum undiff.     |
|15203616 | Monte-Leone-Decke: Dogger-Malm | Monte-Leone-Decke: Dogger-Malm     |
|15203617 | Monte-Leone-Decke: Dogger-Malm: Glimmerschiefer | Monte-Leone-Decke: Dogger-Malm: Glimmerschiefer     |
|15203618 | Monte-Leone-Decke: Dogger-Malm: Marmor | Monte-Leone-Decke: Dogger-Malm: Marmor     |
|15203619 | Monte-Leone-Decke: konglomeratischer Dogger | Monte-Leone-Decke: konglomeratischer Dogger     |
|15203620 | Monte-Leone-Decke: Lias | Monte-Leone-Decke: Lias     |
|15203621 | Monte-Leone-Decke: sandiger Lias | Monte-Leone-Decke: sandiger Lias     |
|15203622 | Monte-Leone-Decke: konglomeratischer Lias | Monte-Leone-Decke: konglomeratischer Lias     |
|15203623 | Monte-Leone-Decke: Trias | Monte-Leone-Decke: Trias     |
|15203624 | Monte-Leone-Decke: quarzitische Trias | Monte-Leone-Decke: quarzitische Trias     |
|15203625 | Pizzo-del-Vallone-Decke: Mesozoikum undiff. | Pizzo-del-Vallone-Decke: Mesozoikum undiff.     |
|15203626 | Pizzo-del-Vallone-Decke: Dogger-Malm | Pizzo-del-Vallone-Decke: Dogger-Malm     |
|15203627 | Pizzo-del-Vallone-Decke: Dogger-Malm: Marmor | Pizzo-del-Vallone-Decke: Dogger-Malm: Marmor     |
|15203628 | Pizzo-del-Vallone-Decke: Dogger-Malm: Glimmerschiefer | Pizzo-del-Vallone-Decke: Dogger-Malm: Glimmerschiefer     |
|15203629 | Pizzo-del-Vallone-Decke: Dogger-Malm: Vulkanit | Pizzo-del-Vallone-Decke: Dogger-Malm: Vulkanit     |
|15203630 | Pizzo-del-Vallone-Decke: Lias | Pizzo-del-Vallone-Decke: Lias     |
|15203631 | Pizzo-del-Vallone-Decke: Trias | Pizzo-del-Vallone-Decke: Trias     |
|15203632 | Artsinol-Sedimentabfolge undiff. | Artsinol-Sedimentabfolge undiff.     |
|15203633 | Artsinol-Sedimentabfolge: Trias | Artsinol-Sedimentabfolge: Trias     |
|15203634 | Artsinol-Sedimentabfolge: Trias: Rauwacke | Artsinol-Sedimentabfolge: Trias: Rauwacke     |
|15203635 | Métailler-Formation: Quarzit | Métailler-Formation: Quarzit     |
|15203636 | Métailler-Formation: Glimmerschiefer | Métailler-Formation: Glimmerschiefer     |
|15203637 | Métailler-Formation: Chloritoid-Glimmerschiefer | Métailler-Formation: Chloritoid-Glimmerschiefer     |
|15203638 | Distulberg-Formation: Schiefer | Distulberg-Formation: Schiefer     |
|15203639 | Distulberg-Formation: Albitgneis | Distulberg-Formation: Albitgneis     |
|15203640 | Barrhorn-Sedimentabfolge: Trias | Barrhorn-Sedimentabfolge: Trias     |
|15203641 | Siviez-Mischabel-Decke: Aplit | Siviez-Mischabel-Decke: Aplit     |
|15203642 | Siviez-Mischabel-Decke: Pegmatit | Siviez-Mischabel-Decke: Pegmatit     |
|15203643 | Lirec-Formation: leukokrater Mikroklingneis | Lirec-Formation: leukokrater Mikroklingneis     |
|15203644 | Adlerflüe-Formation: leukokrater Gneis | Adlerflüe-Formation: leukokrater Gneis     |
|15203645 | Ergischhorn-Komplex: leukokrater aplitischer Gneis | Ergischhorn-Komplex: leukokrater aplitischer Gneis     |
|15203646 | Stalden-Gneiskomplex undiff. | Stalden-Gneiskomplex undiff.     |
|15203647 | Stalden-Gneiskomplex: Ahorn-Augengneis | Stalden-Gneiskomplex: Ahorn-Augengneis     |
|15203648 | Stalden-Gneiskomplex: Amphibolit | Stalden-Gneiskomplex: Amphibolit     |
|15203649 | Printse-Formation: Konglomerat | Printse-Formation: Konglomerat     |
|15203650 | Printse-Formation: Graphitschiefer | Printse-Formation: Graphitschiefer     |
|15203651 | Portjengrat-Decke: Kalzitmarmor | Portjengrat-Decke: Kalzitmarmor     |
|15203652 | Portjengrat-Decke: Dolomitmarmor | Portjengrat-Decke: Dolomitmarmor     |
|15203653 | Portjengrat-Decke: Arkose | Portjengrat-Decke: Arkose     |
|15203654 | Portjengrat-Decke: Grundgebirge | Portjengrat-Decke: Grundgebirge     |
|15203655 | Gornergrat-Decke: Kalkschisfer, sandiger Marmor, Brekzie | Gornergrat-Decke: Kalkschisfer, sandiger Marmor, Brekzie     |
|15203656 | Gornergrat-Decke: Trias | Gornergrat-Decke: Trias     |
|15203657 | Gornergrat-Decke: Phengit-Albitgneis | Gornergrat-Decke: Phengit-Albitgneis     |
|15203658 | Gornergrat-Decke: Basischer Gang | Gornergrat-Decke: Basischer Gang     |
|15203659 | Gornergrat-Decke: Granat-Muskovit-Schiefer | Gornergrat-Decke: Granat-Muskovit-Schiefer     |
|15203660 | Frilihorn-Decke: Trias | Frilihorn-Decke: Trias     |
|15203661 | Frilihorn-Decke: Trias: Rauwacke | Frilihorn-Decke: Trias: Rauwacke     |
|15203662 | Garda-Bordon-Formation: Black Shales (Série feuilletée) | Garda-Bordon-Formation: Black Shales (Série feuilletée)     |
|15203663 | Garda-Bordon-Formation: Quarzschiefer | Garda-Bordon-Formation: Quarzschiefer     |
|15203664 | Tsaté-Decke: Serpentinit | Tsaté-Decke: Serpentinit     |
|15203665 | Zermatt-Saas-Decke: Eklogit | Zermatt-Saas-Decke: Eklogit     |
|15203666 | Zermatt-Saas-Decke: Metapyroxenit | Zermatt-Saas-Decke: Metapyroxenit     |
|15203667 | Zermatt-Saas-Decke: Metagabbro | Zermatt-Saas-Decke: Metagabbro     |
|15203668 | Zermatt-Saas-Decke: Rodingit | Zermatt-Saas-Decke: Rodingit     |
|15203669 | Zermatt-Saas-Decke: Talkschiefer | Zermatt-Saas-Decke: Talkschiefer     |
|15203670 | Lengenbach-Dolomitmarmor | Lengenbach-Dolomitmarmor     |
|15204001 | God-Drosa-Flysch | Flysch du God Drosa     |
|15204002 | Chanèls-Formation | Formation de Chanèls     |
|15204003 | Lech-Formation | Formation de Lech     |
|15204004 | Emmat-Formation | Formation d&#39;Emmat     |
|15204005 | Russenna-Formation | Formation du (Munt) Russenna     |
|15204006 | Ammergau-Formation | Formation d&#39;Ammergau     |
|15204007 | Blais-Formation | Formation du Blais     |
|15204008 | Plattas-Member | Membre de Plattas     |
|15204009 | Ruhpolding-Formation | Formation de Ruhpolding     |
|15204010 | Saluver-Gruppe | Groupe du (Piz) Saluver     |
|15204011 | Saluver-Formation | Formation du (Piz) Saluver     |
|15204012 | Bardella-Formation | Formation de Bardella     |
|15204013 | Salteras-Formation | Formation du (Piz) Salteras     |
|15204014 | Salamun-Brekzie | Brèche de Salamun     |
|15204015 | Err-Brekzie | Brèche d&#39;Err     |
|15204016 | Allgäu-Formation | Formation de l&#39;Allgäu     |
|15204017 | Mezzaun-Member | Membre du (Piz) Mezzaun     |
|15204018 | Blaisun-Member | Membre du (Piz) Blaisun     |
|15204019 | Trupchun-Member | Membre du (Val) Trupchun     |
|15204020 | Agnelli-Formation | Formation d&#39;Agnelli     |
|15204021 | Adnet-Kalk | Calcaire d&#39;Adnet     |
|15204022 | Hierlatz-Kalk | Calcaire de Hierlatz     |
|15204023 | Alv-Brekzie | Brèche d&#39;Alv     |
|15204024 | Kössen-Formation | Formation de Kössen     |
|15204025 | Zirmenkopf-Kalk | Calcaire du Zirmenkopf     |
|15204026 | Mitgel-Member | Membre du (Piz) Mitgel     |
|15204027 | Ramoz-Member | Membre de Ramoz     |
|15204028 | Schesaplana-Member | Membre du Schesaplana     |
|15204029 | Alplihorn-Member | Membre de l&#39;Alplihorn     |
|15204030 | Hauptdolomit-Gruppe | Hauptdolomit-Gruppe     |
|15204031 | Murtèr-Plattenkalk | Calcaire plaqueté du (Piz) Murtèr     |
|15204032 | Murteret-Dolomit | Dolomie du Murteret     |
|15204033 | Diavel-Formation | Formation du (Piz dal) Diavel     |
|15204034 | Quattervals-Formation | Formation du (Piz) Quattervals     |
|15204035 | Crappa-Mala-Mergel | Marne de la Crappa Mala     |
|15204036 | Pra-Grata-Member | Membre de Pra Grata     |
|15204037 | Müschauns-Dolomit | Dolomie du (Val) Müschauns     |
|15204038 | Raibl-Gruppe | Groupe de Raibl     |
|15204039 | Fanez-Formation | Formation de Fanez     |
|15204040 | Valbella-Member | Membre de la Valbella     |
|15204041 | Fanez-Dolomit | Dolomie de Fanez     |
|15204042 | Mezdi-Member | Membre du (Piz) Mezdi     |
|15204043 | Cluozza-Member | Membre du Val Cluozza     |
|15204044 | Stugl-Member | Membre de Stugl     |
|15204045 | Mingèr-Formation | Formation du Val Mingèr     |
|15204046 | Mingèr-Dolomit | Dolomie du Val Mingèr     |
|15204047 | Mora-Member | Membre du Val Mora     |
|15204048 | Garone-Formation | Formation du (Monte) Garone     |
|15204049 | Arlberg-Formation | Formation de l&#39;Arlberg     |
|15204050 | Partnach-Formation | Formation de la Partnach     |
|15204051 | Altein-Formation | Formation de l&#39;Altein     |
|15204052 | Parai-Alba-Member | Membre de la Parai Alba     |
|15204053 | Prosanto-Formation | Formation du (Piz) Prosanto     |
|15204054 | Vallatscha-Formation | Formation du (Piz) Vallatscha     |
|15204055 | Tiaun-Brekzie | Brèche du Tiaun     |
|15204056 | Vallatscha-Member | Membre du (Piz) Vallatscha     |
|15204057 | Turettas-Member | Membre du (Piz) Turettas     |
|15204058 | Landwasser-Member | Membre de la Landwasser     |
|15204059 | S-charl-Formation | Formation de S-charl     |
|15204060 | Sertig-Member | Membre du Sertig     |
|15204061 | Ravais-ch-Member | Membre de Ravais-ch     |
|15204062 | Reifling-Formation | Formation de Reiflingen     |
|15204063 | Ducan-Formation | Formation du (Piz) Ducan     |
|15204064 | Trochitendolomit-Member | Trochitendolomit-Member     |
|15204065 | Brachiopodenkalk-Member | Brachiopodenkalk-Member     |
|15204066 | Eisendolomit-Member | Eisendolomit-Member     |
|15204067 | Gracilis-Member | Gracilis-Member     |
|15204068 | Gutenstein-Formation | Formation de Gutenstein     |
|15204069 | Reichenhall-Formation | Formation de Reichenhall     |
|15204070 | Fuorn-Formation | Formation du Fuorn     |
|15204071 | Punt-la-Drossa-Member | Membre de Punt la Drossa     |
|15204072 | Pflanzenquarzit | Pflanzenquarzit (Fm. du Fuorn)     |
|15204073 | Unteres Member der Fuorn-Formation | Membre inférieur de la Fm. du Fuorn     |
|15204074 | Val-Müstair-Gruppe | Groupe du Val Müstair     |
|15204075 | Chazforà-Formation | Formation de Chazforà     |
|15204076 | Tuors-Member | Membre du (Val) Tuors     |
|15204077 | Val-Püra-Member | Membre du Val Püra     |
|15204078 | Präbichl-Formation | Formation de Präbichl     |
|15204079 | Ruina-Formation | Formation de la Ruina     |
|15204080 | Sandhubel-Member | Membre du Sandhubel     |
|15204081 | Bellaluna-Member | Membre de Bellaluna     |
|15204082 | Mönchalp-Augengneis | Gneiss oeillé de la Mönchalp     |
|15204083 | Tschuggen-Augengneis | Gneiss oeillé de Tschuggen     |
|15204084 | Güstizia-Gneis | Gneiss de la Güstizia     |
|15204085 | Plasseggen-Augengneis | Gneiss oeillé de Plasseggen     |
|15204086 | Trias des Ostalpins | Trias de l&#39;Austroalpin     |
|15204087 | Dogger des Ostalpins | Dogger des Ostalpins     |
|15204088 | Malm des Ostalpins | Malm des Ostalpins     |
|15204089 | Kreide des Ostalpins | Kreide des Ostalpins     |
|15204090 | Lias des Ostalpins | Lias des Ostalpins     |
|15204091 | Kristallin des Ostalpins | Kristallin des Ostalpins     |
|15204092 | Nair-Porphyroid | Nair-Porphyroid     |
|15204093 | Lavatèra-Brekzie | Lavatèra-Brekzie     |
|15204094 | Varaina-Schiefer | Varaina-Schiefer     |
|15204095 | Sprenkel-Schiefer | Sprenkel-Schiefer     |
|15204096 | Fedoz-Gneiskomplex | Complexe gneissique de Fedoz     |
|15204097 | Fedoz-Metagabbro | Fedoz-Metagabbro     |
|15204098 | Maloja-Orthogneis | Maloja-Orthogneis     |
|15204099 | Maloja-Gneiskomplex | Complexe gneissique du Maloja     |
|15204100 | Ur-Brekzie | Ur-Brekzie     |
|15204101 | Tschima-da-Flix-Granit | Tschima-da-Flix-Granit     |
|15204102 | Err-Granodiorit | Granodiorite d&#39;Err     |
|15204103 | Postvariszische Diabasgänge | Filons de diabase postvarisques     |
|15204104 | Flüela-Augnengneis | Gneiss oeillé de la Flüela     |
|15204105 | Dorfberg-Gneis | Gneiss du Dorfberg     |
|15204106 | Chaschauna-Brekzie | Brèche du Piz Chaschauna     |
|15204107 | Sesvenna-Augengneis | Gneiss oeillé de la Sesvenna     |
|15204108 | Vaüglia-Granodiorit | Granodiorite de Vaüglia     |
|15204109 | Döss-Radond-Vulkanite | Roches volcanique du Döss Radond     |
|15204110 | Augsten-Brekzie | Brèche de l&#39;Augsten     |
|15204111 | Piz-Trovat-Metarhyolit | Métarhyolite du Piz Trovat     |
|15204112 | Sass-Queder-Metarhyolith | Métarhyolite du Sass Queder     |
|15204113 | La-Rösa-Orthogneis | Orthogneiss de la Rösa     |
|15204114 | Carale-Paraschiefer | Schistes du Carale     |
|15204115 | Gosau-Gruppe | Groupe de Gosau     |
|15204116 | Morteratsch-Serpentinit | Serpentinite du Morteratsch     |
|15204117 | Forun-Augengneis | Gneiss oeillé du Forun     |
|15204118 | Kesch-Augengneis | Gneiss oeillé du Piz Kesch     |
|15204119 | prävariszisches polyzyklisches Grundgebirge des Ostalpins | socle polycyclique anté-varisque de l&#39;Austroalpin     |
|15204120 | «Jüngere Orthogneise» | «Jüngere Orthogneise»     |
|15204121 | «Ältere Orthogneise» | «Ältere Orthogneise»     |
|15204122 | Val-Rude-Orthogneis | Orthogneiss du Val Rude     |
|15204123 | Corvatsch-Granodiorit | Granodiorite du Corvatsch     |
|15204124 | Julier-Granodiorit | Granodiorite du Julier     |
|15204125 | Sasso-Rosso-Granodiorit | Granodiorite du Sasso Rosso     |
|15204126 | Lavinèr-Brekzie | Brèche du Piz Lavinèr     |
|15204127 | Haupter-Brekzie | Brèche de l&#39;Haupter     |
|15204128 | Permo-Karbon des Ostalpins | Permo-Carbonifère de l&#39;Austroalpin     |
|15204130 | Buffalora-Gruppe | Groupe de Buffalora     |
|15204132 | Variszische Intrusiva des Ostalpins | roches intrusives varisques de l&#39;Austroalpin     |
|15204133 | alkalische Intrusiva des Ostalpins | roches intrusives alcalines de l&#39;Austroalpin     |
|15204134 | kalkalkalische Intrusiva des Ostalpins | roches intrusives calc-alcalines de l&#39;Austroalpin     |
|15204135 | prävariszische Orthogneise des Ostalpins | orthogneiss anté-varisques de l&#39;Austroalpin     |
|15204136 | prävariszische Paragneise des Ostalpins | paragneiss anté-varisques de l&#39;Austroalpin     |
|15204137 | prävariszische Grüngesteine des Ostalpins | roches vertes anté-varisques de l&#39;Austroalpin     |
|15204138 | Uglix-Plattenkalk | Calcaire d&#39;Uglix     |
|15204139 | Parait-Chavagl-Granit | Granite du Parait Chavagl     |
|15204140 | Clavadatsch-Brekzie | Brèche de Clavadatsch     |
|15204141 | Corno-di-Campo-Granodiorit | Granodiorite du Corno di Campo     |
|15204142 | Campocologno-Gabbro | Gabbro de Campocologno     |
|15204143 | Celerina-Orthogneis | Orthogneiss de Celerina     |
|15204144 | Tonale-Schiefer | Schistes du Tonale     |
|15204145 | Gips der Raibl-Gruppe | Gypse du Groupe de Raibl     |
|15204146 | Rauwacke der Raibl-Gruppe | Cornieule du Groupe de Raibl     |
|15204147 | Rifffazies der Arlberg-Formation | faciès récifal de la Formation de l&#39;Arlberg     |
|15204148 | Alpiner Muschelkalk | Alpiner Muschelkalk     |
|15204149 | Raibl-Gr.: Dolomit | Groupe de Raible: dolomite     |
|15204150 | Hauptdolomit-Gr.: bituminöse Dolomitbrekzie | Groupe de la Hauptdolomite: brèche dolomitique bitumineuse     |
|15204151 | Raibl-Gruppe der Zentralschweizer Klippen | Groupe de Raibl des klippes de Suisse centrale     |
|15205001 | Dolin-Gruppe | Groupe du Dolin     |
|15205002 | Dolin-Kalkbrekzie | Brèche calcaire du Dolin     |
|15205003 | Roisan-Zone | zone de Roisan     |
|15205004 | Arolla-Serie | Série d&#39;Arolla     |
|15205005 | Mont-Collon-Komplex | Complexe du Mont Collon     |
|15205006 | Orthogneis der Arolla-Gruppe | orthogneiss du Groupe d&#39;Arolla     |
|15205007 | Valpelline-Serie | Série de Valpelline     |
|15205008 | Castel-di-Sotto-Ton | Argile de Castel di Sotto     |
|15205009 | Pontegana-Konglomerat | Conglomérat de Pontegana     |
|15205010 | Gruppe des Lombardischen Gompholit | Groupe de la Gompholite Lombarde     |
|15205011 | Lucino-Konglomerat | Conglomérat de Lucino     |
|15205012 | Cagno-Sandstein | Grès de Cagno     |
|15205013 | Val-Grande-Sandstein | Grès du Val Grande     |
|15205014 | Prestino-Pelite | Pélite de Prestino     |
|15205015 | Como-Konglomerat | Conglomérat de Como     |
|15205016 | Malnate-Sandstein | Grès de Malnate     |
|15205017 | Rio-dei-Gioghi-Pelite | Pélite du Rio dei Gioghi     |
|15205018 | Chiasso-Formation | Formation de Chiasso     |
|15205019 | Villa-Olmo-Konglomerat | Conglomérat de Villa Olmo     |
|15205020 | Ternate-Formation | Formation de Ternate     |
|15205021 | Brenno-Formation | Formation de Brenno     |
|15205022 | Prella-Konglomerat | Conglomérat de Prella     |
|15205023 | Gruppe des Lombardischen Flysch | Groupe du Flysch Lombard     |
|15205024 | Bergamo-Flysch | Flysch de Bergamo     |
|15205025 | Coldrerio-Flysch | Flysch de Coldrerio     |
|15205026 | Torre-Konglomerat | Conglomérat de Torre     |
|15205027 | Varesotto-Flysch | Flysch du Varesotto     |
|15205028 | Gruppe der Scaglia Lombarda | Groupe de la Scaglia Lombarda     |
|15205029 | Scaglia Rossa Lombarda | Scaglia Rossa Lombarda     |
|15205030 | Scaglia Bianca Lombarda | Scaglia Bianca Lombarda     |
|15205031 | Scaglia Variegata Lombarda | Scaglia Variegata Lombarda     |
|15205032 | Maiolica Lombarda | Maiolica Lombarda     |
|15205033 | Lombardische Radiolarit-Gruppe | Groupe de la Radiolarite Lombarde     |
|15205034 | Rosso ad Aptici | Rosso ad Aptici     |
|15205035 | Calcari a bivalvi planctonici | Calcari a bivalvi planctonici     |
|15205036 | Rosso Ammonitico Lombardo | Rosso Ammonitico Lombardo     |
|15205037 | Grenzposidonienschichten | Lumachelle à Posidonia alpina (Grenzposidonienschichten)     |
|15205038 | Morbio-Formation | Formation de Morbio     |
|15205039 | Besazio-Kalk | Calcaire de Besazio     |
|15205040 | Moltrasio-Formation | Formation de Moltrasio     |
|15205041 | Molino-Member | Membre du Molino     |
|15205042 | Saltrio-Formation | Formation de Saltrio     |
|15205043 | Macchia Vecchia | Macchia Vecchia     |
|15205044 | Broccatello d&#39;Arzo | Broccatello d&#39;Arzo     |
|15205045 | Albenza-Formation | Formation de l&#39;Albenza     |
|15205046 | Zu-Kalk | Calcaire de Zu     |
|15205047 | Tremona-Formation | Formation de Tremona     |
|15205048 | Brecce Retiche | Brecce Retiche     |
|15205049 | Riva-di-Solto-Tonstein | Argilite de Riva di Solto     |
|15205050 | Hauptdolomit | Dolomia Principale     |
|15205051 | Pizzella-Mergel | Marne du (Monte) Pizzella     |
|15205052 | Cunardo-Formation | Formation de Cunardo     |
|15205053 | Meride-Formation | Formation de Meride     |
|15205054 | Kalkschieferzone | Kalkschieferzone (Fm. de Meride)     |
|15205055 | Cassina-Bank | Banc de Cassina     |
|15205056 | Cava Superiore | Cava Superiore     |
|15205057 | Cava Inferiore | Cava Inferiore     |
|15205058 | San-Giorgio-Dolomit | Dolomie du (Monte) San Giorgio     |
|15205059 | Val-Serrata-Tuffite | Tuffite du Val Serrata     |
|15205060 | Besano-Formation | Formation de Besano     |
|15205061 | San-Salvatore-Dolomit | Dolomie du (Monte) San Salvatore     |
|15205062 | Bellano-Formation | Formation de Bellano     |
|15205063 | Servino | Servino     |
|15205064 | Verrucano Lombardo | Verrucano Lombardo     |
|15205065 | Permische Vulkanite | Roches volcanique permienne du Sudalpin     |
|15205066 | Granophyr | Granophyre permien du Sudalpin     |
|15205067 | Andesit und Dazit | Andésite et dacite permiennes du Sudalpin     |
|15205068 | Basalt | Basalte permien du Sudalpin     |
|15205069 | Basaler Tuf | Tuf basal permien du Sudalpin     |
|15205070 | Manno-Formation | Formation de Manno     |
|15205071 | Tertiär des Südalpins | Tertiär des Südalpins     |
|15205072 | Kreide des Südalpins | Kreide des Südalpins     |
|15205073 | Malm des Südalpins | Malm des Südalpins     |
|15205074 | Dogger des Südalpins | Dogger des Südalpins     |
|15205075 | Lias des Südalpins | Lias des Südalpins     |
|15205076 | Trias des Südalpins | Trias des Südalpins     |
|15205077 | Permo-Karbon des Südalpins | Permo-Karbon des Südalpins     |
|15205078 | Kristallin des Südalpins | Kristallin des Südalpins     |
|15205079 | Variszische Intrusiva des Südalpins | roches intrusives varisques du Sudalpin     |
|15205080 | San-Bernardo-Gneis | San-Bernardo-Gneis     |
|15205081 | Prävariszische Metasedimente des Südalpins | métasédiments anté-varisques du Sudalpin     |
|15205082 | Stabbiello-Gneis | Stabbiello-Gneis     |
|15205083 | Giumello-Gneis | Giumello-Gneis     |
|15205084 | Ceneri-Gneis | Ceneri-Gneis     |
|15205085 | Proterozoische und paläozoische Mafite und Ultramafite des Südalpins | Proterozoische und paläozoische Mafite und Ultramafite des Südalpins     |
|15205086 | Mont-Morion-Granit | Mont-Morion-Granit     |
|15205087 | Pointe-d&#39;Otemma-Granodiorit | Pointe-d&#39;Otemma-Granodiorit     |
|15205088 | Bouquetins-Quarzdiorit | Bouquetins-Quarzdiorit     |
|15205089 | Tête-de-Valpelline-Phyllit | Tête-de-Valpelline-Phyllit     |
|15205090 | «Série Rubanée» | «Série Rubanée»     |
|15205091 | Sassa-Metagabbro | Sassa-Metagabbro     |
|15205092 | Maia-Metagabbro | Maia-Metagabbro     |
|15205093 | Losone-Schiefer | Losone-Schiefer     |
|15205094 | Pizzo-Leone-Gneis | Pizzo-Leone-Gneis     |
|15205095 | Fornale-Gabbro | Fornale-Gabbro     |
|15205096 | Matterhorn-Gabbro | Matterhorn-Gabbro     |
|15205097 | Berrio-Gabbro | Berrio-Gabbro     |
|15205098 | Grand-Dolin-Brekzie | Grand-Dolin-Brekzie     |
|15205099 | Oberer Meride-Kalk | Partie supérieure du Calcaire de Meride     |
|15205100 | Unterer Meride-Kalk | Partie inférieure du Calcaire de Meride     |
|15205101 | Dolomit-Band (Meride) | Dolomit-Band (Fm. de Meride)     |
|15205102 | Kalk der Dolin-Gruppe | Calcaire du Groupe du Dolin     |
|15205103 | Dolomit der Dolin-Gruppe | Dolomie du Groupe du Dolin     |
|15205104 | Rauwacke der Dolin-Gruppe | Cornieule du Groupe du Dolin     |
|15205105 | Quarzit der Dolin-Gruppe | Quartzite du Groupe du Dolin     |
|15205106 | Orthogneis der Arolla-Gruppe, leukokrat | Orthogneiss du Groupe d&#39;Arolla, leucocrate     |
|15205107 | Orthogneis der Arolla-Gruppe, augig | Orthogneiss du Groupe d&#39;Arolla, oeillé     |
|15205108 | Orthogneis der Arolla-Gruppe, mylonitisch | Orthogneiss du Groupe d&#39;Arolla, mylonitique     |
|15205109 | Gneis der Arolla-Gruppe, mylonitisch | Gneiss du Groupe d&#39;Arolla, mylonitique     |
|15205110 | Gneis der Arolla-Gruppe, mikroaugig | Gneiss du Groupe d&#39;Arolla, micro-oeillé     |
|15205111 | Metagranitoide der Arolla-Gruppe | Métagranitoïde du Groupe d&#39;Arolla     |
|15205112 | Metabasit der Arolla-Gruppe | Métaroche basique du Groupe d&#39;Arolla     |
|15205113 | Metabasit der Arolla-Gruppe, mylonitisch | Métaroche basique du Groupe d&#39;Arolla, mylonitique     |
|15205114 | Prasinit der Arolla-Gruppe | Prasinite du Groupe d&#39;Arolla     |
|15205115 | Hornblendegabbro der Arolla-Decke | Gabbro à horneblende du Groupe d&#39;Arolla     |
|15205116 | Ultramafitit der Arolla-Gruppe | Roche ultramafique du Groupe d&#39;Arolla     |
|15205117 | Paragneiss der Arolla-Gruppe | Paragneiss du Groupe d&#39;Arolla     |
|15205118 | Glimmerschiefer der Arolla-Gruppe | Micaschiste du Groupe d&#39;Arolla     |
|15205119 | Mylonit der Valpelline-Gruppe | Mylonite du Groupe de Valpelline     |
|15205120 | Amphibolit der Valpelline-Gruppe | Amphibolite du Groupe de Valpelline     |
|15205121 | Marmor der Valpelline-Gruppe | Marbre du Groupe de Valpelline     |
|15205122 | Migmatit der Valpelline-Gruppe | Migmatite du Groupe de Valpelline     |
|15205123 | Roisan-Marmor | Marbre de Roisan     |
|15205124 | Musella-Granit | Granite de Musella     |
|15205125 | Sella-Granodiorit | Granodiorite de la Sella     |
|15205126 | Marinelli-Formation | Formation de Marinelli     |
|15205127 | Kristallin der Margna-Sella | socle cristallin de la nappe de la Margna-Sella     |
|15205128 | Variszische Intrusiva der Margna-Sella | roches intrusives de la nappe de la Margna-Sella     |
|15205129 | Prävariszisches Grundgebirge der Margna-Sella | socle polycyclique anté-varisque de la nappe de la Margna-Sella     |
|15205130 | Prävariszische Metaarkose, Orthogneise | Métaarkose, orthogneiss anté-varisque     |
|15205131 | Orthogneis der Sesia-Decke | orthogneiss de la nappe de Sesia     |
|15205132 | Glimmerschiefer der Sesia-Decke | micaschiste de la nappe de Sesia     |
|15205133 | Finero-Peridotit | Péridotite de Finero     |
|15205134 | Ivrea Mafischer Komplex | Complexe Mafique d&#39;Ivrée     |
|15205135 | Zona Dioritico-Kinzigitica | Zona Dioritico-Kinzigitica     |
|15205136 | Prävariszische Orthogneise des Südalpins | orthogneiss anté-varisques du Sudalpin     |
|15205137 | Pontida-Formation | Formation de Pontida     |
|15205138 | Arolla-Einheit: Metagranit | Arolla-Einheit: Metagranit     |
|15205139 | Arolla-Einheit: Leukokrater Granitgneis | Arolla-Einheit: Leukokrater Granitgneis     |
|15206001 | Periadriatische Vulkanite | roches volcaniques cénozoïques péri-adriatiques     |
|15206002 | Novate-Intrusiva | Intrusion de Novate     |
|15206003 | Bergell-Intrusiva | Intrusion du Bergell     |
|15206004 | Adamello-Intrusiva | Intrusion de l&#39;Adamello     |
|15206005 | Melirolo-Augengneis | Melirolo-Augengneis     |
|15206006 | Bergell-Granodiorit | Bergell-Granodiorit     |
|15206007 | Bergell-Tonalit | Bergell-Tonalit     |
|15206008 | Monte-Bassetta-Quarzdiorit | Monte-Bassetta-Quarzdiorit     |
|15206009 | Sorico-Tonalit | Sorico-Tonalit     |
|15206010 | Jorio-Tonalit | Jorio-Tonalit     |
|15206011 | Val-Masino-Granodiorit | Val-Masino-Granodiorit     |
|15206012 | Alpe-Cameraccio-Granodiorit | Alpe-Cameraccio-Granodiorit     |
|15206013 | Monte-Rosso-Mikrogranit | Monte-Rosso-Mikrogranit     |
|15206014 | Zocca-Aplit | Zocca-Aplit     |
|15206015 | San-Fedelino-Granit | San-Fedelino-Granit     |
|15206016 | Informelle Zuordnung | Informelle Zuordnung     |
|15206017 | Tektonische Brekzie, undifferenziert | Tektonische Brekzie, undifferenziert     |
|15206018 | Lochsiten-Kalk | Lochsiten-Kalk     |
|15206019 | Salleren-Brekzie | Salleren-Brekzie     |
|15206020 | Lithologische Einheit, undifferenziert | Lithologische Einheit, undifferenziert     |
|15206021 | Gips, undifferenziert | Gips, undifferenziert     |
|15206022 | Rauwacke, undifferenziert | Rauwacke, undifferenziert     |
|15206023 | Dolomit, undifferenziert | Dolomit, undifferenziert     |
|15206024 | Ganggesteine, undifferenziert | Ganggesteine, undifferenziert     |
|15206025 | Lias, undifferenziert | Lias, indifférencié     |
|15206026 | Dogger, undifferenziert | Dogger, indifférencié     |
|15206027 | Malm, undifferenziert | Malm, indifférencié     |
|15206028 | Kreide, undifferenziert | Crétacé, indifférencié     |
|15206029 | Trias, undifferenziert | Trias, indifférencié     |
|15206030 | Sedimentgestein, undifferenziert | roche sédimentaire, indifférenciée     |
|15206031 | Kristallingestein, undifferenziert | roche cristalline, indifférenciée     |
|15206032 | Granit, undifferenziert | granite, indifférencié     |
|15206033 | Stratigraphische Einheit, undifferenziert | unité stratigraphique indifférenciée     |
|15206034 | Mesozoikum, undifferenziert | Mésozoïque, indifférencié     |
|15206035 | Rhyolit, undifferenziert | rhyolite, indifférenciée     |
|15206036 | Grüngestein, undifferenziert | roche verte, indifférenciée     |
|15206037 | Amphibolit, undifferenziert | amphibolite, indifférenciée     |
|15206038 | Quarzgang | filon de quartz     |
|15206039 | Aplit | aplite     |
|15206040 | Pegmatit | pegmatite     |
|15206041 | Prasinit, undifferenziert | prasinite, indifférenciée     |
|15206042 | Serpentinit, undifferenziert | serpentinite, indifférenciée     |
|15206043 | Mineralisierter Gang | filon minéralisé     |
|15206044 | Mikrogranit | microgranite     |
|15206045 | Rhétien, undifferenziert | Rhétien, indifférencié     |
|15206046 | Biogener Kalk (Eozän) | calcaire biogène (Éocène)     |
|15206047 | Rodingit | rodingite     |
|15206048 | Saurer Gang | filon acide     |
|15206049 | Basischer Gang | filon basique     |
|15206050 | Eklogit, undifferenziert | éclogite, indifférenciée     |
|15206051 | Mylonit, undifferenziert | mylonite, indifférenciée     |
|15206052 | Kalksilikatfels | roche calcsilicatée     |
|15206053 | Mamor, undifferenziert | marbre, indifférencié     |
|15206054 | Sedimentäre Brekzie, undifferenziert | brèche sédimentaire, indifférenciée     |
|15206055 | Paläozoikum, undifferenziert | Paléozoïque, indifférencié     |
|15206056 | Känozoikum, undifferenziert | Cénozoïque, indifférencié     |
|15206057 | Ultramafische Gesteine | roche ultramafique     |
|15206058 | Verwitterter Fels, undifferenziert | roche altérée, indifférenciée     |
|15206059 | Ophikalzit, undifferenziert | ophicalcite, indifférenciée     |
|15206060 | Talkschiefer, undifferenziert | talcschiste, indifférencié     |
|15206061 | Mikrodiorit, undifferenziert | microdiorite, indifférenciée     |
|15206062 | Quarzit, undifferenziert | quartzite, indifférenciée     |
|15206063 | Fuchsit-Zoisitschiefer, undifferenziert | schiste à zoïsite et fuchsite, indifférencié     |
|15206064 | Konglomerat, undifferenziert | conglomérat, indifférencié     |
|15206065 | Glaukophanschiefer, undifferenziert | schiste à glaucophane, indifférencié     |
|15206066 | Bündnerschiefer, undifferenziert | Bündnerschiefer, indifférencié     |
|15206067 | Augengneis, undifferenziert | gneiss oeillé, indifférencié     |
|15206068 | Granatglimmerschiefer, undifferenziert | micaschistes à grenat, indifférencié     |
|15206069 | Albit-Muskowitschiefer, undifferenziert | schiste à muscovite et albite, indifférencié     |
|15206070 | Gneis, undifferenziert | gneiss, indifférencié     |
|15206071 | Graphitschiefer, undifferenziert | schiste graphiteux, indifférencié     |
|15206072 | Glimmerschiefer, undifferenziert | micaschistes, indifférencié     |
|15206073 | Garbenschiefer, undifferenziert | Garbenschiefer, indifférencié     |
|15206074 | Diorit, undifferenziert | diorite, indifférenciée     |
|15206075 | Gabbro, undifferenziert | gabbro, indifférencié     |
|15206076 | Orthogneis, undifferenziert | orthogneiss, indifférencié     |
|15206077 | Paragneis, undifferenziert | paragneiss, indifférencié     |
|15206078 | Vulkanische Gesteine, undifferenziert | roche volcanique, indifférenciée     |
|15206079 | Basalt, undifferenziert | basalte, indifférencié     |
|15206080 | Karbon, undifferenziert | Carbonifère, indifférencié     |
|15206081 | Chloritschiefer, undifferenziert | schiste chloriteux, indifférencié     |
|15206082 | Phyllit, undifferenziert | phyllite, indifférenciée     |
|15206083 | Quarzphyllit, undifferenziert | quartzphyllite, indifférenciée     |
|15206084 | Bündnerschiefer, kalkig | Bündnerschiefer calcaires     |
|15206085 | Bündnerschiefer, tonig | Bündnerschiefer argileux     |
|15206086 | Migmatit, undifferenziert | migmatite, indifférenciée     |
|15206087 | Tonalit, undifferenziert | tonalite, indifférenciée     |
|15206088 | Syenit, undifferenziert | syénite, indifférenciée     |
|15206089 | Tektonit, undifferenziert | tectonite, indifférenciée     |
|15206090 | Hornfels, undifferenziert | cornéenne, indifférenciée     |
|15206091 | Hornblendegneis, undifferenziert | gneiss à hornblende, indifférencié     |
|15206092 | Biotit-Plagioklasgneis, undifferenziert | gneiss à biotite et plagioclase, indifférencié     |
|15206093 | Bändergneis, undifferenziert | gneiss rubané, indifférencié     |
|15206094 | Zweiglimmergneis, undifferenziert | gneiss à deux micas, indifférencié     |
|15206095 | Phyllitgneis, undifferenziert | gneiss phyllitique, indifférencié     |
|15206096 | Peridotit, undifferenziert | péridotite, indifférencié     |
|15206097 | Bänder- und Schollenamphibolit, undifferenziert | amphibolite rubanée et à blocs, indifférencié     |
|15206098 | Granatamphibolit, undifferenziert | amphibolite à grenat, indifférencié     |
|15206099 | Diabasgang, undifferenziert | filon diabasique, indifférencié     |
|15206100 | Perm, undifferenziert | Permien, indifférencié     |
|15206101 | Kalkmarmor, undifferenziert | marbre calcaire, indifférencié     |
|15206102 | Dolomitmarmor, undifferenziert | marbre dolomitique, indifférencié     |
|15206103 | Permokarbon, undifferenziert | Permo-Carbonifère, indifférencié     |
|15206104 | Kalkschiefer, undifferenziert | calcschiste, indifférencié     |
|15206105 | Sandstein, undifferenziert | grès, indifférencié     |
|15206106 | Tonschiefer, undifferenziert | schiste argileux, indifférencié     |
|15206107 | Radiolarit, undifferenziert | radiolarite, indifférenciée     |
|15206108 | Kalkstein, undifferenziert | calcaire, indifférencié     |
|15206109 | Konglomeratgneis, undifferenziert | gneiss conglomératique, indifférencié     |
|15206110 | Prävariszisches, polyzyklisches Grundgebirge, undifferenziert | socle polycyclique anté-varisque, indifférencié     |
|15206111 | Schiefer, undifferenziert | schiste, indifférencié     |
|15206112 | Aplitgneis, undifferenziert | gneiss aplitique, indifférencié     |
|15206113 | Süsswasserkalk, undifferenziert | Süsswasserkalk, undifferenziert     |
|15206114 | Tektonisches Melange | mélange tectonique     |
|15206115 | Flysch, undifferenziert | Flysch, indifférencié     |
|15206116 | Aptychenkalk, undiff. | Calcaire à aptychus, indiff.     |
|15206117 | Quarzsandstein, undiff. | Grès quartzitique, indiff.     |
|15206118 | Mergelstein, undifferenziert | Mergelstein, undifferenziert     |
|15206119 | Basisches Gestein, undifferenziert | Basisches Gestein, undifferenziert     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |


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
|15102001 | Sedimentgestein | roche sédimentaire     |
|15102003 | klastisches Sedimentgestein, undifferenziert | roche sédimentaire clastique, indifférenciée     |
|15102005 | Konglomerat und Brekzie, undifferenziert (Psephit, Korngrösse: Kies, Steine und Blöcke) | conglomérat et brèche, indifférencié (psephite: classe des graviers, cailloux et blocs)     |
|15102006 | Brekzie | brèche     |
|15102007 | Konglomerat | poudingue     |
|15102009 | Sandstein, undifferenziert (Psammit: Sandkorngrösse) | grès, indifférencié (psammite: classe des sables)     |
|15102010 | Quarzsandstein | grès quartzitique     |
|15102011 | Kalksandstein | grès calcaire     |
|15102012 | Dolomitsandstein | grès dolomitique     |
|15102013 | kieseliger Sandstein | grès siliceux     |
|15102014 | mergeliger Sandstein | grès marneux     |
|15102015 | toniger Sandstein | grès argileux     |
|15102016 | Arkose | arkose     |
|15102017 | Flyschsandstein, Grauwacke | grès du flysch, grauwacke     |
|15102018 | Geröll führender Sandstein | grès à galets     |
|15102019 | Glimmersandstein | grès micacé     |
|15102020 | Glaukonitsandstein | grès glauconieux     |
|15102021 | Nummulitensandstein | grès à nummulites     |
|15102022 | Muschelsandstein | grès coquillier     |
|15102024 | Pelit, undifferenziert | pélite, indifférenciée     |
|15102025 | Siltstein | siltite     |
|15102026 | Tonstein | argilite     |
|15102027 | Mergelstein | marne     |
|15102028 | Tonmergelstein | marne argileuse     |
|15102029 | Kalkmergelstein | marne calcaire     |
|15102030 | Schlammstein | mudstone     |
|15102032 | biogenes / biochemisches / organisches Sedimentgestein, undifferenziert | roche sédim. biogène / biochimique / organique, indifférenciée     |
|15102034 | Kalkstein, undifferenziert | calcaire, indifférencié     |
|15102035 | Kieselkalk | calcaire siliceux     |
|15102036 | Spatkalk | calcaire spathique     |
|15102037 | Mikrit | calcaire micritique     |
|15102038 | Arenit | calcarénite     |
|15102039 | Rudit | calcirudite     |
|15102040 | Riffkalk | calcaire récifal     |
|15102041 | Kalkbrekzie | calcaire bréchique     |
|15102042 | Kalkoolith | calcaire oolitique     |
|15102043 | Nummulitenkalk | calcaire à nummulites     |
|15102044 | Aptychenkalk | calcaire à aptychus     |
|15102045 | biogener Kalkstein, undifferenziert | calcaire biogénique, indifférencié     |
|15102046 | detritischer Kalk | calcaire détritique     |
|15102047 | Süsswasserkalk | calcaire d&#39;eau douce     |
|15102049 | Dolomit | dolomie     |
|15102051 | kieseliges Gestein, undifferenziert | sédiment siliceux, indifférencié     |
|15102052 | Radiolarit | radiolarite     |
|15102053 | Spiculit | spiculite     |
|15102054 | Hornstein, Chert | chaille, chert     |
|15102056 | Kohle, undifferenziert | charbon, indifférencié     |
|15102057 | Lignit (organisches Sedimentgestein) | lignite (roche sédimentaire organique)     |
|15102058 | Steinkohle | houille     |
|15102059 | Anthrazit | anthracite     |
|15102061 | Eisenoolith | oolite ferrugineuse     |
|15102063 | phosphoritreiches Gestein, undifferenziert | roche phosphatée, indifférenciée     |
|15102064 | phosphoritreicher Sandstein | grès phosphaté     |
|15102065 | phosphoritreicher Kalkstein | calcaire phosphaté     |
|15102066 | phosphoritreicher Mergelstein | marne phosphatée     |
|15102068 | chemisches Sedimentgestein, undifferenziert | roche sédimentaire chimique, indifférenciée     |
|15102070 | Evaporit, undifferenziert | évaporite, indifférenciée     |
|15102071 | Anhydrit | anhydrite     |
|15102072 | Gips | gypse     |
|15102073 | Steinsalz | sel     |
|15102075 | Karbonat, undifferenziert | roche carbonatée, indifférenciée     |
|15102076 | Rauwacke (Sedimentgestein) | rauwacke (roche sédimentaire)     |
|15102077 | Quelltuff (Kalksinter, Sedimentgestein) | tuf calcaire (roche sédimentaire)     |
|15102078 | Travertin (Kalksinter, Sedimentgestein) | travertin (roche sédimentaire)     |
|15102080 | Residualgestein / pedogen überprägtes Gestein, undifferenziert | roche résiduelle / roche sédim. transf. par pédogenèse, indifférenciée     |
|15102082 | Bohnerz | pisolite ferrugineuse     |
|15102084 | siderolithische Verwitterungsbildungen | sédiment d&#39;altération sidérolithique     |
|15102086 | silikatreiches Gestein, undifferenziert | roche silicatée, indifférenciée     |
|15102087 | Boluston | argile à bolus     |
|15102088 | Huppererde | hupper     |
|15102089 | Quarzsand | sable quartzitique     |
|15102090 | Silcrete | silcrète     |
|15102092 | pedogenes Karbonat, undifferenziert | roche carbonatée pédogénétique, indifférenciée     |
|15102093 | Caliche | caliche     |
|15102094 | Krustenkalk | calcrète     |
|15102100 | Echinodermenkalk | calcaire échinodermique     |
|15102101 | glaukonitischer Kalkstein | calcaire glauconieux     |
|15102102 | Lithothamniensandstein | grès à lithothamnies     |
|15102103 | Eisensandstein | grès ferrugineux     |
|15102104 | glaukonitischer Mergel | marne glauconieuse     |
|15102105 | kreidiger Kalk | calcaire crayeux     |
|15102106 | bioklastischer Kalk | calcaire bioclastique     |
|15102107 | Mergelkalk | calcaire marneux     |
|15102108 | eisenschüssiger Kalk | calcaire ferrugineux     |
|15102109 | Dolomitbrekzie | brèche dolomitique     |
|15103001 | Magmatit | roche magmatique     |
|15103003 | Intrusivgestein, undifferenziert | roche intrusive, indifférenciée     |
|15103005 | Tiefengestein, undifferenziert | roche plutonique, indifférenciée     |
|15103006 | Alkalogranit | granite alcalin     |
|15103007 | Granit | granite     |
|15103008 | Granodiorit | granodiorite     |
|15103009 | Quarzdiorit | diorite quartzique     |
|15103010 | Tonalit | tonalite     |
|15103011 | Diorit | diorite     |
|15103012 | Syenit | syénite     |
|15103013 | Alkalisyenit | syénite alcaline     |
|15103014 | Quarzgabbro | gabbro quartzique     |
|15103015 | Gabbro | gabbro     |
|15103016 | Norit | norite     |
|15103017 | Monzodiorit | monzodiorite     |
|15103018 | Monzogabbro | monzogabbro     |
|15103019 | Monzonit | monzonite     |
|15103020 | Pyroxenit (Intrusivgestein) | pyroxénite (roche intrusive)     |
|15103021 | Peridotit (Intrusivgestein) | péridotite (roche intrusive)     |
|15103022 | nephelinitischer Syenit | syénite néphélinique     |
|15103023 | Essexit | essexite     |
|15103024 | Granophyr | granophyre     |
|15103026 | Ganggestein, undifferenziert | roche filonienne, indifférenciée     |
|15103027 | Mikrogranit | microgranite     |
|15103028 | Rhyolithporphyr | porphyre rhyolitique     |
|15103029 | Pegmatit | pegmatite     |
|15103030 | Aplit | aplite     |
|15103031 | Mikrodiorit | microdiorite     |
|15103032 | Mikrogabbro | microgabbro     |
|15103033 | Lamprophyr | lamprophyre     |
|15103034 | Pikrit (Intrusivgestein) | picrite (roche intrusive)     |
|15103035 | Dolerit | dolérite     |
|15103037 | Extrusivgestein, undifferenziert | roche extrusive, indifférenciée     |
|15103039 | Ergussgestein, undifferenziert | roche effusive, indifférenciée     |
|15103040 | Alkalirhyolith | rhyolite alcaline     |
|15103041 | Rhyolith | rhyolite     |
|15103042 | Rhyodazit | rhyodacite     |
|15103043 | Dazit | dacite     |
|15103044 | Quarzandesit | andésite quartzique     |
|15103045 | Andesit | andésite     |
|15103046 | Alkalitrachyt | trachite alcaline     |
|15103047 | Trachyt | trachite     |
|15103048 | Basalt | basalte     |
|15103049 | Pikrit (Effusiva) | picrite (roche effusive)     |
|15103050 | Phonolith | phonolite     |
|15103051 | Karbonatit | carbonatite     |
|15103053 | pyroklastisches Gestein, undifferenziert (vulkanischer Tuff, &gt; 75 % pyroklast. Komp.) | roche pyroclastique, indifférenciée (tuf volcanique, &gt; 75 % comp. pyrocl.)     |
|15103054 | Ignimbrit | ignimbrite     |
|15103055 | Pyroklastische Brekzie | brèche pyroclastique     |
|15103056 | Lapillituff | lapilli     |
|15103057 | Kristalltuff | tuff à cristaux     |
|15103058 | Aschentuff | cendres volcaniques     |
|15103060 | Tuffit, undifferenziert (pyroklast. und nicht vulk. Sedimente, 75-25 % pyroklast. Komp.) | roche volcano-sédimentaire, indifférenciée (tuffite 75-25 % comp. pyrocl.)     |
|15103061 | tuffitische Brekzie | brèche tuffitique     |
|15103062 | tuffitisches Konglomerat | poudingue tuffitique     |
|15103063 | tuffitischer Sandstein | grès tuffitique     |
|15103064 | tuffitischer Siltstein | siltite tuffitique     |
|15103065 | tuffitischer Tonstein | argilite tuffitique     |
|15103066 | Bentonit | bentonite     |
|15103067 | saures Ganggestein | roche filonienne acide     |
|15103068 | basisches Ganggestein | roche filonienne basique     |
|15103069 | Basisches Gestein | roche basique     |
|15103070 | Ultrabasisches Gestein | roche ultrabasique     |
|15104001 | Metamorphit | roche métamorphique     |
|15104002 | Gestein der Störungszone | roche liée à une zone de déformation     |
|15104003 | Gestein der Störungszone, undifferenziert | roche liée à une zone de déformation, indifférenciée     |
|15104005 | Kakirit, undifferenziert | kakirite, indifférenciée     |
|15104006 | Gesteinsmehl | roche pulvérisée     |
|15104007 | Kluftletten | argile de faille     |
|15104008 | tektonische Brekzie (kohäsionslos) | brèche de faille     |
|15104010 | Kataklasit, undifferenziert | cataclasite, indifférenciée     |
|15104011 | Rauwacke (Kataklasit) | rauwacke (roche cataclastique)     |
|15104012 | tektonische Dolomitbrekzie | brèche tectonique dolomitique     |
|15104013 | tektonische Brekzie (mit Kohäsion) | brèche tectonique     |
|15104014 | Protokataklasit | protocataclasite     |
|15104015 | (Meso)Kataklasit | (méso)cataclasite     |
|15104016 | Ultrakataklasit | ultracataclasite     |
|15104018 | Mylonit, undifferenziert | mylonite, indifférenciée     |
|15104019 | Protomylonit | protomylonite     |
|15104020 | Mylonit | (méso)mylonite     |
|15104021 | Ultramylonit | ultramylonite     |
|15104023 | Phyllonit | phyllonite     |
|15104025 | Pseudotachylit | pseudotachylite     |
|15104027 | Gestein der Regional- und Kontaktmetamorphose, undifferenziert | roche du métamorphisme régional et du contact, indifférenciée     |
|15104029 | Phyllit | phyllite     |
|15104031 | Schiefer, undifferenziert | schiste, indifférencié     |
|15104032 | Tonschiefer (Schiefer) | ardoise, schiste ardoisier     |
|15104033 | Serizitschiefer | séricitoschiste     |
|15104034 | Chloritschiefer | chloritoschiste     |
|15104035 | Glimmerschiefer | micaschiste     |
|15104036 | Glaukophanschiefer | schiste à glaucophane     |
|15104037 | Kalkschiefer | calcschiste     |
|15104038 | Prasinit | prasinite     |
|15104039 | Talkschiefer | talcschiste     |
|15104041 | Gneis, undifferenziert | gneiss, indifférencié     |
|15104042 | Augengneis | gneiss oeillé     |
|15104043 | Bändergneis | gneiss rubané     |
|15104044 | Adergneis | gneiss veiné     |
|15104045 | Zweiglimmergneis | gneiss à deux micas     |
|15104046 | agmatischer Gneis | gneiss agmatique     |
|15104047 | Leptinit | leptynite     |
|15104048 | Paragneis | paragneiss     |
|15104049 | Orthogneis | orthogneiss     |
|15104050 | Stronalit | stronalite     |
|15104051 | Kinzigit | kinzigite     |
|15104053 | Fels, undifferenziert | roche à texture granoblastique, indifférenciée     |
|15104054 | Kalksilikatfels | roche à calcsilicates     |
|15104055 | Marmor (Fels) | marbre (texture granoblastique)     |
|15104056 | Karbonat- und Silikat führendes Gestein | roche à carbonates et silicates     |
|15104057 | silikatreicher Marmor | cipolin     |
|15104058 | Granulit | granulite     |
|15104059 | Rodingit | rodingite     |
|15104060 | Amphibolit | amphibolite     |
|15104061 | Bänderamphibolit | amphibolite rubanée     |
|15104062 | Schollenamphibolit | amphibolite à blocs     |
|15104063 | Amphibolitgneis | gneiss amphibolitique     |
|15104064 | Eklogit | éclogite     |
|15104065 | Peridotit (Metamorphit) | péridotite (roche métamophique)     |
|15104067 | Hornfels | hornfels     |
|15104069 | Metasomatit, undifferenziert | métasomatite, indifférenciée     |
|15104070 | Skarn | skarn     |
|15104071 | Greisen | greisen     |
|15104072 | Gneis mit Feldspatblasten | gneiss à blastes de feldspath     |
|15104074 | Anatexit, undifferenziert | anatexite, indifférenciée     |
|15104075 | Migmatit | migmatite     |
|15104076 | Metatexit mit Fleckentextur | métatexite à structure tachetée     |
|15104077 | Metatexit mit stromatitischer Textur | métatexite à structure stromatitique     |
|15104078 | Metatexit mit Netztextur | métatexite à structure réticulée     |
|15104079 | Diatexit mit nebulitischer Textur | diatexite à structure nébulitique     |
|15104080 | Diatexit mit Schlierentextur | diatexite à structure artéritique (Schlieren)     |
|15104081 | Diatexit mit Schollentextur | diatexite à enclaves (Schollen)     |
|15104084 | monomineralischer Metamorphit, undifferenziert | roche métamorphique monominérale, indifférenciée     |
|15104085 | Biotitit | biotitite     |
|15104086 | Hornblenditit | hornblendite     |
|15104087 | Albitit | albitite     |
|15104088 | Pyroxenit (monomineralischer Metamorphit) | pyroxénite (roche métamorphique monominérale)     |
|15104089 | Chloritit | chloritite     |
|15104090 | Serpentinit | serpentinite     |
|15104091 | Quarzit (monomineralischer Metamorphit) | quartzite (roche métamorphique monominérale)     |
|15104092 | Metamorphit (Protolith erkennbar) | roche métamorphique (protolithe reconnaissable)     |
|15104093 | Metamorphit (sedimentärer Protolith erkennbar) | roche métamorphique (protolithe sédimentaire reconnaissable)     |
|15104095 | Metamorphit (magmatischer Protolith erkennbar) | roche métamorphique (protolithe magmatique reconnaissable)     |
|15104096 | Quarzschiefer | quartzschiste     |
|15104097 | Granat-Glimmerschiefer | micaschiste à grenat     |
|15104098 | Grünschiefer | schiste vert     |
|15104099 | Ophikalzit | ophicalcite     |
|15104201 | Metasediment | métasediment     |
|15104202 | Metapsephit | métaconglomérat     |
|15104203 | Metabrekzie | métabrèche     |
|15104204 | Metakonglomerat | métapoudingue     |
|15104205 | Metasandstein | métagrès     |
|15104206 | Quarzit (sedimentärer Protolith) | quartzite (protolithe sédimentaire)     |
|15104207 | Metapsammit | méta-arénite     |
|15104208 | Metaarkose | méta-arkose     |
|15104209 | Metagrauwacke | métagrauwacke     |
|15104210 | Geröll führender Metasandstein | métagrès à galets     |
|15104211 | Metapelit | métapélite     |
|15104212 | Metasiltstein | métasiltite     |
|15104213 | Tonschiefer (sedimentärer Protolith) | méta-argilite (protolithe sédimentaire)     |
|15104214 | Metamergel | métamarne     |
|15104215 | Marmor (sedimentärer Protolith) | marbre (protolithe sédimentaire)     |
|15104216 | dolomitischer Marmor | marbre dolomitique     |
|15104217 | Metaradiolarit | métaradiolarite     |
|15104218 | Metakarbonat | métaroche carbonatée     |
|15104401 | Metamagmatit | métamagmatite     |
|15104402 | metamorph überprägtes Intrusivgestein | métaroche intrusive     |
|15104403 | Metaplutonit | métaroche plutonique     |
|15104404 | Metaalkalogranit | métagranite alcalin     |
|15104405 | Metagranit | métagranite     |
|15104406 | Metagranodiorit | métagranodiorite     |
|15104407 | Metaquarzdiorit | métadiorite quartzique     |
|15104408 | Metatonalit | métatonalite     |
|15104409 | Metadiorit | métadiorite     |
|15104410 | Metasyenit | métasyénite     |
|15104411 | Metaalkalisyenit | métasyénite alcaline     |
|15104412 | Metaquarzgabbro | métagabbro quartzique     |
|15104413 | Metagabbro | métagabbro     |
|15104414 | Metanorit | métanorite     |
|15104415 | Metamonzodiorit | métamonzodiorite     |
|15104416 | Metamonzogabbro | métamonzogabbro     |
|15104417 | Metamonzonit | métamonzonite     |
|15104418 | Metapyroxenit | métapyroxénite     |
|15104419 | Metaperidotit | métapéridotite     |
|15104420 | nephelinitischer Metasyenit | métasyénite néphélinique     |
|15104421 | Metaessexit | méta-essexite     |
|15104422 | Metagranophyr | métagranophyre     |
|15104423 | Metaganggestein | métaroche filonienne     |
|15104424 | Metamikrogranit | métamicrogranite     |
|15104426 | Metapegmatit | métapegmatite     |
|15104427 | Metaaplit | méta-aplite     |
|15104428 | Metamikrodiorit | métamicrodiorite     |
|15104429 | Metamikrogabbro | métamicrogabbro     |
|15104430 | Metalamprophyr | métalamprophyre     |
|15104431 | Metapikrit | métapicrite     |
|15104432 | Metadolerit | métadolérite     |
|15104433 | Metaalkalirhyolith | métarhyolite alcaline     |
|15104434 | Metarhyolith | métarhyolite     |
|15104435 | Metarhyodazit | métarhyodacite     |
|15104436 | Metadazit | métadacite     |
|15104437 | Metaquarzandesit | méta-andésite quartzique     |
|15104438 | Metaandesit | méta-andésite     |
|15104439 | Metaalkalitrachyt | métatrachite alcaline     |
|15104440 | Metatrachyt | métatrachite     |
|15104441 | Metabasalt | métabasalte     |
|15104443 | Metaphonolit | métaphonolite     |
|15104444 | metamorph überprägtes pyroklastisches Gestein | métaroche pyroclastique     |
|15104445 | Metaignimbrit | méta-ignimbrite     |
|15104446 | Metavulkanit | métavulcanite     |
|15104447 | ultramafisches Gestein | roche ultramafique     |
|15104448 | tektonische Kalkbrekzie | brèche tectonique calcaire     |
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |


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
|999997 | unbekannt | inconnu     |
|999998 | nicht anwendbar | non applicable     |


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
|14509001 | mit Löss | avec loess     |
|14509002 | mit Lösslehm | avec loess argileux     |
|14509003 | mit Seekreide | avec craie lacustre     |
|14509004 | mit Blöcken | avec blocs     |
|14509005 | mit alpinen Geröllen | avec galets alpins     |
|14509006 | mit Block- und Geschiebestreu | parsemé de blocs     |
|14509007 | mit Blockschutt vermischt | mélangé à des dépôts d&#39;éboulement     |
|14509008 | mit Hangschutt vermischt | mélangé à des éboulis     |
|14509009 | mit Verwitterungsschutt vermischt | mélangé à des résidus d&#39;altération     |
|14509010 | mit Torf | avec tourbe     |
|14509011 | mit jurassischen Geröllen | avec galets jurassiens     |
|14509012 | mit Geröllen aus Vogesen / Schwarzwald | avec galets des Vosges / de la Forêt Noire     |
|14509013 | mit Schieferkohle | mit Schieferkohle     |


## Annexe  GC_COMPOSIT {#gc-composit}
Composition de la roche meuble

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14508001 | tonig | argileux     |
|14508002 | lehmig | limoneux     |
|14508003 | siltig | silteux     |
|14508004 | sandig | sableux     |
|14508005 | kiesig | graveleux     |
|14508006 | geröllreich | riche en galets     |
|14508007 | torfig | tourbeux     |


## Annexe  GC_CHARCAT {#gc-charcat}
Structure sédimentaire

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14511001 | fossil | fossile     |
|14511002 | rezent | récent     |
|14511003 | verwittert | altéré     |
|14511004 | verfestigt (durch Überlast), konsolidiert | consolidé (par surcharge)     |
|14511005 | verkittet (zementiert) | cimenté     |
|14511006 | verschwemmt | délavé     |
|14511007 | sumpfig | marécageux     |
|14511008 | umgelagert | remanié     |
|14511009 | abgebaut | exploité     |
|14511010 | drainiert | drainé     |
|14511011 | künstlich bewässert (Wässermatten) | inondé artificiellement (prairies irriguées)     |


## Annexe  GC_SYSTEM {#gc-system}
Groupe de fossile

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12903001 | Vertebraten | vertébrés     |
|12903002 | Ostrakoden | ostracodes     |
|12903003 | Gastropoden | gastéropodes     |
|12903004 | Foraminiferen | foraminifères     |
|12903005 | Algen | algues     |
|12903006 | Blätter | feuilles     |
|12903007 | Gräser | graminées     |
|12903008 | Holz | bois     |
|12903009 | Ammoniten | ammonites     |
|12903010 | Schwämme | éponges     |
|12903011 | Korallen | coraux     |
|12903012 | Brachiopoden | brachiopodes     |
|12903013 | Mollusken | mollusques     |
|12903014 | Cephalopoden | céphalopodes     |
|12903015 | Bivalven | bivalves     |
|12903016 | Echinodermen | échinodermes     |
|12903017 | Fische | poissons     |
|12903018 | Reptilien | reptiles     |
|12903019 | Säugetiere | mammifères     |
|12903021 | Palynomorphe | palynomorphes     |





## Annexe  GeolCodes changés 2022-2024 


### Geolcodes ajoutés 


| Geolcode | Deutsch |
|----------|--------|
| 15309183 | Bosco-Zone |
| 15309184 | Bombogno-Zone |
| 15309185 | Maggia-Decke |
| 15309186 | Sambuco-Decke |
| 15309187 | San-Giorgio-Schuppe |
| 15309188 | Leventina-Lucomagno-Decke |
| 15309189 | Simano-Decke |
| 15309190 | Cima-Lunga-Decke |
| 15309191 | Adula-Decke |
| 15309192 | Gruf-Komplex |
| 15309193 | Soja-Decke |
| 15309194 | Garzott-Schuppen |
| 15309195 | Piz-Terri-Lunschania-Decke |
| 15309196 | Terri-Schuppe |
| 15309197 | Güida-Alpettas-Schuppen |
| 15309198 | Darlun-Schuppe |
| 15309199 | Penninikum |
| 15309200 | Unterpenninikum |
| 15309201 | Niesen-Decke |
| 15309202 | Infraniesen-Melange |
| 15309203 | Voirons-Decke |
| 15309204 | Gurnigel-Decke |
| 15309205 | Schlieren-Decke |
| 15309206 | Wägital-Decke |
| 15309207 | Üntschen-Decke |
| 15309208 | Sigiswang-Decke |
| 15309209 | Triesenberg-Schuppenkomplex |
| 15309210 | Oberstdorf-Decke |
| 15309211 | Sion-Courmayeur-Decke |
| 15309212 | Rosswald-Schuppe |
| 15309213 | Ferret-Schuppe |
| 15309214 | Moûtiers-Schuppe |
| 15309215 | Roignais-Versoyen-Schuppe |
| 15309216 | Pierre-Avoi-Schuppe |
| 15309217 | Petit-St-Bernard-Schuppe |
| 15309218 | Chiavenna-Decke |
| 15309219 | Vals-Schuppen |
| 15309220 | Aul-Decke |
| 15309221 | Grava-Decke |
| 15309222 | Tomül-Decke |
| 15309223 | Forbesch-Schuppe |
| 15309224 | Roz-Champatsch-Melange |
| 15309225 | Ramosch-Zone |
| 15309226 | Pfunds-Decke |
| 15309227 | Mittelpenninikum |
| 15309228 | Zone Submédiane |
| 15309229 | Klippen-Decke |
| 15309230 | Préalpes Médianes Plastiques |
| 15309231 | Préalpes Médianes Rigides |
| 15309232 | Mythen-Roggenegg-Schuppe |
| 15309233 | Obere Rotenflue-Schuppe |
| 15309234 | Stäglerenegg-Brünnelistock-Schuppen  |
| 15309235 | Brekzien-Decke |
| 15309236 | Zone Houillère |
| 15309237 | Zone Houillère externe |
| 15309238 | Zone Houillère interne |
| 15309239 | Visperterminen-Schuppe |
| 15309240 | Untere Stalden-Schuppe |
| 15309241 | Gälmji-Zone |
| 15309242 | Ruginenta-Decke |
| 15309243 | Ruitor-Decke |
| 15309244 | Obere Stalden-Decke |
| 15309245 | Berisal-Decke |
| 15309246 | Camughera-Decke |
| 15309247 | Siviez-Mischabel-Decke |
| 15309248 | Mont-Fort-Decke |
| 15309249 | Portjengrat-Decke |
| 15309250 | Stockhorn-Decke |
| 15309251 | Monte-Rosa-Decke |
| 15309252 | Tambo-Decke |
| 15309253 | Suretta-Decke |
| 15309254 | Schams-Deckenkomplex |
| 15309255 | Gelbhorn-Decke |
| 15309256 | Tschera-Kalkberg-Decke |
| 15309257 | Knorren-Melange |
| 15309258 | Martegnas-Melange |
| 15309259 | Areua-Bruschghorn-Melange |
| 15309260 | Falknis-Decke |
| 15309261 | Tschingel-Schuppe |
| 15309262 | Grauspitz-Schuppe |
| 15309263 | Glegghorn-Schuppe |
| 15309264 | Sulzfluh-Decke |
| 15309265 | Fimber-Zone |
| 15309266 | Tasna-Decke |
| 15309267 | Oberpenninikum |
| 15309268 | Gets-Decke |
| 15309269 | Simmen-Decke |
| 15309270 | Dranses-Decke |
| 15309271 | Saane-Decke |
| 15309272 | Antrona-Decke |
| 15309273 | Zermatt-Saas-Fee-Decke |
| 15309274 | Theodulgletscher-Schuppe |
| 15309275 | Mont-Emilius-Decke |
| 15309276 | Etirol-Levaz-Schuppe |
| 15309277 | Châtillon-St-Vincent-Schuppen |
| 15309278 | Châtillon-Schuppe |
| 15309279 | Pontey-Schuppe |
| 15309280 | Grun-Schuppe |
| 15309281 | Vollon-Schuppe |
| 15309282 | Gornergrat-Decke |
| 15309283 | Cimes-Blanches-Decke |
| 15309284 | Frilihorn-Decke |
| 15309285 | Tsaté-Decke |
| 15309286 | Avers-Decke |
| 15309287 | Malenco-Forno-Lizun-Decke |
| 15309288 | Platta-Decke |
| 15309289 | Arosa-Zone |
| 15309290 | Haupterhorn-Scholle |
| 15309291 | Weissfluh-Scholle |
| 15309292 | Gotschnawang-Scholle |
| 15309293 | Dros-Scholle |
| 15309294 | Totalp-Ophiolithkomplex |
| 15309295 | Salassikum |
| 15309296 | Mont-Mary-Decke |
| 15309297 | Untere Einheit der Mont-Mary-Decke |
| 15309298 | Obere Einheit der Mont-Mary-Decke |
| 15309299 | Roisan-Cignana-Scherzone |
| 15309300 | Dent-Blanche-Decke |
| 15309301 | Arolla-Einheit |
| 15309302 | Valpelline-Einheit |
| 15309303 | Sesia-Decke |
| 15309304 | Seconda Zona Dioritico-Kinzigitica |
| 15309305 | Gneiss-minuti-Einheit |
| 15309306 | Micascisti-eclogitici-Einheit |
| 15309307 | Margna-Decke |
| 15309308 | Forcellina-Schuppe |
| 15309309 | Sella-Decke |
| 15309310 | Ostalpin |
| 15309311 | Unterostalpin |
| 15309312 | Rothorn-Schwarzhorn-Deckenkomplex |
| 15309313 | Rothorn-Decke |
| 15309314 | Tschirpen-Decke |
| 15309315 | Schafläger-Decke |
| 15309316 | Dorfberg-Decke |
| 15309317 | Grüenhorn-Casanna-Schuppenkomplex |
| 15309318 | Grüenhorn-Schuppe |
| 15309319 | Casanna-Schuppe |
| 15309320 | Stammerspitz-Schuppe |
| 15309321 | Bernina-Deckenkomplex |
| 15309322 | Ela-Decke |
| 15309323 | Bernina-Decke |
| 15309324 | Müsella-Schuppe |
| 15309325 | Mezzaun-Schuppe |
| 15309326 | Madulain-Schuppen |
| 15309327 | Schlattain-Clavadatsch-Padella-Schuppen |
| 15309328 | Julier-Decke |
| 15309329 | Err-Deckenkomplex |
| 15309330 | Murtiröl-Schuppe |
| 15309331 | Err-Decke |
| 15309332 | Carungas-Schuppe |
| 15309333 | Corvatsch-Schuppe |
| 15309334 | Chastelets-Schuppe |
| 15309335 | Bardella-Roccabella-Schuppen |
| 15309336 | Oberostalpin |
| 15309337 | Campo-Deckenkomplex |
| 15309338 | Masuccio-Decke |
| 15309339 | Campo-Decke |
| 15309340 | Grosina-Decke |
| 15309341 | Laas-Decke |
| 15309342 | Vinschgau-Scherzone |
| 15309343 | Languard-Decke |
| 15309344 | Tonale-Decke |
| 15309345 | Ulten-Einheit |
| 15309346 | Krabachjoch-Decke |
| 15309347 | Inntal-Decke |
| 15309348 | Roggenstock-Mördergruebi-Decke |
| 15309349 | Lechtal-Decke |
| 15309350 | Madrisa-Schuppe |
| 15309351 | Schesaplana-Schuppe |
| 15309352 | Gorvion-Schuppe |
| 15309353 | Augstenberg-Schuppe |
| 15309354 | Ochsenkopf-Schuppe |
| 15309355 | Heubühl-Schuppe |
| 15309356 | Drei-Schwestern-Schuppe |
| 15309357 | Allgäu-Decke |
| 15309358 | Cenoman-Randschuppe |
| 15309359 | Schiahorn-Decke |
| 15309360 | Silvretta-Decke |
| 15309361 | S-chanf-Schuppen |
| 15309362 | Phyllitgneiszone |
| 15309363 | Ötztal-Deckenkomplex |
| 15309364 | Matsch-Decke |
| 15309365 | Umbrail-Terza-Schuppenkomplex |
| 15309366 | Umbrail-Chavalatsch-Schuppen |
| 15309367 | Terza-Schuppe |
| 15309368 | Quattervals-Decke |
| 15309369 | S-charl-Sesvenna-Decke |
| 15309370 | Tavrü-Schuppe |
| 15309371 | Ortler-Decke |
| 15309372 | Südalpin |
| 15309373 | Canavese-Zone |
| 15309374 | Ivrea-Ceneri-Komplex |
| 15309375 | Ivrea-Zone |
| 15309376 | Strona-Ceneri-Zone (Ivrea-Ceneri-Anteil) |
| 15309377 | Milano-Belt |
| 15309378 | Externe Giudicarie-Zone |
| 15309379 | Untere Orobische Schuppen |
| 15309380 | Interne Giudicarie-Zone |
| 15309381 | Obere Orobische Decke |
| 15309382 | Val-Colla-Zone |
| 15309383 | Strona-Ceneri-Zone (Oberer Orobischer Anteil) |
| 15309384 | Varesotto-Schuppen |
| 15309385 | Strona-Ceneri-Zone (undifferenziert) |
| 15309386 | Känozoische magmatische Gesteine |
| 15309387 | Vulkanische Serie des Hegaus |
| 15309388 | Periadriatische magmatische Provinz |
| 15309389 | Vulkanische Serie von Biella |
| 15309390 | Subvulkanischer Körper vom Colle Gallo |
| 15309391 | Subvulkanischer Körper von Gandino |
| 15309392 | Bregaglia-Intrusionskörper |
| 15309393 | Novate-Intrusionskörper |
| 15309394 | Adamello-Batholith |
| 15501001 | Diverse |
| 15601001 | Laco gerichtete Linie |
| 15601002 | Laco Arbeitsfortschritte |
| 15602001 | Gesteinsbruchstück undifferenziert |
| 15602002 | kieselige Gesteine (Quarzit, Quarz (Mineralisch), Radiolarit, Kieselkalk, Quarzsandstein, Hornstein) |
| 15602003 | Sedimentgestein undifferenziert |
| 15602004 | Tonstein |
| 15602005 | Kalkstein |
| 15602006 | Dolomitstein |
| 15602007 | Kristallingestein undifferenziert |
| 15602008 | Vulkanit |
| 15602009 | Metamorphit |
| 15602010 | Mergelstein |
| 15733001 | alkalisch |
| 15733002 | kalkalkalisch |
| 15733003 | tholeiitisch |
| 15801001 | Sackungsgebiet |
| 15801002 | Gebiet mit Hakenwurf |
| 15801003 | Rutschgebiet |
| 15801004 | Gebiet mit Solifluktion |
| 20001001 | Gesteinsbruchstück undifferenziert |
| 20001002 | Sedimentgestein undifferenziert |
| 20001003 | Tonstein |
| 20001004 | Kalkstein |
| 20001005 | Dolomitstein |
| 20001006 | Kristallingestein undifferenziert |
| 20001007 | Vulkanit |
| 20001008 | Metamorphit |
| 20001009 | Quarzit |
| 20001010 | pyroklastische Komponenten |
| 20001011 | Quarz |
| 20001012 | Feldspat |
| 20001013 | Glaukonit |
| 20001014 | Glimmer |
| 20001015 | intraformationelle Gerölle |
| 20001016 | Kalkkonkretionen |
| 20001017 | Sideritkonkretionen |
| 20001018 | Silexkonkretionen |
| 20001019 | biogene Komponenten |
| 20001020 | terrigener Detritus |
| 20001021 | Phosphorit |
| 20001022 | Mergelstein |
| 20001023 | Kohle |
| 20001024 | Bitumen |
| 20001025 | Evaporit |
| 20001026 | Eisenmineralien |
| 20101001 | massig |
| 20101002 | gebankt |
| 20101003 | dickbankig (&gt;30cm) |
| 20101004 | dünnbankig (1-10cm) |
| 20101005 | blätterig |
| 20101006 | knauerig |
| 20101007 | knollig |
| 20101008 | linsenförmig |
| 20201001 | texturlos |
| 20201002 | geschichtet |
| 20201003 | schräg-/kreuzgeschichtet |
| 20201004 | laminiert |
| 20201005 | normal gradiert |
| 20201006 | invers gradiert |
| 20201007 | bioturbiert |
| 20201008 | stromatolitisch |
| 20301001 | monomikt |
| 20301002 | polymikt |
| 20301003 | mikritisch |
| 20301004 | spätig |
| 20301005 | bioklastisch |
| 20301007 | onkolithisch |
| 20301008 | oolithisch |
| 20301009 | pelitisch |
| 20301010 | pisolithisch |
| 20401001 | Aktinolith |
| 20401002 | Albit |
| 20401003 | Allanit |
| 20401004 | Almandin |
| 20401005 | Amphibol |
| 20401006 | Andalusit |
| 20401007 | Ankerit |
| 20401008 | Anorthit |
| 20401009 | Antigorit |
| 20401010 | Biotit |
| 20401011 | Kalzit |
| 20401012 | Karbonatmineral |
| 20401013 | Karpholith |
| 20401014 | Chlorit |
| 20401015 | Chloritoid |
| 20401016 | Klinozoisit |
| 20401017 | Coesit |
| 20401018 | Cordierit |
| 20401019 | Diopsid |
| 20401020 | Disthen |
| 20401021 | Dolomit |
| 20401022 | Epidot |
| 20401023 | Feldspat |
| 20401024 | Alkalifeldspat |
| 20401026 | Glaukophan |
| 20401027 | Graphit |
| 20401028 | Granat |
| 20401029 | Hornblende |
| 20401030 | Lawsonit |
| 20401031 | Magnetit |
| 20401032 | Glimmer |
| 20401033 | Hellglimmer |
| 20401034 | Mikroklin |
| 20401035 | Muskovit |
| 20401036 | Olivin |
| 20401037 | Omphazit |
| 20401038 | Orthoklas |
| 20401039 | Paragonit |
| 20401040 | Phlogopit |
| 20401041 | Plagioklas |
| 20401042 | Prehnit |
| 20401043 | Pyrit |
| 20401044 | Pyrop |
| 20401045 | Pyrophyllit |
| 20401046 | Pyroxen |
| 20401047 | Quarz |
| 20401049 | Serpentin |
| 20401050 | Alumosilikat |
| 20401051 | Sillimanit |
| 20401052 | Staurolith |
| 20401053 | Stilpnomelan |
| 20401054 | Talk |
| 20401055 | Zoisit |
| 20401056 | Adular |
| 20401057 | Aegirin |
| 20401058 | Aegirin-Augit |
| 20401059 | Andesin |
| 20401060 | Anhydrit |
| 20401061 | Annit |
| 20401062 | Aragonit |
| 20401063 | Augit |
| 20401064 | Chrysotil |
| 20401065 | Grossular |
| 20401066 | Jadeit |
| 20401067 | Margarit |
| 20401068 | Oligoklas |
| 20401069 | Orthopyroxen |
| 20401070 | Klinopyroxen |
| 20401071 | Phengit |
| 20401072 | Pumpellyit |
| 20401073 | Sanidin |
| 20401074 | Sapphirin |
| 20401075 | Spessartin |
| 20401076 | Spinell |
| 20401077 | Titanit |
| 20401078 | Tremolit |
| 20401079 | Turmalin |
| 20401080 | Forsterit |
| 20401081 | Fayalit |
| 20401082 | Enstatit |
| 20401083 | Zeolith |
| 20401084 | Serizit |
| 20401085 | Fuchsit |
| 20501001 | massig |
| 20501002 | gebändert |
| 20501003 | augig |
| 20501004 | mit Schollen |
| 20501005 | schiefrig |
| 20501006 | phyllitisch |
| 20501007 | laminiert |
| 20501008 | lagig |
| 20501009 | plattig |
| 20501010 | gebankt |
| 20501011 | gefältelt |
| 20501012 | geadert |
| 20501013 | schlierig |
| 20501014 | linsig |
| 20501015 | flaserig |
| 20501016 | agmatitisch (migmatitisch) |
| 20501017 | brekziös |
| 20601001 | Name und Begrenzung harmonisiert |
| 20601002 | Untergrenze muss noch revidiert werden |
| 20601003 | Obergrenze muss noch revidiert werden |
| 20601004 | Unter- und Obergrenzen müssen noch revidiert werden |
| 20601005 | Interne Gliederung zu revidieren |
| 20601006 | Unsichere lithostratigraphische Attribuierung |




### Geolcodes effacés 

 Aucun geolcode supprimé 


### Geolcodes changés 

| Geolcode | 2022 | 2024  |
|----------|-------------|------------|
| 15200093 | Vallorbe-Formation | Vallorbe-Member |
| 15200220 | Spät- bis postvariszische Intrusiva des Schwarzwaldes | Spät- bis postvariszische Intrusiva der Nordschweiz |
| 15200221 | Permo-Karbon der NW-Schweiz | Permo-Karbon der Nordschweiz |
| 15200230 | Frühvariszische Intrusiva des Schwarzwaldes | Frühvariszische Intrusiva der Nordschweiz |
| 15200243 | Prä- und frühvariszische Sedimente und Vulkanite des Schwarzwaldes | Prä- und frühvariszische Sedimente und Vulkanite der Nordschweiz |
| 15200245 | Prävariszisches polyzyklisches Grundgebirge des Schwarzwaldes | Prävariszisches polyzyklisches Grundgebirge der Nordschweiz |
| 15200246 | Orthogneise des Schwarzwaldes | Prävariszische Orthogneise der Nordschweiz |
| 15200250 | Migmatite des Schwarzwaldes | Prävariszische Migmatite der Nordschweiz |
| 15200253 | Grüngesteine des Schwarzwaldes | Prävariszische Grüngesteine der Nordschweiz |
| 15201050 | Gondiswil-Interglazial (Letztes Integlazial) | Gondiswil-Interglazial (Letztes Interglazial) |
| 15202149 | Chartegg-Member | Chartegg-Formation |
| 15202283 | Sardona-Quarzit | Sardona-Member |
| 15202542 | Elm- und Matt-Formation: schiefriger Tonstein | Nordhelvetische Flysch-Gruppe, vorw. schiefriger Tonstein |
| 15202588 | Stad-Formation, &#34;Jüngerer Quarzsandstein&#34; | Stad-Formation, «Jüngerer Quarzsandstein» |
| 15202589 | Einsiedeln-Member, &#34;Älterer Quarzsandstein&#34; | Einsiedeln-Member, «Älterer Quarzsandstein» |
| 15202591 | Wängen-Kalk, &#34;Lithothamnienkalk&#34;-Fazies | Wängen-Kalk, Lithothamnienkalk-Fazies |
| 15202592 | Einsiedeln-Member, &#34;Alveolinenkalk&#34;-Fazies | Einsiedeln-Member, Alveolinenkalk-Fazies |
| 15202596 | Euthal-Formation und Steinbach-Member, undiff. | Einsiedeln- und Steinibach-Member, undifferenziert |
| 15203224 | Tasna-Granit | Plattamala-Granit |
| 15203227 | Garde-de-Bordon-Serie | Garde-de-Bordon-Formation |
| 15203228 | Fêta-d&#39;Août-Flysch | Fêta-d&#39;Août-Formation |
| 15203466 | Amphibolit des Ergischhorn-Ensembles | Ergischhorn-Komplex: Amphibolit |
| 15203499 | Radiolarit der Platta-Decke | Falotta-Radiolarit |



