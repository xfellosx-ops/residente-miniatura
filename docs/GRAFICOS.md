# Gráficos de El Residente Miniatura — guía para quien los mejore

Todo el dibujo está en **un solo archivo: `engine/template.html`** (unas 1000 líneas; el JavaScript va dentro de `<script id="eng">`). No hay imágenes: cada cosa se pinta con código sobre un lienzo de **160 × 96 píxeles** (`<canvas id="cv">`), que el navegador amplía con `image-rendering: pixelated`. Las casillas del mapa miden **16 × 16**.

## Dónde está cada cosa (busca el nombre de la función)
Estilo: pixel art a baja resolución, vista cenital, contorno oscuro de 1 px y paletas cortas. El contorno lo pone solo `sprite()`.

| Qué se ve | Función | Notas |
|---|---|---|
| Primitivas | `px`, `circ`, `oval`, `ring2` (anillo exacto por filas, sin moiré), `tint(color, k)`, `mix(a,b,k)`, `line`, `arrow` | `tint` aclara (k>0) u oscurece (k<0) |
| Rótulos dentro del lienzo | `lbl(texto,x,y,color,placa)` y `txt3` | Letra de 3×5 (`F3`), nítida y con caché; acepta acentos, ↑↓→←, α β γ κ λ π µ. `placa:"none"` = sin fondo |
| Primitivas con contorno para viñetas | `oc`, `orc`, `oov`, `vlayer(clave, dibujar)` | `vlayer` pinta la capa fija una vez, le pone contorno y la guarda en caché; lo animado va encima |
| Histología reutilizable | `rbc` (eritrocito con palidez central), `acanto`, `nucleus`, `ecell`, `glom` (Bowman + asas + mesangio), `arteriole`, `tubX` (túbulo en corte) | Úsalas para viñetas nuevas |
| Caché de sprites con contorno | `sprite(clave, ancho, alto, dibujar)` y `stamp(sprite, x, y)` | Se dibuja una vez en un lienzo chico; el contorno se añade solo |
| Personas | `person(x,y,color,dir,frame,piel)` | 16×19, tres vistas, dos cuadros; bata blanca si el color es `#ffffff` |
| Criaturas de combate | `drawCreature(x,y,forma,t,{tcol})`; formas en `CSH` | `shapeOfFoe` recorre `FOE_RULES` (expresiones con `\b` sobre el nombre) y, si nada coincide, usa el tipo. `typeColor(tipo)` tiñe las formas sin color histológico fijo (`fix:1`) |
| Objetos de las casillas | `OBJ` (árbol, roca, cristal, célula, anillo, eritrocito, cama, monitor, estante, mesa, ruina, charco, `tubX`, `cepillo`, `sal`, `celulaPrinc`, `fibra`, `capilar`, `burbuja`, `pliegue`, `fibraHueca`, `linfo`) y `TILESET` | Escenarios genéricos (`hospital, playa, pantano, bosque, rio` (sangre), `delta, acantilado, ruinas, capsula, valle`) y por estructura: `tubulo` (orina ámbar), `proximal`, `henle`, `colector`, `intersticio`, `peritoneo`, `dializador`, `injerto`. `deco` deja ~50 % de muro liso (`wallTile`) y agrupa objetos en bloques de 2×2 con `hsh` (sin diagonales) |
| Suelo y hierba | `floorTile()`, `grassTile()`, `themeOf()` | Colores en `THEME`; los escenarios genéricos se tiñen con `REGPAL` (paleta maestra por región) y `themeOf` asegura contraste camino/hierba/muro |
| Puerta, letrero, cristal de minijuego, salida | `gateSprite`, `signSprite`, `crystalSprite`, `exitSprite` | |
| Combate (fondo, plataformas, cajas de vida) | `drawBattle()`, `uiBox()`, `hpbar()`, `BOSSARENA()` | La arena del jefe usa la paleta de la última zona |
| Villanos con sprite propio en el mapa | `VILLAIN` (aine, contraste, genta, tacro, levamisol, solvente, hemo) y `personAs()` | La clave es el `cast` del entrenador en `story.json` |
| Jefes | `bossSprite(fase,color,oscuro,cabezas)` y `drawBoss(x, yPies, fase)` | Arquetipo por `boss.form`: `defensor, quimera, cristal, ola, masa, maquina, vaso, hialino, microbio, glandula, anticuerpo, iga, muro, quistes, gen` (lista `BOSS_FORMS`). Lienzo 64×60 con pies en la fila 57. F2 ojos rojos y grietas · F3 aura (semiluna solo con `boss.crescent:true`, GN con semilunas) · F4 placas hialinas y remolino de La Esclerosis |
| Pantalla VS antes del jefe · Torre | `drawVS()`, `drawTorre()`, `vortex()`, `crescent()` | Se muestran con `OVER` (capa que reemplaza al mapa mientras dura) |
| Animaciones de ataque | `playFx`, `drawFx`, `fxRecoil` | Tres fases: carga (0–10, el atacante retrocede y brilla), viaje (10–28), impacto (28–38, el blanco parpadea y se sacude). Destello seguro: 2 cuadros al 30 % solo sobre el blanco. Efectos de aliado por `fx` o tipo del movimiento (`FXCOL`): Fagocito, Depurador, Humoral, Regulador, Supresor, Antimetabolito, Endosomal, Podoprotector, Anti-citocina, Depletor, Alquilante, Glucocorticoide, Recambio, Anti-C5aR, Diurético (NKCC2 bloqueado), Nefroprotector (Na⁺ a mácula densa → aferente se contrae), Sonda, Anti-complemento. Ataque enemigo por tipo: Inmunocomplejo (red que se deposita), Complemento (poro), Humoral (Y que se pegan), Innato (NET), Celular (linfocito), Molecular |
| Viñetas al entrar/salir de una zona | `VIG.*`, `drawVignette`, `drawSpec` | Las 10 de lupus más ~55 por contenido: `glomerulo_sano, nefrona, diureticos, henle` (A), `ayg` (B), `adh_aqp2, fgf23, compartimentos, starling, proximal_farmaco, proximal_toxico, proximal_quimio, tfg_ecuacion, sedimento` (E), `biopsia, nta, hemodialisis` (G), `fistula, osmosis, dp_poros` (H), `peritonitis, sindromes, complemento, acantilado_podocito` (corregida), `gefs, membranosa` (C), `if_patrones` (D), `necrosis_fibrinoide, iga_mucosa, iga_mesangio, amiloide, mieloma, nti, fibrosis, tfg_declive, anemia_epo, diabetes_kw, cuatro_pilares, mat, estenosis, preeclampsia, trombosis_vena, alport, tubulopatias, erpad_cilio, erpad_rinon, cristales, itu, pielonefritis, hidronefrosis, vejiga, hta, suprarrenal, embarazo, hla, banff` (F), `bk, desgaste, cocina, edema_cerebral, potasio, minerales, brecha, metanol, intercalada, tumor`. Cada zona de los specs declara `"vignette"`; `tools/nivel.py` usa una por región si falta y `validate_story.py` lee los nombres del motor |
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

## Cómo añadir arte nuevo
- **Viñeta:** `VIG.nombre=t=>{px(0,0,160,96,fondo);vlayer("nombre",()=>{…capa fija con lbl…});…animación con oc/rbc/along…}`. Luego ponla en `"vignette"` de la zona (spec o `story.json`). Usa los códigos de color de la biblia: eosina rosa, hematoxilina violeta, orina ámbar, sangre carmín, tricrómico azul, PAS magenta.
- **Familia de enemigo:** añade la forma a `CSH` (con `fix:1` si su color es histológico), su `case` en `drawCreature` y una regla en `FOE_RULES` (las reglas se prueban en orden; usa `\b`).
- **Escenario por estructura:** entrada en `THEME`, `TILESET` y `PAL` de `tools/nivel.py`.
- **Forma de jefe:** añádela a `BOSS_FORMS` y a su `case` en `bossSprite`; respeta los pies en la fila 57.
