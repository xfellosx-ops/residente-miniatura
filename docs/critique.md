# Crítica de playtest: *El Residente Miniatura · 9-5 Lupus* (prototipo)

**Archivo evaluado:** `/home/claude/game/index.html` (269 líneas; bancos embebidos en L83–84, idénticos a `bankln.json` y `newq.json`, verificado byte a byte)
**Método:** lectura completa del código y juego automatizado con jsdom (`/tmp/jt/play.js`, `/tmp/jt/bugs.js`). Hice 3 modos de recorrido (5 ejecuciones) y 9 pruebas dirigidas a bugs.
**Jugador objetivo:** R4 de nefrología e internista. Examen del CMN el 16-ene-2027 (**faltan 63 días**). Tiene narcolepsia y lee lento.

---

## 1. Resumen ejecutivo

| Dimensión | Veredicto | Motivo principal |
|---|---|---|
| Enganche narrativo | **Bueno** | Los diálogos duran poco (10 palabras de media) y la metáfora fisiopatológica (piel → ganglio → sangre → glomérulo) funciona |
| Duración y volumen | **Insuficiente** | Un recorrido limpio dura unos 33 min, con **27 preguntas** de 41 únicas. El examen tiene 300 |
| Ritmo para narcolepsia | **Regular** | Hay 1 decisión cada ~50 s. Las explicaciones llegan a **254 palabras** (~76 s de lectura), más que la alarma por defecto (45 s) |
| Mecánica tipo Pokémon | **Débil** | No hay movimiento con flechas, el "pasto" es un botón, la criatura se elige 1 vez al final y una opción domina (×1.5 vs ×0.75) |
| Repetición espaciada | **Defectuosa** | Si fallas y aciertas de inmediato, el ítem **sube de caja** (fallo → acierto → intervalo de 3 días). Si repites el pasto el mismo día, un ítem llega a la caja de 35 días |
| Calidad médica | **Alta con errores puntuales** | Hay nomenclatura ISN/RPS 2018 contradictoria (IV-G (A) frente a P-11), hitos de respuesta atribuidos a KDIGO y faltan obinutuzumab y otros temas |
| Sesgo de longitud | **Grave** | En el **63 %** de las MCQ la correcta es la opción más larga (**12/13 = 92 %** en el banco de casos seriados). En V/F, el 71 % es "V" |
| Robustez técnica | **5 bugs P0/P1 reproducidos** | Temporizador fantasma, alarma silenciosa en el 1.er episodio, jefe que se reinicia a 100 HP, HP=0 persistente y poción infinita |

**Conclusión:** la base sirve (narrativa, retroalimentación por opción, alarma y PVT). Pero la versión 2 necesita tres cosas: **(1)** un *overworld* con flechas, pasto real y equipo de criaturas desde el minuto 1; **(2)** un motor de repaso corregido con reaparición dentro de la sesión; **(3)** reescribir las opciones para eliminar el sesgo de longitud y triplicar el banco por subnivel.

---

## 2. Métricas medidas

### 2.1 Por recorrido

| Métrica | Todo correcto | Muchos errores (semilla 11 / 3) | Pasto + repaso espaciado |
|---|---|---|---|
| Resultado | Victoria | Victoria (8 desmayos → centro de recuperación) | Victoria + 3 sesiones de repaso simuladas (+1, +3 y +8 días) |
| Preguntas respondidas | **27** | 102 / 99 | 66 (34 historia + 32 pasto) + 31 en repaso |
| Ítems únicos vistos | 27/41 (66 %) | 36/41 | 38/41 |
| Interacciones (clics) | 116 | 358 / 385 | 240 |
| Decisiones reales (pregunta, piedra, golpe, criatura) | 40, es decir 1 cada ~50 s | ~140 | ~85 |
| Máx. cuadros pasivos seguidos (diálogo, modal o hub sin decisión) | **5** | **7** (diálogo ×2, recuperación, diálogo ×3, hub) | 5 |
| Palabras por cuadro de diálogo (media / máx.) | 10.1 / 15 | 9.4 / 15 | 9.7 / 15 |
| Palabras por caso clínico mostrado (media / máx.) | 40.1 / 62 | 38.5 / 62 | 41.4 / 62 |
| Palabras por pantalla de pregunta (caso + enunciado + opciones) | 68.7 | 55.8 | 39.3 |
| Palabras por bloque de explicación (media) | **97.2** (máx. 254, LN-2) | 82.3 | 51.9 |
| Palabras leídas en total | 4 886 | 16 347 | 6 891 |
| **Tiempo estimado** (200 ppm + 20 s/pregunta) | **33 min** | **116 / 138 min** | **57 min** + ~10 min por sesión de repaso |
| Ítems fallados (eventos) | 0 | 21 (44) / 19 (46) | 11 |
| Reapariciones de falladas en la misma sesión | n/a | 50 / 46. Concentradas en bucles inmediatos: G-1 ×13 seguidas, S-1..3 ×4 | 10–22, casi todas en puertas y duelos. **Las falladas en pasto o río no vuelven ese día** (vencen a las 24 h) |
| Golpes al jefe | 6 (Treg) | 21 (neutrófilo, 31 preguntas del jefe) | 6 |
| Nivel final | 4 | 5 | 4 |

### 2.2 Repaso espaciado (modo pasto)

| Día simulado | Preguntas en repaso | Observación |
|---|---|---|
| 0 (mismo día) | 0 | "No hay preguntas pendientes hoy": el botón REPASO no hace nada tras la primera partida |
| +1 | 10 (tope fijo `slice(0,10)`) | Quedan 11 pendientes. El orden es el de inserción en `S.srs` (G-0 siempre primero), no el de mayor atraso ni el de falladas |
| +3 | 11 | Los errores en el repaso **quitan corazones** |
| +8 | 10 | 21 pendientes acumuladas |
| Distribución final de cajas | P-10 en caja 4 (35 días) **tras un solo día de juego** | El pasto se juega en bloque y promueve sin verificar si el ítem ya vencía |

### 2.3 Banco de preguntas

| Métrica | Valor |
|---|---|
| Ítems únicos | 41 (27 MCQ + 14 V/F) |
| Correcta = opción más larga | **17/27 (63 %)**. Banco seriado `bankln`: **12/13 (92 %)**. `newq`: 5/14 |
| Razón longitud de la correcta / media de distractores | Mediana ×1.44. En el banco seriado va de ×2.4 a **×8.9** (LNB-4) |
| Distribución de claves | C 8 · E 6 · A 6 · D 5 · **B 2** |
| V/F con clave "V" | 10/14 (71 %) |
| Ítems con peso ≥70 (muestran todas las explicaciones) | 15/25 |
| Ítems del jefe que nunca aparecen en un recorrido limpio | LNP-3 (belimumab con TFGe 42), LNP-4 y LNP-5: el jefe muere tras 6 golpes |

### 2.4 Contraste y tipografía

| Elemento | Contraste | Tamaño | Veredicto |
|---|---|---|---|
| Texto / panel | 6.0:1 | VT323 21 px (≈14 px reales) | OK |
| Corazones #a3201b / HUD #8bac0f | **2.9:1** | 8 px Press Start | **Falla WCAG AA** |
| D-pad #545169 / carcasa | 4.3:1 | 8 px | Falla en tamaño |
| Barra superior, HUD, etiqueta `.tag` | 6.0–6.1:1 | **7–8 px** | Ilegible en celular |
| Botones VOZ y AJUSTES | — | 8 px, alto ≈20 px | Objetivo táctil < 44 px |

---

## 3. Bugs (reproducidos en jsdom salvo los marcados *)

| # | Sev. | Línea / función | Bug | Reproducción y efecto | Arreglo |
|---|---|---|---|---|---|
| B1 | **P0** | L160 `ask()` timer; L146 `bB`; L256 `bCfg` | **Temporizador fantasma.** Si sales de una pregunta con tiempo (jefe) con B o AJUSTES, el `setInterval` sigue corriendo | A los 120 s llama `answer(null)`: `grade()` registra un fallo silencioso (`stats.n` 0→1) e **inyecta la explicación y el botón CONTINUAR dentro del MENÚ**. Al pulsarlo se reanuda la lógica del jefe y te quita corazones | Un `clearAll()` global con registro de timers. Cancelarlo en `menu()`, `scene()` y AJUSTES. Pausar el timer mientras la alarma está activa |
| B2 | **P0** | L96 `beep()`, L106 `fireAlert()` | **Alarma silenciosa en el primer episodio.** El `AudioContext` se crea dentro de la alarma, que corre en un timer y no en un gesto del usuario | En la prueba, el contexto lo creó la alarma (0 previos). Chrome y Safari lo dejan en estado `suspended` y nunca se llama `AC.resume()`. Quien se duerme en los primeros diálogos (sin sonido) **no oye la alarma**. `navigator.vibrate` no existe en iOS | Crear y `resume()` el contexto en el primer `pointerdown` (EMPEZAR). Mantener un oscilador mudo. Usar **Wake Lock API** (`navigator.wakeLock.request('screen')`) para que el celular no se bloquee antes de los 45 s |
| B3 | **P0** | L104–105 `poke()` | **Alarma de inactividad con falsos positivos.** Solo `pointerdown/keydown/touchstart` reinician el contador; leer o hacer scroll con rueda no | La explicación de LN-2 (254 palabras) toma ~76 s a 200 ppm y dispara la alarma de 45 s en plena lectura. A la vez, la alarma **no pausa** el timer del jefe | Umbral adaptativo: `max(S.idle, palabras_en_pantalla/3.3 s)` más un "toque de seguimiento" cada 25 s en textos largos (ver P0-3). Contar `scroll` y `wheel`. Pausar timers mientras `alertOn` |
| B4 | **P0** | L142 `grade()`; L202 bucle de puerta; L211 `seq()` | **SRS promueve ítems recién fallados.** Fallo → caja 0, vence en 1 día. El reintento inmediato (con la respuesta ya mostrada) sube a la **caja 1 y 3 días** | Verificado con G-1: tras fallo `{b:0, due:+1 d}`, tras reintento `{b:1, due:+3 d}`. Además, el pasto repetido el mismo día lleva P-10 a la caja 4 (35 días) | Promover solo si `r.due<=now` (ítem vencido). Un ítem fallado hoy queda "bloqueado en caja 0" hasta el día siguiente. Guardar `lastSeen` y no promover dos veces en el mismo día |
| B5 | **P1** | L238 derrota contra el jefe → `pickCreature()` → L230 `startBoss()` | El `BOSS.hp+20` es inútil: `startBoss` crea un jefe nuevo con **100 HP** y reinicia las preguntas | Jefe en 63 HP → muerte → 100 HP e índice 0. Un jugador con errores repite el jefe entero (31 preguntas en el recorrido con errores) | Conservar `BOSS` entre derrotas (`BOSS.hp=min(100,hp+20)`) y solo permitir cambiar de criatura |
| B6 | **P1** | L174 `hurt()` + L88 carga | **HP ≤ 0 se guarda.** Si recargas durante el centro de recuperación, juegas con 0 corazones | Tras recargar: `hp:0` y el HUD muestra "♡♡♡♡♡". El siguiente error manda directo a recuperación | Al cargar: `if(S.hp<=0)S.hp=5`. O guardar `S.inRecovery` y retomar la recuperación |
| B7 | **P1** | L165 `ask()`, rama MCQ | P-13 y P-14 (MCQ del pasto) usan `exp`, no `explicaciones` | La retroalimentación muestra solo "¡Correcto! " (vacía). El centro de recuperación muestra "— " sin texto | Normalizar el esquema al cargar: `q.explicaciones ??= {[q.clave]: q.exp}` |
| B8 | **P1** | L199 NPC C3 | **Poción infinita**: hablar con C3 cura +1 corazón sin límite | 10 conversaciones llevan de 1 a 5 ♥. Vuelve trivial el río | Flag `S.c3Used` o costo (responder una pregunta sobre C3) |
| B9 | **P1** | L252 `review()` → `seq(...,0,...)` | El repaso usa `seq`, que **quita corazones** con los errores y termina con "¡Ganaste! 0/2" | 2 errores en el repaso dejan 5 → 3 ♥. Así se castiga justo lo que hay que practicar | Un modo repaso sin daño. Al final, un resumen ("3 vuelven mañana") |
| B10 | P1 | L258–263 `pvt()` | El PVT deja `setTimeout` vivos al salir | Al pulsar B a mitad del PVT, éste vuelve a dibujar "CHEQUEO DE ALERTA" encima del menú | Mismo registro de timers que en B1 |
| B11 | P2 | L243 `victory()` | La evolución de la Treg es solo de texto y ocurre **después** del único combate. El multiplicador es el mismo (1.5) | Subir de nivel no tiene efecto mecánico | Evolución a mitad del nivel (al llegar al nivel 3), con un movimiento nuevo |
| B12 | P2 | L233 `bossTurn()` | Tras la 1.ª vuelta, `shuf(BOSS.qs)` desordena los casos seriados (LNP-5 puede salir antes que LNP-2) | Se rompe la narrativa del caso | Barajar series completas, no ítems sueltos |
| B13 | P2 | L254 menú | Dice "Alertas de esta sesión" pero `S.alerts` es acumulado de por vida | Dato engañoso para el autocontrol | `S.sessionAlerts`, que se reinicia al cargar |
| B14 | P2 | L264 título | Dice "7 escenas"; hay 11 en `SC` | Texto | — |
| B15 | P2 | L88 | `Object.assign({},DEF,s)` es superficial: si falta `stats`, se comparte la referencia a `DEF.stats`. No hay versión de esquema; si cambian los IDs, los ítems quedan huérfanos en `S.srs` y el contador de pendientes sigue sumándolos | — | `S.v=2` con migración; filtrar `S.srs` por `ALL` al cargar |
| B16 | P2 | L105 y ausencia de *handlers* | **No existe control por teclado** (solo `poke`). Los botones A y B no tienen tecla. B lleva al menú desde cualquier punto sin confirmar y se pierde el progreso de la escena | — | Mapear ←↑→↓, Z = A, X = B y Enter. Confirmar antes de salir de un combate |
| B17 | P2 | L7 | Fuentes de Google sin respaldo *offline*: sin red, cae a monospace y el diseño se descuadra* | — | Incrustar las fuentes en base64 o en un *service worker* |
| B18 | P2 | L22 `.panel` max-height 62vh | En un celular de 375 px, caso + 5 opciones largas + explicación de 254 palabras obligan a mucho scroll. `scrollIntoView` del botón CONTINUAR deja el inicio de la explicación fuera de vista* | — | La explicación en una hoja inferior paginada (ver P0-3) |

---

## 4. Problemas de diseño priorizados

### P0 (bloquean el objetivo de aprendizaje o el pedido explícito del jugador)

| # | Problema | Evidencia | Recomendación implementable |
|---|---|---|---|
| P0-1 | **No hay mundo recorrible.** El canvas es decorativo; el D-pad dice "TOCA LAS OPCIONES" | Pedido explícito: moverse con flechas | Overworld en *tiles* de 16 px en el canvas de 160×96 (cámara 10×6). Mapa por escena en un arreglo de cadenas (`#` muro, `"` pasto, `T` entrenador, `N` NPC, `D` puerta). Mover con `keydown` (flechas/WASD) y con el D-pad táctil en pantalla. Colisiones por *tile*. Los eventos se disparan al pisar o al mirar y pulsar A |
| P0-2 | **El pasto no es pasto.** Es un botón que da una pregunta V/F | Pedido explícito: pasto "como Pokémon" | *Tiles* de pasto con probabilidad de encuentro de **10–12 % por paso** (como en RSE), con al menos 3 pasos entre encuentros. Pantalla de combate contra un salvaje ("Macrófago corrompido", "pDC hiperactiva", "Complejo C1q-ADN"). Cada turno, tu criatura usa un "movimiento" que exige responder. El salvaje tiene 2–3 HP, así que son 2–3 preguntas por encuentro. Si fallas, te pega. El pool del pasto sale de la cola de vencidas, luego de las falladas hoy y luego de ítems nuevos |
| P0-3 | **Muros de texto tras cada respuesta.** Media de 97 palabras, máximo 254. Ningún cuadro exige respuesta | Narcolepsia: se duerme leyendo. Alarma a los 45 s | Retroalimentación **en capas, de ≤40 palabras por tarjeta**: (1) veredicto + 1 línea del porqué; (2) "¿Por qué no tu opción?"; (3) "Profundizar fisiopato" (opcional, ver P1-5). Cada 2 tarjetas, una **microrrecuperación** de 1 toque ("¿El AI suma semilunas fibrosas? Sí/No"). Ningún bloque supera los 25 s de lectura sin pedir un toque |
| P0-4 | **La criatura se elige solo al final y la elección es trivial** (×1.5 contra ×0.75, con el texto "¿Seguro?") | Pedido explícito | **Equipo desde la escena 1**: inicial a elegir (Treg, Macrófago M2, Linfocito B regulador). Captura de salvajes debilitados con una "jeringa" que exige acertar 2 seguidas. Una **tabla de tipos** clínica (ver §6). En cada turno eliges el movimiento: el movimiento correcto contra el tipo del enemigo da ×2 |
| P0-5 | **Los residentes de otras especialidades no son personajes.** Son solo una etiqueta de texto | Pedido explícito | *Sprites* de 12×18 px reutilizando `hero()` con paletas y accesorios: Patología (microscopio), MI (estetoscopio), Reumatología (gafas), Gineco-obstetricia (Doppler fetal), Hematología (frotis), Infectología (cubrebocas), Trasplante (hielera). Visión en línea recta al estilo Pokémon: "¡!" y el NPC camina hacia ti. Equipo de 2–3 "criaturas" del NPC = 2–3 mini-series de 2 preguntas |
| P0-6 | **Sesgo de longitud del 63 % (92 % en casos seriados)** | §2.3 | Reescribir las opciones del banco seriado: todas dentro de **±20 % de la longitud de la clave**. Sacar los matices ("considerar terapia triple…") a la explicación. Añadir una prueba automática en la *build*: `assert(max(len)/min(len) < 1.5)` y balancear claves A–E y V/F 50/50 |
| P0-7 | **El repaso espaciado no funciona en la sesión ni prioriza bien** | B4 y §2.2 | Dos colas: **intra-sesión** (cada fallo vuelve tras 3–5 ítems y otra vez tras ~10 minutos; reglas de "relearning" de Anki) e **inter-sesión** (Leitner 1-3-7-14-21 días con tope de 21 por los 63 días que faltan). Ordenar por atraso × peso. Inyectar las vencidas en el pasto y en los entrenadores, no solo en el menú |
| P0-8 | **Volumen insuficiente**: 27 preguntas y ~33 min en un recorrido limpio | Pedido explícito: niveles más largos | Meta por subnivel: **60–80 encuentros con pregunta, 45–60 min, 4–6 entrenadores, 2 minijuegos y 1 jefe**. Ver §5 para la cifra de ítems |

### P1

| # | Problema | Recomendación |
|---|---|---|
| P1-1 | El río no es un minijuego de esquivar: es un V/F con un bote que se desliza 0.5 s y un inmunocomplejo estático | Un *lane runner* real en el canvas (3 carriles con `requestAnimationFrame` a 60 fps). Los inmunocomplejos bajan por los carriles y se esquivan con ←→. Cada 8–10 s aparece una "compuerta" V/F que se responde **cambiando de carril** (izquierda = V, derecha = F). Así la interacción es continua, algo ideal para la narcolepsia |
| P1-2 | Las piedras no tienen consecuencia ni explicación: un error solo mueve la piedra | Un error te cuesta ½ ♥ y muestra en una línea por qué va antes ("Sin falla de depuración no hay antígeno expuesto"). Añadir **variantes**: cascada de la MAT/SAF, algoritmo KDIGO de inducción III/IV y algoritmo de embarazo |
| P1-3 | Olvida **nombres de ensayos y algoritmos**, y el juego solo los pone en las referencias | Minijuego **"Memorama de ensayos"**: emparejar ensayo, fármaco y resultado (BLISS-LN–belimumab, AURORA 1–voclosporina, REGENCY–obinutuzumab, Euro-Lupus–CFM a dosis bajas, ALMS–MMF frente a CFM, MAINTAIN). Cartas en el canvas, 6 pares, 60 s. Cada carta acertada entra a la cola SRS como ítem propio |
| P1-4 | Algoritmos: el jugador recuerda esquemas, no dosis | Minijuego **"Arma el algoritmo"**: arrastrar 5–7 bloques al orden y rama correctos (p. ej., clase III/IV → TFGe ≤45 → descartar ICN). Es más fiel a "esquemas" que a "dosis" |
| P1-5 | La fisiopatología gustó, pero le faltó profundidad | **Nefrodex por capas** desbloqueables: cada criatura o enemigo capturado abre una ficha con 3 niveles (mecanismo → molécula → implicación terapéutica). Ejemplo: pDC → TLR7/9 → IFN-α → firma de interferón → anifrolumab (TULIP) → por qué falla en NL. Cada nivel se abre al **responder** una pregunta, no al leer |
| P1-6 | El timer del jefe (120/100/80 s) es indulgente y no pausa con la alarma | Mantener tiempos generosos (sirven a quien lee lento), pero pausarlos con la alarma. Añadir un modo "Simulacro CMN" opcional con ~60 s por pregunta |
| P1-7 | El nivel y la XP no tienen efecto mecánico | El nivel desbloquea movimientos (nv 3: "Belimumab", que da ×2 contra tipo B-cel) y evoluciones a mitad del nivel |
| P1-8 | La voz lee solo el enunciado | TTS opcional del **caso + opciones** (narración lenta 0.95), con resaltado sincronizado. Para un lector lento con somnolencia, la vía auditiva ayuda a sostener la atención |
| P1-9 | La recuperación es lectura pasiva de 3 fallos | Que la recuperación sea **re-recuperación**: las 3 falladas vuelven como preguntas (con opciones reordenadas). Si aciertas, recuperas ♥ |

### P2

| # | Problema | Recomendación |
|---|---|---|
| P2-1 | Tipografía de 7–8 px y contraste de corazones 2.9:1 | Mínimo 10 px en Press Start (o 12 px VT323). Corazones en #5a0a08 sobre el HUD o con borde oscuro. Botones táctiles ≥44 px |
| P2-2 | B saca del combate sin aviso | B = cancelar/atrás dentro del contexto. Menú con START (Enter) y confirmación |
| P2-3 | El PVT tiene 5 ensayos y umbral de media >400 ms | Mejor el PVT-B de 3 min, o 10 ensayos. Reportar mediana y lapsos >500 ms. Ajustar unos ~60 ms por la latencia táctil del celular. Guardar la tendencia por día |
| P2-4 | Alerta parpadeante a 1 Hz | Está bajo el umbral de 3 Hz (bien), pero conviene la opción "solo vibración/sonido" |
| P2-5 | Guardado | Guardar a mitad de escena (posición en el mapa, HP del jefe, índice de la serie). Exportar e importar el progreso (JSON) |

---

## 5. Evaluación contra principios de aprendizaje y el perfil narcoléptico

| Principio | Estado actual | Nota (0–5) | Qué falta |
|---|---|---|---|
| Práctica de recuperación | Casi todo es pregunta. La recuperación y el Nefrodex son lectura pasiva | 3.5 | Recuperación activa en recuperación y Nefrodex. Preguntas de 2 niveles ("¿qué?" → "¿por qué?") |
| Repetición espaciada | Leitner 1-3-7-16-35. Bugs B4/B9, tope de 10, sin cola intra-sesión | 1.5 | Ver P0-7. Con 63 días al examen, tope de 21 días y "modo repaso final" en la última semana |
| Intercalado | Todo el nivel es LN y está ordenado por escena | 2 | 30 % de los encuentros en el pasto con ítems de subniveles previos (GN, TRR, trasplante) cuando existan. Mezclar tipos (V/F, MCQ, orden, emparejar) |
| Retroalimentación | **Excelente en contenido** (explicación por opción, perla, referencia) | 4 | Excesiva en volumen. Dosificar en capas |
| Carga cognitiva | Diálogos cortos (bien). Casos previos colapsados (bien). Opciones de hasta 273 caracteres y 5 opciones largas (mal) | 2.5 | Opciones ≤15 palabras. El caso en 2–3 viñetas con valores en negritas |
| Dificultad deseable y examen | Casos seriados al estilo CMN y etiqueta "RECORDADA EXAMEN" (bien). El sesgo de longitud regala aciertos (mal) | 2.5 | Corregir el sesgo. El simulacro con tiempo como modo aparte |
| Motivación y enganche | Historia y jefe con fases funcionan | 3 | Colección (captura), progresión visible, recompensas variables (objetos raros en el pasto) |
| **Perfil narcoléptico** | Alarma + PVT + pausas activas (bien diseñado en concepto). Pero hay 1 decisión cada ~50 s, textos de hasta 76 s, la primera alarma puede sonar muda y no hay Wake Lock | 2.5 | **Regla dura: ≤20–25 s entre toques**, incluido el movimiento en el mapa, que es interacción continua de bajo costo cognitivo. Wake Lock. Alarma adaptativa. Sesiones de 15 min con pausa sugerida |

**Cifra de ítems:** a ~60–80 encuentros por subnivel y con reaparición SRS (unos 2.5 encuentros por ítem), cada subnivel necesita **≥25–30 ítems nuevos**, más los de repaso. El banco actual (41 ítems) cubre ~1.5 subniveles. Para el CMN, priorizar ítems "RECORDADA EXAMEN" y de alto peso.

---

## 6. Comparación con Pokémon Rubí/Zafiro/Esmeralda

| Elemento | RSE | Prototipo 9-5 | Propuesta v2 |
|---|---|---|---|
| Primer combate | ~3–5 min (Ruta 101, eliges inicial y peleas contra un Poochyena) | ~30 min (jefe). El primer "combate" es la apertura sin consecuencia | Inicial en la escena 1 y un salvaje en el primer pasto (≤3 min) |
| Densidad de input | Un toque cada 1–3 s (caminar) | Un toque cada ~17 s; una decisión cada ~50 s | Caminar en el mapa + una pregunta cada 30–60 s |
| Encuentros | 10–12 % por paso en hierba, 1–2 min por combate | Botón opcional, 1 pregunta | Hierba real, 2–3 preguntas por salvaje |
| Entrenadores | 3–6 por ruta, con línea de visión | 2 por nivel, solo como etiqueta | 4–6 residentes con *sprite*, línea de visión y equipo propio |
| Decisión estratégica | Movimiento y cambio de Pokémon en cada turno, tabla de tipos | 1 elección binaria con una opción dominante | Tabla de tipos clínica (ver abajo) en cada turno |
| Curación | Centro Pokémon gratis, sin castigo | Centro de recuperación con repaso pasivo (buena idea) | Mantener la idea, con re-recuperación activa |
| Colección | Pokédex, captura | Nefrodex al final, sin captura | Capturar enemigos para desbloquear fichas por capas |
| Duración entre gimnasios | ~1–1.5 h | 33 min por subnivel | 45–60 min por subnivel |

**Tabla de tipos clínica (ejemplo).** Tipos de enemigo: *Proliferativa*, *Membranosa*, *MAT/SAF*, *Infección*, *Cronicidad*.

| Movimiento | Efecto |
|---|---|
| MMF/CFM | ×2 contra Proliferativa |
| ICN | ×2 contra Membranosa; **×0 si TFGe ≤45** (el enemigo lo anuncia) |
| Anticoagulación | ×2 contra MAT/SAF |
| Antibiótico | ×2 contra Infección |
| Nefroprotección (SRAA, iSGLT2) | Único efectivo contra Cronicidad |
| Pulsos de esteroide | ×0.5 y "quema" 1 ♥ propio contra Cronicidad o Infección |

Esto convierte los algoritmos KDIGO en estrategia de combate, que es justo lo que el jugador olvida.

---

## 7. Evaluación médica de las preguntas

**Global:** el nivel es apropiado para un examen de subespecialidad. Las explicaciones por opción son precisas y bien referenciadas (KDIGO 2024 LN, ISN/RPS 2018, BLISS-LN, AURORA 1, Euro-Lupus y ACR 2020 de salud reproductiva). Encontré **2 problemas de exactitud relevantes**, varias inconsistencias internas y huecos de temario.

| Ítem | Hallazgo | Severidad | Corrección |
|---|---|---|---|
| **LN-2, LNB-2** (y distractor LNP-2 D) | Usan "Clase IV-G (A)" e "IV-G (A/C)". La revisión **ISN/RPS 2018 eliminó la subdivisión S/G y las designaciones A, A/C y C**, que sustituyó por los índices NIH modificados (AI 0–24, CI 0–12). Esto contradice P-11, que declara verdadera esa eliminación | **Alta** (trampa típica de examen) | Reportar "Clase IV, AI 14/24, CI 2/12". Conservar "IV-S" solo como distractor explícito |
| **LN-3, LNB-3** | Atribuyen a KDIGO los hitos "↓25 % a 3 m y ↓50 % a 6 m". Esos hitos vienen sobre todo de **EULAR 2019/2023**. KDIGO 2024 define la respuesta completa (<0.5 g/g con TFGe estable) y la parcial (↓≥50 % y <3 g/g), con un horizonte de 6–12 meses que puede extenderse | Media | Citar "EULAR 2023 / KDIGO 2024" y separar qué dice cada una (verificar contra el texto de KDIGO 2024 antes de publicar) |
| LN-4 | La opción A dice "AAS desde el primer trimestre" y la explicación "desde las 12 semanas" | Baja | "Desde la semana 12 (antes de la 16)" en ambos lados |
| LNB-1 → LNB-3 | Incoherencia en la serie: la proteinuria basal es 1.0 g/24 h en LNB-1 y "basal 1.6 g/g" en LNB-3. LNB-2 menciona una biopsia "a los 3 meses" sin aclarar que es una rebiopsia | Baja | Unificar las cifras y explicitar "rebiopsia por persistencia" |
| LNB-4 | La clave dice que el perfil aPL "confirma SAF". Hace falta persistencia a ≥12 semanas más un criterio clínico (criterios ACR/EULAR 2023) | Baja | "Orienta a SAF (confirmar a 12 sem)". Añadir el puntaje ACR/EULAR 2023 en la perla |
| LN-2 | Con Cr 1.6 mg/dL, mujer de 26 años, la TFGe por CKD-EPI 2021 es ≈45, en el **umbral** del ICN. La clave lo menciona "con TFG conservada" | Baja (y una oportunidad) | Dar la TFGe explícita y convertirlo en un ítem de decisión ICN frente a belimumab, como LNP-3 |
| S-3 | ">90 %" frente a la definición ISN/RPS "≥90 %" | Baja | "≥90 %" |
| G-2 | "Por eso el sitio del depósito define la clase" es una simplificación: la clase depende del sitio **y** de la extensión (≥50 % de glomérulos para IV) | Baja | Ajustar la frase |
| MNB-2 | "tubuloreticulares" | Ortografía | "tubulorreticulares" |
| P-4 | "Se correlacionan con la actividad renal": afirmación absoluta en un V/F | Baja | "Pueden correlacionarse…" o pasarlo a MCQ |
| **Redundancia** | La planeación del embarazo aparece 3 veces (LN-4, MNB-4, LNP-5). Los hitos de respuesta, 4 veces (LN-3, LNB-3, LNP-4, P-16) | Diseño | Sirve como repetición, pero mejor como **ítems SRS espaciados** que como ítems distintos en el mismo nivel. Liberar espacio para temas faltantes |

**Huecos de temario frente a KDIGO 2024 y la práctica actual (prioridad para el CMN 2027):**
1. **Obinutuzumab (REGENCY):** aprobado por la FDA en oct-2025 para NL activa. Es posterior a KDIGO 2024, pero es pregunta probable en enero de 2027.
2. Podocitopatía lúpica (tratamiento como ECM o GSFS).
3. NL refractaria y criterios de cambio de terapia.
4. Mantenimiento: MMF frente a AZA (MAINTAIN, ALMS).
5. Dosis máxima de HCQ (≤5 mg/kg/día) y tamizaje de retinopatía.
6. iSGLT2 como nefroprotección.
7. NL en diálisis y trasplante: momento del trasplante, recurrencia y SAF.
8. Clases I/II: cuándo tratar.
9. NIH frente a Euro-Lupus (nombres de esquemas y ensayos).
10. Anifrolumab y firma de IFN (conecta con la fisiopato que gustó).

**Sesgo de construcción:** además del sesgo de longitud, en el banco seriado la clave es la única opción "matizada" (con "considerar…", "con intervalo de seguridad…"). Todos los distractores son absolutos ("suspender todo", "monoterapia"). Un examinado sin conocimiento acierta por forma. Hay que dar matices también a los distractores, que sean errores plausibles (p. ej., "GC + MMF + voclosporina" con TFGe 42, como ya hace bien LNP-3).

---

## 8. Los 10 cambios de mayor impacto para la versión 2

| # | Cambio | Impacto | Esfuerzo |
|---|---|---|---|
| 1 | **Overworld con flechas y D-pad táctil**: mapa de *tiles* por escena con colisiones; puertas, NPC y entrenadores como objetos del mapa | Pedido central + interacción continua (narcolepsia) | Alto |
| 2 | **Pasto real** con 10–12 % de encuentro por paso y salvajes de 2–3 preguntas, alimentado por la cola SRS (vencidas → falladas hoy → nuevas) | Repetición sin fricción, el núcleo del bucle | Medio |
| 3 | **Equipo de criaturas desde la escena 1 + captura + tabla de tipos clínica** (movimientos = fármacos y mecanismos) | Convierte algoritmos y esquemas en estrategia: ataca lo que olvida | Alto |
| 4 | **Residentes de otras especialidades como *sprites*** con línea de visión y mini-series (Patología, MI, Reuma, GyO, Hemato, Infecto, Trasplante) | Pedido explícito; da ritmo de ruta Pokémon | Medio |
| 5 | **Motor SRS corregido**: sin promoción si el ítem no vencía, cola intra-sesión (reaparece tras 3–5 ítems), tope de 21 días, orden por atraso × peso, repaso sin daño (arregla B4 y B9) | Hace real la repetición que al jugador le funciona | Bajo |
| 6 | **Retroalimentación en capas ≤40 palabras con microrrecuperación cada 2 tarjetas** y Nefrodex profundo desbloqueable por respuesta | Más profundidad fisiopatológica sin muros de texto | Medio |
| 7 | **Reescritura antisesgo del banco** (±20 % de longitud, distractores matizados, claves y V/F balanceados, *lint* automático) + corregir la nomenclatura ISN/RPS 2018 y la atribución KDIGO/EULAR | Validez de la evaluación | Medio |
| 8 | **Alarma robusta**: `AudioContext.resume()` en el primer gesto, Wake Lock, umbral adaptativo a las palabras en pantalla, pausa de timers durante la alerta, alertas por sesión (B2, B3, B13) | Seguridad funcional para la narcolepsia | Bajo |
| 9 | **Minijuegos animados**: río en *lane runner* a 60 fps con compuertas V/F por carril, "Arma el algoritmo" y "Memorama de ensayos" (nombres de ensayos y algoritmos) | Pedido explícito + memoria de nombres | Medio |
| 10 | **Niveles de 45–60 min** (60–80 encuentros, ≥25–30 ítems nuevos por subnivel, temario faltante con REGENCY y podocitopatía) + **limpieza técnica** (registro global de timers, HP ≥1 al cargar, jefe persistente, poción limitada, controles por teclado, fuentes ≥10 px) | Volumen pedido y estabilidad | Medio |

---

### Anexo: reproducibilidad
- `node /tmp/jt/play.js correct|errors|pasto [semilla]`: métricas de §2.
- `node /tmp/jt/bugs.js`: reproduce B1–B10 (acelera los timers ×100 para la alarma, el timer del jefe y el PVT).
- Supuestos: lectura de 200 ppm sobre todo el texto mostrado (caso, enunciado, opciones, explicaciones, diálogos y modales) + 20 s por pregunta. El autómata pulsa el *timing* de inmediato (golpe ×0.8). En modo errores elige el neutrófilo, y en los demás, la Treg.
- Fuente sobre obinutuzumab: comunicado de Genentech sobre la aprobación de la FDA (BusinessWire, oct-2025).
