#!/usr/bin/env python3
"""Ensambla dist/index.html a partir del motor y los datos de un nivel.
Uso: python3 build.py [carpeta_del_nivel]   (por defecto levels/9-5-lupus)"""
import json, sys, pathlib
root = pathlib.Path(__file__).parent
lvl = root / (sys.argv[1] if len(sys.argv) > 1 else "levels/9-5-lupus")
t = (root / "engine/template.html").read_text(encoding="utf-8")
def load(name):
    return json.dumps(json.loads((lvl / name).read_text(encoding="utf-8")), ensure_ascii=False)
out = (t.replace("__STORY__", load("story.json")).replace("__Q1__", load("q_base.json"))
        .replace("__Q2__", load("q_extra.json")).replace("__BANK__", load("q_banco.json")))
(root / "dist").mkdir(exist_ok=True)
(root / "dist/index.html").write_text(out, encoding="utf-8")
print("dist/index.html", len(out), "bytes")
