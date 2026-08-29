CSS = """
:root{
  --ink:#1b1f1c;
  --ink-zacht:#4f5a52;
  --lijn:#dde3dd;
  --papier:#ffffff;
  --vlak:#f3f6f3;
  --accent:#186a4a;
  --accent-donker:#12523a;
  --zand:#b8722a;
  --zand-vlak:#fdf3e8;
  --radius:6px;
  --breed:1080px;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0;background:var(--papier);color:var(--ink);
  font-family:Georgia,"Times New Roman",serif;
  font-size:17.5px;line-height:1.7;
}
img{max-width:100%;height:auto}
.binnen{max-width:var(--breed);margin:0 auto;padding:0 20px}
a{color:var(--accent);text-decoration:underline;text-underline-offset:2px}
a:hover{color:var(--accent-donker)}
.overslaan{position:absolute;left:-9999px;background:var(--ink);color:#fff;padding:10px 16px;z-index:10}
.overslaan:focus{left:8px;top:8px}

/* kop */
.kop{background:var(--accent);color:#fff}
.kopbalk{display:flex;align-items:center;gap:16px;min-height:64px;flex-wrap:wrap}
.merk{font-weight:700;font-size:1.15rem;text-decoration:none;color:#fff;margin-right:auto;
  font-family:"Segoe UI",Roboto,-apple-system,Helvetica,Arial,sans-serif;letter-spacing:-.01em}
.merk span{color:#f0c99a}
.menuknop{display:none;border:1px solid rgba(255,255,255,.5);background:transparent;color:#fff;
  padding:7px 13px;border-radius:4px;font-size:.95rem;cursor:pointer;font-family:inherit}
#hoofdmenu ul{display:flex;gap:18px;list-style:none;margin:0;padding:0;flex-wrap:wrap}
#hoofdmenu a{text-decoration:none;color:rgba(255,255,255,.88);font-size:.95rem;
  font-family:"Segoe UI",Roboto,-apple-system,Helvetica,Arial,sans-serif}
#hoofdmenu a:hover,#hoofdmenu a.actief{color:#fff;text-decoration:underline}
@media (max-width:880px){
  .menuknop{display:block}
  #hoofdmenu{display:none;width:100%;padding-bottom:10px}
  #hoofdmenu.open{display:block}
  #hoofdmenu ul{flex-direction:column;gap:0}
  #hoofdmenu a{display:block;padding:9px 2px;border-bottom:1px solid rgba(255,255,255,.18)}
}

/* kruimels */
.kruimels{max-width:var(--breed);margin:0 auto;padding:14px 20px 0;font-size:.85rem;
  color:var(--ink-zacht);font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.kruimels a{color:var(--ink-zacht)}
.kruimels .sep{opacity:.5;padding:0 2px}

/* secties */
section{max-width:var(--breed);margin:0 auto;padding:24px 20px}
section.smal{max-width:760px}
h1,h2,h3,h4{font-family:"Segoe UI",Roboto,-apple-system,Helvetica,Arial,sans-serif;letter-spacing:-.015em}
h1{font-size:2rem;line-height:1.22;margin:.4em 0 .35em}
h2{font-size:1.32rem;margin:1.8em 0 .5em;padding-bottom:.3em;border-bottom:2px solid var(--lijn)}
h3{font-size:1.08rem;margin:1.5em 0 .4em}
p{margin:0 0 1.05em}
ul,ol{margin:0 0 1.1em;padding-left:1.3em}
li{margin:.32em 0}
.lead{font-size:1.12rem;color:var(--ink-zacht)}

/* hero */
.hero{background:var(--vlak);border-bottom:1px solid var(--lijn)}
.hero .binnen{padding-top:40px;padding-bottom:34px}
.hero h1{margin-top:0;font-size:2.3rem;max-width:26ch}
.hero .lead{max-width:64ch}
@media (max-width:640px){.hero h1{font-size:1.75rem}h1{font-size:1.65rem}}

/* kaders */
.kader{background:var(--vlak);border-left:4px solid var(--accent);padding:15px 18px;margin:1.4em 0}
.kader p:last-child{margin-bottom:0}
.uitgelicht{background:var(--zand-vlak);border:1px solid #eddbc3;border-top:4px solid var(--zand);
  padding:20px;margin:1.7em 0}
.uitgelicht h2,.uitgelicht h3{margin-top:0;border:0;padding:0}
.uitgelicht p:last-child{margin-bottom:0}

/* kaartjes */
.rooster{display:grid;gap:2px;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));
  margin:1.3em 0;background:var(--lijn);border:1px solid var(--lijn)}
.kaart{padding:18px;background:var(--papier);display:flex;flex-direction:column}
.kaart h3{margin:0 0 .35em;font-size:1.03rem}
.kaart h3 a{text-decoration:none}
.kaart h3 a:hover{text-decoration:underline}
.kaart p{margin:0;color:var(--ink-zacht);font-size:.94rem}
.kaart .meta{margin-top:auto;padding-top:10px;font-size:.84rem;color:var(--ink-zacht);
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}

/* cijfers */
.cijfers{display:grid;gap:2px;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));
  margin:1.5em 0;background:var(--lijn);border:1px solid var(--lijn)}
.cijfer{background:var(--papier);padding:16px}
.cijfer b{display:block;font-size:1.55rem;line-height:1.15;color:var(--accent);
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.cijfer span{font-size:.88rem;color:var(--ink-zacht)}

/* tabel */
.tabelwrap{overflow-x:auto;margin:1.2em 0}
table{border-collapse:collapse;width:100%;font-size:.95rem;min-width:440px}
th,td{border:1px solid var(--lijn);padding:9px 12px;text-align:left;vertical-align:top}
th{background:var(--vlak);font-weight:600;
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}

/* stappen */
.stappen{list-style:none;counter-reset:stap;padding:0;margin:1.3em 0}
.stappen li{counter-increment:stap;position:relative;padding-left:44px;margin:0 0 15px}
.stappen li::before{content:counter(stap);position:absolute;left:0;top:2px;width:30px;height:30px;
  background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;
  font-weight:600;font-size:.92rem;font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.stappen b{display:block}

/* tool */
.tool{border:1px solid var(--lijn);padding:20px;background:var(--vlak);margin:1.5em 0}
.tool label{display:block;font-weight:600;margin:14px 0 5px;font-size:.94rem;
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.tool select,.tool input{width:100%;max-width:420px;padding:10px 12px;border:1px solid #c3ccc5;
  border-radius:4px;font-size:1rem;background:#fff;color:var(--ink);font-family:inherit}
.tool .uitkomst{margin-top:20px;padding:16px 18px;background:#fff;border:1px solid var(--lijn)}
.tool .uitkomst b{font-size:1.3rem;color:var(--accent);display:block;
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.tool .let{font-size:.85rem;color:var(--ink-zacht);margin-top:10px}

/* checklist */
.checklist{list-style:none;padding:0;margin:1.2em 0}
.checklist li{padding:11px 0 11px 30px;border-bottom:1px solid var(--lijn);position:relative}
.checklist li::before{content:"";position:absolute;left:2px;top:18px;width:12px;height:12px;
  border:2px solid var(--accent)}

/* nieuws */
.artikelmeta{color:var(--ink-zacht);font-size:.9rem;margin:0 0 1.4em;
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.knoprij{margin:1.5em 0 .4em}
.knop{display:inline-block;background:var(--accent);color:#fff;text-decoration:none;
  padding:12px 22px;font-weight:600;
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.knop:hover{background:var(--accent-donker);color:#fff}

/* voet */
.voet{background:#13261e;color:#c2cec6;margin-top:44px;padding:36px 0 20px;font-size:.93rem}
.voet a{color:#e8efe9}
.voetgrid{display:grid;gap:26px;grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}
.voetmerk{font-weight:700;color:#fff;margin:0 0 .4em;
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.voet h4{margin:0 0 .5em;font-size:.94rem;color:#fff}
.voet ul{list-style:none;padding:0;margin:0}
.voet li{margin:.3em 0}
.voetonder{border-top:1px solid #24382e;margin-top:26px;padding-top:16px;display:flex;
  justify-content:space-between;gap:12px;flex-wrap:wrap;font-size:.87rem}
.voetonder p{margin:0}
.voet .sep{opacity:.5;padding:0 4px}
"""

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="8" fill="#186a4a"/>
<path d="M20 42l16-16" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
<circle cx="41" cy="21" r="8" fill="none" stroke="#f0c99a" stroke-width="5"/>
<path d="M17 45l4 4" stroke="#f0c99a" stroke-width="6" stroke-linecap="round"/>
</svg>
"""
