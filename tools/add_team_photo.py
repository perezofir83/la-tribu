#!/usr/bin/env python3
"""Prepara una foto del equipo en formato "pasaporte" (cuadrada, 600px) y la guarda
donde el sitio la recoge automáticamente.

Uso:
  python3 tools/add_team_photo.py <imagen> <slug> [cx cy lado] [--luz 1.0]

  slug   = nombre en minúsculas con guiones, igual que data-photo en la página
           (p. ej. nelly-bordelais, ofir-perez-weinberg)
  cx cy  = centro de la cara en píxeles de la imagen original (opcional)
  lado   = tamaño del recorte cuadrado en píxeles (opcional)
  --luz  = >1 aclara sombras (para fotos a contraluz), 1.0 = sin cambio

Sin cx/cy/lado recorta un cuadrado centrado, un poco hacia arriba.
Después: python3 build.py  (la foto sustituye a las iniciales).
"""
import sys, pathlib
from PIL import Image, ImageOps, ImageEnhance

args = [a for a in sys.argv[1:] if not a.startswith("--")]
luz = 1.0
if "--luz" in sys.argv:
    luz = float(sys.argv[sys.argv.index("--luz") + 1]); args = [a for a in args if a != str(luz)]
src, slug = args[0], args[1]
im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
W, H = im.size
if len(args) >= 5:
    cx, cy, side = map(int, args[2:5])
else:
    side = min(W, H); cx, cy = W // 2, int(H * 0.45)
half = side // 2
box = (max(0, cx - half), max(0, cy - half), min(W, cx + half), min(H, cy + half))
im = im.crop(box)
im = ImageOps.fit(im, (600, 600), Image.LANCZOS)
if luz != 1.0:
    # aclara sombras con una curva gamma, conservando las luces
    g = 1.0 / luz
    im = im.point(lambda v: int(255 * ((v / 255) ** g)))
    im = ImageEnhance.Contrast(im).enhance(1.05)
out = pathlib.Path(__file__).resolve().parent.parent / "site" / "assets" / "team" / f"{slug}.jpg"
out.parent.mkdir(parents=True, exist_ok=True)
im.save(out, quality=86, optimize=True, progressive=True)
print("guardada:", out, out.stat().st_size // 1024, "KB")
