# El Residente Miniatura — guía para sesiones de Claude Code

Videojuego educativo estilo Pokémon Gen III (HTML/JS, canvas 160×96) para que Alfredo, residente de último año de nefrología, estudie para el examen del Consejo Mexicano de Nefrología (**16 de enero de 2027**, 300 preguntas con casos seriados). Lee `docs/DISENO.md` antes de cambiar nada.

## Comandos
- `npm install` (una vez) · `python3 build.py [levels/<nivel>]` → `dist/index.html`
- `npm test` → construye y juega el nivel completo con un autómata (modo correcto y con 35 % de errores). Debe terminar en `DONE` y `errors []`.
- `python3 tools/validate_story.py levels/<nivel>/story.json`
- `python3 tools/validate_questions.py levels/<nivel>/q_extra.json` (sesgo de longitud ≤25 %, letras balanceadas)

## Reglas que no se negocian
1. **Idioma:** todo el contenido en español de México; términos médicos internacionales en su forma habitual.
2. **Exactitud médica:** cada pregunta lleva referencia (guía KDIGO/ISPD/Banff vigente o ensayo). Verifica en la web lo que no sea seguro; no cites PMID de memoria. Si un borrador KDIGO se apoya en ensayos ya publicados, la respuesta correcta sigue la evidencia nueva y se añade la nota "Ley anterior".
3. **Sin sesgo de longitud:** la opción correcta no puede ser la más larga en más del 25 % de las preguntas; opciones dentro de ±25 % de la longitud media. Corre el validador.
4. **Narcolepsia del jugador:** cuadros de diálogo ≤90 caracteres, máximo 4 cuadros seguidos sin interacción, explicación visible ≤40 palabras (el resto en "Ver más"). No quitar la alarma de inactividad ni el DESPERTADOR.
5. **El conocimiento pesa más que la destreza:** un ataque solo ocurre si se acierta la pregunta.
6. **Prioridad de preguntas:** las recordadas de examen (`origen` terminado en `26` en `data/bank.json`) van a jefes y entrenadores.
7. **Datos personales:** en el Drive de Alfredo hay expedientes de pacientes reales. No usarlos nunca.
8. Las preguntas de `data/bank.json` traen sesgo de longitud (99 % la correcta es la más larga); Alfredo lo está corrigiendo en otra app. Pregúntale por la versión corregida antes de reutilizarlas en masa.

## Cómo añadir un nivel
1. Copia la estructura de `levels/9-5-lupus/` (esquema en `docs/DISENO.md`).
2. Guion → `story.json` (10 zonas aprox. para temas grandes, 3–5 para chicos).
3. Preguntas → `q_extra.json` (pasto, puertas, entrenadores seriados, jefe) + `q_banco.json` (extraídas de `data/bank.json` por `tema_id`).
4. Valida, construye y corre `npm test`. Pide a Alfredo que lo juegue antes de seguir con el siguiente.

## Deuda técnica (hacer primero)
Ver "Pendientes de ingeniería" en `docs/DISENO.md`: varias piezas del motor siguen escritas a mano para lupus.
