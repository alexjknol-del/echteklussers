"""Statische sitegenerator voor echteklussers.nl, zonder dependencies."""
import html
import os
import re
import shutil
import unicodedata
from datetime import date


# ---------------------------------------------------------------- hulp

def slug(tekst):
    t = unicodedata.normalize('NFKD', tekst).encode('ascii', 'ignore').decode()
    t = re.sub(r'[^a-zA-Z0-9]+', '-', t).strip('-').lower()
    return t or 'kop'


def _inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r'\[([^\]]+)\]\(([^)\s]+)(?:\s+"(nofollow|dofollow)")?\)',
                  lambda m: _link(m.group(1), m.group(2), m.group(3)), text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    return text


def _link(label, href, markering=None):
    if href.startswith('http'):
        rel = 'noopener' if markering == 'dofollow' else 'nofollow noopener'
        return ('<a href="%s" rel="%s" target="_blank">%s</a>'
                % (href, rel, label))
    return '<a href="%s">%s</a>' % (href, label)


def render(md, koppen=None):
    """Markdown-subset naar html. Vult koppen met (id, tekst) van elke h2."""
    out = []
    lines = md.strip('\n').split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue
        if line.startswith('## '):
            kop = line[3:].strip()
            kid = slug(kop)
            if koppen is not None:
                koppen.append((kid, kop))
            out.append('<h2 id="%s">%s</h2>' % (kid, _inline(kop)))
            i += 1
        elif line.startswith('### '):
            out.append('<h3>%s</h3>' % _inline(line[4:].strip()))
            i += 1
        elif line.startswith('> '):
            block = []
            while i < len(lines) and lines[i].startswith('> '):
                block.append(_inline(lines[i][2:].strip()))
                i += 1
            out.append('<div class="kader"><p>%s</p></div>' % '</p><p>'.join(block))
        elif line.startswith('- '):
            items = []
            while i < len(lines) and lines[i].startswith('- '):
                items.append('<li>%s</li>' % _inline(lines[i][2:].strip()))
                i += 1
            out.append('<ul>%s</ul>' % ''.join(items))
        elif re.match(r'^\d+\. ', line):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                items.append('<li>%s</li>' % _inline(re.sub(r'^\d+\. ', '', lines[i]).strip()))
                i += 1
            out.append('<ol>%s</ol>' % ''.join(items))
        elif line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
                i += 1
            head = rows[0]
            body = [r for r in rows[1:] if not set(''.join(r)) <= set('-: ')]
            thead = ''.join('<th>%s</th>' % _inline(c) for c in head)
            tbody = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % _inline(c) for c in r)
                            for r in body)
            out.append('<div class="tabelwrap"><table><thead><tr>%s</tr></thead>'
                       '<tbody>%s</tbody></table></div>' % (thead, tbody))
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(
                    r'^(#{2,3} |- |\d+\. |\||> )', lines[i]):
                para.append(lines[i].strip())
                i += 1
            out.append('<p>%s</p>' % _inline(' '.join(para)))
    return '\n'.join(out)


# ---------------------------------------------------------------- onderdelen

def rij(nummer, titel, href, tekst):
    """Eén regel in een genummerde lijstindex. Vervangt het kaartrooster."""
    return ('<li class="rij"><span class="rijnr">%s</span>'
            '<span class="rijtekst"><a href="%s">%s</a><em>%s</em></span></li>'
            % (nummer, href, html.escape(titel), tekst))


def lijst(rijen):
    return '<ol class="lijst">%s</ol>' % ''.join(rijen)


def feit(waarde, uitleg):
    return ('<div class="feit"><dt>%s</dt><dd>%s</dd></div>'
            % (html.escape(waarde), uitleg))


def video(vid, titel, toelichting=None):
    """Klik-om-te-laden YouTube-embed. Laadt niets tot de bezoeker klikt."""
    toelichting = toelichting or (
        'De video staat op YouTube en wordt pas na een klik geladen, via '
        'youtube-nocookie.com. Vanaf dat moment geldt het privacybeleid van YouTube.')
    return (
        '<figure class="video" data-video="%s">'
        '<button type="button" class="videostart">'
        '<span class="videoplay" aria-hidden="true"></span>'
        '<span class="videotekst">%s</span>'
        '<span class="videobron">Kleine-Klussen.nl op YouTube</span>'
        '</button>'
        '<figcaption>%s</figcaption>'
        '</figure>'
        % (html.escape(vid, quote=True), html.escape(titel), html.escape(toelichting)))


def inhoudsopgave(koppen):
    if len(koppen) < 3:
        return ''
    items = ''.join('<li><a href="#%s">%s</a></li>' % (k, html.escape(t)) for k, t in koppen)
    return ('<nav class="inhoud" aria-label="Op deze pagina">'
            '<p class="inhoudkop">Op deze pagina</p><ol>%s</ol></nav>' % items)


# ---------------------------------------------------------------- site

class Site:
    def __init__(self, cfg):
        self.cfg = cfg
        self.pages = []

    def add(self, path, title, description, body, h1=None, extra_head='',
            schema=None, lastmod=None, priority='0.7'):
        self.pages.append(dict(
            path=path, title=title, description=description, body=body,
            h1=h1 or title.split(' |')[0], extra_head=extra_head, schema=schema,
            lastmod=lastmod or self.cfg['builddate'], priority=priority))

    def nav_html(self, current):
        items = []
        for label, href in self.cfg['nav']:
            cls = ' class="actief"' if href == current else ''
            items.append('<li><a href="%s"%s>%s</a></li>' % (href, cls, label))
        return ''.join(items)

    def breadcrumb(self, path, title):
        if path == '/':
            return ''
        parts = [p for p in path.strip('/').split('/') if p]
        crumbs = ['<a href="/">Start</a>']
        acc = ''
        for idx, part in enumerate(parts):
            acc += '/' + part
            label = self.cfg['crumb_labels'].get(acc + '/', part.replace('-', ' ').capitalize())
            if idx == len(parts) - 1:
                crumbs.append('<span aria-current="page">%s</span>' % html.escape(title))
            else:
                crumbs.append('<a href="%s/">%s</a>' % (acc, html.escape(label)))
        return ('<nav class="kruimels" aria-label="Kruimelpad"><div class="binnen">%s</div></nav>'
                % ' &rsaquo; '.join(crumbs))

    def page_html(self, page):
        c = self.cfg
        url = c['base'] + page['path']
        schema = ('<script type="application/ld+json">%s</script>' % page['schema']
                  if page['schema'] else '')
        return """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="{name}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" title="{name} nieuws" href="/rss.xml">
<link rel="stylesheet" href="/stijl.css">
{extra}
{schema}
</head>
<body>
<a class="overslaan" href="#hoofd">Naar de inhoud</a>
<div class="topbalk">
  <div class="binnen topinhoud">
    <a class="merk" href="/">{brandhtml}</a>
    <span class="topclaim">{topclaim}</span>
    <button class="menuknop" aria-expanded="false" aria-controls="hoofdmenu">Menu</button>
  </div>
</div>
<nav class="menubalk" aria-label="Hoofdmenu">
  <div class="binnen"><ul id="hoofdmenu">{nav}</ul></div>
</nav>
{crumbs}
<main id="hoofd">
{body}
</main>
<footer class="voet">
  <div class="binnen">
    <p class="voetmerk">{name}</p>
    <p class="voetregel">{footerline}</p>
    <ul class="voetlinks">{footerlinks}</ul>
    <p class="voetonder">&copy; {year} {name} &middot;
      <a href="/privacybeleid/">Privacybeleid</a> &middot;
      <a href="/cookiebeleid/">Cookiebeleid</a> &middot;
      <a href="mailto:{email}">{email}</a></p>
  </div>
</footer>
<script>
(function(){{
  var b=document.querySelector('.menuknop'),n=document.getElementById('hoofdmenu');
  if(b&&n){{
    b.addEventListener('click',function(){{
      var open=n.classList.toggle('open');
      b.setAttribute('aria-expanded',open?'true':'false');
    }});
  }}
  document.querySelectorAll('.video').forEach(function(f){{
    var knop=f.querySelector('.videostart');
    if(!knop)return;
    knop.addEventListener('click',function(){{
      var id=f.getAttribute('data-video');
      var d=document.createElement('div');
      d.className='videoframe';
      var i=document.createElement('iframe');
      i.src='https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0';
      i.title=knop.querySelector('.videotekst').textContent;
      i.allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
      i.setAttribute('allowfullscreen','');
      i.setAttribute('loading','lazy');
      i.setAttribute('referrerpolicy','strict-origin-when-cross-origin');
      d.appendChild(i);
      knop.replaceWith(d);
    }});
  }});
}})();
</script>
</body>
</html>
""".format(
            title=html.escape(page['title']), desc=html.escape(page['description']),
            url=url, name=html.escape(c['name']), extra=page['extra_head'], schema=schema,
            brandhtml=c['brandhtml'], topclaim=c['topclaim'],
            nav=self.nav_html(page['path']),
            crumbs=self.breadcrumb(page['path'], page['h1']), body=page['body'],
            footerline=c['footerline'], footerlinks=c['footerlinks'],
            email=c['email'], year=date.today().year)

    def build(self, outdir='dist'):
        if os.path.isdir(outdir):
            shutil.rmtree(outdir)
        os.makedirs(outdir)
        for page in self.pages:
            if page['path'] == '/404/':
                continue
            rel = page['path'].strip('/')
            target = (os.path.join(outdir, rel, 'index.html') if rel
                      else os.path.join(outdir, 'index.html'))
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, 'w', encoding='utf-8') as fh:
                fh.write(self.page_html(page))
        with open(os.path.join(outdir, 'stijl.css'), 'w', encoding='utf-8') as fh:
            fh.write(self.cfg['css'])
        with open(os.path.join(outdir, 'favicon.svg'), 'w', encoding='utf-8') as fh:
            fh.write(self.cfg['favicon'])
        with open(os.path.join(outdir, 'robots.txt'), 'w', encoding='utf-8') as fh:
            fh.write('User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % self.cfg['base'])
        with open(os.path.join(outdir, '_headers'), 'w', encoding='utf-8') as fh:
            fh.write('/*\n  X-Content-Type-Options: nosniff\n'
                     '  Referrer-Policy: strict-origin-when-cross-origin\n'
                     '  X-Frame-Options: SAMEORIGIN\n'
                     '  Permissions-Policy: geolocation=(), microphone=(), camera=()\n')
        urls = ['<url><loc>%s%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>'
                % (self.cfg['base'], p['path'], p['lastmod'], p['priority'])
                for p in sorted(self.pages, key=lambda x: x['path']) if p['path'] != '/404/']
        with open(os.path.join(outdir, 'sitemap.xml'), 'w', encoding='utf-8') as fh:
            fh.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                     '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n'
                     % '\n'.join(urls))
        for page in self.pages:
            if page['path'] == '/404/':
                with open(os.path.join(outdir, '404.html'), 'w', encoding='utf-8') as fh:
                    fh.write(self.page_html(page))
        return len(self.pages)

    def rss(self, outdir, items):
        entries = ['<item><title>%s</title><link>%s%s</link><guid>%s%s</guid>'
                   '<pubDate>%s</pubDate><description>%s</description></item>'
                   % (html.escape(it['title']), self.cfg['base'], it['path'],
                      self.cfg['base'], it['path'], it['rfc822'], html.escape(it['summary']))
                   for it in items]
        with open(os.path.join(outdir, 'rss.xml'), 'w', encoding='utf-8') as fh:
            fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>\n'
                     '<title>%s nieuws</title><link>%s/nieuws/</link>'
                     '<description>%s</description><language>nl-nl</language>\n%s\n'
                     '</channel></rss>\n'
                     % (html.escape(self.cfg['name']), self.cfg['base'],
                        html.escape(self.cfg['rssdesc']), '\n'.join(entries)))
