# Documento de diseño — El Residente Miniatura

Resumen de las decisiones tomadas con Alfredo (14 de noviembre de 2026). La biblia narrativa completa de los 26 niveles está en su artefacto de Claude "Biblia narrativa — El Residente Miniatura"; pídele que la exporte a `docs/` si hace falta el detalle.

## 1. Jugador
| Rasgo | Consecuencia de diseño |
|---|---|
| Narcolepsia; se duerme leyendo; lee lento | Interacción cada 30–60 s, texto en cuadros cortos, voz opcional, alarma por inactividad, botón 😴 DESPERTADOR, chequeo de alerta (tiempo de reacción) |
| Aprende por repetición | Repetición espaciada (cajas 1/3/7/14/21 días) + reaparición en la misma sesión 3–5 encuentros después del fallo |
| Fuerte en clínica y fisiopatología | Modo "detective" y "flashback": la historia sigue el mecanismo |
| Olvida nombres de moléculas, algoritmos y ensayos | Moléculas como personajes, "camino de piedras" para ordenar algoritmos, ensayos como "escudos" con mnemotecnia, memorama |
| Le gusta explorar con flechas | Mapa por casillas con curvas, letreros de histología, NPC, hierba |

Retroalimentación tras jugar la v3: lo mantiene despierto, la historia ayuda, la dificultad está bien. Pidió niveles largos, más preguntas y minijuegos.

## 2. Mundo e historia
- **Premisa:** el Dr. J. (homenaje a *Comprehensive Clinical Nephrology*; inventó la miniaturización tras perder a una paciente) envía al residente dentro de pacientes. El Sabio Brenn (homenaje a *Brenner & Rector*) explica la fisiología profunda. Mentores con nombre homenaje, no los autores reales.
- **Jerarquía:** la Gran Guía Global (KDIGO) dicta las leyes; el Consejo envía las misiones.
- **Antagonistas:** Los Nefrotóxicos (AINE, Contraste, Aminoglucósido, Calcineurínico; cómicos), financiados por la corporación Hemo-Eterna, cuyo director está poseído por **La Esclerosis** (jefe final).
- **Rival:** Valeria "Flashcard", memoriza sin entender; termina como aliada.
- **Entrenadores:** residentes de otras especialidades con casos clínicos.
- **Tono:** mixto (drama en fisiopatología, humor en rivales y villanos).
- **Cada nivel:** caso clínico de apertura → miniaturización → zonas por escala (molecular, ultraestructura, órgano) → entrenadores y puertas-llave → jefe por fases → tarjeta de dato y Nefrodex.
- **Final:** Torre del Consejo, 300 preguntas mezcladas con tiempo real; antes, "revancha de errores". Posjuego: arena de casos aleatorios.

## 3. Estructura: 26 niveles en 9 regiones
| Región | Temas (número del temario) | Acto |
|---|---|---|
| 1 · El riñón sano | 1, 2, 3 (+ desarrollo renal como flashback) | Prólogo |
| 2 · Las herramientas | 4, 5 | Prólogo |
| 3 · La lesión aguda | 6, 17, 11 | I |
| 4 · El medio interno | 24, 25, 10 | I |
| 5 · El glomérulo | 9 (7 subniveles; 9-5 y 9-6 largos, el resto compactos) | II |
| 6 · Genes, quistes y cristales | 16, 14, 12, 13 | II |
| 7 · Vasos, presión y embarazo | 15, 23, 18, 26 (cáncer y riñón) | II |
| 8 · La enfermedad crónica | 8, 7, 22 | III |
| 9 · Reemplazo e injerto | 19, 20, 21 | III |

**Orden de construcción (por peso del temario, campo `meta` de `data/temario.json`):** resto del 9 → 6 → 7 → 21 → 4 → 5 → 20, 24, 16, 19, 8, 25, 12, 23 → temas chicos en versión corta. Calendario acordado: construir hasta ~2 de enero; del 3 al 14 de enero solo Torre y repaso; el juego no debe quitar tiempo de estudio.

Temas con muchas entidades pequeñas (tóxicos, cristales): un súbdito por clase o mecanismo, no por entidad. Cada competencia oficial del Consejo debe mapearse a una puerta-llave o fase de jefe (`data/bank.json` trae el campo `obj`).

## 4. Mecánicas implementadas (motor v3)
| Sistema | Regla |
|---|---|
| Movimiento | Casillas de 16 px, 8 cuadros por paso; flechas, WASD o cruceta táctil; A/Z acción, B/X menú |
| Hierba | 13 % de encuentro por paso, mínimo 3 pasos tras un combate, forzado a los 14; preguntas del "pasto" (V/F y opción múltiple de 4) alimentadas por la cola de repaso |
| Combate | LUCHAR / EQUIPO / MOCHILA / HUIR. Elegir movimiento → pregunta → si acierta, animación del ataque por tipo y daño × tabla de tipos; si falla, contraataque |
| Equipo | Hasta 6; criaturas (células y fármacos) se unen por zona (`JOIN`); suben de nivel (curva 20·n^1.5), evolucionan; XP compartida al 50 % |
| Entrenadores | Línea de visión de 4 casillas, "!", caso seriado o preguntas por tema |
| Puertas-llave | Hay que acertar; si fallas llega otra pregunta del mismo concepto |
| Minijuegos | `stones`/`algoritmo` (ordenar), `memorama`, `river` (carriles animados; velocidad 0.45 px/cuadro), `indices` |
| Jefe | 4 fases por vida (75/50/25), temporizador 120→80 s, vida persistente; al perder recupera 15 |
| Derrota | Ganglio: repaso de 3 fallos y curación |
| Zonas | Viñeta animada del daño al entrar y salir; decoración histológica por `tiles`; letreros (`SIGNS`) |
| Vigilia | Alarma adaptada a las palabras en pantalla; ofrece DESPERTADOR (10 V/F con 6 s); Wake Lock |
| Sonido | Chiptune generado con Web Audio (sin archivos, sirve sin conexión): pistas `title`, `walk` (tonalidad y tempo por región), `wild`, `trainer`, `boss` (más rápida en fases 3–4), `victory`, `lose`, `map`, `torre`, `puzzle`. Efectos: `chal` (te retan), `door`/`locked`, `travel`, `roar` (jefe), `heal`, `faint`, `power(tipo)` (firma por tipo de movimiento o enemigo). Botón 🔊→🔉 (solo efectos)→🔇 guardado en `rm_snd`. La alarma de inactividad suena aunque esté en silencio |
| Repaso global | `rm_srs` (se sincroniza): todas las preguntas de todos los niveles; cajas 1-2-4-8-15-25 días con tope de 1/3 de lo que falta para el 16-ene-2027 (acierto con DUDÉ no sube); fallo baja 2 cajas (recordadas de examen a 0); no califica tiempo agotado, DESPERTADOR ni el minuto tras una alarma. REPASO: global, intercalado por tema, máx. 20; sin vencidas, errores de hoy |
| Guardia de hoy | 20 preguntas sin caminar: vencidas → recordadas no vistas → series nuevas de los temas con más `meta` × (1 − dominio). Pantalla HOY: días al examen, meta dinámica, ritmo necesario, pronóstico, racha, siesta sugerida, recordatorio de respaldo. Título: JUGAR/CONTINUAR, MAPA y TORRE bajo HOY; descripción del nivel plegada |
| Dominio / siesta / pausas | 📊 DOMINIO por tema y horas de somnolencia; 💤 SIESTA (repaso de errores de hoy, alarma en pausa 30 min, al despertar chequeo de alerta y las mismas preguntas); pausa de pie cada 20 min activos; chequeo de alerta de 10 estímulos, lapso >355 ms |
| Arco | `data/arco.json`: gancho "PRÓXIMO CASO" y diario de cierre por nivel; nefronas salvadas (1000 × % de aciertos del nivel) |
| Inicio | MENÚ → 🏠 INICIO vuelve al título sin cerrar; en combate o minijuego, MENÚ pregunta antes de salir |
| Apuesta de confianza | Tras responder, CONTINUAR se reemplaza por **✔ SEGURO / ? DUDÉ** (y **😴 SUEÑO** si falló): no añade toques. Acierto con duda no sube de caja (vuelve en ≤2 días); error con SEGURO = **error confiado** (`r.ec`, vuelve en la sesión y mañana); SUEÑO = no se califica. Calibración por tema en `G.cal` (acierto con seguro/dudé, Brier) |
| Reaprendizaje en sesión | `runList` (guardia, repaso, siesta, despertar, revisar falladas): el fallo vuelve 3–5 preguntas después sin calificar hasta acertarlo (máx. 3) |
| Alerta baja | `G.lowUntil` 20 min si el chequeo sale bajo (línea base: >1.15 × mediana de los últimos 20, o ≥2 lapsos; umbral fijo 380 ms/≥3 con <5 registros), dos alertas en 10 min o latencia de microsueño; 15 min al despertar. Mientras dure: no se califica, la guardia da solo vencidas, jefe y examen piden confirmación |
| Latencia | Respuesta >20 s y >2.5 × mediana por palabra de la sesión: no cuenta y suma una señal de sueño a `G.alh` |
| Meta dinámica | `ritmo()`: nuevas por día para ver todo el banco antes del 3-ene; meta del día = nuevas + vencidas (30–90), fija al empezar el día; la guardia garantiza esa cuota de nuevas (recordadas y alto peso primero). HOY muestra pronóstico del examen (Σ peso × exactitud, no vistas 0.35, ±1 EE, meta 70 %), siesta sugerida (media hora antes de las 2 horas con más alertas) y simulacro cada 3 días del 3 al 14 de enero |
| Dominio | Color por límite inferior de Wilson (n≥5, ⚪ con menos), barra de cobertura, exactitud a largo plazo (respuestas tras ≥4 días), dom = 0.6·exactitud + 0.4·caja; 8 temas y «ver todos»; calibración y ⚠ si con SEGURO aciertas <80 % |
| Guardia | Predicción antes (¿cuántas de 20?) y predicho vs real al final; cada pregunta es una cama, «pacientes estables», récord del día, frase de mentor, +10 nefronas por estable. 1 de cada 3 recordadas/alto peso sin serie: opciones ocultas («piensa y toca») |
| Combate | Salvajes de 2 golpes (100 PS); racha ×1.5 desde el 2.º acierto seguido; crítico ×1.5 con recordada de examen; «×2 SÚPER EFICAZ» visible al elegir ataque. Ficha de revivir 🎫 (meta del día, jefes de región) salva al equipo en el jefe |
| Progreso | Niveles en orden dentro de cada región (`G.skip` = saltado con prueba de entrada de 5 preguntas del tema, 4/5); el nivel empezado sigue abierto; GUARDIA, REPASO y Torre nunca se bloquean. Jefes de región opcionales (`G.rboss`) al superar la región: 15 preguntas recordadas de sus temas, recompensa nefronas, ficha y +1 nivel al equipo la primera vez. Nefronas por nivel = 1000 × aciertos/n. Rejuego (`S.replay`): puertas, entrenadores y jefe toman preguntas no vistas del subtema desde el banco completo. Caso del día (serie recordada por fecha, racha `G.cddR`). Logros de estudio (`G.logros`) en el título |
| Torre | Pisos en orden (≥70 % abre el siguiente); revancha y examen siempre abiertos. Al terminar: REVISAR FALLADAS, 🎯 por tema débil, desglose por competencia (`obj`, `data/competencias.json`). Victoria del examen: frase de Elisa y epílogo de 3 cuadros |

## 5. Esquema de un nivel
- `story.json`: `meta`, `cast`, `zones[]`, `boss`, `creatures`, `typeChart`, `shields`, `nefrodex` y, opcionales, `themes`, `enemyTypes`. Validado por `tools/validate_story.py`. Todo lo propio del nivel vive aquí; el motor no conoce ningún nivel.
  - `meta`: `id` ("9-6"), `title`, `key` (clave de guardado en `localStorage`, **única por nivel y no cambiarla una vez publicada**: borra el avance), `arena`, `bossShort`, `bossChange`.
  - `zones[i]`: `id,name,palette,tiles,intro,npcs,trainers,wild,gates,minigames,cutscenes,card` más
    `join` (ids de criaturas que se unen al entrar), `signs` (`[[título,texto],…]`, ≤90 caracteres), `nurse` (true = enfermera que cura),
    `vignette` (nombre de una viñeta de la biblioteca `VIG` del motor —las 10 de lupus y ~55 por contenido, lista en `docs/GRAFICOS.md`— o un objeto `{bg, layers[]}` con capas `rect, circ, ring, stripes, cells, drift, orbit, pulse, grow, person`; cada capa admite `every` para parpadear; ver ejemplos en `levels/9-6-anca/story.json`),
    `theme` (`{f,w,g}`: piso, muro y hierba; sobrescribe los colores del `tiles`).
  - `trainers[]`: `serie` (id de una serie de `q_extra.entrenadores`); si falta, se eligen `n` preguntas por `questionTopics`.
  - `boss`: `intro, phases[], outro` y `color, dark, heads, headColors, form, crescent` (sprite; `form` de `BOSS_FORMS`, `crescent` solo en GN con semilunas). Cada fase: `name, type` (tipo enemigo), `lines`, `topics` y sus preguntas: `questions` (ids), `series` (series completas) y/o `pick` (`{topics,n}` por tema). Si no trae ninguna, se eligen por `topics`.
  - `creatures[]`: además de `moves`, opcionales `color`, `dark` y, por movimiento, `fx` (animación de la biblioteca: `Fagocito, Depurador, Humoral, Regulador, Supresor, Antimetabolito, Endosomal, Podoprotector, Anti-citocina, Depletor, Alquilante, Glucocorticoide, Recambio, Anti-C5aR, Diurético, Nefroprotector, Sonda, Anti-complemento`).
- `tiles` disponibles (decoración del mapa): `hospital, playa, pantano, bosque, rio` (sangre)`, delta, acantilado, ruinas, capsula, valle, arena` y por estructura `tubulo, proximal, henle, colector, intersticio, peritoneo, dializador, injerto`.
- `q_base.json` (opcional, formato de 9-5): `apertura`, `gates{}`, `subditos[]`, `pasto[]`, `stones[]`, `jefeB[]`. Los niveles nuevos ponen todo en `q_extra.json`.
- `q_extra.json`: `pasto[]`, `puertas[]`, `entrenadores[]` (con `serie_id`, `orden`, `caso`, `continuacion`), `jefeC[]`.
- Niveles compactos: las series propias del juego (casos nuevos para temas con poco banco: 1, 3, 11, 9-3 y 9-7) viven en `levels/_specs/series_propias.py`; `nivel.py` las escribe en `q_extra.entrenadores` y en `q_banco.json` (para la Torre y el repaso). Un entrenador de la spec usa una serie propia o una del banco poniendo su clave como 4.º elemento de la tupla. Las series del banco que cruzan temas se traen completas.
- `q_banco.json` (opcional): preguntas del banco de Alfredo para ese tema (mismo formato que `data/bank.json`).
- Pregunta de opción múltiple: `id, enunciado, opciones{A..E}, clave, explicaciones{A..E}, perla, referencias[], peso, tema`. Pasto V/F: `id, vf:true, enunciado, clave:"V"|"F", exp`.

## 6. Pendientes de ingeniería (en orden)
1. ~~Sacar del motor lo específico de lupus~~ **Hecho (15 nov 2026).** `JOIN`, `SERIE_OF`, `PLAN.boss`, `SIGNS`, viñetas, colores por `tiles`, enfermera, `KEY` y textos del título y jefe salen de `story.json` (sección 5). La clave de lupus sigue siendo `rm_v2_95` para no perder la partida de Alfredo. Queda en el motor, como biblioteca reutilizable: los patrones de `deco` por `tiles`, las 10 viñetas de lupus (`VIG`) y las animaciones de ataque (`drawFx`).
2. ~~Selector de niveles / mapa de regiones~~ **Hecho (15 nov 2026).** `python3 build.py` arma el juego completo: mapa de 9 regiones (`data/regiones.json`), 32 niveles, equipo y niveles superados compartidos (`rm_global`), catálogo común de criaturas (`data/criaturas.json`) y la Torre del Consejo (antesala de revancha de errores, 6 pisos de 50 con explicación y modo examen de 300 con reloj; muestra ponderada por `meta` del temario, casos seriados completos). Jefes de región hechos (opcionales, con recompensa; nombres en `data/regiones.json`). Decisión: la Torre **no** se cierra con candado, porque Alfredo la necesita para estudiar.
3. ~~PWA instalable sin internet y pasar la partida entre dispositivos~~ **Hecho (15 nov 2026).** `python3 build.py --pwa` genera `docs/` (service worker `engine/sw.js`: responde de la caché y se actualiza en segundo plano). Botón 💾 PARTIDA: código de exportar/importar (gana lo más nuevo por nivel), descarga del juego en un archivo y, solo en el artefacto de Claude, sincronización automática por la base de datos privada del usuario (`data/users/<id>/`). La app de GitHub Pages no tiene nube: ahí el avance viaja con el código. Falta: sincronización real desde la PWA (necesita un backend).
4. Unificar los tres archivos de preguntas en uno por nivel. (El `data-id` ya está: el autómata identifica las preguntas por `id`, y el falso error de `T2-UCI-4` desapareció.)
5. Imágenes reales de biopsia en preguntas (solo propias o de licencia abierta, con crédito).
6. Ideas aprobadas sin implementar: recuerdo escrito con teclado, tipo de error en 4 categorías (hoy solo 😴 SUEÑO), arte y sonido mejores. (Apuesta de confianza, guardia, prueba de entrada: hechas.)

## 7. Pendientes de contenido
- **Niveles compactos (30 de 32):** 2–3 zonas cada uno, con historia, giro y jefe de la biblia narrativa, pasto V/F (10–12 por nivel; cada afirmación lleva su referencia como 4.º elemento de la tupla en la spec y campo `referencia` en `q_extra.json`) y preguntas de opción múltiple del banco. Alfredo pidió niveles largos: alargar primero los de más peso (6, 7, 21, 4, 5, 20, 24, 16, 19). Temas con poco banco (1, 3, 11, 9-3, 9-4) necesitan casos nuevos.
- **Reparto distinto a la biblia:** posinfecciosa, crioglobulinemia y GNMP/C3G están en 9-1 (no en 9-5); la MAT (9.d.8) está en el nivel 15; 9-7 quedó como paraproteínas y VIH.
- **Borradores KDIGO:** LRA/AKD 2026 y diabetes/ERC 2026 solo aparecen como tarjetas "Ley nueva / Ley anterior" en la Nefrodex de 6 y 8; la guía final no está confirmada (dossier de Drive, 12 nov 2026). Anemia KDIGO 2026: tarjeta en el nivel 7 sin cifras; añadirlas con la guía en mano.
- **Verificación del 15 nov 2026 (PubMed, resumen del artículo original):** coinciden con el juego FLOW (HR 0.76), CONVINCE (HR 0.77), MENTOR (60 % vs 20 % a 24 meses), PATHWAY-2, NefIgArd (16 mg × 9 meses), TESTING (HR 0.53; reducción de dosis por infecciones), DAPA-CKD (HR 0.61, con y sin diabetes), FIDELIO-DKD (HR 0.82), HALT-PKD (menor crecimiento del volumen renal), TEMPO 3:4, STARRT-AKI, AKIKI (49 % sin TRR), TREAT (más ictus) y ELITE-Symphony. Por búsqueda web (fuentes secundarias): meta de proteinuria de KDIGO 2025 en IgAN (<0.5, ideal <0.3 g/día) e ISPD 2022 (14 días coagulasa negativo, 21 días S. aureus, revisar retiro a los 5 días).
- **Pasto V/F (24 nov 2026):** 67 verdaderas se reescribieron como falsas plausibles (50 % V global, ningún nivel >60 %; `tools/nivel.py` y `validate_questions.py` avisan si una letra pasa del 60 %). **Verificado (25 nov 2026):** todo el pasto de los 32 niveles tiene referencia (guía KDIGO/ISPD/KDOQI/EAU vigente, ensayo o libro de la bibliografía del Consejo); no se hallaron errores; `nivel.py` avisa si una afirmación queda sin referencia. **Otros puntos sin verificar:** ISPD 2022 para enterococo y Pseudomonas (3 semanas); ASTRAL/CORAL, IDEAL, SPRINT, BENEFIT, HEMO; y los **límites de agua de la NOM-003-SSA3-2010**: el letrero del nivel 19 usa los de ISO/AAMI porque no se pudo abrir dof.gob.mx desde la sesión. Alfredo: confirma los de la NOM (Apéndice A), que son los que puede preguntar el Consejo.
- **Banco corregido integrado (15 nov 2026):** `data/bank.json`, `temario.json` y `competencias.json` vienen de la app de Alfredo. 9-6 usa sus 14 preguntas de ANCA/anti-MBG (`ANCA` y `GBM` en el jefe, `ANB` con Valeria en z2, `AGB` con Don Solvente en z4); `q_banco.json` de lupus se actualizó a la versión corregida con los mismos `id`. En ese subconjunto la correcta aún es la más larga en 4/14 (ANCA-3, GBM-1, GBM-3, ANB-3) y 5/13 de lupus; ANCA-1 y ANCA-4 tienen una opción fuera de ±25 %.
- **9-5 (regla 4):** `validate_story.py` avisa más de 4 cuadros seguidos al entrar en z1, z2, z6, z7 y z10, y en intro del jefe + fase 1. Recortar con Alfredo.
- Verificar en PubMed los PMID del guion de lupus (`levels/9-5-lupus/guion.md`, refs. 1–5, 18–23, 25) y los puntos marcados `[VERIFICAR]`.
- ~~Nomenclatura "IV-G (A)" en LN-2 y LNB-2~~ **Corregida en `data/correcciones.json` (24 nov 2026)**: clase IV (ISN/RPS 2018) con índices NIH modificados. Ronda 1 del 24 nov: AZ22-6, AZ8-9, AZ30-6, AZ8-1, AZ28-1, DIT-2, TUB-1, LN-2, LNB-2 y 84 perlas nuevas; avisar a Alfredo.
- Temas con pocas preguntas en el banco (1, 3, 10, 11): generar casos nuevos.
- Borradores KDIGO a incorporar: LRA/AKD 2026 (nivel 6) y diabetes y ERC 2026 (nivel 8).
- Bibliografía oficial del Consejo: Brenner 9.ª, Comprehensive 5.ª, Primer NKF, Daugirdas, Danovitch, Rose, Graff, UpToDate. Alfredo puede subir capítulos; los términos de Elsevier restringen su uso con IA, es decisión suya.

## 8. Documentos de apoyo
- `docs/research_pokemon.md`: mecánicas de Rubí/Zafiro/Esmeralda con cifras y adaptación.
- `docs/critique.md`: playtest crítico de la v1 (bugs ya corregidos en v2–v3; sirve como lista de control).
- `levels/9-5-lupus/guion.md`: guion largo con fisiopatología, giros y mnemotecnias.
