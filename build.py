"""Builds the website from content.py. Run:  python build.py  (standard library only).
The 3D scene lives in scene3d.js and is inlined into every page."""
import base64
from html import escape as e
from pathlib import Path

import content as c

OUT = Path(__file__).parent
P = c.PROFILE
PAGES = [("index.html", "About"), ("research.html", "Research"),
         ("publications.html", "Publications"), ("contact.html", "Contact")]
SCENE_JS = (OUT / "scene3d.js").read_text(encoding="utf-8")

CSS = """
:root{--navy:#0B1B2E;--ink:#14263A;--muted:#5A6B7C;--line:#E2E8EE;--soft:#F5F8FB;--accent:#1D58B8;--amber:#E09F1F}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:#fff;color:var(--ink);font:17px/1.65 "Hanken Grotesk",system-ui,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--accent);text-underline-offset:3px}
a:focus-visible{outline:2px solid var(--amber);outline-offset:3px;border-radius:3px}
.wrap{max-width:68rem;margin:0 auto;padding:0 1.5rem}
.top{position:sticky;top:0;z-index:10;background:rgba(11,27,46,.94);backdrop-filter:blur(10px);border-bottom:1px solid rgba(255,255,255,.08)}
.top .wrap{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.4rem 1rem;padding-top:.8rem;padding-bottom:.8rem}
.brand{color:#fff;text-decoration:none;font:500 1.2rem "Newsreader",Georgia,serif}
nav{display:flex;flex-wrap:wrap;gap:.2rem}
nav a{color:#B8C7D8;text-decoration:none;font-size:.95rem;padding:.4rem .85rem;border-radius:8px}
nav a:hover{color:#fff;background:rgba(255,255,255,.08)}
nav a[aria-current]{color:#fff;background:rgba(255,255,255,.14)}
.hero{position:relative;background:var(--navy);color:#fff;overflow:hidden}
#scene{position:absolute;inset:0}
#scene canvas{display:block;width:100%;height:100%}
.hero::after{content:"";position:absolute;inset:0;pointer-events:none;background:linear-gradient(90deg,rgba(11,27,46,.96) 0%,rgba(11,27,46,.78) 40%,rgba(11,27,46,0) 72%)}
.hero .in{position:relative;z-index:2;max-width:68rem;margin:0 auto;padding:4.5rem 1.5rem 5.5rem;display:grid;grid-template-columns:auto minmax(0,36rem);gap:2.5rem;align-items:center;pointer-events:none}
.hero.sm .in{display:block;padding:3.2rem 1.5rem 3.4rem}
.hero .btn{pointer-events:auto}
.photo{display:block;width:11rem;height:11rem;object-fit:cover;border-radius:16px;border:3px solid rgba(255,255,255,.9);box-shadow:0 12px 36px rgba(0,0,0,.35)}
.eyebrow{margin:0 0 .5rem;color:var(--amber);font-weight:600;font-size:.95rem}
h1{font:500 clamp(2.4rem,6vw,3.9rem)/1.05 "Newsreader",Georgia,serif;letter-spacing:-.015em;margin:0 0 1rem}
.hero.sm h1{font-size:clamp(2.1rem,5vw,3rem);margin-bottom:.6rem}
.lede{margin:0 0 .6rem;color:#CBD7E4;font-size:1.12rem;line-height:1.6;max-width:36rem}
.aff{margin:0 0 1.6rem;color:#8EA3B8;font-size:.95rem}
.btn{display:inline-block;padding:.65rem 1.15rem;border-radius:8px;font-weight:600;font-size:.95rem;text-decoration:none;margin:0 .6rem .5rem 0}
.btn.pri{background:#fff;color:var(--navy)}
.btn.pri:hover{background:#E8EEF5}
.btn.ghost{border:1px solid rgba(255,255,255,.4);color:#fff}
.btn.ghost:hover{background:rgba(255,255,255,.1)}
.btn.dark{background:var(--navy);color:#fff;margin:0}
.btn.dark:hover{background:#17304D}
.facts{position:relative;z-index:3;margin-top:-2.6rem;display:grid;grid-template-columns:repeat(auto-fit,minmax(13rem,1fr));gap:1px;background:var(--line);border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:0 10px 30px rgba(11,27,46,.12)}
.facts div{background:#fff;padding:1.1rem 1.3rem}
.fl{display:block;color:var(--muted);font-size:.85rem}
.fv{display:block;font-weight:600;line-height:1.35;margin-top:.15rem}
.sec{padding:3.6rem 0 0}
.sec:last-of-type{padding-bottom:4.5rem}
h2{font:500 1.9rem/1.2 "Newsreader",Georgia,serif;margin:0 0 .4rem}
.sub{color:var(--muted);margin:0 0 1.5rem}
.sec h2+*{margin-top:1.2rem}
.bio p{margin:0 0 1rem;max-width:44rem;font-size:1.05rem}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(19rem,1fr));gap:1rem}
.stack{display:flex;flex-direction:column;gap:1rem}
.card{border:1px solid var(--line);border-radius:12px;padding:1.3rem 1.5rem;background:#fff;transition:box-shadow .2s,border-color .2s}
.card:hover{box-shadow:0 8px 24px rgba(11,27,46,.08);border-color:#CBD6E0}
.card h3{font-size:1.08rem;margin:0;line-height:1.35}
.t{display:flex;flex-wrap:wrap;align-items:baseline;gap:.25rem .7rem}
.badge{font-size:.78rem;font-weight:600;color:#8A5A00;background:#FFF3D6;border-radius:999px;padding:.05rem .65rem;white-space:nowrap}
.authors{margin:.4rem 0 0;font-size:.95rem;max-width:46rem}
.meta{color:var(--muted);font-size:.93rem;margin:.2rem 0 0}
.card p:not(.meta){margin:.55rem 0 0;max-width:46rem}
.chips{display:flex;flex-wrap:wrap;gap:.5rem;list-style:none;padding:0;margin:.9rem 0 0}
.chips li{background:var(--soft);border:1px solid var(--line);border-radius:999px;padding:.1rem .75rem;font-size:.86rem;color:var(--muted)}
.skills{margin-top:0}
.plain{list-style:none;margin:.6rem 0 0;padding:0}
.plain li{margin:0 0 .4rem}
footer{background:var(--navy);color:#8EA3B8;font-size:.9rem}
footer .wrap{display:flex;justify-content:space-between;flex-wrap:wrap;gap:.5rem 2rem;padding-top:1.6rem;padding-bottom:1.6rem}
@media (max-width:760px){.hero .in{grid-template-columns:1fr;gap:1.4rem;padding:2.6rem 1.5rem 4.2rem}.hero::after{background:linear-gradient(180deg,rgba(11,27,46,.92),rgba(11,27,46,.8))}.photo{width:7.5rem;height:7.5rem}}
"""


def item(i):
    title = e(i["title"])
    if i.get("link"):
        title = f'<a href="{e(i["link"])}" rel="noopener">{title}</a>'
    badge = f'<span class="badge">{e(i["status"])}</span>' if i.get("status") else ""
    authors = ""
    if i.get("authors"):
        a = e(i["authors"])
        h = e(getattr(c, "AUTHOR_NAME", ""))
        if h:
            a = a.replace(h, f"<strong>{h}</strong>")
        authors = f'<p class="authors">{a}</p>'
    doi = (f'<p class="meta"><a href="https://doi.org/{e(i["doi"])}" rel="noopener">DOI {e(i["doi"])}</a></p>'
           if i.get("doi") else "")
    meta = f'<p class="meta">{e(i["meta"])}</p>' if i.get("meta") else ""
    text = f"<p>{e(i['text'])}</p>" if i.get("text") else ""
    tags = "".join(f"<li>{e(x)}</li>" for x in i.get("tags", []))
    tags = f'<ul class="chips">{tags}</ul>' if tags else ""
    return f'<article class="card"><div class="t"><h3>{title}</h3>{badge}</div>{authors}{meta}{text}{doi}{tags}</article>'


def sec(title, inner, sub=""):
    s = f'<p class="sub">{e(sub)}</p>' if sub else ""
    return f'<section class="sec"><div class="wrap"><h2>{e(title)}</h2>{s}{inner}</div></section>'


def photo_tag():
    photo = P.get("photo", "")
    if not photo:
        return ""
    f = OUT / photo
    if not f.exists():
        print("warning: photo file not found:", f)
        return ""
    mime = "image/png" if f.suffix.lower() == ".png" else "image/jpeg"
    src = f"data:{mime};base64," + base64.b64encode(f.read_bytes()).decode()
    return f'<img class="photo" src="{src}" alt="Portrait of {e(P["name"])}" width="440" height="440">'


def hero_home():
    links = P.get("links") or []
    third = f'<a class="btn ghost" href="{e(links[0][1])}" rel="noopener">{e(links[0][0].split()[0])}</a>' if links else ""
    return ('<header class="hero"><div id="scene" aria-hidden="true"></div><div class="in">' + photo_tag()
            + f'<div><p class="eyebrow">{e(P["role"])}</p><h1>{e(P["name"])}</h1><p class="lede">{e(P["lede"])}</p>'
            f'<p class="aff">{e(P["affiliation"])}</p><p><a class="btn pri" href="research.html">View research</a>'
            f'<a class="btn ghost" href="contact.html">Contact</a>{third}</p></div></div></header>')


def hero_small(title, intro):
    return ('<header class="hero sm"><div id="scene" aria-hidden="true"></div><div class="in"><div>'
            f'<h1>{e(title)}</h1><p class="lede">{e(intro)}</p></div></div></header>')


def about():
    facts = '<div class="wrap"><div class="facts">' + "".join(
        f'<div><span class="fl">{e(l)}</span><span class="fv">{e(v)}</span></div>' for l, v in c.FACTS) + "</div></div>"
    bio = '<div class="bio">' + "".join(f"<p>{e(x)}</p>" for x in c.BIO) + "</div>"
    chips = '<ul class="chips skills">' + "".join(f"<li>{e(x)}</li>" for x in c.SKILLS) + "</ul>"
    extra = f'<p class="meta" style="margin-top:1.2rem">Languages: {e(c.LANGUAGES)}</p><p class="meta">{e(c.SERVICE)}</p>'
    return (hero_home() + facts + sec("About", bio)
            + sec("Education", '<div class="cards">' + "".join(item(i) for i in c.EDUCATION) + "</div>")
            + sec("Skills and service", chips + extra)
            + sec("Workshops and schools", '<div class="cards">' + "".join(item(i) for i in c.TRAINING) + "</div>"))


def research():
    return hero_small("Research", c.INTRO["research"]) + sec("Projects", '<div class="stack">' + "".join(item(i) for i in c.RESEARCH) + "</div>")


def publications():
    groups = {}
    for i in c.PUBLICATIONS:
        groups.setdefault(i.get("group", "Output"), []).append(i)
    body = "".join(sec(g, '<div class="stack">' + "".join(item(i) for i in its) + "</div>") for g, its in groups.items())
    return hero_small("Publications", c.INTRO["publications"]) + body


def contact():
    mail = (f'<article class="card"><h3>Email</h3><p class="meta">The quickest way to reach me.</p>'
            f'<p><a class="btn dark" href="mailto:{e(P["email"])}">{e(P["email"])}</a></p></article>')
    lk = "".join(f'<li><a href="{e(u)}" rel="noopener">{e(l)}</a></li>' for l, u in P["links"])
    online = f'<article class="card"><h3>Find me online</h3><ul class="plain">{lk}</ul></article>' if lk else ""
    addr = f'<article class="card"><h3>Address</h3><p>{e(P["affiliation"])}</p></article>'
    return hero_small("Contact", c.INTRO["contact"]) + sec("Get in touch", f'<div class="cards">{mail}{online}{addr}</div>')


def shell(file, label, body):
    nav = ""
    for f, l in PAGES:
        cur = ' aria-current="page"' if f == file else ""
        nav += f'<a href="{f}"{cur}>{l}</a>'
    title = f'{P["name"]} | {P["role"]}' if file == "index.html" else f'{label} | {P["name"]}'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(P['lede'])}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='9' fill='%23E8A317'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600&family=Newsreader:opsz,wght@6..72,400;6..72,500&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="top"><div class="wrap"><a class="brand" href="index.html">{e(P['name'])}</a><nav aria-label="Pages">{nav}</nav></div></div>
{body}
<footer><div class="wrap"><span>© {e(P['name'])}</span><span>{e(P['affiliation'])}</span></div></footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>{SCENE_JS}</script>
</body>
</html>
"""


BUILDERS = {"index.html": about, "research.html": research,
            "publications.html": publications, "contact.html": contact}

if __name__ == "__main__":
    for f, label in PAGES:
        (OUT / f).write_text(shell(f, label, BUILDERS[f]()), encoding="utf-8")
        print("wrote", f)
