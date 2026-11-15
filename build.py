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

def load(lvl, name, default):
    f = lvl / name
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else default

def level(lvl):
    story = load(lvl, "story.json", None)
    if story is None: sys.exit(f"falta {lvl}/story.json")
    meta = story.get("meta") or {}
    if not meta.get("key") or not meta.get("id"): sys.exit(f"{lvl}: story.meta.id y story.meta.key son obligatorios")
    return {"story": story, "q1": load(lvl, "q_base.json", {}), "q2": load(lvl, "q_extra.json", {}), "bank": load(lvl, "q_banco.json", [])}

dump = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
def write(levels, title, names):
    out = t.replace("__TITLE__", html.escape(title)).replace("__LEVELS__", dump(levels)).replace("__REGIONS__", dump(regions))
    (root / "dist").mkdir(exist_ok=True)
    for n in names: (root / "dist" / n).write_text(out, encoding="utf-8")
    print("dist/" + " y dist/".join(names), len(out), "bytes,", len(levels), "nivel(es)")

if len(sys.argv) > 1:
    L = level(root / sys.argv[1]); m = L["story"]["meta"]
    write([L], f"{m['id']} {m.get('title','')}".strip(), [f"{m['id']}.html"])
else:
    Ls = [level(d) for d in sorted((root / "levels").iterdir()) if (d / "story.json").exists()]
    ids = [L["story"]["meta"]["id"] for L in Ls]
    for i in ids:
        if i not in order: sys.exit(f"nivel {i} no está en data/regiones.json")
    Ls.sort(key=lambda L: order.index(L["story"]["meta"]["id"]))
    write(Ls, "Juego completo", ["index.html"])
