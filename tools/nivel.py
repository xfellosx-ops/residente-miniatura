"""Generador de niveles compactos: de una especificación corta (levels/_specs/*.py) produce
levels/<dir>/story.json, q_extra.json y q_banco.json. Las preguntas de opción múltiple salen del
banco de Alfredo (data/bank.json): las recordadas de examen van al jefe y a los entrenadores (regla 6).
Uso: python3 tools/nivel.py            (regenera todos los niveles con spec)"""
import json, pathlib, importlib.util, sys
ROOT = pathlib.Path(__file__).parent.parent
BANK = json.loads((ROOT / "data/bank.json").read_text(encoding="utf-8"))
PAL = {"hospital": ["#E0F8F0", "#88C8B0", "#3A7868", "#102820"], "playa": ["#FFF4D6", "#F2C27A", "#B5651D", "#4A2508"],
       "pantano": ["#E8D8F0", "#A080C0", "#583878", "#201030"], "bosque": ["#E0F8D0", "#88C070", "#346856", "#081820"],
       "rio": ["#F8D8D8", "#E07070", "#982828", "#380808"], "delta": ["#FCE4EC", "#F48FB1", "#AD1457", "#3A0418"],
       "acantilado": ["#E8F4FC", "#90C8E8", "#386890", "#0C2030"], "ruinas": ["#F8E0F0", "#D088C0", "#703878", "#200820"],
       "capsula": ["#FFF0E0", "#F0B080", "#A05830", "#301808"], "valle": ["#F4ECD0", "#C8B070", "#806828", "#282008"]}
VIG = {"hospital": "urgencias", "playa": "uv_piel", "pantano": "pantano_restos", "bosque": "ganglio", "rio": "rio_sangre",
       "delta": "delta_endocapilar", "acantilado": "acantilado_podocito", "ruinas": "ruinas_asas", "capsula": "capsula_semiluna", "valle": "valle_tubulovascular"}
CAST = {
 "player": ("Residente", "Protagonista miniaturizado", "#F8F8F8"), "dr_j": ("Dr. J.", "Mentor clínico por radio", "#3B6FB6"),
 "brenn": ("Sabio Brenn", "Mentor de fisiología profunda", "#7FB8E0"), "valeria": ("Dra. Valeria Montes 'Flashcard'", "Rival", "#E05A8A"),
 "urg": ("Dra. Carmen Triaje", "Residente de Urgencias", "#D9534F"), "pato": ("Dra. Iris Hematoxilina", "Residente de Patología", "#2B2B3A"),
 "neumo": ("Dr. Gonzalo Espiro", "Residente de Neumología", "#5BA4CF"), "mi": ("Dr. Ernesto Holístico", "Residente de Medicina Interna", "#E8E8E8"),
 "uti": ("Dr. Max Presor", "Residente de Terapia Intensiva", "#2A9D8F"), "gine": ("Dra. Lucía Bravo", "Residente de Ginecología", "#7B4FA0"),
 "cx": ("Dr. Rocco Filo", "Residente de Cirugía", "#4A7C59"), "uro": ("Dr. Bruno Salas", "Residente de Urología", "#2E8B57"),
 "cardio": ("Dra. Sístole Ruiz", "Residente de Cardiología", "#C0392B"), "endo": ("Dr. Tiro Glándula", "Residente de Endocrinología", "#D4A017"),
 "hema": ("Dra. Sara Esquistocito", "Residente de Hematología", "#8E2B55"), "infecto": ("Dr. Félix Cultivo", "Residente de Infectología", "#6B8E23"),
 "onco": ("Dra. Mitosis Lara", "Residente de Oncología", "#B565A7"), "radio": ("Dr. Hugo Contraste", "Residente de Radiología", "#607D8B"),
 "pedia": ("Dra. Pilar Percentil", "Residente de Pediatría", "#F39C12"), "geria": ("Dr. Anselmo Frágil", "Residente de Geriatría", "#95A5A6"),
 "nutri": ("Lic. Maíz Balance", "Nutrióloga renal", "#27AE60"), "gen": ("Dra. Alelo Vargas", "Residente de Genética", "#16A085"),
 "aine": ("AINE", "Nefrotóxico", "#E67E22"), "contraste": ("Contraste", "Nefrotóxico", "#34495E"),
 "genta": ("Aminoglucósido", "Nefrotóxico", "#9B59B6"), "tacro": ("Calcineurínico", "Nefrotóxico", "#8D6E63"),
 "hemo": ("Director de Hemo-Eterna", "Villano corporativo", "#1A1A2E"),
}
EXTRA_CAST = ["mi", "uti", "urg", "cardio", "endo", "infecto", "cx", "geria", "hema", "pato", "radio", "onco", "gine", "uro", "pedia", "neumo"]
def L(pairs): return [list(p) for p in pairs]
def rec(q): return any(str(o).endswith("26") for o in q.get("origen", []))

def build(S):
    out = ROOT / "levels" / S["dir"]; out.mkdir(parents=True, exist_ok=True)
    subs = set(S.get("subs", [])); temas = set(S.get("temas", []))
    bank = [q for q in BANK if q["sub"] in subs or q["tema_id"] in temas]
    series = {}
    for q in bank: series.setdefault(q["serie_id"], []).append(q)
    for s in series.values(): s.sort(key=lambda q: q["orden"])
    order = sorted(series, key=lambda s: (-sum(rec(q) for q in series[s]), -sum(q["peso"] for q in series[s]) / len(series[s])))
    # jefe: series con más recordadas hasta juntar >=5 preguntas (o lo que haya)
    boss_ids = []; rest = list(order)
    want = S.get("boss_n", 6)
    while rest and len(boss_ids) < want and (len(rest) > 1 or len(boss_ids) < 4):
        s = rest.pop(0); boss_ids += [q["id"] for q in series[s]]
    if len(boss_ids) < 4: sys.exit(f"{S['id']}: el jefe solo tiene {len(boss_ids)} preguntas")
    cast = {k: {"name": v[0], "role": v[1], "color": v[2]} for k, v in CAST.items()}
    for k, v in S.get("cast", {}).items(): cast[k] = {"name": v[0], "role": v[1], "color": v[2]}
    zones = []; ntr = 0
    for zi, Z in enumerate(S["zones"]):
        tiles = Z["tiles"]; trainers = []; cuts = []
        for T in Z.get("trainers", []):
            if not rest: break
            s = rest.pop(0); ntr += 1; tid = f"t{zi}_{len(trainers)}"
            trainers.append({"id": tid, "cast": T[0], "specialty": cast[T[0]]["role"].replace("Residente de ", ""), "serie": s,
                             "intro": L([(cast[T[0]]["name"].split(" '")[0], T[1])]), "defeat": L([(cast[T[0]]["name"].split(" '")[0], T[2])]), "questionTopics": [], "n": len(series[s])})
        if Z.get("enter"): cuts.append({"trigger": "enter", "lines": L([Z["enter"]])})
        if Z.get("exit"): cuts.append({"trigger": "exit", "lines": L(Z["exit"] if isinstance(Z["exit"], list) else [Z["exit"]])})
        mg = []
        for M in Z.get("minis", []):
            mg.append({"type": M[0], "title": M[1], "items": M[2] if M[0] in ("stones", "algoritmo") else [], "pairs": [list(x) for x in M[2]] if M[0] in ("memorama", "river") else []})
        zones.append({"id": f"z{zi+1}", "name": Z["name"], "palette": PAL[tiles], "tiles": tiles, "vignette": Z.get("vignette", VIG[tiles]),
                      "join": (["sonda"] if zi == 0 else []) + Z.get("join", []), "nurse": bool(Z.get("nurse")),
                      "intro": L(Z["intro"]),
                      "npcs": [{"id": f"npc{i+1}", "name": n[0], "lines": L([(n[0], x) for x in n[1]]), "gift": n[2] if len(n) > 2 else None, "recall": n[3] if len(n) > 3 else None} for i, n in enumerate(Z.get("npcs", []))],
                      "signs": [list(s) for s in Z.get("signs", [])], "trainers": trainers,
                      "wild": [{"name": w[0], "type": w[1], "topic": w[0]} for w in Z["wild"]],
                      "gates": [{"after": trainers[-1]["id"] if trainers else None, "topic": Z["gate"][0], "text": L(Z["gate"][1])}] if Z.get("gate") else [],
                      "minigames": mg, "cutscenes": cuts, "card": Z["card"]})
    # series sobrantes: entrenadores automáticos repartidos (máx. 3 por zona); lo demás alimenta las puertas
    k = 0
    while rest and any(len(z["trainers"]) < S.get("max_tr", 3) for z in zones):
        z = zones[k % len(zones)]; k += 1
        if len(z["trainers"]) >= S.get("max_tr", 3): continue
        s = rest.pop(0); ck = EXTRA_CAST[ntr % len(EXTRA_CAST)]; ntr += 1; nm = cast[ck]["name"]; sub = series[s][0]["subtema"]
        z["trainers"].append({"id": f"t{zones.index(z)}_{len(z['trainers'])}", "cast": ck, "specialty": cast[ck]["role"].replace("Residente de ", ""), "serie": s,
                              "intro": L([(nm, ("Te reto con un caso: " + sub)[:88])]), "defeat": L([(nm, "Bien razonado. Sigue tu camino.")]), "questionTopics": [], "n": len(series[s])})
    B = S["boss"]; nph = len(B["phases"]); per = [[] for _ in range(nph)]
    for i, qid in enumerate(boss_ids): per[min(nph - 1, i * nph // len(boss_ids))].append(qid)
    types = ["Molecular", "Celular", "Humoral", "Complemento"]
    story = {"meta": {"id": S["id"], "title": S["title"], "key": "rm_v3_" + S["id"].replace("-", ""), "arena": B.get("arena", "ARENA DEL JEFE"), "bossShort": B["short"], "bossChange": B.get("change", "cambia de forma")},
             "cast": cast, "zones": zones,
             "boss": {"name": B["name"], "color": B.get("color", "#c23a7a"), "dark": B.get("dark", "#6a1f5e"), "heads": B.get("heads", 1),
                      "intro": L(B["intro"]), "outro": L(B["outro"]),
                      "phases": [{"name": P[0], "type": types[i % 4], "lines": L([P[1]]), "topics": [P[0]], "questions": per[i]} for i, P in enumerate(B["phases"])]},
             "creatures": [], "typeChart": {}, "shields": [{"trial": s[0], "mnemonic": s[1], "result": s[2]} for s in S.get("shields", [])],
             "nefrodex": [{"title": n[0], "text": n[1]} for n in S.get("nefrodex", [])] or [{"title": z["name"], "text": z["card"]} for z in zones]}
    pasto = [{"id": f"P2-{i+1}", "vf": True, "enunciado": p[0], "clave": p[1], "exp": p[2], "tema": S["title"], "nivel": "moderada"} for i, p in enumerate(S["vf"])]
    def walk(o, where=""):
        if isinstance(o, list) and len(o) == 2 and all(isinstance(x, str) for x in o) and len(o[1]) > 90: print(f"   LARGO {S['id']} ({len(o[1])}): {o[1]}")
        elif isinstance(o, list): [walk(x) for x in o]
        elif isinstance(o, dict): [walk(v) for k, v in o.items() if k in ("zones", "intro", "npcs", "lines", "signs", "trainers", "defeat", "gates", "text", "cutscenes", "boss", "phases", "outro")]
    walk(story)
    dump = lambda o, f: (out / f).write_text(json.dumps(o, ensure_ascii=False, indent=1), encoding="utf-8")
    dump(story, "story.json"); dump({"pasto": pasto, "puertas": [], "entrenadores": [], "jefeC": []}, "q_extra.json"); dump(bank, "q_banco.json")
    print(f"{S['id']:>4} {S['title'][:34]:34} banco {len(bank):3} | jefe {len(boss_ids):2} | entrenadores {sum(len(z['trainers']) for z in zones):2} | a puertas {sum(len(series[s]) for s in rest):3} | V/F {len(pasto)}")

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for f in sorted((ROOT / "levels/_specs").glob("*.py")):
        sp = importlib.util.spec_from_file_location(f.stem, f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
        for S in m.LEVELS:
            if not only or S["id"] in only: build(S)
