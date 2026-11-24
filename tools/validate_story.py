import json
import sys; d = json.load(open(sys.argv[1] if len(sys.argv)>1 else "levels/9-5-lupus/story.json", encoding="utf-8"))
import re as _re, pathlib as _pl
_ENG = (_pl.Path(__file__).parent.parent / "engine/template.html").read_text(encoding="utf-8")
# viñetas, escenarios y formas de jefe: se leen del motor para no duplicar listas
TILES = set(_re.findall(r"^ (\w+):\{o:", _ENG, _re.M)) | {"arena"}
BOSS_FORMS = set(_re.search(r"const BOSS_FORMS=\[([^\]]*)\]", _ENG).group(1).replace('"', "").split(","))
MG = set("stones river memorama algoritmo indices clasif".split())
WT = set("Innato Humoral Celular Complemento Inmunocomplejo Molecular".split()) | set(d.get("enemyTypes") or {})
VIG = set(_re.findall(r"^VIG\.(\w+)=", _ENG, _re.M)) | set(_re.findall(r"VIG\.(\w+)=t=>", _ENG))
LAYERS = set("rect circ ring stripes cells drift orbit pulse grow person".split())
err = []; warn = []; frames = 0
meta = d.get("meta") or {}
for k in ("id", "title", "key"):
    if not meta.get(k): err.append(("meta", "falta " + k))
import pathlib
R = json.load(open(pathlib.Path(__file__).parent.parent / "data/criaturas.json", encoding="utf-8"))
crea = {c["id"] for c in d["creatures"]} | {c["id"] for c in R["creatures"]}
d.setdefault("typeChart", {}); d["typeChart"] = {**R["typeChart"], **d["typeChart"]}
for c in d["creatures"]:
    for m in c["moves"]:
        if m["type"] not in d["typeChart"]: err.append((c["id"], "tipo de movimiento sin typeChart", m["type"]))
def chk(lines, where):
    global frames
    for l in lines:
        frames += 1
        if not (isinstance(l, list) and len(l) == 2): err.append((where, "formato", l))
        elif len(l[1]) > 90: err.append((where, len(l[1]), l[1]))
nz = nt = nn = nw = nm = 0
for z in d["zones"]:
    nz += 1
    if z["tiles"] not in TILES: err.append((z["id"], "tiles"))
    if len(z["palette"]) != 4: err.append((z["id"], "palette"))
    chk(z["intro"], z["id"] + ".intro")
    for cid in z.get("join", []):
        if cid not in crea: err.append((z["id"], "join desconocido", cid))
    chk(z.get("signs", []), z["id"] + ".signs")
    v = z.get("vignette")
    if isinstance(v, str) and v not in VIG: err.append((z["id"], "viñeta desconocida", v))
    if isinstance(v, dict):
        for L in v.get("layers", []):
            if L.get("k") not in LAYERS: err.append((z["id"], "capa de viñeta", L.get("k")))
    enter = next((c for c in z["cutscenes"] if c["trigger"] == "enter"), None)
    if len(z["intro"]) + (len(enter["lines"]) if enter else 0) > 4: warn.append((z["id"], "más de 4 cuadros seguidos al entrar"))
    for n in z["npcs"]:
        nn += 1; chk(n["lines"], z["id"] + "." + n["id"])
        if n["gift"] not in ("pocion", "xp", None): err.append((n["id"], "gift"))
    for t in z["trainers"]:
        nt += 1; chk(t["intro"], t["id"]); chk(t["defeat"], t["id"])
        if t["cast"] not in d["cast"]: err.append((t["id"], "cast"))
    for w in z["wild"]:
        nw += 1
        if w["type"] not in WT: err.append((w["name"], "type"))
    for g in z["gates"]: chk(g["text"], z["id"] + ".gate")
    for m in z["minigames"]:
        nm += 1
        if m["type"] not in MG: err.append((m["title"], "mgtype"))
        if m["type"] in ("stones", "algoritmo") and not m["items"]: err.append((m["title"], "items"))
        if m["type"] == "memorama" and not m["pairs"]: err.append((m["title"], "pairs"))
        if m["type"] == "clasif" and not (m.get("bins") and all(len(x) == 2 and x[1] in m["bins"] for x in m["items"])): err.append((m["title"], "clasif"))
    for c in z["cutscenes"]:
        chk(c["lines"], z["id"] + "." + c["trigger"])
        if c["trigger"].startswith("after_trainer:") and c["trigger"].split(":")[1] not in [t["id"] for t in z["trainers"]]:
            err.append((c["trigger"], "trigger"))
if d["boss"].get("form") and d["boss"]["form"] not in BOSS_FORMS: err.append(("boss", "forma desconocida", d["boss"]["form"]))
chk(d["boss"]["intro"], "boss"); chk(d["boss"]["outro"], "boss")
if len(d["boss"]["intro"]) + 1 + len(d["boss"]["phases"][0]["lines"]) > 4: warn.append(("boss", "intro + fase 1 > 4 cuadros"))
for p in d["boss"]["phases"]:
    if not (p.get("questions") or p.get("series") or p.get("pick") or p.get("topics")): err.append(("boss." + p["name"], "sin preguntas"))
for p in d["boss"]["phases"]: chk(p["lines"], "boss." + p["name"])
for e in d["nefrodex"]:
    if len(e["text"].split()) > 60: err.append((e["title"], "palabras", len(e["text"].split())))
print("zonas", nz, [z["id"] for z in d["zones"]])
print("entrenadores", nt, "| residentes:", sum(1 for z in d["zones"] for t in z["trainers"] if not t["specialty"].startswith("Nefrotóxico")),
      "| nefrotóxicos:", sum(1 for z in d["zones"] for t in z["trainers"] if t["specialty"].startswith("Nefrotóxico")))
print("npc", nn, "| salvajes", nw, "| minijuegos", nm, "| cuadros", frames)
print("jefe fases", len(d["boss"]["phases"]), "| criaturas", len(d["creatures"]), "| escudos", len(d["shields"]), "| nefrodex", len(d["nefrodex"]), "| cast", len(d["cast"]))
print("max len", max(len(l[1]) for z in d["zones"] for n in z["npcs"] for l in n["lines"]))
print("AVISOS (regla 4):", warn if warn else "ninguno")
print("ERRORES:", err if err else "ninguno")
