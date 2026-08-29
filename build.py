# -*- coding: utf-8 -*-
"""Bouwt de statische site echteklussers.nl naar dist/."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sitegen import Site, render
from theme import CSS, FAVICON
from content import vakmensen as C_VAK
from content import kiezen as C_KIES
from content import nieuws as C_NIEUWS

BASE = 'https://echteklussers.nl'
NAAM = 'Echteklussers.nl'
EMAIL = 'info@echteklussers.nl'
BOUWDATUM = '2026-08-29'
MERK_SUFFIX = ' | Echteklussers.nl'

KK = 'https://www.kleine-klussen.nl/'

NAV = [
    ('Vakmensen', '/vakmensen/'),
    ('Kiezen', '/kiezen/'),
    ('Tarieven', '/tarieven/'),
    ('Hulpmiddelen', '/hulpmiddelen/'),
    ('Nieuws', '/nieuws/'),
    ('Over', '/over/'),
    ('Contact', '/contact/'),
]

CRUMBS = {
    '/vakmensen/': 'Vakmensen',
    '/kiezen/': 'Kiezen',
    '/tarieven/': 'Tarieven',
    '/hulpmiddelen/': 'Hulpmiddelen',
    '/nieuws/': 'Nieuws',
}

FOOTERCOLS = """
<div>
  <h4>Vakmensen</h4>
  <ul>
    <li><a href="/vakmensen/klusjesman/">Klusjesman</a></li>
    <li><a href="/vakmensen/loodgieter/">Loodgieter</a></li>
    <li><a href="/vakmensen/elektricien/">Elektricien</a></li>
    <li><a href="/vakmensen/schilder/">Schilder</a></li>
    <li><a href="/vakmensen/timmerman/">Timmerman</a></li>
  </ul>
</div>
<div>
  <h4>Kiezen en beoordelen</h4>
  <ul>
    <li><a href="/kiezen/betrouwbare-vakman-herkennen/">Betrouwbare vakman herkennen</a></li>
    <li><a href="/kiezen/offerte-lezen/">Offerte lezen</a></li>
    <li><a href="/kiezen/garantie-en-nazorg/">Garantie en nazorg</a></li>
    <li><a href="/kiezen/reviews-beoordelen/">Reviews beoordelen</a></li>
    <li><a href="/kiezen/klacht-en-geschil/">Klacht en geschil</a></li>
  </ul>
</div>
<div>
  <h4>Meer</h4>
  <ul>
    <li><a href="/tarieven/">Tarieven per vakgebied</a></li>
    <li><a href="/hulpmiddelen/kostenindicatie/">Kostenindicatie klus</a></li>
    <li><a href="/hulpmiddelen/vragen-voor-de-vakman/">Vragen voor de vakman</a></li>
    <li><a href="/nieuws/">Nieuws</a></li>
    <li><a href="/contact/">Contact</a></li>
  </ul>
</div>
"""

CFG = dict(
    base=BASE, name=NAAM, email=EMAIL, builddate=BOUWDATUM,
    brandhtml='Echteklussers<span>.nl</span>',
    nav=NAV, crumb_labels=CRUMBS, css=CSS, favicon=FAVICON,
    footerline='Onafhankelijke gids over het vinden en beoordelen van vakmensen.',
    footercols=FOOTERCOLS,
    rssdesc='Nieuws over tarieven, regels en de praktijk van klussen uitbesteden.',
)

site = Site(CFG)


def T(kern):
    volledig = kern + MERK_SUFFIX
    return volledig if len(volledig) <= 62 else kern


def kk_blok(tekst=None, kop='Een klus laten inplannen'):
    tekst = tekst or (
        'Voor kleine klussen aan huis is een vakman per klus of per uur online in te plannen '
        'bij Kleine-Klussen.nl. Postcode invullen, klus en tijdslot kiezen, waarna een vakman '
        'uit het netwerk langskomt. Werkgebied loopt van Groningen en Assen tot Arnhem en '
        'Den Bosch.')
    return ('<div class="uitgelicht"><h2>%s</h2><p>%s</p>'
            '<p class="knoprij"><a class="knop" href="%s" rel="nofollow noopener" '
            'target="_blank">Kleine-Klussen.nl</a></p></div>' % (kop, tekst, KK))


def kaart(titel, href, tekst, meta=''):
    m = '<p class="meta">%s</p>' % meta if meta else ''
    return ('<article class="kaart"><h3><a href="%s">%s</a></h3><p>%s</p>%s</article>'
            % (href, titel, tekst, m))


NL_MAAND = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus',
            'september', 'oktober', 'november', 'december']


def nl_datum(iso):
    j, m, d = iso.split('-')
    return '%d %s %s' % (int(d), NL_MAAND[int(m) - 1], j)


VAK_KORT = {
    'klusjesman': 'De generalist voor losse klussen, met de grens richting erkende installateur.',
    'loodgieter': 'Kranen, afvoeren en lekkages, met spoedtoeslagen en erkenningen.',
    'elektricien': 'Groepenkast, installatie volgens NEN 1010 en het nut van een inspectierapport.',
    'schilder': 'Voorbereiding bepaalt het resultaat, plus het verlaagde btw-tarief op arbeid.',
    'timmerman': 'Van deur afhangen tot maatwerkkast, met levertijden en houtsoorten.',
    'stukadoor': 'Afwerkingsgraden, droogtijden en prijzen per vierkante meter.',
    'tegelzetter': 'Ondergrond, waterdichte laag, formaat en snijverlies.',
    'hovenier': 'Onderhoud tegenover aanleg, seizoen, snoeiverbod en kapregels.',
    'dakdekker': 'Plat en schuin dak, levensduur per dakbedekking en de aanpak bij lekkage.',
    'glaszetter': 'Glas na breuk, isolatieglas, verzekering en subsidie.',
}

KIES_KORT = {
    'betrouwbare-vakman-herkennen': 'Inschrijving, verzekering en de signalen die op problemen wijzen.',
    'offerte-lezen': 'Welke posten erin horen en hoe stelposten vergelijkbaar worden.',
    'uurtarief-of-vaste-prijs': 'Wanneer welk model past, en wat een richtprijs juridisch betekent.',
    'garantie-en-nazorg': 'Gangbare termijnen, en welke rechten er los van garantie bestaan.',
    'keurmerken-en-branches': 'Wat lidmaatschap zegt en hoe een keurmerk te controleren is.',
    'verzekering-en-aansprakelijkheid': 'Wie betaalt bij schade, en wat te doen als het misgaat.',
    'reviews-beoordelen': 'De regels van de ACM en de patronen die op nepreviews wijzen.',
    'klacht-en-geschil': 'Ingebrekestelling, betaling opschorten en de geschillencommissie.',
}

home_vak = ''.join(kaart(t, '/vakmensen/%s/' % s, VAK_KORT[s])
                   for s, t, _d, _md in C_VAK.VAKKEN[:6])
home_kies = ''.join(kaart(t, '/kiezen/%s/' % s, KIES_KORT[s])
                    for s, t, _d, _md in C_KIES.ONDERWERPEN[:6])
home_nieuws = ''.join(kaart(t, '/nieuws/%s/' % s, sam, nl_datum(datum))
                      for s, datum, _rfc, t, _d, sam, _md in C_NIEUWS.ARTIKELEN[:3])

HOME = """
<section class="hero">
  <div class="binnen">
    <h1>Een vakman kiezen zonder gokken</h1>
    <p class="lead">Echteklussers.nl legt uit hoe een klusbedrijf te beoordelen is voordat
    de opdracht wordt gegeven: wat er in een offerte hoort, wat gangbare tarieven zijn per
    vakgebied, wat garantie waard is en wat te doen als het werk niet deugt. Geen
    bemiddeling, geen offerteaanvraag, geen formulier.</p>
    <div class="cijfers">
      <div class="cijfer"><b>5,4%</b><span>stijging van de loonkosten in de woningbouw in juni 2026, volgens het CBS</span></div>
      <div class="cijfer"><b>14 dagen</b><span>bedenktijd bij een overeenkomst die buiten de bedrijfsruimte is gesloten</span></div>
      <div class="cijfer"><b>2 jaar</b><span>verjaringstermijn voor een verborgen gebrek, gerekend vanaf de melding</span></div>
    </div>
  </div>
</section>

<section>
  <h2>Per vakgebied</h2>
  <p>Wat het vak inhoudt, welke klussen erbij horen, wat gangbare tarieven zijn en welke
  erkenningen bestaan.</p>
  <div class="rooster">{vak}</div>
  <p><a href="/vakmensen/">Alle vakgebieden</a></p>
</section>

<section>
  <h2>Kiezen en beoordelen</h2>
  <p>Van de eerste selectie tot een geschil dat toch ontstaat, in de volgorde waarin het
  speelt.</p>
  <div class="rooster">{kies}</div>
  <p><a href="/kiezen/">Alle onderwerpen</a></p>
</section>

<section>
  {kkblok}
</section>

<section>
  <h2>In vier stappen naar een opdracht</h2>
  <ol class="stappen">
    <li><b>Omschrijf de klus op papier</b>Een omschrijving van een paar regels levert offertes op die onderling te vergelijken zijn. Zonder omschrijving offreert iedereen iets anders.</li>
    <li><b>Vraag drie offertes op binnen enkele weken</b>Offertes van verschillende maanden zijn niet vergelijkbaar, omdat tarieven meebewegen met de loonkosten.</li>
    <li><b>Controleer de basis</b>Inschrijving in het handelsregister, een aansprakelijkheidsverzekering en een btw-nummer op de offerte.</li>
    <li><b>Leg garantie en betaling vast</b>Betalen in termijnen op basis van voortgang, met een deel dat pas voldaan wordt na afhandeling van de opleverpunten.</li>
  </ol>
</section>

<section>
  <h2>Laatste artikelen</h2>
  <div class="rooster">{nieuws}</div>
  <p><a href="/nieuws/">Alle artikelen</a></p>
</section>

<section>
  <h2>Wat deze site niet doet</h2>
  <p>Echteklussers.nl bemiddelt niet, vraagt geen offertes aan en verkoopt geen
  contactgegevens door. Er staat geen formulier op deze site. Contact loopt via
  <a href="mailto:{email}">{email}</a>. Meer daarover staat op
  <a href="/over/">de pagina over deze gids</a>.</p>
</section>
""".format(vak=home_vak, kies=home_kies, nieuws=home_nieuws, kkblok=kk_blok(), email=EMAIL)

site.add('/', T('Een vakman kiezen zonder gokken'),
         'Onafhankelijke gids over het vinden en beoordelen van vakmensen: tarieven per '
         'vakgebied, offertes lezen, garantie, reviews en wat te doen bij een geschil.',
         HOME, h1='Een vakman kiezen zonder gokken', priority='1.0',
         schema=json.dumps({
             "@context": "https://schema.org", "@type": "WebSite", "name": NAAM,
             "url": BASE + "/", "inLanguage": "nl-NL",
             "description": "Gids over het vinden en beoordelen van vakmensen in Nederland.",
         }, ensure_ascii=False))

# ---------------------------------------------------------------- vakmensen
vak_index = ('<section class="smal"><h1>Vakgebieden</h1>%s</section>'
             '<section><div class="rooster">%s</div></section><section>%s</section>'
             % (render(C_VAK.INDEX_INTRO),
                ''.join(kaart(t, '/vakmensen/%s/' % s, VAK_KORT[s])
                        for s, t, _d, _md in C_VAK.VAKKEN),
                kk_blok()))

site.add('/vakmensen/', T('Vakgebieden: welk vak voor welke klus'),
         'Overzicht van vakgebieden in de klussector, met per vak de typische klussen, de '
         'gangbare tarieven, de erkenningen en de aandachtspunten.',
         vak_index, h1='Vakgebieden', priority='0.9')

for slug, titel, desc, md in C_VAK.VAKKEN:
    blok = '' if slug == 'klusjesman' else kk_blok()
    body = '<section class="smal"><h1>%s</h1>%s%s</section>' % (titel, render(md), blok)
    site.add('/vakmensen/%s/' % slug, T('%s: werk, tarieven en aandachtspunten' % titel),
             desc, body, h1=titel)

# ---------------------------------------------------------------- kiezen
kies_index = ('<section class="smal"><h1>Kiezen en beoordelen</h1>%s</section>'
              '<section><div class="rooster">%s</div></section>'
              % (render(C_KIES.INDEX_INTRO),
                 ''.join(kaart(t, '/kiezen/%s/' % s, KIES_KORT[s])
                         for s, t, _d, _md in C_KIES.ONDERWERPEN)))

site.add('/kiezen/', T('Vakman kiezen en beoordelen'),
         'Hoe een klusbedrijf te beoordelen is voordat de opdracht wordt gegeven: '
         'controle vooraf, offertes, garantie, reviews en de route bij een geschil.',
         kies_index, h1='Kiezen en beoordelen', priority='0.9')

for slug, titel, desc, md in C_KIES.ONDERWERPEN:
    body = '<section class="smal"><h1>%s</h1>%s%s</section>' % (titel, render(md), kk_blok())
    site.add('/kiezen/%s/' % slug, T(titel), desc, body, h1=titel)

# ---------------------------------------------------------------- tarieven
TARIEVEN_MD = """
Tarieven in de klussector zijn niet gereguleerd. Wat hieronder staat, is de bandbreedte die
in Nederland gangbaar is voor particuliere opdrachtgevers, inclusief btw tenzij anders
vermeld. Regionale verschillen en de complexiteit van de klus zorgen voor afwijkingen.

## Uurtarieven per vakgebied

| Vakgebied | Tarief per uur |
| --- | --- |
| Hovenier, onderhoud | 40 tot 60 euro |
| Klusjesman | 45 tot 65 euro |
| Schilder | 45 tot 70 euro |
| Timmerman | 50 tot 75 euro |
| Stukadoor | 50 tot 75 euro |
| Hovenier, aanleg | 50 tot 75 euro |
| Tegelzetter | 50 tot 80 euro |
| Loodgieter | 55 tot 85 euro |
| Elektricien | 55 tot 85 euro |
| Dakdekker | 55 tot 90 euro |

## Vaste prijzen voor veelvoorkomende klussen

| Klus | Indicatie |
| --- | --- |
| Lamp of armatuur ophangen | 60 tot 120 euro |
| Meubel monteren, standaard kast | 60 tot 150 euro |
| Kraan vervangen | 75 tot 160 euro |
| Toiletpot vervangen | 150 tot 350 euro |
| Binnendeur plaatsen en afhangen | 120 tot 260 euro |
| Klemmende deur verhelpen | 60 tot 130 euro |
| Stopcontact bijplaatsen, opbouw | 70 tot 140 euro |
| Groep bijplaatsen in de meterkast | 150 tot 350 euro |
| Gazon maaien, per beurt | 40 tot 90 euro |
| Tv-beugel monteren | 80 tot 180 euro |

## Werk per vierkante meter

| Werk | Indicatie |
| --- | --- |
| Wanden sausen | 8 tot 16 euro |
| Behangen | 12 tot 22 euro |
| Stucwerk behangklaar | 15 tot 25 euro |
| Stucwerk schuurwerk | 20 tot 32 euro |
| Stucwerk glad | 28 tot 45 euro |
| Wandtegels zetten | 45 tot 75 euro |
| Vloertegels zetten | 40 tot 70 euro |
| Laminaat of pvc leggen | 15 tot 30 euro |
| Bestrating leggen | 30 tot 60 euro |
| Plat dak vernieuwen | 70 tot 140 euro |

## Toeslagen

| Post | Indicatie |
| --- | --- |
| Voorrijkosten | 25 tot 60 euro |
| Spoed binnen kantooruren | 25 tot 50 procent |
| Spoed buiten kantooruren | 50 tot 100 procent |
| Werk in het weekend | 50 tot 100 procent |
| Opslag op materiaal | 10 tot 25 procent |
| Afvoer van afval | 60 tot 180 euro per container |

## Btw

Het algemene tarief is 21 procent. Voor schilder-, stukadoors- en isolatiewerk aan woningen
ouder dan twee jaar geldt onder voorwaarden 9 procent over de arbeid, mits arbeid en
materiaal gescheiden op de factuur staan. De actuele lijst staat op
https://www.belastingdienst.nl

## Waarom tarieven stijgen

Volgens het CBS lagen de bouwkosten voor woningbouw in juni 2026 vijf procent hoger dan een
jaar eerder, met een loonstijging van 5,4 procent als belangrijkste oorzaak. Bij
arbeidsintensieve klussen werkt dat sterker door dan bij materiaalintensieve klussen.
"""

site.add('/tarieven/', T('Tarieven per vakgebied en per klus'),
         'Gangbare uurtarieven per vakgebied, vaste prijzen voor veelvoorkomende klussen, '
         'prijzen per vierkante meter en de gebruikelijke toeslagen.',
         '<section class="smal"><h1>Tarieven</h1>%s%s</section>'
         % (render(TARIEVEN_MD), kk_blok()), h1='Tarieven', priority='0.9')

# ---------------------------------------------------------------- hulpmiddelen
HULP_INDEX = ('<section class="smal"><h1>Hulpmiddelen</h1>'
              '<p>Twee hulpmiddelen die volledig in de browser werken. Er wordt niets '
              'opgeslagen en niets verstuurd.</p></section>'
              '<section><div class="rooster">%s</div></section>'
              % (kaart('Kostenindicatie klus', '/hulpmiddelen/kostenindicatie/',
                       'Uurtarief, geschatte uren, voorrijkosten en spoedtoeslag in een keer doorgerekend.')
                 + kaart('Vragen voor de vakman', '/hulpmiddelen/vragen-voor-de-vakman/',
                         'De vragen die vooraf gesteld horen te worden, per fase van het traject.')))

site.add('/hulpmiddelen/', T('Hulpmiddelen bij het uitbesteden van een klus'),
         'Een kostenindicatie berekenen en de vragen doorlopen die vooraf gesteld horen te '
         'worden. Beide werken volledig in de browser.',
         HULP_INDEX, h1='Hulpmiddelen', priority='0.8')

KOSTEN_TOOL = """
<section class="smal">
<h1>Kostenindicatie klus</h1>
<p>Deze rekenhulp zet een geschat aantal uren om in een indicatie van de rekening, inclusief
voorrijkosten, toeslagen en materiaal. De uitkomst is een orde van grootte om een offerte
tegen af te zetten, geen offerte.</p>

<div class="tool">
  <label for="vak">Vakgebied</label>
  <select id="vak">
    <option value="40|60">Hovenier, onderhoud</option>
    <option value="45|65" selected>Klusjesman</option>
    <option value="45|70">Schilder</option>
    <option value="50|75">Timmerman</option>
    <option value="50|75">Stukadoor</option>
    <option value="50|80">Tegelzetter</option>
    <option value="55|85">Loodgieter</option>
    <option value="55|85">Elektricien</option>
    <option value="55|90">Dakdekker</option>
  </select>

  <label for="uren">Geschat aantal uren</label>
  <input type="number" id="uren" value="3" min="0.5" step="0.5">

  <label for="voorrij">Voorrijkosten in euro</label>
  <input type="number" id="voorrij" value="35" min="0" step="5">

  <label for="toeslag">Moment van uitvoering</label>
  <select id="toeslag">
    <option value="1" selected>Gepland, binnen kantooruren</option>
    <option value="1.35">Spoed binnen kantooruren</option>
    <option value="1.75">Spoed buiten kantooruren</option>
    <option value="1.6">Weekend</option>
  </select>

  <label for="materiaal">Materiaal in euro</label>
  <input type="number" id="materiaal" value="0" min="0" step="10">

  <div class="uitkomst" id="uitkomst" aria-live="polite"></div>
  <p class="let">De berekening draait in de browser. Er wordt niets opgeslagen en niets
  verstuurd. De tarieven zijn bandbreedtes uit de markt, geen vaste prijzen.</p>
</div>

<h2>Hoe de uitkomst te gebruiken</h2>
<p>De uitkomst is een bandbreedte. Een offerte die daarbinnen valt, is marktconform. Een
offerte die er ver onder ligt, is dat meestal doordat er iets niet in zit. Een offerte die
er ver boven ligt, hoort toegelicht te worden met de reden: moeilijke bereikbaarheid,
specialistisch materiaal, of werk dat meer uren vraagt dan geschat.</p>

<h2>Wat in de schatting van de uren meespeelt</h2>
<ul>
<li>Bereikbaarheid: een tweede verdieping zonder lift kost tijd</li>
<li>Ondergrond: boren in beton duurt langer dan in gipsplaat</li>
<li>Voorbereiding en opruimen tellen mee als werktijd</li>
<li>Meerdere klussen achter elkaar zijn per klus goedkoper dan los ingepland</li>
</ul>
<p>Meer over de keuze tussen uurtarief en vaste prijs staat op
<a href="/kiezen/uurtarief-of-vaste-prijs/">uurtarief of vaste prijs</a>. De volledige
tarievenlijst staat op <a href="/tarieven/">tarieven</a>.</p>
</section>
"""

KOSTEN_SCRIPT = """<script>
(function(){
  var euro=function(n){return n.toLocaleString('nl-NL',{style:'currency',currency:'EUR',maximumFractionDigits:0});};
  function reken(){
    var vak=document.getElementById('vak').value.split('|');
    var laag=parseFloat(vak[0]),hoog=parseFloat(vak[1]);
    var uren=parseFloat(document.getElementById('uren').value)||0;
    var voorrij=parseFloat(document.getElementById('voorrij').value)||0;
    var mat=parseFloat(document.getElementById('materiaal').value)||0;
    var f=parseFloat(document.getElementById('toeslag').value);
    var min=uren*laag*f+voorrij+mat;
    var max=uren*hoog*f+voorrij+mat;
    document.getElementById('uitkomst').innerHTML=
      '<b>'+euro(min)+' tot '+euro(max)+'</b>'+
      '<p>Arbeid '+euro(uren*laag*f)+' tot '+euro(uren*hoog*f)+'<br>'+
      'Voorrijkosten '+euro(voorrij)+'<br>'+
      'Materiaal '+euro(mat)+'<br>'+
      'Gehanteerd uurtarief '+euro(laag*f)+' tot '+euro(hoog*f)+'</p>';
  }
  ['vak','uren','voorrij','toeslag','materiaal'].forEach(function(id){
    var el=document.getElementById(id);
    el.addEventListener('input',reken);el.addEventListener('change',reken);
  });
  reken();
})();
</script>"""

site.add('/hulpmiddelen/kostenindicatie/', T('Kostenindicatie voor een klus berekenen'),
         'Rekenhulp die uurtarief, uren, voorrijkosten, toeslagen en materiaal omzet in een '
         'bandbreedte om een offerte tegen af te zetten.',
         KOSTEN_TOOL + KOSTEN_SCRIPT, h1='Kostenindicatie klus')

VRAGEN = """
<section class="smal">
<h1>Vragen voor de vakman</h1>
<p>De meeste problemen bij een klus ontstaan doordat iets niet is gevraagd. Hieronder de
vragen per fase, van het eerste contact tot de afronding.</p>

<h2>Bij het eerste contact</h2>
<ul class="checklist">
<li>Wat is de bedrijfsnaam en het inschrijfnummer in het handelsregister</li>
<li>Wordt het werk door eigen mensen gedaan of door onderaannemers</li>
<li>Is er een aansprakelijkheidsverzekering voor bedrijven</li>
<li>Wat is de gebruikelijke doorlooptijd tussen opdracht en uitvoering</li>
<li>Komt er iemand kijken voordat er een prijs komt</li>
</ul>

<h2>Bij de offerte</h2>
<ul class="checklist">
<li>Is dit een vaste prijs, een richtprijs of een uurtarief</li>
<li>Staan arbeid en materiaal apart vermeld</li>
<li>Welke werkzaamheden zijn expliciet uitgesloten</li>
<li>Zitten voorrijkosten in de prijs of komen die apart</li>
<li>Wat gebeurt er als de ondergrond anders blijkt dan aangenomen</li>
<li>Wie voert het afval af en zit dat in de prijs</li>
<li>Hoe lang is de offerte geldig</li>
<li>Wat is de garantietermijn, en waarop precies</li>
</ul>

<h2>Over betaling</h2>
<ul class="checklist">
<li>Welk bedrag wordt vooraf gevraagd, en waarvoor</li>
<li>Zijn de termijnen gekoppeld aan voortgang of aan data</li>
<li>Blijft er een deel open tot de opleverpunten zijn afgehandeld</li>
<li>Wordt er per bank gefactureerd met btw-nummer op de factuur</li>
</ul>

<h2>Over de uitvoering</h2>
<ul class="checklist">
<li>Op welke dagen en tijden wordt er gewerkt</li>
<li>Wie is het aanspreekpunt tijdens het werk</li>
<li>Hoe wordt meerwerk gemeld en vastgelegd, en gebeurt dat voordat het wordt uitgevoerd</li>
<li>Wie zorgt voor water, stroom en een plek voor materiaal</li>
<li>Hoe wordt de rest van de woning tegen stof beschermd</li>
<li>Worden er foto's gemaakt van leidingwerk voordat wanden dichtgaan</li>
</ul>

<h2>Bij de afronding</h2>
<ul class="checklist">
<li>Wordt er samen een rondgang gedaan bij daglicht</li>
<li>Komen de punten op één lijst, ondertekend door beide partijen</li>
<li>Binnen welke termijn worden die punten verholpen</li>
<li>Worden garantiebewijzen en handleidingen overhandigd</li>
<li>Wordt er een factuur verstrekt met een specificatie van het meerwerk</li>
</ul>

<div class="kader">
<p>Wat op papier staat, telt. Een toezegging aan de telefoon is achteraf moeilijk hard te
maken. Een korte bevestiging per e-mail van wat is afgesproken, is voldoende en kost twee
minuten.</p>
</div>

<p>Meer over de juridische kant staat op <a href="/kiezen/garantie-en-nazorg/">garantie en
nazorg</a> en op <a href="/kiezen/klacht-en-geschil/">klacht en geschil</a>.</p>
</section>
"""

site.add('/hulpmiddelen/vragen-voor-de-vakman/', T('Vragen voor de vakman'),
         'De vragen die vooraf gesteld horen te worden bij een klus, per fase: eerste '
         'contact, offerte, betaling, uitvoering en afronding.',
         VRAGEN, h1='Vragen voor de vakman')

# ---------------------------------------------------------------- nieuws
site.add('/nieuws/', T('Nieuws over tarieven, regels en klussen'),
         'Artikelen over tarieven, regelgeving, reviews en de praktijk van een klus '
         'uitbesteden in Nederland.',
         '<section class="smal"><h1>Nieuws</h1><p>Artikelen over tarieven, regels en de '
         'praktijk van klussen uitbesteden. Nieuwe artikelen verschijnen ook via '
         '<a href="/rss.xml">de rss-feed</a>.</p></section>'
         '<section><div class="rooster">%s</div></section>'
         % ''.join(kaart(t, '/nieuws/%s/' % s, sam, nl_datum(datum))
                   for s, datum, _rfc, t, _d, sam, _md in C_NIEUWS.ARTIKELEN),
         h1='Nieuws', priority='0.9')

for slug, datum, rfc, titel, desc, sam, md in C_NIEUWS.ARTIKELEN:
    schema = json.dumps({
        "@context": "https://schema.org", "@type": "NewsArticle", "headline": titel,
        "datePublished": datum, "dateModified": datum, "inLanguage": "nl-NL",
        "description": desc, "mainEntityOfPage": BASE + '/nieuws/%s/' % slug,
        "publisher": {"@type": "Organization", "name": NAAM},
    }, ensure_ascii=False)
    body = ('<section class="smal"><h1>%s</h1>'
            '<p class="artikelmeta">Gepubliceerd op %s</p>%s%s'
            '<p><a href="/nieuws/">Terug naar het nieuwsoverzicht</a></p></section>'
            % (titel, nl_datum(datum), render(md), kk_blok()))
    site.add('/nieuws/%s/' % slug, T(titel), desc, body, h1=titel, schema=schema, lastmod=datum)

# ---------------------------------------------------------------- over
OVER_MD = """
Echteklussers.nl is een informatieve gids over het vinden en beoordelen van vakmensen in
Nederland. De aanleiding is eenvoudig: voor de meeste klusberoepen bestaat geen beschermde
titel en geen verplichte registratie. Wie zich klusjesman, timmerman of tegelzetter noemt,
mag dat, ongeacht opleiding of ervaring. De beoordeling verschuift daarmee naar wat wel
controleerbaar is.

## Wat deze site wel doet

- Per vakgebied uitleggen wat het werk inhoudt, wat gangbare tarieven zijn en welke erkenningen bestaan
- Laten zien hoe een offerte is opgebouwd en hoe drie offertes vergelijkbaar worden gemaakt
- De wettelijke basis benoemen rond garantie, oplevering, meerwerk en geschillen
- Twee hulpmiddelen aanbieden die volledig in de browser draaien: een kostenindicatie en een vragenlijst

## Wat deze site niet doet

- Bemiddelen tussen opdrachtgevers en vakmensen
- Offertes aanvragen, doorsturen of vergelijken
- Contactgegevens verzamelen of doorverkopen
- Bedrijven aanbevelen tegen betaling

Er staat geen formulier op deze site en er is geen vergelijkingsdienst.

## Herkomst van de cijfers

De genoemde tarieven zijn bandbreedtes die gangbaar zijn voor particuliere opdrachtgevers
in Nederland. Ze dienen om een offerte tegen af te zetten, niet om een prijs te bepalen.
Regionale verschillen en de complexiteit van een klus zorgen in de praktijk voor
afwijkingen.

Waar het om wetgeving, toezicht of officiële cijfers gaat, staat de bron erbij vermeld. Dat
zijn onder meer het Burgerlijk Wetboek, het Centraal Bureau voor de Statistiek, de
Autoriteit Consument en Markt en de Rijksdienst voor Ondernemend Nederland.

## Actualiteit

Regels en tarieven veranderen. De pagina's vermelden de stand op het moment van schrijven
en verwijzen naar de plek waar de actuele versie staat. Bij twijfel geldt de officiële
bron, niet deze site. Deze gids geeft algemene informatie en geen juridisch advies over een
concrete situatie.

## Een klus laten uitvoeren

Deze site voert geen klussen uit en plant er ook geen in. Voor kleine klussen aan huis is
Kleine-Klussen.nl een partij die dat wel doet, met online een datum en tijdslot en een
vakman uit het eigen netwerk. Zie https://www.kleine-klussen.nl/

## Contact

Vragen of opmerkingen over de inhoud kunnen naar info@echteklussers.nl. Meer daarover staat
op de contactpagina.
"""

site.add('/over/', T('Over Echteklussers.nl'),
         'Wat Echteklussers.nl is: een onafhankelijke gids over het beoordelen van '
         'vakmensen, zonder bemiddeling, offerteaanvraag of doorverkoop van gegevens.',
         '<section class="smal"><h1>Over deze gids</h1>%s</section>' % render(OVER_MD),
         h1='Over deze gids', priority='0.6')

# ---------------------------------------------------------------- contact
CONTACT = """
<section class="smal">
<h1>Contact</h1>
<p>Echteklussers.nl is een informatieve gids. Er is één contactmogelijkheid en dat is
e-mail.</p>

<div class="kader">
<p><strong>E-mail</strong><br><a href="mailto:info@echteklussers.nl">info@echteklussers.nl</a></p>
</div>

<h2>Waar deze site niet voor is</h2>
<p>Er wordt niet bemiddeld tussen opdrachtgevers en vakmensen. Er worden geen offertes
aangevraagd of doorgestuurd, en er worden geen bedrijven aanbevolen. Een verzoek om een
klus in te plannen kan hier niet worden behandeld.</p>

<h2>Waarvoor wel</h2>
<ul>
<li>Een feitelijke onjuistheid op een pagina melden</li>
<li>Een suggestie voor een vakgebied of onderwerp dat ontbreekt</li>
<li>Een vraag over de herkomst van een tarief of een verwijzing</li>
<li>Een verzoek in het kader van de privacywetgeving</li>
</ul>

<h2>Een klus laten inplannen</h2>
<p>Voor het daadwerkelijk inplannen van een kleine klus aan huis is Kleine-Klussen.nl een
optie, met online een datum en tijdslot. Zie
<a href="https://www.kleine-klussen.nl/" rel="nofollow noopener" target="_blank">https://www.kleine-klussen.nl/</a></p>

<h2>Reactietermijn</h2>
<p>E-mail wordt doorgaans binnen enkele werkdagen beantwoord. Berichten met een commercieel
aanbod of een verzoek tot linkplaatsing blijven onbeantwoord.</p>
</section>
"""

site.add('/contact/', T('Contact'),
         'Contact met Echteklussers.nl loopt uitsluitend via info@echteklussers.nl. Geen '
         'formulier, geen bemiddeling en geen offerteaanvraag.',
         CONTACT, h1='Contact', priority='0.5')

# ---------------------------------------------------------------- legal
PRIVACY_MD = """
Deze verklaring beschrijft hoe Echteklussers.nl omgaat met persoonsgegevens. Laatste
wijziging: 29 augustus 2026.

## Uitgangspunt

Echteklussers.nl is een informatieve website zonder inlogfunctie, zonder contactformulier,
zonder nieuwsbrief en zonder webwinkel. Er worden geen accounts aangemaakt en er worden
geen gegevens gevraagd om de site te gebruiken.

## Welke gegevens worden verwerkt

### Bij het bezoeken van de site
De website wordt gehost bij Cloudflare Pages. De hostingpartij verwerkt technische gegevens
die nodig zijn om de site te tonen en te beveiligen, waaronder het IP-adres, het tijdstip
van het verzoek, de opgevraagde pagina en het type browser. Die verwerking vindt plaats op
grond van een gerechtvaardigd belang: het beschikbaar en veilig houden van de website.

Er wordt geen bezoekersstatistiek van derden geladen, geen advertentienetwerk, geen
socialemediaknop en geen ingesloten inhoud van andere partijen. De pagina's laden geen
externe bestanden.

### Bij e-mail
Wie mailt naar info@echteklussers.nl, verstuurt daarmee een e-mailadres en de inhoud van
het bericht. Die gegevens worden gebruikt om het bericht te beantwoorden en daarna niet
langer bewaard dan nodig. Er wordt geen mailinglijst opgebouwd en er worden geen
e-mailadressen gedeeld met derden.

## Cookies

Deze website plaatst geen cookies voor analyse, advertenties of profilering. Zie het
cookiebeleid voor de details.

## Bewaartermijn

E-mailcorrespondentie wordt bewaard zolang dat nodig is voor de afhandeling en daarna
verwijderd. Technische logbestanden bij de hostingpartij worden volgens het beleid van die
partij bewaard en daarna verwijderd.

## Delen met derden

Persoonsgegevens worden niet verkocht en niet gedeeld voor commerciële doeleinden. Delen
gebeurt alleen als een wettelijke verplichting daartoe verplicht.

## Rechten

Op grond van de Algemene verordening gegevensbescherming bestaat het recht op inzage,
correctie, verwijdering, beperking en bezwaar. Een verzoek daartoe kan naar
info@echteklussers.nl. Er wordt binnen een maand gereageerd.

Een klacht over de verwerking van persoonsgegevens kan worden ingediend bij de Autoriteit
Persoonsgegevens via https://www.autoriteitpersoonsgegevens.nl

## Beveiliging

De site wordt uitsluitend over https aangeboden. Er worden geen gegevens op de website
opgeslagen, omdat er geen formulieren en geen database zijn.

## Externe links

Deze site verwijst naar websites van derden. Op die websites geldt het privacybeleid van
die partij. Echteklussers.nl is niet verantwoordelijk voor de inhoud of de
gegevensverwerking van externe websites.

## Wijzigingen

Deze verklaring kan worden aangepast als de opzet van de website verandert. De datum
bovenaan geeft de laatste wijziging aan.
"""

site.add('/privacybeleid/', T('Privacybeleid'),
         'Hoe Echteklussers.nl omgaat met persoonsgegevens: geen formulieren, geen '
         'tracking en geen cookies voor analyse of advertenties.',
         '<section class="smal"><h1>Privacybeleid</h1>%s</section>' % render(PRIVACY_MD),
         h1='Privacybeleid', priority='0.3')

COOKIE_MD = """
Laatste wijziging: 29 augustus 2026.

## Geen cookies

Echteklussers.nl plaatst geen cookies. Er is geen analysepakket, geen advertentienetwerk,
geen socialemediaknop en geen ingesloten inhoud van derden. Daarom staat er ook geen
cookiemelding op deze site: een toestemmingsvraag zonder cookies heeft geen functie.

## Wat er technisch wel gebeurt

De website draait op Cloudflare Pages. De hostingpartij kan een technische voorziening
inzetten om misbruik en overbelasting tegen te gaan. Dat is geen cookie voor analyse of
advertenties en er wordt geen bezoekersprofiel mee opgebouwd.

## Lokale opslag

De hulpmiddelen op deze site rekenen volledig in de browser. Er wordt niets opgeslagen in
de browser en er gaat niets naar een server. Wie de pagina sluit, laat niets achter.

## Externe links

Links naar andere websites openen in een nieuw tabblad. Zodra een externe website wordt
geopend, geldt het cookiebeleid van die partij. Dat kan afwijken van het beleid op deze
site.

## Cookies uitzetten

Elke browser biedt de mogelijkheid cookies te blokkeren of te verwijderen. Omdat deze site
geen cookies plaatst, heeft dat geen invloed op de werking ervan.

## Vragen

Vragen over dit cookiebeleid kunnen naar info@echteklussers.nl
"""

site.add('/cookiebeleid/', T('Cookiebeleid'),
         'Echteklussers.nl plaatst geen cookies voor analyse, advertenties of profilering. '
         'Uitleg over wat er technisch wel gebeurt op de website.',
         '<section class="smal"><h1>Cookiebeleid</h1>%s</section>' % render(COOKIE_MD),
         h1='Cookiebeleid', priority='0.3')

site.add('/404/', T('Pagina niet gevonden'),
         'Deze pagina bestaat niet of is verplaatst. De overzichten hieronder geven toegang '
         'tot de rest van de gids.',
         '<section class="smal"><h1>Pagina niet gevonden</h1>'
         '<p>Deze pagina bestaat niet of is verplaatst. Onderstaande overzichten geven '
         'toegang tot de rest van de gids.</p>'
         '<ul><li><a href="/">Home</a></li>'
         '<li><a href="/vakmensen/">Vakgebieden</a></li>'
         '<li><a href="/kiezen/">Kiezen en beoordelen</a></li>'
         '<li><a href="/tarieven/">Tarieven</a></li>'
         '<li><a href="/hulpmiddelen/">Hulpmiddelen</a></li>'
         '<li><a href="/nieuws/">Nieuws</a></li>'
         '<li><a href="/contact/">Contact</a></li></ul></section>',
         h1='Pagina niet gevonden')

if __name__ == '__main__':
    aantal = site.build('dist')
    site.rss('dist', [dict(title=t, path='/nieuws/%s/' % s, rfc822=rfc, summary=sam)
                      for s, _d, rfc, t, _desc, sam, _md in C_NIEUWS.ARTIKELEN])
    print('%d pagina\'s geschreven naar dist/' % aantal)
