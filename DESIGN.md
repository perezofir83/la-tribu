# La Tribu — Design System

**Brand:** La Tribu — Escuela Secundaria comunitaria, Zapotal, Oaxaca (cerca de Mazunte).
**Personality:** cálido, honesto, comunitario, cercano a la tierra. Editorial y humano, nunca corporativo ni "tech". Fotografía real de jóvenes en la naturaleza; textura de papel, tierra, bambú.
**Language:** Spanish (Mexico). Tone: directo, sin rodeos, primera persona del plural ("nos", "platicamos").

## Colors

| Token | Hex | Use |
|---|---|---|
| `--color-bg` | `#FAF8F4` | Page background (crema / papel) |
| `--color-bg-alt` | `#F1ECE2` | Alternating sections, cards |
| `--color-surface` | `#FFFFFF` | Cards on alt background, form fields |
| `--color-ink` | `#2D3E33` | Primary text, forest green |
| `--color-ink-soft` | `#5B6B60` | Secondary text |
| `--color-accent` | `#D96C4A` | Terracotta: CTAs, headings accent, links |
| `--color-accent-hover` | `#AD5540` | CTA hover |
| `--color-earth` | `#3A1A10` | Dark sections (quotes, hero overlay, footer) |
| `--color-sage` | `#93A893` | Icons, dividers, subtle badges |
| `--color-olive` | `#2F3B22` | Alternate dark heading |
| `--color-line` | `#E3DCCF` | Borders, separators |
| `--color-success` | `#4F7A5A` | Form success |
| `--color-error` | `#B33A2B` | Form error |
| `--color-whatsapp` | `#25D366` | WhatsApp button only |

Contrast: `#2D3E33` on `#FAF8F4` = 10.9:1. `#D96C4A` on `#FAF8F4` = 3.4:1 → use only for text ≥ 24px or as background with white text (5.0:1 with `#FFFFFF`? no — use `#FAF8F4` text on `#D96C4A` buttons at ≥ 16px semibold; body-size accent text uses `#AD5540`, 5.1:1).

## Typography

- **Display / headings:** Fraunces (Google Fonts), variable, optical size on. Weights 500–600. Tight tracking (-0.01em). Italic allowed for single emphasized word.
- **Body:** Manrope, 400/500/600. Line-height 1.6.
- **UI / labels / nav / eyebrows:** Space Grotesk 500, uppercase, letter-spacing 0.12em, 12–13px.

Scale (desktop / mobile):
- Display `h1`: 64 / 40px, Fraunces 500, lh 1.05
- `h2`: 44 / 32px, Fraunces 500, lh 1.15
- `h3`: 26 / 22px, Fraunces 600
- Lead: 20 / 18px, Manrope 400
- Body: 17 / 16px
- Small: 14px
- Eyebrow: 13px Space Grotesk uppercase

## Spacing & layout

- Base unit 8px. Section padding 96px desktop / 64px mobile.
- Container max-width 1200px, gutters 24px (mobile) / 48px.
- Grid 12 col. Cards in 4 → 2 → 1 columns.
- Radius: cards 16px, buttons 999px (pill), images 20px, inputs 12px.
- Shadows: none by default; cards on hover `0 8px 24px rgba(45,62,51,0.08)`.
- Borders 1px `--color-line`.

## Components

**Buttons**
- Primary: bg `--color-accent`, text `#FAF8F4`, pill, 16px Manrope 600, padding 14px 28px. Hover `--color-accent-hover`, translateY(-1px).
- Secondary: transparent, 1.5px border `--color-ink`, text `--color-ink`. Hover fill `--color-ink`, text `#FAF8F4`.
- WhatsApp: bg `#25D366`, white text, WhatsApp icon left. Used in nav (compact) and CTA blocks.
- Ghost link: accent text + arrow, underline on hover.

**Nav**: sticky, cream with 1px bottom line, logo left (icon + "La Tribu" in Fraunces 600), links center (Space Grotesk 500 15px), CTA right "Inscripciones" (primary) + WhatsApp icon button. Mobile: hamburger → full-screen menu on `--color-earth`.

**Hero**: full-bleed photo with gradient overlay (`rgba(58,26,16,0.55)` → `0.25`), centered white Fraunces h1, one primary CTA + one secondary (outline light). Height 80vh min 560px.

**Cards** (talleres, pilares, materias): `--color-surface` on alt bg, 16px radius, 32px padding, line icon 40px (stroke 2px, `--color-ink`), h3, body. Numbered steps use a 48px circle with Fraunces numeral in accent.

**Quote block**: full-width `--color-earth`, Fraunces italic 32–40px, cream text, author in Space Grotesk uppercase sage.

**Accordion (FAQ)**: rows separated by `--color-line`, question Fraunces 22px, plus/minus icon in accent, answer Manrope.

**Forms (landing)**: labels Space Grotesk uppercase 12px; inputs 52px height, `--color-surface`, 1px `--color-line`, radius 12px, focus ring 2px accent. Required marker in accent. Submit = primary full-width on mobile. Success state: sage panel with check icon.

**Footer**: `--color-earth` background, cream text, 4 columns (marca + descripción, navegación, contacto, redes), social icons row, legal line small.

## Imagery & icons

- Photos: warm, natural light, real teens outdoors (mar, sendero, huerto). No stock smiles. Slight warm grade.
- Icons: 2px stroke line icons, rounded caps, `--color-ink` (see extracted set: pala, escuadra, matraz, semillas, corazón, balanza, brote, triángulo).
- Logo: chevron/dot pyramid in `--color-ink`; on dark use cream.

## Motion

- Fade-up on scroll 400ms ease-out, 24px. Reduced-motion respected.
- Hover transitions 150ms.

## Pages

1. Inicio · 2. Quiénes somos · 3. El proyecto educativo · 4. La biblioteca · 5. Preguntas frecuentes · 6. **Inscripciones** (landing con formulario de datos: nombre, WhatsApp, email, nombre y edad del/la estudiante, grado de interés 1º/2º, cómo nos conociste, mensaje).
