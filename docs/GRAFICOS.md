# Gráficos de El Residente Miniatura — guía para quien los mejore

Todo el dibujo está en **un solo archivo: `engine/template.html`** (unas 600 líneas; el JavaScript va dentro de `<script id="eng">`). No hay imágenes: cada cosa se pinta con código sobre un lienzo de **160 × 96 píxeles** (`<canvas id="cv">`), que el navegador amplía con `image-rendering: pixelated`. Las casillas del mapa miden **16 × 16**.

## Dónde está cada cosa (busca el nombre de la función)
| Qué se ve | Función | Notas |
|---|---|---|
| Primitivas | `px(x,y,w,h,color)`, `circ(x,y,r,color)`, `ring2(...)` | Todo lo demás se arma con estas |
| Personas (jugador, NPC, entrenadores) | `person(x,y,color,dir,frame,piel)` | Sprite de 16×16, 2 cuadros de caminata |
| Criaturas y enemigos en combate | `blob(...)` y `drawBattle()` | Hoy son círculos con ojos; el jefe se dibuja en `drawBattle` |
| Casillas del mapa | `deco()` (muros/decoración por `tiles`), `floorTile()`, `grassTile()` | Colores base en `THEME`; estilos: hospital, playa, pantano, bosque, rio, delta, acantilado, ruinas, capsula, valle |
| Mapa completo y objetos (puertas, letreros, cristales) | `drawWorld()` | Cámara de 10 × 6 casillas |
| Animaciones de ataque | `drawFx()` | Una por tipo de movimiento, 36 cuadros |
| Viñetas al entrar/salir de una zona | `VIG.*` (dibujadas a mano) y `drawSpec()` (capas declaradas en `story.json`) | |
| Minijuego del río, despertador, título, Torre | `drawRiver()`, `drawWake()`, `title()`, `torre()` | |
| Botones, paneles, tipografía | bloque `<style>` al inicio | Paleta tipo Game Boy en `:root` |

## Reglas para no romper el juego
1. Mantén el lienzo en 160 × 96 y las casillas en 16 × 16: el mapa, la cámara y las pruebas dependen de eso.
2. No cambies nombres ni parámetros de las funciones de la tabla; cambia solo lo que pintan por dentro.
3. Si quieres usar imágenes (sprites PNG), intégralas como texto dentro del mismo archivo (`data:image/png;base64,…`) y dibújalas con `cx.drawImage`. El juego debe seguir siendo **un solo HTML sin archivos externos**, para que funcione sin conexión.
4. No toques la lógica de preguntas, guardado (`save`, `rm_*`), alarma de inactividad ni DESPERTADOR.
5. Los datos de los niveles llegan en los marcadores `__LEVELS__`, `__REGIONS__`, `__TEMARIO__`, `__TITLE__` y `<!--PWA-->`: no los borres.

## Cómo probar un cambio
```
python3 build.py            # arma dist/index.html; ábrelo en el navegador
npm test                    # juega todo con el autómata; todo debe decir PASA
python3 build.py --pwa      # actualiza la app instalable en docs/
```
