#!/usr/bin/env python3
"""Ensambla site/*.html a partir de src/layout.html + src/pages/*.html.
Uso: python3 build.py
"""
import re, pathlib

ROOT = pathlib.Path(__file__).parent
LAYOUT = (ROOT / "src" / "layout.html").read_text(encoding="utf-8")
PAGES = ROOT / "src" / "pages"
OUT = ROOT / "site"

ICONS = {
    "ICON_WA": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 12 12 0 0 0 4.6 4c.6.3 1.1.4 1.5.5a3.6 3.6 0 0 0 1.6.1 2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.2c0-.1-.2-.2-.5-.3z"/></svg>',
    "ICON_IG": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>',
    "ICON_FB": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 22v-8h2.7l.4-3.2h-3.1V8.8c0-.9.3-1.6 1.6-1.6h1.7V4.4c-.3 0-1.3-.1-2.5-.1-2.5 0-4.1 1.5-4.1 4.2v2.3H7.4V14h2.8v8h3.3z"/></svg>',
    "ICON_YT": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22.5 7.2a2.8 2.8 0 0 0-2-2C18.8 4.8 12 4.8 12 4.8s-6.8 0-8.5.4a2.8 2.8 0 0 0-2 2A29 29 0 0 0 1.1 12a29 29 0 0 0 .4 4.8 2.8 2.8 0 0 0 2 2c1.7.4 8.5.4 8.5.4s6.8 0 8.5-.4a2.8 2.8 0 0 0 2-2 29 29 0 0 0 .4-4.8 29 29 0 0 0-.4-4.8zM9.8 15V9l5.7 3-5.7 3z"/></svg>',
    "ICON_TT": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.5 3c.3 2.3 1.7 3.7 4 3.9v3a7.3 7.3 0 0 1-4-1.3v6.3A5.9 5.9 0 1 1 10.6 9v3.1a2.9 2.9 0 1 0 2.9 2.9V3h3z"/></svg>',
}

def build_page(src: pathlib.Path):
    raw = src.read_text(encoding="utf-8")
    meta = dict(re.findall(r"<!--\s*(\w+):\s*(.*?)\s*-->", raw.split("\n<!-- /meta -->")[0]))
    content = raw.split("<!-- /meta -->", 1)[1] if "<!-- /meta -->" in raw else raw
    html = LAYOUT.replace("{{TITLE}}", meta.get("title", "La Tribu")) \
                 .replace("{{DESC}}", meta.get("desc", "")) \
                 .replace("{{CONTENT}}", content.strip("\n"))
    for k, v in ICONS.items():
        html = html.replace("{{" + k + "}}", v)
    (OUT / src.name).write_text(html, encoding="utf-8")
    print("built", src.name)

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for p in sorted(PAGES.glob("*.html")):
        build_page(p)
