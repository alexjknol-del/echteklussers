# -*- coding: utf-8 -*-
"""Pagina's per vakgebied: wat het vak inhoudt, tarieven, erkenningen en aandachtspunten."""

INDEX_INTRO = """
De titel klusjesman is niet beschermd. Loodgieter en elektricien evenmin. Wie zich zo
noemt, mag dat, ongeacht opleiding of ervaring. Voor sommige werkzaamheden gelden wel
eisen aan certificering, en voor werk aan gas en aan de aansluiting op het openbare net
gelden wettelijke beperkingen.

Per vakgebied staat hieronder wat het werk inhoudt, welke klussen erbij horen, wat de
gangbare tarieven zijn en welke erkenningen bestaan. Wie eerst wil weten hoe een vakman
beoordeeld wordt, begint bij de onderwerpen over kiezen en beoordelen.
"""

VAKKEN = [
    ("klusjesman", "Klusjesman",
     "Wat een klusjesman doet, welke klussen erbij horen, gangbare uurtarieven en waar de grens ligt met een erkende installateur.",
     """
De klusjesman is de generalist: iemand die uiteenlopende kleine klussen aankan zonder dat
er per klus een specialist bij hoeft. Precies daar zit de waarde, want een halve dag met
één persoon voor acht losse klussen is efficiënter dan vier vakmensen die elk twintig
minuten werken.

## Typische klussen

- Lampen, spiegels, planken, kapstokken en televisiebeugels ophangen
- Meubels monteren, inclusief kasten op maat stellen
- Klemmende deuren afstellen, scharnieren vervangen, deuren inkorten
- Tochtstrips, rookmelders en deurdrangers plaatsen
- Gordijnrails en rolgordijnen monteren
- Kleine reparaties aan bestrating, schuttingen en tuinhuizen
- Kitwerk vernieuwen in keuken en badkamer

## Tarieven

| Vorm | Indicatie |
| --- | --- |
| Uurtarief | 45 tot 65 euro |
| Halve dag, vier uur | 180 tot 260 euro |
| Voorrijkosten | 25 tot 50 euro |
| Klus met vaste prijs, eenvoudig | 60 tot 130 euro |

Materiaal komt daar doorgaans bovenop, met of zonder opslag. Die opslag hoort vooraf
benoemd te worden, niet op de factuur te verschijnen.

## Waar de grens ligt

Een klusjesman mag veel, maar niet alles. Werk aan gasleidingen en aan de aansluiting op
het openbare gas- of elektriciteitsnet is voorbehouden aan erkende installateurs. Werk in
de meterkast, aan groepen en aan aardingsvoorzieningen wordt in de praktijk aan een
elektricien overgelaten, omdat een verzekeraar bij brandschade kan vragen wie het heeft
aangelegd.

## Waar op te letten

- Een vast bedrag per klus of een uurtarief met een maximum, zodat de rekening niet openeindig is
- Duidelijkheid over wie het materiaal levert en tegen welke prijs
- Een bedrijfsaansprakelijkheidsverzekering, zeker bij boren in wanden met leidingen
- Bij een lijst klussen: alles vooraf doorgeven, zodat het juiste gereedschap meekomt

> Voor dit type klussen is een vakman per klus of per uur online in te plannen bij
> Kleine-Klussen.nl, met een datum en tijdslot naar keuze. Zie https://www.kleine-klussen.nl/
"""),

    ("loodgieter", "Loodgieter",
     "Wanneer een loodgieter nodig is, wat spoedwerk kost, welke erkenningen bestaan en hoe een lekkage wordt opgespoord.",
     """
Loodgieterswerk gaat over water: aanvoer, afvoer en alles wat er tussenin lekt. Een deel
van het werk is planbaar, een deel niet. Dat onderscheid bepaalt het tarief.

## Typische klussen

- Kranen vervangen in keuken, badkamer en toilet
- Wastafels, toiletten, douchebakken en fonteintjes plaatsen
- Afvoeren aansluiten en ontstoppen
- Lekkages opsporen en verhelpen
- Waterleidingen verleggen of splitsen
- Wasmachine, vaatwasser of buitenkraan aansluiten
- Radiatoren plaatsen, vervangen en ontluchten

## Tarieven

| Vorm | Indicatie |
| --- | --- |
| Uurtarief | 55 tot 85 euro |
| Voorrijkosten | 30 tot 60 euro |
| Spoed buiten kantooruren | toeslag van 50 tot 100 procent |
| Kraan vervangen, vaste prijs | 75 tot 160 euro |
| Lekkage opsporen | 90 tot 250 euro |

## Erkenningen

Voor werk aan gasleidingen geldt de eis van een erkende installateur. Erkenningsregelingen
lopen onder meer via Techniek Nederland en via de erkenningsregeling voor
gasinstallaties. Voor waterleidingwerk gelden de eisen van de drinkwaterregelgeving en de
voorwaarden van het waterbedrijf.

## Lekkage opsporen

Een lekkage die niet zichtbaar is, wordt opgespoord met vochtmeting, een warmtebeeldcamera
of met een druktest op de leiding. Dat is specialistisch werk en wordt apart gerekend van
de reparatie. Bij een lekkage die tot waterschade heeft geleid, is de opsporing vaak
gedekt door de opstal- of inboedelverzekering, ook als de reparatie zelf dat niet is. Het
loont om dat te controleren voordat de opdracht wordt gegeven.

## Waar op te letten

- Bij spoed: vooraf navragen wat het starttarief is en hoeveel uren minimaal gerekend worden
- Bij een offerte voor sanitair: of het aan- en afvoerwerk erin zit of als meerwerk komt
- Bij een oude woning: loden leidingen komen nog voor en zijn een reden voor volledige vervanging
- Foto's van het leidingwerk voordat de wand dichtgaat
"""),

    ("elektricien", "Elektricien",
     "Werk aan groepenkast en installatie, tarieven, de eisen aan een erkende installateur en waarom een inspectierapport zinvol is.",
     """
Elektrisch werk is het vakgebied waar fouten het langst onzichtbaar blijven. Een verkeerd
aangesloten aardleiding werkt jarenlang naar behoren, tot het moment dat die zijn functie
moet vervullen.

## Typische klussen

- Groepenkast vervangen of uitbreiden
- Wandcontactdozen en schakelaars bijplaatsen
- Bestaande bedrading doortrekken of infrezen
- Buitenverlichting, tuinverlichting en grondkabels
- Aansluiting voor inductiekookplaat, warmtepomp of laadpunt
- Spots inbouwen, verlichting vervangen door led
- Storingen opsporen in een bestaande installatie

## Tarieven

| Vorm | Indicatie |
| --- | --- |
| Uurtarief | 55 tot 85 euro |
| Voorrijkosten | 30 tot 60 euro |
| Groep bijplaatsen | 150 tot 350 euro |
| Groepenkast vervangen | 700 tot 1.600 euro |
| Stopcontact bijplaatsen, opbouw | 70 tot 140 euro |
| Inspectie woninginstallatie | 150 tot 400 euro |

## Norm en erkenning

Installaties in woningen worden aangelegd volgens NEN 1010. De aansluiting op het openbare
net is voorbehouden aan de netbeheerder en aan erkende partijen. Een erkenning zegt niets
over de kwaliteit van de afwerking, maar wel dat het bedrijf aan een aantal voorwaarden
voldoet en dat er een aanspreekpunt is bij problemen.

## Inspectierapport

Bij aankoop van een oudere woning, bij twijfel over eerder uitgevoerd werk of bij een
verzwaring van de aansluiting is een inspectie van de installatie zinvol. Het rapport geeft
aan welke groepen niet beveiligd zijn, waar de aarding ontbreekt en welke bedrading aan
vervanging toe is. Dat rapport is ook bruikbaar richting een verzekeraar.

## Waar op te letten

- Een schema in de meterkast dat klopt met de werkelijkheid, opgesteld na afloop
- Aardlekschakelaars die getest zijn met de testknop, in aanwezigheid van de opdrachtgever
- Bij het bijplaatsen van groepen: of de hoofdaansluiting de belasting aankan
- Bij infrezen: dat de leidingen verticaal en horizontaal lopen volgens de installatiezones, zodat later boren veilig blijft
"""),

    ("schilder", "Schilder",
     "Binnen- en buitenschilderwerk, het verschil in voorbereiding, tarieven per uur en per vierkante meter en het verlaagde btw-tarief.",
     """
Bij schilderwerk zit tachtig procent van het resultaat in de voorbereiding. Een schilder
die op de eerste dag al verf op de kwast heeft, heeft iets overgeslagen.

## Typische klussen

- Binnenschilderwerk: kozijnen, deuren, plinten, trappen
- Wanden en plafonds sausen of spuiten
- Buitenschilderwerk aan kozijnen, deuren en boeidelen
- Houtrot herstellen voordat er geschilderd wordt
- Behangen en behang verwijderen
- Schuren, plamuren en gronden van ondergronden

## Tarieven

| Vorm | Indicatie |
| --- | --- |
| Uurtarief | 45 tot 70 euro |
| Wanden sausen, per vierkante meter | 8 tot 16 euro |
| Kozijnen binnen, per stuk | 60 tot 140 euro |
| Buitenschilderwerk woning, compleet | 1.800 tot 5.000 euro |
| Houtrotherstel, per plek | 80 tot 350 euro |

## Btw

Voor schilder- en stukadoorswerk aan woningen ouder dan twee jaar geldt het verlaagde
btw-tarief van 9 procent over de arbeid. Het materiaal blijft belast tegen 21 procent.
Voorwaarde is dat de offerte en de factuur arbeid en materiaal gescheiden vermelden. De
actuele regels staan op https://www.belastingdienst.nl

## Voorbereiding als maatstaf

Wat een goede schilder doet voordat de eerste laag erop gaat:

1. Ondergrond reinigen en ontvetten
2. Losse en beschadigde delen wegschuren tot vaste ondergrond
3. Houtrot herstellen of het onderdeel vervangen
4. Kale plekken gronden
5. Naden en kieren afkitten met een elastische kit
6. Pas daarna twee lagen aanbrengen

Een offerte die alleen het aantal lagen noemt zonder de voorbereiding te benoemen, laat de
belangrijkste post open.

## Waar op te letten

- Het merk en type verf, en het aantal lagen, expliciet in de offerte
- Wie de steiger of hoogwerker levert en betaalt
- Bij buitenwerk: het seizoen, met een ondergrens rond de vijf graden en een droge ondergrond
- Garantie op het werk, doorgaans twee tot zes jaar bij buitenschilderwerk
"""),

    ("timmerman", "Timmerman",
     "Wat een timmerman maakt en repareert, verschil tussen onderhoudstimmerwerk en meubelmaatwerk, en gangbare tarieven.",
     """
Timmerwerk loopt van een deur afhangen tot een complete kapconstructie. In de praktijk
splitst het vak zich in onderhoudstimmerwerk, ruwbouw en maatwerk in de afbouw.

## Typische klussen

- Deuren plaatsen, afhangen, inkorten en afstellen
- Kozijnen plaatsen, aftimmeren en vervangen
- Plinten, koven en vensterbanken
- Kasten op maat, wandmeubels en werkbladen
- Vlizotrap of zoldertrap plaatsen
- Open trap dichtmaken
- Dakbeschot, betimmering en houten vloeren
- Schuttingen, vlonders en overkappingen

## Tarieven

| Vorm | Indicatie |
| --- | --- |
| Uurtarief | 50 tot 75 euro |
| Binnendeur plaatsen inclusief afhangen | 120 tot 260 euro |
| Vlizotrap plaatsen | 350 tot 700 euro |
| Kast op maat, per strekkende meter | 400 tot 1.200 euro |
| Plinten plaatsen, per strekkende meter | 8 tot 18 euro |

## Maatwerk of standaard

Bij maatwerk gaat het grootste deel van de prijs naar arbeid en naar de werkplaats.
Verschil tussen een standaardkast en een kast op maat is niet alleen de pasvorm maar ook
de constructie: een kast op maat wordt aan de wand bevestigd en is niet mee te verhuizen.
Dat is een keuze met gevolgen bij verkoop van de woning.

## Waar op te letten

- Houtsoort en plaatmateriaal expliciet benoemd, want het verschil tussen mdf, multiplex en massief is groot in prijs en levensduur
- Wie het schilderwerk doet: veel timmerlieden leveren onbehandeld op
- Levertijd van maatwerk, doorgaans drie tot acht weken
- Bij vervanging van kozijnen: wie de dagmaten inmeet en wie verantwoordelijk is als die niet kloppen
"""),

    ("stukadoor", "Stukadoor",
     "Stucwerk binnen: soorten afwerking, droogtijden, tarieven per vierkante meter en het verlaagde btw-tarief.",
     """
Stucwerk maakt van een ruwe wand een vlakke ondergrond. Het verschil tussen een acceptabel
en een goed resultaat wordt zichtbaar bij strijklicht, dus onder een raam of een spot.

## Soorten afwerking

| Afwerking | Toepassing |
| --- | --- |
| Behangklaar | Wand wordt daarna behangen, lichte structuur toegestaan |
| Schuurwerk | Fijne korrel, gangbaar in woningen, verbergt kleine oneffenheden |
| Glad pleisterwerk | Strak en vlak, geschikt voor verf, vraagt de meeste arbeid |
| Spachtelputz | Structuur, veel toegepast in gangen en trappenhuizen |
| Sierpleister | Grovere structuur, ook buiten toegepast |

## Tarieven

| Vorm | Indicatie |
| --- | --- |
| Uurtarief | 50 tot 75 euro |
| Behangklaar, per vierkante meter | 15 tot 25 euro |
| Schuurwerk, per vierkante meter | 20 tot 32 euro |
| Glad pleisterwerk, per vierkante meter | 28 tot 45 euro |
| Plafond, toeslag | 10 tot 25 procent |

## Droogtijden

Vers stucwerk bevat veel vocht. Voordat er geverfd of behangen kan worden, moet dat eruit.
Als richtlijn geldt twee tot vier weken bij normale ventilatie, langer bij dikke lagen of
een koud vertrek. Wie eerder verft, sluit vocht in en ziet dat terug als vlekken of
loslatende verf.

Ventileren tijdens het drogen is nodig, verwarmen met een bouwdroger versnelt het maar mag
niet leiden tot te snel drogen aan de oppervlakte.

## Btw

Voor stukadoorswerk aan woningen ouder dan twee jaar geldt het verlaagde btw-tarief van
9 procent over de arbeid, mits arbeid en materiaal gescheiden op de factuur staan. Zie
https://www.belastingdienst.nl

## Waar op te letten

- De afwerkingsgraad expliciet benoemd in de offerte, want het verschil tussen behangklaar en glad is fors in prijs
- Wie de wanden voorbehandelt en oude lagen verwijdert
- Hoe de aansluitingen op kozijnen en plafonds worden afgewerkt
- Wie het stof en het afval opruimt
"""),

    ("tegelzetter", "Tegelzetter",
     "Tegelwerk in badkamer, keuken en woonkamer: ondergrond, formaat, tarieven per vierkante meter en de waterdichte laag.",
     """
Tegelwerk is het onderdeel van een badkamer dat het langst zichtbaar blijft en dat het
minst eenvoudig te herstellen is. De ondergrond eronder bepaalt of het resultaat blijft
liggen.

## Wat er vooraf moet kloppen

- Een vlakke ondergrond. Grote formaten vragen een vlakkere ondergrond dan kleine
- Een waterdichte laag in natte ruimtes, aangebracht op de wand en de vloer voordat er getegeld wordt. Tegels en voegen zijn zelf niet waterdicht
- Kimband in de hoeken en rond doorvoeren
- Voldoende afschot naar het putje bij een inloopdouche

## Tarieven

| Vorm | Indicatie |
| --- | --- |
| Uurtarief | 50 tot 80 euro |
| Wandtegels, per vierkante meter | 45 tot 75 euro |
| Vloertegels, per vierkante meter | 40 tot 70 euro |
| Groot formaat vanaf 60 bij 60, toeslag | 15 tot 30 procent |
| Mozaïek of visgraat, toeslag | 30 tot 60 procent |
| Waterdichte laag aanbrengen, per vierkante meter | 15 tot 30 euro |
| Voegen, per vierkante meter | 8 tot 15 euro |

## Formaat en verlies

Bij het bestellen van tegels wordt tien procent extra gerekend voor snijverlies. Bij
visgraat of een diagonaal patroon loopt dat op tot vijftien à twintig procent. Tegels uit
één productiepartij hebben dezelfde kleur; nabestellen levert vaak een zichtbaar verschil
op. Dat maakt de marge bij de eerste bestelling belangrijker dan de prijs per vierkante
meter.

## Waar op te letten

- Of de waterdichte laag in de offerte zit of als apart onderdeel wordt gerekend
- De voegbreedte en de voegkleur, vooraf afgesproken
- Wie de tegels afhaalt en op de verdieping krijgt
- Kitwerk als laatste, na het uitharden van de voegen, met een sanitaire kit
"""),

    ("hovenier", "Hovenier en tuinman",
     "Verschil tussen onderhoud en aanleg, seizoenswerk, tarieven per uur en per vierkante meter en de regels rond kappen en snoeien.",
     """
Het verschil tussen een tuinman en een hovenier zit in de omvang van het werk. Onderhoud
is terugkerend werk aan een bestaande tuin. Aanleg verandert de tuin en vraagt grondwerk,
bestrating en beplantingsplan.

## Onderhoud

- Gazon maaien, bemesten, verticuteren en herstellen
- Snoeien van hagen, heesters en kleine bomen
- Onkruid verwijderen en bestrijden
- Bladruimen in het najaar
- Tegels en terrassen reinigen
- Beplanting vervangen en bijplanten

## Aanleg

- Grondwerk, egaliseren en afvoeren van grond
- Bestrating, opsluitbanden en drainage
- Schuttingen, vlonders en overkappingen
- Beplantingsplan en aanplant
- Tuinverlichting en buitenkranen

## Tarieven

| Vorm | Indicatie |
| --- | --- |
| Uurtarief onderhoud | 40 tot 60 euro |
| Uurtarief aanleg | 50 tot 75 euro |
| Gazon maaien, per beurt | 40 tot 90 euro |
| Haag snoeien, per strekkende meter | 4 tot 12 euro |
| Bestrating leggen, per vierkante meter | 30 tot 60 euro |
| Afvoer groenafval | 60 tot 180 euro per container |

## Seizoen

Snoeien van hagen gebeurt buiten het broedseizoen, dat globaal van half maart tot half juli
loopt. De Wet natuurbescherming, opgenomen in de Omgevingswet, verbiedt het verstoren van
broedende vogels. Dat geldt ook voor particuliere tuinen. Planten gaat het beste in het
najaar of vroeg voorjaar.

## Kappen

Voor het kappen van een boom geldt in veel gemeenten een vergunningplicht boven een
bepaalde stamomtrek, gemeten op 1,30 meter hoogte. De regels verschillen per gemeente en
staan in de plaatselijke verordening. De check per adres loopt via
https://omgevingswet.overheid.nl

## Waar op te letten

- Of de afvoer van snoeiafval en grond in de prijs zit
- Bij aanleg: de opbouw onder de bestrating, want daar zit de duurzaamheid
- Bij onderhoud: een vaste frequentie per jaar in plaats van losse beurten
- Garantie op aanplant, doorgaans één groeiseizoen
"""),

    ("dakdekker", "Dakdekker",
     "Plat dak en schuin dak, levensduur van dakbedekking, kosten per vierkante meter en de aanpak bij een lekkage.",
     """
Een dak wordt pas opgemerkt als het lekt, en dan is de schade meestal groter dan de
reparatie. Onderhoud aan een dak is daarmee het duidelijkste voorbeeld van werk dat zich
terugbetaalt.

## Plat dak

| Dakbedekking | Levensduur |
| --- | --- |
| Bitumen, twee lagen | 20 tot 30 jaar |
| EPDM, rubber | 30 tot 50 jaar |
| Kunststof, pvc of tpo | 25 tot 40 jaar |

Kosten voor het vernieuwen van een plat dak liggen doorgaans tussen 70 en 140 euro per
vierkante meter, inclusief het verwijderen van de oude laag en exclusief isolatie. Isolatie
erbij tilt dat naar 110 tot 190 euro per vierkante meter, maar levert wel recht op subsidie
op via de ISDE. Zie https://www.rvo.nl

## Schuin dak

- Pannen vervangen of het dak opnieuw leggen
- Dakbeschot vernieuwen bij houtrot
- Loodwerk bij schoorsteen en dakkapel
- Nokvorsten opnieuw aanbrengen, tegenwoordig doorgaans droog in plaats van in mortel
- Goten vervangen en reinigen

Het opnieuw leggen van een pannendak kost doorgaans 60 tot 120 euro per vierkante meter,
afhankelijk van het hergebruik van de bestaande pannen.

## Bij een lekkage

De plek waar het water binnenkomt, is zelden de plek waar het naar binnen gaat. Water loopt
over het dakbeschot en over balken voordat het zichtbaar wordt. Een dakdekker die na twee
minuten een prijs noemt zonder op het dak te zijn geweest, gokt.

## Waar op te letten

- Een offerte met het type dakbedekking, het aantal lagen en de fabrikant erbij
- Garantie op materiaal en garantie op het werk apart benoemd
- Wie de veiligheidsvoorzieningen regelt, want valbeveiliging is verplicht bij werken op hoogte
- Bij een appartement: het dak is doorgaans gemeenschappelijk eigendom en dus een zaak van de vereniging van eigenaars
"""),

    ("glaszetter", "Glaszetter",
     "Glas vervangen na breuk, isolatieglas plaatsen, kosten per vierkante meter en de rol van de opstalverzekering.",
     """
Glaswerk splitst zich in twee situaties: een ruit die kapot is en glas dat vervangen wordt
om isolatieredenen. De eerste is spoed, de tweede is planbaar.

## Na een breuk

Bij een gebroken ruit gaat het eerst om dichtzetten en daarna om vervangen. Veel
glaszetters werken met een noodvoorziening van plaatmateriaal totdat het nieuwe glas op
maat geleverd is. Levertijd voor standaard isolatieglas is enkele werkdagen, voor
speciaal glas langer.

Glasschade is bij veel woningen gedekt via de opstalverzekering of via een aparte
glasverzekering. Melden vóór opdracht is de volgorde die problemen voorkomt, omdat de
verzekeraar soms een eigen hersteller inschakelt.

## Isolatieglas

| Type | Toepassing |
| --- | --- |
| Enkel glas | Alleen nog in oudbouw en monumenten |
| Dubbel glas, oud | Standaard tussen 1975 en 2000, isoleert matig |
| HR++ | Huidige standaard bij vervanging |
| Triple | Vraagt zwaarder kozijn en beslag, meerprijs is fors |

Kosten voor HR++ glas liggen doorgaans tussen 110 en 200 euro per vierkante meter inclusief
plaatsen. Voor glasisolatie bestaat subsidie via de ISDE, met een minimum van drie
vierkante meter en 25 euro per vierkante meter voor HR++ glas. Zie https://www.rvo.nl

## Waar op te letten

- Of het kozijn geschikt is voor de nieuwe glasdikte; bij triple is dat vaak niet zo
- Of er ventilatieroosters in het glas of het kozijn komen, want een luchtdichtere woning vraagt luchtverversing
- De U-waarde van het glas expliciet in de offerte
- Bij monumenten en beschermd stadsgezicht: aanvullende eisen aan het aanzicht van het glas
- Wie het oude glas afvoert
"""),
]
