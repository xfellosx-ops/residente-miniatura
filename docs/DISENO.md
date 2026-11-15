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
| 5 · El glomérulo | 9 (7 subniveles; hechos 9-5 lupus y 9-6 ANCA/anti-MBG) | II |
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

## 5. Esquema de un nivel
- `story.json`: `meta`, `cast`, `zones[]`, `boss`, `creatures`, `typeChart`, `shields`, `nefrodex` y, opcionales, `themes`, `enemyTypes`. Validado por `tools/validate_story.py`. Todo lo propio del nivel vive aquí; el motor no conoce ningún nivel.
  - `meta`: `id` ("9-6"), `title`, `key` (clave de guardado en `localStorage`, **única por nivel y no cambiarla una vez publicada**: borra el avance), `arena`, `bossShort`, `bossChange`.
  - `zones[i]`: `id,name,palette,tiles,intro,npcs,trainers,wild,gates,minigames,cutscenes,card` más
    `join` (ids de criaturas que se unen al entrar), `signs` (`[[título,texto],…]`, ≤90 caracteres), `nurse` (true = enfermera que cura),
    `vignette` (nombre de una viñeta de la biblioteca `VIG` del motor —las 10 de lupus: `urgencias, uv_piel, pantano_restos, ganglio, rio_sangre, delta_endocapilar, acantilado_podocito, ruinas_asas, capsula_semiluna, valle_tubulovascular`— o un objeto `{bg, layers[]}` con capas `rect, circ, ring, stripes, cells, drift, orbit, pulse, grow, person`; cada capa admite `every` para parpadear; ver ejemplos en `levels/9-6-anca/story.json`),
    `theme` (`{f,w,g}`: piso, muro y hierba; sobrescribe los colores del `tiles`).
  - `trainers[]`: `serie` (id de una serie de `q_extra.entrenadores`); si falta, se eligen `n` preguntas por `questionTopics`.
  - `boss`: `intro, phases[], outro` y `color, dark, heads, headColors` (sprite). Cada fase: `name, type` (tipo enemigo), `lines`, `topics` y sus preguntas: `questions` (ids), `series` (series completas) y/o `pick` (`{topics,n}` por tema). Si no trae ninguna, se eligen por `topics`.
  - `creatures[]`: además de `moves`, opcionales `color`, `dark` y, por movimiento, `fx` (animación de la biblioteca: `Fagocito, Depurador, Humoral, Regulador, Supresor, Antimetabolito, Endosomal, Podoprotector, Anti-citocina, Depletor, Alquilante`).
- `tiles` disponibles (decoración del mapa): `hospital, playa, pantano, bosque, rio, delta, acantilado, ruinas, capsula, valle, arena`.
- `q_base.json` (opcional, formato de 9-5): `apertura`, `gates{}`, `subditos[]`, `pasto[]`, `stones[]`, `jefeB[]`. Los niveles nuevos ponen todo en `q_extra.json`.
- `q_extra.json`: `pasto[]`, `puertas[]`, `entrenadores[]` (con `serie_id`, `orden`, `caso`, `continuacion`), `jefeC[]`.
- `q_banco.json` (opcional): preguntas del banco de Alfredo para ese tema (mismo formato que `data/bank.json`).
- Pregunta de opción múltiple: `id, enunciado, opciones{A..E}, clave, explicaciones{A..E}, perla, referencias[], peso, tema`. Pasto V/F: `id, vf:true, enunciado, clave:"V"|"F", exp`.

## 6. Pendientes de ingeniería (en orden)
1. ~~Sacar del motor lo específico de lupus~~ **Hecho (15 nov 2026).** `JOIN`, `SERIE_OF`, `PLAN.boss`, `SIGNS`, viñetas, colores por `tiles`, enfermera, `KEY` y textos del título y jefe salen de `story.json` (sección 5). La clave de lupus sigue siendo `rm_v2_95` para no perder la partida de Alfredo. Queda en el motor, como biblioteca reutilizable: los patrones de `deco` por `tiles`, las 10 viñetas de lupus (`VIG`) y las animaciones de ataque (`drawFx`).
2. **Selector de niveles / mapa de regiones** con progreso global y equipo persistente entre niveles.
3. **PWA instalable sin internet** (service worker, manifest) y exportar/importar partida para pasar de celular a tableta; sincronización real si se añade un backend.
4. Unificar los tres archivos de preguntas en uno por nivel. (El `data-id` ya está: el autómata identifica las preguntas por `id`, y el falso error de `T2-UCI-4` desapareció.)
5. Imágenes reales de biopsia en preguntas (solo propias o de licencia abierta, con crédito).
6. Ideas aprobadas sin implementar: apuesta de confianza, modo guardia (caso sorpresa), prueba de entrada por tema que acorta o alarga el nivel, recuerdo escrito con teclado, arte y sonido mejores.

## 7. Pendientes de contenido
- **9-6:** `q_banco.json` está vacío a propósito: las 14 preguntas de ANCA/anti-MBG del banco (series `ANCA`, `ANB`, `GBM`, `AGB`; varias recordadas `…26`) tienen sesgo de longitud fuerte. Alfredo pidió esperar su versión corregida; cuando llegue, copiarlas y repartirlas entre jefe y entrenadores (regla 6).
- **9-5 (regla 4):** `validate_story.py` avisa más de 4 cuadros seguidos al entrar en z1, z2, z6, z7 y z10, y en intro del jefe + fase 1. Recortar con Alfredo.
- Verificar en PubMed los PMID del guion de lupus (`levels/9-5-lupus/guion.md`, refs. 1–5, 18–23, 25) y los puntos marcados `[VERIFICAR]`.
- `q_banco.json` de lupus: nomenclatura "IV-G (A)" obsoleta (ISN/RPS 2018 la eliminó) y sesgo de longitud.
- Temas con pocas preguntas en el banco (1, 3, 10, 11): generar casos nuevos.
- Borradores KDIGO a incorporar: LRA/AKD 2026 (nivel 6) y diabetes y ERC 2026 (nivel 8).
- Bibliografía oficial del Consejo: Brenner 9.ª, Comprehensive 5.ª, Primer NKF, Daugirdas, Danovitch, Rose, Graff, UpToDate. Alfredo puede subir capítulos; los términos de Elsevier restringen su uso con IA, es decisión suya.

## 8. Documentos de apoyo
- `docs/research_pokemon.md`: mecánicas de Rubí/Zafiro/Esmeralda con cifras y adaptación.
- `docs/critique.md`: playtest crítico de la v1 (bugs ya corregidos en v2–v3; sirve como lista de control).
- `levels/9-5-lupus/guion.md`: guion largo con fisiopatología, giros y mnemotecnias.
