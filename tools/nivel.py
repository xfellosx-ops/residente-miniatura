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
PAL.update({"tubulo": ["#FFF4C0", "#E8C84A", "#9A7A1A", "#3A2A08"], "proximal": ["#FBD8E2", "#E48AA8", "#A8436A", "#4A1A2A"], "henle": ["#E8F6FF", "#8AB8E0", "#2A5A8A", "#0F2A4A"],
            "colector": ["#D0F0FF", "#5AB4E8", "#1F6AA8", "#0A2A4A"], "intersticio": ["#F0E2C8", "#C8A87A", "#8A6A4A", "#3A2A1A"], "peritoneo": ["#FDE2D4", "#E8957A", "#A0503A", "#3A1A10"],
            "dializador": ["#F0FCFF", "#8AE0E8", "#2A8A9A", "#0A2A33"], "injerto": ["#E8F8F0", "#6AC0A0", "#1F6B4A", "#0E2A24"]})
# viñeta por CONTENIDO: cada zona del spec declara "vignette"; si falta, una viñeta de su región (nunca las de lupus fuera de la región 5)
REG = {lv[0]: r["id"] for r in json.loads((ROOT / "data/regiones.json").read_text(encoding="utf-8")) for lv in r["levels"]}
VIG_REG = {1: "nefrona", 2: "biopsia", 3: "nta", 4: "compartimentos", 5: "sindromes", 6: "erpad_rinon", 7: "hta", 8: "fibrosis", 9: "hemodialisis"}
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

# frases de los entrenadores automáticos: cada especialidad cree saber más nefrología que tú (y lo admite al perder)
RETO = {
 "mi": [("El riñón es un órgano más. Yo veo al paciente completo.", "Bueno… el riñón es EL órgano. Pasa."),
        ("Creatinina alta, pido interconsulta y me olvido.", "Debí razonarlo antes de llamarte."),
        ("Con un buen interrogatorio no necesito sedimento.", "Ese sedimento decía todo. Lo anoto.")],
 "uti": [("Mi protocolo: volumen, presor y que el riñón aguante.", "Balance positivo también mata. Lo anoto."),
         ("Si orina poco, más furosemida. Siempre funciona.", "La prueba de estrés no es tratamiento. Entendido."),
         ("Diálisis temprana a todos, por si acaso.", "STARRT y AKIKI… esperar también es decisión.")],
 "urg": [("Tres camas, un minuto. Yo resuelvo sin pensar.", "Pensar un minuto salvó la cama tres."),
         ("Potasio alto: insulina y a la casa.", "Sin calcio ni ECG no era seguro. Me ganaste."),
         ("Triaje rápido: todo riñón es prerrenal.", "No todo era volumen. Bien visto.")],
 "cardio": [("Primero el corazón. El riñón que espere.", "Cardiorrenal: van juntos. Aprendí."),
            ("Creatinina sube con IECA: lo suspendo.", "Subir 30 % es esperable. No lo quito."),
            ("Diurético a dosis bajas, para no lastimar.", "Congestión también daña al riñón. Pasa.")],
 "endo": [("Hormona que veo, hormona que repongo.", "Primero el riñón, luego el frasco. Sigue."),
          ("Glucosa bien, riñón bien. Simple.", "Albuminuria pese a la glucosa… tienes razón."),
          ("La aldosterona explica todo.", "No siempre era ella. Buen razonamiento.")],
 "infecto": [("Ningún cultivo me falta. Riñón, ¿qué es eso?", "Ajustar la dosis también cura. Lo anoto."),
             ("Antibiótico a dosis plena, sin importar la TFG.", "Dosis por función renal. Me cachaste."),
             ("Si hay fiebre, todo es infección.", "Era inmune, no bacteria. Bien.")],
 "cx": [("Si duele, se opera. Si no, también.", "No todo se resuelve con bisturí. Pasa."),
        ("El riñón se cuida solo después de cirugía.", "Hipotensión y AINE… sí lo cuido."),
        ("Contraste y quirófano el mismo día, sin problema.", "Planear ayuda al riñón. Tienes razón.")],
 "geria": [("A esta edad la creatinina miente. Mejor no medir.", "Cistatina C… debí pedirla."),
           ("En el anciano todo es por la edad.", "No todo es edad. Bien buscado."),
           ("Diálisis para todos, sin preguntar.", "Preguntar qué quiere el paciente. Sigue.")],
 "hema": [("Esquistocitos: ya sé, pura coagulopatía.", "MAT: el riñón sí importa. Pasa."),
          ("Las cadenas ligeras no son asunto renal.", "El riñón de mieloma… ahora lo veo."),
          ("Anemia en ERC: transfundo y listo.", "AEE y hierro primero. Lo anoto.")],
 "pato": [("Sin biopsia no hablo. Y casi nunca hablo.", "La clínica también diagnostica. Sigue."),
          ("La inmunofluorescencia es un adorno.", "El patrón de IF lo dijo todo. Bien."),
          ("Un glomérulo basta para opinar.", "Necesitaba más muestra. Tienes razón.")],
 "radio": [("Hugo Contraste. No, no soy pariente del villano.", "Bueno, primos lejanos. Sigue."),
           ("Todo se ve en la tomografía.", "El ultrasonido bastaba. Me ganaste."),
           ("Gadolinio sin pensar en la TFG.", "Fibrosis nefrogénica… cuidado. Pasa.")],
 "onco": [("Quimio primero; el riñón se acomoda.", "Ajustar dosis salva al paciente. Pasa."),
          ("Inmunoterapia sin efectos renales.", "Nefritis intersticial por ICI… sí existe."),
          ("Lisis tumoral: eso pasa solo en leucemias.", "Prevenirla en tumores sólidos también. Bien.")],
 "gine": [("En el embarazo todo es normal.", "La TFG sube; creatinina de 1 ya es alta."),
          ("Presión alta en el embarazo: esperar.", "Preeclampsia no espera. Sigue."),
          ("Proteinuria leve, nada importante.", "Medirla bien cambia todo. Pasa.")],
 "uro": [("Piedra que veo, piedra que rompo.", "Prevenirla con citrato y agua. Lo anoto."),
         ("Si hay sonda, no hay obstrucción.", "Hidronefrosis con sonda… me cachaste."),
         ("Hematuria siempre es urológica.", "Dismórfica: glomerular. Bien visto.")],
 "pedia": [("Los niños son adultos pequeños.", "Dosis y valores por edad. Pasa."),
           ("Nefrótico en niño: esteroide y adiós.", "Si recae, hay que pensar más. Bien."),
           ("Reflujo leve: cirugía ya.", "Observación primero. Tienes razón.")],
 "neumo": [("Respiro por ellos. El riñón, otro día.", "Ácido-base: pulmón y riñón juntos. Sigue."),
           ("Hemoptisis: puro pulmón.", "Pulmón-riñón: buscar ANCA y anti-MBG. Bien."),
           ("Hipercapnia crónica sin compensación renal.", "El riñón sí compensa. Me ganaste.")],
}
EXTRA_CAST = ["mi", "uti", "urg", "cardio", "endo", "infecto", "cx", "geria", "hema", "pato", "radio", "onco", "gine", "uro", "pedia", "neumo"]
def L(pairs): return [list(p) for p in pairs]
J1 = json.loads((ROOT / "data/juegos.json").read_text(encoding="utf-8"))
J2 = json.loads((ROOT / "data/juegos2.json").read_text(encoding="utf-8"))
def perlas(bank, n=8):
    """Perlas de mayor peso del banco del nivel, sin repetir, como páginas de la Nefrodex."""
    out, seen = [], set()
    for q in sorted(bank, key=lambda q: -q.get("peso", 0)):
        pl = (q.get("perla") or "").strip(); k = pl[:40]
        if not pl or k in seen: continue
        seen.add(k); words = pl.split()
        out.append({"title": "💎 " + (q.get("subtema") or q.get("tema") or "Perla")[:40], "text": " ".join(words[:60])})
        if len(out) >= n: break
    return out
def rec(q): return any(str(o).endswith("26") for o in q.get("origen", []))

def build(S):
    out = ROOT / "levels" / S["dir"]; out.mkdir(parents=True, exist_ok=True)
    subs = set(S.get("subs", [])); temas = set(S.get("temas", []))
    bank = [q for q in BANK if q["sub"] in subs or q["tema_id"] in temas]
    own = own_series(S)  # series propias del juego (casos nuevos), declaradas en la spec
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
            if len(T) > 3: s, n = own[T[3]][0]["serie_id"], len(own[T[3]])  # serie propia (4.º elemento)
            elif not rest: break
            else: s = rest.pop(0); n = len(series[s])
            ntr += 1; tid = f"t{zi}_{len(trainers)}"
            trainers.append({"id": tid, "cast": T[0], "specialty": cast[T[0]]["role"].replace("Residente de ", ""), "serie": s,
                             "intro": L([(cast[T[0]]["name"].split(" '")[0], T[1])]), "defeat": L([(cast[T[0]]["name"].split(" '")[0], T[2])]), "questionTopics": [], "n": n})
        if Z.get("enter"): cuts.append({"trigger": "enter", "lines": L([Z["enter"]])})
        if Z.get("exit"): cuts.append({"trigger": "exit", "lines": L(Z["exit"] if isinstance(Z["exit"], list) else [Z["exit"]])})
        mg = []
        for M in Z.get("minis", []):
            mg.append({"type": M[0], "title": M[1], "items": M[2] if M[0] in ("stones", "algoritmo") else [], "pairs": [list(x) for x in M[2]] if M[0] in ("memorama", "river") else []})
        zones.append({"id": f"z{zi+1}", "name": Z["name"], "palette": PAL[tiles], "tiles": tiles, "vignette": Z.get("vignette") or VIG_REG.get(REG.get(S["id"]), "nefrona"),
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
                              "intro": L([(nm, RETO[ck][(ntr // len(EXTRA_CAST)) % 3][0]), (nm, ("Mi caso: " + sub)[:88])]), "defeat": L([(nm, RETO[ck][(ntr // len(EXTRA_CAST)) % 3][1])]), "questionTopics": [], "n": len(series[s])})
    # minijuegos de la app NefroQuest (data/juegos.json y juegos2.json): clasificación, algoritmos y memorama del tema
    tids = set(S.get("temas", [])) | ({9} if S["id"] == "9-1" else set())
    extra = []
    for c in J2.get("clasif", []):
        if c["tid"] in tids: extra.append({"type": "clasif", "title": c["t"], "bins": c["bins"], "items": [list(x) for x in c["items"]], "pairs": []})
    for o in J2.get("orden", []):
        if o["tid"] in tids: extra.append({"type": "algoritmo", "title": o["t"], "items": o["s"], "pairs": []})
    for tid in sorted(tids):
        pr = J1.get(str(tid), {}).get("pares", [])
        if len(pr) >= 6: extra.append({"type": "memorama", "title": "Memorama del tema", "items": [], "pairs": [list(x) for x in pr]})
    for i, m in enumerate(extra):
        # si la especificación ya tiene un minijuego con ese título, gana la versión más nueva de la app
        same = [(z, k) for z in zones for k, x in enumerate(z["minigames"]) if x.get("title", "").strip().lower() == m["title"].strip().lower()]
        if same: z, k = same[0]; z["minigames"][k] = m; continue
        z = min(zones, key=lambda z: (len(z["minigames"]), zones.index(z)))
        z["minigames"].append(m)
    B = S["boss"]; nph = len(B["phases"]); per = [[] for _ in range(nph)]
    for i, qid in enumerate(boss_ids): per[min(nph - 1, i * nph // len(boss_ids))].append(qid)
    types = ["Molecular", "Celular", "Humoral", "Complemento"]
    story = {"meta": {"id": S["id"], "title": S["title"], "key": "rm_v3_" + S["id"].replace("-", ""), "arena": B.get("arena", "ARENA DEL JEFE"), "bossShort": B["short"], "bossChange": B.get("change", "cambia de forma")},
             "cast": cast, "zones": zones,
             "boss": {"name": B["name"], "color": B.get("color", "#c23a7a"), "dark": B.get("dark", "#6a1f5e"), "heads": B.get("heads", 1), "form": B.get("form", "defensor"), "crescent": bool(B.get("crescent")),
                      "intro": L(B["intro"]), "outro": L(B["outro"]),
                      "phases": [{"name": P[0], "type": types[i % 4], "lines": L([P[1]]), "topics": [P[0]], "questions": per[i]} for i, P in enumerate(B["phases"])]},
             "creatures": [], "typeChart": {}, "shields": [{"trial": s[0], "mnemonic": s[1], "result": s[2]} for s in S.get("shields", [])],
             "nefrodex": ([{"title": n[0], "text": n[1]} for n in S.get("nefrodex", [])] or [{"title": z["name"], "text": z["card"]} for z in zones]) + perlas(bank)}
    pasto = [{"id": f"P2-{i+1}", "vf": True, "enunciado": p[0], "clave": p[1], "exp": p[2], "tema": S["title"], "nivel": "moderada"} for i, p in enumerate(S["vf"])]
    def walk(o, where=""):
        if isinstance(o, list) and len(o) == 2 and all(isinstance(x, str) for x in o) and len(o[1]) > 90: print(f"   LARGO {S['id']} ({len(o[1])}): {o[1]}")
        elif isinstance(o, list): [walk(x) for x in o]
        elif isinstance(o, dict): [walk(v) for k, v in o.items() if k in ("zones", "intro", "npcs", "lines", "signs", "trainers", "defeat", "gates", "text", "cutscenes", "boss", "phases", "outro")]
    walk(story)
    dump = lambda o, f: (out / f).write_text(json.dumps(o, ensure_ascii=False, indent=1), encoding="utf-8")
    ent = [q for k in own for q in own[k]]
    # las series propias también van a q_banco.json para que entren a la Torre, la GUARDIA y el repaso global
    dump(story, "story.json"); dump({"pasto": pasto, "puertas": [], "entrenadores": ent, "jefeC": []}, "q_extra.json"); dump(bank + ent, "q_banco.json")
    nv = sum(p["clave"] == "V" for p in pasto)
    print(f"{S['id']:>4} {S['title'][:34]:34} banco {len(bank):3} | jefe {len(boss_ids):2} | entrenadores {sum(len(z['trainers']) for z in zones):2} | a puertas {sum(len(series[s]) for s in rest):3} | V/F {len(pasto)} ({nv} V) | propias {len(ent)}")
    if pasto and max(nv, len(pasto) - nv) / len(pasto) > 0.6: print(f"   AVISO {S['id']}: el pasto V/F tiene {100*nv//len(pasto)} % de V (máximo 60 % de una letra)")
    return pasto

def own_series(S):
    """Series propias del juego: S["series"] = {clave: {"subtema", "caso", "qs": [(continuacion, enunciado, {A..E}, clave, {A..E explicaciones}, perla, [refs])]}}.
    Se identifican T2-<nivel><clave>-<n>; el entrenador las usa con un 4.º elemento en su tupla."""
    tema_id = (S.get("temas") or [9])[0]
    tema = next((q["tema"] for q in BANK if q["tema_id"] == tema_id), S["title"])
    out = {}
    for key, D in S.get("series", {}).items():
        sid = f"T2-{S['id'].replace('-', '')}{key}"; out[key] = []
        for i, Q in enumerate(D["qs"]):
            cont, enun, ops, clave, exps, perla, refs = Q
            out[key].append({"id": f"{sid}-{i+1}", "serie_id": sid, "orden": i + 1, "sub": D.get("sub", str(tema_id)), "subtema": D["subtema"],
                             "caso": D["caso"] if i == 0 else "", "continuacion": cont if i else "", "enunciado": enun, "opciones": ops, "clave": clave,
                             "explicaciones": exps, "perla": perla, "referencias": refs, "peso": D.get("peso", 70), "tema_id": tema_id, "tema": tema,
                             "obj": D.get("obj", ""), "origen": ["El Residente Miniatura (nov 2026)"], "tipo_item": "juego", "dificultad": "moderada"})
    return out

if __name__ == "__main__":
    ALLVF = []
    only = set(sys.argv[1:])
    for f in sorted((ROOT / "levels/_specs").glob("*.py")):
        sp = importlib.util.spec_from_file_location(f.stem, f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
        for S in m.LEVELS:
            if not only or S["id"] in only: ALLVF.extend(build(S))
    if ALLVF:
        nv = sum(p["clave"] == "V" for p in ALLVF)
        print(f"pasto V/F global: {nv}/{len(ALLVF)} V ({100*nv/len(ALLVF):.1f} %; meta 45–55 %)")
