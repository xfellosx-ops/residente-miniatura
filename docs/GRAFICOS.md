# Gráficos de El Residente Miniatura — guía para quien los mejore

Todo el dibujo está en **un solo archivo: `engine/template.html`** (unas 600 líneas; el JavaScript va dentro de `<script id="eng">`). No hay imágenes: cada cosa se pinta con código sobre un lienzo de **160 × 96 píxeles** (`<canvas id="cv">`), que el navegador amplía con `image-rendering: pixelated`. Las casillas del mapa miden **16 × 16**.

## Dónde está cada cosa (busca el nombre de la función)
Estilo: pixel art a baja resolución, vista cenital, contorno oscuro de 1 px y paletas cortas. El contorno lo pone solo `sprite()`.

| Qué se ve | Función | Notas |
|---|---|---|
| Primitivas | `px`, `circ`, `oval`, `ring2`, `tint(color, k)` | `tint` aclara (k>0) u oscurece (k<0) |
| Caché de sprites con contorno | `sprite(clave, ancho, alto, dibujar)` y `stamp(sprite, x, y)` | Se dibuja una vez en un lienzo chico; el contorno se añade solo |
| Personas | `person(x,y,color,dir,frame,piel)` | 16×19, tres vistas, dos cuadros; bata blanca si el color es `#ffffff` |
| Criaturas de combate | `drawCreature(x,y,forma,t,opciones)`; formas en `CSH` | `shapeOfFoe` elige por nombre y tipo del enemigo; `shapeOfAlly`, por criatura del equipo |
| Objetos de las casillas | `OBJ` (árbol, roca, cristal, célula, anillo/túbulo, eritrocito, cama, monitor, estante, mesa, ruina, charco) y `TILESET` (qué objetos y colores usa cada tipo de zona) | Para un escenario nuevo basta añadir una entrada a `TILESET` |
| Suelo y hierba | `floorTile()` (con borde junto a los muros), `grassTile()` | Colores base en `THEME` |
| Puerta, letrero, cristal de minijuego, salida | `gateSprite`, `signSprite`, `crystalSprite`, `exitSprite` | |
| Combate (fondo, plataformas, cajas de vida) | `drawBattle()`, `uiBox()`, `hpbar()` | |
| Villanos con sprite propio en el mapa | `VILLAIN` (aine, contraste, genta, tacro, levamisol, solvente, hemo) y `personAs()` | La clave es el `cast` del entrenador en `story.json` |
| Jefes | `bossSprite(fase,color,oscuro,cabezas)` y `drawBoss()` | F1 defensor · F2 corrupto (ojos rojos) · F3 cuernos de semiluna y tentáculos · F4 avatar de La Esclerosis con remolino |
| Pantalla VS antes del jefe · Torre | `drawVS()`, `drawTorre()`, `vortex()`, `crescent()` | Se muestran con `OVER` (capa que reemplaza al mapa mientras dura) |
| Animaciones de ataque | `drawFx()` | |
| Viñetas al entrar/salir de una zona | `VIG.*` y `drawSpec()` | |
| Paneles, botones y diálogo | bloque `<style>` | Paneles crema, cabeceras verdes, diálogo con borde azul |

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
