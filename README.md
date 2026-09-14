# La Tribu — sitio web nuevo

Sitio estático (HTML/CSS/JS, sin frameworks) para **La Tribu — Escuela Secundaria**, Zapotal, Oaxaca.

## Estructura

```
DESIGN.md              Design system (subido a Google Stitch, proyecto "La Tribu — Escuela Secundaria")
extracted/content.md   Todo el contenido copiado del Wix original (5 páginas)
extracted/images/      Imágenes originales descargadas de Wix
src/layout.html        Nav + footer compartidos
src/pages/*.html       Contenido de cada página
build.py               Ensambla src → site/
site/                  Sitio listo para publicar (sube esta carpeta tal cual)
site/assets/config.js  WhatsApp, correo de leads, Web3Forms key, redes sociales
```

Páginas: `index`, `quienes-somos`, `proyecto-educativo`, `biblioteca`, `preguntas-frecuentes`, `inscripciones` (landing con formulario de leads).

## Editar

1. Cambia texto en `src/pages/*.html` (o nav/footer en `src/layout.html`).
2. `python3 build.py`
3. Sube `site/`.

Vista local: `python3 -m http.server 8765 --directory site` → http://localhost:8765

## Leads → Gmail (pendiente de configurar)

El formulario de `inscripciones.html` envía por **Web3Forms** (gratis, 250 envíos/mes) al correo que se configure.
Mientras no haya key, el formulario abre WhatsApp con los datos ya escritos (respaldo funcional).

1. Crear el Gmail nuevo de La Tribu (p. ej. `latribu.zapotal@gmail.com`).
2. Entrar a https://web3forms.com → "Create Access Key" con ese Gmail → confirmar el correo.
3. Pegar en `site/assets/config.js`:
   ```js
   leadEmail: "latribu.zapotal@gmail.com",
   web3formsKey: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
   ```
4. En Gmail: crear filtro "Asunto contiene: Nuevo lead La Tribu" → etiqueta **Leads** + estrella.

Campos que llegan: nombre, whatsapp, email, estudiante, edad, grado, origen, mensaje, consentimiento, resumen.

## Redes sociales

En `config.js` → `social: { instagram, facebook, youtube, tiktok }`. Los íconos del footer aparecen solo si hay URL.

## Dominio (verificado 14-sep-2026)

| Dominio | Estado | Precio aprox./año (Porkbun) |
|---|---|---|
| latribu.edu.mx | libre en registro, **pero .edu.mx requiere acreditar institución educativa ante NIC México** (RVOE/acta); La Tribu no está incorporada a la SEP → probablemente no elegible | ~$40 USD (Akky/NIC) |
| latribu.mx / latribu.com.mx / latribu.com / .org / .net | ocupados | — |
| **escuelalatribu.mx**, latribuzapotal.mx, secundarialatribu.mx | libres | ~$36 reg / $41 renov |
| **latribu.school** | libre | $5.66 reg / $29 renov |
| latribu.education | libre | $21 reg / $28 renov |
| **escuelalatribu.com**, latribuzapotal.com, secundarialatribu.com, latribu-zapotal.com | libres | ~$11 reg / $11 renov |
| escuelalatribu.org, latribuzapotal.org | libres | $8 reg / $12 renov |

Recomendación costo/beneficio: **escuelalatribu.com** (barato y estable) y, si quieren identidad MX, **escuelalatribu.mx**.

## Publicar

Cualquier hosting estático: Netlify (arrastrar `site/`), Cloudflare Pages, GitHub Pages o Vercel. Sin build.
