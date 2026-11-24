import json, statistics, collections, sys
import sys; d=json.load(open(sys.argv[1] if len(sys.argv)>1 else 'levels/9-5-lupus/q_extra.json'))
ids=[]; mc=[]; vf=0; errs=[]
for k in ('pasto','puertas','entrenadores','jefeC'): d.setdefault(k,[])
for sec,qs in d.items():
    for q in qs:
        ids.append(q['id'])
        if q.get('vf'):
            vf+=1
            if q['clave'] not in ('V','F'): errs.append(f"{q['id']}: clave VF inválida")
            if not q.get('exp'): errs.append(f"{q['id']}: sin exp")
            continue
        o=q.get('opciones',{})
        if q['clave'] not in o: errs.append(f"{q['id']}: clave {q['clave']} no está en opciones")
        if sec in ('puertas','entrenadores','jefeC'):
            if len(o)!=5: errs.append(f"{q['id']}: {len(o)} opciones (esperadas 5)")
            for k in o:
                if not q.get('explicaciones',{}).get(k): errs.append(f"{q['id']}: falta explicación {k}")
            for f in ('perla','referencias','peso','tema' if sec=='puertas' else 'subtema'):
                if not q.get(f): errs.append(f"{q['id']}: falta {f}")
            if sec!='puertas' and not (60<=q['peso']<=85): errs.append(f"{q['id']}: peso {q['peso']} fuera de 60-85")
        else:
            if len(o)!=4: errs.append(f"{q['id']}: {len(o)} opciones (esperadas 4)")
        mc.append((sec,q))
dup=[i for i,c in collections.Counter(ids).items() if c>1]
if dup: errs.append(f"ids duplicados: {dup}")
for sec,qs in d.items():
    pre={'pasto':'P2-','puertas':'K2-','entrenadores':'T2-','jefeC':'B2-'}[sec]
    for q in qs:
        if not q['id'].startswith(pre): errs.append(f"{q['id']}: prefijo esperado {pre}")
# series
ser=collections.defaultdict(list)
for q in d['entrenadores']+d['jefeC']: ser[q['serie_id']].append(q['orden'])
for s,o in ser.items():
    if sorted(o)!=list(range(1,len(o)+1)): errs.append(f"serie {s}: orden {sorted(o)}")
    for q in d['entrenadores']+d['jefeC']:
        if q['serie_id']==s and ((q['orden']==1)!=bool(q['caso'])): errs.append(f"{q['id']}: caso/orden inconsistente")

print("=== VALIDACIÓN ESTRUCTURAL ===")
print("reactivos por sección:", {k:len(v) for k,v in d.items()}, "| total", sum(len(v) for v in d.values()))
print("verdadero/falso:", vf, "| opción múltiple:", len(mc))
print("errores:", errs if errs else "ninguno")

print("\n=== SESGO DE LONGITUD ===")
rows=[]
for sec,q in mc:
    L={k:len(v) for k,v in q['opciones'].items()}
    mx=max(L.values()); mean=statistics.mean(L.values()); sd=statistics.pstdev(L.values())
    cv=sd/mean
    maxdev=max(abs(v-mean)/mean for v in L.values())
    others=[v2 for k2,v2 in L.items() if k2!=q['clave']]
    rows.append((sec,q['id'],q['clave'],L[q['clave']]==mx,cv,maxdev,L[q['clave']]==min(L.values()),
                 (min(others)-L[q['clave']])/mean>0.05))
tot=len(rows); longest=sum(r[3] for r in rows)
if not tot:
    print("sin opción múltiple propia (solo V/F)"); c_=collections.Counter(q["clave"] for q in d["pasto"] if q.get("vf")); print("V/F:", dict(c_))
    if c_ and max(c_.values())/sum(c_.values())>0.6: print(f"AVISO: una letra del V/F supera el 60 % ({dict(c_)})")
    sys.exit(1 if errs else 0)
print(f"preguntas de opción múltiple: {tot}")
print(f"correcta = opción más larga: {longest}/{tot} = {100*longest/tot:.1f}%  (límite 25%)  -> {'PASA' if longest/tot<=0.25 else 'FALLA'}")
for s in ('pasto','puertas','entrenadores','jefeC'):
    sub=[r for r in rows if r[0]==s]
    if sub: print(f"   {s}: {sum(r[3] for r in sub)}/{len(sub)} ({100*sum(r[3] for r in sub)/len(sub):.0f}%)")
short=sum(r[6] for r in rows)
print(f"correcta = opción más corta (incluye empates): {short}/{tot} = {100*short/tot:.1f}%")
print(f"correcta más corta con margen >5% de la media: {sum(r[7] for r in rows)}/{tot} = {100*sum(r[7] for r in rows)/tot:.1f}%  (control de sobrecorrección)")
cvs=[r[4] for r in rows]
print(f"CV de longitudes por pregunta: media {100*statistics.mean(cvs):.1f}%, máx {100*max(cvs):.1f}%")
bad=[r for r in rows if r[5]>0.25]
print(f"preguntas con alguna opción fuera de ±25% de la media: {len(bad)} -> {'PASA' if not bad else 'FALLA'}")
for r in sorted(bad,key=lambda x:-x[5])[:12]: print(f"   {r[1]} desviación máx {100*r[5]:.0f}% (CV {100*r[4]:.0f}%)")

print("\n=== DISTRIBUCIÓN DE LETRA CORRECTA ===")
for s in ('pasto','puertas','entrenadores','jefeC','TOTAL'):
    sub=[r for r in rows if s=='TOTAL' or r[0]==s]
    c=collections.Counter(r[2] for r in sub)
    print(f"{s:14s}", {k:c.get(k,0) for k in 'ABCDE'}, f"n={len(sub)}")
c=collections.Counter(q['clave'] for sec,q in mc if q.get('vf') is None)
vfc=collections.Counter(q['clave'] for qs in d.values() for q in qs if q.get('vf'))
print("V/F:", dict(vfc))
if vfc and max(vfc.values())/sum(vfc.values())>0.6: print(f"AVISO: una letra del V/F supera el 60 % ({dict(vfc)})")
for s_ in ('puertas','entrenadores','jefeC'):
    c_=collections.Counter(q['clave'] for q in d[s_] if not q.get('vf'))
    if sum(c_.values())>=5 and max(c_.values())/sum(c_.values())>0.6: print(f"AVISO: en {s_} la letra {c_.most_common(1)[0][0]} supera el 60 %")
sys.exit(1 if (errs or bad or longest/tot>0.25) else 0)
