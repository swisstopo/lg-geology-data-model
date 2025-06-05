
# Datenmodell Geologie, Revision 4.1.0 #





![Auszug aus Geocover und Beispiel für die Darstellung](geocover.png "Figure alt text")





\pagebreak





## Thema ROCK_BODIES

### Klasse Unconsolidated_Deposits_PT (Runc){#unconsolidated-deposits-pt}
Die Klasse [Unconsolidated_Deposits_PT](#unconsolidated-deposits-pt) umfasst einzelne Gesteine (Korngrösse: Steine bis Blöcke), die durch gravitative, glaziale oder anthropogene Transportprozesse an ihren heutigen Ort gelangten, respektive sich an Ort und Stelle durch Verwitterung des umliegenden Gesteins gebildet haben.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**STATUS**                 | [CD](#unconsolidated-deposits-pt-status)  | Zustand der Objektart. | [1]
**ROCK_TYPE**                 | [CD](#unconsolidated-deposits-pt-rock-type)  | Gesteinstyp. | [0..1]
**ROCK_SPE**                 | [CD](#unconsolidated-deposits-pt-rock-spe)  | Bezeichnung des Leitgesteins.. | [0..1]
**MAT_TYPE**                 | [ Tabelle ](#gc-litho-unco-cd)  | Materialbezeichnung (lithologische Einheit). | [0..1]
**ORIG_DESCR**                 | string                  | Originalbezeichnung gemäss der Legende der zugrundeliegenden geologischen Karte | [0..1]
**PROTECTED**                 | boolean                  | Geschützt: ja/nein | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14401001 | erratischer Block | Runc erratischer Block     |
|14401002 | Schwarm erratischer Blöcke | Runc Schwarm erratischer Blöcke     |
|14401003 | anthropogene Ansammlung von erratischen Blöcken | Runc anthropogene Ansammlung von erratischen Blöcken     |
|14401004 | Wanderblock | Runc Wanderblock     |
|14401005 | Geschiebe | Runc Geschiebe     |
|14401006 | Sturzblock | Runc Sturzblock     |
|14401007 | Lesesteinhaufen | Runc Lesesteinhaufen     |
|14401008 | Verwitterungsrückstände (Gerölle und/oder Konkretionen) | Runc Verwitterungsrückstände (Gerölle und/oder Konkretionen)     |




#### Attribut  STATUS {#unconsolidated-deposits-pt-status}
_Zustand der Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14402001 | versetzt | versetzt     |
|14402002 | zerstört | zerstört     |
|14402003 | in Situ | in Situ     |
|14402004 | umgelagert | umgelagert     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  ROCK_TYPE {#unconsolidated-deposits-pt-rock-type}
_Gesteinstyp_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14403001 | Kristallingestein | Kristallingestein     |
|14403002 | Sedimentgestein | Sedimentgestein     |
|14403003 | Basisches / Ultrabasisches Gestein | Basisches / Ultrabasisches Gestein     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  ROCK_SPE {#unconsolidated-deposits-pt-rock-spe}
_Bezeichnung des Leitgesteins._


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
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  MAT_TYPE
_Materialbezeichnung (lithologische Einheit)_

Siehe [GC_LITHO_UNCO_CD](#gc-litho-unco-cd) in der Anhang





#### Attribut  ORIG_DESCR
_Originalbezeichnung gemäss der Legende der zugrundeliegenden geologischen Karte_

_Datentyp :  string_





#### Attribut  PROTECTED
_Geschützt: ja/nein_

_Datentyp :  boolean_





### Klasse Unconsolidated_Deposits_PLG (Runc){#unconsolidated-deposits-plg}
Die Klasse [Unconsolidated_Deposits_PLG](#unconsolidated-deposits-plg) beinhaltet alle flächenhaft
ausgeschiedenen Lockergesteine.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**LITSTRAT**                 | [ Tabelle ](#gc-litstrat-unco-cd)  | Lithostratigraphische Einheit.. | [1]
**LITHO**                 | [ Tabelle ](#gc-litho-cd)  | Lithologische Beschreibung. | [1..3]
**CHRONO_T**                 | [ Tabelle ](#gc-chrono-cd)  | Chronostratigraphische Zuordnung der Obergrenze der Kartiereinheit (Top). | [1]
**CHRONO_B**                 | [ Tabelle ](#gc-chrono-cd)  | Chronostratigraphische Zuordnung der Untergrenze der Kartiereinheit (Basis). | [1]
**MAT_TYPE**                 | string                  | Materialbezeichnung (lithologische Einheit) | [0..3]
**BURIED_OUT**                 | boolean                  | Wurde das Lockergestein wieder verdeckt (ja/nein)? | [1]
**COMPOSIT**                 | [ Tabelle ](#gc-composit)  | Zusammensetzung des Lockergesteins. | [0..3]
**ADMIXTURE**                 | [ Tabelle ](#gc-admixture)  | Beimengung. | [0..2]
**STRUCTUR**                 | [CD](#unconsolidated-deposits-plg-structur)  | Textur des Lockergesteins. | [0..1]
**CHARACT**                 | [ Tabelle ](#gc-charcat)  | Spezifische Eigenschaft. | [0..3]
**MORPHOLO**                 | [CD](#unconsolidated-deposits-plg-morpholo)  | Morphologie der Lockergesteinseinheit. | [0..1]
**GLAC_TYPE**                 | [CD](#unconsolidated-deposits-plg-glac-type)  | Gletschertyp; Attribut nur für Moränen. | [0..1]
**REF_YEAR**                 | string                  | Zeitpunkt oder Zeitperiode. Zum Beispiel «1940 1943, Periode der Drainage» (muss präzisiert werden). | [0..1]
**THIN_COVER**                 | [CD](#unconsolidated-deposits-plg-thin-cover)  | Typ der geringmächtigen Lockermaterialbedeckung, wenn vorhanden.. | [0..1]
**ORIG_DESCR**                 | string                  | Originalbezeichnung gemäss der Legende der zugrunde liegenden geologischen Karte | [1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14517001 | Lockergestein | Runc Lockergestein     |




#### Attribut  LITSTRAT
_Lithostratigraphische Einheit._

Siehe [GC_LITSTRAT_UNCO_CD](#gc-litstrat-unco-cd) in der Anhang





#### Attribut  LITHO
_Lithologische Beschreibung_

Siehe [GC_LITHO_CD](#gc-litho-cd) in der Anhang





#### Attribut  CHRONO_T
_Chronostratigraphische Zuordnung der Obergrenze der Kartiereinheit (Top)_

Siehe [GC_CHRONO_CD](#gc-chrono-cd) in der Anhang





#### Attribut  CHRONO_B
_Chronostratigraphische Zuordnung der Untergrenze der Kartiereinheit (Basis)_

Siehe [GC_CHRONO_CD](#gc-chrono-cd) in der Anhang





#### Attribut  MAT_TYPE
_Materialbezeichnung (lithologische Einheit)_

_Datentyp :  string_





#### Attribut  BURIED_OUT
_Wurde das Lockergestein wieder verdeckt (ja/nein)?_

_Datentyp :  boolean_





#### Attribut  COMPOSIT
_Zusammensetzung des Lockergesteins_

Siehe [gc_composit](#gc-composit) in der Anhang





#### Attribut  ADMIXTURE
_Beimengung_

Siehe [gc_admixture](#gc-admixture) in der Anhang





#### Attribut  STRUCTUR {#unconsolidated-deposits-plg-structur}
_Textur des Lockergesteins_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14510001 | texturlos | texturlos     |
|14510002 | geschichtet | geschichtet     |
|14510003 | schräg-/kreuzgeschichtet | schräg-/kreuzgeschichtet     |
|14510004 | grossmassstäbliche Schrägschichtung (z.B. Deltaschichtung) | grossmassstäbliche Schrägschichtung (z.B. Deltaschichtung)     |
|14510005 | glaziale Überprägung (Glazitektonik) | glaziale Überprägung (Glazitektonik)     |
|14510006 | periglazial gestörte Schichtung (Diapir, Eiskeil, etc.) | periglazial gestörte Schichtung (Diapir, Eiskeil, etc.)     |
|14510007 | laminiert | laminiert     |
|14510008 | mit Warven | mit Warven     |
|14510009 | normal gradiert | normal gradiert     |
|14510010 | invers gradiert | invers gradiert     |
|14510011 | bioturbiert | bioturbiert     |
|14510012 | pedogen überprägt | pedogen überprägt     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  CHARACT
_Spezifische Eigenschaft_

Siehe [gc_charcat](#gc-charcat) in der Anhang





#### Attribut  MORPHOLO {#unconsolidated-deposits-plg-morpholo}
_Morphologie der Lockergesteinseinheit_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14512001 | Kegel / Fächer | Kegel / Fächer     |
|14512002 | Schleier | Schleier     |
|14512003 | Düne | Düne     |
|14512004 | Wall | Wall     |
|14512005 | Terrasse | Terrasse     |
|14512006 | Sander | Sander     |
|14512007 | Os | Os     |
|14512008 | Bastion | Bastion     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  GLAC_TYPE {#unconsolidated-deposits-plg-glac-type}
_Gletschertyp; Attribut nur für Moränen_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14513001 | Lokalgletscher | Lokalgletscher     |
|14513002 | grosse Tal- und Vorlandgletscher | grosse Tal- und Vorlandgletscher     |
|14513003 | Bündner Gletscher | Bündner Gletscher     |
|14513004 | Bodensee-Rheingletscher | Bodensee-Rheingletscher     |
|14513005 | Linth-Rheingletscher | Linth-Rheingletscher     |
|14513006 | Reussgletscher | Reussgletscher     |
|14513007 | Waldemme- und Entlegletscher | Waldemme- und Entlegletscher     |
|14513008 | Walliser Gletscher | Walliser Gletscher     |
|14513009 | Aaregletscher | Aaregletscher     |
|14513010 | Saanegletscher | Saanegletscher     |
|14513011 | Schlierengletscher | Schlierengletscher     |
|14513012 | Engelberger Gletscher | Engelberger Gletscher     |
|14513013 | Brünig-Aaregletscher | Brünig-Aaregletscher     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  REF_YEAR
_Zeitpunkt oder Zeitperiode. Zum Beispiel «1940 1943, Periode der Drainage» (muss präzisiert werden)._

_Datentyp :  string_





#### Attribut  THIN_COVER {#unconsolidated-deposits-plg-thin-cover}
_Typ der geringmächtigen Lockermaterialbedeckung, wenn vorhanden._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14515001 | geringmächtige Lockergesteinsbedeckung, undifferenziert | geringmächtige Lockergesteinsbedeckung, undifferenziert     |
|14515002 | geringmächtige Moränenbedeckung | geringmächtige Moränenbedeckung     |
|14515003 | geringmächtige Schotterbedeckung | geringmächtige Schotterbedeckung     |
|14515004 | geringmächtige Schwemmlehmbedeckung | geringmächtige Schwemmlehmbedeckung     |
|14515005 | geringmächtige Löss- oder Lösslehmbedeckung | geringmächtige Löss- oder Lösslehmbedeckung     |
|14515006 | tiefgründige Verwitterungsdecke | tiefgründige Verwitterungsdecke     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  ORIG_DESCR
_Originalbezeichnung gemäss der Legende der zugrunde liegenden geologischen Karte_

_Datentyp :  string_





### Klasse Bedrock_PLG (Rbed){#bedrock-plg}
Die Klasse [Bedrock_PLG](#bedrock-plg) enthält alle lithostratigraphischen Festgesteinseinheiten.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**RBED_CHRONO_T**                 | [ Tabelle ](#gc-chrono-cd)  | Chronostratigraphische Zuordnung der Obergrenze der Kartiereinheit (Top). | [1]
**RBED_CHRONO_B**                 | [ Tabelle ](#gc-chrono-cd)  | Chronostratigraphische Zuordnung der Untergrenze der Kartiereinheit (Basis). | [1]
**TECTO**                 | [ Tabelle ](#gc-tecto-cd)  | Tektonische Zugehörigkeit. | [1]
**GEOL_MAPPING_UNIT_ATT**                 | [ Tabelle ](#gc-geol-mapping-unit-att)  | Kartographische Einheiten. | [1]
**LITSTRAT_FORMATION_BANK**                 | [ Tabelle ](#gc-litstrat-formation-bank-cd)  | -todo-. | [1]
**DESCRIPTION**                 | string                  | Originalbezeichnung gemäss der Legende der zugrundeliegenden geologischen Karte | [1]
**RBED_EXOTIC_ELE**                 | boolean                  | Handelt es sich bei der Objektart um ein exotisches Element; z.B. Einschluss, Linse, Tasche, Olistholith (ja / nein)? | [1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14334001 | Festgestein | Rbed Festgestein     |




#### Attribut  RBED_CHRONO_T
_Chronostratigraphische Zuordnung der Obergrenze der Kartiereinheit (Top)_

Siehe [GC_CHRONO_CD](#gc-chrono-cd) in der Anhang





#### Attribut  RBED_CHRONO_B
_Chronostratigraphische Zuordnung der Untergrenze der Kartiereinheit (Basis)_

Siehe [GC_CHRONO_CD](#gc-chrono-cd) in der Anhang





#### Attribut  TECTO
_Tektonische Zugehörigkeit_

Siehe [GC_TECTO_CD](#gc-tecto-cd) in der Anhang





#### Attribut  GEOL_MAPPING_UNIT_ATT
_Kartographische Einheiten_

Siehe [GC_GEOL_MAPPING_UNIT_ATT](#gc-geol-mapping-unit-att) in der Anhang





#### Attribut  LITSTRAT_FORMATION_BANK
_-todo-_

Siehe [GC_LITSTRAT_FORMATION_BANK_CD](#gc-litstrat-formation-bank-cd) in der Anhang





#### Attribut  DESCRIPTION
_Originalbezeichnung gemäss der Legende der zugrundeliegenden geologischen Karte_

_Datentyp :  string_





#### Attribut  RBED_EXOTIC_ELE
_Handelt es sich bei der Objektart um ein exotisches Element; z.B. Einschluss, Linse, Tasche, Olistholith (ja / nein)?_

_Datentyp :  boolean_









## Thema GEOMORPHOLOGY

### Klasse Instability_Structures_PT (Gins){#instability-structures-pt}
Die Klasse [Instability_Structures_PT](#instability-structures-pt) enthält lokal beobachtete Hinweise auf Hanginstabilitäten
(Rutschungen), die räumlich nicht abgegrenzt werden können. Wenn möglich, sollen instabile
Gesteinsmassen durch Polygone erfasst werden (Klasse Instabilities_PLG).




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11601001 | Hinweis auf Hanginstabilität | Gins Hinweis auf Hanginstabilität     |




### Klasse Instability_Structures_L (Gins){#instability-structures-l}
Die Klasse [Instability_Structures_L](#instability-structures-l) umfasst linienförmige Morphologien, die sich als Folge von
Hanginstabilitäten an der Oberfläche ausgebildet haben.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11701001 | Stauchwulst | Gins Stauchwulst     |
|11701002 | Nackentälchen, Zerrstruktur | Gins Nackentälchen, Zerrstruktur     |
|11701003 | Abrissrand | Gins Abrissrand     |
|11701004 | offene Spalte | Gins offene Spalte     |




### Klasse Instabilities_PLG (Gins){#instabilities-plg}
Die Klasse [Instabilities_PLG](#instabilities-plg) beinhaltet alle Polygone, die Gebiete mit instabilen
Festgesteinen oder Lockergestein begrenzen. In dieser Klasse werden die Prozessräume
der verschiedenen Typen von gleitenden Massenbewegungsprozessen ausgeschieden; die
eigentlichen Gesteinskörper oder Lockergesteinsablagerungen, die von Massenbewegungsprozessen
betroffen bzw. gebildet worden sind, werden in der Klasse [Bedrock_PLG](#bedrock-plg) beschrieben.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**MAIN_MOV**                 | [CD](#instabilities-plg-main-mov)  | Hauptbewegungsphase. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15801001 | Sackungsgebiet | Gins Sackungsgebiet     |
|15801002 | Gebiet mit Hakenwurf | Gins Gebiet mit Hakenwurf     |
|15801003 | Rutschgebiet | Gins Rutschgebiet     |
|15801004 | Gebiet mit Solifluktion | Gins Gebiet mit Solifluktion     |




#### Attribut  MAIN_MOV {#instabilities-plg-main-mov}
_Hauptbewegungsphase_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11502001 | Hauptbewegungsphase vor dem letzteiszeitlichen Maximum | Hauptbewegungsphase vor dem letzteiszeitlichen Maximum     |
|11502002 | Hauptbewegungsphase nach dem letzteiszeitlichen Maximum | Hauptbewegungsphase nach dem letzteiszeitlichen Maximum     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




### Klasse Glacial_Structures_PT (Ggla){#glacial-structures-pt}
Die Klasse [Glacial_Structures_PT](#glacial-structures-pt) enthält Objektarten, welche die ehemalige Anwesenheit eines
Gletschers punktuell dokumentieren (Gletscherschliff ist ein räumlich orientiertes Objekt und
befindet sich deshalb in der Klasse Lineation_PT).




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11201002 | Gletschermühle, Strudelloch | Ggla Gletschermühle, Strudelloch     |
|11201001 | glazitektonische Deformation | Ggla glazitektonische Deformation     |




### Klasse Glacial_and_Periglacial_Structures_L (Ggla){#glacial-and-periglacial-structures-l}
Die Klasse [Glacial_and_Periglacial_Structures_L](#glacial-and-periglacial-structures-l) enthält linienförmige Strukturen, die auf ein
glaziales oder periglaziales Bildungsmilieu hindeuten.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**MORAI_MO**                 | [CD](#glacial-and-periglacial-structures-l-morai-mo)  | Morphologie der Moräne. | [0..1]
**GLAC_TYP**                 | [CD](#glacial-and-periglacial-structures-l-glac-typ)  | Gletschertyp, auf welchen die Objektart bezogen ist. | [0..1]
**ICE_M_P**                 | [CD](#glacial-and-periglacial-structures-l-ice-m-p)  | Räumlicher Gletscherstand. | [0..1]
**QUAT_STR**                 | [CD](#glacial-and-periglacial-structures-l-quat-str)  | Zeitliche quartärstratigraphische Zuordnung des Moränenwälls. | [0..1]
**REF_YEAR**                 | integer                  | Referenzjahr des älteren Gletscherstandes. | [0..1]
**SOURCE**                 | string                  | Quellenangabe der historischen Unterlagen | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11301001 | Moränenwall | Ggla Moränenwall     |
|11301002 | Moränenwall auf Gletscher oder auf Toteis | Ggla Moränenwall auf Gletscher oder auf Toteis     |
|11301003 | Kameterrassenkante | Ggla Kameterrassenkante     |
|11301004 | älterer Gletscherstand, basierend auf historischen Daten | Ggla älterer Gletscherstand, basierend auf historischen Daten     |
|11301005 | Schliffgrenze | Ggla Schliffgrenze     |
|11301006 | Protalus Rampart Wulst | Ggla Protalus Rampart Wulst     |
|11301007 | Blockwulst im Blockgletscher | Ggla Blockwulst im Blockgletscher     |
|11301008 | Schneehaldenmoränenwall | Ggla Schneehaldenmoränenwall     |
|11301009 | Verbreitungsgrenze von Geschiebe | Ggla Verbreitungsgrenze von Geschiebe     |
|11301010 | periglazialer Wulst im Allg. | Ggla periglazialer Wulst im Allg.     |




#### Attribut  MORAI_MO {#glacial-and-periglacial-structures-l-morai-mo}
_Morphologie der Moräne_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11302001 | symmetrisch | symmetrisch     |
|11302002 | einseitig abfallend | einseitig abfallend     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  GLAC_TYP {#glacial-and-periglacial-structures-l-glac-typ}
_Gletschertyp, auf welchen die Objektart bezogen ist_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11303001 | Lokalgletscher | Lokalgletscher     |
|11303002 | grosse Tal- und Vorlandgletscher | grosse Tal- und Vorlandgletscher     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  ICE_M_P {#glacial-and-periglacial-structures-l-ice-m-p}
_Räumlicher Gletscherstand_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11304001 | Maximalstand, undifferenziert | Maximalstand, undifferenziert     |
|11304002 | Bern | Bern     |
|11304003 | Bremgarten, undifferenziert | Bremgarten, undifferenziert     |
|11304004 | Konstanz | Konstanz     |
|11304005 | Feuerthalen, undifferenziert | Feuerthalen, undifferenziert     |
|11304006 | Gurten | Gurten     |
|11304007 | Hurden | Hurden     |
|11304008 | Killwangen | Killwangen     |
|11304009 | Mellingen | Mellingen     |
|11304010 | Muri | Muri     |
|11304011 | Rotkreuz | Rotkreuz     |
|11304012 | Schaffhausen, undifferenziert | Schaffhausen, undifferenziert     |
|11304013 | Schlieren, undifferenziert | Schlieren, undifferenziert     |
|11304014 | Schosshalde | Schosshalde     |
|11304015 | Seftigschwand | Seftigschwand     |
|11304016 | Solothurn | Solothurn     |
|11304017 | Spreitenbach | Spreitenbach     |
|11304018 | Spreitenbach-Killwangen | Spreitenbach-Killwangen     |
|11304019 | Stein am Rhein, undifferenziert | Stein am Rhein, undifferenziert     |
|11304020 | Stetten, undifferenziert | Stetten, undifferenziert     |
|11304021 | Wangen I | Wangen I     |
|11304022 | Wangen II | Wangen II     |
|11304023 | Wittigkofen | Wittigkofen     |
|11304024 | Zürich, undifferenziert | Zürich, undifferenziert     |
|11304025 | Stein-am-Rhein I | Stein-am-Rhein I     |
|11304026 | Stein-am-Rhein II | Stein-am-Rhein II     |
|11304027 | Stein-am-Rhein III | Stein-am-Rhein III     |
|11304028 | Feuerthalen I | Feuerthalen I     |
|11304029 | Feuerthalen II | Feuerthalen II     |
|11304030 | Schaffausen I | Schaffausen I     |
|11304031 | Schaffausen II | Schaffausen II     |
|11304035 | Küblis | Küblis     |
|11304036 | Lunden | Lunden     |
|11304037 | Chur | Chur     |
|11304038 | Sargans | Sargans     |
|11304039 | Koblach | Koblach     |
|11304040 | Fideris | Fideris     |
|11304041 | Serneus | Serneus     |
|11304042 | Wangen, undifferenziert | Wangen, undifferenziert     |
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
|11304054 | Bülach, undifferenziert | Bülach, undifferenziert     |
|11304055 | Dättikon | Dättikon     |
|11304056 | Regensdorf | Regensdorf     |
|11304057 | Seeb | Seeb     |
|11304058 | Stetten I | Stetten I     |
|11304059 | Stetten II | Stetten II     |
|11304060 | Würenlos I | Würenlos I     |
|11304061 | Würenlos II | Würenlos II     |
|11304062 | Würenlos, undifferenziert | Würenlos, undifferenziert     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  QUAT_STR {#glacial-and-periglacial-structures-l-quat-str}
_Zeitliche quartärstratigraphische Zuordnung des Moränenwälls_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11305001 | 1. Vergletscherung der letzten Eiszeit (MIS 5d) | 1. Vergletscherung der letzten Eiszeit (MIS 5d)     |
|11305002 | 2. Vergletscherung der letzten Eiszeit (MIS 4) | 2. Vergletscherung der letzten Eiszeit (MIS 4)     |
|11305003 | 3. Vergletscherung der letzten Eiszeit (LGM, MIS 2) | 3. Vergletscherung der letzten Eiszeit (LGM, MIS 2)     |
|11305004 | Gschnitz | Gschnitz     |
|11305005 | Clavadel | Clavadel     |
|11305006 | Daun | Daun     |
|11305007 | Egesen | Egesen     |
|11305008 | Mittleres Pleistozän | Mittleres Pleistozän     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  REF_YEAR
_Referenzjahr des älteren Gletscherstandes._

_Datentyp :  integer_





#### Attribut  SOURCE
_Quellenangabe der historischen Unterlagen_

_Datentyp :  string_





### Klasse Glacial_Structures_PLG (Ggla){#glacial-structures-plg}
Die Klasse [Glacial_Structures_PLG](#glacial-structures-plg) umfasst flächenhafte glaziale Landschaftsformen, die durch basales Fliessen des Gletschereises oder dessen Abschmelzen entstanden sind.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11401001 | Drumlin, drumlinartige Kieskuppe | Ggla Drumlin, drumlinartige Kieskuppe     |
|11401003 | Rundhöcker | Ggla Rundhöcker     |
|11401004 | Toteisloch, Soll | Ggla Toteisloch, Soll     |
|11401005 | Kame | Ggla Kame     |




### Klasse Erosional_Structures_PT (Gero){#erosional-structures-pt}
Die Klasse [Erosional_Structures_PT](#erosional-structures-pt) beinhaltet lokale Landschaftselemente, die sich im Laufe der
Zeit unter Einwirkung von diversen Erosionsprozessen gebildet haben.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11001001 | Erdpyramide | Gero Erdpyramide     |




### Klasse Erosional_Structures_L (Gero){#erosional-structures-l}
Die Klasse [Erosional_Structures_L](#erosional-structures-l) enthält linienförmige erosive Formen wie Erosionsränder im
Allgemeinen oder Terrassenkanten.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11101001 | Erosionsrand | Gero Erosionsrand     |
|11101002 | Terrassenkante | Gero Terrassenkante     |
|11101003 | Schichtstufenkante | Gero Schichtstufenkante     |




### Klasse Karstic_Structures_PT (Gkar){#karstic-structures-pt}
Die Klasse [Karstic_Structures_PT](#karstic-structures-pt) beinhaltet Karstphänomene, die punktförmig dargestellt werden.
Darunter fallen u.a. der Ponor oder der Eingang zu einer Höhle.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**ICE_CAVE**                 | boolean                  | Eisgrotte (ja / nein) | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11301001 | Moränenwall | Ggla Moränenwall     |
|11301002 | Moränenwall auf Gletscher oder auf Toteis | Ggla Moränenwall auf Gletscher oder auf Toteis     |
|11301003 | Kameterrassenkante | Ggla Kameterrassenkante     |
|11301004 | älterer Gletscherstand, basierend auf historischen Daten | Ggla älterer Gletscherstand, basierend auf historischen Daten     |
|11301005 | Schliffgrenze | Ggla Schliffgrenze     |
|11301006 | Protalus Rampart Wulst | Ggla Protalus Rampart Wulst     |
|11301007 | Blockwulst im Blockgletscher | Ggla Blockwulst im Blockgletscher     |
|11301008 | Schneehaldenmoränenwall | Ggla Schneehaldenmoränenwall     |
|11301009 | Verbreitungsgrenze von Geschiebe | Ggla Verbreitungsgrenze von Geschiebe     |
|11301010 | periglazialer Wulst im Allg. | Ggla periglazialer Wulst im Allg.     |




#### Attribut  ICE_CAVE
_Eisgrotte (ja / nein)_

_Datentyp :  boolean_





### Klasse Karstic_Structures_PLG (Gkar){#karstic-structures-plg}
Die Klasse [Karstic_Structures_PLG](#karstic-structures-plg) umfasst flächenhafte Karstformen wie Dolinen oder Poljen.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12001001 | Senke ohne oberirdischen Abfluss | Gkar Senke ohne oberirdischen Abfluss     |
|12001002 | Doline | Gkar Doline     |
|12001003 | Karrenfeld | Gkar Karrenfeld     |
|12001004 | Polje | Gkar Polje     |




### Klasse Alluvial_and_Lacustrine_Structures_L (Gall){#alluvial-and-lacustrine-structures-l}
Die Klasse [Alluvial_and_Lacustrine_Structures_L](#alluvial-and-lacustrine-structures-l) beinhaltet linienförmige Morphologien
fluviatilen oder lakustrischen Ursprungs.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**AGE**                 | [CD](#alluvial-and-lacustrine-structures-l-age)  | Alter der Objektart.. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10901001 | Strandwall | Gall Strandwall     |
|10901002 | Achse einer Murgangrinne | Gall Achse einer Murgangrinne     |




#### Attribut  AGE {#alluvial-and-lacustrine-structures-l-age}
_Alter der Objektart._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10902001 | fossil | fossil     |
|10902002 | rezent | rezent     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |








## Thema TECTONICS

### Klasse Deformation_Structures_PT (Tdef){#deformation-structures-pt}
Die Klasse [Deformation_Structures_PT](#deformation-structures-pt) beinhaltet punktuell beobachtete tektonische
Deformationsstrukturen wie lokal stark verfaltete Stellen (Fältelung) oder Orte mit ausgeprägter
Klüftung. Ebenfalls in dieser Klasse befinden sich konstruierte Punkte wie z.B. die Orientierung
der Faltenachsenfläche.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**AZIMUTH**                 | integer                  | Fallrichtung (Azimut) der jeweiligen Punktobjektart. Wert in Grad von 0° bis 359° im Uhrzeigersinn gemessen. | [0..1]
**DIP**                 | integer                  | Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen
aus der Horizontalen (0°) nach unten bis in die Vertikale (90°). | [0..1]
**FOLD_TYP**                 | [CD](#deformation-structures-pt-fold-typ)  | Objekttyp. | [0..1]
**FOLD_FOR**                 | [CD](#deformation-structures-pt-fold-for)  | Objektform. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14601001 | punktuell beobachtete tektonische Brekzie | Tdef punktuell beobachtete tektonische Brekzie     |
|14601002 | ausgeprägte Klüftung | Tdef ausgeprägte Klüftung     |
|14601003 | tektonische Diskordanz | Tdef tektonische Diskordanz     |
|14601004 | Orientierung der Faltenachsenfläche | Tdef Orientierung der Faltenachsenfläche     |
|14601005 | Fältelung | Tdef Fältelung     |
|14601006 | Darstellung der Spur einer Achsenfläche | Tdef Darstellung der Spur einer Achsenfläche     |
|14601007 | Chevron-Falte, Kink Fold | Tdef Chevron-Falte, Kink Fold     |




#### Attribut  AZIMUTH
_Fallrichtung (Azimut) der jeweiligen Punktobjektart. Wert in Grad von 0° bis 359° im Uhrzeigersinn gemessen._

_Datentyp :  integer_





#### Attribut  DIP
_Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen
aus der Horizontalen (0°) nach unten bis in die Vertikale (90°)._

_Datentyp :  integer_





#### Attribut  FOLD_TYP {#deformation-structures-pt-fold-typ}
_Objekttyp_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14604001 | Antiklinale | Antiklinale     |
|14604002 | Synklinale | Synklinale     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  FOLD_FOR {#deformation-structures-pt-fold-for}
_Objektform_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14605001 | Antiform | Antiform     |
|14605002 | Synform | Synform     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




### Klasse Deformation_Structures_L (Tdef){#deformation-structures-l}
Die Klasse [Deformation_Structures_L](#deformation-structures-l) enthält linienförmige tektonische Deformationsstrukturen,
wie den Verlauf des Faltenscharniers.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14701001 | Faltenscharnier | Tdef Faltenscharnier     |




### Klasse Deformation_Structures_PLG (Tdef){#deformation-structures-plg}
In der Klasse [Deformation_Structures_PLG](#deformation-structures-plg) befinden sich tektonisch geprägte Zonen wie
tektonisierte Zonen oder Kluftzonen.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**TYPE**                 | [CD](#deformation-structures-plg-type)  | Charakteristik der Objektarten. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14801001 | Kluftzone | Tdef Kluftzone     |
|14801002 | tektonisierte Zone | Tdef tektonisierte Zone     |




#### Attribut  TYPE {#deformation-structures-plg-type}
_Charakteristik der Objektarten_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14802001 | kataklastisch | kataklastisch     |
|14802002 | kakiritisch | kakiritisch     |
|14802003 | mylonitisch | mylonitisch     |
|14802004 | pseudotachylitisch | pseudotachylitisch     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




### Klasse Tectonic_Boundaries_L (Ttec){#tectonic-boundaries-l}
Die Klasse [Tectonic_Boundaries_L](#tectonic-boundaries-l) umfasst alle tektonischen Verwerfungen.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**FAULT_MO**                 | [CD](#tectonic-boundaries-l-fault-mo)  | Bewegungsrichtung des Bruchs. | [0..1]
**VERTI_MO**                 | [CD](#tectonic-boundaries-l-verti-mo)  | Bewegung parallel zur Fallrichtung der Bruchfläche.. | [0..1]
**HORIZ_MO**                 | [CD](#tectonic-boundaries-l-horiz-mo)  | Bewegung parallel zur Streichrichtung der Bruch- oder Scherfläche. | [0..1]
**LIM_TYP**                 | [CD](#tectonic-boundaries-l-lim-typ)  | Typ der tektonischen Grenze (Deckengrenze,Schuppengrenze, etc.). | [1]
**HIERA**                 | [CD](#tectonic-boundaries-l-hiera)  | Typ der tektonischen Grenze (Deckengrenze,Schuppengrenze, etc.). | [1]
**STATUS**                 | [CD](#tectonic-boundaries-l-status)  | Zustand der Objektart. | [1]
**META_STA**                 | [CD](#tectonic-boundaries-l-meta-sta)  | Tektonometamorphe Chronologie der Objektart. | [0..1]
**NAME**                 | string                  | Spezifischer Name der Objektart. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14901001 | Überschiebung | Ttec Überschiebung     |
|14901002 | Abschiebung | Ttec Abschiebung     |
|14901004 | Bruch | Ttec Bruch     |
|14901005 | Aufschiebung | Ttec Aufschiebung     |
|14901006 | Blattverschiebung | Ttec Blattverschiebung     |
|14901007 | komplexe Störung | Ttec komplexe Störung     |
|14901008 | Störung i. Allg. | Ttec Störung i. Allg.     |
|14901009 | neotektonischer Bruch | Ttec neotektonischer Bruch     |




#### Attribut  FAULT_MO {#tectonic-boundaries-l-fault-mo}
_Bewegungsrichtung des Bruchs_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14902001 | schrägverschiebend (oblique slip) | schrägverschiebend (oblique slip)     |
|14902002 | parallel zur Streichrichtung (Horizontalverschiebung) | parallel zur Streichrichtung (Horizontalverschiebung)     |
|14902003 | parallel zur Fallrichtung (strike slip) | parallel zur Fallrichtung (strike slip)     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  VERTI_MO {#tectonic-boundaries-l-verti-mo}
_Bewegung parallel zur Fallrichtung der Bruchfläche._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14903001 | aufschiebend | aufschiebend     |
|14903002 | abschiebend | abschiebend     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  HORIZ_MO {#tectonic-boundaries-l-horiz-mo}
_Bewegung parallel zur Streichrichtung der Bruch- oder Scherfläche_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14904001 | dextral | dextral     |
|14904002 | sinistral | sinistral     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  LIM_TYP {#tectonic-boundaries-l-lim-typ}
_Typ der tektonischen Grenze (Deckengrenze,Schuppengrenze, etc.)_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14910001 | Decken trennend | Decken trennend     |
|14910002 | Schuppen trennend | Schuppen trennend     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  HIERA {#tectonic-boundaries-l-hiera}
_Typ der tektonischen Grenze (Deckengrenze,Schuppengrenze, etc.)_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14911001 | Störung | Störung     |
|14911002 | Teilstörungssystem | Teilstörungssystem     |
|14911003 | Grossstörungssystem | Grossstörungssystem     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  STATUS {#tectonic-boundaries-l-status}
_Zustand der Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14906001 | gesichert, im Allgemeinen | gesichert, im Allgemeinen     |
|14906002 | gesichert, unter Tage festgestellt | gesichert, unter Tage festgestellt     |
|14906003 | vermutet | vermutet     |
|14906004 | aus Seismikdaten interpretiert | aus Seismikdaten interpretiert     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  META_STA {#tectonic-boundaries-l-meta-sta}
_Tektonometamorphe Chronologie der Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14908001 | vor der Platznahme der Decken | vor der Platznahme der Decken     |
|14908002 | während der Platznahme der Decken | während der Platznahme der Decken     |
|14908003 | nach der Platznahme der Decken | nach der Platznahme der Decken     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  NAME
_Spezifischer Name der Objektart._

_Datentyp :  string_









## Thema MEASUREMENTS_SPATIAL_ORIENTATION

### Klasse Folds_PT (Mfol){#folds-pt}
Die Klasse [Folds_PT](#folds-pt) enthält Objektarten, welche die räumliche Lage von verfalteten geologischen
Objekten (mit direkten Feldmessungen) beschreiben.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**FOLD_TYP**                 | [CD](#folds-pt-fold-typ)  | Faltentyp. | [0..1]
**FOLD_FOR**                 | [CD](#folds-pt-fold-for)  | Faltenform. | [0..1]
**PHASE**                 | [CD](#folds-pt-phase)  | Deformationsphase.. | [0..1]
**PHASE_REF**                 | string                  | Referenz für die Angabe der Deformationsphase. | [0..1]
**AZIMUTH**                 | integer                  | Einfallsrichtung (Azimut) der jeweiligen Punktobjektart (z.B. Scheitellinie, Faltenachse). Wert in Grad (0° 359°) im Uhrzeigersinn gemessen | [1]
**DIP**                 | integer                  | Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die Vertikale (90°). | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13601001 | Orientierung der Faltenachse | Mfol Orientierung der Faltenachse     |
|13601002 | Orientierung der Scheitellinie | Mfol Orientierung der Scheitellinie     |
|13601003 | Orientierung der Muldenlinie | Mfol Orientierung der Muldenlinie     |




#### Attribut  FOLD_TYP {#folds-pt-fold-typ}
_Faltentyp_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13602001 | Antiklinale | Antiklinale     |
|13602002 | Synklinale | Synklinale     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  FOLD_FOR {#folds-pt-fold-for}
_Faltenform_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|




#### Attribut  PHASE {#folds-pt-phase}
_Deformationsphase._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13604001 | F1 (1. Phase) | F1 (1. Phase)     |
|13604002 | F2 (2. Phase) | F2 (2. Phase)     |
|13604003 | F3 (3. Phase) | F3 (3. Phase)     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  PHASE_REF
_Referenz für die Angabe der Deformationsphase._

_Datentyp :  string_





#### Attribut  AZIMUTH
_Einfallsrichtung (Azimut) der jeweiligen Punktobjektart (z.B. Scheitellinie, Faltenachse). Wert in Grad (0° 359°) im Uhrzeigersinn gemessen_

_Datentyp :  integer_





#### Attribut  DIP
_Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die Vertikale (90°)._

_Datentyp :  integer_





### Klasse Lineation_PT (Mlin){#lineation-pt}
In der Klasse [Lineation_PT](#lineation-pt) finden sich Objektarten, welche die räumliche Lage von diversen
Linearen mit direkten Feldmessungen beschreiben. Die räumliche Lage u.a. von Gletscherschliffen
und Rutschharnischen ist ebenso Teil dieser Klasse wie die Orientierung von Streckungs- oder
Intersektionslineationen.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**AZIMUTH**                 | integer                  | Einfallsrichtung (Azimut) der jeweiligen Punktobjektart (z.B. Scheitellinie, Faltenachse). Wert in Grad (0° 359°) im Uhrzeigersinn gemessen | [1]
**DIP**                 | integer                  | Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die Vertikale (90°). | []





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13701001 | Orientierung der Intersektionslineation | Mlin Orientierung der Intersektionslineation     |
|13701002 | Orientierung der Streckungslineation | Mlin Orientierung der Streckungslineation     |
|13701003 | Orientierung von Rutschharnischen | Mlin Orientierung von Rutschharnischen     |
|13701004 | Orientierung von Gletscherschliffen | Mlin Orientierung von Gletscherschliffen     |




#### Attribut  AZIMUTH
_Einfallsrichtung (Azimut) der jeweiligen Punktobjektart (z.B. Scheitellinie, Faltenachse). Wert in Grad (0° 359°) im Uhrzeigersinn gemessen_

_Datentyp :  integer_





#### Attribut  DIP
_Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die Vertikale (90°)._

_Datentyp :  integer_





### Klasse Planar_Structures_PT (Mpla){#planar-structures-pt}
Die Klasse [Planar_Structures_PT](#planar-structures-pt) enthält Objektarten, welche die räumliche Lage von planaren Strukturen mit direkten Feldmessungen beschreiben.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**POLARITY**                 | [CD](#planar-structures-pt-polarity)  | Position der Objektart im Raum. | [0..1]
**PHASE**                 | [CD](#planar-structures-pt-phase)  | Deformationsphase. | [0..1]
**PHASE_REF**                 | string                  | Referenz für die Angabe der Deformationsphase. | [0..1]
**OB_DIP_SLO**                 | boolean                  | Dip slope (ja / nein)? | [0..1]
**AZIMUTH**                 | integer                  | Einfallsrichtung (Azimut) der jeweiligen Punktobjektart (z.B. Scheitellinie, Faltenachse). Wert in Grad (0° 359°) im Uhrzeigersinn gemessen | [1]
**DIP**                 | integer                  | Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die Vertikale (90°). | []





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13801002 | Orientierung eines Ganges | Mpla Orientierung eines Ganges     |
|13801003 | Orientierung einer Bruchfläche | Mpla Orientierung einer Bruchfläche     |
|13801004 | Orientierung der Schieferung | Mpla Orientierung der Schieferung     |
|13801005 | Orientierung einer Schichtung oder Schieferung | Mpla Orientierung einer Schichtung oder Schieferung     |
|13801001 | Orientierung der Schichten | Mpla Orientierung der Schichten     |
|13801006 | Schüttungsrichtung | Mpla Schüttungsrichtung     |




#### Attribut  POLARITY {#planar-structures-pt-polarity}
_Position der Objektart im Raum_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13802001 | normal | normal     |
|13802002 | überkippt | überkippt     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  PHASE {#planar-structures-pt-phase}
_Deformationsphase_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13803001 | S1 (1. Phase) | S1 (1. Phase)     |
|13803002 | S2 (2. Phase) | S2 (2. Phase)     |
|13803003 | S3 (3. Phase) | S3 (3. Phase)     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  PHASE_REF
_Referenz für die Angabe der Deformationsphase._

_Datentyp :  string_





#### Attribut  OB_DIP_SLO
_Dip slope (ja / nein)?_

_Datentyp :  boolean_





#### Attribut  AZIMUTH
_Einfallsrichtung (Azimut) der jeweiligen Punktobjektart (z.B. Scheitellinie, Faltenachse). Wert in Grad (0° 359°) im Uhrzeigersinn gemessen_

_Datentyp :  integer_





#### Attribut  DIP
_Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die Vertikale (90°)._

_Datentyp :  integer_









## Thema LOCAL_ADDITIONAL_INFORMATION

### Klasse Anomalies_PT (Lano){#anomalies-pt}
Die Klasse [Anomalies_PT](#anomalies-pt) beinhaltet lokal beobachtete und / oder gemessene Anomalien.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**TYPE**                 | [CD](#anomalies-pt-type)  | Charakteristik der Objektart.. | []





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12801001 | gemessene Anomalie | Lano gemessene Anomalie     |
|12801002 | Fulgurit | Lano Fulgurit     |




#### Attribut  TYPE {#anomalies-pt-type}
_Charakteristik der Objektart._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|




### Klasse Fossils_PT (Lfos){#fossils-pt}
Die Klasse [Fossils_PT](#fossils-pt) enthält alle Fossilfundstellen.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**DIVISION**                 | [CD](#fossils-pt-division)  | Fossilienkategorie, zu welcher die Objektinstanz gehört.. | [0..1]
**SYSTEM**                 | [ Tabelle ](#gc-system)  | Fossiliengruppe.. | [0..5]
**DAT_METH**                 | [CD](#fossils-pt-dat-meth)  | Datierungsmethode.. | [0..1]
**STATUS**                 | [CD](#fossils-pt-status)  | Zustand der Objektart. | [0..1]
**PROTECTED**                 | boolean                  | Geschützte Fossilfundstelle (ja / nein)? | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12901001 | Fossilfundstelle | Lfos Fossilfundstelle     |




#### Attribut  DIVISION {#fossils-pt-division}
_Fossilienkategorie, zu welcher die Objektinstanz gehört._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12902001 | Tierreste | Tierreste     |
|12902002 | Pflanzen- und Tierreste | Pflanzen- und Tierreste     |
|12902003 | Pflanzenreste | Pflanzenreste     |
|12902004 | Spuren | Spuren     |
|12902006 | Einzeller | Einzeller     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  SYSTEM
_Fossiliengruppe._

Siehe [gc_system](#gc-system) in der Anhang





#### Attribut  DAT_METH {#fossils-pt-dat-meth}
_Datierungsmethode._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12904001 | radiometrisch datiert | radiometrisch datiert     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  STATUS {#fossils-pt-status}
_Zustand der Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12905001 | aufgeschlossen | aufgeschlossen     |
|12905002 | wieder verdeckt | wieder verdeckt     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  PROTECTED
_Geschützte Fossilfundstelle (ja / nein)?_

_Datentyp :  boolean_





### Klasse Indication_of_Resources_PT (Lind){#indication-of-resources-pt}
Die Klasse [Indication_of_Resources_PT](#indication-of-resources-pt) beinhaltet Fundstellen von vulkanischen, mineralischen
und nicht-mineralischen Rohstoffen.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**STATUS**                 | [CD](#indication-of-resources-pt-status)  | Zustand der Objektart. | [0..1]
**MATERIAL**                 | [CD](#indication-of-resources-pt-material)  | Material, das mit der Objektart in Verbindung steht. | [0..1]
**CHEMISTRY**                 | string                  | Chemische Komponente(n) oder Mineralien, welche die Natur der Objektart charakterisieren. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13201001 | Mineralfundstelle | Lres Mineralfundstelle     |
|13201002 | Gasquelle | Lres Gasquelle     |
|13201003 | Anzeichen auf Öl | Lres Anzeichen auf Öl     |
|13201006 | Fundstelle vulkanischer Auswürflinge (Tephra) | Lres Fundstelle vulkanischer Auswürflinge (Tephra)     |
|13201007 | Fundstelle von Ries-Auswürflingen | Lres Fundstelle von Ries-Auswürflingen     |
|13201008 | Asphalt, vereinzeltes Vorkommen | Lres Asphalt, vereinzeltes Vorkommen     |
|13201005 | Fundstelle von vulkanischem Tuffit | Lres Fundstelle von vulkanischem Tuffit     |
|13201004 | Tasche, Karsttasche, Kluft, mit Füllung von siderolithischem Sediment | Lres Tasche, Karsttasche, Kluft, mit Füllung von siderolithischem Sediment     |
|13201009 | Meteoritenfundstelle | Lres Meteoritenfundstelle     |




#### Attribut  STATUS {#indication-of-resources-pt-status}
_Zustand der Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13202001 | aufgeschlossen | aufgeschlossen     |
|13202002 | wieder verdeckt | wieder verdeckt     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  MATERIAL {#indication-of-resources-pt-material}
_Material, das mit der Objektart in Verbindung steht_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13203001 | Boluston | Boluston     |
|13203002 | Huppererde | Huppererde     |
|13203003 | Bohnerz | Bohnerz     |
|13203004 | Glas- / Quarzsand | Glas- / Quarzsand     |
|13203005 | Walkerde | Walkerde     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  CHEMISTRY
_Chemische Komponente(n) oder Mineralien, welche die Natur der Objektart charakterisieren._

_Datentyp :  string_





### Klasse Mineralised_Zone_L (Lmin){#mineralised-zone-l}
Die Klasse [Mineralised_Zone_L](#mineralised-zone-l) beinhaltet Vererzungszonen.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**CHEMISTRY**                 | string                  | Chemische Komponente(n), welche die Natur der Objektart charakterisieren. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13301001 | Vererzungszone | Lmin Vererzungszone     |




#### Attribut  CHEMISTRY
_Chemische Komponente(n), welche die Natur der Objektart charakterisieren._

_Datentyp :  string_





### Klasse Sedimentary_Structures_PT (Lsed){#sedimentary-structures-pt}
Die Klasse [Sedimentary_Structures_PT](#sedimentary-structures-pt) enthält beobachtete Sedimentstrukturen.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**AZIMUTH**                 | integer                  | Orientierung des Symbols. Wert in Grad (0° bis 359°) im Uhrzeigersinn gemessen. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13401001 | Sedimentstrukturen | Lsed Sedimentstrukturen     |
|13401002 | Riffstrukturen | Lsed Riffstrukturen     |
|13401003 | Erosions- oder Omissionsfläche, Hartgrund, Kondensationshorizont | Lsed Erosions- oder Omissionsfläche, Hartgrund, Kondensationshorizont     |
|13401004 | stratigraphische Lage (Polarität) einer Schichtserie | Lsed stratigraphische Lage (Polarität) einer Schichtserie     |
|13401005 | Winkeldiskordanz | Lsed Winkeldiskordanz     |
|13401006 | Entwässerungstrichter (blow-out structure) | Lsed Entwässerungstrichter (blow-out structure)     |




#### Attribut  AZIMUTH
_Orientierung des Symbols. Wert in Grad (0° bis 359°) im Uhrzeigersinn gemessen._

_Datentyp :  integer_





### Klasse Type_Localities_PT (Ltyp){#type-localities-pt}
Die Klasse [Type_Localities_PT](#type-localities-pt) beinhaltet diejenigen Objektarten, die Typusprofile oder wichtige
geologische Aufschlüsse beschreiben.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**STRATI**                 | [CD](#type-localities-pt-strati)  | Lithostratigraphischer Zusatz zum Objekt. | [0..1]
**NAME**                 | string                  | Name der Typlokalität. / Beschreibung des geologisch relevanten Aufschlusses | [0..1]
**ACCESSIBIL**                 | boolean                  | Ist die Objektart zum Zeitpunkt der Aufnahme aufgeschlossen (ja / nein)? | [0..1]
**PROTECTED**                 | boolean                  | Geschütztes geologisches Objekt (ja / nein)? | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13501001 | geologisch relevanter Aufschluss | Ltyp geologisch relevanter Aufschluss     |
|13501003 | Typusprofil | Ltyp Typusprofil     |




#### Attribut  STRATI {#type-localities-pt-strati}
_Lithostratigraphischer Zusatz zum Objekt_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13502001 | Gruppe | Gruppe     |
|13502002 | Subgruppe | Subgruppe     |
|13502003 | Formation | Formation     |
|13502004 | Member | Member     |
|13502005 | Bank | Bank     |
|13502006 | Stufe | Stufe     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  NAME
_Name der Typlokalität. / Beschreibung des geologisch relevanten Aufschlusses_

_Datentyp :  string_





#### Attribut  ACCESSIBIL
_Ist die Objektart zum Zeitpunkt der Aufnahme aufgeschlossen (ja / nein)?_

_Datentyp :  boolean_





#### Attribut  PROTECTED
_Geschütztes geologisches Objekt (ja / nein)?_

_Datentyp :  boolean_





### Klasse Prominent_Lithological_Features_L (Lpro){#prominent-lithological-features-l}
In der Klasse [Prominent_Lithological_Features_L](#prominent-lithological-features-l) befinden sich linienförmige Gesteinshorizonte.
Diese Gesteinshorizonte haben lediglich Hinweischarakter (z.B. «markante Sandsteinbank» innerhalb
von Wechsellagerungen von Sandstein und Mergel) und sind von den Leithorizonten (z.B.
«Spatkalk im Hauptrogenstein») zu unterschieden. Leithorizonte befinden sich im Thema Rock Bodies.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**CONG_SPE**                 | [CD](#prominent-lithological-features-l-cong-spe)  | Charakterisation der Konglomerate nach ihrem Geröllspektrum.. | [0..1]
**NAME_HORIZ**                 | [ Tabelle ](#gc-geol-mapping-unit-cd)  | Name des Leithorizonts.. | [0..1]
**ORIG_DESCR**                 | string                  | Originalbezeichnung gemäss der Legende der zugrundeliegenden geologischen Karte. | [0..1]
**LITHO**                 | [ Tabelle ](#gc-litho-cd)  | Materialbezeichnung (lithologische Einheit).. | [1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13101001 | Gesteinshorizont | Lpro Gesteinshorizont     |




#### Attribut  CONG_SPE {#prominent-lithological-features-l-cong-spe}
_Charakterisation der Konglomerate nach ihrem Geröllspektrum._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13102001 | kristallinfreie bis -arme (Kalk-)Nagelfluh | kristallinfreie bis -arme (Kalk-)Nagelfluh     |
|13102002 | kristallinführende (Kalk-)Nagelfluh | kristallinführende (Kalk-)Nagelfluh     |
|13102003 | bunte bis polygene Nagelfluh | bunte bis polygene Nagelfluh     |
|13102004 | Flyschsandstein-Nagelfluh, Riesenkonglomerat | Flyschsandstein-Nagelfluh, Riesenkonglomerat     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  NAME_HORIZ
_Name des Leithorizonts._

Siehe [GC_GEOL_MAPPING_UNIT_CD](#gc-geol-mapping-unit-cd) in der Anhang





#### Attribut  ORIG_DESCR
_Originalbezeichnung gemäss der Legende der zugrundeliegenden geologischen Karte._

_Datentyp :  string_





#### Attribut  LITHO
_Materialbezeichnung (lithologische Einheit)._

Siehe [GC_LITHO_CD](#gc-litho-cd) in der Anhang





### Klasse Miscellaneous_PT (Lmis){#miscellaneous-pt}
Die Klasse [Miscellaneous_PT](#miscellaneous-pt) ist für lokale, sehr spezielle geologische Objekte reserviert, die für die
Gesamtheit der geologischen Daten irrelevant sind und deshalb im Datenmodell Geologie nicht
standardisiert werden




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**ORIG_NAME**                 | string                  | Ursprüngliche Bezeichnung des Objektes. | [1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15501001 | Diverse | Lmis Diverse     |




#### Attribut  ORIG_NAME
_Ursprüngliche Bezeichnung des Objektes._

_Datentyp :  string_





### Klasse Geological_Outlines_L (Lgeo){#geological-outlines-l}
Die Klasse [Geological_Outlines_L](#geological-outlines-l) beinhaltet geologische Konturen.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**STATUS**                 | [CD](#geological-outlines-l-status)  | Zustand der Objektart.. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13001001 | geologische Kontur | Lgeo geologische Kontur     |




#### Attribut  STATUS {#geological-outlines-l-status}
_Zustand der Objektart._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13002001 | im Allgemeinen | im Allgemeinen     |
|13002002 | vermutet | vermutet     |
|13002003 | künstlich | künstlich     |
|13002004 | gesichert, tektonisch überprägt | gesichert, tektonisch überprägt     |
|13002005 | vermutet, tektonisch überprägt | vermutet, tektonisch überprägt     |
|13002006 | Gewässerlinie | Gewässerlinie     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |








## Thema PARAMETER_AND_MODELLING

### Klasse Slope_Bedrock_PT (Pslo){#slope-bedrock-pt}
Die Klasse [Slope_Bedrock_PT](#slope-bedrock-pt) enthält Punktinformationen aus Modellierungen des Festgestein-
verlaufs im Untergrund.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**TYPE**                 | [CD](#slope-bedrock-pt-type)  | Referenzoberfläche.. | [1]
**AZIMUTH**                 | integer                  | Fallrichtung (Azimut) der jeweiligen Punktobjektart. Wert in Grad (0° bis 359°) im Uhrzeigersinn gemessen. | [0..1]
**DIP**                 | integer                  | Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die Vertikale (90°). | [0..1]
**FORMATIO**                 | [ Tabelle ](#gc-geol-mapping-unit-cd)  | Lithostratigraphische Einheit der modellierten Formation. | [1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14201001 | Neigungsrichtung | Pslo Neigungsrichtung     |




#### Attribut  TYPE {#slope-bedrock-pt-type}
_Referenzoberfläche._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14202001 | Felsoberfläche | Felsoberfläche     |
|14202002 | Obergrenze einer gegebenen Formation | Obergrenze einer gegebenen Formation     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  AZIMUTH
_Fallrichtung (Azimut) der jeweiligen Punktobjektart. Wert in Grad (0° bis 359°) im Uhrzeigersinn gemessen._

_Datentyp :  integer_





#### Attribut  DIP
_Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die Vertikale (90°)._

_Datentyp :  integer_





#### Attribut  FORMATIO
_Lithostratigraphische Einheit der modellierten Formation_

Siehe [GC_GEOL_MAPPING_UNIT_CD](#gc-geol-mapping-unit-cd) in der Anhang





### Klasse Contour_Lines_Bedrock_L (Pcon){#contour-lines-bedrock-l}
Die Klasse [Contour_Lines_Bedrock_L](#contour-lines-bedrock-l) beinhaltet Isohypsen, die sich auf den Verlauf des Fest-
gesteins beziehen und die das Resultat von Modellierungen darstellen. U.a. befinden sich die Iso-
hypsen der Felsoberfläche in dieser Klasse.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**TYPE**                 | [CD](#contour-lines-bedrock-l-type)  | Referenzoberfläche.. | [1]
**ALTITUDE**                 | float                  | Höhenangabe (m ü.M.) von Isohypsen. | [1]
**LITSTRAT**                 | [ Tabelle ](#gc-geol-mapping-unit-cd)  | Lithostratigraphische Einheit der modellierten Formation. | [1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13901001 | Isohypse | Pcob Isohypse     |




#### Attribut  TYPE {#contour-lines-bedrock-l-type}
_Referenzoberfläche._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13902001 | Felsoberfläche | Felsoberfläche     |
|13902002 | Obergrenze einer gegebenen Formation | Obergrenze einer gegebenen Formation     |
|13902003 | Untergrenze einer gegebenen Formation | Untergrenze einer gegebenen Formation     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  ALTITUDE
_Höhenangabe (m ü.M.) von Isohypsen._

_Datentyp :  float_





#### Attribut  LITSTRAT
_Lithostratigraphische Einheit der modellierten Formation_

Siehe [GC_GEOL_MAPPING_UNIT_CD](#gc-geol-mapping-unit-cd) in der Anhang





### Klasse Modelled_Water_Table_PT (Pmod){#modelled-water-table-pt}
Die Klasse [Modelled_Water_Table_PT](#modelled-water-table-pt) enthält Punktinformationen aus Modellierungen des
Grundwasserspiegels.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**AZIMUTH**                 | integer                  | Fallrichtung (Azimut) der jeweiligen Punktobjektart. Wert in Grad (0° bis 359°) im Uhrzeigersinn gemessen. | [0..1]
**DIP**                 | integer                  | Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die Vertikale (90°). | [0..1]
**HEIGHT**                 | float                  | Kote des Grundwasserspiegels (m ü.M.). | [0..1]
**MEA_PERIOD**                 | range                  | Messperiode. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14101001 | Grundwasserfliessrichtung | Pmod Grundwasserfliessrichtung     |
|14101002 | mittlere Höhe des Grundwasserspiegels | Pmod mittlere Höhe des Grundwasserspiegels     |




#### Attribut  AZIMUTH
_Fallrichtung (Azimut) der jeweiligen Punktobjektart. Wert in Grad (0° bis 359°) im Uhrzeigersinn gemessen._

_Datentyp :  integer_





#### Attribut  DIP
_Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die Vertikale (90°)._

_Datentyp :  integer_





#### Attribut  HEIGHT
_Kote des Grundwasserspiegels (m ü.M.)._

_Datentyp :  float_





#### Attribut  MEA_PERIOD
_Messperiode._

_Datentyp :  range_





### Klasse Contour_Lines_Hydro_L (Pcon){#contour-lines-hydro-l}
In der Klasse [Contour_Lines_Hydro_L](#contour-lines-hydro-l) befinden sich die Isohypsen, die sich auf das Grundwasser
beziehen.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**CONFINE**                 | [CD](#contour-lines-hydro-l-confine)  | Druckzustand im Grundwasserleiter.. | [0..1]
**ALTITUDE**                 | float                  | Höhenangabe (m ü.M.) von Isohypsen. | [1]
**WA_TABLE**                 | [CD](#contour-lines-hydro-l-wa-table)  | Wasserstand.. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14001001 | Isohypse des Grundwasserspiegels | Pcoh Isohypse des Grundwasserspiegels     |




#### Attribut  CONFINE {#contour-lines-hydro-l-confine}
_Druckzustand im Grundwasserleiter._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14002001 | frei | frei     |
|14002002 | gespannt | gespannt     |
|14002003 | artesisch | artesisch     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  ALTITUDE
_Höhenangabe (m ü.M.) von Isohypsen._

_Datentyp :  float_





#### Attribut  WA_TABLE {#contour-lines-hydro-l-wa-table}
_Wasserstand._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14004001 | mittlere Höhe des Niedrigwasserstands | mittlere Höhe des Niedrigwasserstands     |
|14004002 | mittlere Höhe des Hochwasserstands | mittlere Höhe des Hochwasserstands     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |








## Thema ANTHROPOGENIC_FEATURES

### Klasse Archaeology_PT (Aarc){#archaeology-pt}
Die Klasse [Archaeology_PT](#archaeology-pt) enthält Objektarten zu einzelnen archäologischen Relikten.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | []
**EPOCH**                 | [CD](#archaeology-pt-epoch)  | Archäologische Epoche der Objektart. | [0..1]
**PERIOD**                 | [CD](#archaeology-pt-period)  | Archäologische Periode der Objektart.. | [0..1]
**AGE**                 | [CD](#archaeology-pt-age)  | Archäologisches Alter der Objektart.. | [0..1]
**TYPE**                 | [CD](#archaeology-pt-type)  | Art des Kultsteins.. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10101001 | archäologische Fundstelle, Anlage, Siedlungsreste | Aarc archäologische Fundstelle, Anlage, Siedlungsreste     |
|10101005 | Gräber, Gräberfeld | Aarc Gräber, Gräberfeld     |
|10101007 | Grabhügel, Dolmengrab | Aarc Grabhügel, Dolmengrab     |
|10101008 | Kultstein | Aarc Kultstein     |
|10101009 | Kalkofen | Aarc Kalkofen     |
|10101010 | Felsenkeller | Aarc Felsenkeller     |
|10101011 | Schlackenhalde | Aarc Schlackenhalde     |
|10101012 | Glashütte | Aarc Glashütte     |
|10101013 | Schmelzofen | Aarc Schmelzofen     |
|10101004 | Burgstelle, Burghügel, Wachtturm | Aarc Burgstelle, Burghügel, Wachtturm     |
|10101002 | Höhlensiedlung, Abri | Aarc Höhlensiedlung, Abri     |
|10101003 | Pfahlbauten | Aarc Pfahlbauten     |
|10101006 | Steinplattengrab | Aarc Steinplattengrab     |
|10101015 | Abbaustelle | Aarc Abbaustelle     |




#### Attribut  EPOCH {#archaeology-pt-epoch}
_Archäologische Epoche der Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10002001 | historisch | historisch     |
|10002002 | prähistorisch | prähistorisch     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  PERIOD {#archaeology-pt-period}
_Archäologische Periode der Objektart._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10003001 | Neuzeit | Neuzeit     |
|10003002 | Mittelalter | Mittelalter     |
|10003003 | Römerzeit | Römerzeit     |
|10003004 | Eisenzeit | Eisenzeit     |
|10003005 | Bronzezeit | Bronzezeit     |
|10003006 | Steinzeit | Steinzeit     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  AGE {#archaeology-pt-age}
_Archäologisches Alter der Objektart._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10004001 | Latènezeit | Latènezeit     |
|10004002 | Hallstattzeit | Hallstattzeit     |
|10004003 | Jungbronzezeit | Jungbronzezeit     |
|10004004 | Mittelbronzezeit | Mittelbronzezeit     |
|10004005 | Altbronzezeit | Altbronzezeit     |
|10004006 | Neolithikum | Neolithikum     |
|10004007 | Mesolithikum | Mesolithikum     |
|10004008 | Paläolithikum | Paläolithikum     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  TYPE {#archaeology-pt-type}
_Art des Kultsteins._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10105001 | Menhir | Menhir     |
|10105002 | Schalenstein | Schalenstein     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




### Klasse Archaeology_L (Aarc){#archaeology-l}
Die Klasse [Archaeology_L](#archaeology-l) umfasst linienförmige archäologische Elemente. Historische Strassen,
Hohlwege oder Befestigungsgräben sind Teile dieser Klasse.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | []
**EPOCH**                 | [CD](#archaeology-l-epoch)  | Archäologische Epoche der Objektart. | [0..1]
**PERIOD**                 | [CD](#archaeology-l-period)  | Archäologische Periode der Objektart.. | [0..1]
**AGE**                 | [CD](#archaeology-l-age)  | Archäologisches Alter der Objektart.. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10201001 | Verkehrsweg | Aarc Verkehrsweg     |
|10201002 | Hohlweg | Aarc Hohlweg     |
|10201003 | künstlicher Graben, Befestigungsgraben | Aarc künstlicher Graben, Befestigungsgraben     |
|10201004 | künstlicher Erdwall | Aarc künstlicher Erdwall     |
|10201005 | Wasserleitung | Aarc Wasserleitung     |
|10201006 | Steinreihe | Aarc Steinreihe     |
|10201007 | Schützengraben | Aarc Schützengraben     |




#### Attribut  EPOCH {#archaeology-l-epoch}
_Archäologische Epoche der Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10002001 | historisch | historisch     |
|10002002 | prähistorisch | prähistorisch     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  PERIOD {#archaeology-l-period}
_Archäologische Periode der Objektart._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10003001 | Neuzeit | Neuzeit     |
|10003002 | Mittelalter | Mittelalter     |
|10003003 | Römerzeit | Römerzeit     |
|10003004 | Eisenzeit | Eisenzeit     |
|10003005 | Bronzezeit | Bronzezeit     |
|10003006 | Steinzeit | Steinzeit     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  AGE {#archaeology-l-age}
_Archäologisches Alter der Objektart._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10004001 | Latènezeit | Latènezeit     |
|10004002 | Hallstattzeit | Hallstattzeit     |
|10004003 | Jungbronzezeit | Jungbronzezeit     |
|10004004 | Mittelbronzezeit | Mittelbronzezeit     |
|10004005 | Altbronzezeit | Altbronzezeit     |
|10004006 | Neolithikum | Neolithikum     |
|10004007 | Mesolithikum | Mesolithikum     |
|10004008 | Paläolithikum | Paläolithikum     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




### Klasse Archaeology_PLG (Aarc){#archaeology-plg}
Die Klasse [Archaeology_PLG](#archaeology-plg) beinhaltet archäologische Relikte (z.B. römisches Castrum), die ein
grösseres Gebiet (Fläche) abdecken.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | []
**EPOCH**                 | [CD](#archaeology-plg-epoch)  | Archäologische Epoche der Objektart. | [0..1]
**PERIOD**                 | [CD](#archaeology-plg-period)  | Archäologische Periode der Objektart.. | [0..1]
**AGE**                 | [CD](#archaeology-plg-age)  | Archäologisches Alter der Objektart.. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10301001 | Castrum | Aarc Castrum     |
|10301002 | Refugium, Höhensiedlung, Erdwerk | Aarc Refugium, Höhensiedlung, Erdwerk     |




#### Attribut  EPOCH {#archaeology-plg-epoch}
_Archäologische Epoche der Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10002001 | historisch | historisch     |
|10002002 | prähistorisch | prähistorisch     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  PERIOD {#archaeology-plg-period}
_Archäologische Periode der Objektart._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10003001 | Neuzeit | Neuzeit     |
|10003002 | Mittelalter | Mittelalter     |
|10003003 | Römerzeit | Römerzeit     |
|10003004 | Eisenzeit | Eisenzeit     |
|10003005 | Bronzezeit | Bronzezeit     |
|10003006 | Steinzeit | Steinzeit     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  AGE {#archaeology-plg-age}
_Archäologisches Alter der Objektart._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10004001 | Latènezeit | Latènezeit     |
|10004002 | Hallstattzeit | Hallstattzeit     |
|10004003 | Jungbronzezeit | Jungbronzezeit     |
|10004004 | Mittelbronzezeit | Mittelbronzezeit     |
|10004005 | Altbronzezeit | Altbronzezeit     |
|10004006 | Neolithikum | Neolithikum     |
|10004007 | Mesolithikum | Mesolithikum     |
|10004008 | Paläolithikum | Paläolithikum     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




### Klasse Exploitation_Geomaterials_PT (Aexp){#exploitation-geomaterials-pt}
Die Klasse [Exploitation_Geomaterials_PT](#exploitation-geomaterials-pt) enthält punktförmige Angaben zu Abbaustellen von
Geomaterialien.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | []
**EXP_UNIT**                 | [ Tabelle ](#gc-geol-mapping-unit-cd)  | Abgebaute lithostratigraphische Einheit.. | [0..*]
**STATUS**                 | [CD](#exploitation-geomaterials-pt-status)  | Abbaustatus.. | [0..1]
**DEPTH_TOT**                 | float                  | Endtiefe (m ab Terrainoberfläche) der Objektart. | [0..1]
**TARG_MAT**                 | [CD](#exploitation-geomaterials-pt-targ-mat)  | Abgebautes Material.. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10601001 | Bergwerk, Untertageabbau | Aexp Bergwerk, Untertageabbau     |
|10601002 | Stolleneingang | Aexp Stolleneingang     |
|10601003 | Schacht | Aexp Schacht     |
|10601004 | Pinge (dolinenartiger Stolleneinbruch) | Aexp Pinge (dolinenartiger Stolleneinbruch)     |
|10601005 | Schürfloch | Aexp Schürfloch     |
|10601006 | ausgeräumte Bohnerztasche | Aexp ausgeräumte Bohnerztasche     |




#### Attribut  EXP_UNIT
_Abgebaute lithostratigraphische Einheit._

Siehe [GC_GEOL_MAPPING_UNIT_CD](#gc-geol-mapping-unit-cd) in der Anhang





#### Attribut  STATUS {#exploitation-geomaterials-pt-status}
_Abbaustatus._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10603001 | in Betrieb | in Betrieb     |
|10603002 | stillgelegt | stillgelegt     |
|10603003 | aufgefüllt | aufgefüllt     |
|10603004 | verfallen | verfallen     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  DEPTH_TOT
_Endtiefe (m ab Terrainoberfläche) der Objektart._

_Datentyp :  float_





#### Attribut  TARG_MAT {#exploitation-geomaterials-pt-targ-mat}
_Abgebautes Material._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10605001 | Erze allgemein | Erze allgemein     |
|10605002 | Gold | Gold     |
|10605003 | Silber | Silber     |
|10605004 | Kupfer, z.T. mit Silber, Wismut und Arsen | Kupfer, z.T. mit Silber, Wismut und Arsen     |
|10605005 | Eisen / Eisenoolith | Eisen / Eisenoolith     |
|10605006 | Blei-Zink | Blei-Zink     |
|10605007 | Chrom-Nickel, z.T. mit Kobalt | Chrom-Nickel, z.T. mit Kobalt     |
|10605008 | Mangan | Mangan     |
|10605009 | Molybdän und Wolfram | Molybdän und Wolfram     |
|10605010 | Antimon | Antimon     |
|10605011 | Baryt | Baryt     |
|10605012 | Kalzit | Kalzit     |
|10605013 | Fluorit | Fluorit     |
|10605014 | Quarz | Quarz     |
|10605015 | Kaolin | Kaolin     |
|10605016 | Magnesit | Magnesit     |
|10605017 | Magnesium | Magnesium     |
|10605018 | Phosphorit, Apatit | Phosphorit, Apatit     |
|10605019 | Talk | Talk     |
|10605020 | Schwefel | Schwefel     |
|10605021 | Uran | Uran     |
|10605022 | Bohnerz | Bohnerz     |
|10605023 | Asbest | Asbest     |
|10605024 | Kohle allgemein | Kohle allgemein     |
|10605025 | Steinkohle / Anthrazit | Steinkohle / Anthrazit     |
|10605026 | Lignit | Lignit     |
|10605027 | Graphit | Graphit     |
|10605028 | Ölschiefer | Ölschiefer     |
|10605029 | Asphalt / Bitumen | Asphalt / Bitumen     |
|10605030 | Hartgestein | Hartgestein     |
|10605031 | Dachschiefer / Tafelschiefer | Dachschiefer / Tafelschiefer     |
|10605032 | Serpentin | Serpentin     |
|10605033 | Speckstein | Speckstein     |
|10605034 | Gips | Gips     |
|10605035 | Salz / Steinsalz | Salz / Steinsalz     |
|10605036 | Ton / Ton und Silt (Lehm) | Ton / Ton und Silt (Lehm)     |
|10605037 | Sand | Sand     |
|10605038 | Sand und Kies | Sand und Kies     |
|10605039 | Pyrit | Pyrit     |
|10605040 | Kies | Kies     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




### Klasse Exploitation_Geomaterials_L (Aexp){#exploitation-geomaterials-l}
Die Klasse [Exploitation_Geomaterials_L](#exploitation-geomaterials-l) beinhaltet linienförmige Informationen zum Abbau von
Geomaterialien (z.B. Verlauf der Abbaufront).




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | []
**STATUS**                 | [CD](#exploitation-geomaterials-l-status)  | Abbaustatus.. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10701001 | Abbaufront | Aexp Abbaufront     |
|10701002 | Bergwerksstollen | Aexp Bergwerksstollen     |




#### Attribut  STATUS {#exploitation-geomaterials-l-status}
_Abbaustatus._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10702001 | in Betrieb | in Betrieb     |
|10702002 | stillgelegt | stillgelegt     |
|10702003 | aufgefüllt | aufgefüllt     |
|10702004 | verfallen | verfallen     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




### Klasse Exploitation_Geomaterials_PLG (Aexp){#exploitation-geomaterials-plg}
Die Klasse [Exploitation_Geomaterials_PLG](#exploitation-geomaterials-plg) enthält Flächen, wo zur Zeit der geologischen
Aufnahmen Geomaterialien abgebaut wurden.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | []
**EXP_UNIT**                 | [ Tabelle ](#gc-geol-mapping-unit-cd)  | Abgebaute lithostratigraphische Einheit.. | [1..*]
**STATUS**                 | [CD](#exploitation-geomaterials-plg-status)  | Abbaustatus.. | [0..1]
**DEPTH_TOT**                 | float                  | Endtiefe (m ab Terrainoberfläche) der Objektart. | [0..1]
**TARG_MAT**                 | [CD](#exploitation-geomaterials-plg-targ-mat)  | Abgebautes Material.. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10801001 | Steinbruch | Aexp Steinbruch     |
|10801002 | Grube (Lockergesteinsabbau) | Aexp Grube (Lockergesteinsabbau)     |




#### Attribut  EXP_UNIT
_Abgebaute lithostratigraphische Einheit._

Siehe [GC_GEOL_MAPPING_UNIT_CD](#gc-geol-mapping-unit-cd) in der Anhang





#### Attribut  STATUS {#exploitation-geomaterials-plg-status}
_Abbaustatus._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10802001 | in Betrieb | in Betrieb     |
|10802002 | stillgelegt | stillgelegt     |
|10802003 | aufgefüllt | aufgefüllt     |
|10802004 | verfallen | verfallen     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  DEPTH_TOT
_Endtiefe (m ab Terrainoberfläche) der Objektart._

_Datentyp :  float_





#### Attribut  TARG_MAT {#exploitation-geomaterials-plg-targ-mat}
_Abgebautes Material._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10804001 | Ton / Ton und Silt (Lehm) | Ton / Ton und Silt (Lehm)     |
|10804002 | Sand | Sand     |
|10804003 | Sand und Kies | Sand und Kies     |
|10804004 | Hartgestein | Hartgestein     |
|10804005 | Dachschiefer / Tafelschiefer | Dachschiefer / Tafelschiefer     |
|10804006 | Gips | Gips     |
|10804007 | Serpentin | Serpentin     |
|10804008 | Speckstein | Speckstein     |
|10804009 | Talk | Talk     |
|10804010 | Baryt | Baryt     |
|10804011 | Kalzit / Kalk | Kalzit / Kalk     |
|10804012 | Eisen / Eisenoolithe | Eisen / Eisenoolithe     |
|10804013 | Kaolin | Kaolin     |
|10804014 | Quarz / Quarzit | Quarz / Quarzit     |
|10804015 | Asbest | Asbest     |
|10804016 | Bohnerz | Bohnerz     |
|10804017 | Torf | Torf     |
|10804018 | Mergel | Mergel     |
|10804019 | Kohle | Kohle     |
|10804020 | Salz / Steinsalz | Salz / Steinsalz     |
|10804021 | Kies | Kies     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




### Klasse Boreholes_PT (Abor){#boreholes-pt}
Die Klasse [Boreholes_PT](#boreholes-pt) beinhaltet Bohrungen und Sondierungen. (Auf alten gedruckten Karten
wurde die Art der Sondierung nicht immer unterschieden. Es kann daher sein, dass in alten Karten
Rammkernsondierungen als Bohrungen aufgenommen wurden.)




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | []
**DEPTH_BEDR**                 | float                  | Tiefe (in Meter ab Terrainoberfläche) der Felsoberfläche. (Sofern die Bohrung das Festgestein nicht erreicht, z.B. «Bohrung, Fels nicht erreicht», beträgt der Wert 999, falls die Bohrung bereits im Festgestein beginnt, beträgt der Wert 0). Falls Festgestein erreicht wurde, aber nicht klar ist, dass es sich um die Felsoberfläche handelt, beträgt der Wert 888. | [0..1]
**D_C_UNDERG**                 | boolean                  | Bohransatzpunkt unter Terrain (ja / nein) | [1]
**MAIN_TAR**                 | [CD](#boreholes-pt-main-tar)  | Ziel der Sondierung.. | [0..1]
**TARG_MAT**                 | [CD](#boreholes-pt-targ-mat)  | Durch die Sondierung gefördertes Material.. | [0..1]
**DEPTH_TOT**                 | float                  | Gemessene Länge (Measured Depth) der Bohrung. Vgl. DM Bohrdaten. Die tatsächliche Tiefe (True Vertical Depth) ist oft nicht bekannt. | [0..1]
**DEPTH_FM_A**                 | [ Tabelle ](#gc-geol-mapping-unit-cd)  | Lithostratigraphische Einheit der erreichten Formation A. | [0..1]
**DEPTH_FM_B**                 | float                  | Tiefe (m ab Terrainoberfläche) der erreichten Formation B. | [0..1]
**FM_A**                 | [ Tabelle ](#gc-geol-mapping-unit-cd)  | Lithostratigraphische Einheit der erreichten Formation A. | [0..1]
**DEPTH_FM_B**                 | float                  | Tiefe (m ab Terrainoberfläche) der erreichten Formation B. | [0..1]
**DEPTH_WT**                 | float                  | Tiefe (m ab Terrainoberfläche) des Grundwasserspiegels. | [0..1]
**AZIMUTH**                 | integer                  | Fallrichtung (Azimut) der jeweiligen Punktobjektart. Wert in Grad (0° 359°) im Uhrzeigersinn gemessen. | [0..1]
**DIP**                 | integer                  | Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die Vertikale (90°). | [0..1]
**REF_NUMBER**                 | integer                  | Bohrungs-ID der Objektart in einem zusätzlichen Dokument (Erläuterungen, ...). | [0..1]
**LITHO**                 | [ Tabelle ](#gc-litho-unco-cd)  | Erreichte lithologische Einheit (im Falle von Bohrungen, die den Fels nicht erreicht haben). | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10501001 | Bohrung | Abor Bohrung     |
|10501002 | Sondierschlitz | Abor Sondierschlitz     |
|10501003 | Handsondierung | Abor Handsondierung     |
|10501004 | Rammsondierung | Abor Rammsondierung     |
|10501005 | Rammkernsondierung | Abor Rammkernsondierung     |




#### Attribut  DEPTH_BEDR
_Tiefe (in Meter ab Terrainoberfläche) der Felsoberfläche. (Sofern die Bohrung das Festgestein nicht erreicht, z.B. «Bohrung, Fels nicht erreicht», beträgt der Wert 999, falls die Bohrung bereits im Festgestein beginnt, beträgt der Wert 0). Falls Festgestein erreicht wurde, aber nicht klar ist, dass es sich um die Felsoberfläche handelt, beträgt der Wert 888._

_Datentyp :  float_





#### Attribut  D_C_UNDERG
_Bohransatzpunkt unter Terrain (ja / nein)_

_Datentyp :  boolean_





#### Attribut  MAIN_TAR {#boreholes-pt-main-tar}
_Ziel der Sondierung._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10505001 | Geotechnik | Geotechnik     |
|10505002 | Hydrogeologie | Hydrogeologie     |
|10505004 | mineralische Rohstoffe | mineralische Rohstoffe     |
|10505005 | Kohlenwasserstoffe | Kohlenwasserstoffe     |
|10505006 | belasteter Standort | belasteter Standort     |
|10505007 | Seismik | Seismik     |
|10505008 | Geothermie | Geothermie     |
|10505012 | Forschung | Forschung     |
|10505013 | Naturgefahren | Naturgefahren     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  TARG_MAT {#boreholes-pt-targ-mat}
_Durch die Sondierung gefördertes Material._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10506001 | Salz / Steinsalz | Salz / Steinsalz     |
|10506002 | Erdöl | Erdöl     |
|10506003 | Erdgas | Erdgas     |
|10506004 | Erdwärme | Erdwärme     |
|10506005 | Thermalwasser | Thermalwasser     |
|10506006 | Grundwasser | Grundwasser     |
|10506007 | Mineralwasser | Mineralwasser     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  DEPTH_TOT
_Gemessene Länge (Measured Depth) der Bohrung. Vgl. DM Bohrdaten. Die tatsächliche Tiefe (True Vertical Depth) ist oft nicht bekannt._

_Datentyp :  float_





#### Attribut  DEPTH_FM_A
_Lithostratigraphische Einheit der erreichten Formation A_

Siehe [GC_GEOL_MAPPING_UNIT_CD](#gc-geol-mapping-unit-cd) in der Anhang





#### Attribut  DEPTH_FM_B
_Tiefe (m ab Terrainoberfläche) der erreichten Formation B._

_Datentyp :  float_





#### Attribut  FM_A
_Lithostratigraphische Einheit der erreichten Formation A_

Siehe [GC_GEOL_MAPPING_UNIT_CD](#gc-geol-mapping-unit-cd) in der Anhang





#### Attribut  DEPTH_FM_B
_Tiefe (m ab Terrainoberfläche) der erreichten Formation B._

_Datentyp :  float_





#### Attribut  DEPTH_WT
_Tiefe (m ab Terrainoberfläche) des Grundwasserspiegels._

_Datentyp :  float_





#### Attribut  AZIMUTH
_Fallrichtung (Azimut) der jeweiligen Punktobjektart. Wert in Grad (0° 359°) im Uhrzeigersinn gemessen._

_Datentyp :  integer_





#### Attribut  DIP
_Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die Vertikale (90°)._

_Datentyp :  integer_





#### Attribut  REF_NUMBER
_Bohrungs-ID der Objektart in einem zusätzlichen Dokument (Erläuterungen, ...)._

_Datentyp :  integer_





#### Attribut  LITHO
_Erreichte lithologische Einheit (im Falle von Bohrungen, die den Fels nicht erreicht haben)_

Siehe [GC_LITHO_UNCO_CD](#gc-litho-unco-cd) in der Anhang





### Klasse Artificial_Surface_Modifications_PLG (Aart){#artificial-surface-modifications-plg}
Die Klasse [Artificial_Surface_Modifications_PLG](#artificial-surface-modifications-plg) enthält bedeutende künstliche Veränderungen
des Geländes (Golfplatz, Skigebiet, etc.), die zur Folge haben, dass das ursprüngliche Relief nicht
mehr zu erkennen ist, was bei einer geomorphologischen Deutung zu falschen Schlüssen führen könnte.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10401001 | künstlich verändertes Gelände | Aart künstlich verändertes Gelände     |
|10401002 | künstliche Ablagerung, undifferenziert | Aart künstliche Ablagerung, undifferenziert     |
|10401003 | Aufschüttung, Damm | Aart Aufschüttung, Damm     |
|10401004 | Auffüllung | Aart Auffüllung     |
|10401005 | Deponie | Aart Deponie     |
|10401006 | Halde | Aart Halde     |








## Thema HYDROGEOLOGY

### Klasse Construction_PT (Hcon){#construction-pt}
Die Klasse [Construction_PT](#construction-pt) beinhaltet Wasserbauten wie Grundwasserfassungen und Zisternen.
Desweiteren kommen in dieser Klasse auch Messgeräte wie Piezometer und Limnigraphen vor.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**STATUS**                 | [CD](#construction-pt-status)  | Zustand der Objektart.. | [0..1]
**EPOCH**                 | [CD](#construction-pt-epoch)  | Epoche der Erbauung der Objektart.. | [0..1]
**DEPTH**                 | float                  | Tiefe der Objektart (m ab Terrainoberfläche). | [0..1]
**DEPTH_WT**                 | float                  | Tiefe (m ab Terrainoberfläche) des Grundwasserspiegels (Mittelwert). | [0..1]
**MEA_PERIOD**                 | range                  | Messperiode. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12101001 | Grundwasserfassung | Hcon Grundwasserfassung     |
|12101002 | Zisterne | Hcon Zisterne     |
|12101003 | laufender Brunnen (in wasserarmem Gebiet) | Hcon laufender Brunnen (in wasserarmem Gebiet)     |
|12101004 | Sodbrunnen | Hcon Sodbrunnen     |
|12101005 | Versickerungsschacht | Hcon Versickerungsschacht     |
|12101006 | Limnigraph | Hcon Limnigraph     |
|12101007 | Piezometer | Hcon Piezometer     |




#### Attribut  STATUS {#construction-pt-status}
_Zustand der Objektart._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12102001 | in Betrieb | in Betrieb     |
|12102002 | stillgelegt | stillgelegt     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  EPOCH {#construction-pt-epoch}
_Epoche der Erbauung der Objektart._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12103001 | Mittelalter | Mittelalter     |
|12103002 | Römerzeit | Römerzeit     |
|12103003 | prähistorisch | prähistorisch     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  DEPTH
_Tiefe der Objektart (m ab Terrainoberfläche)._

_Datentyp :  float_





#### Attribut  DEPTH_WT
_Tiefe (m ab Terrainoberfläche) des Grundwasserspiegels (Mittelwert)._

_Datentyp :  float_





#### Attribut  MEA_PERIOD
_Messperiode._

_Datentyp :  range_





### Klasse Construction_L (Hcon){#construction-l}
Die Klasse [Construction_L](#construction-l) enthält linienförmige Wasserbauten wie den Wasserfassungsstollen,
welcher mit Objektarten der Klasse [Surface_Water_PT](#surface-water-pt) kombiniert werden kann.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**COMBI**                 | [CD](#construction-l-combi)  | Objektart einer anderen Klasse, die mit der Objektart in Kombination vorkommen kann. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12201001 | Wasserfassungsstollen | Hcon Wasserfassungsstollen     |
|12201002 | künstlicher Gewässerlauf | Hcon künstlicher Gewässerlauf     |




#### Attribut  COMBI {#construction-l-combi}
_Objektart einer anderen Klasse, die mit der Objektart in Kombination vorkommen kann_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12202001 | mit Quellfassung (orientiert) in Stollen | mit Quellfassung (orientiert) in Stollen     |
|12202002 | mit gefasster Mineralquelle (orientiert) in Stollen | mit gefasster Mineralquelle (orientiert) in Stollen     |
|12202003 | mit gefasster Thermalquelle (orientiert) in Stollen | mit gefasster Thermalquelle (orientiert) in Stollen     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




### Klasse Palaeohydrology_L (Hpal){#palaeohydrology-l}
In der Klasse [Palaeohydrology_L](#palaeohydrology-l) befinden sich alle linienförmigen Objektarten, welche einen
gewissen Bezug zu einem ehemaligen Gewässer aufweisen.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**REL_AGE**                 | [CD](#palaeohydrology-l-rel-age)  | Relatives Alter der Objektart. | [0..1]
**CHRONO**                 | [ Tabelle ](#gc-chrono-cd)  | Chronostratigraphische Zuordnung.. | [0..1]
**REF_YEAR**                 | integer                  | Referenzjahr der ehemaligen Uferlinie. | [1]
**SOURCE**                 | string                  | Datenquelle der historischen Unterlagen. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12301001 | Paläotal | Hpal Paläotal     |
|12301002 | ehemalige Entwässerungsrinne | Hpal ehemalige Entwässerungsrinne     |
|12301004 | Trockental | Hpal Trockental     |
|12301005 | ehemaliges Bachbett | Hpal ehemaliges Bachbett     |
|12301006 | Ufer eines ehemaligen Flussbetts | Hpal Ufer eines ehemaligen Flussbetts     |
|12301007 | ehemalige Uferlinie | Hpal ehemalige Uferlinie     |
|12301003 | ehemalige glaziale Abflussrinne | Hpal ehemalige glaziale Abflussrinne     |




#### Attribut  REL_AGE {#palaeohydrology-l-rel-age}
_Relatives Alter der Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12302001 | die Jüngste oder Einzige | die Jüngste oder Einzige     |
|12302002 | älter als die Jüngste | älter als die Jüngste     |
|12302003 | älter als die Zweitjüngste | älter als die Zweitjüngste     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  CHRONO
_Chronostratigraphische Zuordnung._

Siehe [GC_CHRONO_CD](#gc-chrono-cd) in der Anhang





#### Attribut  REF_YEAR
_Referenzjahr der ehemaligen Uferlinie._

_Datentyp :  integer_





#### Attribut  SOURCE
_Datenquelle der historischen Unterlagen._

_Datentyp :  string_





### Klasse Subsurface_Water_L (Hsub){#subsurface-water-l}
In der Klasse [Subsurface_Water_L](#subsurface-water-l) befinden sich linienförmigen Objektarten, welche einen
unterirdischen Gewässerlauf anzeigen.

Der genaue Verlauf des unterirdischen Gewässerlaufes ist meistens vermutet.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**COMBI**                 | [CD](#subsurface-water-l-combi)  | Objektart einer anderen Klasse, die mit der Objektart in Kombination vorkommen kann. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12401001 | unterirdischer Gewässerlauf | Hsub unterirdischer Gewässerlauf     |




#### Attribut  COMBI {#subsurface-water-l-combi}
_Objektart einer anderen Klasse, die mit der Objektart in Kombination vorkommen kann_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12402001 | mit Versickerungsstelle eines Baches | mit Versickerungsstelle eines Baches     |
|12402002 | mit Wiederaustritt eines unterirdischen Bachlaufes | mit Wiederaustritt eines unterirdischen Bachlaufes     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




### Klasse Surface_Water_PT (Hsur){#surface-water-pt}
Die Klasse [Surface_Water_PT](#surface-water-pt) umfasst lokal (punktuell) beobachtete Oberflächengewässer, wie
natürliche Wasseraustritts- und Versickerungsstellen. Zudem befindet sich die Objektart Steilstufe
in Bachrinne, Wasserfall in dieser Klasse, die eine spezielle Stelle in Fliessgewässern markiert und
die durch die darunterliegende Geologie bedingt ist.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]
**STATUS**                 | [CD](#surface-water-pt-status)  | Zustand der Objektart.. | [0..1]
**FLOW_CON**                 | [CD](#surface-water-pt-flow-con)  | Wasserfluss Bedingungen.. | [0..1]
**TYPE**                 | [CD](#surface-water-pt-type)  | Charakteristik der Objektart. | [0..1]
**DIS_LOCA**                 | [CD](#surface-water-pt-dis-loca)  | Ort des Wasserausflusses.. | [0..1]
**COMBI**                 | [CD](#surface-water-pt-combi)  | Objektart einer anderen Klasse, die mit der Objektart in Kombination vorkommen kann. | [0..1]
**TEMP**                 | integer                  | Mittlere Wassertemperatur (°C). | [0..1]
**CHEMISTRY**                 | string                  | Charakteristisches chemisches Element im Mineralwasser (z.B. Fe). | [0..1]
**AZIMUTH**                 | integer                  | Richtung (Azimut) der jeweiligen Punktobjektart. Wert in Grad (0° bis 359°) im Uhrzeigersinn gemessen. | [0..1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12501001 | Quelle | Hsur Quelle     |
|12501002 | diffuse Quelle | Hsur diffuse Quelle     |
|12501003 | Wiederaustritt eines unterirdischen Bachlaufes | Hsur Wiederaustritt eines unterirdischen Bachlaufes     |
|12501004 | Versickerungsstelle eines Baches | Hsur Versickerungsstelle eines Baches     |
|12501005 | Steilstufe in Bachrinne, Wasserfall | Hsur Steilstufe in Bachrinne, Wasserfall     |
|12501006 | Grundwasseraufstoss | Hsur Grundwasseraufstoss     |




#### Attribut  STATUS {#surface-water-pt-status}
_Zustand der Objektart._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12502001 | gefasst | gefasst     |
|12502002 | nicht gefasst | nicht gefasst     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  FLOW_CON {#surface-water-pt-flow-con}
_Wasserfluss Bedingungen._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12503001 | perennierend | perennierend     |
|12503002 | temporär | temporär     |
|12503003 | versiegt | versiegt     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  TYPE {#surface-water-pt-type}
_Charakteristik der Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12504001 | Karstquelle | Karstquelle     |
|12504002 | Mineralquelle | Mineralquelle     |
|12504003 | Thermalquelle | Thermalquelle     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  DIS_LOCA {#surface-water-pt-dis-loca}
_Ort des Wasserausflusses._


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12505002 | in Stollen | in Stollen     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  COMBI {#surface-water-pt-combi}
_Objektart einer anderen Klasse, die mit der Objektart in Kombination vorkommen kann_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12506001 | mit Wasserfassungsstollen | mit Wasserfassungsstollen     |
|12506002 | mit unterirdischem Gewässerlauf | mit unterirdischem Gewässerlauf     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |




#### Attribut  TEMP
_Mittlere Wassertemperatur (°C)._

_Datentyp :  integer_





#### Attribut  CHEMISTRY
_Charakteristisches chemisches Element im Mineralwasser (z.B. Fe)._

_Datentyp :  string_





#### Attribut  AZIMUTH
_Richtung (Azimut) der jeweiligen Punktobjektart. Wert in Grad (0° bis 359°) im Uhrzeigersinn gemessen._

_Datentyp :  integer_





### Klasse Surface_Water_L (Hsur){#surface-water-l}
In der Klasse [Surface_Water_L](#surface-water-l) sind linienförmige Oberflächengewässer (Quellhorizonte) beschrieben.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12601001 | Quellhorizont | Hsur Quellhorizont     |
|12601002 | Bachlauf | Hsur Bachlauf     |




### Klasse Surface_Water_PLG (Hsur){#surface-water-plg}
Die Klasse [Surface_Water_PLG](#surface-water-plg) beinhaltet oberflächliche Wasserspeicher wie Gletscher, Seen und
Flüsse.




Name             | Typ | Beschreibung                             |  Kard.
--------------------------|------------|-----------------------------------------------------|-----
**KIND**                 | subtype                  | Objektart | [1]





#### Attribut  KIND
_Objektart_


|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12701001 | Gletscher | Hsur Gletscher     |
|12701002 | See | Hsur See     |
|12701003 | Fluss | Hsur Fluss     |









\blandscape


## Anhang  GC_GEOL_MAPPING_UNIT_ATT {#gc-geol-mapping-unit-att}
Kartiereinheiten



| Code    |  GMU      |Litho main | Litho sec | Litho ter |  Formation | Chrono top | Chrono base | Correlation |
|---------|-----------|-----------|-----------|------------|------------|-------------|-------------|
|15202091 |Öhrli-Fm. | Kalkstein: Bioklasten-Ooide  | Kalkstein: sandig   | Mergelstein |  Öhrli-Formation |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202092 |Palfris-Fm. | Mergelstein: schiefrig  | Tonstein: schiefrig   | Kalkstein: Bioklasten |  Palfris-Formation |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202093 |Zementstein-Fm. | Mergelstein  | Kalkstein: mergelig   | Kalkstein: mikritisch |  15253121 |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202094 |Zementstein-Fm.: Grasspass-Mb. | Brekzie: kalkig  | Brekzie: dolomitisch   | Mergelstein |  Graspass-Member |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202095 |Zementstein-Fm.: Gassen-Kalk | Kalkstein: arenitisch-spätig  | Kalkstein: mikritisch   | – |  Gassen-Kalk |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202096 |Helvetikum: Malm | Kalkstein  | Mergelstein   | – |  – |  Berriasien     | Callovien   | Malm  |
|15202097 |Quinten-Fm. | Kalkstein: mikritisch  | –   | – |  Quinten-Formation |  Berriasien     | Oxfordien   | Malm  |
|15202098 |Quinten-Fm.: Tros-Kalk | Kalkstein: Korallen  | Kalkstein: Ooide   | – |  Tros-Kalk |  Berriasien     | Tithonien   | Malm  |
|15202099 |Quinten-Fm.: Mergelband | Mergelstein  | Kalkstein: mergelig   | – |  «Mergelband» (Quinten-Fm.) |  Kimméridgien     | Kimméridgien   | Malm  |
|15202100 |Schilt-Fm. | Kalkstein  | Mergelstein   | – |  Schilt-Formation |  Oxfordien     | Callovien   | Malm  |
|15202101 |Schilt-Fm.: Mürtschen-Mb. | Mergelstein: schiefrig  | Kalkstein: mikritisch   | – |  Mürtschen-Member |  Oxfordien     | Oxfordien   | Malm  |
|15202102 |Schilt-Fm.: Mergelstein-dominierte Fazies | Mergelstein: schiefrig  | Mergelstein: kalkig   | – |  Schilt-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15202103 |Schilt-Fm.: Kalkstein-dominierte Fazies | Kalkstein  | –   | – |  Schilt-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15202104 |Schilt-Fm.: Seeztal-Mb. | Siltstein: mergelig  | Kalkstein: spätig: Bioklasten   | – |  Seeztal-Member |  Oxfordien     | Callovien   | Malm  |
|15202105 |Schilt-Fm.: Windgällen-Mb. | Kalkstein: mergelig  | Tonstein   | – |  Windgällen-Member |  Oxfordien     | Oxfordien   | Malm  |
|15202106 |Helvetikum: Dogger | Kalkstein  | Mergelstein   | Sandstein |  – |  Oxfordien     | Toarcien   | Syn-Rift  |
|15202107 |Erzegg-Fm. | Tonstein: schiefrig  | Mergelstein: schiefrig   | – |  Erzegg-Formation |  Oxfordien     | Bajocien   | Lias-Dogger in pelagischer Fazies  |
|15202108 |Reischiben-Fm. | Kalkstein: spätig: Bioklasten-Chert  | Kalkstein: sandig   | Kalkstein: mergelig |  Reischiben-Formation |  Bathonien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15202109 |Reischiben-Fm.: Blegi-Eisenoolith | Kalkstein: Eisenooide  | –   | – |  Blegi-Eisenoolith |  Callovien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15202110 |Reischiben-Fm.: Bannalp-Konglomerat | Mergelstein: dolomitisch  | Konglomerat   | – |  Bannalp-Konglomerat |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15202111 |Reischiben-Fm.: Guppen-Fossilhorizont | Kalkstein: Bioklasten  | –   | – |  Guppen-Fossilhorizont |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15202112 |Reischiben-Fm.: Gursbach-Fossilhorizont | Kalkstein: Bioklasten  | –   | – |  Gursbach-Fossilhorizont |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15202113 |Hochstollen-Fm. | Kalkstein: sandig-spätig  | Mergelstein: sandig   | – |  Hochstollen-Formation |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15202114 |Hochstollen-Fm.: Schwarzhorn-Mb. | Kalkstein: sandig-kieselig  | Mergelstein   | Kalkstein: spätig: Bioklasten |  Schwarzhorn-Member |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15202115 |Hochstollen-Fm.: Bietenhorn-Mb. | Mergelstein: siltig  | Tonstein: schiefrig   | Kalkstein: sandig |  Bietenhorn-Member |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15202116 |Bommerstein-Fm. | Sandstein: Quarz  | Kalkstein: spätig: Bioklasten   | Tonstein: schiefrig |  Bommerstein-Formation |  Aalénien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15202117 |Bommerstein-Fm.: Mols-Mb. | Tonstein: schiefrig  | Kalkstein: spätig: Bioklasten   | – |  Mols-Member |  Aalénien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15202118 |Dugny-Fm. | Tonstein: siltig: Glimmer  | Siltstein   | – |  Dugny-Formation |  Aalénien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15202119 |Coroi-Fm. | Tonstein: schiefrig  | Siltstein   | Sandstein |  Coroi-Formation |  Aalénien     | Aalénien   | Syn-Rift  |
|15202120 |Helvetikum: Lias | Mergelstein  | Kalkstein   | Sandstein |  – |  Aalénien     | Rhät   | Lias-Dogger in neritischer Fazies  |
|15202121 |Brunnistock-Fm. | Kalkstein: sandig-spätig  | Tonstein   | – |  Brunnistock-Formation |  Toarcien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202122 |Inferno-Fm. | Kalkstein: mergelig-schiefrig  | Tonstein: schiefrig   | Kalkstein: spätig: Bioklasten |  Inferno-Formation |  Toarcien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202123 |Monts-Rosset-Fm. | Mergelstein  | Kalkstein: spätig: Bioklasten   | – |  Monts-Rosset-Formation |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15202124 |Torrenthorn-Fm.: Torrentalp-Mb. | Sandstein: kalkig-kieselig  | Kalkstein: mergelig   | Tonstein |  Torrentalp-Member |  Aalénien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202125 |Sexmor-Fm. | Kalkstein: spätig: Bioklasten  | Mergelstein   | Kalkstein: kieselig |  Sexmor-Formation |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202126 |Mont-Joly-Fm. | Kalkstein: kieselig  | Kalkstein: spätig: Bioklasten   | Kalkstein: sandig-tonig |  Mont-Joly-Formation |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202127 |Torrenthorn-Fm.: Galm-Mb. | Sandstein: kalkig-kieselig  | Kalkstein: sandig-spätig   | – |  Galm-Member |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202128 |Spitzmeilen-Fm. | Kalkstein: sandig  | Sandstein: kalkig   | Mergelstein |  Spitzmeilen-Formation |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202129 |Tierces-Fm. | Mergelstein  | Kalkstein: mikritisch   | Kalkstein: sandig-spätig |  Tierces-Formation |  Sinémurien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15202130 |Bachalp-Fm. | Mergelstein: kalkig  | Kalkstein: spätig   | – |  Bachalp-Formation |  Sinémurien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15202131 |Prodkamm-Fm. | Tonstein  | Mergelstein   | Sandstein: kalkig |  Prodkamm-Formation |  Sinémurien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15202132 |Prodkamm-Fm.: Cardinien-Mb. | Tonstein: schiefrig  | Sandstein: kalkig   | Kalkstein: Bioklasten |  «Cardinia-Member» |  Sinémurien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15202133 |Stgir-Fm. | Kalkstein: sandig  | Tonstein: schiefrig   | Sandstein: Quarz |  Stgir-Formation |  Sinémurien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15202134 |Helvetikum: Trias | Dolomitstein  | Sandstein   | Gestein: pelitisch |  – |  Rhät     | Olénékien   | Prä-Rift  |
|15202135 |Besoëns-Fm. | Sandstein: Quarz  | Kalkstein: sandig: Bioklasten   | Tonstein: schiefrig |  Besoëns-Formation |  Rhät     | Rhät   | «Rhät»  |
|15202136 |Quarten-Fm. | Tonstein: schiefrig  | Siltstein: schiefrig   | Dolomitstein |  Quarten-Formation |  Späte Trias     | Späte Trias   | Keuper  |
|15202137 |Arandellys-Fm. | Kalkstein: dolomitisch  | Dolomitstein   | Rauwacke |  Arandellys-Formation |  Späte Trias     | Mittlere Trias   | Muschelkalk  |
|15202138 |Arandellys-Fm.: Griaz-Mb. | Evaporit: Gips  | Rauwacke   | – |  Griaz-Member |  Späte Trias     | Späte Trias   | Muschelkalk  |
|15202139 |Röti-Fm. | Dolomitstein  | Rauwacke   | Tonstein: dolomitisch |  Röti-Formation |  Carnien     | Anisien   | Muschelkalk  |
|15202140 |Vieux-Emosson-Fm. | Sandstein: Quarz  | Sandstein: Feldspat   | Tonstein |  Vieux-Emosson-Formation |  Anisien     | Olénékien   | Buntsandstein  |
|15202141 |Mels-Fm. | Sandstein: Quarz  | Tonstein: schiefrig   | Dolomitstein |  Mels-Formation |  Anisien     | Olénékien   | Buntsandstein  |
|15202142 |Helvetikum: Spät- bis postvariszische Sedimente und Vulkanite | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Perm     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15202143 |Helvetikum: Verrucano | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15202144 |Glarner Verrucano | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Lopingien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202145 |Schönbühl-Fm. | Tonstein: sandig-schiefrig  | Sandstein: Quarz   | – |  Schönbühl-Formation |  Lopingien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202146 |Schönbühl-Fm.: Quarzit | Sandstein: Quarz  | –   | – |  Schönbühl-Formation |  Lopingien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202147 |Kärpf-Fm. | Konglomerat  | Sandstein   | Tonstein: siltig-schiefrig |  Kärpf-Formation |  Lopingien     | Guadalupien   | Spät- bis postvariszisches Grundgebirge  |
|15202148 |Karrenstock-Fm. | Tonstein: sandig-schiefrig  | Gestein: vulkanisch   | Sandstein: konglomeratisch |  Karrenstock-Formation |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202149 |Murgtal-Fm.: Chartegg-Mb. | Tonstein: siltig-schiefrig  | –   | – |  Chartegg-Member |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202150 |Karrenstock-Fm.: Fuggstock-Mb. | Konglomerat  | –   | – |  Fuggstock-Member |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202151 |Mären-Fm. | Tonstein: siltig-schiefrig  | Brekzie   | Sandstein |  Mären-Formation |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202217 |Montenvers-Granit | Granit  | Granit: mylonitisch   | – |  Montenvers-Granit |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202218 |Lognan-Orthogneis | Gneis: augig  | Gneis: gebändert   | – |  Lognan-Orthogneis |  Ordovizium     | Ordovizium   | Prävariszisches Grundgebirge  |
|15202219 |Pétoudes-Orthogneis | Gneis: magmatisch  | –   | – |  Pétoudes-Orthogneis |  Ordovizium     | Ordovizium   | Prävariszisches Grundgebirge  |
|15202220 |Gotthard-Decke: Postvariszische Intrusiva | Gestein: plutonisch  | –   | – |  – |  Cisuralien     | Cisuralien   | Postvariszisches Grundgebirge  |
|15202221 |Rotondo-Granit | Granit: Biotit-Granat  | –   | – |  Rotondo-Granit |  Sakmarien     | Sakmarien   | Postvariszisches Grundgebirge  |
|15202222 |Cacciola-Granit | Granit: Biotit-Muskovit  | –   | – |  Cacciola-Granit |  Cisuralien     | Cisuralien   | Postvariszisches Grundgebirge  |
|15202223 |Sädelhorn-Diorit | Diorit  | –   | – |  Sädelhorn-Diorit |  Cisuralien     | Cisuralien   | Postvariszisches Grundgebirge  |
|15202224 |Winterhorn-Granit | Granit: aplitisch: Granat  | –   | – |  Winterhorn-Granit |  Cisuralien     | Cisuralien   | Postvariszisches Grundgebirge  |
|15202225 |Gotthard-Decke: Spätvariszische Intrusiva | Gestein: plutonisch  | –   | – |  – |  Cisuralien     | Pennsylvanien   | Spätvariszisches Grundgebirge  |
|15202226 |Medel-Granit | Granit: porphyrisch  | Gneis: granitisch   | – |  Medel-Granit |  Cisuralien     | Cisuralien   | Spätvariszisches Grundgebirge  |
|15202227 |Cristallina-Granodiorit | Granodiorit  | –   | – |  Cristallina-Granodiorit |  Cisuralien     | Pennsylvanien   | Spätvariszisches Grundgebirge  |
|15202228 |Gamsboden-Granit | Granit: Biotit-Muskovit  | Gneis: augig   | – |  Gamsboden-Granit |  Cisuralien     | Pennsylvanien   | Spätvariszisches Grundgebirge  |
|15202229 |Uffiern-Diorit | Diorit: Biotit-Hornblende  | –   | – |  Uffiern-Diorit |  Cisuralien     | Pennsylvanien   | Spätvariszisches Grundgebirge  |
|15202230 |Fibbia-Granit | Granit: Biotit-Muskovit  | Gneis: augig   | – |  Fibbia-Granit |  Cisuralien     | Pennsylvanien   | Spätvariszisches Grundgebirge  |
|15202231 |Gotthard-Decke: Prä- und frühvariszische Metasedimentgesteine und Vulkanoklastika | Gneis: sedimentär  | Schiefer   | – |  – |  Paläozoikum     | Paläozoikum   | Prä- bis frühvariszisches Grundgebirge  |
|15202232 |Borel-Gneiskomplex | Schiefer: Glimmer-Hornblende  | –   | – |  Borel-Gneiskomplex |  Paläozoikum     | Paläozoikum   | Prä- bis frühvariszisches Grundgebirge  |
|15202233 |Tenelin-Gneiskomplex | Schiefer: Hornblende  | Gneis: Hornblende   | Amphibolit: Granat |  Tenelin-Gneiskomplex |  Paläozoikum     | Paläozoikum   | Prä- bis frühvariszisches Grundgebirge  |
|15202234 |Laiets-Gneiskomplex | Gneis  | Schiefer: Glimmer   | – |  Laiets-Gneiskomplex |  Paläozoikum     | Paläozoikum   | Prä- bis frühvariszisches Grundgebirge  |
|15202235 |Tremola-Gneiskomplex | Gneis: Hornblende  | Schiefer: Hornblende-Granat   | Amphibolit |  Tremola-Gneiskomplex |  Paläozoikum     | Paläozoikum   | Prä- bis frühvariszisches Grundgebirge  |
|15202236 |Tremola-Gneiskomplex: Pontino-Schiefer | Schiefer: Glimmer-Hornblende  | Gneis: schiefrig: Hornblende   | Amphibolit |  Pontino-Gneiskomplex |  Paläozoikum     | Paläozoikum   | Prä- bis frühvariszisches Grundgebirge  |
|15202237 |Tremola-Gneiskomplex: Nelva-Gneis | Gneis  | Schiefer: Glimmer-Granat   | Schiefer: Hornblende |  Nelva-Gneiskomplex |  Paläozoikum     | Paläozoikum   | Prä- bis frühvariszisches Grundgebirge  |
|15202238 |Tremola-Gneiskomplex: Sasso-Rosso-Schiefer | Schiefer: Glimmer  | Gneis: schiefrig: Chlorit   | Schiefer: Hornblende |  Sasso-Rosso-Gneiskomplex |  Paläozoikum     | Paläozoikum   | Prä- bis frühvariszisches Grundgebirge  |
|15202239 |Prüsfa-Gneiskomplex | Gneis: Granat  | Quarzit   | Rhyolith |  Prüsfa-Gneiskomplex |  Paläozoikum     | Paläozoikum   | Prä- bis frühvariszisches Grundgebirge  |
|15202240 |Streifengneis-Komplex | Gneis: granitisch  | Gneis: Biotit-Muskovit   | – |  Streifengneis-Komplex |  Llandovery     | Spätes Ordovizium   | Prävariszisches Grundgebirge  |
|15202241 |Chastelhorn-Metagabbro | Amphibolit: Granat  | Gabbro   | – |  Chastelhorn-Metagabbro |  Mittleres Ordovizium     | Frühes Ordovizium   | Prävariszisches Grundgebirge  |
|15202242 |Val-Nalps-Gneiskomplex: Gurschen-Gneis | Gneis  | Schiefer   | Gneis: migmatitisch |  Gurschen-Gneis |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202243 |Val-Nalps-Gneiskomplex: Guspis-Gneis | Gneis  | Schiefer   | Gneis: migmatitisch |  Guspis-Gneis |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202244 |Paradis-Gneiskomplex: Sorescia-Gneis | Gneis  | Gneis: migmatitisch   | – |  Sorescia-Gneis |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202246 |Helvetikum: Grundgebirge: Granit | Granit  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15202247 |Helvetikum: Grundgebirge: Saures vulkanisches Gestein | Gestein: saur-vulkanisch  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15202255 |Helvetikum: Grundgebirge: Permisch verwittertes Kristallin | Gestein: residual  | Gneis   | – |  – |  Perm     | Perm   | Grundgebirge  |
|15202256 |Goltschenried-Fm. | Schiefer: Graphit  | Gneis   | – |  Goltschenried-Formation |  Cisuralien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202263 |Gärsthorn-Gneiskomplex: Engi-Granit | Granit: porphyrisch  | –   | – |  Engi-Granit |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202264 |Calmut-Gneiskomplex | Gneis: migmatitisch  | –   | – |  Calmut-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202265 |Val-Pigniu-Gneiskomplex | Gneis  | –   | – |  Val-Pigniu-Gneiskomplex |  Proterozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202266 |Urseren-Garvera-Zone: Permo-Karbon | Sandstein  | Konglomerat   | Gestein: pelitisch |  – |  Perm     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15202267 |Goms-Gneiskomplex | Gneis  | Migmatit   | Amphibolit |  Goms-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202271 |Prosa-Granit | Granit: Biotit-Granat  | –   | – |  Prosa-Granit |  Cisuralien     | Cisuralien   | Postvariszisches Grundgebirge  |
|15202272 |Val-Tremola-Granit | Granit: aplitisch  | –   | – |  Val-Tremola-Granit |  Cisuralien     | Cisuralien   | Postvariszisches Grundgebirge  |
|15202273 |Leventina-Gneis | Gneis: Biotit-Muskovit  | Granit: porphyrisch   | – |  Leventina-Gneis |  Cisuralien     | Mississippien   | Grundgebirge  |
|15202274 |Lucomagno-Decke: Prävariszischer Orthogneis | Gneis: magmatisch  | –   | – |  – |  Cisuralien     | Karbon   | Grundgebirge  |
|15202275 |Lucomagno-Decke: Prävariszischer Paragneis | Gneis: sedimentär  | –   | – |  – |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15202276 |Val-Stgira-Riffmarmor | Kalkstein: Korallen  | –   | – |  Val-Stgira-Riffmarmor |  Früher Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15202277 |Piz-Terri-Lunschania: Fossilmarmor | Marmor: sandig: Bioklasten  | –   | – |  – |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202278 |Piz-Terri-Lunschania: Trias | Dolomitstein  | Kalkstein   | Sandstein: Quarz |  – |  Späte Trias     | Frühe Trias   | Sedimentbedeckung  |
|15202279 |Ultrahelvetischer Flysch | Sandstein  | Mergelstein   | Kalkstein |  – |  Eozän     | Eozän   | Flysch  |
|15202281 |Martinsmad-Fm. | Mergelstein: kalkig  | Kalkstein: kieselig   | Sandstein: Quarz |  Martinsmad-Formation |  Yprésien     | Maastrichtien   | Flysch  |
|15202282 |Martinsmad-Fm.: Supraquarzitischer Flysch | Kalkstein: sandig: Bioklasten  | Sandstein: kalkig   | Tonstein: schiefrig |  «Supraquarzitischer Flysch» (Martinsmad-Fm.) |  Bartonien     | Lutétien   | Flysch  |
|15202283 |Martinsmad-Fm.: Sardona-Mb. | Sandstein: Quarz  | –   | – |  Sardona-Member |  Yprésien     | Thanétien   | Flysch  |
|15202284 |Martinsmad-Fm.: Infraquarzitischer Flysch | Kalkstein: sandig: Glimmer  | Kalkstein: mergelig   | Tonstein: schiefrig |  «Infraquarzitischer Flysch» (Martinsmad-Fm.) |  Danien     | Maastrichtien   | Flysch  |
|15202285 |Meilleret-Fm. | Konglomerat  | Tonstein: schiefrig   | Kalkstein: Bioklasten |  Meilleret-Formation |  Priabonien     | Lutétien   | Flysch  |
|15202286 |Lavtina-Sandstein | Sandstein: kalkig: Glimmer  | Tonstein: schiefrig   | – |  Lavtina-Sandstein |  Priabonien     | Mittleres Eozän   | Flysch  |
|15202287 |Blattengrat-Sandstein | Sandstein: Glimmer  | Mergelstein: schiefrig   | Kalkstein: kieselig |  Blattengrat-Sandstein |  Priabonien     | Priabonien   | Flysch  |
|15202288 |Burg-Sandstein | Kalkstein: sandig  | Sandstein: kalkig   | Mergelstein |  Burg-Sandstein |  Priabonien     | Priabonien   | Flysch  |
|15202289 |Elm-Fm.: Val-d&#39;Illiez-Sandstein | Sandstein: tonig  | –   | – |  Val-d&#39;Illiez-Sandstein |  Rupélien     | Priabonien   | Flysch  |
|15202290 |Muot-da-Rubi-Fm. | Mergelstein: siltig-schiefrig  | Sandstein: tonig   | – |  Muot-da-Rubi-Formation |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202291 |Muot-da-Rubi-Fm.: Ahornen-Mb. | Sandstein: tonig: Lithoklasten  | Mergelstein   | – |  Ahornen-Member |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202292 |Muot-da-Rubi-Fm.: Kistenstöckli-Mb. | Konglomerat  | Kalkstein: sandig: Glimmer   | Mergelstein: sandig |  Kistenstöckli-Member |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202293 |Muot-da-Rubi-Fm.: Ghölzwald-Mb. | Kalkstein: sandig: Glimmer  | Sandstein: kalkig: Glimmer   | – |  Ghölzwald-Member |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202294 |Muot-da-Rubi-Fm.: Malor-Mb. | Mergelstein  | Sandstein: Glimmer   | – |  Malor-Member |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202295 |Südelgrabe-Melange | Mergelstein  | Kalkstein: siltig   | Brekzie: polymikt |  Südelgrabe-Melange |  Priabonien     | Priabonien   | Mélange  |
|15202296 |Stad-Fm.: Kleintal-Konglomerat | Konglomerat: kalkig  | –   | – |  Kleintal-Konglomerat |  Priabonien     | Lutétien   | Syn-Kollision  |
|15202297 |Stad-Fm.: Rütenen-Konglomerat | Konglomerat  | Mergelstein   | – |  Rütenen-Konglomerat |  Priabonien     | Lutétien   | Syn-Kollision  |
|15202298 |Helvetikum: Jura | Kalkstein  | Mergelstein   | Sandstein |  – |  Berriasien     | Rhät   | Sedimentbedeckung  |
|15202299 |Wang-Fm.: Brekzie | Brekzie  | –   | – |  «Wang-Brekzie» |  Maastrichtien     | Maastrichtien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202300 |Schrattenkalk-Fm.: Oberer Teil | Kalkstein: mikritisch: Bioklasten  | –   | – |  «Oberer Schrattenkalk» |  Aptien     | Aptien   | «Urgonien»  |
|15202301 |Schrattenkalk-Fm.: Unterer Teil | Kalkstein: mikritisch: Bioklasten  | –   | – |  «Unterer Schrattenkalk» |  Aptien     | Barrémien   | «Urgonien»  |
|15202302 |Quinten-Fm.: Oberer Quintner Kalk | Kalkstein: mikritisch  | –   | – |  «Oberer Quintner Kalk» |  Berriasien     | Tithonien   | Malm  |
|15202303 |Quinten-Fm.: Unterer Quintner Kalk | Kalkstein: mikritisch: Chert  | –   | – |  «Unterer Quintner Kalk» |  Kimméridgien     | Oxfordien   | Malm  |
|15202304 |Erzegg-Fm.: Planplatte-Eisenoolith | Kalkstein: Eisenooide  | –   | – |  Planplatte-Eisenoolith |  Callovien     | Callovien   | Lias-Dogger in pelagischer Fazies  |
|15202305 |Bommerstein-Fm.: Geissbach-Konglomerat | Konglomerat  | –   | – |  Geissbach-Konglomerat |  Aalénien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15202306 |Bommerstein-Fm.: Stöckli-Sandstein | Sandstein: Quarz  | Brekzie: dolomitisch   | – |  Stöckli-Sandstein |  Aalénien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15202307 |Infrapräalpines Melange | Tonstein  | Sandstein   | Kalkstein |  «Infrapräalpines Melange» |  Priabonien     | Priabonien   | Mélange  |
|15202308 |Iberg-Melange | Mergelstein  | Tonstein   | – |  Iberg-Melange |  Eozän     | Eozän   | Mélange  |
|15202309 |Iberg-Melange: Surbrunnen-Flysch | Tonstein  | Sandstein: tonig: Lithoklasten   | – |  Surbrunnen-Flysch |  Thanétien     | Danien   | Flysch  |
|15202310 |Iberg-Melange: Roggenegg-Komplex | Mergelstein  | Kalkstein   | – |  Roggenegg-Komplex |  Yprésien     | Trias   | Mélange  |
|15202311 |Iberg-Melange: Isentobel-Komplex | Siltstein  | Mergelstein   | – |  Isentobel-Komplex |  Eozän     | Späte Kreide   | Mélange  |
|15202312 |Serhalten-Melange | Tonstein  | Mergelstein   | – |  Serhalten-Flysch |  Eozän     | Eozän   | Mélange  |
|15202313 |Iberg-Melange: Gwürz-Flysch | Tonstein  | Sandstein: tonig   | – |  Gwürz-Flysch |  Paläogen     | Paläogen   | Flysch  |
|15202314 |Ruestel-Flysch | Sandstein: tonig  | Tonstein: schiefrig   | – |  Ruestel-Flysch |  Yprésien     | Paleozän   | Flysch  |
|15202315 |Iberg-Melange: Scheidegg-Flysch | Mergelstein  | Siltstein   | Sandstein: Glaukonit |  Scheidegg-Flysch |  Paläogen     | Paläogen   | Flysch  |
|15202316 |Habkern-Granit | Granit  | –   | – |  Habkern-Granit |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15202317 |Infrapräalpines Melange: Gros-Plané-Melange | Tonstein  | Sandstein   | – |  Gros-Plané-Melange |  Rupélien     | Rupélien   | Mélange  |
|15202318 |Infrapräalpines Melange: Bodevena-Melange | Tonstein  | Sandstein   | – |  Bodevena-Melange |  Priabonien     | Späte Kreide   | Mélange  |
|15202319 |Subalpiner Flysch | Tonstein  | Sandstein: Quarz   | – |  «Subalpiner Flysch» |  Rupélien     | Priabonien   | Flysch  |
|15202320 |Torrenthorn-Fm. | Sandstein: kalkig-kieselig  | Kalkstein: sandig-spätig   | Tonstein |  Torrenthorn-Formation |  Toarcien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202321 |Prodkamm-Fm.: Cardinien-Mb.: Weissgandstöckli-Bk. | Sandstein: kalkig: Glimmer  | –   | – |  Weissgandstöckli-Bank |  Sinémurien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15202322 |Mären-Fm.: Grisch-Mb. | Tonstein: siltig-schiefrig  | Kalkstein   | – |  Grisch-Member |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202323 |Mären-Fm.: Foostock-Mb. | Tonstein: siltig-schiefrig  | –   | – |  Foostock-Member |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202324 |Murgtal-Fm. | Brekzie  | Sandstein   | Tonstein: siltig-schiefrig |  Murgtal-Formation |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202325 |Vernayaz-Fm.: Dzéman-Mb. | Konglomerat  | Sandstein   | Tonstein |  Dzéman-Member |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15202326 |Zentraler-Aare-Granit: Aplitische Randfazies | Granit: aplitisch  | –   | – |  Zentraler Aare-Granit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202327 |Windgällen-Fm.: Rhyolith | Rhyolith: ignimbritisch  | –   | – |  Windgällen-Formation |  Asselien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202328 |Bäregg-Gneiskomplex | Gneis  | Gneis: mylonitisch   | Granodiorit |  Bäregg-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202329 |Gärsthorn-Gneiskomplex | Gneis: augig  | –   | – |  Gärsthorn-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202330 |Sogn-Placi-Gneiskomplex | Gneis  | Schiefer: Glimmer   | Schiefer: tonig |  Sogn-Placi-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202331 |Massa-Gneiskomplex | Gneis: migmatitisch  | Migmatit   | Amphibolit |  Massa-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202332 |Aiguilles-Rouges-Massiv: Mittelvariszische Intrusiva | Gestein: plutonisch  | –   | – |  – |  Pennsylvanien     | Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202333 |Aiguilles-Rouges-Massiv: Frühvariszische Intrusiva | Gestein: plutonisch  | –   | – |  – |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15202334 |Aiguilles-Rouges-Massiv: Prävariszisches Grundgebirge | Gneis  | Schiefer   | Amphibolit |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202335 |Chéserys-Gneis | Gneis: Kyanit  | –   | – |  Chéserys-Gneis |  Devon     | Paläozoikum   | Prävariszisches Grundgebirge  |
|15202336 |Mont-Blanc-Massiv: Spät- bis postvariszische Intrusiva | Gestein: plutonisch  | –   | – |  – |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202337 |Mont-Blanc-Massiv: Prävariszisches Grundgebirge | Gneis  | Schiefer   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202338 |Alp-Cavradi-Gneiskomplex | Gneis  | Schiefer: tonig   | Schiefer: Graphit |  Alp-Cavradi-Gneiskomplex |  Paläozoikum     | Paläozoikum   | Prä- bis frühvariszisches Grundgebirge  |
|15202339 |Giubine-Gneiskomplex | Gneis  | Schiefer: Glimmer   | – |  Giubine-Gneiskomplex |  Paläozoikum     | Paläozoikum   | Prä- bis frühvariszisches Grundgebirge  |
|15202340 |Gotthardt-Decke: Prävariszisches polyzyklisches Grundgebirge | Gneis  | Schiefer   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202341 |Goms-Gneiskomplex: Unterwassern-Gneis | Gneis  | –   | – |  Unterwassern-Gneis |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202343 |Streifengneis-Komplex: Sassina-Augengneis | Gneis: granitisch-augig  | –   | – |  Sassina-Spans-Augengneis |  Paläozoikum     | Paläozoikum   | Prävariszisches Grundgebirge  |
|15202344 |Streifengneis-Komplex: Alp-Ramosa-Granitgneis | Gneis: granitisch  | –   | – |  Alp-Ramosa-Granitgneis |  Paläozoikum     | Paläozoikum   | Prävariszisches Grundgebirge  |
|15202346 |Val-Nalps-Gneiskomplex | Gneis  | Amphibolit: Granat   | Gestein: ultramafisch |  Val-Nalps-Gneiskomplex |  Kambrium     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202347 |Val-Nalps-Gneiskomplex: Prato-Gneis | Gneis  | Schiefer: Glimmer   | Amphibolit |  Prato-Gneis |  Kambrium     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202348 |Val-Nalps-Gneiskomplex: Distelgrat-Gneis | Gneis: sedimentär  | –   | – |  Distelgrat-Gneis |  Kambrium     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202349 |Paradis-Gneiskomplex: Val-Gronda-Augengneis | Gneis: migmatitisch-augig  | –   | – |  Val-Gronda-Augengneis |  Kambrium     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202350 |Val-Nalps-Gneiskomplex: Fuorcla-Paradis-Serpentinit | Serpentinit  | –   | – |  Fuorcla-Paradis-Serpentinit |  Kambrium     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202351 |Paradis-Gneiskomplex | Gneis: migmatitisch  | –   | – |  Paradis-Gneiskomplex |  Kambrium     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202352 |Paradis-Gneiskomplex: Oberstafel-Gneis | Gneis: Biotit-Plagioklas  | –   | – |  Oberstafel-Gneis |  Mittleres Ordovizium     | Frühes Ordovizium   | Prävariszisches Grundgebirge  |
|15202353 |Paradis-Gneiskomplex: Ganneretsch-Gneis | Gneis: migmatitisch  | –   | – |  Ganneretsch-Gneis |  Kambrium     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202354 |Paradis-Gneiskomplex: Corandoni-Amphibolit | Amphibolit  | Schiefer: Hornblende   | Gneis |  Corandoni-Amphibolit |  Kambrium     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202355 |Tavetsch-Decke: Prävariszisches polyzyklisches Grundgebirge | Gneis  | Migmatit   | Amphibolit |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202356 |Rueras-Gneiskomplex | Gneis: Muskovit  | –   | – |  Rueras-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202357 |Aiguilles-Rouges-Massiv: Prä- und frühvariszische Sedimente und Vulkanite | Gestein: sedimentär  | Gestein: vulkanisch   | – |  – |  Mississippien     | Mississippien   | Prä- bis frühvariszisches Grundgebirge  |
|15202358 |Vernayaz-Fm.: Salvan-Mb.: Au-d&#39;Arbignon-Schiefer | Tonstein: schiefrig: Anthrazit  | –   | – |  Au-d&#39;Arbignon-Schiefer |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202359 |Vernayaz-Fm.: Salvan-Mb.: Dorénaz-Konglomerat | Konglomerat  | –   | – |  Dorénaz-Konglomerat |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202360 |Wildflysch | Tonstein  | –   | – |  – |  Paläogen     | Paläogen   | Mélange  |
|15205032 |Maiolica Lombarda | Kalkstein: mikritisch: Chert  | Tonstein   | – |  «Maiolica Lombarda» |  Barrémien     | Tithonien   | Maiolica / Aptychenkalk  |
|15205033 |Selcifero Lombardo | Gestein: kieselig: Radiolarien  | Kalkstein: mergelig   | – |  «Selcifero Lombardo» |  Tithonien     | Bajocien   | Radiolarit  |
|15205034 |Selcifero Lombardo: Rosso ad Aptici | Mergelstein  | Kalkstein: mergelig: Chert   | – |  «Rosso ad Aptici» |  Tithonien     | Kimméridgien   | Radiolarit  |
|15205035 |Calcare a bivalvi planctonici | 15111227  | Mergelstein   | – |  «Calcare a bivalvi planctonici» |  Bajocien     | Aalénien   | Lias-Dogger in pelagischer Fazies  |
|15205036 |Rosso Ammonitico Lombardo | Kalkstein: mergelig: Bioklasten  | Mergelstein   | – |  «Rosso Ammonitico Lombardo» |  Aalénien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15205037 |Rosso Ammonitico Lombardo: Grenzposidonienschichten | Mergelstein: Bioklasten  | –   | – |  «Grenzposidonienschichten» |  Toarcien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15205038 |Morbio-Fm. | Kalkstein: mikritisch  | Mergelstein   | – |  Morbio-Formation |  Toarcien     | Pliensbachien   | Lias-Dogger in pelagischer Fazies  |
|15205039 |Besazio-Kalk | Kalkstein: Bioklasten  | –   | – |  Besazio-Kalk |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15205040 |Moltrasio-Fm. | Kalkstein: kieselig  | Mergelstein   | Brekzie |  Moltrasio-Formation |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15205041 |Moltrasio-Fm.: Molino-Mb. | Kalkstein: kieselig  | Mergelstein   | – |  Molino-Member |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15205042 |Saltrio-Fm. | Kalkstein: arenitisch: Bioklasten  | –   | – |  Saltrio-Formation |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15205043 |Macchia Vecchia | Brekzie  | –   | – |  «Macchia Vecchia» |  Pliensbachien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15205044 |Broccatello d&#39;Arzo | Kalkstein: Bioklasten  | Brekzie   | – |  Broccatello d&#39;Arzo |  Sinémurien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15205045 |Albenza-Fm. | Kalkstein: dolomitisch  | Dolomitstein: kalkig   | Kalkstein: Ooide |  Albenza-Formation |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15205046 |Zu-Kalk | Kalkstein: Bioklasten  | Kalkstein: mergelig   | Mergelstein |  Zu-Kalk |  Rhät     | Norien   | Pelitische Trias  |
|15205047 |Tremona-Fm. | 15111193  | Mergelstein   | Dolomitstein |  Tremona-Formation |  Rhät     | Rhät   | Pelitische Trias  |
|15205048 |Brecce Retiche | Brekzie  | –   | – |  «Brecce Retiche» |  Rhät     | Rhät   | Pelitische Trias  |
|15205049 |Riva-di-Solto-Tonstein | Tonstein  | Mergelstein   | Kalkstein: mergelig |  Riva-di-Solto-Tonstein |  Norien     | Norien   | Pelitische Trias  |
|15205050 |Dolomia Principale | Dolomitstein  | Dolomitstein: stromatolithisch   | – |  «Dolomia Principale» |  Norien     | Norien   | Hauptdolomit  |
|15205051 |Pizzella-Mergel | Mergelstein  | Mergelstein: Bitumen   | Kalkstein |  Pizzella-Mergel |  Carnien     | Carnien   | Raibl  |
|15205052 |Cunardo-Fm. | Kalkstein: Chert  | –   | – |  Cunardo-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205053 |Meride-Fm. | Kalkstein: tonig  | Tonstein: schiefrig: Bitumen   | Dolomitstein |  Meride-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205054 |Meride-Fm.: Kalkschieferzone | Schiefer: kalkig  | Kalkstein: mikritisch   | Mergelstein |  «Kalkschieferzone» (Meride-Fm.) |  Carnien     | Ladinien   | Karbonatische Trias  |
|15205055 |Meride-Fm.: Unterer Kalk: Cassina-Bk. | Tonstein: schiefrig: Bitumen  | Kalkstein   | Tuffit |  Cassina-Bank |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205056 |Meride-Fm.: Unterer Kalk: Cava Superiore | Tonstein: schiefrig: Bitumen  | –   | – |  «Cava Superiore» |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205057 |Meride-Fm.: Unterer Kalk: Cava Inferiore | Tonstein: schiefrig: Bitumen  | –   | – |  «Cava Inferiore» |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205058 |San-Giorgio-Dolomit | 15111281  | –   | – |  San-Giorgio-Dolomit |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205059 |San-Giorgio-Dolomit: Val-Serrata-Tuffite | Tuffit  | –   | – |  Val-Serrata-Tuffite |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205060 |Besano-Fm. | 15111288  | Tonstein: schiefrig: Bitumen   | – |  Besano-Formation |  Ladinien     | Anisien   | Karbonatische Trias  |
|15205061 |San-Salvatore-Dolomit | Dolomitstein  | –   | – |  San-Salvatore-Dolomit |  Ladinien     | Anisien   | Karbonatische Trias  |
|15205062 |Bellano-Fm. | Konglomerat  | Sandstein   | – |  Bellano-Formation |  Anisien     | Frühe Trias   | Detritische Trias  |
|15205063 |Servino | Sandstein  | Tonstein   | – |  «Servino» |  Frühe Trias     | Perm   | Detritische Trias  |
|15205064 |Verrucano Lombardo | Konglomerat  | Sandstein   | Tonstein |  – |  Changhsingien     | Changhsingien   | Spät- bis postvariszisches Grundgebirge  |
|15205065 |Morcote-Vulkanite | Gestein: vulkanisch  | –   | – |  – |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15205066 |Morcote-Vulkanite: Granophyr | Granophyr  | –   | – |  – |  Kungurien     | Kungurien   | Spät- bis postvariszisches Grundgebirge  |
|15205067 |Morcote-Vulkanite: Andesit und Dazit | Andesit  | Dazit   | – |  – |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15205068 |Morcote-Vulkanite: Basalt | Basalt  | –   | – |  – |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15205069 |Morcote-Vulkanite: Basaler Tuf | Tuffit  | –   | – |  – |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15205070 |Manno-Fm. | Konglomerat  | Sandstein   | Schiefer: tonig: Anthrazit |  Manno-Formation |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15205071 |Südalpin: Paläogen-Neogen | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Tertiär     | Tertiär   | Sedimentbedeckung  |
|15205072 |Südalpin: Kreide | Sandstein  | Gestein: pelitisch   | Kalkstein |  – |  Kreide     | Kreide   | Sedimentbedeckung  |
|15205073 |Südalpin: Radiolarit-Aptychenkalk | Gestein: kieselig: Radiolarien  | Kalkstein: mergelig   | – |  – |  Später Jura     | Später Jura   | Radiolarit  |
|15205074 |Südalpin: Dogger | 15111227  | Mergelstein   | – |  – |  Mittlerer Jura     | Mittlerer Jura   | Lias-Dogger in pelagischer Fazies  |
|15205075 |Südalpin: Lias | Kalkstein  | Mergelstein   | Brekzie |  – |  Früher Jura     | Früher Jura   | Syn-Rift  |
|15205076 |Südalpin: Trias | Dolomitstein  | Gestein: pelitisch   | Kalkstein |  – |  Trias     | Trias   | Prä-Rift  |
|15205077 |Südalpin: Permo-Karbon | Konglomerat  | Sandstein   | Gestein: vulkanisch |  – |  Perm     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15205078 |Südalpin: Grundgebirge | Gneis  | Amphibolit   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15205079 |Südalpin: Variszische Intrusiva | Gestein: plutonisch  | –   | – |  – |  Paläozoikum     | Paläozoikum   | Variszisches Grundgebirge  |
|15205080 |San-Bernardo-Gneis | Gneis  | –   | – |  San-Bernardo-Gneis |  Silur     | Ordovizium   | Grundgebirge  |
|15205081 |Südalpin: Prävariszische Metasedimente | Gneis: sedimentär  | Schiefer: Glimmer   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15205082 |Stabbiello-Gneis | 15111554  | –   | – |  Stabbiello-Gneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15205083 |Giumello-Gneis | 15111513  | –   | – |  Giumello-Gneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15205084 |Ceneri-Gneis | Gneis: Granat  | –   | – |  Ceneri-Gneis |  Spätes Ordovizium     | Spätes Ordovizium   | Grundgebirge  |
|15205085 |Südalpin: Proterozoische und paläozoische mafische und ultramafische Gesteine | Gestein: mafisch  | Gestein: ultramafisch   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15205086 |Mont-Morion-Granit | Granit: porphyrisch  | –   | – |  Mont-Morion-Granit |  Perm     | Perm   | Variszisches Grundgebirge  |
|15205087 |Pointe-d&#39;Otemma-Granodiorit | 15111412  | Gneis: granodioritisch   | – |  Pointe-d&#39;Otemma-Granodiorit |  Perm     | Perm   | Variszisches Grundgebirge  |
|15205088 |Bouquetins-Quarzdiorit | 15111439  | Gneis: dioritisch   | – |  Bouquetins-Quarzdiorit |  Perm     | Perm   | Variszisches Grundgebirge  |
|15205089 |Tête-de-Valpelline-Phyllit | Schiefer: tonig: Graphit  | –   | – |  Tête-de-Valpelline-Phyllit |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15205090 |Arolla-Einheit: Série rubanée | Gneis: gebändert  | Gneis: granitisch   | Gneis: dioritisch |  «Série Rubanée» |  Paläozoikum     | Paläozoikum   | Variszisches Grundgebirge  |
|15205091 |Sassa-Metagabbro | Gabbro  | Diorit   | Gestein: ultramafisch |  Sassa-Metagabbro |  Perm     | Perm   | Variszisches Grundgebirge  |
|15205092 |Maia-Metagabbro | Gabbro: Hornblende  | –   | – |  Maia-Metagabbro |  Perm     | Perm   | Variszisches Grundgebirge  |
|15205093 |Losone-Schiefer | Schiefer: Serizit-Chlorit  | Gneis   | – |  Losone-Schiefer |  Mesozoikum     | Proterozoikum   | Grundgebirge  |
|15205094 |Pizzo-Leone-Gneis | Gneis: Chlorit  | –   | – |  Pizzo-Leone-Gneis |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203562 |Zentralschweizerische Klippen: Flysch | Sandstein  | Mergelstein   | – |  – |  Eozän     | Eozän   | Flysch  |
|15203559 |Simano-Decke: Ultramafisches Gestein | Gestein: ultramafisch  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203560 |Alpbach-Schiefer | Schiefer: tonig  | Sandstein   | Kalkstein |  Alpbach-Schiefer |  Kreide     | Kreide   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203561 |Arosa-Decke: Gabbro | Gabbro  | –   | – |  – |  Mittlerer Jura     | Mittlerer Jura   | Ophiolithische Abfolge  |
|15203563 |Zentralschweizerische Klippen: Couches-Rouges | Kalkstein: mergelig  | Kalkstein: mikritisch   | Mergelstein |  – |  Maastrichtien     | Albien   | Couches Rouges  |
|15203564 |Wägital-Flysch: Oberer Teil (Paläogen) | Brekzie: polymikt  | Sandstein   | Kalkstein: siltig-tonig |  Wägital-Flysch |  Yprésien     | Yprésien   | Flysch  |
|15203565 |Wägital-Flysch: Unterer Teil (Kreide) | Brekzie: polymikt  | Mergelstein   | Kalkstein: mikritisch |  Wägital-Flysch |  Maastrichtien     | Santonien   | Flysch  |
|15203566 |Wägital-Flysch: Basaler tektonisierter Teil | Sandstein  | Mergelstein   | Kalkstein: siltig-tonig |  Wägital-Flysch |  Maastrichtien     | Santonien   | Flysch  |
|15203567 |Gibel- und Griggeli-Fm. | Kalkstein: sandig  | –   | – |  – |  Oxfordien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15203568 |Mittelpenninikum: Trias: Dolomit | Dolomitstein  | –   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15203569 |Mittelpenninikum: Trias: Dolomit und Kalk | Dolomitstein  | Kalkstein   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15203570 |Mittelpenninikum: Trias: Dolomit und Rauwacke | Dolomitstein: schiefrig  | Rauwacke   | – |  – |  Trias     | Trias   | Prä-Rift  |
|15203571 |Mittelpenninikum: Trias: Rauwacke | Rauwacke  | –   | – |  – |  Trias     | Trias   | Prä-Rift  |
|15203572 |Mittelpenninikum: Trias: Gipsmergel und Sandstein | Mergelstein: Gips  | Sandstein   | – |  – |  Trias     | Trias   | Prä-Rift  |
|15203573 |Schlieren-Sandstein: Im Paläogen tektonisch überprägt | Sandstein  | Siltstein   | Tonstein |  Schlieren-Sandstein |  Paläogen     | Paläogen   | Flysch  |
|15203574 |Leimern-Sch. | Kalkstein: mergelig  | Mergelstein: kalkig   | – |  Leimern-Schichten |  Santonien     | Coniacien   | Couches Rouges  |
|15203575 |Mittelpenninikum: Trias: Rauwacke und Sandstein | Rauwacke  | Sandstein: Quarz   | – |  – |  Mittlere Trias     | Frühe Trias   | Prä-Rift  |
|15203576 |Guber- Schoni- und Schlieren-Sandstein | Sandstein  | Siltstein   | – |  – |  Yprésien     | Yprésien   | Flysch  |
|15203577 |Zentralschweizerische Klippen: Mittellias | Kalkstein: sandig  | Kalkstein: spätig   | – |  – |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15203579 |Nolla-Tonschiefer: Quarzsandstein | Sandstein: Quarz  | –   | – |  Nolla-Tonschiefer |  Albien     | Aptien   | Sedimentbedeckung  |
|15203580 |Bärenhorn-Fm.: Quarzsandstein | Sandstein: Quarz  | –   | – |  Bärenhorn-Formation |  Barrémien     | Berriasien   | Sedimentbedeckung  |
|15203581 |Grava-Decke: Kalkschiefer | Schiefer: kalkig  | –   | – |  – |  Kreide     | Kreide   | Sedimentbedeckung  |
|15203582 |Grava-Decke: Tonschiefer | Schiefer: tonig  | –   | – |  – |  Kreide     | Kreide   | Sedimentbedeckung  |
|15203583 |Grava-Decke: Trias | Schiefer: Serizit  | –   | – |  – |  Trias     | Trias   | Prä-Rift  |
|15203584 |Soladier- und Verdy-Mb. | Mergelstein  | Kalkstein   | – |  Staldengraben-Formation |  Bajocien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15203585 |Col-de-Tompey- und Bois-de-Luan-Mb. | Mergelstein  | Sandstein: kalkig   | Kalkstein: mikritisch |  – |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15203586 |Heiti- und Rossinière-Fm. | Mergelstein  | Kalkstein: kieselig   | Kalkstein: spätig |  – |  Bajocien     | Sinémurien   | Syn-Rift  |
|15203587 |Coulaytes-Melange und Cuvigne-Derrey-Fm. | Tonstein  | Kalkstein   | Sandstein: tonig: Lithoklasten |  – |  Priabonien     | Mittleres Eozän   | Syn-Kollision  |
|15203588 |Langel- und Col-de-Cordon-Mb. | Kalkstein: Ooide  | Kalkstein: arenitisch   | – |  – |  Callovien     | Bajocien   | Syn-Rift  |
|15203589 |Grande-Bonavau-Fm. und Fm. spathique | Kalkstein: spätig  | Kalkstein: mikritisch   | Dolomitstein |  – |  Aalénien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15203590 |Col-de-Tompey- und Agreblierai-Mb. | Mergelstein  | Sandstein: kalkig   | Kalkstein: Ooide |  – |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15203591 |Chavanette- und Rubli-Mb. | Brekzie  | Mergelstein   | Kalkstein |  – |  Callovien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15203592 |Barrhorn-Einheit: Flysch | Sandstein  | Gestein: pelitisch   | – |  – |  Lutétien     | Lutétien   | Flysch  |
|15203593 |Barrhorn-Einheit: Couches-Rouges | Kalkstein: mergelig  | Mergelstein   | – |  – |  Maastrichtien     | Cénomanien   | Couches Rouges  |
|15203594 |Barrhorn-Einheit: Malm | Kalkstein  | Mergelstein   | – |  – |  Berriasien     | Oxfordien   | Malm  |
|15203595 |Barrhorn-Einheit: Dogger | Sandstein  | Mergelstein   | Kalkstein: Ooide |  – |  Callovien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15203596 |St-Triphon- und Wiriehorn-Fm. | Kalkstein  | Dolomitstein   | – |  – |  Anisien     | Olénékien   | Karbonatische Trias  |
|15203597 |Printse-Fm. | Sandstein  | Schiefer: tonig: Anthrazit   | – |  Printse-Formation |  Karbon     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15203598 |Métailler-Fm.: Louvie-Gabbro | Gabbro  | –   | – |  Louvie-Gabbro |  Spätes Ordovizium     | Mittleres Ordovizium   | Grundgebirge  |
|15203599 |Distulberg-Fm.: Graphitschiefer | Schiefer: Graphit  | –   | – |  Distulberg-Formation |  Kambrium     | Kambrium   | Grundgebirge  |
|15203600 |Lirec-Fm.: Amphibolit | Amphibolit  | –   | – |  Lirec-Formation |  Kambrium     | Kambrium   | Grundgebirge  |
|15203601 |Ergischhorn-Komplex: Brändjispitz-Gabbro | Gabbro  | –   | – |  Brändjispitz-Metagabbro |  Kambrium     | Kambrium   | Grundgebirge  |
|15203602 |Ergischhorn-Komplex: Eklogit | Eklogit  | –   | – |  Ergischhorn-Komplex |  Proterozoikum     | Proterozoikum   | Grundgebirge  |
|15203603 |Südegg-Komplex: Prasinit | Prasinit  | Basalt   | – |  Südegg-Komplex |  Mesozoikum     | Mesozoikum   | Mélange  |
|15203604 |Südegg-Komplex: Talk-Chloritschiefer | Schiefer: Chlorit-Talk  | –   | – |  Südegg-Komplex |  Mesozoikum     | Mesozoikum   | Mélange  |
|15203605 |Gurnigel-Decke: Flysch-3 | Mergelstein  | Sandstein: kalkig   | – |  «Flysch 3» |  Thanétien     | Danien   | Flysch  |
|15203606 |Gurnigel-Decke: Flysch-2 | Sandstein  | Tonstein   | – |  «Flysch 2» |  Yprésien     | Yprésien   | Flysch  |
|15203607 |Hellstätt-Fm. und Flysch 2a | Tonstein  | Sandstein   | Kalkstein: siltig-tonig |  – |  Danien     | Maastrichtien   | Flysch  |
|15203608 |Aroley-, Marmontains- und St-Chritophe-Fm. | Schiefer  | Marmor   | Quarzit |  – |  Paläogen     | Kreide   | Sedimentbedeckung  |
|15203609 |Südegg-Komplex: Schwarzer Schiefer | Schiefer: tonig  | –   | – |  Südegg-Komplex |  Karbon     | Karbon   | Mélange  |
|15203610 |Südegg-Komplex: Serpentinit | Serpentinit  | –   | – |  Südegg-Komplex |  Perm     | Karbon   | Mélange  |
|15203611 |Südegg-Komplex: Albitgneis | Gneis: Albit  | –   | – |  Südegg-Komplex |  Perm     | Perm   | Mélange  |
|15203612 |Südegg-Komplex: Marmor | Marmor: kalkig  | Marmor: dolomitisch   | Brekzie: dolomitisch |  Südegg-Komplex |  Späte Trias     | Mittlere Trias   | Mélange  |
|15203613 |Südegg-Komplex: Brekzie | Brekzie  | –   | – |  Südegg-Komplex |  Jura     | Jura   | Mélange  |
|15203614 |Südegg-Komplex: Gips | Evaporit: Gips  | –   | – |  Südegg-Komplex |  Späte Trias     | Mittlere Trias   | Mélange  |
|15203615 |Monte-Leone-Decke: Sedimentbedeckung | Schiefer  | Marmor   | Konglomerat |  – |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15203616 |Monte-Leone-Decke: Dogger-Malm | Konglomerat: polymikt  | Marmor   | Schiefer: Glimmer |  – |  Später Jura     | Mittlerer Jura   | Post-Rift  |
|15203617 |Monte-Leone-Decke: Dogger-Malm: Glimmerschiefer | Schiefer: Glimmer  | –   | – |  – |  Später Jura     | Mittlerer Jura   | Post-Rift  |
|15203618 |Monte-Leone-Decke: Dogger-Malm: Marmor | Marmor  | –   | – |  – |  Später Jura     | Mittlerer Jura   | Post-Rift  |
|15203619 |Monte-Leone-Decke: Dogger: Konglomerat | Konglomerat  | Sandstein   | – |  – |  Später Jura     | Mittlerer Jura   | Syn-Rift  |
|15203620 |Monte-Leone-Decke: Lias | Konglomerat  | Marmor   | Schiefer |  – |  Mittlerer Jura     | Früher Jura   | Syn-Rift  |
|15203621 |Monte-Leone-Decke: Lias: Sandstein | Sandstein  | –   | – |  – |  Mittlerer Jura     | Früher Jura   | Lias-Dogger in detritischer Fazies  |
|15203622 |Monte-Leone-Decke: Lias: Konglomerat | Konglomerat  | Sandstein   | – |  – |  Mittlerer Jura     | Früher Jura   | Lias-Dogger in detritischer Fazies  |
|15205095 |Fornale-Gabbro | Gabbro: Hornblende  | –   | – |  Fornale-Gabbro |  Perm     | Perm   | Variszisches Grundgebirge  |
|15205096 |Matterhorn-Gabbro | Gabbro  | –   | – |  Matterhorn-Gabbro |  Perm     | Perm   | Ophiolithische Abfolge  |
|15205097 |Berrio-Gabbro | Gabbro  | –   | – |  Berrio-Gabbro |  Perm     | Perm   | Variszisches Grundgebirge  |
|15205098 |Grand-Dolin-Brekzie | Brekzie: polymikt  | –   | – |  Grand-Dolin-Brekzie |  Später Jura     | Mittlerer Jura   | Lias-Dogger in neritischer Fazies  |
|15205099 |Meride-Fm.: Oberer Kalk | Kalkstein: Bitumen  | Mergelstein   | Kalkstein: mergelig |  Meride-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205100 |Meride-Fm.: Unterer Kalk | Kalkstein  | Mergelstein: schiefrig: Bitumen   | – |  Meride-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205101 |Meride-Fm.: Dolomit-Band | Dolomitstein  | –   | – |  «Dolomitband» (Meride-Fm.) |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15205102 |Dent-Blanche-Decke: Lias: Kalkstein | Kalkstein: spätig: Bioklasten  | –   | – |  – |  Früher Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15205103 |Dent-Blanche-Decke: Trias: Dolomit | Dolomitstein  | Kalkstein   | – |  – |  Norien     | Norien   | Karbonatische Trias  |
|15205104 |Dent-Blanche-Decke: Trias: Rauwacke | Rauwacke  | –   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15205105 |Dent-Blanche-Decke: Trias: Quarzit | Sandstein: Quarz  | Konglomerat: Quarz   | – |  – |  Trias     | Trias   | Detritische Trias  |
|15205106 |Arolla-Orthogneis: Leukokrater Gneis | Gneis: granitisch  | –   | – |  Arolla-Orthogneis |  Perm     | Perm   | Variszisches Grundgebirge  |
|15205107 |Arolla-Orthogneis: Augengneis | Gneis: granitisch-augig  | Gneis   | – |  Arolla-Orthogneis |  Perm     | Perm   | Variszisches Grundgebirge  |
|15205108 |Arolla-Orthogneis: Mylonit | Gneis: mylonitisch  | –   | – |  Arolla-Orthogneis |  Perm     | Perm   | Variszisches Grundgebirge  |
|15205109 |Arolla-Einheit: Série rubanée: Mylonit | Gneis: mylonitisch  | –   | – |  «Série Rubanée» |  Paläozoikum     | Proterozoikum   | Variszisches Grundgebirge  |
|15205110 |Arolla-Einheit: Série rubanée: Mikroaugengneis | Gneis: augig  | –   | – |  «Série Rubanée» |  Paläozoikum     | Proterozoikum   | Variszisches Grundgebirge  |
|15205111 |Arolla-Orthogneis: Granitoid | Gneis: granitisch-augig  | –   | – |  Arolla-Orthogneis |  Perm     | Perm   | Variszisches Grundgebirge  |
|15205112 |Arolla-Einheit: Basisches Gestein | Diorit  | Gabbro: Hornblende   | – |  – |  Paläozoikum     | Proterozoikum   | Variszisches Grundgebirge  |
|15205113 |Arolla-Einheit: Basisches Gestein: Mylonitisch | 15111448  | Schiefer: Zoisit-Fuchsit   | – |  – |  Paläozoikum     | Proterozoikum   | Variszisches Grundgebirge  |
|15205114 |Arolla-Einheit: Prasinit | Prasinit  | –   | – |  – |  Mesozoikum     | Proterozoikum   | Grundgebirge  |
|15205115 |Arolla-Einheit: Hornblendegabbro | Gabbro: Hornblende  | Diorit   | – |  – |  Perm     | Perm   | Grundgebirge  |
|15205116 |Arolla-Einheit: Ultramafisches Gestein | Gestein: ultramafisch  | Serpentinit   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15205117 |Arolla-Einheit: Paragneis | Gneis: sedimentär  | Gneis: Amphibol   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15205118 |Arolla-Einheit: Glimmerschiefer | Schiefer: Glimmer-Granat  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15205119 |Valpelline-Einheit: Mylonit | Mylonit  | Schiefer: Chlorit-Epidot   | Gneis: Albit |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15205120 |Valpelline-Einheit: Amphibolit | Amphibolit  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15205121 |Valpelline-Einheit: Marmor | Marmor: kalkig  | Marmor: Kalksilikat   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15205122 |Valpelline-Einheit: Migmatit | Gneis: migmatitisch  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15205123 |Roisan-Cignana-Zone: Marmor | Marmor: kalkig  | Marmor: dolomitisch   | Schiefer: kalkig: Glimmer |  – |  Mittlere Trias     | Perm   | Sedimentbedeckung  |
|15205124 |Musella-Granit | Granit: porphyrisch: Hornblende  | –   | – |  Musella-Granit |  Karbon     | Karbon   | Grundgebirge  |
|15205125 |Sella-Granodiorit | 15111412  | –   | – |  Sella-Granodiorit |  Karbon     | Karbon   | Grundgebirge  |
|15205126 |Marinelli-Fm. | 15111580  | Schiefer: tonig: Graphit   | Amphibolit |  Marinelli-Formation |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15205127 |Margna- und Sella-Decke: Grundgebirge | Gneis  | Amphibolit   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15205128 |Margna- und Sella-Decke: Variszische Intrusiva | Granit  | Granodiorit   | – |  – |  Perm     | Karbon   | Variszisches Grundgebirge  |
|15205129 |Margna- und Sella-Decke: Prävariszisches Grundgebirge | Gneis  | Schiefer   | Amphibolit |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15205130 |Margna-Decke: Metaarkose, Orthogneise | Gneis  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15205131 |Sesia-Decke: Orthogneis | Gneis: magmatisch  | –   | – |  – |  Perm     | Karbon   | Grundgebirge  |
|15205132 |Sesia-Decke: Micascisti Eclogitici | Schiefer: Glimmer  | Eklogit   | Marmor |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15205133 |Finero-Peridotit | Peridotit  | –   | – |  Finero-Peridotit |  Perm     | Perm   | Variszisches Grundgebirge  |
|15205134 |Ivrea Mafischer Komplex | Gabbro  | Diorit   | – |  – |  Perm     | Perm   | Variszisches Grundgebirge  |
|15205135 |Sesia-Decke: Zona Dioritico-Kinzigitica | Gneis: granulitisch  | Gestein: basisch   | Marmor |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15205136 |Südalpin: Prävariszischer Orthogneis | Gneis: magmatisch  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15205137 |Pontida-Fm. | Sandstein  | Tonstein   | – |  Pontida-Formation |  Coniacien     | Turonien   | Flysch  |
|15205138 |Arolla-Einheit: Metagranit | Granit  | –   | – |  – |  Perm     | Perm   | Variszisches Grundgebirge  |
|15205139 |Arolla-Einheit: Leukokrater Granitgneis | Gneis: granitisch  | –   | – |  – |  Perm     | Perm   | Variszisches Grundgebirge  |
|15206001 |Periadriatische Vulkanite | Gestein: vulkanisch  | –   | – |  – |  Paläogen     | Paläogen   | Periadriatisches Vulkanismus  |
|15206002 |Novate-Intrusiva | Granit  | –   | – |  – |  Frühes Miozän     | Chattien   | Novate-Intrusion  |
|15206003 |Bergell-Intrusiva | Granodiorit  | Tonalit   | Granit |  – |  Oligozän     | Oligozän   | Bregaglia-Intrusion  |
|15206004 |Adamello-Intrusiva | Granodiorit  | Tonalit   | Granit |  – |  Rupélien     | Priabonien   | Adamello-Intrusion  |
|15206005 |Melirolo-Augengneis | Gneis: augig  | –   | – |  Melirolo-Augengneis |  Rupélien     | Rupélien   | Bregaglia-Intrusion  |
|15206006 |Bergell-Intrusiva: Granodioritische Fazies | Granodiorit  | –   | – |  – |  Rupélien     | Rupélien   | Bregaglia-Intrusion  |
|15206007 |Bergell-Intrusiva: Tonalitische Fazies | Tonalit  | –   | – |  – |  Rupélien     | Rupélien   | Bregaglia-Intrusion  |
|15206008 |Monte-Bassetta-Quarzdiorit | Diorit: Quarz  | –   | – |  Monte-Bassetta-Quarzdiorit |  Rupélien     | Rupélien   | Bregaglia-Intrusion  |
|15206009 |Sorico-Tonalit | Tonalit  | –   | – |  Sorico-Tonalit |  Rupélien     | Rupélien   | Bregaglia-Intrusion  |
|15206010 |Jorio-Tonalit | Tonalit  | –   | – |  Jorio-Tonalit |  Rupélien     | Rupélien   | Bregaglia-Intrusion  |
|15206011 |Val-Masino-Granodiorit | Granodiorit  | –   | – |  Val-Masino-Granodiorit |  Rupélien     | Rupélien   | Bregaglia-Intrusion  |
|15206012 |Alpe-Cameraccio-Granodiorit | Granodiorit  | –   | – |  Alpe-Cameraccio-Granodiorit |  Rupélien     | Rupélien   | Bregaglia-Intrusion  |
|15206013 |Monte-Rosso-Mikrogranit | Granit: mikrokristallin  | –   | – |  Monte-Rosso-Mikrogranit |  Oligozän     | Oligozän   | Bregaglia-Intrusion  |
|15206014 |Zocca-Aplit | Aplit  | –   | – |  Zocca-Aplit |  Oligozän     | Oligozän   | Bregaglia-Intrusion  |
|15206015 |San-Fedelino-Granit | Granit  | –   | – |  San-Fedelino-Granit |  Chattien     | Chattien   | Novate-Intrusion  |
|15206016 |Undifferenzierte Einheit | Gestein  | –   | – |  – |  Känozoikum     | Proterozoikum   | –  |
|15206017 |Undifferenzierte lithologische Einheit: Tektonische Brekzie | Brekzie: tektonisch  | –   | – |  – |  Holozän     | Proterozoikum   | –  |
|15206018 |Lochsiten-Kalk | 15111475  | –   | – |  Lochsiten-Kalk |  Tertiär     | Mesozoikum   | Sedimentbedeckung  |
|15206019 |Salleren-Brekzie | Brekzie: tektonisch  | –   | – |  Salleren-Brekzie |  Tertiär     | Mesozoikum   | Sedimentbedeckung  |
|15206020 |Undifferenzierte lithologische Einheit | Gestein  | –   | – |  – |  Känozoikum     | Proterozoikum   | –  |
|15202364 |Kiental-Melange | Tonstein  | Sandstein   | – |  Kiental-Melange |  Späte Kreide     | Späte Kreide   | Mélange  |
|15202361 |Plaine-Morte-Melange | Mergelstein  | Sandstein   | – |  Plaine-Morte-Melange |  Tertiär     | Späte Kreide   | Mélange  |
|15202362 |Mättental-Melange | Tonstein  | Mergelstein   | Sandstein |  Mättental-Melange |  Rupélien     | Priabonien   | Mélange  |
|15202363 |Meilleret-Fm.: Höchst-Flysch | Sandstein  | –   | – |  Höchst-Flysch |  Priabonien     | Mittleres Eozän   | Flysch  |
|15202365 |Termen-Zone: Tonschiefer | Schiefer: Glimmer-Granat  | –   | – |  – |  Toarcien     | Pliensbachien   | Sedimentbedeckung  |
|15202366 |Termen-Zone: Kalkschiefer | Schiefer: kalkig  | Marmor: kalkig   | – |  – |  Pliensbachien     | Rhät   | Sedimentbedeckung  |
|15202367 |Nufenen-Zone: Knotenschiefer | Schiefer: kalkig: Zoisit  | Marmor: kalkig   | – |  – |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202368 |Nufenen-Zone: Sandstein | Sandstein: Quarz  | Schiefer: tonig-kalkig   | – |  – |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202369 |Nufenen-Zone: Granatschiefer | Schiefer: Glimmer-Granat  | –   | – |  – |  Sinémurien     | Rhät   | Lias-Dogger in neritischer Fazies  |
|15202370 |Stgir-Fm.: Unterer Teil | Tonstein: schiefrig  | Kalkstein: Bioklasten   | Kalkstein: sandig |  Stgir-Formation |  Sinémurien     | Rhät   | Lias-Dogger in neritischer Fazies  |
|15202371 |Stgir-Fm.: Oberer Teil | Sandstein: Quarz  | Kalkstein: sandig-spätig   | Tonstein: schiefrig |  Stgir-Formation |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202372 |Inferno-Fm.: Oberer Teil: Runcaleida-Sch. | Sandstein: Quarz  | Kalkstein: Bioklasten   | Tonstein: schiefrig |  Runcaldeida-Schichten |  Toarcien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202373 |Inferno-Fm.: Unterer Teil: Riein-Sch. | Kalkstein: sandig  | –   | – |  Riein-Schichten |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202374 |Meierhof-Phyllit | Phyllit  | Schiefer: Serizit   | – |  Meierhof-Phyllit |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15202375 |Waltensburg-Verrucano | Rhyolith  | Sandstein   | Konglomerat |  Waltensburg-Verrucano |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15202376 |Ruinas Sandstein | Sandstein  | Rhyolith   | Tonstein |  Ruinas-Sandstein |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15202377 |Niederhorn-Fm.: Hohgant-Sandstein: Berglikehle-Bk. | Kalkstein: Bitumen  | Mergelstein: Kohle   | – |  Berglikehle-Bank |  Priabonien     | Priabonien   | «Nummulitikum»  |
|15202378 |Rossplatten-Diorit | Diorit  | Granit   | – |  Rossplatten-Diorit |  Pennsylvanien     | Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202379 |Schöllenen-Diorit | Diorit  | –   | – |  Schöllenen-Diorit |  Spätes Pennsylvanien     | Mittleres Pennsylvanien   | Mittelvariszisches Grundgebirge  |
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
|15202394 |Stad-Fm.: Spirstock-Mb. | Sandstein: Quarz  | Mergelstein   | – |  Spirstock-Member |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202395 |Seewen-Fm.: Roter-Seewer-Kalk | Kalkstein: mikritisch  | –   | – |  «Roter Seewenkalk» |  Turonien     | Turonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202396 |Seewen-Fm.: Untere Götzis-Bk. | Sandstein: Glaukonit  | –   | – |  Untere Götzis-Bank |  Turonien     | Cénomanien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202397 |Garschella-Fm.: Grünten-Mb.: Col-de-la-Plaine-Morte-Bk. | Sandstein: mergelig: Glaukonit  | –   | – |  Col-de-la-Plaine-Morte-Bank |  Aptien     | Aptien   | «Gault»  |
|15202398 |Betlis-Fm.: Oberer Teil | Kalkstein: Bioklasten-Chert  | –   | – |  «Oberer Betliskalk» |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202399 |Betlis-Fm.: Unterer Teil | Kalkstein: sandig: Bioklasten  | Kalkstein: spätig   | – |  «Unterer Betliskalk» |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202400 |Bommerstein-Fm.: Vättis-Brekzie | Kalkstein: spätig: Bioklasten  | Kalkstein: Glaukonit   | – |  Vättis-Fossilbrekzie |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15202401 |Inferno-Fm.: Oberer Teil | Schiefer: kalkig: Zoisit  | Kalkstein: spätig: Echinodermen   | – |  Inferno-Formation |  Toarcien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202402 |Inferno-Fm.: Mittlerer Teil | Schiefer: Zoisit  | Mergelstein: Bioklasten   | – |  Inferno-Formation |  Toarcien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202403 |Inferno-Fm.: Unterer Teil | Kalkstein  | Schiefer: Zoisit   | Mergelstein: Bioklasten |  Inferno-Formation |  Toarcien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202404 |Sexmor-Fm.: Oberer Teil | Kalkstein: kieselig  | Kalkstein: spätig   | Kalkstein: sandig |  Sexmor-Formation |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202405 |Sexmor-Fm.: Unterer Teil | Mergelstein: kalkig  | Kalkstein: kieselig   | Kalkstein: spätig: Bioklasten |  Sexmor-Formation |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202406 |Prodkamm-Fm.: Unterer Teil: Leitoolith | Kalkstein: Bioklasten-Ooide  | –   | – |  «Leitoolith» (Prodkamm-Fm.) |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15202411 |Stad-Fm.: Lochegg-Brekzie | Brekzie: kalkig: Bioklasten  | –   | – |  Lochegg-Brekzie |  Eozän     | Eozän   | Syn-Kollision  |
|15202412 |Zementstein-Fm.: Oberer Teil | Mergelstein: schiefrig  | Kalkstein: mikritisch   | – |  15253121 |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202413 |Zementstein-Fm.: Unterer Teil | Mergelstein  | Kalkstein: mergelig   | – |  15253121 |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202414 |Bommerstein-Fm.: Glockhaus-Mb.: Roter Echinodermenkalk | Kalkstein: spätig: Bioklasten  | –   | – |  «Rote Echinodermenbrekzie» (Bommerstein-Fm.) |  Bajocien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15202415 |Bommerstein-Fm.: Glockhaus-Mb.: Obere Tonschiefer | Tonstein: schiefrig  | Mergelstein: siltig-schiefrig   | – |  «Obere Tonschiefer» (Bommerstein-Fm.) |  Bajocien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15202416 |Bommerstein-Fm.: Glockhaus-Mb. | Sandstein: Quarz  | Kalkstein: sandig: Bioklasten   | Tonstein |  Glockhaus-Member |  Bajocien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15202417 |Coroi-Fm.: Basaler Quarzit | Sandstein: Quarz  | –   | – |  «Basaler Quarzit» (Coroi-Fm.) |  Aalénien     | Aalénien   | Syn-Rift  |
|15202418 |Röti-Fm.: Rauwacke | Rauwacke  | –   | – |  Röti-Formation |  Carnien     | Anisien   | Muschelkalk  |
|15202419 |Vieux-Emosson-Fm.: Col-du-Jorat-Mb. | Tonstein  | Sandstein   | Dolomitstein |  Col-du-Jorat-Member |  Anisien     | Anisien   | Buntsandstein  |
|15202420 |Quarten-Fm.: Equisetenschiefer | Tonstein: schiefrig  | Siltstein: schiefrig   | – |  Quarten-Formation |  Späte Trias     | Späte Trias   | Keuper  |
|15202421 |Amden-Fm.: Leist-Mergel | Mergelstein  | –   | – |  Leist-Mergel |  Campanien     | Santonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202422 |Amden Fm.: Leiboden-Mergel | Mergelstein: Bioklasten  | –   | – |  Leiboden-Mergel |  Santonien     | Coniacien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202423 |Covayes-Fm. | Mergelstein  | Kalkstein: mikritisch   | – |  Covayes-Formation |  Turonien     | Turonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202424 |Javrex-Fm. | Kalkstein: arenitisch  | Kalkstein: sandig: Glaukonit   | – |  Javrex-Formation |  Albien     | Aptien   | «Gault»  |
|15202425 |Javrex-Fm.: Mergelstein-Fazies | Mergelstein  | –   | – |  Javrex-Formation |  Albien     | Aptien   | «Gault»  |
|15202426 |Javrex-Fm.: Kalksandstein-Fazies | Kalkstein: sandig: Glaukonit  | Mergelstein: siltig: Glaukonit   | – |  Javrex-Formation |  Aptien     | Aptien   | «Gault»  |
|15203626 |Pizzo-del-Vallone-Decke: Dogger-Malm | Sandstein  | Schiefer: Glimmer   | Marmor |  – |  Später Jura     | Mittlerer Jura   | Sedimentbedeckung  |
|15203623 |Monte-Leone-Decke: Trias | Quarzit  | Marmor   | Rauwacke |  – |  Trias     | Trias   | Prä-Rift  |
|15203624 |Monte-Leone-Decke: Quarzitische Trias | Quarzit  | –   | – |  – |  Trias     | Trias   | Prä-Rift  |
|15203625 |Pizzo-del-Vallone-Decke: Sedimentbedeckung | Schiefer  | Marmor   | Sandstein |  – |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15203627 |Pizzo-del-Vallone-Decke: Dogger-Malm: Marmor | Marmor  | –   | – |  – |  Später Jura     | Mittlerer Jura   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15203628 |Pizzo-del-Vallone-Decke: Dogger-Malm: Glimmerschiefer | Schiefer: Glimmer  | –   | – |  – |  Später Jura     | Mittlerer Jura   | Post-Rift Mesozoikum in detritischer Fazies  |
|15203629 |Pizzo-del-Vallone-Decke: Dogger-Malm: Vulkanit | Gestein: vulkanisch  | –   | – |  – |  Später Jura     | Mittlerer Jura   | Sedimentbedeckung  |
|15203630 |Pizzo-del-Vallone-Decke: Lias | Konglomerat  | Quarzit   | Schiefer: Glimmer |  – |  Aalénien     | Früher Jura   | Syn-Rift  |
|15203631 |Pizzo-del-Vallone-Decke: Trias | Rauwacke  | Marmor   | Evaporit: Gips |  – |  Trias     | Trias   | Prä-Rift  |
|15203632 |Mont-Fort-Decke: Sedimentbedeckung | Brekzie  | Marmor   | Rauwacke |  – |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15203633 |Mont-Fort-Decke: Trias | Marmor: dolomitisch  | Marmor: kalkig   | Rauwacke |  – |  Trias     | Trias   | Sedimentbedeckung  |
|15203634 |Mont-Fort-Decke: Trias: Rauwacke | Rauwacke  | –   | – |  – |  Trias     | Trias   | Sedimentbedeckung  |
|15203635 |Métailler-Fm.: Quarzit | Quarzit  | –   | – |  – |  Ordovizium     | Ordovizium   | Grundgebirge  |
|15203636 |Métailler-Fm.: Glimmerschiefer | Schiefer: Glimmer  | –   | – |  – |  Ordovizium     | Ordovizium   | Grundgebirge  |
|15203637 |Métailler-Fm.: Chloritoid-Glimmerschiefer | Schiefer: Glimmer-Chloritoid  | –   | – |  – |  Ordovizium     | Ordovizium   | Grundgebirge  |
|15203638 |Distulberg-Fm.: Schiefer | Schiefer  | –   | – |  – |  Kambrium     | Kambrium   | Grundgebirge  |
|15203639 |Distulberg-Fm.: Albitgneis | Gneis: Albit  | –   | – |  – |  Kambrium     | Kambrium   | Grundgebirge  |
|15203640 |Barrhorn-Einheit: Trias | Dolomitstein  | Rauwacke   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15203641 |Siviez-Mischabel-Decke: Aplit | Aplit  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203642 |Siviez-Mischabel-Decke: Pegmatit | Pegmatit  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203643 |Lirec-Fm.: Leukokrater Mikroklingneis | Gneis: Mikroklin  | –   | – |  Lirec-Formation |  Kambrium     | Kambrium   | Grundgebirge  |
|15203644 |Adlerflüe-Fm.: Leukokrater Gneiss | Gneis  | –   | – |  Adlerflüe-Formation |  Kambrium     | Proterozoikum   | Grundgebirge  |
|15203645 |Ergischhorn-Komplex: Leukokrater aplitischer Gneis | Gneis: aplitisch  | –   | – |  Ergischhorn-Komplex |  Proterozoikum     | Proterozoikum   | Grundgebirge  |
|15203646 |Stalden-Gneiskomplex | Gneis  | –   | – |  Stalden-Gneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203647 |Stalden-Gneiskomplex: Ahorn-Augengneis | Gneis: augig  | –   | – |  Ahorn-Augengneiss |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203648 |Stalden-Gneiskomplex: Amphibolit | Amphibolit  | –   | – |  Stalden-Gneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203649 |Printse-Fm.: Konglomerat | Konglomerat  | –   | – |  Printse-Formation |  Perm     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15203650 |Printse-Fm.: Graphitschiefer | Schiefer: Graphit  | Schiefer: tonig: Anthrazit   | – |  Printse-Formation |  Perm     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15203651 |Portjengrat-Decke: Kalzitmarmor | Marmor: kalkig  | –   | – |  – |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15203652 |Portjengrat-Decke: Dolomitmarmor | Marmor: dolomitisch  | –   | – |  – |  Trias     | Trias   | Sedimentbedeckung  |
|15203653 |Portjengrat-Decke: Arkose | Sandstein: Feldspat  | –   | – |  – |  Trias     | Trias   | Prä-Rift  |
|15203654 |Portjengrat-Decke: Grundgebirge | Gneis: migmatitisch  | Gneis   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203655 |Gornergrat-Decke: Kalkschiefer, sandiger Marmor, Brekzie | Schiefer: kalkig  | Marmor: sandig   | Brekzie |  – |  Mesozoikum     | Mesozoikum   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203656 |Gornergrat-Decke: Trias | Marmor: dolomitisch  | Marmor: kalkig   | Rauwacke |  – |  Trias     | Trias   | Karbonatische Trias  |
|15203657 |Gornergrat-Decke: Phengit-Albitgneis | Gneis: Albit  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203658 |Gornergrat-Decke: Basisches Ganggestein | Gestein: basisch-gangartig  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203659 |Gornergrat-Decke: Granat-Muskovit-Schiefer | Schiefer: Glimmer-Granat  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203660 |Frilihorn-Decke: Trias | Marmor: dolomitisch  | Marmor: kalkig   | Rauwacke |  – |  Trias     | Trias   | Karbonatische Trias  |
|15203661 |Frilihorn-Decke: Trias: Rauwacke | Rauwacke  | –   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15203662 |Garda-Bordon-Fm.: Série feuilletée | Schiefer: tonig: Bitumen  | –   | – |  Garda-Bordon-Formation |  Kreide     | Kreide   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203663 |Garda-Bordon-Fm.: Quarzschiefer | Schiefer: Quarz  | –   | – |  Garda-Bordon-Formation |  Kreide     | Kreide   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203664 |Serra-Neire-Serpentinit | Serpentinit  | –   | – |  Serra-Neire-Serpentinit |  Jura     | Jura   | Ophiolithische Abfolge  |
|15203665 |Zermatt-Saas-Decke: Eklogit | Eklogit  | –   | – |  – |  Jura     | Jura   | Ophiolithische Abfolge  |
|15203666 |Zermatt-Saas-Decke: Metapyroxenit | 15111466  | –   | – |  – |  Jura     | Jura   | Ophiolithische Abfolge  |
|15203667 |Zermatt-Saas-Decke: Metagabbro | Gabbro  | –   | – |  – |  Jura     | Jura   | Ophiolithische Abfolge  |
|15203668 |Zermatt-Saas-Decke: Rodingit | Rodingit  | –   | – |  – |  Jura     | Jura   | Ophiolithische Abfolge  |
|15203669 |Zermatt-Saas-Decke: Talkschiefer | Schiefer: Talk  | –   | – |  – |  Jura     | Jura   | Ophiolithische Abfolge  |
|15203670 |Lengenbach-Dolomitmarmor | Marmor: dolomitisch  | –   | – |  Lengenbach-Dolomitmarmor |  Trias     | Trias   | Prä-Rift  |
|15204001 |God-Drosa-Flysch | Tonstein: kieselig  | Sandstein: Feldspat   | Kalkstein: arenitisch |  God-Drosa-Flysch |  Turonien     | Cénomanien   | Flysch  |
|15204002 |Chanèls-Fm. | Kalkstein: mergelig-schiefrig  | Tonstein: kalkig: Glaukonit   | – |  Chanèls-Formation |  Turonien     | Aptien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15204003 |Lech-Fm. | Gestein: pelitisch  | Gestein: pelitisch   | – |  Lech-Formation |  Cénomanien     | Frühe Kreide   | Flysch  |
|15204004 |Emmat-Fm. | Tonstein: kieselig  | Mergelstein   | Kalkstein: mikritisch |  Emmat-Formation |  Albien     | Aptien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15204005 |Russenna-Fm. | Kalkstein: mikritisch: Chert  | Tonstein   | Kalkstein: spätig: Bioklasten |  Russenna-Formation |  Aptien     | Tithonien   | Maiolica / Aptychenkalk  |
|15204006 |Ammergau-Fm. | Kalkstein: mikritisch: Aptychen  | –   | – |  Ammergau-Formation |  Frühe Kreide     | Später Jura   | Maiolica / Aptychenkalk  |
|15204007 |Blais-Fm. | Gestein: kieselig: Radiolarien  | Tonstein: kieselig   | Kalkstein: mikritisch: Bioklasten |  Blais-Radiolarit |  Tithonien     | Callovien   | Radiolarit  |
|15204008 |Blais-Fm.: Plattas-Mb. | Kalkstein: mikritisch: Bioklasten-Chert  | –   | – |  Plattas-Member |  Tithonien     | Tithonien   | Radiolarit  |
|15204009 |Ruhpolding-Fm. | 15111108  | –   | – |  Ruhpolding-Formation |  Tithonien     | Oxfordien   | Radiolarit  |
|15204010 |Ostalpin: Dogger | Brekzie: polymikt  | Sandstein   | Tonstein |  – |  Callovien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15204011 |Saluver-Fm. | Brekzie: polymikt  | Sandstein   | Tonstein: schiefrig |  Saluver-Formation |  Mittlerer Jura     | Mittlerer Jura   | Lias-Dogger in neritischer Fazies  |
|15204012 |Bardella-Fm. | 15111108  | Kalkstein: sandig   | Brekzie: polymikt |  Bardella-Formation |  Mittlerer Jura     | Mittlerer Jura   | Sedimentbedeckung  |
|15204013 |Salteras-Fm. | 15111108  | Sandstein: Glimmer   | Brekzie: polymikt |  Salteras-Formation |  Mittlerer Jura     | Mittlerer Jura   | Sedimentbedeckung  |
|15204014 |Salamun-Brekzie | 15111009  | –   | – |  Salamun-Brekzie |  Mittlerer Jura     | Mittlerer Jura   | Sedimentbedeckung  |
|15204015 |Err-Brekzie | 15111009  | –   | – |  Err-Brekzie |  Mittlerer Jura     | Mittlerer Jura   | Sedimentbedeckung  |
|15204016 |Allgäu-Fm. | Mergelstein  | Kalkstein: tonig   | Kalkstein: arenitisch |  Allgäu-Formation |  Callovien     | Hettangien   | Syn-Rift  |
|15206024 |Undifferenzierte lithologische Einheit: Ganggestein | Gestein: gangartig  | –   | – |  – |  Känozoikum     | Proterozoikum   | –  |
|15206021 |Undifferenzierte lithologische Einheit: Gips | Evaporit: Gips  | –   | – |  – |  Trias     | Trias   | Sedimentbedeckung  |
|15206022 |Undifferenzierte lithologische Einheit: Rauwacke | Rauwacke  | –   | – |  – |  Trias     | Trias   | Sedimentbedeckung  |
|15206023 |Undifferenzierte lithologische Einheit: Dolomitmarmor | Dolomitstein  | –   | – |  – |  Trias     | Trias   | Sedimentbedeckung  |
|15206025 |Undifferenzierte stratigraphische Einheit: Lias | Kalkstein  | Gestein: pelitisch   | – |  – |  Früher Jura     | Früher Jura   | Sedimentbedeckung  |
|15206026 |Undifferenzierte stratigraphische Einheit: Dogger | Mergelstein  | Kalkstein   | Sandstein |  – |  Mittlerer Jura     | Mittlerer Jura   | Sedimentbedeckung  |
|15206027 |Undifferenzierte stratigraphische Einheit: Malm | Kalkstein  | Mergelstein   | – |  – |  Später Jura     | Später Jura   | Sedimentbedeckung  |
|15206028 |Undifferenzierte stratigraphische Einheit: Kreide | Kalkstein  | Mergelstein   | Sandstein |  – |  Kreide     | Kreide   | Sedimentbedeckung  |
|15206029 |Undifferenzierte stratigraphische Einheit: Trias | Dolomitstein  | Evaporit   | Gestein: klastisch |  – |  Trias     | Trias   | Prä-Rift  |
|15206030 |Undifferenzierte lithologische Einheit: Sedimentgestein | Gestein: sedimentär  | –   | – |  – |  Känozoikum     | Proterozoikum   | –  |
|15206031 |Undifferenzierte lithologische Einheit: Kristallingestein | Gestein: kristallin  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15206032 |Undifferenzierte lithologische Einheit: Granit | Granit  | –   | – |  – |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15206033 |Undifferenzierte stratigraphische Einheit | Gestein  | –   | – |  – |  Känozoikum     | Paläozoikum   | –  |
|15206034 |Undifferenzierte stratigraphische Einheit: Mesozoikum | Gestein  | –   | – |  – |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15206035 |Undifferenzierte lithologische Einheit: Rhyolith | Rhyolith  | –   | – |  – |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15206036 |Undifferenzierte lithologische Einheit: Grüngestein | Amphibolit  | Prasinit   | – |  – |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15206037 |Undifferenzierte lithologische Einheit: Amphibolit | Amphibolit  | –   | – |  – |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15206038 |Undifferenzierte lithologische Einheit: Quarzgang | Gestein: gangartig: Quarz  | –   | – |  – |  Känozoikum     | Proterozoikum   | –  |
|15206039 |Undifferenzierte lithologische Einheit: Aplit | Aplit  | –   | – |  – |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15206040 |Undifferenzierte lithologische Einheit: Pegmatit | Pegmatit  | –   | – |  – |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15206041 |Undifferenzierte lithologische Einheit: Prasinit | Prasinit  | –   | – |  – |  Känozoikum     | Proterozoikum   | –  |
|15206042 |Undifferenzierte lithologische Einheit: Serpentinit | Serpentinit  | –   | – |  – |  Känozoikum     | Proterozoikum   | –  |
|15206043 |Undifferenzierte lithologische Einheit: Mineralisierter Gang | Gestein: gangartig  | –   | – |  – |  Känozoikum     | Proterozoikum   | –  |
|15206044 |Undifferenzierte lithologische Einheit: Mikrogranit | Granit: mikrokristallin  | –   | – |  – |  Känozoikum     | Proterozoikum   | Grundgebirge  |
|15206045 |Undifferenzierte stratigraphische Einheit: Rhät | Kalkstein  | Gestein: pelitisch   | Dolomitstein |  – |  Hettangien     | Rhät   | «Rhät»  |
|15206046 |Undifferenzierte lithologische Einheit: Biogener Kalkstein | Kalkstein: Bioklasten  | –   | – |  – |  Priabonien     | Lutétien   | «Nummulitikum»  |
|15206047 |Undifferenzierte lithologische Einheit: Rodingit | Rodingit  | –   | – |  – |  Känozoikum     | Proterozoikum   | Ophiolithische Abfolge  |
|15206048 |Undifferenzierte lithologische Einheit: Saures Ganggestein | Gestein: saur-gangartig  | –   | – |  – |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15206049 |Undifferenzierte lithologische Einheit: Basisches Ganggestein | Gestein: basisch-gangartig  | –   | – |  – |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15206050 |Undifferenzierte lithologische Einheit: Eklogit | Eklogit  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15206051 |Undifferenzierte lithologische Einheit: Mylonit | Mylonit  | –   | – |  – |  Känozoikum     | Proterozoikum   | –  |
|15206052 |Undifferenzierte lithologische Einheit: Kalksilikatfels | Granofels: Kalksilikat  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15206053 |Undifferenzierte lithologische Einheit: Marmor | Marmor  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15206054 |Undifferenzierte lithologische Einheit: Sedimentäre Brekzie | Brekzie: sedimentär  | –   | – |  – |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15206055 |Undifferenzierte stratigraphische Einheit: Paläozoikum | Gestein: sedimentär  | Gestein: magmatisch   | Gestein: metamorph |  – |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15206056 |Undifferenzierte stratigraphische Einheit: Känozoikum | Gestein  | –   | – |  – |  Känozoikum     | Känozoikum   | Sedimentbedeckung  |
|15206057 |Undifferenzierte lithologische Einheit: Ultramafisches Gestein | Gestein: ultramafisch  | –   | – |  – |  Känozoikum     | Proterozoikum   | –  |
|15206058 |Undifferenzierte lithologische Einheit: Verwitterter Fels | Gestein: residual  | –   | – |  – |  Holozän     | Paläozoikum   | –  |
|15206059 |Undifferenzierte lithologische Einheit: Ophikalzit | Serpentinit: brekziös: Karbonat  | –   | – |  – |  Mesozoikum     | Mesozoikum   | Ophiolithische Abfolge  |
|15206060 |Undifferenzierte lithologische Einheit: Talkschiefer | Schiefer: Talk  | –   | – |  – |  Phanerozoikum     | Phanerozoikum   | Sedimentbedeckung  |
|15206061 |Undifferenzierte lithologische Einheit: Mirkodiorit | Diorit: mikrokristallin  | –   | – |  – |  Phanerozoikum     | Phanerozoikum   | –  |
|15206062 |Undifferenzierte lithologische Einheit: Quarzit | Quarzit  | –   | – |  – |  Phanerozoikum     | Phanerozoikum   | –  |
|15206063 |Undifferenzierte lithologische Einheit: Fuchsit-Zoisitschiefer | Schiefer: Zoisit-Fuchsit  | –   | – |  – |  Phanerozoikum     | Phanerozoikum   | –  |
|15206064 |Undifferenzierte lithologische Einheit: Konglomerat | Konglomerat  | –   | – |  – |  Phanerozoikum     | Phanerozoikum   | Sedimentbedeckung  |
|15206065 |Undifferenzierte lithologische Einheit: Glaukophanschiefer | Schiefer: Glaukophan  | –   | – |  – |  Phanerozoikum     | Phanerozoikum   | –  |
|15206066 |Bündnerschiefer | Schiefer: kalkig  | Schiefer: Glimmer   | – |  – |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15206067 |Undifferenzierte lithologische Einheit: Augengneis | Gneis: augig  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15206068 |Undifferenzierte lithologische Einheit: Granat-Glimmerschiefer | Schiefer: Glimmer-Granat  | –   | – |  – |  Phanerozoikum     | Phanerozoikum   | –  |
|15206069 |Undifferenzierte lithologische Einheit: Albit-Muskowitschiefer | Schiefer: Muskovit-Albit  | –   | – |  – |  Phanerozoikum     | Phanerozoikum   | –  |
|15206070 |Undifferenzierte lithologische Einheit: Gneis | Gneis  | –   | – |  – |  Phanerozoikum     | Phanerozoikum   | Grundgebirge  |
|15206071 |Undifferenzierte lithologische Einheit: Graphitschiefer | Schiefer: Graphit  | –   | – |  – |  Phanerozoikum     | Phanerozoikum   | –  |
|15206072 |Undifferenzierte lithologische Einheit: Glimmerschiefer | Schiefer: Glimmer  | –   | – |  – |  Mesozoikum     | Proterozoikum   | –  |
|15206073 |Undifferenzierte lithologische Einheit: Garbenschiefer | Schiefer  | –   | – |  – |  Mesozoikum     | Proterozoikum   | –  |
|15206074 |Undifferenzierte lithologische Einheit: Diorit | Diorit  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15206075 |Undifferenzierte lithologische Einheit: Gabbro | Gabbro  | –   | – |  – |  Mesozoikum     | Proterozoikum   | –  |
|15206076 |Undifferenzierte lithologische Einheit: Orthogneis | Gneis: magmatisch  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15206077 |Undifferenzierte lithologische Einheit: Paragneis | Gneis: sedimentär  | –   | – |  – |  Mesozoikum     | Proterozoikum   | –  |
|15206078 |Undifferenzierte lithologische Einheit: Vulkanisches Gestein | Gestein: vulkanisch  | –   | – |  – |  Känozoikum     | Proterozoikum   | –  |
|15206079 |Undifferenzierte lithologische Einheit: Basalt | Basalt  | –   | – |  – |  Känozoikum     | Proterozoikum   | –  |
|15206080 |Undifferenzierte stratigraphische Einheit: Karbon | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Karbon     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15206081 |Undifferenzierte lithologische Einheit: Chloritschiefer | Schiefer: Chlorit  | –   | – |  – |  Mesozoikum     | Proterozoikum   | –  |
|15206082 |Undifferenzierte lithologische Einheit: Phyllit | Phyllit  | –   | – |  – |  Mesozoikum     | Proterozoikum   | –  |
|15206083 |Undifferenzierte lithologische Einheit: Quarzphyllit | Phyllit: Quarz  | –   | – |  – |  Mesozoikum     | Proterozoikum   | –  |
|15206084 |Bündnerschiefer: Kalkschiefer | Schiefer: kalkig  | –   | – |  – |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15206085 |Bündnerschiefer: Tonschiefer | Schiefer: tonig  | –   | – |  – |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15206086 |Undifferenzierte lithologische Einheit: Migmatit | Migmatit  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15206087 |Undifferenzierte lithologische Einheit: Tonalit | Tonalit  | –   | – |  – |  Känozoikum     | Paläozoikum   | –  |
|15206088 |Undifferenzierte lithologische Einheit: Syenit | Syenit  | –   | – |  – |  Paläozoikum     | Paläozoikum   | –  |
|15202431 |Villarbeney-Fm.: Riondouneire-Mb. | Kalkstein: mikritisch  | Mergelstein   | Kalkstein: arenitisch |  Riondouneire-Member |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202427 |Montsalvens-Kalkarenit | Kalkstein: arenitisch: Bioklasten  | –   | – |  Montsalvens-Kalkarenit |  Barrémien     | Barrémien   | «Urgonien»  |
|15202429 |Villarbeney-Fm. | Kalkstein: mikritisch  | Mergelstein   | – |  Villarbeney-Formation |  Aptien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202430 |Villarbeney-Fm.: Veveyse-de-Châtel-Mb. | Kalkstein: mikritisch  | Mergelstein   | Kalkstein: kieselig |  Veveyse-de-Châtel-Member |  Barrémien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202432 |Jogne-Fm. | Kalkstein: mikritisch  | Mergelstein   | – |  Jogne-Formation |  Tithonien     | Oxfordien   | Malm  |
|15202433 |Jogne-Fm.: Kalkbrekzie | Brekzie: kalkig  | –   | – |  Jogne-Formation |  Tithonien     | Tithonien   | Malm  |
|15202434 |Jogne-Fm.: Vuavres-Mb. | Kalkstein: mikritisch: Chert  | Mergelstein   | – |  Vuavres-Member |  Tithonien     | Kimméridgien   | Malm  |
|15202435 |Jogne-Fm.: Planière-Mb. | Kalkstein: mikritisch  | Mergelstein   | – |  Planière-Member |  Oxfordien     | Oxfordien   | Malm  |
|15202436 |Bifé-Fm. | Tonstein: schiefrig  | Mergelstein   | Kalkstein: tonig |  Bifé-Formation |  Oxfordien     | Callovien   | Lias-Dogger in pelagischer Fazies  |
|15202437 |Bifé-Fm.: Zementkalk | Kalkstein  | –   | – |  Bifé-Formation |  Oxfordien     | Oxfordien   | Lias-Dogger in pelagischer Fazies  |
|15202438 |Bifé-Fm.: Joux-Galez-Mb. | Mergelstein: Glimmer  | –   | – |  Joux-Galez-Member |  Oxfordien     | Callovien   | Lias-Dogger in pelagischer Fazies  |
|15202439 |Pereyre-Fm. | Kalkstein: spätig: Bioklasten  | Kalkstein: Ooide   | Kalkstein: sandig: Glaukonit |  Pereyres-Formation |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15202440 |Praz-Couquain-Fm. | Kalkstein: tonig  | Mergelstein: schiefrig   | Kalkstein: sandig: Bioklasten |  Praz-Couquain-Formation |  Bajocien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15202442 |Gryonne-Fm. | Mergelstein: schiefrig  | Kalkstein: mergelig   | Kalkstein: kieselig |  Gryonne-Formation |  Früher Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15202443 |Praz-Couquain-Fm.: Taffon-Mb. | Mergelstein: schiefrig  | Kalkstein   | – |  Taffon-Member |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15202444 |Praz-Couquain-Fm.: Saix-Mb. | Sandstein  | Mergelstein: Glimmer   | Kalkstein |  Saix-Member |  Aalénien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15202445 |Villarbeney-Fm.: Cergnement-Mb. | Kalkstein: mikritisch  | Mergelstein   | – |  Cergnement-Member |  Barrémien     | Barrémien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202446 |Arveyes-Flysch | Mergelstein  | Sandstein: kalkig: Glimmer   | – |  Arveyes-Flysch |  Eozän     | Eozän   | Flysch  |
|15202447 |Sex-Mort-Flysch | Mergelstein  | Sandstein: kalkig: Bioklasten   | – |  Sex-Mort-Flysch |  Priabonien     | Priabonien   | Flysch  |
|15202448 |Diechtergletscher-Fm.: Maasplanggstock-Metaandesit | Andesit  | –   | – |  Maasplanggstock-Metaandesit |  Cisuralien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202449 |Dammagletscher-Diorit | Diorit  | –   | – |  Dammagletscher-Diorit |  Spätes Pennsylvanien     | Spätes Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202450 |Gryonne-Fm.: Schiefrige Fazies | Mergelstein: schiefrig  | –   | – |  Gryonne-Formation |  Toarcien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15202451 |Gryonne-Fm.: Kalkige Fazies | Kalkstein: kieselig  | Mergelstein   | – |  Gryonne-Formation |  Pliensbachien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15202452 |Gryonne-Fm.: Basaler Teil | Kalkstein: Bioklasten  | Mergelstein: sandig: Glimmer   | – |  Gryonne-Formation |  Hettangien     | Rhät   | «Rhät»  |
|15202453 |Glarner-Verrucano: Tektonisierte Basis | Schiefer: konglomeratisch  | Gneis: mylonitisch   | – |  – |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202454 |Chrüzlistock-Migmatit | Migmatit  | Gneis: migmatitisch   | – |  Chrüzlistock-Migmatit |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202455 |Piz-Cuolmet-Gneiskomplex | Gneis: migmatitisch  | Gneis: gebändert   | Schiefer: Serizit-Chlorit |  Piz-Cuolmet-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202456 |Pulanera-Gneiskomplex | Gneis  | Schiefer   | – |  Pulanera-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202465 |Aiguilles-Rouges-Massiv: Spät- bis postvariszische Sedimente und Vulkanite | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Perm     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202467 |Helvetikum: Variszisches Kristallin | Gneis  | Schiefer   | Gestein: magmatisch |  – |  Paläozoikum     | Proterozoikum   | Variszisches Grundgebirge  |
|15202468 |Helvetikum: Prävariszisches polyzyklisches Grundgebirge | Gneis  | Schiefer   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202469 |Helvetikum: Grundgebirge | Gneis  | Schiefer   | Gestein: magmatisch |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15202472 |Catogne-Gneiskomplex | Migmatit  | Gneis: migmatitisch   | Amphibolit |  Catogne-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202473 |Grépillons-Leukogranit | Granit: mikrokristallin-porphyrisch  | –   | – |  Grépillons-Leukogranit |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202474 |Arpette-Leukogranit | Granit: mikrokristallin  | –   | – |  Arpette-Leukogranit |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202475 |Gärsthorn-Gneiskomplex: Bitschji-Augengneis | Gneis: augig  | –   | – |  Bitschji-Augengneis |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202476 |Gärsthorn-Gneiskomplex: Geimen-Augengneis | Gneis: augig  | –   | – |  Geimen-Augengneis |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202477 |Mont-Blanc-Massiv: Prävariszische Migmatite | Migmatit  | Gneis   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202478 |Mont-Blanc-Massiv: Prävariszisches Grundgebirge: Amphibolit-reiche Fazies | Gneis: migmatitisch  | Amphibolit   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202479 |Mont-Blanc-Massiv: Prävariszisches Grundgebirge: Mylonit | Gneis: mylonitisch  | Mylonit   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202480 |Morcles-Mikrogranit | Granit: mikrokristallin  | –   | – |  Morcles-Mikrogranit |  Spätes Pennsylvanien     | Spätes Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202481 |Aiguilles-Rouges-Massiv: Prävariszisches Migmatite | Migmatit  | Gneis   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202482 |Fully-Gneiskomplex | Migmatit  | –   | – |  Fully-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202483 |Hinterbalm-Granit | Granit  | –   | – |  Hinterbalm-Granit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202484 |Balmenegg-Granit | Granit: porphyrisch: Biotit  | –   | – |  Balmenegg-Granit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202485 |Zentraler-Aare-Granit: Unter-der-Flue-Varietät | Granit: aplitisch  | –   | – |  Unter-der-Flue-Granit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202486 |Pardatschas-Granit | Granit  | Granit: mylonitisch   | – |  Pardatschas-Granit |  Spätes Mississippien     | Spätes Mississippien   | Frühvariszisches Grundgebirge  |
|15202487 |Rossbodenstock-Diorit | Diorit: Quarz-Biotit  | –   | – |  Rossbodenstock-Diorit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202488 |Val-da-Surplattas-Diorit | Diorit  | –   | – |  Val-da-Surplattas-Diorit |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15202489 |Tscharren-Fm.: Rinderbiel-Mikrogranit | Granit: mikrokristallin-porphyrisch  | –   | – |  Rinderbiel-Mikrogranit |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202490 |Leventina-Lucomagno-Decke: Trias: Quarzit | Quarzit  | –   | – |  – |  Trias     | Trias   | Detritische Trias  |
|15202491 |Kapfen-Fm. | Konglomerat  | Sandstein   | – |  Kapfen-Formation |  Lopingien     | Guadalupien   | Spät- bis postvariszisches Grundgebirge  |
|15202492 |Kapfen-Fm.: Sandstein-dominierte Fazies | Sandstein  | –   | – |  Kapfen-Formation |  Lopingien     | Guadalupien   | Spät- bis postvariszisches Grundgebirge  |
|15202493 |Kärpf-Fm.: Kärpfgipfel-Sernifit | Konglomerat  | –   | – |  Kärpfgipfel-Sernifit |  Lopingien     | Guadalupien   | Spät- bis postvariszisches Grundgebirge  |
|15202494 |Fulen-Fm. | Tonstein: sandig-schiefrig  | –   | – |  Fulen-Formation |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15202495 |Karrenstock-Fm.: Glattmatt-Mb. | Tonstein  | Sandstein   | Brekzie |  Glattmatt-Member |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202496 |Mären-Fm.: Grisch-Mb.: Hanenstock-Keratophyr | Trachyt  | –   | – |  Hahnenstock-Keratophyr |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202497 |Mären-Fm.: Grisch-Mb.: Sonnenberg-Horizonte | Sandstein: Feldspat  | Kalkstein   | Tonstein: siltig-schiefrig |  Sonnenberg-Horizonte |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202498 |Mären-Fm.: Grisch-Mb.: Chamseeli-Konglomerat | Konglomerat  | –   | – |  Chamseeli-Konglomerat |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202499 |Murgtal-Fm.: Chartegg-Mb.: Rotberg-Sandstein | Sandstein  | –   | – |  Rotberg-Sandstein |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202500 |Murgtal-Fm.: Seez-Mb. | Konglomerat  | –   | – |  Seez-Member |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202501 |Murgtal-Fm.: Gufelialp-Mb. | Brekzie: siltig  | Tonstein   | Siltstein |  Gufelialp-Member |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202505 |Windgällen-Fm.: Mikrogranit | Granit: mikrokristallin-porphyrisch  | –   | – |  Windgällen-Formation |  Spätes Pennsylvanien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15204020 |Agnelli-Fm. | Kalkstein: kieselig  | Kalkstein: spätig: Bioklasten   | – |  Agnelli-Formation |  Toarcien     | Sinémurien   | Syn-Rift  |
|15204017 |Allgäu-Fm.: Mezzaun-Mb. | Kalkstein: kieselig  | Mergelstein   | – |  Mezzaun-Member |  Callovien     | Aalénien   | Syn-Rift  |
|15204018 |Allgäu-Fm.: Blaisun-Mb. | Mergelstein: schiefrig  | Kalkstein: kieselig   | – |  Blaisun-Member |  Toarcien     | Toarcien   | Syn-Rift  |
|15204019 |Allgäu-Fm.: Trupchun-Mb. | Kalkstein: siltig  | Kalkstein: kieselig   | Brekzie: kalkig |  Trupchun-Member |  Pliensbachien     | Sinémurien   | Syn-Rift  |
|15204021 |Agnelli-Fm.: Knollenkalk-Fazies | Kalkstein  | Mergelstein   | – |  Agnelli-Formation |  Toarcien     | Sinémurien   | Syn-Rift  |
|15204022 |Agnelli-Fm.: Echinodermenkalk-Fazies | Kalkstein: spätig: Echinodermen  | –   | – |  Agnelli-Formation |  Pliensbachien     | Sinémurien   | Syn-Rift  |
|15204023 |Alv-Brekzie | Brekzie: kalkig-dolomitisch  | –   | – |  Alv-Brekzie |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15204024 |Kössen-Fm. | Tonstein  | Kalkstein: Bioklasten   | – |  Kössen-Formation |  Rhät     | Norien   | «Rhät»  |
|15204025 |Kössen-Fm.: Zirmenkopf-Mb. | Kalkstein: Korallen  | Mergelstein   | – |  Zirmenkopf-Kalk |  Rhät     | Norien   | «Rhät»  |
|15204026 |Kössen-Fm.: Mitgel-Mb. | Kalkstein  | Dolomitstein: kalkig   | Mergelstein: siltig |  Mitgel-Member |  Rhät     | Norien   | «Rhät»  |
|15204027 |Kössen-Fm.: Ramoz-Mb. | Mergelstein  | Kalkstein   | – |  Ramoz-Member |  Rhät     | Norien   | «Rhät»  |
|15204028 |Kössen-Fm.: Schesaplana-Mb. | 15111272  | Kalkstein: Korallen   | – |  Schesaplana-Member |  Rhät     | Norien   | «Rhät»  |
|15204029 |Kössen-Fm.: Alplihorn-Mb. | Tonstein: schiefrig  | Kalkstein: mergelig-schiefrig   | Kalkstein |  Alplihorn-Member |  Rhät     | Norien   | «Rhät»  |
|15204030 |Ostalpin: Hauptdolomit-Gr. | Dolomitstein  | Brekzie   | – |  – |  Norien     | Norien   | Hauptdolomit  |
|15204031 |Murtèr-Plattenkalk | Kalkstein: mikritisch: Bioklasten-Chert  | Kalkstein: mergelig   | Tonstein |  Murtèr-Plattenkalk |  Norien     | Norien   | Hauptdolomit  |
|15204032 |Murteret-Dolomit | Dolomitstein  | –   | – |  Murteret-Dolomit |  Norien     | Norien   | Hauptdolomit  |
|15204033 |Diavel-Fm. | Kalkstein: kieselig  | Mergelstein   | – |  Diavel-Formation |  Norien     | Norien   | Hauptdolomit  |
|15204034 |Quattervals-Fm. | 15111227  | Brekzie   | Kalkstein: Bioklasten |  Quattervals-Formation |  Norien     | Norien   | Hauptdolomit  |
|15204035 |Quattervals-Fm.: Crappa-Mala-Mb. | Mergelstein  | Tonstein   | Kalkstein: tonig |  Crappa-Mala-Mergel |  Norien     | Norien   | Hauptdolomit  |
|15204036 |Quattervals-Fm.: Pra-Grata-Mb. | Kalkstein: spätig: Chert  | Dolomitstein   | Brekzie |  Pra-Grata-Member |  Norien     | Norien   | Hauptdolomit  |
|15204037 |Müschauns-Dolomit | Dolomitstein: spätig  | –   | – |  Müschauns-Dolomit |  Norien     | Norien   | Hauptdolomit  |
|15204038 |Ostalpin: Raibl-Gr. | Evaporit: Gips  | Dolomitstein   | Rauwacke |  – |  Carnien     | Ladinien   | Raibl  |
|15204039 |Fanez-Fm. | Sandstein  | Tonstein: schiefrig   | Dolomitstein: stromatolithisch |  Fanez-Formation |  Carnien     | Carnien   | Raibl  |
|15204040 |Fanez-Fm.: Valbella-Mb. | Brekzie: polymikt  | –   | – |  Valbella-Member |  Carnien     | Carnien   | Raibl  |
|15204041 |Fanez-Fm.: Dolomit | Dolomitstein  | –   | – |  Fanez-Formation |  Carnien     | Carnien   | Raibl  |
|15204042 |Fanez-Fm.: Mezdi-Mb. | Tonstein  | Kalkstein: Bioklasten-Ooide   | – |  Mezdi-Member |  Carnien     | Carnien   | Raibl  |
|15204043 |Fanez-Fm.: Cluozza-Mb. | Sandstein: Feldspat  | Siltstein   | Dolomitstein |  Cluozza-Member |  Carnien     | Carnien   | Raibl  |
|15204044 |Fanez-Fm.: Stugl-Gips | Evaporit: Gips  | –   | – |  Stugl-Gips |  Carnien     | Carnien   | Raibl  |
|15204045 |Minger-Fm. | Dolomitstein  | Rauwacke   | – |  Minger-Formation |  Carnien     | Ladinien   | Raibl  |
|15204046 |Minger-Fm.: Dolomit | Dolomitstein  | –   | – |  Minger-Formation |  Carnien     | Ladinien   | Raibl  |
|15204047 |Mingèr-Fm.: Mora-Mb. | Rauwacke  | Tonstein: schiefrig   | Dolomitstein |  Mora-Member |  Carnien     | Ladinien   | Raibl  |
|15204048 |Garone-Fm. | Rauwacke  | Tonstein   | Dolomitstein |  Garone-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204049 |Arlberg-Fm. | Kalkstein  | Tonstein   | Dolomitstein |  Arlberg-Formation |  Carnien     | Ladinien   | Karbonatische Trias  |
|15204050 |Partnach-Fm. | Mergelstein: schiefrig  | Tonstein: kieselig   | – |  Partnach-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204051 |Altein-Fm. | Dolomitstein  | Kalkstein: Chert   | Tonstein |  Altein-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204052 |Altein-Fm.: Parai-Alba-Mb. | 15111282  | Tonstein   | Tuff: vulkanisch |  Parai-Alba-Member |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204053 |Prosanto-Fm. | Kalkstein: Bitumen  | Dolomitstein   | Tonstein |  Prosanto-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204054 |Vallatscha-Fm. | Dolomitstein: stromatolithisch  | Brekzie: dolomitisch   | – |  Vallatscha-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204055 |Vallatscha-Fm.: Tiaun-Brekzie | Brekzie  | –   | – |  Tiaun-Brekzie |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204056 |Vallatscha-Fm.: Dolomit | Dolomitstein  | –   | – |  Vallatscha-Formation |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204057 |Vallatscha-Fm.: Turettas-Mb. | 15111279  | Dolomitstein: Ooide   | Rauwacke |  Turettas-Member |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204058 |Vallatscha-Fm.: Landwasser-Mb. | Dolomitstein  | –   | – |  Landwasser-Member |  Ladinien     | Ladinien   | Karbonatische Trias  |
|15204059 |S-charl-Fm. | Dolomitstein  | Kalkstein   | – |  S-charl-Formation |  Ladinien     | Anisien   | Karbonatische Trias  |
|15204060 |S-charl-Fm.: Sertig-Mb. | Kalkstein  | Kalkstein: Ooide   | – |  Sertig-Member |  Ladinien     | Anisien   | Karbonatische Trias  |
|15204061 |S-charl-Fm.: Ravais-ch-Mb. | Dolomitstein  | Sandstein   | Rauwacke |  Ravais-ch-Member |  Ladinien     | Anisien   | Karbonatische Trias  |
|15204062 |Reiflingen-Fm. | Kalkstein: mikritisch  | Kalkstein: spätig: Bioklasten   | Tuffit |  Reiflingen-Formation |  Ladinien     | Anisien   | Karbonatische Trias  |
|15204063 |Ducan-Fm. | Dolomitstein  | Dolomitstein: sandig   | Sandstein |  Ducan-Formation |  Anisien     | Anisien   | Karbonatische Trias  |
|15204064 |Ducan-Fm.: Trochitendolomit | 15111293  | –   | – |  «Trochitendolomit-Member» |  Anisien     | Anisien   | Karbonatische Trias  |
|15204065 |Ducan-Fm.: Brachiopodenkalk | Kalkstein: Bioklasten-Chert  | Kalkstein: siltig-tonig   | – |  «Brachiopodenkalk-Member» |  Anisien     | Anisien   | Karbonatische Trias  |
|15204066 |Ducan-Fm.: Eisendolomit-Mb. | Dolomitstein: Bioklasten  | –   | – |  «Eisendolomit-Member» |  Anisien     | Anisien   | Karbonatische Trias  |
|15204067 |Ducan-Fm.: Gracilis-Mb. | 15111286  | Dolomitstein: stromatolithisch   | – |  «Gracilis-Member» |  Anisien     | Anisien   | Karbonatische Trias  |
|15204068 |Gutenstein-Fm. | Kalkstein  | Dolomitstein: spätig   | – |  Gutenstein-Formation |  Ladinien     | Anisien   | Karbonatische Trias  |
|15204069 |Reichenhall-Fm. | 15111298  | Dolomitstein   | Brekzie: dolomitisch |  Reichenhall-Formation |  Anisien     | Olénékien   | Karbonatische Trias  |
|15204070 |Fuorn-Fm. | Sandstein: Quarz  | Siltstein   | Dolomitstein |  Fuorn-Formation |  Anisien     | Frühe Trias   | Detritische Trias  |
|15204071 |Fuorn-Fm.: Punt-la-Drossa-Mb. | Sandstein: kalkig  | Dolomitstein   | Rauwacke |  Punt-la-Drossa-Member |  Anisien     | Frühe Trias   | Detritische Trias  |
|15204072 |Fuorn-Fm.: Pflanzenquarzit | Sandstein: Quarz  | –   | – |  «Pflanzenquarzit» |  Anisien     | Frühe Trias   | Detritische Trias  |
|15204073 |Fuorn-Fm.: Unterer Teil | Sandstein: kalkig  | Siltstein   | – |  Fuorn-Formation |  Frühe Trias     | Frühe Trias   | Detritische Trias  |
|15204074 |Ruina- und Chazfora-Fm. | Konglomerat  | Sandstein   | Rhyolith |  – |  Frühe Trias     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15204075 |Chazforà-Fm. | Konglomerat  | Sandstein   | Siltstein |  Chazforà-Formation |  Frühe Trias     | Lopingien   | Spät- bis postvariszisches Grundgebirge  |
|15204076 |Chazforà-Fm.: Tuors-Mb. | Sandstein  | Konglomerat: Quarz   | – |  Tuors-Member |  Frühe Trias     | Frühe Trias   | Spät- bis postvariszisches Grundgebirge  |
|15204077 |Chazforà-Fm.: Val-Püra-Mb. | Brekzie  | –   | – |  Val-Püra-Member |  Lopingien     | Lopingien   | Spät- bis postvariszisches Grundgebirge  |
|15206089 |Undifferenzierte lithologische Einheit: Tektonit | Gestein: tektonisch  | –   | – |  – |  Känozoikum     | Proterozoikum   | –  |
|15206090 |Undifferenzierte lithologische Einheit: Hornfels | Hornfels  | –   | – |  – |  Känozoikum     | Proterozoikum   | –  |
|15206091 |Undifferenzierte lithologische Einheit: Hornblendegneis | Gneis: Hornblende  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15206092 |Undifferenzierte lithologische Einheit: Biotit-Plagioklasgneis | Gneis: Biotit-Plagioklas  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15206093 |Undifferenzierte lithologische Einheit: Bändergneis | Gneis: gebändert  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15206094 |Undifferenzierte lithologische Einheit: Zweiglimmergneis | Gneis: Biotit-Muskovit  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15206095 |Undifferenzierte lithologische Einheit: Phyllitgneis | Gneis: phyllitisch  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15206096 |Undifferenzierte lithologische Einheit: Peridotit | Peridotit  | –   | – |  – |  Mesozoikum     | Proterozoikum   | –  |
|15206097 |Undifferenzierte lithologische Einheit: Bänder- und Schollenamphibolit | Amphibolit  | –   | – |  – |  Mesozoikum     | Proterozoikum   | Grundgebirge  |
|15206098 |Undifferenzierte lithologische Einheit: Granatamphibolit | Amphibolit: Granat  | –   | – |  – |  Mesozoikum     | Proterozoikum   | Grundgebirge  |
|15206099 |Undifferenzierte lithologische Einheit: Diabasgang | Basalt  | –   | – |  – |  Mesozoikum     | Proterozoikum   | –  |
|15206100 |Undifferenzierte stratigraphische Einheit: Perm | Sandstein  | Konglomerat   | Gestein: vulkanisch |  – |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15206101 |Undifferenzierte lithologische Einheit: Kalkmarmor | Marmor: kalkig  | –   | – |  – |  Mesozoikum     | Paläozoikum   | –  |
|15206103 |Undifferenzierte stratigraphische Einheit: Permo-Karbon | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Perm     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15206104 |Undifferenzierte lithologische Einheit: Kalkschiefer | Schiefer: kalkig  | –   | – |  – |  Känozoikum     | Paläozoikum   | –  |
|15206105 |Undifferenzierte lithologische Einheit: Sandstein | Sandstein  | –   | – |  – |  Känozoikum     | Paläozoikum   | Sedimentbedeckung  |
|15206106 |Undifferenzierte lithologische Einheit: Tonschiefer | Schiefer: tonig  | –   | – |  – |  Mesozoikum     | Proterozoikum   | –  |
|15206107 |Undifferenzierte lithologische Einheit: Radiolarit | Gestein: kieselig: Radiolarien  | –   | – |  – |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15206108 |Undifferenzierte lithologische Einheit: Kalkstein | Kalkstein  | –   | – |  – |  Känozoikum     | Paläozoikum   | Sedimentbedeckung  |
|15206109 |Undifferenzierte lithologische Einheit: Konglomeratgneis | Gneis: psephitisch  | –   | – |  – |  Mesozoikum     | Proterozoikum   | –  |
|15206110 |Undifferenzierte stratigraphische Einheit: Prävariszisches polyzyklisches Grundgebirge | Gneis  | Schiefer   | Amphibolit |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15206111 |Undifferenzierte lithologische Einheit: Schiefer | Schiefer  | –   | – |  – |  Mesozoikum     | Proterozoikum   | –  |
|15206112 |Undifferenzierte lithologische Einheit: Aplitgneis | Gneis: aplitisch  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15206113 |Undifferenzierte lithologische Einheit: Süsswasserkalk | Kalkstein  | –   | – |  – |  Tertiär     | Tertiär   | Sedimentbedeckung  |
|15206114 |Undifferenzierte stratigraphische Einheit: Tektonisches Melange | Tonstein: schiefrig  | –   | – |  – |  Neogen     | Paläogen   | Mélange  |
|15206115 |Undifferenzierte stratigraphische Einheit: Flysch | Sandstein  | Gestein: pelitisch   | – |  – |  Paläogen     | Späte Kreide   | Flysch  |
|15206116 |Undifferenzierte lithologische Einheit: Aptychenkalk | Kalkstein: mikritisch: Aptychen  | –   | – |  – |  Frühe Kreide     | Später Jura   | Sedimentbedeckung  |
|15206117 |Undifferenzierte lithologische Einheit: Quarzsandstein | Sandstein: Quarz  | –   | – |  – |  Trias     | Trias   | Sedimentbedeckung  |
|15206118 |Undifferenzierte lithologische Einheit: Mergelstein | Mergelstein  | –   | – |  – |  Känozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15206119 |Undifferenzierte lithologische Einheit: Basisches Gestein | Gestein: basisch  | –   | – |  – |  Känozoikum     | Präkambrium   | –  |
|15200001 |Twannbach-Fm. | Kalkstein: mikritisch  | Dolomitstein   | Kalkstein: stromatolithisch |  Twannbach-Formation |  Tithonien     | Kimméridgien   | Malm  |
|15200002 |Reuchenette-Fm. | Kalkstein: mikritisch  | Kalkstein: Bioklasten   | Mergelstein |  Reuchenette-Formation |  Kimméridgien     | Kimméridgien   | Malm  |
|15200003 |Courgenay-Fm. | Kalkstein: mikritisch  | Kalkstein: kreidig   | – |  Courgenay-Formation |  Kimméridgien     | Oxfordien   | Malm  |
|15200004 |Vellerat-Fm. | Kalkstein: mergelig  | Kalkstein: mikritisch   | Mergelstein |  Vellerat-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15200005 |St-Ursanne-Fm. | Kalkstein: Korallen  | Kalkstein: Ooide   | Kalkstein: arenitisch: Bioklasten |  St-Ursanne-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15200006 |Bärschwil-Fm. | Tonstein: mergelig  | Mergelstein   | Kalkstein: Chert |  Bärschwil-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15200007 |Ifenthal-Fm. | Mergelstein  | Kalkstein: Eisenooide   | Mergelstein: Bioklasten |  Ifenthal-Formation |  Callovien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200008 |Hauptrogenstein | Kalkstein: Ooide  | Kalkstein: Bioklasten   | Mergelstein |  Hauptrogenstein |  Bathonien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200009 |Passwang-Fm. | Tonstein  | Mergelstein: Eisenooide   | Kalkstein: sandig: Bioklasten |  Passwang-Formation |  Bathonien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15200010 |Opalinus-Ton | Tonstein  | Mergelstein: siltig   | Siltstein: Glimmer |  Opalinus-Ton |  Aalénien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15200011 |Staffelegg-Fm. | Mergelstein  | Kalkstein   | Sandstein: kalkig |  Staffelegg-Formation |  Toarcien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15200012 |Juragebirge: Malm | Kalkstein  | Mergelstein   | – |  – |  Tithonien     | Oxfordien   | Malm  |
|15200013 |Twannbach-Fm.: Vouglans-Mb. | Kalkstein: mikritisch  | Dolomitstein   | – |  Vouglans-Member |  Tithonien     | Tithonien   | Malm  |
|15200014 |Twannbach-Fm.: Chailley-Mb. | Dolomitstein  | Kalkstein: stromatolithisch   | Kalkstein: Bioklasten |  Chailley-Member |  Tithonien     | Kimméridgien   | Malm  |
|15200015 |Twannbach-Fm.: Oberer Virgula-Mergel | Mergelstein: Bioklasten  | –   | – |  «Oberer Virgula-Mergel» |  Kimméridgien     | Kimméridgien   | Malm  |
|15200016 |Reuchenette-Fm.: Chevenez-Mb.: Grenznerineen-Bk. | Kalkstein: Bioklasten  | –   | – |  «Grenznerineen-Bank» |  Kimméridgien     | Kimméridgien   | Malm  |
|15200017 |Reuchenette-Fm.: Chevenez-Mb.: Cladocoropsis-Kalk | Kalkstein: Bioklasten  | –   | – |  «Cladocoropsis-Kalk» |  Kimméridgien     | Kimméridgien   | Malm  |
|15200018 |Reuchenette-Fm.: Chevenez-Mb.: Unterer Virgula-Mergel | Mergelstein: Bioklasten  | –   | – |  «Unterer Virgula-Mergel» |  Kimméridgien     | Kimméridgien   | Malm  |
|15200019 |Reuchenette-Fm.: Courtedoux-Mb. | Kalkstein: Bioklasten  | –   | – |  Courtedoux-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200020 |Reuchenette-Fm.: Banné-Mb. | Mergelstein: Bioklasten  | Kalkstein: mergelig   | – |  Banné-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200021 |Reuchenette-Fm.: Vabenau-Mb. | Kalkstein: mikritisch  | Kalkstein: mergelig   | – |  Vabenau-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200022 |Reuchenette-Fm.: Vabenau-Mb.: Creugenat-Sch. | Mergelstein: Bioklasten  | Kalkstein: mergelig   | – |  Creugenat-Schichten |  Kimméridgien     | Kimméridgien   | Malm  |
|15200023 |Etiollets-Fm. | Kalkstein: mikritisch  | Kalkstein: Korallen   | Mergelstein |  Etiollets-Formation |  Kimméridgien     | Kimméridgien   | Malm  |
|15200024 |Etiollets-Fm.: Complexe récifal | Kalkstein: Korallen  | Kalkstein: mikritisch   | Kalkstein: arenitisch |  «Complexe récifal» |  Kimméridgien     | Kimméridgien   | Malm  |
|15200025 |Etiollets-Fm.: Couvaloup-Mb. | Mergelstein  | Kalkstein: mikritisch   | – |  Couvaloup-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200026 |Courgenay-Fm.: Porrentruy-Mb. | Kalkstein: kreidig  | Kalkstein: arenitisch   | – |  Porrentruy-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200027 |Courgenay-Fm.: La-May-Mb. | Kalkstein: mikritisch  | –   | – |  La-May-Member |  Kimméridgien     | Oxfordien   | Malm  |
|15200028 |Vellerat-Fm.: Oolithe-Rousse-Mb. | Kalkstein: Ooide  | –   | – |  «Oolithe-Rousse-Member» |  Oxfordien     | Oxfordien   | Malm  |
|15200029 |Vellerat-Fm.: Bure-Mb. | Mergelstein: kalkig  | –   | – |  Bure-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200030 |Vellerat-Fm.: Hauptmumienbank-Mb. | Kalkstein: mikritisch: Onkoide  | –   | – |  «Hauptmumienbank-Member» |  Oxfordien     | Oxfordien   | Malm  |
|15200031 |Vellerat-Fm.: Röschenz-Mb. | Kalkstein: mergelig: Bioklasten  | Kalkstein: Bioklasten   | – |  Röschenz-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200032 |Vellerat-Fm.: Vorbourg-Mb. | Kalkstein: mikritisch  | –   | – |  Vorbourg-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200033 |St-Ursanne-Fm.: Tiergarten-Mb. | Kalkstein: Ooide  | Kalkstein: Korallen   | – |  Tiergarten-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200034 |St-Ursanne-Fm.: Buix-Mb. | Kalkstein: kreidig: Chert  | Kalkstein: Korallen   | – |  Buix-Member |  Oxfordien     | Oxfordien   | Malm  |
|15202509 |Euthal-Fm.: Guschakopf-Sandstein | Sandstein: Quarz  | –   | – |  Guschakopf-Sandstein |  Paläogen     | Paläogen   | «Nummulitikum»  |
|15202506 |Bifertengrätli-Fm.: Sandalp-Rhyolith | Rhyolith  | –   | – |  Sandalp-Rhyolith |  Asselien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202507 |Tscharren-Fm.: Tuffitische Fazies | Tuffit  | –   | – |  Tscharren-Formation |  Spätes Pennsylvanien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202508 |Tscharren-Fm.: Ignimbritische Fazies | Ignimbrit  | –   | – |  Tscharren-Formation |  Spätes Pennsylvanien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202510 |Quinten-Fm.: Gonzen-Eisenerzhorizont | Kalkstein: Eisenooide  | –   | – |  Gonzen-Eisenerzhorizont |  Kimméridgien     | Oxfordien   | Malm  |
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
|15202526 |Telltistock-Granit | Granit: Biotit  | Granit: mylonitisch   | – |  Telltistock-Granit |  Spätes Pennsylvanien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202527 |Öhrli-Fm.: von Siderolithikum durchsetzt | Kalkstein  | Gestein: residual: Eisenmineralien   | – |  Öhrli-Formation |  Eozän     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202528 |Zentraler-Aare-Granit: Beesten-Varietät | Granit: porphyrisch  | –   | – |  Beesten-Granit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202529 |Diechtergletscher-Fm.: Garwiidi-Diorit | Diorit: Quarz-Hornblende  | –   | – |  Garwiidi-Diorit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202530 |Alp-Crap-Ner-Granit | Granit  | –   | – |  Alp-Crap-Ner-Granit |  Mittleres Mississippien     | Mittleres Mississippien   | Frühvariszisches Grundgebirge  |
|15202531 |Innertkirchen-Migmatit: Permisch verwittert | Gestein: residual  | Migmatit   | Gneis |  Innertkirchen-Migmatit |  Perm     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202532 |Erstfeld-Gneiskomplex: Permisch verwittert | Gestein: residual  | Gneis   | – |  Erstfeld-Gneiskomplex |  Perm     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202533 |Martinsmad-Fm.: Supraquarzitischer Flysch: Suren-Flysch | Sandstein: tonig  | Tonstein: schiefrig   | – |  Suren-Flysch |  Mittleres Eozän     | Yprésien   | Flysch  |
|15202534 |Stad-Fm.: Spirstock-Mb.: Obere Sandsteine | Sandstein: kalkig: Quarz  | Konglomerat: polymikt   | – |  Spirstock-Member |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202535 |Stad-Fm.: Spirstock-Mb.: Blockmergel | Mergelstein: konglomeratisch  | –   | – |  Spirstock-Member |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202536 |Stad-Fm.: Spirstock-Mb.: Untere Sandsteine | Sandstein: Feldspat  | Mergelstein: schiefrig   | – |  Spirstock-Member |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202537 |Helvetischer Kieselkalk: Ringgenberg-Sch. | Kalkstein: mikritisch  | Mergelstein: schiefrig   | – |  Ringgenberg-Schichten |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202538 |Quinten-Fm.: Brekziöse Fazies | Brekzie: kalkig  | Brekzie: dolomitisch   | – |  Quinten-Formation |  Tithonien     | Kimméridgien   | Malm  |
|15202539 |Schattwald-Mergelkalk | Kalkstein: mergelig  | Kalkstein: mikritisch   | – |  Schattwald-Mergelkalk |  Frühe Kreide     | Tithonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202540 |Elm- und Matt-Fm. | Sandstein: Quarz  | Sandstein: tonig   | Tonstein |  – |  Rupélien     | Priabonien   | Flysch  |
|15202541 |Elm- und Matt-Fm.: Quarzsandstein | Sandstein: Quarz  | –   | – |  – |  Rupélien     | Priabonien   | Flysch  |
|15202542 |Nordhelvetische Flysch-Gr.: Schiefriger Tonstein | Tonstein: schiefrig  | –   | – |  – |  Rupélien     | Priabonien   | Flysch  |
|15202543 |Tierwis-Fm.: Schiefrige Fazies | Mergelstein: schiefrig  | –   | – |  Tierwis-Formation |  Barrémien     | Barrémien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202544 |Tierwis-Fm.: Kalkige Fazies | Mergelstein: kalkig-kieselig  | Kalkstein: spätig: Bioklasten   | Kalkstein: sandig |  Tierwis-Formation |  Barrémien     | Barrémien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202545 |Bommerstein-Fm.: Glockhaus-Mb.: Schiefriger Eisensandstein | Sandstein: Eisenmineralien  | –   | – |  Glockhaus-Member |  Bajocien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15202546 |Helvetikum: Trias: Dolomit | Dolomitstein  | –   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15202547 |Helvetikum: Trias: Rauwacke | Rauwacke  | –   | – |  – |  Trias     | Trias   | Prä-Rift  |
|15202548 |Helvetikum: Trias: Gips | Evaporit: Gips  | –   | – |  – |  Trias     | Trias   | Prä-Rift  |
|15202549 |Baltschieder-Granodiorit: Biotittonalit | Tonalit: Biotit  | –   | – |  Baltschieder-Granodiorit |  Mississippien     | Mississippien   | Prävariszisches Grundgebirge  |
|15202550 |Baltschieder-Granodiorit: Hornblende Biotittonalit | Tonalit: Biotit-Hornblende  | –   | – |  Baltschieder-Granodiorit |  Mississippien     | Mississippien   | Prävariszisches Grundgebirge  |
|15202551 |Erstfeld-Gneiskomplex: Biotit-Plagioklasgneis | Gneis: migmatitisch  | Migmatit   | – |  Erstfeld-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202552 |Erstfeld-Gneiskomplex: Orthogneis | Gneis: granitisch  | –   | – |  Erstfeld-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202553 |Erstfeld-Gneiskomplex: Migmatit | Migmatit  | –   | – |  Erstfeld-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202554 |Guttannen-Gneiskomplex: Paragneis | Gneis: sedimentär  | –   | – |  Guttannen-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202555 |Guttannen-Gneiskomplex: Orthogneis | Gneis: magmatisch  | –   | – |  Guttannen-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202556 |Guttannen-Gneiskomplex: Biotit-Chloritschiefer | Schiefer  | Gneis   | – |  Guttannen-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202557 |Guttannen-Gneiskomplex: Chlorit-Serizitschiefer | Schiefer  | Gneis   | – |  Guttannen-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202558 |Lötschental-Gneiskomplex: Muskovitgneis | Gneis: Muskovit  | –   | – |  Lötschental-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202559 |Lötschental-Gneiskomplex: Migmatitischer Biotitgneis | Gneis: migmatitisch  | –   | – |  Lötschental-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202560 |Lötschental-Gneiskomplex: Chloritschiefer | Schiefer: Chlorit  | –   | – |  Lötschental-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202561 |Ofenhorn-Stampfhorn-Gneiskomplex: Gebänderter Biotitgneis | Gneis: gebändert  | Migmatit   | – |  Ofenhorn-Stampfhorn-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202562 |Ofenhorn-Stampfhorn-Gneiskomplex: Migmatit | Migmatit  | Gneis   | – |  Ofenhorn-Stampfhorn-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202563 |Ofenhorn-Stampfhorn-Gneiskomplex: Biotitgneis | Gneis: Biotit  | –   | – |  Ofenhorn-Stampfhorn-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202564 |Ofenhorn-Stampfhorn-Gneiskomplex: Orthogneis | Gneis: magmatisch  | –   | – |  Ofenhorn-Stampfhorn-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202565 |Bäregg-Gneiskomplex: Mylonitischer Orthogneis | Gneis: mylonitisch  | –   | – |  Bäregg-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202566 |Bäregg-Gneiskomplex: Mylonitischer Paragneis | Gneis: mylonitisch  | –   | – |  Bäregg-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202567 |Bäregg-Gneiskomplex: Metavulkanite | Gestein: vulkanisch  | –   | – |  Bäregg-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202568 |Grimsel-Granodiorit: Aplitische Randfazies | Granit: aplitisch  | –   | – |  Grimsel-Granodiorit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15204081 |Ruina-Fm.: Bellaluna-Mb. | Rhyolith  | Dazit: rhyolithisch   | – |  Bellaluna-Member |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15204078 |Präbichl-Fm. | Konglomerat: polymikt  | Sandstein: tonig: Lithoklasten   | Tonstein: schiefrig |  Präbichl-Formation |  Frühe Trias     | Perm   | Grundgebirge  |
|15204079 |Ruina-Fm. | Rhyolith  | Dazit: rhyolithisch   | Tuff: vulkanisch |  Ruina-Formation |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15204080 |Ruina-Fm.: Sandhubel-Mb. | Ignimbrit  | Tuff: vulkanisch   | – |  Sandhubel-Member |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15204082 |Mönchalp-Augengneis | 15111535  | –   | – |  Mönchalp-Augengneis |  Kambrium     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15204083 |Tschuggen-Augengneis | Gneis: augig  | –   | – |  Tschuggen-Augengneis |  Ordovizium     | Ordovizium   | Prävariszisches Grundgebirge  |
|15204084 |Güstizia-Gneis | Gneis: Muskovit  | –   | – |  Güstizia-Gneis |  Ordovizium     | Ordovizium   | Prävariszisches Grundgebirge  |
|15204085 |Plasseggen-Augengneis | Gneis: augig  | Granit   | Diorit: Quarz |  Plasseggen-Augengneis |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15204086 |Ostalpin: Trias | Dolomitstein  | Rauwacke   | Gestein: pelitisch |  – |  Trias     | Trias   | Prä-Rift  |
|15204087 |Ostalpin: Dogger | Brekzie: polymikt  | Sandstein   | Tonstein |  – |  Mittlerer Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15204088 |Ostalpin: Radiolarit-Aptychenkalk | Gestein: kieselig: Radiolarien  | Kalkstein: mikritisch: Aptychen   | – |  – |  Später Jura     | Mittlerer Jura   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15204089 |Ostalpin: Kreide | Kalkstein  | Gestein: pelitisch   | Brekzie |  – |  Kreide     | Kreide   | Sedimentbedeckung  |
|15204090 |Ostalpin: Lias | Kalkstein  | Sandstein   | Mergelstein |  – |  Perm     | Karbon   | Syn-Rift  |
|15204091 |Ostalpin: Grundgebirge | Gneis  | Schiefer   | Amphibolit |  – |  Perm     | Proterozoikum   | Grundgebirge  |
|15204092 |Nair-Porphyroid | Rhyolith  | Dazit: rhyolithisch   | – |  Nair-Porphyroid |  Karbon     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15204093 |Nair-Porphyroid: Lavatèra-Brekzie | 15111021  | –   | – |  Lavatèra-Brekzie |  Mesozoikum     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15204094 |Varaina-Schiefer | Andesit  | Schiefer: Chlorit   | – |  Varaina-Schiefer |  Karbon     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15204095 |Sprenkel-Schiefer | Dazit: rhyolithisch  | Tuffit   | – |  «Sprenkelschiefer» |  Karbon     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15204096 |Fedoz-Gneiskomplex | 15111525  | Schiefer   | Marmor: kalkig |  Fedoz-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15204097 |Fedoz-Metagabbro | Gabbro  | Schiefer: Chlorit   | – |  Fedoz-Metagabbro |  Guadalupien     | Guadalupien   | Grundgebirge  |
|15204098 |Maloja-Orthogneis | Gneis: magmatisch  | –   | – |  Maloja-Orthogneis |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15204099 |Maloja-Gneiskomplex | Schiefer: Glimmer-Chloritoid  | Schiefer: Glimmer-Granat   | Gneis: Amphibol |  Maloja-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15204100 |Ur-Brekzie | Brekzie: tektonisch  | Serpentinit: brekziös: Karbonat   | – |  Ur-Brekzie |  Mesozoikum     | Paläozoikum   | Ophiolithische Abfolge  |
|15204101 |Tschima-da-Flix-Granit | Granit: porphyrisch  | –   | – |  Tschima-da-Flix-Granit |  Karbon     | Karbon   | Variszisches Grundgebirge  |
|15204102 |Err-Granodiorit | Granodiorit  | –   | – |  Err-Granodiorit |  Perm     | Karbon   | Grundgebirge  |
|15204103 |Ostalpin: Postvariszische Diabasgänge | 15111445  | –   | – |  – |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15204104 |Flüela-Augengneis | Gneis: augig  | Granit: porphyrisch   | – |  Flüela-Augengneis |  Ordovizium     | Ordovizium   | Prävariszisches Grundgebirge  |
|15204105 |Dorfberg-Gneis | Gneis  | –   | – |  Dorfberg-Gneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15204106 |Allgäu-Fm.: Alpisella-Mb.: Chaschauna-Brekzie | Brekzie: kalkig: Bioklasten  | –   | – |  Chaschauna-Brekzie |  Früher Jura     | Früher Jura   | Syn-Rift  |
|15204107 |Sesvenna-Augengneis | Gneis: granitisch-augig  | –   | – |  Sesvenna-Augengneis |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15204108 |Vaüglia-Granodiorit | Granodiorit  | –   | – |  Vaüglia-Granodiorit |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15204109 |Mingèr-Fm.: Mora-Mb.: Döss-Radond-Vulkanite | 15111445  | Tuff: vulkanisch   | – |  Döss-Radond-Vulkanite |  Carnien     | Ladinien   | Raibl  |
|15204110 |Augsten-Brekzie | Brekzie: polymikt  | Tonstein   | – |  Augsten-Brekzie |  Späte Kreide     | Späte Kreide   | Sedimentbedeckung  |
|15204111 |Piz-Trovat-Metarhyolith | Rhyolith  | –   | – |  Piz-Trovat-Metarhyolit |  Sakmarien     | Sakmarien   | Spät- bis postvariszisches Grundgebirge  |
|15204112 |Sass-Queder-Metarhyolith | Rhyolith  | –   | – |  Sass-Queder-Metarhyolith |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15204113 |La-Rösa-Orthogneis | Gneis: magmatisch  | –   | – |  La-Rösa-Orthogneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15204114 |Carale-Schiefer | 15111580  | Schiefer: Quarz-Glimmer   | Gneis |  Carale-Schiefer |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15204115 |Gosau-Gruppe | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Eozän     | Späte Kreide   | Post-Kollision  |
|15204116 |Morteratsch-Serpentinit | Serpentinit  | –   | – |  Morteratsch-Serpentinit |  Karbon     | Karbon   | Grundgebirge  |
|15204117 |Forun-Augengneis | Gneis: augig  | –   | – |  Forun-Augengneis |  Spätes Ordovizium     | Spätes Ordovizium   | Prävariszisches Grundgebirge  |
|15204118 |Kesch-Augengneis | Gneis: augig  | Gneis: gebändert   | – |  Kesch-Augengneis |  Ordovizium     | Ordovizium   | Prävariszisches Grundgebirge  |
|15204119 |Ostalpin: Prävariszisches polyzyklisches Grundgebirge | Gneis  | Schiefer   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15204120 |Silvretta-Decke: «Jüngere Orthogneise» | Gneis: magmatisch  | –   | – |  – |  Spätes Ordovizium     | Spätes Ordovizium   | Prävariszisches Grundgebirge  |
|15204121 |Silvretta-Decke: «Ältere Orthogneise» | Gneis: magmatisch  | –   | – |  – |  Kambrium     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15204122 |Val-Rude-Orthogneis | Gneis: augig  | –   | – |  Val-Rude-Orthogneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15204123 |Corvatsch-Granitkomplex: Corvatsch-Granodiorit | Granodiorit  | –   | – |  Corvatsch-Granodiorit |  Karbon     | Karbon   | Grundgebirge  |
|15204124 |Julier-Granodiorit | Granodiorit  | –   | – |  Julier-Granodiorit |  Karbon     | Karbon   | Grundgebirge  |
|15204125 |Sasso-Rosso-Granodiorit | Granodiorit  | –   | – |  Sasso-Rosso-Granodiorit |  Karbon     | Karbon   | Grundgebirge  |
|15204126 |Vallatscha-Fm.: Lavinèr-Brekzie | Brekzie: dolomitisch  | –   | – |  Lavinèr-Brekzie |  Trias     | Trias   | Karbonatische Trias  |
|15204127 |Haupter-Brekzie | Brekzie: polymikt  | –   | – |  Haupter-Brekzie |  Mittlerer Jura     | Früher Jura   | Syn-Rift  |
|15204130 |Garone-, Vallatscha-,Prosanto- und Altein-Fm. | Dolomitstein  | Kalkstein   | Mergelstein |  – |  Ladinien     | Anisien   | Karbonatische Trias  |
|15204132 |Ostalpin: Variszische Intrusiva | Granit  | Granodiorit   | Gabbro |  – |  Perm     | Karbon   | Variszisches Grundgebirge  |
|15204135 |Ostalpin: Prävariszischer Orthogneis | Gneis: magmatisch  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15204136 |Ostalpin: Prävariszischer Paragneis | Gneis: sedimentär  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15204137 |Ostalpin: Prävariszische Grüngesteine | Prasinit  | Serpentinit   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15204138 |Uglix-Plattenkalk | Kalkstein: dolomitisch  | Tuffit   | – |  Uglix-Plattenkalk |  Norien     | Norien   | Hauptdolomit  |
|15204139 |Parait-Chavagl-Granit | Granit  | –   | – |  Parait-Chavagl-Granit |  Perm     | Pennsylvanien   | Variszisches Grundgebirge  |
|15204140 |God-Drosa-Flysch: Clavadatsch-Brekzie | Brekzie  | –   | – |  Clavadatsch-Brekzie |  Cénomanien     | Cénomanien   | Flysch  |
|15204141 |Corno-di-Campo-Granodiorit | Granodiorit  | Syenit   | Gabbro |  Corno-di-Campo-Granodiorit |  Perm     | Karbon   | Grundgebirge  |
|15204142 |Campocologno-Gabbro | Gabbro  | Diorit   | – |  Campocologno-Gabbro |  Perm     | Karbon   | Grundgebirge  |
|15200035 |St-Ursanne-Fm.: Chestel-Mb. | Kalkstein: arenitisch: Bioklasten  | Kalkstein: Korallen   | Kalkstein: Ooide |  Chestel-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200036 |St-Ursanne-Fm.: Chestel-Mb.: Caquerelle-Pisolith | Kalkstein: Onkoide  | –   | – |  15251130 |  Oxfordien     | Oxfordien   | Malm  |
|15200037 |St-Ursanne-Fm.: Grellingen-Mb. | Kalkstein: mikritisch  | Kalkstein: Korallen   | – |  Grellingen-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200039 |Pichoux-Fm. | Kalkstein: mikritisch  | Kalkstein: mergelig   | – |  Pichoux-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15200040 |Bärschwil-Fm.: Liesberg-Mb. | Mergelstein  | Kalkstein: Chert   | – |  Liesberg-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200041 |Bärschwil-Fm.: Sornetan-Mb. | Tonstein: mergelig  | Kalkstein   | – |  Sornetan-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200042 |Bärschwil-Fm.: Renggeri-Mb. | Tonstein: mergelig  | Kalkstein   | – |  «Renggeri-Member» |  Oxfordien     | Oxfordien   | Malm  |
|15200043 |Ifenthal-Fm.: Graitery-Mb. | Mergelstein  | Kalkstein: mergelig   | – |  Graitery-Member |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15200044 |Ifenthal-Fm.: Herznach-Mb. | Kalkstein: Eisenooide  | Mergelstein: Eisenooide   | – |  Herznach-Member |  Oxfordien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15200045 |Ifenthal-Fm.: Herznach-Mb.: Schellenbrücke-Bk. | Kalkstein: Eisenooide  | –   | – |  Schellenbrücke-Bank |  Oxfordien     | Oxfordien   | Lias-Dogger in neritischer Fazies  |
|15200046 |Ifenthal-Fm.: Bollement-Mb. | Kalkstein: spätig: Bioklasten  | Kalkstein: arenitisch: Bioklasten-Chert   | – |  Bollement-Member |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15200047 |Ifenthal-Fm.: Ängistein-Mb. | Kalkstein: spätig: Bioklasten  | Kalkstein: arenitisch: Bioklasten   | – |  Ängistein-Member |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15200048 |Ifenthal-Fm.: Ängistein-Mb.: Unter-Erli-Bk. | Kalkstein: Bioklasten  | –   | – |  Unter-Erli-Bank |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15200049 |Ifenthal-Fm.: Bözen-Mb. | Mergelstein  | Kalkstein: mergelig   | – |  Bözen-Member |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15200050 |Ifenthal-Fm.: Saulcy-Mb. | Mergelstein: tonig  | –   | – |  Saulcy-Member |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15200051 |Ifenthal-Fm.: Schelmenloch-Mb. | Mergelstein  | Kalkstein: mergelig   | – |  Schelmenloch-Member |  Callovien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200052 |Ifenthal-Fm.: Schelmenloch-Mb.: Anwil-Bk. | Kalkstein: Eisenooide  | –   | – |  Anwil-Bank |  Callovien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200053 |Ifenthal-Fm.: Châtillon-Mb. | Mergelstein  | Kalkstein: Bioklasten   | – |  Châtillon-Member |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15200054 |Ifenthal-Fm.: St-Brais-Mb. | Kalkstein: Bioklasten-Ooide  | Mergelstein: sandig   | – |  St-Brais-Member |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200055 |Juragebirge: Dogger | Kalkstein  | Mergelstein   | Tonstein |  – |  Oxfordien     | Toarcien   | Syn-Rift  |
|15200056 |Juragebirge: Lias | Mergelstein  | Kalkstein   | Tonstein |  – |  Toarcien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15200057 |Hauptrogenstein: Spatkalk | Kalkstein: spätig: Bioklasten  | –   | – |  «Spatkalk» (Hauptrogenstein) |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200058 |Hauptrogenstein: Pierre-Blanche | Kalkstein: mikritisch: Ooide  | –   | – |  «Pierre Blanche» (Hauptrogenstein) |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200059 |Hauptrogenstein: Movelier-Sch. | Mergelstein: Bioklasten  | Mergelstein: kalkig   | – |  Movelier-Schichten |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200060 |Hauptrogenstein: Grande Oolithe | Kalkstein: Ooide  | Kalkstein: spätig: Bioklasten   | – |  15251167 |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200061 |Hauptrogenstein: Obere Acuminata-Sch. | Mergelstein: Bioklasten  | Kalkstein: spätig   | – |  «Obere Acuminata-Schichten» |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200062 |Hauptrogenstein: Oolithe Subcompacte | Kalkstein: Bioklasten-Ooide  | Kalkstein: mikritisch   | – |  «Oolithe Subcompacte» (Hauptrogenstein) |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200063 |Passwang-Fm.: Grenchenberg-Mb. | Kalkstein: siltig: Bioklasten  | Mergelstein   | – |  Grenchenberg-Member |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200064 |Passwang-Fm.: Rothenfluh-Mb. | Mergelstein: sandig: Bioklasten  | Kalkstein: sandig   | – |  Rothenfluh-Member |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200065 |Passwang-Fm.: Brüggli-Mb. | Kalkstein: sandig  | Kalkstein: Bioklasten   | Mergelstein: Eisenooide |  Brüggli-Member |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200066 |Passwang-Fm.: Brüggli-Mb.: Humphriesi-Sch. | Kalkstein: Bioklasten  | Mergelstein: Eisenooide   | – |  «Humphriesi-Schichten» (Brüggli-Mb.) |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200067 |Passwang-Fm.: Waldenburg-Mb. | Tonstein  | Mergelstein   | Mergelstein: Eisenooide |  Waldenburg-Member |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200068 |Passwang-Fm.: Hirnichopf-Mb. | Tonstein  | Kalkstein: sandig   | Mergelstein: Eisenooide |  Hirnichopf-Member |  Bajocien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15200069 |Passwang-Fm.: Hauenstein-Mb. | Tonstein  | Kalkstein: sandig   | – |  Hauenstein-Member |  Aalénien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15200070 |Passwang-Fm.: Sissach-Mb. | Kalkstein: sandig: Glimmer  | Kalkstein: Bioklasten   | Mergelstein: Eisenooide |  Sissach-Member |  Aalénien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15200071 |Staffelegg-Fm.: Gross-Wolf-Mb. | Mergelstein: Bioklasten  | Kalkstein: mergelig   | – |  Gross-Wolf-Member |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15200072 |Staffelegg-Fm.: Gross-Wolf-Mb.: Eriwis-Bk. | Kalkstein: Bioklasten  | –   | – |  Eriwis-Bank |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15200073 |Staffelegg-Fm.: Gross-Wolf-Mb.: Erlimoos-Bk. | Mergelstein: Glaukonit-Bioklasten  | –   | – |  Erlimoos-Bank |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15200074 |Staffelegg-Fm.: Gross-Wolf-Mb.: Gipf-Bk. | Mergelstein: Bioklasten  | Kalkstein: Eisenooide   | – |  Gipf-Bank |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15200075 |Staffelegg-Fm.: Rietheim-Mb. | Mergelstein: tonig: Bitumen  | –   | – |  Rietheim-Member |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15200076 |Staffelegg-Fm.: Rietheim-Mb.: Unterer Stein | Kalkstein: Bitumen  | –   | – |  «Unterer Stein» (Staffelegg-Fm.) |  Toarcien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15200077 |Staffelegg-Fm.: Rickenbach-Mb. | Mergelstein: kalkig: Glaukonit  | –   | – |  Rickenbach-Member |  Toarcien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15200078 |Staffelegg-Fm.: Rickenbach-Mb.: Müsenegg-Bk. | Mergelstein  | Kalkstein: mergelig   | – |  Müsenegg-Bank |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15200079 |Staffelegg-Fm.: Breitenmatt-Mb. | Mergelstein: kalkig: Bioklasten  | Kalkstein   | – |  Breitenmatt-Member |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15200080 |Staffelegg-Fm.: Breitenmatt-Mb.: Trasadingen-Bk. | Mergelstein: kalkig  | –   | – |  Trasadingen-Bank |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15200081 |Staffelegg-Fm.: Grünschholz-Mb. | Mergelstein: kalkig: Glaukonit  | Kalkstein   | – |  Grünschholz-Member |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15200082 |Staffelegg-Fm.: Frick-Mb. | Tonstein  | Siltstein: Glimmer   | – |  Frick-Member |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15200083 |Staffelegg-Fm.: Mont-Terri-Mb. | Mergelstein: Glimmer  | Kalkstein: mergelig   | – |  Mont-Terri-Member |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15200084 |Staffelegg-Fm.: Fasiswald-Mb. | Kalkstein: sandig  | Tonstein: siltig   | – |  Fasiswald-Member |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15200085 |Staffelegg-Fm.: Weissenstein-Mb. | Kalkstein: sandig  | Sandstein: kalkig   | – |  Weissenstein-Member |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15200086 |Staffelegg-Fm.: Beggingen-Mb. | Kalkstein: arenitisch-spätig  | Tonstein   | Siltstein |  Beggingen-Member |  Sinémurien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15200087 |Staffelegg-Fm.: Beggingen-Mb.: Gächlingen-Bk. | Kalkstein: Eisenooide  | Kalkstein: Bioklasten   | – |  Gächlingen-Bank |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15200088 |Staffelegg-Fm.: Beggingen-Mb.: Schleitheim-Bk. | Kalkstein: Eisenooide  | Kalkstein: Bioklasten   | – |  Schleitheim-Bank |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15200089 |Staffelegg-Fm.: Schambelen-Mb. | Tonstein: mergelig: Bitumen  | Tonstein: siltig   | – |  Schambelen-Member |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15200090 |Staffelegg-Fm.: Schambelen-Mb.: Hallau-Bk. | Tonstein: Bitumen  | Kalkstein: sandig: Glaukonit   | – |  Hallau-Bank |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15200091 |Juragebirge: Siderolithikum | Gestein: residual: Eisenmineralien  | –   | – |  – |  Bartonien     | Lutétien   | Siderolithikum  |
|15200092 |Gorges-de-l&#39;Orbe- und Vallorbe-Mb. | Kalkstein: Bioklasten  | Kalkstein: Ooide   | Mergelstein |  – |  Barrémien     | Hauterivien   | «Urgonien»  |
|15200093 |Rocher-des-Hirondelles-Fm.: Vallorbe-Mb. | Kalkstein: Bioklasten  | –   | – |  Vallorbe-Member |  Barrémien     | Hauterivien   | «Urgonien»  |
|15200094 |Rocher-des-Hirondelles-Fm.: Rivière-Mb. | Kalkstein: mergelig  | Mergelstein   | – |  La-Rivière-Member |  Barrémien     | Barrémien   | «Urgonien»  |
|15200096 |Gorges-de-l&#39;Orbe-Fm. | Kalkstein: Ooide  | Kalkstein: Bioklasten   | Mergelstein |  Gorges-de-l&#39;Orbe-Formation |  Hauterivien     | Hauterivien   | «Urgonien»  |
|15200097 |Pierre-Châtel- Vions- und Chambotte-Fm. | Kalkstein: mikritisch  | Kalkstein: Bioklasten-Ooide   | Mergelstein |  – |  Valanginien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200098 |Chambotte-Fm. | Kalkstein: mikritisch: Bioklasten  | –   | – |  Chambotte-Formation |  Valanginien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202572 |Tamina-Gneiskomplex: Mylonit | Gneis: mylonitisch  | –   | – |  Tamina-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202569 |Voralp-Granit: Saure Randfazies | Granit: aplitisch  | –   | – |  Voralp-Granit |  Pennsylvanien     | Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202570 |Tamina-Gneiskomplex | Gneis: migmatitisch  | –   | – |  Tamina-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202571 |Tamina-Gneiskomplex: Schiefriger Biotitgneis | Gneis: schiefrig: Biotit  | –   | – |  Tamina-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202573 |Innertkirchen-Migmatit: Marmor | Marmor  | –   | – |  Innertkirchen-Migmatit |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202574 |Guttannen-Gneiskomplex: Migmatit | Migmatit  | –   | – |  Guttannen-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202575 |Guttannen-Gneiskomplex: Amphibolit-reiche Fazies | Gneis: migmatitisch  | Amphibolit   | – |  Guttannen-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202576 |Guttannen-Gneiskomplex: Aplitischer Granit | Granit: aplitisch  | –   | – |  Guttannen-Gneiskomplex |  Karbon     | Karbon   | Prävariszisches Grundgebirge  |
|15202577 |Guttannen-Gneiskomplex: Marmor | Marmor  | –   | – |  Guttannen-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202578 |Guttannen-Gneiskomplex: Ultramafisches Gestein | Gestein: ultramafisch  | –   | – |  Guttannen-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202579 |Ofenhorn-Stampfhorn-Gneiskomplex: Schollenamphibolit-reiche Fazies | Gneis: migmatitisch  | Amphibolit: migmatitisch   | – |  Ofenhorn-Stampfhorn-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202580 |Ofenhorn-Stampfhorn-Gneiskomplex: Aplitischer Granit | Granit: aplitisch  | –   | – |  Ofenhorn-Stampfhorn-Gneiskomplex |  Karbon     | Karbon   | Prävariszisches Grundgebirge  |
|15202581 |Ofenhorn-Stampfhorn-Gneiskomplex: Schollenamphibolit | Amphibolit: migmatitisch  | –   | – |  Ofenhorn-Stampfhorn-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202582 |Ofenhorn-Stampfhorn-Gneiskomplex: Ultramafisches Gestein | Gestein: ultramafisch  | –   | – |  Ofenhorn-Stampfhorn-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202583 |Bommerstein- und Reischiben-Fm. | Tonstein  | Kalkstein: spätig   | Mergelstein |  – |  Bathonien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15202584 |Mels- und Röti-Fm. | Dolomitstein  | Sandstein   | – |  – |  Carnien     | Frühe Trias   | Prä-Rift  |
|15202585 |Guttannen-Gneiskomplex: Schierfriger Biotit-Chlorit-Serizit-Gneis | Gneis  | Schiefer   | – |  Guttannen-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202586 |Zettenalp-Trochematt-Melange | Mergelstein: schiefrig  | Sandstein   | Brekzie: kalkig: Bioklasten |  Zettenalp-Trochematt-Melange |  Eozän     | Eozän   | Mélange  |
|15202587 |Laubersmad-Flysch | Brekzie: kristallin  | –   | – |  Laubersmad-Flysch |  Priabonien     | Mittleres Eozän   | Flysch  |
|15202588 |Stad-Fm.: Quarzsandstein | Sandstein: Quarz  | –   | – |  Stad-Formation |  Priabonien     | Mittleres Eozän   | «Nummulitikum»  |
|15202589 |Euthal-Fm.: Einsiedeln-Mb.: Quarzsandstein | Sandstein: Quarz  | –   | – |  Einsiedeln-Member |  Mittleres Eozän     | Yprésien   | «Nummulitikum»  |
|15202590 |Schrattenkalk-Fm.: vermergelt | Kalkstein: mergelig  | Mergelstein   | – |  Schrattenkalk-Formation |  Aptien     | Aptien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202591 |Stad-Fm.: Wängen-Kalk: Lithothamnienkalk-Fazies | Kalkstein: Bioklasten  | –   | – |  Wängen-Kalk |  Priabonien     | Mittleres Eozän   | «Nummulitikum»  |
|15202592 |Euthal-Fm.: Einsiedeln-Mb.: Alveolinenkalk-Fazies | Kalkstein: Nummuliten  | –   | – |  Einsiedeln-Member |  Mittleres Eozän     | Yprésien   | «Nummulitikum»  |
|15202593 |Niederhorn-Fm.: Hohgant-Sandstein: Sandkalk und Kalk | Kalkstein: sandig  | Kalkstein   | – |  Hohgant-Sandstein |  Priabonien     | Bartonien   | «Nummulitikum»  |
|15202594 |Interne Einsiedeln-Schuppen: Tektonisches Melange | Mergelstein  | –   | – |  – |  Eozän     | Eozän   | Mélange  |
|15202595 |Bürgen- und Wildstrubel-Fm. | Kalkstein  | Sandstein   | Mergelstein |  – |  Priabonien     | Lutétien   | «Nummulitikum»  |
|15202596 |Einsiedeln- und Steinbach-Mb. | Kalkstein: Nummuliten  | Sandstein: Glaukonit   | – |  – |  Yprésien     | Thanétien   | «Nummulitikum»  |
|15202597 |Stad-Fm.: e6 | Tonstein  | –   | – |  Stad-Formation |  Priabonien     | Priabonien   | «Nummulitikum»  |
|15202598 |Stgir- und Inferno-Fm. | Schiefer: tonig  | Schiefer: kalkig   | Quarzit |  – |  Früher Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15202599 |Quinten-Fm.: Oberer Quintner Kalk: Korallenkalk | Kalkstein: Korallen  | –   | – |  «Oberer Quintner Kalk» |  Tithonien     | Tithonien   | Malm  |
|15202600 |Quinten-Fm.: Oberer Quintner Kalk: Unterer Kalk | Kalkstein: mikritisch  | –   | – |  «Oberer Quintner Kalk» |  Tithonien     | Tithonien   | Malm  |
|15202601 |Prodkamm- bis Sexmor-Fm. | Gestein: pelitisch  | Kalkstein   | Sandstein |  – |  Früher Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15202602 |Plattenzüg-Fm. | Schiefer: Chlorit  | Phyllit   | Dazit |  Plattenzüg-Formation |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15202603 |Zemenstein- bis Garschella Fm. | Kalkstein  | Mergelstein   | Sandstein |  – |  Frühe Kreide     | Frühe Kreide   | Post-Rift  |
|15202604 |Euthal-Fm.: Vasanachopf-Mb | Tonstein: schiefrig  | Konglomerat   | Sandstein: Quarz |  Vasanachopf-Member |  Paleozän     | Paleozän   | «Nummulitikum»  |
|15202605 |Pfäfers-Fm. | Mergelstein  | Kalkstein: kieselig   | Sandstein: Glimmer |  Pfäfers-Formation |  Eozän     | Maastrichtien   | Flysch  |
|15202606 |Euthal- und Bürgen-Fm. | Kalkstein  | Sandstein   | – |  – |  Lutétien     | Sélandien   | «Nummulitikum»  |
|15202607 |Amden- und Wang-Fm. | Mergelstein  | Kalkstein: sandig   | – |  – |  Maastrichtien     | Santonien   | Post-Rift  |
|15202608 |Seewen- und Amden-Fm. | Mergelstein  | Kalkstein: mikritisch   | – |  – |  Campanien     | Cénomanien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202609 |Betlis- bis Schrattenkalk-Fm. | Kalkstein  | Mergelstein   | – |  – |  Albien     | Valanginien   | Post-Rift  |
|15202610 |Öhrli- bis Schrattenkalk-Fm. | Kalkstein  | Mergelstein   | – |  – |  Frühe Kreide     | Frühe Kreide   | Post-Rift  |
|15202611 |Bommerstein-Fm.: Basisbildungen | Brekzie  | Sandstein   | Kalkstein: spätig |  Bommerstein-Formation |  Aalénien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15202612 |Öhrli- und Betlis-Fm. | Kalkstein: Bioklasten  | Mergelstein   | – |  – |  Valanginien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202613 |Erzegg-Fm.: Grenzschicht | Kalkstein: mikritisch: Bioklasten  | Kalkstein: spätig: Glaukonit   | – |  «Grenzschicht» (Erzegg-Fm.) |  Callovien     | Bajocien   | Lias-Dogger in pelagischer Fazies  |
|15202614 |Spitzmeilen-Fm.: Bränd-Brekzie | Brekzie: dolomitisch  | –   | – |  Bränd-Brekzie |  Früher Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15202615 |Infralias-Sandstein | Sandstein: Quarz  | Mergelstein: sandig: Bioklasten   | Tonstein: schiefrig |  «Infralias-Sandstein» |  Hettangien     | Rhät   | «Rhät»  |
|15202616 |Nufenen-Zone: Phyllitische Trias | Phyllit  | Schiefer   | – |  – |  Trias     | Trias   | Pelitische Trias  |
|15202617 |Nufenen-Zone: Karbonatische Trias | Marmor: kalkig  | Rauwacke   | Dolomitstein |  – |  Trias     | Trias   | Karbonatische Trias  |
|15202618 |Nufenen-Zone: Karbonatische Trias: Kalkmarmor | Marmor: kalkig  | –   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15202619 |Nufenen-Zone: Karbonatische Trias: Dolomit | Dolomitstein  | –   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15202620 |Nufenen-Zone: Karbonatische Trias: Rauwacke | Rauwacke  | –   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15202621 |Nufenen-Zone: Quarzitische Trias | Quarzit  | –   | – |  – |  Trias     | Trias   | Detritische Trias  |
|15202622 |Urseren-Garvera-Zone: Malm | Schiefer: tonig  | –   | – |  – |  Später Jura     | Später Jura   | Malm  |
|15202623 |Urseren-Garvera-Zone: Dogger | Schiefer: tonig  | –   | – |  – |  Mittlerer Jura     | Mittlerer Jura   | Lias-Dogger in neritischer Fazies  |
|15202624 |Urseren-Garvera-Zone: Lias | Schiefer: tonig  | –   | – |  – |  Früher Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15202625 |Urseren-Garvera-Zone: Oberer Lias | Schiefer: kalkig  | –   | – |  – |  Früher Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15202626 |Urseren-Garvera-Zone: Mittlerer Lias | Schiefer: kalkig: Zoisit  | –   | – |  – |  Früher Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15202627 |Urseren-Garvera-Zone: Unterer Lias | Sandstein: Quarz  | –   | – |  – |  Früher Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15202628 |Urseren-Garvera-Zone: Phyllitische Trias | Phyllit  | Schiefer   | – |  – |  Trias     | Trias   | Pelitische Trias  |
|15202629 |Urseren-Garvera-Zone: Karbonatische Trias | Marmor: kalkig  | Rauwacke   | Dolomitstein |  – |  Trias     | Trias   | Karbonatische Trias  |
|15202630 |Urseren-Garvera-Zone: Permo-Karbon: Psephit- und Psammitgneis | Gneis: psammitisch  | Gneis: psephitisch   | – |  – |  Perm     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15202631 |Urseren-Garvera-Zone: Permo-Karbon: Metarhyolith | Rhyolith  | –   | – |  – |  Perm     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15202632 |Urseren-Garvera-Zone: Permo-Karbon: Chloritschiefer | Schiefer: Chlorit  | –   | – |  – |  Perm     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15204143 |Celerina-Orthogneis | Gneis: magmatisch  | –   | – |  Celerina-Orthogneis |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15204144 |Tonale-Schiefer | Schiefer: Glimmer-Granat  | Gneis: Granat   | – |  Tonale-Schiefer |  Paläozoikum     | Proterozoikum   | Sedimentbedeckung  |
|15204145 |Ostalpin: Raibl-Gr.: Gips | Evaporit: Gips  | –   | – |  – |  Carnien     | Ladinien   | Raibl  |
|15204146 |Ostalpin: Raibl-Gr.: Rauwacke | Rauwacke  | –   | – |  – |  Carnien     | Ladinien   | Raibl  |
|15204147 |Arlberg-Fm.: Rifffazies | Kalkstein: Korallen  | –   | – |  Arlberg-Formation |  Carnien     | Ladinien   | Karbonatische Trias  |
|15204148 |Ducan- und S-charl-Fm. | Kalkstein  | Dolomitstein   | – |  – |  Anisien     | Anisien   | Karbonatische Trias  |
|15204149 |Ostalpin: Raibl-Gr.: Dolomit | Dolomitstein  | –   | – |  – |  Carnien     | Carnien   | Raibl  |
|15204150 |Ostalpin: Hauptdolomit-Gr.: bituminöser Dolomit | 15111279  | –   | – |  – |  Norien     | Norien   | Hauptdolomit  |
|15204151 |Zentralschweizerische Klippen: Raibl-Gr. | Rauwacke  | Dolomitstein   | Rauwacke |  – |  Carnien     | Carnien   | Raibl  |
|15200099 |Chambotte-Fm.: Guiers-Mb. | Mergelstein: Bioklasten  | Kalkstein: mergelig   | – |  Guiers-Member |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200100 |Vions-Fm. | Kalkstein: arenitisch: Quarz  | Mergelstein   | – |  Vions-Formation |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200101 |Pierre-Châtel-Fm. | Kalkstein: mikritisch  | Kalkstein: Bioklasten-Ooide   | Mergelstein |  Pierre-Châtel-Formation |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200102 |Burghorn-Fm. | Kalkstein: mikritisch  | Mergelstein   | – |  Burghorn-Formation |  Kimméridgien     | Kimméridgien   | Malm  |
|15200103 |Burghorn-Fm.: Wettingen-Mb. | Kalkstein: mikritisch  | Kalkstein: Chert   | – |  Wettingen-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200104 |Burghorn-Fm.: Baden-Mb. | Kalkstein: mikritisch: Glaukonit  | Mergelstein   | – |  Baden-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200105 |Villigen-Fm. | Kalkstein: mikritisch  | Mergelstein   | – |  Villigen-Formation |  Kimméridgien     | Oxfordien   | Malm  |
|15200106 |Villigen-Fm.: Wangental-Mb. | Kalkstein: mikritisch  | Mergelstein   | – |  Wangental-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200107 |Villigen-Fm.: Letzi-Mb. | Kalkstein: mikritisch  | –   | – |  Letzi-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200108 |Villigen-Fm.: Knollen-Bk. | Kalkstein: mergelig: Glaukonit  | –   | – |  «Knollen-Bank» |  Kimméridgien     | Oxfordien   | Malm  |
|15200109 |Villigen-Fm.: Küssaburg-Mb. | Kalkstein: spätig: Bioklasten  | Kalkstein: mikritisch   | – |  Küssaburg-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200110 |Villigen-Fm.: Wangen-Mb. | Kalkstein: mikritisch  | Kalkstein: kreidig   | – |  Wangen-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200111 |Villigen-Fm.: Hornbuck-Mb. | Kalkstein: mergelig: Chert  | Mergelstein   | – |  Hornbuck-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200112 |Villigen-Fm.: Crenularis-Mb. | Kalkstein: Glaukonit-Bioklasten  | –   | – |  «Crenularis-Member» |  Oxfordien     | Oxfordien   | Malm  |
|15200113 |Villigen-Fm.: Geissberg-Mb. | Kalkstein: mikritisch  | Mergelstein   | – |  Geissberg-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200114 |Wildegg-Fm. | Mergelstein  | Kalkstein: mergelig   | Kalkstein: mikritisch |  Wildegg-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15200115 |Wildegg-Fm.: Effingen-Mb. | Mergelstein  | Mergelstein: kalkig   | – |  Effingen-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200116 |Wildegg-Fm.: Effingen-Mb.: Gerstenhübel-Bk. | Kalkstein: mikritisch  | Kalkstein: mergelig   | – |  Gerstenhübel-Bank |  Oxfordien     | Oxfordien   | Malm  |
|15200117 |Wildegg-Fm.: Birmenstorf-Mb. | Kalkstein: mikritisch: Glaukonit  | Kalkstein: mergelig   | – |  Birmenstorf-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200118 |Günsberg-Fm. | Kalkstein: Korallen  | Kalkstein: Ooide   | Mergelstein |  Günsberg-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15200119 |Günsberg-Fm.: Moutier-Korallenkalk | Kalkstein: Korallen  | Mergelstein   | – |  Moutier-Korallenkalk |  Oxfordien     | Oxfordien   | Malm  |
|15200120 |Klingnau-Fm. | Mergelstein  | Kalkstein: Bioklasten   | Kalkstein: Ooide |  Klingnau-Formation |  Bathonien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200121 |Klingnau-Fm.: Knorri-Ton | Tonstein  | Kalkstein: mergelig   | – |  «Knorri-Ton» |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200122 |Klingnau-Fm.: Wuerttembergica-Sch. | Mergelstein  | Kalkstein: Bioklasten   | – |  «Wuerttembergica-Schichten» |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200123 |Klingnau-Fm.: Parkinsoni-Sch.: Subfurcatum-Bk. | Mergelstein: Bioklasten  | –   | – |  «Subfurcatum-Bank» |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200124 |Klingnau-Fm.: Blagdeni-Sch. | Kalkstein: sandig  | Mergelstein   | – |  «Blagdeni-Schichten» (Klingnau-Fm.) |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200125 |Juragebirge: Keuper | Sandstein  | Gestein: pelitisch   | Evaporit |  – |  Rhät     | Ladinien   | Keuper  |
|15200126 |Klettgau-Fm. | Mergelstein  | Sandstein   | Dolomitstein |  Klettgau-Formation |  Rhät     | Carnien   | Keuper  |
|15200127 |Klettgau-Fm.: Belchen-Mb. | Sandstein: Quarz  | Tonstein   | – |  Belchen-Member |  Rhät     | Rhät   | Keuper  |
|15200128 |Bänkerjoch-Fm. | Tonstein  | Evaporit: Sulfat   | Evaporit: Halit |  Bänkerjoch-Formation |  Carnien     | Ladinien   | Keuper  |
|15200129 |Juragebirge: Muschelkalk | Dolomitstein  | Kalkstein   | Evaporit |  – |  Ladinien     | Anisien   | Muschelkalk  |
|15200130 |Schinznach-Fm. | Dolomitstein  | Kalkstein: Bioklasten   | Mergelstein |  Schinznach-Formation |  Ladinien     | Anisien   | Muschelkalk  |
|15200131 |Schinznach-Fm.: Asp-Mb. | Tonstein: siltig  | Mergelstein: dolomitisch   | Dolomitstein |  Asp-Member |  Ladinien     | Ladinien   | Muschelkalk  |
|15200132 |Schinznach-Fm.: Stamberg-Mb. | Dolomitstein  | Dolomitstein: Ooide   | Dolomitstein: Bioklasten |  Stamberg-Member |  Ladinien     | Ladinien   | Muschelkalk  |
|15200133 |Schinznach-Fm.: Liedertswil-Mb. | Kalkstein: mikritisch  | Dolomitstein   | – |  Liedertswil-Member |  Ladinien     | Ladinien   | Muschelkalk  |
|15200134 |Schinznach-Fm.: Kienberg-Mb. | Kalkstein: spätig: Bioklasten  | –   | – |  Kienberg-Member |  Ladinien     | Ladinien   | Muschelkalk  |
|15200135 |Zeglingen-Fm. | Evaporit: Anhydrit  | Mergelstein   | Dolomitstein |  Zeglingen-Formation |  Anisien     | Anisien   | Muschelkalk  |
|15200136 |Zeglingen-Fm.: Obere Sufatzone | Evaporit: Anhydrit  | Mergelstein   | – |  «Obere Sufatzone» (Zeglingen-Fm.) |  Anisien     | Anisien   | Muschelkalk  |
|15200137 |Zeglingen-Fm.: Salzlager | Evaporit: Halit  | –   | – |  «Salzlager» (Zeglingen-Fm.) |  Anisien     | Anisien   | Muschelkalk  |
|15200138 |Zeglingen-Fm.: Untere Sulfatzone | Evaporit: Anhydrit  | Dolomitstein   | Mergelstein |  «Untere Sulfatzone» (Zeglingen-Fm.) |  Anisien     | Anisien   | Muschelkalk  |
|15200139 |Kaiseraugst-Fm. | Dolomitstein  | Kalkstein: mergelig   | Mergelstein: Glimmer |  Kaiseraugst-Formation |  Anisien     | Anisien   | Muschelkalk  |
|15200140 |Kaiseraugst-Fm.: Orbicularis-Mergel | Mergelstein: kalkig: Bitumen  | Evaporit: Anhydrit   | – |  «Orbicularis-Mergel» |  Anisien     | Anisien   | Muschelkalk  |
|15200141 |Kaiseraugst-Fm.: Wellenkalk / Wellenmergel | Kalkstein: mergelig  | Mergelstein   | – |  «Wellenkalk / Wellenmergel» |  Anisien     | Anisien   | Muschelkalk  |
|15200142 |Kaiseraugst-Fm.: Wellendolomit | Dolomitstein  | Kalkstein   | Mergelstein |  «Wellendolomit» |  Anisien     | Anisien   | Muschelkalk  |
|15200143 |Juragebirge: Buntsandstein | Sandstein  | Tonstein   | – |  – |  Anisien     | Olénékien   | Buntsandstein  |
|15200144 |Dinkelberg-Fm. | Sandstein: Glimmer  | Tonstein   | – |  Dinkelberg-Formation |  Anisien     | Olénékien   | Buntsandstein  |
|15200145 |Dinkelberg-Fm.: Rötton | Tonstein: siltig: Glimmer  | –   | – |  «Rhötton» |  Anisien     | Anisien   | Buntsandstein  |
|15200146 |Dinkelberg-Fm.: Plattensandstein | Sandstein: Glimmer  | –   | – |  «Plattensandstein» (Dinkelberg-Fm.) |  Anisien     | Olénékien   | Buntsandstein  |
|15200147 |Dinkelberg-Fm.: Karneolhorizont | Sandstein: kieselig  | –   | – |  «Karneol-Horizont» (Dinkelberg-Fm.) |  Olénékien     | Olénékien   | Buntsandstein  |
|15200148 |Narlay-Fm. | Kalkstein: kreidig: Chert  | Kalkstein: mergelig   | – |  Narlay-Formation |  Coniacien     | Cénomanien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15200149 |Perte-du-Rhône-Fm. | Sandstein: Glaukonit  | Kalkstein: mergelig   | Tonstein |  Perte-du-Rhône-Formation |  Cénomanien     | Aptien   | «Gault»  |
|15200150 |Grand-Essert-Fm. | Kalkstein: spätig: Bioklasten-Glaukonit  | Kalkstein: Ooide   | Mergelstein: Bioklasten |  Grand-Essert-Formation |  Hauterivien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200151 |Grand-Essert-Fm: Neuchâtel-Mb. | Kalkstein: spätig: Bioklasten-Glaukonit  | Kalkstein: Ooide   | – |  Neuchâtel-Member |  Hauterivien     | Hauterivien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200152 |Grand-Essert-Fm: Hauterive-Mb. | Mergelstein: Bioklasten  | Kalkstein: spätig: Bioklasten-Glaukonit   | Mergelstein: kalkig |  Hauterive-Member |  Hauterivien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200153 |Vuache-Fm. | Kalkstein: spätig: Bioklasten-Ooide  | Mergelstein   | – |  Vuache-Formation |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200154 |Vuache-Fm.: Alectryonia-Kalk | Kalkstein: spätig: Bioklasten  | –   | – |  «Alectryonia-Kalk» |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200155 |Vuache-Fm.: Arzier-Mergel | Mergelstein: Bioklasten  | Kalkstein: mergelig   | – |  Arzier-Mergel |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200156 |Goldberg-Fm. | Mergelstein  | Kalkstein   | Brekzie: polymikt |  Goldberg-Formation |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in detritischer Fazies  |
|15200157 |Wiesental-Fm. | Sandstein: Feldspat  | Sandstein: dolomitisch   | – |  Wiesental-Formation |  Lopingien     | Lopingien   | Spät- bis postvariszisches Grundgebirge  |
|15200158 |Weitenau-Fm. | Sandstein: Feldspat  | Konglomerat   | – |  Weitenau-Formation |  Lopingien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15200159 |Weiach-Fm. | Sandstein: Feldspat  | Konglomerat   | Tonstein |  Weiach-Formation |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200160 |Günsberg- Vellerat- Villigen- Balsthal- und Courgenay-Fm. | Kalkstein: mikritisch  | Kalkstein: Ooide   | Mergelstein |  – |  Kimméridgien     | Oxfordien   | Malm  |
|15202636 |Gotthard-Decke: Prävariszischer Paragneis | Gneis: sedimentär  | –   | – |  – |  Paläozoikum     | Präkambrium   | Prävariszisches Grundgebirge  |
|15202633 |Urseren-Garvera-Zone: Permo-Karbon: Graphitschiefer | Schiefer: Graphit  | –   | – |  – |  Perm     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15202634 |Gotthard-Decke: Prävariszischer Orthogneis | Gneis: magmatisch  | –   | – |  – |  Paläozoikum     | Präkambrium   | Prävariszisches Grundgebirge  |
|15202635 |Gotthard-Decke: Prävariszischer Augengneis | Gneis: augig  | –   | – |  – |  Paläozoikum     | Präkambrium   | Prävariszisches Grundgebirge  |
|15202637 |Camosci-Decke: Paragneis | Gneis: sedimentär  | –   | – |  – |  Mittlerer Jura     | Mittlerer Jura   | Sedimentbedeckung  |
|15202638 |Camosci-Decke: Lias-Dogger | Schiefer: Glimmer  | Schiefer: kalkig   | – |  – |  Aalénien     | Toarcien   | Syn-Rift  |
|15202639 |Camosci-Decke: Lias-Dogger: Kalkglimmerschiefer | Schiefer: kalkig: Glimmer  | –   | – |  – |  Aalénien     | Toarcien   | Syn-Rift  |
|15202640 |Camosci-Decke: Lias-Dogger: Granatglimmerschiefer | Schiefer: Glimmer-Granat  | –   | – |  – |  Aalénien     | Toarcien   | Syn-Rift  |
|15202641 |Camosci-Decke: Lias | Marmor  | Quarzit   | – |  – |  Früher Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15202642 |Camosci-Decke: Trias | Marmor: dolomitisch  | Rauwacke   | Schiefer: Glimmer |  – |  Trias     | Trias   | Prä-Rift  |
|15202643 |Camosci-Decke: Sandige Trias | Sandstein  | –   | – |  – |  Trias     | Trias   | Detritische Trias  |
|15202644 |Camosci-Decke: Karbonatische Trias | Dolomitstein  | Rauwacke   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15202645 |Urseren-Garvera-Zone | Marmor  | Schiefer   | Rauwacke |  – |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15202646 |Urseren-Garvera-Zone: Trias | Rauwacke  | Phyllit   | Marmor |  – |  Trias     | Trias   | Prä-Rift  |
|15202647 |Nufenen-Zone: Trias | Rauwacke  | Phyllit   | Quarzit |  – |  Trias     | Trias   | Prä-Rift  |
|15202648 |Nufenen-Zone: Lias | Schiefer: tonig  | Quarzit   | Schiefer: kalkig |  – |  Früher Jura     | Rhät   | Lias-Dogger in neritischer Fazies  |
|15203001 |Niesen-Decke: Flysch | Konglomerat  | Sandstein   | Tonstein: schiefrig |  – |  Lutétien     | Maastrichtien   | Flysch  |
|15203002 |Chesselbach-Fm. | Sandstein  | Tonstein: schiefrig   | – |  Chesselbach-Formation |  Lutétien     | Paleozän   | Flysch  |
|15203003 |Seron-Fm. | Konglomerat: polymikt  | Kalkstein: sandig: Bioklasten   | – |  Seron-Formation |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203004 |Niesenkulm-Fm. | Konglomerat  | Brekzie: kalkig   | Kalkstein: mikritisch |  Niesenkulm-Formation |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203005 |Frutigen-Fm. | Konglomerat  | Sandstein: tonig-kalkig   | Tonstein: schiefrig |  Frutigen-Formation |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203006 |Grande-Eau-Fm. | Tonstein  | Sandstein: kalkig   | Konglomerat: polymikt |  Grande-Eau-Formation |  Bathonien     | Aalénien   | Syn-Rift  |
|15203007 |Grande-Eau-Fm.: Langy-Mb. | Sandstein: kalkig  | Tonstein   | Konglomerat |  Langy-Member |  Bathonien     | Bathonien   | Syn-Rift  |
|15203008 |Grande-Eau-Fm.: Forclaz-Mb. | Sandstein: kalkig  | Mergelstein: Bioklasten   | – |  Forclaz-Member |  Bathonien     | Bathonien   | Syn-Rift  |
|15203009 |Grande-Eau-Fm.: Grès de Passage | Sandstein  | –   | – |  «Grès de Passage» |  Bathonien     | Bathonien   | Syn-Rift  |
|15203010 |Grande-Eau-Fm.: Leyderry-Mb. | Konglomerat: polymikt  | –   | – |  Leyderry-Member |  Bathonien     | Bathonien   | Syn-Rift  |
|15203011 |Grande-Eau-Fm.: Raverette-Mb. | Konglomerat: kalkig  | Mergelstein: Glimmer   | Sandstein: kalkig |  Raverette-Member |  Bajocien     | Bajocien   | Syn-Rift  |
|15203012 |Grande-Eau-Fm.: Schistes à miches | Tonstein: siltig: Glimmer  | –   | – |  «Schistes à Miches» |  Aalénien     | Aalénien   | Syn-Rift  |
|15203013 |Murgaz-Kalk | Kalkstein: kieselig-spätig  | Tonstein: schiefrig   | – |  Murgaz-Kalk |  Sinémurien     | Sinémurien   | Syn-Rift  |
|15203014 |Niesen-Decke: Trias | Sandstein  | Kalkstein: dolomitisch   | Rauwacke |  – |  Trias     | Trias   | Prä-Rift  |
|15203015 |Chlussli-Fm. | Schiefer: Chlorit  | Gneis   | – |  Chlussli-Formation |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203016 |Coulaytes-Melange | Tonstein  | –   | – |  Coulaytes-Melange |  Priabonien     | Mittleres Eozän   | Mélange  |
|15203017 |Cuvigne-Derrey-Fm. | Sandstein  | Mergelstein   | – |  Cuvigne-Derrey-Formation |  Lutétien     | Lutétien   | Flysch  |
|15203018 |Couches-Rouges | Kalkstein: mergelig  | Kalkstein: mikritisch   | Mergelstein |  – |  Maastrichtien     | Cénomanien   | Couches Rouges  |
|15203019 |Chenaux-Rouges-Fm. | Kalkstein: mergelig  | Mergelstein   | – |  Chenaux-Rouges-Formation |  Yprésien     | Sélandien   | Couches Rouges  |
|15203020 |Chenaux-Rouges-Fm.: Hochmatt-Kalkarenit | Kalkstein: arenitisch  | –   | – |  Hochmatt-Kalkarenit |  Yprésien     | Sélandien   | Couches Rouges  |
|15203021 |Chenaux-Rouges-Fm.: Chenaux-Rouges-Mineralkruste | Kalkstein: stromatolithisch: Eisenmineralien-Phosphorit  | Konglomerat   | – |  Chenaux-Rouges-Mineralkruste |  Yprésien     | Paleozän   | Couches Rouges  |
|15203022 |Forclettes-Fm. | Kalkstein: mikritisch  | Mergelstein   | – |  Forclettes-Formation |  Maastrichtien     | Maastrichtien   | Couches Rouges  |
|15203023 |Forclettes-Fm.: Roter-Sattel-Hartgrund | Kalkstein: stromatolithisch: Eisenmineralien-Phosphorit  | –   | – |  Roter-Sattel-Hartgrund |  Sélandien     | Maastrichtien   | Couches Rouges  |
|15203024 |Forclettes-Fm.: Beaumont-Konglomerat | Konglomerat  | –   | – |  Beaumont-Konglomerat |  Maastrichtien     | Maastrichtien   | Couches Rouges  |
|15203025 |Forclettes-Fm.: Rayes-Kalk | Kalkstein: Bioklasten  | –   | – |  Rayes-Kalk |  Maastrichtien     | Maastrichtien   | Couches Rouges  |
|15203026 |Forclettes-Fm.: Pissot-Mb. | Kalkstein  | Tonstein   | – |  Pissot-Member |  Maastrichtien     | Maastrichtien   | Couches Rouges  |
|15203027 |Rote-Platte-Fm. | Kalkstein: mikritisch  | Kalkstein: mergelig   | – |  Rote-Platte-Formation |  Santonien     | Turonien   | Couches Rouges  |
|15203028 |Rote-Platte-Fm.: Wildenbach-Mb. | Kalkstein  | Kalkstein: tonig   | Mergelstein: schiefrig |  Wildenbach-Member |  Santonien     | Santonien   | Couches Rouges  |
|15203029 |Rote-Platte-Fm.: Pra-du-Pont-Hartgrund | Kalkstein: Glaukonit  | –   | – |  Pra-du-Pont-Hartgrund |  Santonien     | Santonien   | Couches Rouges  |
|15203030 |Rote-Platte-Fm.: Rontins-Mb. | Kalkstein  | Kalkstein: tonig   | Tonstein |  Rontins-Member |  Santonien     | Turonien   | Couches Rouges  |
|15203031 |Rote-Platte-Fm.: Allières-Mb. | Kalkstein: tonig  | Mergelstein   | – |  Allières-Member |  Turonien     | Turonien   | Couches Rouges  |
|15203032 |Rote-Platte-Fm.: Gérignoz-Kalk | Kalkstein  | –   | – |  Gérignoz-Kalk |  Turonien     | Turonien   | Couches Rouges  |
|15203033 |Rote-Platte-Fm.: Plagersflue-Kalkarenit | Kalkstein: arenitisch  | –   | – |  Plagersflue-Kalkarenit |  Turonien     | Turonien   | Couches Rouges  |
|15203034 |Intyamon-Fm. | Kalkstein: tonig  | Mergelstein: Bitumen   | – |  Intyamon-Formation |  Turonien     | Aptien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203035 |Intyamon-Fm.: Chällihorn-Mb. | Kalkstein: mikritisch  | Mergelstein   | – |  Chällihorn-Member |  Turonien     | Cénomanien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203036 |Intyamon-Fm.: Comba-d&#39;Avau-Mb. | Mergelstein  | Kalkstein: mergelig: Pyrit   | Kalkstein: kieselig |  Comba-d&#39;Avau-Member |  Albien     | Aptien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203037 |Intyamon-Fm.: Rodosex-Mb. | Kalkstein: stromatolithisch  | Mergelstein: Bioklasten   | Kalkstein: arenitisch: Glaukonit |  Rodosex-Member |  Aptien     | Aptien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203038 |Sciernes-d&#39;Albeuve-Fm. | Kalkstein: mikritisch: Chert  | Mergelstein   | – |  Sciernes-d&#39;Albeuve-Formation |  Barrémien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203039 |Moléson-Fm. | Kalkstein: mikritisch  | Kalkstein: Onkoide   | Kalkstein: Bioklasten |  Moléson-Formation |  Berriasien     | Kimméridgien   | Malm  |
|15203040 |Torrent-de-Lessoc-Fm. | Kalkstein: tonig  | Kalkstein: kieselig   | Mergelstein |  Torrent-de-Lessoc-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15203041 |Staldengraben-Fm. | Kalkstein: mergelig  | Mergelstein: schiefrig   | – |  Staldengraben-Formation |  Callovien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15203042 |Staldengraben-Fm.: Col-de-Lys-Mb. | Kalkstein: sandig-kieselig  | Kalkstein: spätig: Glaukonit   | Mergelstein |  Col-de-Lys-Member |  Callovien     | Callovien   | Lias-Dogger in pelagischer Fazies  |
|15203043 |Staldengraben-Fm.: Vanil-Carré-Mb. | Mergelstein  | Kalkstein: sandig-spätig   | Kalkstein: Ooide |  Vanil-Carré-Member |  Bathonien     | Bajocien   | Lias-Dogger in pelagischer Fazies  |
|15203044 |Staldengraben-Fm.: Verdy-Mb. | Kalkstein: tonig  | Mergelstein: schiefrig   | – |  Verdy-Member |  Bajocien     | Bajocien   | Lias-Dogger in pelagischer Fazies  |
|15203045 |Staldengraben-Fm.: Soladier-Mb. | Mergelstein: schiefrig  | Kalkstein: tonig   | – |  Soladier-Member |  Aalénien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15203046 |Sommant-Fm. | Kalkstein: mikritisch  | Kalkstein: sandig: Bioklasten   | Kalkstein: Ooide |  Sommant-Formation |  Bathonien     | Bajocien   | Syn-Rift  |
|15200175 |Siderolithikum: Bohnerzton | Gestein: residual-tonig: Eisenpisoide  | –   | – |  – |  Rupélien     | Lutétien   | Siderolithikum  |
|15200161 |Juragebirge: Kreide | Kalkstein  | Mergelstein   | Sandstein: kalkig |  – |  Coniacien     | Berriasien   | Post-Rift  |
|15200162 |Juragebirge: Jura | Kalkstein  | Mergelstein   | Tonstein |  – |  Tithonien     | Hettangien   | Sedimentbedeckung  |
|15200163 |Juragebirge: Trias | Dolomitstein  | Mergelstein   | Evaporit |  – |  Rhät     | Olénékien   | Prä-Rift  |
|15200176 |Siderolithikum: Boluston | Gestein: residual-tonig: Limonit  | –   | – |  – |  Priabonien     | Bartonien   | Siderolithikum  |
|15200177 |Siderolithikum: Huppererde | Gestein: residual-sandig: Quarz  | Gestein: residual-tonig: Kaolinit   | – |  – |  Priabonien     | Mittleres Eozän   | Siderolithikum  |
|15200178 |Hauptrogenstein: Homomyenmergel | Mergelstein: Bioklasten  | Kalkstein: spätig   | – |  «Homomya-Mergel» |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200179 |Dinkelberg-Fm.: Vogesen-Sandstein | Sandstein  | –   | – |  Vogesen-Sandstein |  Olénékien     | Olénékien   | Buntsandstein  |
|15200180 |Siderolithikum: Quarzsand | Gestein: residual-sandig: Quarz  | –   | – |  – |  Priabonien     | Mittleres Eozän   | Siderolithikum  |
|15200181 |Perte-du-Rhône-Fm.: Mussel-Mb. | Sandstein: Glaukonit  | –   | – |  Mussel-Member |  Albien     | Aptien   | «Gault»  |
|15200182 |Perte-du-Rhône-Fm.: Fulie-Mb. | Kalkstein: mergelig  | Mergelstein   | – |  Fulie-Member |  Albien     | Aptien   | «Gault»  |
|15200183 |Grand-Essert-Fm: Neuchâtel-Mb.: Uttins-Mergel | Mergelstein: Bioklasten  | Mergelstein: kalkig   | – |  Les-Uttins-Mergel |  Hauterivien     | Hauterivien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200184 |Grand-Essert-Fm: Hauterive-Mb.: Ecluse-Mergelkalk | Mergelstein: Bioklasten  | Kalkstein: spätig: Glaukonit-Chert   | – |  L&#39;Ecluse-Mergelkalk |  Hauterivien     | Hauterivien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200185 |Vuache-Fm.: Bryozoen-Mergel | Mergelstein: Bioklasten  | –   | – |  «Bryozoen-Mergel» |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200186 |Twannbach-Fm.: Zuckerkörniger Kalk | Kalkstein: kristallin  | Dolomitstein   | Rauwacke |  Twannbach-Formation |  Tithonien     | Tithonien   | Malm  |
|15200187 |Reuchenette-Fm.: Chevenez-Mb. | Kalkstein: Bioklasten  | Mergelstein: Bioklasten   | – |  Chevenez-Member |  Kimméridgien     | Kimméridgien   | Malm  |
|15200188 |Balsthal-Fm. | Kalkstein: Ooide  | Kalkstein: Onkoide   | Kalkstein: mikritisch |  Balsthal-Formation |  Kimméridgien     | Oxfordien   | Malm  |
|15200189 |Balsthal-Fm.: Verena-Mb. | Kalkstein: arenitisch: Bioklasten  | Kalkstein: kreidig   | – |  Verena-Member |  Kimméridgien     | Oxfordien   | Malm  |
|15200190 |Balsthal-Fm.: Holzflue-Mb. | Kalkstein: Ooide  | Kalkstein: mikritisch   | – |  Holzflue-Member |  Kimméridgien     | Oxfordien   | Malm  |
|15200191 |Balsthal-Fm.: Laufen-Mb. | Kalkstein: mikritisch  | Kalkstein: Ooide   | Kalkstein: Onkoide |  Laufen-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200192 |Balsthal-Fm.: Olten-Mb. | Kalkstein: mikritisch: Chert  | Kalkstein: Korallen   | – |  Olten-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200193 |Balsthal-Fm.: Steinibach-Mb. | Kalkstein: Ooide  | –   | – |  Steinibach-Member |  Oxfordien     | Oxfordien   | Malm  |
|15200194 |Vellerat-Fm.: Röschenz-Mb.: Grüne Mumienbank | Kalkstein: mikritisch: Onkoide  | –   | – |  «Grüne Mumienbank» |  Oxfordien     | Oxfordien   | Malm  |
|15200195 |Wildegg-Fm.: Effingen-Mb.: Pecten-Bk. | Kalkstein: mergelig: Bioklasten  | Kalkstein: mikritisch   | – |  «Pecten-Bank» |  Oxfordien     | Oxfordien   | Malm  |
|15200196 |Hauptrogenstein: Ferrugineus-Oolith | Mergelstein: Bioklasten-Ooide  | Mergelstein: kalkig   | – |  «Ferrugineus-Oolith» |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200197 |Hauptrogenstein: Wittnau-Korallenkalk | Kalkstein: Korallen  | –   | – |  Wittnau-Korallenkalk |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200198 |Hauptrogenstein: Furcil-Mergel | Mergelstein  | Kalkstein: mergelig   | – |  Furcil-Mergel |  Bathonien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200199 |Hauptrogenstein: Maeandrina-Sch. | Mergelstein: Bioklasten-Ooide  | –   | – |  «Maeandrina-Schichten» |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200200 |Hauptrogenstein: Gisliflue-Korallenkalk | Kalkstein: Korallen  | Kalkstein: Bioklasten   | – |  Gisliflue-Korallenkalk |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200201 |Hauptrogenstein: Untere Acuminata-Sch. | Kalkstein: Bioklasten  | Kalkstein: Ooide   | Mergelstein |  «Untere Acuminata-Schichten» |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200202 |Klingnau-Fm.: Parkinsoni-Sch. | Mergelstein  | Kalkstein: Bioklasten   | – |  «Parkinsoni-Schichten» (Klingnau-Fm.) |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200203 |Dewalquei-Kalk | Kalkstein  | Kalkstein: mergelig: Bioklasten   | – |  «Couches à Pecten dewalquei» |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200204 |Brot-Sch. | Mergelstein: kalkig: Bioklasten  | –   | – |  Brot-Schichten |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200205 |Passwang-Fm.: Sissach-Mb.: Comptum-Bk. | Kalkstein: Eisenooide  | Kalkstein: spätig   | – |  «Comptum-Bank» (Passwang-Fm.) |  Aalénien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15200206 |Klettgau-Fm.: Seebi-Mb. | Sandstein: dolomitisch  | Dolomitstein   | Tonstein |  Seebi-Member |  Norien     | Norien   | Keuper  |
|15200207 |Klettgau-Fm.: Gruhalde-Mb. | Mergelstein: dolomitisch  | –   | – |  Gruhalde-Member |  Norien     | Carnien   | Keuper  |
|15200208 |Klettgau-Fm.: Berlingen-Mb. | Sandstein: kalkig  | –   | – |  Berlingen-Member |  Carnien     | Carnien   | Keuper  |
|15200209 |Klettgau-Fm.: Gansingen-Mb. | Dolomitstein: stromatolithisch  | Mergelstein: dolomitisch   | Evaporit: Sulfat |  Gansingen-Member |  Carnien     | Carnien   | Keuper  |
|15200210 |Klettgau-Fm.: Ergolz-Mb. | Mergelstein: siltig-dolomitisch  | Dolomitstein   | Sandstein |  Ergolz-Member |  Carnien     | Carnien   | Keuper  |
|15200211 |Schinznach-Fm.: Stamberg-Mb.: Kaisten-Bk. | Dolomitstein: Ooide  | –   | – |  Kaisten-Bank |  Ladinien     | Ladinien   | Muschelkalk  |
|15200212 |Schinznach-Fm.: Eptingen-Bk. | Dolomitstein: Ooide-Chert  | Kalkstein: Ooide   | – |  Eptingen-Bank |  Ladinien     | Ladinien   | Muschelkalk  |
|15200213 |Schinznach-Fm.: Dünnlenberg-Bk. | Mergelstein  | –   | – |  Dünnlenberg-Bank |  Anisien     | Anisien   | Muschelkalk  |
|15200214 |Schinznach-Fm.: Kienberg-Mb.: Saalhof-Bk. | Kalkstein: Bioklasten  | –   | – |  Saalhof-Bank |  Anisien     | Anisien   | Muschelkalk  |
|15200215 |Schinznach-Fm.: Leutschenberg-Mb.: Fützen-Bk. | Kalkstein: Ooide-Chert  | –   | – |  Fützen-Bank |  Anisien     | Anisien   | Muschelkalk  |
|15200216 |Zeglingen-Fm.: Dolomitzone | Dolomitstein: stromatolithisch: Chert  | –   | – |  «Dolomitzone» (Zeglingen-Fm.) |  Anisien     | Anisien   | Muschelkalk  |
|15200217 |Weitenau-Fm.: Oberer Schuttfächer | Sandstein: Feldspat  | Konglomerat   | – |  «Oberer Schuttfächer» (Weitenau-Fm.) |  Lopingien     | Guadalupien   | Spät- bis postvariszisches Grundgebirge  |
|15200218 |Weitenau-Fm.: Playa-Serie | Sandstein: tonig: Glimmer  | Sandstein: tonig: Feldspat   | – |  «Playa-Serie» (Weitenau-Fm.) |  Lopingien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15200219 |Weitenau-Fm.: Unterer Schuttfächer | Sandstein: Feldspat  | Konglomerat   | Tonstein |  «Unterer Schuttfächer» (Weitenau-Fm.) |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15200220 |Schwarzwald-Massiv: Spät- bis postvariszische Intrusiva | Gestein: plutonisch  | –   | – |  – |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200221 |Nordalpines Vorland: Spät- bis postvariszische Sedimente und Vulkanite | Sandstein  | Konglomerat   | Tonstein |  – |  Perm     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15200222 |Stockberg-Quarzporphyr | Rhyolith  | –   | – |  Stockberg-Rhyolith |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200223 |Bärhalde-Granit | Granit: Biotit-Muskovit  | –   | – |  Bärhalde-Granit |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200224 |Schluchsee-Granit | Granit: Biotit-Muskovit  | –   | – |  Schluchsee-Granit |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200225 |Säckingen-Granit | Granit: aplitisch  | –   | – |  Säckingen-Granit |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200226 |Weiach-Fm.: Jüngere Flussablagerungen | Sandstein: Feldspat  | –   | – |  «Jüngere Flussablagerungen» (Weiach-Fm.) |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15200227 |Weiach-Fm.: Seeablagerungen | Tonstein  | –   | – |  «Seeablagerungen» (Weiach-Fm.) |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15200228 |Weiach-Fm.: Ältere Flussablagerungen | Sandstein: Feldspat  | Tonstein   | Konglomerat |  «Ältere Flussablagerungen» (Weiach-Fm.) |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200229 |Weiach-Fm.: Ältere Flussablagerungen: Kohle-Serie | Sandstein  | Tonstein: Kohle   | – |  «Kohle-Serie» (Weiach-Fm.) |  Spätes Pennsylvanien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15200230 |Schwarzwald-Massiv: Früh- bis mittelvariszische Intrusiva | Gestein: plutonisch  | –   | – |  – |  Mississippien     | Frühes Devon   | Frühvariszisches Grundgebirge  |
|15200231 |Albtal-Granit | Granit: porphyrisch: Biotit  | –   | – |  Albtal-Granit |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15200232 |Malsburg-Granit | Granit: Biotit  | –   | – |  Malsburg-Granit |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15200233 |Blauen-Granit | Granit: Biotit  | –   | – |  Blauen-Granit |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15200234 |Klemmbach-Granit | Granit: Biotit-Muskovit  | –   | – |  Klemmbach-Granit |  Mississippien     | Frühes Devon   | Frühvariszisches Grundgebirge  |
|15203050 |Combe-du-Pissot-Fm.: Chevalets-Mb. | Kalkstein: kieselig  | Mergelstein: Glaukonit   | – |  Chevalets-Schichten |  Toarcien     | Toarcien   | Syn-Rift  |
|15203047 |Rossinière-Fm. | Kalkstein: spätig: Glaukonit  | –   | – |  Rossinière-Formation |  Aalénien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15203048 |Heiti-Fm. | Mergelstein  | Kalkstein: kieselig   | – |  Heiti-Formation |  Bajocien     | Sinémurien   | Lias-Dogger in pelagischer Fazies  |
|15203049 |Combe-du-Pissot-Fm. | Tonstein: schiefrig: Bitumen  | Kalkstein: kieselig   | Mergelstein: Glaukonit |  Combe-du-Pissot-Formation |  Toarcien     | Toarcien   | Syn-Rift  |
|15203051 |Combe-du-Pissot-Fm.: Creux-de-l&#39;Ours-Mb. | Mergelstein: Bitumen  | Kalkstein   | – |  Creux-de-l&#39;Ours-Schichten |  Toarcien     | Toarcien   | Syn-Rift  |
|15203052 |Petit-Liençon-Fm. | Kalkstein: kieselig  | Mergelstein: schiefrig   | – |  Petit-Liençon-Formation |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15203053 |Arvel-Fm. | Kalkstein: spätig: Bioklasten  | Mergelstein: schiefrig   | – |  Arvel-Formation |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15203054 |Grande-Bonavau-Fm. | Kalkstein: spätig: Glaukonit  | Kalkstein: dolomitisch: Bioklasten   | – |  Grande-Bonavau-Formation |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15203055 |Chauderon-Fm. | Kalkstein: kieselig-spätig  | Mergelstein: schiefrig   | – |  Chauderon-Formation |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15203056 |Vudalla-Fm. | Kalkstein: mikritisch  | Kalkstein: Ooide   | – |  Vudalla-Formation |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15203057 |Vudalla-Fm.: Bois-de-Luan-Mb. | Kalkstein: mikritisch  | Kalkstein: sandig: Bioklasten   | Mergelstein |  Bois-de-Luan-Member |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15203058 |Vudalla-Fm.: Agreblierai-Mb. | Kalkstein: Ooide  | –   | – |  Agreblierai-Member |  Hettangien     | Hettangien   | Lias-Dogger in neritischer Fazies  |
|15203059 |Col-de-Tompey-Fm. | Mergelstein: dolomitisch  | Sandstein: kalkig: Glaukonit   | – |  Col-de-Tompey-Formation |  Hettangien     | Rhät   | «Rhät»  |
|15203060 |Plan-Falcon-Fm. | Mergelstein: schiefrig  | Kalkstein: mergelig-dolomitisch   | Kalkstein: Bioklasten-Ooide |  Plan-Falcon-Formation |  Rhät     | Rhät   | «Rhät»  |
|15203061 |Dolomies Blondes | Dolomitstein  | Tonstein   | Mergelstein: dolomitisch |  «Dolomies Blondes» |  Norien     | Norien   | Hauptdolomit  |
|15203062 |Clôt-la-Cime-Fm. | Dolomitstein  | Evaporit: Gips   | Brekzie |  Clôt-la-Cime-Formation |  Carnien     | Carnien   | Raibl  |
|15203066 |Griggeli-Fm. | Kalkstein: kieselig  | Mergelstein   | – |  Griggeli-Formation |  Oxfordien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15203067 |Griggeli-Fm.: Mythen-Kieselkalk | Kalkstein: kieselig  | Mergelstein   | Kalkstein: spätig |  Mythen-Kieselkalk |  Oxfordien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15203068 |Griggeli-Fm.: Griggeli-Bk. | Kalkstein: spätig: Bioklasten  | –   | – |  «Griggeli-Bank» |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15203069 |Gibel-Fm. | Kalkstein: kieselig-spätig  | –   | – |  Gibel-Formation |  Callovien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15203070 |Gibel-Fm.: Rämsi-Mb. | Brekzie: dolomitisch  | Kalkstein: Korallen   | – |  Rämsi-Member |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15203071 |Gibel-Fm.: Gibel-Mb. | Kalkstein: sandig: Bioklasten  | Konglomerat   | Kalkstein: spätig: Bioklasten |  «Gibel-Member» |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15203072 |Gibel-Fm.: Steinberg-Konglomerat | Konglomerat  | –   | – |  Steinberg-Konglomerat |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15203073 |Gibel-Fm.: Musenalp-Mb. | Kalkstein: spätig: Chert  | Kalkstein: Ooide   | – |  Musenalp-Member |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15203074 |Stanserhorn-Fm. | Mergelstein  | Kalkstein: kieselig   | – |  Stanserhorn-Formation |  Bajocien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15203075 |Stanserhorn-Fm.: Zoophycos-Sch. | Mergelstein  | Kalkstein: kieselig   | – |  «Zoophycos-Schichten» (Stanserhorn-Fm.) |  Bajocien     | Aalénien   | Lias-Dogger in pelagischer Fazies  |
|15203076 |Stanserhorn-Fm.: Spis-Kalk | Kalkstein: Onkoide  | Kalkstein: Bioklasten   | Kalkstein: Eisenmineralien |  Spis-Kalk |  Toarcien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15203077 |Stanserhorn-Fm.: Posidonienschiefer | Tonstein: schiefrig: Bitumen  | Mergelstein   | Kalkstein |  «Posidonienschiefer» (Stanserhorn-Fm.) |  Toarcien     | Toarcien   | Lias-Dogger in pelagischer Fazies  |
|15203078 |Obflue-Fm. | Kalkstein: kieselig  | Mergelstein: Glaukonit   | – |  Obflue-Formation |  Pliensbachien     | Pliensbachien   | Lias-Dogger in neritischer Fazies  |
|15203079 |Brand-Fm. | Kalkstein: spätig: Bioklasten-Chert  | Mergelstein   | – |  Brand-Formation |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15203080 |Horngraben-Fm. | Kalkstein: sandig  | Mergelstein: Bioklasten   | Brekzie |  Horngraben-Formation |  Hettangien     | Hettangien   | «Rhät»  |
|15203081 |Lückengraben-Fm. | Kalkstein: dolomitisch  | Kalkstein: spätig   | Mergelstein |  Lückengraben-Formation |  Rhät     | Rhät   | «Rhät»  |
|15203082 |Dorfflüe-Fm. | Kalkstein: mikritisch  | –   | – |  Dorfflüe-Formation |  Berriasien     | Oxfordien   | Malm  |
|15203083 |Dorfflüe-Fm.: Gummfluh-Mikrofazies | Kalkstein: arenitisch: Bioklasten  | –   | – |  Gummfluh-Mikrofazies |  Später Jura     | Später Jura   | Malm  |
|15203084 |Dorfflüe-Fm.: Pfad-Mikrofazies | Kalkstein: Bioklasten  | –   | – |  Pfad-Mikrofazies |  Später Jura     | Später Jura   | Malm  |
|15203085 |Dorfflüe-Fm.: Rindenkorn-Mikrofazies | Kalkstein: Onkoide  | –   | – |  Rindenkorn-Mikrofazies |  Später Jura     | Später Jura   | Malm  |
|15203086 |Dorfflüe-Fm.: Gastlosen-Oolith | Kalkstein: Ooide  | –   | – |  Gastlosen-Oolith |  Später Jura     | Später Jura   | Malm  |
|15203087 |Dorfflüe-Fm.: Wandfluh-Mikrofazies | Kalkstein: mikritisch: Bioklasten  | Kalkstein: Ooide   | – |  Wandfluh-Mikrofazies |  Später Jura     | Später Jura   | Malm  |
|15203088 |Mytilus-Sch. | Mergelstein: sandig: Kohle  | Kalkstein: sandig: Bioklasten   | Konglomerat |  Mytilus-Schichten |  Callovien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15203089 |Mytilus-Sch.: Col-de-Cordon-Mb. | Kalkstein: sandig  | Kalkstein: arenitisch   | Konglomerat |  Col-de-Cordon-Member |  Callovien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15203090 |Mytilus-Sch.: Col-de-Cordon-Mb.: Klus-Konglomerat | Kalkstein: sandig: Bioklasten  | –   | – |  Klus-Konglomerat |  Callovien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15203092 |Mytilus-Sch.: Rubli-Mb. | Kalkstein: mergelig: Bioklasten  | Kalkstein: mikritisch: Onkoide   | – |  Rubli-Member |  Callovien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15203093 |Mytilus-Sch.: Chavanette-Mb. | Konglomerat  | Mergelstein: sandig: Kohle   | – |  Chavanette-Member |  Bajocien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15203094 |Pralet-Fm.: Erpilles-Mb. | Dolomitstein  | Brekzie: dolomitisch   | Mergelstein: schiefrig |  Erpilles-Member |  Ladinien     | Ladinien   | Raibl  |
|15203095 |Wiriehorn-Fm. | Kalkstein  | Dolomitstein   | – |  Wiriehorn-Formation |  Anisien     | Anisien   | Karbonatische Trias  |
|15203096 |St-Triphon-Fm. | Kalkstein  | Dolomitstein   | Tonstein |  St-Triphon-Formation |  Anisien     | Olénékien   | Karbonatische Trias  |
|15203097 |St-Triphon-Fm.: Andonces-Mb. | Kalkstein  | Kalkstein: stromatolithisch   | Tonstein |  Andonces-Member |  Anisien     | Anisien   | Karbonatische Trias  |
|15203098 |St-Triphon-Fm.: Lessus-Mb. | Kalkstein  | –   | – |  Lessus-Member |  Anisien     | Anisien   | Karbonatische Trias  |
|15203099 |St-Triphon-Fm.: Dorchaux-Mb. | Dolomitstein: stromatolithisch  | Tonstein   | – |  Dorchaux-Member |  Anisien     | Olénékien   | Karbonatische Trias  |
|15203100 |Mattes-Melange | Tonstein  | Siltstein   | Sandstein |  Mattes-Melange |  Priabonien     | Priabonien   | Mélange  |
|15203101 |Chumi-Fm. | Mergelstein: kalkig  | Sandstein   | Brekzie: polymikt |  Chumi-Formation |  Mittleres Eozän     | Yprésien   | Flysch  |
|15203102 |Joux-Verte-Fm. | Mergelstein  | Kalkstein: kieselig: Glaukonit   | – |  Joux-Verte-Formation |  Turonien     | Barrémien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203103 |Bonave-Fm. | Kalkstein: mikritisch: Chert  | Kalkstein: arenitisch   | Brekzie |  Bonave-Formation |  Valanginien     | Tithonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203104 |Obere Brekzie | Kalkstein: mikritisch  | Brekzie: kalkig   | – |  «Obere Brekzie» (Brekzien-Decke) |  Tithonien     | Kimméridgien   | Lias-Dogger in neritischer Fazies  |
|15203105 |Obere Schiefer | Tonstein: kieselig  | Kalkstein: arenitisch   | – |  «Obere Schiefer» (Brekzien-Decke) |  Oxfordien     | Callovien   | Lias-Dogger in pelagischer Fazies  |
|15203106 |Untere Brekzie | Brekzie: polymikt  | Brekzie: dolomitisch   | – |  «Untere Brekzie» (Brekzien-Decke) |  Callovien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15203107 |Untere Schiefer | Tonstein: sandig-schiefrig  | Kalkstein: spätig   | Brekzie |  «Untere Schiefer» (Brekzien-Decke) |  Aalénien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15203108 |Untere Schiefer: Untere Kalke | Kalkstein: spätig: Chert  | –   | – |  «Untere Kalke» (Brekzien-Decke) |  Sinémurien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15203109 |Brekzien-Decke:Trias | Dolomitstein  | Gestein: pelitisch   | Kalkstein: Bioklasten |  – |  Späte Trias     | Späte Trias   | Prä-Rift  |
|15203110 |Gurnigel-Decke: Flysch | Sandstein  | Mergelstein   | – |  – |  Paleozän     | Maastrichtien   | Flysch  |
|15203111 |Gurnigel-Decke: Flysch-4 | Mergelstein: tonig  | Sandstein: kalkig   | Sandstein: kieselig |  «Flysch 4 mit siltigen Turbiditen» |  Lutétien     | Lutétien   | Flysch  |
|15200238 |St.-Blasien-Granit | Granit: Biotit  | –   | – |  St.-Blasien-Granit |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15200235 |Randgranit | Granit: Biotit-Muskovit  | –   | – |  «Randgranit» |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15200236 |Münsterhalden-Granit | Granit  | –   | – |  Münsterhalden-Granit |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15200237 |Schönau-Herrenschwand-Granit | Granit  | –   | – |  Schönau-Herrenschwand-Granit |  Mississippien     | Frühes Devon   | Frühvariszisches Grundgebirge  |
|15200239 |Mambach-Granit | Granit  | Granodiorit   | – |  Mambach-Granit |  Mississippien     | Frühes Devon   | Frühvariszisches Grundgebirge  |
|15200240 |Lenzkirch-Steina-Granit | Granit: Biotit  | –   | – |  Lenzkirch-Steina-Granit |  Mississippien     | Frühes Devon   | Frühvariszisches Grundgebirge  |
|15200241 |Hauenstein-Granit | Granit  | –   | – |  Hauenstein-Granit |  Mississippien     | Frühes Devon   | Frühvariszisches Grundgebirge  |
|15200242 |Böttstein-Granit | Granit: porphyrisch: Biotit  | –   | – |  Böttstein-Granit |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15200243 |Schwarzwald-Massiv: Früh- bis mittelvariszische Sedimente | Gestein: sedimentär  | –   | – |  – |  Mississippien     | Devon   | Prä- bis frühvariszisches Grundgebirge  |
|15200245 |Schwarzwald-Massiv: Prävariszisches polyzyklisches Grundgebirge | Gneis: migmatitisch  | Gneis: magmatisch   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15200246 |Schwarzwald-Massiv: Prävariszische Orthogneise | Gneis: magmatisch  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15200247 |Todtmoos-Gneiskomplex | Gneis: migmatitisch  | Gneis: Hornblende   | – |  Todtmoos-Horbach-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15200248 |Murgtal-Gneiskomplex | Gneis: migmatitisch: Cordierit  | –   | – |  Murgtal-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15200249 |Laufenburg-Gneiskomplex | Gneis: migmatitisch  | –   | – |  Laufenburg-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15200250 |Schwarzwald-Massiv: Prävariszische Migmatite | Gneis: migmatitisch  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15200251 |Wiesen-Wehratal-Gneiskomplex | Gneis: migmatitisch  | –   | – |  Wiesen-Wehratal-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15200252 |Wiesen-Wehratal-Gneiskomplex: Wehratal-Syenit | Syenit  | –   | – |  Wehratal-Syenit |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15200253 |Schwarzwald-Massiv: Prävariszische Grüngesteine | Amphibolit  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15200254 |Molasse | Sandstein  | Mergelstein   | Konglomerat |  – |  Serravallien     | Rupélien   | Molasse  |
|15200255 |OSM (Obere Süsswassermolasse) | Mergelstein  | Sandstein   | Konglomerat |  – |  Serravallien     | Burdigalien   | OSM  |
|15200256 |Pfänder-Fm.: Tannenberg-Sch. | Sandstein  | Konglomerat   | – |  Tannenberg-Schichten |  Tortonien     | Serravallien   | Molasse  |
|15200257 |Pfänder-Fm. | Konglomerat  | Sandstein   | Mergelstein: tonig |  Pfänder-Formation |  Serravallien     | Spätes Burdigalien   | Molasse  |
|15200258 |Napf-Fm. | Konglomerat: polymikt: Quarz  | Sandstein: Feldspat   | Mergelstein |  Napf-Formation |  Langhien     | Burdigalien   | OSM  |
|15200259 |Napf-Fm.: Eimätteli-Mb.: Blapbach-Kohlehorizont | Mergelstein: Kohle  | –   | – |  Blapbach-Kohleflöz |  Burdigalien     | Burdigalien   | OSM  |
|15200260 |Napf-Fm.: Eimätteli-Mb. | Mergelstein: Glimmer  | Konglomerat: ophiolithisch   | Siltstein: tonig |  Eimätteli-Member |  Burdigalien     | Burdigalien   | OSM  |
|15200261 |Schüpferegg-Nagelfluh | Konglomerat: polymikt: Quarz  | Sandstein   | Mergelstein |  Schüpferegg-Nagelfluh |  Burdigalien     | Burdigalien   | Molasse  |
|15200262 |OSM-II | Konglomerat  | Sandstein   | – |  – |  Tortonien     | Langhien   | OSM  |
|15200263 |Hegau-Vulkanite | Gestein: vulkanisch  | –   | – |  – |  Messinien     | Langhien   | Hegau-Vulkanismus  |
|15200264 |Höwenegg-Basalt | Basalt  | –   | – |  Höwenegg-Basalt |  Messinien     | Messinien   | Hegau-Vulkanismus  |
|15200265 |Hohenwiel-Phonolith | 15111372  | –   | – |  Hohenwiel-Phonolith |  Tortonien     | Tortonien   | Hegau-Vulkanismus  |
|15200266 |Hegau-Tuffit | Tuffit  | –   | – |  Hegau-Tuffit |  Serravallien     | Langhien   | Hegau-Vulkanismus  |
|15200267 |Hörnli-Fm.: Hörnligipfel-Nagelfluh | Konglomerat  | Mergelstein   | Sandstein |  Hörnligipfel-Nagelfluh |  Tortonien     | Tortonien   | OSM  |
|15200268 |Hörnli-Fm.: Hörnligubel-Mergel: Höchegg-Brekzie | Brekzie: sandig  | –   | – |  Höchegg-Brekzie |  Serravallien     | Serravallien   | OSM  |
|15200269 |Hörnli-Fm.: Hörnligubel-Mergel | Mergelstein  | Sandstein: mergelig   | Konglomerat |  Hörnligubel-Mergel |  Tortonien     | Serravallien   | OSM  |
|15200270 |Hörnli-Fm.: Tösswald-Mb. | Konglomerat: kalkig-dolomitisch  | Mergelstein   | Sandstein |  Tösswald-Member |  Serravallien     | Langhien   | OSM  |
|15200271 |Öhningen-Fm.: Bischofszell-Bentonit | Bentonit  | –   | – |  Bischofzell-Bentonit |  Langhien     | Langhien   | OSM  |
|15200272 |Hörnli-Fm.: Mergelstein-dominierte Fazies | Mergelstein  | Siltstein: Kohle   | Sandstein |  Hörnli-Formation |  Langhien     | Langhien   | OSM  |
|15200273 |Hörnli-Fm.: Krinau-Mb. | Konglomerat  | Mergelstein: Kohle   | Sandstein: Glimmer |  Krinau-Member |  Langhien     | Langhien   | OSM  |
|15200274 |OSM-II: Glimmersand-Fazies | Sandstein: Quarz-Glimmer  | –   | – |  – |  Tortonien     | Langhien   | OSM  |
|15200275 |Zürich-Fm.: Fellitobel-Süsswasserkalk | Kalkstein  | –   | – |  Fellitobel-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200276 |Uetliberg-Fm. | Konglomerat: kalkig-dolomitisch  | Mergelstein   | – |  Uetliberg-Formation |  Serravallien     | Serravallien   | OSM  |
|15200277 |Uetliberg-Fm.: Uetliberggipfel-Nagelfluh | Konglomerat: kalkig-dolomitisch  | –   | – |  Uetliberggipfel-Nagelfluh |  Serravallien     | Serravallien   | OSM  |
|15200278 |Uetliberg-Fm.: Uetliberg-Mergel | Mergelstein  | –   | – |  Uetliberg-Mergel |  Serravallien     | Serravallien   | OSM  |
|15200279 |Pfannenstiel-Fm.: Falätschen-Mergel | Mergelstein  | –   | – |  Falätschen-Mergel |  Langhien     | Langhien   | OSM  |
|15200280 |Pfannenstiel-Fm. | Mergelstein  | Sandstein   | – |  Pfannenstiel-Formation |  Serravallien     | Serravallien   | OSM  |
|15200281 |Zürich-Fm. | Mergelstein  | Kalkstein   | – |  Zürich-Formation |  Langhien     | Langhien   | OSM  |
|15200282 |Zürich-Fm.: Leimbach-Bentonit | Bentonit  | –   | – |  Leimbach-Bentonit |  Langhien     | Langhien   | OSM  |
|15200283 |Zürich-Fm.: Rütschlibach-Riedhof-Süsswasserkalk | Kalkstein  | –   | – |  Rütschlibach-Riedhof-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200284 |Zürich-Fm.: Winterthur-Bentonit | Bentonit  | –   | – |  Winterthur-Bentonit |  Langhien     | Langhien   | OSM  |
|15200285 |Zürich-Fm.: Aeugstertal-Bentonit | Bentonit  | –   | – |  Aeugstertal-Bentonit |  Langhien     | Langhien   | OSM  |
|15200286 |Zürich-Fm.: Äntlisberg-Doldertobel-Süsswasserkalk | Kalkstein: Bitumen  | –   | – |  Äntlisberg-Doldertobel-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200287 |Zürich-Fm.: Wehrenbach-Höckler-Süsswasserkalk | Kalkstein  | Mergelstein: Bitumen   | – |  Wehrenbach-Höckler-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200288 |Meilen-Fm.: Küsnacht-Bentonit | Bentonit  | –   | – |  Küsnacht-Bentonit |  Langhien     | Langhien   | OSM  |
|15200289 |Meilen-Fm.: Urdorf-Bentonit | Bentonit  | –   | – |  Urdorf-Bentonit |  Langhien     | Langhien   | OSM  |
|15200290 |Appenzellergranit-Leitniveau | Konglomerat  | Sandstein: kalkig   | Siltstein: kalkig |  «Appenzellergranit-Leitniveau» |  Langhien     | Langhien   | OSM  |
|15200291 |Appenzellergranit-Leitniveau: Abtwil-Konglomerat | Konglomerat  | –   | – |  Abtwil-Konglomerat |  Langhien     | Langhien   | OSM  |
|15200292 |Appenzellergranit-Leitniveau: Hüllistein-Konglomerat | Konglomerat: kalkig-dolomitisch  | Brekzie   | – |  Hüllistein-Konglomerat |  Langhien     | Langhien   | OSM  |
|15200293 |Appenzellergranit-Leitniveau: Degersheim-Kalknagelfluh | Konglomerat  | Brekzie   | Kalkstein |  Degersheim-Kalknagelfluh |  Langhien     | Langhien   | OSM  |
|15200294 |Appenzellergranit-Leitniveau: Meilen-Kalk | Siltstein: kalkig  | Sandstein: siltig-kalkig   | Kalkstein: arenitisch |  Meilen-Kalk |  Langhien     | Langhien   | OSM  |
|15200295 |OSM-I | Konglomerat  | Sandstein   | Mergelstein |  – |  Langhien     | Burdigalien   | OSM  |
|15200296 |Lichtensteig-Fm. | Konglomerat: polymikt  | Sandstein   | Mergelstein |  Lichtensteig-Formation |  Langhien     | Spätes Burdigalien   | OSM  |
|15200297 |Hörnli-Fm. | Konglomerat  | Sandstein   | Mergelstein |  Hörnli-Formation |  Tortonien     | Langhien   | OSM  |
|15200298 |Guggershorn-Fm. | Konglomerat: kalkig-dolomitisch  | Sandstein   | Mergelstein |  Guggershorn-Formation |  Langhien     | Spätes Burdigalien   | OSM  |
|15203115 |Gurnigel-Decke: Flysch-2a | Tonstein  | Sandstein: Glaukonit   | – |  «Flysch 2a tonig-sandig» |  Danien     | Danien   | Flysch  |
|15203112 |Gurnigel-Decke: Flysch-3b | Mergelstein  | Sandstein: kalkig: Bioklasten   | – |  «Flysch 3b mit bioklastischen Turbiditen» |  Yprésien     | Yprésien   | Flysch  |
|15203113 |Gurnigel-Decke: Flysch-3a | Mergelstein  | Sandstein: kalkig   | – |  «Flysch 3a mergelig-sandig» |  Yprésien     | Yprésien   | Flysch  |
|15203114 |Gurnigel-Decke: Flysch-2b | Sandstein: kieselig  | Sandstein: Glaukonit   | Mergelstein |  «Flysch 2b mit sandigen Turbiditen» |  Thanétien     | Thanétien   | Flysch  |
|15203116 |Hellstätt-Fm. | Tonstein  | Kalkstein: siltig-tonig   | Sandstein |  Hellstätt-Formation |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203117 |Schlieren-Decke: Flysch | Sandstein  | Siltstein   | – |  – |  Yprésien     | Maastrichtien   | Flysch  |
|15203118 |Schlieren-Sandstein | Sandstein: kalkig: Nummuliten  | Siltstein   | Tonstein |  Schlieren-Sandstein |  Yprésien     | Yprésien   | Flysch  |
|15203119 |Schoni-Sandstein | Sandstein: kalkig: Nummuliten  | Siltstein   | Tonstein |  Schoni-Sandstein |  Yprésien     | Yprésien   | Flysch  |
|15203120 |Schoni-Sandstein: Oberer Tonstein | Tonstein  | Siltstein   | – |  «Obere Tonsteinschichten» (Schlieren-Flysch) |  Yprésien     | Yprésien   | Flysch  |
|15203121 |Guber-Sandstein | Sandstein  | Siltstein   | – |  Guber-Sandstein |  Thanétien     | Thanétien   | Flysch  |
|15203122 |Guber-Sandstein: Unterer Tonstein | Tonstein  | Sandstein: Quarz   | – |  «Untere Tonsteinschichten» (Schlieren-Flysch) |  Paleozän     | Paleozän   | Flysch  |
|15203123 |Schlieren-Decke: Basaler Flysch | Sandstein  | Siltstein   | Kalkstein: mergelig |  – |  Maastrichtien     | Campanien   | Flysch  |
|15203124 |Estavannens-Fm. | Sandstein: kalkig  | Mergelstein   | Tonstein |  Estavannens-Flysch |  Thanétien     | Danien   | Flysch  |
|15203125 |Reidigen-Fm. | Sandstein: Glimmer  | Tonstein   | Kalkstein: mikritisch |  Reidigen-Formation |  Danien     | Maastrichtien   | Flysch  |
|15203126 |Biot-Fm. | Sandstein: kalkig  | Kalkstein: mikritisch   | – |  Biot-Formation |  Maastrichtien     | Campanien   | Flysch  |
|15203127 |Chétillon-Fm. | Tonstein  | Siltstein   | Sandstein |  Chétillon-Formation |  Santonien     | Coniacien   | Flysch  |
|15203128 |Rodomonts-Fm. | Sandstein  | Mergelstein: schiefrig   | Konglomerat: polymikt |  Rodomonts-Formation |  Coniacien     | Turonien   | Flysch  |
|15203129 |Rodomonts-Fm.: Mocausa-Nagelfluh | Sandstein  | Konglomerat: polymikt   | – |  Mocausa-Nagelfluh |  Coniacien     | Turonien   | Flysch  |
|15203130 |Tissota-Melange | Tonstein  | Mergelstein   | – |  Tissota-Melange |  Santonien     | Santonien   | Mélange  |
|15203131 |Tissota-Melange: Gueyraz-Komplex | Kalkstein  | Mergelstein   | – |  Gueyraz-Komplex |  Späte Kreide     | Früher Jura   | Mélange  |
|15203132 |Manche-Fm.: Weissenburg-Flysch | Konglomerat: kalkig  | Sandstein: kalkig-dolomitisch   | Mergelstein |  Weissenburg-Flysch |  Santonien     | Turonien   | Flysch  |
|15203133 |Manche-Fm. | Sandstein: siltig-kalkig  | Mergelstein   | – |  Manche-Formation |  Santonien     | Turonien   | Flysch  |
|15203134 |Fouyet-Fm. | Tonstein  | Kalkstein: tonig-schiefrig   | Kalkstein: sandig |  Fouyet-Formation |  Turonien     | Albien   | Flysch  |
|15203135 |Tissota-Melange: Gueyraz-Komplex: Foraminiferenschichten | Kalkstein: tonig-schiefrig  | Mergelstein: schiefrig   | – |  «Foraminiferenschichten» (Tissota-Melange) |  Cénomanien     | Barrémien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203136 |Tissota-Melange: Gueyraz-Komplex: Aptychenkalk | Kalkstein: mikritisch: Aptychen  | –   | – |  «Aptychenkalk» (Tissota-Melange) |  Barrémien     | Tithonien   | Maiolica / Aptychenkalk  |
|15203137 |Tissota-Melange: Gueyraz-Komplex: Radiolarit | Gestein: kieselig: Radiolarien  | –   | – |  «Radiolarit» (Tissota-Melange) |  Kimméridgien     | Bathonien   | Radiolarit  |
|15203138 |Tissota-Melange: Gueyraz-Komplex: Filamentkalk | Kalkstein: Bioklasten  | Mergelstein   | – |  «Filamentkalk» (Tissota-Melange) |  Callovien     | Aalénien   | Lias-Dogger in pelagischer Fazies  |
|15203139 |Tissota-Melange: Gueyraz-Komplex: Spatkalk | Kalkstein: spätig  | –   | – |  «Spatkalk» (Tissota-Melange) |  Früher Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15203140 |Hundsrügg-Fm. | Sandstein: Glimmer  | Konglomerat   | – |  Hundsrügg-Formation |  Campanien     | Coniacien   | Flysch  |
|15203141 |Perrières-Fm. | Tonstein  | Kalkstein: mikritisch   | Sandstein |  Perrières-Formation |  Coniacien     | Turonien   | Flysch  |
|15203142 |Rhenodanubischer Flysch | Sandstein  | Gestein: pelitisch   | – |  – |  Späte Kreide     | Frühe Kreide   | Flysch  |
|15203143 |Vorarlberg-Flysch | Sandstein  | Gestein: pelitisch   | Kalkstein |  – |  Späte Kreide     | Späte Kreide   | Flysch  |
|15203144 |Fanola-Fm. | Tonstein: sandig-mergelig  | Brekzie: polymikt   | Sandstein: Quarz |  Fanola-Formation |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203145 |Planknerbrücke-Fm. | Sandstein  | Tonstein   | Kalkstein: mikritisch |  Planknerbrücke-Formation |  Maastrichtien     | Campanien   | Flysch  |
|15203146 |Planken-Fm. | Kalkstein: mikritisch  | Kalkstein: siltig   | Mergelstein |  Planken-Formation |  Santonien     | Coniacien   | Flysch  |
|15203147 |Reiselsberg-Fm. | Sandstein  | Tonstein   | – |  Reiselsberg-Formation |  Turonien     | Turonien   | Flysch  |
|15203148 |Reiselsberg-Fm.: Basaler Teil | Kalkstein: mergelig  | Tonstein   | Sandstein: Glimmer |  Reiselsberg-Formation |  Turonien     | Turonien   | Flysch  |
|15203149 |Liechtenstein-Flysch | Kalkstein: kieselig: Glaukonit  | Tonstein   | – |  – |  Paläogen     | Frühe Kreide   | Flysch  |
|15203150 |Triesen-Fm. | Kalkstein: kieselig  | Tonstein   | Brekzie: polymikt |  Triesen-Formation |  Yprésien     | Maastrichtien   | Flysch  |
|15203151 |Vaduz-Flysch | Kalkstein: kieselig: Glaukonit  | Mergelstein   | Sandstein |  – |  Maastrichtien     | Turonien   | Flysch  |
|15203152 |Eichholztobel-Fm. | Kalkstein: kieselig: Glaukonit  | Mergelstein   | – |  Eichholztobel-Formation |  Santonien     | Coniacien   | Flysch  |
|15203153 |Schloss-Fm. | Sandstein: Glaukonit  | Kalkstein: kieselig: Glaukonit   | – |  Schloss-Formation |  Turonien     | Turonien   | Flysch  |
|15203154 |Gaschlo-Fm. | Sandstein: Quarz  | Kalkstein: kieselig: Glaukonit   | Mergelstein |  Gaschlo-Formation |  Maastrichtien     | Coniacien   | Flysch  |
|15203155 |Leimern-Sch.: Kalkige-Fazies | Kalkstein: mikritisch  | Mergelstein: kalkig   | – |  Leimern-Schichten |  Santonien     | Coniacien   | Couches Rouges  |
|15203156 |Pierre-Avoi-Melange | Schiefer  | Kalkstein: mergelig   | Brekzie |  Pierre-Avoi-Melange |  Rupélien     | Mittleres Eozän   | Mélange  |
|15203157 |St-Christophe-Fm. | Kalkstein: sandig: Glimmer  | Schiefer: kalkig   | – |  St-Christophe-Formation |  Späte Kreide     | Späte Kreide   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203158 |Marmontains-Fm. | Schiefer: tonig-kieselig: Bitumen  | Quarzit   | – |  Marmontains-Formation |  Cénomanien     | Aptien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203159 |Aroley-Fm. | Kalkstein: sandig  | Brekzie: kalkig   | – |  Aroley-Formation |  Aptien     | Barrémien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203160 |Ferret-Schiefer: Peula-Sch. | Quarzit  | Sandstein: kalkig   | Schiefer: tonig |  Peula-Schichten |  Frühe Kreide     | Frühe Kreide   | Sedimentbedeckung  |
|15203161 |Versoyen-Sch. | Basalt  | Gabbro   | Schiefer |  Versoyen-Schichten |  Kreide     | Kreide   | Sedimentbedeckung  |
|15203162 |Prättigau-Schiefer | Schiefer  | –   | – |  – |  Yprésien     | Valanginien   | Sedimentbedeckung  |
|15203163 |Ruchberg-Fm. | Sandstein: Feldspat  | Schiefer: tonig   | Brekzie: polymikt |  Ruchberg-Formation |  Yprésien     | Yprésien   | Sedimentbedeckung  |
|15203164 |Oberälpli-Fm. | Tonstein: schiefrig  | Kalkstein: sandig-kieselig   | Sandstein: Quarz-Glaukonit |  Oberälpli-Formation |  Thanétien     | Danien   | Sedimentbedeckung  |
|15203165 |Eggberg-Fm. | Kalkstein: mergelig-schiefrig  | Brekzie: polymikt   | Kalkstein: sandig |  Eggberg-Formation |  Maastrichtien     | Maastrichtien   | Sedimentbedeckung  |
|15203166 |Gyrenspitz-Fm. | Brekzie: polymikt  | Kalkstein: sandig-kieselig   | Mergelstein: schiefrig |  Gyrenspitz-Formation |  Maastrichtien     | Campanien   | Sedimentbedeckung  |
|15203167 |Fadura-Fm. | Kalkstein: mergelig-schiefrig  | Kalkstein: sandig-kieselig   | Brekzie |  Fadura-Formation |  Santonien     | Coniacien   | Sedimentbedeckung  |
|15203168 |Pfävigrat-Fm. | Kalkstein: sandig-kieselig  | Mergelstein   | Brekzie: polymikt |  Pfävigrat-Formation |  Turonien     | Turonien   | Sedimentbedeckung  |
|15203169 |Sassauna-Fm. | Kalkstein: sandig-kieselig  | Tonstein: schiefrig   | Mergelstein: schiefrig |  Sassauna-Formation |  Cénomanien     | Cénomanien   | Sedimentbedeckung  |
|15203170 |Valzeina-Fm. | Tonstein: schiefrig  | Kalkstein: sandig   | – |  Valzeina-Formation |  Albien     | Aptien   | Sedimentbedeckung  |
|15203171 |Klus-Fm. | Kalkstein: sandig-kieselig  | Kalkstein: spätig   | Tonstein: schiefrig |  Klus-Formation |  Barrémien     | Valanginien   | Sedimentbedeckung  |
|15203172 |Stätzerhorn-Fm. | Schiefer: sandig-kalkig  | Schiefer: tonig   | – |  Stätzerhorn-Formation |  Eozän     | Späte Kreide   | Flysch  |
|15200302 |OSM-J: Juranagelfluh | Konglomerat: kalkig  | –   | – |  – |  Tortonien     | Aquitanien   | OSM  |
|15200299 |Käpfnach-Fm.: Horgen-Süsswasserkalk | Kalkstein  | Gestein: organisch: Kohle   | – |  Horgen-Käpfnach-Süsswasserkalk |  Burdigalien     | Burdigalien   | OSM  |
|15200300 |OSM-J | Sandstein  | Kalkstein: kreidig   | Konglomerat: kalkig |  – |  Langhien     | Spätes Burdigalien   | OSM  |
|15200301 |Bois-de-Raube-Fm. | Konglomerat  | Sandstein   | Mergelstein |  Bois-de-Raube-Formation |  Tortonien     | Serravallien   | OSM  |
|15200304 |Le-Locle-Fm.: Combe-Girard Mb.: Combe-Girard-Bentonit | Bentonit  | –   | – |  Combe-Girard-Bentonit |  Langhien     | Langhien   | OSM  |
|15200305 |Vermes-Süsswasserkalk | Kalkstein: mikritisch: Bioklasten  | Kalkstein: Onkoide   | Mergelstein |  Vermes-Süsswasserkalk |  Langhien     | Burdigalien   | OSM  |
|15200306 |Crêt-du-Locle-Fm.: Gompholitfazies | Konglomerat: kalkig  | –   | – |  Crêt-du-Locle-Formation |  Langhien     | Langhien   | Molasse  |
|15200307 |OMM (Obere Meeresmolasse) | Sandstein  | Mergelstein   | Konglomerat |  – |  Burdigalien     | Aquitanien   | OMM  |
|15200308 |OMM-II | Sandstein  | Konglomerat   | Mergelstein |  – |  Burdigalien     | Burdigalien   | OMM  |
|15200309 |St.-Gallen-Fm. | Sandstein: Glaukonit  | Mergelstein   | Konglomerat |  St.-Gallen-Formation |  Spätes Burdigalien     | Burdigalien   | OMM  |
|15200310 |St.-Gallen-Fm.: Staffelbach-Grobsandstein | Sandstein  | –   | – |  Staffelbach-Grobsandstein |  Burdigalien     | Burdigalien   | OMM  |
|15200311 |OMM-I | Sandstein  | Konglomerat   | Mergelstein |  – |  Burdigalien     | Aquitanien   | OMM  |
|15200312 |Luzern-Fm. | Sandstein: Glaukonit  | Mergelstein   | Konglomerat |  Luzern-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200313 |Luzern-Fm.: Safenwil-Muschelsandstein | Sandstein: kalkig: Muscheln  | –   | – |  Safenwil-Muschelsandstein |  Burdigalien     | Burdigalien   | OMM  |
|15200314 |USM (Untere Süsswassermolasse) | Sandstein  | Konglomerat   | Mergelstein |  – |  Aquitanien     | Rupélien   | USM  |
|15200315 |Höhronen-Nagelfluh | Konglomerat  | Sandstein   | Siltstein |  Höhronen-Nagelfluh |  Aquitanien     | Aquitanien   | USM  |
|15200316 |Kronberg-Nagelfluh | Konglomerat: polymikt  | –   | – |  Kronberg-Nagelfluh |  Aquitanien     | Aquitanien   | USM  |
|15200317 |Cornalle-Sandstein | Sandstein: kalkig  | Mergelstein: siltig   | – |  Cornalle-Sandstein |  Spätes Chattien     | Spätes Chattien   | USM  |
|15200318 |Mont-Pèlerin-Nagelfluh | Konglomerat: kalkig  | Mergelstein: siltig   | Sandstein: tonig |  Mont-Pèlerin-Nagelfluh |  Spätes Chattien     | Frühes Chattien   | USM  |
|15200319 |Speer-Fm. | Konglomerat: kalkig  | Mergelstein   | Sandstein: kalkig |  Speer-Formation |  Chattien     | Rupélien   | USM  |
|15200320 |Thun-Fm. | Konglomerat  | Sandstein   | Mergelstein |  Thun-Formation |  Spätes Chattien     | Frühes Chattien   | USM  |
|15200321 |Thun-Fm.: Gunten-Quarzitnagelfluh | Konglomerat: Quarz  | Sandstein   | Mergelstein |  Gunten-Nagelfluh |  Chattien     | Chattien   | USM  |
|15200322 |Rigi-Fm. | Konglomerat  | Tonstein: siltig   | – |  Rigi-Formation |  Chattien     | Chattien   | USM  |
|15200323 |Rigi-Fm.: Scheidegg-Nagelfluh | Konglomerat: kalkig  | Mergelstein   | – |  Scheidegg-Nagelfluh |  Chattien     | Chattien   | USM  |
|15200324 |Rigi-Fm.: Bunte Rigi-Nagelfluh | Konglomerat: kalkig-dolomitisch  | Sandstein   | Mergelstein |  «Bunte Rigi-Nagelfluh» |  Chattien     | Chattien   | USM  |
|15200325 |Rigi-Fm.: Radiolaritreiche Nagelfluh | Konglomerat: kalkig  | Sandstein   | Mergelstein |  «Radiolaritreiche Nagelfluh» (Rigi-Fm.) |  Chattien     | Chattien   | USM  |
|15200326 |USM-III | Konglomerat  | Mergelstein   | – |  – |  Burdigalien     | Burdigalien   | USM  |
|15200327 |Sommersberg-Nagelfluh | Konglomerat  | Mergelstein   | Sandstein: kalkig |  Sommersberg-Nagelfluh |  Burdigalien     | Burdigalien   | USM  |
|15200328 |Sommersberg-Nagelfluh: Brendenbach-Mergel | Mergelstein  | –   | – |  Brendenbach-Mergel |  Burdigalien     | Burdigalien   | USM  |
|15200329 |USM-II | Sandstein  | Mergelstein   | Konglomerat |  – |  Burdigalien     | Aquitanien   | USM  |
|15200330 |Fm. der Granitischen Molasse | Sandstein: Feldspat  | Mergelstein   | Konglomerat: polymikt |  «Formation der Granitischen Molasse» |  Aquitanien     | Spätes Chattien   | USM  |
|15200331 |Fm. der Granitischen Molasse: Oberaquitane Mergelzone | Mergelstein  | Sandstein: mergelig   | Sandstein: kalkig |  «Oberaquitane Mergelzone» |  Aquitanien     | Aquitanien   | USM  |
|15200332 |Lausanne-Fm. | Sandstein: tonig-kalkig  | Mergelstein: siltig   | – |  «Molasse Grise de Lausanne» |  Aquitanien     | Aquitanien   | USM  |
|15200333 |Lausanne-Fm.: Bois-Genoud-Bentonit | Bentonit  | –   | – |  Bois-Genoud-Bentonit |  Aquitanien     | Aquitanien   | USM  |
|15200334 |Lausanne-Fm.: Cuarny-Sandstein | Sandstein  | –   | – |  Cuarny-Sandstein |  Aquitanien     | Aquitanien   | USM  |
|15200335 |USM-I | Mergelstein  | Sandstein   | Konglomerat |  – |  Chattien     | Rupélien   | USM  |
|15200336 |Grès et Marnes Gris à Gypse | Mergelstein: Gips  | Sandstein   | Kalkstein |  «Grès et Marnes Gris à Gypse» |  Chattien     | Chattien   | USM  |
|15200337 |Molasse à Charbon | Sandstein: kalkig  | Mergelstein: sandig   | Tonstein: Kohle |  «Molasse à Charbon» |  Chattien     | Chattien   | USM  |
|15200338 |Molasse Rouge | Mergelstein  | Siltstein   | Sandstein: kalkig |  – |  Chattien     | Rupélien   | USM  |
|15200339 |Heuboden-Äschitannen-Nagelfluh | Konglomerat  | Mergelstein   | – |  Heuboden-Äschitannen-Nagelfluh |  Chattien     | Rupélien   | USM  |
|15200340 |Beichlen-Fm. | Konglomerat: kalkig  | Sandstein   | Mergelstein |  Beichlen-Formation |  Rupélien     | Rupélien   | USM  |
|15200341 |USM-J | Sandstein  | Mergelstein   | – |  – |  Chattien     | Chattien   | USM  |
|15200342 |USM-J: La-Chaux-Süsswasserkalk | Kalkstein: kreidig: Pisoide  | –   | – |  La-Chaux-Süsswasserkalk |  Aquitanien     | Aquitanien   | USM  |
|15200343 |Elsässer Molasse | Mergelstein  | Siltstein   | Sandstein: Glimmer |  «Elsässer-Molasse» |  Chattien     | Chattien   | USM  |
|15200344 |Elsässer Molasse: Delémont-Süsswasserkalk | Kalkstein: mikritisch  | –   | – |  Delémont-Süsswasserkalk |  Chattien     | Chattien   | USM  |
|15200345 |Elsässer Molasse: Matzendorf-Süsswasserkalk | Kalkstein  | –   | – |  Matzendorf-Süsswasserkalk |  Chattien     | Chattien   | USM  |
|15200346 |Elsässer Molasse: Oensingen-Süsswasserkalk | Kalkstein  | –   | – |  Oensingen-Süsswasserkalk |  Chattien     | Chattien   | USM  |
|15200347 |Elsässer Molasse: Wynau-Süsswasserkalk | Kalkstein  | –   | – |  Wynau-Süsswasserkalk |  Frühes Chattien     | Rupélien   | USM  |
|15200348 |UMM (Untere Meeresmolasse) | Mergelstein  | Sandstein   | – |  – |  Rupélien     | Rupélien   | UMM  |
|15200349 |UMM-III | Sandstein: kalkig: Glimmer  | Mergelstein   | – |  – |  Rupélien     | Rupélien   | UMM  |
|15200350 |Horw-Sandstein | Sandstein: kalkig: Glimmer  | Mergelstein   | – |  Horw-Sandstein |  Rupélien     | Rupélien   | UMM  |
|15200351 |UMM-II | Mergelstein  | Sandstein: kalkig: Glimmer   | – |  – |  Rupélien     | Rupélien   | UMM  |
|15200352 |Grisigen-Mergel | Mergelstein  | Sandstein: kalkig: Glimmer   | – |  Grisigen-Mergel |  Rupélien     | Rupélien   | UMM  |
|15200353 |UMM-I | Mergelstein: tonig  | Siltstein   | Sandstein: tonig: Lithoklasten |  – |  Rupélien     | Rupélien   | UMM  |
|15200354 |Cucloz-Fm. | Sandstein: Glimmer  | Mergelstein   | Siltstein |  Cucloz-Formation |  Rupélien     | Rupélien   | UMM  |
|15200355 |Cucloz-Fm.: Cucloz-Sandstein | Sandstein: Glimmer  | Brekzie: polymikt   | – |  Cucloz-Sandstein |  Rupélien     | Rupélien   | UMM  |
|15200356 |Cucloz-Fm.: Marnes gris-souris | Mergelstein  | Siltstein   | – |  «Marnes gris-souris» (Cucloz-Fm.) |  Rupélien     | Rupélien   | UMM  |
|15200357 |Cucloz-Fm.: Schistes marno-micacés | Mergelstein: siltig: Glimmer  | Sandstein   | – |  «Schistes marno-micacés» (Cucloz-Fm.) |  Rupélien     | Rupélien   | UMM  |
|15200358 |Hilfern-Fm. | Mergelstein: tonig  | Siltstein   | Sandstein |  Hilfern-Formation |  Rupélien     | Rupélien   | UMM  |
|15200359 |Rietbad-Fm. | Sandstein  | Mergelstein   | Konglomerat |  Rietbad-Formation |  Rupélien     | Rupélien   | UMM  |
|15200360 |Jordisboden-Mergel | Mergelstein: Glimmer  | Sandstein   | – |  Jordisboden-Mergel |  Rupélien     | Rupélien   | UMM  |
|15200361 |Goldegg-Sandstein | Sandstein: Glimmer  | Konglomerat: polymikt   | – |  Goldegg-Sandstein |  Rupélien     | Rupélien   | UMM  |
|15203176 |Nolla-Kalkschiefer | Schiefer: sandig-kalkig  | Schiefer: tonig   | – |  Nolla-Kalkschiefer |  Cénomanien     | Cénomanien   | Sedimentbedeckung  |
|15203173 |Stätzerhorn-Fm.: Basaler Konglomerat | Konglomerat: kalkig  | –   | – |  «Hauptkonglomerat» |  Coniacien     | Coniacien   | Flysch  |
|15203174 |Carnusa-Fm. | Sandstein: kalkig: Quarz  | Schiefer: tonig   | Konglomerat |  Carnusa-Formation |  Turonien     | Turonien   | Sedimentbedeckung  |
|15203175 |Nolla-Kalkschiefer: Safien-Kalk | Kalkstein: sandig  | –   | – |  Safien-Kalk |  Turonien     | Turonien   | Sedimentbedeckung  |
|15203177 |Nolla-Tonschiefer | Schiefer: tonig: Bitumen  | Kalkstein: sandig   | – |  Nolla-Tonschiefer |  Albien     | Aptien   | Sedimentbedeckung  |
|15203178 |Bärenhorn-Fm. | Schiefer: sandig-tonig  | Schiefer: kalkig   | Prasinit |  Bärenhorn-Formation |  Barrémien     | Berriasien   | Sedimentbedeckung  |
|15203179 |Tomül-Decke: Grüngesteine | Prasinit  | Basalt   | – |  – |  Später Jura     | Später Jura   | Sedimentbedeckung  |
|15203180 |Tomül-Decke: Mélange | Brekzie  | Quarzit   | Amphibolit |  – |  Mesozoikum     | Mesozoikum   | Mélange  |
|15203181 |Touno-Einheit | Marmor  | Schiefer: tonig   | Schiefer: sandig-kalkig |  – |  Eozän     | Mittlere Trias   | Sedimentbedeckung  |
|15203182 |Barrhorn-Einheit | Schiefer: kalkig  | Marmor   | Dolomitstein |  – |  Eozän     | Mesozoikum   | Sedimentbedeckung  |
|15203183 |Bruneggjoch-Fm. | Quarzit  | Konglomerat: Quarz   | – |  Bruneggjoch-Formation |  Frühe Trias     | Lopingien   | Detritische Trias  |
|15203184 |Bruneggjoch-Fm.: Sous-le-Rocher-Mb. | Quarzit  | Konglomerat: Quarz   | Sandstein: kalkig |  Sous-le-Rocher-Member |  Frühe Trias     | Lopingien   | Detritische Trias  |
|15203185 |Randa-Augengneis | Granit: porphyrisch  | Gneis: augig   | – |  Randa-Augengneis |  Guadalupien     | Cisuralien   | Variszisches Grundgebirge  |
|15203186 |Col-de-Chassoure-Fm. | Schiefer: Quarz-Serizit  | Quarzit   | Gestein: vulkanisch |  Col-de-Chassoure-Formation |  Lopingien     | Cisuralien   | Grundgebirge  |
|15203187 |Col-de-Chassoure-Fm.: Gouille-Verte-Mb. | Schiefer: Quarz-Serizit  | Schiefer: Serizit-Chlorit   | – |  Gouille-Verte-Member |  Lopingien     | Lopingien   | Grundgebirge  |
|15203188 |Col-de-Chassoure-Fm.: Matse-Mb. | Schiefer: Serizit  | Gestein: vulkanisch   | Dolomitstein |  Matse-Member |  Lopingien     | Lopingien   | Grundgebirge  |
|15203189 |Col-de-Chassoure-Fm.: Dent-de-Nendaz-Mb. | Konglomerat: polymikt  | Sandstein   | Schiefer: tonig |  Dent-de-Nendaz-Member |  Lopingien     | Cisuralien   | Grundgebirge  |
|15203190 |Col-de-Chassoure-Fm.: Goli-d&#39;Aget-Mb. | Konglomerat  | Sandstein: Feldspat   | Schiefer: Chlorit |  Goli-d&#39;Aget-Member |  Guadalupien     | Cisuralien   | Grundgebirge  |
|15203191 |Col-de-Chassoure-Fm.: Mondra-Mb. | Schiefer: Quarz-Chlorit  | Schiefer: Anthrazit   | – |  Mondra-Member |  Cisuralien     | Cisuralien   | Grundgebirge  |
|15203192 |Col-de-Chassoure-Fm.: Cleuson-Mb. | Rhyolith  | Konglomerat   | Schiefer: Quarz |  Cleuson-Member |  Cisuralien     | Cisuralien   | Grundgebirge  |
|15203193 |Métailler-Fm. | Gneis: Chlorit  | Schiefer: Chlorit   | Prasinit |  Métailler-Formation |  Frühes Ordovizium     | Kambrium   | Grundgebirge  |
|15203194 |Distulberg-Fm. | Schiefer: Glimmer  | Prasinit: Albit-Chlorit   | Gneis |  Distulberg-Formation |  Kambrium     | Kambrium   | Grundgebirge  |
|15203195 |Thyon-Metagranophyr | Granophyr  | –   | – |  Thyon-Metagranophyr |  Kambrium     | Kambrium   | Grundgebirge  |
|15203196 |Mont-Rogneux-Metagranit | Granit: Biotit  | –   | – |  Mont-Rogneux-Metagranit |  Kambrium     | Kambrium   | Grundgebirge  |
|15203197 |Lirec-Fm. undiff | Gneis: augig  | Gneis: gebändert   | Gestein: vulkanisch |  Lirec-Formation |  Kambrium     | Kambrium   | Grundgebirge  |
|15203198 |Adlerflüe-Fm. | Amphibolit: gebändert  | Gneis   | Schiefer: augig: Glimmer |  Adlerflüe-Formation |  Kambrium     | Proterozoikum   | Grundgebirge  |
|15203199 |Ergischhorn-Komplex | Gneis  | Amphibolit   | – |  Ergischhorn-Komplex |  Proterozoikum     | Proterozoikum   | Grundgebirge  |
|15203200 |Gelbhorn-Flysch | Tonstein: schiefrig  | Marmor: kalkig: Serizit   | – |  Gelbhorn-Flysch |  Eozän     | Kreide   | Flysch  |
|15203201 |Obrist-Fm. | Marmor: kalkig: Serizit  | Quarzit   | Schiefer: tonig |  Obrist-Formation |  Kreide     | Später Jura   | Sedimentbedeckung  |
|15203202 |Vizan-Brekzie | Brekzie: dolomitisch  | Sandstein: Feldspat   | – |  Vizan-Brekzie |  Albien     | Toarcien   | Sedimentbedeckung  |
|15203203 |Tschera-Marmor | Marmor: kalkig  | –   | – |  Tschera-Marmor |  Tithonien     | Oxfordien   | Sedimentbedeckung  |
|15203204 |Tschera-Marmor: Wissberg-Brekzie | Brekzie: kalkig-dolomitisch  | Marmor: kalkig   | – |  Wissberg-Brekzie |  Tithonien     | Oxfordien   | Sedimentbedeckung  |
|15203205 |Nisellas-Fm. | Schiefer: tonig  | Schiefer: sandig-kalkig   | Brekzie: kalkig-dolomitisch |  Nisellas-Formation |  Callovien     | Aalénien   | Sedimentbedeckung  |
|15203206 |Tumpriv-Fm. | Rauwacke  | Evaporit: Gips   | Dolomitstein |  Tumpriv-Formation |  Toarcien     | Carnien   | Sedimentbedeckung  |
|15203207 |Kalkberg-Fm. | Dolomitstein  | Kalkstein   | – |  Kalkberg-Formation |  Ladinien     | Anisien   | Sedimentbedeckung  |
|15203208 |Bavugls-Fm. | Dolomitstein  | Quarzit   | Konglomerat |  Bavugls-Formation |  Mittlere Trias     | Karbon   | Sedimentbedeckung  |
|15203209 |Nolla-Kristallin | Gneis: schiefrig  | –   | – |  – |  Karbon     | Karbon   | Grundgebirge  |
|15203210 |Falknis-Decke: Flysch | Kalkstein: sandig-kieselig  | Sandstein: Quarz   | Tonstein |  – |  Lutétien     | Yprésien   | Flysch  |
|15203211 |Globorotalien-Sch. | Sandstein: kalkig  | Kalkstein: mergelig   | Tonstein: schiefrig |  «Globorotalien-Schichten» |  Thanétien     | Danien   | Sedimentbedeckung  |
|15203212 |Quarzsandstein-Flysch | Sandstein: Quarz-Glaukonit  | Kalkstein: sandig   | Konglomerat: polymikt |  «Quarzsandstein-Flysch» |  Cénomanien     | Aptien   | «Gault»  |
|15203213 |Tristel-Fm. | Kalkstein: sandig  | Brekzie: kalkig-dolomitisch   | Tonstein |  Tristel-Formation |  Aptien     | Barrémien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203214 |Fleckenkalk-Flysch | Kalkstein: mergelig  | Kalkstein: kieselig   | Tonstein: sandig |  «Fleckenkalk-Flysch» |  Barrémien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203215 |Jes-Fm. | Kalkstein: mikritisch: Chert  | Brekzie: kalkig-dolomitisch   | Mergelstein |  Jes-Formation |  Berriasien     | Tithonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203216 |Falknis-Brekzie | Brekzie: polymikt  | Sandstein: kalkig   | Kalkstein: kieselig |  Falknis-Brekzie |  Tithonien     | Kimméridgien   | Post-Rift Mesozoikum in detritischer Fazies  |
|15203217 |Sanalada-Fm. | Mergelstein  | Kalkstein: mergelig   | Kalkstein: arenitisch |  Sanalada-Formation |  Kimméridgien     | Oxfordien   | Post-Rift Mesozoikum in detritischer Fazies  |
|15203218 |Panier-Fm. | Mergelstein: schiefrig  | Tonstein   | Brekzie: polymikt |  Panier-Formation |  Oxfordien     | Toarcien   | Lias-Dogger in neritischer Fazies  |
|15203219 |Sulzfluh-Decke: Flysch | Tonstein: schiefrig  | Sandstein   | Kalkstein: kieselig |  – |  Yprésien     | Thanétien   | Flysch  |
|15203220 |Sulzfluh-Kalk | Kalkstein: mikritisch  | Kalkstein: Ooide   | Kalkstein: arenitisch |  Sulzfluh-Kalk |  Tithonien     | Tithonien   | Malm  |
|15203221 |Sulzfluh-Decke: Granit | Granit  | –   | – |  – |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203222 |Tasna-Decke: Flysch | Tonstein  | Sandstein   | – |  – |  Yprésien     | Yprésien   | Flysch  |
|15203223 |Steinsberg-Kalk | Kalkstein: spätig: Bioklasten  | Kalkstein: sandig: Bioklasten   | – |  Steinsberg-Kalk |  Früher Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15203224 |Plattamala-Granit | Granit  | –   | – |  Plattamala-Granit |  Paläozoikum     | Proterozoikum   | Variszisches Grundgebirge  |
|15203225 |Série Rousse | Marmor: sandig  | Marmor: tonig-schiefrig   | Konglomerat |  «Série-Rousse» |  Späte Kreide     | Cénomanien   | Couches Rouges  |
|15203226 |Série Grise | Schiefer: kalkig  | Marmor   | Prasinit |  «Série Grise» |  Späte Kreide     | Cénomanien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203227 |Garda-Bordon-Fm. | Schiefer: tonig: Bitumen  | Schiefer: kalkig   | – |  Garda-Bordon-Formation |  Späte Kreide     | Frühe Kreide   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203228 |Fêta-d&#39;Août-Fm. | Schiefer: tonig  | Marmor: kalkig   | – |  Fêta-d&#39;Août-Formation |  Späte Kreide     | Frühe Kreide   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203229 |Allalin-Metagabbro | Gabbro  | Gabbro: Omphazit   | – |  Allalin-Gabbro |  Oxfordien     | Bathonien   | Ophiolithische Abfolge  |
|15203230 |Arosa-Decke: Melange | Gestein: pelitisch  | Sandstein: tonig: Lithoklasten   | – |  – |  Paläogen     | Späte Kreide   | Mélange  |
|15203231 |Verspala-Fm. | Sandstein: tonig  | Mergelstein   | – |  Verspala-Formation |  Coniacien     | Cénomanien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203232 |Lavagna-Fm. | Schiefer: kieselig  | –   | – |  Lavagna-Formation |  Albien     | Aptien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203233 |Palombini-Fm. | Schiefer: tonig-kieselig  | Marmor: kalkig-kieselig   | – |  «Palombini-Formation» |  Barrémien     | Tithonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15200365 |UMM-J: Foraminiferenmergel | Mergelstein: sandig: Glimmer  | –   | – |  «Foraminiferenmergel» (UMM-J) |  Rupélien     | Rupélien   | UMM  |
|15200362 |UMM-J | Sandstein: kalkig  | Mergelstein   | Tonstein |  – |  Chattien     | Rupélien   | UMM  |
|15200363 |UMM-J: Septarienton | Tonstein: mergelig: Glimmer  | Sandstein   | – |  «Septarienton» (UMM-J) |  Chattien     | Rupélien   | UMM  |
|15200364 |UMM-J: Fischschiefer | Tonstein: siltig  | Tonstein: mergelig   | – |  «Fischschiefer» (UMM-J) |  Rupélien     | Rupélien   | UMM  |
|15200366 |UMM-J: Meeressand | Sandstein: kalkig: Quarz  | Konglomerat: kalkig   | – |  «Meeressand» (UMM-J) |  Chattien     | Rupélien   | UMM  |
|15200368 |UMM-J: Cyathulabank | Mergelstein  | –   | – |  «Cyathulabank» (UMM-J) |  Rupélien     | Priabonien   | UMM  |
|15200369 |UMM-J: Cyrenenmergel | Mergelstein  | Sandstein: Glimmer   | – |  «Cyrenenmergel» (UMM-J) |  Chattien     | Chattien   | UMM  |
|15200370 |Porrentruy-Konglomerat | Konglomerat: kalkig  | –   | – |  Porrentruy-Konglomerat |  Rupélien     | Priabonien   | USM  |
|15200371 |Rossemaison-Fm.: Süsswasserkalk | Kalkstein  | –   | – |  Rossemaison-Formation |  Rupélien     | Priabonien   | Siderolithikum  |
|15200373 |Ajoie-Gompholit | Brekzie: kalkig  | –   | – |  Ajoie-Gompholit |  Rupélien     | Rupélien   | UMM  |
|15200378 |Tüllingen-Süsswasserkalk | Kalkstein: mikritisch  | Mergelstein   | – |  Tüllingen-Süsswasserkalk |  Spätes Chattien     | Spätes Chattien   | USM  |
|15200380 |Hauptogenstein: Oberer Teil | Kalkstein: Ooide  | Mergelstein   | – |  Hauptrogenstein |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200382 |Hauptogenstein: Unterer Teil | Kalkstein: Ooide  | Mergelstein   | – |  Hauptrogenstein |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200383 |Hauptrogenstein: Calcaire roux marneux | Kalkstein: mergelig: Bioklasten  | –   | – |  «Calcaire roux marneux» (Hauptrogenstein) |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200384 |Bois-de-Raube-Fm.: Ajoie-Mb. | Sandstein  | Mergelstein   | Konglomerat |  Ajoie-Member |  Spätes Miozän     | Spätes Miozän   | OSM  |
|15200385 |Bois-de-Raube-Fm.: Bois-de-Raube-Mb. | Konglomerat  | Sandstein   | Mergelstein |  Bois-de-Raube-Member |  Serravallien     | Serravallien   | OSM  |
|15200386 |Bois-de-Raube-Fm.: Montchaibeux-Mb. | Sandstein  | Mergelstein   | – |  Montchaibeux-Member |  Serravallien     | Serravallien   | OSM  |
|15200387 |Daubrée-Konglomerat | Konglomerat: kalkig-residual: Eisenpisoide  | –   | – |  «Daubrée-Konglomerat» |  Priabonien     | Mittleres Eozän   | Siderolithikum  |
|15200388 |Wanderblock-Bildungen | Gestein: residual  | –   | – |  – |  Pliozän     | Spätes Miozän   | Post-Messinien  |
|15200389 |OMM-II: Geröllsande | Sandstein: konglomeratisch  | –   | – |  – |  Burdigalien     | Burdigalien   | OMM  |
|15200390 |OMM-II: Polymikte Nagelfluh | Konglomerat: polymikt  | –   | – |  – |  Burdigalien     | Burdigalien   | OMM  |
|15200391 |OMM-I: Muschelsandstein | Sandstein: kalkig: Muscheln  | –   | – |  – |  Burdigalien     | Burdigalien   | OMM  |
|15200392 |OMM-I: Graue Molasse | Sandstein: Glimmer  | Sandstein: kalkig: Muscheln   | – |  – |  Burdigalien     | Burdigalien   | OMM  |
|15200393 |Daubrée-Konglomerat: Süsswasserkalk | Kalkstein: Eisenooide  | –   | – |  «Daubrée-Konglomerat» |  Mittleres Eozän     | Mittleres Eozän   | Siderolithikum  |
|15200394 |USM: Basale Süsswassermolasse | Kalkstein  | Gestein: residual: Eisenmineralien   | – |  – |  Rupélien     | Priabonien   | USM  |
|15200395 |Laufen-Juranagelfluh | Konglomerat: kalkig  | –   | – |  Laufen-Juranagelfluh |  Tortonien     | Langhien   | OSM  |
|15200396 |Basler Juranagelfluh | Konglomerat: kalkig  | Sandstein   | Mergelstein |  Basler Juranagelfluh |  Langhien     | Langhien   | OSM  |
|15200397 |Aargauer Juranagelfluh | Konglomerat: kalkig  | –   | – |  Aargauer Juranagelfluh |  Tortonien     | Langhien   | OSM  |
|15200399 |Jensberg-Fm. | Sandstein: Glaukonit  | Mergelstein   | – |  Jensberg-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200400 |Jensberg-Fm.: Rebhubel-Sch. | Sandstein: mergelig: Glimmer  | Sandstein: konglomeratisch   | Konglomerat |  Rebhubel-Schichten |  Spätes Burdigalien     | Spätes Burdigalien   | OMM  |
|15200401 |Niedermatt-Fm. | Sandstein  | Konglomerat: polymikt   | – |  Niedermatt-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200402 |Belpberg-Fm. | Sandstein  | Mergelstein   | Konglomerat |  Belpberg-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200403 |Kalchstätten-Fm.: Pfadflüe-Nagelfluh | Konglomerat: kalkig  | Mergelstein   | Sandstein |  Pfadflüe-Member |  Burdigalien     | Burdigalien   | Molasse  |
|15200404 |Belpberg-Fm.: Sädel-Kalknagelfluh | Konglomerat: kalkig  | –   | – |  Sädel-Kalknagelfluh |  Burdigalien     | Burdigalien   | OMM  |
|15200405 |Belpberg-Fm.: Utzigen-Muschelsandstein | Sandstein: kalkig: Muscheln  | –   | – |  Utzigen-Muschelsandstein |  Burdigalien     | Burdigalien   | OMM  |
|15200406 |Belpberg-Fm.: Ulmiz-Quarzitnagelfluh | Konglomerat: Quarz  | –   | – |  Ulmiz-Quarzitnagelfluh |  Burdigalien     | Burdigalien   | OMM  |
|15200407 |Belpberg-Fm.: Bütschelbach-Nagelfluh | Konglomerat  | –   | – |  Bütschelbach-Nagelfluh |  Burdigalien     | Burdigalien   | OMM  |
|15200408 |Kalchstätten-Fm. | Konglomerat: kalkig  | Sandstein   | Mergelstein |  Kalchstätten-Formation |  Langhien     | Burdigalien   | Molasse  |
|15200409 |St.-Gallen-Fm.: Freudenberg-Nagelfluh | Konglomerat: kalkig  | –   | – |  Freudenberg-Nagelfluh |  Burdigalien     | Burdigalien   | OMM  |
|15200410 |St.-Gallen-Fm.: Goldbrunnen-Sch. | Mergelstein  | Sandstein   | – |  Goldbrunnen-Schichten |  Burdigalien     | Burdigalien   | OMM  |
|15200411 |St.-Gallen-Fm.: Dreilinden-Nagelfluh | Konglomerat  | –   | – |  Dreilinden-Nagelfluh |  Burdigalien     | Burdigalien   | OMM  |
|15200412 |St.-Gallen-Fm.: Obere Grenznagelfluh | Konglomerat  | –   | – |  «Obere Grenznagelfluh» |  Burdigalien     | Burdigalien   | OMM  |
|15200413 |Kirchberg-Fm. | Tonstein  | Mergelstein   | – |  Kirchberg-Formation |  Spätes Burdigalien     | Spätes Burdigalien   | Molasse  |
|15200414 |Grimmelfingen-Fm. | Tonstein  | Mergelstein   | Sandstein |  Grimmelfingen-Formation |  Spätes Burdigalien     | Spätes Burdigalien   | Molasse  |
|15200415 |Chnebelburg-Fm. | Sandstein: Glaukonit  | Sandstein: kalkig: Muscheln   | Mergelstein |  Chnebelburg-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200416 |Chnebelburg-Fm.: Meinisberg-Muschelsandstein | Sandstein: kalkig: Muscheln  | –   | – |  Meinisberg-Muschelsandstein |  Burdigalien     | Burdigalien   | OMM  |
|15200417 |Chnebelburg-Fm.: Brüttelen-Grobsandstein | Sandstein: konglomeratisch-kalkig: Muscheln  | –   | – |  Brüttelen-Grobsandstein |  Burdigalien     | Burdigalien   | OMM  |
|15200418 |Sense-Fm. | Sandstein: Glaukonit  | Siltstein   | Mergelstein |  Sense-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200419 |Sense-Fm.: Montécu-Sch. | Mergelstein: siltig  | –   | – |  Montécu-Schichten |  Burdigalien     | Burdigalien   | OMM  |
|15200420 |Sense-Fm.: Molière-Muschelsandstein | Sandstein: kalkig: Muscheln  | –   | – |  Molière-Muschelsandstein |  Burdigalien     | Burdigalien   | OMM  |
|15200421 |Sense-Fm.: Scherli-Nagelfluh | Konglomerat: Quarz  | –   | – |  Scherli-Quarzitnagelfluh |  Burdigalien     | Burdigalien   | OMM  |
|15200422 |Grilly-Süsswasserkalk | Kalkstein  | –   | – |  Grilly-Süsswasserkalk |  Rupélien     | Rupélien   | USM  |
|15200423 |Orbe-Süsswasserkalk | Kalkstein: Bitumen-Bioklasten  | –   | – |  Orbe-Süsswasserkalk |  Rupélien     | Priabonien   | USM  |
|15200424 |USM: Basale Süsswassermolasse: Krustenkalk | Kalkstein: pedogen-verkrustet  | –   | – |  – |  Rupélien     | Priabonien   | USM  |
|15200425 |Gümmenen-Fm. | Sandstein  | Mergelstein: siltig   | – |  Gümmenen-Formation |  Aquitanien     | Spätes Chattien   | USM  |
|15200429 |USM-II: Obere Bunte Molasse | Mergelstein: siltig  | Sandstein   | Sandstein: kalkig |  «Obere Bunte Molasse» (USM-II) |  Aquitanien     | Aquitanien   | USM  |
|15200430 |Oberdorf-Süsswasserkalk | Kalkstein: kreidig  | Mergelstein   | – |  Oberdorf-Süsswasserkalk |  Rupélien     | Rupélien   | Siderolithikum  |
|15200431 |St.-Gallen-Fm.: Limnischer Horizont | Mergelstein: siltig  | Kalkstein   | – |  St.-Gallen-Formation |  Spätes Burdigalien     | Spätes Burdigalien   | OMM  |
|15200432 |OMM-II: Quarzitnagelfluh | Konglomerat: Quarz  | Konglomerat: kalkig: Muscheln   | – |  – |  Burdigalien     | Burdigalien   | OMM  |
|15200433 |Luzern-Fm.: Basales Konglomerat | Konglomerat: polymikt  | –   | – |  Luzern-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200436 |Perte-du-Rhône-Fm.: Poncin-Mb. | Sandstein: Glimmer-Glaukonit  | –   | – |  Poncin-Member |  Cénomanien     | Cénomanien   | «Gault»  |
|15200437 |Perte-du-Rhône-Fm.: Mussel-Mb.: Vraconne-Sandstein | Sandstein: Glaukonit  | Mergelstein: sandig   | – |  Vraconne-Sandstein |  Albien     | Albien   | «Gault»  |
|15203238 |Coulaytes-Melange: Buufal-Konglomerat | Konglomerat: dolomitisch  | –   | – |  Buufal-Konglomerat |  Priabonien     | Mittleres Eozän   | Mélange  |
|15203234 |Arosa-Decke: Calpionellenkalk | Kalkstein: mikritisch: Aptychen  | –   | – |  – |  Tithonien     | Tithonien   | Maiolica / Aptychenkalk  |
|15203235 |Arosa-Decke: Radiolarit | Gestein: kieselig: Radiolarien  | Schiefer: kieselig   | – |  – |  Kimméridgien     | Oxfordien   | Radiolarit  |
|15203236 |Arosa-Decke: Ophiolith | Serpentinit  | Gabbro   | Basalt |  – |  Oxfordien     | Bathonien   | Ophiolithische Abfolge  |
|15203239 |Sommant-Fm.: Langel-Mb. | Kalkstein: Ooide  | Kalkstein: Onkoide   | – |  Langel-Member |  Bathonien     | Bajocien   | Syn-Rift  |
|15203240 |Pralet-Fm.: Obere Rauwacke | Rauwacke  | –   | – |  «Obere Rauhwacke» (Pralet-Fm.) |  Carnien     | Carnien   | Raibl  |
|15203241 |Clôt-la-Cime-Fm.: Gips | Evaporit: Gips  | –   | – |  Clôt-la-Cime-Formation |  Trias     | Trias   | Raibl  |
|15203242 |Brekzien-Decke: Couches-Rouges | Kalkstein: tonig  | Brekzie   | – |  – |  Thanétien     | Campanien   | Couches Rouges  |
|15203243 |Brekzien-Decke: Trias: Rauwacke | Rauwacke  | –   | – |  – |  Trias     | Trias   | Prä-Rift  |
|15203244 |Manche-Fm.: Lamperehubel-Sandstein | Sandstein: kalkig  | –   | – |  Lamperehubel-Sandstein |  Albien     | Albien   | Flysch  |
|15203245 |Perrières-Fm.: Gets-Ophiolith | Serpentinit  | Gabbro   | Basalt |  Gets-Ophiolith |  Bathonien     | Bathonien   | Ophiolithische Abfolge  |
|15203246 |Piz-Terri-Lunschania: Obere Kalk- und Tonschiefer | Schiefer: kalkig: Glimmer  | Schiefer: tonig   | – |  – |  Mittlerer Jura     | Mittlerer Jura   | Sedimentbedeckung  |
|15203247 |Piz-Terri-Lunschania: Gneisquarzit | Quarzit: kalkig  | Schiefer: kalkig: Glimmer   | – |  – |  Mittlerer Jura     | Mittlerer Jura   | Sedimentbedeckung  |
|15203248 |Piz-Terri-Lunschania: Untere Kalk- und Tonschiefer | Schiefer: tonig  | Schiefer: kalkig   | Schiefer: sandig |  – |  Früher Jura     | Früher Jura   | Sedimentbedeckung  |
|15203249 |Aul-Marmor | Marmor  | –   | – |  Aul-Marmor |  Tithonien     | Oxfordien   | Sedimentbedeckung  |
|15203250 |Piz-Terri-Lunschania: Dolomitbrekzie | Brekzie: dolomitisch  | –   | – |  – |  Früher Jura     | Früher Jura   | Sedimentbedeckung  |
|15203251 |Grava-Decke: Gryphäenkalk | Kalkstein: sandig: Bioklasten  | –   | – |  – |  Pliensbachien     | Sinémurien   | Lias-Dogger in neritischer Fazies  |
|15203252 |Unterpenninikum: Trias | Quarzit  | Marmor: dolomitisch   | Sandstein: Feldspat |  – |  Trias     | Trias   | Prä-Rift  |
|15203253 |Zervreila-Granitgneis | Gneis: granitisch-augig  | –   | – |  Zervreila-Orthogneis |  Cisuralien     | Cisuralien   | Grundgebirge  |
|15203254 |Garenstock-Augengneis | Gneis: augig  | –   | – |  Garenstock-Augengneis |  Ordovizium     | Ordovizium   | Grundgebirge  |
|15203255 |Salahorn-Fm.: Glimmerschiefer und Paragneis | Schiefer: Glimmer  | Gneis   | – |  Salahorn-Formation |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203256 |Adula-Decke: Amphibolit | Amphibolit  | –   | – |  – |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203257 |Zone Submédiane: Melange | Evaporit: Gips  | Tonstein   | – |  – |  Paläogen     | Späte Kreide   | Mélange  |
|15203258 |Zone Submédiane: Truche-Brekzie | Brekzie: polymikt  | –   | – |  Truche-Brekzie |  Eozän     | Eozän   | Mélange  |
|15203259 |Zone Submédiane: Trom-Brekzie | Brekzie: polymikt  | Kalkstein: mikritisch   | – |  Trom-Brekzie |  Tertiär     | Späte Kreide   | Mélange  |
|15203260 |Zone Submédiane: Exergillod-Brekzie | Brekzie  | Brekzie: kalkig: Bioklasten   | – |  Exergillod-Brekzie |  Später Jura     | Früher Jura   | Mélange  |
|15203261 |Zone Submédiane: Troublon-Kalk | Kalkstein: mikritisch: Bioklasten  | Sandstein: mergelig   | – |  Troublon-Kalk |  Später Jura     | Später Jura   | Mélange  |
|15203262 |Zone Submédiane: Zünegg-Knollenkalk | Kalkstein: mergelig  | –   | – |  Zünegg-Knollenkalk |  Später Jura     | Später Jura   | Mélange  |
|15203263 |Zone Submédiane: Hauta-Crêtaz-Fm. | Kalkstein: spätig: Bioklasten  | Brekzie: kalkig   | – |  Hauta-Crêtaz-Formation |  Später Jura     | Früher Jura   | Mélange  |
|15203264 |Zone Submédiane: Pointe-de-l&#39;Au-Brekzie | Brekzie: kalkig  | –   | – |  Pointe-de-l&#39;Au-Brekzie |  Bathonien     | Bathonien   | Mélange  |
|15203265 |Zone Submédiane: Bonaveau-Kalk | Kalkstein: sandig  | Kalkstein: sandig   | – |  Bonaveau-Kalk |  Toarcien     | Toarcien   | Mélange  |
|15203266 |Zone Submédiane: Sex-du-Tronc-Kalk | Kalkstein: spätig: Bioklasten  | –   | – |  Sex-du-Tronc-Kalk |  Sinémurien     | Sinémurien   | Mélange  |
|15203267 |Zone Submédiane: Grand-Herba-Kalk | Kalkstein  | –   | – |  Grand-Herba-Kalk |  Sinémurien     | Sinémurien   | Mélange  |
|15203268 |Oudiou-Fm. | Kalkstein: Bioklasten  | Kalkstein: kieselig-spätig   | – |  Oudiou-Formation |  Aalénien     | Rhät   | Syn-Rift  |
|15203269 |Klippen-Decke: Malm | Kalkstein  | Mergelstein   | – |  – |  Berriasien     | Oxfordien   | Malm  |
|15203270 |Moléson-Fm.: Albeuve-Serie | Mergelstein: Glaukonit-Bioklasten  | –   | – |  Albeuve-Serie |  Kimméridgien     | Kimméridgien   | Malm  |
|15203271 |Sciernes-d&#39;Albeuve-Fm.: Kummli-Sch. | Kalkstein: mikritisch  | –   | – |  Kummli-Schichten |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203272 |Klippen-Decke: Dogger | Kalkstein  | Mergelstein   | – |  – |  Callovien     | Bajocien   | Syn-Rift  |
|15203273 |Mytilus-Sch.: Col-de-Cordon-Mb.: Stockenflue-Kalk | Kalkstein: sandig: Bioklasten  | –   | – |  Stockenflue-Kalk |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15203274 |Sommant-Fm.: Mieussy-Mb. | Kalkstein: arenitisch  | Kalkstein: Bioklasten   | Kalkstein: mikritisch |  Mieussy-Member |  Bathonien     | Bajocien   | Syn-Rift  |
|15203275 |Klippen-Decke: Lias | Mergelstein  | Kalkstein: spätig   | Kalkstein: kieselig |  – |  Bajocien     | Rhät   | Syn-Rift  |
|15203276 |Klippen-Decke: Trias | Dolomitstein  | Kalkstein: Bioklasten   | Gestein: pelitisch |  – |  Ladinien     | Olénékien   | Prä-Rift  |
|15203277 |Pralet-Fm. | Dolomitstein  | Kalkstein: spätig: Bioklasten   | Tonstein |  Pralet-Formation |  Ladinien     | Ladinien   | Raibl  |
|15203278 |Pralet-Fm.: Balmi-Mb. | Dolomitstein  | Kalkstein: arenitisch   | Kalkstein: spätig: Echinodermen |  Balmi-Member |  Ladinien     | Ladinien   | Raibl  |
|15203279 |Wiriehorn-Fm.: Bodeflue-Mb. | Dolomitstein  | –   | – |  Bodeflue-Member |  Anisien     | Anisien   | Karbonatische Trias  |
|15203280 |Wiriehorn-Fm.: Wildgrimmi-Mb. | Kalkstein  | Dolomitstein   | – |  Wildgrimmi-Member |  Anisien     | Anisien   | Karbonatische Trias  |
|15203281 |St-Triphon-Fm.: Dorchaux-Mb.: Untere Rauwacke | Rauwacke  | –   | – |  «Untere Rauhwacke» (St-Triphon-Fm.) |  Anisien     | Frühe Trias   | Karbonatische Trias  |
|15203282 |Infrabrèche-Melange | Gestein: pelitisch  | Brekzie   | – |  «Infrabrèche-Melange» |  Paläogen     | Späte Kreide   | Mélange  |
|15203283 |Wägital-Decke: Flysch | Sandstein  | Brekzie: polymikt   | Tonstein |  Wägital-Flysch |  Yprésien     | Campanien   | Flysch  |
|15203284 |Gurnigel-Decke: Flysch-5 | Konglomerat  | Sandstein: kieselig   | – |  «Flysch 5, mit kieseligen Mikrokonglomeraten» |  Lutétien     | Lutétien   | Flysch  |
|15203285 |Voirons-Decke: Flysch | Sandstein  | Konglomerat   | Mergelstein |  – |  Rupélien     | Mittleres Eozän   | Flysch  |
|15203286 |Boëge-Mergel | Mergelstein  | Sandstein   | – |  Boëge-Mergel |  Rupélien     | Priabonien   | Flysch  |
|15203287 |Vouan-Konglomerat | Konglomerat  | Sandstein   | Mergelstein |  Vouan-Konglomerat |  Rupélien     | Priabonien   | Flysch  |
|15203288 |Voirons-Sandstein | Sandstein  | Mergelstein   | – |  Voirons-Sandstein |  Priabonien     | Mittleres Eozän   | Flysch  |
|15203291 |Klippen-Decke: Couches-Rouges | Kalkstein: mergelig  | Kalkstein: mikritisch   | Mergelstein |  – |  Yprésien     | Turonien   | Couches Rouges  |
|15203292 |Simmen-Decke: Flysch | Sandstein  | Gestein: pelitisch   | Konglomerat |  – |  Santonien     | Albien   | Flysch  |
|15203293 |Trepsen-Flysch | Brekzie: polymikt  | Sandstein   | Tonstein |  Trepsen-Flysch |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203294 |Cocco-Gneis | Gneis: granodioritisch  | –   | – |  Cocco-Gneis |  Pennsylvanien     | Pennsylvanien   | Variszisches Grundgebirge  |
|15203295 |Verzasca-Gneis | Gneis: Biotit-Muskovit  | –   | – |  Verzasca-Gneis |  Cisuralien     | Pennsylvanien   | Grundgebirge  |
|15203296 |Vogorno-Gneis | Gneis: Biotit-Muskovit  | –   | – |  Vogorno-Gneis |  Cisuralien     | Pennsylvanien   | Grundgebirge  |
|15203297 |Ruscada-Gneis | Gneis  | –   | – |  Ruscada-Gneis |  Paläozoikum     | Paläozoikum   | Variszisches Grundgebirge  |
|15203298 |Mergoscia-Gneis | Gneis: Biotit  | Gneis: migmatitisch   | – |  Mergoscia-Gneis |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203299 |Monte-Rosa-Orthogneis | Gneis: granodioritisch  | Granodiorit   | – |  Monte-Rosa-Orthogneis  |  Karbon     | Karbon   | Grundgebirge  |
|15200441 |Perte-du-Rhône-Fm.: Mussel-Mb.: Scie-Besse-Sandstein | Sandstein: Glaukonit  | –   | – |  Scie-Besse-Sandstein |  Aptien     | Aptien   | «Gault»  |
|15200438 |Perte-du-Rhône-Fm.: Mussel-Mb.: La-Presta-Mergel | Tonstein: sandig  | –   | – |  La-Presta-Mergel |  Albien     | Albien   | «Gault»  |
|15200439 |Perte-du-Rhône-Fm.: Mussel-Mb.: Vernettes-Sandstein | Sandstein: Glaukonit  | –   | – |  Vernettes-Sandstein |  Albien     | Albien   | «Gault»  |
|15200440 |Perte-du-Rhône-Fm.: Mussel-Mb.: Ponthoud-Bk. | Kalkstein: Bioklasten  | –   | – |  Ponthoud-Bank |  Aptien     | Aptien   | «Gault»  |
|15200442 |Perte-du-Rhône-Fm.: Fulie-Mb.: Mortier-Mergel | Mergelstein  | –   | – |  Mortier-Mergel |  Aptien     | Aptien   | «Gault»  |
|15200443 |Perte-du-Rhône-Fm.: Fulie-Mb.: Vauglène-Bk. | Mergelstein: kalkig  | –   | – |  Vauglène-Bänke |  Aptien     | Aptien   | «Gault»  |
|15200444 |Perte-du-Rhône-Fm.: Fulie-Mb.: Poet-Bk. | Kalkstein: mergelig: Bioklasten  | –   | – |  Poet-Bank |  Aptien     | Aptien   | «Gault»  |
|15200445 |Rossemaison-Fm.: Courcelon-Süsswasserkalk | Kalkstein  | –   | – |  Courcelon-Süsswasserkalk |  Rupélien     | Priabonien   | Siderolithikum  |
|15200446 |Erzmatt-Krustenkalk | Kalkstein: Limonit  | –   | – |  Erzmatt-Krustenkalk |  Rupélien     | Priabonien   | Siderolithikum  |
|15200447 |Diegten-Süsswasserkalk | Kalkstein: Bioklasten  | –   | – |  Diegten-Süsswasserkalk |  Rupélien     | Mittleres Eozän   | Siderolithikum  |
|15200448 |La-Verrerie-Süsswasserkalk | Kalkstein: kreidig  | Mergelstein   | – |  La-Verrerie-Süsswasserkalk |  Rupélien     | Priabonien   | Siderolithikum  |
|15200449 |La-Charrue-Süsswasserkalk | Kalkstein  | Mergelstein   | – |  La-Charrue-Süsswasserkalk |  Rupélien     | Priabonien   | Siderolithikum  |
|15200450 |Vuache-Fm.: Astieria-Mergel | Mergelstein: Bioklasten  | –   | – |  «Astieria-Mergel» |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200451 |Vuache-Fm.: Villers-Sch. | Mergelstein  | –   | – |  Villers-Schichten |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200452 |Pierre-Châtel-Fm.: Unité Moyenne Calcaire | Kalkstein: mikritisch  | –   | – |  «Unité Moyenne Calcaire» |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200453 |Pierre-Châtel-Fm.: Unité Inférieure Oolithique | Kalkstein: Bioklasten-Ooide  | Mergelstein   | – |  «Unité Inférieure Oolithique» |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200456 |Etiollets-Fm.: Complexe récifal: Landaize-Kalk | Kalkstein: Bioklasten  | –   | – |  Landaize-Kalk |  Kimméridgien     | Kimméridgien   | Malm  |
|15200457 |Balsthal-Fm.: Holzflue-Mb.: Balmberg-Oolith | Kalkstein: Ooide  | –   | – |  Balmberg-Oolith |  Kimméridgien     | Oxfordien   | Malm  |
|15200458 |Balsthal-Fm.: Laufen-Mb.: Hautes-Roches-Algenkalk | Kalkstein: mikritisch: Onkoide  | Kalkstein: dolomitisch   | – |  Hautes-Roches-Algenkalk |  Oxfordien     | Oxfordien   | Malm  |
|15200459 |Balsthal-Fm.: Laufen-Mb.: Akzessorische Mumienbänke | Kalkstein: Onkoide  | –   | – |  Akzessorische Mumienbänke |  Oxfordien     | Oxfordien   | Malm  |
|15200460 |Vellerat-Fm.: Röschenz-Mb.: Brauner Oolith | Kalkstein: Ooide  | –   | – |  «Brauner Oolith» |  Oxfordien     | Oxfordien   | Malm  |
|15200461 |Kaiseraugst-Fm.: Wellendolomit: Bleiglanz-Bk. | Dolomitstein  | –   | – |  «Bleiglanzbank» (Kaiseraugst-Fm.) |  Anisien     | Anisien   | Muschelkalk  |
|15200462 |Dinkelberg-Fm.: Rötton: Arenicolites-Bk. | Kalkstein  | –   | – |  «Arenicolites-Bank» |  Anisien     | Anisien   | Buntsandstein  |
|15200463 |Dinkelberg-Fm.: Diagonalschichtiger Sandstein | Sandstein: tonig: Glimmer  | –   | – |  «Diagonalschichtiger Sandstein» (Dinkelberg-Fm.) |  Olénékien     | Olénékien   | Buntsandstein  |
|15200464 |Schinznach-Fm.: Leutschenberg-Mb. | Kalkstein: dolomitisch  | Kalkstein: Bioklasten   | – |  Leutschenberg-Member |  Anisien     | Anisien   | Muschelkalk  |
|15200465 |Schlächtenhaus-Granit | Granit: Biotit-Muskovit  | –   | – |  Schlächtenhaus-Granit |  Mississippien     | Frühes Devon   | Frühvariszisches Grundgebirge  |
|15200466 |Steinatal-Gneiskomplex | Gneis: migmatitisch  | Amphibolit   | – |  Steinatal-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15200467 |Schinznach-Fm.: Asp-Mb.: Grenzdolomit | Dolomitstein  | –   | – |  «Grenzdolomit» (Schinznach-Fm.) |  Ladinien     | Ladinien   | Muschelkalk  |
|15200468 |Schinznach-Fm.: Asp-Mb.: Estherien-Sch. | Mergelstein: Bitumen  | –   | – |  «Estherien-Schichten» |  Ladinien     | Ladinien   | Muschelkalk  |
|15200469 |Hangende-Bankkalke-Fm. | Kalkstein: mikritisch  | –   | – |  Hangende-Bankkalke-Formation |  Tithonien     | Tithonien   | Malm  |
|15200470 |Zementmergel-Fm. | Mergelstein  | Kalkstein   | – |  Zementmergel-Formation |  Tithonien     | Kimméridgien   | Malm  |
|15200471 |Liegende-Bankkalke-Fm. | Kalkstein: Bioklasten  | Mergelstein   | – |  Liegende-Bankkalke-Formation |  Kimméridgien     | Kimméridgien   | Malm  |
|15200472 |Obere-Felsenkalke-Fm. | Kalkstein: mikritisch  | –   | – |  Obere-Felsenkalke-Formation |  Kimméridgien     | Kimméridgien   | Malm  |
|15200473 |Untere-Felsenkalke-Fm. | Kalkstein  | Mergelstein   | – |  Untere-Felsenkalke-Formation |  Kimméridgien     | Kimméridgien   | Malm  |
|15200474 |Lacunosamergel-Fm. | Mergelstein  | Kalkstein: mergelig   | – |  Lacunosamergel-Formation |  Kimméridgien     | Kimméridgien   | Malm  |
|15200475 |Oberjura-Massenkalk-Fm. | Kalkstein: Schwämme  | –   | – |  Oberjura-Massenkalk-Formation |  Tithonien     | Kimméridgien   | Malm  |
|15200476 |Oberjura-Massenkalk-Fm.: Lochen-Sbf. | Kalkstein: Schwämme  | –   | – |  Lochen-Subformation |  Kimméridgien     | Oxfordien   | Malm  |
|15200477 |Wohlgeschichtete-Kalke-Fm. | Kalkstein: mikritisch  | –   | – |  Wohlgeschichtete-Kalke-Formation |  Kimméridgien     | Oxfordien   | Malm  |
|15200478 |Impressamergel-Fm. | Mergelstein: tonig  | Kalkstein: mergelig   | – |  Impressamergel-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15200479 |Ornatenton-Fm. | Tonstein  | Mergelstein: tonig   | Kalkstein: Eisenooide |  Ornatenton-Formation |  Oxfordien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200480 |Ornatenton-Fm.: Glaukonitsandmergel-Sbf. | Mergelstein: sandig-tonig: Glaukonit  | –   | – |  Glaukonitsandmergel-Subformation |  Oxfordien     | Oxfordien   | Lias-Dogger in neritischer Fazies  |
|15200481 |Ornatenton-Fm.: Glaukonitsandmergel-Sbf.: Grenzkalk | Mergelstein: kalkig: Ooide  | –   | – |  Grenzkalk |  Callovien     | Callovien   | Lias-Dogger in neritischer Fazies  |
|15200482 |Ornatenton-Fm.: Macrocephalenoolith-Sbf. | Tonstein: Eisenooide  | –   | – |  Macrocephalenoolith-Subformation |  Callovien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200483 |Wutach-Fm. | Mergelstein: kalkig: Eisenooide  | –   | – |  Wutach-Formation |  Callovien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200484 |Variansmergel-Fm. | Mergelstein  | Kalkstein   | – |  Variansmergel-Formation |  Bathonien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200485 |Dentalienton-Fm. | Mergelstein: tonig  | –   | – |  Dentalienton-Formation |  Bathonien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15200486 |Hamitenton-Fm. | Mergelstein: tonig  | –   | – |  Hamitenton-Formation |  Bathonien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200487 |Hamitenton-Fm.: Parkinsonioolith-Sbf. | Kalkstein: Eisenooide  | Mergelstein: tonig   | – |  Parkinsonioolith-Subformation |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200488 |Gosheim-Fm. | Kalkstein: Eisenooide  | Mergelstein   | – |  Gosheim-Formation |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200489 |Gosheim-Fm.: Blagdeni-Sbf. | Mergelstein  | Kalkstein   | – |  Blagdeni-Subformation |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200490 |Gosheim-Fm.: Humphriesioolith-Sbf. | Mergelstein: Eisenooide  | –   | – |  Humphriesioolith-Subformation |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200491 |Wedelsandstein-Fm. | Mergelstein  | Kalkstein   | – |  Wedelsandstein-Formation |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200492 |Wedelsandstein-Fm.: Blaukalk-Sbf. | Kalkstein  | Mergelstein   | – |  Blaukalk-Subformation |  Bajocien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15200493 |Murchisonaeoolith-Fm. | Kalkstein: sandig  | Sandstein: kalkig   | Sandstein: Eisenooide |  Murchisonaeoolith-Formation |  Aalénien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15200494 |Achdorf-Fm. | Tonstein: sandig: Glimmer  | Kalkstein: Ooide   | Kalkstein: Bioklasten |  Achdorf-Formation |  Aalénien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15200495 |Tannenwald-Sch. | Konglomerat  | Sandstein   | – |  Tannenwald-Schichten |  Serravallien     | Serravallien   | Molasse  |
|15200496 |Schüpferegg-Nagelfluh: Gabelspitz-Sch. | Konglomerat: polymikt: Quarz  | Sandstein   | Mergelstein |  Gabelspitz-Schichten |  Burdigalien     | Burdigalien   | Molasse  |
|15200497 |Schüpferegg-Nagelfluh: Schallenberg-Mergel | Mergelstein  | Sandstein   | Konglomerat: polymikt |  Schallenberg-Member |  Burdigalien     | Burdigalien   | Molasse  |
|15200498 |Schüpferegg-Nagelfluh: Seli-Nagelfluh | Konglomerat: polymikt: Quarz  | –   | – |  Seli-Nagelfluh |  Burdigalien     | Burdigalien   | Molasse  |
|15200499 |Brand-Herrentisch-Tuffit | Tuffit  | –   | – |  Brand-Herrentisch-Tuffit |  Tortonien     | Langhien   | Hegau-Vulkanismus  |
|15200500 |Wangen-Tuffit | Tuffit  | –   | – |  Wangen-Tuffit |  Serravallien     | Langhien   | Hegau-Vulkanismus  |
|15200501 |Hohenolber-Tuffit | Tuffit  | –   | – |  Hohenolber-Tuffit |  Serravallien     | Serravallien   | Hegau-Vulkanismus  |
|15200502 |Eichbol-Tuffit | Tuffit  | –   | – |  Eichbol-Tuffit |  Langhien     | Langhien   | Hegau-Vulkanismus  |
|15203303 |Spegnas-Fm. | Sandstein  | Schiefer   | Kalkstein: sandig |  Spegnas-Formation |  Paleozän     | Paleozän   | Sedimentbedeckung  |
|15203300 |Arblatsch-Flysch | Sandstein  | Schiefer: tonig-kalkig   | Konglomerat |  Arblatsch-Flysch |  Yprésien     | Maastrichtien   | Flysch  |
|15203301 |Arblatsch-Flysch: Sandstein-dominierte Fazies | Sandstein  | –   | – |  Arblatsch-Flysch |  Yprésien     | Yprésien   | Flysch  |
|15203302 |Arblatsch-Flysch: Konglomerat-dominierte Fazies | Konglomerat  | –   | – |  Arblatsch-Flysch |  Yprésien     | Yprésien   | Flysch  |
|15203304 |Rudnal-Fm. | Kalkstein: mergelig  | Tonstein: schiefrig   | Sandstein |  Rudnal-Formation |  Maastrichtien     | Maastrichtien   | Sedimentbedeckung  |
|15203305 |Savognin-Fm. | Rauwacke  | Evaporit: Gips   | Brekzie |  Savognin-Formation |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15203306 |Stätzerhorn-Fm.: Bleis-Pintgas-Mb. | Kalkstein: sandig  | Schiefer: tonig   | – |  Bleis-Pintgas-Member |  Maastrichtien     | Santonien   | Flysch  |
|15203307 |Stätzerhorn-Fm.: Parnegl-Mb. | Kalkstein: sandig  | Schiefer: tonig   | – |  Parnegl-Member |  Maastrichtien     | Santonien   | Flysch  |
|15203308 |Stätzerhorn-Fm.: Danis-Mb. | Kalkstein: sandig  | –   | – |  Danis-Member |  Maastrichtien     | Santonien   | Flysch  |
|15203309 |Stätzerhorn-Fm.: Raschil-Mb. | Kalkstein: sandig  | Schiefer: tonig   | – |  Raschil-Member |  Maastrichtien     | Santonien   | Flysch  |
|15203310 |Bruneggjoch-Fm.: Embd-Mb. | Quarzit  | Konglomerat: Quarz   | – |  Embd-Member |  Lopingien     | Lopingien   | Detritische Trias  |
|15203311 |Randa-Augengneis: Bonigersee-Augengneis | Granit: porphyrisch  | Gneis: augig   | – |  Bonigersee-Augengneis |  Ordovizium     | Ordovizium   | Variszisches Grundgebirge  |
|15203312 |Törbel-Gneis | Gneis  | –   | – |  Törbel-Gneis |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203313 |Lodano-Gneis | Gneis: gebändert  | –   | – |  Lodano-Gneis |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203314 |Vergeletto-Gneis | Gneis  | –   | – |  Vergeletto-Gneis |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203315 |Cortascia-Gneis | Gneis: Biotit-Muskovit  | –   | – |  Cortascia-Gneis |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203316 |Forcoletta-Gneis | Gneis: Biotit-Muskovit  | –   | – |  Forcoletta-Gneis |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203317 |Matorello-Gneis | Gneis  | Granodiorit   | – |  Matorello-Gneis |  Asselien     | Spätes Pennsylvanien   | Variszisches Grundgebirge  |
|15203318 |Lebendun-Komplex | Gneis: psephitisch  | Marmor   | Schiefer: Glimmer |  Lebendun-Komplex |  Mesozoikum     | Paläozoikum   | Grundgebirge  |
|15203319 |Sabbione-Sandstein | Sandstein  | Gestein: vulkanisch   | – |  Sabbione-Sandstein |  Bathonien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15203320 |Monte-Leone-Decke: Grundgebirge | Gneis: augig  | Gneis   | – |  – |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203321 |Ganter-Gneis | Gneis: augig  | –   | – |  Ganter-Gneis |  Paläozoikum     | Paläozoikum   | Variszisches Grundgebirge  |
|15203322 |Ritter-Gneis | Gneis  | –   | – |  Ritter-Gneis |  Paläozoikum     | Paläozoikum   | Variszisches Grundgebirge  |
|15203323 |Geisspfad-Serpentinit | Serpentinit  | Peridotit   | Granofels: Pyroxen |  Geisspfad-Serpentinit |  Mesozoikum     | Paläozoikum   | Grundgebirge  |
|15203325 |Holzerspitz-Kalkschiefer | Schiefer: kalkig  | –   | – |  Holzerspitz-Kalkschiefer |  Mesozoikum     | Mesozoikum   | Post-Rift  |
|15203327 |Rinderbach-Fm. | Tonstein  | Sandstein: Quarz   | – |  Rinderbach-Formation |  Danien     | Danien   | Flysch  |
|15203328 |Langenegg-Fm. | Sandstein: kalkig  | Mergelstein   | – |  Langenegg-Formation |  Turonien     | Cénomanien   | Flysch  |
|15203329 |Rombach-Fm. | Brekzie: polymikt  | Mergelstein   | – |  Rombach-Formation |  Santonien     | Coniacien   | Flysch  |
|15203330 |Roffna-Gneis | Gneis: granitisch  | Gneis: granitisch   | – |  Roffna-Gneis |  Mississippien     | Mississippien   | Variszisches Grundgebirge  |
|15203331 |Roffna-Gneis: Porphyrische Fazies | Granit: porphyrisch  | –   | – |  Roffna-Gneis |  Mississippien     | Mississippien   | Variszisches Grundgebirge  |
|15203332 |Burgruinen-Gneis | Gneis  | Pegmatit   | – |  Burgruinen-Gneis |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203333 |Taspegn-Gneis | Gneis: psephitisch  | –   | – |  Taspegn-Gneis |  Perm     | Karbon   | Sedimentbedeckung  |
|15203334 |Aigremont-Brekzie | Brekzie: polymikt  | Siltstein: schiefrig   | – |  Aigremont-Brekzie |  Späte Kreide     | Späte Kreide   | Flysch  |
|15203335 |Sulzgrabe-Fm. | Mergelstein: kalkig  | Sandstein   | Kalkstein |  Sulzgrabe-Formation |  Frühe Kreide     | Später Jura   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203336 |Brekzien-Decke: Rhät | Schiefer: kalkig  | –   | – |  – |  Rhät     | Rhät   | «Rhät»  |
|15203337 |Klippen-Decke: Siderolithischer Dogger | Tonstein  | Gestein: residual: Eisenmineralien   | Brekzie: dolomitisch |  – |  Mittlerer Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15203338 |St-Triphon-Fm.: Andonces-Mb.: Silex-Niveau | Kalkstein: Chert  | –   | – |  «Silex-Niveau» (St-Triphon-Fm.) |  Anisien     | Anisien   | Karbonatische Trias  |
|15203339 |St-Triphon-Fm.: Andonces-Mb.: Mittlere Rauwacke | Rauwacke  | Dolomitstein   | Mergelstein |  «Mittlere Rauhwacke» (St-Triphon-Fm.) |  Ladinien     | Anisien   | Karbonatische Trias  |
|15203340 |Timun-Gneiskomplex | Schiefer: Serizit-Chlorit  | Gneis   | Amphibolit |  Timun-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15203341 |Malenco-Serpentinit | Serpentinit  | Schiefer: Antigorit   | – |  Malenco-Serpentinit |  Bathonien     | Bajocien   | Ophiolithische Abfolge  |
|15203342 |Forno-Amphibolit | Amphibolit: gebändert  | Basalt   | Brekzie: pyroklastisch |  Forno-Amphibolit |  Tithonien     | Callovien   | Ophiolithische Abfolge  |
|15203343 |Muretto-Quarzit | Quarzit  | Schiefer: Quarz   | – |  Muretto-Quarzit |  Späte Kreide     | Späte Kreide   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203344 |Biot-Fm.: Colerin-Konglomerat | Konglomerat  | –   | – |  Colerin-Konglomerat |  Maastrichtien     | Campanien   | Flysch  |
|15203345 |Pierre-Avoi-Melange: Brekzie | Brekzie: polymikt  | –   | – |  Pierre-Avoi-Brekzie |  Mesozoikum     | Mesozoikum   | Mélange  |
|15203346 |Dréveneuse-Bauxit | Gestein: residual  | –   | – |  Dréveneuse-Bauxit |  Mittlerer Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15203347 |Barrhorn-Einheit: Metabauxit | Schiefer: Chloritoid-Kyanit  | –   | – |  Brunnegjoch-Metabauxit |  Mittlerer Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15203349 |Terri-Schiefer | Schiefer: kalkig  | Schiefer: tonig   | Marmor |  Terri-Schiefer |  Mittlerer Jura     | Früher Jura   | Sedimentbedeckung  |
|15203350 |Robiei-Wildflysch | Siltstein  | Sandstein: kalkig: Glimmer   | Schiefer: Glimmer-Granat |  Robiei-Wildflysch |  Priabonien     | Mittleres Eozän   | Mélange  |
|15203351 |Robiei-Wildflysch: Pizzo-Castello-Wildflysch | Gneis  | Sandstein: kalkig   | Marmor |  Pizzo-Castello-Wildflysch |  Priabonien     | Mittleres Eozän   | Mélange  |
|15203352 |Robiei-Wildflysch: Tamier-Zött-Wildflysch | Gneis  | Gestein: basisch   | – |  Tamier-Zött-Wildflysch |  Priabonien     | Mittleres Eozän   | Mélange  |
|15203353 |Robiei-Wildflysch: Alpe-Tamia-Campo-Wildflysch | Marmor: kalkig  | –   | – |  Alpe-Tamia-Campo-Wildflysch |  Priabonien     | Mittleres Eozän   | Mélange  |
|15203354 |Teggiolo-Kalkschiefer | Schiefer: kalkig  | –   | – |  Teggiolo-Kalkschiefer |  Mittleres Eozän     | Späte Kreide   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203355 |Teggiolo-Kalkschiefer: Medola-Quarzit | Quarzit  | Sandstein: kalkig   | Schiefer: Glimmer |  Medola-Quarzit |  Mittleres Eozän     | Späte Kreide   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203356 |Teggiolo-Kalkschiefer: Pianasciom-Kalkschiefer | Schiefer: kalkig  | Sandstein   | Kalkstein |  Pianasciom-Kalkschiefer |  Mittleres Eozän     | Späte Kreide   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203357 |Teggiolo-Kalkschiefer: Piano-delle-Creste-Sandstein | Sandstein: Quarz  | Sandstein: kalkig   | – |  Piano-delle-Creste-Sandstein |  Mittleres Eozän     | Späte Kreide   | Post-Rift Mesozoikum in detritischer Fazies  |
|15203358 |Antabia-Gr. | Marmor  | Sandstein   | Konglomerat |  – |  Berriasien     | Früher Jura   | Sedimentbedeckung  |
|15203359 |Vanis-Fm. | Marmor  | Schiefer: kalkig   | – |  Vanis-Formation |  Berriasien     | Berriasien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203360 |Sevinera-Marmor | Marmor: kalkig  | –   | – |  Sevinera-Marmor |  Tithonien     | Oxfordien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15203361 |Sevinera-Sandstein | Sandstein: kalkig  | –   | – |  Sevinera-Sandstein |  Callovien     | Bathonien   | Lias-Dogger in neritischer Fazies  |
|15203362 |Ri-d&#39;Antabia-Konglomerat | Konglomerat  | –   | – |  Ri-d&#39;Antabia-Konglomerat |  Mittlerer Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15203363 |Lebendun-Komplex: Scisti bruni | Schiefer: Glimmer  | –   | – |  «Scisti bruni» (Lebendun) |  Mesozoikum     | Paläozoikum   | Grundgebirge  |
|15203364 |Lebendun-Komplex: Basaler Gneis | Gneis: augig  | –   | – |  Lebendun-Komplex |  Mesozoikum     | Paläozoikum   | Grundgebirge  |
|15200506 |Hörnli-Fm.: Seerücken-Tuffit | Tuffit  | –   | – |  Seerücken-Tuffit |  Serravallien     | Serravallien   | OSM  |
|15200503 |Öhningen-Fm. | Mergelstein  | Gestein: vulkanisch   | – |  Öhningen-Formation |  Langhien     | Langhien   | OSM  |
|15200504 |Öhningen-Fm.: Öhningen-Süsswasserkalk | Kalkstein  | Tonstein   | Gestein: vulkanisch |  Öhningen-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200505 |Öhningen-Fm.: Ramschwag-Nagelfluh | Konglomerat: kalkig-dolomitisch  | –   | – |  Ramschwag-Nagelfluh |  Langhien     | Langhien   | OSM  |
|15200507 |Meilen-Fm. | Mergelstein  | –   | – |  Meilen-Formation |  Langhien     | Langhien   | OSM  |
|15200508 |Meilen-Fm.: Wulp-Rotzone | Bentonit  | –   | – |  «Wulp-Rotzone» |  Langhien     | Langhien   | OSM  |
|15200509 |Käpfnach-Fm. | Mergelstein  | Gestein: organisch: Kohle   | – |  Kapfnach-Formation |  Langhien     | Spätes Burdigalien   | OSM  |
|15200510 |OSM-J: Juranagelfluh: Mergel-dominierte Fazies | Mergelstein  | –   | – |  – |  Tortonien     | Langhien   | OSM  |
|15200511 |Golat-Süsswasserkalk | Kalkstein: kreidig: Bitumen  | Mergelstein   | Sandstein |  Golat-Süsswasserkalk |  Mittleres Miozän     | Mittleres Miozän   | OSM  |
|15200512 |Belpberg-Fm.: Fossilreicher Horizont | Mergelstein: Bioklasten  | Sandstein: mergelig   | – |  Belpberg-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200513 |Fm. der Granitischen Molasse: Hombach-Mb. | Sandstein: Feldspat  | Mergelstein   | Konglomerat |  Hombach-Member |  Spätes Chattien     | Spätes Chattien   | USM  |
|15200514 |Homberg-Fm. | Sandstein: Feldspat  | Siltstein   | Mergelstein |  Homberg-Formation |  Frühes Chattien     | Frühes Chattien   | USM  |
|15200515 |Gäbris-Nagelfluh | Konglomerat  | Sandstein   | – |  Gäbris-Nagelfluh |  Aquitanien     | Aquitanien   | USM  |
|15200516 |Gäbris-Nagelfluh: Gstaldenbach-Mb. | Mergelstein  | Konglomerat   | – |  Gstaldenbach-Member |  Aquitanien     | Aquitanien   | USM  |
|15200517 |Gäbris-Nagelfluh: Heiden-Mb. | Sandstein: kalkig  | –   | – |  Heiden-Member |  Aquitanien     | Aquitanien   | USM  |
|15200518 |Gäbris-Nagelfluh: Klusbach-Mb. | Konglomerat  | –   | – |  Klusbach-Member |  Aquitanien     | Aquitanien   | USM  |
|15200519 |Gäbris-Nagelfluh: Eggen-Mb. | Sandstein  | –   | – |  Eggen-Member |  Aquitanien     | Aquitanien   | USM  |
|15200520 |Gäbris-Sulzbach: Sulzbach-Mb. | Sandstein: Feldspat  | Sandstein: kalkig   | Konglomerat: kalkig |  Sulzbach-Member |  Aquitanien     | Aquitanien   | USM  |
|15200521 |Gäbris-Sulzbach: Sulzbach-Mb.: Kalknagelfluh | Konglomerat: kalkig  | –   | – |  Sulzbach-Member |  Aquitanien     | Aquitanien   | USM  |
|15200522 |Kronberg-Nagelfluh: Pfingstboden-Mb. | Konglomerat: polymikt  | –   | – |  Pfingstboden-Member |  Aquitanien     | Aquitanien   | USM  |
|15200523 |Kronberg-Nagelfluh: Hochfläschli-Mb. | Konglomerat  | Mergelstein   | – |  Hochfläschli-Member |  Aquitanien     | Aquitanien   | USM  |
|15200524 |Kronberg-Nagelfluh: Ennetbühl-Mb. | Konglomerat  | Mergelstein   | – |  Ennetbühl-Member |  Aquitanien     | Aquitanien   | USM  |
|15200525 |Kronberg-Nagelfluh: Hochalp-Mb. | Konglomerat: kalkig-dolomitisch  | Mergelstein   | – |  Hochalp-Member |  Aquitanien     | Aquitanien   | USM  |
|15200526 |Kronberg-Nagelfluh: Krummenau-Mb. | Mergelstein  | Konglomerat: kalkig   | Sandstein: kalkig |  Krummenau-Member |  Aquitanien     | Aquitanien   | USM  |
|15200527 |USM-J: Ältere Juranagelfluh | Konglomerat: kalkig  | Mergelstein   | – |  «Ältere Juranagelfluh» |  Aquitanien     | Aquitanien   | USM  |
|15200528 |Gitzischöpf-Nagelfluh | Konglomerat  | Sandstein   | Tonstein |  Gitzschöpf-Nagelfluh |  Spätes Chattien     | Spätes Chattien   | USM  |
|15200529 |Honegg-Mergel | Mergelstein: sandig  | Konglomerat   | – |  Honegg-Mergel |  Aquitanien     | Spätes Chattien   | USM  |
|15200530 |Honegg-Mergel: Kaltbach-Nagelfluh | Konglomerat  | –   | – |  Kaltbach-Nagelfluh |  Aquitanien     | Spätes Chattien   | USM  |
|15200531 |Thun-Fm.: Hünibach-Nagelfluh | Konglomerat  | Sandstein   | Mergelstein |  Hünibach-Nagelfluh |  Chattien     | Chattien   | USM  |
|15200532 |Losenegg-Fm. | Konglomerat: polymikt  | Sandstein   | Siltstein |  Losenegg-Formation |  Chattien     | Chattien   | USM  |
|15200533 |Homberg-Fm.: Schwändibach-Nagelfluh | Konglomerat  | Sandstein   | Mergelstein |  Schwändibach-Nagelfluh |  Frühes Chattien     | Frühes Chattien   | USM  |
|15200534 |Uerscheli-Fm. | Sandstein  | Siltstein   | Konglomerat: polymikt |  Uerscheli-Formation |  Frühes Chattien     | Frühes Chattien   | USM  |
|15200535 |Uerscheli-Fm.: Bumbach-Nagelfluh | Konglomerat  | Siltstein   | – |  Bumbach-Nagelfluh |  Frühes Chattien     | Frühes Chattien   | USM  |
|15200536 |USM-I: Untere Bunte Molasse: Kalksandstein | Sandstein: kalkig: Glimmer  | Mergelstein: sandig   | – |  «Untere Bunte Molasse» (USM-I) |  Chattien     | Chattien   | USM  |
|15200537 |Gérignoz-Fm. | Mergelstein  | Sandstein: Glimmer   | Tonstein: Kohle |  Gérignoz-Formation |  Aquitanien     | Spätes Chattien   | USM  |
|15200538 |Speer-Fm.: Leuenfall-Nagelfluh | Konglomerat: kalkig  | –   | – |  Leuenfall-Nagelfluh |  Chattien     | Rupélien   | USM  |
|15200539 |Speer-Fm.: Wintersberg-Mb. | Mergelstein  | Sandstein: kalkig   | Konglomerat |  Wintersberg-Member |  Chattien     | Chattien   | USM  |
|15200540 |Speer-Fm.: Ebnat-Mb. | Mergelstein  | Sandstein: mergelig   | Sandstein: kalkig |  Ebnat-Member |  Chattien     | Rupélien   | USM  |
|15200541 |Speer-Fm.: Ebnat-Mb.: Rütiberg-Kalksandstein | Sandstein: kalkig  | –   | – |  Rütiberg-Kalksandstein |  Chattien     | Rupélien   | USM  |
|15200542 |Rigi-Fm.: Bunte Rigi-Nagelfluh: Pfiffegg-Nagelfluh | Konglomerat: kalkig-dolomitisch  | Sandstein   | – |  Pfiffegg-Nagelfluh |  Chattien     | Chattien   | USM  |
|15200543 |Weggis-Fm. | Konglomerat: kalkig-dolomitisch  | Sandstein   | Mergelstein |  Weggis-Formation |  Frühes Chattien     | Rupélien   | USM  |
|15200544 |Weggis-Fm.: Kännelegg-Nagelfluh | Konglomerat: kalkig  | –   | – |  Kännelegg-Nagelfluh |  Frühes Chattien     | Rupélien   | USM  |
|15200545 |Molasse Rouge des Jurasüdfusses | Mergelstein: sandig  | Sandstein: Glimmer   | Konglomerat: kalkig |  «Molasse Rouge des Jurasüdfusses» |  Spätes Chattien     | Rupélien   | USM  |
|15200546 |Molasse Rouge des Jurasüdfusses: Mathod-Sandstein | Sandstein  | –   | – |  Mathod-Sandstein |  Spätes Chattien     | Spätes Chattien   | USM  |
|15200547 |Molasse Rouge des Jurasüdfusses: Goumoëns-Sandstein | Sandstein  | Konglomerat: kalkig   | – |  Goumoëns-Sandstein |  Frühes Chattien     | Frühes Chattien   | USM  |
|15200548 |Molasse Rouge de Vevey | Mergelstein: siltig: Glimmer  | Sandstein: mergelig   | – |  «Molasse Rouge de Vevey» |  Chattien     | Chattien   | USM  |
|15200549 |Molasse Rouge de Monthey | Schiefer  | Sandstein   | – |  «Molasse Rouge de Monthey» |  Chattien     | Chattien   | USM  |
|15200550 |Grindelegg-Fm. | Mergelstein  | Sandstein: kalkig: Glimmer   | Konglomerat: kalkig |  Grindelegg-Formation |  Chattien     | Chattien   | USM  |
|15200551 |Grès et Marnes Gris à Gypse: Tillerée-Sch. | Mergelstein: tonig: Kohle  | Mergelstein: siltig   | – |  Tillerée-Schichten |  Aquitanien     | Spätes Chattien   | USM  |
|15200552 |Grès et Marnes Gris à Gypse: Süsswasserkalke und Dolomite | Kalkstein  | Dolomitstein   | – |  «Grès et Marnes Gris à Gypse» |  Spätes Chattien     | Spätes Chattien   | USM  |
|15200553 |Oltingue-Kalkarenit | Kalkstein: arenitisch  | –   | – |  Oltingue-Kalkarenit |  Rupélien     | Rupélien   | UMM  |
|15200554 |Vaulruz-Fm. | Sandstein: kalkig: Glimmer  | Mergelstein   | – |  Vaulruz-Formation |  Rupélien     | Rupélien   | UMM  |
|15200555 |Hilfern-Fm.: Unter-Lochsiti-Nagelfluh | Konglomerat  | –   | – |  Unter-Lochsiti-Nagelfluh |  Rupélien     | Rupélien   | UMM  |
|15200556 |Hilfern-Fm.: Flühli-Nagelfluh | Konglomerat  | –   | – |  Flühli-Nagelfluh |  Rupélien     | Rupélien   | UMM  |
|15200557 |St.-Gallen-Fm.: Mergelstein-dominierte Fazies | Mergelstein: Bioklasten  | –   | – |  St.-Gallen-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200558 |Fm. der Granitischen Molasse: Marbach-Mb. | Sandstein: Glimmer  | Mergelstein   | – |  Marbach-Member |  Aquitanien     | Aquitanien   | USM  |
|15200560 |USM-I: Untere Bunte Molasse | Mergelstein: siltig  | Sandstein   | – |  «Untere Bunte Molasse» (USM-I) |  Spätes Chattien     | Spätes Chattien   | USM  |
|15200562 |OSM-J: Mittlere Juranagelfluh | Konglomerat  | –   | – |  Mittlere Juranagelfluh |  Langhien     | Burdigalien   | OSM  |
|15200563 |OSM-J: Albstein | Kalkstein  | –   | – |  Albstein |  Burdigalien     | Burdigalien   | OSM  |
|15200564 |Grimmelfingen-Fm.: Graupensand-Fazies | Sandstein  | –   | – |  Grimmelfingen-Formation |  Burdigalien     | Burdigalien   | Molasse  |
|15200565 |OSM-J: Heliciden-Mergel | Mergelstein: Bioklasten  | Tonstein   | – |  «Heliciden-Mergel» (OSM-J) |  Tortonien     | Langhien   | OSM  |
|15200566 |Haldenhof-Mergel | Mergelstein  | Sandstein   | – |  Haldenhof-Mergel |  Langhien     | Spätes Burdigalien   | OSM  |
|15203368 |Pierre-Avoi-Melange: Quarzschiefer-dominierte Fazies | Schiefer: tonig  | Quarzit   | Schiefer: kalkig |  Pierre-Avoi-Melange |  Rupélien     | Mittleres Eozän   | Mélange  |
|15203365 |Antigorio-Orthogneis | Gneis: magmatisch  | –   | – |  Antigorio-Orthogneis |  Cisuralien     | Cisuralien   | Grundgebirge  |
|15203366 |Falknis-, Sulzfluh- und Tasna-Decke: Couches Rouges | Kalkstein: mergelig  | Mergelstein   | Brekzie |  – |  Maastrichtien     | Albien   | Couches Rouges  |
|15203367 |Piz-Terri-Lunschania: Lagensandkalk | Schiefer: tonig-kalkig  | Quarzit: Chlorit   | – |  – |  Früher Jura     | Früher Jura   | Sedimentbedeckung  |
|15203369 |Pierre-Avoi-Melange: Konglomerat-dominierte Fazies | Konglomerat  | –   | – |  Pierre-Avoi-Melange |  Rupélien     | Mittleres Eozän   | Mélange  |
|15203370 |Südegg-Komplex | Schiefer  | Gestein: metamorph   | – |  Südegg-Komplex |  Mesozoikum     | Paläozoikum   | Mélange  |
|15203371 |Punta-Rossa-Komplex | Gneis  | Serpentinit   | Konglomerat |  Punta-Rossa-Komplex |  Mesozoikum     | Paläozoikum   | Mélange  |
|15203372 |Ferret-Schiefer | Schiefer: tonig  | Schiefer: kieselig   | Kalkstein |  Ferret-Schiefer |  Späte Kreide     | Frühe Kreide   | Sedimentbedeckung  |
|15203373 |Piz-Terri-Lunschania: Basale Tonschiefer | Schiefer: sandig-tonig  | –   | – |  – |  Früher Jura     | Früher Jura   | Sedimentbedeckung  |
|15203374 |Grava-Decke: Kalk- und Tonschiefer | Schiefer  | –   | – |  – |  Kreide     | Kreide   | Sedimentbedeckung  |
|15203376 |Piz-Terri-Lunschania: Konglomeratgneis | Gneis: psephitisch  | –   | – |  – |  Frühe Trias     | Perm   | Sedimentbedeckung  |
|15203377 |Garzott-Brekzie | Brekzie  | Kalkstein: sandig   | Quarzit |  Garzott-Brekzie |  Mittlerer Jura     | Früher Jura   | Sedimentbedeckung  |
|15203378 |Areua-Bruschghorn-Melange | Gneis  | Brekzie   | – |  Areua-Bruschghorn-Melange |  Känozoikum     | Paläozoikum   | Mélange  |
|15203379 |Grava-Decke: Albitquarzit | Quarzit: Albit  | –   | – |  – |  Mittlerer Jura     | Mittlerer Jura   | Sedimentbedeckung  |
|15203380 |Grava-Decke: Basale Tonschiefer | Schiefer: tonig  | –   | – |  – |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15203381 |Aul-Decke: Phengitgneis | Gneis: augig: Phengit  | –   | – |  – |  Paläozoikum     | Paläozoikum   | Sedimentbedeckung  |
|15203382 |Haute-Pointe-Fm. | Kalkstein: kieselig: Bioklasten-Chert  | Kalkstein: mergelig-schiefrig   | – |  Haute-Pointe-Formation |  Oxfordien     | Callovien   | Syn-Rift  |
|15203383 |Brasses-Fm. | Kalkstein: kieselig  | Kalkstein: spätig: Bioklasten   | Kalkstein: mergelig-schiefrig |  Brasses-Formation |  Bajocien     | Pliensbachien   | Syn-Rift  |
|15203385 |Macugnaga-Augengneis | Gneis: augig  | –   | – |  Macugnaga-Augengneis |  Pennsylvanien     | Pennsylvanien   | Grundgebirge  |
|15203386 |Zone Houillère: Perm | Schiefer: Quarz  | Konglomerat   | Sandstein |  – |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15203387 |Zone Houillère: Perm: Quarzschiefer | Schiefer: Quarz  | Gneis   | – |  – |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15203388 |Ricard-Rhyolit | Rhyolith  | –   | – |  Ricard-Rhyolit |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15203389 |Zone Houillère: Perm: Konglomerat | Konglomerat  | –   | – |  – |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15203390 |Printse-Fm.: Sandig-schiefrige Fazies | Schiefer: sandig  | –   | – |  Printse-Formation |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15203391 |Printse-Fm.: Tonige Fazies | Schiefer: tonig  | –   | – |  Printse-Formation |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15203392 |Printse-Fm.: Chandoline-Sandstein | Sandstein  | Sandstein: konglomeratisch   | – |  Chandoline-Sandstein |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15203393 |Gälmji-Gneis | Gneis  | Schiefer: Glimmer-Granat   | Amphibolit |  Gälmji-Gneis |  Perm     | Karbon   | Grundgebirge  |
|15203394 |Scherbadung-Gabbro | Gabbro  | –   | – |  Scherbadung-Gabbro |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203395 |Lacerandes-Augengneis | Gneis: augig  | –   | – |  Lacerandes-Augengneis |  Spätes Ordovizium     | Mittleres Ordovizium   | Grundgebirge  |
|15203396 |Mont-Mort-Metapelit | Schiefer: Glimmer-Granat  | Amphibolit   | – |  Mont-Mort-Metapelit |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203397 |Pierre-Avoi-Melange: Schwarze Schiefer | Schiefer: tonig  | –   | – |  Pierre-Avoi-Melange |  Mesozoikum     | Paläozoikum   | Mélange  |
|15203398 |Ferret-Schiefer: La-Dotse-Albitkalk | Kalkstein: Albit  | –   | – |  La-Dotse-Albitkalk |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15203399 |Ergischhorn-Komplex-Fm.: Ginals-Gneis | Gneis: augig  | –   | – |  Ginals-Gneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203400 |Berisal-Gneiskomplex | Gneis: Granat  | Schiefer: Glimmer-Granat   | Amphibolit |  Berisal-Gneiskomplex |  Perm     | Ordovizium   | Grundgebirge  |
|15203401 |Berisal-Gneiskomplex: Augengneis | Gneis: augig  | –   | – |  Berisal-Gneiskomplex |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203402 |Ruitor-Gneiskomplex | Gneis: augig  | Schiefer: Glimmer-Granat   | Amphibolit |  Ruitor-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203403 |Corno-Gneis | Gneis: psammitisch  | Gneis: psephitisch: Phengit   | – |  Corno-Gneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203404 |Unterpenninikum: Trias: Quarzit | Quarzit  | –   | – |  – |  Trias     | Trias   | Detritische Trias  |
|15203405 |Mittelpenninikum: Grundgebirge | Gneis  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203406 |Mont-Brûlé-Quarzit | Quarzit  | Schiefer: Quarz-Glimmer   | – |  Mont-Brûlé-Quarzit |  Perm     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15203407 |Mont-Brûlé-Quarzit: Plan-Palasuit-Konglomerat | Konglomerat  | –   | – |  Plan-Palasuit-Konglomerat |  Perm     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15203408 |Oberpenninikum: Metasedimente | 15111591  | Schiefer: tonig   | – |  – |  Mesozoikum     | Mesozoikum   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203409 |Tsaté-Decke: Metasedimente | Gestein: sedimentär  | –   | – |  – |  Mesozoikum     | Mesozoikum   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203410 |Tsaté-Decke: Marmor | Marmor  | Brekzie   | – |  – |  Später Jura     | Später Jura   | Maiolica / Aptychenkalk  |
|15203411 |Tsaté-Decke: Radiolarit | Gestein: kieselig: Radiolarien  | Schiefer: kieselig   | – |  Chanrion-Radiolarit |  Später Jura     | Mittlerer Jura   | Radiolarit  |
|15203412 |Zermatt-Saas-Decke: Metasedimente | Gestein: sedimentär  | –   | – |  – |  Mesozoikum     | Mesozoikum   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203413 |Oberpenninikum: Ophiolith | Serpentinit  | Gabbro   | Basalt |  – |  Später Jura     | Mittlerer Jura   | Ophiolithische Abfolge  |
|15203414 |Tsaté-Decke: Ophiolith | Serpentinit  | Gabbro   | Basalt |  – |  Später Jura     | Mittlerer Jura   | Ophiolithische Abfolge  |
|15203415 |Mont-des-Ritzes-Metabasalt | Basalt  | Prasinit   | – |  Mont-des-Ritzes-Metabasalt |  Später Jura     | Mittlerer Jura   | Ophiolithische Abfolge  |
|15203416 |Aiguilles-Rouges-d&#39;Arolla-Metagabbro | Gabbro  | –   | – |  Aiguilles-Rouges-d&#39;Arolla-Metagabbro |  Später Jura     | Mittlerer Jura   | Ophiolithische Abfolge  |
|15203417 |Torrembey-Brekzie | Brekzie: kalkig  | –   | – |  Torrembey-Brekzie |  Trias     | Trias   | Prä-Rift  |
|15203418 |Zermatt-Saas-Decke: Marmor | Marmor  | –   | – |  – |  Später Jura     | Später Jura   | Maiolica / Aptychenkalk  |
|15203419 |Zermatt-Saas-Decke: Quarzit | Quarzit  | Gestein: kieselig: Radiolarien   | – |  – |  Später Jura     | Mittlerer Jura   | Radiolarit  |
|15203420 |Riffelberg-Melange | Eklogit  | Schiefer   | – |  Riffelberg-Melange |  Mesozoikum     | Mesozoikum   | Mélange  |
|15203421 |Zermatt-Saas-Decke: Schiefer | 15111591  | Schiefer: tonig   | – |  – |  Mesozoikum     | Mesozoikum   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203422 |Zermatt-Saas-Decke: Ophiolith | Serpentinit  | Gabbro   | Basalt |  – |  Später Jura     | Mittlerer Jura   | Ophiolithische Abfolge  |
|15203423 |Pfulwe-Metabasalt | Basalt  | Prasinit   | – |  Pfulwe-Metabasalt |  Später Jura     | Mittlerer Jura   | Ophiolithische Abfolge  |
|15203424 |Antrona-Decke: Ophiolith | Serpentinit  | Gabbro   | Basalt |  – |  Später Jura     | Mittlerer Jura   | Ophiolithische Abfolge  |
|15203425 |Ergischhorn-Komplex-Fm.: Böshorn-Gneis | Gneis  | Granit   | – |  Böshorn-Gneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203426 |Monte-Leone-Decke: Orthogneis | Gneis: magmatisch  | –   | – |  – |  Perm     | Karbon   | Grundgebirge  |
|15203427 |Monte-Leone-Decke: Leukogneis | Gneis  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203428 |Monte-Leone-Decke: Hyperaugengneis | Gneis: augig  | –   | – |  – |  Ordovizium     | Ordovizium   | Grundgebirge  |
|15203429 |Monte-Leone-Decke: Paragneis | Gneis: sedimentär  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15200567 |OMM-J | Sandstein  | Mergelstein   | Konglomerat |  – |  Burdigalien     | Burdigalien   | OMM  |
|15200568 |Tenniken-Muschelagglomerat | Sandstein: kalkig: Muscheln  | Konglomerat: kalkig: Muscheln   | – |  Tenniken-Muschelagglomerat |  Burdigalien     | Burdigalien   | OMM  |
|15200569 |OMM-II: Turritellen-Kalk | Kalkstein: sandig: Bioklasten  | –   | – |  – |  Burdigalien     | Burdigalien   | OMM  |
|15200570 |Randen-Grobkalk | Kalkstein: sandig: Bioklasten  | –   | – |  Randen-Grobkalk |  Burdigalien     | Burdigalien   | OMM  |
|15200571 |Péry-Sandstein | Sandstein: konglomeratisch  | –   | – |  Péry-Sandstein |  Burdigalien     | Burdigalien   | OMM  |
|15200572 |Les-Bayards-Juranagelfluh | Brekzie: kalkig  | –   | – |  Les-Bayards-Juranagelfluh |  Pliozän     | Miozän   | OSM  |
|15200573 |Günsberg- und Vellerat-Fm. | Kalkstein  | Mergelstein   | – |  – |  Oxfordien     | Oxfordien   | Malm  |
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
|15200616 |Schwarzwald-Massiv: Grundgebirge | Gestein: metamorph  | Gestein: plutonisch   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15200617 |Schwarzwald-Massiv: Variszische Intrusiva | Gestein: plutonisch  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Variszisches Grundgebirge  |
|15200618 |USM-I: Untere Bunte Molasse: Mümliswil-Süsswasserkalk | Kalkstein  | –   | – |  Mümliswil-Süsswasserkalk |  Frühes Chattien     | Frühes Chattien   | USM  |
|15200619 |Luzern-Fm.: Limnischer Horizont | Mergelstein  | Gestein: organisch: Kohle   | – |  Luzern-Formation |  Burdigalien     | Burdigalien   | OMM  |
|15200620 |Molasse Rouge des Jurasüdfusses: Dardagny-Sandstein | Sandstein: Bitumen  | –   | – |  Dardagny-Sandstein |  Frühes Chattien     | Frühes Chattien   | USM  |
|15200621 |Napf-Fm.: Konglomerat-dominierte Fazies | Konglomerat: polymikt: Quarz  | Sandstein: Feldspat   | – |  Napf-Formation |  Langhien     | Burdigalien   | OSM  |
|15200622 |Napf-Fm.: Sandstein-Mergelstein-dominierte Fazies | Sandstein: Feldspat  | Mergelstein   | – |  Napf-Formation |  Langhien     | Burdigalien   | OSM  |
|15200623 |Le-Locle-Fm. | Kalkstein: kreidig  | Mergelstein: Lignit   | Tonstein |  Le-Locle-Formation |  Serravallien     | Langhien   | OSM  |
|15200624 |Le-Locle-Fm.: Le-Verger Mb. | Kalkstein: kreidig  | Mergelstein: Lignit   | – |  Le-Verger-Member |  Serravallien     | Langhien   | OSM  |
|15200625 |Le-Locle-Fm.: Combe-Girard Mb. | Kalkstein: kreidig  | –   | – |  Combe-Girard-Member |  Serravallien     | Langhien   | OSM  |
|15200626 |Crêt-du-Locle-Fm. | Mergelstein  | Konglomerat: kalkig   | – |  Crêt-du-Locle-Formation |  Serravallien     | Langhien   | Molasse  |
|15200627 |Crêt-du-Locle-Fm.: Mergelfazies | Mergelstein  | –   | – |  Crêt-du-Locle-Formation |  Serravallien     | Langhien   | Molasse  |
|15200628 |St.-Gallen-Fm.: Gitzigrabe-Grobsandstein | Sandstein  | –   | – |  Gitzigrabe-Grobsandstein |  Burdigalien     | Burdigalien   | OMM  |
|15200629 |Trois-Rods-Süsswasserkalk | Kalkstein: Bioklasten  | –   | – |  Trois-Rods-Süsswasserkalk |  Frühes Chattien     | Frühes Chattien   | USM  |
|15200630 |Champ-Vuillerat-Süsswasserkalk | Kalkstein  | –   | – |  Champ-Vuillerat-Süsswasserkalk |  Rupélien     | Priabonien   | Siderolithikum  |
|15200631 |Napf-Fm.: Wolhusen-Bentonit | Bentonit  | –   | – |  Wolhusen-Bentonit |  Langhien     | Burdigalien   | OSM  |
|15200632 |OSM-II: Gitzitobel-Süsswasserkalk | Kalkstein  | –   | – |  Gitzitobel-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200633 |OSM-II: Wissenbach-Süsswasserkalk | Kalkstein  | –   | – |  Wissenbach-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200634 |OSM-II: Altbach-Süsswasserkalk | Kalkstein  | –   | – |  Altbach-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200635 |OSM-II: Tröleten-Süsswasserkalk | Kalkstein  | –   | – |  Tröleten-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200636 |OSM-II: Tschöplihof-Süsswasserkalk | Kalkstein  | –   | – |  Tschöplihof-Süsswasserkalk |  Langhien     | Langhien   | OSM  |
|15200637 |Lienegg-Fm. | Konglomerat: kalkig  | Sandstein   | Mergelstein |  Lienegg-Formation |  Aquitanien     | Chattien   | USM  |
|15200638 |Öligraben-Fm. | Konglomerat: polymikt  | Sandstein   | Mergelstein: Kohle |  Öligraben-Formation |  Chattien     | Chattien   | USM  |
|15200639 |Studweid-Fm. | Sandstein  | Mergelstein   | Konglomerat: polymikt |  Studweid-Formation |  Aquitanien     | Aquitanien   | USM  |
|15200640 |Rossemaison-Fm. | Mergelstein: siltig  | Gestein: residual   | – |  Rossemaison-Formation |  Rupélien     | Priabonien   | Siderolithikum  |
|15200641 |Schwaningen-Merenbach-Rhyolith | Rhyolith  | –   | – |  Schwaningen-Merenbach-Rhyolith |  Perm     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15200642 |Schwaningen-Weizen-Granit | Granit  | –   | – |  Schwaningen-Weizen-Granit |  Perm     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15200643 |Etzgen-Granit | Granit  | –   | – |  Etzgen-Granit |  Perm     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15200645 |USM-I: Kalk-Dolomit-Nagelfluh | Konglomerat: kalkig-dolomitisch  | –   | – |  – |  Chattien     | Rupélien   | USM  |
|15200646 |Hornbüel-Melange | Sandstein  | Mergelstein   | Konglomerat |  Hornbüel-Melange |  Chattien     | Rupélien   | Mélange  |
|15200647 |Kalter-Wangen-Fm. | Konglomerat: kalkig  | Sandstein   | Mergelstein |  Kalter-Wangen-Formation |  Tortonien     | Langhien   | OSM  |
|15200648 |Baltersweil-Nagelfluh | Konglomerat: polymikt: Bioklasten  | –   | – |  Baltersweil-Nagelfluh |  Burdigalien     | Burdigalien   | OMM  |
|15200649 |Netzbachtal-Nagelfluh | Konglomerat  | –   | – |  Netzbachtal-Nagelfluh |  Burdigalien     | Burdigalien   | OMM  |
|15200650 |Rocher-des-Hirondelles-Fm. | Kalkstein: Bioklasten  | Mergelstein   | – |  Rocher-des-Hirondelles-Formation |  Barrémien     | Hauterivien   | «Urgonien»  |
|15200651 |Rocher-des-Hirondelles-Fm.: Fort-de-l&#39;Ecluse-Mb. | Kalkstein: Bioklasten  | Kalkstein: Ooide   | – |  Fort-de-l&#39;Écluse-Member |  Barrémien     | Hauterivien   | «Urgonien»  |
|15200652 |Gorges-de-l&#39;Orbe-Fm.: Bôle-Mb. | Mergelstein: Bioklasten  | Kalkstein: mergelig   | – |  Bôle-Member |  Barrémien     | Barrémien   | «Urgonien»  |
|15203433 |Ruginenta-Decke: Grundgebirge | Gneis  | Gestein: ultramafisch   | Schiefer: Glimmer-Granat |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203430 |Lebendun-Komplex: Arkose | Sandstein: Feldspat  | –   | – |  Lebendun-Komplex |  Mesozoikum     | Perm   | Grundgebirge  |
|15203431 |Lebendun-Komplex: Konglomerat | Konglomerat  | –   | – |  Lebendun-Komplex |  Mesozoikum     | Perm   | Grundgebirge  |
|15203432 |Ruginenta-Decke: Sedimentbedeckung | Kalkstein  | Dolomitstein   | Serpentinit |  – |  Trias     | Pennsylvanien   | Sedimentbedeckung  |
|15203434 |Ruginenta-Decke: Glimmerschiefer | Schiefer: Glimmer-Granat  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203435 |Ruginenta-Decke: Paragneis | Gneis: sedimentär  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203436 |Preja-Fm. | Quarzit  | Rauwacke   | Marmor |  Preja-Formation |  Später Jura     | Trias   | Sedimentbedeckung  |
|15203437 |Cavalli-Fm. | Sandstein: tonig  | Sandstein: Quarz   | Schiefer: Glimmer |  Cavalli-Formation |  Perm     | Perm   | Sedimentbedeckung  |
|15203438 |Monte-Rosa-Decke: Sedimentbedeckung | Sandstein: Feldspat  | Quarzit   | Marmor |  – |  Mesozoikum     | Perm   | Sedimentbedeckung  |
|15203439 |Mezzalama-Granit | Granit: porphyrisch  | –   | – |  Mezzalama-Granit |  Guadalupien     | Cisuralien   | Grundgebirge  |
|15203440 |Monte-Rosa-Orthogneis: Grobkörnige Fazies | Gneis: magmatisch  | –   | – |  Monte-Rosa-Orthogneis  |  Karbon     | Karbon   | Grundgebirge  |
|15203441 |Rottal-Migmatit | Migmatit  | –   | – |  Rottal-Migmatit |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203442 |Monte-Rosa-Orthogneis: Mylonitische Fazies | Gneis: mylonitisch  | –   | – |  Monte-Rosa-Orthogneis  |  Karbon     | Karbon   | Grundgebirge  |
|15203443 |Monte-Rosa-Decke: Paragneis | Gneis: sedimentär  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203444 |Monte-Rosa-Decke: Biotitgneis | Gneis: Biotit  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203445 |Monte-Rosa-Decke: Bändergneis | Gneis: gebändert  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203446 |Monte-Rosa-Decke: Glimmerschiefer | Schiefer: Glimmer  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203447 |Portjengrat-Decke: Sedimentbedeckung | Marmor  | Marmor   | Dolomitstein |  – |  Späte Kreide     | Trias   | Sedimentbedeckung  |
|15203449 |Portjengrat-Orthogneis | Gneis: magmatisch  | –   | – |  Portjengrat-Orthogneis |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203450 |Saas-Fee-Augengneis | Gneis: augig  | –   | – |  Saas-Fee-Augengneis |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203451 |Almagelhorn-Migmatit | Migmatit  | –   | – |  Almagelhorn-Migmatit |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203452 |Weissmies-Paragneis | Gneis: sedimentär  | Gneis: migmatitisch   | – |  Weissmies-Paragneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203453 |Monte-Rosa-Orthogneis: Mittelkörnige Fazies | Gneis: magmatisch  | –   | – |  Monte-Rosa-Orthogneis  |  Karbon     | Karbon   | Grundgebirge  |
|15203454 |Stellihorn-Mylonit | Gneis: mylonitisch  | –   | – |  Stellihorn-Mylonit |  Känozoikum     | Paläozoikum   | Grundgebirge  |
|15203455 |Pizzo-del-Vallone-Decke: Kalkschiefer | Schiefer: kalkig  | Schiefer: Glimmer   | – |  – |  Mesozoikum     | Mesozoikum   | Post-Rift  |
|15203456 |Unterpenninikum: Dogger | Schiefer  | –   | – |  – |  Mittlerer Jura     | Mittlerer Jura   | Lias-Dogger in detritischer Fazies  |
|15203457 |Unterpenninikum: Lias | Kalkstein  | –   | – |  – |  Aalénien     | Früher Jura   | Lias-Dogger in detritischer Fazies  |
|15203458 |Unterpenninikum: Trias: Dolomit | Marmor: dolomitisch  | –   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15203459 |Valgrande-Paragneis | Gneis: sedimentär  | Gneis: Biotit-Muskovit   | Schiefer: Glimmer |  Valgrande-Paragneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203460 |Mittelpenninikum: Variszische Intrusiva | Gneis: magmatisch  | –   | – |  – |  Perm     | Karbon   | Variszisches Grundgebirge  |
|15203461 |Mittelpenninikum: Prävariszisches Grundgebirge | Gneis  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15203462 |Moncucco-Peridotit | Peridotit  | –   | – |  Moncucco-Peridotit |  Mesozoikum     | Paläozoikum   | Grundgebirge  |
|15203463 |Adlerflüe-Fm.: Albitaugenschiefer | Schiefer: augig: Glimmer  | –   | – |  Adlerflüe-Formation |  Kambrium     | Proterozoikum   | Grundgebirge  |
|15203464 |Adlerflüe-Fm.: Bänderamphibolit | Amphibolit: gebändert  | –   | – |  Adlerflüe-Formation |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203465 |Adlerflüe-Fm.: Minugrat-Eklogit | Eklogit  | –   | – |  Minugrat-Eklogit |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203466 |Ergischhorn-Komplex: Amphibolit | Amphibolit  | –   | – |  Ergischhorn-Komplex |  Proterozoikum     | Proterozoikum   | Grundgebirge  |
|15203467 |Distulberg-Fm.: Grüngesteine | Gestein: mafisch  | –   | – |  Distulberg-Formation |  Kambrium     | Kambrium   | Grundgebirge  |
|15203468 |Métailler-Fm.: Prasinit | Prasinit  | –   | – |  Métailler-Formation |  Rupélien     | Kambrium   | Grundgebirge  |
|15203469 |Métailler-Fm.: Ultramafisches Gestein | Gestein: ultramafisch  | –   | – |  Métailler-Formation |  Rupélien     | Kambrium   | Grundgebirge  |
|15203470 |Randa-Augengneis: Oberems-Albitgneis | Gneis: Albit  | Rhyolith   | – |  Oberems-Albitgneis |  Perm     | Perm   | Variszisches Grundgebirge  |
|15203471 |Maggia-Decke: Permo-Karbon | Schiefer  | Konglomerat   | – |  – |  Perm     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15203472 |Maggia-Decke: Quarz-Glimmerschiefer | Schiefer: Quarz-Glimmer  | –   | – |  – |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15203473 |Maggia-Decke: Muskovit-Graphitschiefer | Schiefer: Glimmer-Graphit  | –   | – |  – |  Karbon     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15203474 |Maggia-Decke: Variszische Intrusive | Gestein: plutonisch  | –   | – |  – |  Perm     | Karbon   | Variszisches Grundgebirge  |
|15203475 |Maggia-Decke: Prävariszisches Grundgebirge | Gneis  | Amphibolit   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15203476 |Maggia-Decke: Paragneis | Gneis: sedimentär  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15203477 |Maggia-Decke: Bändergneis | Gneis: gebändert  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15203478 |Maggia-Decke: Augengneis | Gneis: augig  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15203479 |Alpigia-Gneis | Gneis: migmatitisch  | Amphibolit: migmatitisch   | – |  Alpigia-Gneis |  Perm     | Perm   | Grundgebirge  |
|15203480 |Gresso-Someo-Zone | Quarzit  | Marmor: kalkig   | – |  – |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15203481 |Pertusio-Zone | Quarzit  | Marmor: kalkig   | – |  – |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15203482 |Passo-di-Cristallina-Zone | Marmor  | Quarzit   | Schiefer: Glimmer-Granat |  – |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15203483 |Lago-Scuro-Fm. | Marmor: konglomeratisch  | Brekzie: kalkig   | – |  Lago-Scuro-Formation |  Später Jura     | Mittlerer Jura   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15203484 |Val-Sabbia-Fm. | Quarzit  | –   | – |  Val-Sabbia-Formation |  Sinémurien     | Sinémurien   | Lias-Dogger in detritischer Fazies  |
|15203485 |Massari-Fm. | Sandstein  | Kalkstein: sandig   | – |  Massari-Formation |  Pliensbachien     | Hettangien   | Lias-Dogger in detritischer Fazies  |
|15203486 |Naret-Fm. | Schiefer: Quarz-Glimmer  | Schiefer: Glimmer-Graphit   | Marmor |  Naret-Formation |  Hettangien     | Rhät   | Lias-Dogger in detritischer Fazies  |
|15203487 |Breithorn-Serpentinit | Serpentinit  | –   | – |  Breithorn-Serpentinit |  Später Jura     | Mittlerer Jura   | Ophiolithische Abfolge  |
|15203488 |Loranco-Amphibolit | Amphibolit  | –   | – |  Loranco-Amphibolit |  Später Jura     | Mittlerer Jura   | Ophiolithische Abfolge  |
|15203489 |Andolla-Eklogit | Eklogit  | –   | – |  Andolla-Eklogit |  Später Jura     | Mittlerer Jura   | Ophiolithische Abfolge  |
|15203490 |Roz-Schiefer | Schiefer: sandig-kalkig  | Schiefer: sandig   | Schiefer: tonig |  Roz-Schiefer |  Paläogen     | Späte Kreide   | Sedimentbedeckung  |
|15203491 |Ramosch-Zone: Ophiolith | Serpentinit  | Amphibolit   | – |  – |  Frühe Kreide     | Jura   | Ophiolithische Abfolge  |
|15203492 |Arosa-Decke: Metasedimente | Schiefer  | Marmor   | Sandstein |  – |  Späte Kreide     | Später Jura   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203493 |Totalp-Serpentinit | Serpentinit  | –   | – |  Totalp-Serpentinit |  Oxfordien     | Bathonien   | Ophiolithische Abfolge  |
|15203494 |Maran-Brekzie | Brekzie: polymikt  | Schiefer: tonig-kieselig   | – |  Maran-Brekzie |  Später Jura     | Später Jura   | Syn-Rift  |
|15200659 |Wangen- und Letzi-Mb. | Kalkstein: mikritisch  | –   | – |  Villigen-Formation |  Kimméridgien     | Oxfordien   | Malm  |
|15200653 |Gorges-de-l&#39;Orbe-Fm.: Montcherand-Mb. | Mergelstein  | Kalkstein: Bioklasten   | – |  Montcherand-Member |  Barrémien     | Hauterivien   | «Urgonien»  |
|15200654 |Vuache-Fm.: Calcaire roux s.s. | Kalkstein: spätig: Ooide  | –   | – |  Vuache-Formation |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15200658 |Schwarzbach-Fm. | Kalkstein: mergelig: Bioklasten  | Mergelstein   | – |  Schwarzbach-Formation |  Kimméridgien     | Kimméridgien   | Malm  |
|15200660 |Grand-Essert- bis Narlay-Fm. | Kalkstein  | Mergelstein   | Sandstein: Glaukonit |  – |  Pleistozän     | Valanginien   | Post-Rift  |
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
|15200680 |Lindau-Granit | Granit: Biotit-Cordierit  | –   | – |  Lindau-Granit |  Mississippien     | Devon   | Frühvariszisches Grundgebirge  |
|15200681 |Kreuzlingen-Granit | Granit: Biotit-Cordierit  | –   | – |  Kreuzlingen-Granit |  Mississippien     | Devon   | Frühvariszisches Grundgebirge  |
|15200682 |Schlächtenhaus-Schiefer | Sandstein: tonig  | Schiefer: tonig   | – |  Schlächtenhaus-Schiefer |  Mississippien     | Frühes Devon   | Prä- bis frühvariszisches Grundgebirge  |
|15200683 |Gersbach-Schiefer | Schiefer: Hornblende  | –   | – |  Gersbach-Schiefer |  Ordovizium     | Ordovizium   | Prä- bis frühvariszisches Grundgebirge  |
|15200685 |Courgenay- Balsthal- und VilligenFm. | Kalkstein  | Mergelstein   | – |  – |  Kimméridgien     | Oxfordien   | Malm  |
|15200686 |Pichoux-Fm.: Korallenfazies | Kalkstein: Korallen  | Kalkstein: mergelig   | – |  Pichoux-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15200687 |Pichoux-Fm.: Schwammfazies | Kalkstein: Schwämme  | Kalkstein: mergelig   | Mergelstein |  Pichoux-Formation |  Oxfordien     | Oxfordien   | Malm  |
|15200688 |Kalter-Wangen-Fm.: Konglomerat-dominierte Fazies | Konglomerat: kalkig  | Sandstein   | Mergelstein |  Kalter-Wangen-Formation |  Tortonien     | Langhien   | OSM  |
|15200689 |Kalter-Wangen-Fm.: Sandstein-Mergelstein-dominierte Fazies | Sandstein  | Mergelstein   | Konglomerat: kalkig |  Kalter-Wangen-Formation |  Tortonien     | Langhien   | OSM  |
|15200690 |Kalter-Wangen-Fm.: Heilsberg-Bentonit | Bentonit  | –   | – |  Heilsberg-Bentonit |  Tortonien     | Langhien   | OSM  |
|15200691 |OSM: Humlikon-Bentonit | Bentonit  | –   | – |  Humlikon-Bentonit |  Tortonien     | Langhien   | OSM  |
|15200684 |Herdern-Streifengneis | Gneis: Biotit  | –   | – |  Herdern-Streifengneis |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202001 |Habkern-Melange | Mergelstein  | Tonstein   | – |  Habkern-Melange |  Eozän     | Späte Kreide   | Mélange  |
|15202002 |Sörenberg-Melange | Mergelstein  | Tonstein   | – |  Sörenberg-Melange |  Priabonien     | Priabonien   | Mélange  |
|15202003 |Wildhaus-Melange | Mergelstein  | –   | – |  Wildhaus-Melange |  Eozän     | Eozän   | Mélange  |
|15202004 |Südhelvetischer Flysch | Mergelstein  | Sandstein: kalkig   | Kalkstein: Nummuliten |  – |  Priabonien     | Lutétien   | Flysch  |
|15202005 |Nordhelvetische Flysch-Gr. | Sandstein: tonig  | Tonstein   | – |  – |  Rupélien     | Priabonien   | Flysch  |
|15202006 |Matt-Fm. | Sandstein: Quarz  | Tonstein: schiefrig   | Konglomerat: polymikt |  Matt-Formation |  Rupélien     | Rupélien   | Flysch  |
|15202007 |Matt-Fm.: Engi-Dachschiefer | Tonstein: schiefrig  | Sandstein: Quarz   | – |  Engi-Dachschiefer |  Rupélien     | Rupélien   | Flysch  |
|15202008 |Matt-Fm.: Gruontal-Konglomerat | Konglomerat: polymikt  | Brekzie   | – |  Gruontal-Konglomerat |  Rupélien     | Rupélien   | Flysch  |
|15202009 |Elm-Fm. | Tonstein: schiefrig  | Sandstein: tonig   | – |  Elm-Formation |  Rupélien     | Priabonien   | Flysch  |
|15202010 |Matt-Fm.: Gruontal-Konglomerat: Rüschenweid-Bk. | Sandstein  | –   | – |  Rüschenweid-Bank |  Rupélien     | Rupélien   | Flysch  |
|15202011 |Taveyannaz-Fm. | Sandstein: tonig  | Tonstein: schiefrig   | – |  Taveyannaz-Formation |  Rupélien     | Priabonien   | Flysch  |
|15202012 |Helvetikum: Paläogen | Kalkstein: Bioklasten  | Sandstein   | Mergelstein |  – |  Paläogen     | Paläogen   | Sedimentbedeckung  |
|15202013 |Stad-Fm. | Mergelstein: siltig  | –   | – |  Stad-Formation |  Priabonien     | Lutétien   | «Nummulitikum»  |
|15202014 |Stad-Fm.: Wängen-Kalk | Kalkstein: Bioklasten  | –   | – |  Wängen-Kalk |  Priabonien     | Lutétien   | «Nummulitikum»  |
|15202015 |Stad-Fm.: Jochstock-Konglomerat | Konglomerat: kalkig  | Brekzie: kalkig   | Mergelstein: sandig-kalkig |  Jochstock-Konglomerat |  Priabonien     | Priabonien   | Syn-Kollision  |
|15202016 |Sanetsch-Fm. | Kalkstein: sandig: Bioklasten  | Sandstein: kalkig   | – |  Sanetsch-Formation |  Rupélien     | Priabonien   | «Nummulitikum»  |
|15202017 |Sanetsch-Fm.: Pierredar-Kalk | Kalkstein: Bioklasten  | –   | – |  Pierredar-Kalk |  Rupélien     | Priabonien   | «Nummulitikum»  |
|15202018 |Sanetsch-Fm.: Tsanfleuron-Mb. | Sandstein: kalkig: Bioklasten  | Kalkstein: arenitisch   | – |  Tsanfleuron-Member |  Priabonien     | Priabonien   | «Nummulitikum»  |
|15202019 |Sanetsch-Fm.: Diablerets-Mb. | Kalkstein: sandig  | Mergelstein: Kohle   | – |  Diablerets-Member |  Frühes Priabonien     | Frühes Priabonien   | «Nummulitikum»  |
|15202020 |Niederhorn-Fm. | Sandstein: kalkig: Quarz  | Kalkstein: Bioklasten   | – |  Niederhorn-Formation |  Priabonien     | Bartonien   | «Nummulitikum»  |
|15202021 |Niederhorn-Fm.: Gemmenalp-Kalk | Kalkstein: Bioklasten  | –   | – |  Gemmenalp-Kalk |  Priabonien     | Bartonien   | «Nummulitikum»  |
|15202022 |Niederhorn-Fm.: Hohgant-Sandstein | Sandstein: kalkig: Quarz  | Sandstein: kalkig: Bioklasten   | – |  Hohgant-Sandstein |  Priabonien     | Bartonien   | «Nummulitikum»  |
|15202023 |Niederhorn-Fm.: Hohgant-Sandstein: Wagenmoos-Bk. | Sandstein: Quarz  | –   | – |  Wagenmoos-Bänke |  Priabonien     | Priabonien   | «Nummulitikum»  |
|15202024 |Wildstrubel-Fm. | Mergelstein: sandig-kalkig  | Sandstein: Glaukonit   | – |  Wildstrubel-Formation |  Priabonien     | Bartonien   | «Nummulitikum»  |
|15202025 |Wildstrubel-Fm.: Schimberg-Mb. | Mergelstein: sandig  | Sandstein: Quarz   | Konglomerat |  Schimberg-Member |  Priabonien     | Priabonien   | «Nummulitikum»  |
|15202026 |Wildstrubel-Fm.: Tierberg-Mb. | Sandstein: Glaukonit  | Mergelstein: sandig   | – |  Tierberg-Member |  Bartonien     | Bartonien   | «Nummulitikum»  |
|15202027 |Wildstrubel-Fm.: Küblibad-Mb. | Sandstein: Glaukonit  | –   | – |  Küblibad-Member |  Bartonien     | Bartonien   | «Nummulitikum»  |
|15203498 |Platta-Decke: Calpionellenkalk | 15111233  | Mergelstein   | – |  – |  Jura     | Jura   | Maiolica / Aptychenkalk  |
|15203495 |Tumpriv-Fm.: Solis-Kalk | Kalkstein: tonig: Chert  | –   | – |  Solis-Kalk |  Später Jura     | Früher Jura   | Sedimentbedeckung  |
|15203496 |Platta-Decke: Metasedimente | Gestein: sedimentär  | –   | – |  – |  Känozoikum     | Jura   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203497 |Flix-Sch. | Schiefer: tonig  | Schiefer: kieselig   | – |  Flix-Schichten |  Albien     | Aptien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203499 |Falotta-Radiolarit | Gestein: kieselig: Radiolarien  | Schiefer: tonig-kieselig   | Brekzie |  Falotta-Radiolarit |  Jura     | Jura   | Radiolarit  |
|15203500 |Platta-Decke: Ophiolith | Serpentinit  | Gabbro   | Basalt |  – |  Später Jura     | Mittlerer Jura   | Ophiolithische Abfolge  |
|15203501 |Vignun-Gneis | Gneis  | –   | – |  Vignun-Gneis |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203502 |Avers-Decke: Metasedimente | Gestein: sedimentär  | –   | – |  – |  Känozoikum     | Jura   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203503 |Avers-Decke: Ophiolith | Serpentinit  | Gabbro   | Basalt |  – |  Später Jura     | Mittlerer Jura   | Ophiolithische Abfolge  |
|15203504 |Tasna-Decke: Couches Rouges | Brekzie  | –   | – |  – |  Späte Kreide     | Albien   | Couches Rouges  |
|15203505 |Tasna-Decke: Tristel-Fm.: Minschun-Brekzie | Brekzie: polymikt  | –   | – |  Minschun-Brekzie (Tasna) |  Aptien     | Barrémien   | Couches Rouges  |
|15203506 |Tasna-Decke: Prävariszisches Grundgebrige | Gneis: sedimentär  | Schiefer   | Migmatit |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15203507 |Piz-del-Palo-Gneis | Gneis: augig  | Gneis: gebändert   | – |  Piz-del-Palo-Gneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203508 |Truzzo-Granit | Granit  | Gneis: augig   | – |  Truzzo-Granit |  Perm     | Karbon   | Variszisches Grundgebirge  |
|15203509 |Rebi-Gneis | Gneis  | Granit   | – |  Rebi-Gneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203510 |Brione-Gabbro | Gabbro  | –   | – |  Brione-Gabbro |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203511 |Gruf-Migmatit | Gneis: migmatitisch  | –   | – |  Gruf-Migmatit |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203512 |Adula-Decke: Basaler Gneis | Gneis: Biotit-Muskovit  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203513 |Val-Chironico-Gneis | Gneis: Biotit-Hornblende  | –   | – |  Val-Chironico-Gneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203514 |Ganna-Gneis | Gneis: schiefrig-augig  | –   | – |  Ganna-Gneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203515 |Adula-Decke: Albit-Oligoklasgneis | Gneis: Albit-Oligoklas  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203516 |Sivigia-Gneis | Gneis  | Schiefer: Glimmer-Granat   | – |  Sivigia-Gneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203517 |Aula-Spruga-Gneiskomplex | Gneis: Biotit  | Gneis: Hornblende   | – |  Aula-Spruga-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203518 |Lizun-Grünschiefer | 15111629  | Gabbro   | – |  Lizun-Prasinit |  Später Jura     | Mittlerer Jura   | Ophiolithische Abfolge  |
|15203519 |Rossi-Fm. | Schiefer: Glimmer-Granat  | –   | – |  Rossi-Formation |  Kreide     | Später Jura   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203520 |Bosco-Gneis | Gneis  | –   | – |  Bosco-Gneis |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203521 |Batnall-Gneis | Gneis: augig  | –   | – |  Batnall-Gneis |  Paläozoikum     | Paläozoikum   | Grundgebirge  |
|15203522 |Seron-Fm.: Sandig-kalkige Fazies | Kalkstein: sandig: Bioklasten  | –   | – |  Seron-Formation |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203523 |Seron-Fm.: Konglomerat-dominierte Fazies | Konglomerat: polymikt  | –   | – |  Seron-Formation |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203524 |Frutigen-Fm.: Konglomerat-dominierte Fazies | Konglomerat: polymikt  | Sandstein   | – |  Frutigen-Formation |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203525 |Frutigen-Fm.: Schiefrige Fazies | Tonstein: schiefrig  | Sandstein: kalkig   | Sandstein: tonig |  Frutigen-Formation |  Maastrichtien     | Maastrichtien   | Flysch  |
|15203526 |Zone Submédiane: Gips | Evaporit: Gips  | –   | – |  – |  Trias     | Trias   | Mélange  |
|15203527 |Zentralschweizerische Klippen: Keuper | Kalkstein: Korallen  | Tonstein   | – |  – |  Späte Trias     | Späte Trias   | Pelitische Trias  |
|15203528 |Zwischenmythen-Mergel | Mergelstein: sandig: Glimmer  | –   | – |  Zwischenmythen-Mergel |  Späte Trias     | Späte Trias   | Pelitische Trias  |
|15203529 |Arosa-Decke: Cenomanbrekzien-Serie | Brekzie  | Tonstein: schiefrig   | Mergelstein |  «Cenomanbrekzien-Serie» |  Cénomanien     | Cénomanien   | Post-Rift Mesozoikum in detritischer Fazies  |
|15203530 |Arosa-Decke: Bettlerjoch-Brekzie | Brekzie  | –   | – |  Bettlerjoch-Brekzie |  Mesozoikum     | Mesozoikum   | Post-Rift Mesozoikum in detritischer Fazies  |
|15203531 |Arosa-Decke: Bargella-Brekzie | Brekzie  | –   | – |  Bargella-Brekzie |  Cénomanien     | Cénomanien   | Post-Rift Mesozoikum in detritischer Fazies  |
|15203532 |Adula-Decke: Kalkschiefer und Marmor | Schiefer: kalkig  | Marmor: kalkig   | – |  – |  Mesozoikum     | Mesozoikum   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203533 |Salahorn-Fm.: Metaplutonit | Gestein: plutonisch  | –   | – |  Salahorn-Formation |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203534 |Salahorn-Fm.: Paragneis | Gneis: sedimentär  | –   | – |  Salahorn-Formation |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203535 |Adula-Decke: Ultramafisches Gestein | Gestein: ultramafisch  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203536 |Cima-Lunga-Decke: Kalkschiefer und Marmor | Schiefer: kalkig  | Marmor: kalkig   | – |  – |  Mesozoikum     | Mesozoikum   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15203537 |Cima-Lunga-Decke: Dolomitmarmor | Marmor: dolomitisch  | –   | – |  – |  Trias     | Trias   | Karbonatische Trias  |
|15203538 |Cima-Lunga-Decke: Paragneis | Gneis: sedimentär  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203539 |Vacarisc-Gneis | Gneis  | –   | – |  Vacarisc-Gneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203540 |Rognoi-Gneis | Gneis  | –   | – |  Rognoi-Gneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203541 |Cima-Lunga-Decke: Granatit | Granofels: Granat  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203542 |Cima-Lunga-Decke: Amphibolit | Amphibolit  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203543 |Cima-Lunga-Decke: Eklogit | Eklogit  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203544 |Cima-Lunga-Decke: Ultramafisches Gestein | Gestein: ultramafisch  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203545 |Personico-Gneis | Gneis  | Granit   | – |  Personico-Gneis |  Perm     | Karbon   | Grundgebirge  |
|15203546 |Leventina-Gneis: Oberer Teil | Gneis: Biotit-Muskovit  | Granit   | – |  Leventina-Gneis |  Perm     | Karbon   | Grundgebirge  |
|15203547 |Leventina-Gneis: Unterer Teil | Gneis  | Granit   | – |  Leventina-Gneis |  Perm     | Karbon   | Grundgebirge  |
|15203548 |Leventina-Decke: Kalksilikatfels | Granofels: Kalksilikat  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203549 |Leventina-Decke: Leukogneis | Gneis  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203550 |Leventina-Decke: Paragneis | Gneis: sedimentär  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203551 |Leventina-Decke: Amphibolit | Amphibolit  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203552 |Maggia-Decke: Amphibolit | Amphibolit  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15203553 |Simano-Decke: Kalkmarmor | Marmor: kalkig  | –   | – |  – |  Mesozoikum     | Mesozoikum   | Grundgebirge  |
|15203554 |Simano-Decke: Dolomitmarmor | Marmor: dolomitisch  | –   | – |  – |  Trias     | Trias   | Grundgebirge  |
|15203555 |Simano-Decke: Paragneis | Gneis: sedimentär  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203556 |Renten-Gneis | Gneis  | –   | – |  Renten-Gneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203557 |Legiuna-Gneis | Gneis: augig  | –   | – |  Legiuna-Gneis |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15203558 |Simano-Decke: Amphibolit | Amphibolit  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Grundgebirge  |
|15204129 |Ostalpin: Jura | Gestein: kieselig: Radiolarien  | Kalkstein: mikritisch: Bioklasten   | Tonstein |  – |  Jura     | Jura   | Sedimentbedeckung  |
|15202441 |Bretaye-Fm. | Tonstein: siltig: Glimmer  | –   | – |  Formation de Bretaye |  Aalénien     | Aalénien   | Syn-Rift  |
|15203091 |Mytilus-Sch.: Col-de-Cordon-Mb.: Holzerhorn-Einheit | Mergelstein: sandig: Kohle  | Kalkstein: sandig: Bioklasten   | Konglomerat |  Holzerhorn-Einheit |  Callovien     | Aalénien   | Lias-Dogger in neritischer Fazies  |
|15204128 |Ostalpin: Postvariszische Vulkanite und Sedimente | Gestein: vulkanisch  | Gestein: sedimentär   | – |  – |  Perm     | Karbon   | Spät- bis postvariszisches Grundgebirge  |
|15202342 |Streifengneis-Komplex: Hüenerstock-Gneis | Gneis: granitisch  | –   | – |  Hüenerstock-Gneis |  Paläozoikum     | Paläozoikum   | Prävariszisches Grundgebirge  |
|15202345 |Paradis-Gneiskomplex: Val-Camadra-Migmatit | Gneis: migmatitisch  | –   | – |  Val-Camadra-Migmatit |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202502 |Ilanz-Verrucano s.s. | Sandstein  | Konglomerat   | – |  – |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15202503 |Ilanz-Verrucano: Buntgefleckte Schiefer | Schiefer  | Phyllit   | – |  – |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15202504 |Tavetsch-Decke: Perm | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15202254 |Ilanz-Zone: Permische Sedimente | Konglomerat  | Sandstein   | Gestein: pelitisch |  – |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15202257 |Oberaar Furka Zone | Gneis  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202258 |Ausserberg-Avat-Zone | Gneis  | Migmatit   | Schiefer |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15200596 |Helvetischer Flysch | Sandstein  | Tonstein   | – |  – |  Rupélien     | Lutétien   | Flysch  |
|15200597 |Euthal- bis Stad-Fm. | Kalkstein: Bioklasten  | Sandstein   | Mergelstein |  – |  Priabonien     | Sélandien   | «Nummulitikum»  |
|15200598 |Stad- und Muot-da-Rubi-Fm. | Mergelstein  | Sandstein   | – |  – |  Priabonien     | Lutétien   | Sedimentbedeckung  |
|15200599 |Euthal- bis Sanetsch-Fm. | Kalkstein: Bioklasten  | Sandstein   | Mergelstein |  – |  Rupélien     | Sélandien   | «Nummulitikum»  |
|15202260 |Ausserberg-Avat-Zone: Granitischer Gneis | Gneis: granitisch  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202261 |Ausserberg-Avat-Zone: Paragneis | Gneis: sedimentär  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202262 |Clavaniev-Zone | Gestein: tektonisch  | –   | – |  – |  Paläozoikum     | Proterozoikum   | Spät- bis postvariszisches Grundgebirge  |
|15202649 |Nufenen-Zone | Schiefer: tonig  | Schiefer: kalkig   | Quarzit |  – |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15202268 |Ausserbinn-Piz-Cavel-Zone | Gneis  | Amphibolit   | Schiefer |  – |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202650 |Termen-Zone | Schiefer: tonig  | Schiefer: kalkig   | – |  – |  Mesozoikum     | Mesozoikum   | Sedimentbedeckung  |
|15203671 |Salahorn-Fm. | Schiefer: Glimmer  | Gneis: sedimentär   | – |  Salahorn-Formation |  Kambrium     | Kambrium   | Grundgebirge  |
|15200607 |Etiollets- Reuchenette- und Twannbach-Fm. | Kalkstein: mikritisch  | Mergelstein   | – |  – |  Tithonien     | Kimméridgien   | Malm  |
|15200608 |Bärschwil-, St-Ursanne-, Pichoux- und Wildegg-Fm. | Mergelstein  | Kalkstein   | Tonstein |  – |  Oxfordien     | Oxfordien   | Malm  |
|15203672 |Col-de-Tompey- und Vudalla-Fm. | Mergelstein  | Kalkstein   | Sandstein: kalkig |  – |  Hettangien     | Rhät   | Lias-Dogger in neritischer Fazies  |
|15202407 |Punteglias-Granit: Posta-Biala-Granit | Granit  | –   | – |  Posta-Biala-Granit |  Mittleres Mississippien     | Mittleres Mississippien   | Prävariszisches Grundgebirge  |
|15202280 |Sardona-Decke: Melange | Mergelstein  | Sandstein   | – |  – |  Tertiär     | Späte Kreide   | Mélange  |
|15202409 |Punteglias-Granit: Val-Punteglias-Diorit | Diorit: Biotit-Hornblende  | Diorit: monzonitisch   | Monzonit: Quarz |  Val-Punteglias-Diorit |  Viséen     | Viséen   | Prävariszisches Grundgebirge  |
|15200379 |15200379 | Mergelstein  | Siltstein   | Sandstein: Glimmer |  «Elsässer-Molasse» |  Chattien     | Chattien   | USM  |
|15200381 |Hauptogenstein: Mittlerer Teil | Mergelstein  | Kalkstein: mergelig   | – |  Hauptrogenstein |  Bathonien     | Bajocien   | Lias-Dogger in neritischer Fazies  |
|15205001 |Dent-Blanche-Decke: Sedimentbedeckung | Brekzie  | Dolomitstein   | Sandstein |  – |  Mittlerer Jura     | Trias   | Sedimentbedeckung  |
|15205002 |Petit-Dolin-Kalkbrekzie | Brekzie: kalkig-dolomitisch  | –   | – |  Petit-Dolin-Kalkbrekzie |  Mittlerer Jura     | Früher Jura   | Lias-Dogger in neritischer Fazies  |
|15205003 |Roisan-Cignana-Zone | Marmor  | Schiefer   | – |  – |  Mittlere Trias     | Perm   | Sedimentbedeckung  |
|15205004 |Arolla-Einheit | Gneis: gebändert  | Schiefer: Glimmer   | – |  – |  Cisuralien     | Cisuralien   | Grundgebirge  |
|15205005 |Mont-Collon-Gabbro | 15111449  | –   | – |  Mont-Collon-Gabbro |  Cisuralien     | Cisuralien   | Variszisches Grundgebirge  |
|15205006 |Arolla-Orthogneis | Gneis: granitisch  | –   | – |  Arolla-Orthogneis |  Perm     | Perm   | Variszisches Grundgebirge  |
|15205007 |Valpelline-Einheit | 15111557  | Gneis: granulitisch   | – |  – |  Paläogen     | Proterozoikum   | Grundgebirge  |
|15205008 |Castel-di-Sotto-Ton | Tonstein  | Mergelstein   | Siltstein |  Castel-di-Sotto-Ton |  Zancléen     | Zancléen   | Post-Messinien  |
|15205009 |Pontegana-Konglomerat | Konglomerat: kalkig  | Sandstein   | – |  Pontegana-Konglomerat |  Messinien     | Messinien   | Post-Kollision  |
|15205010 |Lombardischer Gompholith | Konglomerat  | Sandstein   | Tonstein |  – |  Langhien     | Chattien   | Lombardischer Gompholit  |
|15205011 |Lucino-Konglomerat | Konglomerat  | Sandstein   | Tonstein |  Lucino-Konglomerat |  Langhien     | Burdigalien   | Lombardischer Gompholit  |
|15205012 |Lucino-Konglomerat: Cagno-Sandstein | Sandstein  | Konglomerat   | – |  Cagno-Sandstein |  Langhien     | Burdigalien   | Lombardischer Gompholit  |
|15205013 |Como-Konglomerat: Val-Grande-Sandstein | Sandstein  | Sandstein: konglomeratisch   | Tonstein |  Val-Grande-Sandstein |  Burdigalien     | Burdigalien   | Lombardischer Gompholit  |
|15205014 |Como-Konglomerat: Prestino-Pelite | Tonstein  | Siltstein   | Sandstein |  Prestino-Pelite |  Aquitanien     | Aquitanien   | Lombardischer Gompholit  |
|15205015 |Como-Konglomerat | Konglomerat: polymikt  | Sandstein   | Tonstein |  Como-Konglomerat |  Burdigalien     | Chattien   | Lombardischer Gompholit  |
|15205016 |Como-Konglomerat: Malnate-Sandstein | Sandstein  | Sandstein: konglomeratisch   | Tonstein |  Malnate-Sandstein |  Burdigalien     | Burdigalien   | Lombardischer Gompholit  |
|15205017 |Como-Konglomerat: Rio-dei-Gioghi-Pelite | Tonstein  | Siltstein   | Sandstein |  Rio-dei-Gioghi-Pelite |  Aquitanien     | Aquitanien   | Lombardischer Gompholit  |
|15205018 |Chiasso-Fm. | Tonstein  | Sandstein   | Konglomerat |  Chiasso-Formation |  Chattien     | Chattien   | Lombardischer Gompholit  |
|15205019 |Chiasso-Fm: Villa-Olmo-Konglomerat | Konglomerat: polymikt  | Sandstein   | Tonstein |  Villa-Olmo-Konglomerat |  Chattien     | Chattien   | Lombardischer Gompholit  |
|15205020 |Ternate-Fm. | Kalkstein: arenitisch: Bioklasten  | Mergelstein   | – |  Ternate-Formation |  Priabonien     | Priabonien   | Post-Kollision in pelagischer Fazies  |
|15205021 |Brenno-Fm. | Kalkstein: mikritisch  | Kalkstein: arenitisch   | – |  Brenno-Formation |  Maastrichtien     | Campanien   | Post-Kollision in pelagischer Fazies  |
|15205022 |Prella-Konglomerat | Konglomerat: polymikt  | Kalkstein: arenitisch   | Kalkstein: mikritisch |  Prella-Konglomerat |  Campanien     | Campanien   | Post-Kollision in pelagischer Fazies  |
|15205023 |Südalpin: Flysch | Sandstein  | Konglomerat: polymikt   | Kalkstein |  – |  Campanien     | Cénomanien   | Flysch  |
|15205024 |Bergamo-Flysch | Tonstein  | Kalkstein: arenitisch   | – |  Bergamo-Flysch |  Campanien     | Santonien   | Flysch  |
|15205025 |Coldrerio-Flysch | Sandstein  | Siltstein   | Mergelstein |  Coldrerio-Flysch |  Campanien     | Santonien   | Flysch  |
|15205026 |Torre-Konglomerat | Konglomerat: polymikt  | Sandstein   | – |  Torre-Konglomerat |  Santonien     | Santonien   | Flysch  |
|15205027 |Varesotto-Flysch | Sandstein  | Siltstein   | Mergelstein |  Varesotto-Flysch |  Santonien     | Cénomanien   | Flysch  |
|15205028 |Scaglia Lombarda | Kalkstein: mergelig  | Mergelstein   | – |  – |  Cénomanien     | Aptien   | Scaglia  |
|15205029 |Scaglia Rossa Lombarda | Kalkstein: mergelig  | Mergelstein   | – |  «Scaglia Rossa Lombarda» |  Cénomanien     | Cénomanien   | Scaglia  |
|15205030 |Scaglia Bianca Lombarda | Kalkstein: mergelig  | Mergelstein   | Tonstein: schiefrig: Bitumen |  «Scaglia Bianca Lombarda» |  Albien     | Albien   | Scaglia  |
|15205031 |Scaglia Variegata Lombarda | Kalkstein: mergelig  | Mergelstein   | Tonstein: schiefrig: Bitumen |  «Scaglia Variegata Lombarda» |  Albien     | Aptien   | Scaglia  |
|15202031 |Klimsenhorn-Fm.: Fräkmünt-Mb. | Sandstein: Quarz-Glaukonit  | Kalkstein: mikritisch   | Sandstein: kalkig: Bioklasten |  Fräkmünt-Member |  Bartonien     | Lutétien   | «Nummulitikum»  |
|15202028 |Klimsenhorn-Fm. | Sandstein: Quarz  | Kalkstein: sandig   | Kalkstein: mikritisch |  Klimsenhorn-Formation |  Bartonien     | Lutétien   | «Nummulitikum»  |
|15202029 |Klimsenhorn-Fm.: Fruttli-Mb. | Kalkstein: mikritisch  | Sandstein: kalkig: Bioklasten   | Kalkstein: sandig: Bioklasten |  Fruttli-Member |  Lutétien     | Lutétien   | «Nummulitikum»  |
|15202030 |Klimsenhorn-Fm.: Band-Mb. | Sandstein: Quarz  | Sandstein: kalkig   | Kalkstein |  Band-Member |  Bartonien     | Lutétien   | «Nummulitikum»  |
|15202032 |Bürgen-Fm. | Kalkstein: mikritisch  | Kalkstein: sandig: Glaukonit   | Mergelstein: Bioklasten |  Bürgen-Formation |  Lutétien     | Lutétien   | «Nummulitikum»  |
|15202033 |Bürgen-Fm.: Foribach-Mb. | Kalkstein: sandig: Glaukonit  | Kalkstein: mikritisch: Bioklasten   | – |  Foribach-Member |  Lutétien     | Lutétien   | «Nummulitikum»  |
|15202034 |Bürgen-Fm.: Mattgrat-Mb. | Kalkstein: mikritisch: Bioklasten  | –   | – |  Mattgrat-Member |  Lutétien     | Lutétien   | «Nummulitikum»  |
|15202035 |Bürgen-Fm.: Scharti-Mb. | Sandstein: kalkig: Glaukonit  | Kalkstein: sandig: Bioklasten   | Mergelstein |  Scharti-Member |  Lutétien     | Lutétien   | «Nummulitikum»  |
|15202036 |Euthal-Fm. | Kalkstein: Nummuliten  | Sandstein: Quarz-Glaukonit   | – |  Euthal-Formation |  Lutétien     | Sélandien   | «Nummulitikum»  |
|15202037 |Bürgen-Fm.: Steinbach-Mb. | Sandstein: Glaukonit  | Kalkstein: Bioklasten   | – |  Steinbach-Member |  Lutétien     | Lutétien   | «Nummulitikum»  |
|15202038 |Euthal-Fm.: Einsiedeln-Mb. | Kalkstein: Nummuliten  | Sandstein: kalkig: Glaukonit   | – |  Einsiedeln-Member |  Lutétien     | Yprésien   | «Nummulitikum»  |
|15202039 |Euthal-Fm.: Batöni-Mb. | Sandstein: Quarz-Glaukonit  | –   | – |  Batöni-Member |  Yprésien     | Thanétien   | «Nummulitikum»  |
|15202040 |Euthal-Fm.: Chruteren-Mb. | Sandstein: Glaukonit  | Kalkstein: spätig: Bioklasten   | Kalkstein: Algen |  Chruteren-Member |  Yprésien     | Thanétien   | «Nummulitikum»  |
|15202041 |Euthal-Fm.: Fliegenspitz-Mb. | Mergelstein: sandig  | –   | – |  Fliegenspitz-Member |  Thanétien     | Sélandien   | «Nummulitikum»  |
|15202043 |Siderolithikum: Grindelwald-Marmor | Brekzie: kalkig  | –   | – |  Grindelwald-Marmor |  Mittleres Eozän     | Mittleres Eozän   | Siderolithikum  |
|15202044 |Niederhorn-Fm.: Hohgant-Sandstein: Mürren-Brekzie | Brekzie: kalkig: Bioklasten  | –   | – |  Mürren-Brekzie |  Priabonien     | Priabonien   | «Nummulitikum»  |
|15202045 |Siderolithikum: Dünden-Konglomerat | Konglomerat: kalkig-residual: Eisenpisoide  | –   | – |  Dünden-Konglomerat |  Mittleres Eozän     | Mittleres Eozän   | Siderolithikum  |
|15202046 |Siderolithikum: Rosenlaui-Marmor | Brekzie: kalkig  | –   | – |  Rosenlaui-Marmor |  Mittleres Eozän     | Mittleres Eozän   | Siderolithikum  |
|15202047 |Helvetikum: Kreide | Kalkstein  | Mergelstein   | Sandstein |  – |  Kreide     | Kreide   | Post-Rift  |
|15202048 |Wang-Fm. | Kalkstein: sandig-kieselig  | Mergelstein   | – |  Wang-Formation |  Maastrichtien     | Campanien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202049 |Amden-Fm. | Mergelstein: Bioklasten  | Siltstein: kalkig   | – |  Amden-Mergel |  Campanien     | Santonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202050 |Seewen Fm. | Kalkstein: mikritisch  | Mergelstein   | – |  Seewen-Formation |  Santonien     | Cénomanien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202051 |Seewen-Fm.: Choltal-Mb. | Mergelstein: kalkig  | Kalkstein: mikritisch   | – |  Choltal-Member |  Santonien     | Santonien   | Post-Rift Mesozoikum in pelagischer Fazies  |
|15202052 |Garschella-Fm. | Sandstein: Glaukonit  | Kalkstein: spätig: Bioklasten   | Mergelstein: sandig |  Garschella-Formation |  Cénomanien     | Aptien   | «Gault»  |
|15202053 |Garschella-Fm.: Selun-Mb. | Sandstein: Glaukonit  | Kalkstein: sandig-tonig   | Kalkstein: sandig: Bioklasten |  Selun-Member |  Cénomanien     | Aptien   | «Gault»  |
|15202054 |Garschella-Fm.: Selun-Mb.: Kamm-Bk. | Kalkstein: mikritisch: Bioklasten  | Kalkstein: spätig: Bioklasten   | – |  Kamm-Bank |  Cénomanien     | Albien   | «Gault»  |
|15202055 |Garschella-Fm.: Selun-Mb.: Aubrig-Sch. | Kalkstein: sandig: Glaukonit  | Sandstein: Quarz-Glaukonit   | – |  Aubrig-Schichten |  Cénomanien     | Albien   | «Gault»  |
|15202056 |Garschella-Fm.: Selun-Mb.: Wannenalp-Bk. | Sandstein: Glaukonit  | –   | – |  Wannenalp-Bank |  Albien     | Albien   | «Gault»  |
|15202057 |Garschella-Fm.: Selun-Mb.: Sellamatt-Sch. | Kalkstein: spätig: Glaukonit  | Kalkstein: mergelig   | Siltstein: kalkig |  Sellamatt-Schichten |  Albien     | Albien   | «Gault»  |
|15202058 |Garschella-Fm.: Selun-Mb.: Plattenwald-Bk. | Kalkstein: mikritisch: Bioklasten  | –   | – |  Plattenwald-Bank |  Albien     | Aptien   | «Gault»  |
|15202059 |Garschella-Fm.: Selun-Mb.: Durschlägi-Bk. | Sandstein: Glaukonit  | –   | – |  Durschlägi-Bank |  Albien     | Albien   | «Gault»  |
|15202060 |Garschella-Fm.: Selun-Mb.: Niederi-Sch. | Sandstein: Glaukonit  | –   | – |  Niederi-Schichten |  Albien     | Albien   | «Gault»  |
|15202061 |Garschella-Fm.: Selun-Mb.: Twäriberg-Bk. | Sandstein: Quarz-Glaukonit  | –   | – |  Twäriberg-Bank |  Albien     | Aptien   | «Gault»  |
|15202062 |Garschella-Fm.: Selun-Mb.: Klaus-Bk. | Sandstein: Glaukonit  | Kalkstein: mikritisch   | – |  Klaus-Bank |  Albien     | Aptien   | «Gault»  |
|15202063 |Garschella-Fm.: Rankweil-Mb. | Sandstein: Glaukonit  | –   | – |  Rankweil-Member |  Albien     | Aptien   | «Gault»  |
|15202064 |Garschella-Fm.: Brisi-Mb. | Sandstein: Quarz-Glaukonit  | Kalkstein: sandig: Bioklasten   | – |  Brisi-Member |  Aptien     | Aptien   | «Gault»  |
|15202065 |Garschella-Fm.: Brisi-Mb.: Kalkige Fazies | Kalkstein: sandig: Bioklasten  | Kalkstein: spätig: Bioklasten   | – |  Brisi-Member |  Aptien     | Aptien   | «Gault»  |
|15202066 |Garschella-Fm.: Brisi-Mb.: Sandige Fazies | Sandstein: Quarz-Glaukonit  | –   | – |  Brisi-Member |  Aptien     | Aptien   | «Gault»  |
|15202067 |Garschella-Fm.: Brisi-Mb.: Gams-Sch. | Sandstein: tonig: Glaukonit  | Mergelstein: kalkig-schiefrig   | – |  Gams-Schichten |  Aptien     | Aptien   | «Gault»  |
|15202068 |Garschella-Fm.: Brisi-Mb.: Luitere-Bk. | Sandstein: mergelig: Glaukonit  | –   | – |  Luitere-Bank |  Aptien     | Aptien   | «Gault»  |
|15202069 |Garschella-Fm.: Freschen-Mb. | Tonstein: mergelig  | Sandstein   | Kalkstein |  Freschen-Member |  Albien     | Albien   | «Gault»  |
|15202070 |Garschella-Fm.: Freschen-Mb.: Hochkugel-Sch. | Kalkstein: kieselig  | Tonstein: mergelig   | – |  Hochkugel-Schichten |  Aptien     | Aptien   | «Gault»  |
|15202071 |Garschella-Fm.: Grünten-Mb. | Mergelstein: sandig: Glaukonit  | Kalkstein: sandig   | Kalkstein: spätig: Bioklasten |  Grünten-Member |  Aptien     | Aptien   | «Gault»  |
|15202072 |Garschella-Fm.: Grünten-Mb.: Rohrbachstein-Bk. | Kalkstein: arenitisch: Glaukonit  | –   | – |  Rohrbachstein-Bank |  Aptien     | Aptien   | «Gault»  |
|15202073 |Schrattenkalk-Fm. | Kalkstein: Bioklasten  | –   | – |  Schrattenkalk-Formation |  Aptien     | Barrémien   | «Urgonien»  |
|15202074 |Schrattenkalk-Fm.: Rawil-Mb. | Kalkstein: mergelig: Bioklasten  | Mergelstein   | – |  Rawil-Member |  Aptien     | Aptien   | «Urgonien»  |
|15202075 |Tierwis-Fm. | Mergelstein: Glaukonit  | Kalkstein: kieselig   | – |  Tierwis-Formation |  Barrémien     | Hauterivien   | «Urgonien»  |
|15202076 |Tierwis-Fm.: Chopf-Bk. | Kalkstein: sandig  | Mergelstein: Glaukonit-Bioklasten   | – |  Chopf-Bank |  Barrémien     | Barrémien   | «Urgonien»  |
|15202077 |Tierwis-Fm.: Drusberg-Mb. | Mergelstein  | Kalkstein: kieselig   | – |  Drusberg-Member |  Barrémien     | Barrémien   | «Urgonien»  |
|15202078 |Tierwis-Fm.: Altmann-Mb. | Mergelstein: sandig: Glaukonit  | Kalkstein: sandig   | – |  Altmann-Member |  Barrémien     | Hauterivien   | «Urgonien»  |
|15202079 |Helvetischer Kieselkalk | Kalkstein: kieselig: Bioklasten  | Mergelstein: kieselig   | – |  15253100 |  Hauterivien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202080 |Helvetischer Kieselkalk: Chriesiloch-Echinodermenkalk | Kalkstein: spätig: Bioklasten  | –   | – |  Chriesiloch-Echinodermenkalk |  Hauterivien     | Hauterivien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202081 |Helvetischer Kieselkalk: Lidernen-Mb. | Kalkstein: sandig: Glaukonit  | Mergelstein   | – |  Lidernen-Member |  Hauterivien     | Hauterivien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202082 |Helvetischer Kieselkalk: Gemsmättli-Bk. | Kalkstein: mikritisch: Glaukonit  | Kalkstein: sandig: Bioklasten   | – |  Gemsmättli-Bank |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202083 |Helvetischer Kieselkalk: Rahberg-Bk. | Kalkstein: sandig: Glaukonit  | –   | – |  Rahberg-Bank |  Hauterivien     | Hauterivien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202084 |Betlis-Fm. | Kalkstein: spätig: Bioklasten-Chert  | Mergelstein   | – |  Betlis-Formation |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202085 |Betlis-Fm.: Pygurus-Mb. | Kalkstein: sandig-spätig  | –   | – |  «Pygurus-Member» |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202086 |Betlis-Fm.: Spitzern-Mb. | Kalkstein  | Mergelstein   | – |  Spitzern-Member |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202087 |Betlis-Fm.: Büls-Bk. | Kalkstein: sandig: Glaukonit  | Mergelstein   | – |  Büls-Bank |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202088 |Sichel-Kalk | Kalkstein: mikritisch: Bioklasten-Chert  | –   | – |  Sichel-Kalk |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202089 |Diphyoides-Kalk | Kalkstein: mikritisch  | –   | – |  15253114 |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202090 |Vitznau-Mergel | Mergelstein  | Kalkstein: mikritisch: Bioklasten   | – |  Vitznau-Mergel |  Valanginien     | Valanginien   | Post-Rift Mesozoikum in Plattform-Fazies  |
|15202155 |Vernayaz-Fm.: Salvan-Mb. | Sandstein  | –   | – |  Salvan-Member |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202152 |Üblital-Fm. | Brekzie  | Tonstein   | Gestein: basisch-vulkanisch |  Üblital-Formation |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202153 |Ilanz-Verrucano | Schiefer  | Gneis   | – |  – |  Perm     | Perm   | Spät- bis postvariszisches Grundgebirge  |
|15202154 |Vernayaz-Fm. | Sandstein  | Tonstein   | Konglomerat |  Vernayaz-Formation |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202156 |Vernayaz-Fm.: Salvan-Mb.: Vallorcine-Konglomerat | Konglomerat  | –   | – |  Vallorcine-Konglomerat |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202157 |Aar-Massiv: Spät- bis postvariszische Intrusiva | Gestein: plutonisch  | –   | – |  – |  Asselien     | Asselien   | Spät- bis postvariszisches Grundgebirge  |
|15202158 |Gastern-Granit | Granit: Biotit  | –   | – |  Gastern-Granit |  Asselien     | Spätes Pennsylvanien   | Frühvariszisches Grundgebirge  |
|15202159 |Mittagflue-Granit | Granit: Biotit  | Granit: mylonitisch   | – |  Mittagfluh-Granit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202160 |Zentraler Aare-Granit | Granit: Biotit  | Granit: schiefrig   | – |  Zentraler Aare-Granit |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202161 |Grimsel-Granodiorit | Granodiorit: porphyrisch  | Granit: Biotit   | Gneis: augig |  Grimsel-Granodiorit |  Spätes Pennsylvanien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202162 |Südwestlicher Aare-Granit | Granit  | Granit: schiefrig   | – |  «Südwestlicher Aare-Granit» |  Cisuralien     | Cisuralien   | Spät- bis postvariszisches Grundgebirge  |
|15202163 |Bugnei-Granodiorit | Granodiorit  | –   | – |  Bugnei-Granodiorit |  Mittleres Pennsylvanien     | Mittleres Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202164 |Aar-Massiv: Spät- bis postvariszische Sedimente und Vulkanite | Gestein: sedimentär  | Gestein: vulkanisch   | – |  – |  Cisuralien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202165 |Wendenjoch-Fm. | Schiefer: tonig: Graphit  | Sandstein   | Konglomerat |  Wendenjoch-Formation |  Cisuralien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202166 |Windgällen-Fm. | Granit: mikrokristallin-porphyrisch  | Rhyolith: ignimbritisch   | Schiefer: tonig |  Windgällen-Formation |  Cisuralien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202167 |Trift-Fm. | Schiefer: tonig  | Konglomerat   | Gestein: pyroklastisch |  Trift-Formation |  Cisuralien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202168 |Intschi-Fm. | Rhyolith  | Ignimbrit   | Schiefer: tonig: Graphit |  Intschi-Formation |  Cisuralien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202169 |Bifertengrätli-Fm. | Konglomerat  | Sandstein: Feldspat   | Schiefer: tonig: Graphit |  Bifertengrätli-Formation |  Cisuralien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202170 |Bifertengrätli-Fm.: Lakustrisches Mb. | Sandstein  | Siltstein: schiefrig   | Tonstein |  «Lakustrisches Member» (Bifertengrätli-Fm.) |  Cisuralien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202171 |Bifertengrätli-Fm.: Estuarisches Mb. | Konglomerat  | Sandstein   | Tonstein: Anthrazit |  «Estuarisches Member» (Bifertengrätli-Fm.) |  Cisuralien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202172 |Bifertengrätli-Fm.: Grünhorn-Mb.: Basales Konglomerat | Konglomerat  | –   | – |  «Basales Konglomerat» (Bifertengrätli-Fm.) |  Cisuralien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202173 |Bifertengrätli-Fm.: Grünhorn-Mb. | Konglomerat  | Sandstein: Quarz   | Tuffit |  Grünhorn-Member |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202174 |Diechtergletscher-Fm. | Schiefer: tonig  | Gestein: pyroklastisch   | – |  Diechtergletscher-Formation |  Cisuralien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202175 |Tscharren-Fm. | Ignimbrit  | Tuffit   | Konglomerat |  Tscharren-Formation |  Cisuralien     | Spätes Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202177 |Aar-Massiv: Mittelvariszische Intrusiva | Gestein: plutonisch  | –   | – |  – |  Mittleres Pennsylvanien     | Mittleres Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202178 |Brunni-Granit | Granit  | –   | – |  Brunni-Granit |  Mittleres Pennsylvanien     | Mittleres Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202179 |Düssi-Diorit | Diorit  | Aplit   | Pegmatit |  Düssi-Diorit |  Mittleres Pennsylvanien     | Mittleres Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202180 |Munt-Dado-Granit | Granit  | –   | – |  Munt-Dado-Granit |  Mittleres Pennsylvanien     | Mittleres Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202181 |Russein-Diorit | Diorit  | –   | – |  Russein-Diorit |  Mittleres Pennsylvanien     | Frühes Pennsylvanien   | Frühvariszisches Grundgebirge  |
|15202182 |Voralp-Granit | Granit: Biotit  | –   | – |  Voralp-Granit |  Pennsylvanien     | Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202183 |Aar-Massiv: Frühvariszische Intrusiva | Gestein: plutonisch  | –   | – |  – |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15202184 |Punteglias-Granit | Granit: porphyrisch: Hornblende  | –   | – |  Punteglias-Granit |  Mittleres Mississippien     | Mittleres Mississippien   | Prävariszisches Grundgebirge  |
|15202185 |Tödi-Granit | Granit  | Granit: Hornblende   | – |  Tödi-Granit |  Mittleres Mississippien     | Mittleres Mississippien   | Frühvariszisches Grundgebirge  |
|15202186 |Strem-Granit | Granit  | Granit: mylonitisch   | – |  Strem-Granit |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202187 |Baltschieder-Granodiorit | Granodiorit  | –   | – |  Baltschieder-Granodiorit |  Mississippien     | Mississippien   | Prävariszisches Grundgebirge  |
|15202188 |Giuv-Syenit | Syenit: porphyrisch: Quarz  | Monzonit: porphyrisch: Quarz   | – |  Giuv-Syenit |  Mittleres Mississippien     | Mittleres Mississippien   | Frühvariszisches Grundgebirge  |
|15202189 |Curtin-Monzodiorit | Monzonit: Quarz  | Syenit: Quarz   | – |  Curtin-Monzodiorit |  Mississippien     | Mississippien   | Frühvariszisches Grundgebirge  |
|15202190 |Bristenstock-Syenit | Syenit: Quarz-Hornblende  | –   | – |  Bristenstock-Syenit |  Mittleres Mississippien     | Mittleres Mississippien   | Mittelvariszisches Grundgebirge  |
|15202191 |Aar-Massiv: Frühvariszische Sedimente | Gestein: sedimentär  | –   | – |  – |  Mississippien     | Paläozoikum   | Frühvariszisches Grundgebirge  |
|15202192 |Val-Gliems-Fm. | Ignimbrit  | Tuffit   | Konglomerat |  Val-Gliems-Formation |  Mississippien     | Paläozoikum   | Frühvariszisches Grundgebirge  |
|15202193 |Bifertenfirn-Fm. | Schiefer: tonig: Anthrazit  | Gneis   | – |  Bifertenfirn-Formation |  Mississippien     | Paläozoikum   | Frühvariszisches Grundgebirge  |
|15202194 |Aar-Massiv: Prävariszisches polyzyklisches Grundgebirge | Gneis  | Schiefer   | – |  – |  Devon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202195 |Innertkirchen-Migmatit | Migmatit: Cordierit  | Gneis: migmatitisch   | Amphibolit |  Innertkirchen-Migmatit |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202196 |Innertkirchen-Migmatit: Zäsenberg-Gneis | Gneis  | –   | – |  Zäsenberg-Gneis |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202197 |Erstfeld-Gneiskomplex | Gneis: migmatitisch  | Gneis: granitisch   | Schiefer |  Erstfeld-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202198 |Guttannen-Gneiskomplex | Gneis: migmatitisch  | Migmatit   | Granofels: Kalksilikat |  Guttannen-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202199 |Straligenstöckli-Gneiskomplex | Granit: porphyrisch: Biotit  | Granodiorit: aplitisch   | – |  Straligenstöckli-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202200 |Lötschental-Gneiskomplex | Gneis: migmatitisch  | Schiefer: Chlorit   | – |  Lötschental-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202201 |Ofenhorn-Stampfhorn-Gneiskomplex | Gneis  | Migmatit   | Schiefer |  Ofenhorn-Stampfhorn-Gneiskomplex |  Karbon     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202202 |Fully-Granodiorit | Granodiorit  | Migmatit: Cordierit   | – |  Fully-Granodiorit |  Pennsylvanien     | Pennsylvanien   | Prävariszisches Grundgebirge  |
|15202203 |Vernayaz-Fm.: Salvan-Mb.: Plex-Aboyeu-Rhyolith | Dazit: rhyolithisch  | –   | – |  Plex-Aboyeu-Rhyolith |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202204 |Vallorcine-Granit | Granit: Biotit-Cordierit  | –   | – |  Vallorcine-Granit |  Pennsylvanien     | Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202205 |Vallorcine-Granit: Miéville-Mylonit | Granit: mylonitisch  | Mylonit   | – |  Miéville-Mylonit |  Pennsylvanien     | Pennsylvanien   | Mittelvariszisches Grundgebirge  |
|15202206 |Montées-Pélissiers-Granit | Granit  | –   | – |  Montées-Pélissiers-Granit |  Mittleres Mississippien     | Mittleres Mississippien   | Frühvariszisches Grundgebirge  |
|15202207 |Pormenaz-Granit | Granit  | –   | – |  Pormenaz-Granit |  Mittleres Mississippien     | Mittleres Mississippien   | Frühvariszisches Grundgebirge  |
|15202210 |Emosson-Gneiskomplex | Gneis: schiefrig: Biotit  | Schiefer: Glimmer   | Gneis: migmatitisch |  Emosson-Gneiskomplex |  Paläozoikum     | Proterozoikum   | Prävariszisches Grundgebirge  |
|15202211 |Luisin-Orthogneis | Gneis: granodioritisch  | Granodiorit   | – |  Luisin-Orthogneis |  Ordovizium     | Ordovizium   | Prävariszisches Grundgebirge  |
|15202212 |Val-Bérard-Gneiskomplex | Gneis: magmatisch  | –   | – |  Val-Bérard-Gneiskomplex |  Ordovizium     | Ordovizium   | Prävariszisches Grundgebirge  |
|15202213 |Lac-Cornu-Eklogit | Eklogit  | –   | – |  Lac-Cornu-Eklogit |  Ordovizium     | Ordovizium   | Prävariszisches Grundgebirge  |
|15202214 |Perrons-Orthogneis | Gneis: granodioritisch  | Granodiorit   | – |  Perrons-Orthogneis |  Ordovizium     | Ordovizium   | Prävariszisches Grundgebirge  |
|15202215 |Breya-Rhyolith | Rhyolith  | –   | – |  Breya-Rhyolith |  Cisuralien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |
|15202216 |Mont-Blanc-Granit | Granit  | –   | – |  Mont-Blanc-Granit |  Pennsylvanien     | Pennsylvanien   | Spät- bis postvariszisches Grundgebirge  |

\elandscape






## Anhang  GC_GEOL_MAPPING_UNIT_CD {#gc-geol-mapping-unit-cd}
Kartiereinheiten

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15200199 | Hauptrogenstein: Maeandrina-Sch. | Hauptrogenstein: Maeandrina-Sch.     |
|15200200 | Hauptrogenstein: Gisliflue-Korallenkalk | Hauptrogenstein: Gisliflue-Korallenkalk     |
|15200201 | Hauptrogenstein: Untere Acuminata-Sch. | Hauptrogenstein: Untere Acuminata-Sch.     |
|15200202 | Klingnau-Fm.: Parkinsoni-Sch. | Klingnau-Fm.: Parkinsoni-Sch.     |
|15200203 | Dewalquei-Kalk | Dewalquei-Kalk     |
|15200204 | Brot-Sch. | Brot-Sch.     |
|15200205 | Passwang-Fm.: Sissach-Mb.: Comptum-Bk. | Passwang-Fm.: Sissach-Mb.: Comptum-Bk.     |
|15200206 | Klettgau-Fm.: Seebi-Mb. | Klettgau-Fm.: Seebi-Mb.     |
|15200207 | Klettgau-Fm.: Gruhalde-Mb. | Klettgau-Fm.: Gruhalde-Mb.     |
|15200208 | Klettgau-Fm.: Berlingen-Mb. | Klettgau-Fm.: Berlingen-Mb.     |
|15200209 | Klettgau-Fm.: Gansingen-Mb. | Klettgau-Fm.: Gansingen-Mb.     |
|15200210 | Klettgau-Fm.: Ergolz-Mb. | Klettgau-Fm.: Ergolz-Mb.     |
|15200211 | Schinznach-Fm.: Stamberg-Mb.: Kaisten-Bk. | Schinznach-Fm.: Stamberg-Mb.: Kaisten-Bk.     |
|15200212 | Schinznach-Fm.: Eptingen-Bk. | Schinznach-Fm.: Eptingen-Bk.     |
|15200213 | Schinznach-Fm.: Dünnlenberg-Bk. | Schinznach-Fm.: Dünnlenberg-Bk.     |
|15200214 | Schinznach-Fm.: Kienberg-Mb.: Saalhof-Bk. | Schinznach-Fm.: Kienberg-Mb.: Saalhof-Bk.     |
|15200215 | Schinznach-Fm.: Leutschenberg-Mb.: Fützen-Bk. | Schinznach-Fm.: Leutschenberg-Mb.: Fützen-Bk.     |
|15200216 | Zeglingen-Fm.: Dolomitzone | Zeglingen-Fm.: Dolomitzone     |
|15200217 | Weitenau-Fm.: Oberer Schuttfächer | Weitenau-Fm.: Oberer Schuttfächer     |
|15200218 | Weitenau-Fm.: Playa-Serie | Weitenau-Fm.: Playa-Serie     |
|15200219 | Weitenau-Fm.: Unterer Schuttfächer | Weitenau-Fm.: Unterer Schuttfächer     |
|15200220 | Schwarzwald-Massiv: Spät- bis postvariszische Intrusiva | Schwarzwald-Massiv: Spät- bis postvariszische Intrusiva     |
|15200221 | Nordalpines Vorland: Spät- bis postvariszische Sedimente und Vulkanite | Nordalpines Vorland: Spät- bis postvariszische Sedimente und Vulkanite     |
|15200222 | Stockberg-Quarzporphyr | Stockberg-Quarzporphyr     |
|15200223 | Bärhalde-Granit | Bärhalde-Granit     |
|15200224 | Schluchsee-Granit | Schluchsee-Granit     |
|15200225 | Säckingen-Granit | Säckingen-Granit     |
|15200226 | Weiach-Fm.: Jüngere Flussablagerungen | Weiach-Fm.: Jüngere Flussablagerungen     |
|15200227 | Weiach-Fm.: Seeablagerungen | Weiach-Fm.: Seeablagerungen     |
|15200228 | Weiach-Fm.: Ältere Flussablagerungen | Weiach-Fm.: Ältere Flussablagerungen     |
|15200229 | Weiach-Fm.: Ältere Flussablagerungen: Kohle-Serie | Weiach-Fm.: Ältere Flussablagerungen: Kohle-Serie     |
|15200230 | Schwarzwald-Massiv: Früh- bis mittelvariszische Intrusiva | Schwarzwald-Massiv: Früh- bis mittelvariszische Intrusiva     |
|15200231 | Albtal-Granit | Albtal-Granit     |
|15200232 | Malsburg-Granit | Malsburg-Granit     |
|15200233 | Blauen-Granit | Blauen-Granit     |
|15200234 | Klemmbach-Granit | Klemmbach-Granit     |
|15200235 | Randgranit | Randgranit     |
|15200236 | Münsterhalden-Granit | Münsterhalden-Granit     |
|15200237 | Schönau-Herrenschwand-Granit | Schönau-Herrenschwand-Granit     |
|15200238 | St.-Blasien-Granit | St.-Blasien-Granit     |
|15200239 | Mambach-Granit | Mambach-Granit     |
|15200240 | Lenzkirch-Steina-Granit | Lenzkirch-Steina-Granit     |
|15200241 | Hauenstein-Granit | Hauenstein-Granit     |
|15200242 | Böttstein-Granit | Böttstein-Granit     |
|15200243 | Schwarzwald-Massiv: Früh- bis mittelvariszische Sedimente | Schwarzwald-Massiv: Früh- bis mittelvariszische Sedimente     |
|15200245 | Schwarzwald-Massiv: Prävariszisches polyzyklisches Grundgebirge | Schwarzwald-Massiv: Prävariszisches polyzyklisches Grundgebirge     |
|15200246 | Schwarzwald-Massiv: Prävariszische Orthogneise | Schwarzwald-Massiv: Prävariszische Orthogneise     |
|15200247 | Todtmoos-Gneiskomplex | Todtmoos-Gneiskomplex     |
|15200248 | Murgtal-Gneiskomplex | Murgtal-Gneiskomplex     |
|15200249 | Laufenburg-Gneiskomplex | Laufenburg-Gneiskomplex     |
|15200250 | Schwarzwald-Massiv: Prävariszische Migmatite | Schwarzwald-Massiv: Prävariszische Migmatite     |
|15200251 | Wiesen-Wehratal-Gneiskomplex | Wiesen-Wehratal-Gneiskomplex     |
|15200252 | Wiesen-Wehratal-Gneiskomplex: Wehratal-Syenit | Wiesen-Wehratal-Gneiskomplex: Wehratal-Syenit     |
|15200253 | Schwarzwald-Massiv: Prävariszische Grüngesteine | Schwarzwald-Massiv: Prävariszische Grüngesteine     |
|15200254 | Molasse | Molasse     |
|15200255 | OSM (Obere Süsswassermolasse) | OSM (Obere Süsswassermolasse)     |
|15200256 | Pfänder-Fm.: Tannenberg-Sch. | Pfänder-Fm.: Tannenberg-Sch.     |
|15200257 | Pfänder-Fm. | Pfänder-Fm.     |
|15200258 | Napf-Fm. | Napf-Fm.     |
|15200259 | Napf-Fm.: Eimätteli-Mb.: Blapbach-Kohlehorizont | Napf-Fm.: Eimätteli-Mb.: Blapbach-Kohlehorizont     |
|15200260 | Napf-Fm.: Eimätteli-Mb. | Napf-Fm.: Eimätteli-Mb.     |
|15200261 | Schüpferegg-Nagelfluh | Schüpferegg-Nagelfluh     |
|15200262 | OSM-II | OSM-II     |
|15200263 | Hegau-Vulkanite | Hegau-Vulkanite     |
|15200264 | Höwenegg-Basalt | Höwenegg-Basalt     |
|15200265 | Hohenwiel-Phonolith | Hohenwiel-Phonolith     |
|15200266 | Hegau-Tuffit | Hegau-Tuffit     |
|15200267 | Hörnli-Fm.: Hörnligipfel-Nagelfluh | Hörnli-Fm.: Hörnligipfel-Nagelfluh     |
|15200268 | Hörnli-Fm.: Hörnligubel-Mergel: Höchegg-Brekzie | Hörnli-Fm.: Hörnligubel-Mergel: Höchegg-Brekzie     |
|15200269 | Hörnli-Fm.: Hörnligubel-Mergel | Hörnli-Fm.: Hörnligubel-Mergel     |
|15200270 | Hörnli-Fm.: Tösswald-Mb. | Hörnli-Fm.: Tösswald-Mb.     |
|15200271 | Öhningen-Fm.: Bischofszell-Bentonit | Öhningen-Fm.: Bischofszell-Bentonit     |
|15200272 | Hörnli-Fm.: Mergelstein-dominierte Fazies | Hörnli-Fm.: Mergelstein-dominierte Fazies     |
|15200273 | Hörnli-Fm.: Krinau-Mb. | Hörnli-Fm.: Krinau-Mb.     |
|15200274 | OSM-II: Glimmersand-Fazies | OSM-II: Glimmersand-Fazies     |
|15200275 | Zürich-Fm.: Fellitobel-Süsswasserkalk | Zürich-Fm.: Fellitobel-Süsswasserkalk     |
|15200276 | Uetliberg-Fm. | Uetliberg-Fm.     |
|15200277 | Uetliberg-Fm.: Uetliberggipfel-Nagelfluh | Uetliberg-Fm.: Uetliberggipfel-Nagelfluh     |
|15200278 | Uetliberg-Fm.: Uetliberg-Mergel | Uetliberg-Fm.: Uetliberg-Mergel     |
|15200279 | Pfannenstiel-Fm.: Falätschen-Mergel | Pfannenstiel-Fm.: Falätschen-Mergel     |
|15200280 | Pfannenstiel-Fm. | Pfannenstiel-Fm.     |
|15200281 | Zürich-Fm. | Zürich-Fm.     |
|15200282 | Zürich-Fm.: Leimbach-Bentonit | Zürich-Fm.: Leimbach-Bentonit     |
|15200283 | Zürich-Fm.: Rütschlibach-Riedhof-Süsswasserkalk | Zürich-Fm.: Rütschlibach-Riedhof-Süsswasserkalk     |
|15200284 | Zürich-Fm.: Winterthur-Bentonit | Zürich-Fm.: Winterthur-Bentonit     |
|15200285 | Zürich-Fm.: Aeugstertal-Bentonit | Zürich-Fm.: Aeugstertal-Bentonit     |
|15200286 | Zürich-Fm.: Äntlisberg-Doldertobel-Süsswasserkalk | Zürich-Fm.: Äntlisberg-Doldertobel-Süsswasserkalk     |
|15200287 | Zürich-Fm.: Wehrenbach-Höckler-Süsswasserkalk | Zürich-Fm.: Wehrenbach-Höckler-Süsswasserkalk     |
|15200288 | Meilen-Fm.: Küsnacht-Bentonit | Meilen-Fm.: Küsnacht-Bentonit     |
|15200289 | Meilen-Fm.: Urdorf-Bentonit | Meilen-Fm.: Urdorf-Bentonit     |
|15200290 | Appenzellergranit-Leitniveau | Appenzellergranit-Leitniveau     |
|15200291 | Appenzellergranit-Leitniveau: Abtwil-Konglomerat | Appenzellergranit-Leitniveau: Abtwil-Konglomerat     |
|15200292 | Appenzellergranit-Leitniveau: Hüllistein-Konglomerat | Appenzellergranit-Leitniveau: Hüllistein-Konglomerat     |
|15200293 | Appenzellergranit-Leitniveau: Degersheim-Kalknagelfluh | Appenzellergranit-Leitniveau: Degersheim-Kalknagelfluh     |
|15200294 | Appenzellergranit-Leitniveau: Meilen-Kalk | Appenzellergranit-Leitniveau: Meilen-Kalk     |
|15200295 | OSM-I | OSM-I     |
|15200296 | Lichtensteig-Fm. | Lichtensteig-Fm.     |
|15200297 | Hörnli-Fm. | Hörnli-Fm.     |
|15200298 | Guggershorn-Fm. | Guggershorn-Fm.     |
|15200299 | Käpfnach-Fm.: Horgen-Süsswasserkalk | Käpfnach-Fm.: Horgen-Süsswasserkalk     |
|15200300 | OSM-J | OSM-J     |
|15200301 | Bois-de-Raube-Fm. | Bois-de-Raube-Fm.     |
|15200302 | OSM-J: Juranagelfluh | OSM-J: Juranagelfluh     |
|15200304 | Le-Locle-Fm.: Combe-Girard Mb.: Combe-Girard-Bentonit | Le-Locle-Fm.: Combe-Girard Mb.: Combe-Girard-Bentonit     |
|15200305 | Vermes-Süsswasserkalk | Vermes-Süsswasserkalk     |
|15200306 | Crêt-du-Locle-Fm.: Gompholitfazies | Crêt-du-Locle-Fm.: Gompholitfazies     |
|15200307 | OMM (Obere Meeresmolasse) | OMM (Obere Meeresmolasse)     |
|15200308 | OMM-II | OMM-II     |
|15200309 | St.-Gallen-Fm. | St.-Gallen-Fm.     |
|15200310 | St.-Gallen-Fm.: Staffelbach-Grobsandstein | St.-Gallen-Fm.: Staffelbach-Grobsandstein     |
|15200311 | OMM-I | OMM-I     |
|15200312 | Luzern-Fm. | Luzern-Fm.     |
|15200313 | Luzern-Fm.: Safenwil-Muschelsandstein | Luzern-Fm.: Safenwil-Muschelsandstein     |
|15200314 | USM (Untere Süsswassermolasse) | USM (Untere Süsswassermolasse)     |
|15200315 | Höhronen-Nagelfluh | Höhronen-Nagelfluh     |
|15200316 | Kronberg-Nagelfluh | Kronberg-Nagelfluh     |
|15200317 | Cornalle-Sandstein | Cornalle-Sandstein     |
|15200318 | Mont-Pèlerin-Nagelfluh | Mont-Pèlerin-Nagelfluh     |
|15200319 | Speer-Fm. | Speer-Fm.     |
|15200320 | Thun-Fm. | Thun-Fm.     |
|15200321 | Thun-Fm.: Gunten-Quarzitnagelfluh | Thun-Fm.: Gunten-Quarzitnagelfluh     |
|15200322 | Rigi-Fm. | Rigi-Fm.     |
|15200323 | Rigi-Fm.: Scheidegg-Nagelfluh | Rigi-Fm.: Scheidegg-Nagelfluh     |
|15200324 | Rigi-Fm.: Bunte Rigi-Nagelfluh | Rigi-Fm.: Bunte Rigi-Nagelfluh     |
|15200325 | Rigi-Fm.: Radiolaritreiche Nagelfluh | Rigi-Fm.: Radiolaritreiche Nagelfluh     |
|15200326 | USM-III | USM-III     |
|15200327 | Sommersberg-Nagelfluh | Sommersberg-Nagelfluh     |
|15200328 | Sommersberg-Nagelfluh: Brendenbach-Mergel | Sommersberg-Nagelfluh: Brendenbach-Mergel     |
|15200329 | USM-II | USM-II     |
|15200001 | Twannbach-Fm. | Twannbach-Fm.     |
|15200002 | Reuchenette-Fm. | Reuchenette-Fm.     |
|15200003 | Courgenay-Fm. | Courgenay-Fm.     |
|15200004 | Vellerat-Fm. | Vellerat-Fm.     |
|15200005 | St-Ursanne-Fm. | St-Ursanne-Fm.     |
|15200006 | Bärschwil-Fm. | Bärschwil-Fm.     |
|15200007 | Ifenthal-Fm. | Ifenthal-Fm.     |
|15200008 | Hauptrogenstein | Hauptrogenstein     |
|15200009 | Passwang-Fm. | Passwang-Fm.     |
|15200010 | Opalinus-Ton | Opalinus-Ton     |
|15200011 | Staffelegg-Fm. | Staffelegg-Fm.     |
|15200012 | Juragebirge: Malm | Juragebirge: Malm     |
|15200013 | Twannbach-Fm.: Vouglans-Mb. | Twannbach-Fm.: Vouglans-Mb.     |
|15200014 | Twannbach-Fm.: Chailley-Mb. | Twannbach-Fm.: Chailley-Mb.     |
|15200015 | Twannbach-Fm.: Oberer Virgula-Mergel | Twannbach-Fm.: Oberer Virgula-Mergel     |
|15200016 | Reuchenette-Fm.: Chevenez-Mb.: Grenznerineen-Bk. | Reuchenette-Fm.: Chevenez-Mb.: Grenznerineen-Bk.     |
|15200017 | Reuchenette-Fm.: Chevenez-Mb.: Cladocoropsis-Kalk | Reuchenette-Fm.: Chevenez-Mb.: Cladocoropsis-Kalk     |
|15200018 | Reuchenette-Fm.: Chevenez-Mb.: Unterer Virgula-Mergel | Reuchenette-Fm.: Chevenez-Mb.: Unterer Virgula-Mergel     |
|15200019 | Reuchenette-Fm.: Courtedoux-Mb. | Reuchenette-Fm.: Courtedoux-Mb.     |
|15200020 | Reuchenette-Fm.: Banné-Mb. | Reuchenette-Fm.: Banné-Mb.     |
|15200021 | Reuchenette-Fm.: Vabenau-Mb. | Reuchenette-Fm.: Vabenau-Mb.     |
|15200022 | Reuchenette-Fm.: Vabenau-Mb.: Creugenat-Sch. | Reuchenette-Fm.: Vabenau-Mb.: Creugenat-Sch.     |
|15200023 | Etiollets-Fm. | Etiollets-Fm.     |
|15200024 | Etiollets-Fm.: Complexe récifal | Etiollets-Fm.: Complexe récifal     |
|15200025 | Etiollets-Fm.: Couvaloup-Mb. | Etiollets-Fm.: Couvaloup-Mb.     |
|15200026 | Courgenay-Fm.: Porrentruy-Mb. | Courgenay-Fm.: Porrentruy-Mb.     |
|15200027 | Courgenay-Fm.: La-May-Mb. | Courgenay-Fm.: La-May-Mb.     |
|15200028 | Vellerat-Fm.: Oolithe-Rousse-Mb. | Vellerat-Fm.: Oolithe-Rousse-Mb.     |
|15200029 | Vellerat-Fm.: Bure-Mb. | Vellerat-Fm.: Bure-Mb.     |
|15200030 | Vellerat-Fm.: Hauptmumienbank-Mb. | Vellerat-Fm.: Hauptmumienbank-Mb.     |
|15200031 | Vellerat-Fm.: Röschenz-Mb. | Vellerat-Fm.: Röschenz-Mb.     |
|15200032 | Vellerat-Fm.: Vorbourg-Mb. | Vellerat-Fm.: Vorbourg-Mb.     |
|15200033 | St-Ursanne-Fm.: Tiergarten-Mb. | St-Ursanne-Fm.: Tiergarten-Mb.     |
|15200034 | St-Ursanne-Fm.: Buix-Mb. | St-Ursanne-Fm.: Buix-Mb.     |
|15200035 | St-Ursanne-Fm.: Chestel-Mb. | St-Ursanne-Fm.: Chestel-Mb.     |
|15200036 | St-Ursanne-Fm.: Chestel-Mb.: Caquerelle-Pisolith | St-Ursanne-Fm.: Chestel-Mb.: Caquerelle-Pisolith     |
|15200037 | St-Ursanne-Fm.: Grellingen-Mb. | St-Ursanne-Fm.: Grellingen-Mb.     |
|15200039 | Pichoux-Fm. | Pichoux-Fm.     |
|15200040 | Bärschwil-Fm.: Liesberg-Mb. | Bärschwil-Fm.: Liesberg-Mb.     |
|15200041 | Bärschwil-Fm.: Sornetan-Mb. | Bärschwil-Fm.: Sornetan-Mb.     |
|15200042 | Bärschwil-Fm.: Renggeri-Mb. | Bärschwil-Fm.: Renggeri-Mb.     |
|15200043 | Ifenthal-Fm.: Graitery-Mb. | Ifenthal-Fm.: Graitery-Mb.     |
|15200044 | Ifenthal-Fm.: Herznach-Mb. | Ifenthal-Fm.: Herznach-Mb.     |
|15200045 | Ifenthal-Fm.: Herznach-Mb.: Schellenbrücke-Bk. | Ifenthal-Fm.: Herznach-Mb.: Schellenbrücke-Bk.     |
|15200046 | Ifenthal-Fm.: Bollement-Mb. | Ifenthal-Fm.: Bollement-Mb.     |
|15200047 | Ifenthal-Fm.: Ängistein-Mb. | Ifenthal-Fm.: Ängistein-Mb.     |
|15200048 | Ifenthal-Fm.: Ängistein-Mb.: Unter-Erli-Bk. | Ifenthal-Fm.: Ängistein-Mb.: Unter-Erli-Bk.     |
|15200049 | Ifenthal-Fm.: Bözen-Mb. | Ifenthal-Fm.: Bözen-Mb.     |
|15200050 | Ifenthal-Fm.: Saulcy-Mb. | Ifenthal-Fm.: Saulcy-Mb.     |
|15200051 | Ifenthal-Fm.: Schelmenloch-Mb. | Ifenthal-Fm.: Schelmenloch-Mb.     |
|15200052 | Ifenthal-Fm.: Schelmenloch-Mb.: Anwil-Bk. | Ifenthal-Fm.: Schelmenloch-Mb.: Anwil-Bk.     |
|15200053 | Ifenthal-Fm.: Châtillon-Mb. | Ifenthal-Fm.: Châtillon-Mb.     |
|15200054 | Ifenthal-Fm.: St-Brais-Mb. | Ifenthal-Fm.: St-Brais-Mb.     |
|15200055 | Juragebirge: Dogger | Juragebirge: Dogger     |
|15200056 | Juragebirge: Lias | Juragebirge: Lias     |
|15200057 | Hauptrogenstein: Spatkalk | Hauptrogenstein: Spatkalk     |
|15200058 | Hauptrogenstein: Pierre-Blanche | Hauptrogenstein: Pierre-Blanche     |
|15200059 | Hauptrogenstein: Movelier-Sch. | Hauptrogenstein: Movelier-Sch.     |
|15200060 | Hauptrogenstein: Grande Oolithe | Hauptrogenstein: Grande Oolithe     |
|15200061 | Hauptrogenstein: Obere Acuminata-Sch. | Hauptrogenstein: Obere Acuminata-Sch.     |
|15200062 | Hauptrogenstein: Oolithe Subcompacte | Hauptrogenstein: Oolithe Subcompacte     |
|15200063 | Passwang-Fm.: Grenchenberg-Mb. | Passwang-Fm.: Grenchenberg-Mb.     |
|15200064 | Passwang-Fm.: Rothenfluh-Mb. | Passwang-Fm.: Rothenfluh-Mb.     |
|15200065 | Passwang-Fm.: Brüggli-Mb. | Passwang-Fm.: Brüggli-Mb.     |
|15200066 | Passwang-Fm.: Brüggli-Mb.: Humphriesi-Sch. | Passwang-Fm.: Brüggli-Mb.: Humphriesi-Sch.     |
|15200067 | Passwang-Fm.: Waldenburg-Mb. | Passwang-Fm.: Waldenburg-Mb.     |
|15200068 | Passwang-Fm.: Hirnichopf-Mb. | Passwang-Fm.: Hirnichopf-Mb.     |
|15200069 | Passwang-Fm.: Hauenstein-Mb. | Passwang-Fm.: Hauenstein-Mb.     |
|15200070 | Passwang-Fm.: Sissach-Mb. | Passwang-Fm.: Sissach-Mb.     |
|15200071 | Staffelegg-Fm.: Gross-Wolf-Mb. | Staffelegg-Fm.: Gross-Wolf-Mb.     |
|15200072 | Staffelegg-Fm.: Gross-Wolf-Mb.: Eriwis-Bk. | Staffelegg-Fm.: Gross-Wolf-Mb.: Eriwis-Bk.     |
|15200073 | Staffelegg-Fm.: Gross-Wolf-Mb.: Erlimoos-Bk. | Staffelegg-Fm.: Gross-Wolf-Mb.: Erlimoos-Bk.     |
|15200074 | Staffelegg-Fm.: Gross-Wolf-Mb.: Gipf-Bk. | Staffelegg-Fm.: Gross-Wolf-Mb.: Gipf-Bk.     |
|15200075 | Staffelegg-Fm.: Rietheim-Mb. | Staffelegg-Fm.: Rietheim-Mb.     |
|15200076 | Staffelegg-Fm.: Rietheim-Mb.: Unterer Stein | Staffelegg-Fm.: Rietheim-Mb.: Unterer Stein     |
|15200077 | Staffelegg-Fm.: Rickenbach-Mb. | Staffelegg-Fm.: Rickenbach-Mb.     |
|15200078 | Staffelegg-Fm.: Rickenbach-Mb.: Müsenegg-Bk. | Staffelegg-Fm.: Rickenbach-Mb.: Müsenegg-Bk.     |
|15200079 | Staffelegg-Fm.: Breitenmatt-Mb. | Staffelegg-Fm.: Breitenmatt-Mb.     |
|15200080 | Staffelegg-Fm.: Breitenmatt-Mb.: Trasadingen-Bk. | Staffelegg-Fm.: Breitenmatt-Mb.: Trasadingen-Bk.     |
|15200081 | Staffelegg-Fm.: Grünschholz-Mb. | Staffelegg-Fm.: Grünschholz-Mb.     |
|15200082 | Staffelegg-Fm.: Frick-Mb. | Staffelegg-Fm.: Frick-Mb.     |
|15200083 | Staffelegg-Fm.: Mont-Terri-Mb. | Staffelegg-Fm.: Mont-Terri-Mb.     |
|15200084 | Staffelegg-Fm.: Fasiswald-Mb. | Staffelegg-Fm.: Fasiswald-Mb.     |
|15200085 | Staffelegg-Fm.: Weissenstein-Mb. | Staffelegg-Fm.: Weissenstein-Mb.     |
|15200086 | Staffelegg-Fm.: Beggingen-Mb. | Staffelegg-Fm.: Beggingen-Mb.     |
|15200087 | Staffelegg-Fm.: Beggingen-Mb.: Gächlingen-Bk. | Staffelegg-Fm.: Beggingen-Mb.: Gächlingen-Bk.     |
|15200088 | Staffelegg-Fm.: Beggingen-Mb.: Schleitheim-Bk. | Staffelegg-Fm.: Beggingen-Mb.: Schleitheim-Bk.     |
|15200089 | Staffelegg-Fm.: Schambelen-Mb. | Staffelegg-Fm.: Schambelen-Mb.     |
|15200090 | Staffelegg-Fm.: Schambelen-Mb.: Hallau-Bk. | Staffelegg-Fm.: Schambelen-Mb.: Hallau-Bk.     |
|15200091 | Juragebirge: Siderolithikum | Juragebirge: Siderolithikum     |
|15200092 | Gorges-de-l&#39;Orbe- und Vallorbe-Mb. | Gorges-de-l&#39;Orbe- und Vallorbe-Mb.     |
|15200093 | Rocher-des-Hirondelles-Fm.: Vallorbe-Mb. | Rocher-des-Hirondelles-Fm.: Vallorbe-Mb.     |
|15200094 | Rocher-des-Hirondelles-Fm.: Rivière-Mb. | Rocher-des-Hirondelles-Fm.: Rivière-Mb.     |
|15200096 | Gorges-de-l&#39;Orbe-Fm. | Gorges-de-l&#39;Orbe-Fm.     |
|15200097 | Pierre-Châtel- Vions- und Chambotte-Fm. | Pierre-Châtel- Vions- und Chambotte-Fm.     |
|15200098 | Chambotte-Fm. | Chambotte-Fm.     |
|15200099 | Chambotte-Fm.: Guiers-Mb. | Chambotte-Fm.: Guiers-Mb.     |
|15200100 | Vions-Fm. | Vions-Fm.     |
|15200101 | Pierre-Châtel-Fm. | Pierre-Châtel-Fm.     |
|15200102 | Burghorn-Fm. | Burghorn-Fm.     |
|15200103 | Burghorn-Fm.: Wettingen-Mb. | Burghorn-Fm.: Wettingen-Mb.     |
|15200104 | Burghorn-Fm.: Baden-Mb. | Burghorn-Fm.: Baden-Mb.     |
|15200105 | Villigen-Fm. | Villigen-Fm.     |
|15200106 | Villigen-Fm.: Wangental-Mb. | Villigen-Fm.: Wangental-Mb.     |
|15200107 | Villigen-Fm.: Letzi-Mb. | Villigen-Fm.: Letzi-Mb.     |
|15200108 | Villigen-Fm.: Knollen-Bk. | Villigen-Fm.: Knollen-Bk.     |
|15200109 | Villigen-Fm.: Küssaburg-Mb. | Villigen-Fm.: Küssaburg-Mb.     |
|15200110 | Villigen-Fm.: Wangen-Mb. | Villigen-Fm.: Wangen-Mb.     |
|15200111 | Villigen-Fm.: Hornbuck-Mb. | Villigen-Fm.: Hornbuck-Mb.     |
|15200112 | Villigen-Fm.: Crenularis-Mb. | Villigen-Fm.: Crenularis-Mb.     |
|15200113 | Villigen-Fm.: Geissberg-Mb. | Villigen-Fm.: Geissberg-Mb.     |
|15200114 | Wildegg-Fm. | Wildegg-Fm.     |
|15200115 | Wildegg-Fm.: Effingen-Mb. | Wildegg-Fm.: Effingen-Mb.     |
|15200116 | Wildegg-Fm.: Effingen-Mb.: Gerstenhübel-Bk. | Wildegg-Fm.: Effingen-Mb.: Gerstenhübel-Bk.     |
|15200117 | Wildegg-Fm.: Birmenstorf-Mb. | Wildegg-Fm.: Birmenstorf-Mb.     |
|15200118 | Günsberg-Fm. | Günsberg-Fm.     |
|15200119 | Günsberg-Fm.: Moutier-Korallenkalk | Günsberg-Fm.: Moutier-Korallenkalk     |
|15200120 | Klingnau-Fm. | Klingnau-Fm.     |
|15200121 | Klingnau-Fm.: Knorri-Ton | Klingnau-Fm.: Knorri-Ton     |
|15200122 | Klingnau-Fm.: Wuerttembergica-Sch. | Klingnau-Fm.: Wuerttembergica-Sch.     |
|15200123 | Klingnau-Fm.: Parkinsoni-Sch.: Subfurcatum-Bk. | Klingnau-Fm.: Parkinsoni-Sch.: Subfurcatum-Bk.     |
|15200124 | Klingnau-Fm.: Blagdeni-Sch. | Klingnau-Fm.: Blagdeni-Sch.     |
|15200125 | Juragebirge: Keuper | Juragebirge: Keuper     |
|15200126 | Klettgau-Fm. | Klettgau-Fm.     |
|15200127 | Klettgau-Fm.: Belchen-Mb. | Klettgau-Fm.: Belchen-Mb.     |
|15200128 | Bänkerjoch-Fm. | Bänkerjoch-Fm.     |
|15200129 | Juragebirge: Muschelkalk | Juragebirge: Muschelkalk     |
|15200130 | Schinznach-Fm. | Schinznach-Fm.     |
|15200131 | Schinznach-Fm.: Asp-Mb. | Schinznach-Fm.: Asp-Mb.     |
|15200132 | Schinznach-Fm.: Stamberg-Mb. | Schinznach-Fm.: Stamberg-Mb.     |
|15200133 | Schinznach-Fm.: Liedertswil-Mb. | Schinznach-Fm.: Liedertswil-Mb.     |
|15200134 | Schinznach-Fm.: Kienberg-Mb. | Schinznach-Fm.: Kienberg-Mb.     |
|15200135 | Zeglingen-Fm. | Zeglingen-Fm.     |
|15200136 | Zeglingen-Fm.: Obere Sufatzone | Zeglingen-Fm.: Obere Sufatzone     |
|15200137 | Zeglingen-Fm.: Salzlager | Zeglingen-Fm.: Salzlager     |
|15200138 | Zeglingen-Fm.: Untere Sulfatzone | Zeglingen-Fm.: Untere Sulfatzone     |
|15200139 | Kaiseraugst-Fm. | Kaiseraugst-Fm.     |
|15200140 | Kaiseraugst-Fm.: Orbicularis-Mergel | Kaiseraugst-Fm.: Orbicularis-Mergel     |
|15200141 | Kaiseraugst-Fm.: Wellenkalk / Wellenmergel | Kaiseraugst-Fm.: Wellenkalk / Wellenmergel     |
|15200142 | Kaiseraugst-Fm.: Wellendolomit | Kaiseraugst-Fm.: Wellendolomit     |
|15200143 | Juragebirge: Buntsandstein | Juragebirge: Buntsandstein     |
|15200144 | Dinkelberg-Fm. | Dinkelberg-Fm.     |
|15200145 | Dinkelberg-Fm.: Rötton | Dinkelberg-Fm.: Rötton     |
|15200146 | Dinkelberg-Fm.: Plattensandstein | Dinkelberg-Fm.: Plattensandstein     |
|15200147 | Dinkelberg-Fm.: Karneolhorizont | Dinkelberg-Fm.: Karneolhorizont     |
|15200148 | Narlay-Fm. | Narlay-Fm.     |
|15200149 | Perte-du-Rhône-Fm. | Perte-du-Rhône-Fm.     |
|15200150 | Grand-Essert-Fm. | Grand-Essert-Fm.     |
|15200151 | Grand-Essert-Fm: Neuchâtel-Mb. | Grand-Essert-Fm: Neuchâtel-Mb.     |
|15200152 | Grand-Essert-Fm: Hauterive-Mb. | Grand-Essert-Fm: Hauterive-Mb.     |
|15200153 | Vuache-Fm. | Vuache-Fm.     |
|15200154 | Vuache-Fm.: Alectryonia-Kalk | Vuache-Fm.: Alectryonia-Kalk     |
|15200155 | Vuache-Fm.: Arzier-Mergel | Vuache-Fm.: Arzier-Mergel     |
|15200156 | Goldberg-Fm. | Goldberg-Fm.     |
|15200157 | Wiesental-Fm. | Wiesental-Fm.     |
|15200158 | Weitenau-Fm. | Weitenau-Fm.     |
|15200159 | Weiach-Fm. | Weiach-Fm.     |
|15200160 | Günsberg- Vellerat- Villigen- Balsthal- und Courgenay-Fm. | Günsberg- Vellerat- Villigen- Balsthal- und Courgenay-Fm.     |
|15200161 | Juragebirge: Kreide | Juragebirge: Kreide     |
|15200162 | Juragebirge: Jura | Juragebirge: Jura     |
|15200163 | Juragebirge: Trias | Juragebirge: Trias     |
|15200175 | Siderolithikum: Bohnerzton | Siderolithikum: Bohnerzton     |
|15200176 | Siderolithikum: Boluston | Siderolithikum: Boluston     |
|15200177 | Siderolithikum: Huppererde | Siderolithikum: Huppererde     |
|15200178 | Hauptrogenstein: Homomyenmergel | Hauptrogenstein: Homomyenmergel     |
|15200179 | Dinkelberg-Fm.: Vogesen-Sandstein | Dinkelberg-Fm.: Vogesen-Sandstein     |
|15200180 | Siderolithikum: Quarzsand | Siderolithikum: Quarzsand     |
|15200181 | Perte-du-Rhône-Fm.: Mussel-Mb. | Perte-du-Rhône-Fm.: Mussel-Mb.     |
|15200182 | Perte-du-Rhône-Fm.: Fulie-Mb. | Perte-du-Rhône-Fm.: Fulie-Mb.     |
|15200183 | Grand-Essert-Fm: Neuchâtel-Mb.: Uttins-Mergel | Grand-Essert-Fm: Neuchâtel-Mb.: Uttins-Mergel     |
|15200184 | Grand-Essert-Fm: Hauterive-Mb.: Ecluse-Mergelkalk | Grand-Essert-Fm: Hauterive-Mb.: Ecluse-Mergelkalk     |
|15200185 | Vuache-Fm.: Bryozoen-Mergel | Vuache-Fm.: Bryozoen-Mergel     |
|15200186 | Twannbach-Fm.: Zuckerkörniger Kalk | Twannbach-Fm.: Zuckerkörniger Kalk     |
|15200187 | Reuchenette-Fm.: Chevenez-Mb. | Reuchenette-Fm.: Chevenez-Mb.     |
|15200188 | Balsthal-Fm. | Balsthal-Fm.     |
|15200189 | Balsthal-Fm.: Verena-Mb. | Balsthal-Fm.: Verena-Mb.     |
|15200190 | Balsthal-Fm.: Holzflue-Mb. | Balsthal-Fm.: Holzflue-Mb.     |
|15200191 | Balsthal-Fm.: Laufen-Mb. | Balsthal-Fm.: Laufen-Mb.     |
|15200192 | Balsthal-Fm.: Olten-Mb. | Balsthal-Fm.: Olten-Mb.     |
|15200193 | Balsthal-Fm.: Steinibach-Mb. | Balsthal-Fm.: Steinibach-Mb.     |
|15200194 | Vellerat-Fm.: Röschenz-Mb.: Grüne Mumienbank | Vellerat-Fm.: Röschenz-Mb.: Grüne Mumienbank     |
|15200195 | Wildegg-Fm.: Effingen-Mb.: Pecten-Bk. | Wildegg-Fm.: Effingen-Mb.: Pecten-Bk.     |
|15200196 | Hauptrogenstein: Ferrugineus-Oolith | Hauptrogenstein: Ferrugineus-Oolith     |
|15200197 | Hauptrogenstein: Wittnau-Korallenkalk | Hauptrogenstein: Wittnau-Korallenkalk     |
|15200198 | Hauptrogenstein: Furcil-Mergel | Hauptrogenstein: Furcil-Mergel     |
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
|15203349 | Terri-Schiefer | Terri-Schiefer     |
|15203350 | Robiei-Wildflysch | Robiei-Wildflysch     |
|15203351 | Robiei-Wildflysch: Pizzo-Castello-Wildflysch | Robiei-Wildflysch: Pizzo-Castello-Wildflysch     |
|15203352 | Robiei-Wildflysch: Tamier-Zött-Wildflysch | Robiei-Wildflysch: Tamier-Zött-Wildflysch     |
|15203353 | Robiei-Wildflysch: Alpe-Tamia-Campo-Wildflysch | Robiei-Wildflysch: Alpe-Tamia-Campo-Wildflysch     |
|15203354 | Teggiolo-Kalkschiefer | Teggiolo-Kalkschiefer     |
|15203355 | Teggiolo-Kalkschiefer: Medola-Quarzit | Teggiolo-Kalkschiefer: Medola-Quarzit     |
|15203356 | Teggiolo-Kalkschiefer: Pianasciom-Kalkschiefer | Teggiolo-Kalkschiefer: Pianasciom-Kalkschiefer     |
|15203357 | Teggiolo-Kalkschiefer: Piano-delle-Creste-Sandstein | Teggiolo-Kalkschiefer: Piano-delle-Creste-Sandstein     |
|15203358 | Antabia-Gr. | Antabia-Gr.     |
|15203359 | Vanis-Fm. | Vanis-Fm.     |
|15203360 | Sevinera-Marmor | Sevinera-Marmor     |
|15203361 | Sevinera-Sandstein | Sevinera-Sandstein     |
|15203362 | Ri-d&#39;Antabia-Konglomerat | Ri-d&#39;Antabia-Konglomerat     |
|15203363 | Lebendun-Komplex: Scisti bruni | Lebendun-Komplex: Scisti bruni     |
|15203364 | Lebendun-Komplex: Basaler Gneis | Lebendun-Komplex: Basaler Gneis     |
|15203365 | Antigorio-Orthogneis | Antigorio-Orthogneis     |
|15203366 | Falknis-, Sulzfluh- und Tasna-Decke: Couches Rouges | Falknis-, Sulzfluh- und Tasna-Decke: Couches Rouges     |
|15203367 | Piz-Terri-Lunschania: Lagensandkalk | Piz-Terri-Lunschania: Lagensandkalk     |
|15203368 | Pierre-Avoi-Melange: Quarzschiefer-dominierte Fazies | Pierre-Avoi-Melange: Quarzschiefer-dominierte Fazies     |
|15203369 | Pierre-Avoi-Melange: Konglomerat-dominierte Fazies | Pierre-Avoi-Melange: Konglomerat-dominierte Fazies     |
|15203370 | Südegg-Komplex | Südegg-Komplex     |
|15203371 | Punta-Rossa-Komplex | Punta-Rossa-Komplex     |
|15203372 | Ferret-Schiefer | Ferret-Schiefer     |
|15203373 | Piz-Terri-Lunschania: Basale Tonschiefer | Piz-Terri-Lunschania: Basale Tonschiefer     |
|15203374 | Grava-Decke: Kalk- und Tonschiefer | Grava-Decke: Kalk- und Tonschiefer     |
|15203376 | Piz-Terri-Lunschania: Konglomeratgneis | Piz-Terri-Lunschania: Konglomeratgneis     |
|15203377 | Garzott-Brekzie | Garzott-Brekzie     |
|15203378 | Areua-Bruschghorn-Melange | Areua-Bruschghorn-Melange     |
|15203379 | Grava-Decke: Albitquarzit | Grava-Decke: Albitquarzit     |
|15203380 | Grava-Decke: Basale Tonschiefer | Grava-Decke: Basale Tonschiefer     |
|15203381 | Aul-Decke: Phengitgneis | Aul-Decke: Phengitgneis     |
|15203382 | Haute-Pointe-Fm. | Haute-Pointe-Fm.     |
|15203383 | Brasses-Fm. | Brasses-Fm.     |
|15203385 | Macugnaga-Augengneis | Macugnaga-Augengneis     |
|15203386 | Zone Houillère: Perm | Zone Houillère: Perm     |
|15203387 | Zone Houillère: Perm: Quarzschiefer | Zone Houillère: Perm: Quarzschiefer     |
|15203388 | Ricard-Rhyolit | Ricard-Rhyolit     |
|15203389 | Zone Houillère: Perm: Konglomerat | Zone Houillère: Perm: Konglomerat     |
|15203390 | Printse-Fm.: Sandig-schiefrige Fazies | Printse-Fm.: Sandig-schiefrige Fazies     |
|15203391 | Printse-Fm.: Tonige Fazies | Printse-Fm.: Tonige Fazies     |
|15203392 | Printse-Fm.: Chandoline-Sandstein | Printse-Fm.: Chandoline-Sandstein     |
|15203393 | Gälmji-Gneis | Gälmji-Gneis     |
|15203394 | Scherbadung-Gabbro | Scherbadung-Gabbro     |
|15203395 | Lacerandes-Augengneis | Lacerandes-Augengneis     |
|15203396 | Mont-Mort-Metapelit | Mont-Mort-Metapelit     |
|15203397 | Pierre-Avoi-Melange: Schwarze Schiefer | Pierre-Avoi-Melange: Schwarze Schiefer     |
|15203398 | Ferret-Schiefer: La-Dotse-Albitkalk | Ferret-Schiefer: La-Dotse-Albitkalk     |
|15203399 | Ergischhorn-Komplex-Fm.: Ginals-Gneis | Ergischhorn-Komplex-Fm.: Ginals-Gneis     |
|15203400 | Berisal-Gneiskomplex | Berisal-Gneiskomplex     |
|15203401 | Berisal-Gneiskomplex: Augengneis | Berisal-Gneiskomplex: Augengneis     |
|15203402 | Ruitor-Gneiskomplex | Ruitor-Gneiskomplex     |
|15203403 | Corno-Gneis | Corno-Gneis     |
|15203404 | Unterpenninikum: Trias: Quarzit | Unterpenninikum: Trias: Quarzit     |
|15203405 | Mittelpenninikum: Grundgebirge | Mittelpenninikum: Grundgebirge     |
|15203406 | Mont-Brûlé-Quarzit | Mont-Brûlé-Quarzit     |
|15203407 | Mont-Brûlé-Quarzit: Plan-Palasuit-Konglomerat | Mont-Brûlé-Quarzit: Plan-Palasuit-Konglomerat     |
|15203408 | Oberpenninikum: Metasedimente | Oberpenninikum: Metasedimente     |
|15203409 | Tsaté-Decke: Metasedimente | Tsaté-Decke: Metasedimente     |
|15203410 | Tsaté-Decke: Marmor | Tsaté-Decke: Marmor     |
|15203411 | Tsaté-Decke: Radiolarit | Tsaté-Decke: Radiolarit     |
|15203412 | Zermatt-Saas-Decke: Metasedimente | Zermatt-Saas-Decke: Metasedimente     |
|15203413 | Oberpenninikum: Ophiolith | Oberpenninikum: Ophiolith     |
|15203414 | Tsaté-Decke: Ophiolith | Tsaté-Decke: Ophiolith     |
|15203415 | Mont-des-Ritzes-Metabasalt | Mont-des-Ritzes-Metabasalt     |
|15203416 | Aiguilles-Rouges-d&#39;Arolla-Metagabbro | Aiguilles-Rouges-d&#39;Arolla-Metagabbro     |
|15203417 | Torrembey-Brekzie | Torrembey-Brekzie     |
|15203418 | Zermatt-Saas-Decke: Marmor | Zermatt-Saas-Decke: Marmor     |
|15203419 | Zermatt-Saas-Decke: Quarzit | Zermatt-Saas-Decke: Quarzit     |
|15203420 | Riffelberg-Melange | Riffelberg-Melange     |
|15203421 | Zermatt-Saas-Decke: Schiefer | Zermatt-Saas-Decke: Schiefer     |
|15203422 | Zermatt-Saas-Decke: Ophiolith | Zermatt-Saas-Decke: Ophiolith     |
|15203423 | Pfulwe-Metabasalt | Pfulwe-Metabasalt     |
|15203424 | Antrona-Decke: Ophiolith | Antrona-Decke: Ophiolith     |
|15203425 | Ergischhorn-Komplex-Fm.: Böshorn-Gneis | Ergischhorn-Komplex-Fm.: Böshorn-Gneis     |
|15203426 | Monte-Leone-Decke: Orthogneis | Monte-Leone-Decke: Orthogneis     |
|15203427 | Monte-Leone-Decke: Leukogneis | Monte-Leone-Decke: Leukogneis     |
|15203428 | Monte-Leone-Decke: Hyperaugengneis | Monte-Leone-Decke: Hyperaugengneis     |
|15203429 | Monte-Leone-Decke: Paragneis | Monte-Leone-Decke: Paragneis     |
|15203430 | Lebendun-Komplex: Arkose | Lebendun-Komplex: Arkose     |
|15203431 | Lebendun-Komplex: Konglomerat | Lebendun-Komplex: Konglomerat     |
|15203432 | Ruginenta-Decke: Sedimentbedeckung | Ruginenta-Decke: Sedimentbedeckung     |
|15203433 | Ruginenta-Decke: Grundgebirge | Ruginenta-Decke: Grundgebirge     |
|15203434 | Ruginenta-Decke: Glimmerschiefer | Ruginenta-Decke: Glimmerschiefer     |
|15203435 | Ruginenta-Decke: Paragneis | Ruginenta-Decke: Paragneis     |
|15203436 | Preja-Fm. | Preja-Fm.     |
|15203437 | Cavalli-Fm. | Cavalli-Fm.     |
|15203438 | Monte-Rosa-Decke: Sedimentbedeckung | Monte-Rosa-Decke: Sedimentbedeckung     |
|15203439 | Mezzalama-Granit | Mezzalama-Granit     |
|15203440 | Monte-Rosa-Orthogneis: Grobkörnige Fazies | Monte-Rosa-Orthogneis: Grobkörnige Fazies     |
|15203441 | Rottal-Migmatit | Rottal-Migmatit     |
|15203442 | Monte-Rosa-Orthogneis: Mylonitische Fazies | Monte-Rosa-Orthogneis: Mylonitische Fazies     |
|15203443 | Monte-Rosa-Decke: Paragneis | Monte-Rosa-Decke: Paragneis     |
|15203444 | Monte-Rosa-Decke: Biotitgneis | Monte-Rosa-Decke: Biotitgneis     |
|15203445 | Monte-Rosa-Decke: Bändergneis | Monte-Rosa-Decke: Bändergneis     |
|15203446 | Monte-Rosa-Decke: Glimmerschiefer | Monte-Rosa-Decke: Glimmerschiefer     |
|15203447 | Portjengrat-Decke: Sedimentbedeckung | Portjengrat-Decke: Sedimentbedeckung     |
|15203449 | Portjengrat-Orthogneis | Portjengrat-Orthogneis     |
|15203164 | Oberälpli-Fm. | Oberälpli-Fm.     |
|15203165 | Eggberg-Fm. | Eggberg-Fm.     |
|15203166 | Gyrenspitz-Fm. | Gyrenspitz-Fm.     |
|15203167 | Fadura-Fm. | Fadura-Fm.     |
|15203168 | Pfävigrat-Fm. | Pfävigrat-Fm.     |
|15203169 | Sassauna-Fm. | Sassauna-Fm.     |
|15203170 | Valzeina-Fm. | Valzeina-Fm.     |
|15203171 | Klus-Fm. | Klus-Fm.     |
|15203172 | Stätzerhorn-Fm. | Stätzerhorn-Fm.     |
|15203173 | Stätzerhorn-Fm.: Basaler Konglomerat | Stätzerhorn-Fm.: Basaler Konglomerat     |
|15203174 | Carnusa-Fm. | Carnusa-Fm.     |
|15203175 | Nolla-Kalkschiefer: Safien-Kalk | Nolla-Kalkschiefer: Safien-Kalk     |
|15203176 | Nolla-Kalkschiefer | Nolla-Kalkschiefer     |
|15203177 | Nolla-Tonschiefer | Nolla-Tonschiefer     |
|15203178 | Bärenhorn-Fm. | Bärenhorn-Fm.     |
|15203179 | Tomül-Decke: Grüngesteine | Tomül-Decke: Grüngesteine     |
|15203180 | Tomül-Decke: Mélange | Tomül-Decke: Mélange     |
|15203181 | Touno-Einheit | Touno-Einheit     |
|15203182 | Barrhorn-Einheit | Barrhorn-Einheit     |
|15203183 | Bruneggjoch-Fm. | Bruneggjoch-Fm.     |
|15203184 | Bruneggjoch-Fm.: Sous-le-Rocher-Mb. | Bruneggjoch-Fm.: Sous-le-Rocher-Mb.     |
|15203185 | Randa-Augengneis | Randa-Augengneis     |
|15201182 | Juraschotter | Juraschotter     |
|15201183 | Alte Doubsschotter | Alte Doubsschotter     |
|15201184 | Wutach-Schotter | Wutach-Schotter     |
|15201185 | Merenbach-Schotter | Merenbach-Schotter     |
|15201186 | Malmkalk-Schotter der Randen-Täler | Malmkalk-Schotter der Randen-Täler     |
|15201002 | Niederterrasse | Niederterrasse     |
|15201006 | Birrfeld-Eiszeit (Letzte Eiszeit) | Birrfeld-Eiszeit (Letzte Eiszeit)     |
|15201008 | LGM-Rückzug | LGM-Rückzug     |
|15201187 | Solothurn-Stadium | Solothurn-Stadium     |
|15201129 | Zürich-Stein-Bremgarten-Stadien | Zürich-Stein-Bremgarten-Stadien     |
|15201130 | Untere Singen-Terrasse | Untere Singen-Terrasse     |
|15201131 | Schlieren-Diessenhofen-Stetten-Stadien | Schlieren-Diessenhofen-Stetten-Stadien     |
|15201132 | Obere Singen-Terrasse | Obere Singen-Terrasse     |
|15201133 | Rheinau-Terrasse | Rheinau-Terrasse     |
|15201134 | Nohl-Terrasse | Nohl-Terrasse     |
|15201135 | Altenburg-Fulach-Terrasse | Altenburg-Fulach-Terrasse     |
|15201136 | Aare-Schotter | Aare-Schotter     |
|15201137 | Schüss-Schotter | Schüss-Schotter     |
|15201138 | Orvin-Schotter | Orvin-Schotter     |
|15201139 | Seeablagerungen von Frinvillier und Rondchâtel | Seeablagerungen von Frinvillier und Rondchâtel     |
|15201140 | Stauschotter von Diessbach | Stauschotter von Diessbach     |
|15201141 | Mély-Formation | Mély-Formation     |
|15201007 | Last Glacial Maximum (LGM), undiff. | Last Glacial Maximum (LGM), undiff.     |
|15201142 | Kiessande von Madretsch | Kiessande von Madretsch     |
|15201143 | Seeland-Schotter | Seeland-Schotter     |
|15201144 | Emme-Schotter | Emme-Schotter     |
|15201145 | Gäu-Schotter | Gäu-Schotter     |
|15201146 | Flumenthal-Lehm | Flumenthal-Lehm     |
|15201147 | Killwangen-Schaffhausen-Mellingen-Stadium | Killwangen-Schaffhausen-Mellingen-Stadium     |
|15201148 | Munot-Terrasse | Munot-Terrasse     |
|15201149 | Stokar-Terrasse | Stokar-Terrasse     |
|15201150 | Breite-Terrasse | Breite-Terrasse     |
|15201151 | Maximalstand (Kilwangen-Schaffhausen-Stadium) | Maximalstand (Kilwangen-Schaffhausen-Stadium)     |
|15201009 | Birmenstorf-Vergletscherung (2. LGM-Vorstoss) | Birmenstorf-Vergletscherung (2. LGM-Vorstoss)     |
|15201010 | Wettingen-Vorstoss | Wettingen-Vorstoss     |
|15201011 | Flüefeld-Schotter | Flüefeld-Schotter     |
|15201012 | Altberg-Till | Altberg-Till     |
|15203186 | Col-de-Chassoure-Fm. | Col-de-Chassoure-Fm.     |
|15203187 | Col-de-Chassoure-Fm.: Gouille-Verte-Mb. | Col-de-Chassoure-Fm.: Gouille-Verte-Mb.     |
|15203188 | Col-de-Chassoure-Fm.: Matse-Mb. | Col-de-Chassoure-Fm.: Matse-Mb.     |
|15203189 | Col-de-Chassoure-Fm.: Dent-de-Nendaz-Mb. | Col-de-Chassoure-Fm.: Dent-de-Nendaz-Mb.     |
|15203190 | Col-de-Chassoure-Fm.: Goli-d&#39;Aget-Mb. | Col-de-Chassoure-Fm.: Goli-d&#39;Aget-Mb.     |
|15203191 | Col-de-Chassoure-Fm.: Mondra-Mb. | Col-de-Chassoure-Fm.: Mondra-Mb.     |
|15203192 | Col-de-Chassoure-Fm.: Cleuson-Mb. | Col-de-Chassoure-Fm.: Cleuson-Mb.     |
|15203193 | Métailler-Fm. | Métailler-Fm.     |
|15203194 | Distulberg-Fm. | Distulberg-Fm.     |
|15203195 | Thyon-Metagranophyr | Thyon-Metagranophyr     |
|15203196 | Mont-Rogneux-Metagranit | Mont-Rogneux-Metagranit     |
|15203197 | Lirec-Fm. undiff | Lirec-Fm. undiff     |
|15203198 | Adlerflüe-Fm. | Adlerflüe-Fm.     |
|15203199 | Ergischhorn-Komplex | Ergischhorn-Komplex     |
|15203200 | Gelbhorn-Flysch | Gelbhorn-Flysch     |
|15203201 | Obrist-Fm. | Obrist-Fm.     |
|15203202 | Vizan-Brekzie | Vizan-Brekzie     |
|15203203 | Tschera-Marmor | Tschera-Marmor     |
|15203204 | Tschera-Marmor: Wissberg-Brekzie | Tschera-Marmor: Wissberg-Brekzie     |
|15203205 | Nisellas-Fm. | Nisellas-Fm.     |
|15201013 | Birmenstorf-Vorstoss | Birmenstorf-Vorstoss     |
|15201014 | Birr-Schotter | Birr-Schotter     |
|15201015 | Oberhard-Till | Oberhard-Till     |
|15201152 | Wehntal-Schotter | Wehntal-Schotter     |
|15201016 | Seon-Vorstoss | Seon-Vorstoss     |
|15201017 | Berg-Schotter | Berg-Schotter     |
|15201018 | Fornholz-Till | Fornholz-Till     |
|15201153 | Bick-Till | Bick-Till     |
|15201154 | Flüe-Till | Flüe-Till     |
|15201155 | Wettingen-Schotter | Wettingen-Schotter     |
|15201019 | Gontenschwil-Vorstoss | Gontenschwil-Vorstoss     |
|15201020 | Gontenschwil-Till | Gontenschwil-Till     |
|15201021 | Staffelbach-Vorstoss | Staffelbach-Vorstoss     |
|15201022 | Staffelbach-Schotter | Staffelbach-Schotter     |
|15201023 | Staffelbach-Till | Staffelbach-Till     |
|15201024 | Lindmühle-Vergletscherung (1. LGM-Vorstoss) | Lindmühle-Vergletscherung (1. LGM-Vorstoss)     |
|15201025 | Otelfingen-Vorstoss | Otelfingen-Vorstoss     |
|15201026 | Tägerhard-Schotter | Tägerhard-Schotter     |
|15201027 | Lindmühle-Vorstoss | Lindmühle-Vorstoss     |
|15201028 | Ämmert-Schotter | Ämmert-Schotter     |
|15201029 | Ämmert-Till | Ämmert-Till     |
|15201030 | Emmet-Vorstoss | Emmet-Vorstoss     |
|15201031 | Gündelmoos-Lehm | Gündelmoos-Lehm     |
|15201032 | Igliste-Schotter | Igliste-Schotter     |
|15201033 | Niderholz-Till | Niderholz-Till     |
|15201034 | Zetzwil-Vorstoss | Zetzwil-Vorstoss     |
|15201035 | Zetzwil-Till | Zetzwil-Till     |
|15201036 | Kirchleerau-Vorstoss | Kirchleerau-Vorstoss     |
|15201037 | Kirchleerau-Till | Kirchleerau-Till     |
|15201038 | Gossau-Interstadial | Gossau-Interstadial     |
|15201039 | Mülligen-Paläoboden | Mülligen-Paläoboden     |
|15201040 | Niederweningen-Formation | Niederweningen-Formation     |
|15201041 | Hombrechtikon-Vergletscherung (Frühletzteiszeitliche Vergl.) | Hombrechtikon-Vergletscherung (Frühletzteiszeitliche Vergl.)     |
|15201042 | Mülligen-Schotter | Mülligen-Schotter     |
|15201043 | 2. letzteiszeitlischs Vorstoss | 2. letzteiszeitlischs Vorstoss     |
|15201044 | 1. letzteiszeitlischs Vorstoss | 1. letzteiszeitlischs Vorstoss     |
|15201001 | Ältere Ablagerungen, undifferenziert | Ältere Ablagerungen, undifferenziert     |
|15201156 | Bersturzmasse von Selzach | Bersturzmasse von Selzach     |
|15203206 | Tumpriv-Fm. | Tumpriv-Fm.     |
|15203207 | Kalkberg-Fm. | Kalkberg-Fm.     |
|15203208 | Bavugls-Fm. | Bavugls-Fm.     |
|15203209 | Nolla-Kristallin | Nolla-Kristallin     |
|15203210 | Falknis-Decke: Flysch | Falknis-Decke: Flysch     |
|15203211 | Globorotalien-Sch. | Globorotalien-Sch.     |
|15203212 | Quarzsandstein-Flysch | Quarzsandstein-Flysch     |
|15203213 | Tristel-Fm. | Tristel-Fm.     |
|15203214 | Fleckenkalk-Flysch | Fleckenkalk-Flysch     |
|15203215 | Jes-Fm. | Jes-Fm.     |
|15203216 | Falknis-Brekzie | Falknis-Brekzie     |
|15203217 | Sanalada-Fm. | Sanalada-Fm.     |
|15203218 | Panier-Fm. | Panier-Fm.     |
|15203219 | Sulzfluh-Decke: Flysch | Sulzfluh-Decke: Flysch     |
|15203220 | Sulzfluh-Kalk | Sulzfluh-Kalk     |
|15203221 | Sulzfluh-Decke: Granit | Sulzfluh-Decke: Granit     |
|15203222 | Tasna-Decke: Flysch | Tasna-Decke: Flysch     |
|15203223 | Steinsberg-Kalk | Steinsberg-Kalk     |
|15203224 | Plattamala-Granit | Plattamala-Granit     |
|15203225 | Série Rousse | Série Rousse     |
|15203226 | Série Grise | Série Grise     |
|15203227 | Garda-Bordon-Fm. | Garda-Bordon-Fm.     |
|15203228 | Fêta-d&#39;Août-Fm. | Fêta-d&#39;Août-Fm.     |
|15203229 | Allalin-Metagabbro | Allalin-Metagabbro     |
|15203230 | Arosa-Decke: Melange | Arosa-Decke: Melange     |
|15203231 | Verspala-Fm. | Verspala-Fm.     |
|15203232 | Lavagna-Fm. | Lavagna-Fm.     |
|15203233 | Palombini-Fm. | Palombini-Fm.     |
|15203234 | Arosa-Decke: Calpionellenkalk | Arosa-Decke: Calpionellenkalk     |
|15203235 | Arosa-Decke: Radiolarit | Arosa-Decke: Radiolarit     |
|15203236 | Arosa-Decke: Ophiolith | Arosa-Decke: Ophiolith     |
|15203238 | Coulaytes-Melange: Buufal-Konglomerat | Coulaytes-Melange: Buufal-Konglomerat     |
|15203239 | Sommant-Fm.: Langel-Mb. | Sommant-Fm.: Langel-Mb.     |
|15203240 | Pralet-Fm.: Obere Rauwacke | Pralet-Fm.: Obere Rauwacke     |
|15203241 | Clôt-la-Cime-Fm.: Gips | Clôt-la-Cime-Fm.: Gips     |
|15203242 | Brekzien-Decke: Couches-Rouges | Brekzien-Decke: Couches-Rouges     |
|15203243 | Brekzien-Decke: Trias: Rauwacke | Brekzien-Decke: Trias: Rauwacke     |
|15203244 | Manche-Fm.: Lamperehubel-Sandstein | Manche-Fm.: Lamperehubel-Sandstein     |
|15203245 | Perrières-Fm.: Gets-Ophiolith | Perrières-Fm.: Gets-Ophiolith     |
|15203246 | Piz-Terri-Lunschania: Obere Kalk- und Tonschiefer | Piz-Terri-Lunschania: Obere Kalk- und Tonschiefer     |
|15203247 | Piz-Terri-Lunschania: Gneisquarzit | Piz-Terri-Lunschania: Gneisquarzit     |
|15203248 | Piz-Terri-Lunschania: Untere Kalk- und Tonschiefer | Piz-Terri-Lunschania: Untere Kalk- und Tonschiefer     |
|15203249 | Aul-Marmor | Aul-Marmor     |
|15203250 | Piz-Terri-Lunschania: Dolomitbrekzie | Piz-Terri-Lunschania: Dolomitbrekzie     |
|15203251 | Grava-Decke: Gryphäenkalk | Grava-Decke: Gryphäenkalk     |
|15203252 | Unterpenninikum: Trias | Unterpenninikum: Trias     |
|15203253 | Zervreila-Granitgneis | Zervreila-Granitgneis     |
|15203254 | Garenstock-Augengneis | Garenstock-Augengneis     |
|15203255 | Salahorn-Fm.: Glimmerschiefer und Paragneis | Salahorn-Fm.: Glimmerschiefer und Paragneis     |
|15203256 | Adula-Decke: Amphibolit | Adula-Decke: Amphibolit     |
|15203257 | Zone Submédiane: Melange | Zone Submédiane: Melange     |
|15203258 | Zone Submédiane: Truche-Brekzie | Zone Submédiane: Truche-Brekzie     |
|15203259 | Zone Submédiane: Trom-Brekzie | Zone Submédiane: Trom-Brekzie     |
|15203260 | Zone Submédiane: Exergillod-Brekzie | Zone Submédiane: Exergillod-Brekzie     |
|15203261 | Zone Submédiane: Troublon-Kalk | Zone Submédiane: Troublon-Kalk     |
|15203262 | Zone Submédiane: Zünegg-Knollenkalk | Zone Submédiane: Zünegg-Knollenkalk     |
|15203263 | Zone Submédiane: Hauta-Crêtaz-Fm. | Zone Submédiane: Hauta-Crêtaz-Fm.     |
|15203264 | Zone Submédiane: Pointe-de-l&#39;Au-Brekzie | Zone Submédiane: Pointe-de-l&#39;Au-Brekzie     |
|15203265 | Zone Submédiane: Bonaveau-Kalk | Zone Submédiane: Bonaveau-Kalk     |
|15203266 | Zone Submédiane: Sex-du-Tronc-Kalk | Zone Submédiane: Sex-du-Tronc-Kalk     |
|15203267 | Zone Submédiane: Grand-Herba-Kalk | Zone Submédiane: Grand-Herba-Kalk     |
|15203268 | Oudiou-Fm. | Oudiou-Fm.     |
|15203269 | Klippen-Decke: Malm | Klippen-Decke: Malm     |
|15203270 | Moléson-Fm.: Albeuve-Serie | Moléson-Fm.: Albeuve-Serie     |
|15203271 | Sciernes-d&#39;Albeuve-Fm.: Kummli-Sch. | Sciernes-d&#39;Albeuve-Fm.: Kummli-Sch.     |
|15203272 | Klippen-Decke: Dogger | Klippen-Decke: Dogger     |
|15203273 | Mytilus-Sch.: Col-de-Cordon-Mb.: Stockenflue-Kalk | Mytilus-Sch.: Col-de-Cordon-Mb.: Stockenflue-Kalk     |
|15203274 | Sommant-Fm.: Mieussy-Mb. | Sommant-Fm.: Mieussy-Mb.     |
|15203275 | Klippen-Decke: Lias | Klippen-Decke: Lias     |
|15203276 | Klippen-Decke: Trias | Klippen-Decke: Trias     |
|15203277 | Pralet-Fm. | Pralet-Fm.     |
|15203278 | Pralet-Fm.: Balmi-Mb. | Pralet-Fm.: Balmi-Mb.     |
|15203279 | Wiriehorn-Fm.: Bodeflue-Mb. | Wiriehorn-Fm.: Bodeflue-Mb.     |
|15203280 | Wiriehorn-Fm.: Wildgrimmi-Mb. | Wiriehorn-Fm.: Wildgrimmi-Mb.     |
|15203281 | St-Triphon-Fm.: Dorchaux-Mb.: Untere Rauwacke | St-Triphon-Fm.: Dorchaux-Mb.: Untere Rauwacke     |
|15203282 | Infrabrèche-Melange | Infrabrèche-Melange     |
|15203283 | Wägital-Decke: Flysch | Wägital-Decke: Flysch     |
|15203284 | Gurnigel-Decke: Flysch-5 | Gurnigel-Decke: Flysch-5     |
|15203285 | Voirons-Decke: Flysch | Voirons-Decke: Flysch     |
|15203286 | Boëge-Mergel | Boëge-Mergel     |
|15203287 | Vouan-Konglomerat | Vouan-Konglomerat     |
|15203288 | Voirons-Sandstein | Voirons-Sandstein     |
|15203291 | Klippen-Decke: Couches-Rouges | Klippen-Decke: Couches-Rouges     |
|15203292 | Simmen-Decke: Flysch | Simmen-Decke: Flysch     |
|15203293 | Trepsen-Flysch | Trepsen-Flysch     |
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
|15201181 | Rhein- und Aareschotter | Rhein- und Aareschotter     |
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
|15203318 | Lebendun-Komplex | Lebendun-Komplex     |
|15203319 | Sabbione-Sandstein | Sabbione-Sandstein     |
|15203320 | Monte-Leone-Decke: Grundgebirge | Monte-Leone-Decke: Grundgebirge     |
|15203321 | Ganter-Gneis | Ganter-Gneis     |
|15203322 | Ritter-Gneis | Ritter-Gneis     |
|15203323 | Geisspfad-Serpentinit | Geisspfad-Serpentinit     |
|15203325 | Holzerspitz-Kalkschiefer | Holzerspitz-Kalkschiefer     |
|15203327 | Rinderbach-Fm. | Rinderbach-Fm.     |
|15203328 | Langenegg-Fm. | Langenegg-Fm.     |
|15201536 | Niederterrassenschotter, oberste Terrasse | Niederterrassenschotter, oberste Terrasse     |
|15201537 | Tiefere Deckenschotter, unteres Niveau | Tiefere Deckenschotter, unteres Niveau     |
|15201538 | Tiefere Deckenschotter, oberes Niveau | Tiefere Deckenschotter, oberes Niveau     |
|15201539 | Kunkels-Formation | Kunkels-Formation     |
|15201540 | Alluvion von Ransun | Alluvion von Ransun     |
|15201541 | Rüdlingen-Till | Rüdlingen-Till     |
|15201542 | Niklaushalden-Formation | Niklaushalden-Formation     |
|15201556 | Saxegrabe-Schotter | Saxegrabe-Schotter     |
|15201557 | Zweidlen-Schotter | Zweidlen-Schotter     |
|15201558 | Burgacher-Schotter | Burgacher-Schotter     |
|15201559 | Chatzenstig-Schotter | Chatzenstig-Schotter     |
|15201560 | Wasterkingen-Schotter | Wasterkingen-Schotter     |
|15203563 | Zentralschweizerische Klippen: Couches-Rouges | Zentralschweizerische Klippen: Couches-Rouges     |
|15203564 | Wägital-Flysch: Oberer Teil (Paläogen) | Wägital-Flysch: Oberer Teil (Paläogen)     |
|15203565 | Wägital-Flysch: Unterer Teil (Kreide) | Wägital-Flysch: Unterer Teil (Kreide)     |
|15203566 | Wägital-Flysch: Basaler tektonisierter Teil | Wägital-Flysch: Basaler tektonisierter Teil     |
|15203567 | Gibel- und Griggeli-Fm. | Gibel- und Griggeli-Fm.     |
|15203568 | Mittelpenninikum: Trias: Dolomit | Mittelpenninikum: Trias: Dolomit     |
|15203569 | Mittelpenninikum: Trias: Dolomit und Kalk | Mittelpenninikum: Trias: Dolomit und Kalk     |
|15203570 | Mittelpenninikum: Trias: Dolomit und Rauwacke | Mittelpenninikum: Trias: Dolomit und Rauwacke     |
|15203571 | Mittelpenninikum: Trias: Rauwacke | Mittelpenninikum: Trias: Rauwacke     |
|15203572 | Mittelpenninikum: Trias: Gipsmergel und Sandstein | Mittelpenninikum: Trias: Gipsmergel und Sandstein     |
|15203573 | Schlieren-Sandstein: Im Paläogen tektonisch überprägt | Schlieren-Sandstein: Im Paläogen tektonisch überprägt     |
|15203574 | Leimern-Sch. | Leimern-Sch.     |
|15203575 | Mittelpenninikum: Trias: Rauwacke und Sandstein | Mittelpenninikum: Trias: Rauwacke und Sandstein     |
|15203576 | Guber- Schoni- und Schlieren-Sandstein | Guber- Schoni- und Schlieren-Sandstein     |
|15203577 | Zentralschweizerische Klippen: Mittellias | Zentralschweizerische Klippen: Mittellias     |
|15203579 | Nolla-Tonschiefer: Quarzsandstein | Nolla-Tonschiefer: Quarzsandstein     |
|15204026 | Kössen-Fm.: Mitgel-Mb. | Kössen-Fm.: Mitgel-Mb.     |
|15204027 | Kössen-Fm.: Ramoz-Mb. | Kössen-Fm.: Ramoz-Mb.     |
|15204028 | Kössen-Fm.: Schesaplana-Mb. | Kössen-Fm.: Schesaplana-Mb.     |
|15204029 | Kössen-Fm.: Alplihorn-Mb. | Kössen-Fm.: Alplihorn-Mb.     |
|15204030 | Ostalpin: Hauptdolomit-Gr. | Ostalpin: Hauptdolomit-Gr.     |
|15204031 | Murtèr-Plattenkalk | Murtèr-Plattenkalk     |
|15204032 | Murteret-Dolomit | Murteret-Dolomit     |
|15204033 | Diavel-Fm. | Diavel-Fm.     |
|15204034 | Quattervals-Fm. | Quattervals-Fm.     |
|15204035 | Quattervals-Fm.: Crappa-Mala-Mb. | Quattervals-Fm.: Crappa-Mala-Mb.     |
|15204036 | Quattervals-Fm.: Pra-Grata-Mb. | Quattervals-Fm.: Pra-Grata-Mb.     |
|15204037 | Müschauns-Dolomit | Müschauns-Dolomit     |
|15204038 | Ostalpin: Raibl-Gr. | Ostalpin: Raibl-Gr.     |
|15204039 | Fanez-Fm. | Fanez-Fm.     |
|15204040 | Fanez-Fm.: Valbella-Mb. | Fanez-Fm.: Valbella-Mb.     |
|15204041 | Fanez-Fm.: Dolomit | Fanez-Fm.: Dolomit     |
|15204042 | Fanez-Fm.: Mezdi-Mb. | Fanez-Fm.: Mezdi-Mb.     |
|15204043 | Fanez-Fm.: Cluozza-Mb. | Fanez-Fm.: Cluozza-Mb.     |
|15204044 | Fanez-Fm.: Stugl-Gips | Fanez-Fm.: Stugl-Gips     |
|15204045 | Minger-Fm. | Minger-Fm.     |
|15204046 | Minger-Fm.: Dolomit | Minger-Fm.: Dolomit     |
|15204047 | Mingèr-Fm.: Mora-Mb. | Mingèr-Fm.: Mora-Mb.     |
|15201562 | Tubeschwanz-Schotter | Tubeschwanz-Schotter     |
|15201563 | Weisweil-Schotter | Weisweil-Schotter     |
|15201561 | Paradiesgärtli-Schotter | Paradiesgärtli-Schotter     |
|15201565 | Stetten-Schotter | Stetten-Schotter     |
|15201544 | Volken-Lehm | Volken-Lehm     |
|15201549 | Weiach-Schotter | Weiach-Schotter     |
|15201545 | Rheinau-Till | Rheinau-Till     |
|15201546 | Ellikerholz-Formation | Ellikerholz-Formation     |
|15201547 | Eggholz-Formation | Eggholz-Formation     |
|15201548 | Bannhalden-Schotter | Bannhalden-Schotter     |
|15201550 | Balm-Schotter | Balm-Schotter     |
|15201551 | Windlach-Till | Windlach-Till     |
|15201552 | Südranden-Till | Südranden-Till     |
|15201553 | Schlossbuck-Schotter | Schlossbuck-Schotter     |
|15201554 | Risibüel-Schotter | Risibüel-Schotter     |
|15201555 | Schmerlet- und Toktri-Formation, undifferenziert | Schmerlet- und Toktri-Formation, undifferenziert     |
|15201534 | Niederterrassenschotter, tiefere Niveaus | Niederterrassenschotter, tiefere Niveaus     |
|15201564 | Hasli-Formation | Hasli-Formation     |
|15201532 | Bergsturzablagerung von Bargis | Bergsturzablagerung von Bargis     |
|15201533 | Bergsturzablagerung von Fidaz | Bergsturzablagerung von Fidaz     |
|15201543 | Stadel-Till | Stadel-Till     |
|15201535 | Niederterrassenschotter, zweitoberste Terrasse | Niederterrassenschotter, zweitoberste Terrasse     |
|15206026 | Undifferenzierte stratigraphische Einheit: Dogger | Undifferenzierte stratigraphische Einheit: Dogger     |
|15206027 | Undifferenzierte stratigraphische Einheit: Malm | Undifferenzierte stratigraphische Einheit: Malm     |
|15206028 | Undifferenzierte stratigraphische Einheit: Kreide | Undifferenzierte stratigraphische Einheit: Kreide     |
|15206029 | Undifferenzierte stratigraphische Einheit: Trias | Undifferenzierte stratigraphische Einheit: Trias     |
|15206030 | Undifferenzierte lithologische Einheit: Sedimentgestein | Undifferenzierte lithologische Einheit: Sedimentgestein     |
|15206031 | Undifferenzierte lithologische Einheit: Kristallingestein | Undifferenzierte lithologische Einheit: Kristallingestein     |
|15206032 | Undifferenzierte lithologische Einheit: Granit | Undifferenzierte lithologische Einheit: Granit     |
|15206033 | Undifferenzierte stratigraphische Einheit | Undifferenzierte stratigraphische Einheit     |
|15206034 | Undifferenzierte stratigraphische Einheit: Mesozoikum | Undifferenzierte stratigraphische Einheit: Mesozoikum     |
|15206035 | Undifferenzierte lithologische Einheit: Rhyolith | Undifferenzierte lithologische Einheit: Rhyolith     |
|15206036 | Undifferenzierte lithologische Einheit: Grüngestein | Undifferenzierte lithologische Einheit: Grüngestein     |
|15206037 | Undifferenzierte lithologische Einheit: Amphibolit | Undifferenzierte lithologische Einheit: Amphibolit     |
|15206038 | Undifferenzierte lithologische Einheit: Quarzgang | Undifferenzierte lithologische Einheit: Quarzgang     |
|15206039 | Undifferenzierte lithologische Einheit: Aplit | Undifferenzierte lithologische Einheit: Aplit     |
|15206040 | Undifferenzierte lithologische Einheit: Pegmatit | Undifferenzierte lithologische Einheit: Pegmatit     |
|15204048 | Garone-Fm. | Garone-Fm.     |
|15204049 | Arlberg-Fm. | Arlberg-Fm.     |
|15204050 | Partnach-Fm. | Partnach-Fm.     |
|15204051 | Altein-Fm. | Altein-Fm.     |
|15204052 | Altein-Fm.: Parai-Alba-Mb. | Altein-Fm.: Parai-Alba-Mb.     |
|15204053 | Prosanto-Fm. | Prosanto-Fm.     |
|15204054 | Vallatscha-Fm. | Vallatscha-Fm.     |
|15204055 | Vallatscha-Fm.: Tiaun-Brekzie | Vallatscha-Fm.: Tiaun-Brekzie     |
|15204056 | Vallatscha-Fm.: Dolomit | Vallatscha-Fm.: Dolomit     |
|15204057 | Vallatscha-Fm.: Turettas-Mb. | Vallatscha-Fm.: Turettas-Mb.     |
|15204058 | Vallatscha-Fm.: Landwasser-Mb. | Vallatscha-Fm.: Landwasser-Mb.     |
|15204059 | S-charl-Fm. | S-charl-Fm.     |
|15204060 | S-charl-Fm.: Sertig-Mb. | S-charl-Fm.: Sertig-Mb.     |
|15204061 | S-charl-Fm.: Ravais-ch-Mb. | S-charl-Fm.: Ravais-ch-Mb.     |
|15204062 | Reiflingen-Fm. | Reiflingen-Fm.     |
|15204063 | Ducan-Fm. | Ducan-Fm.     |
|15204064 | Ducan-Fm.: Trochitendolomit | Ducan-Fm.: Trochitendolomit     |
|15204065 | Ducan-Fm.: Brachiopodenkalk | Ducan-Fm.: Brachiopodenkalk     |
|15204066 | Ducan-Fm.: Eisendolomit-Mb. | Ducan-Fm.: Eisendolomit-Mb.     |
|15204067 | Ducan-Fm.: Gracilis-Mb. | Ducan-Fm.: Gracilis-Mb.     |
|15204068 | Gutenstein-Fm. | Gutenstein-Fm.     |
|15204069 | Reichenhall-Fm. | Reichenhall-Fm.     |
|15204070 | Fuorn-Fm. | Fuorn-Fm.     |
|15204071 | Fuorn-Fm.: Punt-la-Drossa-Mb. | Fuorn-Fm.: Punt-la-Drossa-Mb.     |
|15204072 | Fuorn-Fm.: Pflanzenquarzit | Fuorn-Fm.: Pflanzenquarzit     |
|15204073 | Fuorn-Fm.: Unterer Teil | Fuorn-Fm.: Unterer Teil     |
|15204074 | Ruina- und Chazfora-Fm. | Ruina- und Chazfora-Fm.     |
|15204075 | Chazforà-Fm. | Chazforà-Fm.     |
|15204076 | Chazforà-Fm.: Tuors-Mb. | Chazforà-Fm.: Tuors-Mb.     |
|15204077 | Chazforà-Fm.: Val-Püra-Mb. | Chazforà-Fm.: Val-Püra-Mb.     |
|15204078 | Präbichl-Fm. | Präbichl-Fm.     |
|15204079 | Ruina-Fm. | Ruina-Fm.     |
|15204080 | Ruina-Fm.: Sandhubel-Mb. | Ruina-Fm.: Sandhubel-Mb.     |
|15204081 | Ruina-Fm.: Bellaluna-Mb. | Ruina-Fm.: Bellaluna-Mb.     |
|15204082 | Mönchalp-Augengneis | Mönchalp-Augengneis     |
|15204083 | Tschuggen-Augengneis | Tschuggen-Augengneis     |
|15204084 | Güstizia-Gneis | Güstizia-Gneis     |
|15204085 | Plasseggen-Augengneis | Plasseggen-Augengneis     |
|15204086 | Ostalpin: Trias | Ostalpin: Trias     |
|15204087 | Ostalpin: Dogger | Ostalpin: Dogger     |
|15204088 | Ostalpin: Radiolarit-Aptychenkalk | Ostalpin: Radiolarit-Aptychenkalk     |
|15204089 | Ostalpin: Kreide | Ostalpin: Kreide     |
|15204090 | Ostalpin: Lias | Ostalpin: Lias     |
|15204091 | Ostalpin: Grundgebirge | Ostalpin: Grundgebirge     |
|15204092 | Nair-Porphyroid | Nair-Porphyroid     |
|15201566 | Plaffeien-Seetone | Plaffeien-Seetone     |
|15201567 | Plasselb-Stauschotter | Plasselb-Stauschotter     |
|15206041 | Undifferenzierte lithologische Einheit: Prasinit | Undifferenzierte lithologische Einheit: Prasinit     |
|15206042 | Undifferenzierte lithologische Einheit: Serpentinit | Undifferenzierte lithologische Einheit: Serpentinit     |
|15206043 | Undifferenzierte lithologische Einheit: Mineralisierter Gang | Undifferenzierte lithologische Einheit: Mineralisierter Gang     |
|15206044 | Undifferenzierte lithologische Einheit: Mikrogranit | Undifferenzierte lithologische Einheit: Mikrogranit     |
|15206045 | Undifferenzierte stratigraphische Einheit: Rhät | Undifferenzierte stratigraphische Einheit: Rhät     |
|15206046 | Undifferenzierte lithologische Einheit: Biogener Kalkstein | Undifferenzierte lithologische Einheit: Biogener Kalkstein     |
|15206047 | Undifferenzierte lithologische Einheit: Rodingit | Undifferenzierte lithologische Einheit: Rodingit     |
|15206048 | Undifferenzierte lithologische Einheit: Saures Ganggestein | Undifferenzierte lithologische Einheit: Saures Ganggestein     |
|15206049 | Undifferenzierte lithologische Einheit: Basisches Ganggestein | Undifferenzierte lithologische Einheit: Basisches Ganggestein     |
|15206050 | Undifferenzierte lithologische Einheit: Eklogit | Undifferenzierte lithologische Einheit: Eklogit     |
|15206051 | Undifferenzierte lithologische Einheit: Mylonit | Undifferenzierte lithologische Einheit: Mylonit     |
|15206052 | Undifferenzierte lithologische Einheit: Kalksilikatfels | Undifferenzierte lithologische Einheit: Kalksilikatfels     |
|15206053 | Undifferenzierte lithologische Einheit: Marmor | Undifferenzierte lithologische Einheit: Marmor     |
|15206054 | Undifferenzierte lithologische Einheit: Sedimentäre Brekzie | Undifferenzierte lithologische Einheit: Sedimentäre Brekzie     |
|15206055 | Undifferenzierte stratigraphische Einheit: Paläozoikum | Undifferenzierte stratigraphische Einheit: Paläozoikum     |
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
|15201459 | Novazzano-Sand | Novazzano-Sand     |
|15201444 | Löss, undifferenziert | Löss, undifferenziert     |
|15201707 | Humbel-Schotter | Humbel-Schotter     |
|15201623 | Hochterrasse, unteres Niveau | Hochterrasse, unteres Niveau     |
|15201712 | Birlibänz-Schotter | Birlibänz-Schotter     |
|15201714 | Wentzwiller-Schotter | Wentzwiller-Schotter     |
|15201629 | Zurzach-Formation | Zurzach-Formation     |
|15201715 | Bellevue-Schotter | Bellevue-Schotter     |
|15201713 | Schönenbuch-Schotter | Schönenbuch-Schotter     |
|15206056 | Undifferenzierte stratigraphische Einheit: Känozoikum | Undifferenzierte stratigraphische Einheit: Känozoikum     |
|15206057 | Undifferenzierte lithologische Einheit: Ultramafisches Gestein | Undifferenzierte lithologische Einheit: Ultramafisches Gestein     |
|15206058 | Undifferenzierte lithologische Einheit: Verwitterter Fels | Undifferenzierte lithologische Einheit: Verwitterter Fels     |
|15206059 | Undifferenzierte lithologische Einheit: Ophikalzit | Undifferenzierte lithologische Einheit: Ophikalzit     |
|15206060 | Undifferenzierte lithologische Einheit: Talkschiefer | Undifferenzierte lithologische Einheit: Talkschiefer     |
|15206061 | Undifferenzierte lithologische Einheit: Mirkodiorit | Undifferenzierte lithologische Einheit: Mirkodiorit     |
|15206062 | Undifferenzierte lithologische Einheit: Quarzit | Undifferenzierte lithologische Einheit: Quarzit     |
|15206063 | Undifferenzierte lithologische Einheit: Fuchsit-Zoisitschiefer | Undifferenzierte lithologische Einheit: Fuchsit-Zoisitschiefer     |
|15206064 | Undifferenzierte lithologische Einheit: Konglomerat | Undifferenzierte lithologische Einheit: Konglomerat     |
|15206065 | Undifferenzierte lithologische Einheit: Glaukophanschiefer | Undifferenzierte lithologische Einheit: Glaukophanschiefer     |
|15206066 | Bündnerschiefer | Bündnerschiefer     |
|15206067 | Undifferenzierte lithologische Einheit: Augengneis | Undifferenzierte lithologische Einheit: Augengneis     |
|15206068 | Undifferenzierte lithologische Einheit: Granat-Glimmerschiefer | Undifferenzierte lithologische Einheit: Granat-Glimmerschiefer     |
|15206069 | Undifferenzierte lithologische Einheit: Albit-Muskowitschiefer | Undifferenzierte lithologische Einheit: Albit-Muskowitschiefer     |
|15206070 | Undifferenzierte lithologische Einheit: Gneis | Undifferenzierte lithologische Einheit: Gneis     |
|15201460 | Bergsturzablagerungen vom Stützwald | Bergsturzablagerungen vom Stützwald     |
|15204093 | Nair-Porphyroid: Lavatèra-Brekzie | Nair-Porphyroid: Lavatèra-Brekzie     |
|15204094 | Varaina-Schiefer | Varaina-Schiefer     |
|15204095 | Sprenkel-Schiefer | Sprenkel-Schiefer     |
|15204096 | Fedoz-Gneiskomplex | Fedoz-Gneiskomplex     |
|15204097 | Fedoz-Metagabbro | Fedoz-Metagabbro     |
|15204098 | Maloja-Orthogneis | Maloja-Orthogneis     |
|15204099 | Maloja-Gneiskomplex | Maloja-Gneiskomplex     |
|15204100 | Ur-Brekzie | Ur-Brekzie     |
|15204101 | Tschima-da-Flix-Granit | Tschima-da-Flix-Granit     |
|15204102 | Err-Granodiorit | Err-Granodiorit     |
|15204103 | Ostalpin: Postvariszische Diabasgänge | Ostalpin: Postvariszische Diabasgänge     |
|15204104 | Flüela-Augengneis | Flüela-Augengneis     |
|15204105 | Dorfberg-Gneis | Dorfberg-Gneis     |
|15204106 | Allgäu-Fm.: Alpisella-Mb.: Chaschauna-Brekzie | Allgäu-Fm.: Alpisella-Mb.: Chaschauna-Brekzie     |
|15204107 | Sesvenna-Augengneis | Sesvenna-Augengneis     |
|15204108 | Vaüglia-Granodiorit | Vaüglia-Granodiorit     |
|15204109 | Mingèr-Fm.: Mora-Mb.: Döss-Radond-Vulkanite | Mingèr-Fm.: Mora-Mb.: Döss-Radond-Vulkanite     |
|15204110 | Augsten-Brekzie | Augsten-Brekzie     |
|15204111 | Piz-Trovat-Metarhyolith | Piz-Trovat-Metarhyolith     |
|15204112 | Sass-Queder-Metarhyolith | Sass-Queder-Metarhyolith     |
|15204113 | La-Rösa-Orthogneis | La-Rösa-Orthogneis     |
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
|15206071 | Undifferenzierte lithologische Einheit: Graphitschiefer | Undifferenzierte lithologische Einheit: Graphitschiefer     |
|15206072 | Undifferenzierte lithologische Einheit: Glimmerschiefer | Undifferenzierte lithologische Einheit: Glimmerschiefer     |
|15206073 | Undifferenzierte lithologische Einheit: Garbenschiefer | Undifferenzierte lithologische Einheit: Garbenschiefer     |
|15206074 | Undifferenzierte lithologische Einheit: Diorit | Undifferenzierte lithologische Einheit: Diorit     |
|15206075 | Undifferenzierte lithologische Einheit: Gabbro | Undifferenzierte lithologische Einheit: Gabbro     |
|15206076 | Undifferenzierte lithologische Einheit: Orthogneis | Undifferenzierte lithologische Einheit: Orthogneis     |
|15206077 | Undifferenzierte lithologische Einheit: Paragneis | Undifferenzierte lithologische Einheit: Paragneis     |
|15206078 | Undifferenzierte lithologische Einheit: Vulkanisches Gestein | Undifferenzierte lithologische Einheit: Vulkanisches Gestein     |
|15206079 | Undifferenzierte lithologische Einheit: Basalt | Undifferenzierte lithologische Einheit: Basalt     |
|15206080 | Undifferenzierte stratigraphische Einheit: Karbon | Undifferenzierte stratigraphische Einheit: Karbon     |
|15206081 | Undifferenzierte lithologische Einheit: Chloritschiefer | Undifferenzierte lithologische Einheit: Chloritschiefer     |
|15206082 | Undifferenzierte lithologische Einheit: Phyllit | Undifferenzierte lithologische Einheit: Phyllit     |
|15206083 | Undifferenzierte lithologische Einheit: Quarzphyllit | Undifferenzierte lithologische Einheit: Quarzphyllit     |
|15206084 | Bündnerschiefer: Kalkschiefer | Bündnerschiefer: Kalkschiefer     |
|15206085 | Bündnerschiefer: Tonschiefer | Bündnerschiefer: Tonschiefer     |
|15204114 | Carale-Schiefer | Carale-Schiefer     |
|15204115 | Gosau-Gruppe | Gosau-Gruppe     |
|15204116 | Morteratsch-Serpentinit | Morteratsch-Serpentinit     |
|15204117 | Forun-Augengneis | Forun-Augengneis     |
|15204118 | Kesch-Augengneis | Kesch-Augengneis     |
|15204119 | Ostalpin: Prävariszisches polyzyklisches Grundgebirge | Ostalpin: Prävariszisches polyzyklisches Grundgebirge     |
|15204120 | Silvretta-Decke: Jüngere Orthogneise | Silvretta-Decke: «Jüngere Orthogneise»     |
|15204121 | Silvretta-Decke: Ältere Orthogneise | Silvretta-Decke: «Ältere Orthogneise»     |
|15204122 | Val-Rude-Orthogneis | Val-Rude-Orthogneis     |
|15204123 | Corvatsch-Granitkomplex: Corvatsch-Granodiorit | Corvatsch-Granitkomplex: Corvatsch-Granodiorit     |
|15204124 | Julier-Granodiorit | Julier-Granodiorit     |
|15204125 | Sasso-Rosso-Granodiorit | Sasso-Rosso-Granodiorit     |
|15204126 | Vallatscha-Fm.: Lavinèr-Brekzie | Vallatscha-Fm.: Lavinèr-Brekzie     |
|15204127 | Haupter-Brekzie | Haupter-Brekzie     |
|15204128 | Ostalpin: Postvariszische Vulkanite und Sedimente | Ostalpin: Postvariszische Vulkanite und Sedimente     |
|15204130 | Garone-, Vallatscha-,Prosanto- und Altein-Fm. | Garone-, Vallatscha-,Prosanto- und Altein-Fm.     |
|15204132 | Ostalpin: Variszische Intrusiva | Ostalpin: Variszische Intrusiva     |
|15204135 | Ostalpin: Prävariszischer Orthogneis | Ostalpin: Prävariszischer Orthogneis     |
|15201653 | Lei-Schotter | Lei-Schotter     |
|15201683 | Tannboden-Schotter | Tannboden-Schotter     |
|15206086 | Undifferenzierte lithologische Einheit: Migmatit | Undifferenzierte lithologische Einheit: Migmatit     |
|15206087 | Undifferenzierte lithologische Einheit: Tonalit | Undifferenzierte lithologische Einheit: Tonalit     |
|15206088 | Undifferenzierte lithologische Einheit: Syenit | Undifferenzierte lithologische Einheit: Syenit     |
|15206089 | Undifferenzierte lithologische Einheit: Tektonit | Undifferenzierte lithologische Einheit: Tektonit     |
|15206090 | Undifferenzierte lithologische Einheit: Hornfels | Undifferenzierte lithologische Einheit: Hornfels     |
|15206091 | Undifferenzierte lithologische Einheit: Hornblendegneis | Undifferenzierte lithologische Einheit: Hornblendegneis     |
|15206092 | Undifferenzierte lithologische Einheit: Biotit-Plagioklasgneis | Undifferenzierte lithologische Einheit: Biotit-Plagioklasgneis     |
|15206093 | Undifferenzierte lithologische Einheit: Bändergneis | Undifferenzierte lithologische Einheit: Bändergneis     |
|15206094 | Undifferenzierte lithologische Einheit: Zweiglimmergneis | Undifferenzierte lithologische Einheit: Zweiglimmergneis     |
|15206095 | Undifferenzierte lithologische Einheit: Phyllitgneis | Undifferenzierte lithologische Einheit: Phyllitgneis     |
|15206096 | Undifferenzierte lithologische Einheit: Peridotit | Undifferenzierte lithologische Einheit: Peridotit     |
|15206097 | Undifferenzierte lithologische Einheit: Bänder- und Schollenamphibolit | Undifferenzierte lithologische Einheit: Bänder- und Schollenamphibolit     |
|15206098 | Undifferenzierte lithologische Einheit: Granatamphibolit | Undifferenzierte lithologische Einheit: Granatamphibolit     |
|15206099 | Undifferenzierte lithologische Einheit: Diabasgang | Undifferenzierte lithologische Einheit: Diabasgang     |
|15206100 | Undifferenzierte stratigraphische Einheit: Perm | Undifferenzierte stratigraphische Einheit: Perm     |
|15204136 | Ostalpin: Prävariszischer Paragneis | Ostalpin: Prävariszischer Paragneis     |
|15204137 | Ostalpin: Prävariszische Grüngesteine | Ostalpin: Prävariszische Grüngesteine     |
|15204138 | Uglix-Plattenkalk | Uglix-Plattenkalk     |
|15204139 | Parait-Chavagl-Granit | Parait-Chavagl-Granit     |
|15204140 | God-Drosa-Flysch: Clavadatsch-Brekzie | God-Drosa-Flysch: Clavadatsch-Brekzie     |
|15204141 | Corno-di-Campo-Granodiorit | Corno-di-Campo-Granodiorit     |
|15204142 | Campocologno-Gabbro | Campocologno-Gabbro     |
|15204143 | Celerina-Orthogneis | Celerina-Orthogneis     |
|15204144 | Tonale-Schiefer | Tonale-Schiefer     |
|15204145 | Ostalpin: Raibl-Gr.: Gips | Ostalpin: Raibl-Gr.: Gips     |
|15204146 | Ostalpin: Raibl-Gr.: Rauwacke | Ostalpin: Raibl-Gr.: Rauwacke     |
|15204147 | Arlberg-Fm.: Rifffazies | Arlberg-Fm.: Rifffazies     |
|15204148 | Ducan- und S-charl-Fm. | Ducan- und S-charl-Fm.     |
|15204149 | Ostalpin: Raibl-Gr.: Dolomit | Ostalpin: Raibl-Gr.: Dolomit     |
|15204150 | Ostalpin: Hauptdolomit-Gr.: bituminöser Dolomit | Ostalpin: Hauptdolomit-Gr.: bituminöser Dolomit     |
|15204151 | Zentralschweizerische Klippen: Raibl-Gr. | Zentralschweizerische Klippen: Raibl-Gr.     |
|15205001 | Dent-Blanche-Decke: Sedimentbedeckung | Dent-Blanche-Decke: Sedimentbedeckung     |
|15205002 | Petit-Dolin-Kalkbrekzie | Petit-Dolin-Kalkbrekzie     |
|15201064 | Löhningen-Engiwald-Vergletscherung | Löhningen-Engiwald-Vergletscherung     |
|15201065 | Engiwald-Vorstoss | Engiwald-Vorstoss     |
|15201066 | Rüfenach-Vorstoss | Rüfenach-Vorstoss     |
|15201175 | Reusstal-Sand | Reusstal-Sand     |
|15201176 | Reusstal-Lehm | Reusstal-Lehm     |
|15201067 | Löhningen-Vorstoss | Löhningen-Vorstoss     |
|15201068 | Remigen-Vorstoss | Remigen-Vorstoss     |
|15201177 | Hausen-Lehm | Hausen-Lehm     |
|15201178 | Hausen-Moräne | Hausen-Moräne     |
|15201069 | Remigen-Schotter | Remigen-Schotter     |
|15201070 | Meikirch-Interglazial | Meikirch-Interglazial     |
|15201071 | Ältere Beckenfüllungen | Ältere Beckenfüllungen     |
|15201072 | Hagenholz-Eiszeit | Hagenholz-Eiszeit     |
|15201179 | Ruckfeld-Schotter | Ruckfeld-Schotter     |
|15201073 | Hagenholz-Vergletscherung | Hagenholz-Vergletscherung     |
|15201074 | Hagenholz-Vorstoss | Hagenholz-Vorstoss     |
|15201075 | Aathal-Schotter | Aathal-Schotter     |
|15201076 | Pfyn-Vorstoss | Pfyn-Vorstoss     |
|15201077 | Ittingen-Schotter | Ittingen-Schotter     |
|15201078 | Ryhirt-Formation | Ryhirt-Formation     |
|15201079 | Geisslingen-Schotter | Geisslingen-Schotter     |
|15201080 | Habsburg-Hagenholz-Interglazial | Habsburg-Hagenholz-Interglazial     |
|15201081 | Möhlinerfeld-Paläoboden | Möhlinerfeld-Paläoboden     |
|15201082 | Habsburg-Eiszeit | Habsburg-Eiszeit     |
|15201083 | Gränichen-Schotter | Gränichen-Schotter     |
|15201084 | Roggehuse-Schotter | Roggehuse-Schotter     |
|15201085 | Buerfeld-Schotter | Buerfeld-Schotter     |
|15201086 | Habsburg-Vergletscherung | Habsburg-Vergletscherung     |
|15201087 | Habsburg-Vorstoss | Habsburg-Vorstoss     |
|15201088 | Habsburg-Schotter | Habsburg-Schotter     |
|15201180 | Endingen-Schotter | Endingen-Schotter     |
|15201089 | Unterschlatt-Vorstoss | Unterschlatt-Vorstoss     |
|15201090 | Thalgut-Interglazial | Thalgut-Interglazial     |
|15201091 | Möhlin-Eiszeit (Grösste Eiszeit) | Möhlin-Eiszeit (Grösste Eiszeit)     |
|15201092 | Möhlin-Vergletscherung | Möhlin-Vergletscherung     |
|15201093 | Möhlin-Vorstoss | Möhlin-Vorstoss     |
|15201094 | Bünten-Till | Bünten-Till     |
|15201095 | Schleitheim-Vorstoss | Schleitheim-Vorstoss     |
|15201004 | Tiefere Deckenschotter | Tiefere Deckenschotter     |
|15206101 | Undifferenzierte lithologische Einheit: Kalkmarmor | Undifferenzierte lithologische Einheit: Kalkmarmor     |
|15206103 | Undifferenzierte stratigraphische Einheit: Permo-Karbon | Undifferenzierte stratigraphische Einheit: Permo-Karbon     |
|15206104 | Undifferenzierte lithologische Einheit: Kalkschiefer | Undifferenzierte lithologische Einheit: Kalkschiefer     |
|15206105 | Undifferenzierte lithologische Einheit: Sandstein | Undifferenzierte lithologische Einheit: Sandstein     |
|15206106 | Undifferenzierte lithologische Einheit: Tonschiefer | Undifferenzierte lithologische Einheit: Tonschiefer     |
|15206107 | Undifferenzierte lithologische Einheit: Radiolarit | Undifferenzierte lithologische Einheit: Radiolarit     |
|15206108 | Undifferenzierte lithologische Einheit: Kalkstein | Undifferenzierte lithologische Einheit: Kalkstein     |
|15206109 | Undifferenzierte lithologische Einheit: Konglomeratgneis | Undifferenzierte lithologische Einheit: Konglomeratgneis     |
|15206110 | Undifferenzierte stratigraphische Einheit: Prävariszisches polyzyklisches Grundgebirge | Undifferenzierte stratigraphische Einheit: Prävariszisches polyzyklisches Grundgebirge     |
|15206111 | Undifferenzierte lithologische Einheit: Schiefer | Undifferenzierte lithologische Einheit: Schiefer     |
|15206112 | Undifferenzierte lithologische Einheit: Aplitgneis | Undifferenzierte lithologische Einheit: Aplitgneis     |
|15206113 | Undifferenzierte lithologische Einheit: Süsswasserkalk | Undifferenzierte lithologische Einheit: Süsswasserkalk     |
|15206114 | Undifferenzierte stratigraphische Einheit: Tektonisches Melange | Undifferenzierte stratigraphische Einheit: Tektonisches Melange     |
|15201499 | Untergrabehüsli-Schotter | Untergrabehüsli-Schotter     |
|15205003 | Roisan-Cignana-Zone | Roisan-Cignana-Zone     |
|15205004 | Arolla-Einheit | Arolla-Einheit     |
|15205005 | Mont-Collon-Gabbro | Mont-Collon-Gabbro     |
|15205006 | Arolla-Orthogneis | Arolla-Orthogneis     |
|15205007 | Valpelline-Einheit | Valpelline-Einheit     |
|15205008 | Castel-di-Sotto-Ton | Castel-di-Sotto-Ton     |
|15205009 | Pontegana-Konglomerat | Pontegana-Konglomerat     |
|15205010 | Lombardischer Gompholith | Lombardischer Gompholith     |
|15205011 | Lucino-Konglomerat | Lucino-Konglomerat     |
|15205012 | Lucino-Konglomerat: Cagno-Sandstein | Lucino-Konglomerat: Cagno-Sandstein     |
|15205013 | Como-Konglomerat: Val-Grande-Sandstein | Como-Konglomerat: Val-Grande-Sandstein     |
|15205014 | Como-Konglomerat: Prestino-Pelite | Como-Konglomerat: Prestino-Pelite     |
|15205015 | Como-Konglomerat | Como-Konglomerat     |
|15205016 | Como-Konglomerat: Malnate-Sandstein | Como-Konglomerat: Malnate-Sandstein     |
|15205017 | Como-Konglomerat: Rio-dei-Gioghi-Pelite | Como-Konglomerat: Rio-dei-Gioghi-Pelite     |
|15205018 | Chiasso-Fm. | Chiasso-Fm.     |
|15205019 | Chiasso-Fm: Villa-Olmo-Konglomerat | Chiasso-Fm: Villa-Olmo-Konglomerat     |
|15205020 | Ternate-Fm. | Ternate-Fm.     |
|15205021 | Brenno-Fm. | Brenno-Fm.     |
|15205022 | Prella-Konglomerat | Prella-Konglomerat     |
|15205023 | Südalpin: Flysch | Südalpin: Flysch     |
|15205024 | Bergamo-Flysch | Bergamo-Flysch     |
|15201096 | Fisibach-Schotter | Fisibach-Schotter     |
|15201097 | Bärengraben-Schotter und -Till | Bärengraben-Schotter und -Till     |
|15201098 | Iberig-Schotterkomplex | Iberig-Schotterkomplex     |
|15201099 | Obere Iberigschotter | Obere Iberigschotter     |
|15201100 | Oberer Till | Oberer Till     |
|15201101 | Mittlere Iberigschotter | Mittlere Iberigschotter     |
|15201102 | Untere Iberigschotter | Untere Iberigschotter     |
|15201103 | Unterer Till | Unterer Till     |
|15201104 | Wolfacher-Schotter und -Till | Wolfacher-Schotter und -Till     |
|15201105 | Fornech-Schotter | Fornech-Schotter     |
|15201005 | Höhere Deckenschotter | Höhere Deckenschotter     |
|15201106 | Forenirchel-Schotter | Forenirchel-Schotter     |
|15201107 | Steig-Schotter | Steig-Schotter     |
|15201108 | Irchel-Schotterkomplex | Irchel-Schotterkomplex     |
|15201109 | Obere Irchelschotter | Obere Irchelschotter     |
|15201111 | Irchel-Dolomitschotter | Irchel-Dolomitschotter     |
|15201112 | Mittlere Irchelschotter | Mittlere Irchelschotter     |
|15201113 | Untere Irchelschotter | Untere Irchelschotter     |
|15201114 | Langacher-Schotter | Langacher-Schotter     |
|15201115 | Dürn-Formation | Dürn-Formation     |
|15201116 | Degermoos-Schotter | Degermoos-Schotter     |
|15201117 | Ebnet-Schotter | Ebnet-Schotter     |
|15201118 | Wannen-Schotter | Wannen-Schotter     |
|15201119 | Egghalden-Schotter | Egghalden-Schotter     |
|15201120 | Buechen-Formation | Buechen-Formation     |
|15201121 | Feusi-Schotter | Feusi-Schotter     |
|15201122 | Lindenhau-Schotter | Lindenhau-Schotter     |
|15201123 | Egg-Schotter | Egg-Schotter     |
|15201124 | Sundgau-Schotter | Sundgau-Schotter     |
|15201125 | Mischschotter | Mischschotter     |
|15201126 | Weisse Serie | Weisse Serie     |
|15206115 | Undifferenzierte stratigraphische Einheit: Flysch | Undifferenzierte stratigraphische Einheit: Flysch     |
|15206116 | Undifferenzierte lithologische Einheit: Aptychenkalk | Undifferenzierte lithologische Einheit: Aptychenkalk     |
|15206117 | Undifferenzierte lithologische Einheit: Quarzsandstein | Undifferenzierte lithologische Einheit: Quarzsandstein     |
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
|15205025 | Coldrerio-Flysch | Coldrerio-Flysch     |
|15205026 | Torre-Konglomerat | Torre-Konglomerat     |
|15205027 | Varesotto-Flysch | Varesotto-Flysch     |
|15205028 | Scaglia Lombarda | Scaglia Lombarda     |
|15205029 | Scaglia Rossa Lombarda | Scaglia Rossa Lombarda     |
|15205030 | Scaglia Bianca Lombarda | Scaglia Bianca Lombarda     |
|15205031 | Scaglia Variegata Lombarda | Scaglia Variegata Lombarda     |
|15205032 | Maiolica Lombarda | Maiolica Lombarda     |
|15205033 | Selcifero Lombardo | Selcifero Lombardo     |
|15205034 | Selcifero Lombardo: Rosso ad Aptici | Selcifero Lombardo: Rosso ad Aptici     |
|15205035 | Calcare a bivalvi planctonici | Calcare a bivalvi planctonici     |
|15205036 | Rosso Ammonitico Lombardo | Rosso Ammonitico Lombardo     |
|15205037 | Rosso Ammonitico Lombardo: Grenzposidonienschichten | Rosso Ammonitico Lombardo: Grenzposidonienschichten     |
|15205038 | Morbio-Fm. | Morbio-Fm.     |
|15205039 | Besazio-Kalk | Besazio-Kalk     |
|15205040 | Moltrasio-Fm. | Moltrasio-Fm.     |
|15205041 | Moltrasio-Fm.: Molino-Mb. | Moltrasio-Fm.: Molino-Mb.     |
|15205042 | Saltrio-Fm. | Saltrio-Fm.     |
|15205043 | Macchia Vecchia | Macchia Vecchia     |
|15205044 | Broccatello d&#39;Arzo | Broccatello d&#39;Arzo     |
|15205045 | Albenza-Fm. | Albenza-Fm.     |
|15205046 | Zu-Kalk | Zu-Kalk     |
|15203450 | Saas-Fee-Augengneis | Saas-Fee-Augengneis     |
|15203451 | Almagelhorn-Migmatit | Almagelhorn-Migmatit     |
|15203452 | Weissmies-Paragneis | Weissmies-Paragneis     |
|15203453 | Monte-Rosa-Orthogneis: Mittelkörnige Fazies | Monte-Rosa-Orthogneis: Mittelkörnige Fazies     |
|15203454 | Stellihorn-Mylonit | Stellihorn-Mylonit     |
|15203455 | Pizzo-del-Vallone-Decke: Kalkschiefer | Pizzo-del-Vallone-Decke: Kalkschiefer     |
|15203456 | Unterpenninikum: Dogger | Unterpenninikum: Dogger     |
|15203457 | Unterpenninikum: Lias | Unterpenninikum: Lias     |
|15203458 | Unterpenninikum: Trias: Dolomit | Unterpenninikum: Trias: Dolomit     |
|15203459 | Valgrande-Paragneis | Valgrande-Paragneis     |
|15203460 | Mittelpenninikum: Variszische Intrusiva | Mittelpenninikum: Variszische Intrusiva     |
|15203461 | Mittelpenninikum: Prävariszisches Grundgebirge | Mittelpenninikum: Prävariszisches Grundgebirge     |
|15203462 | Moncucco-Peridotit | Moncucco-Peridotit     |
|15203463 | Adlerflüe-Fm.: Albitaugenschiefer | Adlerflüe-Fm.: Albitaugenschiefer     |
|15203464 | Adlerflüe-Fm.: Bänderamphibolit | Adlerflüe-Fm.: Bänderamphibolit     |
|15203465 | Adlerflüe-Fm.: Minugrat-Eklogit | Adlerflüe-Fm.: Minugrat-Eklogit     |
|15203466 | Ergischhorn-Komplex: Amphibolit | Ergischhorn-Komplex: Amphibolit     |
|15203467 | Distulberg-Fm.: Grüngesteine | Distulberg-Fm.: Grüngesteine     |
|15201286 | Bergsturzablagerungen von Sierre | Bergsturzablagerungen von Sierre     |
|15201287 | Bergsturzablagerungen von Chiètres | Bergsturzablagerungen von Chiètres     |
|15201288 | Bergsturzablagerungen von Chessel-Noville | Bergsturzablagerungen von Chessel-Noville     |
|15201289 | Bergsturzablagerungen von Novalles-Vugelles | Bergsturzablagerungen von Novalles-Vugelles     |
|15201290 | Bergsturzablagerungen von Gwelber-Laui-Weid | Bergsturzablagerungen von Gwelber-Laui-Weid     |
|15201291 | Bergsturzablagerungen von Castasegna | Bergsturzablagerungen von Castasegna     |
|15201292 | Bergsturzablagerungen von Sogno | Bergsturzablagerungen von Sogno     |
|15201293 | Bergsturzablagerungen von Prapan | Bergsturzablagerungen von Prapan     |
|15201294 | Bergsturzablagerungen von Schaingels | Bergsturzablagerungen von Schaingels     |
|15201295 | Bergsturzablagerungen von Mutta | Bergsturzablagerungen von Mutta     |
|15201296 | Bergsturzablagerungen von Brienz | Bergsturzablagerungen von Brienz     |
|15201297 | Bergsturzablagerungen von Flims | Bergsturzablagerungen von Flims     |
|15201298 | Bergsturzablagerungen von Brüsis | Bergsturzablagerungen von Brüsis     |
|15201299 | Bergsturzablagerungen vom Chapf | Bergsturzablagerungen vom Chapf     |
|15201300 | Bergsturzablagerungen von Derborence | Bergsturzablagerungen von Derborence     |
|15201301 | Bergsturzablagerungen vom Drussetschawald | Bergsturzablagerungen vom Drussetschawald     |
|15201302 | Bergsturzablagerungen vom Delenwald | Bergsturzablagerungen vom Delenwald     |
|15201303 | Bergsturzablagerungen von Elm | Bergsturzablagerungen von Elm     |
|15201304 | Bergsturzablagerungen von Goldau | Bergsturzablagerungen von Goldau     |
|15201305 | Bergsturzablagerungen von Iragell | Bergsturzablagerungen von Iragell     |
|15201306 | Bergsturzablagerungen vom Kernwald | Bergsturzablagerungen vom Kernwald     |
|15201307 | Bergsturzablagerungen von Triesenberg | Bergsturzablagerungen von Triesenberg     |
|15201308 | Bonaduz-Formation | Bonaduz-Formation     |
|15201309 | Bonfol-Ton | Bonfol-Ton     |
|15201310 | Bergsturzablagerungen von Tamins | Bergsturzablagerungen von Tamins     |
|15201311 | Informell benannte Bergsturzablagerungen | Informell benannte Bergsturzablagerungen     |
|15203580 | Bärenhorn-Fm.: Quarzsandstein | Bärenhorn-Fm.: Quarzsandstein     |
|15203581 | Grava-Decke: Kalkschiefer | Grava-Decke: Kalkschiefer     |
|15203582 | Grava-Decke: Tonschiefer | Grava-Decke: Tonschiefer     |
|15203583 | Grava-Decke: Trias | Grava-Decke: Trias     |
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
|15205047 | Tremona-Fm. | Tremona-Fm.     |
|15205048 | Brecce Retiche | Brecce Retiche     |
|15205049 | Riva-di-Solto-Tonstein | Riva-di-Solto-Tonstein     |
|15205050 | Dolomia Principale | Dolomia Principale     |
|15205051 | Pizzella-Mergel | Pizzella-Mergel     |
|15205052 | Cunardo-Fm. | Cunardo-Fm.     |
|15205053 | Meride-Fm. | Meride-Fm.     |
|15205054 | Meride-Fm.: Kalkschieferzone | Meride-Fm.: Kalkschieferzone     |
|15205055 | Meride-Fm.: Unterer Kalk: Cassina-Bk. | Meride-Fm.: Unterer Kalk: Cassina-Bk.     |
|15205056 | Meride-Fm.: Unterer Kalk: Cava Superiore | Meride-Fm.: Unterer Kalk: Cava Superiore     |
|15205057 | Meride-Fm.: Unterer Kalk: Cava Inferiore | Meride-Fm.: Unterer Kalk: Cava Inferiore     |
|15205058 | San-Giorgio-Dolomit | San-Giorgio-Dolomit     |
|15205059 | San-Giorgio-Dolomit: Val-Serrata-Tuffite | San-Giorgio-Dolomit: Val-Serrata-Tuffite     |
|15205060 | Besano-Fm. | Besano-Fm.     |
|15205061 | San-Salvatore-Dolomit | San-Salvatore-Dolomit     |
|15205062 | Bellano-Fm. | Bellano-Fm.     |
|15205063 | Servino | Servino     |
|15205064 | Verrucano Lombardo | Verrucano Lombardo     |
|15205065 | Morcote-Vulkanite | Morcote-Vulkanite     |
|15205066 | Morcote-Vulkanite: Granophyr | Morcote-Vulkanite: Granophyr     |
|15205067 | Morcote-Vulkanite: Andesit und Dazit | Morcote-Vulkanite: Andesit und Dazit     |
|15203468 | Métailler-Fm.: Prasinit | Métailler-Fm.: Prasinit     |
|15203469 | Métailler-Fm.: Ultramafisches Gestein | Métailler-Fm.: Ultramafisches Gestein     |
|15203470 | Randa-Augengneis: Oberems-Albitgneis | Randa-Augengneis: Oberems-Albitgneis     |
|15203471 | Maggia-Decke: Permo-Karbon | Maggia-Decke: Permo-Karbon     |
|15203472 | Maggia-Decke: Quarz-Glimmerschiefer | Maggia-Decke: Quarz-Glimmerschiefer     |
|15203473 | Maggia-Decke: Muskovit-Graphitschiefer | Maggia-Decke: Muskovit-Graphitschiefer     |
|15203474 | Maggia-Decke: Variszische Intrusive | Maggia-Decke: Variszische Intrusive     |
|15203475 | Maggia-Decke: Prävariszisches Grundgebirge | Maggia-Decke: Prävariszisches Grundgebirge     |
|15203476 | Maggia-Decke: Paragneis | Maggia-Decke: Paragneis     |
|15203477 | Maggia-Decke: Bändergneis | Maggia-Decke: Bändergneis     |
|15203478 | Maggia-Decke: Augengneis | Maggia-Decke: Augengneis     |
|15203479 | Alpigia-Gneis | Alpigia-Gneis     |
|15203480 | Gresso-Someo-Zone | Gresso-Someo-Zone     |
|15203481 | Pertusio-Zone | Pertusio-Zone     |
|15203482 | Passo-di-Cristallina-Zone | Passo-di-Cristallina-Zone     |
|15203483 | Lago-Scuro-Fm. | Lago-Scuro-Fm.     |
|15203484 | Val-Sabbia-Fm. | Val-Sabbia-Fm.     |
|15203485 | Massari-Fm. | Massari-Fm.     |
|15203486 | Naret-Fm. | Naret-Fm.     |
|15201188 | Münsingen-Schotterkomplex | Münsingen-Schotterkomplex     |
|15201189 | Alterswil-Schotter | Alterswil-Schotter     |
|15201190 | Karlsruhe-Schotter | Karlsruhe-Schotter     |
|15201191 | Chisetal-Schotter | Chisetal-Schotter     |
|15201192 | Grauholz-Schotter | Grauholz-Schotter     |
|15201193 | Trachslau-Schotter | Trachslau-Schotter     |
|15201194 | Bennau-Schotter | Bennau-Schotter     |
|15201195 | Hütten-Schotter | Hütten-Schotter     |
|15201196 | Schnabelsberg-Stauchotter | Schnabelsberg-Stauchotter     |
|15201197 | Einsiedeln-Lehm | Einsiedeln-Lehm     |
|15201312 | Informell benannte künstliche Ablagerungen | Informell benannte künstliche Ablagerungen     |
|15201313 | Künstliche Ablagerungen des Bahnhofs Brig | Künstliche Ablagerungen des Bahnhofs Brig     |
|15201314 | Künstliche Ablagerungen Golar | Künstliche Ablagerungen Golar     |
|15201315 | Künstliche Ablagerungen der Gamsenried-Deponie | Künstliche Ablagerungen der Gamsenried-Deponie     |
|15201316 | Künstliche Ablagerungen des Riedertals | Künstliche Ablagerungen des Riedertals     |
|15201317 | Informell benannte Sackungsmassen | Informell benannte Sackungsmassen     |
|15201318 | Sackungsmasse des Heinzenbergs | Sackungsmasse des Heinzenbergs     |
|15201319 | Informell benannte fluviatile Schotter | Informell benannte fluviatile Schotter     |
|15201320 | Schotter und Sand der Rhône | Schotter und Sand der Rhône     |
|15201321 | Schotter und Sand der Vispa | Schotter und Sand der Vispa     |
|15201322 | Informell benannter Bachschutt | Informell benannter Bachschutt     |
|15201323 | Bachschutt des Baltschiederbachs | Bachschutt des Baltschiederbachs     |
|15201324 | Bachschutt des Bietschbachs | Bachschutt des Bietschbachs     |
|15201325 | Bachschutt des Chelchbachs | Bachschutt des Chelchbachs     |
|15201326 | Bachschutt der Gamsa | Bachschutt der Gamsa     |
|15201327 | Bachschutt des Jolibachs | Bachschutt des Jolibachs     |
|15201328 | Bachschutt der Lonza | Bachschutt der Lonza     |
|15201329 | Bachschutt der Saltina | Bachschutt der Saltina     |
|15201330 | Bachschutt der Vispa | Bachschutt der Vispa     |
|15201331 | Bachschutt der Gürbe | Bachschutt der Gürbe     |
|15201332 | Bachschutt des Lombachs | Bachschutt des Lombachs     |
|15201333 | Pliozäne Ablagerungen | Pliozäne Ablagerungen     |
|15201334 | Stockesee-Sediment | Stockesee-Sediment     |
|15201335 | Strätligen-Till | Strätligen-Till     |
|15201336 | Bärenholz-Till | Bärenholz-Till     |
|15201337 | Wässerifluh-Formation | Wässerifluh-Formation     |
|15201338 | Schlyffi-Till | Schlyffi-Till     |
|15201339 | Brüggstutz-Schotter | Brüggstutz-Schotter     |
|15201340 | Guntelsei-Till | Guntelsei-Till     |
|15201341 | Guntelsei-Schotter | Guntelsei-Schotter     |
|15201342 | Steghalden-Schotter | Steghalden-Schotter     |
|15201343 | Glütschtal-Formation | Glütschtal-Formation     |
|15201344 | Hahni-Schotter | Hahni-Schotter     |
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
|15205068 | Morcote-Vulkanite: Basalt | Morcote-Vulkanite: Basalt     |
|15205069 | Morcote-Vulkanite: Basaler Tuf | Morcote-Vulkanite: Basaler Tuf     |
|15205070 | Manno-Fm. | Manno-Fm.     |
|15205071 | Südalpin: Paläogen-Neogen | Südalpin: Paläogen-Neogen     |
|15205072 | Südalpin: Kreide | Südalpin: Kreide     |
|15205073 | Südalpin: Radiolarit-Aptychenkalk | Südalpin: Radiolarit-Aptychenkalk     |
|15205074 | Südalpin: Dogger | Südalpin: Dogger     |
|15205075 | Südalpin: Lias | Südalpin: Lias     |
|15205076 | Südalpin: Trias | Südalpin: Trias     |
|15205077 | Südalpin: Permo-Karbon | Südalpin: Permo-Karbon     |
|15205078 | Südalpin: Grundgebirge | Südalpin: Grundgebirge     |
|15205079 | Südalpin: Variszische Intrusiva | Südalpin: Variszische Intrusiva     |
|15205080 | San-Bernardo-Gneis | San-Bernardo-Gneis     |
|15205081 | Südalpin: Prävariszische Metasedimente | Südalpin: Prävariszische Metasedimente     |
|15205082 | Stabbiello-Gneis | Stabbiello-Gneis     |
|15205083 | Giumello-Gneis | Giumello-Gneis     |
|15205084 | Ceneri-Gneis | Ceneri-Gneis     |
|15205085 | Südalpin: Proterozoische und paläozoische mafische und ultramafische Gesteine | Südalpin: Proterozoische und paläozoische mafische und ultramafische Gesteine     |
|15205086 | Mont-Morion-Granit | Mont-Morion-Granit     |
|15203487 | Breithorn-Serpentinit | Breithorn-Serpentinit     |
|15203488 | Loranco-Amphibolit | Loranco-Amphibolit     |
|15203489 | Andolla-Eklogit | Andolla-Eklogit     |
|15203490 | Roz-Schiefer | Roz-Schiefer     |
|15203491 | Ramosch-Zone: Ophiolith | Ramosch-Zone: Ophiolith     |
|15203492 | Arosa-Decke: Metasedimente | Arosa-Decke: Metasedimente     |
|15203493 | Totalp-Serpentinit | Totalp-Serpentinit     |
|15203494 | Maran-Brekzie | Maran-Brekzie     |
|15203495 | Tumpriv-Fm.: Solis-Kalk | Tumpriv-Fm.: Solis-Kalk     |
|15203496 | Platta-Decke: Metasedimente | Platta-Decke: Metasedimente     |
|15203497 | Flix-Sch. | Flix-Sch.     |
|15203498 | Platta-Decke: Calpionellenkalk | Platta-Decke: Calpionellenkalk     |
|15203499 | Falotta-Radiolarit | Falotta-Radiolarit     |
|15203500 | Platta-Decke: Ophiolith | Platta-Decke: Ophiolith     |
|15203501 | Vignun-Gneis | Vignun-Gneis     |
|15203502 | Avers-Decke: Metasedimente | Avers-Decke: Metasedimente     |
|15203503 | Avers-Decke: Ophiolith | Avers-Decke: Ophiolith     |
|15203504 | Tasna-Decke: Couches Rouges | Tasna-Decke: Couches Rouges     |
|15203505 | Tasna-Decke: Tristel-Fm.: Minschun-Brekzie | Tasna-Decke: Tristel-Fm.: Minschun-Brekzie     |
|15201198 | Willisau-Schotter | Willisau-Schotter     |
|15201199 | Wolhusen-Schotter | Wolhusen-Schotter     |
|15201200 | Wiggen-Schotter | Wiggen-Schotter     |
|15201201 | Menzingen-Schotter | Menzingen-Schotter     |
|15201202 | La-Tuffière-Schotter | La-Tuffière-Schotter     |
|15201203 | Gontenschwil-Lehm | Gontenschwil-Lehm     |
|15201204 | Mooslerau-Lehm | Mooslerau-Lehm     |
|15201205 | Triengen-Schotter | Triengen-Schotter     |
|15201206 | Triengen-Lehm | Triengen-Lehm     |
|15201207 | Sihl-Schotter | Sihl-Schotter     |
|15201208 | Haselbach-Schotter | Haselbach-Schotter     |
|15201209 | Jonen-Schotter | Jonen-Schotter     |
|15201210 | Aabach-Schotter | Aabach-Schotter     |
|15201211 | Starrberg-Schotter | Starrberg-Schotter     |
|15201212 | Port-Stauschotter | Port-Stauschotter     |
|15201213 | Rempen-Stauschotter | Rempen-Stauschotter     |
|15201214 | Dagmersellen-Vorstoss | Dagmersellen-Vorstoss     |
|15201215 | Oftringen-Schotter | Oftringen-Schotter     |
|15201216 | Zelg-Schotter | Zelg-Schotter     |
|15201217 | Forst-Schotter | Forst-Schotter     |
|15201218 | Raintal-Deltaschotter | Raintal-Deltaschotter     |
|15201219 | Kleinhöchstetten-Kies-Sand-Komplex | Kleinhöchstetten-Kies-Sand-Komplex     |
|15201220 | Krauchthal-Schotter | Krauchthal-Schotter     |
|15201221 | Brandflue-Schotter | Brandflue-Schotter     |
|15201222 | Küsnacht-Schotter | Küsnacht-Schotter     |
|15201223 | Chatzenstrick-Schotter | Chatzenstrick-Schotter     |
|15201224 | Rabennest-Schotter | Rabennest-Schotter     |
|15201225 | Ratengütsch-Schotter | Ratengütsch-Schotter     |
|15201226 | Scherenspitz-Schotter | Scherenspitz-Schotter     |
|15201227 | Walsenhaus-Schotter | Walsenhaus-Schotter     |
|15201228 | Richterswil-Seeton | Richterswil-Seeton     |
|15201229 | Schwanden-Schotter | Schwanden-Schotter     |
|15201230 | Reidbach-Schotter | Reidbach-Schotter     |
|15201231 | Zell-Schotterkomplex | Zell-Schotterkomplex     |
|15201232 | Gubel-Schotter | Gubel-Schotter     |
|15201233 | Chälen-Schotter | Chälen-Schotter     |
|15201234 | Chälen-Till | Chälen-Till     |
|15201235 | Sihlsprung-Schotter | Sihlsprung-Schotter     |
|15201236 | Kollbrunn-Schotter | Kollbrunn-Schotter     |
|15201237 | Walenberg-Schotter | Walenberg-Schotter     |
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
|15201526 | Wagenmoos-Till | Wagenmoos-Till     |
|15201527 | Niderstalden-Schotter | Niderstalden-Schotter     |
|15201528 | Zulgtal-Schotter | Zulgtal-Schotter     |
|15201529 | Spiez-Schotter | Spiez-Schotter     |
|15201530 | Hahni-Till | Hahni-Till     |
|15201531 | Bergsturzablagerung von Ralligen (im Thunersee) | Bergsturzablagerung von Ralligen (im Thunersee)     |
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
|15205099 | Meride-Fm.: Oberer Kalk | Meride-Fm.: Oberer Kalk     |
|15205100 | Meride-Fm.: Unterer Kalk | Meride-Fm.: Unterer Kalk     |
|15205101 | Meride-Fm.: Dolomit-Band | Meride-Fm.: Dolomit-Band     |
|15205102 | Dent-Blanche-Decke: Lias: Kalkstein | Dent-Blanche-Decke: Lias: Kalkstein     |
|15205103 | Dent-Blanche-Decke: Trias: Dolomit | Dent-Blanche-Decke: Trias: Dolomit     |
|15205104 | Dent-Blanche-Decke: Trias: Rauwacke | Dent-Blanche-Decke: Trias: Rauwacke     |
|15205105 | Dent-Blanche-Decke: Trias: Quarzit | Dent-Blanche-Decke: Trias: Quarzit     |
|15205106 | Arolla-Orthogneis: Leukokrater Gneis | Arolla-Orthogneis: Leukokrater Gneis     |
|15205107 | Arolla-Orthogneis: Augengneis | Arolla-Orthogneis: Augengneis     |
|15203506 | Tasna-Decke: Prävariszisches Grundgebrige | Tasna-Decke: Prävariszisches Grundgebrige     |
|15203507 | Piz-del-Palo-Gneis | Piz-del-Palo-Gneis     |
|15203508 | Truzzo-Granit | Truzzo-Granit     |
|15203509 | Rebi-Gneis | Rebi-Gneis     |
|15203510 | Brione-Gabbro | Brione-Gabbro     |
|15203511 | Gruf-Migmatit | Gruf-Migmatit     |
|15203512 | Adula-Decke: Basaler Gneis | Adula-Decke: Basaler Gneis     |
|15203513 | Val-Chironico-Gneis | Val-Chironico-Gneis     |
|15203514 | Ganna-Gneis | Ganna-Gneis     |
|15203515 | Adula-Decke: Albit-Oligoklasgneis | Adula-Decke: Albit-Oligoklasgneis     |
|15203516 | Sivigia-Gneis | Sivigia-Gneis     |
|15203517 | Aula-Spruga-Gneiskomplex | Aula-Spruga-Gneiskomplex     |
|15203518 | Lizun-Grünschiefer | Lizun-Grünschiefer     |
|15203519 | Rossi-Fm. | Rossi-Fm.     |
|15203520 | Bosco-Gneis | Bosco-Gneis     |
|15203521 | Batnall-Gneis | Batnall-Gneis     |
|15203522 | Seron-Fm.: Sandig-kalkige Fazies | Seron-Fm.: Sandig-kalkige Fazies     |
|15203523 | Seron-Fm.: Konglomerat-dominierte Fazies | Seron-Fm.: Konglomerat-dominierte Fazies     |
|15203524 | Frutigen-Fm.: Konglomerat-dominierte Fazies | Frutigen-Fm.: Konglomerat-dominierte Fazies     |
|15201238 | Ritteren-Schotterkomplex | Ritteren-Schotterkomplex     |
|15201239 | Vorholz-Schotter | Vorholz-Schotter     |
|15201240 | Gutsch-Schotter | Gutsch-Schotter     |
|15201241 | Junkerenwald-Schotter | Junkerenwald-Schotter     |
|15201242 | Chräjeloch-Schotter | Chräjeloch-Schotter     |
|15201243 | Butteberg-Schotter | Butteberg-Schotter     |
|15201244 | Höchi-Schotter | Höchi-Schotter     |
|15201245 | Heitere-Schotter | Heitere-Schotter     |
|15201246 | Holziken-Schotter | Holziken-Schotter     |
|15201247 | Ruedertal-Schotter | Ruedertal-Schotter     |
|15201248 | Bänkel-Schotter | Bänkel-Schotter     |
|15201249 | Quartär, undifferenziert | Quartär, undifferenziert     |
|15201250 | Deckenschotter, undifferenziert | Deckenschotter, undifferenziert     |
|15201251 | Girenbad-Schotter | Girenbad-Schotter     |
|15201252 | Sagenbach-Schotter | Sagenbach-Schotter     |
|15201253 | Schrotzburg-Schotter | Schrotzburg-Schotter     |
|15201254 | Schrotzburg-Till | Schrotzburg-Till     |
|15201255 | Bohlingen-Schotter | Bohlingen-Schotter     |
|15201256 | Bannholz-Schotter | Bannholz-Schotter     |
|15201257 | Hungerbol-Schotter | Hungerbol-Schotter     |
|15201258 | Chilchstapfen-Schotter | Chilchstapfen-Schotter     |
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
|15205108 | Arolla-Orthogneis: Mylonit | Arolla-Orthogneis: Mylonit     |
|15205109 | Arolla-Einheit: Série rubanée: Mylonit | Arolla-Einheit: Série rubanée: Mylonit     |
|15205110 | Arolla-Einheit: Série rubanée: Mikroaugengneis | Arolla-Einheit: Série rubanée: Mikroaugengneis     |
|15205111 | Arolla-Orthogneis: Granitoid | Arolla-Orthogneis: Granitoid     |
|15205112 | Arolla-Einheit: Basisches Gestein | Arolla-Einheit: Basisches Gestein     |
|15205113 | Arolla-Einheit: Basisches Gestein: Mylonitisch | Arolla-Einheit: Basisches Gestein: Mylonitisch     |
|15205114 | Arolla-Einheit: Prasinit | Arolla-Einheit: Prasinit     |
|15205115 | Arolla-Einheit: Hornblendegabbro | Arolla-Einheit: Hornblendegabbro     |
|15205116 | Arolla-Einheit: Ultramafisches Gestein | Arolla-Einheit: Ultramafisches Gestein     |
|15205117 | Arolla-Einheit: Paragneis | Arolla-Einheit: Paragneis     |
|15205118 | Arolla-Einheit: Glimmerschiefer | Arolla-Einheit: Glimmerschiefer     |
|15205119 | Valpelline-Einheit: Mylonit | Valpelline-Einheit: Mylonit     |
|15205120 | Valpelline-Einheit: Amphibolit | Valpelline-Einheit: Amphibolit     |
|15205121 | Valpelline-Einheit: Marmor | Valpelline-Einheit: Marmor     |
|15205122 | Valpelline-Einheit: Migmatit | Valpelline-Einheit: Migmatit     |
|15205123 | Roisan-Cignana-Zone: Marmor | Roisan-Cignana-Zone: Marmor     |
|15205124 | Musella-Granit | Musella-Granit     |
|15205125 | Sella-Granodiorit | Sella-Granodiorit     |
|15205126 | Marinelli-Fm. | Marinelli-Fm.     |
|15205127 | Margna- und Sella-Decke: Grundgebirge | Margna- und Sella-Decke: Grundgebirge     |
|15203525 | Frutigen-Fm.: Schiefrige Fazies | Frutigen-Fm.: Schiefrige Fazies     |
|15203526 | Zone Submédiane: Gips | Zone Submédiane: Gips     |
|15203527 | Zentralschweizerische Klippen: Keuper | Zentralschweizerische Klippen: Keuper     |
|15203528 | Zwischenmythen-Mergel | Zwischenmythen-Mergel     |
|15203529 | Arosa-Decke: Cenomanbrekzien-Serie | Arosa-Decke: Cenomanbrekzien-Serie     |
|15203530 | Arosa-Decke: Bettlerjoch-Brekzie | Arosa-Decke: Bettlerjoch-Brekzie     |
|15203531 | Arosa-Decke: Bargella-Brekzie | Arosa-Decke: Bargella-Brekzie     |
|15203532 | Adula-Decke: Kalkschiefer und Marmor | Adula-Decke: Kalkschiefer und Marmor     |
|15203533 | Salahorn-Fm.: Metaplutonit | Salahorn-Fm.: Metaplutonit     |
|15203534 | Salahorn-Fm.: Paragneis | Salahorn-Fm.: Paragneis     |
|15203535 | Adula-Decke: Ultramafisches Gestein | Adula-Decke: Ultramafisches Gestein     |
|15203536 | Cima-Lunga-Decke: Kalkschiefer und Marmor | Cima-Lunga-Decke: Kalkschiefer und Marmor     |
|15203537 | Cima-Lunga-Decke: Dolomitmarmor | Cima-Lunga-Decke: Dolomitmarmor     |
|15203538 | Cima-Lunga-Decke: Paragneis | Cima-Lunga-Decke: Paragneis     |
|15203539 | Vacarisc-Gneis | Vacarisc-Gneis     |
|15203540 | Rognoi-Gneis | Rognoi-Gneis     |
|15203541 | Cima-Lunga-Decke: Granatit | Cima-Lunga-Decke: Granatit     |
|15203542 | Cima-Lunga-Decke: Amphibolit | Cima-Lunga-Decke: Amphibolit     |
|15203543 | Cima-Lunga-Decke: Eklogit | Cima-Lunga-Decke: Eklogit     |
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
|15204001 | God-Drosa-Flysch | God-Drosa-Flysch     |
|15205128 | Margna- und Sella-Decke: Variszische Intrusiva | Margna- und Sella-Decke: Variszische Intrusiva     |
|15205129 | Margna- und Sella-Decke: Prävariszisches Grundgebirge | Margna- und Sella-Decke: Prävariszisches Grundgebirge     |
|15205130 | Margna-Decke: Metaarkose, Orthogneise | Margna-Decke: Metaarkose, Orthogneise     |
|15205131 | Sesia-Decke: Orthogneis | Sesia-Decke: Orthogneis     |
|15205132 | Sesia-Decke: Micascisti Eclogitici | Sesia-Decke: Micascisti Eclogitici     |
|15205133 | Finero-Peridotit | Finero-Peridotit     |
|15205134 | Ivrea Mafischer Komplex | Ivrea Mafischer Komplex     |
|15205135 | Sesia-Decke: Zona Dioritico-Kinzigitica | Sesia-Decke: Zona Dioritico-Kinzigitica     |
|15205136 | Südalpin: Prävariszischer Orthogneis | Südalpin: Prävariszischer Orthogneis     |
|15205137 | Pontida-Fm. | Pontida-Fm.     |
|15205138 | Arolla-Einheit: Metagranit | Arolla-Einheit: Metagranit     |
|15205139 | Arolla-Einheit: Leukokrater Granitgneis | Arolla-Einheit: Leukokrater Granitgneis     |
|15206001 | Periadriatische Vulkanite | Periadriatische Vulkanite     |
|15206002 | Novate-Intrusiva | Novate-Intrusiva     |
|15206003 | Bergell-Intrusiva | Bergell-Intrusiva     |
|15206004 | Adamello-Intrusiva | Adamello-Intrusiva     |
|15206005 | Melirolo-Augengneis | Melirolo-Augengneis     |
|15206006 | Bergell-Intrusiva: Granodioritische Fazies | Bergell-Intrusiva: Granodioritische Fazies     |
|15206007 | Bergell-Intrusiva: Tonalitische Fazies | Bergell-Intrusiva: Tonalitische Fazies     |
|15203544 | Cima-Lunga-Decke: Ultramafisches Gestein | Cima-Lunga-Decke: Ultramafisches Gestein     |
|15203545 | Personico-Gneis | Personico-Gneis     |
|15203546 | Leventina-Gneis: Oberer Teil | Leventina-Gneis: Oberer Teil     |
|15203547 | Leventina-Gneis: Unterer Teil | Leventina-Gneis: Unterer Teil     |
|15203548 | Leventina-Decke: Kalksilikatfels | Leventina-Decke: Kalksilikatfels     |
|15203549 | Leventina-Decke: Leukogneis | Leventina-Decke: Leukogneis     |
|15203550 | Leventina-Decke: Paragneis | Leventina-Decke: Paragneis     |
|15203551 | Leventina-Decke: Amphibolit | Leventina-Decke: Amphibolit     |
|15203552 | Maggia-Decke: Amphibolit | Maggia-Decke: Amphibolit     |
|15203553 | Simano-Decke: Kalkmarmor | Simano-Decke: Kalkmarmor     |
|15203554 | Simano-Decke: Dolomitmarmor | Simano-Decke: Dolomitmarmor     |
|15203555 | Simano-Decke: Paragneis | Simano-Decke: Paragneis     |
|15203556 | Renten-Gneis | Renten-Gneis     |
|15203557 | Legiuna-Gneis | Legiuna-Gneis     |
|15203558 | Simano-Decke: Amphibolit | Simano-Decke: Amphibolit     |
|15203559 | Simano-Decke: Ultramafisches Gestein | Simano-Decke: Ultramafisches Gestein     |
|15203560 | Alpbach-Schiefer | Alpbach-Schiefer     |
|15203561 | Arosa-Decke: Gabbro | Arosa-Decke: Gabbro     |
|15203562 | Zentralschweizerische Klippen: Flysch | Zentralschweizerische Klippen: Flysch     |
|15204002 | Chanèls-Fm. | Chanèls-Fm.     |
|15204003 | Lech-Fm. | Lech-Fm.     |
|15204004 | Emmat-Fm. | Emmat-Fm.     |
|15204005 | Russenna-Fm. | Russenna-Fm.     |
|15204006 | Ammergau-Fm. | Ammergau-Fm.     |
|15204007 | Blais-Fm. | Blais-Fm.     |
|15204008 | Blais-Fm.: Plattas-Mb. | Blais-Fm.: Plattas-Mb.     |
|15204009 | Ruhpolding-Fm. | Ruhpolding-Fm.     |
|15204010 | Ostalpin: Dogger | Ostalpin: Dogger     |
|15204011 | Saluver-Fm. | Saluver-Fm.     |
|15204012 | Bardella-Fm. | Bardella-Fm.     |
|15204013 | Salteras-Fm. | Salteras-Fm.     |
|15204014 | Salamun-Brekzie | Salamun-Brekzie     |
|15204015 | Err-Brekzie | Err-Brekzie     |
|15204016 | Allgäu-Fm. | Allgäu-Fm.     |
|15204017 | Allgäu-Fm.: Mezzaun-Mb. | Allgäu-Fm.: Mezzaun-Mb.     |
|15204018 | Allgäu-Fm.: Blaisun-Mb. | Allgäu-Fm.: Blaisun-Mb.     |
|15204019 | Allgäu-Fm.: Trupchun-Mb. | Allgäu-Fm.: Trupchun-Mb.     |
|15204020 | Agnelli-Fm. | Agnelli-Fm.     |
|15204021 | Agnelli-Fm.: Knollenkalk-Fazies | Agnelli-Fm.: Knollenkalk-Fazies     |
|15204022 | Agnelli-Fm.: Echinodermenkalk-Fazies | Agnelli-Fm.: Echinodermenkalk-Fazies     |
|15204023 | Alv-Brekzie | Alv-Brekzie     |
|15204024 | Kössen-Fm. | Kössen-Fm.     |
|15204025 | Kössen-Fm.: Zirmenkopf-Mb. | Kössen-Fm.: Zirmenkopf-Mb.     |
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
|15206025 | Undifferenzierte stratigraphische Einheit: Lias | Undifferenzierte stratigraphische Einheit: Lias     |
|15203055 | Chauderon-Fm. | Chauderon-Fm.     |
|15203056 | Vudalla-Fm. | Vudalla-Fm.     |
|15203057 | Vudalla-Fm.: Bois-de-Luan-Mb. | Vudalla-Fm.: Bois-de-Luan-Mb.     |
|15203058 | Vudalla-Fm.: Agreblierai-Mb. | Vudalla-Fm.: Agreblierai-Mb.     |
|15203059 | Col-de-Tompey-Fm. | Col-de-Tompey-Fm.     |
|15203060 | Plan-Falcon-Fm. | Plan-Falcon-Fm.     |
|15203061 | Dolomies Blondes | Dolomies Blondes     |
|15203062 | Clôt-la-Cime-Fm. | Clôt-la-Cime-Fm.     |
|15203066 | Griggeli-Fm. | Griggeli-Fm.     |
|15203067 | Griggeli-Fm.: Mythen-Kieselkalk | Griggeli-Fm.: Mythen-Kieselkalk     |
|15203068 | Griggeli-Fm.: Griggeli-Bk. | Griggeli-Fm.: Griggeli-Bk.     |
|15203069 | Gibel-Fm. | Gibel-Fm.     |
|15203070 | Gibel-Fm.: Rämsi-Mb. | Gibel-Fm.: Rämsi-Mb.     |
|15203071 | Gibel-Fm.: Gibel-Mb. | Gibel-Fm.: Gibel-Mb.     |
|15203072 | Gibel-Fm.: Steinberg-Konglomerat | Gibel-Fm.: Steinberg-Konglomerat     |
|15203073 | Gibel-Fm.: Musenalp-Mb. | Gibel-Fm.: Musenalp-Mb.     |
|15203074 | Stanserhorn-Fm. | Stanserhorn-Fm.     |
|15203075 | Stanserhorn-Fm.: Zoophycos-Sch. | Stanserhorn-Fm.: Zoophycos-Sch.     |
|15203076 | Stanserhorn-Fm.: Spis-Kalk | Stanserhorn-Fm.: Spis-Kalk     |
|15203077 | Stanserhorn-Fm.: Posidonienschiefer | Stanserhorn-Fm.: Posidonienschiefer     |
|15200503 | Öhningen-Fm. | Öhningen-Fm.     |
|15200504 | Öhningen-Fm.: Öhningen-Süsswasserkalk | Öhningen-Fm.: Öhningen-Süsswasserkalk     |
|15200505 | Öhningen-Fm.: Ramschwag-Nagelfluh | Öhningen-Fm.: Ramschwag-Nagelfluh     |
|15200506 | Hörnli-Fm.: Seerücken-Tuffit | Hörnli-Fm.: Seerücken-Tuffit     |
|15200507 | Meilen-Fm. | Meilen-Fm.     |
|15200508 | Meilen-Fm.: Wulp-Rotzone | Meilen-Fm.: Wulp-Rotzone     |
|15200509 | Käpfnach-Fm. | Käpfnach-Fm.     |
|15200510 | OSM-J: Juranagelfluh: Mergel-dominierte Fazies | OSM-J: Juranagelfluh: Mergel-dominierte Fazies     |
|15200511 | Golat-Süsswasserkalk | Golat-Süsswasserkalk     |
|15200512 | Belpberg-Fm.: Fossilreicher Horizont | Belpberg-Fm.: Fossilreicher Horizont     |
|15200513 | Fm. der Granitischen Molasse: Hombach-Mb. | Fm. der Granitischen Molasse: Hombach-Mb.     |
|15200514 | Homberg-Fm. | Homberg-Fm.     |
|15200515 | Gäbris-Nagelfluh | Gäbris-Nagelfluh     |
|15200516 | Gäbris-Nagelfluh: Gstaldenbach-Mb. | Gäbris-Nagelfluh: Gstaldenbach-Mb.     |
|15200517 | Gäbris-Nagelfluh: Heiden-Mb. | Gäbris-Nagelfluh: Heiden-Mb.     |
|15200518 | Gäbris-Nagelfluh: Klusbach-Mb. | Gäbris-Nagelfluh: Klusbach-Mb.     |
|15200519 | Gäbris-Nagelfluh: Eggen-Mb. | Gäbris-Nagelfluh: Eggen-Mb.     |
|15200520 | Gäbris-Sulzbach: Sulzbach-Mb. | Gäbris-Sulzbach: Sulzbach-Mb.     |
|15200521 | Gäbris-Sulzbach: Sulzbach-Mb.: Kalknagelfluh | Gäbris-Sulzbach: Sulzbach-Mb.: Kalknagelfluh     |
|15200522 | Kronberg-Nagelfluh: Pfingstboden-Mb. | Kronberg-Nagelfluh: Pfingstboden-Mb.     |
|15202140 | Vieux-Emosson-Fm. | Vieux-Emosson-Fm.     |
|15202141 | Mels-Fm. | Mels-Fm.     |
|15202142 | Helvetikum: Spät- bis postvariszische Sedimente und Vulkanite | Helvetikum: Spät- bis postvariszische Sedimente und Vulkanite     |
|15202143 | Helvetikum: Verrucano | Helvetikum: Verrucano     |
|15202144 | Glarner Verrucano | Glarner Verrucano     |
|15202145 | Schönbühl-Fm. | Schönbühl-Fm.     |
|15202146 | Schönbühl-Fm.: Quarzit | Schönbühl-Fm.: Quarzit     |
|15202147 | Kärpf-Fm. | Kärpf-Fm.     |
|15202148 | Karrenstock-Fm. | Karrenstock-Fm.     |
|15202149 | Murgtal-Fm.: Chartegg-Mb. | Murgtal-Fm.: Chartegg-Mb.     |
|15202150 | Karrenstock-Fm.: Fuggstock-Mb. | Karrenstock-Fm.: Fuggstock-Mb.     |
|15202151 | Mären-Fm. | Mären-Fm.     |
|15202152 | Üblital-Fm. | Üblital-Fm.     |
|15202153 | Ilanz-Verrucano | Ilanz-Verrucano     |
|15202154 | Vernayaz-Fm. | Vernayaz-Fm.     |
|15202155 | Vernayaz-Fm.: Salvan-Mb. | Vernayaz-Fm.: Salvan-Mb.     |
|15202156 | Vernayaz-Fm.: Salvan-Mb.: Vallorcine-Konglomerat | Vernayaz-Fm.: Salvan-Mb.: Vallorcine-Konglomerat     |
|15202157 | Aar-Massiv: Spät- bis postvariszische Intrusiva | Aar-Massiv: Spät- bis postvariszische Intrusiva     |
|15202158 | Gastern-Granit | Gastern-Granit     |
|15202159 | Mittagflue-Granit | Mittagflue-Granit     |
|15202423 | Covayes-Fm. | Covayes-Fm.     |
|15202424 | Javrex-Fm. | Javrex-Fm.     |
|15202425 | Javrex-Fm.: Mergelstein-Fazies | Javrex-Fm.: Mergelstein-Fazies     |
|15202426 | Javrex-Fm.: Kalksandstein-Fazies | Javrex-Fm.: Kalksandstein-Fazies     |
|15202427 | Montsalvens-Kalkarenit | Montsalvens-Kalkarenit     |
|15202429 | Villarbeney-Fm. | Villarbeney-Fm.     |
|15202430 | Villarbeney-Fm.: Veveyse-de-Châtel-Mb. | Villarbeney-Fm.: Veveyse-de-Châtel-Mb.     |
|15202431 | Villarbeney-Fm.: Riondouneire-Mb. | Villarbeney-Fm.: Riondouneire-Mb.     |
|15202432 | Jogne-Fm. | Jogne-Fm.     |
|15202433 | Jogne-Fm.: Kalkbrekzie | Jogne-Fm.: Kalkbrekzie     |
|15202434 | Jogne-Fm.: Vuavres-Mb. | Jogne-Fm.: Vuavres-Mb.     |
|15202435 | Jogne-Fm.: Planière-Mb. | Jogne-Fm.: Planière-Mb.     |
|15202436 | Bifé-Fm. | Bifé-Fm.     |
|15202437 | Bifé-Fm.: Zementkalk | Bifé-Fm.: Zementkalk     |
|15202438 | Bifé-Fm.: Joux-Galez-Mb. | Bifé-Fm.: Joux-Galez-Mb.     |
|15202439 | Pereyre-Fm. | Pereyre-Fm.     |
|15202440 | Praz-Couquain-Fm. | Praz-Couquain-Fm.     |
|15202442 | Gryonne-Fm. | Gryonne-Fm.     |
|15202443 | Praz-Couquain-Fm.: Taffon-Mb. | Praz-Couquain-Fm.: Taffon-Mb.     |
|15202444 | Praz-Couquain-Fm.: Saix-Mb. | Praz-Couquain-Fm.: Saix-Mb.     |
|15200523 | Kronberg-Nagelfluh: Hochfläschli-Mb. | Kronberg-Nagelfluh: Hochfläschli-Mb.     |
|15200524 | Kronberg-Nagelfluh: Ennetbühl-Mb. | Kronberg-Nagelfluh: Ennetbühl-Mb.     |
|15200525 | Kronberg-Nagelfluh: Hochalp-Mb. | Kronberg-Nagelfluh: Hochalp-Mb.     |
|15200526 | Kronberg-Nagelfluh: Krummenau-Mb. | Kronberg-Nagelfluh: Krummenau-Mb.     |
|15200527 | USM-J: Ältere Juranagelfluh | USM-J: Ältere Juranagelfluh     |
|15200528 | Gitzischöpf-Nagelfluh | Gitzischöpf-Nagelfluh     |
|15200529 | Honegg-Mergel | Honegg-Mergel     |
|15200530 | Honegg-Mergel: Kaltbach-Nagelfluh | Honegg-Mergel: Kaltbach-Nagelfluh     |
|15200531 | Thun-Fm.: Hünibach-Nagelfluh | Thun-Fm.: Hünibach-Nagelfluh     |
|15200532 | Losenegg-Fm. | Losenegg-Fm.     |
|15200533 | Homberg-Fm.: Schwändibach-Nagelfluh | Homberg-Fm.: Schwändibach-Nagelfluh     |
|15200534 | Uerscheli-Fm. | Uerscheli-Fm.     |
|15200535 | Uerscheli-Fm.: Bumbach-Nagelfluh | Uerscheli-Fm.: Bumbach-Nagelfluh     |
|15200536 | USM-I: Untere Bunte Molasse: Kalksandstein | USM-I: Untere Bunte Molasse: Kalksandstein     |
|15200537 | Gérignoz-Fm. | Gérignoz-Fm.     |
|15200538 | Speer-Fm.: Leuenfall-Nagelfluh | Speer-Fm.: Leuenfall-Nagelfluh     |
|15200539 | Speer-Fm.: Wintersberg-Mb. | Speer-Fm.: Wintersberg-Mb.     |
|15200540 | Speer-Fm.: Ebnat-Mb. | Speer-Fm.: Ebnat-Mb.     |
|15200541 | Speer-Fm.: Ebnat-Mb.: Rütiberg-Kalksandstein | Speer-Fm.: Ebnat-Mb.: Rütiberg-Kalksandstein     |
|15200542 | Rigi-Fm.: Bunte Rigi-Nagelfluh: Pfiffegg-Nagelfluh | Rigi-Fm.: Bunte Rigi-Nagelfluh: Pfiffegg-Nagelfluh     |
|15202160 | Zentraler Aare-Granit | Zentraler Aare-Granit     |
|15202161 | Grimsel-Granodiorit | Grimsel-Granodiorit     |
|15202162 | Südwestlicher Aare-Granit | Südwestlicher Aare-Granit     |
|15202163 | Bugnei-Granodiorit | Bugnei-Granodiorit     |
|15202164 | Aar-Massiv: Spät- bis postvariszische Sedimente und Vulkanite | Aar-Massiv: Spät- bis postvariszische Sedimente und Vulkanite     |
|15202165 | Wendenjoch-Fm. | Wendenjoch-Fm.     |
|15202166 | Windgällen-Fm. | Windgällen-Fm.     |
|15202167 | Trift-Fm. | Trift-Fm.     |
|15202168 | Intschi-Fm. | Intschi-Fm.     |
|15202169 | Bifertengrätli-Fm. | Bifertengrätli-Fm.     |
|15202170 | Bifertengrätli-Fm.: Lakustrisches Mb. | Bifertengrätli-Fm.: Lakustrisches Mb.     |
|15202171 | Bifertengrätli-Fm.: Estuarisches Mb. | Bifertengrätli-Fm.: Estuarisches Mb.     |
|15202172 | Bifertengrätli-Fm.: Grünhorn-Mb.: Basales Konglomerat | Bifertengrätli-Fm.: Grünhorn-Mb.: Basales Konglomerat     |
|15202173 | Bifertengrätli-Fm.: Grünhorn-Mb. | Bifertengrätli-Fm.: Grünhorn-Mb.     |
|15202174 | Diechtergletscher-Fm. | Diechtergletscher-Fm.     |
|15202175 | Tscharren-Fm. | Tscharren-Fm.     |
|15202177 | Aar-Massiv: Mittelvariszische Intrusiva | Aar-Massiv: Mittelvariszische Intrusiva     |
|15202178 | Brunni-Granit | Brunni-Granit     |
|15202179 | Düssi-Diorit | Düssi-Diorit     |
|15202180 | Munt-Dado-Granit | Munt-Dado-Granit     |
|15203078 | Obflue-Fm. | Obflue-Fm.     |
|15203079 | Brand-Fm. | Brand-Fm.     |
|15203080 | Horngraben-Fm. | Horngraben-Fm.     |
|15203081 | Lückengraben-Fm. | Lückengraben-Fm.     |
|15203082 | Dorfflüe-Fm. | Dorfflüe-Fm.     |
|15203083 | Dorfflüe-Fm.: Gummfluh-Mikrofazies | Dorfflüe-Fm.: Gummfluh-Mikrofazies     |
|15203084 | Dorfflüe-Fm.: Pfad-Mikrofazies | Dorfflüe-Fm.: Pfad-Mikrofazies     |
|15203085 | Dorfflüe-Fm.: Rindenkorn-Mikrofazies | Dorfflüe-Fm.: Rindenkorn-Mikrofazies     |
|15203086 | Dorfflüe-Fm.: Gastlosen-Oolith | Dorfflüe-Fm.: Gastlosen-Oolith     |
|15203087 | Dorfflüe-Fm.: Wandfluh-Mikrofazies | Dorfflüe-Fm.: Wandfluh-Mikrofazies     |
|15203088 | Mytilus-Sch. | Mytilus-Sch.     |
|15203089 | Mytilus-Sch.: Col-de-Cordon-Mb. | Mytilus-Sch.: Col-de-Cordon-Mb.     |
|15203090 | Mytilus-Sch.: Col-de-Cordon-Mb.: Klus-Konglomerat | Mytilus-Sch.: Col-de-Cordon-Mb.: Klus-Konglomerat     |
|15203091 | Mytilus-Sch.: Col-de-Cordon-Mb.: Holzerhorn-Einheit | Mytilus-Sch.: Col-de-Cordon-Mb.: Holzerhorn-Einheit     |
|15203092 | Mytilus-Sch.: Rubli-Mb. | Mytilus-Sch.: Rubli-Mb.     |
|15203093 | Mytilus-Sch.: Chavanette-Mb. | Mytilus-Sch.: Chavanette-Mb.     |
|15203094 | Pralet-Fm.: Erpilles-Mb. | Pralet-Fm.: Erpilles-Mb.     |
|15203095 | Wiriehorn-Fm. | Wiriehorn-Fm.     |
|15203096 | St-Triphon-Fm. | St-Triphon-Fm.     |
|15203097 | St-Triphon-Fm.: Andonces-Mb. | St-Triphon-Fm.: Andonces-Mb.     |
|15203098 | St-Triphon-Fm.: Lessus-Mb. | St-Triphon-Fm.: Lessus-Mb.     |
|15200543 | Weggis-Fm. | Weggis-Fm.     |
|15200544 | Weggis-Fm.: Kännelegg-Nagelfluh | Weggis-Fm.: Kännelegg-Nagelfluh     |
|15200545 | Molasse Rouge des Jurasüdfusses | Molasse Rouge des Jurasüdfusses     |
|15200546 | Molasse Rouge des Jurasüdfusses: Mathod-Sandstein | Molasse Rouge des Jurasüdfusses: Mathod-Sandstein     |
|15200547 | Molasse Rouge des Jurasüdfusses: Goumoëns-Sandstein | Molasse Rouge des Jurasüdfusses: Goumoëns-Sandstein     |
|15200548 | Molasse Rouge de Vevey | Molasse Rouge de Vevey     |
|15200549 | Molasse Rouge de Monthey | Molasse Rouge de Monthey     |
|15200550 | Grindelegg-Fm. | Grindelegg-Fm.     |
|15200551 | Grès et Marnes Gris à Gypse: Tillerée-Sch. | Grès et Marnes Gris à Gypse: Tillerée-Sch.     |
|15200552 | Grès et Marnes Gris à Gypse: Süsswasserkalke und Dolomite | Grès et Marnes Gris à Gypse: Süsswasserkalke und Dolomite     |
|15200553 | Oltingue-Kalkarenit | Oltingue-Kalkarenit     |
|15200554 | Vaulruz-Fm. | Vaulruz-Fm.     |
|15200555 | Hilfern-Fm.: Unter-Lochsiti-Nagelfluh | Hilfern-Fm.: Unter-Lochsiti-Nagelfluh     |
|15200556 | Hilfern-Fm.: Flühli-Nagelfluh | Hilfern-Fm.: Flühli-Nagelfluh     |
|15200557 | St.-Gallen-Fm.: Mergelstein-dominierte Fazies | St.-Gallen-Fm.: Mergelstein-dominierte Fazies     |
|15200558 | Fm. der Granitischen Molasse: Marbach-Mb. | Fm. der Granitischen Molasse: Marbach-Mb.     |
|15200560 | USM-I: Untere Bunte Molasse | USM-I: Untere Bunte Molasse     |
|15200562 | OSM-J: Mittlere Juranagelfluh | OSM-J: Mittlere Juranagelfluh     |
|15200563 | OSM-J: Albstein | OSM-J: Albstein     |
|15202181 | Russein-Diorit | Russein-Diorit     |
|15202182 | Voralp-Granit | Voralp-Granit     |
|15202183 | Aar-Massiv: Frühvariszische Intrusiva | Aar-Massiv: Frühvariszische Intrusiva     |
|15202184 | Punteglias-Granit | Punteglias-Granit     |
|15202185 | Tödi-Granit | Tödi-Granit     |
|15202186 | Strem-Granit | Strem-Granit     |
|15202187 | Baltschieder-Granodiorit | Baltschieder-Granodiorit     |
|15202188 | Giuv-Syenit | Giuv-Syenit     |
|15202189 | Curtin-Monzodiorit | Curtin-Monzodiorit     |
|15202190 | Bristenstock-Syenit | Bristenstock-Syenit     |
|15202191 | Aar-Massiv: Frühvariszische Sedimente | Aar-Massiv: Frühvariszische Sedimente     |
|15202192 | Val-Gliems-Fm. | Val-Gliems-Fm.     |
|15202193 | Bifertenfirn-Fm. | Bifertenfirn-Fm.     |
|15202194 | Aar-Massiv: Prävariszisches polyzyklisches Grundgebirge | Aar-Massiv: Prävariszisches polyzyklisches Grundgebirge     |
|15202195 | Innertkirchen-Migmatit | Innertkirchen-Migmatit     |
|15202196 | Innertkirchen-Migmatit: Zäsenberg-Gneis | Innertkirchen-Migmatit: Zäsenberg-Gneis     |
|15202197 | Erstfeld-Gneiskomplex | Erstfeld-Gneiskomplex     |
|15202198 | Guttannen-Gneiskomplex | Guttannen-Gneiskomplex     |
|15202199 | Straligenstöckli-Gneiskomplex | Straligenstöckli-Gneiskomplex     |
|15202200 | Lötschental-Gneiskomplex | Lötschental-Gneiskomplex     |
|15202445 | Villarbeney-Fm.: Cergnement-Mb. | Villarbeney-Fm.: Cergnement-Mb.     |
|15202446 | Arveyes-Flysch | Arveyes-Flysch     |
|15202447 | Sex-Mort-Flysch | Sex-Mort-Flysch     |
|15202448 | Diechtergletscher-Fm.: Maasplanggstock-Metaandesit | Diechtergletscher-Fm.: Maasplanggstock-Metaandesit     |
|15202449 | Dammagletscher-Diorit | Dammagletscher-Diorit     |
|15202450 | Gryonne-Fm.: Schiefrige Fazies | Gryonne-Fm.: Schiefrige Fazies     |
|15202451 | Gryonne-Fm.: Kalkige Fazies | Gryonne-Fm.: Kalkige Fazies     |
|15202452 | Gryonne-Fm.: Basaler Teil | Gryonne-Fm.: Basaler Teil     |
|15202453 | Glarner-Verrucano: Tektonisierte Basis | Glarner-Verrucano: Tektonisierte Basis     |
|15202454 | Chrüzlistock-Migmatit | Chrüzlistock-Migmatit     |
|15202455 | Piz-Cuolmet-Gneiskomplex | Piz-Cuolmet-Gneiskomplex     |
|15202456 | Pulanera-Gneiskomplex | Pulanera-Gneiskomplex     |
|15202465 | Aiguilles-Rouges-Massiv: Spät- bis postvariszische Sedimente und Vulkanite | Aiguilles-Rouges-Massiv: Spät- bis postvariszische Sedimente und Vulkanite     |
|15202467 | Helvetikum: Variszisches Kristallin | Helvetikum: Variszisches Kristallin     |
|15202468 | Helvetikum: Prävariszisches polyzyklisches Grundgebirge | Helvetikum: Prävariszisches polyzyklisches Grundgebirge     |
|15202469 | Helvetikum: Grundgebirge | Helvetikum: Grundgebirge     |
|15202472 | Catogne-Gneiskomplex | Catogne-Gneiskomplex     |
|15202473 | Grépillons-Leukogranit | Grépillons-Leukogranit     |
|15203099 | St-Triphon-Fm.: Dorchaux-Mb. | St-Triphon-Fm.: Dorchaux-Mb.     |
|15203100 | Mattes-Melange | Mattes-Melange     |
|15203101 | Chumi-Fm. | Chumi-Fm.     |
|15203102 | Joux-Verte-Fm. | Joux-Verte-Fm.     |
|15203103 | Bonave-Fm. | Bonave-Fm.     |
|15203104 | Obere Brekzie | Obere Brekzie     |
|15203105 | Obere Schiefer | Obere Schiefer     |
|15203106 | Untere Brekzie | Untere Brekzie     |
|15203107 | Untere Schiefer | Untere Schiefer     |
|15203108 | Untere Schiefer: Untere Kalke | Untere Schiefer: Untere Kalke     |
|15203109 | Brekzien-Decke:Trias | Brekzien-Decke:Trias     |
|15203110 | Gurnigel-Decke: Flysch | Gurnigel-Decke: Flysch     |
|15203111 | Gurnigel-Decke: Flysch-4 | Gurnigel-Decke: Flysch-4     |
|15203112 | Gurnigel-Decke: Flysch-3b | Gurnigel-Decke: Flysch-3b     |
|15203113 | Gurnigel-Decke: Flysch-3a | Gurnigel-Decke: Flysch-3a     |
|15203114 | Gurnigel-Decke: Flysch-2b | Gurnigel-Decke: Flysch-2b     |
|15203115 | Gurnigel-Decke: Flysch-2a | Gurnigel-Decke: Flysch-2a     |
|15203116 | Hellstätt-Fm. | Hellstätt-Fm.     |
|15203117 | Schlieren-Decke: Flysch | Schlieren-Decke: Flysch     |
|15203118 | Schlieren-Sandstein | Schlieren-Sandstein     |
|15203119 | Schoni-Sandstein | Schoni-Sandstein     |
|15203120 | Schoni-Sandstein: Oberer Tonstein | Schoni-Sandstein: Oberer Tonstein     |
|15200564 | Grimmelfingen-Fm.: Graupensand-Fazies | Grimmelfingen-Fm.: Graupensand-Fazies     |
|15200565 | OSM-J: Heliciden-Mergel | OSM-J: Heliciden-Mergel     |
|15200566 | Haldenhof-Mergel | Haldenhof-Mergel     |
|15200567 | OMM-J | OMM-J     |
|15200568 | Tenniken-Muschelagglomerat | Tenniken-Muschelagglomerat     |
|15200569 | OMM-II: Turritellen-Kalk | OMM-II: Turritellen-Kalk     |
|15200570 | Randen-Grobkalk | Randen-Grobkalk     |
|15200571 | Péry-Sandstein | Péry-Sandstein     |
|15200572 | Les-Bayards-Juranagelfluh | Les-Bayards-Juranagelfluh     |
|15200573 | Günsberg- und Vellerat-Fm. | Günsberg- und Vellerat-Fm.     |
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
|15202201 | Ofenhorn-Stampfhorn-Gneiskomplex | Ofenhorn-Stampfhorn-Gneiskomplex     |
|15202202 | Fully-Granodiorit | Fully-Granodiorit     |
|15202203 | Vernayaz-Fm.: Salvan-Mb.: Plex-Aboyeu-Rhyolith | Vernayaz-Fm.: Salvan-Mb.: Plex-Aboyeu-Rhyolith     |
|15202204 | Vallorcine-Granit | Vallorcine-Granit     |
|15202205 | Vallorcine-Granit: Miéville-Mylonit | Vallorcine-Granit: Miéville-Mylonit     |
|15202206 | Montées-Pélissiers-Granit | Montées-Pélissiers-Granit     |
|15202207 | Pormenaz-Granit | Pormenaz-Granit     |
|15202210 | Emosson-Gneiskomplex | Emosson-Gneiskomplex     |
|15202211 | Luisin-Orthogneis | Luisin-Orthogneis     |
|15202212 | Val-Bérard-Gneiskomplex | Val-Bérard-Gneiskomplex     |
|15202213 | Lac-Cornu-Eklogit | Lac-Cornu-Eklogit     |
|15202214 | Perrons-Orthogneis | Perrons-Orthogneis     |
|15202215 | Breya-Rhyolith | Breya-Rhyolith     |
|15202216 | Mont-Blanc-Granit | Mont-Blanc-Granit     |
|15202217 | Montenvers-Granit | Montenvers-Granit     |
|15202218 | Lognan-Orthogneis | Lognan-Orthogneis     |
|15202219 | Pétoudes-Orthogneis | Pétoudes-Orthogneis     |
|15202220 | Gotthard-Decke: Postvariszische Intrusiva | Gotthard-Decke: Postvariszische Intrusiva     |
|15202221 | Rotondo-Granit | Rotondo-Granit     |
|15202222 | Cacciola-Granit | Cacciola-Granit     |
|15202474 | Arpette-Leukogranit | Arpette-Leukogranit     |
|15202475 | Gärsthorn-Gneiskomplex: Bitschji-Augengneis | Gärsthorn-Gneiskomplex: Bitschji-Augengneis     |
|15202476 | Gärsthorn-Gneiskomplex: Geimen-Augengneis | Gärsthorn-Gneiskomplex: Geimen-Augengneis     |
|15202477 | Mont-Blanc-Massiv: Prävariszische Migmatite | Mont-Blanc-Massiv: Prävariszische Migmatite     |
|15202478 | Mont-Blanc-Massiv: Prävariszisches Grundgebirge: Amphibolit-reiche Fazies | Mont-Blanc-Massiv: Prävariszisches Grundgebirge: Amphibolit-reiche Fazies     |
|15202479 | Mont-Blanc-Massiv: Prävariszisches Grundgebirge: Mylonit | Mont-Blanc-Massiv: Prävariszisches Grundgebirge: Mylonit     |
|15202480 | Morcles-Mikrogranit | Morcles-Mikrogranit     |
|15202481 | Aiguilles-Rouges-Massiv: Prävariszisches Migmatite | Aiguilles-Rouges-Massiv: Prävariszisches Migmatite     |
|15202482 | Fully-Gneiskomplex | Fully-Gneiskomplex     |
|15202483 | Hinterbalm-Granit | Hinterbalm-Granit     |
|15202484 | Balmenegg-Granit | Balmenegg-Granit     |
|15202485 | Zentraler-Aare-Granit: Unter-der-Flue-Varietät | Zentraler-Aare-Granit: Unter-der-Flue-Varietät     |
|15202486 | Pardatschas-Granit | Pardatschas-Granit     |
|15202487 | Rossbodenstock-Diorit | Rossbodenstock-Diorit     |
|15202488 | Val-da-Surplattas-Diorit | Val-da-Surplattas-Diorit     |
|15202489 | Tscharren-Fm.: Rinderbiel-Mikrogranit | Tscharren-Fm.: Rinderbiel-Mikrogranit     |
|15203121 | Guber-Sandstein | Guber-Sandstein     |
|15203122 | Guber-Sandstein: Unterer Tonstein | Guber-Sandstein: Unterer Tonstein     |
|15203123 | Schlieren-Decke: Basaler Flysch | Schlieren-Decke: Basaler Flysch     |
|15203124 | Estavannens-Fm. | Estavannens-Fm.     |
|15203125 | Reidigen-Fm. | Reidigen-Fm.     |
|15203126 | Biot-Fm. | Biot-Fm.     |
|15203127 | Chétillon-Fm. | Chétillon-Fm.     |
|15203128 | Rodomonts-Fm. | Rodomonts-Fm.     |
|15203129 | Rodomonts-Fm.: Mocausa-Nagelfluh | Rodomonts-Fm.: Mocausa-Nagelfluh     |
|15203130 | Tissota-Melange | Tissota-Melange     |
|15203131 | Tissota-Melange: Gueyraz-Komplex | Tissota-Melange: Gueyraz-Komplex     |
|15203132 | Manche-Fm.: Weissenburg-Flysch | Manche-Fm.: Weissenburg-Flysch     |
|15203133 | Manche-Fm. | Manche-Fm.     |
|15203134 | Fouyet-Fm. | Fouyet-Fm.     |
|15203135 | Tissota-Melange: Gueyraz-Komplex: Foraminiferenschichten | Tissota-Melange: Gueyraz-Komplex: Foraminiferenschichten     |
|15203136 | Tissota-Melange: Gueyraz-Komplex: Aptychenkalk | Tissota-Melange: Gueyraz-Komplex: Aptychenkalk     |
|15203137 | Tissota-Melange: Gueyraz-Komplex: Radiolarit | Tissota-Melange: Gueyraz-Komplex: Radiolarit     |
|15203138 | Tissota-Melange: Gueyraz-Komplex: Filamentkalk | Tissota-Melange: Gueyraz-Komplex: Filamentkalk     |
|15203139 | Tissota-Melange: Gueyraz-Komplex: Spatkalk | Tissota-Melange: Gueyraz-Komplex: Spatkalk     |
|15203140 | Hundsrügg-Fm. | Hundsrügg-Fm.     |
|15200589 | USM-III bis OSM-I | USM-III bis OSM-I     |
|15200590 | Uetliberg-Fm.: Loorenkopf-Nagelfluh | Uetliberg-Fm.: Loorenkopf-Nagelfluh     |
|15200591 | Grand-Essert-Fm: Neuchâtel-Mb.: Oberer Teil | Grand-Essert-Fm: Neuchâtel-Mb.: Oberer Teil     |
|15200592 | Grand-Essert-Fm: Neuchâtel-Mb.: Unterer Teil | Grand-Essert-Fm: Neuchâtel-Mb.: Unterer Teil     |
|15200593 | Chambotte-Fm.: Oberer Teil | Chambotte-Fm.: Oberer Teil     |
|15200594 | Chambotte-Fm.: Unterer Teil | Chambotte-Fm.: Unterer Teil     |
|15200616 | Schwarzwald-Massiv: Grundgebirge | Schwarzwald-Massiv: Grundgebirge     |
|15200617 | Schwarzwald-Massiv: Variszische Intrusiva | Schwarzwald-Massiv: Variszische Intrusiva     |
|15200618 | USM-I: Untere Bunte Molasse: Mümliswil-Süsswasserkalk | USM-I: Untere Bunte Molasse: Mümliswil-Süsswasserkalk     |
|15200619 | Luzern-Fm.: Limnischer Horizont | Luzern-Fm.: Limnischer Horizont     |
|15200620 | Molasse Rouge des Jurasüdfusses: Dardagny-Sandstein | Molasse Rouge des Jurasüdfusses: Dardagny-Sandstein     |
|15200621 | Napf-Fm.: Konglomerat-dominierte Fazies | Napf-Fm.: Konglomerat-dominierte Fazies     |
|15200622 | Napf-Fm.: Sandstein-Mergelstein-dominierte Fazies | Napf-Fm.: Sandstein-Mergelstein-dominierte Fazies     |
|15200623 | Le-Locle-Fm. | Le-Locle-Fm.     |
|15200624 | Le-Locle-Fm.: Le-Verger Mb. | Le-Locle-Fm.: Le-Verger Mb.     |
|15200625 | Le-Locle-Fm.: Combe-Girard Mb. | Le-Locle-Fm.: Combe-Girard Mb.     |
|15200626 | Crêt-du-Locle-Fm. | Crêt-du-Locle-Fm.     |
|15200627 | Crêt-du-Locle-Fm.: Mergelfazies | Crêt-du-Locle-Fm.: Mergelfazies     |
|15200628 | St.-Gallen-Fm.: Gitzigrabe-Grobsandstein | St.-Gallen-Fm.: Gitzigrabe-Grobsandstein     |
|15202223 | Sädelhorn-Diorit | Sädelhorn-Diorit     |
|15202224 | Winterhorn-Granit | Winterhorn-Granit     |
|15202225 | Gotthard-Decke: Spätvariszische Intrusiva | Gotthard-Decke: Spätvariszische Intrusiva     |
|15202226 | Medel-Granit | Medel-Granit     |
|15202227 | Cristallina-Granodiorit | Cristallina-Granodiorit     |
|15202228 | Gamsboden-Granit | Gamsboden-Granit     |
|15202229 | Uffiern-Diorit | Uffiern-Diorit     |
|15202230 | Fibbia-Granit | Fibbia-Granit     |
|15202231 | Gotthard-Decke: Prä- und frühvariszische Metasedimentgesteine und Vulkanoklastika | Gotthard-Decke: Prä- und frühvariszische Metasedimentgesteine und Vulkanoklastika     |
|15202232 | Borel-Gneiskomplex | Borel-Gneiskomplex     |
|15202233 | Tenelin-Gneiskomplex | Tenelin-Gneiskomplex     |
|15202234 | Laiets-Gneiskomplex | Laiets-Gneiskomplex     |
|15202235 | Tremola-Gneiskomplex | Tremola-Gneiskomplex     |
|15202236 | Tremola-Gneiskomplex: Pontino-Schiefer | Tremola-Gneiskomplex: Pontino-Schiefer     |
|15202237 | Tremola-Gneiskomplex: Nelva-Gneis | Tremola-Gneiskomplex: Nelva-Gneis     |
|15202238 | Tremola-Gneiskomplex: Sasso-Rosso-Schiefer | Tremola-Gneiskomplex: Sasso-Rosso-Schiefer     |
|15202239 | Prüsfa-Gneiskomplex | Prüsfa-Gneiskomplex     |
|15202240 | Streifengneis-Komplex | Streifengneis-Komplex     |
|15202241 | Chastelhorn-Metagabbro | Chastelhorn-Metagabbro     |
|15202490 | Leventina-Lucomagno-Decke: Trias: Quarzit | Leventina-Lucomagno-Decke: Trias: Quarzit     |
|15202491 | Kapfen-Fm. | Kapfen-Fm.     |
|15202492 | Kapfen-Fm.: Sandstein-dominierte Fazies | Kapfen-Fm.: Sandstein-dominierte Fazies     |
|15202493 | Kärpf-Fm.: Kärpfgipfel-Sernifit | Kärpf-Fm.: Kärpfgipfel-Sernifit     |
|15202494 | Fulen-Fm. | Fulen-Fm.     |
|15202495 | Karrenstock-Fm.: Glattmatt-Mb. | Karrenstock-Fm.: Glattmatt-Mb.     |
|15202496 | Mären-Fm.: Grisch-Mb.: Hanenstock-Keratophyr | Mären-Fm.: Grisch-Mb.: Hanenstock-Keratophyr     |
|15202497 | Mären-Fm.: Grisch-Mb.: Sonnenberg-Horizonte | Mären-Fm.: Grisch-Mb.: Sonnenberg-Horizonte     |
|15202498 | Mären-Fm.: Grisch-Mb.: Chamseeli-Konglomerat | Mären-Fm.: Grisch-Mb.: Chamseeli-Konglomerat     |
|15202499 | Murgtal-Fm.: Chartegg-Mb.: Rotberg-Sandstein | Murgtal-Fm.: Chartegg-Mb.: Rotberg-Sandstein     |
|15202500 | Murgtal-Fm.: Seez-Mb. | Murgtal-Fm.: Seez-Mb.     |
|15202501 | Murgtal-Fm.: Gufelialp-Mb. | Murgtal-Fm.: Gufelialp-Mb.     |
|15202502 | Ilanz-Verrucano s.s. | Ilanz-Verrucano s.s.     |
|15202503 | Ilanz-Verrucano: Buntgefleckte Schiefer | Ilanz-Verrucano: Buntgefleckte Schiefer     |
|15202504 | Tavetsch-Decke: Perm | Tavetsch-Decke: Perm     |
|15202505 | Windgällen-Fm.: Mikrogranit | Windgällen-Fm.: Mikrogranit     |
|15202506 | Bifertengrätli-Fm.: Sandalp-Rhyolith | Bifertengrätli-Fm.: Sandalp-Rhyolith     |
|15202507 | Tscharren-Fm.: Tuffitische Fazies | Tscharren-Fm.: Tuffitische Fazies     |
|15200629 | Trois-Rods-Süsswasserkalk | Trois-Rods-Süsswasserkalk     |
|15200630 | Champ-Vuillerat-Süsswasserkalk | Champ-Vuillerat-Süsswasserkalk     |
|15200631 | Napf-Fm.: Wolhusen-Bentonit | Napf-Fm.: Wolhusen-Bentonit     |
|15200632 | OSM-II: Gitzitobel-Süsswasserkalk | OSM-II: Gitzitobel-Süsswasserkalk     |
|15200633 | OSM-II: Wissenbach-Süsswasserkalk | OSM-II: Wissenbach-Süsswasserkalk     |
|15200634 | OSM-II: Altbach-Süsswasserkalk | OSM-II: Altbach-Süsswasserkalk     |
|15200635 | OSM-II: Tröleten-Süsswasserkalk | OSM-II: Tröleten-Süsswasserkalk     |
|15200636 | OSM-II: Tschöplihof-Süsswasserkalk | OSM-II: Tschöplihof-Süsswasserkalk     |
|15200637 | Lienegg-Fm. | Lienegg-Fm.     |
|15200638 | Öligraben-Fm. | Öligraben-Fm.     |
|15200639 | Studweid-Fm. | Studweid-Fm.     |
|15200640 | Rossemaison-Fm. | Rossemaison-Fm.     |
|15200641 | Schwaningen-Merenbach-Rhyolith | Schwaningen-Merenbach-Rhyolith     |
|15200642 | Schwaningen-Weizen-Granit | Schwaningen-Weizen-Granit     |
|15200643 | Etzgen-Granit | Etzgen-Granit     |
|15200645 | USM-I: Kalk-Dolomit-Nagelfluh | USM-I: Kalk-Dolomit-Nagelfluh     |
|15200646 | Hornbüel-Melange | Hornbüel-Melange     |
|15200647 | Kalter-Wangen-Fm. | Kalter-Wangen-Fm.     |
|15200648 | Baltersweil-Nagelfluh | Baltersweil-Nagelfluh     |
|15200649 | Netzbachtal-Nagelfluh | Netzbachtal-Nagelfluh     |
|15200650 | Rocher-des-Hirondelles-Fm. | Rocher-des-Hirondelles-Fm.     |
|15202242 | Val-Nalps-Gneiskomplex: Gurschen-Gneis | Val-Nalps-Gneiskomplex: Gurschen-Gneis     |
|15202243 | Val-Nalps-Gneiskomplex: Guspis-Gneis | Val-Nalps-Gneiskomplex: Guspis-Gneis     |
|15202244 | Paradis-Gneiskomplex: Sorescia-Gneis | Paradis-Gneiskomplex: Sorescia-Gneis     |
|15202246 | Helvetikum: Grundgebirge: Granit | Helvetikum: Grundgebirge: Granit     |
|15202247 | Helvetikum: Grundgebirge: Saures vulkanisches Gestein | Helvetikum: Grundgebirge: Saures vulkanisches Gestein     |
|15202254 | Ilanz-Zone: Permische Sedimente | Ilanz-Zone: Permische Sedimente     |
|15202255 | Helvetikum: Grundgebirge: Permisch verwittertes Kristallin | Helvetikum: Grundgebirge: Permisch verwittertes Kristallin     |
|15202256 | Goltschenried-Fm. | Goltschenried-Fm.     |
|15202257 | Oberaar-Furka Zone | Oberaar Furka Zone     |
|15202258 | Ausserberg-Avat-Zone | Ausserberg-Avat-Zone     |
|15202260 | Ausserberg-Avat-Zone: Granitischer Gneis | Ausserberg-Avat-Zone: Granitischer Gneis     |
|15202261 | Ausserberg-Avat-Zone: Paragneis | Ausserberg-Avat-Zone: Paragneis     |
|15202262 | Clavaniev-Zone | Clavaniev-Zone     |
|15202263 | Gärsthorn-Gneiskomplex: Engi-Granit | Gärsthorn-Gneiskomplex: Engi-Granit     |
|15202264 | Calmut-Gneiskomplex | Calmut-Gneiskomplex     |
|15202265 | Val-Pigniu-Gneiskomplex | Val-Pigniu-Gneiskomplex     |
|15202266 | Urseren-Garvera-Zone: Permo-Karbon | Urseren-Garvera-Zone: Permo-Karbon     |
|15202267 | Goms-Gneiskomplex | Goms-Gneiskomplex     |
|15202508 | Tscharren-Fm.: Ignimbritische Fazies | Tscharren-Fm.: Ignimbritische Fazies     |
|15202509 | Euthal-Fm.: Guschakopf-Sandstein | Euthal-Fm.: Guschakopf-Sandstein     |
|15202510 | Quinten-Fm.: Gonzen-Eisenerzhorizont | Quinten-Fm.: Gonzen-Eisenerzhorizont     |
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
|15200651 | Rocher-des-Hirondelles-Fm.: Fort-de-l&#39;Ecluse-Mb. | Rocher-des-Hirondelles-Fm.: Fort-de-l&#39;Ecluse-Mb.     |
|15200652 | Gorges-de-l&#39;Orbe-Fm.: Bôle-Mb. | Gorges-de-l&#39;Orbe-Fm.: Bôle-Mb.     |
|15200653 | Gorges-de-l&#39;Orbe-Fm.: Montcherand-Mb. | Gorges-de-l&#39;Orbe-Fm.: Montcherand-Mb.     |
|15200654 | Vuache-Fm.: Calcaire roux s.s. | Vuache-Fm.: Calcaire roux s.s.     |
|15200658 | Schwarzbach-Fm. | Schwarzbach-Fm.     |
|15200659 | Wangen- und Letzi-Mb. | Wangen- und Letzi-Mb.     |
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
|15201158 | La-Côte-Schotter | La-Côte-Schotter     |
|15201003 | Hochterrasse | Hochterrasse     |
|15201050 | Gondiswil-Interglazial (Letztes Interglazial) | Gondiswil-Interglazial (Letztes Interglazial)     |
|15201051 | Flurlingen-Quelltuff | Flurlingen-Quelltuff     |
|15201052 | Birrfeld- und Klettgau-Paläoböden | Birrfeld- und Klettgau-Paläoböden     |
|15201045 | Klettgau-Schotter | Klettgau-Schotter     |
|15201046 | Obere Klettgauschotter | Obere Klettgauschotter     |
|15201047 | Glazi-lakustrische Serie | Glazi-lakustrische Serie     |
|15201048 | Mittlere Klettgauschotter | Mittlere Klettgauschotter     |
|15201049 | Untere Klettgauschotter | Untere Klettgauschotter     |
|15201159 | Enge-Schotter | Enge-Schotter     |
|15201160 | Attiswil-Schotter | Attiswil-Schotter     |
|15201161 | Lommiswil-Schotter | Lommiswil-Schotter     |
|15201162 | Oensingen-Moos-Lehm | Oensingen-Moos-Lehm     |
|15201163 | Berken-Schotter | Berken-Schotter     |
|15201164 | Berken-Sand | Berken-Sand     |
|15201165 | Schwarzhäusern-Lehm | Schwarzhäusern-Lehm     |
|15201166 | Käppelihof-Schotter | Käppelihof-Schotter     |
|15201167 | Aarburg-Schotter | Aarburg-Schotter     |
|15201168 | Tuileries-Formation | Tuileries-Formation     |
|15201169 | Grandson-Formation | Grandson-Formation     |
|15201170 | Poissine-Formation | Poissine-Formation     |
|15201053 | Beringen-Eiszeit | Beringen-Eiszeit     |
|15201171 | Surbtal-Lehm | Surbtal-Lehm     |
|15201172 | Surbtal-Till | Surbtal-Till     |
|15201173 | Surbtal-Schotter | Surbtal-Schotter     |
|15201174 | Fislisbach-Schotter | Fislisbach-Schotter     |
|15201054 | Entfelden-Schotter | Entfelden-Schotter     |
|15201055 | Aarau-Schotter | Aarau-Schotter     |
|15201056 | Suhr-Schotter | Suhr-Schotter     |
|15201057 | Veltheim-Schotter | Veltheim-Schotter     |
|15201058 | Stüsslingen-Schotter | Stüsslingen-Schotter     |
|15201059 | Langwiesen-Vergletscherung | Langwiesen-Vergletscherung     |
|15201060 | Langwiesen-Vorstoss | Langwiesen-Vorstoss     |
|15201061 | Schaffhausen-Schotter | Schaffhausen-Schotter     |
|15201062 | Reuenthal-Vorstoss | Reuenthal-Vorstoss     |
|15201063 | Lupfig-Schotter | Lupfig-Schotter     |
|15202525 | Bommerstein-Fm.: Glockhaus-Mb.: Grenzquarzit | Bommerstein-Fm.: Glockhaus-Mb.: Grenzquarzit     |
|15202526 | Telltistock-Granit | Telltistock-Granit     |
|15202527 | Öhrli-Fm.: von Siderolithikum durchsetzt | Öhrli-Fm.: von Siderolithikum durchsetzt     |
|15202528 | Zentraler-Aare-Granit: Beesten-Varietät | Zentraler-Aare-Granit: Beesten-Varietät     |
|15202529 | Diechtergletscher-Fm.: Garwiidi-Diorit | Diechtergletscher-Fm.: Garwiidi-Diorit     |
|15202530 | Alp-Crap-Ner-Granit | Alp-Crap-Ner-Granit     |
|15202531 | Innertkirchen-Migmatit: Permisch verwittert | Innertkirchen-Migmatit: Permisch verwittert     |
|15202532 | Erstfeld-Gneiskomplex: Permisch verwittert | Erstfeld-Gneiskomplex: Permisch verwittert     |
|15202533 | Martinsmad-Fm.: Supraquarzitischer Flysch: Suren-Flysch | Martinsmad-Fm.: Supraquarzitischer Flysch: Suren-Flysch     |
|15202534 | Stad-Fm.: Spirstock-Mb.: Obere Sandsteine | Stad-Fm.: Spirstock-Mb.: Obere Sandsteine     |
|15202535 | Stad-Fm.: Spirstock-Mb.: Blockmergel | Stad-Fm.: Spirstock-Mb.: Blockmergel     |
|15202536 | Stad-Fm.: Spirstock-Mb.: Untere Sandsteine | Stad-Fm.: Spirstock-Mb.: Untere Sandsteine     |
|15202537 | Helvetischer Kieselkalk: Ringgenberg-Sch. | Helvetischer Kieselkalk: Ringgenberg-Sch.     |
|15202538 | Quinten-Fm.: Brekziöse Fazies | Quinten-Fm.: Brekziöse Fazies     |
|15202539 | Schattwald-Mergelkalk | Schattwald-Mergelkalk     |
|15202540 | Elm- und Matt-Fm. | Elm- und Matt-Fm.     |
|15202541 | Elm- und Matt-Fm.: Quarzsandstein | Elm- und Matt-Fm.: Quarzsandstein     |
|15203141 | Perrières-Fm. | Perrières-Fm.     |
|15203142 | Rhenodanubischer Flysch | Rhenodanubischer Flysch     |
|15203143 | Vorarlberg-Flysch | Vorarlberg-Flysch     |
|15203144 | Fanola-Fm. | Fanola-Fm.     |
|15203145 | Planknerbrücke-Fm. | Planknerbrücke-Fm.     |
|15203146 | Planken-Fm. | Planken-Fm.     |
|15203147 | Reiselsberg-Fm. | Reiselsberg-Fm.     |
|15203148 | Reiselsberg-Fm.: Basaler Teil | Reiselsberg-Fm.: Basaler Teil     |
|15203149 | Liechtenstein-Flysch | Liechtenstein-Flysch     |
|15203150 | Triesen-Fm. | Triesen-Fm.     |
|15203151 | Vaduz-Flysch | Vaduz-Flysch     |
|15203152 | Eichholztobel-Fm. | Eichholztobel-Fm.     |
|15203153 | Schloss-Fm. | Schloss-Fm.     |
|15203154 | Gaschlo-Fm. | Gaschlo-Fm.     |
|15203155 | Leimern-Sch.: Kalkige-Fazies | Leimern-Sch.: Kalkige-Fazies     |
|15203156 | Pierre-Avoi-Melange | Pierre-Avoi-Melange     |
|15203157 | St-Christophe-Fm. | St-Christophe-Fm.     |
|15203158 | Marmontains-Fm. | Marmontains-Fm.     |
|15203159 | Aroley-Fm. | Aroley-Fm.     |
|15203160 | Ferret-Schiefer: Peula-Sch. | Ferret-Schiefer: Peula-Sch.     |
|15203161 | Versoyen-Sch. | Versoyen-Sch.     |
|15203162 | Prättigau-Schiefer | Prättigau-Schiefer     |
|15203163 | Ruchberg-Fm. | Ruchberg-Fm.     |
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
|15202268 | Ausserbinn-Piz-Cavel-Zone | Ausserbinn-Piz-Cavel-Zone     |
|15202271 | Prosa-Granit | Prosa-Granit     |
|15202272 | Val-Tremola-Granit | Val-Tremola-Granit     |
|15202273 | Leventina-Gneis | Leventina-Gneis     |
|15202274 | Lucomagno-Decke: Prävariszischer Orthogneis | Lucomagno-Decke: Prävariszischer Orthogneis     |
|15202275 | Lucomagno-Decke: Prävariszischer Paragneis | Lucomagno-Decke: Prävariszischer Paragneis     |
|15202276 | Val-Stgira-Riffmarmor | Val-Stgira-Riffmarmor     |
|15202277 | Piz-Terri-Lunschania: Fossilmarmor | Piz-Terri-Lunschania: Fossilmarmor     |
|15202278 | Piz-Terri-Lunschania: Trias | Piz-Terri-Lunschania: Trias     |
|15202279 | Ultrahelvetischer Flysch | Ultrahelvetischer Flysch     |
|15202280 | Sardona-Decke: Melange | Sardona-Decke: Melange     |
|15202281 | Martinsmad-Fm. | Martinsmad-Fm.     |
|15202282 | Martinsmad-Fm.: Supraquarzitischer Flysch | Martinsmad-Fm.: Supraquarzitischer Flysch     |
|15202283 | Martinsmad-Fm.: Sardona-Mb. | Martinsmad-Fm.: Sardona-Mb.     |
|15202284 | Martinsmad-Fm.: Infraquarzitischer Flysch | Martinsmad-Fm.: Infraquarzitischer Flysch     |
|15202285 | Meilleret-Fm. | Meilleret-Fm.     |
|15202286 | Lavtina-Sandstein | Lavtina-Sandstein     |
|15202287 | Blattengrat-Sandstein | Blattengrat-Sandstein     |
|15202288 | Burg-Sandstein | Burg-Sandstein     |
|15202289 | Elm-Fm.: Val-d&#39;Illiez-Sandstein | Elm-Fm.: Val-d&#39;Illiez-Sandstein     |
|15202542 | Nordhelvetische Flysch-Gr.: Schiefriger Tonstein | Nordhelvetische Flysch-Gr.: Schiefriger Tonstein     |
|15202543 | Tierwis-Fm.: Schiefrige Fazies | Tierwis-Fm.: Schiefrige Fazies     |
|15202544 | Tierwis-Fm.: Kalkige Fazies | Tierwis-Fm.: Kalkige Fazies     |
|15202545 | Bommerstein-Fm.: Glockhaus-Mb.: Schiefriger Eisensandstein | Bommerstein-Fm.: Glockhaus-Mb.: Schiefriger Eisensandstein     |
|15202546 | Helvetikum: Trias: Dolomit | Helvetikum: Trias: Dolomit     |
|15202547 | Helvetikum: Trias: Rauwacke | Helvetikum: Trias: Rauwacke     |
|15202548 | Helvetikum: Trias: Gips | Helvetikum: Trias: Gips     |
|15202549 | Baltschieder-Granodiorit: Biotittonalit | Baltschieder-Granodiorit: Biotittonalit     |
|15202550 | Baltschieder-Granodiorit: Hornblende Biotittonalit | Baltschieder-Granodiorit: Hornblende Biotittonalit     |
|15202551 | Erstfeld-Gneiskomplex: Biotit-Plagioklasgneis | Erstfeld-Gneiskomplex: Biotit-Plagioklasgneis     |
|15202552 | Erstfeld-Gneiskomplex: Orthogneis | Erstfeld-Gneiskomplex: Orthogneis     |
|15202553 | Erstfeld-Gneiskomplex: Migmatit | Erstfeld-Gneiskomplex: Migmatit     |
|15202554 | Guttannen-Gneiskomplex: Paragneis | Guttannen-Gneiskomplex: Paragneis     |
|15202555 | Guttannen-Gneiskomplex: Orthogneis | Guttannen-Gneiskomplex: Orthogneis     |
|15202556 | Guttannen-Gneiskomplex: Biotit-Chloritschiefer | Guttannen-Gneiskomplex: Biotit-Chloritschiefer     |
|15202557 | Guttannen-Gneiskomplex: Chlorit-Serizitschiefer | Guttannen-Gneiskomplex: Chlorit-Serizitschiefer     |
|15202558 | Lötschental-Gneiskomplex: Muskovitgneis | Lötschental-Gneiskomplex: Muskovitgneis     |
|15200330 | Fm. der Granitischen Molasse | Fm. der Granitischen Molasse     |
|15200331 | Fm. der Granitischen Molasse: Oberaquitane Mergelzone | Fm. der Granitischen Molasse: Oberaquitane Mergelzone     |
|15200332 | Lausanne-Fm. | Lausanne-Fm.     |
|15200333 | Lausanne-Fm.: Bois-Genoud-Bentonit | Lausanne-Fm.: Bois-Genoud-Bentonit     |
|15200334 | Lausanne-Fm.: Cuarny-Sandstein | Lausanne-Fm.: Cuarny-Sandstein     |
|15200335 | USM-I | USM-I     |
|15200336 | Grès et Marnes Gris à Gypse | Grès et Marnes Gris à Gypse     |
|15200337 | Molasse à Charbon | Molasse à Charbon     |
|15200338 | Molasse Rouge | Molasse Rouge     |
|15200339 | Heuboden-Äschitannen-Nagelfluh | Heuboden-Äschitannen-Nagelfluh     |
|15200340 | Beichlen-Fm. | Beichlen-Fm.     |
|15200341 | USM-J | USM-J     |
|15200342 | USM-J: La-Chaux-Süsswasserkalk | USM-J: La-Chaux-Süsswasserkalk     |
|15200343 | Elsässer Molasse | Elsässer Molasse     |
|15200344 | Elsässer Molasse: Delémont-Süsswasserkalk | Elsässer Molasse: Delémont-Süsswasserkalk     |
|15200345 | Elsässer Molasse: Matzendorf-Süsswasserkalk | Elsässer Molasse: Matzendorf-Süsswasserkalk     |
|15200346 | Elsässer Molasse: Oensingen-Süsswasserkalk | Elsässer Molasse: Oensingen-Süsswasserkalk     |
|15200347 | Elsässer Molasse: Wynau-Süsswasserkalk | Elsässer Molasse: Wynau-Süsswasserkalk     |
|15200348 | UMM (Untere Meeresmolasse) | UMM (Untere Meeresmolasse)     |
|15200349 | UMM-III | UMM-III     |
|15200691 | OSM: Humlikon-Bentonit | OSM: Humlikon-Bentonit     |
|15202001 | Habkern-Melange | Habkern-Melange     |
|15202002 | Sörenberg-Melange | Sörenberg-Melange     |
|15202003 | Wildhaus-Melange | Wildhaus-Melange     |
|15202004 | Südhelvetischer Flysch | Südhelvetischer Flysch     |
|15202005 | Nordhelvetische Flysch-Gr. | Nordhelvetische Flysch-Gr.     |
|15202006 | Matt-Fm. | Matt-Fm.     |
|15202007 | Matt-Fm.: Engi-Dachschiefer | Matt-Fm.: Engi-Dachschiefer     |
|15202008 | Matt-Fm.: Gruontal-Konglomerat | Matt-Fm.: Gruontal-Konglomerat     |
|15202009 | Elm-Fm. | Elm-Fm.     |
|15202010 | Matt-Fm.: Gruontal-Konglomerat: Rüschenweid-Bk. | Matt-Fm.: Gruontal-Konglomerat: Rüschenweid-Bk.     |
|15202011 | Taveyannaz-Fm. | Taveyannaz-Fm.     |
|15202012 | Helvetikum: Paläogen | Helvetikum: Paläogen     |
|15202013 | Stad-Fm. | Stad-Fm.     |
|15202014 | Stad-Fm.: Wängen-Kalk | Stad-Fm.: Wängen-Kalk     |
|15202015 | Stad-Fm.: Jochstock-Konglomerat | Stad-Fm.: Jochstock-Konglomerat     |
|15202016 | Sanetsch-Fm. | Sanetsch-Fm.     |
|15202017 | Sanetsch-Fm.: Pierredar-Kalk | Sanetsch-Fm.: Pierredar-Kalk     |
|15202018 | Sanetsch-Fm.: Tsanfleuron-Mb. | Sanetsch-Fm.: Tsanfleuron-Mb.     |
|15202019 | Sanetsch-Fm.: Diablerets-Mb. | Sanetsch-Fm.: Diablerets-Mb.     |
|15202020 | Niederhorn-Fm. | Niederhorn-Fm.     |
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
|15202290 | Muot-da-Rubi-Fm. | Muot-da-Rubi-Fm.     |
|15202291 | Muot-da-Rubi-Fm.: Ahornen-Mb. | Muot-da-Rubi-Fm.: Ahornen-Mb.     |
|15202292 | Muot-da-Rubi-Fm.: Kistenstöckli-Mb. | Muot-da-Rubi-Fm.: Kistenstöckli-Mb.     |
|15202293 | Muot-da-Rubi-Fm.: Ghölzwald-Mb. | Muot-da-Rubi-Fm.: Ghölzwald-Mb.     |
|15202294 | Muot-da-Rubi-Fm.: Malor-Mb. | Muot-da-Rubi-Fm.: Malor-Mb.     |
|15202295 | Südelgrabe-Melange | Südelgrabe-Melange     |
|15202296 | Stad-Fm.: Kleintal-Konglomerat | Stad-Fm.: Kleintal-Konglomerat     |
|15202297 | Stad-Fm.: Rütenen-Konglomerat | Stad-Fm.: Rütenen-Konglomerat     |
|15202298 | Helvetikum: Jura | Helvetikum: Jura     |
|15202299 | Wang-Fm.: Brekzie | Wang-Fm.: Brekzie     |
|15202300 | Schrattenkalk-Fm.: Oberer Teil | Schrattenkalk-Fm.: Oberer Teil     |
|15202301 | Schrattenkalk-Fm.: Unterer Teil | Schrattenkalk-Fm.: Unterer Teil     |
|15202302 | Quinten-Fm.: Oberer Quintner Kalk | Quinten-Fm.: Oberer Quintner Kalk     |
|15202303 | Quinten-Fm.: Unterer Quintner Kalk | Quinten-Fm.: Unterer Quintner Kalk     |
|15202304 | Erzegg-Fm.: Planplatte-Eisenoolith | Erzegg-Fm.: Planplatte-Eisenoolith     |
|15202305 | Bommerstein-Fm.: Geissbach-Konglomerat | Bommerstein-Fm.: Geissbach-Konglomerat     |
|15202306 | Bommerstein-Fm.: Stöckli-Sandstein | Bommerstein-Fm.: Stöckli-Sandstein     |
|15202307 | Infrapräalpines Melange | Infrapräalpines Melange     |
|15202308 | Iberg-Melange | Iberg-Melange     |
|15202559 | Lötschental-Gneiskomplex: Migmatitischer Biotitgneis | Lötschental-Gneiskomplex: Migmatitischer Biotitgneis     |
|15202560 | Lötschental-Gneiskomplex: Chloritschiefer | Lötschental-Gneiskomplex: Chloritschiefer     |
|15202561 | Ofenhorn-Stampfhorn-Gneiskomplex: Gebänderter Biotitgneis | Ofenhorn-Stampfhorn-Gneiskomplex: Gebänderter Biotitgneis     |
|15202562 | Ofenhorn-Stampfhorn-Gneiskomplex: Migmatit | Ofenhorn-Stampfhorn-Gneiskomplex: Migmatit     |
|15202563 | Ofenhorn-Stampfhorn-Gneiskomplex: Biotitgneis | Ofenhorn-Stampfhorn-Gneiskomplex: Biotitgneis     |
|15202564 | Ofenhorn-Stampfhorn-Gneiskomplex: Orthogneis | Ofenhorn-Stampfhorn-Gneiskomplex: Orthogneis     |
|15202565 | Bäregg-Gneiskomplex: Mylonitischer Orthogneis | Bäregg-Gneiskomplex: Mylonitischer Orthogneis     |
|15202566 | Bäregg-Gneiskomplex: Mylonitischer Paragneis | Bäregg-Gneiskomplex: Mylonitischer Paragneis     |
|15202567 | Bäregg-Gneiskomplex: Metavulkanite | Bäregg-Gneiskomplex: Metavulkanite     |
|15202568 | Grimsel-Granodiorit: Aplitische Randfazies | Grimsel-Granodiorit: Aplitische Randfazies     |
|15202569 | Voralp-Granit: Saure Randfazies | Voralp-Granit: Saure Randfazies     |
|15202570 | Tamina-Gneiskomplex | Tamina-Gneiskomplex     |
|15202571 | Tamina-Gneiskomplex: Schiefriger Biotitgneis | Tamina-Gneiskomplex: Schiefriger Biotitgneis     |
|15202572 | Tamina-Gneiskomplex: Mylonit | Tamina-Gneiskomplex: Mylonit     |
|15202573 | Innertkirchen-Migmatit: Marmor | Innertkirchen-Migmatit: Marmor     |
|15202574 | Guttannen-Gneiskomplex: Migmatit | Guttannen-Gneiskomplex: Migmatit     |
|15202575 | Guttannen-Gneiskomplex: Amphibolit-reiche Fazies | Guttannen-Gneiskomplex: Amphibolit-reiche Fazies     |
|15200350 | Horw-Sandstein | Horw-Sandstein     |
|15200351 | UMM-II | UMM-II     |
|15200352 | Grisigen-Mergel | Grisigen-Mergel     |
|15200353 | UMM-I | UMM-I     |
|15200354 | Cucloz-Fm. | Cucloz-Fm.     |
|15200355 | Cucloz-Fm.: Cucloz-Sandstein | Cucloz-Fm.: Cucloz-Sandstein     |
|15200356 | Cucloz-Fm.: Marnes gris-souris | Cucloz-Fm.: Marnes gris-souris     |
|15200357 | Cucloz-Fm.: Schistes marno-micacés | Cucloz-Fm.: Schistes marno-micacés     |
|15200358 | Hilfern-Fm. | Hilfern-Fm.     |
|15200359 | Rietbad-Fm. | Rietbad-Fm.     |
|15200360 | Jordisboden-Mergel | Jordisboden-Mergel     |
|15200361 | Goldegg-Sandstein | Goldegg-Sandstein     |
|15200362 | UMM-J | UMM-J     |
|15200363 | UMM-J: Septarienton | UMM-J: Septarienton     |
|15200364 | UMM-J: Fischschiefer | UMM-J: Fischschiefer     |
|15200365 | UMM-J: Foraminiferenmergel | UMM-J: Foraminiferenmergel     |
|15200366 | UMM-J: Meeressand | UMM-J: Meeressand     |
|15200368 | UMM-J: Cyathulabank | UMM-J: Cyathulabank     |
|15200369 | UMM-J: Cyrenenmergel | UMM-J: Cyrenenmergel     |
|15200370 | Porrentruy-Konglomerat | Porrentruy-Konglomerat     |
|15200371 | Rossemaison-Fm.: Süsswasserkalk | Rossemaison-Fm.: Süsswasserkalk     |
|15202021 | Niederhorn-Fm.: Gemmenalp-Kalk | Niederhorn-Fm.: Gemmenalp-Kalk     |
|15202022 | Niederhorn-Fm.: Hohgant-Sandstein | Niederhorn-Fm.: Hohgant-Sandstein     |
|15202023 | Niederhorn-Fm.: Hohgant-Sandstein: Wagenmoos-Bk. | Niederhorn-Fm.: Hohgant-Sandstein: Wagenmoos-Bk.     |
|15202024 | Wildstrubel-Fm. | Wildstrubel-Fm.     |
|15202025 | Wildstrubel-Fm.: Schimberg-Mb. | Wildstrubel-Fm.: Schimberg-Mb.     |
|15202026 | Wildstrubel-Fm.: Tierberg-Mb. | Wildstrubel-Fm.: Tierberg-Mb.     |
|15202027 | Wildstrubel-Fm.: Küblibad-Mb. | Wildstrubel-Fm.: Küblibad-Mb.     |
|15202028 | Klimsenhorn-Fm. | Klimsenhorn-Fm.     |
|15202029 | Klimsenhorn-Fm.: Fruttli-Mb. | Klimsenhorn-Fm.: Fruttli-Mb.     |
|15202030 | Klimsenhorn-Fm.: Band-Mb. | Klimsenhorn-Fm.: Band-Mb.     |
|15202031 | Klimsenhorn-Fm.: Fräkmünt-Mb. | Klimsenhorn-Fm.: Fräkmünt-Mb.     |
|15202032 | Bürgen-Fm. | Bürgen-Fm.     |
|15202033 | Bürgen-Fm.: Foribach-Mb. | Bürgen-Fm.: Foribach-Mb.     |
|15202034 | Bürgen-Fm.: Mattgrat-Mb. | Bürgen-Fm.: Mattgrat-Mb.     |
|15202035 | Bürgen-Fm.: Scharti-Mb. | Bürgen-Fm.: Scharti-Mb.     |
|15202036 | Euthal-Fm. | Euthal-Fm.     |
|15202037 | Bürgen-Fm.: Steinbach-Mb. | Bürgen-Fm.: Steinbach-Mb.     |
|15202038 | Euthal-Fm.: Einsiedeln-Mb. | Euthal-Fm.: Einsiedeln-Mb.     |
|15202039 | Euthal-Fm.: Batöni-Mb. | Euthal-Fm.: Batöni-Mb.     |
|15202040 | Euthal-Fm.: Chruteren-Mb. | Euthal-Fm.: Chruteren-Mb.     |
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
|15202309 | Iberg-Melange: Surbrunnen-Flysch | Iberg-Melange: Surbrunnen-Flysch     |
|15202310 | Iberg-Melange: Roggenegg-Komplex | Iberg-Melange: Roggenegg-Komplex     |
|15202311 | Iberg-Melange: Isentobel-Komplex | Iberg-Melange: Isentobel-Komplex     |
|15202312 | Serhalten-Melange | Serhalten-Melange     |
|15202313 | Iberg-Melange: Gwürz-Flysch | Iberg-Melange: Gwürz-Flysch     |
|15202314 | Ruestel-Flysch | Ruestel-Flysch     |
|15202315 | Iberg-Melange: Scheidegg-Flysch | Iberg-Melange: Scheidegg-Flysch     |
|15202316 | Habkern-Granit | Habkern-Granit     |
|15202317 | Infrapräalpines Melange: Gros-Plané-Melange | Infrapräalpines Melange: Gros-Plané-Melange     |
|15202318 | Infrapräalpines Melange: Bodevena-Melange | Infrapräalpines Melange: Bodevena-Melange     |
|15202319 | Subalpiner Flysch | Subalpiner Flysch     |
|15202320 | Torrenthorn-Fm. | Torrenthorn-Fm.     |
|15202321 | Prodkamm-Fm.: Cardinien-Mb.: Weissgandstöckli-Bk. | Prodkamm-Fm.: Cardinien-Mb.: Weissgandstöckli-Bk.     |
|15202322 | Mären-Fm.: Grisch-Mb. | Mären-Fm.: Grisch-Mb.     |
|15202323 | Mären-Fm.: Foostock-Mb. | Mären-Fm.: Foostock-Mb.     |
|15202324 | Murgtal-Fm. | Murgtal-Fm.     |
|15202325 | Vernayaz-Fm.: Dzéman-Mb. | Vernayaz-Fm.: Dzéman-Mb.     |
|15202326 | Zentraler-Aare-Granit: Aplitische Randfazies | Zentraler-Aare-Granit: Aplitische Randfazies     |
|15202576 | Guttannen-Gneiskomplex: Aplitischer Granit | Guttannen-Gneiskomplex: Aplitischer Granit     |
|15202577 | Guttannen-Gneiskomplex: Marmor | Guttannen-Gneiskomplex: Marmor     |
|15202578 | Guttannen-Gneiskomplex: Ultramafisches Gestein | Guttannen-Gneiskomplex: Ultramafisches Gestein     |
|15202579 | Ofenhorn-Stampfhorn-Gneiskomplex: Schollenamphibolit-reiche Fazies | Ofenhorn-Stampfhorn-Gneiskomplex: Schollenamphibolit-reiche Fazies     |
|15202580 | Ofenhorn-Stampfhorn-Gneiskomplex: Aplitischer Granit | Ofenhorn-Stampfhorn-Gneiskomplex: Aplitischer Granit     |
|15202581 | Ofenhorn-Stampfhorn-Gneiskomplex: Schollenamphibolit | Ofenhorn-Stampfhorn-Gneiskomplex: Schollenamphibolit     |
|15202582 | Ofenhorn-Stampfhorn-Gneiskomplex: Ultramafisches Gestein | Ofenhorn-Stampfhorn-Gneiskomplex: Ultramafisches Gestein     |
|15202583 | Bommerstein- und Reischiben-Fm. | Bommerstein- und Reischiben-Fm.     |
|15202584 | Mels- und Röti-Fm. | Mels- und Röti-Fm.     |
|15202585 | Guttannen-Gneiskomplex: Schierfriger Biotit-Chlorit-Serizit-Gneis | Guttannen-Gneiskomplex: Schierfriger Biotit-Chlorit-Serizit-Gneis     |
|15202586 | Zettenalp-Trochematt-Melange | Zettenalp-Trochematt-Melange     |
|15202587 | Laubersmad-Flysch | Laubersmad-Flysch     |
|15202588 | Stad-Fm.: Quarzsandstein | Stad-Fm.: Quarzsandstein     |
|15202589 | Euthal-Fm.: Einsiedeln-Mb.: Quarzsandstein | Euthal-Fm.: Einsiedeln-Mb.: Quarzsandstein     |
|15202590 | Schrattenkalk-Fm.: vermergelt | Schrattenkalk-Fm.: vermergelt     |
|15202591 | Stad-Fm.: Wängen-Kalk: Lithothamnienkalk-Fazies | Stad-Fm.: Wängen-Kalk: Lithothamnienkalk-Fazies     |
|15200373 | Ajoie-Gompholit | Ajoie-Gompholit     |
|15200378 | Tüllingen-Süsswasserkalk | Tüllingen-Süsswasserkalk     |
|15200380 | Hauptogenstein: Oberer Teil | Hauptogenstein: Oberer Teil     |
|15200382 | Hauptogenstein: Unterer Teil | Hauptogenstein: Unterer Teil     |
|15200383 | Hauptrogenstein: Calcaire roux marneux | Hauptrogenstein: Calcaire roux marneux     |
|15200384 | Bois-de-Raube-Fm.: Ajoie-Mb. | Bois-de-Raube-Fm.: Ajoie-Mb.     |
|15200385 | Bois-de-Raube-Fm.: Bois-de-Raube-Mb. | Bois-de-Raube-Fm.: Bois-de-Raube-Mb.     |
|15200386 | Bois-de-Raube-Fm.: Montchaibeux-Mb. | Bois-de-Raube-Fm.: Montchaibeux-Mb.     |
|15200387 | Daubrée-Konglomerat | Daubrée-Konglomerat     |
|15200388 | Wanderblock-Bildungen | Wanderblock-Bildungen     |
|15200389 | OMM-II: Geröllsande | OMM-II: Geröllsande     |
|15200390 | OMM-II: Polymikte Nagelfluh | OMM-II: Polymikte Nagelfluh     |
|15200391 | OMM-I: Muschelsandstein | OMM-I: Muschelsandstein     |
|15200392 | OMM-I: Graue Molasse | OMM-I: Graue Molasse     |
|15200393 | Daubrée-Konglomerat: Süsswasserkalk | Daubrée-Konglomerat: Süsswasserkalk     |
|15200394 | USM: Basale Süsswassermolasse | USM: Basale Süsswassermolasse     |
|15200395 | Laufen-Juranagelfluh | Laufen-Juranagelfluh     |
|15200396 | Basler Juranagelfluh | Basler Juranagelfluh     |
|15200397 | Aargauer Juranagelfluh | Aargauer Juranagelfluh     |
|15200399 | Jensberg-Fm. | Jensberg-Fm.     |
|15202041 | Euthal-Fm.: Fliegenspitz-Mb. | Euthal-Fm.: Fliegenspitz-Mb.     |
|15202043 | Siderolithikum: Grindelwald-Marmor | Siderolithikum: Grindelwald-Marmor     |
|15202044 | Niederhorn-Fm.: Hohgant-Sandstein: Mürren-Brekzie | Niederhorn-Fm.: Hohgant-Sandstein: Mürren-Brekzie     |
|15202045 | Siderolithikum: Dünden-Konglomerat | Siderolithikum: Dünden-Konglomerat     |
|15202046 | Siderolithikum: Rosenlaui-Marmor | Siderolithikum: Rosenlaui-Marmor     |
|15202047 | Helvetikum: Kreide | Helvetikum: Kreide     |
|15202048 | Wang-Fm. | Wang-Fm.     |
|15202049 | Amden-Fm. | Amden-Fm.     |
|15202050 | Seewen Fm. | Seewen Fm.     |
|15202051 | Seewen-Fm.: Choltal-Mb. | Seewen-Fm.: Choltal-Mb.     |
|15202052 | Garschella-Fm. | Garschella-Fm.     |
|15202053 | Garschella-Fm.: Selun-Mb. | Garschella-Fm.: Selun-Mb.     |
|15202054 | Garschella-Fm.: Selun-Mb.: Kamm-Bk. | Garschella-Fm.: Selun-Mb.: Kamm-Bk.     |
|15202055 | Garschella-Fm.: Selun-Mb.: Aubrig-Sch. | Garschella-Fm.: Selun-Mb.: Aubrig-Sch.     |
|15202056 | Garschella-Fm.: Selun-Mb.: Wannenalp-Bk. | Garschella-Fm.: Selun-Mb.: Wannenalp-Bk.     |
|15202057 | Garschella-Fm.: Selun-Mb.: Sellamatt-Sch. | Garschella-Fm.: Selun-Mb.: Sellamatt-Sch.     |
|15202058 | Garschella-Fm.: Selun-Mb.: Plattenwald-Bk. | Garschella-Fm.: Selun-Mb.: Plattenwald-Bk.     |
|15202059 | Garschella-Fm.: Selun-Mb.: Durschlägi-Bk. | Garschella-Fm.: Selun-Mb.: Durschlägi-Bk.     |
|15202060 | Garschella-Fm.: Selun-Mb.: Niederi-Sch. | Garschella-Fm.: Selun-Mb.: Niederi-Sch.     |
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
|15202327 | Windgällen-Fm.: Rhyolith | Windgällen-Fm.: Rhyolith     |
|15202328 | Bäregg-Gneiskomplex | Bäregg-Gneiskomplex     |
|15202329 | Gärsthorn-Gneiskomplex | Gärsthorn-Gneiskomplex     |
|15202330 | Sogn-Placi-Gneiskomplex | Sogn-Placi-Gneiskomplex     |
|15202331 | Massa-Gneiskomplex | Massa-Gneiskomplex     |
|15202332 | Aiguilles-Rouges-Massiv: Mittelvariszische Intrusiva | Aiguilles-Rouges-Massiv: Mittelvariszische Intrusiva     |
|15202333 | Aiguilles-Rouges-Massiv: Frühvariszische Intrusiva | Aiguilles-Rouges-Massiv: Frühvariszische Intrusiva     |
|15202334 | Aiguilles-Rouges-Massiv: Prävariszisches Grundgebirge | Aiguilles-Rouges-Massiv: Prävariszisches Grundgebirge     |
|15202335 | Chéserys-Gneis | Chéserys-Gneis     |
|15202336 | Mont-Blanc-Massiv: Spät- bis postvariszische Intrusiva | Mont-Blanc-Massiv: Spät- bis postvariszische Intrusiva     |
|15202337 | Mont-Blanc-Massiv: Prävariszisches Grundgebirge | Mont-Blanc-Massiv: Prävariszisches Grundgebirge     |
|15202338 | Alp-Cavradi-Gneiskomplex | Alp-Cavradi-Gneiskomplex     |
|15202339 | Giubine-Gneiskomplex | Giubine-Gneiskomplex     |
|15202340 | Gotthardt-Decke: Prävariszisches polyzyklisches Grundgebirge | Gotthardt-Decke: Prävariszisches polyzyklisches Grundgebirge     |
|15202341 | Goms-Gneiskomplex: Unterwassern-Gneis | Goms-Gneiskomplex: Unterwassern-Gneis     |
|15202343 | Streifengneis-Komplex: Sassina-Augengneis | Streifengneis-Komplex: Sassina-Augengneis     |
|15202344 | Streifengneis-Komplex: Alp-Ramosa-Granitgneis | Streifengneis-Komplex: Alp-Ramosa-Granitgneis     |
|15202346 | Val-Nalps-Gneiskomplex | Val-Nalps-Gneiskomplex     |
|15202592 | Euthal-Fm.: Einsiedeln-Mb.: Alveolinenkalk-Fazies | Euthal-Fm.: Einsiedeln-Mb.: Alveolinenkalk-Fazies     |
|15202593 | Niederhorn-Fm.: Hohgant-Sandstein: Sandkalk und Kalk | Niederhorn-Fm.: Hohgant-Sandstein: Sandkalk und Kalk     |
|15202594 | Interne Einsiedeln-Schuppen: Tektonisches Melange | Interne Einsiedeln-Schuppen: Tektonisches Melange     |
|15202595 | Bürgen- und Wildstrubel-Fm. | Bürgen- und Wildstrubel-Fm.     |
|15202596 | Einsiedeln- und Steinbach-Mb. | Einsiedeln- und Steinbach-Mb.     |
|15202597 | Stad-Fm.: e6 | Stad-Fm.: e6     |
|15202598 | Stgir- und Inferno-Fm. | Stgir- und Inferno-Fm.     |
|15202599 | Quinten-Fm.: Oberer Quintner Kalk: Korallenkalk | Quinten-Fm.: Oberer Quintner Kalk: Korallenkalk     |
|15202600 | Quinten-Fm.: Oberer Quintner Kalk: Unterer Kalk | Quinten-Fm.: Oberer Quintner Kalk: Unterer Kalk     |
|15202601 | Prodkamm- bis Sexmor-Fm. | Prodkamm- bis Sexmor-Fm.     |
|15202602 | Plattenzüg-Fm. | Plattenzüg-Fm.     |
|15202603 | Zemenstein- bis Garschella Fm. | Zemenstein- bis Garschella Fm.     |
|15202604 | Euthal-Fm.: Vasanachopf-Mb | Euthal-Fm.: Vasanachopf-Mb     |
|15202605 | Pfäfers-Fm. | Pfäfers-Fm.     |
|15202606 | Euthal- und Bürgen-Fm. | Euthal- und Bürgen-Fm.     |
|15202607 | Amden- und Wang-Fm. | Amden- und Wang-Fm.     |
|15202608 | Seewen- und Amden-Fm. | Seewen- und Amden-Fm.     |
|15202609 | Betlis- bis Schrattenkalk-Fm. | Betlis- bis Schrattenkalk-Fm.     |
|15200400 | Jensberg-Fm.: Rebhubel-Sch. | Jensberg-Fm.: Rebhubel-Sch.     |
|15200401 | Niedermatt-Fm. | Niedermatt-Fm.     |
|15200402 | Belpberg-Fm. | Belpberg-Fm.     |
|15200403 | Kalchstätten-Fm.: Pfadflüe-Nagelfluh | Kalchstätten-Fm.: Pfadflüe-Nagelfluh     |
|15200404 | Belpberg-Fm.: Sädel-Kalknagelfluh | Belpberg-Fm.: Sädel-Kalknagelfluh     |
|15200405 | Belpberg-Fm.: Utzigen-Muschelsandstein | Belpberg-Fm.: Utzigen-Muschelsandstein     |
|15200406 | Belpberg-Fm.: Ulmiz-Quarzitnagelfluh | Belpberg-Fm.: Ulmiz-Quarzitnagelfluh     |
|15200407 | Belpberg-Fm.: Bütschelbach-Nagelfluh | Belpberg-Fm.: Bütschelbach-Nagelfluh     |
|15200408 | Kalchstätten-Fm. | Kalchstätten-Fm.     |
|15200409 | St.-Gallen-Fm.: Freudenberg-Nagelfluh | St.-Gallen-Fm.: Freudenberg-Nagelfluh     |
|15200410 | St.-Gallen-Fm.: Goldbrunnen-Sch. | St.-Gallen-Fm.: Goldbrunnen-Sch.     |
|15200411 | St.-Gallen-Fm.: Dreilinden-Nagelfluh | St.-Gallen-Fm.: Dreilinden-Nagelfluh     |
|15200412 | St.-Gallen-Fm.: Obere Grenznagelfluh | St.-Gallen-Fm.: Obere Grenznagelfluh     |
|15200413 | Kirchberg-Fm. | Kirchberg-Fm.     |
|15200414 | Grimmelfingen-Fm. | Grimmelfingen-Fm.     |
|15200415 | Chnebelburg-Fm. | Chnebelburg-Fm.     |
|15200416 | Chnebelburg-Fm.: Meinisberg-Muschelsandstein | Chnebelburg-Fm.: Meinisberg-Muschelsandstein     |
|15200417 | Chnebelburg-Fm.: Brüttelen-Grobsandstein | Chnebelburg-Fm.: Brüttelen-Grobsandstein     |
|15200418 | Sense-Fm. | Sense-Fm.     |
|15202061 | Garschella-Fm.: Selun-Mb.: Twäriberg-Bk. | Garschella-Fm.: Selun-Mb.: Twäriberg-Bk.     |
|15202062 | Garschella-Fm.: Selun-Mb.: Klaus-Bk. | Garschella-Fm.: Selun-Mb.: Klaus-Bk.     |
|15202063 | Garschella-Fm.: Rankweil-Mb. | Garschella-Fm.: Rankweil-Mb.     |
|15202064 | Garschella-Fm.: Brisi-Mb. | Garschella-Fm.: Brisi-Mb.     |
|15202065 | Garschella-Fm.: Brisi-Mb.: Kalkige Fazies | Garschella-Fm.: Brisi-Mb.: Kalkige Fazies     |
|15202066 | Garschella-Fm.: Brisi-Mb.: Sandige Fazies | Garschella-Fm.: Brisi-Mb.: Sandige Fazies     |
|15202067 | Garschella-Fm.: Brisi-Mb.: Gams-Sch. | Garschella-Fm.: Brisi-Mb.: Gams-Sch.     |
|15202068 | Garschella-Fm.: Brisi-Mb.: Luitere-Bk. | Garschella-Fm.: Brisi-Mb.: Luitere-Bk.     |
|15202069 | Garschella-Fm.: Freschen-Mb. | Garschella-Fm.: Freschen-Mb.     |
|15202070 | Garschella-Fm.: Freschen-Mb.: Hochkugel-Sch. | Garschella-Fm.: Freschen-Mb.: Hochkugel-Sch.     |
|15202071 | Garschella-Fm.: Grünten-Mb. | Garschella-Fm.: Grünten-Mb.     |
|15202072 | Garschella-Fm.: Grünten-Mb.: Rohrbachstein-Bk. | Garschella-Fm.: Grünten-Mb.: Rohrbachstein-Bk.     |
|15202073 | Schrattenkalk-Fm. | Schrattenkalk-Fm.     |
|15202074 | Schrattenkalk-Fm.: Rawil-Mb. | Schrattenkalk-Fm.: Rawil-Mb.     |
|15202075 | Tierwis-Fm. | Tierwis-Fm.     |
|15202076 | Tierwis-Fm.: Chopf-Bk. | Tierwis-Fm.: Chopf-Bk.     |
|15202077 | Tierwis-Fm.: Drusberg-Mb. | Tierwis-Fm.: Drusberg-Mb.     |
|15202078 | Tierwis-Fm.: Altmann-Mb. | Tierwis-Fm.: Altmann-Mb.     |
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
|15200419 | Sense-Fm.: Montécu-Sch. | Sense-Fm.: Montécu-Sch.     |
|15200420 | Sense-Fm.: Molière-Muschelsandstein | Sense-Fm.: Molière-Muschelsandstein     |
|15200421 | Sense-Fm.: Scherli-Nagelfluh | Sense-Fm.: Scherli-Nagelfluh     |
|15200422 | Grilly-Süsswasserkalk | Grilly-Süsswasserkalk     |
|15200423 | Orbe-Süsswasserkalk | Orbe-Süsswasserkalk     |
|15200424 | USM: Basale Süsswassermolasse: Krustenkalk | USM: Basale Süsswassermolasse: Krustenkalk     |
|15200425 | Gümmenen-Fm. | Gümmenen-Fm.     |
|15200429 | USM-II: Obere Bunte Molasse | USM-II: Obere Bunte Molasse     |
|15200430 | Oberdorf-Süsswasserkalk | Oberdorf-Süsswasserkalk     |
|15200431 | St.-Gallen-Fm.: Limnischer Horizont | St.-Gallen-Fm.: Limnischer Horizont     |
|15200432 | OMM-II: Quarzitnagelfluh | OMM-II: Quarzitnagelfluh     |
|15200433 | Luzern-Fm.: Basales Konglomerat | Luzern-Fm.: Basales Konglomerat     |
|15200436 | Perte-du-Rhône-Fm.: Poncin-Mb. | Perte-du-Rhône-Fm.: Poncin-Mb.     |
|15200437 | Perte-du-Rhône-Fm.: Mussel-Mb.: Vraconne-Sandstein | Perte-du-Rhône-Fm.: Mussel-Mb.: Vraconne-Sandstein     |
|15200438 | Perte-du-Rhône-Fm.: Mussel-Mb.: La-Presta-Mergel | Perte-du-Rhône-Fm.: Mussel-Mb.: La-Presta-Mergel     |
|15200439 | Perte-du-Rhône-Fm.: Mussel-Mb.: Vernettes-Sandstein | Perte-du-Rhône-Fm.: Mussel-Mb.: Vernettes-Sandstein     |
|15200440 | Perte-du-Rhône-Fm.: Mussel-Mb.: Ponthoud-Bk. | Perte-du-Rhône-Fm.: Mussel-Mb.: Ponthoud-Bk.     |
|15200441 | Perte-du-Rhône-Fm.: Mussel-Mb.: Scie-Besse-Sandstein | Perte-du-Rhône-Fm.: Mussel-Mb.: Scie-Besse-Sandstein     |
|15200442 | Perte-du-Rhône-Fm.: Fulie-Mb.: Mortier-Mergel | Perte-du-Rhône-Fm.: Fulie-Mb.: Mortier-Mergel     |
|15200443 | Perte-du-Rhône-Fm.: Fulie-Mb.: Vauglène-Bk. | Perte-du-Rhône-Fm.: Fulie-Mb.: Vauglène-Bk.     |
|15202079 | Helvetischer Kieselkalk | Helvetischer Kieselkalk     |
|15202080 | Helvetischer Kieselkalk: Chriesiloch-Echinodermenkalk | Helvetischer Kieselkalk: Chriesiloch-Echinodermenkalk     |
|15202081 | Helvetischer Kieselkalk: Lidernen-Mb. | Helvetischer Kieselkalk: Lidernen-Mb.     |
|15202082 | Helvetischer Kieselkalk: Gemsmättli-Bk. | Helvetischer Kieselkalk: Gemsmättli-Bk.     |
|15202083 | Helvetischer Kieselkalk: Rahberg-Bk. | Helvetischer Kieselkalk: Rahberg-Bk.     |
|15202084 | Betlis-Fm. | Betlis-Fm.     |
|15202085 | Betlis-Fm.: Pygurus-Mb. | Betlis-Fm.: Pygurus-Mb.     |
|15202086 | Betlis-Fm.: Spitzern-Mb. | Betlis-Fm.: Spitzern-Mb.     |
|15202087 | Betlis-Fm.: Büls-Bk. | Betlis-Fm.: Büls-Bk.     |
|15202088 | Sichel-Kalk | Sichel-Kalk     |
|15202089 | Diphyoides-Kalk | Diphyoides-Kalk     |
|15202090 | Vitznau-Mergel | Vitznau-Mergel     |
|15202091 | Öhrli-Fm. | Öhrli-Fm.     |
|15202092 | Palfris-Fm. | Palfris-Fm.     |
|15202093 | Zementstein-Fm. | Zementstein-Fm.     |
|15202094 | Zementstein-Fm.: Grasspass-Mb. | Zementstein-Fm.: Grasspass-Mb.     |
|15202095 | Zementstein-Fm.: Gassen-Kalk | Zementstein-Fm.: Gassen-Kalk     |
|15202096 | Helvetikum: Malm | Helvetikum: Malm     |
|15202097 | Quinten-Fm. | Quinten-Fm.     |
|15202098 | Quinten-Fm.: Tros-Kalk | Quinten-Fm.: Tros-Kalk     |
|15202347 | Val-Nalps-Gneiskomplex: Prato-Gneis | Val-Nalps-Gneiskomplex: Prato-Gneis     |
|15202348 | Val-Nalps-Gneiskomplex: Distelgrat-Gneis | Val-Nalps-Gneiskomplex: Distelgrat-Gneis     |
|15202349 | Paradis-Gneiskomplex: Val-Gronda-Augengneis | Paradis-Gneiskomplex: Val-Gronda-Augengneis     |
|15202350 | Val-Nalps-Gneiskomplex: Fuorcla-Paradis-Serpentinit | Val-Nalps-Gneiskomplex: Fuorcla-Paradis-Serpentinit     |
|15202351 | Paradis-Gneiskomplex | Paradis-Gneiskomplex     |
|15202352 | Paradis-Gneiskomplex: Oberstafel-Gneis | Paradis-Gneiskomplex: Oberstafel-Gneis     |
|15202353 | Paradis-Gneiskomplex: Ganneretsch-Gneis | Paradis-Gneiskomplex: Ganneretsch-Gneis     |
|15202354 | Paradis-Gneiskomplex: Corandoni-Amphibolit | Paradis-Gneiskomplex: Corandoni-Amphibolit     |
|15202355 | Tavetsch-Decke: Prävariszisches polyzyklisches Grundgebirge | Tavetsch-Decke: Prävariszisches polyzyklisches Grundgebirge     |
|15202356 | Rueras-Gneiskomplex | Rueras-Gneiskomplex     |
|15202357 | Aiguilles-Rouges-Massiv: Prä- und frühvariszische Sedimente und Vulkanite | Aiguilles-Rouges-Massiv: Prä- und frühvariszische Sedimente und Vulkanite     |
|15202358 | Vernayaz-Fm.: Salvan-Mb.: Au-d&#39;Arbignon-Schiefer | Vernayaz-Fm.: Salvan-Mb.: Au-d&#39;Arbignon-Schiefer     |
|15202359 | Vernayaz-Fm.: Salvan-Mb.: Dorénaz-Konglomerat | Vernayaz-Fm.: Salvan-Mb.: Dorénaz-Konglomerat     |
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
|15200444 | Perte-du-Rhône-Fm.: Fulie-Mb.: Poet-Bk. | Perte-du-Rhône-Fm.: Fulie-Mb.: Poet-Bk.     |
|15200445 | Rossemaison-Fm.: Courcelon-Süsswasserkalk | Rossemaison-Fm.: Courcelon-Süsswasserkalk     |
|15200446 | Erzmatt-Krustenkalk | Erzmatt-Krustenkalk     |
|15200447 | Diegten-Süsswasserkalk | Diegten-Süsswasserkalk     |
|15200448 | La-Verrerie-Süsswasserkalk | La-Verrerie-Süsswasserkalk     |
|15200449 | La-Charrue-Süsswasserkalk | La-Charrue-Süsswasserkalk     |
|15200450 | Vuache-Fm.: Astieria-Mergel | Vuache-Fm.: Astieria-Mergel     |
|15200451 | Vuache-Fm.: Villers-Sch. | Vuache-Fm.: Villers-Sch.     |
|15200452 | Pierre-Châtel-Fm.: Unité Moyenne Calcaire | Pierre-Châtel-Fm.: Unité Moyenne Calcaire     |
|15200453 | Pierre-Châtel-Fm.: Unité Inférieure Oolithique | Pierre-Châtel-Fm.: Unité Inférieure Oolithique     |
|15200456 | Etiollets-Fm.: Complexe récifal: Landaize-Kalk | Etiollets-Fm.: Complexe récifal: Landaize-Kalk     |
|15200457 | Balsthal-Fm.: Holzflue-Mb.: Balmberg-Oolith | Balsthal-Fm.: Holzflue-Mb.: Balmberg-Oolith     |
|15200458 | Balsthal-Fm.: Laufen-Mb.: Hautes-Roches-Algenkalk | Balsthal-Fm.: Laufen-Mb.: Hautes-Roches-Algenkalk     |
|15200459 | Balsthal-Fm.: Laufen-Mb.: Akzessorische Mumienbänke | Balsthal-Fm.: Laufen-Mb.: Akzessorische Mumienbänke     |
|15200460 | Vellerat-Fm.: Röschenz-Mb.: Brauner Oolith | Vellerat-Fm.: Röschenz-Mb.: Brauner Oolith     |
|15200461 | Kaiseraugst-Fm.: Wellendolomit: Bleiglanz-Bk. | Kaiseraugst-Fm.: Wellendolomit: Bleiglanz-Bk.     |
|15200462 | Dinkelberg-Fm.: Rötton: Arenicolites-Bk. | Dinkelberg-Fm.: Rötton: Arenicolites-Bk.     |
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
|15203001 | Niesen-Decke: Flysch | Niesen-Decke: Flysch     |
|15203002 | Chesselbach-Fm. | Chesselbach-Fm.     |
|15203003 | Seron-Fm. | Seron-Fm.     |
|15203004 | Niesenkulm-Fm. | Niesenkulm-Fm.     |
|15203005 | Frutigen-Fm. | Frutigen-Fm.     |
|15203006 | Grande-Eau-Fm. | Grande-Eau-Fm.     |
|15203007 | Grande-Eau-Fm.: Langy-Mb. | Grande-Eau-Fm.: Langy-Mb.     |
|15203008 | Grande-Eau-Fm.: Forclaz-Mb. | Grande-Eau-Fm.: Forclaz-Mb.     |
|15203009 | Grande-Eau-Fm.: Grès de Passage | Grande-Eau-Fm.: Grès de Passage     |
|15203010 | Grande-Eau-Fm.: Leyderry-Mb. | Grande-Eau-Fm.: Leyderry-Mb.     |
|15203011 | Grande-Eau-Fm.: Raverette-Mb. | Grande-Eau-Fm.: Raverette-Mb.     |
|15203012 | Grande-Eau-Fm.: Schistes à miches | Grande-Eau-Fm.: Schistes à miches     |
|15203013 | Murgaz-Kalk | Murgaz-Kalk     |
|15203014 | Niesen-Decke: Trias | Niesen-Decke: Trias     |
|15203015 | Chlussli-Fm. | Chlussli-Fm.     |
|15200463 | Dinkelberg-Fm.: Diagonalschichtiger Sandstein | Dinkelberg-Fm.: Diagonalschichtiger Sandstein     |
|15200464 | Schinznach-Fm.: Leutschenberg-Mb. | Schinznach-Fm.: Leutschenberg-Mb.     |
|15200465 | Schlächtenhaus-Granit | Schlächtenhaus-Granit     |
|15200466 | Steinatal-Gneiskomplex | Steinatal-Gneiskomplex     |
|15200467 | Schinznach-Fm.: Asp-Mb.: Grenzdolomit | Schinznach-Fm.: Asp-Mb.: Grenzdolomit     |
|15200468 | Schinznach-Fm.: Asp-Mb.: Estherien-Sch. | Schinznach-Fm.: Asp-Mb.: Estherien-Sch.     |
|15200469 | Hangende-Bankkalke-Fm. | Hangende-Bankkalke-Fm.     |
|15200470 | Zementmergel-Fm. | Zementmergel-Fm.     |
|15200471 | Liegende-Bankkalke-Fm. | Liegende-Bankkalke-Fm.     |
|15200472 | Obere-Felsenkalke-Fm. | Obere-Felsenkalke-Fm.     |
|15200473 | Untere-Felsenkalke-Fm. | Untere-Felsenkalke-Fm.     |
|15200474 | Lacunosamergel-Fm. | Lacunosamergel-Fm.     |
|15200475 | Oberjura-Massenkalk-Fm. | Oberjura-Massenkalk-Fm.     |
|15200476 | Oberjura-Massenkalk-Fm.: Lochen-Sbf. | Oberjura-Massenkalk-Fm.: Lochen-Sbf.     |
|15200477 | Wohlgeschichtete-Kalke-Fm. | Wohlgeschichtete-Kalke-Fm.     |
|15200478 | Impressamergel-Fm. | Impressamergel-Fm.     |
|15200479 | Ornatenton-Fm. | Ornatenton-Fm.     |
|15200480 | Ornatenton-Fm.: Glaukonitsandmergel-Sbf. | Ornatenton-Fm.: Glaukonitsandmergel-Sbf.     |
|15200481 | Ornatenton-Fm.: Glaukonitsandmergel-Sbf.: Grenzkalk | Ornatenton-Fm.: Glaukonitsandmergel-Sbf.: Grenzkalk     |
|15202099 | Quinten-Fm.: Mergelband | Quinten-Fm.: Mergelband     |
|15202100 | Schilt-Fm. | Schilt-Fm.     |
|15202101 | Schilt-Fm.: Mürtschen-Mb. | Schilt-Fm.: Mürtschen-Mb.     |
|15202102 | Schilt-Fm.: Mergelstein-dominierte Fazies | Schilt-Fm.: Mergelstein-dominierte Fazies     |
|15202103 | Schilt-Fm.: Kalkstein-dominierte Fazies | Schilt-Fm.: Kalkstein-dominierte Fazies     |
|15202104 | Schilt-Fm.: Seeztal-Mb. | Schilt-Fm.: Seeztal-Mb.     |
|15202105 | Schilt-Fm.: Windgällen-Mb. | Schilt-Fm.: Windgällen-Mb.     |
|15202106 | Helvetikum: Dogger | Helvetikum: Dogger     |
|15202107 | Erzegg-Fm. | Erzegg-Fm.     |
|15202108 | Reischiben-Fm. | Reischiben-Fm.     |
|15202109 | Reischiben-Fm.: Blegi-Eisenoolith | Reischiben-Fm.: Blegi-Eisenoolith     |
|15202110 | Reischiben-Fm.: Bannalp-Konglomerat | Reischiben-Fm.: Bannalp-Konglomerat     |
|15202111 | Reischiben-Fm.: Guppen-Fossilhorizont | Reischiben-Fm.: Guppen-Fossilhorizont     |
|15202112 | Reischiben-Fm.: Gursbach-Fossilhorizont | Reischiben-Fm.: Gursbach-Fossilhorizont     |
|15202113 | Hochstollen-Fm. | Hochstollen-Fm.     |
|15202114 | Hochstollen-Fm.: Schwarzhorn-Mb. | Hochstollen-Fm.: Schwarzhorn-Mb.     |
|15202115 | Hochstollen-Fm.: Bietenhorn-Mb. | Hochstollen-Fm.: Bietenhorn-Mb.     |
|15202116 | Bommerstein-Fm. | Bommerstein-Fm.     |
|15202117 | Bommerstein-Fm.: Mols-Mb. | Bommerstein-Fm.: Mols-Mb.     |
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
|15202394 | Stad-Fm.: Spirstock-Mb. | Stad-Fm.: Spirstock-Mb.     |
|15202395 | Seewen-Fm.: Roter-Seewer-Kalk | Seewen-Fm.: Roter-Seewer-Kalk     |
|15202396 | Seewen-Fm.: Untere Götzis-Bk. | Seewen-Fm.: Untere Götzis-Bk.     |
|15202397 | Garschella-Fm.: Grünten-Mb.: Col-de-la-Plaine-Morte-Bk. | Garschella-Fm.: Grünten-Mb.: Col-de-la-Plaine-Morte-Bk.     |
|15202398 | Betlis-Fm.: Oberer Teil | Betlis-Fm.: Oberer Teil     |
|15202399 | Betlis-Fm.: Unterer Teil | Betlis-Fm.: Unterer Teil     |
|15202400 | Bommerstein-Fm.: Vättis-Brekzie | Bommerstein-Fm.: Vättis-Brekzie     |
|15203016 | Coulaytes-Melange | Coulaytes-Melange     |
|15203017 | Cuvigne-Derrey-Fm. | Cuvigne-Derrey-Fm.     |
|15203018 | Couches-Rouges | Couches-Rouges     |
|15203019 | Chenaux-Rouges-Fm. | Chenaux-Rouges-Fm.     |
|15203020 | Chenaux-Rouges-Fm.: Hochmatt-Kalkarenit | Chenaux-Rouges-Fm.: Hochmatt-Kalkarenit     |
|15203021 | Chenaux-Rouges-Fm.: Chenaux-Rouges-Mineralkruste | Chenaux-Rouges-Fm.: Chenaux-Rouges-Mineralkruste     |
|15203022 | Forclettes-Fm. | Forclettes-Fm.     |
|15203023 | Forclettes-Fm.: Roter-Sattel-Hartgrund | Forclettes-Fm.: Roter-Sattel-Hartgrund     |
|15203024 | Forclettes-Fm.: Beaumont-Konglomerat | Forclettes-Fm.: Beaumont-Konglomerat     |
|15203025 | Forclettes-Fm.: Rayes-Kalk | Forclettes-Fm.: Rayes-Kalk     |
|15203026 | Forclettes-Fm.: Pissot-Mb. | Forclettes-Fm.: Pissot-Mb.     |
|15203027 | Rote-Platte-Fm. | Rote-Platte-Fm.     |
|15203028 | Rote-Platte-Fm.: Wildenbach-Mb. | Rote-Platte-Fm.: Wildenbach-Mb.     |
|15203029 | Rote-Platte-Fm.: Pra-du-Pont-Hartgrund | Rote-Platte-Fm.: Pra-du-Pont-Hartgrund     |
|15203030 | Rote-Platte-Fm.: Rontins-Mb. | Rote-Platte-Fm.: Rontins-Mb.     |
|15203031 | Rote-Platte-Fm.: Allières-Mb. | Rote-Platte-Fm.: Allières-Mb.     |
|15203032 | Rote-Platte-Fm.: Gérignoz-Kalk | Rote-Platte-Fm.: Gérignoz-Kalk     |
|15203033 | Rote-Platte-Fm.: Plagersflue-Kalkarenit | Rote-Platte-Fm.: Plagersflue-Kalkarenit     |
|15203034 | Intyamon-Fm. | Intyamon-Fm.     |
|15200482 | Ornatenton-Fm.: Macrocephalenoolith-Sbf. | Ornatenton-Fm.: Macrocephalenoolith-Sbf.     |
|15200483 | Wutach-Fm. | Wutach-Fm.     |
|15200484 | Variansmergel-Fm. | Variansmergel-Fm.     |
|15200485 | Dentalienton-Fm. | Dentalienton-Fm.     |
|15200486 | Hamitenton-Fm. | Hamitenton-Fm.     |
|15200487 | Hamitenton-Fm.: Parkinsonioolith-Sbf. | Hamitenton-Fm.: Parkinsonioolith-Sbf.     |
|15200488 | Gosheim-Fm. | Gosheim-Fm.     |
|15200489 | Gosheim-Fm.: Blagdeni-Sbf. | Gosheim-Fm.: Blagdeni-Sbf.     |
|15200490 | Gosheim-Fm.: Humphriesioolith-Sbf. | Gosheim-Fm.: Humphriesioolith-Sbf.     |
|15200491 | Wedelsandstein-Fm. | Wedelsandstein-Fm.     |
|15200492 | Wedelsandstein-Fm.: Blaukalk-Sbf. | Wedelsandstein-Fm.: Blaukalk-Sbf.     |
|15200493 | Murchisonaeoolith-Fm. | Murchisonaeoolith-Fm.     |
|15200494 | Achdorf-Fm. | Achdorf-Fm.     |
|15200495 | Tannenwald-Sch. | Tannenwald-Sch.     |
|15200496 | Schüpferegg-Nagelfluh: Gabelspitz-Sch. | Schüpferegg-Nagelfluh: Gabelspitz-Sch.     |
|15200497 | Schüpferegg-Nagelfluh: Schallenberg-Mergel | Schüpferegg-Nagelfluh: Schallenberg-Mergel     |
|15200498 | Schüpferegg-Nagelfluh: Seli-Nagelfluh | Schüpferegg-Nagelfluh: Seli-Nagelfluh     |
|15200499 | Brand-Herrentisch-Tuffit | Brand-Herrentisch-Tuffit     |
|15200500 | Wangen-Tuffit | Wangen-Tuffit     |
|15200501 | Hohenolber-Tuffit | Hohenolber-Tuffit     |
|15200502 | Eichbol-Tuffit | Eichbol-Tuffit     |
|15202118 | Dugny-Fm. | Dugny-Fm.     |
|15202119 | Coroi-Fm. | Coroi-Fm.     |
|15202120 | Helvetikum: Lias | Helvetikum: Lias     |
|15202121 | Brunnistock-Fm. | Brunnistock-Fm.     |
|15202122 | Inferno-Fm. | Inferno-Fm.     |
|15202123 | Monts-Rosset-Fm. | Monts-Rosset-Fm.     |
|15202124 | Torrenthorn-Fm.: Torrentalp-Mb. | Torrenthorn-Fm.: Torrentalp-Mb.     |
|15202125 | Sexmor-Fm. | Sexmor-Fm.     |
|15202126 | Mont-Joly-Fm. | Mont-Joly-Fm.     |
|15202127 | Torrenthorn-Fm.: Galm-Mb. | Torrenthorn-Fm.: Galm-Mb.     |
|15202128 | Spitzmeilen-Fm. | Spitzmeilen-Fm.     |
|15202129 | Tierces-Fm. | Tierces-Fm.     |
|15202130 | Bachalp-Fm. | Bachalp-Fm.     |
|15202131 | Prodkamm-Fm. | Prodkamm-Fm.     |
|15202132 | Prodkamm-Fm.: Cardinien-Mb. | Prodkamm-Fm.: Cardinien-Mb.     |
|15202133 | Stgir-Fm. | Stgir-Fm.     |
|15202134 | Helvetikum: Trias | Helvetikum: Trias     |
|15202135 | Besoëns-Fm. | Besoëns-Fm.     |
|15202136 | Quarten-Fm. | Quarten-Fm.     |
|15202137 | Arandellys-Fm. | Arandellys-Fm.     |
|15202138 | Arandellys-Fm.: Griaz-Mb. | Arandellys-Fm.: Griaz-Mb.     |
|15202139 | Röti-Fm. | Röti-Fm.     |
|15202401 | Inferno-Fm.: Oberer Teil | Inferno-Fm.: Oberer Teil     |
|15202402 | Inferno-Fm.: Mittlerer Teil | Inferno-Fm.: Mittlerer Teil     |
|15202403 | Inferno-Fm.: Unterer Teil | Inferno-Fm.: Unterer Teil     |
|15202404 | Sexmor-Fm.: Oberer Teil | Sexmor-Fm.: Oberer Teil     |
|15202405 | Sexmor-Fm.: Unterer Teil | Sexmor-Fm.: Unterer Teil     |
|15202406 | Prodkamm-Fm.: Unterer Teil: Leitoolith | Prodkamm-Fm.: Unterer Teil: Leitoolith     |
|15202411 | Stad-Fm.: Lochegg-Brekzie | Stad-Fm.: Lochegg-Brekzie     |
|15202412 | Zementstein-Fm.: Oberer Teil | Zementstein-Fm.: Oberer Teil     |
|15202413 | Zementstein-Fm.: Unterer Teil | Zementstein-Fm.: Unterer Teil     |
|15202414 | Bommerstein-Fm.: Glockhaus-Mb.: Roter Echinodermenkalk | Bommerstein-Fm.: Glockhaus-Mb.: Roter Echinodermenkalk     |
|15202415 | Bommerstein-Fm.: Glockhaus-Mb.: Obere Tonschiefer | Bommerstein-Fm.: Glockhaus-Mb.: Obere Tonschiefer     |
|15202416 | Bommerstein-Fm.: Glockhaus-Mb. | Bommerstein-Fm.: Glockhaus-Mb.     |
|15202417 | Coroi-Fm.: Basaler Quarzit | Coroi-Fm.: Basaler Quarzit     |
|15202418 | Röti-Fm.: Rauwacke | Röti-Fm.: Rauwacke     |
|15202419 | Vieux-Emosson-Fm.: Col-du-Jorat-Mb. | Vieux-Emosson-Fm.: Col-du-Jorat-Mb.     |
|15202420 | Quarten-Fm.: Equisetenschiefer | Quarten-Fm.: Equisetenschiefer     |
|15202421 | Amden-Fm.: Leist-Mergel | Amden-Fm.: Leist-Mergel     |
|15202422 | Amden Fm.: Leiboden-Mergel | Amden Fm.: Leiboden-Mergel     |
|15203035 | Intyamon-Fm.: Chällihorn-Mb. | Intyamon-Fm.: Chällihorn-Mb.     |
|15203036 | Intyamon-Fm.: Comba-d&#39;Avau-Mb. | Intyamon-Fm.: Comba-d&#39;Avau-Mb.     |
|15203037 | Intyamon-Fm.: Rodosex-Mb. | Intyamon-Fm.: Rodosex-Mb.     |
|15203038 | Sciernes-d&#39;Albeuve-Fm. | Sciernes-d&#39;Albeuve-Fm.     |
|15203039 | Moléson-Fm. | Moléson-Fm.     |
|15203040 | Torrent-de-Lessoc-Fm. | Torrent-de-Lessoc-Fm.     |
|15203041 | Staldengraben-Fm. | Staldengraben-Fm.     |
|15203042 | Staldengraben-Fm.: Col-de-Lys-Mb. | Staldengraben-Fm.: Col-de-Lys-Mb.     |
|15203043 | Staldengraben-Fm.: Vanil-Carré-Mb. | Staldengraben-Fm.: Vanil-Carré-Mb.     |
|15203044 | Staldengraben-Fm.: Verdy-Mb. | Staldengraben-Fm.: Verdy-Mb.     |
|15203045 | Staldengraben-Fm.: Soladier-Mb. | Staldengraben-Fm.: Soladier-Mb.     |
|15203046 | Sommant-Fm. | Sommant-Fm.     |
|15203047 | Rossinière-Fm. | Rossinière-Fm.     |
|15203048 | Heiti-Fm. | Heiti-Fm.     |
|15203049 | Combe-du-Pissot-Fm. | Combe-du-Pissot-Fm.     |
|15203050 | Combe-du-Pissot-Fm.: Chevalets-Mb. | Combe-du-Pissot-Fm.: Chevalets-Mb.     |
|15203051 | Combe-du-Pissot-Fm.: Creux-de-l&#39;Ours-Mb. | Combe-du-Pissot-Fm.: Creux-de-l&#39;Ours-Mb.     |
|15203052 | Petit-Liençon-Fm. | Petit-Liençon-Fm.     |
|15203053 | Arvel-Fm. | Arvel-Fm.     |
|15203054 | Grande-Bonavau-Fm. | Grande-Bonavau-Fm.     |









## Anhang  GC_CORRELATION_CD {#gc-correlation-cd}
Korrelation

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









## Anhang  GC_LITSTRAT_FORMATION_BANK_CD {#gc-litstrat-formation-bank-cd}
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









## Anhang  GC_LITSTRAT_UNCO_CD {#gc-litstrat-unco-cd}
Wertetabelle der lithostratigraphischen Einheiten

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15201001 | Ältere Ablagerungen, undifferenziert | Ältere Ablagerungen, undifferenziert     |
|15201002 | Niederterrasse | Niederterrasse     |
|15201003 | Hochterrasse | Hochterrasse     |
|15201004 | Tiefere Deckenschotter | Tiefere Deckenschotter     |
|15201005 | Höhere Deckenschotter | Höhere Deckenschotter     |
|15201006 | Birrfeld-Eiszeit (Letzte Eiszeit) | Birrfeld-Eiszeit (Letzte Eiszeit)     |
|15201007 | Last Glacial Maximum (LGM), undiff. | Last Glacial Maximum (LGM), undiff.     |
|15201008 | LGM-Rückzug | LGM-Rückzug     |
|15201009 | Birmenstorf-Vergletscherung (2. LGM-Vorstoss) | Birmenstorf-Vergletscherung (2. LGM-Vorstoss)     |
|15201010 | Wettingen-Vorstoss | Wettingen-Vorstoss     |
|15201011 | Flüefeld-Schotter | Flüefeld-Schotter     |
|15201012 | Altberg-Till | Altberg-Till     |
|15201013 | Birmenstorf-Vorstoss | Birmenstorf-Vorstoss     |
|15201014 | Birr-Schotter | Birr-Schotter     |
|15201015 | Oberhard-Till | Oberhard-Till     |
|15201016 | Seon-Vorstoss | Seon-Vorstoss     |
|15201017 | Berg-Schotter | Berg-Schotter     |
|15201018 | Fornholz-Till | Fornholz-Till     |
|15201019 | Gontenschwil-Vorstoss | Gontenschwil-Vorstoss     |
|15201020 | Gontenschwil-Till | Gontenschwil-Till     |
|15201021 | Staffelbach-Vorstoss | Staffelbach-Vorstoss     |
|15201022 | Staffelbach-Schotter | Staffelbach-Schotter     |
|15201023 | Staffelbach-Till | Staffelbach-Till     |
|15201024 | Lindmühle-Vergletscherung (1. LGM-Vorstoss) | Lindmühle-Vergletscherung (1. LGM-Vorstoss)     |
|15201025 | Otelfingen-Vorstoss | Otelfingen-Vorstoss     |
|15201026 | Tägerhard-Schotter | Tägerhard-Schotter     |
|15201027 | Lindmühle-Vorstoss | Lindmühle-Vorstoss     |
|15201028 | Ämmert-Schotter | Ämmert-Schotter     |
|15201029 | Ämmert-Till | Ämmert-Till     |
|15201030 | Emmet-Vorstoss | Emmet-Vorstoss     |
|15201031 | Gündelmoos-Lehm | Gündelmoos-Lehm     |
|15201032 | Igliste-Schotter | Igliste-Schotter     |
|15201033 | Niderholz-Till | Niderholz-Till     |
|15201034 | Zetzwil-Vorstoss | Zetzwil-Vorstoss     |
|15201035 | Zetzwil-Till | Zetzwil-Till     |
|15201036 | Kirchleerau-Vorstoss | Kirchleerau-Vorstoss     |
|15201037 | Kirchleerau-Till | Kirchleerau-Till     |
|15201038 | Gossau-Interstadial | Gossau-Interstadial     |
|15201039 | Mülligen-Paläoboden | Mülligen-Paläoboden     |
|15201040 | Niederweningen-Formation | Niederweningen-Formation     |
|15201041 | Hombrechtikon-Vergletscherung (Frühletzteiszeitliche Vergl.) | Hombrechtikon-Vergletscherung (Frühletzteiszeitliche Vergl.)     |
|15201042 | Mülligen-Schotter | Mülligen-Schotter     |
|15201043 | 2. letzteiszeitlischs Vorstoss | 2. letzteiszeitlischs Vorstoss     |
|15201044 | 1. letzteiszeitlischs Vorstoss | 1. letzteiszeitlischs Vorstoss     |
|15201045 | Klettgau-Schotter | Klettgau-Schotter     |
|15201046 | Obere Klettgauschotter | Obere Klettgauschotter     |
|15201047 | Glazi-lakustrische Serie | Glazi-lakustrische Serie     |
|15201048 | Mittlere Klettgauschotter | Mittlere Klettgauschotter     |
|15201049 | Untere Klettgauschotter | Untere Klettgauschotter     |
|15201050 | Gondiswil-Interglazial (Letztes Interglazial) | Gondiswil-Interglazial (Letztes Interglazial)     |
|15201051 | Flurlingen-Quelltuff | Flurlingen-Quelltuff     |
|15201052 | Birrfeld- und Klettgau-Paläoböden | Birrfeld- und Klettgau-Paläoböden     |
|15201053 | Beringen-Eiszeit | Beringen-Eiszeit     |
|15201054 | Entfelden-Schotter | Entfelden-Schotter     |
|15201055 | Aarau-Schotter | Aarau-Schotter     |
|15201056 | Suhr-Schotter | Suhr-Schotter     |
|15201057 | Veltheim-Schotter | Veltheim-Schotter     |
|15201058 | Stüsslingen-Schotter | Stüsslingen-Schotter     |
|15201059 | Langwiesen-Vergletscherung | Langwiesen-Vergletscherung     |
|15201060 | Langwiesen-Vorstoss | Langwiesen-Vorstoss     |
|15201061 | Schaffhausen-Schotter | Schaffhausen-Schotter     |
|15201062 | Reuenthal-Vorstoss | Reuenthal-Vorstoss     |
|15201063 | Lupfig-Schotter | Lupfig-Schotter     |
|15201064 | Löhningen-Engiwald-Vergletscherung | Löhningen-Engiwald-Vergletscherung     |
|15201065 | Engiwald-Vorstoss | Engiwald-Vorstoss     |
|15201066 | Rüfenach-Vorstoss | Rüfenach-Vorstoss     |
|15201067 | Löhningen-Vorstoss | Löhningen-Vorstoss     |
|15201068 | Remigen-Vorstoss | Remigen-Vorstoss     |
|15201069 | Remigen-Schotter | Remigen-Schotter     |
|15201070 | Meikirch-Interglazial | Meikirch-Interglazial     |
|15201071 | Ältere Beckenfüllungen | Ältere Beckenfüllungen     |
|15201072 | Hagenholz-Eiszeit | Hagenholz-Eiszeit     |
|15201073 | Hagenholz-Vergletscherung | Hagenholz-Vergletscherung     |
|15201074 | Hagenholz-Vorstoss | Hagenholz-Vorstoss     |
|15201075 | Aathal-Schotter | Aathal-Schotter     |
|15201076 | Pfyn-Vorstoss | Pfyn-Vorstoss     |
|15201077 | Ittingen-Schotter | Ittingen-Schotter     |
|15201078 | Ryhirt-Formation | Ryhirt-Formation     |
|15201079 | Geisslingen-Schotter | Geisslingen-Schotter     |
|15201080 | Habsburg-Hagenholz-Interglazial | Habsburg-Hagenholz-Interglazial     |
|15201081 | Möhlinerfeld-Paläoboden | Möhlinerfeld-Paläoboden     |
|15201082 | Habsburg-Eiszeit | Habsburg-Eiszeit     |
|15201083 | Gränichen-Schotter | Gränichen-Schotter     |
|15201084 | Roggehuse-Schotter | Roggehuse-Schotter     |
|15201085 | Buerfeld-Schotter | Buerfeld-Schotter     |
|15201086 | Habsburg-Vergletscherung | Habsburg-Vergletscherung     |
|15201087 | Habsburg-Vorstoss | Habsburg-Vorstoss     |
|15201088 | Habsburg-Schotter | Habsburg-Schotter     |
|15201089 | Unterschlatt-Vorstoss | Unterschlatt-Vorstoss     |
|15201090 | Thalgut-Interglazial | Thalgut-Interglazial     |
|15201091 | Möhlin-Eiszeit (Grösste Eiszeit) | Möhlin-Eiszeit (Grösste Eiszeit)     |
|15201092 | Möhlin-Vergletscherung | Möhlin-Vergletscherung     |
|15201093 | Möhlin-Vorstoss | Möhlin-Vorstoss     |
|15201094 | Bünten-Till | Bünten-Till     |
|15201095 | Schleitheim-Vorstoss | Schleitheim-Vorstoss     |
|15201096 | Fisibach-Schotter | Fisibach-Schotter     |
|15201097 | Bärengraben-Schotter und -Till | Bärengraben-Schotter und -Till     |
|15201098 | Iberig-Schotterkomplex | Iberig-Schotterkomplex     |
|15201099 | Obere Iberigschotter | Obere Iberigschotter     |
|15201100 | Oberer Till | Oberer Till     |
|15201101 | Mittlere Iberigschotter | Mittlere Iberigschotter     |
|15201102 | Untere Iberigschotter | Untere Iberigschotter     |
|15201103 | Unterer Till | Unterer Till     |
|15201104 | Wolfacher-Schotter und -Till | Wolfacher-Schotter und -Till     |
|15201105 | Fornech-Schotter | Fornech-Schotter     |
|15201106 | Forenirchel-Schotter | Forenirchel-Schotter     |
|15201107 | Steig-Schotter | Steig-Schotter     |
|15201108 | Irchel-Schotterkomplex | Irchel-Schotterkomplex     |
|15201109 | Obere Irchelschotter | Obere Irchelschotter     |
|15201111 | Irchel-Dolomitschotter | Irchel-Dolomitschotter     |
|15201112 | Mittlere Irchelschotter | Mittlere Irchelschotter     |
|15201113 | Untere Irchelschotter | Untere Irchelschotter     |
|15201114 | Langacher-Schotter | Langacher-Schotter     |
|15201115 | Dürn-Formation | Dürn-Formation     |
|15201116 | Degermoos-Schotter | Degermoos-Schotter     |
|15201117 | Ebnet-Schotter | Ebnet-Schotter     |
|15201118 | Wannen-Schotter | Wannen-Schotter     |
|15201119 | Egghalden-Schotter | Egghalden-Schotter     |
|15201120 | Buechen-Formation | Buechen-Formation     |
|15201121 | Feusi-Schotter | Feusi-Schotter     |
|15201122 | Lindenhau-Schotter | Lindenhau-Schotter     |
|15201123 | Egg-Schotter | Egg-Schotter     |
|15201124 | Sundgau-Schotter | Sundgau-Schotter     |
|15201125 | Mischschotter | Mischschotter     |
|15201126 | Weisse Serie | Weisse Serie     |
|15201129 | Zürich-Stein-Bremgarten-Stadien | Zürich-Stein-Bremgarten-Stadien     |
|15201130 | Untere Singen-Terrasse | Untere Singen-Terrasse     |
|15201131 | Schlieren-Diessenhofen-Stetten-Stadien | Schlieren-Diessenhofen-Stetten-Stadien     |
|15201132 | Obere Singen-Terrasse | Obere Singen-Terrasse     |
|15201133 | Rheinau-Terrasse | Rheinau-Terrasse     |
|15201134 | Nohl-Terrasse | Nohl-Terrasse     |
|15201135 | Altenburg-Fulach-Terrasse | Altenburg-Fulach-Terrasse     |
|15201136 | Aare-Schotter | Aare-Schotter     |
|15201137 | Schüss-Schotter | Schüss-Schotter     |
|15201138 | Orvin-Schotter | Orvin-Schotter     |
|15201139 | Seeablagerungen von Frinvillier und Rondchâtel | Seeablagerungen von Frinvillier und Rondchâtel     |
|15201140 | Stauschotter von Diessbach | Stauschotter von Diessbach     |
|15201141 | Mély-Formation | Mély-Formation     |
|15201142 | Kiessande von Madretsch | Kiessande von Madretsch     |
|15201143 | Seeland-Schotter | Seeland-Schotter     |
|15201144 | Emme-Schotter | Emme-Schotter     |
|15201145 | Gäu-Schotter | Gäu-Schotter     |
|15201146 | Flumenthal-Lehm | Flumenthal-Lehm     |
|15201147 | Killwangen-Schaffhausen-Mellingen-Stadium | Killwangen-Schaffhausen-Mellingen-Stadium     |
|15201148 | Munot-Terrasse | Munot-Terrasse     |
|15201149 | Stokar-Terrasse | Stokar-Terrasse     |
|15201150 | Breite-Terrasse | Breite-Terrasse     |
|15201151 | Maximalstand (Kilwangen-Schaffhausen-Stadium) | Maximalstand (Kilwangen-Schaffhausen-Stadium)     |
|15201152 | Wehntal-Schotter | Wehntal-Schotter     |
|15201153 | Bick-Till | Bick-Till     |
|15201154 | Flüe-Till | Flüe-Till     |
|15201155 | Wettingen-Schotter | Wettingen-Schotter     |
|15201156 | Bersturzmasse von Selzach | Bersturzmasse von Selzach     |
|15201157 | Plateauschotter | Plateauschotter     |
|15201158 | La-Côte-Schotter | La-Côte-Schotter     |
|15201159 | Enge-Schotter | Enge-Schotter     |
|15201160 | Attiswil-Schotter | Attiswil-Schotter     |
|15201161 | Lommiswil-Schotter | Lommiswil-Schotter     |
|15201162 | Oensingen-Moos-Lehm | Oensingen-Moos-Lehm     |
|15201163 | Berken-Schotter | Berken-Schotter     |
|15201164 | Berken-Sand | Berken-Sand     |
|15201165 | Schwarzhäusern-Lehm | Schwarzhäusern-Lehm     |
|15201166 | Käppelihof-Schotter | Käppelihof-Schotter     |
|15201167 | Aarburg-Schotter | Aarburg-Schotter     |
|15201168 | Tuileries-Formation | Tuileries-Formation     |
|15201169 | Grandson-Formation | Grandson-Formation     |
|15201170 | Poissine-Formation | Poissine-Formation     |
|15201171 | Surbtal-Lehm | Surbtal-Lehm     |
|15201172 | Surbtal-Till | Surbtal-Till     |
|15201173 | Surbtal-Schotter | Surbtal-Schotter     |
|15201174 | Fislisbach-Schotter | Fislisbach-Schotter     |
|15201175 | Reusstal-Sand | Reusstal-Sand     |
|15201176 | Reusstal-Lehm | Reusstal-Lehm     |
|15201177 | Hausen-Lehm | Hausen-Lehm     |
|15201178 | Hausen-Moräne | Hausen-Moräne     |
|15201179 | Ruckfeld-Schotter | Ruckfeld-Schotter     |
|15201180 | Endingen-Schotter | Endingen-Schotter     |
|15201181 | Rhein- und Aareschotter | Rhein- und Aareschotter     |
|15201182 | Juraschotter | Juraschotter     |
|15201183 | Alte Doubsschotter | Alte Doubsschotter     |
|15201184 | Wutach-Schotter | Wutach-Schotter     |
|15201185 | Merenbach-Schotter | Merenbach-Schotter     |
|15201186 | Malmkalk-Schotter der Randen-Täler | Malmkalk-Schotter der Randen-Täler     |
|15201187 | Solothurn-Stadium | Solothurn-Stadium     |
|15201188 | Münsingen-Schotterkomplex | Münsingen-Schotterkomplex     |
|15201189 | Alterswil-Schotter | Alterswil-Schotter     |
|15201190 | Karlsruhe-Schotter | Karlsruhe-Schotter     |
|15201191 | Chisetal-Schotter | Chisetal-Schotter     |
|15201192 | Grauholz-Schotter | Grauholz-Schotter     |
|15201193 | Trachslau-Schotter | Trachslau-Schotter     |
|15201194 | Bennau-Schotter | Bennau-Schotter     |
|15201195 | Hütten-Schotter | Hütten-Schotter     |
|15201196 | Schnabelsberg-Stauchotter | Schnabelsberg-Stauchotter     |
|15201197 | Einsiedeln-Lehm | Einsiedeln-Lehm     |
|15201198 | Willisau-Schotter | Willisau-Schotter     |
|15201199 | Wolhusen-Schotter | Wolhusen-Schotter     |
|15201200 | Wiggen-Schotter | Wiggen-Schotter     |
|15201201 | Menzingen-Schotter | Menzingen-Schotter     |
|15201202 | La-Tuffière-Schotter | La-Tuffière-Schotter     |
|15201203 | Gontenschwil-Lehm | Gontenschwil-Lehm     |
|15201204 | Mooslerau-Lehm | Mooslerau-Lehm     |
|15201205 | Triengen-Schotter | Triengen-Schotter     |
|15201206 | Triengen-Lehm | Triengen-Lehm     |
|15201207 | Sihl-Schotter | Sihl-Schotter     |
|15201208 | Haselbach-Schotter | Haselbach-Schotter     |
|15201209 | Jonen-Schotter | Jonen-Schotter     |
|15201210 | Aabach-Schotter | Aabach-Schotter     |
|15201211 | Starrberg-Schotter | Starrberg-Schotter     |
|15201212 | Port-Stauschotter | Port-Stauschotter     |
|15201213 | Rempen-Stauschotter | Rempen-Stauschotter     |
|15201214 | Dagmersellen-Vorstoss | Dagmersellen-Vorstoss     |
|15201215 | Oftringen-Schotter | Oftringen-Schotter     |
|15201216 | Zelg-Schotter | Zelg-Schotter     |
|15201217 | Forst-Schotter | Forst-Schotter     |
|15201218 | Raintal-Deltaschotter | Raintal-Deltaschotter     |
|15201219 | Kleinhöchstetten-Kies-Sand-Komplex | Kleinhöchstetten-Kies-Sand-Komplex     |
|15201220 | Krauchthal-Schotter | Krauchthal-Schotter     |
|15201221 | Brandflue-Schotter | Brandflue-Schotter     |
|15201222 | Küsnacht-Schotter | Küsnacht-Schotter     |
|15201223 | Chatzenstrick-Schotter | Chatzenstrick-Schotter     |
|15201224 | Rabennest-Schotter | Rabennest-Schotter     |
|15201225 | Ratengütsch-Schotter | Ratengütsch-Schotter     |
|15201226 | Scherenspitz-Schotter | Scherenspitz-Schotter     |
|15201227 | Walsenhaus-Schotter | Walsenhaus-Schotter     |
|15201228 | Richterswil-Seeton | Richterswil-Seeton     |
|15201229 | Schwanden-Schotter | Schwanden-Schotter     |
|15201230 | Reidbach-Schotter | Reidbach-Schotter     |
|15201231 | Zell-Schotterkomplex | Zell-Schotterkomplex     |
|15201232 | Gubel-Schotter | Gubel-Schotter     |
|15201233 | Chälen-Schotter | Chälen-Schotter     |
|15201234 | Chälen-Till | Chälen-Till     |
|15201235 | Sihlsprung-Schotter | Sihlsprung-Schotter     |
|15201236 | Kollbrunn-Schotter | Kollbrunn-Schotter     |
|15201237 | Walenberg-Schotter | Walenberg-Schotter     |
|15201238 | Ritteren-Schotterkomplex | Ritteren-Schotterkomplex     |
|15201239 | Vorholz-Schotter | Vorholz-Schotter     |
|15201240 | Gutsch-Schotter | Gutsch-Schotter     |
|15201241 | Junkerenwald-Schotter | Junkerenwald-Schotter     |
|15201242 | Chräjeloch-Schotter | Chräjeloch-Schotter     |
|15201243 | Butteberg-Schotter | Butteberg-Schotter     |
|15201244 | Höchi-Schotter | Höchi-Schotter     |
|15201245 | Heitere-Schotter | Heitere-Schotter     |
|15201246 | Holziken-Schotter | Holziken-Schotter     |
|15201247 | Ruedertal-Schotter | Ruedertal-Schotter     |
|15201248 | Bänkel-Schotter | Bänkel-Schotter     |
|15201249 | Quartär, undifferenziert | Quartär, undifferenziert     |
|15201250 | Deckenschotter, undifferenziert | Deckenschotter, undifferenziert     |
|15201251 | Girenbad-Schotter | Girenbad-Schotter     |
|15201252 | Sagenbach-Schotter | Sagenbach-Schotter     |
|15201253 | Schrotzburg-Schotter | Schrotzburg-Schotter     |
|15201254 | Schrotzburg-Till | Schrotzburg-Till     |
|15201255 | Bohlingen-Schotter | Bohlingen-Schotter     |
|15201256 | Bannholz-Schotter | Bannholz-Schotter     |
|15201257 | Hungerbol-Schotter | Hungerbol-Schotter     |
|15201258 | Chilchstapfen-Schotter | Chilchstapfen-Schotter     |
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
|15201286 | Bergsturzablagerungen von Sierre | Bergsturzablagerungen von Sierre     |
|15201287 | Bergsturzablagerungen von Chiètres | Bergsturzablagerungen von Chiètres     |
|15201288 | Bergsturzablagerungen von Chessel-Noville | Bergsturzablagerungen von Chessel-Noville     |
|15201289 | Bergsturzablagerungen von Novalles-Vugelles | Bergsturzablagerungen von Novalles-Vugelles     |
|15201290 | Bergsturzablagerungen von Gwelber-Laui-Weid | Bergsturzablagerungen von Gwelber-Laui-Weid     |
|15201291 | Bergsturzablagerungen von Castasegna | Bergsturzablagerungen von Castasegna     |
|15201292 | Bergsturzablagerungen von Sogno | Bergsturzablagerungen von Sogno     |
|15201293 | Bergsturzablagerungen von Prapan | Bergsturzablagerungen von Prapan     |
|15201294 | Bergsturzablagerungen von Schaingels | Bergsturzablagerungen von Schaingels     |
|15201295 | Bergsturzablagerungen von Mutta | Bergsturzablagerungen von Mutta     |
|15201296 | Bergsturzablagerungen von Brienz | Bergsturzablagerungen von Brienz     |
|15201297 | Bergsturzablagerungen von Flims | Bergsturzablagerungen von Flims     |
|15201298 | Bergsturzablagerungen von Brüsis | Bergsturzablagerungen von Brüsis     |
|15201299 | Bergsturzablagerungen vom Chapf | Bergsturzablagerungen vom Chapf     |
|15201300 | Bergsturzablagerungen von Derborence | Bergsturzablagerungen von Derborence     |
|15201301 | Bergsturzablagerungen vom Drussetschawald | Bergsturzablagerungen vom Drussetschawald     |
|15201302 | Bergsturzablagerungen vom Delenwald | Bergsturzablagerungen vom Delenwald     |
|15201303 | Bergsturzablagerungen von Elm | Bergsturzablagerungen von Elm     |
|15201304 | Bergsturzablagerungen von Goldau | Bergsturzablagerungen von Goldau     |
|15201305 | Bergsturzablagerungen von Iragell | Bergsturzablagerungen von Iragell     |
|15201306 | Bergsturzablagerungen vom Kernwald | Bergsturzablagerungen vom Kernwald     |
|15201307 | Bergsturzablagerungen von Triesenberg | Bergsturzablagerungen von Triesenberg     |
|15201308 | Bonaduz-Formation | Bonaduz-Formation     |
|15201309 | Bonfol-Ton | Bonfol-Ton     |
|15201310 | Bergsturzablagerungen von Tamins | Bergsturzablagerungen von Tamins     |
|15201311 | Informell benannte Bergsturzablagerungen | Informell benannte Bergsturzablagerungen     |
|15201312 | Informell benannte künstliche Ablagerungen | Informell benannte künstliche Ablagerungen     |
|15201313 | Künstliche Ablagerungen des Bahnhofs Brig | Künstliche Ablagerungen des Bahnhofs Brig     |
|15201314 | Künstliche Ablagerungen Golar | Künstliche Ablagerungen Golar     |
|15201315 | Künstliche Ablagerungen der Gamsenried-Deponie | Künstliche Ablagerungen der Gamsenried-Deponie     |
|15201316 | Künstliche Ablagerungen des Riedertals | Künstliche Ablagerungen des Riedertals     |
|15201317 | Informell benannte Sackungsmassen | Informell benannte Sackungsmassen     |
|15201318 | Sackungsmasse des Heinzenbergs | Sackungsmasse des Heinzenbergs     |
|15201319 | Informell benannte fluviatile Schotter | Informell benannte fluviatile Schotter     |
|15201320 | Schotter und Sand der Rhône | Schotter und Sand der Rhône     |
|15201321 | Schotter und Sand der Vispa | Schotter und Sand der Vispa     |
|15201322 | Informell benannter Bachschutt | Informell benannter Bachschutt     |
|15201323 | Bachschutt des Baltschiederbachs | Bachschutt des Baltschiederbachs     |
|15201324 | Bachschutt des Bietschbachs | Bachschutt des Bietschbachs     |
|15201325 | Bachschutt des Chelchbachs | Bachschutt des Chelchbachs     |
|15201326 | Bachschutt der Gamsa | Bachschutt der Gamsa     |
|15201327 | Bachschutt des Jolibachs | Bachschutt des Jolibachs     |
|15201328 | Bachschutt der Lonza | Bachschutt der Lonza     |
|15201329 | Bachschutt der Saltina | Bachschutt der Saltina     |
|15201330 | Bachschutt der Vispa | Bachschutt der Vispa     |
|15201331 | Bachschutt der Gürbe | Bachschutt der Gürbe     |
|15201332 | Bachschutt des Lombachs | Bachschutt des Lombachs     |
|15201333 | Pliozäne Ablagerungen | Pliozäne Ablagerungen     |
|15201334 | Stockesee-Sediment | Stockesee-Sediment     |
|15201335 | Strätligen-Till | Strätligen-Till     |
|15201336 | Bärenholz-Till | Bärenholz-Till     |
|15201337 | Wässerifluh-Formation | Wässerifluh-Formation     |
|15201338 | Schlyffi-Till | Schlyffi-Till     |
|15201339 | Brüggstutz-Schotter | Brüggstutz-Schotter     |
|15201340 | Guntelsei-Till | Guntelsei-Till     |
|15201341 | Guntelsei-Schotter | Guntelsei-Schotter     |
|15201342 | Steghalden-Schotter | Steghalden-Schotter     |
|15201343 | Glütschtal-Formation | Glütschtal-Formation     |
|15201344 | Hahni-Schotter | Hahni-Schotter     |
|15201444 | Löss, undifferenziert | Löss, undifferenziert     |
|15201458 | Ceppo | Ceppo     |
|15201459 | Novazzano-Sand | Novazzano-Sand     |
|15201460 | Bergsturzablagerungen vom Stützwald | Bergsturzablagerungen vom Stützwald     |
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
|15201526 | Wagenmoos-Till | Wagenmoos-Till     |
|15201527 | Niderstalden-Schotter | Niderstalden-Schotter     |
|15201528 | Zulgtal-Schotter | Zulgtal-Schotter     |
|15201529 | Spiez-Schotter | Spiez-Schotter     |
|15201530 | Hahni-Till | Hahni-Till     |
|15201531 | Bergsturzablagerung von Ralligen (im Thunersee) | Bergsturzablagerung von Ralligen (im Thunersee)     |
|15201532 | Bergsturzablagerung von Bargis | Bergsturzablagerung von Bargis     |
|15201533 | Bergsturzablagerung von Fidaz | Bergsturzablagerung von Fidaz     |
|15201534 | Niederterrassenschotter, tiefere Niveaus | Niederterrassenschotter, tiefere Niveaus     |
|15201535 | Niederterrassenschotter, zweitoberste Terrasse | Niederterrassenschotter, zweitoberste Terrasse     |
|15201536 | Niederterrassenschotter, oberste Terrasse | Niederterrassenschotter, oberste Terrasse     |
|15201537 | Tiefere Deckenschotter, unteres Niveau | Tiefere Deckenschotter, unteres Niveau     |
|15201538 | Tiefere Deckenschotter, oberes Niveau | Tiefere Deckenschotter, oberes Niveau     |
|15201539 | Kunkels-Formation | Kunkels-Formation     |
|15201540 | Alluvion von Ransun | Alluvion von Ransun     |
|15201541 | Rüdlingen-Till | Rüdlingen-Till     |
|15201542 | Niklaushalden-Formation | Niklaushalden-Formation     |
|15201543 | Stadel-Till | Stadel-Till     |
|15201544 | Volken-Lehm | Volken-Lehm     |
|15201545 | Rheinau-Till | Rheinau-Till     |
|15201546 | Ellikerholz-Formation | Ellikerholz-Formation     |
|15201547 | Eggholz-Formation | Eggholz-Formation     |
|15201548 | Bannhalden-Schotter | Bannhalden-Schotter     |
|15201549 | Weiach-Schotter | Weiach-Schotter     |
|15201550 | Balm-Schotter | Balm-Schotter     |
|15201551 | Windlach-Till | Windlach-Till     |
|15201552 | Südranden-Till | Südranden-Till     |
|15201553 | Schlossbuck-Schotter | Schlossbuck-Schotter     |
|15201554 | Risibüel-Schotter | Risibüel-Schotter     |
|15201555 | Schmerlet- und Toktri-Formation, undifferenziert | Schmerlet- und Toktri-Formation, undifferenziert     |
|15201556 | Saxegrabe-Schotter | Saxegrabe-Schotter     |
|15201557 | Zweidlen-Schotter | Zweidlen-Schotter     |
|15201558 | Burgacher-Schotter | Burgacher-Schotter     |
|15201559 | Chatzenstig-Schotter | Chatzenstig-Schotter     |
|15201560 | Wasterkingen-Schotter | Wasterkingen-Schotter     |
|15201561 | Paradiesgärtli-Schotter | Paradiesgärtli-Schotter     |
|15201562 | Tubeschwanz-Schotter | Tubeschwanz-Schotter     |
|15201563 | Weisweil-Schotter | Weisweil-Schotter     |
|15201564 | Hasli-Formation | Hasli-Formation     |
|15201565 | Stetten-Schotter | Stetten-Schotter     |
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
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |









## Anhang  GC_LITHO_CD {#gc-litho-cd}
Wertetabellen der lithologischen Beschreibung

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15101001 | Lockergestein | Lockergestein     |
|15101003 | gravitative Sedimente und Verwitterungsbildungen, undifferenziert | gravitative Sedimente und Verwitterungsbildungen, undifferenziert     |
|15101005 | Sturzablagerung, undifferenziert | Sturzablagerung, undifferenziert     |
|15101006 | Bergsturzablagerung | Bergsturzablagerung     |
|15101007 | Felssturzablagerung | Felssturzablagerung     |
|15101008 | Lawinenschutt | Lawinenschutt     |
|15101009 | Hangschutt | Hangschutt     |
|15101010 | Blockschutt | Blockschutt     |
|15101012 | Verwitterungslehm, undifferenziert | Verwitterungslehm, undifferenziert     |
|15101013 | Plateaulehm | Plateaulehm     |
|15101014 | Hanglehm, Schwemmlehm | Hanglehm, Schwemmlehm     |
|15101015 | Blockgletscher | Blockgletscher     |
|15101016 | zerrüttete Sackungsmasse | zerrüttete Sackungsmasse     |
|15101017 | Rutschmasse | Rutschmasse     |
|15101019 | glazigenes Sediment, undifferenziert | glazigenes Sediment, undifferenziert     |
|15101021 | Moräne (Till), undifferenziert | Moräne (Till), undifferenziert     |
|15101024 | Moräne auf Gletscher oder Toteis (Glacier or Dead Ice covered by Till) | Moräne auf Gletscher oder Toteis (Glacier or Dead Ice covered by Till)     |
|15101026 | fluviatiles Sediment, undifferenziert | fluviatiles Sediment, undifferenziert     |
|15101028 | glazifluviatiles Sediment, undifferenziert | glazifluviatiles Sediment, undifferenziert     |
|15101030 | randglazialer Schotter | randglazialer Schotter     |
|15101031 | glazifluviatiler Schotter | glazifluviatiler Schotter     |
|15101032 | Vorstossschotter | Vorstossschotter     |
|15101033 | Rückzugsschotter | Rückzugsschotter     |
|15101034 | Stauschotter | Stauschotter     |
|15101035 | gemischter Schutt | gemischter Schutt     |
|15101037 | Murgangablagerung | Murgangablagerung     |
|15101039 | Alluvion, undifferenziert | Alluvion, undifferenziert     |
|15101040 | fluviatiler Schotter | fluviatiler Schotter     |
|15101041 | Bachschutt | Bachschutt     |
|15101042 | Überschwemmungssediment | Überschwemmungssediment     |
|15101044 | lakustrisches Sediment, undifferenziert | lakustrisches Sediment, undifferenziert     |
|15101046 | glazilakustrisches Sediment, undifferenziert | glazilakustrisches Sediment, undifferenziert     |
|15101047 | glazilakustrisches Deltasediment | glazilakustrisches Deltasediment     |
|15101048 | subaquatisch abgelagerte Moräne (Waterlaid Till) | subaquatisch abgelagerte Moräne (Waterlaid Till)     |
|15101049 | detritische Verlandungsbildung | detritische Verlandungsbildung     |
|15101050 | palustrisches Sediment | palustrisches Sediment     |
|15101051 | palustrisches Sediment, undifferenziert | palustrisches Sediment, undifferenziert     |
|15101052 | Sumpf | Sumpf     |
|15101053 | Torfmoor, Torf | Torfmoor, Torf     |
|15101054 | Lignit (palustrisches Sediment) | Lignit (palustrisches Sediment)     |
|15101056 | Strandablagerungen | Strandablagerungen     |
|15101057 | lakustrisches Deltasediment | lakustrisches Deltasediment     |
|15101058 | Seebodensediment | Seebodensediment     |
|15101059 | Seekreide | Seekreide     |
|15101061 | äolisches Sediment, undifferenziert | äolisches Sediment, undifferenziert     |
|15101062 | äolischer Sand, Flugsand | äolischer Sand, Flugsand     |
|15101063 | Löss, Lösslehm | Löss, Lösslehm     |
|15101065 | vulkanische Asche | vulkanische Asche     |
|15101067 | anthropogene Elemente, undifferenziert | anthropogene Elemente, undifferenziert     |
|15101069 | künstliche Ablagerung, undifferenziert | künstliche Ablagerung, undifferenziert     |
|15101070 | Aufschüttung, Damm | Aufschüttung, Damm     |
|15101071 | Auffüllung | Auffüllung     |
|15101072 | Deponie | Deponie     |
|15101073 | Halde | Halde     |
|15101075 | dünne Lockermaterialbedeckung | dünne Lockermaterialbedeckung     |
|15101076 | geringmächtige Lockergesteinsbedeckung | geringmächtige Lockergesteinsbedeckung     |
|15101078 | tiefgründige Verwitterungsdecke | tiefgründige Verwitterungsdecke     |
|15101079 | Gyttja | Gyttja     |
|15101080 | Quelltuff (Kalksinter, Lockergestein) | Quelltuff (Kalksinter, Lockergestein)     |
|15101081 | hydrochemische Bildungen (Kalksinter) | hydrochemische Bildungen (Kalksinter)     |
|15101082 | Travertin (Kalksinter, Lockergestein) | Travertin (Kalksinter, Lockergestein)     |
|15101083 | In-situ-Verwitterungsschutt | In-situ-Verwitterungsschutt     |
|15101084 | strukturierter Hangschutt | strukturierter Hangschutt     |
|15101085 | Tsunamiablagerung | Tsunamiablagerung     |
|15101086 | Entwässerungssediment | Entwässerungssediment     |
|15101087 | Sedimentärer Gang (clastic dike) | Sedimentärer Gang (clastic dike)     |
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
|999998 | nicht anwendbar | nicht anwendbar     |
|999997 | unbekannt | unbekannt     |









## Anhang  GC_LITHO_UNCO_CD {#gc-litho-unco-cd}
Wertetabellen der lithologischen Beschreibung

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15101001 | Lockergestein | Lockergestein     |
|15101003 | gravitative Sedimente und Verwitterungsbildungen, undifferenziert | gravitative Sedimente und Verwitterungsbildungen, undifferenziert     |
|15101005 | Sturzablagerung, undifferenziert | Sturzablagerung, undifferenziert     |
|15101006 | Bergsturzablagerung | Bergsturzablagerung     |
|15101007 | Felssturzablagerung | Felssturzablagerung     |
|15101008 | Lawinenschutt | Lawinenschutt     |
|15101009 | Hangschutt | Hangschutt     |
|15101010 | Blockschutt | Blockschutt     |
|15101012 | Verwitterungslehm, undifferenziert | Verwitterungslehm, undifferenziert     |
|15101013 | Plateaulehm | Plateaulehm     |
|15101014 | Hanglehm, Schwemmlehm | Hanglehm, Schwemmlehm     |
|15101015 | Blockgletscher | Blockgletscher     |
|15101016 | zerrüttete Sackungsmasse | zerrüttete Sackungsmasse     |
|15101017 | Rutschmasse | Rutschmasse     |
|15101019 | glazigenes Sediment, undifferenziert | glazigenes Sediment, undifferenziert     |
|15101021 | Moräne (Till), undifferenziert | Moräne (Till), undifferenziert     |
|15101024 | Moräne auf Gletscher oder Toteis (Glacier or Dead Ice covered by Till) | Moräne auf Gletscher oder Toteis (Glacier or Dead Ice covered by Till)     |
|15101026 | fluviatiles Sediment, undifferenziert | fluviatiles Sediment, undifferenziert     |
|15101028 | glazifluviatiles Sediment, undifferenziert | glazifluviatiles Sediment, undifferenziert     |
|15101030 | randglazialer Schotter | randglazialer Schotter     |
|15101031 | glazifluviatiler Schotter | glazifluviatiler Schotter     |
|15101032 | Vorstossschotter | Vorstossschotter     |
|15101033 | Rückzugsschotter | Rückzugsschotter     |
|15101034 | Stauschotter | Stauschotter     |
|15101035 | gemischter Schutt | gemischter Schutt     |
|15101037 | Murgangablagerung | Murgangablagerung     |
|15101039 | Alluvion, undifferenziert | Alluvion, undifferenziert     |
|15101040 | fluviatiler Schotter | fluviatiler Schotter     |
|15101041 | Bachschutt | Bachschutt     |
|15101042 | Überschwemmungssediment | Überschwemmungssediment     |
|15101044 | lakustrisches Sediment, undifferenziert | lakustrisches Sediment, undifferenziert     |
|15101046 | glazilakustrisches Sediment, undifferenziert | glazilakustrisches Sediment, undifferenziert     |
|15101047 | glazilakustrisches Deltasediment | glazilakustrisches Deltasediment     |
|15101048 | subaquatisch abgelagerte Moräne (Waterlaid Till) | subaquatisch abgelagerte Moräne (Waterlaid Till)     |
|15101049 | detritische Verlandungsbildung | detritische Verlandungsbildung     |
|15101050 | palustrisches Sediment | palustrisches Sediment     |
|15101051 | palustrisches Sediment, undifferenziert | palustrisches Sediment, undifferenziert     |
|15101052 | Sumpf | Sumpf     |
|15101053 | Torfmoor, Torf | Torfmoor, Torf     |
|15101054 | Lignit (palustrisches Sediment) | Lignit (palustrisches Sediment)     |
|15101056 | Strandablagerungen | Strandablagerungen     |
|15101057 | lakustrisches Deltasediment | lakustrisches Deltasediment     |
|15101058 | Seebodensediment | Seebodensediment     |
|15101059 | Seekreide | Seekreide     |
|15101061 | äolisches Sediment, undifferenziert | äolisches Sediment, undifferenziert     |
|15101062 | äolischer Sand, Flugsand | äolischer Sand, Flugsand     |
|15101063 | Löss, Lösslehm | Löss, Lösslehm     |
|15101065 | vulkanische Asche | vulkanische Asche     |
|15101067 | anthropogene Elemente, undifferenziert | anthropogene Elemente, undifferenziert     |
|15101069 | künstliche Ablagerung, undifferenziert | künstliche Ablagerung, undifferenziert     |
|15101070 | Aufschüttung, Damm | Aufschüttung, Damm     |
|15101071 | Auffüllung | Auffüllung     |
|15101072 | Deponie | Deponie     |
|15101073 | Halde | Halde     |
|15101075 | dünne Lockermaterialbedeckung | dünne Lockermaterialbedeckung     |
|15101076 | geringmächtige Lockergesteinsbedeckung | geringmächtige Lockergesteinsbedeckung     |
|15101078 | tiefgründige Verwitterungsdecke | tiefgründige Verwitterungsdecke     |
|15101079 | Gyttja | Gyttja     |
|15101080 | Quelltuff (Kalksinter, Lockergestein) | Quelltuff (Kalksinter, Lockergestein)     |
|15101081 | hydrochemische Bildungen (Kalksinter) | hydrochemische Bildungen (Kalksinter)     |
|15101082 | Travertin (Kalksinter, Lockergestein) | Travertin (Kalksinter, Lockergestein)     |
|15101083 | In-situ-Verwitterungsschutt | In-situ-Verwitterungsschutt     |
|15101084 | strukturierter Hangschutt | strukturierter Hangschutt     |
|15101085 | Tsunamiablagerung | Tsunamiablagerung     |
|15101086 | Entwässerungssediment | Entwässerungssediment     |
|15101087 | Sedimentärer Gang (clastic dike) | Sedimentärer Gang (clastic dike)     |
|999998 | nicht anwendbar | nicht anwendbar     |
|999997 | unbekannt | unbekannt     |









## Anhang  GC_CHRONO_CD {#gc-chrono-cd}
Wertetabelle der chronostratigraphischen Einheiten

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15001001 | Phanerozoikum | Phanerozoikum     |
|15001002 | Känozoikum | Känozoikum     |
|15001003 | Quartär | Quartär     |
|15001004 | Holozän | Holozän     |
|15001005 | Pleistozän | Pleistozän     |
|15001006 | Spätes Pleistozän | Spätes Pleistozän     |
|15001007 | Mittleres Pleistozän | Mittleres Pleistozän     |
|15001009 | Frühes Pleistozän | Frühes Pleistozän     |
|15001010 | Calabrien | Calabrien     |
|15001011 | Gélasien | Gélasien     |
|15001012 | Tertiär | Tertiär     |
|15001013 | Neogen | Neogen     |
|15001014 | Pliozän | Pliozän     |
|15001015 | Plaisancien | Plaisancien     |
|15001016 | Zancléen | Zancléen     |
|15001017 | Miozän | Miozän     |
|15001018 | Spätes Miozän | Spätes Miozän     |
|15001019 | Messinien | Messinien     |
|15001020 | Tortonien | Tortonien     |
|15001021 | Mittleres Miozän | Mittleres Miozän     |
|15001022 | Serravallien | Serravallien     |
|15001023 | Langhien | Langhien     |
|15001024 | Frühes Miozän | Frühes Miozän     |
|15001025 | Burdigalien | Burdigalien     |
|15001026 | spätes Burdigalien | Spätes Burdigalien     |
|15001027 | frühes Burdigalien | frühes Burdigalien     |
|15001028 | Aquitanien | Aquitanien     |
|15001029 | Paläogen | Paläogen     |
|15001030 | Oligozän | Oligozän     |
|15001031 | Chattien | Chattien     |
|15001032 | spätes Chattien | Spätes Chattien     |
|15001033 | frühes Chattien | Frühes Chattien     |
|15001034 | Rupélien | Rupélien     |
|15001035 | Eozän | Eozän     |
|15001036 | Spätes Eozän | Spätes Eozän     |
|15001037 | Priabonien | Priabonien     |
|15001038 | spätes Priabonien | spätes Priabonien     |
|15001039 | frühes Priabonien | Frühes Priabonien     |
|15001040 | Mittleres Eozän | Mittleres Eozän     |
|15001041 | Bartonien | Bartonien     |
|15001042 | Lutétien | Lutétien     |
|15001043 | Frühes Eozän | Frühes Eozän     |
|15001044 | Yprésien | Yprésien     |
|15001045 | Paleozän | Paleozän     |
|15001046 | Thanétien | Thanétien     |
|15001047 | Sélandien | Sélandien     |
|15001048 | Danien | Danien     |
|15001049 | Mesozoikum | Mesozoikum     |
|15001050 | Kreide | Kreide     |
|15001051 | Späte Kreide | Späte Kreide     |
|15001052 | Maastrichtien | Maastrichtien     |
|15001053 | Campanien | Campanien     |
|15001054 | Santonien | Santonien     |
|15001055 | Coniacien | Coniacien     |
|15001056 | Turonien | Turonien     |
|15001057 | Cénomanien | Cénomanien     |
|15001058 | Frühe Kreide | Frühe Kreide     |
|15001059 | Albien | Albien     |
|15001060 | Aptien | Aptien     |
|15001061 | Barrémien | Barrémien     |
|15001062 | Hauterivien | Hauterivien     |
|15001063 | Valanginien | Valanginien     |
|15001064 | Berriasien | Berriasien     |
|15001065 | Jura | Jura     |
|15001066 | Später Jura | Später Jura     |
|15001067 | Tithonien | Tithonien     |
|15001068 | Kimméridgien | Kimméridgien     |
|15001069 | Oxfordien | Oxfordien     |
|15001070 | Mittlerer Jura | Mittlerer Jura     |
|15001071 | Callovien | Callovien     |
|15001072 | Bathonien | Bathonien     |
|15001073 | Bajocien | Bajocien     |
|15001074 | Aalénien | Aalénien     |
|15001075 | Früher Jura | Früher Jura     |
|15001076 | Toarcien | Toarcien     |
|15001077 | Pliensbachien | Pliensbachien     |
|15001078 | Sinémurien | Sinémurien     |
|15001079 | Hettangien | Hettangien     |
|15001080 | Trias | Trias     |
|15001081 | Späte Trias | Späte Trias     |
|15001082 | Rhät | Rhät     |
|15001083 | Norien | Norien     |
|15001084 | Carnien | Carnien     |
|15001085 | Mittlere Trias | Mittlere Trias     |
|15001086 | Ladinien | Ladinien     |
|15001087 | Anisien | Anisien     |
|15001088 | Frühe Trias | Frühe Trias     |
|15001089 | Olénékien | Olénékien     |
|15001090 | Indusien | Indusien     |
|15001091 | Paläozoikum | Paläozoikum     |
|15001093 | Perm | Perm     |
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
|15001117 | Asselien | Asselien     |
|15001119 | Karbon | Karbon     |
|15001120 | Pennsylvanien | Pennsylvanien     |
|15001121 | Spätes Pennsylvanien | Spätes Pennsylvanien     |
|15001122 | Mittleres Pennsylvanien | Mittleres Pennsylvanien     |
|15001123 | Frühes Pennsylvanien | Frühes Pennsylvanien     |
|15001124 | Mississippien | Mississippien     |
|15001125 | Spätes Mississippien | Spätes Mississippien     |
|15001126 | Mittleres Mississippien | Mittleres Mississippien     |
|15001127 | Frühes Mississippien | Frühes Mississippien     |
|15001128 | Devon | Devon     |
|15001129 | Frühes Devon | Frühes Devon     |
|15001130 | Mittleres Devon | Mittleres Devon     |
|15001131 | Spätes Devon | Spätes Devon     |
|15001133 | Silur | Silur     |
|15001134 | Ordovizium | Ordovizium     |
|15001135 | Kambrium | Kambrium     |
|15001136 | Proterozoikum | Proterozoikum     |
|15001137 | Gzhélien | Gzhélien     |
|15001138 | Kasimovien | Kasimovien     |
|15001139 | Moscovien | Moscovien     |
|15001140 | Bashkirien | Bashkirien     |
|15001141 | Serpukhovien | Serpukhovien     |
|15001142 | Viséen | Viséen     |
|15001143 | Tournaisien | Tournaisien     |
|15001144 | Pridoli | Pridoli     |
|15001145 | Ludlow | Ludlow     |
|15001146 | Wenlock | Wenlock     |
|15001147 | Llandovery | Llandovery     |
|15001148 | Spätes Ordovizium | Spätes Ordovizium     |
|15001149 | Mittleres Ordovizium | Mittleres Ordovizium     |
|15001150 | Frühes Ordovizium | Frühes Ordovizium     |
|15001151 | Chibanien | Chibanien     |
|15001152 | Präkambrium | Präkambrium     |
|15001153 | Archaikum | Archaikum     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |









## Anhang  GC_TECTO_CD {#gc-tecto-cd}
Wertetabelle der tektonischen Einheiten

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
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |









## Anhang  GC_MINERAL_CD {#gc-mineral-cd}
Wichtiges Mineral des metamorphen Gesteins

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|20401001 | Aktinolith | Aktinolith     |
|20401002 | Albit | Albit     |
|20401003 | Allanit | Allanit     |
|20401004 | Almandin | Almandin     |
|20401005 | Amphibol | Amphibol     |
|20401006 | Andalusit | Andalusit     |
|20401007 | Ankerit | Ankerit     |
|20401008 | Anorthit | Anorthit     |
|20401009 | Antigorit | Antigorit     |
|20401010 | Biotit | Biotit     |
|20401011 | Kalzit | Kalzit     |
|20401012 | Karbonatmineral | Karbonatmineral     |
|20401013 | Karpholith | Karpholith     |
|20401014 | Chlorit | Chlorit     |
|20401015 | Chloritoid | Chloritoid     |
|20401016 | Klinozoisit | Klinozoisit     |
|20401017 | Coesit | Coesit     |
|20401018 | Cordierit | Cordierit     |
|20401019 | Diopsid | Diopsid     |
|20401020 | Disthen | Disthen     |
|20401021 | Dolomit | Dolomit     |
|20401022 | Epidot | Epidot     |
|20401023 | Feldspat | Feldspat     |
|20401024 | Alkalifeldspat | Alkalifeldspat     |
|20401026 | Glaukophan | Glaukophan     |
|20401027 | Graphit | Graphit     |
|20401028 | Granat | Granat     |
|20401029 | Hornblende | Hornblende     |
|20401030 | Lawsonit | Lawsonit     |
|20401031 | Magnetit | Magnetit     |
|20401032 | Glimmer | Glimmer     |
|20401033 | Hellglimmer | Hellglimmer     |
|20401034 | Mikroklin | Mikroklin     |
|20401035 | Muskovit | Muskovit     |
|20401036 | Olivin | Olivin     |
|20401037 | Omphazit | Omphazit     |
|20401038 | Orthoklas | Orthoklas     |
|20401039 | Paragonit | Paragonit     |
|20401040 | Phlogopit | Phlogopit     |
|20401041 | Plagioklas | Plagioklas     |
|20401042 | Prehnit | Prehnit     |
|20401043 | Pyrit | Pyrit     |
|20401044 | Pyrop | Pyrop     |
|20401045 | Pyrophyllit | Pyrophyllit     |
|20401046 | Pyroxen | Pyroxen     |
|20401047 | Quarz | Quarz     |
|20401049 | Serpentin | Serpentin     |
|20401050 | Alumosilikat | Alumosilikat     |
|20401051 | Sillimanit | Sillimanit     |
|20401052 | Staurolith | Staurolith     |
|20401053 | Stilpnomelan | Stilpnomelan     |
|20401054 | Talk | Talk     |
|20401055 | Zoisit | Zoisit     |
|20401056 | Adular | Adular     |
|20401057 | Aegirin | Aegirin     |
|20401058 | Aegirin-Augit | Aegirin-Augit     |
|20401059 | Andesin | Andesin     |
|20401060 | Anhydrit | Anhydrit     |
|20401061 | Annit | Annit     |
|20401062 | Aragonit | Aragonit     |
|20401063 | Augit | Augit     |
|20401064 | Chrysotil | Chrysotil     |
|20401065 | Grossular | Grossular     |
|20401066 | Jadeit | Jadeit     |
|20401067 | Margarit | Margarit     |
|20401068 | Oligoklas | Oligoklas     |
|20401069 | Orthopyroxen | Orthopyroxen     |
|20401070 | Klinopyroxen | Klinopyroxen     |
|20401071 | Phengit | Phengit     |
|20401072 | Pumpellyit | Pumpellyit     |
|20401073 | Sanidin | Sanidin     |
|20401074 | Sapphirin | Sapphirin     |
|20401075 | Spessartin | Spessartin     |
|20401076 | Spinell | Spinell     |
|20401077 | Titanit | Titanit     |
|20401078 | Tremolit | Tremolit     |
|20401079 | Turmalin | Turmalin     |
|20401080 | Forsterit | Forsterit     |
|20401081 | Fayalit | Fayalit     |
|20401082 | Enstatit | Enstatit     |
|20401083 | Zeolith | Zeolith     |
|20401084 | Serizit | Serizit     |
|20401085 | Fuchsit | Fuchsit     |
|999997 | unbekannt | unbekannt     |
|999998 | nicht anwendbar | nicht anwendbar     |









## Anhang  GC_ADMIXTURE {#gc-admixture}
Beimengung

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14509008 | mit Hangschutt vermischt | mit Hangschutt vermischt     |
|14509010 | mit Torf | mit Torf     |
|14509004 | mit Blöcken | mit Blöcken     |
|14509013 | mit Schieferkohle | mit Schieferkohle     |
|14509002 | mit Lösslehm | mit Lösslehm     |
|14509011 | mit jurassischen Geröllen | mit jurassischen Geröllen     |
|14509012 | mit Geröllen aus Vogesen / Schwarzwald | mit Geröllen aus Vogesen / Schwarzwald     |
|14509001 | mit Löss | mit Löss     |
|14509006 | mit Block- und Geschiebestreu | mit Block- und Geschiebestreu     |
|14509007 | mit Blockschutt vermischt | mit Blockschutt vermischt     |
|14509003 | mit Seekreide | mit Seekreide     |
|14509005 | mit alpinen Geröllen | mit alpinen Geröllen     |
|14509009 | mit Verwitterungsschutt vermischt | mit Verwitterungsschutt vermischt     |









## Anhang  GC_COMPOSIT {#gc-composit}
Zusammensetzung des Lockergesteins

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14508004 | sandig | sandig     |
|14508002 | lehmig | lehmig     |
|14508001 | tonig | tonig     |
|14508006 | geröllreich | geröllreich     |
|14508007 | torfig | torfig     |
|14508003 | siltig | siltig     |
|14508005 | kiesig | kiesig     |









## Anhang  GC_CHARCAT {#gc-charcat}
Spezifische Eigenschaft.

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14511008 | umgelagert | umgelagert     |
|14511010 | drainiert | drainiert     |
|14511004 | verfestigt (durch Überlast), konsolidiert | verfestigt (durch Überlast), konsolidiert     |
|14511002 | rezent | rezent     |
|14511011 | künstlich bewässert (Wässermatten) | künstlich bewässert (Wässermatten)     |
|14511001 | fossil | fossil     |
|14511006 | verschwemmt | verschwemmt     |
|14511007 | sumpfig | sumpfig     |
|14511003 | verwittert | verwittert     |
|14511005 | verkittet (zementiert) | verkittet (zementiert)     |
|14511009 | abgebaut | abgebaut     |









## Anhang  GC_SYSTEM {#gc-system}
Fossiliengruppe.

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12903008 | Holz | Holz     |
|12903010 | Schwämme | Schwämme     |
|12903018 | Reptilien | Reptilien     |
|12903004 | Foraminiferen | Foraminiferen     |
|12903013 | Mollusken | Mollusken     |
|12903002 | Ostrakoden | Ostrakoden     |
|12903015 | Bivalven | Bivalven     |
|12903021 | Palynomorphe | Palynomorphe     |
|12903011 | Korallen | Korallen     |
|12903012 | Brachiopoden | Brachiopoden     |
|12903001 | Vertebraten | Vertebraten     |
|12903019 | Säugetiere | Säugetiere     |
|12903006 | Blätter | Blätter     |
|12903007 | Gräser | Gräser     |
|12903016 | Echinodermen | Echinodermen     |
|12903003 | Gastropoden | Gastropoden     |
|12903005 | Algen | Algen     |
|12903009 | Ammoniten | Ammoniten     |
|12903014 | Cephalopoden | Cephalopoden     |
|12903017 | Fische | Fische     |












# ESRI Geodatabase Schema Changes Report

Generated on: 2025-06-05 15:00:47.192054
Database: Unknown Database


## Summary
## Summary

- **0** items added
- **8** items removed
- **29** items modified
- **15** iterable items removed


---




## 🟢 Added Items


### GC_CORRELATION_CD
- **Type**: coded_domain
- **Location**: `coded_domain &gt; GC_CORRELATION_CD`



### GC_GEOL_MAPPING_UNIT_CD
- **Type**: coded_domain
- **Location**: `coded_domain &gt; GC_GEOL_MAPPING_UNIT_CD`



### GC_LITSTRAT_FORMATION_BANK_CD
- **Type**: coded_domain
- **Location**: `coded_domain &gt; GC_LITSTRAT_FORMATION_BANK_CD`



### TOPGIS_GC.GC_GEOL_MAPPING_UNIT_ATT
- **Type**: table
- **Location**: `tables &gt; TOPGIS_GC.GC_GEOL_MAPPING_UNIT_ATT`



### TOPGIS_GC.GC_GEOL_MAPPING_UNIT
- **Type**: table
- **Location**: `tables &gt; TOPGIS_GC.GC_GEOL_MAPPING_UNIT`



### TOPGIS_GC.GC_CORRELATION
- **Type**: table
- **Location**: `tables &gt; TOPGIS_GC.GC_CORRELATION`



### TOPGIS_GC.GC_LITSTRAT_FORMATION_BANK
- **Type**: table
- **Location**: `tables &gt; TOPGIS_GC.GC_LITSTRAT_FORMATION_BANK`



### TOPGIS_GC.GC_BEDR_GEOL_MAPPING_UNIT_ATT
- **Type**: relationship
- **Location**: `relationships &gt; TOPGIS_GC.GC_BEDR_GEOL_MAPPING_UNIT_ATT`



### TOPGIS_GC.GC_EX_GEO_PLG_EXP_UNIT_GC_GMU
- **Type**: relationship
- **Location**: `relationships &gt; TOPGIS_GC.GC_EX_GEO_PLG_EXP_UNIT_GC_GMU`



### TOPGIS_GC.GC_EX_GEO_PNT_EXP_UNIT_GC_GMU
- **Type**: relationship
- **Location**: `relationships &gt; TOPGIS_GC.GC_EX_GEO_PNT_EXP_UNIT_GC_GMU`



### 11301010
- **Type**: subtype
- **Location**: `subtypes &gt; 11301010`



### 14901009
- **Type**: subtype
- **Location**: `subtypes &gt; 14901009`



### 11401005
- **Type**: subtype
- **Location**: `subtypes &gt; 11401005`






## 🔴 Removed Items


### TOPGIS_GC.GC_LITSTRAT
- **Type**: table
- **Location**: `tables &gt; TOPGIS_GC.GC_LITSTRAT`



### TOPGIS_GC.GC_LITHO_BED
- **Type**: table
- **Location**: `tables &gt; TOPGIS_GC.GC_LITHO_BED`



### TOPGIS_GC.GC_LITSTRAT_BED
- **Type**: table
- **Location**: `tables &gt; TOPGIS_GC.GC_LITSTRAT_BED`



### TOPGIS_GC.GC_BED_FORM_ATT
- **Type**: table
- **Location**: `tables &gt; TOPGIS_GC.GC_BED_FORM_ATT`



### TOPGIS_GC.GC_FOR_ATT_GC_BEDR_FM_AT
- **Type**: relationship
- **Location**: `relationships &gt; TOPGIS_GC.GC_FOR_ATT_GC_BEDR_FM_AT`



### TOPGIS_GC.GC_BEDR_LITHO_GC_LITHO_BED
- **Type**: relationship
- **Location**: `relationships &gt; TOPGIS_GC.GC_BEDR_LITHO_GC_LITHO_BED`



### TOPGIS_GC.GC_EX_GEO_PNT_EXP_UNIT_GC_LI
- **Type**: relationship
- **Location**: `relationships &gt; TOPGIS_GC.GC_EX_GEO_PNT_EXP_UNIT_GC_LI`



### TOPGIS_GC.GC_EX_GEO_PLG_EXP_UNIT_GC_LI
- **Type**: relationship
- **Location**: `relationships &gt; TOPGIS_GC.GC_EX_GEO_PLG_EXP_UNIT_GC_LI`






## 🟡 Modified Items


### GC_LITHO_CD
- **Location**: `coded_domain &gt; GC_LITHO_CD &gt; codedValues`



**Changes in coded values:**

*Removed values:*

- `15104015`: (Meso)Kataklasit

- `15104044`: Adergneis

- `15104046`: agmatischer Gneis

- `15104087`: Albitit

- `15103040`: Alkalirhyolith

- `15103013`: Alkalisyenit

- `15103046`: Alkalitrachyt

- `15103006`: Alkalogranit

- `15104060`: Amphibolit

- `15104063`: Amphibolitgneis

- `15104074`: Anatexit, undifferenziert

- `15103045`: Andesit

- `15102071`: Anhydrit

- `15102059`: Anthrazit

- `15103030`: Aplit

- `15102044`: Aptychenkalk

- `15102038`: Arenit

- `15102016`: Arkose

- `15103058`: Aschentuff

- `15104042`: Augengneis

- `15104061`: Bänderamphibolit

- `15104043`: Bändergneis

- `15103048`: Basalt

- `15103068`: basisches Ganggestein

- `15103069`: Basisches Gestein

- `15103066`: Bentonit

- `15102045`: biogener Kalkstein, undifferenziert

- `15102032`: biogenes / biochemisches / organisches Sedimentgestein, undifferenziert

- `15102106`: bioklastischer Kalk

- `15104085`: Biotitit

- `15102082`: Bohnerz

- `15102087`: Boluston

- `15102006`: Brekzie

- `15102093`: Caliche

- `15102068`: chemisches Sedimentgestein, undifferenziert

- `15104089`: Chloritit

- `15104034`: Chloritschiefer

- `15103043`: Dazit

- `15102046`: detritischer Kalk

- `15104079`: Diatexit mit nebulitischer Textur

- `15104080`: Diatexit mit Schlierentextur

- `15104081`: Diatexit mit Schollentextur

- `15103011`: Diorit

- `15103035`: Dolerit

- `15102049`: Dolomit

- `15102109`: Dolomitbrekzie

- `15104216`: dolomitischer Marmor

- `15102012`: Dolomitsandstein

- `15102100`: Echinodermenkalk

- `15102061`: Eisenoolith

- `15102103`: Eisensandstein

- `15102108`: eisenschüssiger Kalk

- `15104064`: Eklogit

- `15103039`: Ergussgestein, undifferenziert

- `15103023`: Essexit

- `15102070`: Evaporit, undifferenziert

- `15103037`: Extrusivgestein, undifferenziert

- `15104053`: Fels, undifferenziert

- `15102017`: Flyschsandstein, Grauwacke

- `15103015`: Gabbro

- `15103026`: Ganggestein, undifferenziert

- `15104210`: Geröll führender Metasandstein

- `15102018`: Geröll führender Sandstein

- `15104027`: Gestein der Regional- und Kontaktmetamorphose, undifferenziert

- `15104002`: Gestein der Störungszone

- `15104003`: Gestein der Störungszone, undifferenziert

- `15104006`: Gesteinsmehl

- `15102072`: Gips

- `15102101`: glaukonitischer Kalkstein

- `15102104`: glaukonitischer Mergel

- `15102020`: Glaukonitsandstein

- `15104036`: Glaukophanschiefer

- `15102019`: Glimmersandstein

- `15104035`: Glimmerschiefer

- `15104072`: Gneis mit Feldspatblasten

- `15104041`: Gneis, undifferenziert

- `15104097`: Granat-Glimmerschiefer

- `15103007`: Granit

- `15103008`: Granodiorit

- `15103024`: Granophyr

- `15104058`: Granulit

- `15104071`: Greisen

- `15104098`: Grünschiefer

- `15104086`: Hornblenditit

- `15104067`: Hornfels

- `15102054`: Hornstein, Chert

- `15102088`: Huppererde

- `15103054`: Ignimbrit

- `15103003`: Intrusivgestein, undifferenziert

- `15104005`: Kakirit, undifferenziert

- `15102041`: Kalkbrekzie

- `15102029`: Kalkmergelstein

- `15102042`: Kalkoolith

- `15102011`: Kalksandstein

- `15104037`: Kalkschiefer

- `15104054`: Kalksilikatfels

- `15102034`: Kalkstein, undifferenziert

- `15104056`: Karbonat- und Silikat führendes Gestein

- `15102075`: Karbonat, undifferenziert

- `15103051`: Karbonatit

- `15104010`: Kataklasit, undifferenziert

- `15102013`: kieseliger Sandstein

- `15102051`: kieseliges Gestein, undifferenziert

- `15102035`: Kieselkalk

- `15104051`: Kinzigit

- `15102003`: klastisches Sedimentgestein, undifferenziert

- `15104007`: Kluftletten

- `15102056`: Kohle, undifferenziert

- `15102007`: Konglomerat

- `15102005`: Konglomerat und Brekzie, undifferenziert (Psephit, Korngrösse: Kies, Steine und Blöcke)

- `15102105`: kreidiger Kalk

- `15103057`: Kristalltuff

- `15102094`: Krustenkalk

- `15103033`: Lamprophyr

- `15103056`: Lapillituff

- `15104047`: Leptinit

- `15102057`: Lignit (organisches Sedimentgestein)

- `15102102`: Lithothamniensandstein

- `15103001`: Magmatit

- `15104055`: Marmor (Fels)

- `15104215`: Marmor (sedimentärer Protolith)

- `15102014`: mergeliger Sandstein

- `15102107`: Mergelkalk

- `15102027`: Mergelstein

- `15104433`: Metaalkalirhyolith

- `15104411`: Metaalkalisyenit

- `15104439`: Metaalkalitrachyt

- `15104404`: Metaalkalogranit

- `15104438`: Metaandesit

- `15104427`: Metaaplit

- `15104208`: Metaarkose

- `15104441`: Metabasalt

- `15104203`: Metabrekzie

- `15104436`: Metadazit

- `15104409`: Metadiorit

- `15104432`: Metadolerit

- `15104421`: Metaessexit

- `15104413`: Metagabbro

- `15104423`: Metaganggestein

- `15104405`: Metagranit

- `15104406`: Metagranodiorit

- `15104422`: Metagranophyr

- `15104209`: Metagrauwacke

- `15104445`: Metaignimbrit

- `15104218`: Metakarbonat

- `15104204`: Metakonglomerat

- `15104430`: Metalamprophyr

- `15104401`: Metamagmatit

- `15104214`: Metamergel

- `15104428`: Metamikrodiorit

- `15104429`: Metamikrogabbro

- `15104424`: Metamikrogranit

- `15104415`: Metamonzodiorit

- `15104416`: Metamonzogabbro

- `15104417`: Metamonzonit

- `15104402`: metamorph überprägtes Intrusivgestein

- `15104444`: metamorph überprägtes pyroklastisches Gestein

- `15104001`: Metamorphit

- `15104095`: Metamorphit (magmatischer Protolith erkennbar)

- `15104092`: Metamorphit (Protolith erkennbar)

- `15104093`: Metamorphit (sedimentärer Protolith erkennbar)

- `15104414`: Metanorit

- `15104426`: Metapegmatit

- `15104211`: Metapelit

- `15104419`: Metaperidotit

- `15104443`: Metaphonolit

- `15104431`: Metapikrit

- `15104403`: Metaplutonit

- `15104207`: Metapsammit

- `15104202`: Metapsephit

- `15104418`: Metapyroxenit

- `15104437`: Metaquarzandesit

- `15104407`: Metaquarzdiorit

- `15104412`: Metaquarzgabbro

- `15104217`: Metaradiolarit

- `15104435`: Metarhyodazit

- `15104434`: Metarhyolith

- `15104205`: Metasandstein

- `15104201`: Metasediment

- `15104212`: Metasiltstein

- `15104069`: Metasomatit, undifferenziert

- `15104410`: Metasyenit

- `15104076`: Metatexit mit Fleckentextur

- `15104078`: Metatexit mit Netztextur

- `15104077`: Metatexit mit stromatitischer Textur

- `15104408`: Metatonalit

- `15104440`: Metatrachyt

- `15104446`: Metavulkanit

- `15104075`: Migmatit

- `15102037`: Mikrit

- `15103031`: Mikrodiorit

- `15103032`: Mikrogabbro

- `15103027`: Mikrogranit

- `15104084`: monomineralischer Metamorphit, undifferenziert

- `15103017`: Monzodiorit

- `15103018`: Monzogabbro

- `15103019`: Monzonit

- `15102022`: Muschelsandstein

- `15104020`: Mylonit

- `15104018`: Mylonit, undifferenziert

- `15104420`: nephelinitischer Metasyenit

- `15103022`: nephelinitischer Syenit

- `15103016`: Norit

- `15102043`: Nummulitenkalk

- `15102021`: Nummulitensandstein

- `15104099`: Ophikalzit

- `15104049`: Orthogneis

- `15104048`: Paragneis

- `15102092`: pedogenes Karbonat, undifferenziert

- `15103029`: Pegmatit

- `15102024`: Pelit, undifferenziert

- `15103021`: Peridotit (Intrusivgestein)

- `15104065`: Peridotit (Metamorphit)

- `15103050`: Phonolith

- `15102065`: phosphoritreicher Kalkstein

- `15102066`: phosphoritreicher Mergelstein

- `15102064`: phosphoritreicher Sandstein

- `15102063`: phosphoritreiches Gestein, undifferenziert

- `15104029`: Phyllit

- `15104023`: Phyllonit

- `15103049`: Pikrit (Effusiva)

- `15103034`: Pikrit (Intrusivgestein)

- `15104038`: Prasinit

- `15104014`: Protokataklasit

- `15104019`: Protomylonit

- `15104025`: Pseudotachylit

- `15103055`: Pyroklastische Brekzie

- `15103053`: pyroklastisches Gestein, undifferenziert (vulkanischer Tuff, &gt; 75 % pyroklast. Komp.)

- `15103020`: Pyroxenit (Intrusivgestein)

- `15104088`: Pyroxenit (monomineralischer Metamorphit)

- `15103044`: Quarzandesit

- `15103009`: Quarzdiorit

- `15103014`: Quarzgabbro

- `15104091`: Quarzit (monomineralischer Metamorphit)

- `15104206`: Quarzit (sedimentärer Protolith)

- `15102089`: Quarzsand

- `15102010`: Quarzsandstein

- `15104096`: Quarzschiefer

- `15102077`: Quelltuff (Kalksinter, Sedimentgestein)

- `15102052`: Radiolarit

- `15104011`: Rauwacke (Kataklasit)

- `15102076`: Rauwacke (Sedimentgestein)

- `15102080`: Residualgestein / pedogen überprägtes Gestein, undifferenziert

- `15103042`: Rhyodazit

- `15103041`: Rhyolith

- `15103028`: Rhyolithporphyr

- `15102040`: Riffkalk

- `15104059`: Rodingit

- `15102039`: Rudit

- `15102009`: Sandstein, undifferenziert (Psammit: Sandkorngrösse)

- `15103067`: saures Ganggestein

- `15104031`: Schiefer, undifferenziert

- `15102030`: Schlammstein

- `15104062`: Schollenamphibolit

- `15102001`: Sedimentgestein

- `15104033`: Serizitschiefer

- `15104090`: Serpentinit

- `15102084`: siderolithische Verwitterungsbildungen

- `15102090`: Silcrete

- `15104057`: silikatreicher Marmor

- `15102086`: silikatreiches Gestein, undifferenziert

- `15102025`: Siltstein

- `15104070`: Skarn

- `15102036`: Spatkalk

- `15102053`: Spiculit

- `15102058`: Steinkohle

- `15102073`: Steinsalz

- `15104050`: Stronalit

- `15102047`: Süsswasserkalk

- `15103012`: Syenit

- `15104039`: Talkschiefer

- `15104008`: tektonische Brekzie (kohäsionslos)

- `15104013`: tektonische Brekzie (mit Kohäsion)

- `15104012`: tektonische Dolomitbrekzie

- `15104448`: tektonische Kalkbrekzie

- `15103005`: Tiefengestein, undifferenziert

- `15103010`: Tonalit

- `15102015`: toniger Sandstein

- `15102028`: Tonmergelstein

- `15104032`: Tonschiefer (Schiefer)

- `15104213`: Tonschiefer (sedimentärer Protolith)

- `15102026`: Tonstein

- `15103047`: Trachyt

- `15102078`: Travertin (Kalksinter, Sedimentgestein)

- `15103060`: Tuffit, undifferenziert (pyroklast. und nicht vulk. Sedimente, 75-25 % pyroklast. Komp.)

- `15103061`: tuffitische Brekzie

- `15103063`: tuffitischer Sandstein

- `15103064`: tuffitischer Siltstein

- `15103065`: tuffitischer Tonstein

- `15103062`: tuffitisches Konglomerat

- `15103070`: Ultrabasisches Gestein

- `15104016`: Ultrakataklasit

- `15104447`: ultramafisches Gestein

- `15104021`: Ultramylonit

- `15104045`: Zweiglimmergneis


*Added values:*

- `15111153`: Mergelstein: konglomeratisch

- `15111154`: Mergelstein: Korallen

- `15111155`: Mergelstein: Lignit

- `15111156`: Mergelstein: Ooide

- `15111157`: Mergelstein: Phosphorit

- `15111158`: Mergelstein: sandig

- `15111159`: Mergelstein: sandig: Bioklasten

- `15111160`: Mergelstein: sandig-dolomitisch

- `15111161`: Mergelstein: sandig: Glaukonit

- `15111162`: Mergelstein: sandig: Glimmer

- `15111163`: Mergelstein: sandig: Kohle

- `15111164`: Mergelstein: sandig-kalkig

- `15111165`: Mergelstein: sandig-siltig

- `15111166`: Mergelstein: sandig-tonig

- `15111167`: Mergelstein: sandig-tonig: Glaukonit

- `15111168`: Mergelstein: schiefrig

- `15111169`: Mergelstein: schiefrig: Bitumen

- `15111170`: Mergelstein: siltig

- `15111171`: Mergelstein: siltig: Glaukonit

- `15111172`: Mergelstein: siltig: Glimmer

- `15111173`: Mergelstein: siltig-dolomitisch

- `15111174`: Mergelstein: siltig-kalkig

- `15111175`: Mergelstein: siltig-schiefrig

- `15111176`: Mergelstein: siltig-tonig

- `15111177`: Mergelstein: tonig

- `15111178`: Mergelstein: tonig: Bitumen

- `15111179`: Mergelstein: tonig: Kohle

- `15111180`: Gestein: Karbonat

- `15111181`: Gestein: sedimentär: Karbonat

- `15111182`: Gestein: pedogen: Karbonat

- `15111183`: Gestein: pedogen-verkrustet: Karbonat

- `15111184`: Gestein: vulkanisch: Karbonat

- `15111185`: Gestein: metamorph: Karbonat

- `15111186`: Kalkstein

- `15111187`: Kalkstein: Albit

- `15111188`: Kalkstein: Algen

- `15111189`: Kalkstein: arenitisch

- `15111190`: Kalkstein: arenitisch: Bioklasten

- `15111191`: Kalkstein: arenitisch: Bioklasten-Chert

- `15111192`: Kalkstein: arenitisch: Glaukonit

- `15111193`: Kalkstein: arenitisch: Ooide

- `15111194`: Kalkstein: arenitisch: Quarz

- `15111195`: Kalkstein: arenitisch-spätig

- `15111196`: Kalkstein: Bioklasten

- `15111197`: Kalkstein: Bioklasten-Chert

- `15111198`: Kalkstein: Bioklasten-Ooide

- `15111199`: Kalkstein: Bitumen

- `15111200`: Kalkstein: Bitumen-Bioklasten

- `15111201`: Kalkstein: brekziös

- `15111202`: Kalkstein: Chert

- `15111203`: Kalkstein: dolomitisch

- `15111204`: Kalkstein: dolomitisch: Bioklasten

- `15111205`: Kalkstein: Eisenmineralien

- `15111206`: Kalkstein: Eisenooide

- `15111207`: Kalkstein: Glaukonit

- `15111208`: Kalkstein: Glaukonit-Bioklasten

- `15111209`: Kalkstein: kieselig

- `15111210`: Kalkstein: kieselig: Bioklasten

- `15111211`: Kalkstein: kieselig: Bioklasten-Chert

- `15111212`: Kalkstein: kieselig: Glaukonit

- `15111213`: Kalkstein: kieselig-spätig

- `15111214`: Kalkstein: Korallen

- `15111215`: Kalkstein: kreidig

- `15111216`: Kalkstein: kreidig: Bitumen

- `15111217`: Kalkstein: kreidig: Chert

- `15111218`: Kalkstein: kreidig: Pisoide

- `15111219`: Kalkstein: kristallin

- `15111220`: Kalkstein: Limonit

- `15111221`: Kalkstein: mergelig

- `15111222`: Kalkstein: mergelig: Bioklasten

- `15111223`: Kalkstein: mergelig: Chert

- `15111224`: Kalkstein: mergelig: Glaukonit

- `15111225`: Kalkstein: mergelig: Pyrit

- `15111226`: Kalkstein: mergelig-dolomitisch

- `15111227`: Kalkstein: mergelig-kieselig

- `15111228`: Kalkstein: mergelig-schiefrig

- `15111229`: Kalkstein: mikritisch

- `15111230`: Kalkstein: mikritisch: Aptychen

- `15111231`: Kalkstein: mikritisch: Bioklasten

- `15111232`: Kalkstein: mikritisch: Bioklasten-Chert

- `15111233`: Kalkstein: mikritisch: Calpionellen

- `15111234`: Kalkstein: mikritisch: Chert

- `15111235`: Kalkstein: mikritisch: Glaukonit

- `15111236`: Kalkstein: mikritisch: Onkoide

- `15111237`: Kalkstein: mikritisch: Ooide

- `15111238`: Kalkstein: Nummuliten

- `15111239`: Kalkstein: Onkoide

- `15111240`: Kalkstein: Ooide

- `15111241`: Kalkstein: Ooide-Chert

- `15111242`: Kalkstein: pedogen-verkrustet

- `15111243`: Kalkstein: Phosphorit

- `15111244`: Kalkstein: Pisoide

- `15111245`: Kalkstein: ruditisch

- `15111246`: Kalkstein: ruditisch: Korallen

- `15111247`: Kalkstein: sandig

- `15111248`: Kalkstein: sandig: Bioklasten

- `15111249`: Kalkstein: sandig: Eisenooide

- `15111250`: Kalkstein: sandig: Glaukonit

- `15111251`: Kalkstein: sandig: Glimmer

- `15111252`: Kalkstein: sandig-kieselig

- `15111253`: Kalkstein: sandig-spätig

- `15111254`: Kalkstein: sandig-tonig

- `15111255`: Kalkstein: Schwämme

- `15111256`: Kalkstein: siltig

- `15111257`: Kalkstein: siltig: Bioklasten

- `15111258`: Kalkstein: siltig-tonig

- `15111259`: Kalkstein: spätig

- `15111260`: Kalkstein: spätig: Bioklasten

- `15111261`: Kalkstein: spätig: Bioklasten-Chert

- `15111262`: Kalkstein: spätig: Bioklasten-Glaukonit

- `15111263`: Kalkstein: spätig: Bioklasten-Ooide

- `15111264`: Kalkstein: spätig: Chert

- `15111265`: Kalkstein: spätig: Echinodermen

- `15111001`: Gestein

- `15111002`: Gestein: sedimentär

- `15111003`: Gestein: klastisch

- `15111004`: Gestein: psephitisch

- `15111005`: Brekzie

- `15111006`: Brekzie: sedimentär

- `15111007`: Brekzie: dolomitisch

- `15111008`: Brekzie: dolomitisch: Bitumen

- `15111009`: Brekzie: dolomitisch-polymikt

- `15111010`: Brekzie: kalkig

- `15111011`: Brekzie: kalkig: Bioklasten

- `15111012`: Brekzie: kalkig-dolomitisch

- `15111013`: Brekzie: kalkig-polymikt

- `15111014`: Brekzie: kristallin

- `15111015`: Brekzie: kristallin: polymikt

- `15111016`: Brekzie: monomikt

- `15111017`: Brekzie: polymikt

- `15111018`: Brekzie: sandig

- `15111019`: Brekzie: siltig

- `15111020`: Brekzie: pyroklastisch

- `15111021`: Brekzie: rhyolithisch

- `15111022`: Brekzie: tuffitisch

- `15111023`: Brekzie: tektonisch

- `15111024`: Brekzie: kakiritisch

- `15111025`: Brekzie: kataklastisch

- `15111026`: Brekzie: kataklastisch-dolomitisch

- `15111027`: Brekzie: kataklastisch-kalkig

- `15111028`: Konglomerat

- `15111029`: Konglomerat: dolomitisch

- `15111030`: Konglomerat: kalkig

- `15111031`: Konglomerat: kalkig: Muscheln

- `15111032`: Konglomerat: kalkig-dolomitisch

- `15111033`: Konglomerat: kalkig-residual: Eisenpisoide

- `15111034`: Konglomerat: kristallin

- `15111035`: Konglomerat: monomikt

- `15111036`: Konglomerat: ophiolithisch

- `15111037`: Konglomerat: polymikt

- `15111038`: Konglomerat: polymikt: Bioklasten

- `15111039`: Konglomerat: polymikt: Quarz

- `15111040`: Konglomerat: Quarz

- `15111041`: Konglomerat: pyroklastisch

- `15111042`: Konglomerat: tuffitisch

- `15111043`: Gestein: psammitisch

- `15111044`: Sandstein

- `15111045`: Sandstein: Anthrazit

- `15111046`: Sandstein: Bioklasten

- `15111047`: Sandstein: Bitumen

- `15111048`: Sandstein: dolomitisch

- `15111049`: Sandstein: Eisenmineralien

- `15111050`: Sandstein: Eisenooide

- `15111051`: Sandstein: Feldspat

- `15111052`: Sandstein: Glaukonit

- `15111053`: Sandstein: Glimmer

- `15111054`: Sandstein: Glimmer-Glaukonit

- `15111055`: Sandstein: Gips

- `15111056`: Sandstein: kalkig

- `15111057`: Sandstein: kalkig: Bioklasten

- `15111058`: Sandstein: kalkig: Glaukonit

- `15111059`: Sandstein: kalkig: Glimmer

- `15111060`: Sandstein: kalkig: Kohle

- `15111061`: Sandstein: kalkig: Muscheln

- `15111062`: Sandstein: kalkig: Nummuliten

- `15111063`: Sandstein: kalkig: Quarz

- `15111064`: Sandstein: kalkig-dolomitisch

- `15111065`: Sandstein: kalkig-kieselig

- `15111066`: Sandstein: kieselig

- `15111067`: Sandstein: Kohle

- `15111068`: Sandstein: konglomeratisch

- `15111069`: Sandstein: konglomeratisch-kalkig: Muscheln

- `15111070`: Sandstein: mergelig

- `15111071`: Sandstein: mergelig: Glaukonit

- `15111072`: Sandstein: mergelig: Glimmer

- `15111073`: Sandstein: Phosphorit

- `15111074`: Sandstein: Quarz

- `15111075`: Sandstein: Quarz-Glaukonit

- `15111076`: Sandstein: Quarz-Glimmer

- `15111077`: Sandstein: siltig

- `15111078`: Sandstein: siltig-kalkig

- `15111079`: Sandstein: tonig

- `15111080`: Sandstein: tonig: Feldspat

- `15111081`: Sandstein: tonig: Glaukonit

- `15111082`: Sandstein: tonig: Glimmer

- `15111083`: Sandstein: tonig: Kohle

- `15111084`: Sandstein: tonig: Lithoklasten

- `15111085`: Sandstein: tonig-dolomitisch

- `15111086`: Sandstein: tonig-kalkig

- `15111087`: Sandstein: tonig-kalkig: Kohle

- `15111088`: Sandstein: tuffitisch

- `15111089`: Gestein: pelitisch

- `15111090`: Siltstein

- `15111091`: Siltstein: dolomitisch

- `15111092`: Siltstein: Glimmer

- `15111093`: Siltstein: kalkig

- `15111094`: Siltstein: Kohle

- `15111095`: Siltstein: mergelig

- `15111096`: Siltstein: sandig

- `15111097`: Siltstein: schiefrig

- `15111098`: Siltstein: tonig

- `15111099`: Siltstein: tonig-dolomitisch

- `15111100`: Siltstein: tonig-kalkig

- `15111101`: Siltstein: tuffitisch

- `15111102`: Tonstein

- `15111103`: Tonstein: Anthrazit

- `15111104`: Tonstein: Bitumen

- `15111105`: Tonstein: dolomitisch

- `15111106`: Tonstein: Eisenooide

- `15111107`: Tonstein: Glaukonit

- `15111108`: Tonstein: kalkig

- `15111109`: Tonstein: kalkig: Glaukonit

- `15111110`: Tonstein: kieselig

- `15111111`: Tonstein: Kohle

- `15111112`: Tonstein: mergelig

- `15111113`: Tonstein: mergelig: Bitumen

- `15111114`: Tonstein: mergelig: Glimmer

- `15111115`: Tonstein: Pyrit

- `15111116`: Tonstein: sandig

- `15111117`: Tonstein: sandig: Glimmer

- `15111118`: Tonstein: sandig: Kohle

- `15111119`: Tonstein: sandig-dolomitisch

- `15111120`: Tonstein: sandig-kalkig

- `15111121`: Tonstein: sandig-mergelig

- `15111122`: Tonstein: sandig-schiefrig

- `15111123`: Tonstein: schiefrig

- `15111124`: Tonstein: schiefrig: Anthrazit

- `15111125`: Tonstein: schiefrig: Bitumen

- `15111126`: Tonstein: siltig

- `15111127`: Tonstein: siltig: Glimmer

- `15111128`: Tonstein: siltig-dolomitisch

- `15111129`: Tonstein: siltig-kalkig

- `15111130`: Tonstein: siltig-schiefrig

- `15111131`: Tonstein: tuffitisch

- `15111132`: Mergelstein

- `15111133`: Mergelstein: Bioklasten

- `15111134`: Mergelstein: Bioklasten-Ooide

- `15111135`: Mergelstein: Bitumen

- `15111136`: Mergelstein: dolomitisch

- `15111137`: Mergelstein: Eisenooide

- `15111138`: Mergelstein: Gips

- `15111139`: Mergelstein: Glaukonit

- `15111140`: Mergelstein: Glaukonit-Bioklasten

- `15111141`: Mergelstein: Glimmer

- `15111142`: Mergelstein: kalkig

- `15111143`: Mergelstein: kalkig: Bioklasten

- `15111144`: Mergelstein: kalkig: Bitumen

- `15111145`: Mergelstein: kalkig-dolomitisch

- `15111146`: Mergelstein: kalkig: Eisenooide

- `15111147`: Mergelstein: kalkig: Glaukonit

- `15111148`: Mergelstein: kalkig: Ooide

- `15111149`: Mergelstein: kalkig-kieselig

- `15111150`: Mergelstein: kalkig-schiefrig

- `15111151`: Mergelstein: kieselig

- `15111152`: Mergelstein: Kohle

- `15111437`: Diorit: Quarz

- `15111438`: Diorit: Quarz-Biotit

- `15111439`: Diorit: Quarz-Epidot

- `15111440`: Diorit: Quarz-Hornblende

- `15111441`: Diorit: schiefrig

- `15111442`: Gestein: gabbroisch

- `15111443`: Gabbro

- `15111444`: Gabbro: Hornblende

- `15111445`: Gabbro: mikrokristallin

- `15111446`: Gabbro: monzonitisch

- `15111447`: Gabbro: monzonitisch: Nephelin

- `15111448`: Gabbro: mylonitisch

- `15111449`: Gabbro: Olivin

- `15111450`: Gabbro: Omphazit

- `15111451`: Gabbro: Orthopyroxen

- `15111452`: Gabbro: Quarz

- `15111453`: Gestein: foidolitisch

- `15111454`: Foidolit

- `15111455`: Gestein: ultramafisch

- `15111456`: Peridotit

- `15111457`: Peridotit: plutonisch

- `15111458`: Peridotit: plutonisch: Klinopyroxen-Orthopyroxen

- `15111459`: Peridotit: plutonisch: Olivin

- `15111460`: Peridotit: plutonisch: Olivin-Klinopyroxen

- `15111461`: Peridotit: plutonisch: Olivin-Orthopyroxen

- `15111462`: Peridotit: metamorph

- `15111463`: Peridotit: metamorph: Hornblende

- `15111464`: Peridotit: metamorph: Phlogopit

- `15111465`: Peridotit: metamorph: Serpentin

- `15111466`: Pyroxenit

- `15111467`: Pyroxenit: plutonisch

- `15111468`: Gestein: metamorph

- `15111469`: Gestein: metasomatisch

- `15111470`: Gestein: tektonisch

- `15111471`: Kakirit

- `15111472`: Kakirit: tonig

- `15111473`: Kataklastit

- `15111474`: Mylonit

- `15111475`: Mylonit: kalkig

- `15111476`: Mylonit: phyllitisch

- `15111477`: Pseudotachyllit

- `15111478`: Hornfels

- `15111479`: Granofels

- `15111480`: Granofels: Albit

- `15111481`: Granofels: Granat

- `15111482`: Granofels: Kalksilikat

- `15111483`: Granofels: Olivin

- `15111484`: Granofels: Pyroxen

- `15111485`: Granofels: Silikat-Karbonat

- `15111486`: Marmor

- `15111487`: Marmor: dolomitisch

- `15111488`: Marmor: dolomitisch-schiefrig

- `15111489`: Marmor: kalkig

- `15111490`: Marmor: kalkig: Chlorit

- `15111491`: Marmor: kalkig: Serizit

- `15111492`: Marmor: kalkig-kieselig

- `15111493`: Marmor: Kalksilikat

- `15111494`: Marmor: kieselig

- `15111495`: Marmor: konglomeratisch

- `15111496`: Marmor: konglomeratisch-kalkig

- `15111497`: Marmor: metasomatisch

- `15111498`: Marmor: sandig

- `15111499`: Marmor: sandig: Bioklasten

- `15111500`: Marmor: schiefrig

- `15111501`: Marmor: Serizit

- `15111502`: Marmor: Silikat

- `15111503`: Marmor: tonig

- `15111504`: Marmor: tonig-schiefrig

- `15111505`: Quarzit

- `15111506`: Quarzit: Albit

- `15111507`: Quarzit: Chlorit

- `15111508`: Quarzit: kalkig

- `15111509`: Quarzit: Serizit

- `15111510`: Gneis

- `15111511`: Gneis: Albit

- `15111512`: Gneis: Albit-Oligoklas

- `15111513`: Gneis: Aluminosilikat

- `15111514`: Gneis: Amphibol

- `15111515`: Gneis: aplitisch

- `15111516`: Gneis: augig

- `15111517`: Gneis: augig: Phengit

- `15111518`: Gneis: Biotit

- `15111519`: Gneis: Biotit-Hornblende

- `15111520`: Gneis: Biotit-Muskovit

- `15111521`: Gneis: Biotit-Plagioklas

- `15111522`: Gneis: Chlorit

- `15111523`: Gneis: dioritisch

- `15111524`: Gneis: gebändert

- `15111525`: Gneis: gebändert: Granat

- `15111526`: Gneis: Granat

- `15111527`: Gneis: granitisch

- `15111528`: Gneis: granitisch-augig

- `15111529`: Gneis: granodioritisch

- `15111530`: Gneis: granulitisch

- `15111531`: Gneis: Hornblende

- `15111532`: Gneis: Kyanit

- `15111533`: Gneis: magmatisch

- `15111534`: Gneis: magmatisch-augig

- `15111535`: Gneis: magmatisch-augig: Cordierit

- `15111536`: Gneis: metasomatisch

- `15111537`: Gneis: migmatitisch

- `15111538`: Gneis: migmatitisch: Cordierit

- `15111539`: Gneis: migmatitisch-augig

- `15111540`: Gneis: Mikroklin

- `15111541`: Gneis: Muskovit

- `15111542`: Gneis: mylonitisch

- `15111543`: Gneis: Phengit

- `15111544`: Gneis: phyllitisch

- `15111545`: Gneis: psammitisch

- `15111546`: Gneis: psephitisch

- `15111547`: Gneis: psephitisch: Phengit

- `15111548`: Gneis: schiefrig

- `15111549`: Gneis: schiefrig: Biotit

- `15111550`: Gneis: schiefrig: Chlorit

- `15111551`: Gneis: schiefrig: Hornblende

- `15111552`: Gneis: schiefrig-augig

- `15111266`: Kalkstein: spätig: Glaukonit

- `15111267`: Kalkstein: spätig: Glaukonit-Chert

- `15111268`: Kalkstein: spätig: Ooide

- `15111269`: Kalkstein: stromatolithisch

- `15111270`: Kalkstein: stromatolithisch: Eisenmineralien-Phosphorit

- `15111271`: Kalkstein: tonig

- `15111272`: Kalkstein: tonig: Bioklasten

- `15111273`: Kalkstein: tonig: Chert

- `15111274`: Kalkstein: tonig-schiefrig

- `15111275`: Kalkstein: tufig

- `15111276`: Tuff: kalkig

- `15111277`: Dolomitstein

- `15111278`: Dolomitstein: Bioklasten

- `15111279`: Dolomitstein: Bitumen

- `15111280`: Dolomitstein: kalkig

- `15111281`: Dolomitstein: kieselig

- `15111282`: Dolomitstein: mikritisch

- `15111283`: Dolomitstein: Ooide

- `15111284`: Dolomitstein: Ooide-Chert

- `15111285`: Dolomitstein: sandig

- `15111286`: Dolomitstein: sandig-siltig

- `15111287`: Dolomitstein: sandig-tonig

- `15111288`: Dolomitstein: sandig-tonig: Bitumen

- `15111289`: Dolomitstein: schiefrig

- `15111290`: Dolomitstein: siltig

- `15111291`: Dolomitstein: siltig-tonig

- `15111292`: Dolomitstein: spätig

- `15111293`: Dolomitstein: spätig: Bioklasten

- `15111294`: Dolomitstein: stromatolithisch

- `15111295`: Dolomitstein: stromatolithisch: Chert

- `15111296`: Dolomitstein: tonig

- `15111297`: Rauwacke

- `15111298`: Rauwacke: sandig

- `15111299`: Rauwacke: sedimentär

- `15111300`: Rauwacke: kataklastisch

- `15111301`: Evaporit

- `15111302`: Evaporit: Anhydrit

- `15111303`: Evaporit: Gips

- `15111304`: Evaporit: Halit

- `15111305`: Evaporit: Sulfat

- `15111306`: Evaporit: tonig

- `15111307`: Evaporit: tonig: Anhydrit

- `15111308`: Evaporit: tonig: Gips

- `15111309`: Gestein: kieselig

- `15111310`: Gestein: kieselig-sedimentär

- `15111311`: Gestein: kieselig-kryptokristallin

- `15111312`: Gestein: kieselig-pedogen

- `15111313`: Gestein: kieselig: Radiolarien

- `15111314`: Gestein: kieselig: Schwämme

- `15111315`: Gestein: kieselig-metamorph

- `15111316`: Gestein: Phosphorit

- `15111317`: Gestein: organisch

- `15111318`: Gestein: organisch: Anthrazit

- `15111319`: Gestein: organisch: Kohle

- `15111320`: Gestein: organisch: Lignit

- `15111321`: Gestein: pedogen

- `15111322`: Gestein: residual

- `15111323`: Gestein: residual: Eisenmineralien

- `15111324`: Gestein: residual: Silikat

- `15111325`: Gestein: residual: Silikat-Eisenmineralien

- `15111326`: Gestein: residual-sandig

- `15111327`: Gestein: residual-sandig: Quarz

- `15111328`: Gestein: residual-siltig

- `15111329`: Gestein: residual-tonig

- `15111330`: Gestein: residual-tonig: Eisenpisoide

- `15111331`: Gestein: residual-tonig: Kaolinit

- `15111332`: Gestein: residual-tonig: Limonit

- `15111333`: Gestein: Eisenmineralien

- `15111334`: Gestein: Eisenooide

- `15111335`: Gestein: Eisenpisoide

- `15111336`: Gestein: pyroklastisch

- `15111337`: Ignimbrit

- `15111338`: Tuff

- `15111339`: Tuff: vulkanisch

- `15111340`: Tuff: vulkanisch: Asche

- `15111341`: Tuff: vulkanisch: Kristalle

- `15111342`: Tuff: vulkanisch: Lapilli

- `15111343`: Bentonit

- `15111344`: Gestein: kristallin

- `15111345`: Gestein: saur

- `15111346`: Gestein: basisch

- `15111347`: Gestein: magmatisch

- `15111348`: Gestein: vulkanisch

- `15111349`: Gestein: vulkanisch: Karbonat

- `15111350`: Gestein: saur-vulkanisch

- `15111351`: Gestein: rhyolithisch

- `15111352`: Rhyolith

- `15111353`: Rhyolith: Alkalifeldspat

- `15111354`: Rhyolith: ignimbritisch

- `15111355`: Rhyolith: porphyrisch

- `15111356`: Gestein: dazitisch

- `15111357`: Dazit

- `15111358`: Dazit: rhyolithisch

- `15111359`: Gestein: latitisch

- `15111360`: Latit

- `15111361`: Gestein: trachytisch

- `15111362`: Trachyt

- `15111363`: Trachyt: Alkalifeldspat

- `15111364`: Gestein: andesitisch

- `15111365`: Andesit

- `15111366`: Gestein: basisch-vulkanisch

- `15111367`: Gestein: basaltisch

- `15111368`: Basalt

- `15111369`: Basalt: Olivin

- `15111370`: Basalt: verwittert: Albit

- `15111371`: Gestein: phonolithisch

- `15111372`: Phonolith

- `15111373`: Phonolith: tephritisch

- `15111374`: Gestein: tephritisch

- `15111375`: Tephrit

- `15111376`: Tephrit: phonolithisch

- `15111377`: Basanit

- `15111378`: Gestein: foiditisch

- `15111379`: Foidit

- `15111380`: Tuffit

- `15111381`: Gestein: gangartig

- `15111382`: Gestein: gangartig: Quarz

- `15111383`: Gestein: saur-gangartig

- `15111384`: Aplit

- `15111385`: Pegmatit

- `15111386`: Granophyr

- `15111387`: Gestein: basisch-gangartig

- `15111388`: Rodingit

- `15111389`: Gestein: plutonisch

- `15111390`: Gestein: granitisch

- `15111391`: Granit

- `15111392`: Granit: Alkalifeldspat

- `15111393`: Granit: aplitisch

- `15111394`: Granit: aplitisch: Granat

- `15111395`: Granit: Biotit

- `15111396`: Granit: Biotit-Cordierit

- `15111397`: Granit: Biotit-Granat

- `15111398`: Granit: Biotit-Muskovit

- `15111399`: Granit: Hornblende

- `15111400`: Granit: metasomatisch

- `15111401`: Granit: mikrokristallin

- `15111402`: Granit: mikrokristallin-porphyrisch

- `15111403`: Granit: monzonitisch

- `15111404`: Granit: mylonitisch

- `15111405`: Granit: porphyrisch

- `15111406`: Granit: porphyrisch: Biotit

- `15111407`: Granit: porphyrisch: Hornblende

- `15111408`: Granit: schiefrig

- `15111409`: Granit: syenitisch

- `15111410`: Granodiorit

- `15111411`: Granodiorit: aplitisch

- `15111412`: Granodiorit: Hornblende

- `15111413`: Granodiorit: porphyrisch

- `15111414`: Granodiorit: schiefrig

- `15111415`: Monzonit

- `15111416`: Monzonit: Feldspatoid

- `15111417`: Monzonit: porphyrisch: Quarz

- `15111418`: Monzonit: Quarz

- `15111419`: Tonalit

- `15111420`: Tonalit: Biotit

- `15111421`: Tonalit: Biotit-Hornblende

- `15111422`: Gestein: syenitisch

- `15111423`: Syenit

- `15111424`: Syenit: Alkalifeldspat

- `15111425`: Syenit: Feldspatoid

- `15111426`: Syenit: Nephelin

- `15111427`: Syenit: porphyrisch: Quarz

- `15111428`: Syenit: Quarz

- `15111429`: Syenit: Quarz-Hornblende

- `15111430`: Gestein: dioritisch

- `15111431`: Diorit

- `15111432`: Diorit: Biotit-Hornblende

- `15111433`: Diorit: migmatitisch

- `15111434`: Diorit: mikrokristallin

- `15111435`: Diorit: monzonitisch

- `15111436`: Diorit: porphyrisch

- `15111553`: Gneis: sedimentär

- `15111554`: Gneis: Serizit

- `15111555`: Gneis: Serizit-Granat

- `15111556`: Granulit

- `15111557`: Granulit: Biotit-Granat

- `15111558`: Granulit: Feldspat-Granat

- `15111559`: Migmatit

- `15111560`: Migmatit: Cordierit

- `15111561`: Phyllit

- `15111562`: Phyllit: Graphit

- `15111563`: Phyllit: kalkig

- `15111564`: Phyllit: Quarz

- `15111565`: Schiefer

- `15111566`: Schiefer: Aktinolith

- `15111567`: Schiefer: Amphibol

- `15111568`: Schiefer: Anthrazit

- `15111569`: Schiefer: Antigorit

- `15111570`: Schiefer: augig: Glimmer

- `15111571`: Schiefer: Biotit

- `15111572`: Schiefer: Biotit-Apatit

- `15111573`: Schiefer: Chlorit

- `15111574`: Schiefer: Chlorit-Epidot

- `15111575`: Schiefer: Chlorit-Talk

- `15111576`: Schiefer: Chloritoid

- `15111577`: Schiefer: Chloritoid-Kyanit

- `15111578`: Schiefer: Glaukophan

- `15111579`: Schiefer: Glimmer

- `15111580`: Schiefer: Glimmer-Chlorit

- `15111581`: Schiefer: Glimmer-Chloritoid

- `15111582`: Schiefer: Glimmer-Granat

- `15111583`: Schiefer: Glimmer-Graphit

- `15111584`: Schiefer: Glimmer-Hornblende

- `15111585`: Schiefer: Granat

- `15111586`: Schiefer: Graphit

- `15111587`: Schiefer: Hornblende

- `15111588`: Schiefer: Hornblende-Granat

- `15111589`: Schiefer: kalkig

- `15111590`: Schiefer: kalkig: Glimmer

- `15111591`: Schiefer: kalkig: Serizit

- `15111592`: Schiefer: kalkig: Zoisit

- `15111593`: Schiefer: kieselig

- `15111594`: Schiefer: Kohle

- `15111595`: Schiefer: konglomeratisch

- `15111596`: Schiefer: konglomeratisch-kalkig

- `15111597`: Schiefer: Kyanit

- `15111598`: Schiefer: mergelig

- `15111599`: Schiefer: Muskovit-Albit

- `15111600`: Schiefer: Quarz

- `15111601`: Schiefer: Quarz-Chlorit

- `15111602`: Schiefer: Quarz-Glimmer

- `15111603`: Schiefer: Quarz-Serizit

- `15111604`: Schiefer: sandig

- `15111605`: Schiefer: sandig-kalkig

- `15111606`: Schiefer: sandig-tonig

- `15111607`: Schiefer: Serizit

- `15111608`: Schiefer: Serizit-Chlorit

- `15111609`: Schiefer: Serizit-Staurolith

- `15111610`: Schiefer: Talk

- `15111611`: Schiefer: Talk-Kyanit

- `15111612`: Schiefer: Talk-Serpentin

- `15111613`: Schiefer: Talk-Tremolit

- `15111614`: Schiefer: tonig

- `15111615`: Schiefer: tonig: Anthrazit

- `15111616`: Schiefer: tonig: Bitumen

- `15111617`: Schiefer: tonig: Graphit

- `15111618`: Schiefer: tonig-kalkig

- `15111619`: Schiefer: tonig-kieselig

- `15111620`: Schiefer: tonig-kieselig: Bitumen

- `15111621`: Schiefer: Tremolit

- `15111622`: Schiefer: Turmalin

- `15111623`: Schiefer: Zoisit

- `15111624`: Schiefer: Zoisit-Fuchsit

- `15111625`: Gestein: mafisch

- `15111626`: Prasinit

- `15111627`: Prasinit: Albit-Chlorit

- `15111628`: Prasinit: Chlorit

- `15111629`: Prasinit: schiefrig

- `15111630`: Amphibolit

- `15111631`: Amphibolit: gebändert

- `15111632`: Amphibolit: Granat

- `15111633`: Amphibolit: Hornblende

- `15111634`: Amphibolit: migmatitisch

- `15111635`: Eklogit

- `15111636`: Serpentinit

- `15111637`: Serpentinit: Antigorit

- `15111638`: Serpentinit: brekziös: Karbonat

- `15111639`: Serpentinit: Chrysotil


*Modified values:*

- None





### TOPGIS_GC.GC_LITSTRAT_UNCO
- **Location**: `tables &gt; TOPGIS_GC.GC_LITSTRAT_UNCO &gt; fields &gt; 22 &gt; name`



**Value changed:**
- **From**: GERMAN
- **To**: DESCRIPTION



### TOPGIS_GC.GC_LITSTRAT_UNCO
- **Location**: `tables &gt; TOPGIS_GC.GC_LITSTRAT_UNCO &gt; fields &gt; 21 &gt; name`



**Value changed:**
- **From**: GEOL_CODE_INT
- **To**: GEOLCODE



### TOPGIS_GC.GC_SYSTEM
- **Location**: `tables &gt; TOPGIS_GC.GC_SYSTEM &gt; fields &gt; 22 &gt; name`



**Value changed:**
- **From**: GERMAN
- **To**: DESCRIPTION



### TOPGIS_GC.GC_SYSTEM
- **Location**: `tables &gt; TOPGIS_GC.GC_SYSTEM &gt; fields &gt; 21 &gt; name`



**Value changed:**
- **From**: GEOL_CODE_INT
- **To**: GEOLCODE



### TOPGIS_GC.GC_COMPOSIT
- **Location**: `tables &gt; TOPGIS_GC.GC_COMPOSIT &gt; fields &gt; 22 &gt; name`



**Value changed:**
- **From**: GERMAN
- **To**: DESCRIPTION



### TOPGIS_GC.GC_COMPOSIT
- **Location**: `tables &gt; TOPGIS_GC.GC_COMPOSIT &gt; fields &gt; 21 &gt; name`



**Value changed:**
- **From**: GEOL_CODE_INT
- **To**: GEOLCODE



### TOPGIS_GC.GC_ADMIXTURE
- **Location**: `tables &gt; TOPGIS_GC.GC_ADMIXTURE &gt; fields &gt; 22 &gt; name`



**Value changed:**
- **From**: GERMAN
- **To**: DESCRIPTION



### TOPGIS_GC.GC_ADMIXTURE
- **Location**: `tables &gt; TOPGIS_GC.GC_ADMIXTURE &gt; fields &gt; 21 &gt; name`



**Value changed:**
- **From**: GEOL_CODE_INT
- **To**: GEOLCODE



### TOPGIS_GC.GC_CHARCAT
- **Location**: `tables &gt; TOPGIS_GC.GC_CHARCAT &gt; fields &gt; 22 &gt; name`



**Value changed:**
- **From**: GERMAN
- **To**: DESCRIPTION



### TOPGIS_GC.GC_CHARCAT
- **Location**: `tables &gt; TOPGIS_GC.GC_CHARCAT &gt; fields &gt; 21 &gt; name`



**Value changed:**
- **From**: GEOL_CODE_INT
- **To**: GEOLCODE



### TOPGIS_GC.GC_CHRONO
- **Location**: `tables &gt; TOPGIS_GC.GC_CHRONO &gt; fields &gt; 22 &gt; name`



**Value changed:**
- **From**: GERMAN
- **To**: DESCRIPTION



### TOPGIS_GC.GC_CHRONO
- **Location**: `tables &gt; TOPGIS_GC.GC_CHRONO &gt; fields &gt; 21 &gt; name`



**Value changed:**
- **From**: GEOL_CODE_INT
- **To**: GEOLCODE



### TOPGIS_GC.GC_LITHO
- **Location**: `tables &gt; TOPGIS_GC.GC_LITHO &gt; fields &gt; 22 &gt; name`



**Value changed:**
- **From**: GERMAN
- **To**: DESCRIPTION



### TOPGIS_GC.GC_LITHO
- **Location**: `tables &gt; TOPGIS_GC.GC_LITHO &gt; fields &gt; 21 &gt; name`



**Value changed:**
- **From**: GEOL_CODE_INT
- **To**: GEOLCODE



### TOPGIS_GC.GC_TECTO
- **Location**: `tables &gt; TOPGIS_GC.GC_TECTO &gt; fields &gt; 22 &gt; name`



**Value changed:**
- **From**: GERMAN
- **To**: DESCRIPTION



### TOPGIS_GC.GC_TECTO
- **Location**: `tables &gt; TOPGIS_GC.GC_TECTO &gt; fields &gt; 21 &gt; name`



**Value changed:**
- **From**: GEOL_CODE_INT
- **To**: GEOLCODE



### TOPGIS_GC.GC_LITHO_UNCO
- **Location**: `tables &gt; TOPGIS_GC.GC_LITHO_UNCO &gt; fields &gt; 22 &gt; name`



**Value changed:**
- **From**: GERMAN
- **To**: DESCRIPTION



### TOPGIS_GC.GC_LITHO_UNCO
- **Location**: `tables &gt; TOPGIS_GC.GC_LITHO_UNCO &gt; fields &gt; 21 &gt; name`



**Value changed:**
- **From**: GEOL_CODE_INT
- **To**: GEOLCODE



### TOPGIS_GC.GC_BEDROCK
- **Location**: `featclasses &gt; TOPGIS_GC.GC_BEDROCK &gt; fields &gt; 27 &gt; name`



**Value changed:**
- **From**: RBED_TECTO
- **To**: TECTO



### TOPGIS_GC.GC_BEDROCK
- **Location**: `featclasses &gt; TOPGIS_GC.GC_BEDROCK &gt; fields &gt; 30 &gt; name`



**Value changed:**
- **From**: RBED_ORIG_DESCR
- **To**: DESCRIPTION



### TOPGIS_GC.GC_BEDROCK
- **Location**: `featclasses &gt; TOPGIS_GC.GC_BEDROCK &gt; fields &gt; 32 &gt; name`



**Value changed:**
- **From**: FORM_ATT
- **To**: GEOL_MAPPING_UNIT_ATT_UUID



### TOPGIS_GC.GC_LINEAR_OBJECTS
- **Location**: `featclasses &gt; TOPGIS_GC.GC_LINEAR_OBJECTS &gt; fields &gt; 25 &gt; domain`



**Value changed:**
- **From**: GC_LITSTRAT_BED_CD
- **To**: GC_GEOL_MAPPING_UNIT_CD



### TOPGIS_GC.GC_LINEAR_OBJECTS
- **Location**: `featclasses &gt; TOPGIS_GC.GC_LINEAR_OBJECTS &gt; fields &gt; 40 &gt; domain`



**Value changed:**
- **From**: GC_LITSTRAT_BED_CD
- **To**: GC_GEOL_MAPPING_UNIT_CD



### TOPGIS_GC.GC_POINT_OBJECTS
- **Location**: `featclasses &gt; TOPGIS_GC.GC_POINT_OBJECTS &gt; fields &gt; 24 &gt; domain`



**Value changed:**
- **From**: GC_LITSTRAT_CD
- **To**: GC_GEOL_MAPPING_UNIT_CD



### TOPGIS_GC.GC_POINT_OBJECTS
- **Location**: `featclasses &gt; TOPGIS_GC.GC_POINT_OBJECTS &gt; fields &gt; 25 &gt; domain`



**Value changed:**
- **From**: GC_LITSTRAT_CD
- **To**: GC_GEOL_MAPPING_UNIT_CD



### TOPGIS_GC.GC_POINT_OBJECTS
- **Location**: `featclasses &gt; TOPGIS_GC.GC_POINT_OBJECTS &gt; fields &gt; 26 &gt; domain`



**Value changed:**
- **From**: GC_LITSTRAT_BED_CD
- **To**: GC_GEOL_MAPPING_UNIT_CD



### TOPGIS_GC.GC_POINT_OBJECTS
- **Location**: `featclasses &gt; TOPGIS_GC.GC_POINT_OBJECTS &gt; fields &gt; 56 &gt; domain`



**Value changed:**
- **From**: GC_LITSTRAT_BED_CD
- **To**: GC_GEOL_MAPPING_UNIT_CD



### TOPGIS_GC.GC_UNCO_DESPOSIT
- **Location**: `featclasses &gt; TOPGIS_GC.GC_UNCO_DESPOSIT &gt; fields &gt; 26 &gt; domain`



**Value changed:**
- **From**: GC_LITSTRAT_UNCO_CD
- **To**: GC_GEOL_MAPPING_UNIT_CD






## 🗑️ Removed Iterable Items


### Removed from TOPGIS_GC.GC_LITSTRAT_UNCO table


>>> Field: GEOL_CODE  None




### Removed from TOPGIS_GC.GC_SYSTEM table


>>> Field: GEOL_CODE  None




### Removed from TOPGIS_GC.GC_COMPOSIT table


>>> Field: GEOL_CODE  None




### Removed from TOPGIS_GC.GC_ADMIXTURE table


>>> Field: GEOL_CODE  None




### Removed from TOPGIS_GC.GC_CHARCAT table


>>> Field: GEOL_CODE  None




### Removed from TOPGIS_GC.GC_CHRONO table


>>> Field: GEOL_CODE  None




### Removed from TOPGIS_GC.GC_LITHO table


>>> Field: GEOL_CODE  None




### Removed from TOPGIS_GC.GC_TECTO table


>>> Field: GEOL_CODE  None




### Removed from TOPGIS_GC.GC_LITHO_UNCO table


>>> Field: GEOL_CODE  None




### Removed from TOPGIS_GC.GC_BEDROCK featclasse


>>> Field: RBED_CHRONO_T  GC_CHRONO_CD




### Removed from TOPGIS_GC.GC_BEDROCK featclasse


>>> Field: RBED_CHRONO_B  GC_CHRONO_CD




### Removed from TOPGIS_GC.GC_BEDROCK featclasse


>>> Field: RBED_CHRONO_B_LOC  GC_CHRONO_CD




### Removed from TOPGIS_GC.GC_BEDROCK featclasse


>>> Field: RBED_CHRONO_T_LOC  GC_CHRONO_CD




### Removed from TOPGIS_GC.GC_BEDROCK featclasse


>>> Field: RBED_HARMOS_REV  GC_HARMOS_REV_CD




### Removed from TOPGIS_GC.GC_BEDROCK featclasse


>>> Field: RBED_INDEX  None






---

*Report generated by ESRI Database Schema Diff Tool*


toto

