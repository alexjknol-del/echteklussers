CSS = """
:root{
  --ink:#191d1a;
  --ink-zacht:#55605a;
  --lijn:#d7ded8;
  --lijn-sterk:#b6c2ba;
  --papier:#ffffff;
  --vlak:#f2f5f2;
  --accent:#15613f;
  --accent-donker:#0f4a30;
  --zand:#a9631f;
  --zand-vlak:#fbf2e6;
  --breed:1060px;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0;background:var(--papier);color:var(--ink);
  font-family:Georgia,"Times New Roman",serif;font-size:17.5px;line-height:1.72;
}
img{max-width:100%;height:auto}
.binnen{max-width:var(--breed);margin:0 auto;padding:0 20px}
a{color:var(--accent);text-decoration:underline;text-underline-offset:2px}
a:hover{color:var(--accent-donker)}
.overslaan{position:absolute;left:-9999px;background:var(--ink);color:#fff;padding:10px 16px;z-index:10}
.overslaan:focus{left:8px;top:8px}
.sans{font-family:"Segoe UI",Roboto,-apple-system,Helvetica,Arial,sans-serif}

/* twee balken boven elkaar */
.topbalk{background:var(--accent);color:#fff}
.topinhoud{display:flex;align-items:center;gap:16px;min-height:58px;flex-wrap:wrap}
.merk{font-weight:700;font-size:1.18rem;text-decoration:none;color:#fff;letter-spacing:-.01em;
  font-family:"Segoe UI",Roboto,-apple-system,Helvetica,Arial,sans-serif}
.merk span{color:#eec79a}
.topclaim{margin-left:auto;font-size:.88rem;color:rgba(255,255,255,.82);
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.menuknop{display:none;border:1px solid rgba(255,255,255,.55);background:transparent;color:#fff;
  padding:6px 12px;font-size:.92rem;cursor:pointer;font-family:inherit;margin-left:auto}
.menubalk{border-bottom:1px solid var(--lijn);background:var(--vlak)}
#hoofdmenu{display:flex;gap:0;list-style:none;margin:0;padding:0;flex-wrap:wrap}
#hoofdmenu li{border-right:1px solid var(--lijn)}
#hoofdmenu li:first-child{border-left:1px solid var(--lijn)}
#hoofdmenu a{display:block;padding:11px 16px;text-decoration:none;color:var(--ink-zacht);
  font-size:.93rem;letter-spacing:.01em;
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
#hoofdmenu a:hover{background:#fff;color:var(--accent)}
#hoofdmenu a.actief{background:#fff;color:var(--accent);box-shadow:inset 0 -3px 0 var(--accent)}
@media (max-width:900px){
  .topclaim{display:none}
  .menuknop{display:block}
  .menubalk{border-bottom:0}
  #hoofdmenu{display:none;flex-direction:column;padding-bottom:8px}
  #hoofdmenu.open{display:flex}
  #hoofdmenu li,#hoofdmenu li:first-child{border:0;border-bottom:1px solid var(--lijn)}
}

/* kruimels */
.kruimels{border-bottom:1px solid var(--lijn);padding:9px 0;font-size:.84rem;color:var(--ink-zacht);
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.kruimels a{color:var(--ink-zacht)}
.kruimels span{color:var(--ink)}

/* vlakken */
.blok{max-width:var(--breed);margin:0 auto;padding:30px 20px}
.blok.rand{border-bottom:1px solid var(--lijn)}
h1,h2,h3,h4{font-family:"Segoe UI",Roboto,-apple-system,Helvetica,Arial,sans-serif;letter-spacing:-.015em}
h1{font-size:2.05rem;line-height:1.2;margin:.2em 0 .5em}
h2{font-size:1.3rem;margin:2em 0 .6em}
h3{font-size:1.06rem;margin:1.6em 0 .4em}
p{margin:0 0 1.05em}
ul,ol{margin:0 0 1.1em;padding-left:1.3em}
li{margin:.32em 0}
.lead{font-size:1.14rem;color:var(--ink-zacht);max-width:66ch}
.introtekst{max-width:70ch}
@media (max-width:640px){h1{font-size:1.6rem}}

/* opening */
.opening{background:var(--vlak);border-bottom:1px solid var(--lijn)}
.opening .blok{padding-top:36px;padding-bottom:30px}
.opening h1{max-width:22ch;margin-top:0}

/* tekstpagina met inhoudsopgave ernaast */
.tekstlay{display:grid;grid-template-columns:220px minmax(0,1fr);gap:44px;
  max-width:var(--breed);margin:0 auto;padding:26px 20px 10px;align-items:start}
.tekstlay.zonder{grid-template-columns:minmax(0,760px)}
.tekstlay .tekst{max-width:72ch}
.inhoud{position:sticky;top:16px;font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:.88rem;border-left:2px solid var(--lijn);padding-left:14px}
.inhoudkop{margin:0 0 .5em;font-weight:600;color:var(--ink);text-transform:uppercase;
  letter-spacing:.06em;font-size:.74rem}
.inhoud ol{list-style:none;margin:0;padding:0}
.inhoud li{margin:.45em 0;line-height:1.35}
.inhoud a{color:var(--ink-zacht);text-decoration:none}
.inhoud a:hover{color:var(--accent);text-decoration:underline}
@media (max-width:920px){
  .tekstlay{grid-template-columns:minmax(0,1fr);gap:0}
  .inhoud{position:static;border-left:0;border-top:1px solid var(--lijn);
    border-bottom:1px solid var(--lijn);padding:14px 0;margin-bottom:20px}
  .inhoud ol{columns:2;column-gap:24px}
}

/* genummerde lijstindex, in plaats van kaartjes */
.lijst{list-style:none;margin:1.2em 0;padding:0;border-top:1px solid var(--lijn)}
.rij{display:flex;gap:18px;padding:15px 4px;border-bottom:1px solid var(--lijn);margin:0}
.rij:hover{background:var(--vlak)}
.rijnr{flex:0 0 34px;font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:.86rem;
  color:var(--zand);font-weight:700;padding-top:2px}
.rijtekst{flex:1 1 auto}
.rijtekst a{font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-weight:600;
  font-size:1.02rem;text-decoration:none}
.rijtekst a:hover{text-decoration:underline}
.rijtekst em{display:block;font-style:normal;color:var(--ink-zacht);font-size:.95rem;margin-top:2px}

/* feiten als definitielijst */
.feiten{display:flex;flex-wrap:wrap;gap:0;margin:1.4em 0;border-top:2px solid var(--accent)}
.feit{flex:1 1 210px;padding:14px 20px 14px 0;border-bottom:1px solid var(--lijn)}
.feit dt{font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:1.35rem;
  font-weight:700;color:var(--accent);line-height:1.15}
.feit dd{margin:4px 0 0;font-size:.9rem;color:var(--ink-zacht);line-height:1.45}

/* kaders */
.kader{background:var(--vlak);border-left:3px solid var(--lijn-sterk);padding:14px 18px;margin:1.4em 0}
.kader p:last-child{margin-bottom:0}
.uitgelicht{background:var(--zand-vlak);border-top:3px solid var(--zand);padding:22px;margin:1.8em 0}
.uitgelicht h2{margin-top:0;font-size:1.16rem}
.uitgelicht p:last-child{margin-bottom:0}

/* tabel */
.tabelwrap{overflow-x:auto;margin:1.2em 0}
table{border-collapse:collapse;width:100%;font-size:.95rem;min-width:430px}
th,td{border-bottom:1px solid var(--lijn);padding:9px 14px 9px 0;text-align:left;vertical-align:top}
th{font-weight:600;border-bottom:2px solid var(--lijn-sterk);
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:.88rem;
  text-transform:uppercase;letter-spacing:.05em}

/* stappen als tijdlijn */
.stappen{list-style:none;counter-reset:stap;padding:0;margin:1.4em 0;
  border-left:2px solid var(--lijn)}
.stappen li{counter-increment:stap;position:relative;padding:0 0 20px 26px;margin:0}
.stappen li::before{content:counter(stap);position:absolute;left:-9px;top:2px;width:16px;height:16px;
  background:var(--accent);color:#fff;font-size:.66rem;display:flex;align-items:center;
  justify-content:center;font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-weight:700}
.stappen b{display:block;font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:1rem}

/* hulpmiddel */
.tool{border:1px solid var(--lijn);border-top:3px solid var(--accent);padding:20px;
  background:var(--vlak);margin:1.5em 0}
.tool label{display:block;font-weight:600;margin:14px 0 5px;font-size:.9rem;
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.tool select,.tool input{width:100%;max-width:420px;padding:10px 12px;border:1px solid #b8c4bc;
  font-size:1rem;background:#fff;color:var(--ink);font-family:inherit}
.tool .uitkomst{margin-top:20px;padding:16px 18px;background:#fff;border:1px solid var(--lijn)}
.tool .uitkomst b{font-size:1.3rem;color:var(--accent);display:block;
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.tool .let{font-size:.85rem;color:var(--ink-zacht);margin-top:10px}

/* checklist */
.checklist{list-style:none;padding:0;margin:1.2em 0}
.checklist li{padding:10px 0 10px 28px;border-bottom:1px solid var(--lijn);position:relative}
.checklist li::before{content:"";position:absolute;left:0;top:18px;width:11px;height:11px;
  border:1px solid var(--lijn-sterk);background:#fff}

/* video */
.video{margin:1.6em 0;max-width:330px}
.video .videostart{display:block;width:100%;aspect-ratio:9/16;border:0;cursor:pointer;
  background:linear-gradient(200deg,#0f4a30 0%,#15613f 55%,#a9631f 100%);
  color:#fff;padding:18px;text-align:left;position:relative;font:inherit}
.video .videostart:hover{filter:brightness(1.08)}
.video .videoplay{position:absolute;left:50%;top:46%;width:54px;height:54px;margin:-27px 0 0 -27px;
  border:2px solid rgba(255,255,255,.9)}
.video .videoplay::after{content:"";position:absolute;left:20px;top:14px;border-style:solid;
  border-width:11px 0 11px 17px;border-color:transparent transparent transparent #fff}
.video .videotekst{position:absolute;left:18px;right:18px;bottom:42px;font-weight:600;
  font-size:1rem;line-height:1.35;font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.video .videobron{position:absolute;left:18px;bottom:20px;font-size:.8rem;opacity:.8;
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.video .videoframe{aspect-ratio:9/16;overflow:hidden;border:1px solid var(--lijn)}
.video .videoframe iframe{width:100%;height:100%;border:0;display:block}
.video figcaption{font-size:.83rem;color:var(--ink-zacht);margin-top:8px}

/* nieuws */
.artikelmeta{color:var(--ink-zacht);font-size:.88rem;margin:0 0 1.6em;
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  border-bottom:1px solid var(--lijn);padding-bottom:12px}
.knoprij{margin:1.4em 0 .3em}
.knop{display:inline-block;background:var(--accent);color:#fff;text-decoration:none;
  padding:11px 20px;font-weight:600;font-size:.98rem;
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.knop:hover{background:var(--accent-donker);color:#fff}
.meerlink{font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:.94rem}

/* voet */
.voet{background:var(--vlak);border-top:3px solid var(--accent);margin-top:46px;
  padding:30px 0 22px;font-size:.93rem;color:var(--ink-zacht)}
.voetmerk{font-weight:700;color:var(--ink);margin:0 0 .2em;font-size:1.05rem;
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.voetregel{margin:0 0 1.1em;max-width:60ch}
.voetlinks{list-style:none;padding:0;margin:0 0 1.2em;display:flex;flex-wrap:wrap;gap:8px 20px;
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:.92rem}
.voetlinks li{margin:0}
.voetonder{margin:0;padding-top:14px;border-top:1px solid var(--lijn);font-size:.86rem}
"""

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" fill="#15613f"/>
<path d="M20 42l16-16" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
<circle cx="41" cy="21" r="8" fill="none" stroke="#eec79a" stroke-width="5"/>
<path d="M17 45l4 4" stroke="#eec79a" stroke-width="6" stroke-linecap="round"/>
</svg>
"""
