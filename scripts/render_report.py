#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SECTIONS = [
    ("Synthesis", [("outputs", "synthesis.md")]),
    ("Buyer", [("cards", "*.md"), ("outputs", "literature-casting.md")]),
    ("Gaps", [("outputs", "gaps.md")]),
    ("Competitors", [("outputs", "competitor-map.md"), ("outputs/competitors", "*.md")]),
    ("Search log", [("outputs/competitors", "direct-search.md")]),
    ("Baseline", [("outputs", "baseline.md")]),
    ("Brief", [(".", "brief.md")]),
    ("Calls", [("outputs/clues", "*.md")]),
    ("Watch", [("outputs/watch", "*.md")]),
]


def title_of(path: Path, text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            if "--" not in title:
                return title
            break
    name = path.stem.split("--")
    client = name[0].replace("-", " ").title()
    rest = name[-1]
    date = rest[:10] if rest[:4].isdigit() else ""
    return f"{client} {date}".strip()


KINDS = [("scoping", "Scoping"), ("discovery", "Discovery"), ("proposal", "Pricing"), ("pricing", "Pricing"),
         ("check-in", "Check-in"), ("touchbase", "Touchbase"), ("onsite", "On-site"), ("delivery", "Working session"),
         ("sync", "Sync"), ("bootcamp", "Bootcamp"), ("quick-chat", "Chat"), ("catchup", "Catch-up")]


def call_label(path: Path) -> tuple[str, str]:
    parts = path.stem.split("--")
    group = parts[0].replace("-", " ").title()
    rest = parts[-1].lower()
    date = rest[:10] if rest[:4].isdigit() else ""
    kind = next((name for key, name in KINDS if key in rest), "Call")
    return group, f"{date} · {kind}" if date else kind


LOGS = {"direct-search.md"}


def collect() -> list[dict]:
    docs = []
    for section, patterns in SECTIONS:
        for folder, pattern in patterns:
            base = ROOT / folder
            if not base.exists():
                continue
            for path in sorted(base.glob(pattern)):
                if path.name.lower() == "readme.md" or not path.is_file():
                    continue
                if section == "Competitors" and path.name in LOGS:
                    continue
                text = path.read_text(errors="replace")
                doc = {
                    "id": f"d{len(docs)}",
                    "section": section,
                    "title": title_of(path, text),
                    "path": str(path.relative_to(ROOT)),
                    "md": text,
                }
                if section == "Calls":
                    doc["group"], doc["label"] = call_label(path)
                docs.append(doc)
    return docs


PAGE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Buyer Brain Report</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/marked@12/marked.min.js"></script>
<style>
:root {
  --bg: #fbfaf8; --panel: #ffffff; --ink: #1a1a19; --soft: #4a4946; --muted: #8a8780;
  --line: #ebe8e2; --accent: #1a1a19; --accent-soft: #efede8; --quote-ink: #1a1a19; --link: #2b5bd7; --hover: #f3f1ec;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #121312; --panel: #181a19; --ink: #ecebe7; --soft: #c4c2bc; --muted: #86847e;
    --line: #262826; --accent: #ecebe7; --accent-soft: #232523; --quote-ink: #f4f3ef; --link: #8fb0ff; --hover: #202321;
  }
}
:root[data-theme="dark"] {
  --bg: #121312; --panel: #181a19; --ink: #ecebe7; --soft: #c4c2bc; --muted: #86847e;
  --line: #262826; --accent: #ecebe7; --accent-soft: #232523; --quote-ink: #f4f3ef; --link: #8fb0ff; --hover: #202321;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--ink); font: 16px/1.65 Inter, system-ui, sans-serif; -webkit-font-smoothing: antialiased; }
.wrap { display: grid; grid-template-columns: 280px 1fr; min-height: 100vh; }
nav { border-right: 1px solid var(--line); padding: 28px 16px; position: sticky; top: 0; height: 100vh; overflow-y: auto; background: var(--bg); }
nav h1 { font-size: 15px; font-weight: 600; margin: 0 8px 18px; }
nav input { width: 100%; padding: 8px 12px; border: 1px solid var(--line); border-radius: 999px; background: var(--panel); color: var(--ink); margin-bottom: 8px; font: inherit; font-size: 13px; outline: none; }
nav input:focus { border-color: var(--muted); }
nav .sec { font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: .1em; color: var(--muted); margin: 22px 8px 6px; }
nav a { display: block; padding: 5px 8px; border-radius: 6px; color: var(--soft); text-decoration: none; font-size: 13.5px; line-height: 1.4; }
nav a:hover { background: var(--hover); color: var(--ink); }
nav a.on { background: var(--accent-soft); color: var(--ink); font-weight: 600; }
main { padding: 56px 64px 96px; }
.page { max-width: 760px; margin: 0 auto; }
.path { color: var(--muted); font-size: 12px; margin-bottom: 14px; }
article h1 { font-weight: 700; font-size: 32px; line-height: 1.2; letter-spacing: -.02em; margin: 0 0 20px; }
article h1 + p { color: var(--soft); }
article h2 { font-weight: 700; font-size: 21px; letter-spacing: -.01em; margin: 56px 0 14px; }
article h3 { font-size: 18px; font-weight: 600; margin: 0 0 12px; color: var(--ink); }
article section.pattern { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 24px 28px; margin: 20px 0; }
article p, article li { color: var(--soft); }
article strong { color: var(--ink); font-weight: 600; }
article ul { padding-left: 20px; }
article li { margin: 6px 0; }
article li::marker { color: var(--muted); }
article q { color: var(--quote-ink); font-weight: 500; }
article blockquote { margin: 18px 0; padding: 2px 16px; border-left: 2px solid var(--line); color: var(--quote-ink); }
article code { font-size: 11.5px; color: var(--muted); background: none; padding: 0; overflow-wrap: anywhere; }
article pre { overflow-x: auto; background: var(--panel); border: 1px solid var(--line); padding: 14px; border-radius: 10px; }
article pre code { color: var(--soft); font-size: 13px; }
article a { color: var(--link); }
article table { border-collapse: collapse; width: 100%; display: block; overflow-x: auto; font-size: 14px; }
article th, article td { border-bottom: 1px solid var(--line); padding: 8px 10px; text-align: left; vertical-align: top; }
article hr { border: 0; border-top: 1px solid var(--line); margin: 40px 0; }
.toggle { position: fixed; top: 16px; right: 20px; border: 1px solid var(--line); background: var(--panel); color: var(--soft); border-radius: 999px; padding: 5px 12px; cursor: pointer; font: inherit; font-size: 12px; }
.menu { display: none; }
@media (max-width: 860px) {
  .wrap { grid-template-columns: 1fr; }
  nav { position: fixed; inset: 0 auto 0 0; width: 86%; max-width: 300px; transform: translateX(-100%); transition: transform .2s; z-index: 5; background: var(--panel); }
  nav.open { transform: none; box-shadow: 0 0 40px rgba(0,0,0,.18); }
  main { padding: 64px 16px 64px; }
  article section.pattern { padding: 18px; }
  .menu { display: block; position: fixed; top: 16px; left: 16px; z-index: 6; border: 1px solid var(--line); background: var(--panel); color: var(--soft); border-radius: 999px; padding: 5px 12px; font: inherit; font-size: 12px; }
  article h1 { font-size: 28px; }
}

nav details.grp { margin: 0; }
nav details.grp summary { list-style: none; display: flex; justify-content: space-between; align-items: center; padding: 5px 8px; border-radius: 6px; color: var(--soft); font-size: 13.5px; cursor: pointer; }
nav details.grp summary::-webkit-details-marker { display: none; }
nav details.grp summary:hover { background: var(--hover); color: var(--ink); }
nav details.grp summary em { font-style: normal; font-size: 11px; color: var(--muted); }
nav details.grp[open] summary { color: var(--ink); font-weight: 600; }
nav details.grp a { padding-left: 20px; font-size: 12.5px; color: var(--muted); }
nav details.grp a.on { color: var(--ink); }
nav a { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
sup.cite { font-size: 10px; margin-left: 1px; }
sup.cite a { color: var(--muted); text-decoration: none; padding: 0 2px; }
sup.cite a:hover { color: var(--link); }
.sources { margin-top: 64px; border-top: 1px solid var(--line); padding-top: 8px; }
.sources h2 { font-size: 14px !important; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); }
.sources ol { font-size: 12px; color: var(--muted); padding-left: 22px; }
.sources li { color: var(--muted) !important; margin: 3px 0; }
.sources b { font-weight: 500; color: var(--soft); }
</style>
</head>
<body>
<button class="menu" onclick="document.querySelector('nav').classList.toggle('open')">Menu</button>
<button class="toggle" onclick="flip()">Theme</button>
<div class="wrap">
<nav><h1>Buyer Brain</h1><input id="q" placeholder="Filter" oninput="build()"><div id="links"></div></nav>
<main><div class="page"><div class="path" id="path"></div><article id="doc"></article></div></main>
</div>
<script id="data" type="application/json">__DATA__</script>
<script>
const docs = JSON.parse(document.getElementById('data').textContent);
function visible() { return docs; }
function flip() {
  const r = document.documentElement;
  const dark = r.dataset.theme ? r.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
  r.dataset.theme = dark ? 'light' : 'dark';
}
function build() {
  const q = document.getElementById('q').value.toLowerCase();
  const box = document.getElementById('links');
  box.innerHTML = '';
  let last = '', group = null, groupName = '';
  for (const d of visible()) {
    if (q && !(d.title + ' ' + (d.group || '') + ' ' + d.md).toLowerCase().includes(q)) continue;
    if (d.section !== last) { const s = document.createElement('div'); s.className = 'sec'; s.textContent = d.section; box.appendChild(s); last = d.section; group = null; groupName = ''; }
    const a = document.createElement('a'); a.href = '#' + d.id; a.id = 'l' + d.id;
    if (d.group) {
      if (d.group !== groupName) {
        group = document.createElement('details'); group.className = 'grp';
        if (q) group.open = true;
        const sm = document.createElement('summary'); sm.innerHTML = '<span></span><em></em>';
        sm.firstChild.textContent = d.group; group.appendChild(sm); box.appendChild(group); groupName = d.group;
      }
      a.textContent = d.label; group.appendChild(a);
      group.querySelector('em').textContent = group.querySelectorAll('a').length;
    } else { a.textContent = d.title; box.appendChild(a); }
  }
  mark();
}
function cite(md) {
  const refs = [], index = {};
  let lastFile = '';
  const out = md.replace(/\s*\(\s*`?((?:inputs|outputs|cards)\/[^`)\s]+?|\.\.\.)`?\s*(?::\s*(\d(?:[\d,\-\s]*\d)?))?`?\s*\)/g, (m, file, line) => {
    if (file === '...') file = lastFile; else lastFile = file;
    if (!file) return m;
    const key = file + ':' + (line || '').trim();
    if (!(key in index)) { refs.push({ file, line: (line || '').trim() }); index[key] = refs.length; }
    return '⟦' + index[key] + '⟧';
  });
  const out2 = out.replace(/`((?:inputs|outputs|cards)\/[^`\s]+?)(?::(\d(?:[\d,\-]*\d)?))?`(?::(\d(?:[\d,\-]*\d)?))?/g, (m, file, l1, l2) => {
    const line = (l1 || l2 || '').trim(); lastFile = file;
    const key = file + ':' + line;
    if (!(key in index)) { refs.push({ file, line }); index[key] = refs.length; }
    return '⟦' + index[key] + '⟧';
  });
  const out2b = out2.replace(/(?<![\w\/.:-])`?((?:inputs|outputs|cards)\/[^\s`);,:]*[A-Za-z0-9])`?(?::(\d(?:[\d,\-]*\d)?))?/g, (m, file, line) => {
    line = (line || '').trim();
    const key = file + ':' + line;
    if (!(key in index)) { refs.push({ file, line }); index[key] = refs.length; }
    return '⟦' + index[key] + '⟧';
  });
  const order = {}, sorted = [];
  const out3 = out2b.replace(/⟦(\d+)⟧/g, (m, n) => {
    if (!(n in order)) { sorted.push(refs[n - 1]); order[n] = sorted.length; }
    return '⟦' + order[n] + '⟧';
  });
  return { out: out3, refs: sorted };
}
function dress(h, refs) {
  h = h.replace(/⟦(\d+)⟧/g, (m, n) => '<sup class="cite"><a href="javascript:void(0)" onclick="document.getElementById(\'src' + n + '\').scrollIntoView({behavior:\'smooth\'})">' + n + '</a></sup>');
  if (refs && refs.length) {
    h += '<section class="sources"><h2>Sources</h2><ol>' + refs.map((r, i) => '<li id="src' + (i + 1) + '"><span>' + r.file.split('/').slice(-2).join(' / ') + '</span>' + (r.line ? ' <b>line ' + r.line + '</b>' : '') + '</li>').join('') + '</ol></section>';
  }
  const box = document.createElement('div'); box.innerHTML = h;
  box.querySelectorAll('h3').forEach(h3 => {
    if (h3.closest('.sources')) return;
    const sec = document.createElement('section'); sec.className = 'pattern';
    h3.parentNode.insertBefore(sec, h3);
    let n = h3; while (n && !(n !== h3 && /^H[123]$/.test(n.tagName))) { const next = n.nextSibling; sec.appendChild(n); n = next; }
  });
  const walk = document.createTreeWalker(box, NodeFilter.SHOW_TEXT);
  const texts = []; while (walk.nextNode()) texts.push(walk.currentNode);
  for (const t of texts) {
    if (t.parentNode.closest('code,pre,q')) continue;
    const parts = t.textContent.split(/(“[^”]{3,}”|"[^"]{3,}")/);
    if (parts.length < 2) continue;
    const frag = document.createDocumentFragment();
    parts.forEach((p, i) => { if (i % 2) { const q = document.createElement('q'); q.textContent = p.slice(1, -1); frag.appendChild(q); } else if (p) frag.appendChild(document.createTextNode(p)); });
    t.parentNode.replaceChild(frag, t);
  }
  return box.innerHTML;
}
function show() {
  const vis = visible();
  const id = location.hash.slice(1) || (vis[0] && vis[0].id);
  const d = vis.find(x => x.id === id) || vis[0];
  if (!d) { document.getElementById('doc').innerHTML = '<h1>No outputs yet</h1><p>Run buyer brain first.</p>'; return; }
  document.getElementById('path').textContent = d.path;
  const c = cite(d.md);
  document.getElementById('doc').innerHTML = dress(marked.parse(c.out), c.refs);
  document.querySelector('nav').classList.remove('open');
  window.scrollTo(0, 0);
  mark();
}
function mark() {
  document.querySelectorAll('nav a').forEach(a => { const on = a.hash === location.hash || (!location.hash && docs[0] && a.id === 'l' + docs[0].id); a.classList.toggle('on', on); if (on && a.parentNode.tagName === 'DETAILS') a.parentNode.open = true; });
}
addEventListener('hashchange', show);
build(); show();
</script>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=ROOT / "outputs" / "report.html")
    args = parser.parse_args()
    docs = collect()
    data = json.dumps(docs).replace("</", "<\\/")
    page = PAGE
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(page.replace("__DATA__", data))
    print(f"Wrote {args.out} with {len(docs)} documents")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
