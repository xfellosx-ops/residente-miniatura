#!/usr/bin/env python3
"""Ensambla el juego a partir del motor y los datos de los niveles.
  python3 build.py levels/<nivel>   -> dist/<id>.html (un solo nivel; lo usa el autómata)
  python3 build.py                  -> dist/index.html con TODOS los niveles y el mapa de regiones
Archivos del nivel: story.json (obligatorio), q_base.json, q_extra.json, q_banco.json (opcionales)."""
import json, sys, pathlib, html
root = pathlib.Path(__file__).parent
t = (root / "engine/template.html").read_text(encoding="utf-8")
regions = json.loads((root / "data/regiones.json").read_text(encoding="utf-8"))
order = [lv[0] for r in regions for lv in r["levels"]]
TEMARIO = {str(x["id"]): x.get("meta", 10) for x in json.loads((root / "data/temario.json").read_text(encoding="utf-8"))}
# número de versión visible en la pantalla de inicio: cuenta de commits + fecha (sirve para saber qué copia tiene cada dispositivo)
import subprocess, datetime
try: BUILD = subprocess.run(["git", "rev-list", "--count", "HEAD"], cwd=root, capture_output=True, text=True).stdout.strip() or "0"
except Exception: BUILD = "0"
BUILD = str(int(BUILD) + 1) + " · " + datetime.date.today().strftime("%d/%m")
ROSTER = json.loads((root / "data/criaturas.json").read_text(encoding="utf-8"))

def load(lvl, name, default):
    f = lvl / name
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else default

def level(lvl):
    story = load(lvl, "story.json", None)
    if story is None: sys.exit(f"falta {lvl}/story.json")
    meta = story.get("meta") or {}
    if not meta.get("key") or not meta.get("id"): sys.exit(f"{lvl}: story.meta.id y story.meta.key son obligatorios")
    # catálogo común de criaturas: cualquier nivel puede unir una criatura del catálogo
    have = {c["id"] for c in story["creatures"]}
    story["creatures"] += [c for c in ROSTER["creatures"] if c["id"] not in have]
    story["typeChart"] = {**ROSTER["typeChart"], **story.get("typeChart", {})}
    return {"story": story, "q1": load(lvl, "q_base.json", {}), "q2": load(lvl, "q_extra.json", {}), "bank": load(lvl, "q_banco.json", [])}

dump = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
PWA_HEAD = '<link rel="manifest" href="manifest.webmanifest"><meta name="theme-color" content="#0f380f"><link rel="icon" href="icon-192.png"><link rel="apple-touch-icon" href="icon-192.png">'
def write(levels, title, names, pwa=False):
    out = t.replace("<!--PWA-->", PWA_HEAD if pwa else "").replace("__TITLE__", html.escape(title)).replace("__BUILD__", BUILD).replace("__LEVELS__", dump(levels)).replace("__REGIONS__", dump(regions)).replace("__TEMARIO__", dump(TEMARIO))
    (root / "dist").mkdir(exist_ok=True)
    if pwa: return pwa_site(out)
    for n in names: (root / "dist" / n).write_text(out, encoding="utf-8")
    print("dist/" + " y dist/".join(names), len(out), "bytes,", len(levels), "nivel(es)")

def png(size):
    """Icono de la app: residente pixelado sobre verde, sin dependencias."""
    import zlib, struct
    G, Lc, W, K, S, B = (15, 56, 15), (155, 188, 15), (248, 248, 248), (58, 42, 26), (242, 199, 155), (91, 143, 214)
    art = ["................", "................", ".....KKKKKK.....", ".....KKKKKK.....", ".....SSSSSS.....", ".....SkSSkS.....", ".....SSSSSS.....", ".....SSSSSS.....",
           "....WWWWWWWW....", "...SWWWBBWWWS...", "...SWWWBBWWWS...", "...SWWWBBWWWS...", "....WWWWWWWW....", "....WWWWWWWW....", ".....kk..kk.....", "................"]
    pal = {".": Lc, "K": K, "S": S, "W": W, "B": B, "k": (20, 20, 20)}
    m = size // 8; cell = (size - 2 * m) / 16; rows = b""
    for y in range(size):
        row = b"\x00"
        for x in range(size):
            if m <= x < size - m and m <= y < size - m: c = pal[art[min(15, int((y - m) / cell))][min(15, int((x - m) / cell))]]
            else: c = G
            row += bytes(c)
        rows += row
    ch = lambda k, d: struct.pack(">I", len(d)) + k + d + struct.pack(">I", zlib.crc32(k + d) & 0xffffffff)
    return b"\x89PNG\r\n\x1a\n" + ch(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)) + ch(b"IDAT", zlib.compress(rows, 9)) + ch(b"IEND", b"")

def pwa_site(out):
    """Sitio estático instalable en docs/ (GitHub Pages, rama + carpeta /docs): juego + manifest + service worker + iconos."""
    import hashlib
    site = root / "docs"
    (site / "index.html").write_text(out, encoding="utf-8")
    (site / ".nojekyll").write_text("")
    for s in (192, 512): (site / f"icon-{s}.png").write_bytes(png(s))
    (site / "manifest.webmanifest").write_text(json.dumps({"name": "El Residente Miniatura", "short_name": "Residente", "lang": "es-MX", "start_url": "./", "scope": "./", "display": "standalone", "orientation": "portrait",
        "background_color": "#2b2a33", "theme_color": "#0f380f", "icons": [{"src": f"icon-{s}.png", "sizes": f"{s}x{s}", "type": "image/png", "purpose": "any maskable"} for s in (192, 512)]}, ensure_ascii=False, indent=1), encoding="utf-8")
    ver = hashlib.sha1(out.encode()).hexdigest()[:10]
    (site / "sw.js").write_text((root / "engine/sw.js").read_text(encoding="utf-8").replace("__VER__", ver), encoding="utf-8")
    print("docs/ listo para GitHub Pages:", len(out), "bytes, versión", ver)

if "--pwa" in sys.argv:
    sys.argv.remove("--pwa"); PWA = True
else: PWA = False
if len(sys.argv) > 1:
    L = level(root / sys.argv[1]); m = L["story"]["meta"]
    write([L], f"{m['id']} {m.get('title','')}".strip(), [f"{m['id']}.html"])
else:
    Ls = [level(d) for d in sorted((root / "levels").iterdir()) if (d / "story.json").exists()]
    ids = [L["story"]["meta"]["id"] for L in Ls]
    for i in ids:
        if i not in order: sys.exit(f"nivel {i} no está en data/regiones.json")
    Ls.sort(key=lambda L: order.index(L["story"]["meta"]["id"]))
    write(Ls, "Juego completo", ["index.html"], pwa=PWA)
