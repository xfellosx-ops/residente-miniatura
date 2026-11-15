# EL RESIDENTE MINIATURA — Subnivel 9-5: NEFRITIS LÚPICA
## "El Defensor Corrompido" — guion ampliado (v2, exploración por zonas)

> Documento de diseño narrativo. Español (México). Terminología internacional en inglés cuando es estándar.
> Fuentes verificadas al 14-nov-2026 (ver §15). Lo que no está verificado se marca **[VERIFICAR]**.

---

## 0. CÓMO LEER ESTE GUION

| Símbolo | Significado |
|---|---|
| ▸ | Un **cuadro de diálogo** (máx. 2–3 líneas cortas; la barra `/` = salto de línea) |
| **[PREGUNTA: tema / competencia]** | Interacción obligatoria tipo examen. ✔ = respuesta correcta |
| **[ELECCIÓN]** | Decisión narrativa o clínica sin castigo fuerte |
| **[MINIJUEGO: tipo]** | Mecánica arcade |
| **[OBJETO]** / **[ESCUDO]** | Se agrega al inventario (los escudos = ensayos clínicos) |
| 🔁 | Repetición deliberada de un concepto clave (ver tabla §13) |
| **TARJETA DE DATO** | Cierre de zona; se guarda en el Nefrodex |

**Regla de ritmo:** nunca más de 4 cuadros seguidos sin interacción. Los diálogos largos de mentores se parten con preguntas de "¿Por qué?".

**Competencias (etiquetas del banco):** FISIO (fisiopatología) · DX (diagnóstico) · HISTO (patología) · TX (tratamiento) · EVID (ensayos) · SEG (seguimiento/complicaciones) · ESP (poblaciones especiales).

---

## 1. PERSONAJES DEL SUBNIVEL

### 1.1 Recurrentes
| Personaje | Sprite (16×16 / 32×32) | Personalidad | Muletilla |
|---|---|---|---|
| **Residente (jugador)** | Bata corta, estetoscopio gigante a escala, gorra con logo del Consejo | Bueno en clínica; a veces se queda dormido (mecánica: barra de "Vigilia", ver §2.4) | — |
| **Dr. J.** (radio) | Retrato pixel en esquina: lentes, bigote, taza que dice "URATO" | Práctico, directo, chistes de ácido úrico; culpa secreta | "Al grano… y al cristal de urato." |
| **Sabio Brenn** | Anciano translúcido, túnica con patrón de nefronas; aparece en **Portales de Escala** (vórtice azul) | Calmado, habla en parábolas de hiperfiltración | "Cuando muchos caen, los que quedan trabajan de más… y también caen." |
| **Dra. Valeria Montes "Flashcard"** (rival) | Coleta, tarjetas de estudio volando alrededor, audífonos | Memoriza todo, entiende poco; competitiva pero no mala | "¡Me lo sé de memoria! …¿por qué preguntas *por qué*?" |
| **Los Nefrotóxicos** | Pandilla tipo Team Rocket con gorras de Hemo-Eterna | Cómicos, torpes, se pelean entre ellos | "¡Por cada nefrona caída, Hemo-Eterna gana una silla de diálisis!" |
| ‑ Don Ibuprofeno (AINE) | Pastilla naranja con bigote | Vendedor ambulante | "¿Le duele? ¡Le quito el dolor… y la prostaglandina!" |
| ‑ Yodo Ray (Contraste) | Gota brillante, gafas oscuras | Fotógrafo pretencioso | "¡Sonría para la tomografía!" |
| ‑ Genta Mycin (Aminoglucósido) | Cepillo con corona | Se obsesiona con el borde en cepillo | "Me encanta tu borde en cepillo… me quedo a vivir." |
| ‑ Tacro-Lord (Calcineurínico) | Capa negra, monóculo, aprieta arteriolas aferentes | Villano dramático | "¡Vasoconstricción aferente, muajaja!" |
| **Ing. Perpetuo Diálisis** (director Hemo-Eterna) | Traje gris, ojos con fibrosis | Poseído por **La Esclerosis** | "Todos merecen una silla. Para siempre." |

### 1.2 La paciente
**Sofía R., 24 años.** Estudiante de diseño. Fue a la playa en vacaciones. Sprite en camilla; en el mundo interior su "cielo" cambia de color según su estado (rojo = brote, gris = cronicidad, azul = remisión).

### 1.3 Equipo del jugador (criaturas)
| Criatura | Tipo | Línea evolutiva | Movimiento firma | Notas didácticas |
|---|---|---|---|---|
| **Mac Limpio** (macrófago) | Depurador | Monocito → Macrófago → **Macrófago M2 Eferocítico** | "Eferocitosis" (requiere C1q y MerTK) | Débil si C1q está bloqueado 🔁 |
| **Neutra** (neutrófilo) | Fagocito | Neutrófilo → Neutrófilo veterano | "Fagocitosis"; riesgo de corrupción a **LDG** | Giro en Zona 3 |
| **Bento** (linfocito B) | Humoral | B naïve → B memoria → **Célula plasmática** | "Anticuerpo neutralizante" | Debe mantenerse **tolerante** |
| **Tregúa** (Treg) | Supresor | Treg → Treg FOXP3⁺ → **Guardián IL-2** | "Supresión"; potenciada por objeto IL-2 | Débil sin IL-2 🔁 |
| **MMF-01** (micofenolato, robot) | Antimetabolito | MMF-01 → **MPA-02** (ácido micofenólico activo) | "Bloqueo IMPDH" | Golpea linfocitos y mesangio proliferantes |
| **Paraguas HCQ** (hidroxicloroquina) | Endosomal | Paraguas → **Paraguas Lisosomal** | "Alcalinizar endosoma" (apaga TLR7/9) | Va en TODOS los equipos 🔁 |

**Desbloqueables en 9-5:** Voclosporina (Podoprotector, Zona 7), Beli (Anti-BAFF, Zona 4), Obi (Depletor anti-CD20 tipo II, Zona 10), Ciclón (ciclofosfamida, Alquilante, Zona 5), Ani (anti-IFNAR, **bloqueada**: "aún no aprobada para NL", Zona 4).

### 1.4 Tabla de tipos (simplificada)
| Tipo atacante | Súper eficaz contra | Poco eficaz contra | Lección |
|---|---|---|---|
| Endosomal (HCQ) | pDC, TLR7/9, sensores | Complemento, cicatriz | HCQ apaga sensores, no revierte daño |
| Anti-citocina (Beli) | BAFF, B transicionales autorreactivos | Células plasmáticas de vida larga | BAFF mantiene vivos a los B, no a todas las plasmáticas |
| Depletor (Obi) | Linfocito B CD20⁺ | **Plasmablasto / plasmática (CD20⁻)** | Por eso el anti-ADNdc puede persistir |
| Antimetabolito (MMF) | Linfocitos y mesangio que proliferan | Células en reposo, fibrosis | Las células T/B dependen de síntesis *de novo* de purinas |
| Alquilante (Ciclón) | Todo lo que se divide | — (pero gasta "fertilidad") | Toxicidad gonadal dependiente de dosis |
| Podoprotector (Voclo) | Podocito dañado, Tfh/Th (NFAT) | Fibrosis | Doble mecanismo: T y sinaptopodina |
| Supresor (Treg) | Tfh, Th17 | Inmunocomplejos ya depositados | — |
| Depurador (Mac) | Nucleosomas, cuerpos apoptóticos | Anti-C1q | Sin C1q no hay limpieza |
| **Nadie** | **Semiluna fibrosa, fibrosis intersticial** | — | Lo crónico no responde: **tiempo = nefronas** 🔁 |

---

## 2. MECÁNICAS NUEVAS DEL SUBNIVEL

### 2.1 Exploración con flechas
- Cada zona es un mapa de ~3–4 pantallas Game Boy (160×144) conectadas. Hierba alta = encuentros salvajes (XP opcional).
- **Puertas-llave**: se abren con un concepto (objeto) obtenido en la zona.
- **Portales de Escala** (vórtices azules): cambian la escala (macro → micro → molecular) y traen al Sabio Brenn.

### 2.2 Combate
- El ataque se elige por **tipo/mecanismo**; acertar la pregunta asociada = golpe crítico.
- Enemigos salvajes: 1 pregunta corta (≤2 líneas) por combate; si fallas, el enemigo "huye" y reaparece más adelante con la **misma pregunta en otra forma** (repetición espaciada).

### 2.3 El cielo de Sofía (barra de riñón)
- Arriba de la pantalla: **TFGe** y **Índice de Cronicidad**. Cada pregunta fallada en zonas renales suma 1 punto de "cronicidad visual" (cosmético hasta la fase 4 del jefe, donde importa).

### 2.4 Barra de Vigilia (accesibilidad)
- Si el jugador no toca nada por 60 s, Dr. J. "suena" por la radio con un chiste corto y una pregunta de 1 línea.
- **Modo lectura lenta:** texto avanza solo con botón; opción de ver el último cuadro otra vez (botón B).
- **Guardado automático** al final de cada cuadro de interacción.

### 2.5 Escudos de ensayo (mnemotecnia de evidencia)
Cada ensayo es un escudo con **forma + número grabado + frase**. Al equiparlo, su frase sale en combate.

| Escudo | Forma pixel | Grabado | Frase mnemotécnica | Dónde se obtiene |
|---|---|---|---|---|
| **Euro-Lupus** | Billete de **500 €** | "500 c/2 sem × 6 = 3 g" | "Un billete de 500, cada quincena, seis veces." | Zona 5 |
| **ALMS** | Dos **almas** gemelas tomadas de la mano | "MMF = CYC (inducción) · MMF > AZA (mantenimiento)" | "En ALMS las almas empatan… y en mantenimiento gana el MMF." | Zona 4 |
| **BLISS-LN** | Escudo azul con abeja "B" | "104 sem · 43 vs 32 %" | "La **B** de BAFF, Belimumab y BLISS: dos años de dicha, **4-3 le gana al 3-2**." | Zona 4 |
| **AURORA 1** | Sol naciente | "52 sem · **41 vs 23** %" | "Aurora = amanecer = **1 año**. Marcador 41-23." | Zona 7 |
| **NOBILITY** | Corona | "104 sem · **41 vs 23** %" | "La nobleza copió el marcador de la Aurora: **gemelos 41-23**." | Zona 10 |
| **REGENCY** | Cetro con "76" | "76 sem · 46 vs 33 %" | "La Regencia dura **76**." | Zona 10 |
| **LUNAR** (roto) | Luna rota | "Rituximab: no superó placebo" | "La luna se rompió… el Obi tipo II sí cortó." | Zona 10 |

---

## 3. MAPA GENERAL DEL SUBNIVEL 9-5

```
[Z1 Urgencias Central] → (miniaturización) → [Z2 Playa Dérmica]
        → [Z3 Pantano de Restos] → [Z4 Bosque Ganglionar ★Centro de recuperación]
        → [Z5 Río Sanguíneo (barco)] → [Z6 Delta Endocapilar ⚡GIRO 1]
        → [Z7 Acantilado Podocitario ⚡GIRO 2] → [Z8 Ruinas de Hematoxilina]
        → [Z9 Cápsula de Bowman] → [Z10 Valle Tubulovascular ⚡GIRO 3 → Arena del Defensor]
        → Nefrodex
```

| Zona | Escala | Concepto eje | Entrenador(es) | Villano | Objeto-llave |
|---|---|---|---|---|---|
| Z1 | Hospital | Caso, sedimento | Urología | — | Radio de Dr. J. |
| Z2 | Tisular | UV, apoptosis, C1q | Dermatología | — | **Llave C1q** |
| Z3 | Molecular | DNasas, cGAS-STING, NET, genética | Reumatología | — | **Linterna Genómica** |
| Z4 | Celular | pDC/IFN, BAFF, Tfh, Treg, GC | Rival (1) | — | **Escudos BLISS-LN, ALMS** |
| Z5 | Sistémica | IC circulantes, FcγR, complemento | Terapia Intensiva | — | **Escudo Euro-Lupus** |
| Z6 | Glomerular | In situ, subendotelial, NET, C | — | AINE + Contraste | **Mapa de Depósitos** |
| Z7 | Ultraestructural | Subepitelial, clase V, podocitopatía | Ginecología | Tacro-Lord | **Escudo AURORA 1** |
| Z8 | Histológica | Biopsia, ISN/RPS, índices | Cirugía, Patología, Rival (2) | — | **Lupa NIH** |
| Z9 | Glomerular | Semilunas | Medicina Interna | — | **Brújula Semilunar** |
| Z10 | Tubulointersticial/vascular | TLS, IFTA, MAT/SAF | Hematología | Genta Mycin | **Escudos NOBILITY/REGENCY** |
| Arena | — | Jefe Lupus (4 fases) | — | La Esclerosis (cameo) | Página Nefrodex |

---

## ZONA 1 — URGENCIAS CENTRAL
**Mapa (pixel art):** Pasillo de urgencias con piso de mosaico verde agua, camillas en fila, reloj que marca 03:12, máquina de café descompuesta, ventanilla de laboratorio con foco parpadeante. Al fondo, cubículo 4 con cortina rosa (Sofía). Puerta lateral con letrero "SÓLO PERSONAL — MINIATURIZACIÓN".
**Ambiente:** Pitidos de monitor en 8 bits, ritmo lento.
**NPC:** Enfermera Lupita (da el caso y una "Torta de guardia" = curación), Sofía (paciente), mamá de Sofía (pregunta humana), Químico Chuy en la ventanilla del laboratorio (da el sedimento).
**Hierba (sala de espera, encuentros opcionales):**
| Enemigo salvaje | Qué representa | Pregunta al vencerlo |
|---|---|---|
| **Mito de Pasillo** | "Si no hay rash, no es lupus renal" | ¿Puede haber NL sin manifestaciones cutáneas? (Sí; la NL puede ser la primera manifestación) |
| **Folleto Viral** | Desinformación en redes | ¿Qué porcentaje aproximado de pacientes con LES desarrolla NL? (~40 %; más en hispanos, afrodescendientes y asiáticos) |
| **Tira Reactiva Tramposa** | Falsos positivos de hematuria (mioglobina) | Hemo ++ en tira sin eritrocitos en microscopio → pensar en mio/hemoglobinuria |

### Guion
▸ **ENFERMERA LUPITA:** Doctor, cubículo 4. / Mujer de 24, se hinchó de las piernas / después de unas vacaciones en la playa.
▸ **SOFÍA:** Me salió una mancha en la cara… / y me duelen las manos. / Pensé que era solo el sol.
▸ **MAMÁ:** ¿Es grave, doctor? / Nunca se enferma.
**[ELECCIÓN]** ¿Qué haces primero? → (A) Explorar la cara ✔ (B) Pedir TAC (C) Dar ibuprofeno.
- Si elige (C): aparece una pastilla naranja con bigote que se ríe y huye. *"¡Nos vemos en el glomérulo!"* (presagio de Don Ibuprofeno).
▸ **TÚ (exploración):** Eritema en "alas de mariposa". / Respeta los surcos nasogenianos. / Edema con fóvea ++.
▸ **QUÍMICO CHUY:** Aquí el sedimento, doc. / Eritrocitos dismórficos… y cilindros eritrocitarios. / Esto no viene de la vejiga.
**[PREGUNTA: localización de la hematuria / DX]** ¿Qué hallazgo urinario es prácticamente patognomónico de origen glomerular?
(A) Eritrocitos isomórficos (B) **Cilindros eritrocitarios ✔** (C) Coágulos (D) Cristales de oxalato
> Retro: el cilindro se forma en el túbulo con proteína de Tamm-Horsfall (uromodulina) atrapando eritrocitos que cruzaron el glomérulo.

▸ **LAB (pantalla):** Cr 1.4 · UPCR 3.2 g/g · C3 ↓ · C4 ↓ / Anti-ADNdc (+).
▸ **DR. J. (radio, crepitando):** ¿Me escuchas? Soy el Dr. J. / Lo que ves es un riñón pidiendo auxilio. / Y no, esta vez no es el ácido úrico. Lamentablemente.
▸ **DR. J.:** Complemento bajo, anti-ADNdc, sedimento activo. / Las tres campanas de la nefritis lúpica. 🔁
**[PREGUNTA: patrón de complemento / DX]** C3 y C4 **ambos** bajos sugieren activación de la vía…
(A) Alterna pura (B) **Clásica (por inmunocomplejos) ✔** (C) De las lectinas exclusivamente
> Retro: la vía clásica consume C4 y C2 antes de C3; la vía alterna aislada baja C3 con C4 normal (p. ej., GN C3).

▸ **DR. J.:** Calculemos su función. / Mujer, 24 años, Cr 1.4…
**[MINIJUEGO: Calculadora relámpago]** Elegir el rango de TFGe (CKD-EPI 2021): (A) >90 (B) 60–89 (C) **45–59 ✔ (~54)** (D) <30.
> Este número se guarda: **TFGe ≈ 54** vuelve en el jefe (decisión de voclosporina, umbral >45). 🔁

### Entrenador: Dr. Bruno Salas — Residente de Urología
- **Sprite:** Cistoscopio al hombro como bazuca, gorro quirúrgico con calaveras.
- **Personalidad:** Seguro de sí mismo; todo es "piedra o tumor". Buena onda, pero literal.
- **Reto:** *"¿Hematuria? ¡Mía! Cistoscopia y a casa, campeón."*
- **Combate (3 preguntas):**
  1. [PREGUNTA: DX] ¿Qué % de acantocitos (G1) en orina orienta a origen glomerular? → **≥5 %** ✔
  2. [PREGUNTA: DX] Proteinuria 3.2 g/g + hematuria dismórfica = ¿cistoscopia urgente? → **No; síndrome nefrítico-nefrótico glomerular** ✔
  3. [PREGUNTA: DX] ¿Qué estudio cambia el manejo en esta paciente? → **Biopsia renal** ✔ 🔁
- **Derrota:** *"¿Acantocitos…? Bueno, el riñón también es urológico… a veces. Nos vemos en la biopsia."*

### Cierre de zona
▸ **DR. J.:** Escucha, residente. Hace años perdí a una paciente así. / No resolví su diagnóstico a tiempo.
▸ **DR. J.:** Por eso inventé esto. / Entra a la sala de miniaturización. / Vamos a verlo desde adentro.
**[ELECCIÓN]** ¿Aceptas la misión? → Sí / "Déjame tomar café primero" (Dr. J.: *"La cafeína sube el urato… bueno, ya, ve."*)
▸ *(Pantalla blanca. Sonido de encogimiento: piu-piu-piu.)*

> **TARJETA DE DATO Z1:** Sedimento activo + C3/C4 bajos + anti-ADNdc = sospecha de NL proliferativa → **la biopsia decide** (no la serología).

---

## ZONA 2 — PLAYA DÉRMICA (piel tras radiación UV)
**Mapa (pixel art):** Paisaje de "playa" donde la arena son **queratinocitos** hexagonales; el sol en la esquina emite rayos UVB morados. Charcos con burbujas ("blebs") brillantes. Palmeras = vasos dérmicos. Al norte, una gran **puerta de piedra con forma de C1q** (ramo de 6 tulipanes) cerrada.
**Ambiente:** Olas en 8 bits; cuando pasa un rayo UV, la pantalla parpadea.
**NPC:** Queratinocito anciano "Don Estrato" (explica apoptosis), Macrófago Patrullero cansado (ex-compañero de Mac Limpio), cangrejo-mascota "Cangre-C1q" (pista de la puerta).
**Hierba (arena alta):**
| Enemigo | Qué es | Movimiento | Pregunta |
|---|---|---|---|
| **Queratinocito Quemado** | Queratinocito apoptótico por UVB | "Bleb explosivo" | ¿Qué autoantígenos se concentran en blebs apoptóticos? (Ro/SSA, nucleosomas) |
| **Bleb Ro** | Vesícula superficial con Ro52/Ro60 | "Exposición" | Anti-Ro se asocia a… (LES cutáneo subagudo, lupus neonatal) |
| **IFN-κ Chispa** | Interferón kappa de queratinocitos | "Preparar terreno" | ¿Qué hace IFN-κ en piel lúpica? (amplifica sensibilidad a IFN y fotosensibilidad) |
| **Macrófago Perezoso** | Fagocito con eferocitosis deficiente | "Siesta" | ¿Qué pasa si no se retira a tiempo un cuerpo apoptótico? (necrosis secundaria → liberación de nucleosomas) |

### Guion
▸ **TÚ:** ¿Arena? No… son células. / Miles de queratinocitos.
▸ **DON ESTRATO:** Bienvenido, chiquito. / El sol de la playa nos quemó el ADN. / Muchos decidimos morir con orden: apoptosis.
▸ **DON ESTRATO:** Al morir, sacamos burbujas a la superficie. / Dentro van nuestros secretos: / nucleosomas, Ro, ARN.
**[PREGUNTA: FISIO]** ¿Por qué la apoptosis "ordenada" no debería causar inflamación?
(A) Porque no libera contenido si se retira a tiempo ✔ (B) Porque activa Treg siempre (C) Porque no expone antígenos
> Retro: la apoptosis expone señales "cómeme" (fosfatidilserina) y se depura en silencio. **El problema del lupus no es morir: es no limpiar.** 🔁

▸ **MACRÓFAGO PATRULLERO:** Mac… ¿eres tú? / Ya no doy abasto. / Sin C1q no veo bien a los muertos.
▸ **MAC LIMPIO:** C1q es como mis lentes. / Marca al cuerpo apoptótico / para que lo coma sin escándalo.
▸ **SABIO BRENN (Portal de Escala):** Hijo, escucha esta parábola. / Cuando el barrendero no barre, / la basura se vuelve bandera para el ejército.
**[PREGUNTA: FISIO / genética]** La deficiencia homocigota de **C1q** produce LES en aproximadamente…
(A) 10 % (B) 40 % (C) **>90 % ✔** (D) 0 %
> Retro: es el factor monogénico más penetrante. C4 (~75 %) y C2 (~10–30 %) le siguen. El orden de riesgo sigue al de la cascada: **C1q > C4 > C2**. 🔁

▸ **CANGRE-C1q:** ¡Clic-clac! La puerta tiene seis tulipanes. / Tráeme la cabeza globular / y el tallo de colágeno.
**[MINIJUEGO: Ensamblar C1q]** Arrastrar 6 cabezas globulares (C1qA/B/C) al tallo colagenoso. Al completar: **[OBJETO] Llave C1q**.
▸ **DON ESTRATO:** Otra cosa, doctorcito. / La luz UV también llama neutrófilos. / Vi a algunos irse… hacia el riñón.
**[PREGUNTA: FISIO]** Exposición aguda a UV en modelos murinos se asoció con…
(A) Nada renal (B) **Inflamación renal mediada por neutrófilos que migran de piel a riñón ✔** (C) Solo quemadura
> Retro: puente piel→riñón (Skopelja-Gardner, PNAS 2021). Explica brotes renales tras exposición solar. Por eso **fotoprotección = nefroprotección**.

### Entrenadora: Dra. Pía Lumen — Residente de Dermatología
- **Sprite:** Gafas de sol enormes, sombrero de ala ancha, botella de bloqueador SPF 100 como espada.
- **Personalidad:** Influencer; habla con muletillas ("mi ciela"); en el fondo sabe mucho de piel.
- **Reto:** *"¿Lupus? Eso es rosácea con filtro de playa, mi ciela. ¡Pelea!"*
- **Combate:**
  1. [PREGUNTA: DX] Eritema malar que **respeta** surcos nasogenianos → ¿LES agudo o rosácea? → **LES cutáneo agudo** ✔
  2. [PREGUNTA: FISIO] ¿Qué célula produce IFN tipo I en piel lúpica además de pDC? → **Queratinocitos (IFN-κ)** ✔
  3. [PREGUNTA: TX] ¿Qué fármaco reduce brotes cutáneos **y** renales y se da a casi todos? → **Hidroxicloroquina** ✔ 🔁 → **Paraguas HCQ** sube de nivel.
- **Derrota:** *"Okey, okey… respeta los surcos nasogenianos y yo te respeto a ti. ¡Ponte bloqueador!"* (Entrega **[OBJETO] Bloqueador SPF**: +defensa contra rayos UV en esta zona.)

### Cierre
▸ Usas la **Llave C1q**. La puerta se abre con un acorde. / Detrás: un pantano oscuro.
▸ **DR. J.:** Recuerda esa llave. / Vas a volver a ver a C1q… / y no siempre como amigo.

> **TARJETA DE DATO Z2:** UV → apoptosis → blebs con autoantígenos. Si C1q/eferocitosis fallan → necrosis secundaria → autoantígenos visibles. **C1q > C4 > C2** en riesgo monogénico.

---

## ZONA 3 — PANTANO DE RESTOS (depuración fallida y sensores de ácidos nucleicos)
**Mapa (pixel art):** Ciénaga morada con "troncos" de cromatina flotante; nucleosomas como boyas (bola de histonas envuelta en cuerda de ADN). Al centro, la **Biblioteca Genómica** (torre con estantes de doble hélice). Al este, telarañas brillantes (NET). Tijeras gigantes oxidadas en el suelo (DNasas descompuestas). Alarmas rojas pegadas a las paredes celulares (sensores cGAS).
**Ambiente:** Burbujeo lento, eco de goteo.
**NPC:** **Tijera DNASE1L3** (oxidada, triste), **Exonucleasa TREX1** (bibliotecaria nerviosa), **Alarma cGAS** (grita "¡ADN fuera de lugar!"), Neutrófilo Flotante (tentador de Neutra).
**Hierba (lirio de pantano):**
| Enemigo | Qué es | Movimiento | Pregunta |
|---|---|---|---|
| **Nucleosoma Huérfano** | Cromatina libre por necrosis secundaria | "Rodar" | ¿Qué parte del nucleosoma es catiónica? (histonas) 🔁 |
| **Micropartícula Cargada** | Vesícula apoptótica con ADN | "Escudo membranoso" | ¿Qué DNasa degrada ADN dentro de micropartículas? (DNASE1L3) |
| **ADN Citosólico Fugitivo** | ADN en citosol | "Disparar alarma" | ¿Qué sensor citosólico detecta ADN? (cGAS → cGAMP → STING) |
| **NET Pegajosa** | Trampa extracelular de neutrófilo | "Red" (inmoviliza 1 turno) | ¿Qué protege las NET de degradarse en LES? (inhibidores de DNasa1 y anticuerpos anti-NET) |
| **Granulocito de Baja Densidad (LDG)** | Neutrófilo proinflamatorio | "NETosis" | ¿Qué liberan de forma exagerada? (NET con ADN mitocondrial oxidado; IFN-I) |

### Guion
▸ **TÚ:** Esto huele a basura nuclear. / Restos de células que nadie limpió.
▸ **TIJERA DNASE1L3:** Yo cortaba el ADN de las micropartículas… / pero en algunas familias nací rota. / Esos niños tienen lupus temprano, con riñón.
**[PREGUNTA: genética / FISIO]** Variantes de pérdida de función en **DNASE1L3** causan…
(A) Sólo urticaria (B) **LES familial de inicio temprano con anti-ADNdc y nefritis ✔** (C) Gota
> Retro: Al-Mayouf, Nat Genet 2011. Mnemotecnia: **"L3 = Lupus 3 veces: temprano, familiar, renal".**

▸ **TREX1 (bibliotecaria):** Shhh. Yo borro ADN del citosol. / Si fallo, cGAS cree que hay un virus / y prende todas las alarmas.
▸ **ALARMA cGAS:** ¡ADN EN EL CITOSOL! / ¡Fabricando cGAMP! / ¡STING, avisa a IRF3! ¡INTERFERÓN!
**[MINIJUEGO: Cadena de alarma]** Ordenar: ADN citosólico → **cGAS → cGAMP → STING → TBK1 → IRF3 → IFN-β**. (5 fichas, tiempo generoso, sin penalidad por lento.)
> Al completar: **[OBJETO] Linterna Genómica** (ilumina la Biblioteca).

▸ **SABIO BRENN:** El guardián que no distingue / entre enemigo y hermano / termina disparando a su propia casa.
▸ **SABIO BRENN:** Los sensores nacieron para cazar virus. / En el lupus, el ADN propio se disfraza de virus. 🔁 *(semilla del giro final: el "Defensor corrompido")*

### La Biblioteca Genómica (sala interior)
Estantes con libros-gen. Al tocarlos, la Linterna muestra una ficha (máx. 2 líneas):
| Libro | Ficha |
|---|---|
| **C1Q / C4 / C2** | Depuración de apoptóticos. C1q >90 % penetrancia. 🔁 |
| **TREX1** | Exonucleasa citosólica. Falla → cGAS-STING → IFN. Lupus sabañón familiar, Aicardi-Goutières. |
| **DNASE1L3** | DNasa secretada; corta ADN de micropartículas. LES pediátrico con NL. |
| **TLR7** | En el cromosoma **X**; escapa a la inactivación del X en algunas células → más TLR7 en mujeres. Ganancia de función **Y264H** causa LES (Brown, Nature 2022). |
| **IRF5** | Factor de transcripción río abajo de TLR7/9 → IFN-I. Haplotipo de riesgo clásico. |
| **STAT4** | Señal de IFN-I/IL-12; asociado a NL grave y anti-ADNdc. |
| **PTPN22 (R620W)** | Fosfatasa que ajusta umbral de TCR/BCR; falla la eliminación de autorreactivos. |
| **ITGAM / FCGR** | CD11b y receptores Fcγ: depuran inmunocomplejos peor. (Lo verás en Zona 5.) |
| **APOL1** | En ascendencia africana: riesgo de progresión a ERC terminal en NL. |

**[PREGUNTA: genética]** ¿Por qué el LES es ~9 veces más frecuente en mujeres? Elige la explicación **genética** más directa.
(A) Estrógenos solamente (B) **TLR7 en X escapa a la inactivación → mayor dosis de TLR7 ✔** (C) PTPN22 en el X
> Retro: Souyris, Sci Immunol 2018. Los estrógenos también cuentan, pero la pregunta es genética. 🔁 (TLR7 reaparece en Z4, Z10 y jefe.)

### Giro menor — La tentación de Neutra
▸ **NEUTRÓFILO FLOTANTE:** Neutra, ¿por qué tan pesada? / Sé ligera como yo. Baja densidad. / Escupe tu ADN y sé libre.
▸ **NEUTRA:** Se siente… poderoso. / Mi núcleo quiere salir.
**[ELECCIÓN]** (A) "¡Neutra, no! Las NET alimentan a las pDC" ✔ (B) "Hazlo, necesitamos poder".
- (B): Neutra se vuelve **LDG** por 3 combates (ataca fuerte pero genera "IFN" que cura al enemigo). Lección por mecánica.
- (A): Neutra resiste y aprende "Fagocitosis limpia".
▸ **DR. J.:** Bien. Las NET son ADN + histonas + LL-37. / Las pDC se las comen por FcγRIIA / y gritan interferón. Lo verás en el ganglio. 🔁

### Entrenador: Dr. Rafael Criterio — Residente de Reumatología
- **Sprite:** Laptop con Excel abierto, chaleco con 22 bolsillos (uno por criterio).
- **Personalidad:** Amigo-rival; todo lo puntúa; respeta al nefrólogo pero quiere "su" paciente.
- **Reto:** *"Sin puntaje no hay lupus. ¿Cuántos puntos tiene tu paciente, eh?"*
- **Combate:**
  1. [PREGUNTA: DX] Criterio de entrada EULAR/ACR 2019 → **ANA ≥1:80** ✔
  2. [PREGUNTA: DX] ¿Cuánto vale una biopsia clase III o IV? → **10 puntos (el máximo; basta sola con ANA)** ✔ ; clase II o V → 8; proteinuria >0.5 g/24 h → 4.
  3. [PREGUNTA: FISIO] ¿Qué autoanticuerpo es más sensible que anti-ADNdc para NL activa? → **Anti-nucleosoma** ✔ (y anti-C1q tiene alto VPN) 🔁
- **Derrota:** *"10 puntos por biopsia… me ganaste en mi propio Excel. Te debo un café descafeinado."*

> **TARJETA DE DATO Z3:** Fallas en limpiar ADN (DNASE1L3, TREX1, C1q) + sensores que lo confunden con virus (TLR7/9, cGAS-STING) = **firma de interferón tipo I**.

---

## ZONA 4 — BOSQUE GANGLIONAR (★ Centro de recuperación)
**Mapa (pixel art):** Bosque con árboles en forma de folículos (copa redonda = folículo B, claro central luminoso = **centro germinal**). Senderos de vénulas de endotelio alto. Al oeste, un campamento de pDC con antenas de radar (TLR). Al este, una "fábrica" de plasmablastos con chimeneas. Cabaña de madera = **Centro de Recuperación** (cura al equipo; enfermera **Dra. IL-2** con delantal).
**Ambiente:** Grillos, campanitas al pasar por el centro germinal.
**NPC:** Dra. IL-2 (cura y explica Treg), **Macrófago de Cuerpo Tingible** (casi extinto), **Célula Dendrítica Folicular** (FDC) cubierta de basura apoptótica, vendedor de escudos "Don Ensayo".
**Hierba (helechos):**
| Enemigo | Qué es | Movimiento | Pregunta |
|---|---|---|---|
| **pDC Paranoica** | Célula dendrítica plasmacitoide | "Grito de IFN-α" (sube ataque a todos los enemigos) | ¿Por qué receptor internaliza inmunocomplejos con ADN/ARN? (FcγRIIA/CD32) |
| **BAFF Inflado** | Factor activador de células B | "Salvavidas" (revive B autorreactivos) | ¿Qué B depende más de BAFF para sobrevivir? (B transicionales/naïve autorreactivos) |
| **Tfh Influyente** | T helper folicular | "IL-21 + CD40L" | ¿Qué marcador define Tfh? (CXCR5, PD-1, ICOS; IL-21) |
| **Linfocito B Autorreactivo** | B anti-ADN | "Afinar" | ¿Qué proceso del centro germinal sube la afinidad? (hipermutación somática) |
| **Atajo ABC/DN2** | B extrafolicular CD11c⁺ T-bet⁺ | "Atajo" (salta el folículo) | ¿Qué receptor impulsa esta vía? (TLR7, con IFN-γ/IL-21) 🔁 |
| **Treg Desvelada** | Treg agotada | "Bostezo" (no suprime) | ¿Qué citocina le falta? (IL-2; las T del LES producen poca IL-2) |

### Guion
▸ **DRA. IL-2:** ¡Pásale, mijo! Aquí se cura el equipo. / Pero a mis Treg les falta comida… / y la comida soy yo.
▸ **DRA. IL-2:** Las T del lupus casi no me producen. / Sin IL-2, la Treg se desvela / y deja de frenar a los demás.
**[PREGUNTA: FISIO]** ¿Por qué hay ensayos con **IL-2 a dosis baja** en LES?
(A) Para activar T efectoras (B) **Para expandir Treg selectivamente ✔** (C) Para bloquear BAFF
> Retro: Treg expresan CD25 de alta afinidad; dosis bajas las favorecen. En investigación. → **Tregúa evoluciona a Treg FOXP3⁺**.

▸ *(Llegas al campamento pDC. Todas tienen antenas apuntando a ti.)*
▸ **pDC PARANOICA:** ¡Ácido nucleico! ¡Virus! / ¿Ves esa NET? ¿Ese inmunocomplejo? / ¡Me lo como por CD32 y GRITO!
▸ **SABIO BRENN:** Una sola pDC hace / hasta mil veces más interferón que otra célula. / Un solo grito despierta a todo el bosque.
**[MINIJUEGO: Ordenar la cascada]** (de la versión original, ampliado) Ordenar 6 fichas:
**Inmunocomplejo con ADN/ARN → FcγRIIA (CD32) → endosoma → TLR7 (ARN) / TLR9 (ADN) → MyD88-IRF7/IRF5 → IFN-α**
> Al terminar, **Paraguas HCQ** aparece: *"¡Yo subo el pH del endosoma! Sin acidez, TLR7/9 no se activan."* 🔁

**[PREGUNTA: FISIO / TX]** ¿Qué hace el interferón tipo I en este bosque? Elige **dos**:
(A) **Madura DC y presenta autoantígenos ✔** (B) Inhibe BAFF (C) **Sube BAFF en células mieloides y empuja B → plasmablasto ✔** (D) Activa Treg
> Retro: IFN-I es el "director de orquesta". La **firma de IFN** está en la mayoría de adultos con LES.

▸ **DON ENSAYO (vendedor):** ¡Lleve su escudo, lleve su escudo! / Hoy tengo uno contra el BAFF Inflado.
▸ **BELI** (criatura desbloqueable, abeja azul): ¡Bzzz! Soy **Beli**mumab. / Atrapo al BAFF soluble. / Sin BAFF, los B autorreactivos no sobreviven.
**[ESCUDO] BLISS-LN** → *"La **B** de BAFF, Belimumab y BLISS. Dos años de dicha (104 semanas): **4-3 le gana al 3-2**."*
> Dato: respuesta renal de eficacia primaria **43 % vs 32 %** a 104 sem, añadido a MMF o CYC dosis baja (Furie, NEJM 2020).

▸ **DON ENSAYO:** Y este, de oferta: dos almas gemelas. / Micofenolato y ciclofosfamida… / empatan.
**[ESCUDO] ALMS** → *"En ALMS las **almas** empatan en inducción (MMF = CYC IV)… y en mantenimiento gana MMF sobre azatioprina."*
> Dato: inducción, respuesta 56 % MMF vs 53 % CYC a 24 sem (Appel, JASN 2009); mantenimiento, falla 16 % vs 32 % (Dooley, NEJM 2011). En el subanálisis, hispanos y afrodescendientes respondieron mejor a MMF. 🔁 (Sofía es mexicana.)

▸ **MMF-01 (robot):** BIP. Bloqueo IMPDH. / Los linfocitos fabrican guanina *de novo*. / Sin guanina, no proliferan. BIP.

### Centro germinal (sub-área)
▸ **FDC (cubierta de basura):** Me llenaron de cuerpos apoptóticos. / Los macrófagos de cuerpo tingible / ya casi no vienen. 🔁
▸ **MACRÓFAGO DE CUERPO TINGIBLE:** Soy el último. / Si no limpio aquí, los B ven núcleos todo el día / y aprenden a odiarlos.
**[PREGUNTA: FISIO]** El anti-ADNdc patogénico típico es…
(A) IgM de baja afinidad (B) **IgG de alta afinidad, con cambio de isotipo y mutación somática ✔** (C) IgA secretora
> Retro: necesita ayuda Tfh (IL-21, CD40L). IgG1/IgG3 **fijan complemento** — esto importará en el glomérulo. 🔁

### Entrenador: RIVAL — Dra. Valeria Montes "Flashcard" (combate 1)
- **Sprite:** Coleta, tarjetas girando, sudadera "Tengo 3 000 flashcards".
- **Personalidad:** Rápida, memoriza listas; se frustra con "por qués".
- **Reto:** *"¡Me sé los 9 genes del lupus en orden alfabético! ¿Tú?"*
- **Equipo:** Plasmablasto Nivel 20, BAFF Inflado Nivel 18.
- **Combate:**
  1. [PREGUNTA: FISIO] (Ella) "BAFF se une a BAFF-R, TACI y BCMA". (Tú) ¿Y APRIL? → **Sólo a TACI y BCMA (no a BAFF-R)** ✔
  2. [PREGUNTA: TX] ¿Por qué el anti-CD20 no elimina a las células plasmáticas de vida larga? → **Son CD20 negativas** ✔ 🔁 (Plasmablasto rival resiste el ataque de Obi si lo intentas — mecánica didáctica.)
  3. [PREGUNTA: TX] ¿Qué escudo te protege del BAFF? → **BLISS-LN (belimumab)** ✔ 🔁
- **Derrota:** *"¡Me lo sabía! Pero… ¿por qué las plasmáticas no tienen CD20? ¡No viene en mi tarjeta!"* → se va furiosa a las Ruinas.

### Portal de Escala — Brenn
▸ **SABIO BRENN:** Hay atajos fuera del bosque. / Algunos B no esperan al centro germinal / y salen por la vía extrafolicular, empujados por TLR7.
▸ **SABIO BRENN:** Hay otro hermano, Ani. / Bloquea la puerta del interferón (IFNAR). / Pero aún duerme para el riñón.
**[OBJETO] Ani (bloqueada)** → Nefrodex: *"Anifrolumab: aprobado en LES; en NL, fase 2 TULIP-LN no alcanzó el objetivo primario; fase 3 en curso [VERIFICAR resultado al jugar]."*

> **TARJETA DE DATO Z4:** pDC + TLR7/9 → IFN-I → BAFF ↑ y Tfh ↑ → centro germinal → **IgG anti-ADNdc de alta afinidad**. Treg fallan por **falta de IL-2**.

---

## ZONA 5 — RÍO SANGUÍNEO (persecución en barco)
**Mapa (pixel art):** Río rojo con corriente hacia la derecha; eritrocitos como balsas, plaquetas como piedritas. Inmunocomplejos de tres tamaños: **chiquitos** (canicas), **medianos** (balones), **grandotes** (racimos de uvas). En las orillas, "muelles" de macrófagos del bazo con receptores Fc como grúas. Faro en la desembocadura con letrero "GLOMÉRULO →".
**Ambiente:** Música de persecución, tempo medio.
**NPC:** Capitán Eritrocito (dueño del barco), Grúa FcγR del bazo (pistas), Marinero C3 (consumido, delgado).
**Hierba (remolinos):**
| Enemigo | Qué es | Movimiento | Pregunta |
|---|---|---|---|
| **Inmunocomplejo Errante (grandote)** | IC grande, alta avidez | "Atascar" | ¿Dónde tiende a depositarse? (mesangio/subendotelial) 🔁 |
| **Inmunocomplejo Errante (chiquito)** | IC pequeño/catiónico | "Colarse" | ¿Puede cruzar la MBG? (sí → subepitelial) 🔁 |
| **Convertasa Desbocada** | C3 convertasa (C4b2a) | "Consumir" | ¿Qué baja primero en vía clásica: C4 o C3? (C4 suele bajar primero) |
| **FcγR Torpe** | Variante de baja afinidad (FCGR3A-F158, FCGR2A-R131) | "Soltar" | ¿Qué efecto tiene? (depuración esplénica deficiente de IC) |
| **Plasmablasto Turista** | Plasmablasto circulante | "Disparo IgG" | ¿Se correlaciona con actividad? (sí, sube en brotes) |

### Guion
▸ **CAPITÁN ERITROCITO:** ¡Súbete! Llevo 120 días en este río. / Los inmunocomplejos van al riñón. / Si no los atrapan en el bazo, llegan.
▸ **GRÚA FcγR:** Yo los pescaba con mis ganchos Fc… / pero mis ganchos nacieron flojos. / Y el C3 que los marcaba ya se gastó.
▸ **MARINERO C3 (delgado):** Me usaron para cubrir complejos. / Por eso estoy bajo en los labs. / Igual mi primo C4. 🔁
**[PREGUNTA: FISIO]** El complemento en NL activa está bajo principalmente por…
(A) Falta de síntesis hepática (B) **Consumo por inmunocomplejos (vía clásica) ✔** (C) Pérdida urinaria
> Retro: por eso **C3/C4 que se normalizan** son buen signo de respuesta. 🔁 (Vuelve en el jefe, fase 4.)

**[MINIJUEGO: Esquivar y clasificar]** (versión ampliada) El barco esquiva inmunocomplejos; con botón A se "etiqueta" cada uno con su destino:
| IC | Destino correcto |
|---|---|
| Grandote, alta avidez, aniónico/neutro | **Subendotelial / mesangial** |
| Mediano, cantidad moderada | **Mesangial** |
| Chiquito, catiónico o baja avidez | **Subepitelial** (cruza la MBG) |
> Retro al final (Brenn): *"No sólo importa el tamaño. Importa la carga, la avidez y si el antígeno ya estaba sembrado en el riñón."* (**Presagio del GIRO 1.**) 🔁

### Entrenador: Dr. Maximiliano "Max" Presor — Residente de Terapia Intensiva
- **Sprite:** Ojeras profundas, tres cafés en la mano, catéter central como látigo.
- **Personalidad:** Hiperactivo, no duerme, todo lo arregla "con noradrenalina y fe". Tierno en el fondo.
- **Reto:** *"¿Fiebre, PCR alta y creatinina subiendo? ¡Sepsis! Cultivos, antibiótico y a otra cosa."*
- **Combate:**
  1. [PREGUNTA: DX] En LES con fiebre, ¿qué sugiere más **infección** que brote? → **PCR muy elevada** ✔ (en brote suele estar normal o poco elevada, salvo serositis)
  2. [PREGUNTA: DX] C3/C4 bajos + anti-ADNdc ↑ + sedimento activo → → **Brote lúpico** ✔ 🔁
  3. [PREGUNTA: TX] Paciente con NL grave y ciclofosfamida; ¿qué régimen usa **3 g totales**? → **Euro-Lupus (500 mg c/2 sem × 6)** ✔
- **Derrota:** *"Ok, ok… no todo es sepsis. ¡Pero sí todo es café! Toma, te regalo esto."* → **[ESCUDO] Euro-Lupus** (billete de 500 €).
▸ **CICLÓN (criatura desbloqueable):** Soy ciclofosfamida. Fuerte. / Pero cada golpe me cobra fertilidad. / Úsame en dosis Euro-Lupus.
**[PREGUNTA: EVID]** En Euro-Lupus, la dosis baja comparada con la alta fue…
(A) Inferior (B) **Igual de eficaz con menos infecciones ✔** (C) Superior en mortalidad
> Mnemotecnia: **"Un billete de 500, cada quincena, seis veces = 3 000 (3 g)."** (Houssiau, Arthritis Rheum 2002.)

### Cierre
▸ **DR. J.:** El faro dice "Glomérulo". / Ahí se decide todo. / Prepárate: los Nefrotóxicos llegaron antes.

> **TARJETA DE DATO Z5:** Destino del IC = **tamaño + carga + avidez + cantidad**. Grandes → subendotelial/mesangial; pequeños/catiónicos → subepitelial. C3/C4 bajos = **consumo**.

---

## ZONA 6 — DELTA ENDOCAPILAR (⚡ GIRO 1)
**Mapa (pixel art):** El río se ramifica en asas capilares (tubos rosas enroscados). Paredes de tres capas visibles: **endotelio fenestrado** (coladera), **MBG** (alfombra gris con hilos de heparán sulfato negativos "–"), **podocitos** (pulpos con pies) arriba. Masas amarillas pegadas bajo el endotelio = depósitos subendoteliales ("**asas de alambre**"). Montículos en el centro = **mesangio**. Neutrófilos atrapados en telarañas.
**Ambiente:** Latido grave (presión capilar); la pantalla vibra un poco.
**NPC:** **Célula Mesangial "Mesa"** (con brazos contráctiles, enojada), **Endotelio Fenestra** (asustada), **Sinaptopodina** (aparece al fondo, presagio de Z7), **C1q** (¡el amigo de la puerta! ahora encadenado).
**Villanos:** **Don Ibuprofeno** (AINE) y **Yodo Ray** (Contraste).
**Hierba (asas):**
| Enemigo | Qué es | Movimiento | Pregunta |
|---|---|---|---|
| **Nucleosoma Anclado** | Nucleosoma pegado a MBG por histonas | "Sembrar" | ¿Qué carga tiene la MBG? (negativa, heparán sulfato) 🔁 |
| **Anti-ADNdc Cruzado** | Anticuerpo con reactividad cruzada | "Mimetismo" | ¿Con qué proteína renal cruza? (α-actinina-4, entre otras) |
| **C5a Sirena** | Anafilatoxina | "Canto" (atrae neutrófilos) | ¿Qué hace C5a? (quimiotaxis y activación de neutrófilos/macrófagos) |
| **NET Pegajosa** (regresa) 🔁 | NET en capilar | "Red" | ¿Qué daño causan las NET en el endotelio? (histonas citotóxicas, exponen autoantígeno) |
| **Anti-C1q Traidor** | Autoanticuerpo contra C1q | "Encadenar" | ¿Qué valor tiene anti-C1q? (asociado a NL activa; alto VPN si negativo) |

### Guion — Llegada
▸ **TÚ:** Aquí están, pegados bajo el endotelio. / Amarillos, gruesos… / como asas de alambre.
▸ **ENDOTELIO FENESTRA:** ¡Ayuda! Están justo debajo de mí. / Tocan la sangre directamente. / Todo lo que pasa los ve.
▸ **SABIO BRENN:** Recuerda: lo **subendotelial** mira al río. / Llama al complemento y a los leucocitos. / Por eso inflama y prolifera. 🔁
**[PREGUNTA: FISIO / HISTO]** ¿Por qué los depósitos **subendoteliales** se asocian a clases III/IV y los **subepiteliales** a clase V?
(A) Por el color (B) **Los subendoteliales están expuestos a la circulación (complemento, FcR, leucocitos); los subepiteliales quedan "detrás" de la MBG ✔** (C) Por el tamaño del glomérulo
> Retro: subepitelial → daño por **MAC (C5b-9) al podocito**, sin influjo celular → patrón membranoso, poca proliferación. 🔁

### Combate villano: Los Nefrotóxicos (doble)
▸ **DON IBUPROFENO:** ¡Señorita Sofía tiene artralgias! / ¡Yo le quito el dolor… / y la prostaglandina aferente!
▸ **YODO RAY:** ¡Y yo le tomo una tomografía / con 120 mL de contraste! ¡Sonría!
▸ **AMBOS:** ¡Por cada nefrona caída, / Hemo-Eterna gana una silla!
**[PREGUNTA: FISIO / SEG]** ¿Por qué el AINE baja la TFG en esta paciente?
(A) Por nefritis intersticial siempre (B) **Inhibe prostaglandinas vasodilatadoras de la aferente; en riñón inflamado y con hipoalbuminemia, la TFG depende de ellas ✔** (C) Por cristaluria
**[PREGUNTA: SEG]** ¿Qué haces con el estudio contrastado no urgente? → **Diferirlo o buscar alternativa; si es necesario, contraste iso/bajo-osmolar, mínima dosis y volemia adecuada** ✔
- **Derrota (cómica):** Don Ibuprofeno: *"¡Me ganó un paracetamol con lentes!"* / Yodo Ray: *"Mi foto salió movida…"* Huyen en globo con logo de Hemo-Eterna.

### ⚡ GIRO 1 — "La invasión venía de adentro"
▸ *(Mientras persigues un inmunocomplejo, ves algo raro: anticuerpos llegando SOLOS, sin antígeno, y pegándose a la MBG.)*
▸ **TÚ:** Espera… estos anticuerpos llegaron vacíos. / El antígeno ya estaba aquí. / ¿Quién lo sembró?
▸ **MESA (célula mesangial):** Nosotros. Sin querer. / Los nucleosomas se pegaron a la MBG / porque las histonas son positivas y ella negativa. 🔁
▸ **MESA:** Y la tijera del riñón, la DNasa1 renal… / se apagó. Nadie corta la cromatina aquí. / Por eso se queda.
**[PREGUNTA: FISIO — punto medio]** ¿Qué describe mejor la formación de depósitos en NL?
(A) Sólo IC circulantes que "caen" (B) Sólo formación in situ (C) **Ambas: IC circulantes + formación in situ sobre nucleosomas "plantados" y autoantígenos renales con reactividad cruzada ✔**
> Retro: la **pérdida selectiva de DNasa1 renal** se asocia a retención de cromatina en MBG en NL membranoproliferativa (Zykova, PLoS One 2010). Algunos anti-ADNdc cruzan con **α-actinina-4** y otros antígenos glomerulares (Deocharan, J Immunol 2002). 🔁

▸ **DR. J. (voz quebrada):** Es lo que no vi aquella vez. / Yo esperaba al enemigo en la puerta… / y ya estaba dentro de la casa.
▸ **C1q (encadenado):** ¡Residente! Soy yo, el de la puerta. / Antes limpiaba. Ahora me usan para encender la cascada… / y los anti-C1q me tienen preso.
**[PREGUNTA: FISIO]** ¿Cómo puede C1q **proteger** del LES y a la vez **dañar** el riñón?
(A) No puede (B) **Su deficiencia impide depurar apoptóticos (riesgo de LES), pero al unirse a IgG1/IgG3 en depósitos inicia la vía clásica y el daño; los anti-C1q amplifican la lesión ✔** (C) Sólo daña
> Paradoja de C1q (3.ª aparición). 🔁

**[MINIJUEGO: Liberar a C1q — Cascada inversa]** Romper eslabones en orden: **C1q → C1r/C1s → C4 → C2 → C3 convertasa → C3b (amplificación por asa alterna) → C5 convertasa → C5a/C5b-9**. Cada eslabón pide nombrar su producto. Al final, C1q queda libre (pero débil) y te entrega **[OBJETO] Mapa de Depósitos**.

▸ **NEUTRA:** Veo a mis hermanos atrapados en sus propias NET. / Lastiman al endotelio con histonas. / Y las NET no se degradan… / ¿por qué?
▸ **SABIO BRENN:** Porque en algunos pacientes hay inhibidores de la DNasa1 / o anticuerpos que cubren la NET. / Lo que no se limpia, se vuelve antígeno. 🔁
> Hakkim, PNAS 2010: la degradación deficiente de NET se asocia a nefritis lúpica.

**[PREGUNTA: FISIO]** ¿Qué hace la célula mesangial ante IC mesangiales + IFN?
(A) Se apoptosa en silencio (B) **Prolifera, produce matriz y citocinas (IL-6, CCL2) vía FcγR y TLR ✔** (C) Se convierte en podocito
> Retro: proliferación mesangial e hipercelularidad endocapilar = blancos de **MMF (antiproliferativo)**. 🔁

> **TARJETA DE DATO Z6:** Depósitos = IC circulantes **+ formación in situ** (nucleosomas catiónicos sobre MBG aniónica; DNasa1 renal apagada; anti-ADNdc cruzado con α-actinina). **Subendotelial = expuesto al río = proliferación.**

---

## ZONA 7 — ACANTILADO PODOCITARIO (⚡ GIRO 2)
**Mapa (pixel art):** Acantilado vertical: la pared es la **MBG** vista de lado; arriba, podocitos como pulpos agarrados con sus pies (procesos podales) a la roca, unidos por "puentes colgantes" (diafragma de hendidura: nefrina). Del lado exterior de la MBG, "percebes" amarillos = **depósitos subepiteliales** (espigas al teñir con plata). Abajo, el mar del espacio urinario lleno de proteína (espuma blanca).
**Ambiente:** Viento fuerte, gaviotas 8-bit.
**NPC:** **Podocito Abuela Nefrina** (maternal, sostiene el puente), **Sinaptopodina** (cuerda que mantiene el esqueleto de actina), **Catepsina L** (glotona, rompe la cuerda), **Primo Voclosporina** (encapuchado, ver giro).
**Villano:** **Tacro-Lord** (Calcineurínico).
**Hierba (líquenes):**
| Enemigo | Qué es | Movimiento | Pregunta |
|---|---|---|---|
| **MAC Taladro** | Complejo de ataque de membrana C5b-9 | "Perforar subletal" | ¿Por qué el MAC subletal no mata al podocito pero lo daña? (estrés, desprendimiento, proteinuria) |
| **Podocito Desprendido** | Podocito en orina (podocituria) | "Caída" | ¿Se regenera el podocito? (muy limitado; células progenitoras parietales) |
| **Catepsina L Glotona** | Proteasa | "Comer sinaptopodina" | ¿Qué la protege? (sinaptopodina fosforilada; la calcineurina la desfosforila) |
| **Percebe Subepitelial** | Depósito subepitelial | "Engrosar" | ¿Qué clase ISN/RPS? (V) 🔁 |
| **Pie Borrado** | Proceso podal fusionado | "Aplanar" | ¿Qué es la podocitopatía lúpica? (borramiento difuso sin depósitos subendoteliales/subepiteliales; patrón ECM/GEFS) |

### Guion
▸ **ABUELA NEFRINA:** Ay, mijo, aquí del otro lado / no llegan los neutrófilos. / Pero sí llega el taladro: el MAC.
▸ **ABUELA NEFRINA:** No nos mata. Nos deja heridas. / Soltamos los pies, el puente se cae… / y se escapa la proteína.
**[PREGUNTA: HISTO / FISIO]** Clase V lúpica: ¿qué esperas en la clínica?
(A) Hematuria macroscópica e IRA rápida (B) **Síndrome nefrótico con sedimento poco activo; riesgo de trombosis ✔** (C) Sólo hematuria aislada
> Retro: puede coexistir con III/IV (**III+V o IV+V**). 🔁

▸ *(Aparece una sombra con capa. Aprieta una arteriola con la mano.)*
▸ **TACRO-LORD:** ¡Muajaja! Soy el Calcineurínico. / Aprieto la aferente y mato nefronas. / ¡Hemo-Eterna me paga por arteriola!
**[PREGUNTA: SEG]** Toxicidad típica crónica de calcineurínicos en riñón:
(A) Necrosis papilar (B) **Vasoconstricción aferente, arteriolopatía hialina, fibrosis en banda ✔** (C) Cristales de urato (Dr. J.: *"¡Ojalá!"*)

### ⚡ GIRO 2 — "El primo bueno"
▸ *(Antes del combate, el encapuchado se interpone.)*
▸ **ENCAPUCHADO:** Basta, primo. / Somos de la misma familia… / pero yo vine a curar.
▸ **TACRO-LORD:** ¡¿Voclosporina?! / ¡Traidora! ¡Deshonras a la calcineurina!
▸ **VOCLOSPORINA:** Bloqueo calcineurina en las T: / sin NFAT, no hay IL-2 ni ayuda a los B. / Y en el podocito… protejo a Sinaptopodina.
**[PREGUNTA: FISIO / TX]** ¿Cómo reduce proteinuria un inhibidor de calcineurina **independiente** de la inmunosupresión?
(A) Aumenta presión intraglomerular (B) **Evita la desfosforilación de sinaptopodina → no la degrada catepsina L → estabiliza el citoesqueleto de actina del podocito ✔** (C) Aumenta albúmina hepática
> Retro: Faul et al., Nat Med 2008 (ciclosporina-sinaptopodina). Mnemotecnia: **"VOC = Voz que Calma al podocito."** 🔁

▸ **VOCLOSPORINA:** Pero ojo: soy de la familia. / Si la TFGe está muy baja, / mi primo despierta en mí.
**[PREGUNTA: TX — KDIGO 2024]** Voclosporina + MPAA en NL III/IV: ¿umbral de TFGe en la guía?
(A) >15 (B) >30 (C) **>45 mL/min/1.73 m² ✔** (D) >90
> Retro: dosis **23.7 mg c/12 h**. Sofía tiene TFGe ≈ 54 → **elegible** (dato de Z1). 🔁

**[ESCUDO] AURORA 1** (sol naciente) → *"Aurora = amanecer = **1 año** (52 semanas). Marcador **41-23**."*
> Respuesta renal completa **41 % vs 23 %** con voclosporina + MMF + esteroide reducido vs MMF + esteroide (Rovin, Lancet 2021). 🔁

### Combate villano: Tacro-Lord
- Debilidad: el jugador debe usar a **Voclosporina** + responder 2 preguntas.
  1. [PREGUNTA: TX] Vigilancia con calcineurínico → **TFGe, potasio, magnesio, PA, glucosa; ajustar si TFGe cae** ✔
  2. [PREGUNTA: FARM] Interacción que sube niveles de calcineurínicos → **inhibidores fuertes de CYP3A4 (p. ej., ketoconazol, claritromicina)** ✔
- **Derrota:** *"¡Me venció mi propia familia! ¡Esto no se queda así! ¡Ma-má!"* (Huye arrastrando su capa.)
- **Voclosporina se une al equipo** (tipo Podoprotector).

### Entrenadora: Dra. Lucía Bravo — Residente de Ginecología y Obstetricia
- **Sprite:** Uniforme quirúrgico morado, doppler fetal como pistola de rayos, gorro con cigüeñas.
- **Personalidad:** Práctica, protectora del "binomio", directa, humor seco.
- **Reto:** *"Tu paciente tiene 24 años y quiere ser mamá algún día. ¿Lo pensaste, nefrólogo?"*
- **Combate:**
  1. [PREGUNTA: ESP] ¿Qué fármaco es **teratogénico** y debe suspenderse antes de concebir? → **Micofenolato (≥6 semanas antes; cambiar a azatioprina)** ✔
  2. [PREGUNTA: ESP] ¿Cuál se **continúa** en el embarazo? → **Hidroxicloroquina** ✔ 🔁 (+ aspirina a dosis baja para prevención de preeclampsia)
  3. [PREGUNTA: ESP] Embarazada de 30 sem con proteinuria nueva e HTA: ¿qué orienta a **brote lúpico** vs preeclampsia? → **Sedimento activo, C3/C4 bajos, anti-ADNdc ↑** ✔ (preeclampsia: sFlt-1/PlGF alto, plaquetas/enzimas hepáticas, sedimento inactivo) 🔁
  4. [PREGUNTA: ESP] Momento ideal para embarazo → **NL inactiva ≥6 meses, sin teratógenos** ✔
- **Derrota:** *"Bien. Pero si le das ciclofosfamida, que sea Euro-Lupus. Protege esos ovarios."* 🔁 (Da **[OBJETO] Consejería Preconcepcional**.)

### Portal de Escala — Brenn
▸ **SABIO BRENN:** Hay podocitos que caen sin depósitos. / Sólo los pies se borran. / Se llama podocitopatía lúpica.
▸ **SABIO BRENN:** Se trata como la enfermedad de cambios mínimos: / glucocorticoide, y responde. / No todo lupus renal es inmunocomplejo en asa.
**[PREGUNTA: TX — KDIGO 2024]** Clase I/II con síndrome nefrótico por podocitopatía lúpica:
(A) Ciclofosfamida (B) **Manejar como cambios mínimos (glucocorticoides; CNI como alternativa) ✔** (C) Sólo iSRAA
**[PREGUNTA: TX — KDIGO 2024]** Clase V pura con proteinuria **no nefrótica**:
(A) Ciclofosfamida (B) **iSRAA, control de PA, HCQ; inmunosupresión si proteinuria nefrótica ✔** (C) Nada 🔁

> **TARJETA DE DATO Z7:** Subepitelial → MAC subletal → podocito herido → clase V nefrótica. **CNI** protege sinaptopodina (antiproteinúrico directo). Voclosporina: **TFGe >45**, AURORA 1 **41-23**.

---

## ZONA 8 — RUINAS DE HEMATOXILINA (histología e ISN/RPS 2018)
**Mapa (pixel art):** Templo maya-pixel teñido en rosa (eosina) y morado (hematoxilina). Columnas con glomérulos tallados. Seis tronos de súbditos (Clases I a VI) en una gran sala. Paredes con murales que cambian según la tinción (PAS magenta, plata negra, tricrómico azul). Entrada: un cráter fresco = **sitio de la biopsia** (Cirugía).
**Ambiente:** Eco de templo, flauta de 8 bits.
**NPC:** **Microscopista Elena** (fantasma amable que da lupas), **Inmunofluorescencia "Full-House"** (cinco faroles encendidos: IgG, IgA, IgM, C3, C1q), **Microscopio Electrónico** (gigante dormido con huellas digitales).
**Hierba (piedras sueltas = Súbditos salvajes):**
| Enemigo | Qué es | Pregunta |
|---|---|---|
| **Súbdito I Invisible** | Clase I | Depósitos mesangiales sólo por IF/ME, ML normal |
| **Súbdito II Mesangial** | Clase II | Hipercelularidad mesangial: **≥4 células** en área mesangial (criterio 2018) |
| **Súbdito III Focal** | Clase III | <50 % de glomérulos con lesión endo/extracapilar |
| **Súbdito IV Difuso** | Clase IV | ≥50 % de glomérulos |
| **Súbdito V Membranoso** | Clase V | Depósitos subepiteliales globales o segmentarios (>50 % de la superficie capilar en >50 % de glomérulos) |
| **Súbdito VI Esclerótico** | Clase VI | ≥90 % de glomérulos con esclerosis global sin actividad residual |
| **Asa de Alambre** | Depósito subendotelial grande | Puntúa en índice de **actividad** (depósitos hialinos) |
| **Trombo Hialino** | IC intraluminal | También actividad |
| **Huella Dactilar** | Depósito con subestructura en ME | Típico de lupus |
| **Inclusión Tubulorreticular** | "Huella del interferón" en endotelio (ME) | ¿Qué la induce? (**IFN-α**) 🔁 |

### Entrenador de entrada: Dr. Rocco Filo — Residente de Cirugía General
- **Sprite:** Casco de minero, pico arqueológico con forma de bisturí, cubrebocas como capa.
- **Personalidad:** Impaciente, quiere "sacar el pedazo y ya"; respeta a quien sabe indicaciones.
- **Reto:** *"¿Biopsia? ¡Yo la saco con los ojos cerrados! …¿Para qué la quieres, eh?"*
- **Combate:**
  1. [PREGUNTA: DX — KDIGO 2024] ¿Biopsia en LES con proteinuria persistente ≥0.5 g/d y/o sedimento activo o TFGe que cae sin otra causa? → **Sí** ✔ 🔁
  2. [PREGUNTA: SEG] Complicación más frecuente de biopsia percutánea → **Sangrado (hematoma perirrenal, hematuria)** ✔; contraindicaciones relativas: HTA no controlada, coagulopatía, riñón único.
  3. [PREGUNTA: HISTO] ¿Qué estudios debe incluir el cilindro? → **ML, IF y ME; idealmente ≥10 glomérulos** ✔
  4. [PREGUNTA: SEG] Indicación de **re-biopsia** → **Falta de respuesta, brote con duda (actividad vs cronicidad), o proteinuria persistente** ✔
- **Derrota:** *"Bueno, el pedazo es tuyo. Pero si sangra, me llamas a mí, ¿eh?"* → Abre la entrada del templo.

### Guion — Sala de los Tronos
▸ **MICROSCOPISTA ELENA:** Bienvenido al templo de la clase. / En 2018 cambiamos reglas. / Ya no decimos A, C ni A/C.
▸ **MICROSCOPISTA ELENA:** Ahora usamos índices: / **Actividad** (máx. 24) y **Cronicidad** (máx. 12). / Y la IV ya no se divide en S y G.
**[PREGUNTA: HISTO — ISN/RPS 2018]** ¿Qué cambio NO es de la revisión 2018?
(A) "Proliferación endocapilar" pasó a "hipercelularidad endocapilar" (B) Se eliminaron IV-S/IV-G (C) Se adoptaron índices NIH modificados (D) **Se eliminó la clase V ✔ (falso: sigue existiendo)**

**[MINIJUEGO: Lupa NIH — Puntuar la biopsia de Sofía]** La pantalla muestra 6 "glomérulos-tarjeta". Por cada lesión, el jugador mueve la lupa y elige el puntaje (0 = ausente; 1 = <25 %; 2 = 25–50 %; 3 = >50 % de glomérulos).

| Índice de ACTIVIDAD (máx. 24) | Peso | Biopsia de Sofía |
|---|---|---|
| Hipercelularidad endocapilar | ×1 | 3 |
| Neutrófilos / cariorrexis | ×1 | 2 |
| **Necrosis fibrinoide** | **×2** | 1 → 2 |
| Depósitos hialinos (asas de alambre / trombos hialinos) | ×1 | 2 |
| **Semilunas celulares/fibrocelulares** | **×2** | 1 → 2 |
| Inflamación intersticial | ×1 | 1 |
| **Total actividad** | | **12/24** |

| Índice de CRONICIDAD (máx. 12) | Peso | Biopsia de Sofía |
|---|---|---|
| Glomeruloesclerosis total (global + segmentaria) | ×1 | 1 |
| Semilunas fibrosas | ×1 | 0 |
| Atrofia tubular | ×1 | 1 |
| Fibrosis intersticial | ×1 | 1 |
| **Total cronicidad** | | **3/12** |

> Mnemotecnia: **"Necrosis y Semilunas pesan doble: N y S, como Norte y Sur del glomérulo."** Actividad = lo que **se puede salvar**; cronicidad = lo que **ya se perdió**. 🔁
> Diagnóstico de Sofía: **Clase IV (+ V segmentaria)**, actividad 12, cronicidad 3.

▸ **INMUNOFLUORESCENCIA FULL-HOUSE:** ¡Cinco faroles! IgG, IgA, IgM, C3 y C1q. / Así brillamos en el lupus. 🔁 (4.ª aparición de C1q)
▸ **MICROSCOPIO ELECTRÓNICO (despertando):** Mmm… veo huellas digitales en los depósitos. / Y en el endotelio… inclusiones tubulorreticulares. / Son las pisadas del interferón. 🔁

### Entrenadora: Dra. Iris Hematoxilina — Residente de Patología
- **Sprite:** Gótica, bata negra, lentes redondos morados, una laminilla como abanico, búho mascota "Eosino".
- **Personalidad:** Nocturna, habla con las laminillas ("¿verdad, preciosa?"), exigente pero justa.
- **Reto:** *"Me dicen que tienes una membranosa. ¿Primaria o lúpica? Las laminillas no mienten… los residentes sí."*
- **Combate (comparativo):**

| Rasgo | Membranosa **lúpica** (V) | Membranosa **primaria** |
|---|---|---|
| IF | **Full-house**, C1q + | IgG, C3; C1q usualmente − |
| Subclase IgG | **IgG1/IgG3** | **IgG4** predominante |
| Depósitos | Subepiteliales **+ mesangiales/subendoteliales** | Sólo subepiteliales |
| ME | **Inclusiones tubulorreticulares** | Ausentes |
| Antígeno | PLA2R usualmente −; **EXT1/EXT2** + frecuente; NCAM1 en algunos | **PLA2R +** (~70–80 %), THSD7A |
| Depósitos extraglomerulares (MBT, vasos) | Frecuentes | Raros |

  1. [PREGUNTA: HISTO] IgG4 dominante, PLA2R +, sin C1q → → **Primaria** ✔
  2. [PREGUNTA: HISTO] Full-house, EXT1/EXT2 +, inclusiones tubulorreticulares → → **Lúpica clase V** ✔ 🔁
  3. [PREGUNTA: HISTO] ¿Qué significa EXT1/EXT2 +? → **Membranosa asociada a enfermedad autoinmune (sobre todo lupus) — Sethi, JASN 2019** ✔
- **Derrota:** *"Bien visto… Eosino, anota: este residente sí ve, no sólo memoriza. Toma, una lupa de verdad."* → **[OBJETO] Lupa NIH** (desbloquea índices en el jefe).

### Entrenadora: RIVAL — Dra. Valeria "Flashcard" (combate 2)
▸ **VALERIA:** ¡Ja! Me sé las seis clases de memoria. / I, II, III, IV, V, VI. / ¡Y el índice de actividad es de 24!
▸ **VALERIA:** …Pero no entiendo por qué / la necrosis vale doble. / ¿Me explicas? No, ¡peleemos!
- **Combate:**
  1. [PREGUNTA: HISTO] ¿Qué lesiones pesan ×2 en actividad? → **Necrosis fibrinoide y semilunas celulares/fibrocelulares** ✔ 🔁
  2. [PREGUNTA: FISIO] ¿Por qué pesan doble? → **Implican ruptura de la pared capilar/MBG y fuga de fibrina: daño agudo grave pero potencialmente reversible si se trata rápido** ✔
  3. [PREGUNTA: SEG] Cronicidad alta (p. ej., ≥ 4–5) ¿qué implica? → **Peor pronóstico renal; menor reversibilidad** ✔ [VERIFICAR punto de corte según cohorte]
- **Derrota:** *"Ok… la necrosis rompe la pared. Por eso pesa. No viene en mis tarjetas… voy a hacer una nueva."* (Primera grieta en su arco: empieza a preguntar "por qué".)

> **TARJETA DE DATO Z8:** ISN/RPS 2018: se fueron A/C y S/G; llegaron **índices** (Actividad 24, Cronicidad 12). **N y S pesan doble.** Full-house + C1q + tubulorreticulares = lúpica.

---

## ZONA 9 — CÁPSULA DE BOWMAN (semilunas)
**Mapa (pixel art):** Una gran esfera hueca (la cápsula) vista desde dentro; el ovillo capilar en el centro como árbol rosa. Por una grieta en un asa (ruptura de MBG) sale "lava" de **fibrina** al espacio de Bowman. Las **células epiteliales parietales (PEC)** de la pared forman una media luna creciente que se cierra sobre el ovillo como marea. Al fondo, una media luna ya de piedra azul (fibrosa = crónica).
**Ambiente:** Música tensa; un reloj de arena en la esquina (si tardas, la semiluna "endurece" de celular → fibrocelular → fibrosa).
**NPC:** **PEC Arrepentida** (prolifera sin querer), **Macrófago Constructor**, **Fibrina** (gotea y habla lento), **Glomérulo Anciano** (con semiluna fibrosa; triste, ya no se puede salvar).
**Hierba (grietas):**
| Enemigo | Qué es | Movimiento | Pregunta |
|---|---|---|---|
| **Célula Parietal Furiosa** | PEC proliferante | "Muro" | ¿Qué estímulo la hace proliferar? (fibrina, citocinas, IL-1/IL-6, PDGF tras ruptura de MBG) |
| **Fibrina Fugitiva** | Fibrinógeno que escapó | "Pegamento" | ¿Qué significa fibrina en Bowman? (ruptura de pared capilar; necrosis) 🔁 |
| **Macrófago Medialuna** | Macrófago en semiluna | "Remodelar" | ¿Hacia dónde evoluciona la semiluna sin tratamiento? (fibrocelular → fibrosa) |
| **Semiluna Fibrosa** | Lesión crónica | "Piedra" (inmune a todo ataque) | ¿Puntúa en actividad o cronicidad? (cronicidad) 🔁 |

### Guion
▸ **TÚ:** La pared se rompió. / La fibrina salió al espacio de Bowman. / Las células de la cápsula están formando un muro.
▸ **PEC ARREPENTIDA:** No quiero aplastar al glomérulo… / pero la fibrina me grita "¡crece!". / Y no puedo parar.
**[PREGUNTA: HISTO — ISN/RPS 2018]** Una semiluna se define por proliferación extracapilar en al menos…
(A) 50 % de la circunferencia (B) **10 % de la circunferencia de la cápsula ✔** (C) Todo el glomérulo
> Retro 2018: **celular** (>75 % células y fibrina), **fibrosa** (>75 % matriz), **fibrocelular** (mezcla). 🔁

▸ **GLOMÉRULO ANCIANO (de piedra):** Yo ya no tengo remedio, muchacho. / Mi semiluna es de piedra. / Salva a los jóvenes, mientras aún son células.
▸ **SABIO BRENN:** Aquí está mi parábola. / Cuando un glomérulo cae, sus hermanos filtran más. / Se cansan… y caen también. Así nace la esclerosis. 🔁
**[PREGUNTA: FISIO — hiperfiltración]** ¿Qué pasa con las nefronas sobrevivientes tras perder nefronas por semilunas fibrosas?
(A) Se atrofian de inmediato (B) **Hiperfiltran (↑ presión y flujo glomerular por nefrona) → hipertrofia → podocito estresado → GEFS secundaria ✔** (C) Se regeneran por completo
> Retro: por eso **iSRAA y control estricto de PA** (y considerar **iSGLT2** como nefroprotección en ERC) aun en remisión inmunológica. 🔁 (Primera mención de La Esclerosis: una sombra gris cruza el fondo.)

**[MINIJUEGO: Contrarreloj semilunar]** El jugador debe responder 3 preguntas rápidas (sin límite estricto en modo lectura lenta) para "congelar" semilunas celulares antes de que se vuelvan fibrosas. Cada acierto = una semiluna vuelve a ser glomérulo sano (animación de alivio).
1. ¿La semiluna celular es reversible? → **Potencialmente sí** ✔
2. ¿La fibrosa? → **No** ✔
3. ¿Qué pesa ×2 en el índice de actividad? → **Semilunas celulares/fibrocelulares y necrosis** ✔ 🔁
> Al completar: **[OBJETO] Brújula Semilunar**.

### Entrenador: Dr. Ernesto Holístico — Residente de Medicina Interna
- **Sprite:** Bata larguísima con 40 plumas, libreta enorme de "diagnósticos diferenciales", estetoscopio doble.
- **Personalidad:** Sabe de todo un poco, habla mucho, ama los diferenciales; buena persona.
- **Reto:** *"Semilunas, ¿eh? Pero ¿descartaste ANCA, anti-MBG, endocarditis, crioglobulinas, IgA, Goodpasture, sífilis…? ¡Pelea!"*
- **Combate:**
  1. [PREGUNTA: DX] GN rápidamente progresiva con IF **lineal** de IgG → **Anti-MBG** ✔
  2. [PREGUNTA: DX] IF **pauci-inmune** con semilunas → **ANCA** ✔; en LES puede haber **superposición ANCA + NL** con más necrosis/semilunas.
  3. [PREGUNTA: DX] IF **granular full-house** con semilunas → **NL clase III/IV con actividad extracapilar** ✔ 🔁
  4. [PREGUNTA: TX] En NL con semilunas y TFGe que cae rápido, ¿qué opción de inducción tiene más experiencia? → **Ciclofosfamida IV (o MPAA), con pulsos de metilprednisolona** ✔ 🔁 (Euro-Lupus)
- **Derrota:** *"Bueno, bueno… ya descartaste todo. Me rindo, pero quiero que conste que lo pensé primero."* (Le da **[OBJETO] Libreta de Diferenciales** = +1 pista en el jefe.)

> **TARJETA DE DATO Z9:** Ruptura capilar → fibrina → PEC proliferan → semiluna (≥10 % circunferencia). **Celular = salvable; fibrosa = perdida.** Nefronas perdidas → hiperfiltración → esclerosis.

---

## ZONA 10 — VALLE TUBULOINTERSTICIAL Y ARTERIOLAS (⚡ GIRO 3) → ARENA DEL DEFENSOR
**Mapa (pixel art):** Valle con túbulos como acueductos de piedra (borde en cepillo = césped en el techo del túbulo proximal). Entre ellos, el intersticio: pueblitos de linfocitos agrupados (**estructuras linfoides terciarias**), fibroblastos tejiendo redes de colágeno gris. Al norte, arteriolas como canales: algunas tapadas con trombos rosas (**MAT**) y "telarañas" de íntima engrosada (**SAF crónico**). Al final, una escalinata hacia la **Arena del Defensor** (coliseo con forma de corte coronal del riñón).
**Ambiente:** Viento seco; cuando pasas por arteriolas trombosadas, la música se vuelve un pulso lento.
**NPC:** **Túbulo Proximal "Don Cepillo"**, **Fibroblasto Tejedor**, **Plaqueta Arrepentida**, **Fantasma de Elisa** (la paciente perdida del Dr. J.).
**Villano:** **Genta Mycin** (Aminoglucósido).
**Hierba (pasto intersticial):**
| Enemigo | Qué es | Movimiento | Pregunta |
|---|---|---|---|
| **Estructura Linfoide Terciaria** | Agregado B/T intrarrenal | "Mini-ganglio" (genera autoanticuerpo localmente) | ¿Por qué importa? (producción local de anticuerpo; asocia peor pronóstico) |
| **Fibroblasto Tejedor** | Miofibroblasto | "Tejer colágeno" | ¿Qué predice mejor el pronóstico renal: lesión glomerular o tubulointersticial? (la TI —fibrosis/atrofia— es predictor fuerte) 🔁 |
| **Plaqueta Coagulina** | Plaqueta activada por antifosfolípidos | "Trombosar" | ¿Qué anticuerpos definen SAF? (anticoagulante lúpico, anticardiolipina, anti-β2GPI) |
| **Esquistocito Filoso** | Eritrocito fragmentado | "Cortar" | ¿Qué indica? (hemólisis microangiopática) |
| **Mini-Genta** | Esbirro aminoglucósido | "Pegarse al cepillo" | ¿Dónde entra al túbulo? (megalina-cubilina, túbulo proximal) |

### Guion — Intersticio
▸ **DON CEPILLO:** Aquí abajo nadie nos mira, doctor. / Todos ven al glomérulo. / Pero cuando nosotros morimos, el riñón no regresa.
▸ **FIBROBLASTO TEJEDOR:** La inflamación me pide que teja. / Si tejo mucho, todo se vuelve gris. / Eso es fibrosis. No la puedo destejer.
**[PREGUNTA: HISTO / SEG]** ¿Qué componente de la biopsia es un predictor potente de progresión a ERC en NL?
(A) Sólo la clase (B) **Fibrosis intersticial y atrofia tubular (cronicidad TI) ✔** (C) Número de asas de alambre
> Retro: la inflamación intersticial entra en **actividad**; la fibrosis y atrofia en **cronicidad**. 🔁

### Combate villano: Genta Mycin
▸ **GENTA MYCIN:** ¡Ah, qué borde en cepillo tan hermoso! / La paciente está inmunosuprimida, tiene fiebre… / ¡me llamaron a mí!
**[PREGUNTA: SEG]** En una paciente con NL e infección, ¿qué haces con el aminoglucósido?
(A) Dosis múltiples diarias (B) **Evitar si hay alternativa; si es necesario, dosis única diaria, ajuste a TFGe y niveles valle ✔** (C) Doblar la dosis
**[PREGUNTA: SEG]** Profilaxis en inmunosupresión intensa con esteroide a dosis alta → **Considerar profilaxis contra *Pneumocystis* (TMP-SMX ajustado) y vacunas inactivadas** ✔
- **Derrota:** *"¡Me corrieron del cepillo! ¡Hemo-Eterna me va a descontar el día!"*

### ⚡ GIRO 3 — "Elisa"
▸ *(Llegas a una arteriola tapada. Una figura translúcida, una joven con bata de paciente, te mira.)*
▸ **FANTASMA DE ELISA:** ¿Tú también vienes del Dr. J.? / Él trató mi lupus muy bien. / Pero no vio esto.
▸ **FANTASMA DE ELISA:** Mis arteriolas se taparon. / No era sólo inflamación. / Era coágulo.
**[PREGUNTA: DX — rápida]** Lupus + trombos en arteriolas + plaquetas bajas. ¿Qué perfil pides YA? → **Anticoagulante lúpico, anticardiolipina, anti-β2GPI + frotis (esquistocitos), LDH, haptoglobina, ADAMTS13** ✔
▸ **DR. J. (radio, silencio largo):** …Elisa. / Le di pulsos y ciclofosfamida. / Nunca pedí antifosfolípidos. Nunca vi la microangiopatía.
▸ **DR. J.:** Su riñón no se perdió por el lupus. / Se perdió por lo que yo no busqué. / Por eso existe esta máquina.
**[ELECCIÓN — emocional]** (A) "No fue tu culpa" (B) "Por eso estoy aquí: para ver lo que no se vio" ✔ (C) Silencio.
- Cualquier opción avanza; (B) da +1 "Vínculo" con Dr. J. (desbloquea una línea extra en el epílogo).

**[PREGUNTA: HISTO / DX]** Lesiones vasculares en NL. Relaciona (minijuego de emparejar):
| Lesión | Pista |
|---|---|
| Depósitos inmunes vasculares | IC en pared arteriolar, sin inflamación — la más frecuente |
| Vasculopatía necrosante no inflamatoria | Necrosis fibrinoide con depósitos, sin células inflamatorias |
| **Microangiopatía trombótica (MAT)** | Trombos de fibrina/plaquetas, edema subendotelial; esquistocitos |
| Vasculitis verdadera | Infiltrado inflamatorio transmural (raro; pensar ANCA) |
| Nefropatía por **SAF** | MAT aguda; crónica: hiperplasia fibrosa de íntima, trombos organizados, atrofia cortical focal |

**[PREGUNTA: DX / TX]** MAT en biopsia de NL. ¿Qué buscas para elegir el tratamiento? Elige **tres**:
(A) **Anticuerpos antifosfolípido → SAF: anticoagulación (warfarina; evitar ACOD en triple positivo)** ✔
(B) **ADAMTS13 <10 % → PTT: recambio plasmático** ✔
(C) **Datos de MAT mediada por complemento → considerar bloqueo de C5 (eculizumab)** ✔
(D) Ácido úrico (Dr. J.: *"…ni yo, {JUGADOR}, ni yo. Bueno, un poquito."*) 🔁 *(chiste recurrente)*
> Retro KDIGO 2024: la MAT concomitante modifica el abordaje (sección 10.3.1 de la guía). **Elisa ahora puede descansar**: su arteriola se destapa con la animación de anticoagulación.

### Entrenadora: Dra. Sara Esquistocito — Residente de Hematología
- **Sprite:** Bata impecable, contador de células en la mano, lentes de alta precisión; una gota de sangre como mascota.
- **Personalidad:** Precisa, cuenta todo, odia la imprecisión; humor muy seco.
- **Reto:** *"Dices MAT. ¿Contaste esquistocitos? ¿Cuántos por campo? Exijo números."*
- **Combate:**
  1. [PREGUNTA: DX] Tétrada de laboratorio de hemólisis microangiopática → **Esquistocitos, LDH ↑, haptoglobina ↓, plaquetas ↓ (Coombs −)** ✔
  2. [PREGUNTA: DX] ¿Qué perfil antifosfolípido confiere más riesgo? → **Triple positivo (AL + aCL + anti-β2GPI)** ✔
  3. [PREGUNTA: TX] SAF trombótico con triple positividad: ¿rivaroxabán o warfarina? → **Warfarina (AVK)** ✔
  4. [PREGUNTA: TX] ¿Qué antimalárico reduce trombosis en LES con aPL? → **Hidroxicloroquina** ✔ 🔁 (5.ª aparición de HCQ)
- **Derrota:** *"Tus números son correctos. Eso es lo más bonito que puedo decirle a alguien."*

### Portal de Escala — Brenn (antes del jefe)
▸ **SABIO BRENN:** Lo que vas a enfrentar no es un monstruo. / Es un guardián. Nació para cazar virus. / Se equivocó de enemigo.
▸ **SABIO BRENN:** No lo destruyas. No se puede. / Calma su sed. Enséñale de nuevo. / Eso se llama remisión.

**Obi (desbloqueable), justo antes de la Arena:**
▸ **OBI** (espada láser azul con "CD20"): Soy **Obi**nutuzumab. Anti-CD20 tipo II. / Corto B en sangre y en tejido, / más hondo que mi tío Rituximab.
▸ **OBI:** Mi tío se rompió en LUNAR. / Yo pasé NOBILITY y REGENCY. / Pero ojo: a las plasmáticas CD20⁻ no las alcanzo. 🔁
**[ESCUDO] LUNAR (roto)** · **[ESCUDO] NOBILITY** (corona, *"gemelos **41-23** con la Aurora, pero a **104** semanas"*) · **[ESCUDO] REGENCY** (*"La Regencia dura **76**: 46 vs 33"*).
**[PREGUNTA: EVID]** ¿Qué dos ensayos comparten el marcador **41 % vs 23 %** de respuesta renal completa?
(A) BLISS-LN y ALMS (B) **AURORA 1 (52 sem) y NOBILITY (104 sem) ✔** (C) Euro-Lupus y LUNAR
> Obinutuzumab: aprobado por la FDA para NL activa en oct-2025 con base en NOBILITY y REGENCY. Posterior a KDIGO 2024 (que no lo incluye en sus opciones de primera línea). 🔁

> **TARJETA DE DATO Z10:** El intersticio predice el pronóstico; la **MAT/SAF** cambia el tratamiento (anticoagular, recambio o anti-C5 según causa). **Busca antifosfolípidos siempre.**

---

## ARENA DEL DEFENSOR — JEFE: LUPUS, "EL DEFENSOR CORROMPIDO"
**Mapa (pixel art):** Coliseo con forma de corte coronal renal: gradas = pirámides medulares, arena = corteza. Cielo rojo (brote). Lupus: guerrero gigante con armadura de **mariposa** (alas = eritema malar), escudo con un **receptor TLR7** brillante en el centro, lanza hecha de **doble hélice**. Detrás, en las gradas, una silla de diálisis vacía con logo de Hemo-Eterna.
**Regla:** Cada acierto = daño. Cada fallo = el Defensor se cura y suma 1 punto al **Índice de Cronicidad** visible. Si la cronicidad llega a 6 en la fase 4, final "gris" (ver epílogo alterno).

### Diálogo de apertura
▸ **LUPUS:** Yo protegía a esta casa. / Cazaba virus, ARN extraño, ADN invasor. / ¿Por qué ahora me atacas?
▸ **TÚ:** Porque ya no distingues. / Disparas contra su propio núcleo.
▸ **LUPUS:** ¡Mentira! ¡Siento ácidos nucleicos por todos lados! / Si no disparo, ella muere.
**[ELECCIÓN]** (A) Atacar de frente (B) "Te voy a calmar, no a destruir" ✔ → +10 % daño en toda la pelea (lección narrativa: la meta es remisión, no "curación").

### FASE 1 — "¿Quién eres?" (DIAGNÓSTICO)
Lupus usa "Disfraz": cambia de apariencia (rosácea, GN post-infecciosa, membranosa primaria, MAT).
1. [PREGUNTA: DX] Mujer 24 a, eritema malar, artralgias, edema, Cr 1.4, UPCR 3.2, cilindros eritrocitarios, C3/C4 bajos, anti-ADNdc +. Siguiente paso indispensable → **Biopsia renal (ML, IF, ME) con clase ISN/RPS e índices** ✔ 🔁
2. [PREGUNTA: DX] ¿Qué anticuerpo tiene alto valor predictivo negativo para NL activa si es negativo? → **Anti-C1q** ✔ 🔁
3. [PREGUNTA: DX] ¿Qué complemento esperas en GN postinfecciosa vs NL? → **Postinfecciosa: C3 bajo con C4 normal; NL: C3 y C4 bajos** ✔ 🔁
4. [PREGUNTA: DX] ¿Qué buscas SIEMPRE antes de terminar el abordaje? → **Anticuerpos antifosfolípido** ✔ (Dr. J.: *"Gracias."*) 🔁
▸ **LUPUS (pierde el disfraz):** …Me viste. / Pero ¿sabes de qué estoy hecho?

### FASE 2 — "¿De qué estás hecho?" (CLASE / HISTOLOGÍA)
La armadura se divide en 6 placas = las 6 clases. Usar **Lupa NIH**.
1. [PREGUNTA: HISTO] Biopsia: 60 % de glomérulos con hipercelularidad endocapilar, asas de alambre, 2 semilunas celulares, depósitos subepiteliales segmentarios → **Clase IV + V** ✔
2. [PREGUNTA: HISTO] Actividad 12/24, cronicidad 3/12: ¿qué significa? → **Mucha lesión activa potencialmente reversible, poca cicatriz: tratar intensamente ya** ✔ 🔁
3. [PREGUNTA: HISTO] Inclusiones tubulorreticulares en endotelio → ¿qué citocina? → **IFN tipo I** ✔ 🔁
4. [PREGUNTA: FISIO] ¿Por qué hay proliferación endocapilar? → **Depósitos subendoteliales expuestos a la circulación → complemento (C5a), FcγR, neutrófilos/NET, mesangio** ✔ 🔁
▸ **LUPUS (placas caen):** Ya conoces mi forma. / Pero no podrás calmarme. / Tengo mil manos.

### FASE 3 — "Calma al Defensor" (TRATAMIENTO, KDIGO 2024)
Lupus invoca **mil manos** = mecanismos. Cada pregunta conecta mecanismo → fármaco (el jugador elige la criatura correcta del equipo).

| Mano del Defensor (mecanismo) | Criatura correcta | Fármaco |
|---|---|---|
| Endosoma con TLR7/9 encendido | Paraguas HCQ | Hidroxicloroquina (todos, ≤5 mg/kg/d peso real) |
| Linfocitos y mesangio proliferando | MMF-01 | MPAA (MMF 1.0–1.5 g c/12 h) |
| BAFF manteniendo B autorreactivos | Beli | Belimumab (IV 10 mg/kg c/2 sem ×3, luego c/4 sem) |
| T con NFAT + podocito herido | Voclosporina | Voclosporina 23.7 mg c/12 h (TFGe >45) |
| B CD20⁺ en tejido | Obi | Obinutuzumab (posterior a KDIGO 2024; aprobado FDA 2025) |
| Inflamación aguda masiva | — (objeto "Pulso") | Metilprednisolona IV 0.25–0.5 g/d ×1–3, luego prednisona ~0.35–1 mg/kg/d (máx 80 mg), reducción en pocos meses |
| Todo lo que se divide (semilunas, TFGe en caída rápida) | Ciclón | CYC IV dosis baja (Euro-Lupus) |
| IFNAR | Ani (bloqueada) | Anifrolumab — no aprobado en NL a la fecha [VERIFICAR] |

1. [PREGUNTA: TX — KDIGO 2024] Opciones de inducción para clase III/IV ± V: glucocorticoide + uno de… → **MPAA; CYC IV dosis baja; belimumab + (MPAA o CYC); MPAA + CNI (si función renal no muy deteriorada)** ✔ 🔁
2. [PREGUNTA: TX / ESP] Sofía: 24 a, mexicana, quiere fertilidad futura, TFGe ≈ 54, proteinuria 3.2 g/g. ¿Qué base de inducción es más razonable? → **MPAA (mejor en hispanos — ALMS; sin toxicidad gonadal) + glucocorticoide reducido; considerar añadir belimumab o voclosporina** ✔ 🔁
3. [PREGUNTA: TX] Si eliges triple terapia, ¿cuándo favoreces **voclosporina** sobre **belimumab**? → **Proteinuria alta / componente podocitario (V), buscando reducción rápida de proteinuria, con TFGe >45** ✔ ; ¿y belimumab? → **Riesgo alto de brotes renales/extrarrenales; también útil con CYC** ✔ [ambas válidas según KDIGO 2024]
4. [PREGUNTA: TX] Fármaco que todos reciben salvo contraindicación → **HCQ** ✔ (+ vigilancia retiniana basal y anual después de 5 años) 🔁 (6.ª aparición)
5. [PREGUNTA: ESP] Antes de iniciar MPAA en una mujer de 24 → **Anticoncepción eficaz** ✔ 🔁
▸ **LUPUS (tambaleando):** Mis manos… se duermen. / El interferón ya no me grita. / ¿Qué me está pasando?

### FASE 4 — ⚡ "La sombra en las gradas" (MANTENIMIENTO, RESPUESTA, NEFROPROTECCIÓN)
▸ *(La silla de diálisis en las gradas se mueve. Una sombra gris se levanta: La Esclerosis, con la voz del Ing. Perpetuo Diálisis.)*
▸ **LA ESCLEROSIS:** Bravo, residente. Lo calmaste. / Pero yo no necesito brotes. / Me alimento de cada nefrona que ya perdiste.
▸ **LA ESCLEROSIS:** Cada respuesta que falles, / convierto una semilunita en piedra. / Hemo-Eterna agradece tu lentitud.
**Mecánica:** la barra de cronicidad empieza a llenarse lentamente (pausa total en modo lectura lenta; sólo sube con fallos). Las preguntas defienden nefronas.
1. [PREGUNTA: SEG — KDIGO 2024] Respuesta **completa**: → **UPCR <0.5 g/g con TFGe estable (±10–15 % del basal), idealmente en 6–12 meses** ✔ ; **parcial:** ↓ proteinuria ≥50 % y <3 g/g.
2. [PREGUNTA: TX — KDIGO 2024] Mantenimiento preferido y duración total → **MPAA; inmunosupresión total ≥36 meses** ✔ 🔁 (ALMS: MMF > AZA)
3. [PREGUNTA: SEG] Sin respuesta a los 6 meses. Antes de llamarlo "refractario", descarta → **Mala adherencia, dosis insuficiente (niveles de MPA), cronicidad alta (re-biopsia)** ✔
4. [PREGUNTA: FISIO / TX — Brenn] ¿Qué fármacos protegen a las nefronas sobrevivientes de la hiperfiltración? → **iSRAA (y control de PA); iSGLT2 como nefroprotección en ERC (evidencia indirecta en NL; KDIGO 2024 lo deja como área futura)** ✔ 🔁
5. [PREGUNTA: SEG] Si llega a ERC terminal, la terapia de reemplazo preferida → **Trasplante renal** ✔ (La Esclerosis: *"¡NO! ¡Mi silla!"*)
6. [PREGUNTA: SEG] Dos marcadores que, al normalizarse, apoyan respuesta inmunológica → **C3/C4 y anti-ADNdc** ✔ 🔁

▸ **LA ESCLEROSIS (retrocediendo):** No importa. Siempre queda una nefrona cansada. / Nos veremos en el nivel 26. / En la sala de las 300 preguntas.
▸ *(Se desvanece. La silla de diálisis se rompe en píxeles.)*

### Desenlace del jefe
▸ **LUPUS (se arrodilla, armadura blanca):** Estoy… tranquilo. / No me fui. Sigo aquí, vigilando. / Pero ya sé quién es de la casa.
▸ **SABIO BRENN:** Eso es la remisión, hijo. / No es victoria. Es tregua. / Y la tregua se cuida con años de mantenimiento.
▸ **DR. J. (radio):** Lo hiciste. Viste lo que yo no vi. / …Elisa estaría contenta. / Ahora, ¿alguien quiere hablar de urato? ¿No? Bueno.

**Epílogo en Urgencias (fuera del cuerpo):**
▸ **SOFÍA:** Doctor, ¿me voy a curar? / ¿Podré tener hijos?
▸ **TÚ:** Vamos a controlar esto juntos. / Con tratamiento, cuidado y un plan, sí se puede planear. 🔁 (Ginecología)
▸ **VALERIA (rival, en el pasillo):** Oye… hice una tarjeta nueva. / Dice "¿por qué?" en grande. / ¿Me ayudas a llenarla? *(Arco: rival → futura aliada.)*

**Final alterno "gris"** (si cronicidad ≥6): mismo desenlace, pero el cielo de Sofía queda gris y Dr. J. dice: *"Remisión, sí. Pero perdimos nefronas. Vuelve a la Zona 9 y practica la contrarreloj."* (Permite repetir zonas para mejorar el final; refuerza repetición.)

---

## 11. NEFRODEX — PÁGINAS DESBLOQUEADAS EN 9-5
| # | Entrada | Texto (≤2 líneas) |
|---|---|---|
| 9-5-01 | C1q | Héroe y verdugo: su falta impide limpiar apoptóticos (>90 % LES); en el depósito enciende la vía clásica. |
| 9-5-02 | DNASE1L3 | DNasa secretada que corta ADN de micropartículas; su falta → LES pediátrico con NL. |
| 9-5-03 | TREX1 | Exonucleasa citosólica; si falla, cGAS-STING → IFN-β. |
| 9-5-04 | TLR7 | Sensor de ARN en endosoma, gen en X; ganancia de función Y264H causa LES. |
| 9-5-05 | pDC | Fábrica de IFN-α; capta IC con ácidos nucleicos por FcγRIIA. |
| 9-5-06 | BAFF / APRIL | BAFF: BAFF-R, TACI, BCMA. APRIL: TACI, BCMA. Blanco de belimumab (BAFF soluble). |
| 9-5-07 | Tfh / Treg | Tfh (CXCR5, PD-1, IL-21) impulsa centros germinales; Treg fallan por falta de IL-2. |
| 9-5-08 | NET / LDG | ADN + histonas + LL-37; degradación deficiente → autoantígeno + activación de pDC. |
| 9-5-09 | Sitio del depósito | Tamaño, carga, avidez, cantidad, siembra in situ. Subendotelial = proliferativa; subepitelial = membranosa. |
| 9-5-10 | Formación in situ | Nucleosomas catiónicos sobre MBG aniónica; DNasa1 renal apagada; anti-ADNdc cruzado con α-actinina. |
| 9-5-11 | Podocitopatía lúpica | Borramiento difuso sin depósitos periféricos; se trata como cambios mínimos. |
| 9-5-12 | Índices NIH | Actividad 24 (necrosis y semilunas ×2); cronicidad 12. |
| 9-5-13 | Membranosa lúpica | Full-house, IgG1/3, EXT1/EXT2, tubulorreticulares; PLA2R usualmente −. |
| 9-5-14 | Lesiones vasculares | Depósitos, vasculopatía necrosante, MAT, vasculitis, SAF. Buscar aPL siempre. |
| 9-5-15 | Inducción KDIGO 2024 | GC + MPAA / CYC dosis baja / belimumab + (MPAA o CYC) / MPAA + CNI. HCQ a todos. |
| 9-5-16 | Mantenimiento | MPAA preferido; ≥36 meses en total. |
| 9-5-17 | Nefroprotección | iSRAA, PA, considerar iSGLT2; trasplante si ERC terminal. |
| 9-5-18 | Embarazo | NL inactiva ≥6 meses; MMF fuera ≥6 semanas antes; HCQ + aspirina. |

---

## 12. ÍNDICE DE MNEMOTECNIAS (para repaso rápido)
| Concepto | Mnemotecnia | Zona(s) |
|---|---|---|
| Riesgo monogénico del complemento | **C1q > C4 > C2** (sigue el orden de la cascada) | Z2, Z3 |
| DNASE1L3 | **"L3 = Lupus 3 veces: temprano, familiar, renal"** | Z3 |
| Cadena cGAS | **"ADN → cGAS → cGAMP → STING → IRF3 → IFN"**: "Ganso → Gama → Picadura → Irá → Interferón" | Z3 |
| Sitio del depósito | **"Lo subendotelial mira al río; lo subepitelial vive detrás de la pared"** | Z5, Z6, Z7 |
| Belimumab | **"B de BAFF, Belimumab y BLISS; 4-3 le gana al 3-2 (104 sem)"** | Z4, jefe |
| ALMS | **"Las almas empatan (MMF = CYC) y en mantenimiento gana MMF"** | Z4, jefe |
| Euro-Lupus | **"Billete de 500, cada quincena, seis veces = 3 g"** | Z5, Z7, Z9 |
| Voclosporina | **"VOC = Voz que Calma al podocito"**, **puerta 45**, 23.7 mg c/12 h | Z7, jefe |
| AURORA 1 / NOBILITY | **"Gemelos 41-23"**: Aurora al amanecer (1 año); la Nobleza a los 2 años | Z7, Z10 |
| REGENCY | **"La Regencia dura 76"** (46 vs 33) | Z10 |
| LUNAR | **"La luna se rompió"** (rituximab no superó placebo) | Z10 |
| Obinutuzumab | **"Obi corta más hondo (tipo II), pero no alcanza a las plasmáticas"** | Z4, Z10 |
| Índice de actividad | **"N y S pesan doble"** (Necrosis y Semilunas) | Z8, Z9, jefe |
| ISN/RPS 2018 | **"Se fueron A/C y S/G; llegaron los índices"** | Z8 |

---

## 13. TABLA DE REPETICIÓN DELIBERADA (≥3 apariciones, forma distinta)
| Concepto clave | Apariciones (zona → forma) | Total |
|---|---|---|
| **C1q (paradoja)** | Z2 puerta-llave + pregunta genética → Z3 libro → Z6 encadenado + minijuego → Z8 farol IF → Jefe F1 (anti-C1q) | 6 |
| **Firma de IFN tipo I** | Z2 IFN-κ → Z3 cGAS-STING → Z4 pDC (minijuego) → Z8 inclusiones tubulorreticulares → Jefe F2 | 5 |
| **TLR7 / sensores** | Z3 libro (X, Y264H) + Brenn → Z4 ABC/DN2 → Z10 Brenn "guardián" → Jefe (escudo TLR7) | 4 |
| **HCQ** | Z2 Dermatología → Z4 minijuego → Z7 Ginecología → Z10 Hematología (trombosis) → Jefe F3 | 5+ |
| **Subendotelial vs subepitelial** | Z5 minijuego clasificar → Z6 pregunta + giro → Z7 clase V → Jefe F2 | 4 |
| **Complemento bajo = consumo** | Z1 lab → Z5 Marinero C3 → Z6 cascada → Jefe F1 y F4 | 5 |
| **Anti-CD20 no toca plasmáticas** | Tabla de tipos → Z4 rival → Z10 Obi | 3 |
| **BAFF / belimumab / BLISS-LN** | Z4 enemigo + escudo → Z4 rival → Jefe F3 | 3 |
| **Calcineurina / podocito / TFGe >45** | Z1 TFGe ≈ 54 → Z7 giro + AURORA → Jefe F3 | 3 |
| **Euro-Lupus / fertilidad** | Z5 escudo → Z7 Ginecología → Z9 Medicina Interna → Jefe F3 | 4 |
| **Índices actividad/cronicidad** | Z8 minijuego → Z8 rival → Z9 contrarreloj → Z10 intersticio → Jefe F2/F4 | 5 |
| **Hiperfiltración → esclerosis** | Z9 Brenn → Z9 sombra → Jefe F4 → Epílogo | 4 |
| **Antifosfolípidos / MAT** | Z10 giro Elisa → Z10 Hematología → Jefe F1 | 3 |
| **Biopsia decide** | Z1 tarjeta + Urología → Z8 Cirugía → Jefe F1 | 4 |

---

## 14. NOTAS PARA PRODUCCIÓN
- **Duración estimada:** 60–90 min (vs ~20 min del prototipo). Cada zona termina en un punto de guardado.
- **Banco de preguntas:** cada [PREGUNTA] puede migrar a `bankln.json` con `serie_id: "LN"` y la etiqueta de competencia de §0. Revisar que la opción correcta **no sea siempre la más larga** (en este guion algunas lo son por claridad; al pasar al banco, equilibrar longitud de distractores).
- **Sprites mínimos nuevos:** 10 entrenadores, 4 Nefrotóxicos, Lupus (3 estados), La Esclerosis, Elisa, ~35 enemigos salvajes (reutilizar paletas: piel = naranja, ganglio = verde, sangre = rojo, glomérulo = rosa, histología = morado/rosa, intersticio = ocre).
- **Datos marcados [VERIFICAR]:** estado de anifrolumab en NL (fase 3), punto de corte "cronicidad alta" (varía por cohorte). Revisar antes de cada actualización del juego.

---

## 15. REFERENCIAS
**Guías y clasificación**
1. KDIGO 2024 Clinical Practice Guideline for the Management of Lupus Nephritis. *Kidney Int.* 2024;105(1S):S1–S69. PMID: 38182286. PDF: https://kdigo.org/wp-content/uploads/2024/01/KDIGO_2024_Lupus_Nephritis_Guideline.pdf · Top 10: https://kdigo.org/wp-content/uploads/2024/01/KDIGO-2024-Lupus-Nephritis-Guideline-Top-10-Takeaways-for-Clinicians.pdf
2. Bajema IM, et al. Revision of the ISN/RPS classification for lupus nephritis: clarification of definitions, and modified NIH activity and chronicity indices. *Kidney Int.* 2018;93:789–796. PMID: 29459092.
3. Aringer M, et al. 2019 EULAR/ACR classification criteria for SLE. *Arthritis Rheumatol.* 2019;71:1400–1412. PMID: 31385462.

**Fisiopatología (revisiones)**
4. Lech M, Anders HJ. The pathogenesis of lupus nephritis. *J Am Soc Nephrol.* 2013;24:1357–1366. PMID: 23929771.
5. Anders HJ, et al. Lupus nephritis. *Nat Rev Dis Primers.* 2020;6:7. PMID: 31974366.

**Genética y depuración**
6. Brown GJ, et al. TLR7 gain-of-function genetic variation causes human lupus. *Nature.* 2022;605:349–356. PMID: 35477763. https://pubmed.ncbi.nlm.nih.gov/35477763/
7. Souyris M, et al. TLR7 escapes X chromosome inactivation in immune cells. *Sci Immunol.* 2018;3:eaap8855. https://doi.org/10.1126/sciimmunol.aap8855
8. Al-Mayouf SM, et al. Loss-of-function variant in DNASE1L3 causes a familial form of SLE. *Nat Genet.* 2011;43:1186–1188. https://www.nature.com/articles/ng.975

**Formación de depósitos, NET y piel→riñón**
9. Zykova SN, et al. Renal Dnase1 enzyme activity and protein expression is selectively shut down in murine and human membranoproliferative lupus nephritis. *PLoS One.* 2010;5:e12096. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2938370/
10. Deocharan B, et al. Alpha-actinin is a cross-reactive renal target for pathogenic anti-DNA antibodies. *J Immunol.* 2002;168:3072–3078. https://doi.org/10.4049/jimmunol.168.6.3072
11. Hakkim A, et al. Impairment of neutrophil extracellular trap degradation is associated with lupus nephritis. *Proc Natl Acad Sci USA.* 2010;107:9813–9818. https://pmc.ncbi.nlm.nih.gov/articles/PMC2906830
12. Lande R, et al. Neutrophils activate plasmacytoid dendritic cells by releasing self-DNA–peptide complexes in SLE. *Sci Transl Med.* 2011;3:73ra19. https://doi.org/10.1126/scitranslmed.3001180
13. Garcia-Romo GS, et al. Netting neutrophils are major inducers of type I IFN production in pediatric SLE. *Sci Transl Med.* 2011;3:73ra20. https://doi.org/10.1126/scitranslmed.3001201
14. Skopelja-Gardner S, et al. Acute skin exposure to ultraviolet light triggers neutrophil-mediated kidney inflammation. *Proc Natl Acad Sci USA.* 2021;118:e2019097118. https://doi.org/10.1073/pnas.2019097118
15. Jenks SA, et al. Distinct effector B cells induced by unregulated TLR7 contribute to pathogenic responses in SLE. *Immunity.* 2018;49:725–739. https://doi.org/10.1016/j.immuni.2018.08.015

**Podocito y membranosa lúpica**
16. Faul C, et al. The actin cytoskeleton of kidney podocytes is a direct target of the antiproteinuric effect of cyclosporine A. *Nat Med.* 2008;14:931–938. https://doi.org/10.1038/nm.1857
17. Sethi S, et al. Exostosin 1/Exostosin 2–associated membranous nephropathy. *J Am Soc Nephrol.* 2019;30:1123–1136. https://doi.org/10.1681/ASN.2018080852

**Ensayos clínicos (escudos)**
18. Houssiau FA, et al. Euro-Lupus Nephritis Trial: low-dose vs high-dose IV cyclophosphamide. *Arthritis Rheum.* 2002;46:2121–2131. PMID: 12209517.
19. Appel GB, et al. (ALMS) Mycophenolate mofetil versus cyclophosphamide for induction treatment of lupus nephritis. *J Am Soc Nephrol.* 2009;20:1103–1112. PMID: 19369404.
20. Dooley MA, et al. (ALMS mantenimiento) Mycophenolate versus azathioprine as maintenance therapy for lupus nephritis. *N Engl J Med.* 2011;365:1886–1895. PMID: 22087680.
21. Furie R, et al. (BLISS-LN) Two-year, randomized, controlled trial of belimumab in lupus nephritis. *N Engl J Med.* 2020;383:1117–1128. PMID: 32937045.
22. Rovin BH, et al. (AURORA 1) Efficacy and safety of voclosporin versus placebo for lupus nephritis. *Lancet.* 2021;397:2070–2080. PMID: 33971155.
23. Furie RA, et al. (NOBILITY) B-cell depletion with obinutuzumab for the treatment of proliferative lupus nephritis. *Ann Rheum Dis.* 2022;81:100–107. PMID: 34615636.
24. Furie RA, et al. (REGENCY) Efficacy and safety of obinutuzumab in active lupus nephritis. *N Engl J Med.* 2025. https://doi.org/10.1056/NEJMoa2410965 · PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12214873/
25. Rovin BH, et al. (LUNAR) Efficacy and safety of rituximab in patients with active proliferative lupus nephritis. *Arthritis Rheum.* 2012;64:1215–1226. PMID: 22231479.
26. Jayne D, et al. (TULIP-LN) Phase II randomised trial of type I interferon inhibitor anifrolumab in lupus nephritis. *Ann Rheum Dis.* 2022;81:496–506. https://doi.org/10.1136/annrheumdis-2021-221478
27. FDA aprueba obinutuzumab (Gazyva) para nefritis lúpica (20-oct-2025). Healio: https://www.healio.com/news/rheumatology/20251020/fda-approves-gazyva-for-lupus-nephritis-marking-significant-advancement-for-patients

> **Nota de trazabilidad:** sólo el PMID de la ref. 6 se confirmó en línea. Los demás PMID (refs. 1–5, 18–23, 25) se citan de memoria bibliográfica: la API de PubMed estaba bloqueada en este entorno. Las refs. con URL/DOI/PMC sí se localizaron por búsqueda web. Confirmar cada PMID con el título exacto antes de publicar. Las cifras de REGENCY (46.4 vs 33.1 %) y la fecha de aprobación FDA se verificaron con la ref. 27; las opciones de inducción, dosis y umbral de voclosporina, con la ref. 1.
