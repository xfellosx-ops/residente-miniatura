#!/usr/bin/env python3
"""Ensambla dist/index.html (y dist/<id>.html) a partir del motor y los datos de un nivel.
Uso: python3 build.py [carpeta_del_nivel]   (por defecto levels/9-5-lupus)
Archivos del nivel: story.json (obligatorio), q_base.json, q_extra.json, q_banco.json (opcionales)."""
import json, sys, pathlib, html
root = pathlib.Path(__file__).parent
lvl = root / (sys.argv[1] if len(sys.argv) > 1 else "levels/9-5-lupus")
t = (root / "engine/template.html").read_text(encoding="utf-8")
def load(name, default):
    f = lvl / name
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else default
story = load("story.json", None)
if story is None: sys.exit(f"falta {lvl}/story.json")
meta = story.get("meta") or {}
if not meta.get("key"): sys.exit("story.meta.key es obligatorio (clave de guardado única por nivel)")
dump = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
out = (t.replace("__TITLE__", html.escape(f"{meta.get('id','')} {meta.get('title','')}".strip()))
        .replace("__STORY__", dump(story)).replace("__Q1__", dump(load("q_base.json", {})))
        .replace("__Q2__", dump(load("q_extra.json", {}))).replace("__BANK__", dump(load("q_banco.json", []))))
(root / "dist").mkdir(exist_ok=True)
for name in ("index.html", f"{meta.get('id','nivel')}.html"):
    (root / "dist" / name).write_text(out, encoding="utf-8")
print(f"dist/index.html y dist/{meta.get('id','nivel')}.html", len(out), "bytes")
