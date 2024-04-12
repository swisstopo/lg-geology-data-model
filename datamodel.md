
# Datenmodell Geologie, Version 3.5 #


![Extrait GeoCover vers le Moléson](geocover.png "Moléson")





\pagebreak





## Theme ROCK_BODIES ##

### Class Unconsolidated_Deposits_PT ###
Die Klasse Unconsolidated_Deposits_PT umfasst einzelne Gesteine (Korngrösse: Steine bis Blöcke), die durch gravitative, glaziale oder anthropogene Transportprozesse an ihren heutigen Ort gelangten, respektive sich an Ort und Stelle durch Verwitterung des umliegenden Gesteins gebildet haben.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 14401                                       |  
2 | **status**                | [CodedDomain](#unconsolidated-deposits-pt-status)                    | Zustand der Objektart 
[]()           | Cardinality [1] |                                                      |  
3 | **rock_type**                | [CodedDomain](#unconsolidated-deposits-pt-rock-type)                    | Gesteinstyp (Kristallingestein / Sedimentgestein) 
[]()           | Cardinality [0..1] |                                                      |  
4 | **rock_spe**                | [CodedDomain](#unconsolidated-deposits-pt-rock-spe)                    | Bezeichnung des Leitgesteins 
[]()           | Cardinality [0..1] |                                                      |  
5 | **mat_type**                | [CodedDomain](#unconsolidated-deposits-pt-mat-type)                    | Materialbezeichnung (lithologische Einheit) 
[]()           | Cardinality [0..1] |                                                      |  
6 | **orig_descr**                | string                                    | Originalbezeichnung gemäss der Legende der zugrundeliegenden geologischen Karte 
[]()           | Cardinality [0..1] |                                        |  
7 | **protected**                | boolean                                    | Geschütztes geologisches Objekt 
[]()           | Cardinality [0..1] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14401001 | Runc erratischer Block | Runc erratischer Block     |
|14401002 | Runc Schwarm erratischer Blöcke | Runc Schwarm erratischer Blöcke     |
|14401003 | Runc anthropogene Ansammlung von erratischen Blöcken | Runc anthropogene Ansammlung von erratischen Blöcken     |
|14401004 | Runc Wanderblock | Runc Wanderblock     |
|14401005 | Runc Geschiebe | Runc Geschiebe     |
|14401006 | Runc Sturzblock | Runc Sturzblock     |
|14401007 | Runc Lesesteinhaufen | Runc Lesesteinhaufen     |
|14401008 | Runc Verwitterungsrückstände (Gerölle und/oder Konkretionen) | Runc Verwitterungsrückstände (Gerölle und/oder Konkretionen)     |


   

#### Attribute status{#unconsolidated-deposits-pt-status}
_Zustand der Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14402003 | in Situ | in Situ     |
|14402004 | umgelagert | umgelagert     |
|14402001 | versetzt | versetzt     |
|14402002 | zerstört | zerstört     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute rock_type{#unconsolidated-deposits-pt-rock-type}
_Gesteinstyp (Kristallingestein / Sedimentgestein)_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14403003 | Basisches / Ultrabasisches Gestein | Basisches / Ultrabasisches Gestein     |
|14403001 | Kristallingestein | Kristallingestein     |
|14403002 | Sedimentgestein | Sedimentgestein     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute rock_spe{#unconsolidated-deposits-pt-rock-spe}
_Bezeichnung des Leitgesteins_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14404008 | Aare-Granit | Aare-Granit     |
|14404017 | Albula-Granit | Albula-Granit     |
|14404002 | Allalin-Gabbro | Allalin-Gabbro     |
|14404024 | Alpines Sedimentgestein | Alpines Sedimentgestein     |
|14404020 | Degersheim-Kalknagelfluh | Degersheim-Kalknagelfluh     |
|14404009 | Gastern-Granit | Gastern-Granit     |
|14404012 | Glarner Verrucano | Glarner Verrucano     |
|14404007 | Grindelwald-Marmor | Grindelwald-Marmor     |
|14404026 | Gruontal-Konglomerat | Gruontal-Konglomerat     |
|14404010 | Habkern-Granit | Habkern-Granit     |
|14404006 | Hohgant-Sandstein | Hohgant-Sandstein     |
|14404014 | Ilanz-Verrucano | Ilanz-Verrucano     |
|14404013 | Kalknagelfluh des Speer- und Stockberggebietes | Kalknagelfluh des Speer- und Stockberggebietes     |
|14404023 | Karbon-Brekzie | Karbon-Brekzie     |
|14404015 | Mels-Sandstein | Mels-Sandstein     |
|14404025 | Molassegestein | Molassegestein     |
|14404003 | Mont-Blanc-Granit | Mont-Blanc-Granit     |
|14404022 | Muschelsandstein | Muschelsandstein     |
|14404005 | Niesen-Brekzie | Niesen-Brekzie     |
|14404018 | Punteglias-Granit | Punteglias-Granit     |
|14404019 | Rofna-Porphyr | Rofna-Porphyr     |
|14404004 | Serpentinit | Serpentinit     |
|14404016 | Taspinit-Brekzie | Taspinit-Brekzie     |
|14404021 | Taveyannaz-Sandstein | Taveyannaz-Sandstein     |
|14404001 | Vallorcine-Konglomerat | Vallorcine-Konglomerat     |
|14404011 | Windgällen-Porphyr | Windgällen-Porphyr     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute mat_type{#unconsolidated-deposits-pt-mat-type}
_Materialbezeichnung (lithologische Einheit)_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15101039 | Alluvion, undifferenziert | Alluvion, undifferenziert     |
|15101067 | anthropogene Elemente, undifferenziert | anthropogene Elemente, undifferenziert     |
|15101062 | äolischer Sand, Flugsand | äolischer Sand, Flugsand     |
|15101061 | äolisches Sediment, undifferenziert | äolisches Sediment, undifferenziert     |
|15101071 | Auffüllung | Auffüllung     |
|15101070 | Aufschüttung, Damm | Aufschüttung, Damm     |
|15101041 | Bachschutt | Bachschutt     |
|15101006 | Bergsturzablagerung | Bergsturzablagerung     |
|15101015 | Blockgletscher | Blockgletscher     |
|15101010 | Blockschutt | Blockschutt     |
|15101072 | Deponie | Deponie     |
|15101049 | detritische Verlandungsbildung | detritische Verlandungsbildung     |
|15101075 | dünne Lockermaterialbedeckung | dünne Lockermaterialbedeckung     |
|15101086 | Entwässerungssediment | Entwässerungssediment     |
|15101007 | Felssturzablagerung | Felssturzablagerung     |
|15101040 | fluviatiler Schotter | fluviatiler Schotter     |
|15101026 | fluviatiles Sediment, undifferenziert | fluviatiles Sediment, undifferenziert     |
|15101035 | gemischter Schutt | gemischter Schutt     |
|15101076 | geringmächtige Lockergesteinsbedeckung | geringmächtige Lockergesteinsbedeckung     |
|15101031 | glazifluviatiler Schotter | glazifluviatiler Schotter     |
|15101028 | glazifluviatiles Sediment, undifferenziert | glazifluviatiles Sediment, undifferenziert     |
|15101019 | glazigenes Sediment, undifferenziert | glazigenes Sediment, undifferenziert     |
|15101047 | glazilakustrisches Deltasediment | glazilakustrisches Deltasediment     |
|15101046 | glazilakustrisches Sediment, undifferenziert | glazilakustrisches Sediment, undifferenziert     |
|15101003 | gravitative Sedimente und Verwitterungsbildungen, undifferenziert | gravitative Sedimente und Verwitterungsbildungen, undifferenziert     |
|15101079 | Gyttja | Gyttja     |
|15101073 | Halde | Halde     |
|15101014 | Hanglehm, Schwemmlehm | Hanglehm, Schwemmlehm     |
|15101009 | Hangschutt | Hangschutt     |
|15101081 | hydrochemische Bildungen (Kalksinter) | hydrochemische Bildungen (Kalksinter)     |
|15101083 | In-situ-Verwitterungsschutt | In-situ-Verwitterungsschutt     |
|15101069 | künstliche Ablagerung, undifferenziert | künstliche Ablagerung, undifferenziert     |
|15101057 | lakustrisches Deltasediment | lakustrisches Deltasediment     |
|15101044 | lakustrisches Sediment, undifferenziert | lakustrisches Sediment, undifferenziert     |
|15101008 | Lawinenschutt | Lawinenschutt     |
|15101054 | Lignit (palustrisches Sediment) | Lignit (palustrisches Sediment)     |
|15101001 | Lockergestein | Lockergestein     |
|15101063 | Löss, Lösslehm | Löss, Lösslehm     |
|15101021 | Moräne (Till), undifferenziert | Moräne (Till), undifferenziert     |
|15101024 | Moräne auf Gletscher oder Toteis (Glacier or Dead Ice covered by Till) | Moräne auf Gletscher oder Toteis (Glacier or Dead Ice covered by Till)     |
|15101037 | Murgangablagerung | Murgangablagerung     |
|15101050 | palustrisches Sediment | palustrisches Sediment     |
|15101051 | palustrisches Sediment, undifferenziert | palustrisches Sediment, undifferenziert     |
|15101013 | Plateaulehm | Plateaulehm     |
|15101080 | Quelltuff (Kalksinter, Lockergestein) | Quelltuff (Kalksinter, Lockergestein)     |
|15101030 | randglazialer Schotter | randglazialer Schotter     |
|15101033 | Rückzugsschotter | Rückzugsschotter     |
|15101017 | Rutschmasse | Rutschmasse     |
|15101087 | Sedimentärer Gang (clastic dike) | Sedimentärer Gang (clastic dike)     |
|15101058 | Seebodensediment | Seebodensediment     |
|15101059 | Seekreide | Seekreide     |
|15101034 | Stauschotter | Stauschotter     |
|15101056 | Strandablagerungen | Strandablagerungen     |
|15101084 | strukturierter Hangschutt | strukturierter Hangschutt     |
|15101005 | Sturzablagerung, undifferenziert | Sturzablagerung, undifferenziert     |
|15101048 | subaquatisch abgelagerte Moräne (Waterlaid Till) | subaquatisch abgelagerte Moräne (Waterlaid Till)     |
|15101052 | Sumpf | Sumpf     |
|15101078 | tiefgründige Verwitterungsdecke | tiefgründige Verwitterungsdecke     |
|15101053 | Torfmoor, Torf | Torfmoor, Torf     |
|15101082 | Travertin (Kalksinter, Lockergestein) | Travertin (Kalksinter, Lockergestein)     |
|15101085 | Tsunamiablagerung | Tsunamiablagerung     |
|15101042 | Überschwemmungssediment | Überschwemmungssediment     |
|15101012 | Verwitterungslehm, undifferenziert | Verwitterungslehm, undifferenziert     |
|15101032 | Vorstossschotter | Vorstossschotter     |
|15101065 | vulkanische Asche | vulkanische Asche     |
|15101016 | zerrüttete Sackungsmasse | zerrüttete Sackungsmasse     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute orig_descr
_Originalbezeichnung gemäss der Legende der zugrundeliegenden geologischen Karte_
_Datentyp:  string_



   

#### Attribute protected
_Geschütztes geologisches Objekt_
_Datentyp:  boolean_



   

### Class Unconsolidated_Deposits_PLG ###
Die Klasse Unconsolidated_Deposits_PLG beinhaltet alle flächenhaft
ausgeschiedenen Lockergesteine.\
Die Angabe, ob eine Lockergesteinsmasse bewegt (durch Gravitation versetzt) wurde, geht
aus der Klasse Instabilities_within_Unconsolidated_Deposits_PLG (Thema
Geomorphology) hervor. Eine Ausnahme bilden Lockergesteinsmassen,
welche unter dem Einfluss der Schwerkraft bewegt wurden und keine
Angaben zum Ausgangsmaterial enthalten (Rutschmassen oder zerrüttete
Gesteinsmassen «Sackungsmassen»).\
Solche Lockergesteine werden sowohl in der Klasse Unconsolidated_Deposits_PLG als auch in der Klasse
Instabilities_with_in_Unconsolidated_Deposits_PLG erfasst. Zur näheren
Erklärung der verschiedenen Objektarten sind im Anhang A einige
Fallbeispiele abgebildet.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 14517                                       |  
2 | **litstrat**                | [CodedDomain](#unconsolidated-deposits-plg-litstrat)                    |  
[]()           | Cardinality [1] |                                                      |  
3 | **litho**                | [CodedDomain](#unconsolidated-deposits-plg-litho)                    |  
[]()           | Cardinality [1..3] |                                                      |  
4 | **chrono_t**                | [CodedDomain](#unconsolidated-deposits-plg-chrono-t)                    |  
[]()           | Cardinality [1] |                                                      |  
5 | **chrono_b**                | [CodedDomain](#unconsolidated-deposits-plg-chrono-b)                    |  
[]()           | Cardinality [1] |                                                      |  
6 | **mat_type**                |                                     |  
[]()           | Cardinality [0..3] | Lithostratigraphic_Units_Litho                                       |  
7 | **buried_out**                | boolean                                    |  
[]()           | Cardinality [1] |                                        |  
8 | **composit**                | table                                    |  
[]()           | Cardinality [0..3] | gc_composit                                       |  
9 | **admixture**                | table                                    |  
[]()           | Cardinality [0..2] | gc_admixture                                       |  
10 | **structur**                | [CodedDomain](#unconsolidated-deposits-plg-structur)                    | Textur des Lockergesteins 
[]()           | Cardinality [0..1] |                                                      |  
11 | **charact**                | table                                    | Spezifische Eigenschaft 
[]()           | Cardinality [0..3] | gc_charcat                                       |  
12 | **morpholo**                | [CodedDomain](#unconsolidated-deposits-plg-morpholo)                    | Morphologie der Lockergesteinseinheit 
[]()           | Cardinality [0..1] |                                                      |  
13 | **glac_type**                | [CodedDomain](#unconsolidated-deposits-plg-glac-type)                    | Gletschertyp; Attribut nur für Moränen 
[]()           | Cardinality [0..1] |                                                      |  
14 | **ref_year**                | string                                    | Zeitpunkt oder Zeitperiode. Zum Beispiel «1940 1943, Periode der Drainage» (muss präzisiert werden) 
[]()           | Cardinality [0..1] |                                        |  
15 | **thin_cover**                | [CodedDomain](#unconsolidated-deposits-plg-thin-cover)                    | Lockermaterialbedeckung, wenn vorhanden. 
[]()           | Cardinality [0..1] |                                                      |  
16 | **orig_descr**                |                                     | Originalbezeichnung gemäss der Legende der zugrundeliegenden geologischen Karte 
[]()           | Cardinality [1] | string                                       |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14517001 | Runc Lockergestein | Runc Lockergestein     |


   

#### Attribute litstrat{#unconsolidated-deposits-plg-litstrat}
__

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15201044 | 1. letzteiszeitlischs Vorstoss | 1. letzteiszeitlischs Vorstoss     |
|15201043 | 2. letzteiszeitlischs Vorstoss | 2. letzteiszeitlischs Vorstoss     |
|15201210 | Aabach-Schotter | Aabach-Schotter     |
|15201055 | Aarau-Schotter | Aarau-Schotter     |
|15201167 | Aarburg-Schotter | Aarburg-Schotter     |
|15201136 | Aare-Schotter | Aare-Schotter     |
|15201271 | Aatal-Seebodenlehm | Aatal-Seebodenlehm     |
|15201075 | Aathal-Schotter | Aathal-Schotter     |
|15201540 | Alluvion von Ransun | Alluvion von Ransun     |
|15201012 | Altberg-Till | Altberg-Till     |
|15201183 | Alte Doubsschotter | Alte Doubsschotter     |
|15201135 | Altenburg-Fulach-Terrasse | Altenburg-Fulach-Terrasse     |
|15201001 | Ältere Ablagerungen, undifferenziert | Ältere Ablagerungen, undifferenziert     |
|15201071 | Ältere Beckenfüllungen | Ältere Beckenfüllungen     |
|15201189 | Alterswil-Schotter | Alterswil-Schotter     |
|15201028 | Ämmert-Schotter | Ämmert-Schotter     |
|15201029 | Ämmert-Till | Ämmert-Till     |
|15201512 | Ämmet-Schotter | Ämmet-Schotter     |
|15201160 | Attiswil-Schotter | Attiswil-Schotter     |
|15201326 | Bachschutt der Gamsa | Bachschutt der Gamsa     |
|15201331 | Bachschutt der Gürbe | Bachschutt der Gürbe     |
|15201328 | Bachschutt der Lonza | Bachschutt der Lonza     |
|15201329 | Bachschutt der Saltina | Bachschutt der Saltina     |
|15201330 | Bachschutt der Vispa | Bachschutt der Vispa     |
|15201323 | Bachschutt des Baltschiederbachs | Bachschutt des Baltschiederbachs     |
|15201324 | Bachschutt des Bietschbachs | Bachschutt des Bietschbachs     |
|15201325 | Bachschutt des Chelchbachs | Bachschutt des Chelchbachs     |
|15201327 | Bachschutt des Jolibachs | Bachschutt des Jolibachs     |
|15201332 | Bachschutt des Lombachs | Bachschutt des Lombachs     |
|15201550 | Balm-Schotter | Balm-Schotter     |
|15201248 | Bänkel-Schotter | Bänkel-Schotter     |
|15201548 | Bannhalden-Schotter | Bannhalden-Schotter     |
|15201256 | Bannholz-Schotter | Bannholz-Schotter     |
|15201097 | Bärengraben-Schotter und -Till | Bärengraben-Schotter und -Till     |
|15201336 | Bärenholz-Till | Bärenholz-Till     |
|15201194 | Bennau-Schotter | Bennau-Schotter     |
|15201017 | Berg-Schotter | Berg-Schotter     |
|15201532 | Bergsturzablagerung von Bargis | Bergsturzablagerung von Bargis     |
|15201533 | Bergsturzablagerung von Fidaz | Bergsturzablagerung von Fidaz     |
|15201531 | Bergsturzablagerung von Ralligen (im Thunersee) | Bergsturzablagerung von Ralligen (im Thunersee)     |
|15201299 | Bergsturzablagerungen vom Chapf | Bergsturzablagerungen vom Chapf     |
|15201302 | Bergsturzablagerungen vom Delenwald | Bergsturzablagerungen vom Delenwald     |
|15201301 | Bergsturzablagerungen vom Drussetschawald | Bergsturzablagerungen vom Drussetschawald     |
|15201306 | Bergsturzablagerungen vom Kernwald | Bergsturzablagerungen vom Kernwald     |
|15201460 | Bergsturzablagerungen vom Stützwald | Bergsturzablagerungen vom Stützwald     |
|15201296 | Bergsturzablagerungen von Brienz | Bergsturzablagerungen von Brienz     |
|15201298 | Bergsturzablagerungen von Brüsis | Bergsturzablagerungen von Brüsis     |
|15201291 | Bergsturzablagerungen von Castasegna | Bergsturzablagerungen von Castasegna     |
|15201288 | Bergsturzablagerungen von Chessel-Noville | Bergsturzablagerungen von Chessel-Noville     |
|15201287 | Bergsturzablagerungen von Chiètres | Bergsturzablagerungen von Chiètres     |
|15201300 | Bergsturzablagerungen von Derborence | Bergsturzablagerungen von Derborence     |
|15201303 | Bergsturzablagerungen von Elm | Bergsturzablagerungen von Elm     |
|15201297 | Bergsturzablagerungen von Flims | Bergsturzablagerungen von Flims     |
|15201304 | Bergsturzablagerungen von Goldau | Bergsturzablagerungen von Goldau     |
|15201290 | Bergsturzablagerungen von Gwelber-Laui-Weid | Bergsturzablagerungen von Gwelber-Laui-Weid     |
|15201305 | Bergsturzablagerungen von Iragell | Bergsturzablagerungen von Iragell     |
|15201295 | Bergsturzablagerungen von Mutta | Bergsturzablagerungen von Mutta     |
|15201289 | Bergsturzablagerungen von Novalles-Vugelles | Bergsturzablagerungen von Novalles-Vugelles     |
|15201293 | Bergsturzablagerungen von Prapan | Bergsturzablagerungen von Prapan     |
|15201294 | Bergsturzablagerungen von Schaingels | Bergsturzablagerungen von Schaingels     |
|15201286 | Bergsturzablagerungen von Sierre | Bergsturzablagerungen von Sierre     |
|15201292 | Bergsturzablagerungen von Sogno | Bergsturzablagerungen von Sogno     |
|15201310 | Bergsturzablagerungen von Tamins | Bergsturzablagerungen von Tamins     |
|15201307 | Bergsturzablagerungen von Triesenberg | Bergsturzablagerungen von Triesenberg     |
|15201053 | Beringen-Eiszeit | Beringen-Eiszeit     |
|15201164 | Berken-Sand | Berken-Sand     |
|15201163 | Berken-Schotter | Berken-Schotter     |
|15201156 | Bersturzmasse von Selzach | Bersturzmasse von Selzach     |
|15201523 | Beuggen-Schotter | Beuggen-Schotter     |
|15201153 | Bick-Till | Bick-Till     |
|15201263 | Bire-Bergsturzablagerungen | Bire-Bergsturzablagerungen     |
|15201462 | Birkenhof-Formation | Birkenhof-Formation     |
|15201009 | Birmenstorf-Vergletscherung (2. LGM-Vorstoss) | Birmenstorf-Vergletscherung (2. LGM-Vorstoss)     |
|15201013 | Birmenstorf-Vorstoss | Birmenstorf-Vorstoss     |
|15201014 | Birr-Schotter | Birr-Schotter     |
|15201052 | Birrfeld- und Klettgau-Paläoböden | Birrfeld- und Klettgau-Paläoböden     |
|15201006 | Birrfeld-Eiszeit (Letzte Eiszeit) | Birrfeld-Eiszeit (Letzte Eiszeit)     |
|15201255 | Bohlingen-Schotter | Bohlingen-Schotter     |
|15201308 | Bonaduz-Formation | Bonaduz-Formation     |
|15201309 | Bonfol-Ton | Bonfol-Ton     |
|15201465 | Böschmatt-Schotter | Böschmatt-Schotter     |
|15201466 | Bramegg-Schotter | Bramegg-Schotter     |
|15201221 | Brandflue-Schotter | Brandflue-Schotter     |
|15201150 | Breite-Terrasse | Breite-Terrasse     |
|15201520 | Bruderhäusle-Schotter | Bruderhäusle-Schotter     |
|15201339 | Brüggstutz-Schotter | Brüggstutz-Schotter     |
|15201120 | Buechen-Formation | Buechen-Formation     |
|15201470 | Büel-Schotter | Büel-Schotter     |
|15201469 | Büelm-Schotter | Büelm-Schotter     |
|15201085 | Buerfeld-Schotter | Buerfeld-Schotter     |
|15201471 | Bünten-Schotter | Bünten-Schotter     |
|15201094 | Bünten-Till | Bünten-Till     |
|15201558 | Burgacher-Schotter | Burgacher-Schotter     |
|15201243 | Butteberg-Schotter | Butteberg-Schotter     |
|15201458 | Ceppo | Ceppo     |
|15201233 | Chälen-Schotter | Chälen-Schotter     |
|15201234 | Chälen-Till | Chälen-Till     |
|15201559 | Chatzenstig-Schotter | Chatzenstig-Schotter     |
|15201223 | Chatzenstrick-Schotter | Chatzenstrick-Schotter     |
|15201258 | Chilchstapfen-Schotter | Chilchstapfen-Schotter     |
|15201191 | Chisetal-Schotter | Chisetal-Schotter     |
|15201242 | Chräjeloch-Schotter | Chräjeloch-Schotter     |
|15201214 | Dagmersellen-Vorstoss | Dagmersellen-Vorstoss     |
|15201250 | Deckenschotter, undifferenziert | Deckenschotter, undifferenziert     |
|15201116 | Degermoos-Schotter | Degermoos-Schotter     |
|15201115 | Dürn-Formation | Dürn-Formation     |
|15201472 | Durnagel-Schotter | Durnagel-Schotter     |
|15201473 | Dürrenroth-Schotter | Dürrenroth-Schotter     |
|15201117 | Ebnet-Schotter | Ebnet-Schotter     |
|15201123 | Egg-Schotter | Egg-Schotter     |
|15201119 | Egghalden-Schotter | Egghalden-Schotter     |
|15201547 | Eggholz-Formation | Eggholz-Formation     |
|15201474 | Egghüsli-Schotter | Egghüsli-Schotter     |
|15201197 | Einsiedeln-Lehm | Einsiedeln-Lehm     |
|15201546 | Ellikerholz-Formation | Ellikerholz-Formation     |
|15201284 | Embrach-Seeablagerungen | Embrach-Seeablagerungen     |
|15201144 | Emme-Schotter | Emme-Schotter     |
|15201475 | Emmental-Schotter | Emmental-Schotter     |
|15201030 | Emmet-Vorstoss | Emmet-Vorstoss     |
|15201180 | Endingen-Schotter | Endingen-Schotter     |
|15201159 | Enge-Schotter | Enge-Schotter     |
|15201065 | Engiwald-Vorstoss | Engiwald-Vorstoss     |
|15201054 | Entfelden-Schotter | Entfelden-Schotter     |
|15201476 | Ergolztal-Schotter | Ergolztal-Schotter     |
|15201510 | Ermensee-Schotter | Ermensee-Schotter     |
|15201272 | Eschenbach-Formation | Eschenbach-Formation     |
|15201265 | Fankhusgrabe-Schotter | Fankhusgrabe-Schotter     |
|15201524 | Feldhof-Schotter | Feldhof-Schotter     |
|15201121 | Feusi-Schotter | Feusi-Schotter     |
|15201096 | Fisibach-Schotter | Fisibach-Schotter     |
|15201262 | Fisistock-Bergsturzablagerungen | Fisistock-Bergsturzablagerungen     |
|15201174 | Fislisbach-Schotter | Fislisbach-Schotter     |
|15201154 | Flüe-Till | Flüe-Till     |
|15201011 | Flüefeld-Schotter | Flüefeld-Schotter     |
|15201146 | Flumenthal-Lehm | Flumenthal-Lehm     |
|15201051 | Flurlingen-Quelltuff | Flurlingen-Quelltuff     |
|15201106 | Forenirchel-Schotter | Forenirchel-Schotter     |
|15201105 | Fornech-Schotter | Fornech-Schotter     |
|15201018 | Fornholz-Till | Fornholz-Till     |
|15201217 | Forst-Schotter | Forst-Schotter     |
|15201477 | Gammenthal-Schotter | Gammenthal-Schotter     |
|15201145 | Gäu-Schotter | Gäu-Schotter     |
|15201079 | Geisslingen-Schotter | Geisslingen-Schotter     |
|15201251 | Girenbad-Schotter | Girenbad-Schotter     |
|15201047 | Glazi-lakustrische Serie | Glazi-lakustrische Serie     |
|15201343 | Glütschtal-Formation | Glütschtal-Formation     |
|15201478 | Gondiswil-Formation | Gondiswil-Formation     |
|15201050 | Gondiswil-Interglazial (Letztes Integlazial) | Gondiswil-Interglazial (Letztes Integlazial)     |
|15201203 | Gontenschwil-Lehm | Gontenschwil-Lehm     |
|15201020 | Gontenschwil-Till | Gontenschwil-Till     |
|15201019 | Gontenschwil-Vorstoss | Gontenschwil-Vorstoss     |
|15201038 | Gossau-Interstadial | Gossau-Interstadial     |
|15201169 | Grandson-Formation | Grandson-Formation     |
|15201083 | Gränichen-Schotter | Gränichen-Schotter     |
|15201192 | Grauholz-Schotter | Grauholz-Schotter     |
|15201267 | Grundtal-Schotter | Grundtal-Schotter     |
|15201232 | Gubel-Schotter | Gubel-Schotter     |
|15201275 | Gublen-Schotter | Gublen-Schotter     |
|15201031 | Gündelmoos-Lehm | Gündelmoos-Lehm     |
|15201341 | Guntelsei-Schotter | Guntelsei-Schotter     |
|15201340 | Guntelsei-Till | Guntelsei-Till     |
|15201274 | Günterstall-Schotter | Günterstall-Schotter     |
|15201240 | Gutsch-Schotter | Gutsch-Schotter     |
|15201082 | Habsburg-Eiszeit | Habsburg-Eiszeit     |
|15201080 | Habsburg-Hagenholz-Interglazial | Habsburg-Hagenholz-Interglazial     |
|15201088 | Habsburg-Schotter | Habsburg-Schotter     |
|15201086 | Habsburg-Vergletscherung | Habsburg-Vergletscherung     |
|15201087 | Habsburg-Vorstoss | Habsburg-Vorstoss     |
|15201072 | Hagenholz-Eiszeit | Hagenholz-Eiszeit     |
|15201073 | Hagenholz-Vergletscherung | Hagenholz-Vergletscherung     |
|15201074 | Hagenholz-Vorstoss | Hagenholz-Vorstoss     |
|15201506 | Hagnau-Niveau | Hagnau-Niveau     |
|15201344 | Hahni-Schotter | Hahni-Schotter     |
|15201530 | Hahni-Till | Hahni-Till     |
|15201278 | Halden-Seeablagerungen | Halden-Seeablagerungen     |
|15201208 | Haselbach-Schotter | Haselbach-Schotter     |
|15201479 | Hasewald-Schotter | Hasewald-Schotter     |
|15201264 | Hasle-Schotter | Hasle-Schotter     |
|15201270 | Haslentobel-Schotter | Haslentobel-Schotter     |
|15201564 | Hasli-Formation | Hasli-Formation     |
|15201177 | Hausen-Lehm | Hausen-Lehm     |
|15201178 | Hausen-Moräne | Hausen-Moräne     |
|15201245 | Heitere-Schotter | Heitere-Schotter     |
|15201515 | Heubeerihübel-Schotter | Heubeerihübel-Schotter     |
|15201480 | Hirzmatt-Schotter | Hirzmatt-Schotter     |
|15201244 | Höchi-Schotter | Höchi-Schotter     |
|15201003 | Hochterrasse | Hochterrasse     |
|15201464 | Höhenschotter | Höhenschotter     |
|15201005 | Höhere Deckenschotter | Höhere Deckenschotter     |
|15201246 | Holziken-Schotter | Holziken-Schotter     |
|15201513 | Homberg-Till | Homberg-Till     |
|15201041 | Hombrechtikon-Vergletscherung (Frühletzteiszeitliche Vergl.) | Hombrechtikon-Vergletscherung (Frühletzteiszeitliche Vergl.)     |
|15201257 | Hungerbol-Schotter | Hungerbol-Schotter     |
|15201195 | Hütten-Schotter | Hütten-Schotter     |
|15201098 | Iberig-Schotterkomplex | Iberig-Schotterkomplex     |
|15201032 | Igliste-Schotter | Igliste-Schotter     |
|15201311 | Informell benannte Bergsturzablagerungen | Informell benannte Bergsturzablagerungen     |
|15201319 | Informell benannte fluviatile Schotter | Informell benannte fluviatile Schotter     |
|15201312 | Informell benannte künstliche Ablagerungen | Informell benannte künstliche Ablagerungen     |
|15201317 | Informell benannte Sackungsmassen | Informell benannte Sackungsmassen     |
|15201322 | Informell benannter Bachschutt | Informell benannter Bachschutt     |
|15201111 | Irchel-Dolomitschotter | Irchel-Dolomitschotter     |
|15201108 | Irchel-Schotterkomplex | Irchel-Schotterkomplex     |
|15201077 | Ittingen-Schotter | Ittingen-Schotter     |
|15201209 | Jonen-Schotter | Jonen-Schotter     |
|15201241 | Junkerenwald-Schotter | Junkerenwald-Schotter     |
|15201182 | Juraschotter | Juraschotter     |
|15201467 | Kaltenegg-Schotter | Kaltenegg-Schotter     |
|15201166 | Käppelihof-Schotter | Käppelihof-Schotter     |
|15201190 | Karlsruhe-Schotter | Karlsruhe-Schotter     |
|15201142 | Kiessande von Madretsch | Kiessande von Madretsch     |
|15201147 | Killwangen-Schaffhausen-Mellingen-Stadium | Killwangen-Schaffhausen-Mellingen-Stadium     |
|15201037 | Kirchleerau-Till | Kirchleerau-Till     |
|15201036 | Kirchleerau-Vorstoss | Kirchleerau-Vorstoss     |
|15201219 | Kleinhöchstetten-Kies-Sand-Komplex | Kleinhöchstetten-Kies-Sand-Komplex     |
|15201045 | Klettgau-Schotter | Klettgau-Schotter     |
|15201236 | Kollbrunn-Schotter | Kollbrunn-Schotter     |
|15201220 | Krauchthal-Schotter | Krauchthal-Schotter     |
|15201539 | Kunkels-Formation | Kunkels-Formation     |
|15201315 | Künstliche Ablagerungen der Gamsenried-Deponie | Künstliche Ablagerungen der Gamsenried-Deponie     |
|15201313 | Künstliche Ablagerungen des Bahnhofs Brig | Künstliche Ablagerungen des Bahnhofs Brig     |
|15201316 | Künstliche Ablagerungen des Riedertals | Künstliche Ablagerungen des Riedertals     |
|15201314 | Künstliche Ablagerungen Golar | Künstliche Ablagerungen Golar     |
|15201222 | Küsnacht-Schotter | Küsnacht-Schotter     |
|15201158 | La-Côte-Schotter | La-Côte-Schotter     |
|15201202 | La-Tuffière-Schotter | La-Tuffière-Schotter     |
|15201114 | Langacher-Schotter | Langacher-Schotter     |
|15201059 | Langwiesen-Vergletscherung | Langwiesen-Vergletscherung     |
|15201060 | Langwiesen-Vorstoss | Langwiesen-Vorstoss     |
|15201007 | Last Glacial Maximum (LGM), undiff. | Last Glacial Maximum (LGM), undiff.     |
|15201008 | LGM-Rückzug | LGM-Rückzug     |
|15201514 | Lindenberg-Till | Lindenberg-Till     |
|15201122 | Lindenhau-Schotter | Lindenhau-Schotter     |
|15201024 | Lindmühle-Vergletscherung (1. LGM-Vorstoss) | Lindmühle-Vergletscherung (1. LGM-Vorstoss)     |
|15201027 | Lindmühle-Vorstoss | Lindmühle-Vorstoss     |
|15201064 | Löhningen-Engiwald-Vergletscherung | Löhningen-Engiwald-Vergletscherung     |
|15201067 | Löhningen-Vorstoss | Löhningen-Vorstoss     |
|15201161 | Lommiswil-Schotter | Lommiswil-Schotter     |
|15201444 | Löss, undifferenziert | Löss, undifferenziert     |
|15201063 | Lupfig-Schotter | Lupfig-Schotter     |
|15201186 | Malmkalk-Schotter der Randen-Täler | Malmkalk-Schotter der Randen-Täler     |
|15201151 | Maximalstand (Kilwangen-Schaffhausen-Stadium) | Maximalstand (Kilwangen-Schaffhausen-Stadium)     |
|15201070 | Meikirch-Interglazial | Meikirch-Interglazial     |
|15201141 | Mély-Formation | Mély-Formation     |
|15201201 | Menzingen-Schotter | Menzingen-Schotter     |
|15201185 | Merenbach-Schotter | Merenbach-Schotter     |
|15201481 | Mettlen-Schotter | Mettlen-Schotter     |
|15201125 | Mischschotter | Mischschotter     |
|15201101 | Mittlere Iberigschotter | Mittlere Iberigschotter     |
|15201112 | Mittlere Irchelschotter | Mittlere Irchelschotter     |
|15201048 | Mittlere Klettgauschotter | Mittlere Klettgauschotter     |
|15201091 | Möhlin-Eiszeit (Grösste Eiszeit) | Möhlin-Eiszeit (Grösste Eiszeit)     |
|15201092 | Möhlin-Vergletscherung | Möhlin-Vergletscherung     |
|15201093 | Möhlin-Vorstoss | Möhlin-Vorstoss     |
|15201081 | Möhlinerfeld-Paläoboden | Möhlinerfeld-Paläoboden     |
|15201482 | Möhlinerfeld-Schotter | Möhlinerfeld-Schotter     |
|15201511 | Mooretal-Schotter | Mooretal-Schotter     |
|15201204 | Mooslerau-Lehm | Mooslerau-Lehm     |
|15201039 | Mülligen-Paläoboden | Mülligen-Paläoboden     |
|15201042 | Mülligen-Schotter | Mülligen-Schotter     |
|15201521 | Mumpf-Schotter | Mumpf-Schotter     |
|15201148 | Munot-Terrasse | Munot-Terrasse     |
|15201188 | Münsingen-Schotterkomplex | Münsingen-Schotterkomplex     |
|15201268 | Murg-Schieferkohle | Murg-Schieferkohle     |
|15201483 | Muttenfeld-Schotter | Muttenfeld-Schotter     |
|15201033 | Niderholz-Till | Niderholz-Till     |
|15201527 | Niderstalden-Schotter | Niderstalden-Schotter     |
|15201484 | Nidfurn-Schotter | Nidfurn-Schotter     |
|15201002 | Niederterrasse | Niederterrasse     |
|15201536 | Niederterrassenschotter, oberste Terrasse | Niederterrassenschotter, oberste Terrasse     |
|15201534 | Niederterrassenschotter, tiefere Niveaus | Niederterrassenschotter, tiefere Niveaus     |
|15201535 | Niederterrassenschotter, zweitoberste Terrasse | Niederterrassenschotter, zweitoberste Terrasse     |
|15201040 | Niederweningen-Formation | Niederweningen-Formation     |
|15201542 | Niklaushalden-Formation | Niklaushalden-Formation     |
|15201134 | Nohl-Terrasse | Nohl-Terrasse     |
|15201459 | Novazzano-Sand | Novazzano-Sand     |
|15201099 | Obere Iberigschotter | Obere Iberigschotter     |
|15201109 | Obere Irchelschotter | Obere Irchelschotter     |
|15201046 | Obere Klettgauschotter | Obere Klettgauschotter     |
|15201132 | Obere Singen-Terrasse | Obere Singen-Terrasse     |
|15201100 | Oberer Till | Oberer Till     |
|15201015 | Oberhard-Till | Oberhard-Till     |
|15201485 | Oberhöhe-Grundmoräne | Oberhöhe-Grundmoräne     |
|15201273 | Oberkirch-Seebodenlehm | Oberkirch-Seebodenlehm     |
|15201486 | Obermoos-Schotter | Obermoos-Schotter     |
|15201269 | Oberricken-Schotter | Oberricken-Schotter     |
|15201162 | Oensingen-Moos-Lehm | Oensingen-Moos-Lehm     |
|15201261 | Oeschinensee-Bergsturzablagerungen | Oeschinensee-Bergsturzablagerungen     |
|15201259 | Ofenloch-Karstfüllung | Ofenloch-Karstfüllung     |
|15201487 | Öflingen-Schotter | Öflingen-Schotter     |
|15201215 | Oftringen-Schotter | Oftringen-Schotter     |
|15201138 | Orvin-Schotter | Orvin-Schotter     |
|15201025 | Otelfingen-Vorstoss | Otelfingen-Vorstoss     |
|15201561 | Paradiesgärtli-Schotter | Paradiesgärtli-Schotter     |
|15201076 | Pfyn-Vorstoss | Pfyn-Vorstoss     |
|15201566 | Plaffeien-Seetone | Plaffeien-Seetone     |
|15201567 | Plasselb-Stauschotter | Plasselb-Stauschotter     |
|15201157 | Plateauschotter | Plateauschotter     |
|15201333 | Pliozäne Ablagerungen | Pliozäne Ablagerungen     |
|15201170 | Poissine-Formation | Poissine-Formation     |
|15201212 | Port-Stauschotter | Port-Stauschotter     |
|15201249 | Quartär, undifferenziert | Quartär, undifferenziert     |
|15201224 | Rabennest-Schotter | Rabennest-Schotter     |
|15201218 | Raintal-Deltaschotter | Raintal-Deltaschotter     |
|15201225 | Ratengütsch-Schotter | Ratengütsch-Schotter     |
|15201277 | Regelstein-Till | Regelstein-Till     |
|15201230 | Reidbach-Schotter | Reidbach-Schotter     |
|15201069 | Remigen-Schotter | Remigen-Schotter     |
|15201068 | Remigen-Vorstoss | Remigen-Vorstoss     |
|15201213 | Rempen-Stauschotter | Rempen-Stauschotter     |
|15201062 | Reuenthal-Vorstoss | Reuenthal-Vorstoss     |
|15201505 | Reuss-Schotterkomplex | Reuss-Schotterkomplex     |
|15201176 | Reusstal-Lehm | Reusstal-Lehm     |
|15201175 | Reusstal-Sand | Reusstal-Sand     |
|15201507 | Reusstal-Seebodensediment | Reusstal-Seebodensediment     |
|15201181 | Rhein- und Aareschotter | Rhein- und Aareschotter     |
|15201133 | Rheinau-Terrasse | Rheinau-Terrasse     |
|15201545 | Rheinau-Till | Rheinau-Till     |
|15201228 | Richterswil-Seeton | Richterswil-Seeton     |
|15201509 | Rickenbach-Schotter | Rickenbach-Schotter     |
|15201522 | Riedmatt-Schotter | Riedmatt-Schotter     |
|15201554 | Risibüel-Schotter | Risibüel-Schotter     |
|15201238 | Ritteren-Schotterkomplex | Ritteren-Schotterkomplex     |
|15201516 | Ritzhans-Schotter | Ritzhans-Schotter     |
|15201084 | Roggehuse-Schotter | Roggehuse-Schotter     |
|15201266 | Rossgaden-Schotter | Rossgaden-Schotter     |
|15201488 | Rottal-Schotter | Rottal-Schotter     |
|15201179 | Ruckfeld-Schotter | Ruckfeld-Schotter     |
|15201489 | Rüdelwald-Schotter | Rüdelwald-Schotter     |
|15201541 | Rüdlingen-Till | Rüdlingen-Till     |
|15201247 | Ruedertal-Schotter | Ruedertal-Schotter     |
|15201066 | Rüfenach-Vorstoss | Rüfenach-Vorstoss     |
|15201490 | Rufswil-Schotter | Rufswil-Schotter     |
|15201491 | Rütimatt-Schotter | Rütimatt-Schotter     |
|15201078 | Ryhirt-Formation | Ryhirt-Formation     |
|15201519 | Säckingen-Schotter | Säckingen-Schotter     |
|15201318 | Sackungsmasse des Heinzenbergs | Sackungsmasse des Heinzenbergs     |
|15201252 | Sagenbach-Schotter | Sagenbach-Schotter     |
|15201556 | Saxegrabe-Schotter | Saxegrabe-Schotter     |
|15201279 | Schafbüel-Formation | Schafbüel-Formation     |
|15201061 | Schaffhausen-Schotter | Schaffhausen-Schotter     |
|15201226 | Scherenspitz-Schotter | Scherenspitz-Schotter     |
|15201095 | Schleitheim-Vorstoss | Schleitheim-Vorstoss     |
|15201131 | Schlieren-Diessenhofen-Stetten-Stadien | Schlieren-Diessenhofen-Stetten-Stadien     |
|15201553 | Schlossbuck-Schotter | Schlossbuck-Schotter     |
|15201338 | Schlyffi-Till | Schlyffi-Till     |
|15201555 | Schmerlet- und Toktri-Formation, undifferenziert | Schmerlet- und Toktri-Formation, undifferenziert     |
|15201196 | Schnabelsberg-Stauchotter | Schnabelsberg-Stauchotter     |
|15201518 | Schönegg-Formation | Schönegg-Formation     |
|15201320 | Schotter und Sand der Rhône | Schotter und Sand der Rhône     |
|15201321 | Schotter und Sand der Vispa | Schotter und Sand der Vispa     |
|15201253 | Schrotzburg-Schotter | Schrotzburg-Schotter     |
|15201254 | Schrotzburg-Till | Schrotzburg-Till     |
|15201137 | Schüss-Schotter | Schüss-Schotter     |
|15201493 | Schwande-Seebodensedimente | Schwande-Seebodensedimente     |
|15201229 | Schwanden-Schotter | Schwanden-Schotter     |
|15201492 | Schwanderholzwald-Schotter | Schwanderholzwald-Schotter     |
|15201165 | Schwarzhäusern-Lehm | Schwarzhäusern-Lehm     |
|15201139 | Seeablagerungen von Frinvillier und Rondchâtel | Seeablagerungen von Frinvillier und Rondchâtel     |
|15201143 | Seeland-Schotter | Seeland-Schotter     |
|15201016 | Seon-Vorstoss | Seon-Vorstoss     |
|15201207 | Sihl-Schotter | Sihl-Schotter     |
|15201235 | Sihlsprung-Schotter | Sihlsprung-Schotter     |
|15201187 | Solothurn-Stadium | Solothurn-Stadium     |
|15201494 | Soppensee-Seebodensedimente | Soppensee-Seebodensedimente     |
|15201525 | Spärgacher-Schotter | Spärgacher-Schotter     |
|15201495 | Speicherboden-Lokalmoräne | Speicherboden-Lokalmoräne     |
|15201529 | Spiez-Schotter | Spiez-Schotter     |
|15201543 | Stadel-Till | Stadel-Till     |
|15201022 | Staffelbach-Schotter | Staffelbach-Schotter     |
|15201023 | Staffelbach-Till | Staffelbach-Till     |
|15201021 | Staffelbach-Vorstoss | Staffelbach-Vorstoss     |
|15201211 | Starrberg-Schotter | Starrberg-Schotter     |
|15201140 | Stauschotter von Diessbach | Stauschotter von Diessbach     |
|15201342 | Steghalden-Schotter | Steghalden-Schotter     |
|15201107 | Steig-Schotter | Steig-Schotter     |
|15201468 | Steinhuserberg-Schotter | Steinhuserberg-Schotter     |
|15201565 | Stetten-Schotter | Stetten-Schotter     |
|15201334 | Stockesee-Sediment | Stockesee-Sediment     |
|15201149 | Stokar-Terrasse | Stokar-Terrasse     |
|15201335 | Strätligen-Till | Strätligen-Till     |
|15201058 | Stüsslingen-Schotter | Stüsslingen-Schotter     |
|15201552 | Südranden-Till | Südranden-Till     |
|15201056 | Suhr-Schotter | Suhr-Schotter     |
|15201124 | Sundgau-Schotter | Sundgau-Schotter     |
|15201171 | Surbtal-Lehm | Surbtal-Lehm     |
|15201173 | Surbtal-Schotter | Surbtal-Schotter     |
|15201172 | Surbtal-Till | Surbtal-Till     |
|15201026 | Tägerhard-Schotter | Tägerhard-Schotter     |
|15201496 | terrasse lémanique de 10 m | terrasse lémanique de 10 m     |
|15201497 | terrasse lémanique de 3 m | terrasse lémanique de 3 m     |
|15201090 | Thalgut-Interglazial | Thalgut-Interglazial     |
|15201282 | Tiefenwinkel-Seebodensedimente | Tiefenwinkel-Seebodensedimente     |
|15201004 | Tiefere Deckenschotter | Tiefere Deckenschotter     |
|15201538 | Tiefere Deckenschotter, oberes Niveau | Tiefere Deckenschotter, oberes Niveau     |
|15201537 | Tiefere Deckenschotter, unteres Niveau | Tiefere Deckenschotter, unteres Niveau     |
|15201193 | Trachslau-Schotter | Trachslau-Schotter     |
|15201206 | Triengen-Lehm | Triengen-Lehm     |
|15201205 | Triengen-Schotter | Triengen-Schotter     |
|15201562 | Tubeschwanz-Schotter | Tubeschwanz-Schotter     |
|15201168 | Tuileries-Formation | Tuileries-Formation     |
|15201276 | Unter-Buechwald-Schotter | Unter-Buechwald-Schotter     |
|15201517 | Unterdorf-Schotter | Unterdorf-Schotter     |
|15201102 | Untere Iberigschotter | Untere Iberigschotter     |
|15201113 | Untere Irchelschotter | Untere Irchelschotter     |
|15201049 | Untere Klettgauschotter | Untere Klettgauschotter     |
|15201130 | Untere Singen-Terrasse | Untere Singen-Terrasse     |
|15201498 | Untere Zeller Schotter | Untere Zeller Schotter     |
|15201103 | Unterer Till | Unterer Till     |
|15201280 | Unteres-Huttenbüel-Schotter | Unteres-Huttenbüel-Schotter     |
|15201499 | Untergrabehüsli-Schotter | Untergrabehüsli-Schotter     |
|15201089 | Unterschlatt-Vorstoss | Unterschlatt-Vorstoss     |
|15201500 | Untertreie-Schotter | Untertreie-Schotter     |
|15201283 | Uznach-Schieferkohle | Uznach-Schieferkohle     |
|15201057 | Veltheim-Schotter | Veltheim-Schotter     |
|15201544 | Volken-Lehm | Volken-Lehm     |
|15201239 | Vorholz-Schotter | Vorholz-Schotter     |
|15201526 | Wagenmoos-Till | Wagenmoos-Till     |
|15201237 | Walenberg-Schotter | Walenberg-Schotter     |
|15201501 | Wallbach-Schotter | Wallbach-Schotter     |
|15201227 | Walsenhaus-Schotter | Walsenhaus-Schotter     |
|15201118 | Wannen-Schotter | Wannen-Schotter     |
|15201337 | Wässerifluh-Formation | Wässerifluh-Formation     |
|15201560 | Wasterkingen-Schotter | Wasterkingen-Schotter     |
|15201152 | Wehntal-Schotter | Wehntal-Schotter     |
|15201549 | Weiach-Schotter | Weiach-Schotter     |
|15201126 | Weisse Serie | Weisse Serie     |
|15201563 | Weisweil-Schotter | Weisweil-Schotter     |
|15201502 | Werthenstein-Schotter | Werthenstein-Schotter     |
|15201155 | Wettingen-Schotter | Wettingen-Schotter     |
|15201010 | Wettingen-Vorstoss | Wettingen-Vorstoss     |
|15201200 | Wiggen-Schotter | Wiggen-Schotter     |
|15201503 | Willburg-Formation | Willburg-Formation     |
|15201198 | Willisau-Schotter | Willisau-Schotter     |
|15201504 | Wilzigen-Seebodensedimente | Wilzigen-Seebodensedimente     |
|15201281 | Winden-Schieferkohle | Winden-Schieferkohle     |
|15201551 | Windlach-Till | Windlach-Till     |
|15201104 | Wolfacher-Schotter und -Till | Wolfacher-Schotter und -Till     |
|15201199 | Wolhusen-Schotter | Wolhusen-Schotter     |
|15201260 | Wurmsbach-Deltaablagerungen | Wurmsbach-Deltaablagerungen     |
|15201184 | Wutach-Schotter | Wutach-Schotter     |
|15201508 | Wyna-Schotter | Wyna-Schotter     |
|15201463 | Zeiningen-Till | Zeiningen-Till     |
|15201216 | Zelg-Schotter | Zelg-Schotter     |
|15201231 | Zell-Schotterkomplex | Zell-Schotterkomplex     |
|15201035 | Zetzwil-Till | Zetzwil-Till     |
|15201034 | Zetzwil-Vorstoss | Zetzwil-Vorstoss     |
|15201528 | Zulgtal-Schotter | Zulgtal-Schotter     |
|15201129 | Zürich-Stein-Bremgarten-Stadien | Zürich-Stein-Bremgarten-Stadien     |
|15201557 | Zweidlen-Schotter | Zweidlen-Schotter     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute litho{#unconsolidated-deposits-plg-litho}
__

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15104015 | (Meso)Kataklasit | (Meso)Kataklasit     |
|15104044 | Adergneis | Adergneis     |
|15104046 | agmatischer Gneis | agmatischer Gneis     |
|15104087 | Albitit | Albitit     |
|15103040 | Alkalirhyolith | Alkalirhyolith     |
|15103013 | Alkalisyenit | Alkalisyenit     |
|15103046 | Alkalitrachyt | Alkalitrachyt     |
|15103006 | Alkalogranit | Alkalogranit     |
|15101039 | Alluvion, undifferenziert | Alluvion, undifferenziert     |
|15104060 | Amphibolit | Amphibolit     |
|15104063 | Amphibolitgneis | Amphibolitgneis     |
|15104074 | Anatexit, undifferenziert | Anatexit, undifferenziert     |
|15103045 | Andesit | Andesit     |
|15102071 | Anhydrit | Anhydrit     |
|15102059 | Anthrazit | Anthrazit     |
|15101067 | anthropogene Elemente, undifferenziert | anthropogene Elemente, undifferenziert     |
|15101062 | äolischer Sand, Flugsand | äolischer Sand, Flugsand     |
|15101061 | äolisches Sediment, undifferenziert | äolisches Sediment, undifferenziert     |
|15103030 | Aplit | Aplit     |
|15102044 | Aptychenkalk | Aptychenkalk     |
|15102038 | Arenit | Arenit     |
|15102016 | Arkose | Arkose     |
|15103058 | Aschentuff | Aschentuff     |
|15101071 | Auffüllung | Auffüllung     |
|15101070 | Aufschüttung, Damm | Aufschüttung, Damm     |
|15104042 | Augengneis | Augengneis     |
|15101041 | Bachschutt | Bachschutt     |
|15104061 | Bänderamphibolit | Bänderamphibolit     |
|15104043 | Bändergneis | Bändergneis     |
|15103048 | Basalt | Basalt     |
|15103068 | basisches Ganggestein | basisches Ganggestein     |
|15103069 | Basisches Gestein | Basisches Gestein     |
|15103066 | Bentonit | Bentonit     |
|15101006 | Bergsturzablagerung | Bergsturzablagerung     |
|15102045 | biogener Kalkstein, undifferenziert | biogener Kalkstein, undifferenziert     |
|15102032 | biogenes / biochemisches / organisches Sedimentgestein, undifferenziert | biogenes / biochemisches / organisches Sedimentgestein, undifferenziert     |
|15102106 | bioklastischer Kalk | bioklastischer Kalk     |
|15104085 | Biotitit | Biotitit     |
|15101015 | Blockgletscher | Blockgletscher     |
|15101010 | Blockschutt | Blockschutt     |
|15102082 | Bohnerz | Bohnerz     |
|15102087 | Boluston | Boluston     |
|15102006 | Brekzie | Brekzie     |
|15102093 | Caliche | Caliche     |
|15102068 | chemisches Sedimentgestein, undifferenziert | chemisches Sedimentgestein, undifferenziert     |
|15104089 | Chloritit | Chloritit     |
|15104034 | Chloritschiefer | Chloritschiefer     |
|15103043 | Dazit | Dazit     |
|15101072 | Deponie | Deponie     |
|15101049 | detritische Verlandungsbildung | detritische Verlandungsbildung     |
|15102046 | detritischer Kalk | detritischer Kalk     |
|15104079 | Diatexit mit nebulitischer Textur | Diatexit mit nebulitischer Textur     |
|15104080 | Diatexit mit Schlierentextur | Diatexit mit Schlierentextur     |
|15104081 | Diatexit mit Schollentextur | Diatexit mit Schollentextur     |
|15103011 | Diorit | Diorit     |
|15103035 | Dolerit | Dolerit     |
|15102049 | Dolomit | Dolomit     |
|15102109 | Dolomitbrekzie | Dolomitbrekzie     |
|15104216 | dolomitischer Marmor | dolomitischer Marmor     |
|15102012 | Dolomitsandstein | Dolomitsandstein     |
|15101075 | dünne Lockermaterialbedeckung | dünne Lockermaterialbedeckung     |
|15102100 | Echinodermenkalk | Echinodermenkalk     |
|15102061 | Eisenoolith | Eisenoolith     |
|15102103 | Eisensandstein | Eisensandstein     |
|15102108 | eisenschüssiger Kalk | eisenschüssiger Kalk     |
|15104064 | Eklogit | Eklogit     |
|15101086 | Entwässerungssediment | Entwässerungssediment     |
|15103039 | Ergussgestein, undifferenziert | Ergussgestein, undifferenziert     |
|15103023 | Essexit | Essexit     |
|15102070 | Evaporit, undifferenziert | Evaporit, undifferenziert     |
|15103037 | Extrusivgestein, undifferenziert | Extrusivgestein, undifferenziert     |
|15104053 | Fels, undifferenziert | Fels, undifferenziert     |
|15101007 | Felssturzablagerung | Felssturzablagerung     |
|15101040 | fluviatiler Schotter | fluviatiler Schotter     |
|15101026 | fluviatiles Sediment, undifferenziert | fluviatiles Sediment, undifferenziert     |
|15102017 | Flyschsandstein, Grauwacke | Flyschsandstein, Grauwacke     |
|15103015 | Gabbro | Gabbro     |
|15103026 | Ganggestein, undifferenziert | Ganggestein, undifferenziert     |
|15101035 | gemischter Schutt | gemischter Schutt     |
|15101076 | geringmächtige Lockergesteinsbedeckung | geringmächtige Lockergesteinsbedeckung     |
|15104210 | Geröll führender Metasandstein | Geröll führender Metasandstein     |
|15102018 | Geröll führender Sandstein | Geröll führender Sandstein     |
|15104027 | Gestein der Regional- und Kontaktmetamorphose, undifferenziert | Gestein der Regional- und Kontaktmetamorphose, undifferenziert     |
|15104002 | Gestein der Störungszone | Gestein der Störungszone     |
|15104003 | Gestein der Störungszone, undifferenziert | Gestein der Störungszone, undifferenziert     |
|15104006 | Gesteinsmehl | Gesteinsmehl     |
|15102072 | Gips | Gips     |
|15102101 | glaukonitischer Kalkstein | glaukonitischer Kalkstein     |
|15102104 | glaukonitischer Mergel | glaukonitischer Mergel     |
|15102020 | Glaukonitsandstein | Glaukonitsandstein     |
|15104036 | Glaukophanschiefer | Glaukophanschiefer     |
|15101031 | glazifluviatiler Schotter | glazifluviatiler Schotter     |
|15101028 | glazifluviatiles Sediment, undifferenziert | glazifluviatiles Sediment, undifferenziert     |
|15101019 | glazigenes Sediment, undifferenziert | glazigenes Sediment, undifferenziert     |
|15101047 | glazilakustrisches Deltasediment | glazilakustrisches Deltasediment     |
|15101046 | glazilakustrisches Sediment, undifferenziert | glazilakustrisches Sediment, undifferenziert     |
|15102019 | Glimmersandstein | Glimmersandstein     |
|15104035 | Glimmerschiefer | Glimmerschiefer     |
|15104072 | Gneis mit Feldspatblasten | Gneis mit Feldspatblasten     |
|15104041 | Gneis, undifferenziert | Gneis, undifferenziert     |
|15104097 | Granat-Glimmerschiefer | Granat-Glimmerschiefer     |
|15103007 | Granit | Granit     |
|15103008 | Granodiorit | Granodiorit     |
|15103024 | Granophyr | Granophyr     |
|15104058 | Granulit | Granulit     |
|15101003 | gravitative Sedimente und Verwitterungsbildungen, undifferenziert | gravitative Sedimente und Verwitterungsbildungen, undifferenziert     |
|15104071 | Greisen | Greisen     |
|15104098 | Grünschiefer | Grünschiefer     |
|15101079 | Gyttja | Gyttja     |
|15101073 | Halde | Halde     |
|15101014 | Hanglehm, Schwemmlehm | Hanglehm, Schwemmlehm     |
|15101009 | Hangschutt | Hangschutt     |
|15104086 | Hornblenditit | Hornblenditit     |
|15104067 | Hornfels | Hornfels     |
|15102054 | Hornstein, Chert | Hornstein, Chert     |
|15102088 | Huppererde | Huppererde     |
|15101081 | hydrochemische Bildungen (Kalksinter) | hydrochemische Bildungen (Kalksinter)     |
|15103054 | Ignimbrit | Ignimbrit     |
|15101083 | In-situ-Verwitterungsschutt | In-situ-Verwitterungsschutt     |
|15103003 | Intrusivgestein, undifferenziert | Intrusivgestein, undifferenziert     |
|15104005 | Kakirit, undifferenziert | Kakirit, undifferenziert     |
|15102041 | Kalkbrekzie | Kalkbrekzie     |
|15102029 | Kalkmergelstein | Kalkmergelstein     |
|15102042 | Kalkoolith | Kalkoolith     |
|15102011 | Kalksandstein | Kalksandstein     |
|15104037 | Kalkschiefer | Kalkschiefer     |
|15104054 | Kalksilikatfels | Kalksilikatfels     |
|15102034 | Kalkstein, undifferenziert | Kalkstein, undifferenziert     |
|15104056 | Karbonat- und Silikat führendes Gestein | Karbonat- und Silikat führendes Gestein     |
|15102075 | Karbonat, undifferenziert | Karbonat, undifferenziert     |
|15103051 | Karbonatit | Karbonatit     |
|15104010 | Kataklasit, undifferenziert | Kataklasit, undifferenziert     |
|15102013 | kieseliger Sandstein | kieseliger Sandstein     |
|15102051 | kieseliges Gestein, undifferenziert | kieseliges Gestein, undifferenziert     |
|15102035 | Kieselkalk | Kieselkalk     |
|15104051 | Kinzigit | Kinzigit     |
|15102003 | klastisches Sedimentgestein, undifferenziert | klastisches Sedimentgestein, undifferenziert     |
|15104007 | Kluftletten | Kluftletten     |
|15102056 | Kohle, undifferenziert | Kohle, undifferenziert     |
|15102007 | Konglomerat | Konglomerat     |
|15102005 | Konglomerat und Brekzie, undifferenziert (Psephit, Korngrösse: Kies, Steine und Blöcke) | Konglomerat und Brekzie, undifferenziert (Psephit, Korngrösse: Kies, Steine und Blöcke)     |
|15102105 | kreidiger Kalk | kreidiger Kalk     |
|15103057 | Kristalltuff | Kristalltuff     |
|15102094 | Krustenkalk | Krustenkalk     |
|15101069 | künstliche Ablagerung, undifferenziert | künstliche Ablagerung, undifferenziert     |
|15101057 | lakustrisches Deltasediment | lakustrisches Deltasediment     |
|15101044 | lakustrisches Sediment, undifferenziert | lakustrisches Sediment, undifferenziert     |
|15103033 | Lamprophyr | Lamprophyr     |
|15103056 | Lapillituff | Lapillituff     |
|15101008 | Lawinenschutt | Lawinenschutt     |
|15104047 | Leptinit | Leptinit     |
|15102057 | Lignit (organisches Sedimentgestein) | Lignit (organisches Sedimentgestein)     |
|15101054 | Lignit (palustrisches Sediment) | Lignit (palustrisches Sediment)     |
|15102102 | Lithothamniensandstein | Lithothamniensandstein     |
|15101001 | Lockergestein | Lockergestein     |
|15101063 | Löss, Lösslehm | Löss, Lösslehm     |
|15103001 | Magmatit | Magmatit     |
|15104055 | Marmor (Fels) | Marmor (Fels)     |
|15104215 | Marmor (sedimentärer Protolith) | Marmor (sedimentärer Protolith)     |
|15102014 | mergeliger Sandstein | mergeliger Sandstein     |
|15102107 | Mergelkalk | Mergelkalk     |
|15102027 | Mergelstein | Mergelstein     |
|15104433 | Metaalkalirhyolith | Metaalkalirhyolith     |
|15104411 | Metaalkalisyenit | Metaalkalisyenit     |
|15104439 | Metaalkalitrachyt | Metaalkalitrachyt     |
|15104404 | Metaalkalogranit | Metaalkalogranit     |
|15104438 | Metaandesit | Metaandesit     |
|15104427 | Metaaplit | Metaaplit     |
|15104208 | Metaarkose | Metaarkose     |
|15104441 | Metabasalt | Metabasalt     |
|15104203 | Metabrekzie | Metabrekzie     |
|15104436 | Metadazit | Metadazit     |
|15104409 | Metadiorit | Metadiorit     |
|15104432 | Metadolerit | Metadolerit     |
|15104421 | Metaessexit | Metaessexit     |
|15104413 | Metagabbro | Metagabbro     |
|15104423 | Metaganggestein | Metaganggestein     |
|15104405 | Metagranit | Metagranit     |
|15104406 | Metagranodiorit | Metagranodiorit     |
|15104422 | Metagranophyr | Metagranophyr     |
|15104209 | Metagrauwacke | Metagrauwacke     |
|15104445 | Metaignimbrit | Metaignimbrit     |
|15104218 | Metakarbonat | Metakarbonat     |
|15104204 | Metakonglomerat | Metakonglomerat     |
|15104430 | Metalamprophyr | Metalamprophyr     |
|15104401 | Metamagmatit | Metamagmatit     |
|15104214 | Metamergel | Metamergel     |
|15104428 | Metamikrodiorit | Metamikrodiorit     |
|15104429 | Metamikrogabbro | Metamikrogabbro     |
|15104424 | Metamikrogranit | Metamikrogranit     |
|15104415 | Metamonzodiorit | Metamonzodiorit     |
|15104416 | Metamonzogabbro | Metamonzogabbro     |
|15104417 | Metamonzonit | Metamonzonit     |
|15104402 | metamorph überprägtes Intrusivgestein | metamorph überprägtes Intrusivgestein     |
|15104444 | metamorph überprägtes pyroklastisches Gestein | metamorph überprägtes pyroklastisches Gestein     |
|15104001 | Metamorphit | Metamorphit     |
|15104095 | Metamorphit (magmatischer Protolith erkennbar) | Metamorphit (magmatischer Protolith erkennbar)     |
|15104092 | Metamorphit (Protolith erkennbar) | Metamorphit (Protolith erkennbar)     |
|15104093 | Metamorphit (sedimentärer Protolith erkennbar) | Metamorphit (sedimentärer Protolith erkennbar)     |
|15104414 | Metanorit | Metanorit     |
|15104426 | Metapegmatit | Metapegmatit     |
|15104211 | Metapelit | Metapelit     |
|15104419 | Metaperidotit | Metaperidotit     |
|15104443 | Metaphonolit | Metaphonolit     |
|15104431 | Metapikrit | Metapikrit     |
|15104403 | Metaplutonit | Metaplutonit     |
|15104207 | Metapsammit | Metapsammit     |
|15104202 | Metapsephit | Metapsephit     |
|15104418 | Metapyroxenit | Metapyroxenit     |
|15104437 | Metaquarzandesit | Metaquarzandesit     |
|15104407 | Metaquarzdiorit | Metaquarzdiorit     |
|15104412 | Metaquarzgabbro | Metaquarzgabbro     |
|15104217 | Metaradiolarit | Metaradiolarit     |
|15104435 | Metarhyodazit | Metarhyodazit     |
|15104434 | Metarhyolith | Metarhyolith     |
|15104205 | Metasandstein | Metasandstein     |
|15104201 | Metasediment | Metasediment     |
|15104212 | Metasiltstein | Metasiltstein     |
|15104069 | Metasomatit, undifferenziert | Metasomatit, undifferenziert     |
|15104410 | Metasyenit | Metasyenit     |
|15104076 | Metatexit mit Fleckentextur | Metatexit mit Fleckentextur     |
|15104078 | Metatexit mit Netztextur | Metatexit mit Netztextur     |
|15104077 | Metatexit mit stromatitischer Textur | Metatexit mit stromatitischer Textur     |
|15104408 | Metatonalit | Metatonalit     |
|15104440 | Metatrachyt | Metatrachyt     |
|15104446 | Metavulkanit | Metavulkanit     |
|15104075 | Migmatit | Migmatit     |
|15102037 | Mikrit | Mikrit     |
|15103031 | Mikrodiorit | Mikrodiorit     |
|15103032 | Mikrogabbro | Mikrogabbro     |
|15103027 | Mikrogranit | Mikrogranit     |
|15104084 | monomineralischer Metamorphit, undifferenziert | monomineralischer Metamorphit, undifferenziert     |
|15103017 | Monzodiorit | Monzodiorit     |
|15103018 | Monzogabbro | Monzogabbro     |
|15103019 | Monzonit | Monzonit     |
|15101021 | Moräne (Till), undifferenziert | Moräne (Till), undifferenziert     |
|15101024 | Moräne auf Gletscher oder Toteis (Glacier or Dead Ice covered by Till) | Moräne auf Gletscher oder Toteis (Glacier or Dead Ice covered by Till)     |
|15101037 | Murgangablagerung | Murgangablagerung     |
|15102022 | Muschelsandstein | Muschelsandstein     |
|15104020 | Mylonit | Mylonit     |
|15104018 | Mylonit, undifferenziert | Mylonit, undifferenziert     |
|15104420 | nephelinitischer Metasyenit | nephelinitischer Metasyenit     |
|15103022 | nephelinitischer Syenit | nephelinitischer Syenit     |
|15103016 | Norit | Norit     |
|15102043 | Nummulitenkalk | Nummulitenkalk     |
|15102021 | Nummulitensandstein | Nummulitensandstein     |
|15104099 | Ophikalzit | Ophikalzit     |
|15104049 | Orthogneis | Orthogneis     |
|15101050 | palustrisches Sediment | palustrisches Sediment     |
|15101051 | palustrisches Sediment, undifferenziert | palustrisches Sediment, undifferenziert     |
|15104048 | Paragneis | Paragneis     |
|15102092 | pedogenes Karbonat, undifferenziert | pedogenes Karbonat, undifferenziert     |
|15103029 | Pegmatit | Pegmatit     |
|15102024 | Pelit, undifferenziert | Pelit, undifferenziert     |
|15103021 | Peridotit (Intrusivgestein) | Peridotit (Intrusivgestein)     |
|15104065 | Peridotit (Metamorphit) | Peridotit (Metamorphit)     |
|15103050 | Phonolith | Phonolith     |
|15102065 | phosphoritreicher Kalkstein | phosphoritreicher Kalkstein     |
|15102066 | phosphoritreicher Mergelstein | phosphoritreicher Mergelstein     |
|15102064 | phosphoritreicher Sandstein | phosphoritreicher Sandstein     |
|15102063 | phosphoritreiches Gestein, undifferenziert | phosphoritreiches Gestein, undifferenziert     |
|15104029 | Phyllit | Phyllit     |
|15104023 | Phyllonit | Phyllonit     |
|15103049 | Pikrit (Effusiva) | Pikrit (Effusiva)     |
|15103034 | Pikrit (Intrusivgestein) | Pikrit (Intrusivgestein)     |
|15101013 | Plateaulehm | Plateaulehm     |
|15104038 | Prasinit | Prasinit     |
|15104014 | Protokataklasit | Protokataklasit     |
|15104019 | Protomylonit | Protomylonit     |
|15104025 | Pseudotachylit | Pseudotachylit     |
|15103055 | Pyroklastische Brekzie | Pyroklastische Brekzie     |
|15103053 | pyroklastisches Gestein, undifferenziert (vulkanischer Tuff, &gt; 75 % pyroklast. Komp.) | pyroklastisches Gestein, undifferenziert (vulkanischer Tuff, &gt; 75 % pyroklast. Komp.)     |
|15103020 | Pyroxenit (Intrusivgestein) | Pyroxenit (Intrusivgestein)     |
|15104088 | Pyroxenit (monomineralischer Metamorphit) | Pyroxenit (monomineralischer Metamorphit)     |
|15103044 | Quarzandesit | Quarzandesit     |
|15103009 | Quarzdiorit | Quarzdiorit     |
|15103014 | Quarzgabbro | Quarzgabbro     |
|15104091 | Quarzit (monomineralischer Metamorphit) | Quarzit (monomineralischer Metamorphit)     |
|15104206 | Quarzit (sedimentärer Protolith) | Quarzit (sedimentärer Protolith)     |
|15102089 | Quarzsand | Quarzsand     |
|15102010 | Quarzsandstein | Quarzsandstein     |
|15104096 | Quarzschiefer | Quarzschiefer     |
|15101080 | Quelltuff (Kalksinter, Lockergestein) | Quelltuff (Kalksinter, Lockergestein)     |
|15102077 | Quelltuff (Kalksinter, Sedimentgestein) | Quelltuff (Kalksinter, Sedimentgestein)     |
|15102052 | Radiolarit | Radiolarit     |
|15101030 | randglazialer Schotter | randglazialer Schotter     |
|15104011 | Rauwacke (Kataklasit) | Rauwacke (Kataklasit)     |
|15102076 | Rauwacke (Sedimentgestein) | Rauwacke (Sedimentgestein)     |
|15102080 | Residualgestein / pedogen überprägtes Gestein, undifferenziert | Residualgestein / pedogen überprägtes Gestein, undifferenziert     |
|15103042 | Rhyodazit | Rhyodazit     |
|15103041 | Rhyolith | Rhyolith     |
|15103028 | Rhyolithporphyr | Rhyolithporphyr     |
|15102040 | Riffkalk | Riffkalk     |
|15104059 | Rodingit | Rodingit     |
|15101033 | Rückzugsschotter | Rückzugsschotter     |
|15102039 | Rudit | Rudit     |
|15101017 | Rutschmasse | Rutschmasse     |
|15102009 | Sandstein, undifferenziert (Psammit: Sandkorngrösse) | Sandstein, undifferenziert (Psammit: Sandkorngrösse)     |
|15103067 | saures Ganggestein | saures Ganggestein     |
|15104031 | Schiefer, undifferenziert | Schiefer, undifferenziert     |
|15102030 | Schlammstein | Schlammstein     |
|15104062 | Schollenamphibolit | Schollenamphibolit     |
|15101087 | Sedimentärer Gang (clastic dike) | Sedimentärer Gang (clastic dike)     |
|15102001 | Sedimentgestein | Sedimentgestein     |
|15101058 | Seebodensediment | Seebodensediment     |
|15101059 | Seekreide | Seekreide     |
|15104033 | Serizitschiefer | Serizitschiefer     |
|15104090 | Serpentinit | Serpentinit     |
|15102084 | siderolithische Verwitterungsbildungen | siderolithische Verwitterungsbildungen     |
|15102090 | Silcrete | Silcrete     |
|15104057 | silikatreicher Marmor | silikatreicher Marmor     |
|15102086 | silikatreiches Gestein, undifferenziert | silikatreiches Gestein, undifferenziert     |
|15102025 | Siltstein | Siltstein     |
|15104070 | Skarn | Skarn     |
|15102036 | Spatkalk | Spatkalk     |
|15102053 | Spiculit | Spiculit     |
|15101034 | Stauschotter | Stauschotter     |
|15102058 | Steinkohle | Steinkohle     |
|15102073 | Steinsalz | Steinsalz     |
|15101056 | Strandablagerungen | Strandablagerungen     |
|15104050 | Stronalit | Stronalit     |
|15101084 | strukturierter Hangschutt | strukturierter Hangschutt     |
|15101005 | Sturzablagerung, undifferenziert | Sturzablagerung, undifferenziert     |
|15101048 | subaquatisch abgelagerte Moräne (Waterlaid Till) | subaquatisch abgelagerte Moräne (Waterlaid Till)     |
|15101052 | Sumpf | Sumpf     |
|15102047 | Süsswasserkalk | Süsswasserkalk     |
|15103012 | Syenit | Syenit     |
|15104039 | Talkschiefer | Talkschiefer     |
|15104008 | tektonische Brekzie (kohäsionslos) | tektonische Brekzie (kohäsionslos)     |
|15104013 | tektonische Brekzie (mit Kohäsion) | tektonische Brekzie (mit Kohäsion)     |
|15104012 | tektonische Dolomitbrekzie | tektonische Dolomitbrekzie     |
|15104448 | tektonische Kalkbrekzie | tektonische Kalkbrekzie     |
|15103005 | Tiefengestein, undifferenziert | Tiefengestein, undifferenziert     |
|15101078 | tiefgründige Verwitterungsdecke | tiefgründige Verwitterungsdecke     |
|15103010 | Tonalit | Tonalit     |
|15102015 | toniger Sandstein | toniger Sandstein     |
|15102028 | Tonmergelstein | Tonmergelstein     |
|15104032 | Tonschiefer (Schiefer) | Tonschiefer (Schiefer)     |
|15104213 | Tonschiefer (sedimentärer Protolith) | Tonschiefer (sedimentärer Protolith)     |
|15102026 | Tonstein | Tonstein     |
|15101053 | Torfmoor, Torf | Torfmoor, Torf     |
|15103047 | Trachyt | Trachyt     |
|15101082 | Travertin (Kalksinter, Lockergestein) | Travertin (Kalksinter, Lockergestein)     |
|15102078 | Travertin (Kalksinter, Sedimentgestein) | Travertin (Kalksinter, Sedimentgestein)     |
|15101085 | Tsunamiablagerung | Tsunamiablagerung     |
|15103060 | Tuffit, undifferenziert (pyroklast. und nicht vulk. Sedimente, 75-25 % pyroklast. Komp.) | Tuffit, undifferenziert (pyroklast. und nicht vulk. Sedimente, 75-25 % pyroklast. Komp.)     |
|15103061 | tuffitische Brekzie | tuffitische Brekzie     |
|15103063 | tuffitischer Sandstein | tuffitischer Sandstein     |
|15103064 | tuffitischer Siltstein | tuffitischer Siltstein     |
|15103065 | tuffitischer Tonstein | tuffitischer Tonstein     |
|15103062 | tuffitisches Konglomerat | tuffitisches Konglomerat     |
|15101042 | Überschwemmungssediment | Überschwemmungssediment     |
|15103070 | Ultrabasisches Gestein | Ultrabasisches Gestein     |
|15104016 | Ultrakataklasit | Ultrakataklasit     |
|15104447 | ultramafisches Gestein | ultramafisches Gestein     |
|15104021 | Ultramylonit | Ultramylonit     |
|15101012 | Verwitterungslehm, undifferenziert | Verwitterungslehm, undifferenziert     |
|15101032 | Vorstossschotter | Vorstossschotter     |
|15101065 | vulkanische Asche | vulkanische Asche     |
|15101016 | zerrüttete Sackungsmasse | zerrüttete Sackungsmasse     |
|15104045 | Zweiglimmergneis | Zweiglimmergneis     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute chrono_t{#unconsolidated-deposits-plg-chrono-t}
__

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15001074 | Aalénien | Aalénien     |
|15001059 | Albien | Albien     |
|15001087 | Anisien | Anisien     |
|15001060 | Aptien | Aptien     |
|15001028 | Aquitanien | Aquitanien     |
|15001153 | Archaikum | Archaikum     |
|15001113 | Artinskien | Artinskien     |
|15001117 | Asselien | Asselien     |
|15001073 | Bajocien | Bajocien     |
|15001061 | Barrémien | Barrémien     |
|15001041 | Bartonien | Bartonien     |
|15001140 | Bashkirien | Bashkirien     |
|15001072 | Bathonien | Bathonien     |
|15001064 | Berriasien | Berriasien     |
|15001025 | Burdigalien | Burdigalien     |
|15001010 | Calabrien | Calabrien     |
|15001071 | Callovien | Callovien     |
|15001053 | Campanien | Campanien     |
|15001102 | Capitanien | Capitanien     |
|15001084 | Carnien | Carnien     |
|15001057 | Cénomanien | Cénomanien     |
|15001096 | Changhsingien | Changhsingien     |
|15001031 | Chattien | Chattien     |
|15001151 | Chibanien | Chibanien     |
|15001110 | Cisuralien | Cisuralien     |
|15001055 | Coniacien | Coniacien     |
|15001048 | Danien | Danien     |
|15001128 | Devon | Devon     |
|15001035 | Eozän | Eozän     |
|15001058 | Frühe Kreide | Frühe Kreide     |
|15001088 | Frühe Trias | Frühe Trias     |
|15001075 | Früher Jura | Früher Jura     |
|15001027 | frühes Burdigalien | frühes Burdigalien     |
|15001033 | frühes Chattien | frühes Chattien     |
|15001129 | Frühes Devon | Frühes Devon     |
|15001043 | Frühes Eozän | Frühes Eozän     |
|15001024 | Frühes Miozän | Frühes Miozän     |
|15001127 | Frühes Mississippien | Frühes Mississippien     |
|15001150 | Frühes Ordovizium | Frühes Ordovizium     |
|15001123 | Frühes Pennsylvanien | Frühes Pennsylvanien     |
|15001009 | Frühes Pleistozän | Frühes Pleistozän     |
|15001039 | frühes Priabonien | frühes Priabonien     |
|15001011 | Gélasien | Gélasien     |
|15001101 | Guadalupien | Guadalupien     |
|15001137 | Gzhélien | Gzhélien     |
|15001062 | Hauterivien | Hauterivien     |
|15001079 | Hettangien | Hettangien     |
|15001004 | Holozän | Holozän     |
|15001090 | Indusien | Indusien     |
|15001065 | Jura | Jura     |
|15001135 | Kambrium | Kambrium     |
|15001002 | Känozoikum | Känozoikum     |
|15001119 | Karbon | Karbon     |
|15001138 | Kasimovien | Kasimovien     |
|15001068 | Kimméridgien | Kimméridgien     |
|15001050 | Kreide | Kreide     |
|15001111 | Kungurien | Kungurien     |
|15001086 | Ladinien | Ladinien     |
|15001023 | Langhien | Langhien     |
|15001147 | Llandovery | Llandovery     |
|15001095 | Lopingien | Lopingien     |
|15001145 | Ludlow | Ludlow     |
|15001042 | Lutétien | Lutétien     |
|15001052 | Maastrichtien | Maastrichtien     |
|15001049 | Mesozoikum | Mesozoikum     |
|15001019 | Messinien | Messinien     |
|15001017 | Miozän | Miozän     |
|15001124 | Mississippien | Mississippien     |
|15001085 | Mittlere Trias | Mittlere Trias     |
|15001070 | Mittlerer Jura | Mittlerer Jura     |
|15001130 | Mittleres Devon | Mittleres Devon     |
|15001040 | Mittleres Eozän | Mittleres Eozän     |
|15001021 | Mittleres Miozän | Mittleres Miozän     |
|15001126 | Mittleres Mississippien | Mittleres Mississippien     |
|15001149 | Mittleres Ordovizium | Mittleres Ordovizium     |
|15001122 | Mittleres Pennsylvanien | Mittleres Pennsylvanien     |
|15001007 | Mittleres Pleistozän | Mittleres Pleistozän     |
|15001139 | Moscovien | Moscovien     |
|15001013 | Neogen | Neogen     |
|15001083 | Norien | Norien     |
|15001089 | Olénékien | Olénékien     |
|15001030 | Oligozän | Oligozän     |
|15001134 | Ordovizium | Ordovizium     |
|15001069 | Oxfordien | Oxfordien     |
|15001029 | Paläogen | Paläogen     |
|15001091 | Paläozoikum | Paläozoikum     |
|15001045 | Paleozän | Paleozän     |
|15001120 | Pennsylvanien | Pennsylvanien     |
|15001093 | Perm | Perm     |
|15001001 | Phanerozoikum | Phanerozoikum     |
|15001015 | Plaisancien | Plaisancien     |
|15001005 | Pleistozän | Pleistozän     |
|15001077 | Pliensbachien | Pliensbachien     |
|15001014 | Pliozän | Pliozän     |
|15001152 | Präkambrium | Präkambrium     |
|15001037 | Priabonien | Priabonien     |
|15001144 | Pridoli | Pridoli     |
|15001136 | Proterozoikum | Proterozoikum     |
|15001003 | Quartär | Quartär     |
|15001082 | Rhät | Rhät     |
|15001108 | Roadien | Roadien     |
|15001034 | Rupélien | Rupélien     |
|15001115 | Sakmarien | Sakmarien     |
|15001054 | Santonien | Santonien     |
|15001047 | Sélandien | Sélandien     |
|15001141 | Serpukhovien | Serpukhovien     |
|15001022 | Serravallien | Serravallien     |
|15001133 | Silur | Silur     |
|15001078 | Sinémurien | Sinémurien     |
|15001051 | Späte Kreide | Späte Kreide     |
|15001081 | Späte Trias | Späte Trias     |
|15001066 | Später Jura | Später Jura     |
|15001026 | spätes Burdigalien | spätes Burdigalien     |
|15001032 | spätes Chattien | spätes Chattien     |
|15001131 | Spätes Devon | Spätes Devon     |
|15001036 | Spätes Eozän | Spätes Eozän     |
|15001018 | Spätes Miozän | Spätes Miozän     |
|15001125 | Spätes Mississippien | Spätes Mississippien     |
|15001148 | Spätes Ordovizium | Spätes Ordovizium     |
|15001121 | Spätes Pennsylvanien | Spätes Pennsylvanien     |
|15001006 | Spätes Pleistozän | Spätes Pleistozän     |
|15001038 | spätes Priabonien | spätes Priabonien     |
|15001012 | Tertiär | Tertiär     |
|15001046 | Thanétien | Thanétien     |
|15001067 | Tithonien | Tithonien     |
|15001076 | Toarcien | Toarcien     |
|15001020 | Tortonien | Tortonien     |
|15001143 | Tournaisien | Tournaisien     |
|15001080 | Trias | Trias     |
|15001056 | Turonien | Turonien     |
|15001063 | Valanginien | Valanginien     |
|15001142 | Viséen | Viséen     |
|15001146 | Wenlock | Wenlock     |
|15001106 | Wordien | Wordien     |
|15001098 | Wuchiapingien | Wuchiapingien     |
|15001044 | Yprésien | Yprésien     |
|15001016 | Zancléen | Zancléen     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute chrono_b{#unconsolidated-deposits-plg-chrono-b}
__

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15001074 | Aalénien | Aalénien     |
|15001059 | Albien | Albien     |
|15001087 | Anisien | Anisien     |
|15001060 | Aptien | Aptien     |
|15001028 | Aquitanien | Aquitanien     |
|15001153 | Archaikum | Archaikum     |
|15001113 | Artinskien | Artinskien     |
|15001117 | Asselien | Asselien     |
|15001073 | Bajocien | Bajocien     |
|15001061 | Barrémien | Barrémien     |
|15001041 | Bartonien | Bartonien     |
|15001140 | Bashkirien | Bashkirien     |
|15001072 | Bathonien | Bathonien     |
|15001064 | Berriasien | Berriasien     |
|15001025 | Burdigalien | Burdigalien     |
|15001010 | Calabrien | Calabrien     |
|15001071 | Callovien | Callovien     |
|15001053 | Campanien | Campanien     |
|15001102 | Capitanien | Capitanien     |
|15001084 | Carnien | Carnien     |
|15001057 | Cénomanien | Cénomanien     |
|15001096 | Changhsingien | Changhsingien     |
|15001031 | Chattien | Chattien     |
|15001151 | Chibanien | Chibanien     |
|15001110 | Cisuralien | Cisuralien     |
|15001055 | Coniacien | Coniacien     |
|15001048 | Danien | Danien     |
|15001128 | Devon | Devon     |
|15001035 | Eozän | Eozän     |
|15001058 | Frühe Kreide | Frühe Kreide     |
|15001088 | Frühe Trias | Frühe Trias     |
|15001075 | Früher Jura | Früher Jura     |
|15001027 | frühes Burdigalien | frühes Burdigalien     |
|15001033 | frühes Chattien | frühes Chattien     |
|15001129 | Frühes Devon | Frühes Devon     |
|15001043 | Frühes Eozän | Frühes Eozän     |
|15001024 | Frühes Miozän | Frühes Miozän     |
|15001127 | Frühes Mississippien | Frühes Mississippien     |
|15001150 | Frühes Ordovizium | Frühes Ordovizium     |
|15001123 | Frühes Pennsylvanien | Frühes Pennsylvanien     |
|15001009 | Frühes Pleistozän | Frühes Pleistozän     |
|15001039 | frühes Priabonien | frühes Priabonien     |
|15001011 | Gélasien | Gélasien     |
|15001101 | Guadalupien | Guadalupien     |
|15001137 | Gzhélien | Gzhélien     |
|15001062 | Hauterivien | Hauterivien     |
|15001079 | Hettangien | Hettangien     |
|15001004 | Holozän | Holozän     |
|15001090 | Indusien | Indusien     |
|15001065 | Jura | Jura     |
|15001135 | Kambrium | Kambrium     |
|15001002 | Känozoikum | Känozoikum     |
|15001119 | Karbon | Karbon     |
|15001138 | Kasimovien | Kasimovien     |
|15001068 | Kimméridgien | Kimméridgien     |
|15001050 | Kreide | Kreide     |
|15001111 | Kungurien | Kungurien     |
|15001086 | Ladinien | Ladinien     |
|15001023 | Langhien | Langhien     |
|15001147 | Llandovery | Llandovery     |
|15001095 | Lopingien | Lopingien     |
|15001145 | Ludlow | Ludlow     |
|15001042 | Lutétien | Lutétien     |
|15001052 | Maastrichtien | Maastrichtien     |
|15001049 | Mesozoikum | Mesozoikum     |
|15001019 | Messinien | Messinien     |
|15001017 | Miozän | Miozän     |
|15001124 | Mississippien | Mississippien     |
|15001085 | Mittlere Trias | Mittlere Trias     |
|15001070 | Mittlerer Jura | Mittlerer Jura     |
|15001130 | Mittleres Devon | Mittleres Devon     |
|15001040 | Mittleres Eozän | Mittleres Eozän     |
|15001021 | Mittleres Miozän | Mittleres Miozän     |
|15001126 | Mittleres Mississippien | Mittleres Mississippien     |
|15001149 | Mittleres Ordovizium | Mittleres Ordovizium     |
|15001122 | Mittleres Pennsylvanien | Mittleres Pennsylvanien     |
|15001007 | Mittleres Pleistozän | Mittleres Pleistozän     |
|15001139 | Moscovien | Moscovien     |
|15001013 | Neogen | Neogen     |
|15001083 | Norien | Norien     |
|15001089 | Olénékien | Olénékien     |
|15001030 | Oligozän | Oligozän     |
|15001134 | Ordovizium | Ordovizium     |
|15001069 | Oxfordien | Oxfordien     |
|15001029 | Paläogen | Paläogen     |
|15001091 | Paläozoikum | Paläozoikum     |
|15001045 | Paleozän | Paleozän     |
|15001120 | Pennsylvanien | Pennsylvanien     |
|15001093 | Perm | Perm     |
|15001001 | Phanerozoikum | Phanerozoikum     |
|15001015 | Plaisancien | Plaisancien     |
|15001005 | Pleistozän | Pleistozän     |
|15001077 | Pliensbachien | Pliensbachien     |
|15001014 | Pliozän | Pliozän     |
|15001152 | Präkambrium | Präkambrium     |
|15001037 | Priabonien | Priabonien     |
|15001144 | Pridoli | Pridoli     |
|15001136 | Proterozoikum | Proterozoikum     |
|15001003 | Quartär | Quartär     |
|15001082 | Rhät | Rhät     |
|15001108 | Roadien | Roadien     |
|15001034 | Rupélien | Rupélien     |
|15001115 | Sakmarien | Sakmarien     |
|15001054 | Santonien | Santonien     |
|15001047 | Sélandien | Sélandien     |
|15001141 | Serpukhovien | Serpukhovien     |
|15001022 | Serravallien | Serravallien     |
|15001133 | Silur | Silur     |
|15001078 | Sinémurien | Sinémurien     |
|15001051 | Späte Kreide | Späte Kreide     |
|15001081 | Späte Trias | Späte Trias     |
|15001066 | Später Jura | Später Jura     |
|15001026 | spätes Burdigalien | spätes Burdigalien     |
|15001032 | spätes Chattien | spätes Chattien     |
|15001131 | Spätes Devon | Spätes Devon     |
|15001036 | Spätes Eozän | Spätes Eozän     |
|15001018 | Spätes Miozän | Spätes Miozän     |
|15001125 | Spätes Mississippien | Spätes Mississippien     |
|15001148 | Spätes Ordovizium | Spätes Ordovizium     |
|15001121 | Spätes Pennsylvanien | Spätes Pennsylvanien     |
|15001006 | Spätes Pleistozän | Spätes Pleistozän     |
|15001038 | spätes Priabonien | spätes Priabonien     |
|15001012 | Tertiär | Tertiär     |
|15001046 | Thanétien | Thanétien     |
|15001067 | Tithonien | Tithonien     |
|15001076 | Toarcien | Toarcien     |
|15001020 | Tortonien | Tortonien     |
|15001143 | Tournaisien | Tournaisien     |
|15001080 | Trias | Trias     |
|15001056 | Turonien | Turonien     |
|15001063 | Valanginien | Valanginien     |
|15001142 | Viséen | Viséen     |
|15001146 | Wenlock | Wenlock     |
|15001106 | Wordien | Wordien     |
|15001098 | Wuchiapingien | Wuchiapingien     |
|15001044 | Yprésien | Yprésien     |
|15001016 | Zancléen | Zancléen     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute mat_type
__


   

#### Attribute buried_out
__
_Datentyp:  boolean_



   

#### Attribute composit
__


   

#### Attribute admixture
__


   

#### Attribute structur{#unconsolidated-deposits-plg-structur}
_Textur des Lockergesteins_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14510011 | bioturbiert | bioturbiert     |
|14510002 | geschichtet | geschichtet     |
|14510005 | glaziale Überprägung (Glazitektonik) | glaziale Überprägung (Glazitektonik)     |
|14510004 | grossmassstäbliche Schrägschichtung (z.B. Deltaschichtung) | grossmassstäbliche Schrägschichtung (z.B. Deltaschichtung)     |
|14510010 | invers gradiert | invers gradiert     |
|14510007 | laminiert | laminiert     |
|14510008 | mit Warven | mit Warven     |
|14510009 | normal gradiert | normal gradiert     |
|14510012 | pedogen überprägt | pedogen überprägt     |
|14510006 | periglazial gestörte Schichtung (Diapir, Eiskeil, etc.) | periglazial gestörte Schichtung (Diapir, Eiskeil, etc.)     |
|14510003 | schräg-/kreuzgeschichtet | schräg-/kreuzgeschichtet     |
|14510001 | texturlos | texturlos     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute charact
_Spezifische Eigenschaft_


   

#### Attribute morpholo{#unconsolidated-deposits-plg-morpholo}
_Morphologie der Lockergesteinseinheit_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14512008 | Bastion | Bastion     |
|14512003 | Düne | Düne     |
|14512001 | Kegel / Fächer | Kegel / Fächer     |
|14512007 | Os | Os     |
|14512006 | Sander | Sander     |
|14512002 | Schleier | Schleier     |
|14512005 | Terrasse | Terrasse     |
|14512004 | Wall | Wall     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute glac_type{#unconsolidated-deposits-plg-glac-type}
_Gletschertyp; Attribut nur für Moränen_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14513009 | Aaregletscher | Aaregletscher     |
|14513004 | Bodensee-Rheingletscher | Bodensee-Rheingletscher     |
|14513013 | Brünig-Aaregletscher | Brünig-Aaregletscher     |
|14513003 | Bündner Gletscher | Bündner Gletscher     |
|14513012 | Engelberger Gletscher | Engelberger Gletscher     |
|14513002 | grosse Tal- und Vorlandgletscher | grosse Tal- und Vorlandgletscher     |
|14513005 | Linth-Rheingletscher | Linth-Rheingletscher     |
|14513001 | Lokalgletscher | Lokalgletscher     |
|14513006 | Reussgletscher | Reussgletscher     |
|14513010 | Saanegletscher | Saanegletscher     |
|14513011 | Schlierengletscher | Schlierengletscher     |
|14513007 | Waldemme- und Entlegletscher | Waldemme- und Entlegletscher     |
|14513008 | Walliser Gletscher | Walliser Gletscher     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute ref_year
_Zeitpunkt oder Zeitperiode. Zum Beispiel «1940 1943, Periode der Drainage» (muss präzisiert werden)_
_Datentyp:  string_



   

#### Attribute thin_cover{#unconsolidated-deposits-plg-thin-cover}
_Lockermaterialbedeckung, wenn vorhanden._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14515001 | geringmächtige Lockergesteinsbedeckung, undifferenziert | geringmächtige Lockergesteinsbedeckung, undifferenziert     |
|14515005 | geringmächtige Löss- oder Lösslehmbedeckung | geringmächtige Löss- oder Lösslehmbedeckung     |
|14515002 | geringmächtige Moränenbedeckung | geringmächtige Moränenbedeckung     |
|14515003 | geringmächtige Schotterbedeckung | geringmächtige Schotterbedeckung     |
|14515004 | geringmächtige Schwemmlehmbedeckung | geringmächtige Schwemmlehmbedeckung     |
|14515006 | tiefgründige Verwitterungsdecke | tiefgründige Verwitterungsdecke     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute orig_descr
_Originalbezeichnung gemäss der Legende der zugrundeliegenden geologischen Karte_


   

### Class Bedrock_PLG ###
Die Klasse Bedrock_PLG enthält alle flächenbildenden lithostratigraphischen Festgesteinseinheiten. Die Angabe,  ob ein Festgestein bewegt (durch Gravitation versetzt) wurde, geht aus der Klasse Instabilities_within_Bedrock_PLG (Thema Geomorphology) hervor.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Spezifische Eigenschaft 
[]()           | Cardinality [1] | 14334001                                       |  
2 | **fm_homog**                |                                     | Gesteinsaufbau 
[]()           | Cardinality [] |                                        |  
3 | **listrat**                | [CodedDomain](#bedrock-plg-listrat)                    | Lithostratigraphische Einhei 
[]()           | Cardinality [1] |                                                      |  
4 | **litho**                | [CodedDomain](#bedrock-plg-litho)                    | Lithologische Beschreibung 
[]()           | Cardinality [1..3] |                                                      |  
5 | **chrono_t**                | [CodedDomain](#bedrock-plg-chrono-t)                    | Chronostratigraphische Zuordnung der Obergrenze der Kartiereinheit (Top) 
[]()           | Cardinality [1] |                                                      |  
6 | **chrono_b**                | [CodedDomain](#bedrock-plg-chrono-b)                    | Chronostratigraphische Zuordnung der Untergrenze der Kartiereinheit (Basis) 
[]()           | Cardinality [1] |                                                      |  
7 | **tecto**                | [CodedDomain](#bedrock-plg-tecto)                    | Tektonische Zugehörigkeit 
[]()           | Cardinality [1] |                                                      |  
8 | **orig_descr**                | string                                    | Originalbezeichnung gemäss der Legende der zugrundeliegenden geologischen Karte 
[]()           | Cardinality [1] |                                        |  
9 | **buried_out**                | boolean                                    | Wurde das Festgestein wieder verdeckt (ja / nein)? 
[]()           | Cardinality [1] |                                        |  
10 | **exotic_ele**                |                                     | Handelt es sich bei der Objektart um ein exotisches Element; z.B. Einschluss, Linse, Tasche, Olistholith (ja / nein)? 
[]()           | Cardinality [1] | boolean                                       |  
11 | **colour**                | string                                    | Farbe des Gesteins. Präzisieren ob es sich um die Bruchfarbe, die Verwitterungsfarbe, etc. handelt; z.B.Verwitterungsfarbe grau. 
[]()           | Cardinality [0..1] |                                        |  
12 | **sedi_main_com**                | [CodedDomain](#bedrock-plg-sedi-main-com)                    | Hauptgesteinskomponente des klastischen Sedimentgesteins 
[]()           | Cardinality [0..1] |                                                      |  
13 | **sedi_seco_com**                | [CodedDomain](#bedrock-plg-sedi-seco-com)                    | Nebengesteinskomponente des Sedimentgesteins 
[]()           | Cardinality [0..2] |                                                      |  
14 | **sedi_bond_mat**                | [CodedDomain](#bedrock-plg-sedi-bond-mat)                    | Bindemittel des Sedimentgesteins 
[]()           | Cardinality [0..1] |                                                      |  
15 | **sedi_bedding**                | [CodedDomain](#bedrock-plg-sedi-bedding)                    | Schichtung des Sedimentgesteins 
[]()           | Cardinality [0..2] |                                                      |  
16 | **sedi_str**                | [CodedDomain](#bedrock-plg-sedi-str)                    | Textur des Sedimentgesteins 
[]()           | Cardinality [0..2] |                                                      |  
17 | **sedi_tex**                | [CodedDomain](#bedrock-plg-sedi-tex)                    | Sedimentstruktur 
[]()           | Cardinality [] |                                                      |  
18 | **igne_text**                | [CodedDomain](#bedrock-plg-igne-text)                    | Struktur des magmatischen Gesteins 
[]()           | Cardinality [0..1] |                                                      |  
19 | **igne_grain_si**                | [CodedDomain](#bedrock-plg-igne-grain-si)                    | Korngrösse des magmatischen Gesteins 
[]()           | Cardinality [0..1] |                                                      |  
20 | **igne_affinity**                | [CodedDomain](#bedrock-plg-igne-affinity)                    | Affinität zu einer magmatischen Serie. 
[]()           | Cardinality [] |                                                      |  
21 | **meta_full_name**                | string                                    | Bezeichnung des metamorphen Gesteins 
[]()           | Cardinality [0..1] |                                        |  
22 | **meta_mineral**                | [CodedDomain](#bedrock-plg-meta-mineral)                    | Wichtiges Mineral des metamorphen Gesteins 
[]()           | Cardinality [0..3] |                                                      |  
23 | **meta_str**                | [CodedDomain](#bedrock-plg-meta-str)                    | Textur des metamorphen Gesteins 
[]()           | Cardinality [0..3] |                                                      |  





#### Attribute kind
_Spezifische Eigenschaft_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14334001 | Rbed Festgestein | Rbed Festgestein     |


   

#### Attribute fm_homog
_Gesteinsaufbau_


   

#### Attribute listrat{#bedrock-plg-listrat}
_Lithostratigraphische Einhei_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15204121 | «Ältere Orthogneise» | «Ältere Orthogneise»     |
|15203300 | «Arblatsch-Flysch» | «Arblatsch-Flysch»     |
|15203302 | «Arblatsch-Konglomerat» | «Arblatsch-Konglomerat»     |
|15202417 | «Basaler Quarzit» (Coroi-Fm.) | «Basaler Quarzit» (Coroi-Fm.)     |
|15202437 | «Calcaire à ciment» (Bifé-Fm.) | «Calcaire à ciment» (Bifé-Fm.)     |
|15202428 | «Calcaire siliceux brunâtre» | «Calcaire siliceux brunâtre»     |
|15200674 | «Calcaires à Entroques» | «Calcaires à Entroques»     |
|15202433 | «Calcaires bréchiques» | «Calcaires bréchiques»     |
|15202426 | «Calcaires gréso-glauconieux» | «Calcaires gréso-glauconieux»     |
|15202427 | «Calcarénites beiges oolitiques» | «Calcarénites beiges oolitiques»     |
|15202420 | «Equisetenschiefer» | «Equisetenschiefer»     |
|15200594 | «Formation de la Chambotte Inférieure» | «Formation de la Chambotte Inférieure»     |
|15200593 | «Formation de la Chambotte Supérieure» | «Formation de la Chambotte Supérieure»     |
|15204120 | «Jüngere Orthogneise» | «Jüngere Orthogneise»     |
|15200510 | «Juranagelfluh-Mergel» | «Juranagelfluh-Mergel»     |
|15202406 | «Leitoolith» | «Leitoolith»     |
|15202425 | «Marnes noires pyriteuses» | «Marnes noires pyriteuses»     |
|15202099 | «Mergelband» | «Mergelband»     |
|15203339 | «Mittlere Rauwacke» (St-Triphon-Fm.) | «Mittlere Rauwacke» (St-Triphon-Fm.)     |
|15202415 | «Obere Tonschiefer» (Bommerstein-Fm.) | «Obere Tonschiefer» (Bommerstein-Fm.)     |
|15202412 | «Obere Zementsteinschichten» | «Obere Zementsteinschichten»     |
|15202398 | «Oberer Betliskalk» | «Oberer Betliskalk»     |
|15202383 | «Oberer Öhrlikalk» | «Oberer Öhrlikalk»     |
|15202384 | «Oberer Öhrlimergel» | «Oberer Öhrlimergel»     |
|15202300 | «Oberer Schrattenkalk» | «Oberer Schrattenkalk»     |
|15200592 | «Pierre Jaune Inférieure» | «Pierre Jaune Inférieure»     |
|15200591 | «Pierre Jaune Supérieure» | «Pierre Jaune Supérieure»     |
|15203077 | «Posidonienschiefer» (der Stanserhorn-Fm.) | «Posidonienschiefer» (der Stanserhorn-Fm.)     |
|15203331 | «Roffna-Porphyr» | «Roffna-Porphyr»     |
|15202414 | «Rote Echinodermenbrekzie» | «Rote Echinodermenbrekzie»     |
|15202395 | «Roter Seewenkalk» | «Roter Seewenkalk»     |
|15202103 | «Schilt-Kalk» | «Schilt-Kalk»     |
|15202102 | «Schilt-Mergel» | «Schilt-Mergel»     |
|15205090 | «Série Rubanée» | «Série Rubanée»     |
|15203338 | «Silex-Niveau» (St-Triphon-Fm.) | «Silex-Niveau» (St-Triphon-Fm.)     |
|15202413 | «Untere Zementsteinschichten» | «Untere Zementsteinschichten»     |
|15202399 | «Unterer Betliskalk» | «Unterer Betliskalk»     |
|15202385 | «Unterer Öhrlikalk» | «Unterer Öhrlikalk»     |
|15202301 | «Unterer Schrattenkalk» | «Unterer Schrattenkalk»     |
|15202360 | «Wildflysch», undifferenziert | «Wildflysch», undifferenziert     |
|15200397 | Aargauer Juranagelfluh | Aargauer Juranagelfluh     |
|15200559 | Aarwangen-Molasse | Aarwangen-Molasse     |
|15200291 | Abtwil-Konglomerat | Abtwil-Konglomerat     |
|15200494 | Achdorf-Formation | Achdorf-Formation     |
|15206004 | Adamello-Intrusiva | Adamello-Intrusiva     |
|15203198 | Adlerflüe-Formation | Adlerflüe-Formation     |
|15204021 | Adnet-Kalk | Adnet-Kalk     |
|15203515 | Adula-D.: Albit-Oligoklasgneis | Adula-D.: Albit-Oligoklasgneis     |
|15203256 | Adula-D.: Amphibolit | Adula-D.: Amphibolit     |
|15203512 | Adula-D.: Basaler Gneis | Adula-D.: Basaler Gneis     |
|15203255 | Adula-D.: Glimmerschiefer und Paragneis | Adula-D.: Glimmerschiefer und Paragneis     |
|15203532 | Adula-D.: Kalkschiefer und Marmor | Adula-D.: Kalkschiefer und Marmor     |
|15203535 | Adula-D.: Ultramafitit | Adula-D.: Ultramafitit     |
|15200285 | Aeugstertal-Bentonit | Aeugstertal-Bentonit     |
|15204020 | Agnelli-Formation | Agnelli-Formation     |
|15203058 | Agreblierai-Member | Agreblierai-Member     |
|15202291 | Ahornen-Member | Ahornen-Member     |
|15203334 | Aigremont-Brekzie | Aigremont-Brekzie     |
|15203416 | Aiguilles-Rouges-d&#39;Arolla-Metagabbro | Aiguilles-Rouges-d&#39;Arolla-Metagabbro     |
|15200373 | Ajoie-Gompholit | Ajoie-Gompholit     |
|15200384 | Ajoie-Member | Ajoie-Member     |
|15200459 | Akzessorische Mumienbänke | Akzessorische Mumienbänke     |
|15205045 | Albenza-Formation | Albenza-Formation     |
|15203270 | Albeuve-Serie | Albeuve-Serie     |
|15206069 | Albit-Muskowitschiefer, undifferenziert | Albit-Muskowitschiefer, undifferenziert     |
|15203463 | Albitaugenschiefer (SOPA) der Adlerflüe-Formation | Albitaugenschiefer (SOPA) der Adlerflüe-Formation     |
|15203379 | Albitquarzit der Grava- und Tomül-Decke | Albitquarzit der Grava- und Tomül-Decke     |
|15200563 | Albstein | Albstein     |
|15200231 | Albtal-Granit | Albtal-Granit     |
|15200154 | Alectryonia-Kalk | Alectryonia-Kalk     |
|15204133 | alkalische Intrusiva des Ostalpins | alkalische Intrusiva des Ostalpins     |
|15203229 | Allalin-Gabbro | Allalin-Gabbro     |
|15204016 | Allgäu-Formation | Allgäu-Formation     |
|15203031 | Allières-Member | Allières-Member     |
|15203451 | Almagelhorn-Migmatit | Almagelhorn-Migmatit     |
|15202338 | Alp-Cavradi-Gneiskomplex | Alp-Cavradi-Gneiskomplex     |
|15202530 | Alp-Crap-Ner-Granit | Alp-Crap-Ner-Granit     |
|15202344 | Alp-Ramosa-Granitgneis | Alp-Ramosa-Granitgneis     |
|15203560 | Alpbach-Schiefer | Alpbach-Schiefer     |
|15206012 | Alpe-Cameraccio-Granodiorit | Alpe-Cameraccio-Granodiorit     |
|15203353 | Alpe-Tamia-Campo-Wildflysch | Alpe-Tamia-Campo-Wildflysch     |
|15203479 | Alpigia-Gneis | Alpigia-Gneis     |
|15204148 | Alpiner Muschelkalk | Alpiner Muschelkalk     |
|15204029 | Alplihorn-Member | Alplihorn-Member     |
|15200634 | Altbach-Süsswasserkalk | Altbach-Süsswasserkalk     |
|15204051 | Altein-Formation | Altein-Formation     |
|15200228 | Ältere Flussablagerungen | Ältere Flussablagerungen     |
|15200527 | Ältere Juranagelfluh | Ältere Juranagelfluh     |
|15202481 | Altkristallin des Aiguilles-Rouges-Massivs, migmatitisch | Altkristallin des Aiguilles-Rouges-Massivs, migmatitisch     |
|15202478 | Altkristallin des Mont-Blanc-Massivs, amphibolitreich | Altkristallin des Mont-Blanc-Massivs, amphibolitreich     |
|15202477 | Altkristallin des Mont-Blanc-Massivs, migmatitisch | Altkristallin des Mont-Blanc-Massivs, migmatitisch     |
|15202479 | Altkristallin des Mont-Blanc-Massivs, mylonitisch | Altkristallin des Mont-Blanc-Massivs, mylonitisch     |
|15202078 | Altmann-Member | Altmann-Member     |
|15204023 | Alv-Brekzie | Alv-Brekzie     |
|15200577 | Amaltheenton-Formation | Amaltheenton-Formation     |
|15202049 | Amden-Mergel | Amden-Mergel     |
|15204006 | Ammergau-Formation | Ammergau-Formation     |
|15205120 | Amphibolit der Valpelline-Gruppe | Amphibolit der Valpelline-Gruppe     |
|15203466 | Amphibolit des Ergischhorn-Ensembles | Amphibolit des Ergischhorn-Ensembles     |
|15206037 | Amphibolit, undifferenziert | Amphibolit, undifferenziert     |
|15200574 | Ancepsoolith-Subformation | Ancepsoolith-Subformation     |
|15205067 | Andesit und Dazit | Andesit und Dazit     |
|15203489 | Andolla-Eklogit | Andolla-Eklogit     |
|15203097 | Andonces-Member | Andonces-Member     |
|15200047 | Ängistein-Member | Ängistein-Member     |
|15200581 | Angulatenton-Formation | Angulatenton-Formation     |
|15203358 | Antabia-Gruppe | Antabia-Gruppe     |
|15203365 | Antigorio-Orthogneis | Antigorio-Orthogneis     |
|15200286 | Äntlisberg-Doldertobel-Süsswasserkalk | Äntlisberg-Doldertobel-Süsswasserkalk     |
|15200052 | Anwil-Bank | Anwil-Bank     |
|15206039 | Aplit | Aplit     |
|15206112 | Aplitgneis, undifferenziert | Aplitgneis, undifferenziert     |
|15202326 | Aplitische Randfazies des Zentralen Aare-Granits | Aplitische Randfazies des Zentralen Aare-Granits     |
|15200290 | Appenzellergranit-Leitniveau | Appenzellergranit-Leitniveau     |
|15203136 | Aptychenkalk | Aptychenkalk     |
|15206116 | Aptychenkalk, undiff. | Aptychenkalk, undiff.     |
|15202137 | Arandellys-Formation | Arandellys-Formation     |
|15203301 | Arblatsch-Sandstein | Arblatsch-Sandstein     |
|15200462 | Arenicolites-Bank | Arenicolites-Bank     |
|15203378 | Areua-Bruschghorn-Melange | Areua-Bruschghorn-Melange     |
|15200580 | Arietenkalk-Formation | Arietenkalk-Formation     |
|15204049 | Arlberg-Formation | Arlberg-Formation     |
|15203159 | Aroley-Schichten | Aroley-Schichten     |
|15205004 | Arolla-Serie | Arolla-Serie     |
|15203561 | Arosa-D.: Gabbro | Arosa-D.: Gabbro     |
|15203230 | Arosa-Mélange | Arosa-Mélange     |
|15202474 | Arpette-Leukogranit | Arpette-Leukogranit     |
|15203053 | Arvel-Formation | Arvel-Formation     |
|15202446 | Arveyes-Flysch | Arveyes-Flysch     |
|15200155 | Arzier-Mergel | Arzier-Mergel     |
|15200131 | Asp-Member | Asp-Member     |
|15200450 | Astieria-Mergel | Astieria-Mergel     |
|15202358 | Au-d&#39;Arbignon-Schiefer | Au-d&#39;Arbignon-Schiefer     |
|15202055 | Aubrig-Schichten | Aubrig-Schichten     |
|15203401 | Augengneis der Berisal-Decke | Augengneis der Berisal-Decke     |
|15203478 | Augengneis der Maggia-Decke | Augengneis der Maggia-Decke     |
|15206067 | Augengneis, undifferenziert | Augengneis, undifferenziert     |
|15204110 | Augsten-Brekzie | Augsten-Brekzie     |
|15203249 | Aul-Marmor | Aul-Marmor     |
|15203517 | Aula-Spruga-Gneiskomplex | Aula-Spruga-Gneiskomplex     |
|15202258 | Ausserberg-Avat-Zone | Ausserberg-Avat-Zone     |
|15202268 | Ausserbinn-Piz-Cavel-Zone | Ausserbinn-Piz-Cavel-Zone     |
|15202130 | Bachalp-Formation | Bachalp-Formation     |
|15200104 | Baden-Member | Baden-Member     |
|15200457 | Balmberg-Oolith | Balmberg-Oolith     |
|15202484 | Balmenegg-Granit | Balmenegg-Granit     |
|15203278 | Balmi-Member | Balmi-Member     |
|15200188 | Balsthal-Formation | Balsthal-Formation     |
|15200648 | Baltersweil-Nagelfluh | Baltersweil-Nagelfluh     |
|15202187 | Baltschieder-Granodiorit | Baltschieder-Granodiorit     |
|15202549 | Baltschieder-Granodiorit: Biotittonalit | Baltschieder-Granodiorit: Biotittonalit     |
|15202550 | Baltschieder-Granodiorit: Hornblende Biotittonalit | Baltschieder-Granodiorit: Hornblende Biotittonalit     |
|15202030 | Band-Member | Band-Member     |
|15206097 | Bänder- und Schollenamphibolit, undifferenziert | Bänder- und Schollenamphibolit, undifferenziert     |
|15203464 | Bänderamphibolit der Adlerflüe-Formation | Bänderamphibolit der Adlerflüe-Formation     |
|15203477 | Bändergneis der Maggia-Decke | Bändergneis der Maggia-Decke     |
|15203445 | Bändergneis der Monte-Rosa-Decke | Bändergneis der Monte-Rosa-Decke     |
|15206093 | Bändergneis, undifferenziert | Bändergneis, undifferenziert     |
|15200128 | Bänkerjoch-Formation | Bänkerjoch-Formation     |
|15202110 | Bannalp-Konglomerat | Bannalp-Konglomerat     |
|15200020 | Banné-Member | Banné-Member     |
|15204012 | Bardella-Formation | Bardella-Formation     |
|15202328 | Bäregg-Gneiskomplex | Bäregg-Gneiskomplex     |
|15202567 | Bäregg-Gneiskomplex: Metavulkanite | Bäregg-Gneiskomplex: Metavulkanite     |
|15202565 | Bäregg-Gneiskomplex: mylonitischer Orthogneis | Bäregg-Gneiskomplex: mylonitischer Orthogneis     |
|15202566 | Bäregg-Gneiskomplex: mylonitischer Paragneis | Bäregg-Gneiskomplex: mylonitischer Paragneis     |
|15203178 | Bärenhorn-Formation | Bärenhorn-Formation     |
|15203580 | Bärenhorn-Formation: Quarzsandstein | Bärenhorn-Formation: Quarzsandstein     |
|15203531 | Bargella-Brekzie | Bargella-Brekzie     |
|15200223 | Bärhalde-Granit | Bärhalde-Granit     |
|15203182 | Barrhorn-Serie | Barrhorn-Serie     |
|15200672 | Bärschwil- bis St-Ursanne-Formation, undifferenziert | Bärschwil- bis St-Ursanne-Formation, undifferenziert     |
|15200006 | Bärschwil-Formation | Bärschwil-Formation     |
|15203380 | Basale Tonschiefer der Grava- und Tomül-Decke | Basale Tonschiefer der Grava- und Tomül-Decke     |
|15202452 | Basaler Mines-Lias | Basaler Mines-Lias     |
|15203123 | Basaler Schlieren-Flysch | Basaler Schlieren-Flysch     |
|15205069 | Basaler Tuf | Basaler Tuf     |
|15202172 | Basales Konglomerat (Bifertengrätli) | Basales Konglomerat (Bifertengrätli)     |
|15205068 | Basalt | Basalt     |
|15206079 | Basalt, undifferenziert | Basalt, undifferenziert     |
|15200394 | Basisbildungen der USM-J | Basisbildungen der USM-J     |
|15206049 | Basischer Gang | Basischer Gang     |
|15200433 | Basiskonglomerat (der Luzern-Fm.) | Basiskonglomerat (der Luzern-Fm.)     |
|15203173 | Basiskonglomerat der Stätzerhorn-Gruppe | Basiskonglomerat der Stätzerhorn-Gruppe     |
|15203148 | Basisserie | Basisserie     |
|15200396 | Basler Juranagelfluh | Basler Juranagelfluh     |
|15203521 | Batnall-Gneis | Batnall-Gneis     |
|15202039 | Batöni-Member | Batöni-Member     |
|15203208 | Bavugls-Gruppe | Bavugls-Gruppe     |
|15203024 | Beaumont-Konglomerat | Beaumont-Konglomerat     |
|15202528 | Beesten-Fazies | Beesten-Fazies     |
|15200086 | Beggingen-Member | Beggingen-Member     |
|15200340 | Beichlen-Formation | Beichlen-Formation     |
|15200127 | Belchen-Member | Belchen-Member     |
|15204081 | Bellaluna-Member | Bellaluna-Member     |
|15205062 | Bellano-Formation | Bellano-Formation     |
|15200662 | Bellegarde-Bank | Bellegarde-Bank     |
|15200402 | Belpberg-Formation | Belpberg-Formation     |
|15205024 | Bergamo-Flysch | Bergamo-Flysch     |
|15206006 | Bergell-Granodiorit | Bergell-Granodiorit     |
|15206003 | Bergell-Intrusiva | Bergell-Intrusiva     |
|15206007 | Bergell-Tonalit | Bergell-Tonalit     |
|15202377 | Berglikehle-Bank | Berglikehle-Bank     |
|15200208 | Berlingen-Member | Berlingen-Member     |
|15205097 | Berrio-Gabbro | Berrio-Gabbro     |
|15205060 | Besano-Formation | Besano-Formation     |
|15205039 | Besazio-Kalk | Besazio-Kalk     |
|15202135 | Besoëns-Formation | Besoëns-Formation     |
|15202084 | Betlis-Formation | Betlis-Formation     |
|15203530 | Bettlerjoch-Brekzie | Bettlerjoch-Brekzie     |
|15202115 | Bietenhorn-Member | Bietenhorn-Member     |
|15202436 | Bifé-Formation | Bifé-Formation     |
|15202193 | Bifertenfirn-Formation | Bifertenfirn-Formation     |
|15202169 | Bifertengrätli-Formation | Bifertengrätli-Formation     |
|15206046 | Biogener Kalk (Eozän) | Biogener Kalk (Eozän)     |
|15203126 | Biot-Formation | Biot-Formation     |
|15206092 | Biotit-Plagioklasgneis, undifferenziert | Biotit-Plagioklasgneis, undifferenziert     |
|15203444 | Biotitgneis der Monte-Rosa-Decke | Biotitgneis der Monte-Rosa-Decke     |
|15200117 | Birmenstorf-Member | Birmenstorf-Member     |
|15200271 | Bischofzell-Bentonit | Bischofzell-Bentonit     |
|15202475 | Bitschji-Augengneis | Bitschji-Augengneis     |
|15200124 | Blagdeni-Schichten | Blagdeni-Schichten     |
|15200489 | Blagdeni-Subformation | Blagdeni-Subformation     |
|15204007 | Blais-Formation | Blais-Formation     |
|15204018 | Blaisun-Member | Blaisun-Member     |
|15200259 | Blapbach-Kohleflöz | Blapbach-Kohleflöz     |
|15202287 | Blattengrat-Sandstein | Blattengrat-Sandstein     |
|15200233 | Blauen-Granit | Blauen-Granit     |
|15200492 | Blaukalk-Subformation | Blaukalk-Subformation     |
|15202109 | Blegi-Eisenoolith | Blegi-Eisenoolith     |
|15200461 | Bleiglanz-Bank | Bleiglanz-Bank     |
|15203306 | Bleis-Pintgas-Formation | Bleis-Pintgas-Formation     |
|15202535 | Blockmergel (Spirstock) | Blockmergel (Spirstock)     |
|15203279 | Bodeflue-Member | Bodeflue-Member     |
|15200583 | Bodensee-Nagelfluh | Bodensee-Nagelfluh     |
|15202318 | Bodevena-Melange | Bodevena-Melange     |
|15203286 | Boëge-Mergel | Boëge-Mergel     |
|15200175 | Bohnerzton | Bohnerzton     |
|15203057 | Bois-de-Luan-Member | Bois-de-Luan-Member     |
|15200301 | Bois-de-Raube-Formation | Bois-de-Raube-Formation     |
|15200385 | Bois-de-Raube-Member | Bois-de-Raube-Member     |
|15200333 | Bois-Genoud-Bentonit | Bois-Genoud-Bentonit     |
|15200652 | Bôle-Member | Bôle-Member     |
|15200046 | Bollement-Member | Bollement-Member     |
|15200176 | Boluston | Boluston     |
|15202583 | Bommerstein- und Reischiben-Formation, undifferenziert | Bommerstein- und Reischiben-Formation, undifferenziert     |
|15202116 | Bommerstein-Formation | Bommerstein-Formation     |
|15203103 | Bonave-Formation | Bonave-Formation     |
|15203265 | Bonaveau-Kalk | Bonaveau-Kalk     |
|15203311 | Bonigersee-Augengneis | Bonigersee-Augengneis     |
|15200585 | Bonneville-Sandstein | Bonneville-Sandstein     |
|15202232 | Borel-Gneiskomplex | Borel-Gneiskomplex     |
|15203520 | Bosco-Gneis | Bosco-Gneis     |
|15203425 | Böshorn-Gneis | Böshorn-Gneis     |
|15200242 | Böttstein-Granit | Böttstein-Granit     |
|15205088 | Bouquetins-Quarzdiorit | Bouquetins-Quarzdiorit     |
|15200049 | Bözen-Member | Bözen-Member     |
|15204065 | Brachiopodenkalk-Member | Brachiopodenkalk-Member     |
|15203079 | Brand-Formation | Brand-Formation     |
|15200499 | Brand-Herrentisch-Tuffit | Brand-Herrentisch-Tuffit     |
|15203383 | Brasses-Formation | Brasses-Formation     |
|15200460 | Brauner Oolith | Brauner Oolith     |
|15205048 | Brecce Retiche | Brecce Retiche     |
|15200079 | Breitenmatt-Member | Breitenmatt-Member     |
|15203487 | Breithorn-Serpentinit | Breithorn-Serpentinit     |
|15203504 | Brekzie-Formation | Brekzie-Formation     |
|15200328 | Brendenbach-Mergel | Brendenbach-Mergel     |
|15205021 | Brenno-Formation | Brenno-Formation     |
|15202215 | Breya-Rhyolith | Breya-Rhyolith     |
|15203510 | Brione-Gabbro | Brione-Gabbro     |
|15202065 | Brisi-Kalk | Brisi-Kalk     |
|15202064 | Brisi-Member | Brisi-Member     |
|15202066 | Brisi-Sandstein | Brisi-Sandstein     |
|15202190 | Bristenstock-Syenit | Bristenstock-Syenit     |
|15205044 | Broccatello d&#39;Arzo | Broccatello d&#39;Arzo     |
|15200204 | Brot-Schichten | Brot-Schichten     |
|15200065 | Brüggli-Member | Brüggli-Member     |
|15203183 | Bruneggjoch-Formation | Bruneggjoch-Formation     |
|15203347 | Bruneggjoch-Metabauxit | Bruneggjoch-Metabauxit     |
|15202178 | Brunni-Granit | Brunni-Granit     |
|15202121 | Brunnistock-Formation | Brunnistock-Formation     |
|15200417 | Brüttelen-Muschelnagelfluh | Brüttelen-Muschelnagelfluh     |
|15200185 | Bryozoen-Mergel | Bryozoen-Mergel     |
|15204130 | Buffalora-Gruppe | Buffalora-Gruppe     |
|15202163 | Bugnei-Granodiorit | Bugnei-Granodiorit     |
|15200034 | Buix-Member | Buix-Member     |
|15202087 | Büls-Bank | Büls-Bank     |
|15200535 | Bumbach-Nagelfluh | Bumbach-Nagelfluh     |
|15206084 | Bündnerschiefer, kalkig | Bündnerschiefer, kalkig     |
|15206085 | Bündnerschiefer, tonig | Bündnerschiefer, tonig     |
|15206066 | Bündnerschiefer, undifferenziert | Bündnerschiefer, undifferenziert     |
|15200324 | Bunte Rigi-Nagelfluh | Bunte Rigi-Nagelfluh     |
|15203570 | Bunter schiefriger Dolomit und Rauwacke der Klippen-Decke | Bunter schiefriger Dolomit und Rauwacke der Klippen-Decke     |
|15202503 | Buntgefleckte Schiefer | Buntgefleckte Schiefer     |
|15200143 | Buntsandstein | Buntsandstein     |
|15200029 | Bure-Member | Bure-Member     |
|15202288 | Burg-Sandstein | Burg-Sandstein     |
|15202595 | Bürgen- und Wildstrubel-Formation, undiff. | Bürgen- und Wildstrubel-Formation, undiff.     |
|15202032 | Bürgen-Formation | Bürgen-Formation     |
|15200102 | Burghorn-Formation | Burghorn-Formation     |
|15203332 | Burgruinen-Gneis | Burgruinen-Gneis     |
|15200407 | Bütschelbach-Nagelfluh | Bütschelbach-Nagelfluh     |
|15203238 | Buufal-Konglomerat | Buufal-Konglomerat     |
|15202222 | Cacciola-Granit | Cacciola-Granit     |
|15205012 | Cagno-Sandstein | Cagno-Sandstein     |
|15200455 | Calcaire âpre | Calcaire âpre     |
|15200654 | Calcaire Roux | Calcaire Roux     |
|15200383 | Calcaire roux marneux | Calcaire roux marneux     |
|15205035 | Calcari a bivalvi planctonici | Calcari a bivalvi planctonici     |
|15202264 | Calmut-Gneiskomplex | Calmut-Gneiskomplex     |
|15203234 | Calpionellenkalk der Arosa-Zone | Calpionellenkalk der Arosa-Zone     |
|15203498 | Calpionellenkalk der Platta-Decke | Calpionellenkalk der Platta-Decke     |
|15204142 | Campocologno-Gabbro | Campocologno-Gabbro     |
|15200036 | Caquerelle-Pisolith | Caquerelle-Pisolith     |
|15204114 | Carale-Paraschiefer | Carale-Paraschiefer     |
|15202132 | Cardinia-Member | Cardinia-Member     |
|15203174 | Carnusa-Formation | Carnusa-Formation     |
|15205055 | Cassina-Bank | Cassina-Bank     |
|15205008 | Castel-di-Sotto-Ton | Castel-di-Sotto-Ton     |
|15202472 | Catogne-Gneiskomplex | Catogne-Gneiskomplex     |
|15205057 | Cava Inferiore | Cava Inferiore     |
|15205056 | Cava Superiore | Cava Superiore     |
|15203437 | Cavalli-Formation | Cavalli-Formation     |
|15202191 | Cavardiras-Gruppe | Cavardiras-Gruppe     |
|15204143 | Celerina-Orthogneis | Celerina-Orthogneis     |
|15205084 | Ceneri-Gneis | Ceneri-Gneis     |
|15203529 | Cenomanbrekzien-Serie | Cenomanbrekzien-Serie     |
|15200668 | Censeau-Mergel | Censeau-Mergel     |
|15202445 | Cergnement-Member | Cergnement-Member     |
|15200014 | Chailley-Member | Chailley-Member     |
|15203035 | Chällihorn-Member | Chällihorn-Member     |
|15200098 | Chambotte-Formation | Chambotte-Formation     |
|15200630 | Champ-Vuillerat-Süsswasserkalk | Champ-Vuillerat-Süsswasserkalk     |
|15202498 | Chamseeli-Konglomerat | Chamseeli-Konglomerat     |
|15203392 | Chandoline-Sandstein | Chandoline-Sandstein     |
|15204002 | Chanèls-Formation | Chanèls-Formation     |
|15202149 | Chartegg-Formation | Chartegg-Formation     |
|15204106 | Chaschauna-Brekzie | Chaschauna-Brekzie     |
|15202241 | Chastelhorn-Metagabbro | Chastelhorn-Metagabbro     |
|15200053 | Châtillon-Member | Châtillon-Member     |
|15203055 | Chauderon-Formation | Chauderon-Formation     |
|15203591 | Chavanette- und Rubli-Member, undifferenziert | Chavanette- und Rubli-Member, undifferenziert     |
|15203093 | Chavanette-Member | Chavanette-Member     |
|15204075 | Chazforà-Formation | Chazforà-Formation     |
|15203019 | Chenaux-Rouges-Formation | Chenaux-Rouges-Formation     |
|15203021 | Chenaux-Rouges-Mineralkruste | Chenaux-Rouges-Mineralkruste     |
|15202335 | Chéserys-Gneis | Chéserys-Gneis     |
|15203002 | Chesselbach-Formation | Chesselbach-Formation     |
|15200035 | Chestel-Member | Chestel-Member     |
|15203127 | Chétillon-Formation | Chétillon-Formation     |
|15203050 | Chevalets-Member | Chevalets-Member     |
|15200187 | Chevenez-Member | Chevenez-Member     |
|15205018 | Chiasso-Formation | Chiasso-Formation     |
|15206081 | Chloritschiefer, undifferenziert | Chloritschiefer, undifferenziert     |
|15203015 | Chlussli-Formation | Chlussli-Formation     |
|15200415 | Chnebelburg-Schichten | Chnebelburg-Schichten     |
|15202051 | Choltal-Member | Choltal-Member     |
|15202076 | Chopf-Bank | Chopf-Bank     |
|15202080 | Chriesiloch-Echinodermenkalk | Chriesiloch-Echinodermenkalk     |
|15202040 | Chruteren-Member | Chruteren-Member     |
|15202454 | Chrüzlistock-Migmatit | Chrüzlistock-Migmatit     |
|15203101 | Chumi-Formation | Chumi-Formation     |
|15203542 | Cima-Lunga-D.: Amphibolit | Cima-Lunga-D.: Amphibolit     |
|15203537 | Cima-Lunga-D.: Dolomitmarmor | Cima-Lunga-D.: Dolomitmarmor     |
|15203543 | Cima-Lunga-D.: Eklogit | Cima-Lunga-D.: Eklogit     |
|15203541 | Cima-Lunga-D.: Granatit | Cima-Lunga-D.: Granatit     |
|15203536 | Cima-Lunga-D.: Kalkschiefer und Marmor | Cima-Lunga-D.: Kalkschiefer und Marmor     |
|15203538 | Cima-Lunga-D.: Paragneis | Cima-Lunga-D.: Paragneis     |
|15203544 | Cima-Lunga-D.: Ultramafitit | Cima-Lunga-D.: Ultramafitit     |
|15200017 | Cladocoropsis-Kalk | Cladocoropsis-Kalk     |
|15204140 | Clavadatsch-Brekzie | Clavadatsch-Brekzie     |
|15202262 | Clavaniev-Zone | Clavaniev-Zone     |
|15203192 | Cleuson-Member | Cleuson-Member     |
|15203062 | Clôt-la-Cime-Formation | Clôt-la-Cime-Formation     |
|15204043 | Cluozza-Member | Cluozza-Member     |
|15203294 | Cocco-Gneis | Cocco-Gneis     |
|15203290 | Coicon-Serie | Coicon-Serie     |
|15203186 | Col-de-Chassoure-Formation | Col-de-Chassoure-Formation     |
|15203089 | Col-de-Cordon-Member | Col-de-Cordon-Member     |
|15202397 | Col-de-la-Plaine-Morte-Bank | Col-de-la-Plaine-Morte-Bank     |
|15203042 | Col-de-Lys-Member | Col-de-Lys-Member     |
|15203590 | Col-de-Tompey- und Agreblierai-Member, undifferenziert | Col-de-Tompey- und Agreblierai-Member, undifferenziert     |
|15203585 | Col-de-Tompey- und Bois-de-Luan-Member, undifferenziert | Col-de-Tompey- und Bois-de-Luan-Member, undifferenziert     |
|15203059 | Col-de-Tompey-Formation | Col-de-Tompey-Formation     |
|15202419 | Col-du-Jorat-Member | Col-du-Jorat-Member     |
|15205025 | Coldrerio-Flysch | Coldrerio-Flysch     |
|15203344 | Colerin-Konglomerat | Colerin-Konglomerat     |
|15203036 | Comba-d&#39;Avau-Member | Comba-d&#39;Avau-Member     |
|15203049 | Combe-du-Pissot-Formation | Combe-du-Pissot-Formation     |
|15200304 | Combe-Girard-Bentonit | Combe-Girard-Bentonit     |
|15200625 | Combe-Girard-Member | Combe-Girard-Member     |
|15205015 | Como-Konglomerat | Como-Konglomerat     |
|15200024 | Complexe récifal | Complexe récifal     |
|15200205 | Comptum-Bank | Comptum-Bank     |
|15202354 | Corandoni-Amphibolit | Corandoni-Amphibolit     |
|15200317 | Cornalle-Sandstein | Cornalle-Sandstein     |
|15204141 | Corno-di-Campo-Granodiorit | Corno-di-Campo-Granodiorit     |
|15203403 | Corno-Gneis | Corno-Gneis     |
|15202119 | Coroi-Formation | Coroi-Formation     |
|15203315 | Cortascia-Gneis | Cortascia-Gneis     |
|15204123 | Corvatsch-Granodiorit | Corvatsch-Granodiorit     |
|15203018 | Couches-Rouges-Gruppe | Couches-Rouges-Gruppe     |
|15203366 | Couches-Rouges (Falknis, Sulzfluh, Tasna) | Couches-Rouges (Falknis, Sulzfluh, Tasna)     |
|15203242 | Couches-Rouges der Brekzien-Decke | Couches-Rouges der Brekzien-Decke     |
|15203291 | Couches-Rouges der Klippen-Decke, undifferenziert | Couches-Rouges der Klippen-Decke, undifferenziert     |
|15203563 | Couches-Rouges der ZSK | Couches-Rouges der ZSK     |
|15203016 | Coulaytes-Melange | Coulaytes-Melange     |
|15203587 | Coulaytes-Melange und Cuvigne-Derrey-Formation, undifferenziert | Coulaytes-Melange und Cuvigne-Derrey-Formation, undifferenziert     |
|15200445 | Courcelon-Süsswasserkalk | Courcelon-Süsswasserkalk     |
|15200003 | Courgenay-Formation | Courgenay-Formation     |
|15200019 | Courtedoux-Member | Courtedoux-Member     |
|15200025 | Couvaloup-Member | Couvaloup-Member     |
|15202423 | Covayes-Formation | Covayes-Formation     |
|15204035 | Crappa-Mala-Mergel | Crappa-Mala-Mergel     |
|15200112 | Crenularis-Member | Crenularis-Member     |
|15200626 | Crêt-du-Locle-Formation | Crêt-du-Locle-Formation     |
|15200306 | Crêt-du-Locle-Formation, Gompholitfazies | Crêt-du-Locle-Formation, Gompholitfazies     |
|15200627 | Crêt-du-Locle-Formation, Mergelfazies | Crêt-du-Locle-Formation, Mergelfazies     |
|15200022 | Creugenat-Schichten | Creugenat-Schichten     |
|15203051 | Creux-de-l&#39;Ours-Member | Creux-de-l&#39;Ours-Member     |
|15202227 | Cristallina-Granodiorit | Cristallina-Granodiorit     |
|15200334 | Cuarny-Sandstein | Cuarny-Sandstein     |
|15200355 | Cucloz-Sandstein | Cucloz-Sandstein     |
|15200354 | Cucloz-Subformation | Cucloz-Subformation     |
|15200666 | Cul-du-Nozon-Bank | Cul-du-Nozon-Bank     |
|15205052 | Cunardo-Formation | Cunardo-Formation     |
|15202189 | Curtin-Monzodiorit | Curtin-Monzodiorit     |
|15203017 | Cuvigne-Derrey-Formation | Cuvigne-Derrey-Formation     |
|15200368 | Cyathulabank (Laufen-Becken) | Cyathulabank (Laufen-Becken)     |
|15200369 | Cyrenenmergel | Cyrenenmergel     |
|15202490 | Dachquarzit (Leventina) | Dachquarzit (Leventina)     |
|15202449 | Dammagletscher-Diorit | Dammagletscher-Diorit     |
|15203308 | Danis-Formation | Danis-Formation     |
|15200620 | Dardagny-Sandstein | Dardagny-Sandstein     |
|15200393 | Daubrée-Kalk | Daubrée-Kalk     |
|15200387 | Daubrée-Konglomerat | Daubrée-Konglomerat     |
|15200293 | Degersheim-Kalknagelfluh | Degersheim-Kalknagelfluh     |
|15200344 | Delémont-Süsswasserkalk | Delémont-Süsswasserkalk     |
|15203189 | Dent-de-Nendaz-Member | Dent-de-Nendaz-Member     |
|15200485 | Dentalienton-Formation | Dentalienton-Formation     |
|15200203 | Dewalquei-Kalk | Dewalquei-Kalk     |
|15206099 | Diabasgang, undifferenziert | Diabasgang, undifferenziert     |
|15202019 | Diablerets-Member | Diablerets-Member     |
|15200463 | Diagonalschichtiger Sandstein | Diagonalschichtiger Sandstein     |
|15204033 | Diavel-Formation | Diavel-Formation     |
|15202174 | Diechtergletscher-Formation | Diechtergletscher-Formation     |
|15200447 | Diegten-Süsswasserkalk | Diegten-Süsswasserkalk     |
|15200144 | Dinkelberg-Formation | Dinkelberg-Formation     |
|15206074 | Diorit, undifferenziert | Diorit, undifferenziert     |
|15202089 | Diphyoides-Kalk | Diphyoides-Kalk     |
|15202348 | Distelgrat-Gneis | Distelgrat-Gneis     |
|15203194 | Distulberg-Formation | Distulberg-Formation     |
|15203272 | Dogger der Klippen-Decke | Dogger der Klippen-Decke     |
|15202106 | Dogger des Helvetikums | Dogger des Helvetikums     |
|15200055 | Dogger des Juragebirges | Dogger des Juragebirges     |
|15204087 | Dogger des Ostalpins | Dogger des Ostalpins     |
|15205074 | Dogger des Südalpins | Dogger des Südalpins     |
|15206026 | Dogger, undifferenziert | Dogger, undifferenziert     |
|15205001 | Dolin-Gruppe | Dolin-Gruppe     |
|15205002 | Dolin-Kalkbrekzie | Dolin-Kalkbrekzie     |
|15203061 | Dolomies Blondes | Dolomies Blondes     |
|15205101 | Dolomit-Band (Meride) | Dolomit-Band (Meride)     |
|15205103 | Dolomit der Dolin-Gruppe | Dolomit der Dolin-Gruppe     |
|15202546 | Dolomit der Helvetische Trias | Dolomit der Helvetische Trias     |
|15203568 | Dolomit der Klippen-Decke | Dolomit der Klippen-Decke     |
|15203458 | Dolomit der Nordpenninische Trias | Dolomit der Nordpenninische Trias     |
|15203569 | Dolomit und Kalk der Klippen-Decke | Dolomit und Kalk der Klippen-Decke     |
|15206023 | Dolomit, undifferenziert | Dolomit, undifferenziert     |
|15203250 | Dolomitbrekzie (Terri) | Dolomitbrekzie (Terri)     |
|15206102 | Dolomitmarmor, undifferenziert | Dolomitmarmor, undifferenziert     |
|15200216 | Dolomitzone | Dolomitzone     |
|15202518 | Domérien-Sandstein | Domérien-Sandstein     |
|15203099 | Dorchaux-Member | Dorchaux-Member     |
|15202359 | Dorénaz-Konglomerat | Dorénaz-Konglomerat     |
|15204105 | Dorfberg-Gneis | Dorfberg-Gneis     |
|15203082 | Dorfflüe-Formation | Dorfflüe-Formation     |
|15204109 | Döss-Radond-Vulkanite | Döss-Radond-Vulkanite     |
|15200411 | Dreilinden-Nagelfluh | Dreilinden-Nagelfluh     |
|15203346 | Dréveneuse-Bauxit | Dréveneuse-Bauxit     |
|15202077 | Drusberg-Member | Drusberg-Member     |
|15204063 | Ducan-Formation | Ducan-Formation     |
|15202118 | Dugny-Formation | Dugny-Formation     |
|15202045 | Dünden-Konglomerat | Dünden-Konglomerat     |
|15200213 | Dünnlenberg-Bank | Dünnlenberg-Bank     |
|15202059 | Durschlägi-Bank | Durschlägi-Bank     |
|15202179 | Düssi-Diorit | Düssi-Diorit     |
|15202325 | Dzéman-Member | Dzéman-Member     |
|15200540 | Ebnat-Sandstein | Ebnat-Sandstein     |
|15200115 | Effingen-Member | Effingen-Member     |
|15203165 | Eggberg-Formation | Eggberg-Formation     |
|15200519 | Eggen-Member | Eggen-Member     |
|15200502 | Eichbol-Tuffit | Eichbol-Tuffit     |
|15203152 | Eichholztobel-Formation | Eichholztobel-Formation     |
|15200260 | Eimätteli-Member | Eimätteli-Member     |
|15202038 | Einsiedeln-Member | Einsiedeln-Member     |
|15202589 | Einsiedeln-Member, «Älterer Quarzsandstein» | Einsiedeln-Member, «Älterer Quarzsandstein»     |
|15202592 | Einsiedeln-Member, Alveolinenkalk-Fazies | Einsiedeln-Member, Alveolinenkalk-Fazies     |
|15204066 | Eisendolomit-Member | Eisendolomit-Member     |
|15206050 | Eklogit, undifferenziert | Eklogit, undifferenziert     |
|15202540 | Elm- und Matt-Formation, undifferenziert | Elm- und Matt-Formation, undifferenziert     |
|15202541 | Elm- und Matt-Formation: Quarzsandstein | Elm- und Matt-Formation: Quarzsandstein     |
|15202009 | Elm-Formation | Elm-Formation     |
|15200379 | Elsässer-Molasse s.l. | Elsässer-Molasse s.l.     |
|15200343 | Elsässer Molasse s.s. | Elsässer Molasse s.s.     |
|15203310 | Embd-Member | Embd-Member     |
|15204004 | Emmat-Formation | Emmat-Formation     |
|15202210 | Emosson-Glimmerschiefer | Emosson-Glimmerschiefer     |
|15202007 | Engi-Dachschiefer | Engi-Dachschiefer     |
|15202263 | Engi-Granit | Engi-Granit     |
|15200524 | Ennetbühl-Member | Ennetbühl-Member     |
|15200212 | Eptingen-Member | Eptingen-Member     |
|15203199 | Ergischhorn-Komplex | Ergischhorn-Komplex     |
|15200210 | Ergolz-Member | Ergolz-Member     |
|15200072 | Eriwis-Bank | Eriwis-Bank     |
|15200073 | Erlimoos-Bank | Erlimoos-Bank     |
|15203094 | Erpilles-Member | Erpilles-Member     |
|15204015 | Err-Brekzie | Err-Brekzie     |
|15204102 | Err-Granodiorit | Err-Granodiorit     |
|15202197 | Erstfeld-Gneiskomplex | Erstfeld-Gneiskomplex     |
|15202532 | Erstfeld-Gneiskomplex, permisch verwittert | Erstfeld-Gneiskomplex, permisch verwittert     |
|15202551 | Erstfeld-Gneiskomplex: Biotit-Plagioklasgneis | Erstfeld-Gneiskomplex: Biotit-Plagioklasgneis     |
|15202553 | Erstfeld-Gneiskomplex: Migmatit | Erstfeld-Gneiskomplex: Migmatit     |
|15202552 | Erstfeld-Gneiskomplex: Orthogneis | Erstfeld-Gneiskomplex: Orthogneis     |
|15202107 | Erzegg-Formation | Erzegg-Formation     |
|15200446 | Erzmatt-Krustenkalk | Erzmatt-Krustenkalk     |
|15203124 | Estavannens-Flysch | Estavannens-Flysch     |
|15200468 | Estherien-Schichten | Estherien-Schichten     |
|15202171 | Estuarisches Member | Estuarisches Member     |
|15200023 | Etiollets-Formation | Etiollets-Formation     |
|15200643 | Etzgen-Granit | Etzgen-Granit     |
|15202036 | Euthal-Formation | Euthal-Formation     |
|15202596 | Euthal-Formation und Steinbach-Member, undiff. | Euthal-Formation und Steinbach-Member, undiff.     |
|15202604 | Euthal-Formation: schwarzer schiefriger Tonstein | Euthal-Formation: schwarzer schiefriger Tonstein     |
|15203260 | Exergillod-Brekzie | Exergillod-Brekzie     |
|15203167 | Fadura-Formation | Fadura-Formation     |
|15200279 | Falätschen-Mergel | Falätschen-Mergel     |
|15203326 | Fäldbach-Gruppe | Fäldbach-Gruppe     |
|15203216 | Falknis-Brekzie | Falknis-Brekzie     |
|15203210 | Falknis-Flysch | Falknis-Flysch     |
|15203499 | Falotta-Radiolarit | Falotta-Radiolarit     |
|15202278 | Fanee-Trias | Fanee-Trias     |
|15204041 | Fanez-Dolomit | Fanez-Dolomit     |
|15204039 | Fanez-Formation | Fanez-Formation     |
|15203144 | Fanola-Formation | Fanola-Formation     |
|15200084 | Fasiswald-Member | Fasiswald-Member     |
|15204096 | Fedoz-Gneiskomplex | Fedoz-Gneiskomplex     |
|15204097 | Fedoz-Metagabbro | Fedoz-Metagabbro     |
|15200275 | Fellitobel-Süsswasserkalk | Fellitobel-Süsswasserkalk     |
|15203372 | Ferret-Schiefer | Ferret-Schiefer     |
|15200196 | Ferrugineus-Oolith | Ferrugineus-Oolith     |
|15203228 | Fêta-d&#39;Août-Flysch | Fêta-d&#39;Août-Flysch     |
|15202230 | Fibbia-Granit | Fibbia-Granit     |
|15203138 | Filamentkalk | Filamentkalk     |
|15205133 | Finero-Peridotit | Finero-Peridotit     |
|15200364 | Fischschiefer | Fischschiefer     |
|15203214 | Fleckenkalk-Flysch (Neokom) | Fleckenkalk-Flysch (Neokom)     |
|15202041 | Fliegenspitz-Member | Fliegenspitz-Member     |
|15203497 | Flix-Schichten | Flix-Schichten     |
|15204104 | Flüela-Augnengneis | Flüela-Augnengneis     |
|15200556 | Flühli-Nagelfluh | Flühli-Nagelfluh     |
|15203115 | Flysch 2a tonig-sandig | Flysch 2a tonig-sandig     |
|15203114 | Flysch 2b mit sandigen Turbiditen | Flysch 2b mit sandigen Turbiditen     |
|15203113 | Flysch 3a mergelig-sandig | Flysch 3a mergelig-sandig     |
|15203112 | Flysch 3b mit bioklastischen Turbiditen | Flysch 3b mit bioklastischen Turbiditen     |
|15203111 | Flysch 4 mit siltigen Turbiditen | Flysch 4 mit siltigen Turbiditen     |
|15203284 | Flysch 5, mit kieseligen Mikrokonglomeraten | Flysch 5, mit kieseligen Mikrokonglomeraten     |
|15206115 | Flysch, undifferenziert | Flysch, undifferenziert     |
|15202323 | Foostock-Member | Foostock-Member     |
|15200365 | Foraminiferenmergel | Foraminiferenmergel     |
|15203135 | Foraminiferenschichten | Foraminiferenschichten     |
|15203008 | Forclaz-Member | Forclaz-Member     |
|15203022 | Forclettes-Formation | Forclettes-Formation     |
|15203316 | Forcoletta-Gneis | Forcoletta-Gneis     |
|15202033 | Foribach-Member | Foribach-Member     |
|15200330 | Formation der Granitischen Molasse | Formation der Granitischen Molasse     |
|15205095 | Fornale-Gabbro | Fornale-Gabbro     |
|15203342 | Forno-Amphibolit | Forno-Amphibolit     |
|15200651 | Fort-de-l&#39;Ecluse-Member | Fort-de-l&#39;Ecluse-Member     |
|15204117 | Forun-Augengneis | Forun-Augengneis     |
|15202277 | Fossilmarmor | Fossilmarmor     |
|15203134 | Fouyet-Formation | Fouyet-Formation     |
|15202031 | Fräkmünt-Member | Fräkmünt-Member     |
|15202069 | Freschen-Member | Freschen-Member     |
|15200409 | Freudenberg-Nagelfluh | Freudenberg-Nagelfluh     |
|15200082 | Frick-Member | Frick-Member     |
|15200230 | Frühvariszische Intrusiva der Nordschweiz | Frühvariszische Intrusiva der Nordschweiz     |
|15202333 | Frühvariszische Intrusiva des Aiguilles-Rouges-Massivs | Frühvariszische Intrusiva des Aiguilles-Rouges-Massivs     |
|15203005 | Frutigen-Formation | Frutigen-Formation     |
|15203524 | Frutigen-Formation, Conglomérat intermédiaire | Frutigen-Formation, Conglomérat intermédiaire     |
|15203525 | Frutigen-Formation, Schistes inférieurs | Frutigen-Formation, Schistes inférieurs     |
|15202029 | Fruttli-Member | Fruttli-Member     |
|15202177 | Fruttstock-Gruppe | Fruttstock-Gruppe     |
|15206063 | Fuchsit-Zoisitschiefer, undifferenziert | Fuchsit-Zoisitschiefer, undifferenziert     |
|15202150 | Fuggstock-Member | Fuggstock-Member     |
|15202494 | Fulen-Formation | Fulen-Formation     |
|15200182 | Fulie-Member | Fulie-Member     |
|15202482 | Fully-Gneiskomplex | Fully-Gneiskomplex     |
|15202202 | Fully-Granodiorit | Fully-Granodiorit     |
|15202350 | Fuorcla-Paradis-Serpentinit | Fuorcla-Paradis-Serpentinit     |
|15204070 | Fuorn-Formation | Fuorn-Formation     |
|15200198 | Furcil-Mergel | Furcil-Mergel     |
|15203438 | Furgg-Serie | Furgg-Serie     |
|15200215 | Fützen-Bank | Fützen-Bank     |
|15206075 | Gabbro, undifferenziert | Gabbro, undifferenziert     |
|15200496 | Gabelspitz-Schichten | Gabelspitz-Schichten     |
|15200515 | Gäbris-Nagelfluh | Gäbris-Nagelfluh     |
|15200087 | Gächlingen-Bank | Gächlingen-Bank     |
|15202127 | Galm-Member | Galm-Member     |
|15203393 | Gälmji-Gneiss | Gälmji-Gneiss     |
|15202067 | Gams-Schichten | Gams-Schichten     |
|15202228 | Gamsboden-Granit | Gamsboden-Granit     |
|15206024 | Ganggesteine, undifferenziert | Ganggesteine, undifferenziert     |
|15203514 | Ganna-Gneis | Ganna-Gneis     |
|15202353 | Ganneretsch-Gneis | Ganneretsch-Gneis     |
|15200209 | Gansingen-Member | Gansingen-Member     |
|15203321 | Ganter-Gneis | Ganter-Gneis     |
|15206073 | Garbenschiefer, undifferenziert | Garbenschiefer, undifferenziert     |
|15203227 | Garde-de-Bordon-Serie | Garde-de-Bordon-Serie     |
|15203254 | Garenstock-Augengneis | Garenstock-Augengneis     |
|15204048 | Garone-Formation | Garone-Formation     |
|15202052 | Garschella-Formation | Garschella-Formation     |
|15202329 | Gärsthorn-Gneiskomplex | Gärsthorn-Gneiskomplex     |
|15202529 | Garwiidi-Diorit | Garwiidi-Diorit     |
|15203377 | Garzott-Brekzie | Garzott-Brekzie     |
|15203154 | Gaschlo-Formation | Gaschlo-Formation     |
|15202095 | Gassen-Kalk | Gassen-Kalk     |
|15202158 | Gastern-Granit | Gastern-Granit     |
|15203086 | Gastlosen-Oolith | Gastlosen-Oolith     |
|15202476 | Geimen-Augengneis | Geimen-Augengneis     |
|15202305 | Geissbach-Konglomerat | Geissbach-Konglomerat     |
|15200113 | Geissberg-Member | Geissberg-Member     |
|15203323 | Geisspfad-Serpentinit | Geisspfad-Serpentinit     |
|15203200 | Gelbhorn-Flysch | Gelbhorn-Flysch     |
|15202021 | Gemmenalp-Kalk | Gemmenalp-Kalk     |
|15202082 | Gemsmättli-Bank | Gemsmättli-Bank     |
|15200537 | Gérignoz-Formation | Gérignoz-Formation     |
|15203032 | Gérignoz-Kalk | Gérignoz-Kalk     |
|15200389 | Geröllsande | Geröllsande     |
|15200683 | Gersbach-Schiefer | Gersbach-Schiefer     |
|15200116 | Gerstenhübel-Bank | Gerstenhübel-Bank     |
|15203245 | Gets-Ophiolith | Gets-Ophiolith     |
|15202293 | Ghölzwald-Member | Ghölzwald-Member     |
|15203567 | Gibel- und Griggeli-Formation | Gibel- und Griggeli-Formation     |
|15203069 | Gibel-Formation | Gibel-Formation     |
|15203071 | Gibel-Member | Gibel-Member     |
|15203399 | Ginals-Gneis | Ginals-Gneis     |
|15200074 | Gipf-Bank | Gipf-Bank     |
|15202548 | Gips der Helvetische Trias | Gips der Helvetische Trias     |
|15203241 | Gips der Klippen-Decke | Gips der Klippen-Decke     |
|15204145 | Gips der Raibl-Gruppe | Gips der Raibl-Gruppe     |
|15203526 | Gips der Zone Submédiane | Gips der Zone Submédiane     |
|15206021 | Gips, undifferenziert | Gips, undifferenziert     |
|15203572 | Gipsmergel und Sandstein der Klippen-Decke | Gipsmergel und Sandstein der Klippen-Decke     |
|15200200 | Gisliflue-Korallenkalk | Gisliflue-Korallenkalk     |
|15200628 | Gitzigrabe-Grobsandstein | Gitzigrabe-Grobsandstein     |
|15200528 | Gitzischöpf-Nagelfluh | Gitzischöpf-Nagelfluh     |
|15200632 | Gitzitobel-Süsswasserkalk | Gitzitobel-Süsswasserkalk     |
|15202339 | Giubine-Gneiskomplex | Giubine-Gneiskomplex     |
|15205083 | Giumello-Gneis | Giumello-Gneis     |
|15202188 | Giuv-Syenit | Giuv-Syenit     |
|15203421 | Glanzschiefer der Zermatt-Saas-Decke | Glanzschiefer der Zermatt-Saas-Decke     |
|15202144 | Glarus-Verrucano | Glarus-Verrucano     |
|15200180 | Glassand | Glassand     |
|15202495 | Glattmatt-Member | Glattmatt-Member     |
|15200480 | Glaukonitsandmergel-Subformation | Glaukonitsandmergel-Subformation     |
|15206065 | Glaukophanschiefer, undifferenziert | Glaukophanschiefer, undifferenziert     |
|15200274 | Glimmersandstein-Formation | Glimmersandstein-Formation     |
|15205118 | Glimmerschiefer der Arolla-Gruppe | Glimmerschiefer der Arolla-Gruppe     |
|15203446 | Glimmerschiefer der Monte-Rosa-Decke | Glimmerschiefer der Monte-Rosa-Decke     |
|15205132 | Glimmerschiefer der Sesia-Decke | Glimmerschiefer der Sesia-Decke     |
|15206072 | Glimmerschiefer, undifferenziert | Glimmerschiefer, undifferenziert     |
|15203211 | Globorotalien-Schichten | Globorotalien-Schichten     |
|15202416 | Glockhaus-Member | Glockhaus-Member     |
|15202545 | Glockhaus-Member: Schiefriger Eisensandstein | Glockhaus-Member: Schiefriger Eisensandstein     |
|15205110 | Gneis der Arolla-Gruppe, mikroaugig | Gneis der Arolla-Gruppe, mikroaugig     |
|15205109 | Gneis der Arolla-Gruppe, mylonitisch | Gneis der Arolla-Gruppe, mylonitisch     |
|15206070 | Gneis, undifferenziert | Gneis, undifferenziert     |
|15203247 | Gneisquarzit der Zone Piz Terri - Lunschania | Gneisquarzit der Zone Piz Terri - Lunschania     |
|15203364 | Gneiss basale (Lebendun) | Gneiss basale (Lebendun)     |
|15204001 | God-Drosa-Flysch | God-Drosa-Flysch     |
|15200511 | Golat-Süsswasserkalk | Golat-Süsswasserkalk     |
|15200661 | Goldberg- bis Vuache-Formation, undifferenziert | Goldberg- bis Vuache-Formation, undifferenziert     |
|15200156 | Goldberg-Formation | Goldberg-Formation     |
|15200410 | Goldbrunnen-Schichten | Goldbrunnen-Schichten     |
|15200361 | Goldegg-Sandstein | Goldegg-Sandstein     |
|15203190 | Goli-d&#39;Aget-Member | Goli-d&#39;Aget-Member     |
|15202256 | Goltschenried-Formation | Goltschenried-Formation     |
|15202267 | Goms-Gneiskomplex | Goms-Gneiskomplex     |
|15202510 | Gonzen-Eisenerzhorizont | Gonzen-Eisenerzhorizont     |
|15200092 | Gorges-de-l&#39;Orbe- und Vallorbe-Formation, undifferenziert | Gorges-de-l&#39;Orbe- und Vallorbe-Formation, undifferenziert     |
|15200096 | Gorges-de-l&#39;Orbe-Formation | Gorges-de-l&#39;Orbe-Formation     |
|15204115 | Gosau-Gruppe | Gosau-Gruppe     |
|15200488 | Gosheim-Formation | Gosheim-Formation     |
|15203187 | Gouille-Verte-Member | Gouille-Verte-Member     |
|15200547 | Goumoëns-Sandstein | Goumoëns-Sandstein     |
|15204067 | Gracilis-Member | Gracilis-Member     |
|15200043 | Graitery-Member | Graitery-Member     |
|15206098 | Granatamphibolit, undifferenziert | Granatamphibolit, undifferenziert     |
|15206068 | Granatglimmerschiefer, undifferenziert | Granatglimmerschiefer, undifferenziert     |
|15205098 | Grand-Dolin-Brekzie | Grand-Dolin-Brekzie     |
|15200660 | Grand-Essert- bis Narlay-Formation, undifferenziert | Grand-Essert- bis Narlay-Formation, undifferenziert     |
|15200150 | Grand-Essert-Formation | Grand-Essert-Formation     |
|15203267 | Grand-Herba-Kalk | Grand-Herba-Kalk     |
|15203054 | Grande-Bonavau-Formation | Grande-Bonavau-Formation     |
|15203589 | Grande-Bonavau-Formation und Formation spathique, undifferenziert | Grande-Bonavau-Formation und Formation spathique, undifferenziert     |
|15203006 | Grande-Eau-Formation | Grande-Eau-Formation     |
|15200670 | Grande-Varappe-Bank | Grande-Varappe-Bank     |
|15206032 | Granit, undifferenziert | Granit, undifferenziert     |
|15202246 | Granitartige Gesteine | Granitartige Gesteine     |
|15202260 | Granitischer Gneis der Ausserberg-Avat-Zone | Granitischer Gneis der Ausserberg-Avat-Zone     |
|15205066 | Granophyr | Granophyr     |
|15206071 | Graphitschiefer, undifferenziert | Graphitschiefer, undifferenziert     |
|15202094 | Graspass-Member | Graspass-Member     |
|15200392 | Graue Molasse | Graue Molasse     |
|15200564 | Graupensand | Graupensand     |
|15200037 | Grellingen-Member | Grellingen-Member     |
|15200063 | Grenchenberg-Member | Grenchenberg-Member     |
|15200467 | Grenzdolomit | Grenzdolomit     |
|15200481 | Grenzkalk | Grenzkalk     |
|15200016 | Grenznerineen-Bank | Grenznerineen-Bank     |
|15205037 | Grenzposidonienschichten | Grenzposidonienschichten     |
|15202525 | Grenzquarzit der Bommerstein-Formation | Grenzquarzit der Bommerstein-Formation     |
|15202473 | Grépillon-Leukogranitporphyr | Grépillon-Leukogranitporphyr     |
|15203009 | Grès de Passage | Grès de Passage     |
|15200336 | Grès et Marnes Gris à Gypse | Grès et Marnes Gris à Gypse     |
|15203480 | Gresso-Someo-Zone | Gresso-Someo-Zone     |
|15202138 | Griaz-Member | Griaz-Member     |
|15203068 | Griggeli-Bank | Griggeli-Bank     |
|15203066 | Griggeli-Formation | Griggeli-Formation     |
|15200422 | Grilly-Süsswasserkalk | Grilly-Süsswasserkalk     |
|15200414 | Grimmelfingen-Formation | Grimmelfingen-Formation     |
|15202161 | Grimsel-Granodiorit | Grimsel-Granodiorit     |
|15202568 | Grimsel-Granodiorit: aplitische Randfazies | Grimsel-Granodiorit: aplitische Randfazies     |
|15200550 | Grindelegg-Formation | Grindelegg-Formation     |
|15202043 | Grindelwald-Marmor | Grindelwald-Marmor     |
|15202322 | Grisch-Member | Grisch-Member     |
|15200352 | Grisigen-Mergel | Grisigen-Mergel     |
|15202317 | Gros-Plané-Melange | Gros-Plané-Melange     |
|15200071 | Gross-Wolf-Member | Gross-Wolf-Member     |
|15202380 | Grotzen-Austernbank | Grotzen-Austernbank     |
|15203511 | Gruf-Migmatit | Gruf-Migmatit     |
|15200207 | Gruhalde-Member | Gruhalde-Member     |
|15203447 | Grundberg-Serie | Grundberg-Serie     |
|15200194 | Grüne Mumienbank | Grüne Mumienbank     |
|15206036 | Grüngestein, undifferenziert | Grüngestein, undifferenziert     |
|15203467 | Grüngesteine der Distulberg-Formation | Grüngesteine der Distulberg-Formation     |
|15203179 | Grüngesteine der Grava- und Tomül-Decke | Grüngesteine der Grava- und Tomül-Decke     |
|15202173 | Grünhorn-Member («Vulkanisches Member») | Grünhorn-Member («Vulkanisches Member»)     |
|15200081 | Grünschholz-Member | Grünschholz-Member     |
|15202071 | Grünten-Member | Grünten-Member     |
|15202008 | Gruontal-Konglomerat | Gruontal-Konglomerat     |
|15205028 | Gruppe der Scaglia Lombarda | Gruppe der Scaglia Lombarda     |
|15205023 | Gruppe des Lombardischen Flysch | Gruppe des Lombardischen Flysch     |
|15205010 | Gruppe des Lombardischen Gompholit | Gruppe des Lombardischen Gompholit     |
|15202442 | Gryonne-Formation | Gryonne-Formation     |
|15200516 | Gstaldenbach-Member | Gstaldenbach-Member     |
|15203121 | Guber-Sandstein | Guber-Sandstein     |
|15203131 | Gueyraz-Komplex | Gueyraz-Komplex     |
|15202501 | Gufelialp-Member | Gufelialp-Member     |
|15200657 | Gugenmühle-Member | Gugenmühle-Member     |
|15200298 | Guggershorn-Formation | Guggershorn-Formation     |
|15200099 | Guiers-Member | Guiers-Member     |
|15200425 | Gümmenen-Formation | Gümmenen-Formation     |
|15203083 | Gummfluh-Mikrofazies | Gummfluh-Mikrofazies     |
|15200573 | Günsberg- und Vellerat-Formation, undifferenziert | Günsberg- und Vellerat-Formation, undifferenziert     |
|15200160 | Günsberg-, Vellerat-, Villigen-, Balsthal- und Courgenay-Formation, undifferenziert | Günsberg-, Vellerat-, Villigen-, Balsthal- und Courgenay-Formation, undifferenziert     |
|15200118 | Günsberg-Formation | Günsberg-Formation     |
|15200321 | Gunten-Quarzitnagelfluh | Gunten-Quarzitnagelfluh     |
|15202111 | Guppen-Fossilhorizont | Guppen-Fossilhorizont     |
|15203110 | Gurnigel-Flysch | Gurnigel-Flysch     |
|15202112 | Gursbach-Fossilhorizont | Gursbach-Fossilhorizont     |
|15202242 | Gurschen-Gneis | Gurschen-Gneis     |
|15202509 | Guschakopf-Sandstein | Guschakopf-Sandstein     |
|15202243 | Guspis-Gneis | Guspis-Gneis     |
|15204084 | Güstizia-Gneis | Güstizia-Gneis     |
|15204068 | Gutenstein-Formation | Gutenstein-Formation     |
|15202198 | Guttannen-Gneiskomplex | Guttannen-Gneiskomplex     |
|15202575 | Guttannen-Gneiskomplex: Amphibolit führend | Guttannen-Gneiskomplex: Amphibolit führend     |
|15202576 | Guttannen-Gneiskomplex: aplitischer Granit | Guttannen-Gneiskomplex: aplitischer Granit     |
|15202556 | Guttannen-Gneiskomplex: Biotit-Choritschiefer | Guttannen-Gneiskomplex: Biotit-Choritschiefer     |
|15202557 | Guttannen-Gneiskomplex: Chlorit-Serizitschiefer | Guttannen-Gneiskomplex: Chlorit-Serizitschiefer     |
|15202577 | Guttannen-Gneiskomplex: Marmor | Guttannen-Gneiskomplex: Marmor     |
|15202574 | Guttannen-Gneiskomplex: Migmatit | Guttannen-Gneiskomplex: Migmatit     |
|15202555 | Guttannen-Gneiskomplex: Orthogneis | Guttannen-Gneiskomplex: Orthogneis     |
|15202554 | Guttannen-Gneiskomplex: Paragneis | Guttannen-Gneiskomplex: Paragneis     |
|15202585 | Guttannen-Gneiskomplex: schierfriger Biotit-Chlorit-Serizit-Gneis | Guttannen-Gneiskomplex: schierfriger Biotit-Chlorit-Serizit-Gneis     |
|15202578 | Guttannen-Gneiskomplex: Ultramafit | Guttannen-Gneiskomplex: Ultramafit     |
|15202313 | Gwürz-Flysch | Gwürz-Flysch     |
|15203166 | Gyrenspitz-Formation | Gyrenspitz-Formation     |
|15202316 | Habkern-Granit | Habkern-Granit     |
|15202001 | Habkern-Melange | Habkern-Melange     |
|15202496 | Hahnenstock-Keratophyr | Hahnenstock-Keratophyr     |
|15200566 | Haldenhof-Mergel | Haldenhof-Mergel     |
|15200090 | Hallau-Bank | Hallau-Bank     |
|15200486 | Hamitenton-Formation | Hamitenton-Formation     |
|15200469 | Hangende-Bankkalke-Formation | Hangende-Bankkalke-Formation     |
|15202157 | Haslital-Gruppe | Haslital-Gruppe     |
|15200241 | Hauenstein-Granit | Hauenstein-Granit     |
|15200069 | Hauenstein-Member | Hauenstein-Member     |
|15205050 | Hauptdolomit | Hauptdolomit     |
|15204150 | Hauptdolomit-Gr.: bituminöse Dolomitbrekzie | Hauptdolomit-Gr.: bituminöse Dolomitbrekzie     |
|15204030 | Hauptdolomit-Gruppe | Hauptdolomit-Gruppe     |
|15204127 | Haupter-Brekzie | Haupter-Brekzie     |
|15200030 | Hauptmumienbank-Member | Hauptmumienbank-Member     |
|15200008 | Hauptrogenstein | Hauptrogenstein     |
|15203263 | Hauta-Crêtaz-Formation | Hauta-Crêtaz-Formation     |
|15203382 | Haute-Pointe-Formation | Haute-Pointe-Formation     |
|15200152 | Hauterive-Mergel | Hauterive-Mergel     |
|15200458 | Hautes-Roches-Algenkalk | Hautes-Roches-Algenkalk     |
|15200264 | Hegau-Basalt | Hegau-Basalt     |
|15200266 | Hegau-Deckentuffe | Hegau-Deckentuffe     |
|15200265 | Hegau-Phonolith | Hegau-Phonolith     |
|15200263 | Hegau-Vulkanite | Hegau-Vulkanite     |
|15200517 | Heiden-Member | Heiden-Member     |
|15203586 | Heiti- und Rossinière-Formation, undifferenziert | Heiti- und Rossinière-Formation, undifferenziert     |
|15203048 | Heiti-Formation | Heiti-Formation     |
|15200565 | Heliciden-Mergel | Heliciden-Mergel     |
|15203116 | Hellstätt-Formation | Hellstätt-Formation     |
|15202079 | Helvetischer Kieselkalk | Helvetischer Kieselkalk     |
|15202515 | Helvetischer Kieselkalk, Basisschiefer | Helvetischer Kieselkalk, Basisschiefer     |
|15202513 | Helvetischer Kieselkalk, Oberer Teil | Helvetischer Kieselkalk, Oberer Teil     |
|15202514 | Helvetischer Kieselkalk, Unterer Teil | Helvetischer Kieselkalk, Unterer Teil     |
|15200684 | Herdern-Streifengneis | Herdern-Streifengneis     |
|15200044 | Herznach-Member | Herznach-Member     |
|15200339 | Heuboden-Äschitannen-Nagelfluh | Heuboden-Äschitannen-Nagelfluh     |
|15204022 | Hierlatz-Kalk | Hierlatz-Kalk     |
|15200358 | Hilfern-Formation | Hilfern-Formation     |
|15202483 | Hinterbalm-Granit | Hinterbalm-Granit     |
|15200068 | Hirnichopf-Member | Hirnichopf-Member     |
|15200525 | Hochalp-Member | Hochalp-Member     |
|15200268 | Höchegg-Brekzie | Höchegg-Brekzie     |
|15200523 | Hochfläschli-Member | Hochfläschli-Member     |
|15202070 | Hochkugel-Schichten | Hochkugel-Schichten     |
|15203020 | Hochmatt-Kalkarenit | Hochmatt-Kalkarenit     |
|15202363 | Höchst-Flysch | Höchst-Flysch     |
|15202113 | Hochstollen-Formation | Hochstollen-Formation     |
|15200501 | Hohenolber-Tuffit | Hohenolber-Tuffit     |
|15200655 | Hohentengen-Formation | Hohentengen-Formation     |
|15202022 | Hohgant-Sandstein | Hohgant-Sandstein     |
|15202593 | Hohgant-Sandstein, Sandkalk und Kalk | Hohgant-Sandstein, Sandkalk und Kalk     |
|15200315 | Höhronen-Nagelfluh | Höhronen-Nagelfluh     |
|15203091 | Holzerhorn-Einheit | Holzerhorn-Einheit     |
|15203324 | Holzerspitz-Gruppe | Holzerspitz-Gruppe     |
|15203325 | Holzerspitz-Kalkschiefer | Holzerspitz-Kalkschiefer     |
|15200190 | Holzflue-Member | Holzflue-Member     |
|15200513 | Hombach-Member | Hombach-Member     |
|15200514 | Homberg-Formation | Homberg-Formation     |
|15200178 | Homomya-Mergel | Homomya-Mergel     |
|15200529 | Honegg-Mergel | Honegg-Mergel     |
|15200299 | Horgen-Käpfnach-Süsswasserkalk | Horgen-Käpfnach-Süsswasserkalk     |
|15205115 | Hornblendegabbro der Arolla-Decke | Hornblendegabbro der Arolla-Decke     |
|15206091 | Hornblendegneis, undifferenziert | Hornblendegneis, undifferenziert     |
|15200111 | Hornbuck-Member | Hornbuck-Member     |
|15200646 | Hornbüel-Melange | Hornbüel-Melange     |
|15206090 | Hornfels, undifferenziert | Hornfels, undifferenziert     |
|15203080 | Horngraben-Formation | Horngraben-Formation     |
|15200297 | Hörnli-Formation | Hörnli-Formation     |
|15200267 | Hörnligipfel-Nagelfluh | Hörnligipfel-Nagelfluh     |
|15200269 | Hörnligubel-Mergel | Hörnligubel-Mergel     |
|15200350 | Horw-Sandstein | Horw-Sandstein     |
|15200292 | Hüllistein-Konglomerat | Hüllistein-Konglomerat     |
|15200066 | Humphriesi-Schichten | Humphriesi-Schichten     |
|15200490 | Humphriesioolith-Subformation | Humphriesioolith-Subformation     |
|15203140 | Hundsrügg-Formation | Hundsrügg-Formation     |
|15200531 | Hünibach-Nagelfluh | Hünibach-Nagelfluh     |
|15200177 | Hupper | Hupper     |
|15202381 | Hurst-Mergel | Hurst-Mergel     |
|15203428 | Hyperaugengneis der Monte-Leone-Decke | Hyperaugengneis der Monte-Leone-Decke     |
|15202308 | Iberg-Melange | Iberg-Melange     |
|15200007 | Ifenthal-Formation | Ifenthal-Formation     |
|15202508 | Ignimbritisches Member (Tscharren) | Ignimbritisches Member (Tscharren)     |
|15202153 | Ilanz-Verrucano | Ilanz-Verrucano     |
|15202502 | Ilanz-Verrucano s.s. | Ilanz-Verrucano s.s.     |
|15200478 | Impressamergel-Formation | Impressamergel-Formation     |
|15202122 | Inferno-Formation | Inferno-Formation     |
|15202402 | Inferno-Formation, Mittlerer Teil | Inferno-Formation, Mittlerer Teil     |
|15202401 | Inferno-Formation, Oberer Teil | Inferno-Formation, Oberer Teil     |
|15202403 | Inferno-Formation, Unterer Teil | Inferno-Formation, Unterer Teil     |
|15206016 | Informelle Zuordnung | Informelle Zuordnung     |
|15203282 | Infrabrèche-Melange | Infrabrèche-Melange     |
|15202307 | Infrapräalpines Melange | Infrapräalpines Melange     |
|15202195 | Innertkirchen-Migmatit | Innertkirchen-Migmatit     |
|15202531 | Innertkirchen-Migmatit, permisch verwittert | Innertkirchen-Migmatit, permisch verwittert     |
|15202573 | Innertkirchen-Migmatit: Marmor | Innertkirchen-Migmatit: Marmor     |
|15202168 | Intschi-Formation | Intschi-Formation     |
|15203034 | Intyamon-Formation | Intyamon-Formation     |
|15202311 | Isentobel-Komplex | Isentobel-Komplex     |
|15202521 | Iserin-Flysch | Iserin-Flysch     |
|15205134 | Ivrea Mafischer Komplex | Ivrea Mafischer Komplex     |
|15202424 | Javrex-Formation | Javrex-Formation     |
|15200399 | Jensberg-Schichten | Jensberg-Schichten     |
|15203215 | Jes-Formation | Jes-Formation     |
|15202015 | Jochstock-Konglomerat | Jochstock-Konglomerat     |
|15202432 | Jogne-Formation | Jogne-Formation     |
|15200360 | Jordisboden-Mergel | Jordisboden-Mergel     |
|15206010 | Jorio-Tonalit | Jorio-Tonalit     |
|15202438 | Joux-Galez-Member | Joux-Galez-Member     |
|15203102 | Joux-Verte-Formation | Joux-Verte-Formation     |
|15204124 | Julier-Granodiorit | Julier-Granodiorit     |
|15200226 | Jüngere Flussablagerungen | Jüngere Flussablagerungen     |
|15200302 | Jura-Nagelfluh | Jura-Nagelfluh     |
|15202298 | Jura des Helvetikums | Jura des Helvetikums     |
|15200162 | Jura des Juragebirges | Jura des Juragebirges     |
|15200575 | Jurensismergel-Formation | Jurensismergel-Formation     |
|15200139 | Kaiseraugst-Formation | Kaiseraugst-Formation     |
|15200211 | Kaisten-Bank | Kaisten-Bank     |
|15200408 | Kalchstätten-Formation | Kalchstätten-Formation     |
|15205102 | Kalk der Dolin-Gruppe | Kalk der Dolin-Gruppe     |
|15204134 | kalkalkalische Intrusiva des Ostalpins | kalkalkalische Intrusiva des Ostalpins     |
|15203207 | Kalkberg-Gruppe | Kalkberg-Gruppe     |
|15202451 | Kalkiger Mines-Lias | Kalkiger Mines-Lias     |
|15203581 | Kalkiger Tonschiefer der Grava-Decke | Kalkiger Tonschiefer der Grava-Decke     |
|15206101 | Kalkmarmor, undifferenziert | Kalkmarmor, undifferenziert     |
|15200536 | Kalksandstein-Serie | Kalksandstein-Serie     |
|15203455 | Kalkschiefer der Fäldbach-Serie | Kalkschiefer der Fäldbach-Serie     |
|15206104 | Kalkschiefer, undifferenziert | Kalkschiefer, undifferenziert     |
|15205054 | Kalkschieferzone | Kalkschieferzone     |
|15206052 | Kalksilikatfels | Kalksilikatfels     |
|15206108 | Kalkstein, undifferenziert | Kalkstein, undifferenziert     |
|15200530 | Kaltbach-Nagelfluh | Kaltbach-Nagelfluh     |
|15200647 | Kalter-Wangen-Formation | Kalter-Wangen-Formation     |
|15202054 | Kamm-Bank | Kamm-Bank     |
|15200544 | Kännelegg-Nagelfluh | Kännelegg-Nagelfluh     |
|15206056 | Känozoikum, undifferenziert | Känozoikum, undifferenziert     |
|15202491 | Kapfen-Formation | Kapfen-Formation     |
|15202492 | Kapfen-Sandstein | Kapfen-Sandstein     |
|15200509 | Käpfnach-Formation | Käpfnach-Formation     |
|15203473 | Karbon der Maggia-Decke | Karbon der Maggia-Decke     |
|15203348 | Karbon der Zone-Houillère | Karbon der Zone-Houillère     |
|15206080 | Karbon, undifferenziert | Karbon, undifferenziert     |
|15200644 | Karbonatreiche Molasse | Karbonatreiche Molasse     |
|15200645 | Karbonatreiche Molasse: Kalk-Dolomit-Nagelfluh | Karbonatreiche Molasse: Kalk-Dolomit-Nagelfluh     |
|15200147 | Karneol-Horizont | Karneol-Horizont     |
|15203527 | Karpatischer Keuper | Karpatischer Keuper     |
|15202147 | Kärpf-Formation | Kärpf-Formation     |
|15202493 | Kärpfgipfel-Sernifit | Kärpfgipfel-Sernifit     |
|15202148 | Karrenstock-Formation | Karrenstock-Formation     |
|15204118 | Kesch-Augengneis | Kesch-Augengneis     |
|15200125 | Keuper | Keuper     |
|15200134 | Kienberg-Member | Kienberg-Member     |
|15202364 | Kiental-Melange | Kiental-Melange     |
|15200413 | Kirchberg-Formation | Kirchberg-Formation     |
|15202292 | Kistenstöckli-Member | Kistenstöckli-Member     |
|15202062 | Klaus-Bank | Klaus-Bank     |
|15202296 | Kleintal-Konglomerat | Kleintal-Konglomerat     |
|15200234 | Klemmbach-Granit | Klemmbach-Granit     |
|15200126 | Klettgau-Formation | Klettgau-Formation     |
|15202028 | Klimsenhorn-Formation | Klimsenhorn-Formation     |
|15200120 | Klingnau-Formation | Klingnau-Formation     |
|15203562 | Klippen-Flysch | Klippen-Flysch     |
|15203171 | Klus-Formation | Klus-Formation     |
|15203090 | Klus-Konglomerat | Klus-Konglomerat     |
|15200518 | Klusbach-Member | Klusbach-Member     |
|15200108 | Knollen-Bank | Knollen-Bank     |
|15203065 | Knollenargovien | Knollenargovien     |
|15200121 | Knorri-Ton | Knorri-Ton     |
|15200229 | Kohle-Serie | Kohle-Serie     |
|15206064 | Konglomerat, undifferenziert | Konglomerat, undifferenziert     |
|15203376 | Konglomeratgneis (Terri) | Konglomeratgneis (Terri)     |
|15206109 | Konglomeratgneis, undifferenziert | Konglomeratgneis, undifferenziert     |
|15204024 | Kössen-Formation | Kössen-Formation     |
|15202047 | Kreide des Helvetikums | Kreide des Helvetikums     |
|15200161 | Kreide des Juragebirges | Kreide des Juragebirges     |
|15204089 | Kreide des Ostalpins | Kreide des Ostalpins     |
|15205072 | Kreide des Südalpins | Kreide des Südalpins     |
|15206028 | Kreide, undifferenziert | Kreide, undifferenziert     |
|15200681 | Kreuzlingen-Granit | Kreuzlingen-Granit     |
|15200273 | Krinau-Schichten | Krinau-Schichten     |
|15203400 | Kristallin der Berisal-Decke | Kristallin der Berisal-Decke     |
|15205127 | Kristallin der Margna-Sella | Kristallin der Margna-Sella     |
|15203320 | Kristallin der Monte-Leone-Decke | Kristallin der Monte-Leone-Decke     |
|15200616 | Kristallin der Nordschweiz | Kristallin der Nordschweiz     |
|15203448 | Kristallin der Portjengrat-Decke | Kristallin der Portjengrat-Decke     |
|15203433 | Kristallin der Ruginenta-Decke | Kristallin der Ruginenta-Decke     |
|15203402 | Kristallin der Ruitor-Decke | Kristallin der Ruitor-Decke     |
|15203405 | Kristallin des Briançonnais | Kristallin des Briançonnais     |
|15202466 | Kristallin des Helvetikums | Kristallin des Helvetikums     |
|15204091 | Kristallin des Ostalpins | Kristallin des Ostalpins     |
|15205078 | Kristallin des Südalpins | Kristallin des Südalpins     |
|15206031 | Kristallingestein, undifferenziert | Kristallingestein, undifferenziert     |
|15200316 | Kronberg-Nagelfluh | Kronberg-Nagelfluh     |
|15200526 | Krummenau-Member | Krummenau-Member     |
|15200424 | Krustenkalk | Krustenkalk     |
|15202027 | Küblibad-Member | Küblibad-Member     |
|15203271 | Kummli-Schichten | Kummli-Schichten     |
|15200288 | Küsnacht-Bentonit | Küsnacht-Bentonit     |
|15200109 | Küssaburg-Member | Küssaburg-Member     |
|15200449 | La-Charrue-Süsswasserkalk | La-Charrue-Süsswasserkalk     |
|15200342 | La-Chaux-Süsswasserkalk | La-Chaux-Süsswasserkalk     |
|15203398 | La-Dotse-Albitkalk | La-Dotse-Albitkalk     |
|15200027 | La-May-Member | La-May-Member     |
|15200438 | La-Presta-Mergel | La-Presta-Mergel     |
|15204113 | La-Rösa-Orthogneis | La-Rösa-Orthogneis     |
|15200665 | La-Vaux-Bank | La-Vaux-Bank     |
|15200448 | La-Verrerie-Süsswasserkalk | La-Verrerie-Süsswasserkalk     |
|15202213 | Lac-Cornu-Eklogit | Lac-Cornu-Eklogit     |
|15203395 | Lacerandes-Augengneis | Lacerandes-Augengneis     |
|15200474 | Lacunosamergel-Formation | Lacunosamergel-Formation     |
|15203367 | Lagensandkalk | Lagensandkalk     |
|15203483 | Lago-Scuro-Formation | Lago-Scuro-Formation     |
|15202234 | Laiets-Gneiskomplex | Laiets-Gneiskomplex     |
|15202170 | Lakustrisches Member | Lakustrisches Member     |
|15203244 | Lamperehubel-Sandstein | Lamperehubel-Sandstein     |
|15200456 | Landaize-Kalk | Landaize-Kalk     |
|15204058 | Landwasser-Member | Landwasser-Member     |
|15203588 | Langel- und Col-de-Cordon-Member, undifferenziert | Langel- und Col-de-Cordon-Member, undifferenziert     |
|15203239 | Langel-Member | Langel-Member     |
|15203578 | Langel-Member der Zentralschweizer Klippen | Langel-Member der Zentralschweizer Klippen     |
|15203328 | Langenegg-Formation | Langenegg-Formation     |
|15203007 | Langy-Member | Langy-Member     |
|15202587 | Laubersmad-Flysch | Laubersmad-Flysch     |
|15200395 | Laufen-Juranagelfluh | Laufen-Juranagelfluh     |
|15200191 | Laufen-Member | Laufen-Member     |
|15200249 | Laufenburg-Gneiskomplex | Laufenburg-Gneiskomplex     |
|15203232 | Lavagna-Formation | Lavagna-Formation     |
|15204093 | Lavatèra-Brekzie | Lavatèra-Brekzie     |
|15204126 | Lavinèr-Brekzie | Lavinèr-Brekzie     |
|15202286 | Lavtina-Sandstein | Lavtina-Sandstein     |
|15200671 | Le-Coin-Formation | Le-Coin-Formation     |
|15200623 | Le-Locle-Formation | Le-Locle-Formation     |
|15200624 | Le-Verger-Member | Le-Verger-Member     |
|15203430 | Lebendun-Gneis, arkosisch | Lebendun-Gneis, arkosisch     |
|15203431 | Lebendun-Gneis, konglomeratisch | Lebendun-Gneis, konglomeratisch     |
|15203318 | Lebendun-Gneiskomplex | Lebendun-Gneiskomplex     |
|15204003 | Lech-Formation | Lech-Formation     |
|15203557 | Legiuna-Gneis | Legiuna-Gneis     |
|15202422 | Leiboden-Mergel | Leiboden-Mergel     |
|15200282 | Leimbach-Bentonit | Leimbach-Bentonit     |
|15203155 | Leimern-Kalk | Leimern-Kalk     |
|15203574 | Leimern-Schichten | Leimern-Schichten     |
|15202421 | Leist-Mergel | Leist-Mergel     |
|15200240 | Lenzkirch-Steina-Granit | Lenzkirch-Steina-Granit     |
|15200572 | Les-Bayards-Juranagelfluh | Les-Bayards-Juranagelfluh     |
|15203098 | Lessus-Member | Lessus-Member     |
|15200107 | Letzi-Member | Letzi-Member     |
|15200538 | Leuenfall-Nagelfluh | Leuenfall-Nagelfluh     |
|15203427 | Leukogneis der Monte-Leone-Decke | Leukogneis der Monte-Leone-Decke     |
|15200464 | Leutschenberg-Member | Leutschenberg-Member     |
|15203551 | Leventina-D.: Amphibolit | Leventina-D.: Amphibolit     |
|15203548 | Leventina-D.: Kalksilikatfels | Leventina-D.: Kalksilikatfels     |
|15203549 | Leventina-D.: Leukogneis | Leventina-D.: Leukogneis     |
|15203550 | Leventina-D.: Paragneis | Leventina-D.: Paragneis     |
|15202273 | Leventina-Gneis | Leventina-Gneis     |
|15203546 | Leventina-Gneis: oberer Teil | Leventina-Gneis: oberer Teil     |
|15203547 | Leventina-Gneis: unterer Teil | Leventina-Gneis: unterer Teil     |
|15203010 | Leyderry-Member | Leyderry-Member     |
|15203251 | Lias-Kalk (Grava) | Lias-Kalk (Grava)     |
|15203275 | Lias der Klippen-Decke | Lias der Klippen-Decke     |
|15202120 | Lias des Helvetikums | Lias des Helvetikums     |
|15200056 | Lias des Juragebirges | Lias des Juragebirges     |
|15204090 | Lias des Ostalpins | Lias des Ostalpins     |
|15205075 | Lias des Südalpins | Lias des Südalpins     |
|15206025 | Lias, undifferenziert | Lias, undifferenziert     |
|15200296 | Lichtensteig-Schichten | Lichtensteig-Schichten     |
|15202081 | Lidernen-Member | Lidernen-Member     |
|15203149 | Liechtenstein-Flysch | Liechtenstein-Flysch     |
|15200133 | Liedertswil-Member | Liedertswil-Member     |
|15200471 | Liegende-Bankkalke-Formation | Liegende-Bankkalke-Formation     |
|15200637 | Lienegg-Formation | Lienegg-Formation     |
|15200040 | Liesberg-Member | Liesberg-Member     |
|15200619 | Limnischer Horizont (OMM-I) | Limnischer Horizont (OMM-I)     |
|15200431 | Limnischer Horizont (OMM-II) | Limnischer Horizont (OMM-II)     |
|15200680 | Lindau-Granit | Lindau-Granit     |
|15203197 | Lirec-Formation | Lirec-Formation     |
|15206020 | Lithologische Einheit, undifferenziert | Lithologische Einheit, undifferenziert     |
|15203518 | Lizun-Grünschiefer | Lizun-Grünschiefer     |
|15202411 | Lochegg-Brekzie | Lochegg-Brekzie     |
|15200476 | Lochen-Subformation | Lochen-Subformation     |
|15206018 | Lochsiten-Kalk | Lochsiten-Kalk     |
|15203313 | Lodano-Gneis | Lodano-Gneis     |
|15202218 | Lognan-Orthogneis | Lognan-Orthogneis     |
|15205033 | Lombardische Radiolarit-Gruppe | Lombardische Radiolarit-Gruppe     |
|15200590 | Loorenkopf-Nagelfluh | Loorenkopf-Nagelfluh     |
|15203488 | Loranco-Amphibolit | Loranco-Amphibolit     |
|15200532 | Losenegg-Formation | Losenegg-Formation     |
|15205093 | Losone-Schiefer | Losone-Schiefer     |
|15202520 | Lotharingien-Sandstein | Lotharingien-Sandstein     |
|15202200 | Lötschental-Gneiskomplex | Lötschental-Gneiskomplex     |
|15202560 | Lötschental-Gneiskomplex: Chloritschiefer | Lötschental-Gneiskomplex: Chloritschiefer     |
|15202559 | Lötschental-Gneiskomplex: migmatitischer Biotitgneis | Lötschental-Gneiskomplex: migmatitischer Biotitgneis     |
|15202558 | Lötschental-Gneiskomplex: Muskovitgneis | Lötschental-Gneiskomplex: Muskovitgneis     |
|15205011 | Lucino-Konglomerat | Lucino-Konglomerat     |
|15203081 | Lückengraben-Formation | Lückengraben-Formation     |
|15203374 | Lugnez-Schiefer | Lugnez-Schiefer     |
|15202211 | Luisin-Orthogneis | Luisin-Orthogneis     |
|15202068 | Luitere-Bank | Luitere-Bank     |
|15200312 | Luzern-Formation | Luzern-Formation     |
|15202448 | Maasplanggstock-Metaandesit | Maasplanggstock-Metaandesit     |
|15205043 | Macchia Vecchia | Macchia Vecchia     |
|15200482 | Macrocephalenoolith-Subformation | Macrocephalenoolith-Subformation     |
|15203385 | Macugnaga-Augengneis | Macugnaga-Augengneis     |
|15200199 | Maeandrina-Schichten | Maeandrina-Schichten     |
|15203552 | Maggia-D.: Amphibolit | Maggia-D.: Amphibolit     |
|15203476 | Maggia-D.: Paragneis | Maggia-D.: Paragneis     |
|15205092 | Maia-Metagabbro | Maia-Metagabbro     |
|15205032 | Maiolica Lombarda | Maiolica Lombarda     |
|15203341 | Malenco-Serpentinit | Malenco-Serpentinit     |
|15203269 | Malm der Klippen-Decke | Malm der Klippen-Decke     |
|15202096 | Malm des Helvetikums | Malm des Helvetikums     |
|15200012 | Malm des Juragebirges | Malm des Juragebirges     |
|15204088 | Malm des Ostalpins | Malm des Ostalpins     |
|15205073 | Malm des Südalpins | Malm des Südalpins     |
|15206027 | Malm, undifferenziert | Malm, undifferenziert     |
|15202538 | Malmbrekzie | Malmbrekzie     |
|15203064 | Malmkalk | Malmkalk     |
|15205016 | Malnate-Sandstein | Malnate-Sandstein     |
|15204099 | Maloja-Gneiskomplex | Maloja-Gneiskomplex     |
|15204098 | Maloja-Orthogneis | Maloja-Orthogneis     |
|15202294 | Malor-Member | Malor-Member     |
|15200232 | Malsburg-Granit | Malsburg-Granit     |
|15200239 | Mambach-Granit | Mambach-Granit     |
|15206053 | Mamor, undifferenziert | Mamor, undifferenziert     |
|15203133 | Manche-Formation | Manche-Formation     |
|15205070 | Manno-Formation | Manno-Formation     |
|15203494 | Maran-Brekzie | Maran-Brekzie     |
|15200558 | Marbach-Member | Marbach-Member     |
|15202151 | Mären-Formation | Mären-Formation     |
|15205126 | Marinelli-Formation | Marinelli-Formation     |
|15203158 | Marmontains-Schichten | Marmontains-Schichten     |
|15203410 | Marmor der Tsaté-Decke | Marmor der Tsaté-Decke     |
|15205121 | Marmor der Valpelline-Gruppe | Marmor der Valpelline-Gruppe     |
|15203418 | Marmor der Zermatt-Saas-Decke | Marmor der Zermatt-Saas-Decke     |
|15200356 | Marnes gris-souris | Marnes gris-souris     |
|15202281 | Martinsmad-Formation | Martinsmad-Formation     |
|15202331 | Massa-Gneiskomplex | Massa-Gneiskomplex     |
|15203485 | Massari-Formation | Massari-Formation     |
|15200546 | Mathod-Sandstein | Mathod-Sandstein     |
|15203317 | Matorello-Gneis | Matorello-Gneis     |
|15203188 | Matse-Member | Matse-Member     |
|15202006 | Matt-Formation | Matt-Formation     |
|15202362 | Mättental-Melange | Mättental-Melange     |
|15205096 | Matterhorn-Gabbro | Matterhorn-Gabbro     |
|15203100 | Mattes-Melange | Mattes-Melange     |
|15202034 | Mattgrat-Member | Mattgrat-Member     |
|15200345 | Matzendorf-Süsswasserkalk | Matzendorf-Süsswasserkalk     |
|15202226 | Medel-Granit | Medel-Granit     |
|15203355 | Medola-Quarzit | Medola-Quarzit     |
|15200366 | Meeressand | Meeressand     |
|15202374 | Meierhof-Phyllit | Meierhof-Phyllit     |
|15200294 | Meilen-Kalk | Meilen-Kalk     |
|15200507 | Meilen-Schichten | Meilen-Schichten     |
|15202285 | Meilleret-Formation | Meilleret-Formation     |
|15202523 | Meilleret-Formation, Arkose | Meilleret-Formation, Arkose     |
|15202522 | Meilleret-Formation, Calcaires organo-détritiques | Meilleret-Formation, Calcaires organo-détritiques     |
|15202524 | Meilleret-Formation, Conglomérat basal | Meilleret-Formation, Conglomérat basal     |
|15200416 | Meinisberg-Muschelsandstein | Meinisberg-Muschelsandstein     |
|15206005 | Melirolo-Augengneis | Melirolo-Augengneis     |
|15202584 | Mels- und Röti-Formation, undifferenziert | Mels- und Röti-Formation, undifferenziert     |
|15202141 | Mels-Formation | Mels-Formation     |
|15200454 | Mergel- und Kalkzone (MKZ) | Mergel- und Kalkzone (MKZ)     |
|15200184 | Mergelkalk-Zone | Mergelkalk-Zone     |
|15206118 | Mergelstein, undifferenziert | Mergelstein, undifferenziert     |
|15203298 | Mergoscia-Gneis | Mergoscia-Gneis     |
|15205053 | Meride-Formation | Meride-Formation     |
|15206034 | Mesozoikum, undifferenziert | Mesozoikum, undifferenziert     |
|15205112 | Metabasit der Arolla-Gruppe | Metabasit der Arolla-Gruppe     |
|15205113 | Metabasit der Arolla-Gruppe, mylonitisch | Metabasit der Arolla-Gruppe, mylonitisch     |
|15205111 | Metagranitoide der Arolla-Gruppe | Metagranitoide der Arolla-Gruppe     |
|15203193 | Métailler-Formation | Métailler-Formation     |
|15203411 | Metaradiolarit der Tsaté-Decke | Metaradiolarit der Tsaté-Decke     |
|15203492 | Metasedimente der Arosa-Decke | Metasedimente der Arosa-Decke     |
|15203502 | Metasedimente der Avers-Decke | Metasedimente der Avers-Decke     |
|15203496 | Metasedimente der Platta-Decke | Metasedimente der Platta-Decke     |
|15203409 | Metasedimente der Tsaté-Decke | Metasedimente der Tsaté-Decke     |
|15203412 | Metasedimente der Zermatt-Saas-Decke | Metasedimente der Zermatt-Saas-Decke     |
|15204042 | Mezdi-Member | Mezdi-Member     |
|15203439 | Mezzalama-Granit | Mezzalama-Granit     |
|15204017 | Mezzaun-Member | Mezzaun-Member     |
|15203274 | Mieussy-Member | Mieussy-Member     |
|15202205 | Miéville-Mylonit | Miéville-Mylonit     |
|15202259 | Migmatit der Ausserberg-Avat-Zone | Migmatit der Ausserberg-Avat-Zone     |
|15202269 | Migmatit der Ausserbinn-Piz-Cavel-Zone | Migmatit der Ausserbinn-Piz-Cavel-Zone     |
|15205122 | Migmatit der Valpelline-Gruppe | Migmatit der Valpelline-Gruppe     |
|15206086 | Migmatit, undifferenziert | Migmatit, undifferenziert     |
|15206061 | Mikrodiorit, undifferenziert | Mikrodiorit, undifferenziert     |
|15206044 | Mikrogranit | Mikrogranit     |
|15206043 | Mineralisierter Gang | Mineralisierter Gang     |
|15204046 | Mingèr-Dolomit | Mingèr-Dolomit     |
|15204045 | Mingèr-Formation | Mingèr-Formation     |
|15203505 | Minschun-Brekzie | Minschun-Brekzie     |
|15203465 | Minugrat-Eklogit | Minugrat-Eklogit     |
|15204026 | Mitgel-Member | Mitgel-Member     |
|15202159 | Mittagflue-Granit | Mittagflue-Granit     |
|15203577 | Mittellias der Klippen-Decke | Mittellias der Klippen-Decke     |
|15202332 | Mittelvariszische Intrusiva des Aiguilles-Rouges-Massivs | Mittelvariszische Intrusiva des Aiguilles-Rouges-Massivs     |
|15200562 | Mittlere Juranagelfluh | Mittlere Juranagelfluh     |
|15203129 | Mocausa-Nagelfluh | Mocausa-Nagelfluh     |
|15200254 | Molasse | Molasse     |
|15200337 | Molasse à Charbon | Molasse à Charbon     |
|15200332 | Molasse Grise de Lausanne | Molasse Grise de Lausanne     |
|15200338 | Molasse Rouge | Molasse Rouge     |
|15200545 | Molasse Rouge des Jurasüdfusses | Molasse Rouge des Jurasüdfusses     |
|15200549 | Molasse Rouge von Monthey | Molasse Rouge von Monthey     |
|15200548 | Molasse Rouge von Vevey | Molasse Rouge von Vevey     |
|15203039 | Moléson-Formation | Moléson-Formation     |
|15200420 | Molière-Muschelsandstein | Molière-Muschelsandstein     |
|15205041 | Molino-Member | Molino-Member     |
|15202117 | Mols-Member | Mols-Member     |
|15205040 | Moltrasio-Formation | Moltrasio-Formation     |
|15204082 | Mönchalp-Augengneis | Mönchalp-Augengneis     |
|15203462 | Moncucco-Peridotit | Moncucco-Peridotit     |
|15203191 | Mondra-Member | Mondra-Member     |
|15202216 | Mont-Blanc-Granit | Mont-Blanc-Granit     |
|15205005 | Mont-Collon-Komplex | Mont-Collon-Komplex     |
|15203415 | Mont-des-Ritzes-Metabasalt | Mont-des-Ritzes-Metabasalt     |
|15202126 | Mont-Joly-Formation | Mont-Joly-Formation     |
|15205086 | Mont-Morion-Granit | Mont-Morion-Granit     |
|15203396 | Mont-Mort-Metapelit | Mont-Mort-Metapelit     |
|15200318 | Mont-Pèlerin-Nagelfluh | Mont-Pèlerin-Nagelfluh     |
|15203196 | Mont-Rogneux-Metagranit | Mont-Rogneux-Metagranit     |
|15200083 | Mont-Terri-Member | Mont-Terri-Member     |
|15200586 | Montauban-Mergel | Montauban-Mergel     |
|15200587 | Montauban-Sandstein | Montauban-Sandstein     |
|15200386 | Montchaibeux-Member | Montchaibeux-Member     |
|15200653 | Montcherand-Member | Montcherand-Member     |
|15206008 | Monte-Bassetta-Quarzdiorit | Monte-Bassetta-Quarzdiorit     |
|15203299 | Monte-Rosa-Gneis | Monte-Rosa-Gneis     |
|15203440 | Monte-Rosa-Orthogneis, grobkörnig | Monte-Rosa-Orthogneis, grobkörnig     |
|15203453 | Monte-Rosa-Orthogneis, mittelkörnig | Monte-Rosa-Orthogneis, mittelkörnig     |
|15203442 | Monte-Rosa-Orthogneis, mylonitisch | Monte-Rosa-Orthogneis, mylonitisch     |
|15206013 | Monte-Rosso-Mikrogranit | Monte-Rosso-Mikrogranit     |
|15200419 | Montécu-Schichten | Montécu-Schichten     |
|15202206 | Montées-Pélissiers-Granit | Montées-Pélissiers-Granit     |
|15202217 | Montenvers-Granit | Montenvers-Granit     |
|15202123 | Monts-Rosset-Formation | Monts-Rosset-Formation     |
|15204047 | Mora-Member | Mora-Member     |
|15205038 | Morbio-Formation | Morbio-Formation     |
|15202480 | Morcles-Mikrogranit | Morcles-Mikrogranit     |
|15200588 | Mornex-Nagelfluh | Mornex-Nagelfluh     |
|15200664 | Morteau-Bänke | Morteau-Bänke     |
|15200669 | Morteau-Mergel | Morteau-Mergel     |
|15204116 | Morteratsch-Serpentinit | Morteratsch-Serpentinit     |
|15200442 | Mortier-Mergel | Mortier-Mergel     |
|15200119 | Moutier-Korallenkalk | Moutier-Korallenkalk     |
|15200059 | Movelier-Schichten | Movelier-Schichten     |
|15200618 | Mümliswil-Süsswasserkalk | Mümliswil-Süsswasserkalk     |
|15200236 | Münsterhalden-Granit | Münsterhalden-Granit     |
|15202180 | Munt-Dado-Granit | Munt-Dado-Granit     |
|15202290 | Muot-da-Rubi-Formation | Muot-da-Rubi-Formation     |
|15200493 | Murchisonaeoolith-Formation | Murchisonaeoolith-Formation     |
|15203343 | Muretto-Quarzit | Muretto-Quarzit     |
|15203013 | Murgaz-Kalk | Murgaz-Kalk     |
|15202324 | Murgtal-Formation | Murgtal-Formation     |
|15200248 | Murgtal-Gneiskomplex | Murgtal-Gneiskomplex     |
|15202044 | Mürren-Brekzie | Mürren-Brekzie     |
|15204031 | Murtèr-Plattenkalk | Murtèr-Plattenkalk     |
|15204032 | Murteret-Dolomit | Murteret-Dolomit     |
|15202101 | Mürtschen-Member | Mürtschen-Member     |
|15204037 | Müschauns-Dolomit | Müschauns-Dolomit     |
|15200129 | Muschelkalk | Muschelkalk     |
|15200391 | Muschelsandstein | Muschelsandstein     |
|15205124 | Musella-Granit | Musella-Granit     |
|15203073 | Musenalp-Member | Musenalp-Member     |
|15200078 | Müsenegg-Bank | Müsenegg-Bank     |
|15200181 | Mussel-Member | Mussel-Member     |
|15205119 | Mylonit der Valpelline-Gruppe | Mylonit der Valpelline-Gruppe     |
|15206051 | Mylonit, undifferenziert | Mylonit, undifferenziert     |
|15203067 | Mythen-Kieselkalk | Mythen-Kieselkalk     |
|15203088 | Mytilus-Schichten | Mytilus-Schichten     |
|15204092 | Nair-Porphyroid | Nair-Porphyroid     |
|15200258 | Napf-Formation | Napf-Formation     |
|15200622 | Napf-Formation, distale Fazies | Napf-Formation, distale Fazies     |
|15200621 | Napf-Formation, proximale Fazies | Napf-Formation, proximale Fazies     |
|15203486 | Naret-Formation | Naret-Formation     |
|15200148 | Narlay-Formation | Narlay-Formation     |
|15202237 | Nelva-Gneiskomplex | Nelva-Gneiskomplex     |
|15203063 | Neokom | Neokom     |
|15200649 | Netzbachtal-Nagelfluh | Netzbachtal-Nagelfluh     |
|15202020 | Niederhorn-Formation | Niederhorn-Formation     |
|15202060 | Niederi-Schichten | Niederi-Schichten     |
|15200401 | Niedermatt-Formation | Niedermatt-Formation     |
|15203001 | Niesen-Flysch | Niesen-Flysch     |
|15203004 | Niesenkulm-Formation | Niesenkulm-Formation     |
|15203205 | Nisellas-Gruppe | Nisellas-Gruppe     |
|15203176 | Nolla-Kalkschiefer | Nolla-Kalkschiefer     |
|15203209 | Nolla-Kristallin | Nolla-Kristallin     |
|15203177 | Nolla-Tonschiefer | Nolla-Tonschiefer     |
|15203579 | Nolla-Tonschiefer: Quarzsandstein | Nolla-Tonschiefer: Quarzsandstein     |
|15202005 | Nordhelvetische Flysch-Gruppe | Nordhelvetische Flysch-Gruppe     |
|15202542 | Nordhelvetische Flysch-Gruppe, vorw. schiefriger Tonstein | Nordhelvetische Flysch-Gruppe, vorw. schiefriger Tonstein     |
|15203252 | Nordpenninische Trias | Nordpenninische Trias     |
|15203456 | Nordpenninischer Dogger | Nordpenninischer Dogger     |
|15203457 | Nordpenninischer Lias | Nordpenninischer Lias     |
|15206002 | Novate-Intrusiva | Novate-Intrusiva     |
|15202369 | Nufenen-Granatschiefer | Nufenen-Granatschiefer     |
|15202367 | Nufenen-Knotenschiefer | Nufenen-Knotenschiefer     |
|15202368 | Nufenen-Sandstein | Nufenen-Sandstein     |
|15200578 | Numismalismergel-Formation | Numismalismergel-Formation     |
|15202257 | Oberaar-Furka-Zone | Oberaar-Furka-Zone     |
|15203164 | Oberälpli-Formation | Oberälpli-Formation     |
|15200331 | Oberaquitane Mergelzone | Oberaquitane Mergelzone     |
|15200430 | Oberdorf-Süsswasserkalk | Oberdorf-Süsswasserkalk     |
|15200472 | Obere-Felsenkalke-Formation | Obere-Felsenkalke-Formation     |
|15200061 | Obere Acuminata-Schichten | Obere Acuminata-Schichten     |
|15203104 | Obere Brekzie | Obere Brekzie     |
|15200429 | Obere bunte Molasse | Obere bunte Molasse     |
|15202282 | Obere Flyschabfolge (Sardona) | Obere Flyschabfolge (Sardona)     |
|15200412 | Obere Grenznagelfluh | Obere Grenznagelfluh     |
|15203246 | Obere Kalk- und Tonschiefer der Zone Piz Terri - Lunschania | Obere Kalk- und Tonschiefer der Zone Piz Terri - Lunschania     |
|15200307 | Obere Meeresmolasse (OMM) | Obere Meeresmolasse (OMM)     |
|15200060 | Obere Oolithische Serie (Grande Oolithe) | Obere Oolithische Serie (Grande Oolithe)     |
|15203240 | Obere Rauwacke der Klippen-Decke | Obere Rauwacke der Klippen-Decke     |
|15202534 | Obere Sandsteine (Spirstock) | Obere Sandsteine (Spirstock)     |
|15203105 | Obere Schiefer (Schistes Ardoisiers) | Obere Schiefer (Schistes Ardoisiers)     |
|15200136 | Obere Sufatzone | Obere Sufatzone     |
|15200255 | Obere Süsswassermolasse (OSM) | Obere Süsswassermolasse (OSM)     |
|15203120 | Obere Tonsteinschichten | Obere Tonsteinschichten     |
|15203470 | Oberems-Albitgneis | Oberems-Albitgneis     |
|15205099 | Oberer Meride-Kalk | Oberer Meride-Kalk     |
|15202302 | Oberer Quintner Kalk | Oberer Quintner Kalk     |
|15202599 | Oberer Quintner Kalk: Korallenkalk | Oberer Quintner Kalk: Korallenkalk     |
|15202600 | Oberer Quintner Kalk: Unterer Kalk | Oberer Quintner Kalk: Unterer Kalk     |
|15200217 | Oberer Schuttfächer | Oberer Schuttfächer     |
|15200380 | Oberer Teil des Hauptrogensteins | Oberer Teil des Hauptrogensteins     |
|15200015 | Oberer Virgula-Mergel | Oberer Virgula-Mergel     |
|15200475 | Oberjura-Massenkalk-Formation | Oberjura-Massenkalk-Formation     |
|15202352 | Oberstafel-Gneis | Oberstafel-Gneis     |
|15203078 | Obflue-Formation | Obflue-Formation     |
|15203201 | Obrist-Gruppe | Obrist-Gruppe     |
|15200579 | Obtususton-Formation | Obtususton-Formation     |
|15200303 | Oehningien des Juragebirges | Oehningien des Juragebirges     |
|15200346 | Oensingen-Süsswasserkalk | Oensingen-Süsswasserkalk     |
|15202201 | Ofenhorn-Stampfhorn-Gneiskomplex | Ofenhorn-Stampfhorn-Gneiskomplex     |
|15202580 | Ofenhorn-Stampfhorn-Gneiskomplex: aplitischer Granit | Ofenhorn-Stampfhorn-Gneiskomplex: aplitischer Granit     |
|15202563 | Ofenhorn-Stampfhorn-Gneiskomplex: Biotitgneis | Ofenhorn-Stampfhorn-Gneiskomplex: Biotitgneis     |
|15202561 | Ofenhorn-Stampfhorn-Gneiskomplex: gebänderter Biotit-Plagioklasgneis | Ofenhorn-Stampfhorn-Gneiskomplex: gebänderter Biotit-Plagioklasgneis     |
|15202562 | Ofenhorn-Stampfhorn-Gneiskomplex: Migmatit | Ofenhorn-Stampfhorn-Gneiskomplex: Migmatit     |
|15202579 | Ofenhorn-Stampfhorn-Gneiskomplex: mit Schollenamphibolit | Ofenhorn-Stampfhorn-Gneiskomplex: mit Schollenamphibolit     |
|15202564 | Ofenhorn-Stampfhorn-Gneiskomplex: Orthogneis | Ofenhorn-Stampfhorn-Gneiskomplex: Orthogneis     |
|15202581 | Ofenhorn-Stampfhorn-Gneiskomplex: Schollenamphibolit | Ofenhorn-Stampfhorn-Gneiskomplex: Schollenamphibolit     |
|15202582 | Ofenhorn-Stampfhorn-Gneiskomplex: Ultramafit | Ofenhorn-Stampfhorn-Gneiskomplex: Ultramafit     |
|15200503 | Öhningen-Formation | Öhningen-Formation     |
|15200504 | Öhningen-Süsswasserkalk | Öhningen-Süsswasserkalk     |
|15200272 | Öhningen-Zone im Hörnligebiet | Öhningen-Zone im Hörnligebiet     |
|15202091 | Öhrli-Formation | Öhrli-Formation     |
|15202527 | Öhrli-Formation, von Siderolithikum durchsetzt | Öhrli-Formation, von Siderolithikum durchsetzt     |
|15200638 | Öligraben-Formation | Öligraben-Formation     |
|15200192 | Olten-Member | Olten-Member     |
|15200553 | Oltingue-Kalkarenit | Oltingue-Kalkarenit     |
|15200311 | OMM-I | OMM-I     |
|15200308 | OMM-II | OMM-II     |
|15200567 | OMM-J | OMM-J     |
|15200028 | Oolithe-Rousse-Member | Oolithe-Rousse-Member     |
|15200010 | Opalinus-Ton | Opalinus-Ton     |
|15206059 | Ophikalzit, undifferenziert | Ophikalzit, undifferenziert     |
|15203424 | Ophiolith der Antrona-Decke | Ophiolith der Antrona-Decke     |
|15203236 | Ophiolith der Arosa-Zone | Ophiolith der Arosa-Zone     |
|15203503 | Ophiolith der Avers-Decke | Ophiolith der Avers-Decke     |
|15203500 | Ophiolith der Platta-Decke | Ophiolith der Platta-Decke     |
|15203491 | Ophiolith der Ramosch-Zone | Ophiolith der Ramosch-Zone     |
|15203414 | Ophiolith der Tsaté-Decke | Ophiolith der Tsaté-Decke     |
|15203422 | Ophiolith der Zermatt-Saas-Decke | Ophiolith der Zermatt-Saas-Decke     |
|15200423 | Orbe-Süsswasserkalk | Orbe-Süsswasserkalk     |
|15200140 | Orbicularis-Mergel | Orbicularis-Mergel     |
|15200479 | Ornatenton-Formation | Ornatenton-Formation     |
|15205006 | Orthogneis der Arolla-Gruppe | Orthogneis der Arolla-Gruppe     |
|15205107 | Orthogneis der Arolla-Gruppe, augig | Orthogneis der Arolla-Gruppe, augig     |
|15205106 | Orthogneis der Arolla-Gruppe, leukokrat | Orthogneis der Arolla-Gruppe, leukokrat     |
|15205108 | Orthogneis der Arolla-Gruppe, mylonitisch | Orthogneis der Arolla-Gruppe, mylonitisch     |
|15202274 | Orthogneis der Lukmanier-Decke | Orthogneis der Lukmanier-Decke     |
|15203426 | Orthogneis der Monte-Leone-Decke | Orthogneis der Monte-Leone-Decke     |
|15203449 | Orthogneis der Portjengrat-Decke | Orthogneis der Portjengrat-Decke     |
|15205131 | Orthogneis der Sesia-Decke | Orthogneis der Sesia-Decke     |
|15206076 | Orthogneis, undifferenziert | Orthogneis, undifferenziert     |
|15200295 | OSM-I | OSM-I     |
|15200262 | OSM-II | OSM-II     |
|15200300 | OSM-J | OSM-J     |
|15203268 | Oudiou-Formation | Oudiou-Formation     |
|15202012 | Paläogen des Helvetikums | Paläogen des Helvetikums     |
|15206055 | Paläozoikum, undifferenziert | Paläozoikum, undifferenziert     |
|15202092 | Palfris-Formation | Palfris-Formation     |
|15202382 | Palis-Member | Palis-Member     |
|15203233 | Palombini-Formation | Palombini-Formation     |
|15203218 | Panier-Formation | Panier-Formation     |
|15202351 | Paradis-Gneiskomplex | Paradis-Gneiskomplex     |
|15202261 | Paragneis der Ausserberg-Avat-Zone | Paragneis der Ausserberg-Avat-Zone     |
|15202270 | Paragneis der Ausserbinn-Piz-Cavel-Zone | Paragneis der Ausserbinn-Piz-Cavel-Zone     |
|15202275 | Paragneis der Lukmanier-Decke | Paragneis der Lukmanier-Decke     |
|15203429 | Paragneis der Monte-Leone-Decke | Paragneis der Monte-Leone-Decke     |
|15203443 | Paragneis der Monte-Rosa-Decke | Paragneis der Monte-Rosa-Decke     |
|15203435 | Paragneis der Ruginenta-Decke | Paragneis der Ruginenta-Decke     |
|15206077 | Paragneis, undifferenziert | Paragneis, undifferenziert     |
|15205117 | Paragneiss der Arolla-Gruppe | Paragneiss der Arolla-Gruppe     |
|15204052 | Parai-Alba-Member | Parai-Alba-Member     |
|15204139 | Parait-Chavagl-Granit | Parait-Chavagl-Granit     |
|15202486 | Pardatschas-Granit | Pardatschas-Granit     |
|15200202 | Parkinsoni-Schichten | Parkinsoni-Schichten     |
|15200487 | Parkinsonioolith-Subformation | Parkinsonioolith-Subformation     |
|15203307 | Parnegl-Formation | Parnegl-Formation     |
|15204050 | Partnach-Formation | Partnach-Formation     |
|15203482 | Passo-di-Cristallina-Zone | Passo-di-Cristallina-Zone     |
|15200673 | Passwang- bis Ifenthal-Formation, undifferenziert | Passwang- bis Ifenthal-Formation, undifferenziert     |
|15200009 | Passwang-Formation | Passwang-Formation     |
|15200195 | Pecten-Bank | Pecten-Bank     |
|15206040 | Pegmatit | Pegmatit     |
|15202439 | Pereyres-Formation | Pereyres-Formation     |
|15206001 | Periadriatische Vulkanite | Periadriatische Vulkanite     |
|15206096 | Peridotit, undifferenziert | Peridotit, undifferenziert     |
|15203472 | Perm der Maggia-Decke | Perm der Maggia-Decke     |
|15202504 | Perm der Tavetsch-Decke (Val Acla Mulin) | Perm der Tavetsch-Decke (Val Acla Mulin)     |
|15203386 | Perm der Zone-Houillère | Perm der Zone-Houillère     |
|15203389 | Perm der Zone-Houillère, konglomeratisch | Perm der Zone-Houillère, konglomeratisch     |
|15203387 | Perm der Zone-Houillère, quarzschiefrig | Perm der Zone-Houillère, quarzschiefrig     |
|15206100 | Perm, undifferenziert | Perm, undifferenziert     |
|15202255 | Permisch verwittertes Kristallin | Permisch verwittertes Kristallin     |
|15202254 | Permische Sedimente der Ilanz-Zone | Permische Sedimente der Ilanz-Zone     |
|15205065 | Permische Vulkanite | Permische Vulkanite     |
|15203471 | Permo-Karbon der Maggia-Decke | Permo-Karbon der Maggia-Decke     |
|15200221 | Permo-Karbon der Nordschweiz | Permo-Karbon der Nordschweiz     |
|15203406 | Permo-Karbon der Ruitor-Decke | Permo-Karbon der Ruitor-Decke     |
|15203407 | Permo-Karbon der Ruitor-Decke, konglomeratisch | Permo-Karbon der Ruitor-Decke, konglomeratisch     |
|15202266 | Permo-Karbon der Urseren-Garvera-Zone | Permo-Karbon der Urseren-Garvera-Zone     |
|15202465 | Permo-Karbon des Aiguilles-Rouges-Massivs | Permo-Karbon des Aiguilles-Rouges-Massivs     |
|15202142 | Permo-Karbon des Helvetikums | Permo-Karbon des Helvetikums     |
|15204128 | Permo-Karbon des Ostalpins | Permo-Karbon des Ostalpins     |
|15205077 | Permo-Karbon des Südalpins | Permo-Karbon des Südalpins     |
|15206103 | Permokarbon, undifferenziert | Permokarbon, undifferenziert     |
|15203141 | Perrières-Formation | Perrières-Formation     |
|15202214 | Perrons-Orthogneis | Perrons-Orthogneis     |
|15203545 | Personico-Gneis | Personico-Gneis     |
|15200149 | Perte-du-Rhône-Formation | Perte-du-Rhône-Formation     |
|15203481 | Pertusio-Zone | Pertusio-Zone     |
|15200571 | Péry-Geröllsande | Péry-Geröllsande     |
|15202220 | Pesciora-Gruppe | Pesciora-Gruppe     |
|15203052 | Petit-Liençon-Formation | Petit-Liençon-Formation     |
|15202219 | Pétoudes-Orthogneis | Pétoudes-Orthogneis     |
|15200512 | Petrefaktenlager | Petrefaktenlager     |
|15203160 | Peula-Schichten | Peula-Schichten     |
|15203084 | Pfad-Mikrofazies | Pfad-Mikrofazies     |
|15200403 | Pfadflüe-Nagelfluh | Pfadflüe-Nagelfluh     |
|15200677 | Pfaffnau-Granit | Pfaffnau-Granit     |
|15200257 | Pfänder-Schichten | Pfänder-Schichten     |
|15200280 | Pfannenstiel-Schichten | Pfannenstiel-Schichten     |
|15203168 | Pfävigrat-Formation | Pfävigrat-Formation     |
|15200542 | Pfiffegg-Nagelfluh | Pfiffegg-Nagelfluh     |
|15200522 | Pfingstboden-Member | Pfingstboden-Member     |
|15204072 | Pflanzenquarzit | Pflanzenquarzit     |
|15203423 | Pfulwe-Metabasalt | Pfulwe-Metabasalt     |
|15203381 | Phengitgneis der Aul-Decke | Phengitgneis der Aul-Decke     |
|15206082 | Phyllit, undifferenziert | Phyllit, undifferenziert     |
|15206095 | Phyllitgneis, undifferenziert | Phyllitgneis, undifferenziert     |
|15203356 | Pianasciom-Kalkschiefer | Pianasciom-Kalkschiefer     |
|15203357 | Piano-delle-Creste-Sandstein | Piano-delle-Creste-Sandstein     |
|15200039 | Pichoux-Formation | Pichoux-Formation     |
|15203408 | Piémont-Glanzschiefer | Piémont-Glanzschiefer     |
|15203413 | Piémont-Ophiolith | Piémont-Ophiolith     |
|15203345 | Pierre-Avoi-Brekzie | Pierre-Avoi-Brekzie     |
|15203156 | Pierre-Avoi-Melange | Pierre-Avoi-Melange     |
|15200058 | Pierre-Blanche | Pierre-Blanche     |
|15200097 | Pierre-Châtel-, Vions- und Chambotte-Formation, undifferenziert | Pierre-Châtel-, Vions- und Chambotte-Formation, undifferenziert     |
|15200101 | Pierre-Châtel-Formation | Pierre-Châtel-Formation     |
|15200151 | Pierre Jaune de Neuchâtel | Pierre Jaune de Neuchâtel     |
|15202017 | Pierredar-Kalk | Pierredar-Kalk     |
|15203026 | Pissot-Member | Pissot-Member     |
|15202455 | Piz-Cuolmet-Gneiskomplex | Piz-Cuolmet-Gneiskomplex     |
|15203507 | Piz-del-Palo-Gneis | Piz-del-Palo-Gneis     |
|15204111 | Piz-Trovat-Metarhyolit | Piz-Trovat-Metarhyolit     |
|15205051 | Pizzella-Mergel | Pizzella-Mergel     |
|15203351 | Pizzo-Castello-Wildflysch | Pizzo-Castello-Wildflysch     |
|15205094 | Pizzo-Leone-Gneis | Pizzo-Leone-Gneis     |
|15203033 | Plagersflue-Kalkarenit | Plagersflue-Kalkarenit     |
|15202361 | Plaine-Morte-Melange | Plaine-Morte-Melange     |
|15203060 | Plan-Falcon-Formation | Plan-Falcon-Formation     |
|15202435 | Planière-Member | Planière-Member     |
|15203146 | Planken-Formation | Planken-Formation     |
|15203145 | Planknerbrücke-Formation | Planknerbrücke-Formation     |
|15202304 | Planplatte-Eisenoolith | Planplatte-Eisenoolith     |
|15204085 | Plasseggen-Augengneis | Plasseggen-Augengneis     |
|15203224 | Plattamala-Granit | Plattamala-Granit     |
|15204008 | Plattas-Member | Plattas-Member     |
|15202602 | Plattazüg-Formation | Plattazüg-Formation     |
|15200146 | Plattensandstein | Plattensandstein     |
|15202058 | Plattenwald-Bank | Plattenwald-Bank     |
|15200218 | Playa-Serie | Playa-Serie     |
|15202203 | Plex-Aboyeu-Rhyodazit | Plex-Aboyeu-Rhyodazit     |
|15202519 | Pliensbachien-Spatkalk | Pliensbachien-Spatkalk     |
|15200444 | Poet-Bank | Poet-Bank     |
|15205087 | Pointe-d&#39;Otemma-Granodiorit | Pointe-d&#39;Otemma-Granodiorit     |
|15203264 | Pointe-de-l&#39;Au-Brekzie | Pointe-de-l&#39;Au-Brekzie     |
|15200390 | Polygene Nagelfluh | Polygene Nagelfluh     |
|15200436 | Poncin-Member | Poncin-Member     |
|15200667 | Pont-des-Pierres-Bank | Pont-des-Pierres-Bank     |
|15205009 | Pontegana-Konglomerat | Pontegana-Konglomerat     |
|15200440 | Ponthoud-Bank | Ponthoud-Bank     |
|15205137 | Pontida-Formation | Pontida-Formation     |
|15202236 | Pontino-Gneiskomplex | Pontino-Gneiskomplex     |
|15202207 | Pormenaz-Granit | Pormenaz-Granit     |
|15200370 | Porrentruy-Konglomerat | Porrentruy-Konglomerat     |
|15200026 | Porrentruy-Member | Porrentruy-Member     |
|15200576 | Posidonienschiefer-Formation | Posidonienschiefer-Formation     |
|15204103 | Postvariszische Diabasgänge | Postvariszische Diabasgänge     |
|15200243 | Prä- und frühvariszische Sedimente und Vulkanite der Nordschweiz | Prä- und frühvariszische Sedimente und Vulkanite der Nordschweiz     |
|15202357 | Prä- und Frühvariszische Sedimente und Vulkanite des Aiguilles-Rouges-Massivs | Prä- und Frühvariszische Sedimente und Vulkanite des Aiguilles-Rouges-Massivs     |
|15203029 | Pra-du-Pont-Hartgrund | Pra-du-Pont-Hartgrund     |
|15204036 | Pra-Grata-Member | Pra-Grata-Member     |
|15204078 | Präbichl-Formation | Präbichl-Formation     |
|15203277 | Pralet-Formation | Pralet-Formation     |
|15205114 | Prasinit der Arolla-Gruppe | Prasinit der Arolla-Gruppe     |
|15203468 | Prasinit der Métailler-Formation | Prasinit der Métailler-Formation     |
|15206041 | Prasinit, undifferenziert | Prasinit, undifferenziert     |
|15202347 | Prato-Gneis | Prato-Gneis     |
|15203162 | Prättigau-Schiefer | Prättigau-Schiefer     |
|15200253 | Prävariszische Grüngesteine der Nordschweiz | Prävariszische Grüngesteine der Nordschweiz     |
|15204137 | prävariszische Grüngesteine des Ostalpins | prävariszische Grüngesteine des Ostalpins     |
|15205130 | Prävariszische Metaarkose, Orthogneise | Prävariszische Metaarkose, Orthogneise     |
|15205081 | Prävariszische Metasedimente des Südalpins | Prävariszische Metasedimente des Südalpins     |
|15200250 | Prävariszische Migmatite der Nordschweiz | Prävariszische Migmatite der Nordschweiz     |
|15200246 | Prävariszische Orthogneise der Nordschweiz | Prävariszische Orthogneise der Nordschweiz     |
|15204135 | prävariszische Orthogneise des Ostalpins | prävariszische Orthogneise des Ostalpins     |
|15205136 | Prävariszische Orthogneise des Südalpins | Prävariszische Orthogneise des Südalpins     |
|15204136 | prävariszische Paragneise des Ostalpins | prävariszische Paragneise des Ostalpins     |
|15203475 | Prävariszisches Grundgebirge der Maggia-Decke | Prävariszisches Grundgebirge der Maggia-Decke     |
|15205129 | Prävariszisches Grundgebirge der Margna-Sella | Prävariszisches Grundgebirge der Margna-Sella     |
|15203461 | Prävariszisches Grundgebirge des Briançonnais | Prävariszisches Grundgebirge des Briançonnais     |
|15202340 | Prävariszisches polyzyklisches Grundgebirge der Gotthardt-Decke | Prävariszisches polyzyklisches Grundgebirge der Gotthardt-Decke     |
|15200245 | Prävariszisches polyzyklisches Grundgebirge der Nordschweiz | Prävariszisches polyzyklisches Grundgebirge der Nordschweiz     |
|15202355 | Prävariszisches polyzyklisches Grundgebirge der Tavetsch-Decke | Prävariszisches polyzyklisches Grundgebirge der Tavetsch-Decke     |
|15202194 | Prävariszisches polyzyklisches Grundgebirge des Aar-Massivs | Prävariszisches polyzyklisches Grundgebirge des Aar-Massivs     |
|15202334 | Prävariszisches polyzyklisches Grundgebirge des Aiguilles-Rouges-Massivs | Prävariszisches polyzyklisches Grundgebirge des Aiguilles-Rouges-Massivs     |
|15202468 | Prävariszisches polyzyklisches Grundgebirge des Helvetikums | Prävariszisches polyzyklisches Grundgebirge des Helvetikums     |
|15202337 | Prävariszisches polyzyklisches Grundgebirge des Mont-Blanc-Massivs | Prävariszisches polyzyklisches Grundgebirge des Mont-Blanc-Massivs     |
|15204119 | prävariszisches polyzyklisches Grundgebirge des Ostalpins | prävariszisches polyzyklisches Grundgebirge des Ostalpins     |
|15206110 | Prävariszisches, polyzyklisches Grundgebirge, undifferenziert | Prävariszisches, polyzyklisches Grundgebirge, undifferenziert     |
|15202440 | Praz-Couquain-Formation | Praz-Couquain-Formation     |
|15203289 | Praz-Serie | Praz-Serie     |
|15203436 | Preja-Formation | Preja-Formation     |
|15205022 | Prella-Konglomerat | Prella-Konglomerat     |
|15205014 | Prestino-Pelite | Prestino-Pelite     |
|15202601 | Prodkamm- bis Sexmor-Formation, undifferenziert | Prodkamm- bis Sexmor-Formation, undifferenziert     |
|15202131 | Prodkamm-Formation | Prodkamm-Formation     |
|15202390 | Prodkamm-Formation, Mittlerer Teil | Prodkamm-Formation, Mittlerer Teil     |
|15202389 | Prodkamm-Formation, Oberer Teil | Prodkamm-Formation, Oberer Teil     |
|15202391 | Prodkamm-Formation, Unterer Teil | Prodkamm-Formation, Unterer Teil     |
|15202271 | Prosa-Granit | Prosa-Granit     |
|15204053 | Prosanto-Formation | Prosanto-Formation     |
|15205085 | Proterozoische und paläozoische Mafite und Ultramafite des Südalpins | Proterozoische und paläozoische Mafite und Ultramafite des Südalpins     |
|15202239 | Prüsfa-Gneiskomplex | Prüsfa-Gneiskomplex     |
|15200582 | Psilonotenton-Formation | Psilonotenton-Formation     |
|15202456 | Pulanera-Gneiskomplex | Pulanera-Gneiskomplex     |
|15204071 | Punt-la-Drossa-Member | Punt-la-Drossa-Member     |
|15203371 | Punta-Rossa-Komplex | Punta-Rossa-Komplex     |
|15202184 | Punteglias-Granit | Punteglias-Granit     |
|15202085 | Pygurus-Member | Pygurus-Member     |
|15202136 | Quarten-Formation | Quarten-Formation     |
|15206038 | Quarzgang | Quarzgang     |
|15205105 | Quarzit der Dolin-Gruppe | Quarzit der Dolin-Gruppe     |
|15203404 | Quarzit der Nordpenninische Trias | Quarzit der Nordpenninische Trias     |
|15203419 | Quarzit der Zermatt-Saas-Decke | Quarzit der Zermatt-Saas-Decke     |
|15206062 | Quarzit, undifferenziert | Quarzit, undifferenziert     |
|15200432 | Quarzitnagelfluh (der St.-Gallen-Fm.) | Quarzitnagelfluh (der St.-Gallen-Fm.)     |
|15206083 | Quarzphyllit, undifferenziert | Quarzphyllit, undifferenziert     |
|15203212 | Quarzsandstein-Flysch (Gault) | Quarzsandstein-Flysch (Gault)     |
|15206117 | Quarzsandstein, undiff. | Quarzsandstein, undiff.     |
|15204034 | Quattervals-Formation | Quattervals-Formation     |
|15202097 | Quinten-Formation | Quinten-Formation     |
|15203137 | Radiolarit | Radiolarit     |
|15203235 | Radiolarit der Arosa-Zone | Radiolarit der Arosa-Zone     |
|15206107 | Radiolarit, undifferenziert | Radiolarit, undifferenziert     |
|15200325 | Radiolaritreiche Nagelfluh | Radiolaritreiche Nagelfluh     |
|15202083 | Rahberg-Bank | Rahberg-Bank     |
|15204149 | Raibl-Gr.: Dolomit | Raibl-Gr.: Dolomit     |
|15204038 | Raibl-Gruppe | Raibl-Gruppe     |
|15204151 | Raibl-Gruppe der Zentralschweizer Klippen | Raibl-Gruppe der Zentralschweizer Klippen     |
|15200371 | Raitsche | Raitsche     |
|15204027 | Ramoz-Member | Ramoz-Member     |
|15200505 | Ramschwag-Nagelfluh | Ramschwag-Nagelfluh     |
|15203070 | Rämsi-Member | Rämsi-Member     |
|15203185 | Randa-Augengneis | Randa-Augengneis     |
|15200570 | Randen-Grobkalk | Randen-Grobkalk     |
|15200398 | Randen-Juranagelfluh | Randen-Juranagelfluh     |
|15200235 | Randgranit | Randgranit     |
|15202063 | Rankweil-Member | Rankweil-Member     |
|15203309 | Raschil-Formation | Raschil-Formation     |
|15202418 | Rauwacke (Röti-Fm.) | Rauwacke (Röti-Fm.)     |
|15203243 | Rauwacke der Brekzien-Decke | Rauwacke der Brekzien-Decke     |
|15205104 | Rauwacke der Dolin-Gruppe | Rauwacke der Dolin-Gruppe     |
|15202547 | Rauwacke der Helvetische Trias | Rauwacke der Helvetische Trias     |
|15203571 | Rauwacke der Klippen-Decke | Rauwacke der Klippen-Decke     |
|15204146 | Rauwacke der Raibl-Gruppe | Rauwacke der Raibl-Gruppe     |
|15203575 | Rauwacke und Quarzsandstein der Klippen-Decke (basale Trias) | Rauwacke und Quarzsandstein der Klippen-Decke (basale Trias)     |
|15206022 | Rauwacke, undifferenziert | Rauwacke, undifferenziert     |
|15204061 | Ravais-ch-Member | Ravais-ch-Member     |
|15203011 | Raverette-Member | Raverette-Member     |
|15202074 | Rawil-Member | Rawil-Member     |
|15203025 | Rayes-Kalk | Rayes-Kalk     |
|15200400 | Rebhubel-Schichten | Rebhubel-Schichten     |
|15203509 | Rebi-Gneis | Rebi-Gneis     |
|15204069 | Reichenhall-Formation | Reichenhall-Formation     |
|15203125 | Reidigen-Formation | Reidigen-Formation     |
|15204062 | Reifling-Formation | Reifling-Formation     |
|15202108 | Reischiben-Formation | Reischiben-Formation     |
|15203147 | Reiselsberg-Formation | Reiselsberg-Formation     |
|15200042 | Renggeri-Member | Renggeri-Member     |
|15203556 | Renten-Gneis | Renten-Gneis     |
|15200002 | Reuchenette-Formation | Reuchenette-Formation     |
|15203336 | Rhät der Brekzien-Decke | Rhät der Brekzien-Decke     |
|15203142 | Rhenodanubischer Flysch | Rhenodanubischer Flysch     |
|15206045 | Rhétien, undifferenziert | Rhétien, undifferenziert     |
|15200145 | Rhötton | Rhötton     |
|15206035 | Rhyolit, undifferenziert | Rhyolit, undifferenziert     |
|15203362 | Ri-d&#39;Antabia-Konglomerat | Ri-d&#39;Antabia-Konglomerat     |
|15203388 | Ricard-Rhyolit | Ricard-Rhyolit     |
|15200077 | Rickenbach-Member | Rickenbach-Member     |
|15202373 | Riein-Schichten | Riein-Schichten     |
|15200359 | Rietbad-Subformation | Rietbad-Subformation     |
|15200075 | Rietheim-Member | Rietheim-Member     |
|15203420 | Riffelberg-Melange | Riffelberg-Melange     |
|15204147 | Rifffazies der Arlberg-Formation | Rifffazies der Arlberg-Formation     |
|15200322 | Rigi-Formation | Rigi-Formation     |
|15203085 | Rindenkorn-Mikrofazies | Rindenkorn-Mikrofazies     |
|15203327 | Rinderbach-Formation | Rinderbach-Formation     |
|15202489 | Rinderbiel-Mikrogranit | Rinderbiel-Mikrogranit     |
|15202537 | Ringgenberg-Schichten | Ringgenberg-Schichten     |
|15205017 | Rio-dei-Gioghi-Pelite | Rio-dei-Gioghi-Pelite     |
|15202431 | Riondouneire-Member | Riondouneire-Member     |
|15203322 | Ritter-Gneis | Ritter-Gneis     |
|15205049 | Riva-di-Solto-Tonstein | Riva-di-Solto-Tonstein     |
|15200094 | Rivière-Member | Rivière-Member     |
|15203350 | Robiei-Wildflysch | Robiei-Wildflysch     |
|15202393 | Roc-Champion-Konglomerat | Roc-Champion-Konglomerat     |
|15200650 | Rocher-des-Hirondelles-Formation | Rocher-des-Hirondelles-Formation     |
|15206047 | Rodingit | Rodingit     |
|15203128 | Rodomonts-Formation | Rodomonts-Formation     |
|15203037 | Rodosex-Member | Rodosex-Member     |
|15203330 | Roffna-Gneis | Roffna-Gneis     |
|15202310 | Roggenegg-Komplex | Roggenegg-Komplex     |
|15203540 | Rognoi-Gneis | Rognoi-Gneis     |
|15202072 | Rohrbachstein-Bank | Rohrbachstein-Bank     |
|15205123 | Roisan-Marmor | Roisan-Marmor     |
|15205003 | Roisan-Zone | Roisan-Zone     |
|15203329 | Rombach-Formation | Rombach-Formation     |
|15203030 | Rontins-Member | Rontins-Member     |
|15200031 | Röschenz-Member | Röschenz-Member     |
|15202046 | Rosenlaui-Marmor | Rosenlaui-Marmor     |
|15202487 | Rossbodenstock-Diorit | Rossbodenstock-Diorit     |
|15200640 | Rossemaison-Formation | Rossemaison-Formation     |
|15203519 | Rossi-Formation | Rossi-Formation     |
|15203047 | Rossinière-Formation | Rossinière-Formation     |
|15205034 | Rosso ad Aptici | Rosso ad Aptici     |
|15205036 | Rosso Ammonitico Lombardo | Rosso Ammonitico Lombardo     |
|15202378 | Rossplatten-Diorit | Rossplatten-Diorit     |
|15202499 | Rotberg-Sandstein | Rotberg-Sandstein     |
|15203027 | Rote-Platte-Formation | Rote-Platte-Formation     |
|15203023 | Roter-Sattel-Hartgrund | Roter-Sattel-Hartgrund     |
|15200064 | Rothenfluh-Member | Rothenfluh-Member     |
|15202139 | Röti-Formation | Röti-Formation     |
|15202183 | Rötifirn-Gruppe | Rötifirn-Gruppe     |
|15202221 | Rotondo-Granit | Rotondo-Granit     |
|15203441 | Rottal-Migmatit | Rottal-Migmatit     |
|15203490 | Roz-Schiefer | Roz-Schiefer     |
|15203092 | Rubli-Member | Rubli-Member     |
|15203163 | Ruchberg-Formation | Ruchberg-Formation     |
|15203304 | Rudnal-Formation | Rudnal-Formation     |
|15202356 | Rueras-Gneiskomplex | Rueras-Gneiskomplex     |
|15202314 | Ruestel-Flysch | Ruestel-Flysch     |
|15204009 | Ruhpolding-Formation | Ruhpolding-Formation     |
|15204079 | Ruina-Formation | Ruina-Formation     |
|15202376 | Ruinas-Sandstein | Ruinas-Sandstein     |
|15202372 | Runcaleida-Schichten | Runcaleida-Schichten     |
|15203297 | Ruscada-Gneis | Ruscada-Gneis     |
|15202010 | Rüschenweid-Bank | Rüschenweid-Bank     |
|15202181 | Russein-Diorit | Russein-Diorit     |
|15204005 | Russenna-Formation | Russenna-Formation     |
|15200095 | Russille-Member | Russille-Member     |
|15202297 | Rütenen-Konglomerat | Rütenen-Konglomerat     |
|15200541 | Rütiberg-Kalksandstein | Rütiberg-Kalksandstein     |
|15200283 | Rütschlibach-Riedhof-Süsswasserkalk | Rütschlibach-Riedhof-Süsswasserkalk     |
|15204059 | S-charl-Formation | S-charl-Formation     |
|15200214 | Saalhof-Bank | Saalhof-Bank     |
|15203450 | Saas-Fee-Augengneis | Saas-Fee-Augengneis     |
|15203319 | Sabbione-Sandstein | Sabbione-Sandstein     |
|15200225 | Säckingen-Granit | Säckingen-Granit     |
|15200404 | Sädel-Kalknagelfluh | Sädel-Kalknagelfluh     |
|15202223 | Sädelhorn-Diorit | Sädelhorn-Diorit     |
|15200313 | Safenwil-Muschelsandstein | Safenwil-Muschelsandstein     |
|15203175 | Safien-Kalk | Safien-Kalk     |
|15202444 | Saix-Member | Saix-Member     |
|15203533 | Salahorn-Fm.: Metaplutonit | Salahorn-Fm.: Metaplutonit     |
|15203534 | Salahorn-Fm.: Paragneis | Salahorn-Fm.: Paragneis     |
|15204014 | Salamun-Brekzie | Salamun-Brekzie     |
|15203432 | Salarioli-Serie | Salarioli-Serie     |
|15206019 | Salleren-Brekzie | Salleren-Brekzie     |
|15204013 | Salteras-Formation | Salteras-Formation     |
|15205042 | Saltrio-Formation | Saltrio-Formation     |
|15204011 | Saluver-Formation | Saluver-Formation     |
|15204010 | Saluver-Gruppe | Saluver-Gruppe     |
|15202155 | Salvan-Member | Salvan-Member     |
|15200137 | Salzlager | Salzlager     |
|15205080 | San-Bernardo-Gneis | San-Bernardo-Gneis     |
|15206015 | San-Fedelino-Granit | San-Fedelino-Granit     |
|15205058 | San-Giorgio-Dolomit | San-Giorgio-Dolomit     |
|15205061 | San-Salvatore-Dolomit | San-Salvatore-Dolomit     |
|15203217 | Sanalada-Formation | Sanalada-Formation     |
|15202506 | Sandalp-Rhyolith | Sandalp-Rhyolith     |
|15204080 | Sandhubel-Member | Sandhubel-Member     |
|15202392 | Sandpass-Formation | Sandpass-Formation     |
|15206105 | Sandstein, undifferenziert | Sandstein, undifferenziert     |
|15202016 | Sanetsch-Formation | Sanetsch-Formation     |
|15202280 | Sardona-Melange | Sardona-Melange     |
|15202283 | Sardona-Quarzit | Sardona-Quarzit     |
|15204112 | Sass-Queder-Metarhyolith | Sass-Queder-Metarhyolith     |
|15205091 | Sassa-Metagabbro | Sassa-Metagabbro     |
|15203169 | Sassauna-Formation | Sassauna-Formation     |
|15202343 | Sassina-Augengneis | Sassina-Augengneis     |
|15202238 | Sasso-Rosso-Gneiskomplex | Sasso-Rosso-Gneiskomplex     |
|15204125 | Sasso-Rosso-Granodiorit | Sasso-Rosso-Granodiorit     |
|15200050 | Saulcy-Member | Saulcy-Member     |
|15202247 | Saure vulkanische und subvulkanische Gesteine | Saure vulkanische und subvulkanische Gesteine     |
|15206048 | Saurer Gang | Saurer Gang     |
|15203305 | Savognin-Formation | Savognin-Formation     |
|15205030 | Scaglia Bianca Lombarda | Scaglia Bianca Lombarda     |
|15205029 | Scaglia Rossa Lombarda | Scaglia Rossa Lombarda     |
|15205031 | Scaglia Variegata Lombarda | Scaglia Variegata Lombarda     |
|15202511 | Schabell-Mélange | Schabell-Mélange     |
|15200676 | Schafisheim-Syenit | Schafisheim-Syenit     |
|15200497 | Schallenberg-Member | Schallenberg-Member     |
|15200089 | Schambelen-Member | Schambelen-Member     |
|15202035 | Scharti-Member | Scharti-Member     |
|15202539 | Schattwald-Mergelkalk | Schattwald-Mergelkalk     |
|15202315 | Scheidegg-Flysch | Scheidegg-Flysch     |
|15200323 | Scheidegg-Nagelfluh | Scheidegg-Nagelfluh     |
|15200045 | Schellenbrücke-Bank | Schellenbrücke-Bank     |
|15200051 | Schelmenloch-Member | Schelmenloch-Member     |
|15203394 | Scherbadung-Gabbro | Scherbadung-Gabbro     |
|15200421 | Scherli-Quarzitnagelfluh | Scherli-Quarzitnagelfluh     |
|15204028 | Schesaplana-Member | Schesaplana-Member     |
|15203434 | Schiefer der Ruginenta-Decke | Schiefer der Ruginenta-Decke     |
|15200244 | Schiefer und Grauwacken | Schiefer und Grauwacken     |
|15206111 | Schiefer, undifferenziert | Schiefer, undifferenziert     |
|15202450 | Schiefriger Mines-Lias | Schiefriger Mines-Lias     |
|15202100 | Schilt-Formation | Schilt-Formation     |
|15202025 | Schimberg-Member | Schimberg-Member     |
|15200130 | Schinznach-Formation | Schinznach-Formation     |
|15203012 | Schistes à Miches | Schistes à Miches     |
|15200357 | Schistes marno-micacés | Schistes marno-micacés     |
|15203397 | Schistes noirs (Pierre Avoi) | Schistes noirs (Pierre Avoi)     |
|15200465 | Schlächtenhaus-Granit | Schlächtenhaus-Granit     |
|15200682 | Schlächtenhaus-Schiefer | Schlächtenhaus-Schiefer     |
|15200088 | Schleitheim-Bank | Schleitheim-Bank     |
|15203117 | Schlieren-Flysch | Schlieren-Flysch     |
|15203576 | Schlieren-Flysch: Hauptmasse (Paläogen) | Schlieren-Flysch: Hauptmasse (Paläogen)     |
|15203118 | Schlieren-Sandstein | Schlieren-Sandstein     |
|15203573 | Schlieren-Sandstein, im Paläogen tektonisch überprägt | Schlieren-Sandstein, im Paläogen tektonisch überprägt     |
|15203153 | Schloss-Formation | Schloss-Formation     |
|15200224 | Schluchsee-Granit | Schluchsee-Granit     |
|15202379 | Schöllenen-Diorit | Schöllenen-Diorit     |
|15200237 | Schönau-Herrenschwand-Granit | Schönau-Herrenschwand-Granit     |
|15202145 | Schönbüel-Formation | Schönbüel-Formation     |
|15202146 | Schönbüel-Quarzit | Schönbüel-Quarzit     |
|15203119 | Schoni-Sandstein | Schoni-Sandstein     |
|15202073 | Schrattenkalk-Formation | Schrattenkalk-Formation     |
|15202590 | Schrattenkalk-Formation, vermergelt | Schrattenkalk-Formation, vermergelt     |
|15200261 | Schüpferegg-Nagelfluh | Schüpferegg-Nagelfluh     |
|15202544 | Schwalmern-Kalk | Schwalmern-Kalk     |
|15202543 | Schwalmern-Schiefer | Schwalmern-Schiefer     |
|15200533 | Schwändibach-Naglelfuh | Schwändibach-Naglelfuh     |
|15200641 | Schwaningen-Merenbach-Rhyolith | Schwaningen-Merenbach-Rhyolith     |
|15200642 | Schwaningen-Weizen-Granit | Schwaningen-Weizen-Granit     |
|15200658 | Schwarzbach-Schichten | Schwarzbach-Schichten     |
|15202114 | Schwarzhorn-Member | Schwarzhorn-Member     |
|15200441 | Scie-Besse-Sandstein | Scie-Besse-Sandstein     |
|15203038 | Sciernes-d&#39;Albeuve-Formation | Sciernes-d&#39;Albeuve-Formation     |
|15203363 | Scisti bruni (Lebendun) | Scisti bruni (Lebendun)     |
|15206054 | Sedimentäre Brekzie, undifferenziert | Sedimentäre Brekzie, undifferenziert     |
|15206030 | Sedimentgestein, undifferenziert | Sedimentgestein, undifferenziert     |
|15200227 | Seeablagerungen | Seeablagerungen     |
|15200206 | Seebi-Member | Seebi-Member     |
|15200506 | Seerücken-Tuffit | Seerücken-Tuffit     |
|15202050 | Seewen-Formation | Seewen-Formation     |
|15202500 | Seez-Member | Seez-Member     |
|15202104 | Seeztal-Member | Seeztal-Member     |
|15200498 | Seli-Nagelfluh | Seli-Nagelfluh     |
|15205125 | Sella-Granodiorit | Sella-Granodiorit     |
|15202057 | Sellamatt-Schichten | Sellamatt-Schichten     |
|15202053 | Selun-Member | Selun-Member     |
|15200418 | Sense-Formation | Sense-Formation     |
|15200363 | Septarienton | Septarienton     |
|15202312 | Serhalten-Flysch | Serhalten-Flysch     |
|15203369 | Série conglomératique (Pierre Avoi) | Série conglomératique (Pierre Avoi)     |
|15200552 | Serie der Süsswasserkalke und Dolomite | Serie der Süsswasserkalke und Dolomite     |
|15203181 | Série du Tounô | Série du Tounô     |
|15203226 | Série Grise | Série Grise     |
|15203225 | Série Rousse | Série Rousse     |
|15203391 | Série schisteuse moyenne | Série schisteuse moyenne     |
|15203390 | Série schisto-gréseuse supérieure | Série schisto-gréseuse supérieure     |
|15203368 | Série schisto-quartzitique (Pierre Avoi) | Série schisto-quartzitique (Pierre Avoi)     |
|15203003 | Seron-Formation | Seron-Formation     |
|15203522 | Seron-Formation, Calcschistes zoogènes | Seron-Formation, Calcschistes zoogènes     |
|15203523 | Seron-Formation, Conglomérat moyen | Seron-Formation, Conglomérat moyen     |
|15206042 | Serpentinit, undifferenziert | Serpentinit, undifferenziert     |
|15200663 | Serrières-Bank | Serrières-Bank     |
|15204060 | Sertig-Member | Sertig-Member     |
|15205063 | Servino | Servino     |
|15204107 | Sesvenna-Augengneis | Sesvenna-Augengneis     |
|15203360 | Sevinera-Marmor | Sevinera-Marmor     |
|15203361 | Sevinera-Sandstein | Sevinera-Sandstein     |
|15203266 | Sex-du-Tronc-Kalk | Sex-du-Tronc-Kalk     |
|15202447 | Sex-Mort-Flysch | Sex-Mort-Flysch     |
|15202125 | Sexmor-Formation | Sexmor-Formation     |
|15202404 | Sexmor-Formation, Oberer Teil | Sexmor-Formation, Oberer Teil     |
|15202405 | Sexmor-Formation, Unterer Teil | Sexmor-Formation, Unterer Teil     |
|15200679 | Siblingen-Granit | Siblingen-Granit     |
|15202088 | Sichel-Kalk | Sichel-Kalk     |
|15202042 | Siderolithikum (des Helvetikums) | Siderolithikum (des Helvetikums)     |
|15200091 | Siderolithikum des Juragebirges | Siderolithikum des Juragebirges     |
|15203337 | Siderolithisches Dogger der Klippen-Decke | Siderolithisches Dogger der Klippen-Decke     |
|15203558 | Simano-D.: Amphibolit | Simano-D.: Amphibolit     |
|15203554 | Simano-D.: Dolomitmarmor | Simano-D.: Dolomitmarmor     |
|15203553 | Simano-D.: Kalkmarmor | Simano-D.: Kalkmarmor     |
|15203555 | Simano-D.: Paragneis | Simano-D.: Paragneis     |
|15203559 | Simano-D.: Ultramafitit | Simano-D.: Ultramafitit     |
|15203292 | Simmen-Flysch, undifferenziert | Simmen-Flysch, undifferenziert     |
|15200070 | Sissach-Member | Sissach-Member     |
|15203516 | Sivigia-Gneis | Sivigia-Gneis     |
|15202330 | Sogn-Placi-Gneiskomplex | Sogn-Placi-Gneiskomplex     |
|15203584 | Soladier- und Verdy-Member, undifferenziert | Soladier- und Verdy-Member, undifferenziert     |
|15203045 | Soladier-Member | Soladier-Member     |
|15203495 | Solis-Kalk | Solis-Kalk     |
|15200426 | Solothurner Schildkrötenkalk | Solothurner Schildkrötenkalk     |
|15203046 | Sommant-Formation | Sommant-Formation     |
|15200327 | Sommersberg-Nagelfluh | Sommersberg-Nagelfluh     |
|15202497 | Sonnenberg-Horizonte | Sonnenberg-Horizonte     |
|15202002 | Sörenberg-Melange | Sörenberg-Melange     |
|15202244 | Sorescia-Gneis | Sorescia-Gneis     |
|15206009 | Sorico-Tonalit | Sorico-Tonalit     |
|15200041 | Sornetan-Member | Sornetan-Member     |
|15203375 | Sosto-Schiefer | Sosto-Schiefer     |
|15203184 | Sous-le-Rocher-Member | Sous-le-Rocher-Member     |
|15200220 | Spät- bis postvariszische Intrusiva der Nordschweiz | Spät- bis postvariszische Intrusiva der Nordschweiz     |
|15202336 | Spät- bis postvariszische Intrusiva des Mont-Blanc-Massivs | Spät- bis postvariszische Intrusiva des Mont-Blanc-Massivs     |
|15202164 | Spät- bis postvariszische Sedimente und Vulkanite des Aar-Massivs | Spät- bis postvariszische Sedimente und Vulkanite des Aar-Massivs     |
|15202464 | Spät- bis postvariszische Sedimente und Vulkanite des Helvetikums | Spät- bis postvariszische Sedimente und Vulkanite des Helvetikums     |
|15200057 | Spatkalk | Spatkalk     |
|15203139 | Spatkalk (Tissota-Melange) | Spatkalk (Tissota-Melange)     |
|15200319 | Speer-Formation | Speer-Formation     |
|15203303 | Spegnas-Formation | Spegnas-Formation     |
|15202394 | Spirstock-Member | Spirstock-Member     |
|15203076 | Spis-Kalk | Spis-Kalk     |
|15202086 | Spitzern-Member | Spitzern-Member     |
|15202128 | Spitzmeilen-Formation | Spitzmeilen-Formation     |
|15202388 | Spitzmeilen-Formation, Basaler Teil | Spitzmeilen-Formation, Basaler Teil     |
|15202386 | Spitzmeilen-Formation, Oberer Teil | Spitzmeilen-Formation, Oberer Teil     |
|15202387 | Spitzmeilen-Formation, Unterer Teil | Spitzmeilen-Formation, Unterer Teil     |
|15204095 | Sprenkel-Schiefer | Sprenkel-Schiefer     |
|15200054 | St-Brais-Member | St-Brais-Member     |
|15203157 | St-Christophe-Schichten | St-Christophe-Schichten     |
|15200309 | St-Gallen-Formation | St-Gallen-Formation     |
|15203096 | St-Triphon-Formation | St-Triphon-Formation     |
|15200005 | St-Ursanne-Formation | St-Ursanne-Formation     |
|15200238 | St.-Blasien-Granit | St.-Blasien-Granit     |
|15205082 | Stabbiello-Gneis | Stabbiello-Gneis     |
|15202013 | Stad-Formation | Stad-Formation     |
|15202597 | Stad-Formation (e6) | Stad-Formation (e6)     |
|15202588 | Stad-Formation, «Jüngerer Quarzsandstein» | Stad-Formation, «Jüngerer Quarzsandstein»     |
|15200310 | Staffelbach-Grobsandstein | Staffelbach-Grobsandstein     |
|15200011 | Staffelegg-Formation | Staffelegg-Formation     |
|15200675 | Staffelegg-Formation und Opalinus-Ton, undifferenziert | Staffelegg-Formation und Opalinus-Ton, undifferenziert     |
|15203041 | Staldengraben-Formation | Staldengraben-Formation     |
|15200132 | Stamberg-Member | Stamberg-Member     |
|15203074 | Stanserhorn-Formation | Stanserhorn-Formation     |
|15203172 | Stätzerhorn-Gruppe | Stätzerhorn-Gruppe     |
|15200466 | Steinatal-Gneiskomplex | Steinatal-Gneiskomplex     |
|15202037 | Steinbach-Member | Steinbach-Member     |
|15203072 | Steinberg-Konglomerat | Steinberg-Konglomerat     |
|15200193 | Steinibach-Member | Steinibach-Member     |
|15203223 | Steinsberg-Kalk | Steinsberg-Kalk     |
|15203454 | Stellihorn-Mylonit | Stellihorn-Mylonit     |
|15202598 | Stgir- und Inferno-Formation, undifferenziert | Stgir- und Inferno-Formation, undifferenziert     |
|15202133 | Stgir-Formation | Stgir-Formation     |
|15202371 | Stgir-Formation, Oberer Teil | Stgir-Formation, Oberer Teil     |
|15202370 | Stgir-Formation, Unterer Teil | Stgir-Formation, Unterer Teil     |
|15200222 | Stockberg-Quarzporphyr | Stockberg-Quarzporphyr     |
|15203273 | Stockenflue-Kalk | Stockenflue-Kalk     |
|15202306 | Stöcki-Sandstein | Stöcki-Sandstein     |
|15202199 | Straligenstöckli-Gneiskomplex | Straligenstöckli-Gneiskomplex     |
|15206033 | Stratigraphische Einheit, undifferenziert | Stratigraphische Einheit, undifferenziert     |
|15202240 | Streifengneis-Komplex | Streifengneis-Komplex     |
|15202186 | Strem-Granit | Strem-Granit     |
|15200639 | Studweid-Formation | Studweid-Formation     |
|15204044 | Stugl-Member | Stugl-Member     |
|15202319 | Subalpiner Flysch | Subalpiner Flysch     |
|15200123 | Subfurcatum-Bank | Subfurcatum-Bank     |
|15203257 | Submédiane-Melange | Submédiane-Melange     |
|15203370 | Südegg-Komplex | Südegg-Komplex     |
|15202295 | Südelbach-Member | Südelbach-Member     |
|15202004 | Südhelvetische Flyscheinheiten | Südhelvetische Flyscheinheiten     |
|15202162 | Südwestlicher Aare-Granit | Südwestlicher Aare-Granit     |
|15200520 | Sulzbach-Member | Sulzbach-Member     |
|15200521 | Sulzbach-Nagelfluh | Sulzbach-Nagelfluh     |
|15203219 | Sulzfluh-Flysch | Sulzfluh-Flysch     |
|15203221 | Sulzfluh-Granit | Sulzfluh-Granit     |
|15203220 | Sulzfluh-Kalk | Sulzfluh-Kalk     |
|15203335 | Sulzgrabe-Formation | Sulzgrabe-Formation     |
|15202309 | Surbrunnen-Flysch | Surbrunnen-Flysch     |
|15202533 | Suren-Flysch | Suren-Flysch     |
|15206113 | Süsswasserkalk, undifferenziert | Süsswasserkalk, undifferenziert     |
|15206088 | Syenit, undifferenziert | Syenit, undifferenziert     |
|15200584 | Tabalcon-Kalk | Tabalcon-Kalk     |
|15202443 | Taffon-Member | Taffon-Member     |
|15206060 | Talkschiefer, undifferenziert | Talkschiefer, undifferenziert     |
|15203352 | Tamier-Zött-Wildflysch | Tamier-Zött-Wildflysch     |
|15202570 | Tamina-Gneiskomplex | Tamina-Gneiskomplex     |
|15202572 | Tamina-Gneiskomplex: mylonitisch | Tamina-Gneiskomplex: mylonitisch     |
|15202571 | Tamina-Gneiskomplex: schiefriger Biotitgneis | Tamina-Gneiskomplex: schiefriger Biotitgneis     |
|15200256 | Tannenberg-Schichten | Tannenberg-Schichten     |
|15200495 | Tannenwald-Schichten | Tannenwald-Schichten     |
|15203506 | Tasna-Altkristallin | Tasna-Altkristallin     |
|15203222 | Tasna-Flysch | Tasna-Flysch     |
|15203333 | Taspegn-Gneis | Taspegn-Gneis     |
|15202011 | Taveyannaz-Formation | Taveyannaz-Formation     |
|15202512 | Taveyannaz-Sandstein, Dachschiefer vorherrschend | Taveyannaz-Sandstein, Dachschiefer vorherrschend     |
|15203354 | Teggiolo-Kalkschiefer | Teggiolo-Kalkschiefer     |
|15206017 | Tektonische Brekzie, undifferenziert | Tektonische Brekzie, undifferenziert     |
|15206114 | Tektonisches Melange | Tektonisches Melange     |
|15202594 | Tektonisches Melange der Internen Einsiedeln-Schuppen | Tektonisches Melange der Internen Einsiedeln-Schuppen     |
|15202453 | Tektonisierte Basis des Glarner-Verrucano | Tektonisierte Basis des Glarner-Verrucano     |
|15206089 | Tektonit, undifferenziert | Tektonit, undifferenziert     |
|15202526 | Telltistock-Granit | Telltistock-Granit     |
|15202233 | Tenelin-Gneiskomplex | Tenelin-Gneiskomplex     |
|15200568 | Tenniken-Muschelagglomerat | Tenniken-Muschelagglomerat     |
|15202366 | Termen-Kalkschiefer | Termen-Kalkschiefer     |
|15202365 | Termen-Tonschiefer | Termen-Tonschiefer     |
|15205020 | Ternate-Formation | Ternate-Formation     |
|15203349 | Terri-Schiefer | Terri-Schiefer     |
|15203373 | Terri-Schiefer_Basale | Terri-Schiefer_Basale     |
|15205071 | Tertiär des Südalpins | Tertiär des Südalpins     |
|15205089 | Tête-de-Valpelline-Phyllit | Tête-de-Valpelline-Phyllit     |
|15200320 | Thun-Formation | Thun-Formation     |
|15203195 | Thyon-Metagranophyr | Thyon-Metagranophyr     |
|15204055 | Tiaun-Brekzie | Tiaun-Brekzie     |
|15202026 | Tierberg-Member | Tierberg-Member     |
|15202129 | Tierces-Formation | Tierces-Formation     |
|15200033 | Tiergarten-Member | Tiergarten-Member     |
|15202075 | Tierwis-Formation | Tierwis-Formation     |
|15200551 | Tillerée-Schichten | Tillerée-Schichten     |
|15203340 | Timun-Komplex | Timun-Komplex     |
|15203130 | Tissota-Melange | Tissota-Melange     |
|15202516 | Toarcienschiefer | Toarcienschiefer     |
|15202517 | Toarcienspatkalk | Toarcienspatkalk     |
|15202185 | Tödi-Granit | Tödi-Granit     |
|15200247 | Todtmoos-Horbach-Gneiskomplex | Todtmoos-Horbach-Gneiskomplex     |
|15203180 | Tomül-Mélange | Tomül-Mélange     |
|15204144 | Tonale-Schiefer | Tonale-Schiefer     |
|15206087 | Tonalit, undifferenziert | Tonalit, undifferenziert     |
|15203582 | Toniger Kalkschiefer der Grava-Decke | Toniger Kalkschiefer der Grava-Decke     |
|15206106 | Tonschiefer, undifferenziert | Tonschiefer, undifferenziert     |
|15203312 | Törbel-Gneis | Törbel-Gneis     |
|15205026 | Torre-Konglomerat | Torre-Konglomerat     |
|15203417 | Torrembey-Brekzie | Torrembey-Brekzie     |
|15203040 | Torrent-de-Lessoc-Formation | Torrent-de-Lessoc-Formation     |
|15202124 | Torrentalp-Member | Torrentalp-Member     |
|15202320 | Torrenthorn-Formation | Torrenthorn-Formation     |
|15200270 | Tösswald-Schichten | Tösswald-Schichten     |
|15203493 | Totalp-Serpentinit | Totalp-Serpentinit     |
|15200080 | Trasadingen-Bank | Trasadingen-Bank     |
|15202235 | Tremola-Gneiskomplex | Tremola-Gneiskomplex     |
|15205047 | Tremona-Formation | Tremona-Formation     |
|15203293 | Trepsen-Flysch | Trepsen-Flysch     |
|15203109 | Trias der Brekzien-Decke | Trias der Brekzien-Decke     |
|15203583 | Trias der Grava-Decke, undifferenziert | Trias der Grava-Decke, undifferenziert     |
|15203276 | Trias der Klippen-Decke | Trias der Klippen-Decke     |
|15203014 | Trias der Niesen-Decke | Trias der Niesen-Decke     |
|15202134 | Trias des Helvetikums | Trias des Helvetikums     |
|15200163 | Trias des Juragebirges | Trias des Juragebirges     |
|15204086 | Trias des Ostalpins | Trias des Ostalpins     |
|15205076 | Trias des Südalpins | Trias des Südalpins     |
|15206029 | Trias, undifferenziert | Trias, undifferenziert     |
|15203150 | Triesen-Formation | Triesen-Formation     |
|15202167 | Trift-Formation | Trift-Formation     |
|15203213 | Tristel-Formation | Tristel-Formation     |
|15204064 | Trochitendolomit-Member | Trochitendolomit-Member     |
|15200629 | Trois-Rods-Süsswasserkalk | Trois-Rods-Süsswasserkalk     |
|15200635 | Tröleten-Süsswasserkalk | Tröleten-Süsswasserkalk     |
|15203259 | Trom-Brekzie | Trom-Brekzie     |
|15202098 | Tros-Kalk | Tros-Kalk     |
|15203261 | Troublon-Kalk | Troublon-Kalk     |
|15203258 | Truche-Brekzie | Truche-Brekzie     |
|15204019 | Trupchun-Member | Trupchun-Member     |
|15203508 | Truzzo-Granit | Truzzo-Granit     |
|15202018 | Tsanfleuron-Member | Tsanfleuron-Member     |
|15202175 | Tscharren-Formation | Tscharren-Formation     |
|15203203 | Tschera-Marmor | Tschera-Marmor     |
|15204101 | Tschima-da-Flix-Granit | Tschima-da-Flix-Granit     |
|15200636 | Tschöplihof-Süsswasserkalk | Tschöplihof-Süsswasserkalk     |
|15204083 | Tschuggen-Augengneis | Tschuggen-Augengneis     |
|15202507 | Tuffitisches Member (Tscharren) | Tuffitisches Member (Tscharren)     |
|15200378 | Tüllingen-Süsswasserkalk | Tüllingen-Süsswasserkalk     |
|15203206 | Tumpriv-Gruppe | Tumpriv-Gruppe     |
|15204076 | Tuors-Member | Tuors-Member     |
|15204057 | Turettas-Member | Turettas-Member     |
|15200569 | Turritellen-Kalk | Turritellen-Kalk     |
|15200001 | Twannbach-Formation | Twannbach-Formation     |
|15202061 | Twäriberg-Bank | Twäriberg-Bank     |
|15202152 | Üblital-Formation | Üblital-Formation     |
|15200534 | Uerscheli-Formation | Uerscheli-Formation     |
|15200278 | Uetliberg-Mergel | Uetliberg-Mergel     |
|15200276 | Uetliberg-Schichten | Uetliberg-Schichten     |
|15200277 | Uetliberggipfel-Nagelfluh | Uetliberggipfel-Nagelfluh     |
|15202229 | Uffiern-Diorit | Uffiern-Diorit     |
|15204138 | Uglix-Plattenkalk | Uglix-Plattenkalk     |
|15200406 | Ulmiz-Quarzitnagelfluh | Ulmiz-Quarzitnagelfluh     |
|15202279 | Ultrahelvetische Flyscheinheiten | Ultrahelvetische Flyscheinheiten     |
|15206057 | Ultramafische Gesteine | Ultramafische Gesteine     |
|15203469 | Ultramafit der Métailler-Formation | Ultramafit der Métailler-Formation     |
|15205116 | Ultramafitit der Arolla-Gruppe | Ultramafitit der Arolla-Gruppe     |
|15200353 | UMM-I | UMM-I     |
|15200351 | UMM-II | UMM-II     |
|15200349 | UMM-III | UMM-III     |
|15200362 | UMM-J | UMM-J     |
|15202245 | Undifferenzierte Kristallingesteine | Undifferenzierte Kristallingesteine     |
|15202469 | Undifferenziertes Kristallin des Helvetikums | Undifferenziertes Kristallin des Helvetikums     |
|15200453 | Unité Inférieure Oolithique (UIO) | Unité Inférieure Oolithique (UIO)     |
|15200452 | Unité Moyenne Calcaire (UMC) | Unité Moyenne Calcaire (UMC)     |
|15202485 | Unter-der-Flue-Fazies | Unter-der-Flue-Fazies     |
|15200048 | Unter-Erli-Bank | Unter-Erli-Bank     |
|15200555 | Unter-Lochsiti-Nagelfluh | Unter-Lochsiti-Nagelfluh     |
|15200473 | Untere-Felsenkalke-Formation | Untere-Felsenkalke-Formation     |
|15200201 | Untere Acuminata-Schichten | Untere Acuminata-Schichten     |
|15203106 | Untere Brekzie | Untere Brekzie     |
|15200560 | Untere Bunte Molasse des Jurasüdfusses | Untere Bunte Molasse des Jurasüdfusses     |
|15202284 | Untere Flyschabfolge (Sardona) | Untere Flyschabfolge (Sardona)     |
|15202396 | Untere Götzis-Bank | Untere Götzis-Bank     |
|15203248 | Untere Kalk- und Tonschiefer der Zone Piz Terri - Lunschania | Untere Kalk- und Tonschiefer der Zone Piz Terri - Lunschania     |
|15203108 | Untere Kalke | Untere Kalke     |
|15200348 | Untere Meeresmolasse (UMM) | Untere Meeresmolasse (UMM)     |
|15200062 | Untere Oolithische Serie (Oolithe Subcompacte) | Untere Oolithische Serie (Oolithe Subcompacte)     |
|15203281 | Untere Rauwacke der Klippen-Decke | Untere Rauwacke der Klippen-Decke     |
|15202536 | Untere Sandsteine (Spirstock) | Untere Sandsteine (Spirstock)     |
|15203107 | Untere Schiefer | Untere Schiefer     |
|15200138 | Untere Sulfatzone | Untere Sulfatzone     |
|15200314 | Untere Süsswassermolasse (USM) | Untere Süsswassermolasse (USM)     |
|15203122 | Untere Tonsteinschichten | Untere Tonsteinschichten     |
|15205100 | Unterer Meride-Kalk | Unterer Meride-Kalk     |
|15202303 | Unterer Quintner Kalk | Unterer Quintner Kalk     |
|15200219 | Unterer Schuttfächer | Unterer Schuttfächer     |
|15200076 | Unterer Stein | Unterer Stein     |
|15200382 | Unterer Teil des Hauptrogensteins | Unterer Teil des Hauptrogensteins     |
|15200018 | Unterer Virgula-Mergel | Unterer Virgula-Mergel     |
|15204073 | Unteres Member der Fuorn-Formation | Unteres Member der Fuorn-Formation     |
|15202341 | Unterwassern-Gneis | Unterwassern-Gneis     |
|15204100 | Ur-Brekzie | Ur-Brekzie     |
|15200289 | Urdorf-Bentonit | Urdorf-Bentonit     |
|15200335 | USM-I | USM-I     |
|15200329 | USM-II | USM-II     |
|15200326 | USM-III | USM-III     |
|15200589 | USM-III bis OSM-I | USM-III bis OSM-I     |
|15200341 | USM-J | USM-J     |
|15200183 | Uttins-Mergel | Uttins-Mergel     |
|15200405 | Utzigen-Muschelsandstein | Utzigen-Muschelsandstein     |
|15200021 | Vabenau-Member | Vabenau-Member     |
|15203539 | Vacarisc-Gneis | Vacarisc-Gneis     |
|15203151 | Vaduz-Flysch | Vaduz-Flysch     |
|15202212 | Val-Bérard-Gneiskomplex | Val-Bérard-Gneiskomplex     |
|15203513 | Val-Chironico-Gneis | Val-Chironico-Gneis     |
|15202289 | Val-d&#39;Illiez-Sandstein | Val-d&#39;Illiez-Sandstein     |
|15202488 | Val-da-Surplattas-Diorit | Val-da-Surplattas-Diorit     |
|15202192 | Val-Gliems-Formation | Val-Gliems-Formation     |
|15205013 | Val-Grande-Sandstein | Val-Grande-Sandstein     |
|15202349 | Val-Gronda-Augengneis | Val-Gronda-Augengneis     |
|15202225 | Val-Lavaz-Gruppe | Val-Lavaz-Gruppe     |
|15206011 | Val-Masino-Granodiorit | Val-Masino-Granodiorit     |
|15204074 | Val-Müstair-Gruppe | Val-Müstair-Gruppe     |
|15202346 | Val-Nalps-Gneiskomplex | Val-Nalps-Gneiskomplex     |
|15202265 | Val-Pigniu-Gneiskomplex | Val-Pigniu-Gneiskomplex     |
|15204077 | Val-Püra-Member | Val-Püra-Member     |
|15202231 | Val-Rondadura-Gruppe | Val-Rondadura-Gruppe     |
|15204122 | Val-Rude-Orthogneis | Val-Rude-Orthogneis     |
|15203484 | Val-Sabbia-Formation | Val-Sabbia-Formation     |
|15205059 | Val-Serrata-Tuffite | Val-Serrata-Tuffite     |
|15202276 | Val-Stgira-Riffmarmor | Val-Stgira-Riffmarmor     |
|15202272 | Val-Tremola-Granit | Val-Tremola-Granit     |
|15204040 | Valbella-Member | Valbella-Member     |
|15203459 | Valgrande-Paragneis | Valgrande-Paragneis     |
|15204054 | Vallatscha-Formation | Vallatscha-Formation     |
|15204056 | Vallatscha-Member | Vallatscha-Member     |
|15200093 | Vallorbe-Member | Vallorbe-Member     |
|15202204 | Vallorcine-Granit | Vallorcine-Granit     |
|15202156 | Vallorcine-Konglomerat | Vallorcine-Konglomerat     |
|15205007 | Valpelline-Serie | Valpelline-Serie     |
|15203170 | Valzeina-Formation | Valzeina-Formation     |
|15203043 | Vanil-Carré-Member | Vanil-Carré-Member     |
|15203359 | Vanis-Formation | Vanis-Formation     |
|15204094 | Varaina-Schiefer | Varaina-Schiefer     |
|15205027 | Varesotto-Flysch | Varesotto-Flysch     |
|15200484 | Variansmergel-Formation | Variansmergel-Formation     |
|15203474 | Variszische Intrusiva der Maggia-Decke | Variszische Intrusiva der Maggia-Decke     |
|15205128 | Variszische Intrusiva der Margna-Sella | Variszische Intrusiva der Margna-Sella     |
|15203460 | Variszische Intrusiva des Briançonnais | Variszische Intrusiva des Briançonnais     |
|15204132 | Variszische Intrusiva des Ostalpins | Variszische Intrusiva des Ostalpins     |
|15205079 | Variszische Intrusiva des Südalpins | Variszische Intrusiva des Südalpins     |
|15200617 | Variszisches Grundgebirge der Nordschweiz | Variszisches Grundgebirge der Nordschweiz     |
|15202467 | Variszisches Kristallin des Helvetikums | Variszisches Kristallin des Helvetikums     |
|15202400 | Vättis-Fossilbrekzie | Vättis-Fossilbrekzie     |
|15200443 | Vauglène-Bänke | Vauglène-Bänke     |
|15204108 | Vaüglia-Granodiorit | Vaüglia-Granodiorit     |
|15200554 | Vaulruz-Formation (UMM-II+III undiff.) | Vaulruz-Formation (UMM-II+III undiff.)     |
|15200004 | Vellerat-Formation | Vellerat-Formation     |
|15203044 | Verdy-Member | Verdy-Member     |
|15200189 | Verena-Member | Verena-Member     |
|15203314 | Vergeletto-Gneis | Vergeletto-Gneis     |
|15200305 | Vermes-Süsswasserkalk | Vermes-Süsswasserkalk     |
|15202154 | Vernayaz-Formation | Vernayaz-Formation     |
|15200439 | Vernettes-Sandstein | Vernettes-Sandstein     |
|15202143 | Verrucano-Gruppe | Verrucano-Gruppe     |
|15205064 | Verrucano Lombardo | Verrucano Lombardo     |
|15203161 | Versoyen-Schichten | Versoyen-Schichten     |
|15203231 | Verspala-Formation | Verspala-Formation     |
|15206058 | Verwitterter Fels, undifferenziert | Verwitterter Fels, undifferenziert     |
|15203295 | Verzasca-Gneis | Verzasca-Gneis     |
|15202430 | Veveyse-de-Châtel-Member | Veveyse-de-Châtel-Member     |
|15202140 | Vieux-Emosson-Formation | Vieux-Emosson-Formation     |
|15203501 | Vignun-Gneis | Vignun-Gneis     |
|15205019 | Villa-Olmo-Konglomerat | Villa-Olmo-Konglomerat     |
|15202429 | Villarbeney-Formation | Villarbeney-Formation     |
|15200451 | Villers-Schichten | Villers-Schichten     |
|15200105 | Villigen-Formation | Villigen-Formation     |
|15200100 | Vions-Formation | Vions-Formation     |
|15202209 | Viséen | Viséen     |
|15202090 | Vitznau-Mergel | Vitznau-Mergel     |
|15203202 | Vizan-Brekzie | Vizan-Brekzie     |
|15200179 | Vogesen-Sandstein | Vogesen-Sandstein     |
|15203296 | Vogorno-Gneis | Vogorno-Gneis     |
|15203285 | Voirons-Flysch | Voirons-Flysch     |
|15203288 | Voirons-Sandstein | Voirons-Sandstein     |
|15202182 | Voralp-Granit | Voralp-Granit     |
|15202569 | Voralp-Granit: saure Randfazies | Voralp-Granit: saure Randfazies     |
|15203143 | Vorarlberg-Flysch | Vorarlberg-Flysch     |
|15200032 | Vorbourg-Member | Vorbourg-Member     |
|15203287 | Vouan-Konglomerat | Vouan-Konglomerat     |
|15200013 | Vouglans-Member | Vouglans-Member     |
|15200437 | Vraconne-Sandstein | Vraconne-Sandstein     |
|15200153 | Vuache-Formation | Vuache-Formation     |
|15202434 | Vuavres-Member | Vuavres-Member     |
|15203056 | Vudalla-Formation | Vudalla-Formation     |
|15206078 | Vulkanische Gesteine, undifferenziert | Vulkanische Gesteine, undifferenziert     |
|15202023 | Wagenmoos-Bänke | Wagenmoos-Bänke     |
|15203283 | Wägital-Flysch | Wägital-Flysch     |
|15203566 | Wägital-Flysch: basaler, tektonisierter Teil | Wägital-Flysch: basaler, tektonisierter Teil     |
|15203564 | Wägital-Flysch: oberer Teil (Paläogen) | Wägital-Flysch: oberer Teil (Paläogen)     |
|15203565 | Wägital-Flysch: untererer Teil (Kreide) | Wägital-Flysch: untererer Teil (Kreide)     |
|15200067 | Waldenburg-Member | Waldenburg-Member     |
|15202375 | Waltensburg-Verrucano | Waltensburg-Verrucano     |
|15200388 | Wanderblock-Bildungen | Wanderblock-Bildungen     |
|15203087 | Wandfluh-Mikrofazies | Wandfluh-Mikrofazies     |
|15202299 | Wang-Brekzie | Wang-Brekzie     |
|15202048 | Wang-Formation | Wang-Formation     |
|15200659 | Wangen- und Letzi-Member, undifferenziert | Wangen- und Letzi-Member, undifferenziert     |
|15202014 | Wängen-Kalk | Wängen-Kalk     |
|15202591 | Wängen-Kalk, Lithothamnienkalk-Fazies | Wängen-Kalk, Lithothamnienkalk-Fazies     |
|15200110 | Wangen-Member | Wangen-Member     |
|15200500 | Wangen-Tuffit | Wangen-Tuffit     |
|15200106 | Wangental-Member | Wangental-Member     |
|15202056 | Wannenalp-Bank | Wannenalp-Bank     |
|15200491 | Wedelsandstein-Formation | Wedelsandstein-Formation     |
|15200543 | Weggis-Formation | Weggis-Formation     |
|15200252 | Wehratal-Syenit | Wehratal-Syenit     |
|15200287 | Wehrenbach-Höckler-Süsswasserkalk | Wehrenbach-Höckler-Süsswasserkalk     |
|15200159 | Weiach-Formation | Weiach-Formation     |
|15200656 | Weilergraben-Formation | Weilergraben-Formation     |
|15203132 | Weissenburg-Flysch | Weissenburg-Flysch     |
|15200085 | Weissenstein-Member | Weissenstein-Member     |
|15202321 | Weissgandstöckli-Bank | Weissgandstöckli-Bank     |
|15203452 | Weissmies-Paragneis | Weissmies-Paragneis     |
|15200158 | Weitenau-Formation | Weitenau-Formation     |
|15200142 | Wellendolomit | Wellendolomit     |
|15200141 | Wellenkalk / Wellenmergel | Wellenkalk / Wellenmergel     |
|15202165 | Wendenjoch-Formation | Wendenjoch-Formation     |
|15200103 | Wettigen-Member | Wettigen-Member     |
|15200251 | Wiesen-Wehratal-Komplex | Wiesen-Wehratal-Komplex     |
|15200157 | Wiesental-Formation | Wiesental-Formation     |
|15200114 | Wildegg-Formation | Wildegg-Formation     |
|15203028 | Wildenbach-Member | Wildenbach-Member     |
|15203280 | Wildgrimmi-Member | Wildgrimmi-Member     |
|15202003 | Wildhaus-Melange | Wildhaus-Melange     |
|15202024 | Wildstrubel-Formation | Wildstrubel-Formation     |
|15202166 | Windgällen-Formation | Windgällen-Formation     |
|15202505 | Windgällen-Formation, Mikrogranit | Windgällen-Formation, Mikrogranit     |
|15202327 | Windgällen-Formation, Rhyolith | Windgällen-Formation, Rhyolith     |
|15202105 | Windgällen-Member | Windgällen-Member     |
|15202224 | Winterhorn-Granit | Winterhorn-Granit     |
|15200539 | Wintersberg-Member | Wintersberg-Member     |
|15200284 | Winterthur-Bentonit | Winterthur-Bentonit     |
|15203095 | Wiriehorn-Formation | Wiriehorn-Formation     |
|15203204 | Wissberg-Brekzie | Wissberg-Brekzie     |
|15200633 | Wissenbach-Süsswasserkalk | Wissenbach-Süsswasserkalk     |
|15200197 | Wittnau-Korallenkalk | Wittnau-Korallenkalk     |
|15200477 | Wohlgeschichtete-Kalke-Formation | Wohlgeschichtete-Kalke-Formation     |
|15200631 | Wolhusen-Bentonit | Wolhusen-Bentonit     |
|15200122 | Wuerttembergica-Schichten | Wuerttembergica-Schichten     |
|15200508 | Wulp-Rotzone | Wulp-Rotzone     |
|15200483 | Wutach-Formation | Wutach-Formation     |
|15200347 | Wynau-Süsswasserkalk | Wynau-Süsswasserkalk     |
|15202196 | Zäsenberg-Gneis | Zäsenberg-Gneis     |
|15200135 | Zeglingen-Formation | Zeglingen-Formation     |
|15202603 | Zemenstein- bis Garschella-Formation, undifferenziert | Zemenstein- bis Garschella-Formation, undifferenziert     |
|15200470 | Zementmergel-Formation | Zementmergel-Formation     |
|15202093 | Zementstein-Formation | Zementstein-Formation     |
|15202160 | Zentraler Aare-Granit | Zentraler Aare-Granit     |
|15203253 | Zervreila-Granitgneis | Zervreila-Granitgneis     |
|15202586 | Zettenalp-Trochematt-Melange | Zettenalp-Trochematt-Melange     |
|15204025 | Zirmenkopf-Kalk | Zirmenkopf-Kalk     |
|15206014 | Zocca-Aplit | Zocca-Aplit     |
|15205135 | Zona Dioritico-Kinzigitica | Zona Dioritico-Kinzigitica     |
|15200557 | Zone der Schiefermergel (der St.-Gallen-Fm.) | Zone der Schiefermergel (der St.-Gallen-Fm.)     |
|15203075 | Zoophycos-Schichten | Zoophycos-Schichten     |
|15205046 | Zu-Kalk | Zu-Kalk     |
|15200186 | Zuckerkörniger Kalk | Zuckerkörniger Kalk     |
|15203262 | Zünegg-Knollenkalk | Zünegg-Knollenkalk     |
|15200281 | Zürich-Schichten | Zürich-Schichten     |
|15200678 | Zurzach-Granit | Zurzach-Granit     |
|15206094 | Zweiglimmergneis, undifferenziert | Zweiglimmergneis, undifferenziert     |
|15203528 | Zwischenmythen-Mergel | Zwischenmythen-Mergel     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute litho{#bedrock-plg-litho}
_Lithologische Beschreibung_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15104015 | (Meso)Kataklasit | (Meso)Kataklasit     |
|15104044 | Adergneis | Adergneis     |
|15104046 | agmatischer Gneis | agmatischer Gneis     |
|15104087 | Albitit | Albitit     |
|15103040 | Alkalirhyolith | Alkalirhyolith     |
|15103013 | Alkalisyenit | Alkalisyenit     |
|15103046 | Alkalitrachyt | Alkalitrachyt     |
|15103006 | Alkalogranit | Alkalogranit     |
|15101039 | Alluvion, undifferenziert | Alluvion, undifferenziert     |
|15104060 | Amphibolit | Amphibolit     |
|15104063 | Amphibolitgneis | Amphibolitgneis     |
|15104074 | Anatexit, undifferenziert | Anatexit, undifferenziert     |
|15103045 | Andesit | Andesit     |
|15102071 | Anhydrit | Anhydrit     |
|15102059 | Anthrazit | Anthrazit     |
|15101067 | anthropogene Elemente, undifferenziert | anthropogene Elemente, undifferenziert     |
|15101062 | äolischer Sand, Flugsand | äolischer Sand, Flugsand     |
|15101061 | äolisches Sediment, undifferenziert | äolisches Sediment, undifferenziert     |
|15103030 | Aplit | Aplit     |
|15102044 | Aptychenkalk | Aptychenkalk     |
|15102038 | Arenit | Arenit     |
|15102016 | Arkose | Arkose     |
|15103058 | Aschentuff | Aschentuff     |
|15101071 | Auffüllung | Auffüllung     |
|15101070 | Aufschüttung, Damm | Aufschüttung, Damm     |
|15104042 | Augengneis | Augengneis     |
|15101041 | Bachschutt | Bachschutt     |
|15104061 | Bänderamphibolit | Bänderamphibolit     |
|15104043 | Bändergneis | Bändergneis     |
|15103048 | Basalt | Basalt     |
|15103068 | basisches Ganggestein | basisches Ganggestein     |
|15103069 | Basisches Gestein | Basisches Gestein     |
|15103066 | Bentonit | Bentonit     |
|15101006 | Bergsturzablagerung | Bergsturzablagerung     |
|15102045 | biogener Kalkstein, undifferenziert | biogener Kalkstein, undifferenziert     |
|15102032 | biogenes / biochemisches / organisches Sedimentgestein, undifferenziert | biogenes / biochemisches / organisches Sedimentgestein, undifferenziert     |
|15102106 | bioklastischer Kalk | bioklastischer Kalk     |
|15104085 | Biotitit | Biotitit     |
|15101015 | Blockgletscher | Blockgletscher     |
|15101010 | Blockschutt | Blockschutt     |
|15102082 | Bohnerz | Bohnerz     |
|15102087 | Boluston | Boluston     |
|15102006 | Brekzie | Brekzie     |
|15102093 | Caliche | Caliche     |
|15102068 | chemisches Sedimentgestein, undifferenziert | chemisches Sedimentgestein, undifferenziert     |
|15104089 | Chloritit | Chloritit     |
|15104034 | Chloritschiefer | Chloritschiefer     |
|15103043 | Dazit | Dazit     |
|15101072 | Deponie | Deponie     |
|15101049 | detritische Verlandungsbildung | detritische Verlandungsbildung     |
|15102046 | detritischer Kalk | detritischer Kalk     |
|15104079 | Diatexit mit nebulitischer Textur | Diatexit mit nebulitischer Textur     |
|15104080 | Diatexit mit Schlierentextur | Diatexit mit Schlierentextur     |
|15104081 | Diatexit mit Schollentextur | Diatexit mit Schollentextur     |
|15103011 | Diorit | Diorit     |
|15103035 | Dolerit | Dolerit     |
|15102049 | Dolomit | Dolomit     |
|15102109 | Dolomitbrekzie | Dolomitbrekzie     |
|15104216 | dolomitischer Marmor | dolomitischer Marmor     |
|15102012 | Dolomitsandstein | Dolomitsandstein     |
|15101075 | dünne Lockermaterialbedeckung | dünne Lockermaterialbedeckung     |
|15102100 | Echinodermenkalk | Echinodermenkalk     |
|15102061 | Eisenoolith | Eisenoolith     |
|15102103 | Eisensandstein | Eisensandstein     |
|15102108 | eisenschüssiger Kalk | eisenschüssiger Kalk     |
|15104064 | Eklogit | Eklogit     |
|15101086 | Entwässerungssediment | Entwässerungssediment     |
|15103039 | Ergussgestein, undifferenziert | Ergussgestein, undifferenziert     |
|15103023 | Essexit | Essexit     |
|15102070 | Evaporit, undifferenziert | Evaporit, undifferenziert     |
|15103037 | Extrusivgestein, undifferenziert | Extrusivgestein, undifferenziert     |
|15104053 | Fels, undifferenziert | Fels, undifferenziert     |
|15101007 | Felssturzablagerung | Felssturzablagerung     |
|15101040 | fluviatiler Schotter | fluviatiler Schotter     |
|15101026 | fluviatiles Sediment, undifferenziert | fluviatiles Sediment, undifferenziert     |
|15102017 | Flyschsandstein, Grauwacke | Flyschsandstein, Grauwacke     |
|15103015 | Gabbro | Gabbro     |
|15103026 | Ganggestein, undifferenziert | Ganggestein, undifferenziert     |
|15101035 | gemischter Schutt | gemischter Schutt     |
|15101076 | geringmächtige Lockergesteinsbedeckung | geringmächtige Lockergesteinsbedeckung     |
|15104210 | Geröll führender Metasandstein | Geröll führender Metasandstein     |
|15102018 | Geröll führender Sandstein | Geröll führender Sandstein     |
|15104027 | Gestein der Regional- und Kontaktmetamorphose, undifferenziert | Gestein der Regional- und Kontaktmetamorphose, undifferenziert     |
|15104002 | Gestein der Störungszone | Gestein der Störungszone     |
|15104003 | Gestein der Störungszone, undifferenziert | Gestein der Störungszone, undifferenziert     |
|15104006 | Gesteinsmehl | Gesteinsmehl     |
|15102072 | Gips | Gips     |
|15102101 | glaukonitischer Kalkstein | glaukonitischer Kalkstein     |
|15102104 | glaukonitischer Mergel | glaukonitischer Mergel     |
|15102020 | Glaukonitsandstein | Glaukonitsandstein     |
|15104036 | Glaukophanschiefer | Glaukophanschiefer     |
|15101031 | glazifluviatiler Schotter | glazifluviatiler Schotter     |
|15101028 | glazifluviatiles Sediment, undifferenziert | glazifluviatiles Sediment, undifferenziert     |
|15101019 | glazigenes Sediment, undifferenziert | glazigenes Sediment, undifferenziert     |
|15101047 | glazilakustrisches Deltasediment | glazilakustrisches Deltasediment     |
|15101046 | glazilakustrisches Sediment, undifferenziert | glazilakustrisches Sediment, undifferenziert     |
|15102019 | Glimmersandstein | Glimmersandstein     |
|15104035 | Glimmerschiefer | Glimmerschiefer     |
|15104072 | Gneis mit Feldspatblasten | Gneis mit Feldspatblasten     |
|15104041 | Gneis, undifferenziert | Gneis, undifferenziert     |
|15104097 | Granat-Glimmerschiefer | Granat-Glimmerschiefer     |
|15103007 | Granit | Granit     |
|15103008 | Granodiorit | Granodiorit     |
|15103024 | Granophyr | Granophyr     |
|15104058 | Granulit | Granulit     |
|15101003 | gravitative Sedimente und Verwitterungsbildungen, undifferenziert | gravitative Sedimente und Verwitterungsbildungen, undifferenziert     |
|15104071 | Greisen | Greisen     |
|15104098 | Grünschiefer | Grünschiefer     |
|15101079 | Gyttja | Gyttja     |
|15101073 | Halde | Halde     |
|15101014 | Hanglehm, Schwemmlehm | Hanglehm, Schwemmlehm     |
|15101009 | Hangschutt | Hangschutt     |
|15104086 | Hornblenditit | Hornblenditit     |
|15104067 | Hornfels | Hornfels     |
|15102054 | Hornstein, Chert | Hornstein, Chert     |
|15102088 | Huppererde | Huppererde     |
|15101081 | hydrochemische Bildungen (Kalksinter) | hydrochemische Bildungen (Kalksinter)     |
|15103054 | Ignimbrit | Ignimbrit     |
|15101083 | In-situ-Verwitterungsschutt | In-situ-Verwitterungsschutt     |
|15103003 | Intrusivgestein, undifferenziert | Intrusivgestein, undifferenziert     |
|15104005 | Kakirit, undifferenziert | Kakirit, undifferenziert     |
|15102041 | Kalkbrekzie | Kalkbrekzie     |
|15102029 | Kalkmergelstein | Kalkmergelstein     |
|15102042 | Kalkoolith | Kalkoolith     |
|15102011 | Kalksandstein | Kalksandstein     |
|15104037 | Kalkschiefer | Kalkschiefer     |
|15104054 | Kalksilikatfels | Kalksilikatfels     |
|15102034 | Kalkstein, undifferenziert | Kalkstein, undifferenziert     |
|15104056 | Karbonat- und Silikat führendes Gestein | Karbonat- und Silikat führendes Gestein     |
|15102075 | Karbonat, undifferenziert | Karbonat, undifferenziert     |
|15103051 | Karbonatit | Karbonatit     |
|15104010 | Kataklasit, undifferenziert | Kataklasit, undifferenziert     |
|15102013 | kieseliger Sandstein | kieseliger Sandstein     |
|15102051 | kieseliges Gestein, undifferenziert | kieseliges Gestein, undifferenziert     |
|15102035 | Kieselkalk | Kieselkalk     |
|15104051 | Kinzigit | Kinzigit     |
|15102003 | klastisches Sedimentgestein, undifferenziert | klastisches Sedimentgestein, undifferenziert     |
|15104007 | Kluftletten | Kluftletten     |
|15102056 | Kohle, undifferenziert | Kohle, undifferenziert     |
|15102007 | Konglomerat | Konglomerat     |
|15102005 | Konglomerat und Brekzie, undifferenziert (Psephit, Korngrösse: Kies, Steine und Blöcke) | Konglomerat und Brekzie, undifferenziert (Psephit, Korngrösse: Kies, Steine und Blöcke)     |
|15102105 | kreidiger Kalk | kreidiger Kalk     |
|15103057 | Kristalltuff | Kristalltuff     |
|15102094 | Krustenkalk | Krustenkalk     |
|15101069 | künstliche Ablagerung, undifferenziert | künstliche Ablagerung, undifferenziert     |
|15101057 | lakustrisches Deltasediment | lakustrisches Deltasediment     |
|15101044 | lakustrisches Sediment, undifferenziert | lakustrisches Sediment, undifferenziert     |
|15103033 | Lamprophyr | Lamprophyr     |
|15103056 | Lapillituff | Lapillituff     |
|15101008 | Lawinenschutt | Lawinenschutt     |
|15104047 | Leptinit | Leptinit     |
|15102057 | Lignit (organisches Sedimentgestein) | Lignit (organisches Sedimentgestein)     |
|15101054 | Lignit (palustrisches Sediment) | Lignit (palustrisches Sediment)     |
|15102102 | Lithothamniensandstein | Lithothamniensandstein     |
|15101001 | Lockergestein | Lockergestein     |
|15101063 | Löss, Lösslehm | Löss, Lösslehm     |
|15103001 | Magmatit | Magmatit     |
|15104055 | Marmor (Fels) | Marmor (Fels)     |
|15104215 | Marmor (sedimentärer Protolith) | Marmor (sedimentärer Protolith)     |
|15102014 | mergeliger Sandstein | mergeliger Sandstein     |
|15102107 | Mergelkalk | Mergelkalk     |
|15102027 | Mergelstein | Mergelstein     |
|15104433 | Metaalkalirhyolith | Metaalkalirhyolith     |
|15104411 | Metaalkalisyenit | Metaalkalisyenit     |
|15104439 | Metaalkalitrachyt | Metaalkalitrachyt     |
|15104404 | Metaalkalogranit | Metaalkalogranit     |
|15104438 | Metaandesit | Metaandesit     |
|15104427 | Metaaplit | Metaaplit     |
|15104208 | Metaarkose | Metaarkose     |
|15104441 | Metabasalt | Metabasalt     |
|15104203 | Metabrekzie | Metabrekzie     |
|15104436 | Metadazit | Metadazit     |
|15104409 | Metadiorit | Metadiorit     |
|15104432 | Metadolerit | Metadolerit     |
|15104421 | Metaessexit | Metaessexit     |
|15104413 | Metagabbro | Metagabbro     |
|15104423 | Metaganggestein | Metaganggestein     |
|15104405 | Metagranit | Metagranit     |
|15104406 | Metagranodiorit | Metagranodiorit     |
|15104422 | Metagranophyr | Metagranophyr     |
|15104209 | Metagrauwacke | Metagrauwacke     |
|15104445 | Metaignimbrit | Metaignimbrit     |
|15104218 | Metakarbonat | Metakarbonat     |
|15104204 | Metakonglomerat | Metakonglomerat     |
|15104430 | Metalamprophyr | Metalamprophyr     |
|15104401 | Metamagmatit | Metamagmatit     |
|15104214 | Metamergel | Metamergel     |
|15104428 | Metamikrodiorit | Metamikrodiorit     |
|15104429 | Metamikrogabbro | Metamikrogabbro     |
|15104424 | Metamikrogranit | Metamikrogranit     |
|15104415 | Metamonzodiorit | Metamonzodiorit     |
|15104416 | Metamonzogabbro | Metamonzogabbro     |
|15104417 | Metamonzonit | Metamonzonit     |
|15104402 | metamorph überprägtes Intrusivgestein | metamorph überprägtes Intrusivgestein     |
|15104444 | metamorph überprägtes pyroklastisches Gestein | metamorph überprägtes pyroklastisches Gestein     |
|15104001 | Metamorphit | Metamorphit     |
|15104095 | Metamorphit (magmatischer Protolith erkennbar) | Metamorphit (magmatischer Protolith erkennbar)     |
|15104092 | Metamorphit (Protolith erkennbar) | Metamorphit (Protolith erkennbar)     |
|15104093 | Metamorphit (sedimentärer Protolith erkennbar) | Metamorphit (sedimentärer Protolith erkennbar)     |
|15104414 | Metanorit | Metanorit     |
|15104426 | Metapegmatit | Metapegmatit     |
|15104211 | Metapelit | Metapelit     |
|15104419 | Metaperidotit | Metaperidotit     |
|15104443 | Metaphonolit | Metaphonolit     |
|15104431 | Metapikrit | Metapikrit     |
|15104403 | Metaplutonit | Metaplutonit     |
|15104207 | Metapsammit | Metapsammit     |
|15104202 | Metapsephit | Metapsephit     |
|15104418 | Metapyroxenit | Metapyroxenit     |
|15104437 | Metaquarzandesit | Metaquarzandesit     |
|15104407 | Metaquarzdiorit | Metaquarzdiorit     |
|15104412 | Metaquarzgabbro | Metaquarzgabbro     |
|15104217 | Metaradiolarit | Metaradiolarit     |
|15104435 | Metarhyodazit | Metarhyodazit     |
|15104434 | Metarhyolith | Metarhyolith     |
|15104205 | Metasandstein | Metasandstein     |
|15104201 | Metasediment | Metasediment     |
|15104212 | Metasiltstein | Metasiltstein     |
|15104069 | Metasomatit, undifferenziert | Metasomatit, undifferenziert     |
|15104410 | Metasyenit | Metasyenit     |
|15104076 | Metatexit mit Fleckentextur | Metatexit mit Fleckentextur     |
|15104078 | Metatexit mit Netztextur | Metatexit mit Netztextur     |
|15104077 | Metatexit mit stromatitischer Textur | Metatexit mit stromatitischer Textur     |
|15104408 | Metatonalit | Metatonalit     |
|15104440 | Metatrachyt | Metatrachyt     |
|15104446 | Metavulkanit | Metavulkanit     |
|15104075 | Migmatit | Migmatit     |
|15102037 | Mikrit | Mikrit     |
|15103031 | Mikrodiorit | Mikrodiorit     |
|15103032 | Mikrogabbro | Mikrogabbro     |
|15103027 | Mikrogranit | Mikrogranit     |
|15104084 | monomineralischer Metamorphit, undifferenziert | monomineralischer Metamorphit, undifferenziert     |
|15103017 | Monzodiorit | Monzodiorit     |
|15103018 | Monzogabbro | Monzogabbro     |
|15103019 | Monzonit | Monzonit     |
|15101021 | Moräne (Till), undifferenziert | Moräne (Till), undifferenziert     |
|15101024 | Moräne auf Gletscher oder Toteis (Glacier or Dead Ice covered by Till) | Moräne auf Gletscher oder Toteis (Glacier or Dead Ice covered by Till)     |
|15101037 | Murgangablagerung | Murgangablagerung     |
|15102022 | Muschelsandstein | Muschelsandstein     |
|15104020 | Mylonit | Mylonit     |
|15104018 | Mylonit, undifferenziert | Mylonit, undifferenziert     |
|15104420 | nephelinitischer Metasyenit | nephelinitischer Metasyenit     |
|15103022 | nephelinitischer Syenit | nephelinitischer Syenit     |
|15103016 | Norit | Norit     |
|15102043 | Nummulitenkalk | Nummulitenkalk     |
|15102021 | Nummulitensandstein | Nummulitensandstein     |
|15104099 | Ophikalzit | Ophikalzit     |
|15104049 | Orthogneis | Orthogneis     |
|15101050 | palustrisches Sediment | palustrisches Sediment     |
|15101051 | palustrisches Sediment, undifferenziert | palustrisches Sediment, undifferenziert     |
|15104048 | Paragneis | Paragneis     |
|15102092 | pedogenes Karbonat, undifferenziert | pedogenes Karbonat, undifferenziert     |
|15103029 | Pegmatit | Pegmatit     |
|15102024 | Pelit, undifferenziert | Pelit, undifferenziert     |
|15103021 | Peridotit (Intrusivgestein) | Peridotit (Intrusivgestein)     |
|15104065 | Peridotit (Metamorphit) | Peridotit (Metamorphit)     |
|15103050 | Phonolith | Phonolith     |
|15102065 | phosphoritreicher Kalkstein | phosphoritreicher Kalkstein     |
|15102066 | phosphoritreicher Mergelstein | phosphoritreicher Mergelstein     |
|15102064 | phosphoritreicher Sandstein | phosphoritreicher Sandstein     |
|15102063 | phosphoritreiches Gestein, undifferenziert | phosphoritreiches Gestein, undifferenziert     |
|15104029 | Phyllit | Phyllit     |
|15104023 | Phyllonit | Phyllonit     |
|15103049 | Pikrit (Effusiva) | Pikrit (Effusiva)     |
|15103034 | Pikrit (Intrusivgestein) | Pikrit (Intrusivgestein)     |
|15101013 | Plateaulehm | Plateaulehm     |
|15104038 | Prasinit | Prasinit     |
|15104014 | Protokataklasit | Protokataklasit     |
|15104019 | Protomylonit | Protomylonit     |
|15104025 | Pseudotachylit | Pseudotachylit     |
|15103055 | Pyroklastische Brekzie | Pyroklastische Brekzie     |
|15103053 | pyroklastisches Gestein, undifferenziert (vulkanischer Tuff, &gt; 75 % pyroklast. Komp.) | pyroklastisches Gestein, undifferenziert (vulkanischer Tuff, &gt; 75 % pyroklast. Komp.)     |
|15103020 | Pyroxenit (Intrusivgestein) | Pyroxenit (Intrusivgestein)     |
|15104088 | Pyroxenit (monomineralischer Metamorphit) | Pyroxenit (monomineralischer Metamorphit)     |
|15103044 | Quarzandesit | Quarzandesit     |
|15103009 | Quarzdiorit | Quarzdiorit     |
|15103014 | Quarzgabbro | Quarzgabbro     |
|15104091 | Quarzit (monomineralischer Metamorphit) | Quarzit (monomineralischer Metamorphit)     |
|15104206 | Quarzit (sedimentärer Protolith) | Quarzit (sedimentärer Protolith)     |
|15102089 | Quarzsand | Quarzsand     |
|15102010 | Quarzsandstein | Quarzsandstein     |
|15104096 | Quarzschiefer | Quarzschiefer     |
|15101080 | Quelltuff (Kalksinter, Lockergestein) | Quelltuff (Kalksinter, Lockergestein)     |
|15102077 | Quelltuff (Kalksinter, Sedimentgestein) | Quelltuff (Kalksinter, Sedimentgestein)     |
|15102052 | Radiolarit | Radiolarit     |
|15101030 | randglazialer Schotter | randglazialer Schotter     |
|15104011 | Rauwacke (Kataklasit) | Rauwacke (Kataklasit)     |
|15102076 | Rauwacke (Sedimentgestein) | Rauwacke (Sedimentgestein)     |
|15102080 | Residualgestein / pedogen überprägtes Gestein, undifferenziert | Residualgestein / pedogen überprägtes Gestein, undifferenziert     |
|15103042 | Rhyodazit | Rhyodazit     |
|15103041 | Rhyolith | Rhyolith     |
|15103028 | Rhyolithporphyr | Rhyolithporphyr     |
|15102040 | Riffkalk | Riffkalk     |
|15104059 | Rodingit | Rodingit     |
|15101033 | Rückzugsschotter | Rückzugsschotter     |
|15102039 | Rudit | Rudit     |
|15101017 | Rutschmasse | Rutschmasse     |
|15102009 | Sandstein, undifferenziert (Psammit: Sandkorngrösse) | Sandstein, undifferenziert (Psammit: Sandkorngrösse)     |
|15103067 | saures Ganggestein | saures Ganggestein     |
|15104031 | Schiefer, undifferenziert | Schiefer, undifferenziert     |
|15102030 | Schlammstein | Schlammstein     |
|15104062 | Schollenamphibolit | Schollenamphibolit     |
|15101087 | Sedimentärer Gang (clastic dike) | Sedimentärer Gang (clastic dike)     |
|15102001 | Sedimentgestein | Sedimentgestein     |
|15101058 | Seebodensediment | Seebodensediment     |
|15101059 | Seekreide | Seekreide     |
|15104033 | Serizitschiefer | Serizitschiefer     |
|15104090 | Serpentinit | Serpentinit     |
|15102084 | siderolithische Verwitterungsbildungen | siderolithische Verwitterungsbildungen     |
|15102090 | Silcrete | Silcrete     |
|15104057 | silikatreicher Marmor | silikatreicher Marmor     |
|15102086 | silikatreiches Gestein, undifferenziert | silikatreiches Gestein, undifferenziert     |
|15102025 | Siltstein | Siltstein     |
|15104070 | Skarn | Skarn     |
|15102036 | Spatkalk | Spatkalk     |
|15102053 | Spiculit | Spiculit     |
|15101034 | Stauschotter | Stauschotter     |
|15102058 | Steinkohle | Steinkohle     |
|15102073 | Steinsalz | Steinsalz     |
|15101056 | Strandablagerungen | Strandablagerungen     |
|15104050 | Stronalit | Stronalit     |
|15101084 | strukturierter Hangschutt | strukturierter Hangschutt     |
|15101005 | Sturzablagerung, undifferenziert | Sturzablagerung, undifferenziert     |
|15101048 | subaquatisch abgelagerte Moräne (Waterlaid Till) | subaquatisch abgelagerte Moräne (Waterlaid Till)     |
|15101052 | Sumpf | Sumpf     |
|15102047 | Süsswasserkalk | Süsswasserkalk     |
|15103012 | Syenit | Syenit     |
|15104039 | Talkschiefer | Talkschiefer     |
|15104008 | tektonische Brekzie (kohäsionslos) | tektonische Brekzie (kohäsionslos)     |
|15104013 | tektonische Brekzie (mit Kohäsion) | tektonische Brekzie (mit Kohäsion)     |
|15104012 | tektonische Dolomitbrekzie | tektonische Dolomitbrekzie     |
|15104448 | tektonische Kalkbrekzie | tektonische Kalkbrekzie     |
|15103005 | Tiefengestein, undifferenziert | Tiefengestein, undifferenziert     |
|15101078 | tiefgründige Verwitterungsdecke | tiefgründige Verwitterungsdecke     |
|15103010 | Tonalit | Tonalit     |
|15102015 | toniger Sandstein | toniger Sandstein     |
|15102028 | Tonmergelstein | Tonmergelstein     |
|15104032 | Tonschiefer (Schiefer) | Tonschiefer (Schiefer)     |
|15104213 | Tonschiefer (sedimentärer Protolith) | Tonschiefer (sedimentärer Protolith)     |
|15102026 | Tonstein | Tonstein     |
|15101053 | Torfmoor, Torf | Torfmoor, Torf     |
|15103047 | Trachyt | Trachyt     |
|15101082 | Travertin (Kalksinter, Lockergestein) | Travertin (Kalksinter, Lockergestein)     |
|15102078 | Travertin (Kalksinter, Sedimentgestein) | Travertin (Kalksinter, Sedimentgestein)     |
|15101085 | Tsunamiablagerung | Tsunamiablagerung     |
|15103060 | Tuffit, undifferenziert (pyroklast. und nicht vulk. Sedimente, 75-25 % pyroklast. Komp.) | Tuffit, undifferenziert (pyroklast. und nicht vulk. Sedimente, 75-25 % pyroklast. Komp.)     |
|15103061 | tuffitische Brekzie | tuffitische Brekzie     |
|15103063 | tuffitischer Sandstein | tuffitischer Sandstein     |
|15103064 | tuffitischer Siltstein | tuffitischer Siltstein     |
|15103065 | tuffitischer Tonstein | tuffitischer Tonstein     |
|15103062 | tuffitisches Konglomerat | tuffitisches Konglomerat     |
|15101042 | Überschwemmungssediment | Überschwemmungssediment     |
|15103070 | Ultrabasisches Gestein | Ultrabasisches Gestein     |
|15104016 | Ultrakataklasit | Ultrakataklasit     |
|15104447 | ultramafisches Gestein | ultramafisches Gestein     |
|15104021 | Ultramylonit | Ultramylonit     |
|15101012 | Verwitterungslehm, undifferenziert | Verwitterungslehm, undifferenziert     |
|15101032 | Vorstossschotter | Vorstossschotter     |
|15101065 | vulkanische Asche | vulkanische Asche     |
|15101016 | zerrüttete Sackungsmasse | zerrüttete Sackungsmasse     |
|15104045 | Zweiglimmergneis | Zweiglimmergneis     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute chrono_t{#bedrock-plg-chrono-t}
_Chronostratigraphische Zuordnung der Obergrenze der Kartiereinheit (Top)_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15001074 | Aalénien | Aalénien     |
|15001059 | Albien | Albien     |
|15001087 | Anisien | Anisien     |
|15001060 | Aptien | Aptien     |
|15001028 | Aquitanien | Aquitanien     |
|15001153 | Archaikum | Archaikum     |
|15001113 | Artinskien | Artinskien     |
|15001117 | Asselien | Asselien     |
|15001073 | Bajocien | Bajocien     |
|15001061 | Barrémien | Barrémien     |
|15001041 | Bartonien | Bartonien     |
|15001140 | Bashkirien | Bashkirien     |
|15001072 | Bathonien | Bathonien     |
|15001064 | Berriasien | Berriasien     |
|15001025 | Burdigalien | Burdigalien     |
|15001010 | Calabrien | Calabrien     |
|15001071 | Callovien | Callovien     |
|15001053 | Campanien | Campanien     |
|15001102 | Capitanien | Capitanien     |
|15001084 | Carnien | Carnien     |
|15001057 | Cénomanien | Cénomanien     |
|15001096 | Changhsingien | Changhsingien     |
|15001031 | Chattien | Chattien     |
|15001151 | Chibanien | Chibanien     |
|15001110 | Cisuralien | Cisuralien     |
|15001055 | Coniacien | Coniacien     |
|15001048 | Danien | Danien     |
|15001128 | Devon | Devon     |
|15001035 | Eozän | Eozän     |
|15001058 | Frühe Kreide | Frühe Kreide     |
|15001088 | Frühe Trias | Frühe Trias     |
|15001075 | Früher Jura | Früher Jura     |
|15001027 | frühes Burdigalien | frühes Burdigalien     |
|15001033 | frühes Chattien | frühes Chattien     |
|15001129 | Frühes Devon | Frühes Devon     |
|15001043 | Frühes Eozän | Frühes Eozän     |
|15001024 | Frühes Miozän | Frühes Miozän     |
|15001127 | Frühes Mississippien | Frühes Mississippien     |
|15001150 | Frühes Ordovizium | Frühes Ordovizium     |
|15001123 | Frühes Pennsylvanien | Frühes Pennsylvanien     |
|15001009 | Frühes Pleistozän | Frühes Pleistozän     |
|15001039 | frühes Priabonien | frühes Priabonien     |
|15001011 | Gélasien | Gélasien     |
|15001101 | Guadalupien | Guadalupien     |
|15001137 | Gzhélien | Gzhélien     |
|15001062 | Hauterivien | Hauterivien     |
|15001079 | Hettangien | Hettangien     |
|15001004 | Holozän | Holozän     |
|15001090 | Indusien | Indusien     |
|15001065 | Jura | Jura     |
|15001135 | Kambrium | Kambrium     |
|15001002 | Känozoikum | Känozoikum     |
|15001119 | Karbon | Karbon     |
|15001138 | Kasimovien | Kasimovien     |
|15001068 | Kimméridgien | Kimméridgien     |
|15001050 | Kreide | Kreide     |
|15001111 | Kungurien | Kungurien     |
|15001086 | Ladinien | Ladinien     |
|15001023 | Langhien | Langhien     |
|15001147 | Llandovery | Llandovery     |
|15001095 | Lopingien | Lopingien     |
|15001145 | Ludlow | Ludlow     |
|15001042 | Lutétien | Lutétien     |
|15001052 | Maastrichtien | Maastrichtien     |
|15001049 | Mesozoikum | Mesozoikum     |
|15001019 | Messinien | Messinien     |
|15001017 | Miozän | Miozän     |
|15001124 | Mississippien | Mississippien     |
|15001085 | Mittlere Trias | Mittlere Trias     |
|15001070 | Mittlerer Jura | Mittlerer Jura     |
|15001130 | Mittleres Devon | Mittleres Devon     |
|15001040 | Mittleres Eozän | Mittleres Eozän     |
|15001021 | Mittleres Miozän | Mittleres Miozän     |
|15001126 | Mittleres Mississippien | Mittleres Mississippien     |
|15001149 | Mittleres Ordovizium | Mittleres Ordovizium     |
|15001122 | Mittleres Pennsylvanien | Mittleres Pennsylvanien     |
|15001007 | Mittleres Pleistozän | Mittleres Pleistozän     |
|15001139 | Moscovien | Moscovien     |
|15001013 | Neogen | Neogen     |
|15001083 | Norien | Norien     |
|15001089 | Olénékien | Olénékien     |
|15001030 | Oligozän | Oligozän     |
|15001134 | Ordovizium | Ordovizium     |
|15001069 | Oxfordien | Oxfordien     |
|15001029 | Paläogen | Paläogen     |
|15001091 | Paläozoikum | Paläozoikum     |
|15001045 | Paleozän | Paleozän     |
|15001120 | Pennsylvanien | Pennsylvanien     |
|15001093 | Perm | Perm     |
|15001001 | Phanerozoikum | Phanerozoikum     |
|15001015 | Plaisancien | Plaisancien     |
|15001005 | Pleistozän | Pleistozän     |
|15001077 | Pliensbachien | Pliensbachien     |
|15001014 | Pliozän | Pliozän     |
|15001152 | Präkambrium | Präkambrium     |
|15001037 | Priabonien | Priabonien     |
|15001144 | Pridoli | Pridoli     |
|15001136 | Proterozoikum | Proterozoikum     |
|15001003 | Quartär | Quartär     |
|15001082 | Rhät | Rhät     |
|15001108 | Roadien | Roadien     |
|15001034 | Rupélien | Rupélien     |
|15001115 | Sakmarien | Sakmarien     |
|15001054 | Santonien | Santonien     |
|15001047 | Sélandien | Sélandien     |
|15001141 | Serpukhovien | Serpukhovien     |
|15001022 | Serravallien | Serravallien     |
|15001133 | Silur | Silur     |
|15001078 | Sinémurien | Sinémurien     |
|15001051 | Späte Kreide | Späte Kreide     |
|15001081 | Späte Trias | Späte Trias     |
|15001066 | Später Jura | Später Jura     |
|15001026 | spätes Burdigalien | spätes Burdigalien     |
|15001032 | spätes Chattien | spätes Chattien     |
|15001131 | Spätes Devon | Spätes Devon     |
|15001036 | Spätes Eozän | Spätes Eozän     |
|15001018 | Spätes Miozän | Spätes Miozän     |
|15001125 | Spätes Mississippien | Spätes Mississippien     |
|15001148 | Spätes Ordovizium | Spätes Ordovizium     |
|15001121 | Spätes Pennsylvanien | Spätes Pennsylvanien     |
|15001006 | Spätes Pleistozän | Spätes Pleistozän     |
|15001038 | spätes Priabonien | spätes Priabonien     |
|15001012 | Tertiär | Tertiär     |
|15001046 | Thanétien | Thanétien     |
|15001067 | Tithonien | Tithonien     |
|15001076 | Toarcien | Toarcien     |
|15001020 | Tortonien | Tortonien     |
|15001143 | Tournaisien | Tournaisien     |
|15001080 | Trias | Trias     |
|15001056 | Turonien | Turonien     |
|15001063 | Valanginien | Valanginien     |
|15001142 | Viséen | Viséen     |
|15001146 | Wenlock | Wenlock     |
|15001106 | Wordien | Wordien     |
|15001098 | Wuchiapingien | Wuchiapingien     |
|15001044 | Yprésien | Yprésien     |
|15001016 | Zancléen | Zancléen     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute chrono_b{#bedrock-plg-chrono-b}
_Chronostratigraphische Zuordnung der Untergrenze der Kartiereinheit (Basis)_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15001074 | Aalénien | Aalénien     |
|15001059 | Albien | Albien     |
|15001087 | Anisien | Anisien     |
|15001060 | Aptien | Aptien     |
|15001028 | Aquitanien | Aquitanien     |
|15001153 | Archaikum | Archaikum     |
|15001113 | Artinskien | Artinskien     |
|15001117 | Asselien | Asselien     |
|15001073 | Bajocien | Bajocien     |
|15001061 | Barrémien | Barrémien     |
|15001041 | Bartonien | Bartonien     |
|15001140 | Bashkirien | Bashkirien     |
|15001072 | Bathonien | Bathonien     |
|15001064 | Berriasien | Berriasien     |
|15001025 | Burdigalien | Burdigalien     |
|15001010 | Calabrien | Calabrien     |
|15001071 | Callovien | Callovien     |
|15001053 | Campanien | Campanien     |
|15001102 | Capitanien | Capitanien     |
|15001084 | Carnien | Carnien     |
|15001057 | Cénomanien | Cénomanien     |
|15001096 | Changhsingien | Changhsingien     |
|15001031 | Chattien | Chattien     |
|15001151 | Chibanien | Chibanien     |
|15001110 | Cisuralien | Cisuralien     |
|15001055 | Coniacien | Coniacien     |
|15001048 | Danien | Danien     |
|15001128 | Devon | Devon     |
|15001035 | Eozän | Eozän     |
|15001058 | Frühe Kreide | Frühe Kreide     |
|15001088 | Frühe Trias | Frühe Trias     |
|15001075 | Früher Jura | Früher Jura     |
|15001027 | frühes Burdigalien | frühes Burdigalien     |
|15001033 | frühes Chattien | frühes Chattien     |
|15001129 | Frühes Devon | Frühes Devon     |
|15001043 | Frühes Eozän | Frühes Eozän     |
|15001024 | Frühes Miozän | Frühes Miozän     |
|15001127 | Frühes Mississippien | Frühes Mississippien     |
|15001150 | Frühes Ordovizium | Frühes Ordovizium     |
|15001123 | Frühes Pennsylvanien | Frühes Pennsylvanien     |
|15001009 | Frühes Pleistozän | Frühes Pleistozän     |
|15001039 | frühes Priabonien | frühes Priabonien     |
|15001011 | Gélasien | Gélasien     |
|15001101 | Guadalupien | Guadalupien     |
|15001137 | Gzhélien | Gzhélien     |
|15001062 | Hauterivien | Hauterivien     |
|15001079 | Hettangien | Hettangien     |
|15001004 | Holozän | Holozän     |
|15001090 | Indusien | Indusien     |
|15001065 | Jura | Jura     |
|15001135 | Kambrium | Kambrium     |
|15001002 | Känozoikum | Känozoikum     |
|15001119 | Karbon | Karbon     |
|15001138 | Kasimovien | Kasimovien     |
|15001068 | Kimméridgien | Kimméridgien     |
|15001050 | Kreide | Kreide     |
|15001111 | Kungurien | Kungurien     |
|15001086 | Ladinien | Ladinien     |
|15001023 | Langhien | Langhien     |
|15001147 | Llandovery | Llandovery     |
|15001095 | Lopingien | Lopingien     |
|15001145 | Ludlow | Ludlow     |
|15001042 | Lutétien | Lutétien     |
|15001052 | Maastrichtien | Maastrichtien     |
|15001049 | Mesozoikum | Mesozoikum     |
|15001019 | Messinien | Messinien     |
|15001017 | Miozän | Miozän     |
|15001124 | Mississippien | Mississippien     |
|15001085 | Mittlere Trias | Mittlere Trias     |
|15001070 | Mittlerer Jura | Mittlerer Jura     |
|15001130 | Mittleres Devon | Mittleres Devon     |
|15001040 | Mittleres Eozän | Mittleres Eozän     |
|15001021 | Mittleres Miozän | Mittleres Miozän     |
|15001126 | Mittleres Mississippien | Mittleres Mississippien     |
|15001149 | Mittleres Ordovizium | Mittleres Ordovizium     |
|15001122 | Mittleres Pennsylvanien | Mittleres Pennsylvanien     |
|15001007 | Mittleres Pleistozän | Mittleres Pleistozän     |
|15001139 | Moscovien | Moscovien     |
|15001013 | Neogen | Neogen     |
|15001083 | Norien | Norien     |
|15001089 | Olénékien | Olénékien     |
|15001030 | Oligozän | Oligozän     |
|15001134 | Ordovizium | Ordovizium     |
|15001069 | Oxfordien | Oxfordien     |
|15001029 | Paläogen | Paläogen     |
|15001091 | Paläozoikum | Paläozoikum     |
|15001045 | Paleozän | Paleozän     |
|15001120 | Pennsylvanien | Pennsylvanien     |
|15001093 | Perm | Perm     |
|15001001 | Phanerozoikum | Phanerozoikum     |
|15001015 | Plaisancien | Plaisancien     |
|15001005 | Pleistozän | Pleistozän     |
|15001077 | Pliensbachien | Pliensbachien     |
|15001014 | Pliozän | Pliozän     |
|15001152 | Präkambrium | Präkambrium     |
|15001037 | Priabonien | Priabonien     |
|15001144 | Pridoli | Pridoli     |
|15001136 | Proterozoikum | Proterozoikum     |
|15001003 | Quartär | Quartär     |
|15001082 | Rhät | Rhät     |
|15001108 | Roadien | Roadien     |
|15001034 | Rupélien | Rupélien     |
|15001115 | Sakmarien | Sakmarien     |
|15001054 | Santonien | Santonien     |
|15001047 | Sélandien | Sélandien     |
|15001141 | Serpukhovien | Serpukhovien     |
|15001022 | Serravallien | Serravallien     |
|15001133 | Silur | Silur     |
|15001078 | Sinémurien | Sinémurien     |
|15001051 | Späte Kreide | Späte Kreide     |
|15001081 | Späte Trias | Späte Trias     |
|15001066 | Später Jura | Später Jura     |
|15001026 | spätes Burdigalien | spätes Burdigalien     |
|15001032 | spätes Chattien | spätes Chattien     |
|15001131 | Spätes Devon | Spätes Devon     |
|15001036 | Spätes Eozän | Spätes Eozän     |
|15001018 | Spätes Miozän | Spätes Miozän     |
|15001125 | Spätes Mississippien | Spätes Mississippien     |
|15001148 | Spätes Ordovizium | Spätes Ordovizium     |
|15001121 | Spätes Pennsylvanien | Spätes Pennsylvanien     |
|15001006 | Spätes Pleistozän | Spätes Pleistozän     |
|15001038 | spätes Priabonien | spätes Priabonien     |
|15001012 | Tertiär | Tertiär     |
|15001046 | Thanétien | Thanétien     |
|15001067 | Tithonien | Tithonien     |
|15001076 | Toarcien | Toarcien     |
|15001020 | Tortonien | Tortonien     |
|15001143 | Tournaisien | Tournaisien     |
|15001080 | Trias | Trias     |
|15001056 | Turonien | Turonien     |
|15001063 | Valanginien | Valanginien     |
|15001142 | Viséen | Viséen     |
|15001146 | Wenlock | Wenlock     |
|15001106 | Wordien | Wordien     |
|15001098 | Wuchiapingien | Wuchiapingien     |
|15001044 | Yprésien | Yprésien     |
|15001016 | Zancléen | Zancléen     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute tecto{#bedrock-plg-tecto}
_Tektonische Zugehörigkeit_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15301125 | «Zone Kronberg-Süd» | «Zone Kronberg-Süd»     |
|15303009 | Aar-Massiv | Aar-Massiv     |
|15301027 | Abgescherter Tafeljura | Abgescherter Tafeljura     |
|15301001 | Abgeschertes Nordalpines Vorland | Abgeschertes Nordalpines Vorland     |
|15307004 | Adamello-Intrusion | Adamello-Intrusion     |
|15304018 | Adula-Decke | Adula-Decke     |
|15303003 | Aiguilles-Rouges-Massiv | Aiguilles-Rouges-Massiv     |
|15305007 | Allgäu-Decke | Allgäu-Decke     |
|15304151 | Antigorio-Decke | Antigorio-Decke     |
|15304010 | Antigorio-Deckenkomplex | Antigorio-Deckenkomplex     |
|15304092 | Antrona-Decke | Antrona-Decke     |
|15303081 | Anzeinde-Decke | Anzeinde-Decke     |
|15303017 | Ardon-Decke | Ardon-Decke     |
|15304076 | Areua-Bruschghorn-Melange | Areua-Bruschghorn-Melange     |
|15304130 | Argio-Schuppe | Argio-Schuppe     |
|15308015 | Arolla-Einheit | Arolla-Einheit     |
|15304100 | Arosa-Decke | Arosa-Decke     |
|15303075 | Arveyes-Decke | Arveyes-Decke     |
|15304158 | Aubrig-Schuppe | Aubrig-Schuppe     |
|15305053 | Augstenberg-Schuppe | Augstenberg-Schuppe     |
|15304036 | Aul-Decke | Aul-Decke     |
|15302040 | Autochtones Nordalpines Vorland | Autochtones Nordalpines Vorland     |
|15301022 | Avant-Monts-Zone | Avant-Monts-Zone     |
|15304097 | Avers-Decke | Avers-Decke     |
|15303041 | Axen-Decke | Axen-Decke     |
|15303131 | Axen-Nordschuppe | Axen-Nordschuppe     |
|15303130 | Axen-Südschuppe | Axen-Südschuppe     |
|15303086 | Bächistock-Schuppe | Bächistock-Schuppe     |
|15303119 | Bad-Ragaz-Decke | Bad-Ragaz-Decke     |
|15305043 | Bardella-Padella-Schuppenkomplex | Bardella-Padella-Schuppenkomplex     |
|15303002 | Belledonne-Massiv | Belledonne-Massiv     |
|15301131 | Belmont-Schuppe | Belmont-Schuppe     |
|15304082 | Berisal-Decke | Berisal-Decke     |
|15305029 | Bernina-Decke | Bernina-Decke     |
|15305028 | Bernina-Deckenkomplex | Bernina-Deckenkomplex     |
|15303074 | Bex-Laubhorn-Decke | Bex-Laubhorn-Decke     |
|15303082 | Blattengrat-Decke | Blattengrat-Decke     |
|15301127 | Blueme-Beichle-Schuppe | Blueme-Beichle-Schuppe     |
|15304131 | Bodengo-Schuppe | Bodengo-Schuppe     |
|15303109 | Bois-de-Bouleyres-Schuppe | Bois-de-Bouleyres-Schuppe     |
|15304078 | Bombogno-Zone | Bombogno-Zone     |
|15304026 | Bosco-Zone | Bosco-Zone     |
|15307006 | Bregaglia-Intrusion | Bregaglia-Intrusion     |
|15304065 | Brekzien-Decke | Brekzien-Decke     |
|15302046 | Bresse-Graben | Bresse-Graben     |
|15303105 | Broc-Schuppenkomplex | Broc-Schuppenkomplex     |
|15303099 | Bürgenstock-Urmiberg-Schuppe | Bürgenstock-Urmiberg-Schuppe     |
|15303091 | Calanda-Decke | Calanda-Decke     |
|15303145 | Calanda-Decke (Blattengrat-Anteil) | Calanda-Decke (Blattengrat-Anteil)     |
|15303149 | Calanda-Decke (Sardona-Anteil) | Calanda-Decke (Sardona-Anteil)     |
|15303151 | Calanda-Schuppe (Aar-Massiv-Anteil) | Calanda-Schuppe (Aar-Massiv-Anteil)     |
|15303102 | Camosci-Decke | Camosci-Decke     |
|15305019 | Campo-Decke | Campo-Decke     |
|15304153 | Camughera-Decke | Camughera-Decke     |
|15306004 | Canavese-Zone | Canavese-Zone     |
|15305039 | Carungas-Schuppe | Carungas-Schuppe     |
|15305060 | Casanna-Schuppe | Casanna-Schuppe     |
|15303027 | Cavistrau-Decke | Cavistrau-Decke     |
|15303011 | Chaînes-subalpines-Decke | Chaînes-subalpines-Decke     |
|15303121 | Chamerstock-Schuppe | Chamerstock-Schuppe     |
|15301139 | Champotey-Ramsera-Schuppe | Champotey-Ramsera-Schuppe     |
|15305042 | Chastelets-Schuppe | Chastelets-Schuppe     |
|15308028 | Chatillon-Schuppe | Chatillon-Schuppe     |
|15308026 | Chatillon-St-Vincent-Schuppen | Chatillon-St-Vincent-Schuppen     |
|15304034 | Chiavenna-Decke | Chiavenna-Decke     |
|15301123 | Chräzerli-Schuppe | Chräzerli-Schuppe     |
|15303128 | Chropfsberg-Gaffia-Schuppen | Chropfsberg-Gaffia-Schuppen     |
|15303094 | Chropfsberg-Schuppe | Chropfsberg-Schuppe     |
|15304017 | Cima-Lunga-Decke | Cima-Lunga-Decke     |
|15304055 | Cimes-Blanches-Decke | Cimes-Blanches-Decke     |
|15303120 | Clariden-Schuppenkomplex | Clariden-Schuppenkomplex     |
|15304118 | Claro-Schuppe | Claro-Schuppe     |
|15305041 | Corvatsch-Schuppe | Corvatsch-Schuppe     |
|15301133 | Cully-Schuppe | Cully-Schuppe     |
|15304128 | Darlun-Schuppe | Darlun-Schuppe     |
|15308014 | Dent-Blanche-Decke | Dent-Blanche-Decke     |
|15303030 | Diablerets-Decke | Diablerets-Decke     |
|15303016 | Doldenhorn-Decke | Doldenhorn-Decke     |
|15305058 | Dorfberg-Decke | Dorfberg-Decke     |
|15304107 | Dranses-Decke | Dranses-Decke     |
|15305056 | Drei-Schwestern-Schuppe | Drei-Schwestern-Schuppe     |
|15304148 | Dros-Scholle | Dros-Scholle     |
|15303046 | Drusberg-Decke | Drusberg-Decke     |
|15301150 | Eichberg-Schuppe | Eichberg-Schuppe     |
|15303060 | Einsiedeln-Schuppenkomplex | Einsiedeln-Schuppenkomplex     |
|15305032 | Ela-Decke | Ela-Decke     |
|15305038 | Err-Decke | Err-Decke     |
|15305035 | Err-Deckenkomplex | Err-Deckenkomplex     |
|15308025 | Etirol-Levaz-Schuppe | Etirol-Levaz-Schuppe     |
|15303061 | Externe Einsiedeln-Schuppen | Externe Einsiedeln-Schuppen     |
|15301024 | Externer Faltenjura | Externer Faltenjura     |
|15303112 | Externes Aar-Massiv | Externes Aar-Massiv     |
|15303141 | Externes Belledonne-Massiv | Externes Belledonne-Massiv     |
|15303115 | Externes Mont-Blanc-Massiv | Externes Mont-Blanc-Massiv     |
|15301025 | Faisceaux | Faisceaux     |
|15304066 | Falknis-Decke | Falknis-Decke     |
|15304113 | Fanella-Schuppe | Fanella-Schuppe     |
|15304029 | Ferret-Schuppe | Ferret-Schuppe     |
|15304043 | Feuerstätter-Decke | Feuerstätter-Decke     |
|15303127 | Fiseten-Orthalgen-Schuppen | Fiseten-Orthalgen-Schuppen     |
|15303071 | Fläscherberg-Decke | Fläscherberg-Decke     |
|15304134 | Forcellina-Schuppe | Forcellina-Schuppe     |
|15304056 | Frilihorn-Decke | Frilihorn-Decke     |
|15303138 | Friteren-Schuppe | Friteren-Schuppe     |
|15301126 | Gäbris-Schuppe | Gäbris-Schuppe     |
|15303095 | Gaffia-Schuppe | Gaffia-Schuppe     |
|15304143 | Gälmji-Zone | Gälmji-Zone     |
|15304117 | Gana-Palingera-Schuppe | Gana-Palingera-Schuppe     |
|15304111 | Garzott-Schuppe | Garzott-Schuppe     |
|15303008 | Gastern-Massiv | Gastern-Massiv     |
|15303122 | Geisstritt-Schuppe | Geisstritt-Schuppe     |
|15304070 | Gelbhorn-Decke | Gelbhorn-Decke     |
|15303020 | Gellihorn-Decke | Gellihorn-Decke     |
|15303124 | Gemsfairen-Schuppe | Gemsfairen-Schuppe     |
|15301137 | Gérignoz-La-Roche-Schuppe | Gérignoz-La-Roche-Schuppe     |
|15304096 | Gets-Decke | Gets-Decke     |
|15301151 | Giebelegg-Schuppe | Giebelegg-Schuppe     |
|15303026 | Gitschen-Decke | Gitschen-Decke     |
|15303038 | Glarner Deckenkomplex | Glarner Deckenkomplex     |
|15304139 | Glegghorn-Schuppe | Glegghorn-Schuppe     |
|15308019 | Gneiss-minuti-Einheit | Gneiss-minuti-Einheit     |
|15303044 | Gonzen-Walenstadt-Schuppen | Gonzen-Walenstadt-Schuppen     |
|15304140 | Gornergrat-Decke | Gornergrat-Decke     |
|15305052 | Gorvion-Schuppe | Gorvion-Schuppe     |
|15304147 | Gotschnawang-Scholle | Gotschnawang-Scholle     |
|15303058 | Gotthard-Decke | Gotthard-Decke     |
|15304138 | Grauspitz-Schuppe | Grauspitz-Schuppe     |
|15304038 | Grava-Decke | Grava-Decke     |
|15303023 | Griessstock-Decke | Griessstock-Decke     |
|15303106 | Gros-Plané-Melange | Gros-Plané-Melange     |
|15304129 | Groven-Schuppe | Groven-Schuppe     |
|15305059 | Grüenhorn-Schuppe | Grüenhorn-Schuppe     |
|15304019 | Gruf-Komplex | Gruf-Komplex     |
|15308030 | Grun-Schuppe | Grun-Schuppe     |
|15308027 | Grun-Schuppe | Grun-Schuppe     |
|15304006 | Güida-Alpettas-Schuppen | Güida-Alpettas-Schuppen     |
|15304103 | Gurnigel-Decke | Gurnigel-Decke     |
|15303077 | Habkern-Melange-Zone | Habkern-Melange-Zone     |
|15304145 | Haupterhorn-Scholle | Haupterhorn-Scholle     |
|15302042 | Haute-Saône-Tafel | Haute-Saône-Tafel     |
|15302020 | Hegau-Bodensee-Störungszone | Hegau-Bodensee-Störungszone     |
|15307010 | Hegau-Provinz | Hegau-Provinz     |
|15303100 | Helvetikum | Helvetikum     |
|15305055 | Heubühl-Schuppe | Heubühl-Schuppe     |
|15301128 | Hilfern-Schuppe | Hilfern-Schuppe     |
|15301148 | Hirschberg-Schuppe | Hirschberg-Schuppe     |
|15303088 | Hoch-Fulen-Decke | Hoch-Fulen-Decke     |
|15303133 | Höch-Turm-Schuppen | Höch-Turm-Schuppen     |
|15303101 | Hochflue-Schuppe | Hochflue-Schuppe     |
|15303040 | Hohenems-Decke | Hohenems-Decke     |
|15301120 | Höhronen-Schuppe | Höhronen-Schuppe     |
|15301149 | Hölzliberg-Schuppe | Hölzliberg-Schuppe     |
|15301129 | Hornbüel-Schuppenzone | Hornbüel-Schuppenzone     |
|15303104 | Iberg-Melange | Iberg-Melange     |
|15308018 | IIa Zona Dioritico-Kinzigitica | IIa Zona Dioritico-Kinzigitica     |
|15303055 | Ilanz-Decke | Ilanz-Decke     |
|15304154 | Infra-Niesen-Melange | Infra-Niesen-Melange     |
|15304159 | Infrapräalpines Melange | Infrapräalpines Melange     |
|15305005 | Inntal-Decke | Inntal-Decke     |
|15303062 | Interne Einsiedeln-Schuppen | Interne Einsiedeln-Schuppen     |
|15301023 | Interner Faltenjura | Interner Faltenjura     |
|15303113 | Internes Aar-Massiv | Internes Aar-Massiv     |
|15303140 | Internes Belledonne-Massiv | Internes Belledonne-Massiv     |
|15303116 | Internes Mont-Blanc-Massiv | Internes Mont-Blanc-Massiv     |
|15304025 | Isorno-Zone | Isorno-Zone     |
|15306002 | Ivrea-Verbano-Zone | Ivrea-Verbano-Zone     |
|15303018 | Jägerchrüz-Decke | Jägerchrüz-Decke     |
|15305033 | Julier-Decke | Julier-Decke     |
|15303129 | Kaminspitz-Schuppe | Kaminspitz-Schuppe     |
|15303025 | Kammlistock-Decke | Kammlistock-Decke     |
|15307009 | Känozoische magmatische Provinzen | Känozoische magmatische Provinzen     |
|15304120 | Kiental-Melange | Kiental-Melange     |
|15303024 | Klausenpass-Schuppen | Klausenpass-Schuppen     |
|15304057 | Klippen-Decke | Klippen-Decke     |
|15304073 | Knorren-Melange | Knorren-Melange     |
|15305004 | Krabachjoch-Decke | Krabachjoch-Decke     |
|15301124 | Kronberg-Schuppe | Kronberg-Schuppe     |
|15301140 | La-Pattaz-La-Holena-Schuppe | La-Pattaz-La-Holena-Schuppe     |
|15303126 | Langfirn-Schuppe | Langfirn-Schuppe     |
|15305020 | Languard-Decke | Languard-Decke     |
|15301134 | Lavaux-Schuppe | Lavaux-Schuppe     |
|15304011 | Lebendun-Decke | Lebendun-Decke     |
|15305006 | Lechtal-Decke | Lechtal-Decke     |
|15304123 | Lenk-Decke | Lenk-Decke     |
|15303108 | Les-Pléiades-Schuppe | Les-Pléiades-Schuppe     |
|15304002 | Leventina-Lucomagno-Decke | Leventina-Lucomagno-Decke     |
|15303068 | Liebenstein-Decke | Liebenstein-Decke     |
|15304133 | Livizung-Schuppe | Livizung-Schuppe     |
|15303096 | Logsbach-Schuppe | Logsbach-Schuppe     |
|15301132 | Lutry-Thonon-Schuppe | Lutry-Thonon-Schuppe     |
|15305072 | Madrisa-Schuppe | Madrisa-Schuppe     |
|15305031 | Madulain-Schuppenkomplex | Madulain-Schuppenkomplex     |
|15304086 | Maggia-Decke | Maggia-Decke     |
|15303139 | Maisander-Schuppe | Maisander-Schuppe     |
|15304098 | Malenco-Forno-Lizun-Decke | Malenco-Forno-Lizun-Decke     |
|15303155 | Maliens-Schuppe | Maliens-Schuppe     |
|15301142 | Marbach-Berneck-Dreieckzone | Marbach-Berneck-Dreieckzone     |
|15303144 | Marchegghorn-Schuppe (Blattengrat-Anteil) | Marchegghorn-Schuppe (Blattengrat-Anteil)     |
|15303147 | Marchegghorn-Schuppe (Sardona-Anteil) | Marchegghorn-Schuppe (Sardona-Anteil)     |
|15308022 | Margna-Decke | Margna-Decke     |
|15304075 | Martegnas-Melange | Martegnas-Melange     |
|15303118 | Mättental-Melange | Mättental-Melange     |
|15304121 | Meilleret-Decke | Meilleret-Decke     |
|15304132 | Mergoscia-Zone | Mergoscia-Zone     |
|15305030 | Mezzaun-Schuppe | Mezzaun-Schuppe     |
|15308021 | Micascisti-eclogitici-Einheit | Micascisti-eclogitici-Einheit     |
|15306008 | Milan Belt | Milan Belt     |
|15303092 | Mirutta-Decke | Mirutta-Decke     |
|15303152 | Mirutta-Schuppen (Aar-Massiv-Anteil) | Mirutta-Schuppen (Aar-Massiv-Anteil)     |
|15303146 | Mirutta-Schuppen (Blattengrat-Anteil) | Mirutta-Schuppen (Blattengrat-Anteil)     |
|15303150 | Mirutta-Schuppen (Sardona-Anteil) | Mirutta-Schuppen (Sardona-Anteil)     |
|15304049 | Mittelpenninikum | Mittelpenninikum     |
|15304077 | Moncucco-Decke | Moncucco-Decke     |
|15303007 | Mont-Blanc-Massiv | Mont-Blanc-Massiv     |
|15303049 | Mont-Chétif-Decke | Mont-Chétif-Decke     |
|15308009 | Mont-Emilius-Decke | Mont-Emilius-Decke     |
|15304084 | Mont-Fort-Decke | Mont-Fort-Decke     |
|15303033 | Mont-Gond-Decke | Mont-Gond-Decke     |
|15308010 | Mont-Mary-Decke | Mont-Mary-Decke     |
|15301135 | Mont-Pèlerin-Schuppe | Mont-Pèlerin-Schuppe     |
|15304012 | Monte-Leone-Decke | Monte-Leone-Decke     |
|15304085 | Monte-Rosa-Decke | Monte-Rosa-Decke     |
|15303107 | Montsalvens-Schuppe | Montsalvens-Schuppe     |
|15303015 | Morcles-Decke | Morcles-Decke     |
|15304030 | Moûtiers-Schuppe | Moûtiers-Schuppe     |
|15305036 | Murtiröl-Schuppe | Murtiröl-Schuppe     |
|15303039 | Mürtschen-Decke | Mürtschen-Decke     |
|15304047 | Muttler-Decke | Muttler-Decke     |
|15304155 | Mythen-Roggenegg-Schuppe | Mythen-Roggenegg-Schuppe     |
|15303098 | Niederhorn-Pilatus-Schuppe | Niederhorn-Pilatus-Schuppe     |
|15304027 | Niesen-Decke | Niesen-Decke     |
|15307005 | Novate-Intrusion | Novate-Intrusion     |
|15308013 | Obere Einheit der Mont-Mary-Decke | Obere Einheit der Mont-Mary-Decke     |
|15306005 | Obere Orobische Decke | Obere Orobische Decke     |
|15304156 | Obere Rotenflue-Schuppe | Obere Rotenflue-Schuppe     |
|15304081 | Obere Stalden-Decke | Obere Stalden-Decke     |
|15304142 | Obere Vals-Schuppen | Obere Vals-Schuppen     |
|15303028 | Oberhelvetikum | Oberhelvetikum     |
|15305002 | Oberostalpin | Oberostalpin     |
|15304091 | Oberpenninikum | Oberpenninikum     |
|15302045 | Oberrhein-Graben | Oberrhein-Graben     |
|15305054 | Ochsenkopf-Schuppe | Ochsenkopf-Schuppe     |
|15304122 | Ochsenweid-Decke | Ochsenweid-Decke     |
|15303143 | Orglen-Schuppen (Aar-Massiv-Anteil) | Orglen-Schuppen (Aar-Massiv-Anteil)     |
|15303148 | Orglen-Schuppen (Sardona-Anteil) | Orglen-Schuppen (Sardona-Anteil)     |
|15304119 | Orselina-Bellinzona-Zone | Orselina-Bellinzona-Zone     |
|15305018 | Ortler-Decke | Ortler-Decke     |
|15305001 | Ostalpin | Ostalpin     |
|15305013 | Ötztal-Decke | Ötztal-Decke     |
|15304014 | Penninikum | Penninikum     |
|15307003 | Periadriatische Provinz | Periadriatische Provinz     |
|15307008 | Periadriatische Vulkanite entlang der Insubrischen Linie | Periadriatische Vulkanite entlang der Insubrischen Linie     |
|15304033 | Petit-St-Bernard-Schuppe | Petit-St-Bernard-Schuppe     |
|15304032 | Pierre-Avoi-Schuppe | Pierre-Avoi-Schuppe     |
|15303103 | Piora-Peiden-Schuppenkomplex | Piora-Peiden-Schuppenkomplex     |
|15303111 | Piz-d&#39;Artgas-Decke | Piz-d&#39;Artgas-Decke     |
|15304005 | Piz-Terri-Lunschania-Decke | Piz-Terri-Lunschania-Decke     |
|15303137 | Pizalun-Schuppe | Pizalun-Schuppe     |
|15304013 | Pizzo-del-Vallone-Decke | Pizzo-del-Vallone-Decke     |
|15303072 | Plaine-Morte-Decke | Plaine-Morte-Decke     |
|15303019 | Plammis-Decke | Plammis-Decke     |
|15301026 | Plateaus | Plateaus     |
|15304099 | Platta-Decke | Platta-Decke     |
|15306007 | Po-Becken | Po-Becken     |
|15308029 | Pontey-Schuppe | Pontey-Schuppe     |
|15304126 | Portjengrat-Decke | Portjengrat-Decke     |
|15304058 | Préalpes médianes plastiques | Préalpes médianes plastiques     |
|15304059 | Préalpes médianes rigides | Préalpes médianes rigides     |
|15305015 | Quattervals-Decke | Quattervals-Decke     |
|15301147 | Ralligen-Schuppenzone | Ralligen-Schuppenzone     |
|15304046 | Ramosch-Zone | Ramosch-Zone     |
|15301118 | Rigi-Rossberg-Schuppe | Rigi-Rossberg-Schuppe     |
|15305070 | Roggenstock-Mördergruebi-Decke | Roggenstock-Mördergruebi-Decke     |
|15304031 | Roignais-Versoyen-Schuppe | Roignais-Versoyen-Schuppe     |
|15308011 | Roisan-Cignana-Scherzone | Roisan-Cignana-Scherzone     |
|15303029 | Roselette-Decke | Roselette-Decke     |
|15304152 | Rosswald-Schuppe | Rosswald-Schuppe     |
|15305024 | Rothorn-Decke | Rothorn-Decke     |
|15303125 | Rotstock-Schuppe | Rotstock-Schuppe     |
|15304045 | Roz-Champatsch-Melange | Roz-Champatsch-Melange     |
|15304125 | Ruginenta-Decke | Ruginenta-Decke     |
|15304080 | Ruitor-Decke | Ruitor-Decke     |
|15305012 | S-chanf-Schuppen | S-chanf-Schuppen     |
|15305016 | S-charl-Sesvenna-Decke | S-charl-Sesvenna-Decke     |
|15304108 | Saane-Decke | Saane-Decke     |
|15308001 | Salassikum | Salassikum     |
|15308002 | Salassikum Sub-Domäne undifferenziert | Salassikum Sub-Domäne undifferenziert     |
|15304088 | Sambuco-Decke | Sambuco-Decke     |
|15304109 | San-Giorgio-Schuppe | San-Giorgio-Schuppe     |
|15303045 | Säntis-Decke | Säntis-Decke     |
|15303069 | Sardona-Decke | Sardona-Decke     |
|15304150 | Sasseneire-Decke | Sasseneire-Decke     |
|15303135 | Schabell-Melange | Schabell-Melange     |
|15303132 | Schächentaler Windgällen-Schuppen | Schächentaler Windgällen-Schuppen     |
|15305057 | Schafläger-Decke | Schafläger-Decke     |
|15304069 | Schams-Deckenkomplex | Schams-Deckenkomplex     |
|15301130 | Schangnau-Schuppe | Schangnau-Schuppe     |
|15305051 | Schesaplana-Schuppe | Schesaplana-Schuppe     |
|15305048 | Schiahorn-Decke | Schiahorn-Decke     |
|15304105 | Schlieren-Decke | Schlieren-Decke     |
|15301122 | Schorhüttenberg-Schuppe | Schorhüttenberg-Schuppe     |
|15303078 | Scopi-Decke | Scopi-Decke     |
|15301144 | Seftigschwand-Schuppe | Seftigschwand-Schuppe     |
|15308023 | Sella-Decke | Sella-Decke     |
|15308017 | Sesia-Decke | Sesia-Decke     |
|15303073 | Sex-Mort-Decke | Sex-Mort-Decke     |
|15303085 | Silberen-Schuppen | Silberen-Schuppen     |
|15305009 | Silvretta-Decke | Silvretta-Decke     |
|15304008 | Simano-Decke | Simano-Decke     |
|15308024 | Simmen-Decke | Simmen-Decke     |
|15304028 | Sion-Courmayeur-Decke | Sion-Courmayeur-Decke     |
|15304083 | Siviez-Mischabel-Decke | Siviez-Mischabel-Decke     |
|15304115 | Soazza-Schuppe | Soazza-Schuppe     |
|15304004 | Soja-Decke | Soja-Decke     |
|15303154 | Sörenberg-Melange | Sörenberg-Melange     |
|15301121 | Speer-Stockberg-Schuppe | Speer-Stockberg-Schuppe     |
|15301119 | St.-Jost-Schuppe | St.-Jost-Schuppe     |
|15304157 | Stäglerenegg-Brünnelistock-Schuppen  | Stäglerenegg-Brünnelistock-Schuppen      |
|15305027 | Stammerspitz-Schuppe | Stammerspitz-Schuppe     |
|15301145 | Steffisburg-Schuppe | Steffisburg-Schuppe     |
|15303142 | Stelli-Schuppe | Stelli-Schuppe     |
|15303123 | Stichplatten-Schuppe | Stichplatten-Schuppe     |
|15304127 | Stockhorn-Decke | Stockhorn-Decke     |
|15306003 | Strona-Ceneri-Zone | Strona-Ceneri-Zone     |
|15303059 | Subalpine Flysch-Zone | Subalpine Flysch-Zone     |
|15301116 | Subalpine Molasse | Subalpine Molasse     |
|15301143 | Subalpiner Schuppenkomplex | Subalpiner Schuppenkomplex     |
|15303034 | Sublage-Decke | Sublage-Decke     |
|15306001 | Südalpin | Südalpin     |
|15306009 | Südalpin Sub-Domäne undifferenziert | Südalpin Sub-Domäne undifferenziert     |
|15302043 | Süddeutsche Tafel | Süddeutsche Tafel     |
|15303153 | Südelbach-Zone | Südelbach-Zone     |
|15304067 | Sulzfluh-Decke | Sulzfluh-Decke     |
|15304090 | Suretta-Decke | Suretta-Decke     |
|15304089 | Tambo-Decke | Tambo-Decke     |
|15304068 | Tasna-Decke | Tasna-Decke     |
|15303057 | Tavetsch-Decke | Tavetsch-Decke     |
|15304112 | Terri-Schuppe | Terri-Schuppe     |
|15305047 | Terza-Schuppe | Terza-Schuppe     |
|15304041 | Tomül-Decke | Tomül-Decke     |
|15305022 | Tonale-Decke | Tonale-Decke     |
|15303097 | Toralp-Schuppe | Toralp-Schuppe     |
|15304149 | Totalp-Ophiolithkomplex | Totalp-Ophiolithkomplex     |
|15304114 | Trescolmen-Schuppe | Trescolmen-Schuppe     |
|15304136 | Triesenberg-Schuppenkomplex | Triesenberg-Schuppenkomplex     |
|15303114 | Trun-Punteglias-Teilmassiv | Trun-Punteglias-Teilmassiv     |
|15304094 | Tsaté-Decke | Tsaté-Decke     |
|15303021 | Tschep-Schuppe | Tschep-Schuppe     |
|15304072 | Tschera-Kalkberg-Decke | Tschera-Kalkberg-Decke     |
|15304137 | Tschingel-Schuppe | Tschingel-Schuppe     |
|15303136 | Tschingelhörner-Schuppe | Tschingelhörner-Schuppe     |
|15305026 | Tschirpen-Decke | Tschirpen-Decke     |
|15303110 | Tulle-Melange | Tulle-Melange     |
|15303048 | Ultrahelvetikum | Ultrahelvetikum     |
|15305082 | Umbrail-Chavalatsch-Schuppen | Umbrail-Chavalatsch-Schuppen     |
|15305014 | Umbrail-Terza-Schuppenkomplex | Umbrail-Terza-Schuppenkomplex     |
|15308012 | Untere Einheit der Mont-Mary-Decke | Untere Einheit der Mont-Mary-Decke     |
|15306006 | Untere Orobische Decke | Untere Orobische Decke     |
|15304054 | Untere Stalden-Schuppe | Untere Stalden-Schuppe     |
|15304141 | Untere Vals-Schuppen | Untere Vals-Schuppen     |
|15303001 | Unterhelvetikum | Unterhelvetikum     |
|15305023 | Unterostalpin | Unterostalpin     |
|15304015 | Unterpenninikum | Unterpenninikum     |
|15304044 | Üntschen-Decke | Üntschen-Decke     |
|15304135 | Val-Gronda-Schuppe | Val-Gronda-Schuppe     |
|15308016 | Valpelline-Einheit | Valpelline-Einheit     |
|15304035 | Vals-Schuppenkomplex | Vals-Schuppenkomplex     |
|15301138 | Vaulruz-Schuppe | Vaulruz-Schuppe     |
|15304009 | Verampio-Decke | Verampio-Decke     |
|15301136 | Vevey-Evian-Schuppe | Vevey-Evian-Schuppe     |
|15301141 | Villarvolard-Schuppe | Villarvolard-Schuppe     |
|15304053 | Visperterminen-Schuppe | Visperterminen-Schuppe     |
|15304104 | Voirons-Decke | Voirons-Decke     |
|15308031 | Vollon-Schuppe | Vollon-Schuppe     |
|15301031 | Vorfaltenzone | Vorfaltenzone     |
|15301030 | Vorlandplateau | Vorlandplateau     |
|15303037 | Wageten-Schuppe | Wageten-Schuppe     |
|15304106 | Wägital-Decke | Wägital-Decke     |
|15304146 | Weissfluh-Scholle | Weissfluh-Scholle     |
|15303063 | Wildhaus-Melange | Wildhaus-Melange     |
|15303031 | Wildhorn-Deckenkomplex | Wildhorn-Deckenkomplex     |
|15303042 | Wissberg-Schuppe | Wissberg-Schuppe     |
|15303134 | Wissenwand-Schuppe | Wissenwand-Schuppe     |
|15301146 | Wolfsegg-Schuppe | Wolfsegg-Schuppe     |
|15304093 | Zermatt-Saas-Fee-Decke | Zermatt-Saas-Fee-Decke     |
|15304116 | Zervreila-Schuppe | Zervreila-Schuppe     |
|15304050 | Zone Houillère | Zone Houillère     |
|15304051 | Zone Houillère externe | Zone Houillère externe     |
|15304052 | Zone Houillère interne | Zone Houillère interne     |
|15304048 | Zone Submédiane | Zone Submédiane     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute orig_descr
_Originalbezeichnung gemäss der Legende der zugrundeliegenden geologischen Karte_
_Datentyp:  string_



   

#### Attribute buried_out
_Wurde das Festgestein wieder verdeckt (ja / nein)?_
_Datentyp:  boolean_



   

#### Attribute exotic_ele
_Handelt es sich bei der Objektart um ein exotisches Element; z.B. Einschluss, Linse, Tasche, Olistholith (ja / nein)?_


   

#### Attribute colour
_Farbe des Gesteins. Präzisieren ob es sich um die Bruchfarbe, die Verwitterungsfarbe, etc. handelt; z.B.Verwitterungsfarbe grau._
_Datentyp:  string_



   

#### Attribute sedi_main_com{#bedrock-plg-sedi-main-com}
_Hauptgesteinskomponente des klastischen Sedimentgesteins_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15602006 | Dolomitstein | Dolomitstein     |
|15602001 | Gesteinsbruchstück undifferenziert | Gesteinsbruchstück undifferenziert     |
|15602005 | Kalkstein | Kalkstein     |
|15602002 | kieselige Gesteine (Quarzit, Quarz (Mineralisch), Radiolarit, Kieselkalk, Quarzsandstein, Hornstein) | kieselige Gesteine (Quarzit, Quarz (Mineralisch), Radiolarit, Kieselkalk, Quarzsandstein, Hornstein)     |
|15602007 | Kristallingestein undifferenziert | Kristallingestein undifferenziert     |
|15602010 | Mergelstein | Mergelstein     |
|15602009 | Metamorphit | Metamorphit     |
|15602003 | Sedimentgestein undifferenziert | Sedimentgestein undifferenziert     |
|15602004 | Tonstein | Tonstein     |
|15602008 | Vulkanit | Vulkanit     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute sedi_seco_com{#bedrock-plg-sedi-seco-com}
_Nebengesteinskomponente des Sedimentgesteins_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|20001019 | biogene Komponenten | biogene Komponenten     |
|20001024 | Bitumen | Bitumen     |
|20001005 | Dolomitstein | Dolomitstein     |
|20001026 | Eisenmineralien | Eisenmineralien     |
|20001025 | Evaporit | Evaporit     |
|20001012 | Feldspat | Feldspat     |
|20001001 | Gesteinsbruchstück undifferenziert | Gesteinsbruchstück undifferenziert     |
|20001013 | Glaukonit | Glaukonit     |
|20001014 | Glimmer | Glimmer     |
|20001015 | intraformationelle Gerölle | intraformationelle Gerölle     |
|20001016 | Kalkkonkretionen | Kalkkonkretionen     |
|20001004 | Kalkstein | Kalkstein     |
|20001023 | Kohle | Kohle     |
|20001006 | Kristallingestein undifferenziert | Kristallingestein undifferenziert     |
|20001022 | Mergelstein | Mergelstein     |
|20001008 | Metamorphit | Metamorphit     |
|20001021 | Phosphorit | Phosphorit     |
|20001010 | pyroklastische Komponenten | pyroklastische Komponenten     |
|20001011 | Quarz | Quarz     |
|20001009 | Quarzit | Quarzit     |
|20001002 | Sedimentgestein undifferenziert | Sedimentgestein undifferenziert     |
|20001017 | Sideritkonkretionen | Sideritkonkretionen     |
|20001018 | Silexkonkretionen | Silexkonkretionen     |
|20001020 | terrigener Detritus | terrigener Detritus     |
|20001003 | Tonstein | Tonstein     |
|20001007 | Vulkanit | Vulkanit     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute sedi_bond_mat{#bedrock-plg-sedi-bond-mat}
_Bindemittel des Sedimentgesteins_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14313008 | dolomitische Matrix | dolomitische Matrix     |
|14313002 | dolomitischer Zement | dolomitischer Zement     |
|14313007 | kalkige Matrix | kalkige Matrix     |
|14313001 | kalkiger Zement | kalkiger Zement     |
|14313003 | kieseliger Zement | kieseliger Zement     |
|14313010 | mineralische Imprägnierung | mineralische Imprägnierung     |
|14313009 | organische Imprägnierung (Asphalt) | organische Imprägnierung (Asphalt)     |
|14313006 | sandige Matrix | sandige Matrix     |
|14313005 | siltige Matrix | siltige Matrix     |
|14313004 | tonige Matrix | tonige Matrix     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute sedi_bedding{#bedrock-plg-sedi-bedding}
_Schichtung des Sedimentgesteins_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|20101005 | blätterig | blätterig     |
|20101003 | dickbankig (&gt;30cm) | dickbankig (&gt;30cm)     |
|20101004 | dünnbankig (1-10cm) | dünnbankig (1-10cm)     |
|20101002 | gebankt | gebankt     |
|20101006 | knauerig | knauerig     |
|20101007 | knollig | knollig     |
|20101008 | linsenförmig | linsenförmig     |
|20101001 | massig | massig     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute sedi_str{#bedrock-plg-sedi-str}
_Textur des Sedimentgesteins_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|20201007 | bioturbiert | bioturbiert     |
|20201002 | geschichtet | geschichtet     |
|20201006 | invers gradiert | invers gradiert     |
|20201004 | laminiert | laminiert     |
|20201005 | normal gradiert | normal gradiert     |
|20201003 | schräg-/kreuzgeschichtet | schräg-/kreuzgeschichtet     |
|20201008 | stromatolitisch | stromatolitisch     |
|20201001 | texturlos | texturlos     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute sedi_tex{#bedrock-plg-sedi-tex}
_Sedimentstruktur_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|20301005 | bioklastisch | bioklastisch     |
|20301003 | mikritisch | mikritisch     |
|20301001 | monomikt | monomikt     |
|20301007 | onkolithisch | onkolithisch     |
|20301008 | oolithisch | oolithisch     |
|20301009 | pelitisch | pelitisch     |
|20301010 | pisolithisch | pisolithisch     |
|20301002 | polymikt | polymikt     |
|20301004 | spätig | spätig     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute igne_text{#bedrock-plg-igne-text}
_Struktur des magmatischen Gesteins_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14317001 | gleichkörnig | gleichkörnig     |
|14317003 | porphyrisch | porphyrisch     |
|14317002 | ungleichkörnig | ungleichkörnig     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute igne_grain_si{#bedrock-plg-igne-grain-si}
_Korngrösse des magmatischen Gesteins_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14318003 | aphanitisch | aphanitisch     |
|14318002 | feinkörnig | feinkörnig     |
|14318001 | grobkörnig | grobkörnig     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute igne_affinity{#bedrock-plg-igne-affinity}
_Affinität zu einer magmatischen Serie._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15733001 | alkalisch | alkalisch     |
|15733002 | kalkalkalisch | kalkalkalisch     |
|15733003 | tholeiitisch | tholeiitisch     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute meta_full_name
_Bezeichnung des metamorphen Gesteins_
_Datentyp:  string_



   

#### Attribute meta_mineral{#bedrock-plg-meta-mineral}
_Wichtiges Mineral des metamorphen Gesteins_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|20401056 | Adular | Adular     |
|20401057 | Aegirin | Aegirin     |
|20401058 | Aegirin-Augit | Aegirin-Augit     |
|20401001 | Aktinolith | Aktinolith     |
|20401002 | Albit | Albit     |
|20401024 | Alkalifeldspat | Alkalifeldspat     |
|20401003 | Allanit | Allanit     |
|20401004 | Almandin | Almandin     |
|20401050 | Alumosilikat | Alumosilikat     |
|20401005 | Amphibol | Amphibol     |
|20401006 | Andalusit | Andalusit     |
|20401059 | Andesin | Andesin     |
|20401060 | Anhydrit | Anhydrit     |
|20401007 | Ankerit | Ankerit     |
|20401061 | Annit | Annit     |
|20401008 | Anorthit | Anorthit     |
|20401009 | Antigorit | Antigorit     |
|20401062 | Aragonit | Aragonit     |
|20401063 | Augit | Augit     |
|20401010 | Biotit | Biotit     |
|20401014 | Chlorit | Chlorit     |
|20401015 | Chloritoid | Chloritoid     |
|20401064 | Chrysotil | Chrysotil     |
|20401017 | Coesit | Coesit     |
|20401018 | Cordierit | Cordierit     |
|20401019 | Diopsid | Diopsid     |
|20401020 | Disthen | Disthen     |
|20401021 | Dolomit | Dolomit     |
|20401082 | Enstatit | Enstatit     |
|20401022 | Epidot | Epidot     |
|20401081 | Fayalit | Fayalit     |
|20401023 | Feldspat | Feldspat     |
|20401080 | Forsterit | Forsterit     |
|20401085 | Fuchsit | Fuchsit     |
|20401026 | Glaukophan | Glaukophan     |
|20401032 | Glimmer | Glimmer     |
|20401028 | Granat | Granat     |
|20401027 | Graphit | Graphit     |
|20401065 | Grossular | Grossular     |
|20401033 | Hellglimmer | Hellglimmer     |
|20401029 | Hornblende | Hornblende     |
|20401066 | Jadeit | Jadeit     |
|20401011 | Kalzit | Kalzit     |
|20401012 | Karbonatmineral | Karbonatmineral     |
|20401013 | Karpholith | Karpholith     |
|20401070 | Klinopyroxen | Klinopyroxen     |
|20401016 | Klinozoisit | Klinozoisit     |
|20401030 | Lawsonit | Lawsonit     |
|20401031 | Magnetit | Magnetit     |
|20401067 | Margarit | Margarit     |
|20401034 | Mikroklin | Mikroklin     |
|20401035 | Muskovit | Muskovit     |
|20401068 | Oligoklas | Oligoklas     |
|20401036 | Olivin | Olivin     |
|20401037 | Omphazit | Omphazit     |
|20401038 | Orthoklas | Orthoklas     |
|20401069 | Orthopyroxen | Orthopyroxen     |
|20401039 | Paragonit | Paragonit     |
|20401071 | Phengit | Phengit     |
|20401040 | Phlogopit | Phlogopit     |
|20401041 | Plagioklas | Plagioklas     |
|20401042 | Prehnit | Prehnit     |
|20401072 | Pumpellyit | Pumpellyit     |
|20401043 | Pyrit | Pyrit     |
|20401044 | Pyrop | Pyrop     |
|20401045 | Pyrophyllit | Pyrophyllit     |
|20401046 | Pyroxen | Pyroxen     |
|20401047 | Quarz | Quarz     |
|20401073 | Sanidin | Sanidin     |
|20401074 | Sapphirin | Sapphirin     |
|20401084 | Serizit | Serizit     |
|20401049 | Serpentin | Serpentin     |
|20401051 | Sillimanit | Sillimanit     |
|20401075 | Spessartin | Spessartin     |
|20401076 | Spinell | Spinell     |
|20401052 | Staurolith | Staurolith     |
|20401053 | Stilpnomelan | Stilpnomelan     |
|20401054 | Talk | Talk     |
|20401077 | Titanit | Titanit     |
|20401078 | Tremolit | Tremolit     |
|20401079 | Turmalin | Turmalin     |
|20401083 | Zeolith | Zeolith     |
|20401055 | Zoisit | Zoisit     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute meta_str{#bedrock-plg-meta-str}
_Textur des metamorphen Gesteins_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|20501016 | agmatitisch (migmatitisch) | agmatitisch (migmatitisch)     |
|20501003 | augig | augig     |
|20501017 | brekziös | brekziös     |
|20501015 | flaserig | flaserig     |
|20501012 | geadert | geadert     |
|20501002 | gebändert | gebändert     |
|20501010 | gebankt | gebankt     |
|20501011 | gefältelt | gefältelt     |
|20501008 | lagig | lagig     |
|20501007 | laminiert | laminiert     |
|20501014 | linsig | linsig     |
|20501001 | massig | massig     |
|20501004 | mit Schollen | mit Schollen     |
|20501006 | phyllitisch | phyllitisch     |
|20501009 | plattig | plattig     |
|20501005 | schiefrig | schiefrig     |
|20501013 | schlierig | schlierig     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   





## Theme GEOMORPHOLOGY ##

### Class Instability_Structures_PT ###
Die Klasse Instability_Structures_PT enthält lokal beobachtete Hinweise auf Hanginstabilitäten 
(Rutschungen), die räumlich nicht abgegrenzt werden können. Wenn möglich, sollen instabile 
Gesteinsmassen durch Polygone erfasst werden (Klasse Instabilities_within_Unconsolidated_ 
Deposits_PLG), die punktförmige Aufnahme ist zu vermeiden und vorwiegend für die Vektorisierung älterer
gedruckter Karten gedacht.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Spezifische Eigenschaft 
[]()           | Cardinality [1] | 11601                                       |  





#### Attribute kind
_Spezifische Eigenschaft_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11601001 | Gins Hinweis auf Hanginstabilität | Gins Hinweis auf Hanginstabilität     |


   

### Class Instability_Structures_L ###
Die Klasse Instability_Structures_L umfasst linienförmige Morphologien, die sich als Folge von 
Hanginstabilitäten an der Oberfläche ausgebildet haben. Beim Abrissrand handelt es sich um den 
oberen Rand der durch das Abgleiten der bewegten Masse freigelegten Gleitfläche einer 
Rutschung oder Sackung (Abrissnische)




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Spezifische Eigenschaft 
[]()           | Cardinality [1] | 11701                                       |  





#### Attribute kind
_Spezifische Eigenschaft_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11701001 | Gins Stauchwulst | Gins Stauchwulst     |
|11701002 | Gins Nackentälchen, Zerrstruktur | Gins Nackentälchen, Zerrstruktur     |
|11701003 | Gins Abrissrand | Gins Abrissrand     |
|11701004 | Gins offene Spalte | Gins offene Spalte     |


   

### Class Instabilities_within_Unconsolidated_Deposits_PLG ###
Die Klasse Instabilities_within_Unconsolidated_Deposits_PLG beinhaltet alle Polygone, die Gebiete 
mit instabilen Lockergesteinen begrenzen. In dieser Klasse werden die Prozessräume der 
verschiedenen Typen von gleitenden Massenbewegungsprozessen ausgeschieden; die 
eigentlichen Gesteinskörper und Ablagerungen, die von Massenbewegungsprozessen betroffen 
bzw. gebildet worden sind, werden in der Klasse Unconsolidated_Deposits_PLG beschrieben. Zur 
näheren Erklärung der verschiedenen Objektarten sind im Anhang A einige Fallbeispiele 
abgebildet.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Spezifische Eigenschaft 
[]()           | Cardinality [1] | 11801                                       |  





#### Attribute kind
_Spezifische Eigenschaft_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|


   

### Class Instabilities_within_Bedrock_PLG ###
Die Klasse Instabilities_within_Bedrock_PLG beinhaltet alle Polygone, die Gebiete mit instabilen 
Festgesteinen begrenzen. In dieser Klasse werden die Prozessräume der verschiedenen Typen von 
gleitenden Massenbewegungsprozessen ausgeschieden; die eigentlichen Gesteinskörper, die von 
Massenbewegungsprozessen betroffen sind, werden in der Klasse Bedrock_PLG beschrieben. Zur 
näheren Erklärung der verschiedenen Objektarten sind im Anhang A einige Fallbeispiele 
abgebildet.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Spezifische Eigenschaft 
[]()           | Cardinality [1] | 11501                                       |  
2 | **main_mov**                | [CodedDomain](#instabilities-within-bedrock-plg-main-mov)                    | Hauptbewegungsphase 
[]()           | Cardinality [0..1] |                                                      |  





#### Attribute kind
_Spezifische Eigenschaft_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|


   

#### Attribute main_mov{#instabilities-within-bedrock-plg-main-mov}
_Hauptbewegungsphase_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11502002 | Hauptbewegungsphase nach dem letzteiszeitlichen Maximum | Hauptbewegungsphase nach dem letzteiszeitlichen Maximum     |
|11502001 | Hauptbewegungsphase vor dem letzteiszeitlichen Maximum | Hauptbewegungsphase vor dem letzteiszeitlichen Maximum     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

### Class Glacial_Structures_PT ###
Die Klasse Glacial_Structures_PT enthält Objektarten, welche die ehemalige Anwesenheit eines 
Gletschers punktuell dokumentieren (Gletscherschliff ist ein räumlich orientiertes Objekt und 
befindet sich deshalb in der Klasse Lineation_PT).




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Spezifische Eigenschaft 
[]()           | Cardinality [1] | 11201                                       |  





#### Attribute kind
_Spezifische Eigenschaft_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11201002 | Ggla Gletschermühle, Strudelloch | Ggla Gletschermühle, Strudelloch     |
|11201001 | Ggla glazitektonische Deformation | Ggla glazitektonische Deformation     |


   

### Class Glacial_and_Periglacial_Structures_L ###
Die Klasse Glacial_and_Periglacial_Structures_L enthält linienförmige Strukturen, die auf ein 
glaziales oder periglaziales Bildungsmilieu hindeuten. Mit Ausnahme der Schliffgrenze handelt es 
sich in dieser Klasse ausschliesslich um akkummulative Landschaftsformen wie Moränenwälle oder 
Blockwülste im Blockgletscher.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 11301                                       |  
2 | **morai_mo**                | [CodedDomain](#glacial-and-periglacial-structures-l-morai-mo)                    | Morphologie der Moräne 
[]()           | Cardinality [0..1] |                                                      |  
3 | **glac_typ**                | [CodedDomain](#glacial-and-periglacial-structures-l-glac-typ)                    | Gletschertyp, auf welchen die Objektart bezogen ist 
[]()           | Cardinality [0..1] |                                                      |  
4 | **ice_m_p**                | [CodedDomain](#glacial-and-periglacial-structures-l-ice-m-p)                    | Räumlicher Gletscherstand 
[]()           | Cardinality [0..1] |                                                      |  
5 | **quat_str**                | [CodedDomain](#glacial-and-periglacial-structures-l-quat-str)                    | Zeitliche quartärstratigraphische Zuordnung des Moränenwälls 
[]()           | Cardinality [0..1] |                                                      |  
6 | **ref_year**                | integer                                    | Referenzjahr des älteren Gletscherstandes. 
[]()           | Cardinality [0..1] |                                        |  
7 | **source**                | string                                    | Quellenangabe der historischen Unterlagen 
[]()           | Cardinality [0..1] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11301001 | Ggla Moränenwall | Ggla Moränenwall     |
|11301002 | Ggla Moränenwall auf Gletscher oder auf Toteis | Ggla Moränenwall auf Gletscher oder auf Toteis     |
|11301003 | Ggla Kameterrassenkante | Ggla Kameterrassenkante     |
|11301004 | Ggla älterer Gletscherstand, basierend auf historischen Daten | Ggla älterer Gletscherstand, basierend auf historischen Daten     |
|11301005 | Ggla Schliffgrenze | Ggla Schliffgrenze     |
|11301006 | Ggla Protalus Rampart Wulst | Ggla Protalus Rampart Wulst     |
|11301007 | Ggla Blockwulst im Blockgletscher | Ggla Blockwulst im Blockgletscher     |
|11301008 | Ggla Schneehaldenmoränenwall | Ggla Schneehaldenmoränenwall     |
|11301009 | Ggla Verbreitungsgrenze von Geschiebe | Ggla Verbreitungsgrenze von Geschiebe     |


   

#### Attribute morai_mo{#glacial-and-periglacial-structures-l-morai-mo}
_Morphologie der Moräne_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11302002 | einseitig abfallend | einseitig abfallend     |
|11302001 | symmetrisch | symmetrisch     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute glac_typ{#glacial-and-periglacial-structures-l-glac-typ}
_Gletschertyp, auf welchen die Objektart bezogen ist_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11303002 | grosse Tal- und Vorlandgletscher | grosse Tal- und Vorlandgletscher     |
|11303001 | Lokalgletscher | Lokalgletscher     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute ice_m_p{#glacial-and-periglacial-structures-l-ice-m-p}
_Räumlicher Gletscherstand_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11304002 | Bern | Bern     |
|11304050 | Bremgarten I | Bremgarten I     |
|11304051 | Bremgarten II | Bremgarten II     |
|11304003 | Bremgarten, undifferenziert | Bremgarten, undifferenziert     |
|11304052 | Bülach I | Bülach I     |
|11304053 | Bülach II | Bülach II     |
|11304054 | Bülach, undifferenziert | Bülach, undifferenziert     |
|11304037 | Chur | Chur     |
|11304055 | Dättikon | Dättikon     |
|11304028 | Feuerthalen I | Feuerthalen I     |
|11304029 | Feuerthalen II | Feuerthalen II     |
|11304005 | Feuerthalen, undifferenziert | Feuerthalen, undifferenziert     |
|11304040 | Fideris | Fideris     |
|11304006 | Gurten | Gurten     |
|11304007 | Hurden | Hurden     |
|11304008 | Killwangen | Killwangen     |
|11304039 | Koblach | Koblach     |
|11304004 | Konstanz | Konstanz     |
|11304035 | Küblis | Küblis     |
|11304036 | Lunden | Lunden     |
|11304001 | Maximalstand, undifferenziert | Maximalstand, undifferenziert     |
|11304009 | Mellingen | Mellingen     |
|11304010 | Muri | Muri     |
|11304056 | Regensdorf | Regensdorf     |
|11304011 | Rotkreuz | Rotkreuz     |
|11304038 | Sargans | Sargans     |
|11304030 | Schaffausen I | Schaffausen I     |
|11304031 | Schaffausen II | Schaffausen II     |
|11304012 | Schaffhausen, undifferenziert | Schaffhausen, undifferenziert     |
|11304048 | Schlieren I | Schlieren I     |
|11304049 | Schlieren II | Schlieren II     |
|11304013 | Schlieren, undifferenziert | Schlieren, undifferenziert     |
|11304014 | Schosshalde | Schosshalde     |
|11304057 | Seeb | Seeb     |
|11304015 | Seftigschwand | Seftigschwand     |
|11304041 | Serneus | Serneus     |
|11304016 | Solothurn | Solothurn     |
|11304017 | Spreitenbach | Spreitenbach     |
|11304018 | Spreitenbach-Killwangen | Spreitenbach-Killwangen     |
|11304045 | Staffelbach-Stand | Staffelbach-Stand     |
|11304025 | Stein-am-Rhein I | Stein-am-Rhein I     |
|11304026 | Stein-am-Rhein II | Stein-am-Rhein II     |
|11304027 | Stein-am-Rhein III | Stein-am-Rhein III     |
|11304019 | Stein am Rhein, undifferenziert | Stein am Rhein, undifferenziert     |
|11304058 | Stetten I | Stetten I     |
|11304059 | Stetten II | Stetten II     |
|11304020 | Stetten, undifferenziert | Stetten, undifferenziert     |
|11304043 | Sursee | Sursee     |
|11304044 | Triengen | Triengen     |
|11304021 | Wangen I | Wangen I     |
|11304022 | Wangen II | Wangen II     |
|11304042 | Wangen, undifferenziert | Wangen, undifferenziert     |
|11304023 | Wittigkofen | Wittigkofen     |
|11304060 | Würenlos I | Würenlos I     |
|11304061 | Würenlos II | Würenlos II     |
|11304062 | Würenlos, undifferenziert | Würenlos, undifferenziert     |
|11304046 | Zürich I | Zürich I     |
|11304047 | Zürich II | Zürich II     |
|11304024 | Zürich, undifferenziert | Zürich, undifferenziert     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute quat_str{#glacial-and-periglacial-structures-l-quat-str}
_Zeitliche quartärstratigraphische Zuordnung des Moränenwälls_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11305001 | 1. Vergletscherung der letzten Eiszeit (MIS 5d) | 1. Vergletscherung der letzten Eiszeit (MIS 5d)     |
|11305002 | 2. Vergletscherung der letzten Eiszeit (MIS 4) | 2. Vergletscherung der letzten Eiszeit (MIS 4)     |
|11305003 | 3. Vergletscherung der letzten Eiszeit (LGM, MIS 2) | 3. Vergletscherung der letzten Eiszeit (LGM, MIS 2)     |
|11305005 | Clavadel | Clavadel     |
|11305006 | Daun | Daun     |
|11305007 | Egesen | Egesen     |
|11305004 | Gschnitz | Gschnitz     |
|11305008 | Mittleres Pleistozän | Mittleres Pleistozän     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute ref_year
_Referenzjahr des älteren Gletscherstandes._
_Datentyp:  integer_



   

#### Attribute source
_Quellenangabe der historischen Unterlagen_
_Datentyp:  string_



   

### Class Glacial_Structures_PLG ###
Die Klasse Glacial_Structures_PLG umfasst flächenhafte glaziale Landschaftsformen, die durch
basales Fliessen des Gletschereises oder dessen Abschmelzen entstanden sind.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 11401                                       |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11401001 | Ggla Drumlin, drumlinartige Kieskuppe | Ggla Drumlin, drumlinartige Kieskuppe     |
|11401003 | Ggla Rundhöcker | Ggla Rundhöcker     |
|11401004 | Ggla Toteisloch, Soll | Ggla Toteisloch, Soll     |


   

### Class Erosional_Structures_PT ###
Die Klasse Erosional_Structures_PT beinhaltet lokale Landschaftselemente, die sich im Laufe der 
Zeit unter Einwirkung von diversen Erosionsprozessen gebildet haben.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 11001                                       |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11001001 | Gero Erdpyramide | Gero Erdpyramide     |


   

### Class Erosional_Structures_L ###
Die Klasse Erosional_Structures_L enthält linienförmige erosive Formen wie Erosionsränder im 
Allgemeinen oder Terrassenkanten. 
Auf älteren gedruckten Karten wurden Erosionsränder und Terrassenkanten oftmals nicht 
unterschieden. In den Vektordaten wird diese Unterscheidung jedoch konsequent vollzogen. Dies
bedingt, dass im Rahmen der Vektorisierung älterer gedruckter Karten Erosionsränder und 
Terrassenkanten aufgeteilt werden müssen. Terrassenkanten werden nur dann als solche 
attributiert, wenn sie durch ihre Lage und entsprechende Schotterterrassen eindeutig zugeordnet
werden können. Zweifelhafte Fälle werden als Erosionsränder aufgenommen.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 11101                                       |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11101001 | Gero Erosionsrand | Gero Erosionsrand     |
|11101002 | Gero Terrassenkante | Gero Terrassenkante     |
|11101003 | Gero Schichtstufenkante | Gero Schichtstufenkante     |


   

### Class Karstic_Structures_PT ###
Die Klasse Karstic_Structures_PT beinhaltet Karstphänomene, die punktförmig dargestellt werden. 
Darunter fallen u.a. der Ponor oder der Eingang zu einer Höhle.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 11301                                       |  
2 | **ice_cave**                | boolean                                    | Handelt es sich bei der Höhle um eine Eisgrotte («glacière», aussergewöhnlich kalte Höhle in der sich
durch die winterlichen Schneefälle oder durch das Gefrieren von eingedrungenem Wasser Eis akkumuliert
und das auch die warme Jahreszeit überdauert) (ja / nein)? 
[]()           | Cardinality [0..1] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|11301001 | Ggla Moränenwall | Ggla Moränenwall     |
|11301002 | Ggla Moränenwall auf Gletscher oder auf Toteis | Ggla Moränenwall auf Gletscher oder auf Toteis     |
|11301003 | Ggla Kameterrassenkante | Ggla Kameterrassenkante     |
|11301004 | Ggla älterer Gletscherstand, basierend auf historischen Daten | Ggla älterer Gletscherstand, basierend auf historischen Daten     |
|11301005 | Ggla Schliffgrenze | Ggla Schliffgrenze     |
|11301006 | Ggla Protalus Rampart Wulst | Ggla Protalus Rampart Wulst     |
|11301007 | Ggla Blockwulst im Blockgletscher | Ggla Blockwulst im Blockgletscher     |
|11301008 | Ggla Schneehaldenmoränenwall | Ggla Schneehaldenmoränenwall     |
|11301009 | Ggla Verbreitungsgrenze von Geschiebe | Ggla Verbreitungsgrenze von Geschiebe     |


   

#### Attribute ice_cave
_Handelt es sich bei der Höhle um eine Eisgrotte («glacière», aussergewöhnlich kalte Höhle in der sich
durch die winterlichen Schneefälle oder durch das Gefrieren von eingedrungenem Wasser Eis akkumuliert
und das auch die warme Jahreszeit überdauert) (ja / nein)?_
_Datentyp:  boolean_



   

### Class Karstic_Structures_PLG ###
Die Klasse Karstic_Structures_PLG umfasst flächenhafte Karstformen wie Dolinen oder Poljen. 
Dolinen werden immer als Polygone erfasst (das) bildet dafür eine wichtige Grundlage). Kleine 
Dolinen (Durchmesser &lt; 25 m), werden durch eine definierte Einheitsfläche von 500 m²
dargestellt.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 12001                                       |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12001001 | Gkar Senke ohne oberirdischen Abfluss | Gkar Senke ohne oberirdischen Abfluss     |
|12001002 | Gkar Doline | Gkar Doline     |
|12001003 | Gkar Karrenfeld | Gkar Karrenfeld     |
|12001004 | Gkar Polje | Gkar Polje     |


   

### Class Alluvial_and_Lacustrine_Structures_L ###
Die Klasse Alluvial_and_Lacustrine_Structures_L beinhaltet linienförmige Morphologien 
fluviatilen oder lakustrischen Ursprungs.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 10901                                       |  
2 | **age**                | [CodedDomain](#alluvial-and-lacustrine-structures-l-age)                    | Alter der Objektart. 
[]()           | Cardinality [0..1] |                                                      |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10901001 | Gall Strandwall | Gall Strandwall     |
|10901002 | Gall Achse einer Murgangrinne | Gall Achse einer Murgangrinne     |


   

#### Attribute age{#alluvial-and-lacustrine-structures-l-age}
_Alter der Objektart._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10902001 | fossil | fossil     |
|10902002 | rezent | rezent     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   





## Theme TECTONICS ##

### Class Deformation_Structures_PT ###
Die Klasse Deformation_Structures_PT beinhaltet punktuell beobachtete tektonische 
Deformationsstrukturen wie lokal stark verfaltete Stellen (Fältelung) oder Orte mit ausgeprägter 
Klüftung. Ebenfalls in dieser Klasse befinden sich konstruierte Punkte wie z.B. die Orientierung 
der Faltenachsenfläche. Die Darstellung der Spur einer Achsenfläche entspricht der Symbolisierung 
eines konstruierten Faltenscharniers, in einem Punkt der Intersektion einer Achsenfläche und der 
Topografie. Diese beiden letzterwähnten Objektarten sind im Anhang A zur besseren 
Verständlichkeit abgebildet.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 14601                                       |  
2 | **azimuth**                | integer                                    | Fallrichtung (Azimut) der jeweiligen Punktobjektart. Wert in Grad (0° 359°) im Uhrzeigersinn gemessen. 
[]()           | Cardinality [0..1] |                                        |  
3 | **dip**                | integer                                    | Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die
Vertikale (90°). 
[]()           | Cardinality [0..1] |                                        |  
4 | **fold_typ**                | [CodedDomain](#deformation-structures-pt-fold-typ)                    | Objekttyp 
[]()           | Cardinality [0..1] |                                                      |  
5 | **fold_for**                | [CodedDomain](#deformation-structures-pt-fold-for)                    | Objektform 
[]()           | Cardinality [0..1] |                                                      |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14601001 | Tdef punktuell beobachtete tektonische Brekzie | Tdef punktuell beobachtete tektonische Brekzie     |
|14601002 | Tdef ausgeprägte Klüftung | Tdef ausgeprägte Klüftung     |
|14601003 | Tdef tektonische Diskordanz | Tdef tektonische Diskordanz     |
|14601004 | Tdef Orientierung der Faltenachsenfläche | Tdef Orientierung der Faltenachsenfläche     |
|14601005 | Tdef Fältelung | Tdef Fältelung     |
|14601006 | Tdef Darstellung der Spur einer Achsenfläche | Tdef Darstellung der Spur einer Achsenfläche     |
|14601007 | Tdef Chevron-Falte, Kink Fold | Tdef Chevron-Falte, Kink Fold     |


   

#### Attribute azimuth
_Fallrichtung (Azimut) der jeweiligen Punktobjektart. Wert in Grad (0° 359°) im Uhrzeigersinn gemessen._
_Datentyp:  integer_



   

#### Attribute dip
_Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die
Vertikale (90°)._
_Datentyp:  integer_



   

#### Attribute fold_typ{#deformation-structures-pt-fold-typ}
_Objekttyp_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14604001 | Antiklinale | Antiklinale     |
|14604002 | Synklinale | Synklinale     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute fold_for{#deformation-structures-pt-fold-for}
_Objektform_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14605001 | Antiform | Antiform     |
|14605002 | Synform | Synform     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

### Class Deformation_Structures_L ###
Die Klasse Deformation_Structures_L enthält linienförmige tektonische Deformationsstrukturen,
wie den Verlauf des Faltenscharniers. Ein Beispiel der Objektart ist zur Veranschaulichung im
Anhang A abgebildet.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 14701                                       |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14701001 | Tdef Faltenscharnier | Tdef Faltenscharnier     |


   

### Class Deformation_Structures_PLG ###
In der Klasse Deformation_Structures_PLG befinden sich tektonisch geprägte Zonen wie
tektonisierte Zonen oder Kluftzonen.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 14801                                       |  
2 | **type**                | [CodedDomain](#deformation-structures-plg-type)                    | Charakteristik der Objektarten 
[]()           | Cardinality [0..1] |                                                      |  
3 | **gen_rela**                | CDD                                    | Genetische Beziehung. 
[]()           | Cardinality [0..1] | None                                       |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14801001 | Tdef Kluftzone | Tdef Kluftzone     |
|14801002 | Tdef tektonisierte Zone | Tdef tektonisierte Zone     |


   

#### Attribute type{#deformation-structures-plg-type}
_Charakteristik der Objektarten_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14802002 | kakiritisch | kakiritisch     |
|14802001 | kataklastisch | kataklastisch     |
|14802003 | mylonitisch | mylonitisch     |
|14802004 | pseudotachylitisch | pseudotachylitisch     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute gen_rela
_Genetische Beziehung._


   

### Class Tectonic_Boundaries_L ###
Die Klasse Tectonic_Boundaries_L umfasst alle tektonischen Verwerfungen. Die Horizontal-
verschiebungen in der Schweiz können als «Bruch, (Attribut «Fault_Mo» (Fault Movement))
parallel zur Streichrichtung» abgebildet werden. Als Pendant zu «Überschiebung» oder
«Abschiebung» gibt es in der Schweiz keine «Horizontalverschiebung» mit vergleichbarer
Grössenausdehnung. Ein Abscherhorizont wird als «Überschiebung» oder als «Abschiebung»
dargestellt. Wenn die Bewegungsrichtung nicht bekannt ist, wird er zur «tektonischen Grenze mit
unbekannter Bewegungsrichtung». Zur näheren Erklärung der verschiedenen Objektarten sind im
Anhang A Beispiele abgebildet.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 14901                                       |  
2 | **fault_mo**                | [CodedDomain](#tectonic-boundaries-l-fault-mo)                    | Bewegungsrichtung des Bruchs 
[]()           | Cardinality [0..1] |                                                      |  
3 | **verti_mo**                | [CodedDomain](#tectonic-boundaries-l-verti-mo)                    | Bewegung parallel zur Fallrichtung der Bruchfläche. 
[]()           | Cardinality [0..1] |                                                      |  
4 | **horiz_mo**                | [CodedDomain](#tectonic-boundaries-l-horiz-mo)                    | Bewegung parallel zur Streichrichtung der Bruch- oder Scherfläche 
[]()           | Cardinality [0..1] |                                                      |  
5 | **lim_tect_b**                | boolean                                    | Grenze einer tektonischen Einheit wie Deckengrenze,Schuppengrenze, Zonengrenze, etc. (ja / nein)? 
[]()           | Cardinality [1] |                                        |  
6 | **status**                | [CodedDomain](#tectonic-boundaries-l-status)                    | Zustand der Objektart 
[]()           | Cardinality [1] |                                                      |  
7 | **activity**                | TODO                                    | Aktivität der Objektart 
[]()           | Cardinality [0..1] |                                        |  
8 | **meta_sta**                | [CodedDomain](#tectonic-boundaries-l-meta-sta)                    | Tektonometamorphe Chronologie der Objektart 
[]()           | Cardinality [0..1] |                                                      |  
9 | **name**                | string                                    | Spezifischer Name der Objektart. 
[]()           | Cardinality [0..1] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14901001 | Ttec Überschiebung | Ttec Überschiebung     |
|14901002 | Ttec Abschiebung | Ttec Abschiebung     |
|14901004 | Ttec Bruch | Ttec Bruch     |
|14901005 | Ttec Aufschiebung | Ttec Aufschiebung     |
|14901006 | Ttec Blattverschiebung | Ttec Blattverschiebung     |
|14901007 | Ttec komplexe Störung | Ttec komplexe Störung     |
|14901008 | Ttec Störung i. Allg. | Ttec Störung i. Allg.     |


   

#### Attribute fault_mo{#tectonic-boundaries-l-fault-mo}
_Bewegungsrichtung des Bruchs_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14902003 | parallel zur Fallrichtung (strike slip) | parallel zur Fallrichtung (strike slip)     |
|14902002 | parallel zur Streichrichtung (Horizontalverschiebung) | parallel zur Streichrichtung (Horizontalverschiebung)     |
|14902001 | schrägverschiebend (oblique slip) | schrägverschiebend (oblique slip)     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute verti_mo{#tectonic-boundaries-l-verti-mo}
_Bewegung parallel zur Fallrichtung der Bruchfläche._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14903002 | abschiebend | abschiebend     |
|14903001 | aufschiebend | aufschiebend     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute horiz_mo{#tectonic-boundaries-l-horiz-mo}
_Bewegung parallel zur Streichrichtung der Bruch- oder Scherfläche_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14904001 | dextral | dextral     |
|14904002 | sinistral | sinistral     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute lim_tect_b
_Grenze einer tektonischen Einheit wie Deckengrenze,Schuppengrenze, Zonengrenze, etc. (ja / nein)?_
_Datentyp:  boolean_



   

#### Attribute status{#tectonic-boundaries-l-status}
_Zustand der Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14906004 | aus Seismikdaten interpretiert | aus Seismikdaten interpretiert     |
|14906001 | gesichert, im Allgemeinen | gesichert, im Allgemeinen     |
|14906002 | gesichert, unter Tage festgestellt | gesichert, unter Tage festgestellt     |
|14906003 | vermutet | vermutet     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute activity
_Aktivität der Objektart_


   

#### Attribute meta_sta{#tectonic-boundaries-l-meta-sta}
_Tektonometamorphe Chronologie der Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14908003 | nach der Platznahme der Decken | nach der Platznahme der Decken     |
|14908001 | vor der Platznahme der Decken | vor der Platznahme der Decken     |
|14908002 | während der Platznahme der Decken | während der Platznahme der Decken     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute name
_Spezifischer Name der Objektart._
_Datentyp:  string_



   





## Theme MEASUREMENTS_SPATIAL_ORIENTATION ##

### Class Folds_PT ###
Die Klasse Folds_PT enthält Objektarten, welche die räumliche Lage von verfalteten geologischen
Objekten (mit direkten Feldmessungen) beschreiben. Beispiele der Objektarten Orientierung der
Faltenachse und der Scheitellinie sind im Anhang A zur besseren Verständlichkeit abgebildet.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 13601                                       |  
2 | **fold_typ**                | [CodedDomain](#folds-pt-fold-typ)                    | Objekttyp 
[]()           | Cardinality [0..1] |                                                      |  
3 | **fold_for**                |                                     | Form der Objektart 
[]()           | Cardinality [0..1] | 13603                                       |  
4 | **phase**                | [CodedDomain](#folds-pt-phase)                    | Deformationsphase. 
[]()           | Cardinality [0..1] |                                                      |  
5 | **phase_ref**                | string                                    | Referenz für die Angabe der Deformationsphase. 
[]()           | Cardinality [0..1] |                                        |  
6 | **azimuth**                | integer                                    | Einfallsrichtung (Azimut) der jeweiligen Punktobjektart (z.B. Scheitellinie, Faltenachse).
Wert in Grad (0° 359°) im Uhrzeigersinn gemessen 
[]()           | Cardinality [1] |                                        |  
7 | **dip**                | integer                                    | Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die
Vertikale (90°). 
[]()           | Cardinality [0..1] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13601001 | Mfol Orientierung der Faltenachse | Mfol Orientierung der Faltenachse     |
|13601002 | Mfol Orientierung der Scheitellinie | Mfol Orientierung der Scheitellinie     |
|13601003 | Mfol Orientierung der Muldenlinie | Mfol Orientierung der Muldenlinie     |


   

#### Attribute fold_typ{#folds-pt-fold-typ}
_Objekttyp_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13602001 | Antiklinale | Antiklinale     |
|13602002 | Synklinale | Synklinale     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute fold_for
_Form der Objektart_


   

#### Attribute phase{#folds-pt-phase}
_Deformationsphase._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13604001 | F1 (1. Phase) | F1 (1. Phase)     |
|13604002 | F2 (2. Phase) | F2 (2. Phase)     |
|13604003 | F3 (3. Phase) | F3 (3. Phase)     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute phase_ref
_Referenz für die Angabe der Deformationsphase._
_Datentyp:  string_



   

#### Attribute azimuth
_Einfallsrichtung (Azimut) der jeweiligen Punktobjektart (z.B. Scheitellinie, Faltenachse).
Wert in Grad (0° 359°) im Uhrzeigersinn gemessen_
_Datentyp:  integer_



   

#### Attribute dip
_Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die
Vertikale (90°)._
_Datentyp:  integer_



   

### Class Lineation_PT ###
In der Klasse Lineation_PT finden sich Objektarten, welche die räumliche Lage von diversen
Linearen mit direkten Feldmessungen beschreiben. Die räumliche Lage u.a. von Gletscherschliffen
und Rutschharnischen ist ebenso Teil dieser Klasse wie die Orientierung von Streckungs- oder
Intersektionslineationen.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 13701                                       |  
2 | **azimuth**                | integer                                    | Einfallsrichtung (Azimut) der jeweiligen Punktobjektart (z.B. Scheitellinie, Faltenachse).
Wert in Grad (0° 359°) im Uhrzeigersinn gemessen 
[]()           | Cardinality [1] |                                        |  
3 | **dip**                |                                     | Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die
Vertikale (90°). 
[]()           | Cardinality [] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13701001 | Mlin Orientierung der Intersektionslineation | Mlin Orientierung der Intersektionslineation     |
|13701002 | Mlin Orientierung der Streckungslineation | Mlin Orientierung der Streckungslineation     |
|13701003 | Mlin Orientierung von Rutschharnischen | Mlin Orientierung von Rutschharnischen     |
|13701004 | Mlin Orientierung von Gletscherschliffen | Mlin Orientierung von Gletscherschliffen     |


   

#### Attribute azimuth
_Einfallsrichtung (Azimut) der jeweiligen Punktobjektart (z.B. Scheitellinie, Faltenachse).
Wert in Grad (0° 359°) im Uhrzeigersinn gemessen_
_Datentyp:  integer_



   

#### Attribute dip
_Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die
Vertikale (90°)._


   

### Class Planar_Structures_PT ###
Die Klasse Planar_Structures_PT enthält Objektarten, welche die räumliche Lage von planaren
Strukturen mit direkten Feldmessungen beschreiben. Ein Beispiel der Objektart Orientierung der
Schieferung ist im Anhang A zur Veranschaulichung abgebildet.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 13801                                       |  
2 | **polarity**                | [CodedDomain](#planar-structures-pt-polarity)                    | Position der Objektart im Raum 
[]()           | Cardinality [0..1] |                                                      |  
3 | **phase**                | [CodedDomain](#planar-structures-pt-phase)                    | Deformationsphase 
[]()           | Cardinality [] |                                                      |  
4 | **phase_ref**                | string                                    | Referenz für die Angabe der Deformationsphase. 
[]()           | Cardinality [0..1] |                                        |  
5 | **ob_dip_slo**                | boolean                                    | Dip slope beobachtet (ja / nein)? 
[]()           | Cardinality [0..1] |                                        |  
6 | **azimuth**                | integer                                    | Einfallsrichtung (Azimut) der jeweiligen Punktobjektart (z.B. Scheitellinie, Faltenachse).
Wert in Grad (0° 359°) im Uhrzeigersinn gemessen 
[]()           | Cardinality [1] |                                        |  
7 | **dip**                |                                     | Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die
Vertikale (90°). 
[]()           | Cardinality [] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13801002 | Mpla Orientierung eines Ganges | Mpla Orientierung eines Ganges     |
|13801003 | Mpla Orientierung einer Bruchfläche | Mpla Orientierung einer Bruchfläche     |
|13801004 | Mpla Orientierung der Schieferung | Mpla Orientierung der Schieferung     |
|13801005 | Mpla Orientierung einer Schichtung oder Schieferung | Mpla Orientierung einer Schichtung oder Schieferung     |
|13801001 | Mpla Orientierung der Schichten | Mpla Orientierung der Schichten     |
|13801006 | Mpla Schüttungsrichtung | Mpla Schüttungsrichtung     |


   

#### Attribute polarity{#planar-structures-pt-polarity}
_Position der Objektart im Raum_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13802001 | normal | normal     |
|13802002 | überkippt | überkippt     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute phase{#planar-structures-pt-phase}
_Deformationsphase_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13803001 | S1 (1. Phase) | S1 (1. Phase)     |
|13803002 | S2 (2. Phase) | S2 (2. Phase)     |
|13803003 | S3 (3. Phase) | S3 (3. Phase)     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute phase_ref
_Referenz für die Angabe der Deformationsphase._
_Datentyp:  string_



   

#### Attribute ob_dip_slo
_Dip slope beobachtet (ja / nein)?_
_Datentyp:  boolean_



   

#### Attribute azimuth
_Einfallsrichtung (Azimut) der jeweiligen Punktobjektart (z.B. Scheitellinie, Faltenachse).
Wert in Grad (0° 359°) im Uhrzeigersinn gemessen_
_Datentyp:  integer_



   

#### Attribute dip
_Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die
Vertikale (90°)._


   





## Theme LOCAL_ADDITIONAL_INFORMATION ##

### Class Anomalies_PT ###
Die Klasse Anomalies_PT beinhaltet lokal beobachtete und / oder gemessene Anomalien.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 128001                                       |  
2 | **type**                |                                     | Charakteristik der Objektart. 
[]()           | Cardinality [] | 128002                                       |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|


   

#### Attribute type
_Charakteristik der Objektart._


   

### Class Fossils_PT ###
Die Klasse Fossils_PT enthält alle Fossilfundstellen.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 12901                                       |  
2 | **division**                | [CodedDomain](#fossils-pt-division)                    | Fossilienkategorie, zu welcher die Objektinstanz gehört. 
[]()           | Cardinality [0..1] |                                                      |  
3 | **system**                | table                                    | Fossiliengruppe. 
[]()           | Cardinality [0..1] | gc_system                                       |  
4 | **dat_meth**                | [CodedDomain](#fossils-pt-dat-meth)                    | Datierungsmethode. 
[]()           | Cardinality [0..1] |                                                      |  
5 | **status**                | [CodedDomain](#fossils-pt-status)                    | Zustand der Objektart 
[]()           | Cardinality [0..1] |                                                      |  
6 | **protected**                | boolean                                    | Geschützte Fossilfundstelle (ja / nein)? 
[]()           | Cardinality [0..1] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12901001 | Lfos Fossilfundstelle | Lfos Fossilfundstelle     |


   

#### Attribute division{#fossils-pt-division}
_Fossilienkategorie, zu welcher die Objektinstanz gehört._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12902006 | Einzeller | Einzeller     |
|12902002 | Pflanzen- und Tierreste | Pflanzen- und Tierreste     |
|12902003 | Pflanzenreste | Pflanzenreste     |
|12902004 | Spuren | Spuren     |
|12902001 | Tierreste | Tierreste     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute system
_Fossiliengruppe._


   

#### Attribute dat_meth{#fossils-pt-dat-meth}
_Datierungsmethode._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12904001 | radiometrisch datiert | radiometrisch datiert     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute status{#fossils-pt-status}
_Zustand der Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12905001 | aufgeschlossen | aufgeschlossen     |
|12905002 | wieder verdeckt | wieder verdeckt     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute protected
_Geschützte Fossilfundstelle (ja / nein)?_
_Datentyp:  boolean_



   

### Class Indication_of_Resources_PT ###
Die Klasse Indication_of_Resources_PT beinhaltet Fundstellen von vulkanischen, mineralischen
und nicht-mineralischen Rohstoffen.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 13201                                       |  
2 | **status**                | [CodedDomain](#indication-of-resources-pt-status)                    | Zustand der Objektart 
[]()           | Cardinality [0..1] |                                                      |  
3 | **material**                | [CodedDomain](#indication-of-resources-pt-material)                    | Material, das mit der Objektart in Verbindung steht 
[]()           | Cardinality [0..1] |                                                      |  
4 | **chemistry**                | string                                    | Chemische Komponente(n) oder Mineralien, welche die Natur der Objektart charakterisieren. 
[]()           | Cardinality [0..1] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13201001 | Lres Mineralfundstelle | Lres Mineralfundstelle     |
|13201002 | Lres Gasquelle | Lres Gasquelle     |
|13201003 | Lres Anzeichen auf Öl | Lres Anzeichen auf Öl     |
|13201006 | Lres Fundstelle vulkanischer Auswürflinge (Tephra) | Lres Fundstelle vulkanischer Auswürflinge (Tephra)     |
|13201007 | Lres Fundstelle von Ries-Auswürflingen | Lres Fundstelle von Ries-Auswürflingen     |
|13201008 | Lres Asphalt, vereinzeltes Vorkommen | Lres Asphalt, vereinzeltes Vorkommen     |
|13201005 | Lres Fundstelle von vulkanischem Tuffit | Lres Fundstelle von vulkanischem Tuffit     |
|13201004 | Lres Tasche, Karsttasche, Kluft, mit Füllung von siderolithischem Sediment | Lres Tasche, Karsttasche, Kluft, mit Füllung von siderolithischem Sediment     |
|13201009 | Lres Meteoritenfundstelle | Lres Meteoritenfundstelle     |


   

#### Attribute status{#indication-of-resources-pt-status}
_Zustand der Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13202001 | aufgeschlossen | aufgeschlossen     |
|13202002 | wieder verdeckt | wieder verdeckt     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute material{#indication-of-resources-pt-material}
_Material, das mit der Objektart in Verbindung steht_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13203003 | Bohnerz | Bohnerz     |
|13203001 | Boluston | Boluston     |
|13203004 | Glas- / Quarzsand | Glas- / Quarzsand     |
|13203002 | Huppererde | Huppererde     |
|13203005 | Walkerde | Walkerde     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute chemistry
_Chemische Komponente(n) oder Mineralien, welche die Natur der Objektart charakterisieren._
_Datentyp:  string_



   

### Class Mineralised_Zone_L ###





    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 13301                                       |  
2 | **chemistry**                | string                                    | Chemische Komponente(n), welche die Natur der Objektart charakterisieren. 
[]()           | Cardinality [0..1] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13301001 | Lmin Vererzungszone | Lmin Vererzungszone     |


   

#### Attribute chemistry
_Chemische Komponente(n), welche die Natur der Objektart charakterisieren._
_Datentyp:  string_



   

### Class Sedimentary_Structures_PT ###





    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 13401                                       |  
2 | **azimuth**                | integer                                    | Orientierung des Symbols. Wert in Grad (0° 359°) im Uhrzeigersinn gemessen. 
[]()           | Cardinality [0..1] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13401001 | Lsed Sedimentstrukturen | Lsed Sedimentstrukturen     |
|13401002 | Lsed Riffstrukturen | Lsed Riffstrukturen     |
|13401003 | Lsed Erosions- oder Omissionsfläche, Hartgrund, Kondensationshorizont | Lsed Erosions- oder Omissionsfläche, Hartgrund, Kondensationshorizont     |
|13401004 | Lsed stratigraphische Lage (Polarität) einer Schichtserie | Lsed stratigraphische Lage (Polarität) einer Schichtserie     |
|13401005 | Lsed Winkeldiskordanz | Lsed Winkeldiskordanz     |
|13401006 | Lsed Entwässerungstrichter (blow-out structure) | Lsed Entwässerungstrichter (blow-out structure)     |


   

#### Attribute azimuth
_Orientierung des Symbols. Wert in Grad (0° 359°) im Uhrzeigersinn gemessen._
_Datentyp:  integer_



   

### Class Type_Localities_PT ###
Die Klasse Type_Localities_PT beinhaltet diejenigen Objektarten, die Typlokalitäten oder wichtige
geologische Aufschlüsse beschreiben.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 13501                                       |  
2 | **strati**                | [CodedDomain](#type-localities-pt-strati)                    | Lithostratigraphischer Zusatz zum Objekt 
[]()           | Cardinality [0..1] |                                                      |  
3 | **name**                | string                                    | Name der Typlokalität. / Beschreibung des geologisch relevanten Aufschlusses 
[]()           | Cardinality [0..1] |                                        |  
4 | **accessibil**                | boolean                                    | Ist die Objektart zum Zeitpunkt der Aufnahme aufgeschlossen (ja / nein)? 
[]()           | Cardinality [0..1] |                                        |  
5 | **protected**                | boolean                                    | Geschütztes geologisches Objekt (ja / nein)? 
[]()           | Cardinality [0..1] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13501001 | Ltyp geologisch relevanter Aufschluss | Ltyp geologisch relevanter Aufschluss     |
|13501003 | Ltyp Typusprofil | Ltyp Typusprofil     |


   

#### Attribute strati{#type-localities-pt-strati}
_Lithostratigraphischer Zusatz zum Objekt_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13502005 | Bank | Bank     |
|13502003 | Formation | Formation     |
|13502001 | Gruppe | Gruppe     |
|13502004 | Member | Member     |
|13502006 | Stufe | Stufe     |
|13502002 | Subgruppe | Subgruppe     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute name
_Name der Typlokalität. / Beschreibung des geologisch relevanten Aufschlusses_
_Datentyp:  string_



   

#### Attribute accessibil
_Ist die Objektart zum Zeitpunkt der Aufnahme aufgeschlossen (ja / nein)?_
_Datentyp:  boolean_



   

#### Attribute protected
_Geschütztes geologisches Objekt (ja / nein)?_
_Datentyp:  boolean_



   

### Class Prominent_Lithological_Features_L ###
In der Klasse Prominent_Lithological_Features_L befinden sich linienförmige Gesteinshorizonte.
Diese Gesteinshorizonte haben bloss Hinweischarakter (z.B. «markante Sandsteinbank» innerhalb
von Wechsellagerungen von Sandstein und Mergel) und sind von den Leithorizonten (z.B.
«Spatkalk im Hauptrogenstein») zu unterschieden. Leithorizonte befinden sich im Thema Rock Bodies.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 13101                                       |  
2 | **cong_spe**                | [CodedDomain](#prominent-lithological-features-l-cong-spe)                    | Charakterisation der Konglomerate nach ihrem Geröllspektrum. 
[]()           | Cardinality [0..1] |                                                      |  
3 | **name_horiz**                |                                     | Name des Bentonit-Leithorizonts. 
[]()           | Cardinality [0..1] | 13103                                       |  
4 | **orig_descr**                | string                                    | Originalbezeichnung gemäss der Legende der zugrundeliegenden geologischen Karte. 
[]()           | Cardinality [0..1] |                                        |  
5 | **litho**                | table                                    | Materialbezeichnung (lithologische Einheit). 
[]()           | Cardinality [1] | gc_litho                                       |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13101001 | Lpro Gesteinshorizont | Lpro Gesteinshorizont     |


   

#### Attribute cong_spe{#prominent-lithological-features-l-cong-spe}
_Charakterisation der Konglomerate nach ihrem Geröllspektrum._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13102003 | bunte bis polygene Nagelfluh | bunte bis polygene Nagelfluh     |
|13102004 | Flyschsandstein-Nagelfluh, Riesenkonglomerat | Flyschsandstein-Nagelfluh, Riesenkonglomerat     |
|13102001 | kristallinfreie bis -arme (Kalk-)Nagelfluh | kristallinfreie bis -arme (Kalk-)Nagelfluh     |
|13102002 | kristallinführende (Kalk-)Nagelfluh | kristallinführende (Kalk-)Nagelfluh     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute name_horiz
_Name des Bentonit-Leithorizonts._


   

#### Attribute orig_descr
_Originalbezeichnung gemäss der Legende der zugrundeliegenden geologischen Karte._
_Datentyp:  string_



   

#### Attribute litho
_Materialbezeichnung (lithologische Einheit)._


   

### Class Miscellaneous_PT ###
Die Klasse Miscellaneous_PT ist für lokale, sehr spezielle geologische Objekte reserviert, die für die
Gesamtheit der geologischen Daten irrelevant sind und deshalb im Datenmodell Geologie nicht
standardisiert werden




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 15501                                       |  
2 | **orig_name**                | string                                    | Ursprüngliche Bezeichnung des Objektes. 
[]()           | Cardinality [1] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|15501001 | Lmis Diverse | Lmis Diverse     |


   

#### Attribute orig_name
_Ursprüngliche Bezeichnung des Objektes._
_Datentyp:  string_



   

### Class Geological_Outlines_L ###
Die Klasse Geological_Outlines_L beinhaltet geologische Konturen. Darunter fallen die Umrisse
von Fest- und Lockergesteinen, von tektonisierten Zonen, sowie die Umgrenzungen von
Rutschungs- und Sackungsmassen, welche nicht durch andere Konturarten (z.B. tektonische
Grenzen) abgegrenzt werden.
Eine geologische Kontur mit Status im Allgemeinen umfasst stratigraphische und petrographische
Grenzen. Geologische Konturen, welche von quartären Ablagerungen, Gewässern oder
Gletschern bedeckt sind oder graduelle Übergänge in Locker- und Festgesteinen (keine klaren
lithologischen Grenzen; im Sinne der Signaturgrenze nach dem Zeichenverzeichnis (ZV)), haben
den Status vermutet. Künstliche geologische Konturen sind Konturen, welche Gebiete mit
detaillierter Information von Gebieten mit geringerer Informationsdichte aufgrund fehlender
Informationen oder aus darstellerischen Gründen (Digitalisierungsmassstab)
ab-grenzen (Abgrenzungskontur nach dem ZV).




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 13001                                       |  
2 | **status**                | [CodedDomain](#geological-outlines-l-status)                    | Zustand der Objektart. 
[]()           | Cardinality [0..1] |                                                      |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13001001 | Lgeo geologische Kontur | Lgeo geologische Kontur     |


   

#### Attribute status{#geological-outlines-l-status}
_Zustand der Objektart._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13002004 | gesichert, tektonisch überprägt | gesichert, tektonisch überprägt     |
|13002001 | im Allgemeinen | im Allgemeinen     |
|13002003 | künstlich | künstlich     |
|13002002 | vermutet | vermutet     |
|13002005 | vermutet, tektonisch überprägt | vermutet, tektonisch überprägt     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |
|13002006 | Gewässerlinie | Gewässerlinie     |


   





## Theme PARAMETER_AND_MODELLING ##

### Class Slope_Bedrock_PT ###
Die Klasse Slope_Bedrock_PT enthält Punktinformationen aus Modellierungen des Festgestein-
verlaufs im Untergrund.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 14201                                       |  
2 | **type**                | [CodedDomain](#slope-bedrock-pt-type)                    | Referenzoberfläche. 
[]()           | Cardinality [1] |                                                      |  
3 | **azimuth**                | integer                                    | Fallrichtung (Azimut) der jeweiligen Punktobjektart. Wert in Grad (0° 359°) im Uhrzeigersinn gemessen. 
[]()           | Cardinality [0..1] |                                        |  
4 | **dip**                | integer                                    | Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die
Vertikale (90°). 
[]()           | Cardinality [0..1] |                                        |  
5 | **litstrat**                | table                                    | Lithostratigraphische Einheit der modellierten Formation 
[]()           | Cardinality [1] | gc_litstrat_bed                                       |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14201001 | Pslo Neigungsrichtung | Pslo Neigungsrichtung     |


   

#### Attribute type{#slope-bedrock-pt-type}
_Referenzoberfläche._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14202001 | Felsoberfläche | Felsoberfläche     |
|14202002 | Obergrenze einer gegebenen Formation | Obergrenze einer gegebenen Formation     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute azimuth
_Fallrichtung (Azimut) der jeweiligen Punktobjektart. Wert in Grad (0° 359°) im Uhrzeigersinn gemessen._
_Datentyp:  integer_



   

#### Attribute dip
_Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die
Vertikale (90°)._
_Datentyp:  integer_



   

#### Attribute litstrat
_Lithostratigraphische Einheit der modellierten Formation_


   

### Class Contour_Lines_Bedrock_L ###
Die Klasse Contour_Lines_Bedrock_L beinhaltet Isohypsen, die sich auf den Verlauf des Fest-
gesteins beziehen und die das Resultat von Modellierungen darstellen. U.a. befinden sich die Iso-
hypsen der Felsoberfläche in dieser Klasse.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 13901                                       |  
2 | **type**                | [CodedDomain](#contour-lines-bedrock-l-type)                    | Referenzoberfläche. 
[]()           | Cardinality [1] |                                                      |  
3 | **altitude**                | float                                    | Höhenangabe (m ü.M.) von Isohypsen. 
[]()           | Cardinality [1] |                                        |  
4 | **litstrat**                | table                                    | Lithostratigraphische Einheit der modellierten Formation 
[]()           | Cardinality [1] | gc_litstrat_bed                                       |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13901001 | Pcob Isohypse | Pcob Isohypse     |


   

#### Attribute type{#contour-lines-bedrock-l-type}
_Referenzoberfläche._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|13902001 | Felsoberfläche | Felsoberfläche     |
|13902002 | Obergrenze einer gegebenen Formation | Obergrenze einer gegebenen Formation     |
|13902003 | Untergrenze einer gegebenen Formation | Untergrenze einer gegebenen Formation     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute altitude
_Höhenangabe (m ü.M.) von Isohypsen._
_Datentyp:  float_



   

#### Attribute litstrat
_Lithostratigraphische Einheit der modellierten Formation_


   

### Class Modelled_Water_Table_PT ###
Die Klasse Modelled_Water_Table_PT enthält Punktinformationen aus Modellierungen des
Grundwasserspiegels.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 14101                                       |  
2 | **azimuth**                | integer                                    | Fallrichtung (Azimut) der jeweiligen Punktobjektart. Wert in Grad (0° 359°) im Uhrzeigersinn gemessen. 
[]()           | Cardinality [0..1] |                                        |  
3 | **dip**                | integer                                    | Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die
Vertikale (90°). 
[]()           | Cardinality [0..1] |                                        |  
4 | **height**                | float                                    | Kote des Grundwasserspiegels (m ü.M.). 
[]()           | Cardinality [0..1] |                                        |  
5 | **mea_period**                | range                                    | Messperiode. 
[]()           | Cardinality [0..1] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14101001 | Pmod Grundwasserfliessrichtung | Pmod Grundwasserfliessrichtung     |
|14101002 | Pmod mittlere Höhe des Grundwasserspiegels | Pmod mittlere Höhe des Grundwasserspiegels     |


   

#### Attribute azimuth
_Fallrichtung (Azimut) der jeweiligen Punktobjektart. Wert in Grad (0° 359°) im Uhrzeigersinn gemessen._
_Datentyp:  integer_



   

#### Attribute dip
_Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die
Vertikale (90°)._
_Datentyp:  integer_



   

#### Attribute height
_Kote des Grundwasserspiegels (m ü.M.)._
_Datentyp:  float_



   

#### Attribute mea_period
_Messperiode._
_Datentyp:  range_



   

### Class Contour_Lines_Hydro_L ###
In der Klasse Contour_Lines_Hydro_L befinden sich die Isohypsen, die sich auf das Grundwasser
beziehen.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 14001                                       |  
2 | **confine**                | [CodedDomain](#contour-lines-hydro-l-confine)                    | Druckzustand im Grundwasserleiter. 
[]()           | Cardinality [0..1] |                                                      |  
3 | **altitude**                |                                     | Höhenangabe (m ü.M.) von Isohypsen. 
[]()           | Cardinality [1] |                                        |  
4 | **wa_table**                | [CodedDomain](#contour-lines-hydro-l-wa-table)                    | Wasserstand. 
[]()           | Cardinality [0..1] |                                                      |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14001001 | Pcoh Isohypse des Grundwasserspiegels | Pcoh Isohypse des Grundwasserspiegels     |


   

#### Attribute confine{#contour-lines-hydro-l-confine}
_Druckzustand im Grundwasserleiter._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14002003 | artesisch | artesisch     |
|14002001 | frei | frei     |
|14002002 | gespannt | gespannt     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute altitude
_Höhenangabe (m ü.M.) von Isohypsen._


   

#### Attribute wa_table{#contour-lines-hydro-l-wa-table}
_Wasserstand._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|14004002 | mittlere Höhe des Hochwasserstands | mittlere Höhe des Hochwasserstands     |
|14004001 | mittlere Höhe des Niedrigwasserstands | mittlere Höhe des Niedrigwasserstands     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   





## Theme ANTHROPOGENIC_FEATURES ##

### Class Archaeology_PT ###
Die Klasse Archaeology_PT enthält Objektarten zu einzelnen archäologischen Relikten.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [] | 10101                                       |  
2 | **epoch**                | [CodedDomain](#archaeology-pt-epoch)                    | Archäologische Epoche der Objektart 
[]()           | Cardinality [0..1] |                                                      |  
3 | **period**                | [CodedDomain](#archaeology-pt-period)                    | Archäologische Periode der Objektart. 
[]()           | Cardinality [0..1] |                                                      |  
4 | **age**                | [CodedDomain](#archaeology-pt-age)                    | Archäologisches Alter der Objektart. 
[]()           | Cardinality [0..1] |                                                      |  
5 | **type**                | [CodedDomain](#archaeology-pt-type)                    | Art des Kultsteins. 
[]()           | Cardinality [0..1] |                                                      |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10101001 | Aarc archäologische Fundstelle, Anlage, Siedlungsreste | Aarc archäologische Fundstelle, Anlage, Siedlungsreste     |
|10101005 | Aarc Gräber, Gräberfeld | Aarc Gräber, Gräberfeld     |
|10101007 | Aarc Grabhügel, Dolmengrab | Aarc Grabhügel, Dolmengrab     |
|10101008 | Aarc Kultstein | Aarc Kultstein     |
|10101009 | Aarc Kalkofen | Aarc Kalkofen     |
|10101010 | Aarc Felsenkeller | Aarc Felsenkeller     |
|10101011 | Aarc Schlackenhalde | Aarc Schlackenhalde     |
|10101012 | Aarc Glashütte | Aarc Glashütte     |
|10101013 | Aarc Schmelzofen | Aarc Schmelzofen     |
|10101004 | Aarc Burgstelle, Burghügel, Wachtturm | Aarc Burgstelle, Burghügel, Wachtturm     |
|10101002 | Aarc Höhlensiedlung, Abri | Aarc Höhlensiedlung, Abri     |
|10101003 | Aarc Pfahlbauten | Aarc Pfahlbauten     |
|10101006 | Aarc Steinplattengrab | Aarc Steinplattengrab     |
|10101015 | Aarc Abbaustelle | Aarc Abbaustelle     |


   

#### Attribute epoch{#archaeology-pt-epoch}
_Archäologische Epoche der Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10002001 | historisch | historisch     |
|10002002 | prähistorisch | prähistorisch     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute period{#archaeology-pt-period}
_Archäologische Periode der Objektart._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10003005 | Bronzezeit | Bronzezeit     |
|10003004 | Eisenzeit | Eisenzeit     |
|10003002 | Mittelalter | Mittelalter     |
|10003001 | Neuzeit | Neuzeit     |
|10003003 | Römerzeit | Römerzeit     |
|10003006 | Steinzeit | Steinzeit     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute age{#archaeology-pt-age}
_Archäologisches Alter der Objektart._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10004005 | Altbronzezeit | Altbronzezeit     |
|10004002 | Hallstattzeit | Hallstattzeit     |
|10004003 | Jungbronzezeit | Jungbronzezeit     |
|10004001 | Latènezeit | Latènezeit     |
|10004007 | Mesolithikum | Mesolithikum     |
|10004004 | Mittelbronzezeit | Mittelbronzezeit     |
|10004006 | Neolithikum | Neolithikum     |
|10004008 | Paläolithikum | Paläolithikum     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute type{#archaeology-pt-type}
_Art des Kultsteins._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10105001 | Menhir | Menhir     |
|10105002 | Schalenstein | Schalenstein     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

### Class Archaeology_L ###
Die Klasse Archaeology_L umfasst linienförmige archäologische Elemente. Historische Strassen,
Hohlwege oder Befestigungsgräben sind Teile dieser Klasse.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [] | 10201                                       |  
2 | **epoch**                | [CodedDomain](#archaeology-l-epoch)                    | Archäologische Epoche der Objektart 
[]()           | Cardinality [0..1] |                                                      |  
3 | **period**                | [CodedDomain](#archaeology-l-period)                    | Archäologische Periode der Objektart. 
[]()           | Cardinality [0..1] |                                                      |  
4 | **age**                | [CodedDomain](#archaeology-l-age)                    | Archäologisches Alter der Objektart. 
[]()           | Cardinality [0..1] |                                                      |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10201001 | Aarc Verkehrsweg | Aarc Verkehrsweg     |
|10201002 | Aarc Hohlweg | Aarc Hohlweg     |
|10201003 | Aarc künstlicher Graben, Befestigungsgraben | Aarc künstlicher Graben, Befestigungsgraben     |
|10201004 | Aarc künstlicher Erdwall | Aarc künstlicher Erdwall     |
|10201005 | Aarc Wasserleitung | Aarc Wasserleitung     |
|10201006 | Aarc Steinreihe | Aarc Steinreihe     |
|10201007 | Aarc Schützengraben | Aarc Schützengraben     |


   

#### Attribute epoch{#archaeology-l-epoch}
_Archäologische Epoche der Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10002001 | historisch | historisch     |
|10002002 | prähistorisch | prähistorisch     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute period{#archaeology-l-period}
_Archäologische Periode der Objektart._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10003005 | Bronzezeit | Bronzezeit     |
|10003004 | Eisenzeit | Eisenzeit     |
|10003002 | Mittelalter | Mittelalter     |
|10003001 | Neuzeit | Neuzeit     |
|10003003 | Römerzeit | Römerzeit     |
|10003006 | Steinzeit | Steinzeit     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute age{#archaeology-l-age}
_Archäologisches Alter der Objektart._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10004005 | Altbronzezeit | Altbronzezeit     |
|10004002 | Hallstattzeit | Hallstattzeit     |
|10004003 | Jungbronzezeit | Jungbronzezeit     |
|10004001 | Latènezeit | Latènezeit     |
|10004007 | Mesolithikum | Mesolithikum     |
|10004004 | Mittelbronzezeit | Mittelbronzezeit     |
|10004006 | Neolithikum | Neolithikum     |
|10004008 | Paläolithikum | Paläolithikum     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

### Class Archaeology_PLG ###
Die Klasse Archaeology_PLG beinhaltet archäologische Relikte (z.B. römisches Castrum), die ein
grösseres Gebiet (Fläche) abdecken.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [] | 10301                                       |  
2 | **epoch**                | [CodedDomain](#archaeology-plg-epoch)                    | Archäologische Epoche der Objektart 
[]()           | Cardinality [0..1] |                                                      |  
3 | **period**                | [CodedDomain](#archaeology-plg-period)                    | Archäologische Periode der Objektart. 
[]()           | Cardinality [0..1] |                                                      |  
4 | **age**                | [CodedDomain](#archaeology-plg-age)                    | Archäologisches Alter der Objektart. 
[]()           | Cardinality [0..1] |                                                      |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10301001 | Aarc Castrum | Aarc Castrum     |
|10301002 | Aarc Refugium, Höhensiedlung, Erdwerk | Aarc Refugium, Höhensiedlung, Erdwerk     |


   

#### Attribute epoch{#archaeology-plg-epoch}
_Archäologische Epoche der Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10002001 | historisch | historisch     |
|10002002 | prähistorisch | prähistorisch     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute period{#archaeology-plg-period}
_Archäologische Periode der Objektart._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10003005 | Bronzezeit | Bronzezeit     |
|10003004 | Eisenzeit | Eisenzeit     |
|10003002 | Mittelalter | Mittelalter     |
|10003001 | Neuzeit | Neuzeit     |
|10003003 | Römerzeit | Römerzeit     |
|10003006 | Steinzeit | Steinzeit     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute age{#archaeology-plg-age}
_Archäologisches Alter der Objektart._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10004005 | Altbronzezeit | Altbronzezeit     |
|10004002 | Hallstattzeit | Hallstattzeit     |
|10004003 | Jungbronzezeit | Jungbronzezeit     |
|10004001 | Latènezeit | Latènezeit     |
|10004007 | Mesolithikum | Mesolithikum     |
|10004004 | Mittelbronzezeit | Mittelbronzezeit     |
|10004006 | Neolithikum | Neolithikum     |
|10004008 | Paläolithikum | Paläolithikum     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

### Class Exploitation_Geomaterials_PT ###
Die Klasse Exploitation_Geomaterials_PT enthält punktförmige Angaben zu Abbaustellen von
Geomaterialien.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [] | 10601                                       |  
2 | **exp_unit**                | table                                    | Abgebaute lithostratigraphische Einheit. 
[]()           | Cardinality [0..*] | gc_litstrat_bed                                       |  
3 | **status**                | [CodedDomain](#exploitation-geomaterials-pt-status)                    | Abbaustatus. 
[]()           | Cardinality [0..1] |                                                      |  
4 | **depth_tot**                | float                                    | Endtiefe (m ab Terrainoberfläche) der Objektart. 
[]()           | Cardinality [0..1] |                                        |  
5 | **targ_mat**                | [CodedDomain](#exploitation-geomaterials-pt-targ-mat)                    | Abgebautes Material. 
[]()           | Cardinality [0..1] |                                                      |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10601001 | Aexp Bergwerk, Untertageabbau | Aexp Bergwerk, Untertageabbau     |
|10601002 | Aexp Stolleneingang | Aexp Stolleneingang     |
|10601003 | Aexp Schacht | Aexp Schacht     |
|10601004 | Aexp Pinge (dolinenartiger Stolleneinbruch) | Aexp Pinge (dolinenartiger Stolleneinbruch)     |
|10601005 | Aexp Schürfloch | Aexp Schürfloch     |
|10601006 | Aexp ausgeräumte Bohnerztasche | Aexp ausgeräumte Bohnerztasche     |


   

#### Attribute exp_unit
_Abgebaute lithostratigraphische Einheit._


   

#### Attribute status{#exploitation-geomaterials-pt-status}
_Abbaustatus._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10603003 | aufgefüllt | aufgefüllt     |
|10603001 | in Betrieb | in Betrieb     |
|10603002 | stillgelegt | stillgelegt     |
|10603004 | verfallen | verfallen     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute depth_tot
_Endtiefe (m ab Terrainoberfläche) der Objektart._
_Datentyp:  float_



   

#### Attribute targ_mat{#exploitation-geomaterials-pt-targ-mat}
_Abgebautes Material._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10605010 | Antimon | Antimon     |
|10605023 | Asbest | Asbest     |
|10605029 | Asphalt / Bitumen | Asphalt / Bitumen     |
|10605011 | Baryt | Baryt     |
|10605006 | Blei-Zink | Blei-Zink     |
|10605022 | Bohnerz | Bohnerz     |
|10605007 | Chrom-Nickel, z.T. mit Kobalt | Chrom-Nickel, z.T. mit Kobalt     |
|10605031 | Dachschiefer / Tafelschiefer | Dachschiefer / Tafelschiefer     |
|10605005 | Eisen / Eisenoolith | Eisen / Eisenoolith     |
|10605001 | Erze allgemein | Erze allgemein     |
|10605013 | Fluorit | Fluorit     |
|10605034 | Gips | Gips     |
|10605002 | Gold | Gold     |
|10605027 | Graphit | Graphit     |
|10605030 | Hartgestein | Hartgestein     |
|10605012 | Kalzit | Kalzit     |
|10605015 | Kaolin | Kaolin     |
|10605040 | Kies | Kies     |
|10605024 | Kohle allgemein | Kohle allgemein     |
|10605004 | Kupfer, z.T. mit Silber, Wismut und Arsen | Kupfer, z.T. mit Silber, Wismut und Arsen     |
|10605026 | Lignit | Lignit     |
|10605016 | Magnesit | Magnesit     |
|10605017 | Magnesium | Magnesium     |
|10605008 | Mangan | Mangan     |
|10605009 | Molybdän und Wolfram | Molybdän und Wolfram     |
|10605028 | Ölschiefer | Ölschiefer     |
|10605018 | Phosphorit, Apatit | Phosphorit, Apatit     |
|10605039 | Pyrit | Pyrit     |
|10605014 | Quarz | Quarz     |
|10605035 | Salz / Steinsalz | Salz / Steinsalz     |
|10605037 | Sand | Sand     |
|10605038 | Sand und Kies | Sand und Kies     |
|10605020 | Schwefel | Schwefel     |
|10605032 | Serpentin | Serpentin     |
|10605003 | Silber | Silber     |
|10605033 | Speckstein | Speckstein     |
|10605025 | Steinkohle / Anthrazit | Steinkohle / Anthrazit     |
|10605019 | Talk | Talk     |
|10605036 | Ton / Ton und Silt (Lehm) | Ton / Ton und Silt (Lehm)     |
|10605021 | Uran | Uran     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

### Class Exploitation_Geomaterials_L ###
Die Klasse Exploitation_Geomaterials_L beinhaltet linienförmige Informationen zum Abbau von
Geomaterialien (z.B. Verlauf der Abbaufront).




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [] | 10701                                       |  
2 | **status**                | [CodedDomain](#exploitation-geomaterials-l-status)                    | Abbaustatus. 
[]()           | Cardinality [0..1] |                                                      |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10701001 | Aexp Abbaufront | Aexp Abbaufront     |
|10701002 | Aexp Bergwerksstollen | Aexp Bergwerksstollen     |


   

#### Attribute status{#exploitation-geomaterials-l-status}
_Abbaustatus._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10702003 | aufgefüllt | aufgefüllt     |
|10702001 | in Betrieb | in Betrieb     |
|10702002 | stillgelegt | stillgelegt     |
|10702004 | verfallen | verfallen     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

### Class Exploitation_Geomaterials_PLG ###
Die Klasse Exploitation_Geomaterials_PLG enthält Flächen, wo zur Zeit der geologischen
Aufnahmen Geomaterialien abgebaut wurden.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [] | 10801                                       |  
2 | **exp_unit**                | table                                    | Abgebaute lithostratigraphische Einheit. 
[]()           | Cardinality [1..*] | gc_litstrat_bed                                       |  
3 | **status**                | [CodedDomain](#exploitation-geomaterials-plg-status)                    | Abbaustatus. 
[]()           | Cardinality [0..1] |                                                      |  
4 | **depth_tot**                | float                                    | Endtiefe (m ab Terrainoberfläche) der Objektart. 
[]()           | Cardinality [0..1] |                                        |  
5 | **targ_mat**                | [CodedDomain](#exploitation-geomaterials-plg-targ-mat)                    | Abgebautes Material. 
[]()           | Cardinality [0..1] |                                                      |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10801001 | Aexp Steinbruch | Aexp Steinbruch     |
|10801002 | Aexp Grube (Lockergesteinsabbau) | Aexp Grube (Lockergesteinsabbau)     |


   

#### Attribute exp_unit
_Abgebaute lithostratigraphische Einheit._


   

#### Attribute status{#exploitation-geomaterials-plg-status}
_Abbaustatus._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10802003 | aufgefüllt | aufgefüllt     |
|10802001 | in Betrieb | in Betrieb     |
|10802002 | stillgelegt | stillgelegt     |
|10802004 | verfallen | verfallen     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute depth_tot
_Endtiefe (m ab Terrainoberfläche) der Objektart._
_Datentyp:  float_



   

#### Attribute targ_mat{#exploitation-geomaterials-plg-targ-mat}
_Abgebautes Material._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10804015 | Asbest | Asbest     |
|10804010 | Baryt | Baryt     |
|10804016 | Bohnerz | Bohnerz     |
|10804005 | Dachschiefer / Tafelschiefer | Dachschiefer / Tafelschiefer     |
|10804012 | Eisen / Eisenoolithe | Eisen / Eisenoolithe     |
|10804006 | Gips | Gips     |
|10804004 | Hartgestein | Hartgestein     |
|10804011 | Kalzit / Kalk | Kalzit / Kalk     |
|10804013 | Kaolin | Kaolin     |
|10804021 | Kies | Kies     |
|10804019 | Kohle | Kohle     |
|10804018 | Mergel | Mergel     |
|10804014 | Quarz / Quarzit | Quarz / Quarzit     |
|10804020 | Salz / Steinsalz | Salz / Steinsalz     |
|10804002 | Sand | Sand     |
|10804003 | Sand und Kies | Sand und Kies     |
|10804007 | Serpentin | Serpentin     |
|10804008 | Speckstein | Speckstein     |
|10804009 | Talk | Talk     |
|10804001 | Ton / Ton und Silt (Lehm) | Ton / Ton und Silt (Lehm)     |
|10804017 | Torf | Torf     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

### Class Boreholes_PT ###
Die Klasse Boreholes_PT beinhaltet Bohrungen und Sondierungen. (Auf alten gedruckten Karten
wurde die Art der Sondierung nicht immer unterschieden. Es kann daher sein, dass in alten Karten
Rammkernsondierungen als Bohrungen aufgenommen wurden.)




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [] | 10501                                       |  
2 | **drill_mo**                |                                     | Bohrmethode. 
[]()           | Cardinality [0..1] | 10502                                       |  
3 | **depth_bedrock**                | float                                    | Tiefe (in Meter ab Terrainoberfläche) der Felsober-
fläche. (Sofern die Bohrung das Festgestein nicht
Depth_Bedrock erreicht, z.B. «Bohrung, Fels nicht erreicht», beträgt der
Wert -9999, falls die Bohrung bereits im Festgestein beginnt, beträgt
der Wert 0). Falls Festgestein erreicht wurde, aber nicht klar ist,
dass es sich um die Felsoberfläche handelt, beträgt der Wert -8888. 
[]()           | Cardinality [0..1] |                                        |  
4 | **d_c_underg**                | boolean                                    | Bohransatzpunkt unter Terrain (ja / nein) 
[]()           | Cardinality [1] |                                        |  
5 | **main_tar**                | [CodedDomain](#boreholes-pt-main-tar)                    | Ziel der Sondierung. 
[]()           | Cardinality [0..1] |                                                      |  
6 | **targ_mat**                | [CodedDomain](#boreholes-pt-targ-mat)                    | Durch die Sondierung gefördertes Material. 
[]()           | Cardinality [0..1] |                                                      |  
7 | **depth_tot**                | float                                    | Gemessene Länge (Measured Depth) der Bohrung. Vgl.
DM Bohrdaten. Die tatsächliche Tiefe (True Vertical
Depth) ist oft nicht bekannt. 
[]()           | Cardinality [0..1] |                                        |  
8 | **fm_a**                | table                                    | Lithostratigraphische Einheit der erreichten Formation A 
[]()           | Cardinality [0..1] | gc_litstrat_bed                                       |  
9 | **depth_fm_a**                | float                                    | Tiefe (m ab Terrainoberfläche) der erreichten Formation A. 
[]()           | Cardinality [0..1] |                                        |  
10 | **fm_b**                | table                                    | Lithostratigraphische Einheit der erreichten Formation B 
[]()           | Cardinality [0..1] | gc_litstrat_bed                                       |  
11 | **depth_fm_b**                | float                                    | Tiefe (m ab Terrainoberfläche) der erreichten Formation B. 
[]()           | Cardinality [0..1] |                                        |  
12 | **depth_wt**                | float                                    | Tiefe (m ab Terrainoberfläche) des Grundwasserspiegels. 
[]()           | Cardinality [0..1] |                                        |  
13 | **azimuth**                | integer                                    | Fallrichtung (Azimut) der jeweiligen Punktobjektart. Wert in Grad (0° 359°) im Uhrzeigersinn gemessen. 
[]()           | Cardinality [0..1] |                                        |  
14 | **dip**                | integer                                    | Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die
Vertikale (90°). 
[]()           | Cardinality [0..1] |                                        |  
15 | **ref_number**                | integer                                    | Bohrungs-ID der Objektart in einem zusätzlichen Dokument (Erläuterungen, ...). 
[]()           | Cardinality [0..1] |                                        |  
16 | **link**                | integer                                    | Objektnummer in der Datenbank von INFOGEOL. 
[]()           | Cardinality [0..1] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10501001 | Abor Bohrung | Abor Bohrung     |
|10501002 | Abor Sondierschlitz | Abor Sondierschlitz     |
|10501003 | Abor Handsondierung | Abor Handsondierung     |
|10501004 | Abor Rammsondierung | Abor Rammsondierung     |
|10501005 | Abor Rammkernsondierung | Abor Rammkernsondierung     |


   

#### Attribute drill_mo
_Bohrmethode._


   

#### Attribute depth_bedrock
_Tiefe (in Meter ab Terrainoberfläche) der Felsober-
fläche. (Sofern die Bohrung das Festgestein nicht
Depth_Bedrock erreicht, z.B. «Bohrung, Fels nicht erreicht», beträgt der
Wert -9999, falls die Bohrung bereits im Festgestein beginnt, beträgt
der Wert 0). Falls Festgestein erreicht wurde, aber nicht klar ist,
dass es sich um die Felsoberfläche handelt, beträgt der Wert -8888._
_Datentyp:  float_



   

#### Attribute d_c_underg
_Bohransatzpunkt unter Terrain (ja / nein)_
_Datentyp:  boolean_



   

#### Attribute main_tar{#boreholes-pt-main-tar}
_Ziel der Sondierung._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10505006 | belasteter Standort | belasteter Standort     |
|10505012 | Forschung | Forschung     |
|10505001 | Geotechnik | Geotechnik     |
|10505008 | Geothermie | Geothermie     |
|10505002 | Hydrogeologie | Hydrogeologie     |
|10505005 | Kohlenwasserstoffe | Kohlenwasserstoffe     |
|10505004 | mineralische Rohstoffe | mineralische Rohstoffe     |
|10505013 | Naturgefahren | Naturgefahren     |
|10505007 | Seismik | Seismik     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute targ_mat{#boreholes-pt-targ-mat}
_Durch die Sondierung gefördertes Material._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10506003 | Erdgas | Erdgas     |
|10506002 | Erdöl | Erdöl     |
|10506004 | Erdwärme | Erdwärme     |
|10506006 | Grundwasser | Grundwasser     |
|10506007 | Mineralwasser | Mineralwasser     |
|10506001 | Salz / Steinsalz | Salz / Steinsalz     |
|10506005 | Thermalwasser | Thermalwasser     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute depth_tot
_Gemessene Länge (Measured Depth) der Bohrung. Vgl.
DM Bohrdaten. Die tatsächliche Tiefe (True Vertical
Depth) ist oft nicht bekannt._
_Datentyp:  float_



   

#### Attribute fm_a
_Lithostratigraphische Einheit der erreichten Formation A_


   

#### Attribute depth_fm_a
_Tiefe (m ab Terrainoberfläche) der erreichten Formation A._
_Datentyp:  float_



   

#### Attribute fm_b
_Lithostratigraphische Einheit der erreichten Formation B_


   

#### Attribute depth_fm_b
_Tiefe (m ab Terrainoberfläche) der erreichten Formation B._
_Datentyp:  float_



   

#### Attribute depth_wt
_Tiefe (m ab Terrainoberfläche) des Grundwasserspiegels._
_Datentyp:  float_



   

#### Attribute azimuth
_Fallrichtung (Azimut) der jeweiligen Punktobjektart. Wert in Grad (0° 359°) im Uhrzeigersinn gemessen._
_Datentyp:  integer_



   

#### Attribute dip
_Einfallswert der jeweiligen Punktobjektart. Wert in Grad gemessen aus der Horizontalen (0°) nach unten bis in die
Vertikale (90°)._
_Datentyp:  integer_



   

#### Attribute ref_number
_Bohrungs-ID der Objektart in einem zusätzlichen Dokument (Erläuterungen, ...)._
_Datentyp:  integer_



   

#### Attribute link
_Objektnummer in der Datenbank von INFOGEOL._
_Datentyp:  integer_



   

### Class Artificial_Surface_Modifications_PLG ###
Die Klasse Artificial_Surface_Modifications_PLG enthält bedeutende künstliche Veränderungen
des Geländes (Golfplatz, Skigebiet, etc.), die zur Folge haben, dass das ursprüngliche Relief nicht
mehr zu erkennen ist, was bei einer geomorphologischen Deutung zu falschen Schlüssen führen könnte.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 10401                                       |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|10401001 | Aart künstlich verändertes Gelände | Aart künstlich verändertes Gelände     |
|10401002 | Aart künstliche Ablagerung, undifferenziert | Aart künstliche Ablagerung, undifferenziert     |
|10401003 | Aart Aufschüttung, Damm | Aart Aufschüttung, Damm     |
|10401004 | Aart Auffüllung | Aart Auffüllung     |
|10401005 | Aart Deponie | Aart Deponie     |
|10401006 | Aart Halde | Aart Halde     |


   





## Theme HYDROGEOLOGY ##

### Class Construction_PT ###
Die Klasse Construction_PT beinhaltet Wasserbauten wie Grundwasserfassungen und Zisternen.
Desweiteren kommen in dieser Klasse auch Messgeräte wie Piezometer und Limnigraphen vor.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 12101                                       |  
2 | **status**                | [CodedDomain](#construction-pt-status)                    | Zustand der Objektart. 
[]()           | Cardinality [0..1] |                                                      |  
3 | **epoch**                | [CodedDomain](#construction-pt-epoch)                    | Epoche der Erbauung der Objektart. 
[]()           | Cardinality [0..1] |                                                      |  
4 | **depth**                | float                                    | Tiefe der Objektart (m ab Terrainoberfläche). 
[]()           | Cardinality [0..1] |                                        |  
5 | **depth_wt**                | float                                    | Tiefe (m ab Terrainoberfläche) des Grundwasserspiegels (Mittelwert). 
[]()           | Cardinality [0..1] |                                        |  
6 | **mea_period**                | range                                    | Messperiode. 
[]()           | Cardinality [0..1] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12101001 | Hcon Grundwasserfassung | Hcon Grundwasserfassung     |
|12101002 | Hcon Zisterne | Hcon Zisterne     |
|12101003 | Hcon laufender Brunnen (in wasserarmem Gebiet) | Hcon laufender Brunnen (in wasserarmem Gebiet)     |
|12101004 | Hcon Sodbrunnen | Hcon Sodbrunnen     |
|12101005 | Hcon Versickerungsschacht | Hcon Versickerungsschacht     |
|12101006 | Hcon Limnigraph | Hcon Limnigraph     |
|12101007 | Hcon Piezometer | Hcon Piezometer     |


   

#### Attribute status{#construction-pt-status}
_Zustand der Objektart._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12102001 | in Betrieb | in Betrieb     |
|12102002 | stillgelegt | stillgelegt     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute epoch{#construction-pt-epoch}
_Epoche der Erbauung der Objektart._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12103001 | Mittelalter | Mittelalter     |
|12103003 | prähistorisch | prähistorisch     |
|12103002 | Römerzeit | Römerzeit     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute depth
_Tiefe der Objektart (m ab Terrainoberfläche)._
_Datentyp:  float_



   

#### Attribute depth_wt
_Tiefe (m ab Terrainoberfläche) des Grundwasserspiegels (Mittelwert)._
_Datentyp:  float_



   

#### Attribute mea_period
_Messperiode._
_Datentyp:  range_



   

### Class Construction_L ###
Die Klasse Construction_L enthält linienförmige Wasserbauten wie den Wasserfassungsstollen,
welcher mit Objektarten der Klasse Surface_Water_PT kombiniert werden kann.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 12201                                       |  
2 | **combi**                | [CodedDomain](#construction-l-combi)                    | Objektart einer anderen Klasse, die mit der Objektart in Kombination vorkommen kann 
[]()           | Cardinality [0..1] |                                                      |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12201001 | Hcon Wasserfassungsstollen | Hcon Wasserfassungsstollen     |
|12201002 | Hcon künstlicher Gewässerlauf | Hcon künstlicher Gewässerlauf     |


   

#### Attribute combi{#construction-l-combi}
_Objektart einer anderen Klasse, die mit der Objektart in Kombination vorkommen kann_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12202002 | mit gefasster Mineralquelle (orientiert) in Stollen | mit gefasster Mineralquelle (orientiert) in Stollen     |
|12202003 | mit gefasster Thermalquelle (orientiert) in Stollen | mit gefasster Thermalquelle (orientiert) in Stollen     |
|12202001 | mit Quellfassung (orientiert) in Stollen | mit Quellfassung (orientiert) in Stollen     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

### Class Palaeohydrology_L ###
In der Klasse Palaeohydrology_L befinden sich alle linienförmigen Objektarten, welche einen
gewissen Bezug zu einem ehemaligen Gewässer aufweisen.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 12301                                       |  
2 | **rel_age**                | [CodedDomain](#palaeohydrology-l-rel-age)                    | Relatives Alter der Objektart 
[]()           | Cardinality [0..1] |                                                      |  
3 | **chrono**                | table                                    | Chronostratigraphische Zuordnung. 
[]()           | Cardinality [0..1] | gc_chrono                                       |  
4 | **ref_year**                | integer                                    | Referenzjahr der ehemaligen Uferlinie. 
[]()           | Cardinality [1] |                                        |  
5 | **source**                | string                                    | Datenquelle der historischen Unterlagen. 
[]()           | Cardinality [0..1] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12301001 | Hpal Paläotal | Hpal Paläotal     |
|12301002 | Hpal ehemalige Entwässerungsrinne | Hpal ehemalige Entwässerungsrinne     |
|12301004 | Hpal Trockental | Hpal Trockental     |
|12301005 | Hpal ehemaliges Bachbett | Hpal ehemaliges Bachbett     |
|12301006 | Hpal Ufer eines ehemaligen Flussbetts | Hpal Ufer eines ehemaligen Flussbetts     |
|12301007 | Hpal ehemalige Uferlinie | Hpal ehemalige Uferlinie     |
|12301003 | Hpal ehemalige glaziale Abflussrinne | Hpal ehemalige glaziale Abflussrinne     |


   

#### Attribute rel_age{#palaeohydrology-l-rel-age}
_Relatives Alter der Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12302002 | älter als die Jüngste | älter als die Jüngste     |
|12302003 | älter als die Zweitjüngste | älter als die Zweitjüngste     |
|12302001 | die Jüngste oder Einzige | die Jüngste oder Einzige     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute chrono
_Chronostratigraphische Zuordnung._


   

#### Attribute ref_year
_Referenzjahr der ehemaligen Uferlinie._
_Datentyp:  integer_



   

#### Attribute source
_Datenquelle der historischen Unterlagen._
_Datentyp:  string_



   

### Class Subsurface_Water_L ###
In der Klasse Subsurface_Water_L befinden sich linienförmigen Objektarten, welche einen
unterirdischen Gewässerlauf anzeigen.

Der genaue Verlauf des unterirdischen Gewässerlaufes ist in fast jedem Fall vermutet, mit
wenigen Ausnahmen von erforschten Höhlensystemen. Liegen Färbversuche vor, so werden diese
in den Erläuterungen erwähnt, sofern diese existieren. Der unterirdische Gewässerlauf
kann mit Objeken aus der Klasse Surface_Water_PT kombiniert werden.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 12401                                       |  
2 | **combi**                | [CodedDomain](#subsurface-water-l-combi)                    | Objektart einer anderen Klasse, die mit der Objektart in Kombination vorkommen kann 
[]()           | Cardinality [0..1] |                                                      |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12401001 | Hsub unterirdischer Gewässerlauf | Hsub unterirdischer Gewässerlauf     |


   

#### Attribute combi{#subsurface-water-l-combi}
_Objektart einer anderen Klasse, die mit der Objektart in Kombination vorkommen kann_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12402001 | mit Versickerungsstelle eines Baches | mit Versickerungsstelle eines Baches     |
|12402002 | mit Wiederaustritt eines unterirdischen Bachlaufes | mit Wiederaustritt eines unterirdischen Bachlaufes     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

### Class Surface_Water_PT ###
Die Klasse Surface_Water_PT umfasst lokal (punktuell) beobachtete Oberflächengewässer, wie
natürliche Wasseraustritts- und Versickerungsstellen. Zudem befindet sich die Objektart Steilstufe
in Bachrinne, Wasserfall in dieser Klasse, die eine spezielle Stelle in Fliessgewässern markiert und
die durch die darunterliegende Geologie bedingt ist.
Eine Quelle wird als «Thermalquelle» bezeichnet, wenn das Wasser eine mittlere Jahrestem-
20°C aufweist. Für diesen Quelltyp ist das Attribut «Temp» vorgesehen und
beschränkt sich i.d.R. auf die mittlere Wassertemperatur. Deshalb wird für dieses Attribut auch
kein Datum einer Analyse angegeben. Um eine Mineralquelle handelt es sich bei einer Quelle mit
einer Mineralkonzentration 1g / l Wasser oder einer CO2- 250 mg / l Wasser.
Für diesen Quelltyp ist das Attribut «Chemistry» vorgesehen. D.h. unter diesem Attribut wird das
charakteristische chemische Element im Mineralwasser angegeben und nicht die komplette
Wasserchemie.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 12501                                       |  
2 | **status**                | [CodedDomain](#surface-water-pt-status)                    | Zustand der Objektart. 
[]()           | Cardinality [0..1] |                                                      |  
3 | **flow_con**                | [CodedDomain](#surface-water-pt-flow-con)                    | Wasserfluss Bedingungen. 
[]()           | Cardinality [0..1] |                                                      |  
4 | **type**                | [CodedDomain](#surface-water-pt-type)                    | Charakteristik der Objektart 
[]()           | Cardinality [0..1] |                                                      |  
5 | **dis_loca**                | [CodedDomain](#surface-water-pt-dis-loca)                    | Ort des Wasserausflusses. 
[]()           | Cardinality [0..1] |                                                      |  
6 | **combi**                | [CodedDomain](#surface-water-pt-combi)                    | Objektart einer anderen Klasse, die mit der Objektart in Kombination vorkommen kann 
[]()           | Cardinality [0..1] |                                                      |  
7 | **temp**                | integer                                    | Mittlere Wassertemperatur (°C). 
[]()           | Cardinality [0..1] |                                        |  
8 | **chemistry**                | string                                    | Charakteristisches chemisches Element im Mineralwasser (z.B. Fe). 
[]()           | Cardinality [0..1] |                                        |  
9 | **azimuth**                | integer                                    | Richtung (Azimut) der jeweiligen Punktobjektart. Wert in
Grad (0° 359°) im Uhrzeigersinn gemessen. 
[]()           | Cardinality [0..1] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12501001 | Hsur Quelle | Hsur Quelle     |
|12501002 | Hsur diffuse Quelle | Hsur diffuse Quelle     |
|12501003 | Hsur Wiederaustritt eines unterirdischen Bachlaufes | Hsur Wiederaustritt eines unterirdischen Bachlaufes     |
|12501004 | Hsur Versickerungsstelle eines Baches | Hsur Versickerungsstelle eines Baches     |
|12501005 | Hsur Steilstufe in Bachrinne, Wasserfall | Hsur Steilstufe in Bachrinne, Wasserfall     |
|12501006 | Hsur Grundwasseraufstoss | Hsur Grundwasseraufstoss     |


   

#### Attribute status{#surface-water-pt-status}
_Zustand der Objektart._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12502001 | gefasst | gefasst     |
|12502002 | nicht gefasst | nicht gefasst     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute flow_con{#surface-water-pt-flow-con}
_Wasserfluss Bedingungen._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12503001 | perennierend | perennierend     |
|12503002 | temporär | temporär     |
|12503003 | versiegt | versiegt     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute type{#surface-water-pt-type}
_Charakteristik der Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12504001 | Karstquelle | Karstquelle     |
|12504002 | Mineralquelle | Mineralquelle     |
|12504003 | Thermalquelle | Thermalquelle     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute dis_loca{#surface-water-pt-dis-loca}
_Ort des Wasserausflusses._

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12505002 | in Stollen | in Stollen     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute combi{#surface-water-pt-combi}
_Objektart einer anderen Klasse, die mit der Objektart in Kombination vorkommen kann_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12506002 | mit unterirdischem Gewässerlauf | mit unterirdischem Gewässerlauf     |
|12506001 | mit Wasserfassungsstollen | mit Wasserfassungsstollen     |
|999997 | Unknown | Unknown     |
|999998 | Not applicable | Not applicable     |


   

#### Attribute temp
_Mittlere Wassertemperatur (°C)._
_Datentyp:  integer_



   

#### Attribute chemistry
_Charakteristisches chemisches Element im Mineralwasser (z.B. Fe)._
_Datentyp:  string_



   

#### Attribute azimuth
_Richtung (Azimut) der jeweiligen Punktobjektart. Wert in
Grad (0° 359°) im Uhrzeigersinn gemessen._
_Datentyp:  integer_



   

### Class Surface_Water_L ###
In der Klasse Surface_Water_L sind linienförmige Oberflächengewässer (Quellhorizonte)
beschrieben.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 12601                                       |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12601001 | Hsur Quellhorizont | Hsur Quellhorizont     |
|12601002 | Hsur Bachlauf | Hsur Bachlauf     |


   

### Class Surface_Water_PLG ###
Die Klasse Surface_Water_PLG beinhaltet oberflächliche Wasserspeicher wie Gletscher, Seen und
Flüsse, welche geologische Einheiten bedecken und oftmals eine Interpretation der darunter-
liegenden Geologie verunmöglichen. Das vollständige Gewässernetz ist nicht Teil des Daten-
modells Geologie




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 12701                                       |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|
|12701001 | Hsur Gletscher | Hsur Gletscher     |
|12701002 | Hsur See | Hsur See     |
|12701003 | Hsur Fluss | Hsur Fluss     |


   





## Theme META_DATA ##

### Class Mapsheet ###
Die Klasse Mapsheet ist eine geometrielose Klasse. Sie beinhaltet alle Metadaten zur Objektart
(Kartengrundlage). Neben der Kartenart sind Angaben wie der Titel, Massstab, Autor, Datenherr,
Publikationsjahr und über die öffentliche Verfügbarkeit der Karte grundlegend. Verfügt die Karte
(wie z.B. die Karten der Landesgeologie) über eine Kartennummer, kann dies bei «Map_Nbr»
angegeben werden, während bei «Mapping_Period» die Zeitspanne der Datenaufnahme
(Kartierung) erfasst wird. Das Attribut «Basis_Topo» beschreibt die topographische Grundlage
und «Basis_Vect» den Vektordatensatz.




    | Name                         | Type                              | Description
----|------------------------------|-----------------------------------|--------------------------------------
1 | **kind**                | subtype                                    | Objektart 
[]()           | Cardinality [1] | 15410                                       |  
2 | **map_title**                | string                                    | Originaltitel (Kartentitel) der Objektart. 
[]()           | Cardinality [1] |                                        |  
3 | **map_nbr**                | integer                                    | Originalnummer (Kartennummer) der Objektart. 
[]()           | Cardinality [0..1] |                                        |  
4 | **map_scale**                | string                                    | Massstab der Objektart (Kartenmassstab). 
[]()           | Cardinality [1] |                                        |  
5 | **basis_topo**                |                                     | Angabe zur topographischen Grundlage der Objektart.
Wird vor allem bei Karten der Landesgeologie angegeben. 
[]()           | Cardinality [0..1] |                                        |  
6 | **author**                | string                                    | Autor oder Autoren der Objektart. 
[]()           | Cardinality [1..*] |                                        |  
7 | **owner**                | string                                    | Angabe zum Datenherr / zu den Datenherren der Objektart. 
[]()           | Cardinality [1..*] |                                        |  
8 | **map_period**                | string                                    | Angabe zum Kartierzeitraum der Objektart. 
[]()           | Cardinality [0..1] |                                        |  
9 | **publ_year**                | integer                                    | Publikationsjahr der Objektart. 
[]()           | Cardinality [1] |                                        |  
10 | **basis_vect**                | string                                    | Grundlage Vektordatensatz. 
[]()           | Cardinality [0..1] |                                        |  
11 | **restriction**                | boolean                                    | Angabe darüber, ob die Objektart öffentlich verfügbar ist (ja) oder einer Beschränkung (nein) unterliegt 
[]()           | Cardinality [1] |                                        |  





#### Attribute kind
_Objektart_

|GeolCode|Deutsch|Français|
|---------------|----------------------------------------|----------------------------------------|


   

#### Attribute map_title
_Originaltitel (Kartentitel) der Objektart._
_Datentyp:  string_



   

#### Attribute map_nbr
_Originalnummer (Kartennummer) der Objektart._
_Datentyp:  integer_



   

#### Attribute map_scale
_Massstab der Objektart (Kartenmassstab)._
_Datentyp:  string_



   

#### Attribute basis_topo
_Angabe zur topographischen Grundlage der Objektart.
Wird vor allem bei Karten der Landesgeologie angegeben._


   

#### Attribute author
_Autor oder Autoren der Objektart._
_Datentyp:  string_



   

#### Attribute owner
_Angabe zum Datenherr / zu den Datenherren der Objektart._
_Datentyp:  string_



   

#### Attribute map_period
_Angabe zum Kartierzeitraum der Objektart._
_Datentyp:  string_



   

#### Attribute publ_year
_Publikationsjahr der Objektart._
_Datentyp:  integer_



   

#### Attribute basis_vect
_Grundlage Vektordatensatz._
_Datentyp:  string_



   

#### Attribute restriction
_Angabe darüber, ob die Objektart öffentlich verfügbar ist (ja) oder einer Beschränkung (nein) unterliegt_
_Datentyp:  boolean_



   


