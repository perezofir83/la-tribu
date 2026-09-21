#!/usr/bin/env python3
"""Ensambla site/ a partir de src/layout.html + src/pages/<lang>/*.html.
ES (default) → site/*.html · EN → site/en/*.html · FR → site/fr/*.html
Uso: python3 build.py
"""
import re, pathlib, shutil, time

ROOT = pathlib.Path(__file__).parent
LAYOUT = (ROOT / "src" / "layout.html").read_text(encoding="utf-8")
PAGES = ROOT / "src" / "pages"
OUT = ROOT / "site"

LANGS = {
    "es": {"dir": "", "html_lang": "es-MX", "og_locale": "es_MX", "label": "ES", "name": "Español"},
    "en": {"dir": "en", "html_lang": "en", "og_locale": "en_US", "label": "EN", "name": "English"},
    "fr": {"dir": "fr", "html_lang": "fr", "og_locale": "fr_FR", "label": "FR", "name": "Français"},
}

# Nombres de archivo por idioma (misma clave lógica en los tres).
SLUGS = {
    "index":     {"es": "index.html", "en": "index.html", "fr": "index.html"},
    "about":     {"es": "quienes-somos.html", "en": "about.html", "fr": "qui-sommes-nous.html"},
    "project":   {"es": "proyecto-educativo.html", "en": "educational-project.html", "fr": "projet-educatif.html"},
    "library":   {"es": "biblioteca.html", "en": "library.html", "fr": "bibliotheque.html"},
    "faq":       {"es": "preguntas-frecuentes.html", "en": "faq.html", "fr": "faq.html"},
    "enroll":    {"es": "inscripciones.html", "en": "enrollment.html", "fr": "inscriptions.html"},
}

STRINGS = {
    "es": {
        "skip": "Ir al contenido", "home": "Inicio", "about": "Quiénes somos", "project": "El proyecto educativo",
        "library": "La biblioteca", "faq": "Preguntas frecuentes", "enroll": "Inscripciones",
        "cta_data": "Déjanos tus datos", "wa_aria": "Escríbenos por WhatsApp", "menu_open": "Abrir menú", "menu_close": "Cerrar menú",
        "f_desc": "Proyecto educativo sin fines de lucro con un enfoque humano, consciente, comunitario y de desarrollo integral.",
        "f_nav": "Navegación", "f_contact": "Contacto", "f_contact1": "Nos puedes contactar por WhatsApp.",
        "f_contact2": "Zapotal, Oaxaca · cerca de Mazunte", "f_follow": "Síguenos",
        "f_legal": "© 2026 La Tribu — Escuela Secundaria. Zapotal, Oaxaca. Proyecto comunitario sin fines de lucro.",
        "lang_aria": "Idioma",
        "schema_desc": "Secundaria comunitaria sin fines de lucro en Zapotal, Oaxaca, cerca de Mazunte. Pedagogía activa: hacer, sentir y pensar.",
    },
    "en": {
        "skip": "Skip to content", "home": "Home", "about": "About us", "project": "Educational project",
        "library": "Library", "faq": "FAQ", "enroll": "Enrollment",
        "cta_data": "Leave your details", "wa_aria": "Message us on WhatsApp", "menu_open": "Open menu", "menu_close": "Close menu",
        "f_desc": "A non-profit educational project with a human, conscious, community-based approach to whole-person development.",
        "f_nav": "Navigation", "f_contact": "Contact", "f_contact1": "You can reach us on WhatsApp.",
        "f_contact2": "Zapotal, Oaxaca · near Mazunte", "f_follow": "Follow us",
        "f_legal": "© 2026 La Tribu — Secondary School. Zapotal, Oaxaca. Non-profit community project.",
        "lang_aria": "Language",
        "schema_desc": "Non-profit community secondary school in Zapotal, Oaxaca, near Mazunte. Active pedagogy: doing, feeling and thinking.",
    },
    "fr": {
        "skip": "Aller au contenu", "home": "Accueil", "about": "Qui sommes-nous", "project": "Le projet éducatif",
        "library": "La bibliothèque", "faq": "Questions fréquentes", "enroll": "Inscriptions",
        "cta_data": "Laissez-nous vos coordonnées", "wa_aria": "Écrivez-nous sur WhatsApp", "menu_open": "Ouvrir le menu", "menu_close": "Fermer le menu",
        "f_desc": "Projet éducatif à but non lucratif, avec une approche humaine, consciente, communautaire et de développement intégral.",
        "f_nav": "Navigation", "f_contact": "Contact", "f_contact1": "Vous pouvez nous contacter sur WhatsApp.",
        "f_contact2": "Zapotal, Oaxaca · près de Mazunte", "f_follow": "Suivez-nous",
        "f_legal": "© 2026 La Tribu — Collège (secundaria). Zapotal, Oaxaca. Projet communautaire à but non lucratif.",
        "lang_aria": "Langue",
        "schema_desc": "Collège communautaire à but non lucratif à Zapotal, Oaxaca, près de Mazunte. Pédagogie active : faire, sentir et penser.",
    },
}

ICONS = {
    "ICON_WA": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 12 12 0 0 0 4.6 4c.6.3 1.1.4 1.5.5a3.6 3.6 0 0 0 1.6.1 2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.2c0-.1-.2-.2-.5-.3z"/></svg>',
    "ICON_IG": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>',
    "ICON_FB": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 22v-8h2.7l.4-3.2h-3.1V8.8c0-.9.3-1.6 1.6-1.6h1.7V4.4c-.3 0-1.3-.1-2.5-.1-2.5 0-4.1 1.5-4.1 4.2v2.3H7.4V14h2.8v8h3.3z"/></svg>',
    "ICON_YT": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22.5 7.2a2.8 2.8 0 0 0-2-2C18.8 4.8 12 4.8 12 4.8s-6.8 0-8.5.4a2.8 2.8 0 0 0-2 2A29 29 0 0 0 1.1 12a29 29 0 0 0 .4 4.8 2.8 2.8 0 0 0 2 2c1.7.4 8.5.4 8.5.4s6.8 0 8.5-.4a2.8 2.8 0 0 0 2-2 29 29 0 0 0 .4-4.8 29 29 0 0 0-.4-4.8zM9.8 15V9l5.7 3-5.7 3z"/></svg>',
    "ICON_TT": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.5 3c.3 2.3 1.7 3.7 4 3.9v3a7.3 7.3 0 0 1-4-1.3v6.3A5.9 5.9 0 1 1 10.6 9v3.1a2.9 2.9 0 1 0 2.9 2.9V3h3z"/></svg>',
}

SITE_URL = "https://escuelalatribu.xyz/"
VERSION = str(int(time.time()))


def page_key_for(lang, filename):
    for key, m in SLUGS.items():
        if m[lang] == filename:
            return key
    raise SystemExit(f"Página sin slug registrado: {lang}/{filename}")


def href(lang, key, from_lang):
    """Ruta relativa desde una página de from_lang a la página key en lang."""
    if lang == from_lang:
        return SLUGS[key][lang]
    target_dir = LANGS[lang]["dir"]
    from_dir = LANGS[from_lang]["dir"]
    up = "../" if from_dir else ""
    prefix = (target_dir + "/") if target_dir else ""
    return up + prefix + SLUGS[key][lang]


def build_page(lang, src: pathlib.Path):
    raw = src.read_text(encoding="utf-8")
    head = raw.split("<!-- /meta -->", 1)[0]
    meta = dict(re.findall(r"<!--\s*(\w+):\s*(.*?)\s*-->", head))
    content = raw.split("<!-- /meta -->", 1)[1]
    key = page_key_for(lang, src.name)
    base = "../" if LANGS[lang]["dir"] else ""
    s = STRINGS[lang]

    # Fotos del equipo: si existe site/assets/team/<slug>.jpg sustituye a las iniciales.
    def team_photo(m):
        slug, initials = m.group(1), m.group(2)
        if (OUT / "assets" / "team" / f"{slug}.jpg").exists():
            return (f'<div class="person__avatar person__avatar--photo">'
                    f'<img src="{base}assets/team/{slug}.jpg?v={VERSION}" alt="" width="600" height="600" loading="lazy"></div>')
        return f'<div class="person__avatar">{initials}</div>'
    content = re.sub(r'<div class="person__avatar" data-photo="([^"]+)">([^<]*)</div>', team_photo, content)

    # Enlaces internos dentro del contenido: {{P:about}} → ruta correcta.
    content = re.sub(r"\{\{P:(\w+)\}\}", lambda m: href(lang, m.group(1), lang), content)

    html = LAYOUT
    repl = {
        "TITLE": meta.get("title", "La Tribu"),
        "DESC": meta.get("desc", ""),
        "CONTENT": content.strip("\n"),
        "BASE": base,
        "HTML_LANG": LANGS[lang]["html_lang"],
        "OG_LOCALE": LANGS[lang]["og_locale"],
        "LANG": lang,
        "V": VERSION,
        "CANONICAL": SITE_URL + ((LANGS[lang]["dir"] + "/") if LANGS[lang]["dir"] else "") + SLUGS[key][lang],
        "ALT_ES": SITE_URL + SLUGS[key]["es"],
        "ALT_EN": SITE_URL + "en/" + SLUGS[key]["en"],
        "ALT_FR": SITE_URL + "fr/" + SLUGS[key]["fr"],
        "LNK_ES": href("es", key, lang), "LNK_EN": href("en", key, lang), "LNK_FR": href("fr", key, lang),
        "CUR_ES": ' aria-current="true"' if lang == "es" else "",
        "CUR_EN": ' aria-current="true"' if lang == "en" else "",
        "CUR_FR": ' aria-current="true"' if lang == "fr" else "",
    }
    for k in SLUGS:
        repl["P_" + k.upper()] = href(lang, k, lang)
    for k, v in s.items():
        repl["S_" + k.upper()] = v
    for k, v in repl.items():
        html = html.replace("{{" + k + "}}", v)
    for k, v in ICONS.items():
        html = html.replace("{{" + k + "}}", v)
    out_dir = OUT / LANGS[lang]["dir"] if LANGS[lang]["dir"] else OUT
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / src.name).write_text(html, encoding="utf-8")
    leftover = re.findall(r"\{\{[A-Z_:a-z]+\}\}", html)
    if leftover:
        print("  ⚠ placeholders sin resolver en", lang, src.name, set(leftover))
    print("built", lang, src.name)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for lang in LANGS:
        d = PAGES / lang
        if LANGS[lang]["dir"]:
            shutil.rmtree(OUT / LANGS[lang]["dir"], ignore_errors=True)
        for p in sorted(d.glob("*.html")):
            build_page(lang, p)
