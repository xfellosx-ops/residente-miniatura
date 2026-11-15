# Investigación de diseño: Pokémon Rubí/Zafiro/Esmeralda (Gen III) y su adaptación a un RPG de estudio para el CMN

> **Leyenda de trazabilidad**
> - **[S#]** = dato verificado en esta sesión en la fuente numerada (lista al final).
> - **[†]** = conocimiento general o del *decomp* (pokeemerald) que **no** se verificó en esta sesión. Es fiable, pero confírmalo antes de citarlo como dato duro.
> - **[Diseño]** = recomendación propia, no un dato de Pokémon.

---

## 0. Ficha técnica de referencia

| Parámetro | GBA (RSE) | GBC (estética objetivo) | Nuestro juego (160×96) |
|---|---|---|---|
| Resolución | 240×160 [†] | 160×144 [†] | 160×96 |
| Celda de mapa | metatile 16×16 (de 4 tiles de 8×8) [†] | 16×16 (2×2 tiles de 8×8) [†] | 16×16 recomendado |
| Celdas visibles | 15×10 [†] | 10×9 [†] | **10×6** (ver §8.1) |
| Frecuencia | ≈59.73 Hz [S1] | ≈59.7 Hz [†] | 60 fps (requestAnimationFrame) |
| Sprite del jugador en el mapa | 16×32 [†] | 16×16 [†] | 16×16 (o 16×24 si cabe) |
| Sprites de combate | 64×64 [†] | 56×56 [†] | 32×32 o 48×48 |
| Color | 15 bits, 16 paletas × 16 colores [†] | 4 tonos por paleta, 8 paletas BG + 8 OBJ [†] | 4 tonos por zona (ya tienes `PAL`) |

---

## 1. Exploración

### 1.1 Movimiento por cuadrícula (medido en el decomp de Esmeralda) [S1]

| Acción | Píxeles/cuadro | Cuadros por celda | ms por celda | Celdas/s |
|---|---|---|---|---|
| Caminar | 1 | 16 | ≈268 | 3.73 |
| Correr (Running Shoes, mantener B) / Surf | 2 | 8 | ≈134 | ≈7.5 |
| Mach Bike (velocidad máxima) | 4 | 4 | ≈67 | ≈15 |
| Acro Bike | patrón 2,3,3,2,3,3 | ≈6 | — | ≈9.95 |
| Girar sin avanzar (toque corto) | — | 8 cuadros | ≈134 | — |
| Chocar contra una pared | — | 32 cuadros | ≈536 | — |

- **Animación al caminar:** paso-pie-paso-pie, 8 cuadros por dibujo, 32 cuadros cada 2 celdas. Al correr, 16 cuadros cada 2 celdas con duraciones 5/3/5/3 [S1].
- **Running Shoes:** te las da tu madre en Villa Raíz después de recibir la Pokédex. Se corre manteniendo B, al doble de velocidad que caminando [S2].
- **Regla clave del motor:** el input se lee **solo cuando el jugador está alineado a la celda**. Mientras va de una celda a otra, el movimiento no se interrumpe. Un toque corto solo gira al personaje, y mantener la flecha lo hace avanzar [S1][†].
- **Cambiar de dirección no cuenta como paso** para el contador de pasos (Repel, encuentros) desde la Gen II [S3].

### 1.2 Cámara [S1]
- La cámara está fija sobre el jugador, sin retardo: el jugador queda inmóvil en pantalla y el mundo se desplaza el mismo número de píxeles en el mismo cuadro.
- En los bordes, el mapa **no** frena la cámara: se rellena con *border tiles* (árboles, agua).

### 1.3 Colisiones y tipos de celda [†]

| Tipo de celda | Comportamiento |
|---|---|
| Sólida (árbol, muro, mueble) | Bloquea, suena el "bump" y se reproducen los 32 cuadros de choque |
| Hierba alta | Transitable, hace una tirada de encuentro por paso, anima la hierba al pisarla |
| Saliente (*ledge*) | Solo se cruza en una dirección, con un salto de 2 celdas |
| Agua | Requiere Surf |
| Warp (puerta, escalera, alfombra) | Cambia de mapa |
| NPC u objeto | Bloquea como sólido; A interactúa |

### 1.4 Transiciones entre mapas
- **Conexión de rutas:** los mapas contiguos (Ruta ↔ Ciudad) se unen sin pantalla de carga; el mapa vecino se ve antes de cruzar [†].
- **Puerta en Esmeralda:** 4 dibujos de la puerta de 5 cuadros cada uno (≈335 ms), un paso forzado de 16 cuadros, cierre de 20 cuadros y un fundido de 9 niveles que termina en el cuadro 21. El mapa nuevo no carga antes del cuadro 79 (≈1.32 s) [S1].
- **Red:** fundido a negro de 32 cuadros (≈536 ms). **Crystal:** fundido a blanco de 8 cuadros de ida y 8 de vuelta [S1].
- Al entrar a una zona nueva aparece un cartel con su nombre durante ≈2 s [†].

### 1.5 Interacción [†]
- **NPCs:** el jugador mira al NPC y pulsa A. El NPC **se gira hacia el jugador** y abre una caja de diálogo. Algunos caminan al azar dentro de un radio pequeño.
- **Letreros:** se leen mirándolos y pulsando A. Dan el nombre de la ruta o un consejo.
- **Objetos en el suelo:** una Poké Ball visible. Con A aparece "¡X obtuvo POCIÓN!" con un *jingle*. También hay objetos ocultos que se encuentran con el Itemfinder.

---

## 2. Hierba alta y encuentros salvajes

### 2.1 Tasa de encuentro (Gen III)
El juego compara `rand mod 2880 < tasa` en cada paso [S4][S5].

| Zona | Tasa | Probabilidad por paso | Pasos medios entre encuentros |
|---|---|---|---|
| Hierba alta (estándar) | 320 | 11.1 % (≈1/9) | ≈9 pasos ≈ 2.4 s caminando |
| Ruta 119 (hierba) | 240 | 8.3 % | ≈12 |
| Zona Safari (hierba) | 400 | 13.9 % | ≈7 |
| Cuevas y arena profunda | 160 | 5.6 % | ≈18 |
| Agua | 64 | 2.2 % | ≈45 |

- **Modificadores:** bici ×0.8, Flauta Blanca ×1.5, Flauta Negra ×0.5, Amuleto ×0.66. Aun así la bici da más encuentros por segundo que correr, porque avanza más rápido [S4].
- Hay mitigaciones internas que reducen los encuentros consecutivos [†]; no se verificaron en esta sesión.

### 2.2 Tabla de encuentros: 12 *slots* en hierba [S6]

| Slot | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| % | 20 | 20 | 10 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 1 | 1 |

Hay 2 especies comunes (40 %), 4 medias (40 %), 4 poco comunes (18 %) y 2 raras (2 %). El nivel varía ±1–3 por *slot* [†].

### 2.3 Transición a combate [†]
1. La pantalla parpadea 2–3 veces y cambia la música al instante.
2. Viene un patrón de transición (espiral, persiana, fragmentos o barrido) de ≈1 s. Los entrenadores tienen patrones propios, y el Alto Mando y los líderes de Esmeralda tienen *mugshot*.
3. Las plataformas entran deslizándose, aparece el rival salvaje y sale el texto "¡Un X salvaje apareció!".

### 2.4 Ritmo (análisis de diseño) [S7]
- La hierba **le da el control al jugador**: decide cuándo arriesgarse, salir a "respirar" o volver, y eso baja la frustración frente al encuentro aleatorio puro.
- El riesgo es graduable: entrenar cerca del Centro es seguro, y adentrarse en zonas difíciles con pocas pociones es tenso.

### 2.5 Repelentes y huida
- **Repel:** 100 pasos, ₽350 [S3]. Super Repel 200 y Max Repel 250 pasos [†]. Bloquea a los salvajes de nivel inferior al del primer miembro del equipo [†].
- **Huida (Gen III):** si tu Velocidad ≥ la del rival, siempre escapas. Si no, depende de las Velocidades sin modificar y del número de intentos (cada intento sube la probabilidad), con una tirada de 0–255 [S8]. Fórmula exacta [†]: `F = (Vel_propia·128/Vel_rival + 30·intentos) mod 256`; escapas si `rand(0..255) < F`. Contra entrenadores no se puede huir.

---

## 3. Entrenadores, gimnasios y Liga

### 3.1 Entrenador de ruta [†][S9]
| Fase | Detalle |
|---|---|
| Visión | Línea recta en la dirección en que mira, de 1–5 celdas o más (configurable por NPC); bloqueada por obstáculos |
| Detección | "¡!" sobre la cabeza, 1 s de pausa, música de "mirada", el entrenador **camina hacia ti** |
| Diálogo previo | 1–2 cajas de presentación |
| Combate | Obligatorio; no se puede huir. "Cuando dos entrenadores se miran a los ojos, deben combatir" [S9] |
| Después | Frase de derrota, dinero y el NPC deja de combatir (en Esmeralda hay revanchas por Match Call [†]) |
| Recompensa | `₽ = pago_base × nivel del ÚLTIMO Pokémon`. Ejemplos de pago base: Youngster ₽16, Líder ₽100, Alto Mando ₽100, Campeón ₽200 [S10] |
| Derrota del jugador | En RSE pierdes **la mitad del dinero** y reapareces en el último Centro [S10] |

### 3.2 Gimnasios de Hoenn (Esmeralda) [S11]
| # | Ciudad | Líder | Tipo | Nivel del as | Puzle |
|---|---|---|---|---|---|
| 1 | Ciudad Férrica | Petra | Roca | 15 | Camino opcional para evitar entrenadores |
| 2 | Pueblo Azuliza | Marcial | Lucha | 19 | Oscuridad; se ilumina al vencer entrenadores |
| 3 | Ciudad Malvalona | Erico | Eléctrico | 24 | Interruptores que cambian muros eléctricos |
| 4 | Pueblo Lavacalda | Candela | Fuego | 29 | Dos niveles conectados por agujeros |
| 5 | Ciudad Petalia | Norman | Normal | 31 | Salas a elegir (cada sala es una "pregunta") |
| 6 | Ciudad Arborada | Alana | Volador | 33 | Puertas giratorias |
| 7 | Ciudad Algaria | Vito y Leti | Psíquico | 42 | Teletransportadores y combate doble |
| 8 | Arrecípolis | Plubio | Agua | 46 | Hielo: pisar cada celda una vez o reiniciar |

- **Estructura común:** guía en la entrada con consejo de tipo, 2–5 entrenadores del mismo tipo como "examen parcial", puzle del espacio, líder con 3–5 Pokémon, medalla + MT [†][S11].
- **Curva:** el nivel del as sube unos 3–5 niveles por gimnasio, y +9 entre el 6.º y el 7.º [S11].

### 3.3 Liga Pokémon [S12][S13]
- Se llega por la Calle Victoria, después de las 8 medallas. Son 4 miembros del Alto Mando en salas separadas (Sidney, Fátima, Nívea, Dracón) y luego el Campeón (Máximo en RS, Plubio en Esmeralda).
- Cada miembro del Alto Mando usa 2 Restaurar Todo y el Campeón 4 [S12]. El Alto Mando se diseñó deliberadamente "demasiado fuerte", y el equipo esperaba que el jugador llegara a nivel ≈50 [S13]. Los combates son seguidos, sin Centro entre salas [†].

---

## 4. Sistema de combate

### 4.1 Pantalla y menús [†]
```
┌──────────────────────────────┐
│ [RIVAL Nv12 ▓▓▓▓░░]   (spr)  │  rival: arriba-dcha; su caja de PS arriba-izq
│ (spr)    [TÚ Nv14 ▓▓▓▓▓▓]    │  jugador: abajo-izq (de espaldas); PS numéricos + barra EXP
│                     23/ 40   │
├──────────────────┬───────────┤
│ ¿Qué debería     │LUCHAR MOCH│  menú 2×2, cursor con flechas
│ hacer X?         │POKÉM. HUIR│
└──────────────────┴───────────┘
```
- **LUCHAR** abre 4 movimientos en 2×2. Al lado del cursor se ve el *PP actual/máx* y el **tipo** del movimiento.
- **Barra de PS:** verde >50 %, amarilla 20–50 %, roja <20 %, con pitido continuo de PS bajos. La barra se vacía de forma gradual (≈1 px por cuadro) [†].

### 4.2 Orden y resolución del turno [†][S5]
1. Ambos eligen. Cambiar de Pokémon, usar un objeto o huir va **antes** que cualquier movimiento.
2. Prioridad del movimiento (por ejemplo, Ataque Rápido +1). Luego la **Velocidad** decide, y un empate se sortea.
3. Precisión: impacta si `rand mod 100 < precisión%` [S5].
4. Daño: `((2·Nv/5+2)·Poder·Atq/Def)/50 + 2`, multiplicado por STAB, efectividad y un aleatorio de 0.85–1.00 [S14][†].
   - **STAB ×1.5** si el tipo del movimiento coincide con el del usuario [S14].
   - **Efectividad:** ×0, 0.25, 0.5, 1, 2 o 4 [S14].
   - **Crítico ×2**, con probabilidad 1/16 en el nivel 0 que sube a 1/8, 1/4, 1/3 y 1/2 por nivel [S15].
   - En Gen III, ser físico o especial depende del **tipo**, no del movimiento [†].
5. Mensajes en español: "¡Es muy eficaz!", "No es muy eficaz…", "No afecta a X…", "¡Un golpe crítico!" [†].

### 4.3 PP [†]
Cada movimiento tiene 5–40 PP. Con 0 PP en los 4 se usa Forcejeo. Se restauran en el Centro o con Éter/Elixir.

### 4.4 Estados alterados (Gen III) [†]
| Estado | Efecto | Duración |
|---|---|---|
| Sueño | No actúa | 2–5 turnos |
| Parálisis | 25 % de no actuar; Vel ×0.25 | Permanente |
| Veneno / Tóxico | −1/8 de PS por turno / −n/16 creciente | Permanente |
| Quemadura | −1/8 de PS por turno; Atq ×0.5 | Permanente |
| Congelación | No actúa; 20 % de descongelarse por turno | Variable |
| Confusión (volátil) | 50 % de golpearse a sí mismo | 2–5 turnos |

Los estados también facilitan la captura: sueño/congelación ×2, parálisis/veneno/quemadura ×1.5 [S16].

### 4.5 Experiencia y curvas
- **EXP ganada (Gen III):** `ΔE = (a · t · b · e · L) / (7 · s)` [†]. Las variables vienen de [S17]: a = 1.5 si es de entrenador, b = EXP base de la especie, L = nivel del vencido, s = participantes, e = 1.5 con Huevo Suerte, t = 1.5 si es intercambiado.

| Curva | EXP total a Nv100 [S17] | Fórmula [†] |
|---|---|---|
| Rápida | 800 000 | 4n³/5 |
| **Media-rápida** | 1 000 000 | **n³** [S17] |
| Media-lenta | 1 059 860 | 6n³/5 − 15n² + 100n − 140 |
| Lenta | 1 250 000 | 5n³/4 |
| Errática | 600 000 | n³ × factor que baja de 2 a 0.6 [S17] |
| Fluctuante | 1 640 000 | n³ × factor que sube de 0.48 a 1.64 [S17] |

Desde la Gen III las curvas se leen de una tabla precalculada, no se calculan [S17].

### 4.6 Subir de nivel, aprender movimientos, evolución [†]
- La barra azul de EXP se llena, suena el jingle de nivel y una ventana muestra +stats.
- **Movimiento nuevo con 4 ya aprendidos:** "¿Olvidar un movimiento?" → elegir → "1, 2 y… ¡Puf!".
- **Evolución por nivel:** ocurre **al terminar el combate**, con animación de destellos y silueta de ≈5–10 s. Se puede cancelar con B.

### 4.7 Captura (Gen III) [S16]
- `a = ((3·PSmáx − 2·PSact) / (3·PSmáx)) · tasa · bonus_ball · bonus_estado`
- `b = 1048560 / √√(16711680 / a)`. Se hacen 4 tiradas de 0–65535 contra b; cada una superada es una sacudida, y con las 4 se captura. La probabilidad es ≈ a/255; con a ≥ 255 la captura es segura.
- **Lección de diseño:** bajar los PS y aplicar un estado multiplica la captura, así que **la preparación premia**.

---

## 5. Equipo y economía

| Sistema | Detalle |
|---|---|
| Equipo | Máximo 6; el primero sale a combatir |
| Centro Pokémon | Curación total gratuita con jingle de ≈3 s; también es el punto de reaparición [†] |
| PC | 14 cajas de 30 en Gen III [†] |
| Pokédex | ≈200 especies en la Pokédex de Hoenn, ≈135 nuevas [S18] |
| Objetos [†] | Poción 20 PS (₽300), Superpoción 50 (₽700), Hiperpoción 200 (₽1200), Antídoto, Poké Ball (₽200) |
| Dinero | Lo dan los entrenadores (§3.1); en RSE se pierde la mitad al caer derrotado [S10] |

---

## 6. Bucle de progresión y enganche

### 6.1 Bucle principal [Diseño, basado en S7, S13]
```
Ciudad (curar, comprar) → Ruta (hierba + 3–8 entrenadores) → Ciudad nueva
      ↑                                                          ↓
  Recompensa (medalla, MT, nueva zona) ← Líder ← Gimnasio (puzle + entrenadores)
```
- **Micro (5–30 s):** paso → encuentro → combate corto → EXP.
- **Medio (5–15 min):** ruta completa con entrenadores fijos, cada uno con un pago claro [†].
- **Macro (1–2 h):** gimnasio → medalla → se abre una zona nueva o una MO (Corte, Surf) que habilita la exploración [†].

### 6.2 Motores de enganche
| Motor | Cómo funciona en RSE |
|---|---|
| Grinding opcional | La hierba junto al Centro es una zona segura para subir 2–3 niveles antes del líder [S7] |
| Rival (Bruno/Aura, Blasco) | Aparece en cada etapa como "medidor" de tu progreso [†] |
| Colección | Pokédex, especies raras al 1 % [S6] |
| Mundo no lineal | Hoenn invita a desvíos; Masuda lo compara con "soltar la mano del niño" [S13] |
| Picos de dificultad | El Alto Mando es deliberadamente fuerte [S13]; hay un salto de 9 niveles entre los gimnasios 6 y 7 [S11] |
| Recompensas escalonadas | Objetos en el suelo cada pocas celdas, MT del líder, nuevas MO |

---

## 7. UI y estética

| Elemento | RSE / GBC | Nota |
|---|---|---|
| Caja de diálogo | **2 líneas**, ancho de pantalla; flecha parpadeante ▼ al llenarse; A avanza o completa el texto [†] | — |
| Velocidad de texto | Lenta / Media / Rápida [S19]; en el decomp, 8/4/1 cuadros por carácter [†] | Usa 1–2 cuadros por carácter |
| Opciones | Estilo de combate Cambio/Fijo, escena de combate On/Off, modo de botones [S19] | "Escena Off" acelera; útil para repasar |
| Fuente | Proporcional, ≈6–8 px de ancho, líneas de 16 px en GBA; 8×8 monoespaciada en GBC [†] | A 160 px: fuente de 4×6 o 5×7 para ≈26–30 caracteres por línea |
| Sonidos | "Select" al pulsar A, "bump" al chocar, puerta, PC, jingle de curación, de objeto y de nivel, pitido de PS bajos [†] | Retroalimentación sonora en *cada* input |
| Paleta | GBC: 4 tonos por paleta; GBA: 16 colores por paleta [†] | Una paleta de 4 tonos por órgano o zona |

---

## 8. Adaptación a nuestro juego

### 8.1 Restricciones de pantalla (160×96)
- Con celdas de 16×16 se ven **10×6**. Coloca la cámara por píxel con el jugador en (72,40). Así quedan 4.5 celdas a cada lado y 2.5 arriba y abajo.
- La caja de diálogo debe medir **32 px** de alto (2 líneas de 8 px con margen). Deja 64 px de mundo visible durante el diálogo.
- **El caso clínico es largo** (el banco actual tiene casos de 300–500 caracteres). No lo metas en 2 líneas: usa **paginación en cajas de 2–3 líneas (≤60–80 caracteres por caja)** con A para avanzar. Cada pulsación es interacción, y eso es bueno para la narcolepsia. Pon en negrita o en otro color los datos clave (creatinina, C3/C4).
- **Opciones A–D:** usa una lista vertical con cursor ▶. **El panel superior muestra completa la opción resaltada** (hasta 3 líneas), y abajo solo van las etiquetas "A B C D" o abreviaturas de 12 caracteres. Las flechas recorren las opciones y A confirma, así que nunca hay que leer 4 opciones largas a la vez.

### 8.2 Mapa de mecánicas → estudio
| Pokémon | Nuestro juego | Implementación JS |
|---|---|---|
| Hierba alta | "Parénquima infiltrado" o "luz tubular": celdas con tirada de encuentro | `tile===GRASS && Math.random()<RATE` |
| Pokémon salvaje | **Célula o agente enemigo** (linfocito T, complejo inmune, cristal de oxalato), con 1–3 preguntas fáciles o moderadas | Saca de `BANK` por `subtema` y dificultad ≤2 |
| Tabla de 12 *slots* | Subtemas ponderados: 40 % ítems vencidos en el SRS, 40 % nuevos, 18 % de repaso, 2 % "rara" de alto rendimiento (perla de examen) | Ver `pickEncounter()` |
| Movimiento (4) | **Estrategia terapéutica o diagnóstica**: elegirla es una decisión clínica, y luego se responde la pregunta asociada | `move = {name, type, topic, power, pp}` |
| PP | Intentos por subtema y combate; se restauran en el Centro, lo que obliga a rotar temas | `move.pp--` al usarlo |
| Tipo del movimiento | **Mecanismo**: Inmunosupresor, Diurético, Depurativo (TRR), Electrolito, Antiproteinúrico, Antiinfeccioso | Tabla `EFF[moveType][enemyType]` |
| Efectividad ×2 / ×0.5 / ×0 | Usar el mecanismo correcto contra el enemigo (por ejemplo, Depurativo contra Toxina dializable) multiplica el daño. Es conocimiento puro, no destreza | `dmg = base * EFF * (correcta?1:0)` |
| "¡Es muy eficaz!" | Una caja de 1 línea con la **perla** de por qué (por ejemplo, "Litio: bajo Vd, dializable") | — |
| STAB | Bonus ×1.5 si el aliado es del dominio de la pregunta | — |
| Crítico | **Racha de 3 respuestas correctas**: la siguiente hace ×2 | `streak>=3` |
| Precisión | Sustituida por la respuesta: correcta = impacto; incorrecta = fallo y contraataque | — |
| Velocidad / orden | El enemigo ataca después de tu respuesta si fallas, o cada N turnos (opcional) | — |
| Estados | Aplicados a **enemigos**: "Opsonizado" (captura ×2), "Bloqueado" (pierde un turno). En el jugador solo estados leves de examen: "Distracción" (se ocultan 2 s las opciones) y "Duda" (se baraja el orden) | Evita "Sueño" en el jugador por la narcolepsia |
| Barra de PS | PS del residente; ya tienes `hp:5`. 1 error = −1 PS (o −2 contra un líder) | — |
| EXP / nivel | XP por acierto según dificultad. Curva sugerida: `xpNext = 20 + 10·nivel` (lineal) para subir de nivel cada 3–4 combates en una sesión de 1 h. **n³ es demasiado lenta para niveles de 1 h** | — |
| Aprender movimiento | Al subir de nivel se desbloquea un subtema nuevo (por ejemplo, "Belimumab en NL"); con 4 hay que elegir cuál olvidar | — |
| Evolución | El aliado evoluciona al dominar un dominio (≥80 % de aciertos en N ítems de la serie). Ejemplo: "Furosemida → Bloqueo secuencial" | Usa `srs` por `serie_id` |
| Captura | Con el enemigo <25 % de PS, opción "ARCHIVAR": una **pregunta de recuerdo** (flashcard) y, si aciertas, el ítem entra a la **Nefro-dex** | Probabilidad tipo Gen III: `1 - PS/PSmax` + bonus de estado |
| Pokédex | Glosario de perlas desbloqueadas, consultable fuera de combate | — |
| Equipo de 6 | 6 aliados = 6 dominios del temario: Glomerular, Electrolitos/Ácido-base, TRR, Trasplante, ERC/Anemia-MBD, Farmacología renal | Cambiar de aliado = cambiar de dominio (cuesta 1 turno) |
| Centro Pokémon | "Sala de residentes": cura PS, restaura PP y **muestra un resumen de los errores del nivel** (repaso de 30 s) | — |
| PC | "Expediente": mazo SRS completo; ya tienes `BOX=[1,3,7,16,35]` | — |
| Pociones | "Café de guardia" (+2 PS); "Interconsulta" (elimina 2 distractores, como un 50/50); "Guía KDIGO" (pista de 1 línea) | Se compran con créditos |
| Dinero | "Créditos": `pago_base × dificultad` del último caso | — |
| Entrenadores | **Residentes de otras especialidades** (MI, Urgencias, Reumato, Uro) con línea de visión, "¡!", diálogo y un caso clínico de 3–5 preguntas encadenadas (misma `serie_id`, `orden` 1→n) | Usa la estructura de serie del banco |
| Líder | **Adscrito o jefe del módulo**: caso largo de 6–10 preguntas en 2–3 fases (diagnóstico → tratamiento → complicación), con 2 "Restaurar Todo" (el líder recupera PS dos veces, como el Alto Mando [S12]) | — |
| Puzle de gimnasio | Puertas que se abren respondiendo bien: estilo Norman, salas con preguntas [S11], o interruptores estilo Erico donde cada interruptor es un dato de laboratorio | — |
| Alto Mando | Examen final: 4 jefes temáticos + "Presidente del CMN" seguidos, sin curación intermedia | — |
| Repel | "Pase directo": 50 pasos sin encuentros, para ir rápido al jefe | — |
| Huida | Siempre posible contra salvajes. El ítem vuelve al SRS con intervalo corto, así que **nunca se pierde la pregunta** | — |

### 8.3 Ritmo para la narcolepsia [Diseño]
- **Interacción cada ≤20–30 s.** Encuentro en hierba con `RATE ≈ 0.12–0.14` (≈1/8; algo más que el 1/9 de Pokémon) más:
  - **mínimo de 3 pasos** sin encuentro tras cada combate (anti-frustración);
  - **"pity" a los 14 pasos** en hierba: encuentro forzado.
- **Cajas cortas:** ≤60–80 caracteres, siempre con A para avanzar. **Nada de auto-avance**: el input mantiene la alerta.
- **Feedback inmediato:** sonido y destello en cada A, en cada paso y en cada acierto o fallo. "Bump" al chocar.
- **Detector de inactividad:** sin input en 25 s → un NPC o el enemigo "te llama", con un sonido suave y una micro-pregunta de 1 línea de verdadero/falso. No es punitivo y da un pequeño bonus de XP. Opcional y desactivable.
- **Escena de combate rápida:** transición de ≤600 ms (Pokémon usa ≈1 s), barras de PS a 2–3 px por cuadro y texto a 1 cuadro por carácter.
- **Explicación tras el error, obligatoria pero breve:** 1–2 cajas con la perla y el ítem al SRS. Tras un acierto, 1 caja opcional.

### 8.4 Presupuesto de un nivel de 45–60 min [Diseño]

| Bloque | Cantidad | Preguntas | Tiempo estimado |
|---|---|---|---|
| Encuentros salvajes | **20–25** | 1–3 cada uno (≈45) | 20–25 min (≈60 s cada uno) |
| Entrenadores (residentes) | **6–8** (3–4 en la ruta, 2–4 en el gimnasio) | 3–5 cada uno (≈30) | 12–16 min |
| Puzle del gimnasio | 3–4 "puertas" | 1 cada una (4) | 3–4 min |
| Líder | 1 | 6–10 | 6–8 min |
| Exploración, Centro, objetos, diálogo | — | — | 5–7 min |
| **Total** | — | **≈85–95 preguntas** | **≈50–60 min** |

- **Banco por nivel:** **35–50 ítems únicos** con repetición. El SRS reinyecta los fallados en el mismo nivel: un ítem fallado reaparece en 3–6 encuentros y uno acertado vuelve en el siguiente nivel o sesión. Así se consigue la "mucha repetición" sin agotar el banco.
- **Mapa del nivel ("órgano"):**

| Zona | Tamaño (celdas) | Contenido |
|---|---|---|
| Hub / Centro | 12×10 | Sala de residentes (curar), tienda y 2 NPCs con pistas |
| Ruta | **40×12** (horizontal; cruzarla caminando ≈11 s, corriendo ≈5.5 s) | 3–4 parches de hierba de 4×4 a 6×5 celdas (≈80–100 celdas de hierba en total), 3–4 entrenadores, 3 objetos en el suelo, 2 letreros |
| Gimnasio | 16×14 | Puzle de 3–4 puertas, 2–4 entrenadores y el líder al fondo |

- **Comprobación:** 20–25 encuentros × ≈8 pasos de media en hierba ≈ 160–200 pasos en hierba ≈ 45–55 s de caminata pura. El tiempo lo ocupa el estudio, no el desplazamiento.
- **Curva de dificultad dentro del nivel:** salvajes con dificultad 1–2 → entrenadores de 2–3 → líder de 3–4 (casos tipo examen del CMN). Es la misma lógica de +3–5 niveles por gimnasio de RSE [S11].

### 8.5 Pseudocódigo: motor de movimiento por cuadrícula
```js
const T=16, WALK=1, RUN=2;              // px/cuadro → 16 y 8 cuadros por celda [S1]
const p={tx:5,ty:5,px:80,py:80,dir:'down',moving:false,tgtX:0,tgtY:0,turnT:0,bumpT:0};
let stepsSinceBattle=0, stepsInGrass=0;

function updatePlayer(){
  if(state!=='OVERWORLD') return;
  if(p.moving){
    const sp = keys.b ? RUN : WALK;
    p.px += Math.sign(p.tgtX - p.px)*sp;
    p.py += Math.sign(p.tgtY - p.py)*sp;
    if(p.px===p.tgtX && p.py===p.tgtY){ p.moving=false; onStepEnd(); }
    return;                              // sin input a mitad de la celda
  }
  if(p.bumpT>0){ p.bumpT--; return; }
  const d = heldDir();                   // 'up'|'down'|'left'|'right'|null
  if(keys.aPressed) return interact();
  if(!d) return;
  if(d!==p.dir && !wasHeldLastFrame(d)){ p.dir=d; p.turnT=8; return; } // toque = girar
  if(p.turnT>0){ p.turnT--; return; }
  p.dir=d;
  const [nx,ny]=[p.tx+DX[d], p.ty+DY[d]];
  if(isSolid(nx,ny) || npcAt(nx,ny)){ sfx('bump'); p.bumpT=16; return; }
  p.tx=nx; p.ty=ny; p.tgtX=nx*T; p.tgtY=ny*T; p.moving=true;
}

function onStepEnd(){
  const w = warpAt(p.tx,p.ty); if(w) return fadeWarp(w);         // puerta: fundido ≈300 ms
  if(checkTrainerSight()) return;                                 // "!" + caminar hacia ti
  stepsSinceBattle++;
  if(tileAt(p.tx,p.ty)===GRASS){
    stepsInGrass++; grassRustle(p.tx,p.ty);
    const roll = Math.random() < RATE || stepsInGrass>=14;        // pity
    if(stepsSinceBattle>=3 && roll && repelSteps<=0){ stepsInGrass=0; startBattle(pickEncounter(), 'wild'); }
  }
  if(repelSteps>0) repelSteps--;
}

function checkTrainerSight(){
  for(const t of trainers) if(!t.beaten){
    for(let i=1;i<=t.range;i++){
      const x=t.tx+DX[t.dir]*i, y=t.ty+DY[t.dir]*i;
      if(isSolid(x,y)) break;
      if(x===p.tx && y===p.ty){ queue([showBang(t), walkTo(t,p), talk(t.intro), ()=>startBattle(t,'trainer')]); return true; }
    }
  }
  return false;
}

function camera(){ camX = p.px - 72; camY = p.py - 40; }          // fija al jugador [S1]
```

### 8.6 Pseudocódigo: bucle de combate (máquina de estados)
```js
// Estados: INTRO → MENU → MOVE_SELECT → QUESTION → RESOLVE → ENEMY_TURN → CHECK_END → (MENU | WIN | LOSE)
function startBattle(enemy, kind){
  B={enemy:clone(enemy), kind, phase:'INTRO', streak:0, qIdx:0, archive:false};
  transition(kind==='wild'?'flash3':'blinds', 600).then(()=>say(`¡${enemy.name} apareció!`, ()=>B.phase='MENU'));
}

function battleUpdate(){
  switch(B.phase){
    case 'MENU':        // LUCHAR / MOCHILA / EQUIPO / HUIR (2×2, flechas)
      menu2x2(['LUCHAR','MOCHILA','EQUIPO', B.kind==='wild'?'HUIR':'—'], choice=>{
        if(choice==='LUCHAR') B.phase='MOVE_SELECT';
        if(choice==='MOCHILA') openBag(item=>{ useItem(item); B.phase='ENEMY_TURN'; });
        if(choice==='EQUIPO')  openParty(a=>{ swapAlly(a); B.phase='ENEMY_TURN'; });
        if(choice==='HUIR')   { srsPush(B.enemy.qid, 'short'); endBattle('fled'); }
        if(choice==='ARCHIVAR') B.phase='CAPTURE';     // aparece con PS enemigo <25 %
      }); break;

    case 'MOVE_SELECT': // 4 movimientos con PP y tipo visibles
      menuMoves(ally.moves, m=>{ if(m.pp<=0) return say('Sin PP. Rota de tema.');
        m.pp--; B.move=m; B.q=pickQuestion(m.topic, B.enemy.diff); B.phase='QUESTION'; }); break;

    case 'QUESTION':    // caso paginado (A avanza) → opciones con panel de opción completa
      showCase(B.q, ()=> chooseOption(B.q, ans=>{ B.correct=(ans===B.q.correcta); B.phase='RESOLVE'; })); break;

    case 'RESOLVE':
      srsUpdate(B.q.id, B.correct);
      if(B.correct){
        B.streak++;
        const eff = EFF[B.move.type][B.enemy.type] ?? 1;
        const stab = ally.type===B.move.type ? 1.5 : 1;
        const crit = B.streak>=3 ? 2 : 1; if(crit>1) B.streak=0;
        const dmg = Math.ceil(B.move.power * eff * stab * crit);
        animHit(); B.enemy.hp=Math.max(0,B.enemy.hp-dmg);
        say([crit>1?'¡Golpe crítico!':null, effMsg(eff), B.q.perla].filter(Boolean), ()=>B.phase='CHECK_END');
      } else {
        B.streak=0;
        say([`Incorrecto. Era ${B.q.correcta}.`, B.q.perla], ()=>B.phase='ENEMY_TURN');
      } break;

    case 'ENEMY_TURN':  // el enemigo sólo daña tras un error o un turno no ofensivo
      animShake(); player.hp -= B.enemy.atk; say(`${B.enemy.name} usó ${B.enemy.move}.`, ()=>B.phase='CHECK_END'); break;

    case 'CHECK_END':
      if(B.enemy.hp<=0) return win();
      if(player.hp<=0)  return lose();   // vuelve a la sala de residentes, pierde ½ créditos
      B.phase='MENU'; break;

    case 'CAPTURE':     // flashcard de recuerdo; probabilidad estilo Gen III [S16]
      flashcard(B.enemy.card, ok=>{ const pc = ok ? Math.min(1, 1 - B.enemy.hp/B.enemy.max + 0.5) : 0;
        if(Math.random()<pc){ dexAdd(B.enemy); endBattle('caught'); } else B.phase='ENEMY_TURN'; }); break;
  }
}
const effMsg = e => e>1?'¡Es muy eficaz!': e===0?'No afecta…': e<1?'No es muy eficaz…':null;

function win(){
  const xp = B.enemy.xp * (B.kind==='trainer'?1.5:1);           // a = 1.5 de Gen III [S17]
  gainXP(xp);                                                    // xpNext = 20 + 10·nivel
  if(B.kind!=='wild') credits += B.enemy.base * B.enemy.diff;    // ≈ pago_base × nivel [S10]
  checkEvolution(); endBattle('won');
}
```

### 8.7 Prioridades de implementación (orden sugerido)
1. Movimiento por cuadrícula + colisión + cámara (§8.5): es la base del "le gusta moverse con flechas".
2. Hierba + encuentro con mínimo y *pity* + transición ≤600 ms.
3. Combate con 4 movimientos y PP + pregunta paginada + perla tras el fallo.
4. Entrenadores con línea de visión y series de casos (`serie_id`).
5. Centro (curar y repaso de errores) + líder de 2–3 fases.
6. Tipos y efectividad, captura y Nefro-dex, evolución por dominio.

---

## Fuentes
| # | Fuente | URL |
|---|---|---|
| S1 | Blake Crosley, "Pixel-Art Motion: Walks, Cameras and Doors" (cifras contadas del decomp de Esmeralda) | https://blakecrosley.com/blog/pixel-art-motion-on-iphone |
| S2 | Bulbapedia – Running Shoes | https://bulbapedia.bulbagarden.net/wiki/Running_Shoes |
| S3 | Bulbapedia – Repel | https://bulbapedia.bulbagarden.net/wiki/Repel |
| S4 | Bulbapedia – Wild Pokémon (tasas de encuentro Gen III) | https://bulbapedia.bulbagarden.net/wiki/Wild_Pok%C3%A9mon |
| S5 | TASVideos – Pokémon Gen 3 RNG (comprobación por paso, crítico, precisión, captura) | https://tasvideos.org/GameResources/GBA/PokemonGen3/RNG |
| S6 | Pokébip – Encounter slots Rubis (12 *slots* en hierba) | https://www.pokebip.com/page/jeux-video/dossier-shasse/encounter-slot/rubis/lieux |
| S7 | Geek to Geek Media – "Pokémon's grassy route to success" (análisis de diseño) | https://geektogeekmedia.com/geekery/pokemons-grassy-route-to-success |
| S8 | Bulbapedia – Fleeing (escape) | https://bulbapedia.bulbagarden.net/wiki/Fleeing |
| S9 | Bulbapedia – Pokémon Trainer | https://m.bulbapedia.bulbagarden.net/wiki/Trainer |
| S10 | Bulbapedia – Prize money (pagos base Gen III; derrota en RSE) | https://bulbapedia.bulbagarden.net/wiki/Payout |
| S11 | Serebii – Hoenn Gyms (Esmeralda) | https://serebii.net/emerald/gym.shtml |
| S12 | Bulbapedia – Pokémon League (Hoenn) | https://bulbapedia.bulbagarden.net/wiki/Pokemon_League_(Hoenn) |
| S13 | Dr Lava – Traducción de la entrevista a Sugimori y Masuda sobre el desarrollo de la Gen 3 | https://lavacutcontent.com/sugimori-masuda-gen-3-interview/ |
| S14 | Bulbapedia – Damage | https://bulbapedia.bulbagarden.net/wiki/Damage |
| S15 | Bulbapedia – Critical hit | https://bulbapedia.bulbagarden.net/wiki/Critical_hit |
| S16 | Bulbapedia – Catch rate | https://bulbapedia.bulbagarden.net/wiki/Catch_rate |
| S17 | Bulbapedia – Experience | https://m.bulbapedia.bulbagarden.net/wiki/Experience |
| S18 | saschb2b – Pokémon RSE: design tensions | https://saschb2b.github.io/game-mechanics/games/pokemon-rse/design-tensions |
| S19 | Bulbapedia – Options | https://bulbapedia.bulbagarden.net/wiki/Option |

Fuentes complementarias consultadas sin datos extraídos: Siliconera / GameSpot sobre Masuda y la dificultad de desarrollar RS (https://www.siliconera.com/game-freaks-junichi-masuda-says-pokmon-ruby-sapphire-hardest-make/); pret/pokeemerald wiki, "New Options Plus" (https://github-wiki-see.page/m/pret/pokeemerald/wiki/New-Options-Plus-%E2%80%90-Multipage-Options-Menu-with-Faster-Text,-HP%E2%80%90EXP-Bar-Speeds-and-Metric).

**Pendiente de verificar [†] antes de usarlo como dato duro:** la fórmula exacta de huida, la de EXP ganada, los polinomios de las curvas no cúbicas, los pasos de Super/Max Repel, los retardos de texto 8/4/1, los precios de pociones, las capacidades del PC, la duración de los estados y los nombres de los mensajes en español.
