# El Residente Miniatura — guía para sesiones de Claude Code

Videojuego educativo estilo Pokémon Gen III (HTML/JS, canvas 160×96) para que Alfredo, residente de último año de nefrología, estudie para el examen del Consejo Mexicano de Nefrología (**16 de enero de 2027**, 300 preguntas con casos seriados). Lee `docs/DISENO.md` antes de cambiar nada.

## Comandos
- `npm install` (una vez) · `python3 build.py` → `dist/index.html` (juego completo: mapa, 32 niveles y Torre) · `python3 build.py levels/<nivel>` → `dist/<id>.html` (un nivel)
- `python3 build.py --pwa` → `docs/` (app instalable que GitHub Pages sirve desde la rama, carpeta `/docs`: `index.html`, `sw.js`, `manifest.webmanifest`, iconos). **Vuelve a correrlo y haz commit de `docs/` cada vez que cambie el juego**, o los dispositivos no reciben la versión nueva.
- `python3 tools/nivel.py [id…]` → regenera los niveles compactos desde `levels/_specs/*.py` (no edites a mano su `story.json`, `q_extra.json` ni `q_banco.json`)
- `npm test` → construye y juega **todos** los niveles con un autómata (modo correcto y con 35 % de errores), y prueba el mapa y la Torre; `npm test -- levels/<nivel>` juega solo uno. Todo debe decir `PASA`.
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
8. `data/bank.json` es la versión corregida de la app "Banco maestro de nefrología" de Alfredo (24 nov 2026: 1789 preguntas; la correcta es la más larga en ~21 %). Si Alfredo actualiza la app, vuelve a copiar `bank.json`, `temario.json` y `competencias.json` desde su artefacto y regenera los `q_banco.json` por `id` (`python3 tools/nivel.py`). Las correcciones médicas propias del juego van en `data/correcciones.json` (se aplican al construir) y se avisan a Alfredo.

## Cómo añadir un nivel
Hay dos clases de nivel:
- **Largos, a mano** (`9-5-lupus`, `9-6-anca`): `story.json` y `q_extra.json` propios, con preguntas nuevas. Esquema en `docs/DISENO.md`, sección 5.
- **Compactos, generados** (los otros 30): una especificación corta en `levels/_specs/*.py` (zonas, diálogos, minijuegos, jefe y pasto V/F). `tools/nivel.py` toma las preguntas de opción múltiple de `data/bank.json` y las reparte: recordadas de examen al jefe y a los entrenadores, el resto a las puertas.

Para alargar un nivel compacto: añade zonas a su spec, o conviértelo en largo copiando la estructura de `9-6-anca`. Después valida, construye y corre `npm test`. El orden y el nombre de los niveles en el mapa están en `data/regiones.json`; las criaturas comunes, en `data/criaturas.json`.

## Deuda técnica
Ver "Pendientes de ingeniería" en `docs/DISENO.md`. El punto 1 (sacar lupus del motor) ya está hecho: el motor no debe volver a conocer ningún nivel; todo lo propio va en `story.json`.
