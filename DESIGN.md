# La Tribu — Design System (v2, paleta "tierra y costa")

**Brand:** La Tribu — Escuela Secundaria comunitaria, Zapotal, Oaxaca (cerca de Mazunte).
**Personality:** cálido, honesto, comunitario, cercano a la tierra y al mar. Editorial y humano, nunca corporativo ni "tech". Fotografía real de jóvenes en la naturaleza con luz cálida; textura de papel.
**Language:** Spanish (Mexico) default; EN and FR versions. Tone: directo, sin rodeos, primera persona del plural.

## Colors

| Token | Hex | Use |
|---|---|---|
| `--color-bg` | `#F3EEE5` | Page background (papel crema) |
| `--color-bg-alt` | `#E9E3D8` | Alternating sections (beige) |
| `--color-surface` | `#FBF9F5` | Cards, form fields |
| `--color-ink` | `#2F3E46` | Primary text, headings (slate oscuro) |
| `--color-ink-soft` | `#5C6B70` | Secondary text |
| `--color-accent` | `#B8694B` | Terracota: primary CTA, links, CTA band |
| `--color-accent-hover` | `#9E5740` | CTA hover / accent text at body size |
| `--color-earth` | `#2E4A56` | Slate azul-verde profundo: footer, quote blocks, mobile menu |
| `--color-olive` | `#6B7A54` | Verde oliva: secondary CTA band |
| `--color-olive-deep` | `#5F6E55` | Secondary buttons, checkmarks |
| `--color-sage` | `#8FA08A` | Dividers, subtle badges |
| `--color-rose` | `#E5C4BD` | Icon circle tint, footer labels |
| `--color-sand` | `#E3D5C0` | Icon circle tint, avatars |
| `--color-stone` | `#B7BFC0` | Icon circle tint (gris azulado) |
| `--color-mint` | `#C9D3C4` | Icon circle tint (salvia claro) |
| `--color-line` | `#DCD5C8` | Borders, separators |
| `--color-success` | `#5F6E55` | Form success |
| `--color-error` | `#A9432F` | Form error |
| `--color-whatsapp` | `#25D366` | WhatsApp button only |

Contrast: `#2F3E46` on `#F3EEE5` = 10.2:1. `#F3EEE5` on `#B8694B` = 4.6:1 (buttons ≥16px semibold OK). `#F3EEE5` on `#6B7A54` = 5.1:1. `#F3EEE5` on `#2E4A56` = 9.4:1. Body-size terracotta text uses `#9E5740` (5.6:1).

Palette rhythm on a page: cream → beige → cream, with one deep slate quote block, one terracotta CTA band and one olive CTA band. Never two dark bands adjacent.

## Typography

- **Display / headings:** Alegreya (Google Fonts), humanist calligraphic serif. Weights 500 (h1/h2) and 700 (h3, brand). Tight tracking (-0.01em). Italic for quotes.
- **Body:** Alegreya Sans, 400/500/700. Line-height 1.6. Runs small, so body is 17.5px mobile / 19px desktop.
- **UI / labels / nav / eyebrows:** Alegreya Sans 700, uppercase, letter-spacing 0.12em, 13–14px. One type family across the site (chosen for its warmth, close to the Waldorf / anthroposophic visual world).

Scale (desktop / mobile): h1 64/40 · h2 44/32 · h3 26/22 · lead 20/18 · body 17/16 · small 14 · eyebrow 13.

## Spacing & layout

- Base unit 8px. Section padding 96px desktop / 64px mobile. Container 1200px, gutters 24/48px.
- Radius: cards 16px, buttons pill (999px), images 20px, inputs 12px, icon circles 50%.
- Shadows none by default; cards on hover `0 8px 24px rgba(47,62,70,0.08)`. Borders 1px `--color-line`.

## Components

**Buttons**: Primary terracotta pill, cream text. Secondary olive-deep pill, cream text. Cream pill (on colored bands) with terracotta text. Light outline pill on photos. WhatsApp green with icon. Ghost link terracotta + arrow.

**Nav**: sticky cream, 1px line, logo + "La Tribu" Alegreya, links Alegreya Sans, active link underlined terracotta; language switcher ES/EN/FR pill; CTA "Inscripciones" primary + WhatsApp icon. Mobile menu full-screen on `--color-earth`.

**Hero**: full-bleed warm photo, slate gradient overlay (`rgba(47,62,70,.30)` → `rgba(46,74,86,.62)`), cream Alegreya h1, primary + light outline CTAs.

**Feature icons**: 2px line icons in 64px tinted circles, rotating sand → rose → stone → mint.

**Cards**: surface on beige, 16px radius, 32px padding, tinted icon circle, h3, body.

**Quote block**: `--color-earth` full width, Alegreya italic cream, author uppercase in rose.

**CTA bands**: terracotta (`--color-accent`) for enrollment; olive (`--color-olive`) for "get to know us"; both with cream headings, cream pill + WhatsApp button. On home the two can sit side by side (split band) like the mockup.

**Accordion (FAQ)**: rows separated by `--color-line`, Alegreya questions, terracotta ± circle.

**Forms**: uppercase Alegreya Sans labels, 52px inputs on `--color-surface`, 12px radius, 2px terracotta focus ring, olive success panel.

**Footer**: `--color-earth`, cream text, rose uppercase column headings, social icon circles, legal line small.

## Imagery & icons

Photos: warm natural light, real teens outdoors (mar, sendero, huerto, cocina). Icons: 2px stroke, rounded caps, `--color-ink`. Logo: chevron/dot pyramid in `--color-ink`; cream on dark.

## Motion

Fade-up on scroll 400ms ease-out, 24px. Hover 150ms. Reduced-motion respected.
