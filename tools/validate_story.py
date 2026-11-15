import json
import sys; d = json.load(open(sys.argv[1] if len(sys.argv)>1 else "levels/9-5-lupus/story.json", encoding="utf-8"))
TILES = set("hospital playa pantano bosque rio delta acantilado ruinas capsula valle arena".split())
MG = set("stones river memorama algoritmo indices".split())
WT = set("Innato Humoral Celular Complemento Inmunocomplejo Molecular".split())
err = []; frames = 0
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
    for c in z["cutscenes"]:
        chk(c["lines"], z["id"] + "." + c["trigger"])
        if c["trigger"].startswith("after_trainer:") and c["trigger"].split(":")[1] not in [t["id"] for t in z["trainers"]]:
            err.append((c["trigger"], "trigger"))
chk(d["boss"]["intro"], "boss"); chk(d["boss"]["outro"], "boss")
for p in d["boss"]["phases"]: chk(p["lines"], "boss." + p["name"])
for e in d["nefrodex"]:
    if len(e["text"].split()) > 60: err.append((e["title"], "palabras", len(e["text"].split())))
print("zonas", nz, [z["id"] for z in d["zones"]])
print("entrenadores", nt, "| residentes:", sum(1 for z in d["zones"] for t in z["trainers"] if not t["specialty"].startswith("Nefrotóxico")),
      "| nefrotóxicos:", sum(1 for z in d["zones"] for t in z["trainers"] if t["specialty"].startswith("Nefrotóxico")))
print("npc", nn, "| salvajes", nw, "| minijuegos", nm, "| cuadros", frames)
print("jefe fases", len(d["boss"]["phases"]), "| criaturas", len(d["creatures"]), "| escudos", len(d["shields"]), "| nefrodex", len(d["nefrodex"]), "| cast", len(d["cast"]))
print("max len", max(len(l[1]) for z in d["zones"] for n in z["npcs"] for l in n["lines"]))
print("ERRORES:", err if err else "ninguno")
