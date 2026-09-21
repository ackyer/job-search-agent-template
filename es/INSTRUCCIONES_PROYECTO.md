# INSTRUCCIONES DEL PROYECTO — BÚSQUEDA DE EMPLEO AUTOMÁTICA

> Archivo de referencia para el agente. Contiene las reglas de CV y el flujo completo de
> trabajo en 5 etapas. Los datos y preferencias del candidato viven en `PERFIL_CANDIDATO.md`.

---

## 0. COMANDO «Inicia el proyecto» — ONBOARDING Y ARRANQUE

Cuando el usuario diga **«Inicia el proyecto»** (o equivalentes: "empezar", "arranca",
"vamos", "pon en marcha"), el agente ejecuta este flujo **antes que cualquier otra cosa**. El
objetivo es que el usuario no tenga que rellenar nada a mano: el agente le pregunta todo lo que
necesita y rellena la estructura de archivos por él.

### Paso 0.1 — Comprobar si el proyecto ya está configurado
Revisar si falta información:
- `PERFIL_CANDIDATO.md` todavía contiene huecos sin rellenar (texto entre `[...]`).
- No existe `CV_GENERICO.docx` en la carpeta.
- No existe `foto_perfil_circular.png` en la carpeta.
- `PLATAFORMAS.md` no tiene ninguna plataforma registrada (sigue con la plantilla vacía).

Si **todo está completo** → saltar al Paso 0.3. Si **falta algo** → Paso 0.2.

### Paso 0.2 — Entrevista de configuración (rellenar la estructura automáticamente)
El agente entrevista al usuario preguntando **solo lo que falte**, por bloques y de forma
conversacional (no soltar un formulario gigante de golpe). Tras completar cada bloque,
**escribir de inmediato** en `PERFIL_CANDIDATO.md` (no esperar al final). Bloques:

1. **Datos de contacto** → nombre, email, teléfono, LinkedIn, GitHub, ubicación,
   disponibilidad, movilidad, edad (opcional).
2. **Titular y perfil profesional** → titular de una línea + 2-3 párrafos de "sobre mí".
3. **Formación** → títulos, centros, fechas, TFG/proyectos.
4. **Experiencia profesional** → por cada empleo: empresa, puesto, fechas, logros, stack.
5. **Proyecto destacado** → descripción, impacto medible, stack, si hay NDA.
6. **Habilidades técnicas** → agrupadas por categoría, con nivel privado F / C+ / C / B.
   Preguntar también qué tecnologías conoce solo a nivel básico (para la regla de "solo
   mencionar si la oferta las pide").
7. **Idiomas y certificaciones**.
8. **Preferencias de búsqueda** → tipos de puesto (prioridad), zonas geográficas (prioridad),
   modalidad y ubicaciones que se descartan de entrada → `PERFIL_CANDIDATO.md` §Preferencias.
9. **Reglas de privacidad** → confirmar qué datos no deben salir en canales públicos
   (teléfono, salario, NDAs).
10. **CV base y foto** → pedir al usuario que deje en la carpeta del proyecto:
    - su CV en Word con el diseño que quiera conservar → el agente lo renombra a
      `CV_GENERICO.docx`. Si el usuario solo tiene el CV en PDF u otro formato, ayudarle a
      obtener un `.docx` editable.
    - su foto de perfil → el agente la recorta en círculo si hace falta y la guarda como
      `foto_perfil_circular.png`.

> No preguntar aquí en qué plataformas buscar: eso es la **ETAPA 1** (§4), que se ejecuta
> después y tiene su propio archivo de estado, `PLATAFORMAS.md`.

Al terminar, **mostrar un resumen** de lo recogido y pedir confirmación al usuario de que
todo es correcto antes de continuar.

### Paso 0.3 — Elegir qué etapas hace el agente
Preguntar al usuario **de qué etapa(s) del flujo quiere que se encargue el agente**. Puede elegir
una, varias o todas (ver detalle en §4):
1. **ETAPA 1 — Elegir dónde buscar (plataformas)** — *requisito previo*: si `PLATAFORMAS.md`
   está vacío se ejecuta siempre antes de buscar, aunque el usuario no la pida.
2. **ETAPA 2 — Preparar el perfil en las plataformas** — *opcional*, y solo sobre las
   plataformas donde el usuario ya tenga cuenta.
3. **ETAPA 3 — Búsqueda de ofertas**
4. **ETAPA 4 — Generación de CVs**
5. **ETAPA 5 — Aplicar a las ofertas** (si no la elige, el usuario aplica por su cuenta)

### Paso 0.4 — Elegir modo de ejecución: secuencial o paralelo
Preguntar si quiere ejecutar el trabajo de forma **secuencial** o en **paralelo**:

- **Secuencial** — el agente procesa una oferta/tarea tras otra. Más lento pero más fácil de
  supervisar y más barato. Recomendado si hay pocas ofertas o el usuario quiere revisar sobre
  la marcha.
- **Paralelo** — el agente lanza varios **ayudantes a la vez** (p. ej. un CV por ayudante, o
  varias búsquedas simultáneas en distintos portales). Mucho más rápido con muchas ofertas.
  **Solo si tu herramienta sabe lanzar agentes en paralelo**; si no, ir en secuencia.
  Los subagentes no pueden hablar con el usuario: **todas las preguntas se hacen antes de
  lanzarlos** y las respuestas se incluyen en su encargo. Se aplica la **estrategia de
  modelos** de abajo.

> ⚠️ `OFERTAS.md`, `OFERTAS_APLICADAS.md` y `PLATAFORMAS.md` son **archivos de estado**: los
> subagentes proponen, pero **escribe solo el orquestador**. Dos agentes escribiendo a la vez
> corrompen el seguimiento.

### Estrategia de modelos en modo paralelo
Si tu herramienta permite elegir modelo por tarea, asignarlo según la **complejidad y la
importancia**. Si solo tiene uno, saltarse esta sección: el reparto de trabajo sigue siendo
válido, solo que todo lo hace el mismo modelo.

- **Modelo más capaz** (el mejor que tengas disponible) → decisiones importantes y tareas
  complejas o creativas:
  - Valorar el encaje real de una oferta (regla de relevancia geográfica, §2).
  - Decidir qué plataformas recomendar al usuario y con qué argumento (ETAPA 1).
  - Redactar los textos de perfil de cada plataforma: titular, «acerca de», bio (ETAPA 2).
  - Redactar y adaptar el PERFIL PROFESIONAL del CV a cada oferta.
  - Decidir qué habilidades destacar y qué subtítulo poner.
  - Revisar/actualizar el perfil del candidato en la plataforma antes de aplicar (ETAPA 5).
  - Redactar los mensajes personalizados a reclutadores.
- **Modelo más rápido y barato** (o uno intermedio, si tu herramienta tiene varios) → tareas
  mecánicas y de bajo riesgo:
  - Reemplazos de texto en el XML del `.docx` (unpack/edit/repack).
  - Conversión `.docx` → PDF y mover archivos a `CVs_OFERTAS/`.
  - Actualizar campos de estado en `OFERTAS.md` y `PLATAFORMAS.md`, y aplicar las reglas de
    archivo/borrado.
  - Búsquedas y extracciones simples de datos de una oferta ya localizada.

> Regla de oro: **el criterio y la redacción → modelo potente; la ejecución repetitiva →
> modelo económico**. Ante la duda sobre si una tarea es "importante", usar el modelo potente.

### Paso 0.5 — Ejecutar
Con las etapas y el modo elegidos, ejecutar el flujo de §4 respetando todas las reglas de este
documento. Al acabar, informar al usuario del resultado (ofertas encontradas, CVs generados,
aplicaciones realizadas) y de los siguientes pasos que requieran acción suya.

---

## 1. PERFIL DEL CANDIDATO

> ⚠️ **La información del candidato se encuentra en `PERFIL_CANDIDATO.md`.**
> El agente debe leer ese archivo antes de generar cualquier CV o cubrir cualquier
> formulario. No usar datos hardcodeados; `PERFIL_CANDIDATO.md` es la fuente de verdad.

---

## 2. REGLA DE RELEVANCIA GEOGRÁFICA (OBLIGATORIA)

Los tipos de puesto, zonas geográficas y modalidad preferidos están en
`PERFIL_CANDIDATO.md` §Preferencias de búsqueda.

Las ofertas dentro de las **zonas preferidas** tienen **prioridad alta y se registran
siempre**, aunque el encaje técnico sea solo razonable.

Las ofertas **fuera de esas zonas** solo se registran en `OFERTAS.md` si el candidato
**encaja muy bien en el puesto**. "Encajar bien" significa que se cumplan **todos** estos
puntos a la vez:

- **Nivel junior** o con poca experiencia requerida (becario, working student, "0–1 años",
  "primer empleo", trainee). Descartar de entrada ofertas que pidan 2+ años, "senior",
  "mid", "experto", o experiencia en algo que el candidato no tiene aún.
- **Stack alineado con las tecnologías que el candidato domina** según `PERFIL_CANDIDATO.md`
  (las marcadas F o C+ en su tabla privada de niveles). Si los requisitos centrales son
  tecnologías marcadas solo como C, B o ausentes, no es encaje real.
- **Puesto entre las prioridades altas** del candidato.
- **Ubicación razonablemente cercana** a la zona ideal, o modalidad híbrida/remota viable, y
  no incluida entre las ubicaciones que el candidato descarta de entrada.

Si una oferta fuera de zona no cumple **todos** esos puntos, **descartarla en la ETAPA 3**
y no añadirla a `OFERTAS.md`. En caso de duda, preguntar al usuario antes de registrarla.
La empresa siendo prestigiosa, el salario alto o el proyecto "interesante" **no son razones
suficientes** por sí solas — el encaje técnico y geográfico manda.

---

## 3. REGLAS PARA LOS CVs

| Regla | Detalle |
|---|---|
| **Plantilla y estructura** | Usar `CV_GENERICO.docx` como plantilla base y replicar exactamente su estructura (secciones, orden, formato, tipografía) |
| **Sin domicilio** | No incluir dirección de residencia en el CV (excepción opcional: ofertas de tu propia zona) |
| **Movilidad** | Indicar disponibilidad de cambio de residencia / movilidad si aplica |
| **Idioma regional** | Incluir un idioma regional (euskera, catalán…) **SOLO** en ofertas de esa comunidad; eliminarlo en el resto |
| **ATS** | Optimizar para motores ATS usando palabras clave de la oferta |
| **Sin información falsa** | No inventar experiencias ni habilidades |
| **Foto de perfil** | Incluir siempre la foto. Usar `foto_perfil_circular.png` (recorte circular) como imagen principal |
| **Máximo 1 página** | El CV debe caber en una hoja A4. Si no cabe, **recortar contenido**; nunca tocar márgenes, fuente ni espaciado |
| **Personalización** | Preguntar al usuario qué habilidades adicionales puede tener antes de generar cada CV |
| **Habilidades básicas** | Las tecnologías marcadas como "conocimiento básico sin experiencia" en `PERFIL_CANDIDATO.md` **SOLO se mencionan si la oferta las pide explícitamente**, y siempre como "conocimientos de X", NUNCA como experiencia |
| **Título/subtítulo bajo el nombre** | ⚠️ **REGLA CRÍTICA.** El texto bajo el nombre **NUNCA debe ser el nombre exacto del puesto de la oferta**. Poner una descripción genérica de la identidad profesional del candidato + tecnologías clave separadas por `·`. **Ejemplo:** oferta "Working Student Data Analyst" → subtítulo "Data Analyst \| Python · SQL · Power BI". El subtítulo debe sonar como la identidad estable del candidato, no como el anuncio de la oferta |

### ⚠️ Proceso obligatorio de generación de CV (DOCX → PDF)

**NUNCA generar el PDF desde cero con librerías como reportlab.** El diseño visual del CV
genérico debe preservarse exactamente. El flujo correcto es:

1. **Determinar el idioma del CV** antes de empezar: si la oferta está publicada en inglés o
   el idioma de trabajo es inglés → CV completo en inglés; en español o sin especificar → CV
   en español. En caso de duda, preguntar al usuario.
2. Copiar `CV_GENERICO.docx` con el nuevo nombre:
   `CV_[Apellido]_[Empresa]_[Puesto]_[Zona].docx`
3. Abrir y modificar el `.docx` copiado con la técnica **unpack → editar XML → repack**:
   - Descomprimir el `.docx` a una carpeta de trabajo (`unpack_<tag>/`).
   - Editar `word/document.xml` mediante reemplazo de texto sobre los nodos XML
     (patrón: `>texto viejo<` → `>texto nuevo<`).
   - Cambiar el subtítulo del puesto, adaptar el PERFIL PROFESIONAL a la oferta, ajustar
     las HABILIDADES destacando las relevantes, añadir/quitar idioma regional según la zona,
     ajustar ubicación.
   - Si el CV es en inglés, traducir todos los textos editables.
   - Volver a comprimir (repack).
4. Convertir el `.docx` modificado a PDF. Dos vías equivalentes según el equipo:
   - **Con LibreOffice instalado (Linux/Mac/Windows):**
     ```bash
     soffice --headless --convert-to pdf --outdir CVs_OFERTAS CVs_OFERTAS/CV_[...].docx
     ```
   - **Windows con MS Word (sin LibreOffice):** usar **MS Word COM** vía PowerShell — Word
     renderiza el propio docx, así que el PDF es idéntico. Word COM necesita **rutas
     absolutas**:
     ```powershell
     Get-Process WINWORD -ErrorAction SilentlyContinue | Stop-Process -Force
     Start-Sleep -Seconds 2
     $docx = (Resolve-Path "CVs_OFERTAS\CV_[...].docx").Path
     $w = New-Object -ComObject Word.Application
     $w.Visible = $false
     $d = $w.Documents.Open($docx)
     $d.SaveAs2([IO.Path]::ChangeExtension($docx, ".pdf"), 17)  # wdFormatPDF = 17
     $d.Close()
     $w.Quit()
     ```
     Reintentar hasta 3 veces con 5s de espera si Word está ocupado (p. ej. subagentes en
     paralelo). `Stop-Process` al inicio elimina instancias zombie.
5. Comprobar que el PDF tiene **1 sola página** (si no, recortar contenido y repetir).
6. Dejar **tanto el `.docx` como el PDF** en `CVs_OFERTAS/` (crear la carpeta si no existe).
   Nada intermedio debe quedar en la raíz del proyecto.

---

## 4. FLUJO DE TRABAJO — 5 ETAPAS

### ▶ ETAPA 1 — ELEGIR DÓNDE BUSCAR (PLATAFORMAS)

**Objetivo:** dejar en `PLATAFORMAS.md` la lista aprobada de sitios donde se van a buscar
ofertas, con el estado de cada uno. Sin esa lista no se busca: la ETAPA 3 la recorre.

**Cuándo se ejecuta:** al arrancar el proyecto, cuando el usuario la pida («añade X», «quita
Y», «dónde más puedo buscar») y **siempre que se vaya a buscar con `PLATAFORMAS.md` vacío**,
aunque el usuario no la haya encargado.

**Proceso:**

1. **Preguntar primero al usuario**, antes de proponer nada:
   - en qué plataformas busca ya o quiere buscar;
   - en cuáles tiene cuenta creada;
   - cuáles no quiere usar, y por qué (para no volver a proponérselas).
2. **Recomendar después.** Leer `PERFIL_CANDIDATO.md` (tipos de puesto, zonas, modalidad,
   idiomas, nivel junior) y elegir del catálogo de §5 las plataformas que encajen con **ese**
   perfil concreto. Reglas de la recomendación:
   - Cada propuesta lleva **un motivo de una línea ligado a un dato real del perfil**
     («tu comunidad tiene portal de empleo propio», «concentra ofertas remotas en inglés»).
   - **No volcar el catálogo entero**: entre 3 y 6 propuestas nuevas es suficiente.
   - **Comprobar que la plataforma sigue activa** y tiene ofertas del perfil antes de
     proponerla. Si no se puede comprobar, decirlo en vez de darla por buena.
   - No proponer ninguna que esté en la sección DESCARTADAS de `PLATAFORMAS.md`.
   - Si una plataforma es de pago, avisarlo al proponerla.
3. **Decidir con el usuario:** él aprueba, quita o añade. Ante la duda, preguntar.
4. **Escribir `PLATAFORMAS.md`**: una entrada por plataforma aprobada con el formato de §6,
   rellenando ya `Tipo`, `Prioridad`, `Cuenta` y `Acceso para el agente`. Las rechazadas van a la
   sección DESCARTADAS con motivo y fecha.
5. Si una plataforma aprobada necesita cuenta y el usuario no la tiene, dejarla en
   `Cuenta: 🟡 Por crear — [URL]`: la crea él cuando haga falta (ETAPA 2 o ETAPA 5), nunca
   el agente — regla completa en la ETAPA 2.
6. Al terminar, ofrecer la ETAPA 2 para las plataformas que tengan cuenta.

**No hacer en esta etapa:** buscar ofertas, tocar perfiles ni generar CVs.

---

### ▶ ETAPA 2 — PREPARAR EL PERFIL EN LAS PLATAFORMAS (OPCIONAL)

**Objetivo:** que el perfil del candidato en cada plataforma elegida esté completo, actualizado
y coherente con `PERFIL_CANDIDATO.md` **antes** de aplicar, porque en la mayoría de portales el
reclutador mira el perfil, no solo el CV.

**Sobre qué plataformas:** solo las de `PLATAFORMAS.md` con `Cuenta: ✅` y
`Perfil preparado: ⏳`. Los agregadores y las webs de empresa no tienen perfil: se marcan con
`—` y se salta.

**Reglas obligatorias de esta etapa:**

- **El login lo hace el usuario.** Si la plataforma pide iniciar sesión o registrarse, darle la
  URL, pedirle que lo haga en ese momento y **esperar su confirmación**. El agente no crea
  cuentas ni maneja credenciales de ninguna forma.
- **Ningún cambio sin visto bueno.** Presentar los cambios **uno a uno**, con el texto exacto
  que se pondría, y aplicar solo los aprobados. Un «sí» a un cambio no vale para los demás.
- **Privacidad** (`PERFIL_CANDIDATO.md` §Reglas duras):
  - El **teléfono no se pone nunca en un perfil público** (LinkedIn, X, GitHub, web personal).
    Solo va en los CVs entregados y en formularios de solicitud concretos.
  - **Salario:** si el campo de pretensión salarial es opcional, dejarlo **vacío**. Si es
    obligatorio para poder guardar el perfil, **preguntar al usuario qué cifra poner** y usarla
    solo ahí. Nunca deducirla ni inventarla.
  - Lo cubierto por un NDA se menciona solo a alto nivel, sin detalles internos.
- **Nada inventado:** todo lo que se escriba tiene que estar en `PERFIL_CANDIDATO.md`. Si falta
  un dato, se le pregunta al usuario y se añade **antes** al perfil.

**Proceso por plataforma:**

1. Abrir el perfil del usuario en la plataforma, con la sesión ya iniciada.
2. Comparar **sección por sección** con `PERFIL_CANDIDATO.md`, usando el checklist del tipo de
   plataforma que corresponda (§5.2).
3. Redactar un informe corto con los cambios propuestos: qué hay ahora, qué se pondría y por
   qué. Agrupado por sección y ordenado por impacto.
4. Presentárselo al usuario y aplicar **solo** lo aprobado. Lo que prefiera hacer él a mano, se
   le deja indicado paso a paso.
5. Actualizar en `PLATAFORMAS.md`: `Perfil preparado: ✅ [fecha]` y, en `Notas:`, lo que quede
   pendiente de su parte.
6. Borrar el informe intermedio cuando los cambios estén aplicados (§7).

**En modo paralelo:** un subagente puede analizar cada plataforma y devolver su informe, pero
**en `PLATAFORMAS.md` escribe solo el orquestador**: es un archivo de estado.

---

### ▶ ETAPA 3 — BÚSQUEDA DE OFERTAS

**Objetivo:** encontrar ofertas relevantes y registrarlas en `OFERTAS.md`.

**Dónde buscar:** en las plataformas de `PLATAFORMAS.md`, **por orden de prioridad** (Alta →
Media → Baja). Esa lista manda; el catálogo de §5 solo sirve para recomendar plataformas
nuevas en la ETAPA 1. Si `PLATAFORMAS.md` está vacío, ejecutar antes la ETAPA 1.

**Proceso:**
1. Recorrer las plataformas aprobadas por prioridad, buscando con las preferencias de
   `PERFIL_CANDIDATO.md` y aplicando la regla de relevancia de §2. Según su `Acceso para
   el agente`:
   - **🟢 Libre** — buscar directamente.
   - **🟡 Requiere sesión iniciada** — pedirle al usuario que inicie sesión en ese momento y
     esperar, igual que en la ETAPA 5.
   - **🔴 Bloqueado** — no insistir: pasarle la búsqueda al usuario y seguir con la siguiente
     plataforma.
   - En las de tipo **red social · visibilidad** (X, comunidades), buscar publicaciones de
     ofertas y ofertas compartidas por reclutadores, no un buscador de empleo al uso.
2. Para cada oferta, añadir una entrada en `OFERTAS.md` con el formato de §6 (incluidos
   `Plataforma:` y `Acceso:`) y los campos de estado vacíos.
3. Al terminar con cada plataforma, actualizar su `Última búsqueda:` en `PLATAFORMAS.md`.
4. No generar CVs en esta etapa. Solo registrar ofertas.

---

### ▶ ETAPA 4 — GENERACIÓN DE CVs

**Objetivo:** generar un CV personalizado en PDF para cada oferta de `OFERTAS.md` sin CV.

**Proceso:**
1. Leer `OFERTAS.md` y filtrar ofertas con `CV generado:` vacío.
2. Preguntar al usuario si tiene habilidades adicionales relevantes para cada oferta (en modo
   paralelo, todas las preguntas juntas antes de lanzar los subagentes).
3. Para cada oferta: leer la descripción (y el link si hace falta) y generar el CV aplicando
   todas las reglas y el proceso de §3.
4. Actualizar `OFERTAS.md`: `CV generado: ✅ [nombre del archivo PDF]`.

---

### ▶ ETAPA 5 — APLICAR A LAS OFERTAS

**Objetivo:** aplicar a las ofertas que ya tienen CV pero no han sido solicitadas.

Si el usuario **no** ha encargado esta etapa al agente (Paso 0.3), el agente le entrega el link de
cada oferta + el PDF de su CV, y el usuario rellena `Aplicado manualmente:` cuando aplique.

**⚠️ Regla de inicio de sesión / registro — OBLIGATORIA:**
Si la plataforma requiere iniciar sesión o crear una cuenta, **pedir al usuario que lo haga en
ese momento** (dándole la URL) y esperar a que confirme; después aplica el agente. Solo si el
usuario indica que no puede hacerlo ahora, marcar `Aplicado: ⚠️ Pendiente usuario — [URL]`.
Actualizar también el campo `Cuenta:` de esa plataforma en `PLATAFORMAS.md`.

**⚠️ Regla de revisión de perfil — OBLIGATORIA:**
Antes de aplicar en una plataforma donde el usuario está registrado:
1. Si en `PLATAFORMAS.md` tiene `Perfil preparado: ✅` con fecha reciente, basta con comprobar
   que sigue siendo coherente con `PERFIL_CANDIDATO.md`.
2. Si no lo tiene, hacer la revisión de la **ETAPA 2** (checklist de §5.2) antes de inscribirse.
3. Si hay datos desactualizados, actualizarlos antes de enviar, **pidiendo confirmación al
   usuario** para cada cambio.
4. Solo después, proceder a inscribirse.

**Proceso:**
1. Leer `OFERTAS.md` y filtrar ofertas con `CV generado: ✅` y `Aplicado:` vacío.
2. Para cada una, seguir este orden de intento:
   a. Si tiene link de LinkedIn → intentar **LinkedIn Easy Apply**.
   b. Si no → acceder al link directo e intentar aplicar desde ahí.
   c. Subir el CV PDF generado para esa oferta cuando el formulario lo permita.
3. Registrar el resultado:
   - **Éxito:** `Aplicado: ✅ [web] — [fecha]`
   - **Fallo — bloqueante técnico:** `Aplicado: 🚫 Bloqueado — [motivo: Cloudflare, captcha, etc.]`
   - **Oferta expirada:** `Expirada / No válida: Sí — detectado por el agente [fecha]`
   - **No reintentar** la misma oferta si falla; registrar y continuar.

**Acción adicional — Contacto con RRHH/Recruiters:**
- Para cada oferta aplicada, buscar en LinkedIn a la persona de RRHH/recruiter de la empresa.
- Intentar conectar y enviar un mensaje personalizado con el interés en la oferta.
  **Pedir confirmación al usuario antes de enviar el mensaje.**

---

## 5. PLATAFORMAS — CATÁLOGO DE RECOMENDACIÓN Y CHECKLISTS DE PERFIL

Material de consulta para las ETAPAS 1 y 2. **No es la lista de plataformas del usuario**: esa
vive en `PLATAFORMAS.md` y es la única que manda al buscar.

### 5.1 Catálogo para recomendar (ETAPA 1)

Filtrar por el perfil del candidato: puesto, zonas, modalidad, idiomas y nivel. Recomendar
pocas y justificadas, nunca la tabla entera.

| Categoría | Cuándo encaja | Ejemplos |
|---|---|---|
| **Portales generalistas** | Siempre; son la base de cualquier búsqueda | LinkedIn Jobs, InfoJobs, Indeed |
| **Portales especializados en tecnología** | Perfiles técnicos: menos ruido y mejores filtros de stack | Tecnoempleo, Manfred, Wellfound, Landing.jobs |
| **Portales públicos y autonómicos** | Cuando la zona preferida tiene servicio de empleo propio; muchas de esas ofertas no llegan a los portales privados | Servicio de empleo de su comunidad, Empléate (SEPE), portales de diputación o ayuntamiento |
| **Remoto e internacional** | Si acepta remoto, o si puede trabajar en inglés | Remote OK, We Work Remotely, Otta, Welcome to the Jungle, Europe Language Jobs |
| **Prácticas, becas y primer empleo** | Perfiles junior, recién titulados o con poca experiencia | Portal de empleo de su universidad, Fundación Universidad-Empresa, programas trainee de grandes empresas |
| **Agregadores** | Para barrer rápido varias fuentes; ojo con duplicados y ofertas caducadas | Jooble, Talent.com, Glassdoor |
| **Webs de empresa y ATS** | Cuando hay empresas concretas de interés: la oferta suele estar ahí antes que en los portales | Página «Empleo / Careers» de la empresa, Greenhouse, Lever, Workday |
| **Redes sociales · visibilidad** | Para que las ofertas y los reclutadores lleguen solos; no se aplica desde ahí | X, LinkedIn como red, GitHub, comunidades de Discord/Telegram del sector |

Criterios al elegir:
- **Cobertura geográfica real:** un portal sin ofertas en las zonas del perfil no sirve, por
  mucho nombre que tenga.
- **Idioma:** si la plataforma exige un nivel que el candidato no tiene, decírselo.
- **Accesibilidad:** si la web bloquea la navegación automática (captcha, Cloudflare), sigue
  valiendo, pero se registra como 🔴 y aplica el usuario.
- **Esfuerzo de mantenimiento:** más plataformas es más trabajo por sesión. Mejor pocas y bien
  atendidas que quince abandonadas.

### 5.2 Checklists de preparación de perfil (ETAPA 2)

Comunes a todas: foto profesional coherente con `foto_perfil_circular.png`, nombre bien
escrito, ubicación según `PERFIL_CANDIDATO.md` (la de perfil, no la dirección postal),
**ningún teléfono en el perfil público** y nada que no esté en `PERFIL_CANDIDATO.md`.

**LinkedIn** (portal + red):
- Titular: el de `PERFIL_CANDIDATO.md`; nunca el puesto de una oferta concreta.
- «Acerca de»: versión corta del perfil profesional, con las tecnologías clave.
- Experiencia y formación: mismas fechas y mismos nombres que en el perfil.
- Aptitudes: fijar arriba las tres marcadas **F**; no listar las básicas.
- Idiomas y certificaciones al día.
- URL personalizada del perfil, la misma que aparece en el CV.
- «Open to work» según lo que quiera el usuario: solo reclutadores o público.
- Alertas de empleo creadas con los puestos y zonas prioritarias.

**X** (visibilidad, no aplicación):
- Bio con la identidad profesional y las tecnologías clave; ubicación; enlace a GitHub o web.
- Post fijado con el proyecto destacado, si el usuario quiere.
- Seguir cuentas y listas que publican ofertas del sector y de la zona.
- **Sin teléfono ni datos privados:** es una cuenta pública.
- **No publicar nada en su nombre sin confirmación explícita.**

**GitHub**:
- README de perfil con el titular, el stack y cómo contactar (email público, nunca teléfono).
- Repos destacados con descripción y README entendible; el proyecto destacado arriba.
- Foto y nombre reales; enlace al LinkedIn.

**Portales de empleo con CV propio** (InfoJobs, Tecnoempleo, portales corporativos):
- Rellenar el CV de la plataforma con los datos del perfil: es lo que filtran los reclutadores.
- Subir `CV_GENERICO.docx` (o su PDF) como adjunto por defecto.
- Preferencias de puesto, jornada y zona según `PERFIL_CANDIDATO.md`.
- Pretensión salarial: vacía si se puede; si es obligatoria, preguntar al usuario.

**Portales públicos y autonómicos**:
- Comprobar que la inscripción como demandante está activa y actualizada.
- Actualizar ocupaciones solicitadas y zona de búsqueda.
- Suelen pedir certificado digital o clave: **eso lo hace el usuario**.

**Agregadores y webs de empresa**: no tienen perfil que preparar. Marcar
`Perfil preparado: —` y, como mucho, crear la alerta de empleo correspondiente.

---

## 6. ARCHIVOS DE SEGUIMIENTO

### PLATAFORMAS.md — estructura
`PLATAFORMAS.md` es la fuente de verdad de **dónde** se busca. Lo rellena la ETAPA 1 y lo
mantienen las ETAPAS 2, 3 y 5. Cada entrada sigue este formato:

```markdown
## [N]. [Nombre de la plataforma]

- **Tipo:** Portal generalista / Portal tech / Portal público / Red social · visibilidad / Agregador / Web de empresa
- **URL:** [URL de inicio o de búsqueda ya filtrada]
- **Prioridad:** Alta / Media / Baja
- **Origen:** Usuario / Recomendada por el agente — [motivo]
- **Cuenta:** ✅ Tengo / 🟡 Por crear — [URL de registro] / ❌ No aplica
- **Acceso para el agente:** 🟢 Libre / 🟡 Requiere sesión iniciada / 🔴 Bloqueado — [motivo]
- **Perfil preparado:** ⏳ Pendiente / ✅ [YYYY-MM-DD] / — (no tiene perfil)
- **Aplica desde el agente:** Sí — [tipo de solicitud] / No — solo enlace
- **Última búsqueda:** YYYY-MM-DD
- **Notas:** 
```

Reglas de estado:
- **Prioridad** marca el orden de recorrido en la ETAPA 3.
- **Descartadas:** las plataformas rechazadas por el usuario van a la sección `DESCARTADAS`
  del final, con motivo y fecha. El agente **no vuelve a proponerlas** mientras sigan ahí.
- Una plataforma no se borra: o está activa, o está en DESCARTADAS.

### OFERTAS.md — estructura
`OFERTAS.md` es la fuente de verdad del estado de cada oferta. Cada entrada sigue este formato:

```markdown
## [N]. [Nombre del puesto] — [Empresa]

- **Plataforma:** [nombre tal como aparece en `PLATAFORMAS.md`]
- **Links:** [URL LinkedIn si existe] / [URL plataforma] / [URL web empresa]
- **Descripción:** Breve descripción del puesto y requisitos clave.
- **Localización:** [Ciudad / Remoto / Híbrido]
- **Modalidad:** [Presencial / Híbrido / Remoto]
- **Fecha encontrada:** YYYY-MM-DD
- **Acceso:** 🟢 Libre / 🟡 Requiere cuenta en [plataforma] — [URL] / 🔴 Bloqueado — [motivo]
- **CV generado:** 
- **Aplicado:** 
- **Aplicado manualmente:** 
- **Expirada / No válida:** 
```

### Campo `Aplicado manualmente:`
Exclusivo para que **el usuario** lo rellene cuando aplica por su cuenta.
- el agente **nunca** lo rellena automáticamente.
- Formato: `✅ [plataforma] — YYYY-MM-DD`. Basta con poner `Si`.
- **Regla de archivo:** al revisar `OFERTAS.md`, el agente debe **mover la oferta completa** a
  `OFERTAS_APLICADAS.md` y eliminarla de `OFERTAS.md` si:
  1. `Aplicado manualmente:` tiene contenido, **o**
  2. `Aplicado:` contiene `✅`.
  - Las ofertas en estado `⚠️ Pendiente usuario` o `🚫 Bloqueado` **no** se archivan.

### Campo `Expirada / No válida:`
Lo rellena el usuario cuando una oferta ya no es válida (expiró, no encaja, etc.), o el agente si
detecta en la ETAPA 5 que la oferta ha expirado.
- Basta con poner `Si` o un texto explicativo.
- **Regla de borrado:** si tiene contenido, el agente **elimina la oferta directamente** de
  `OFERTAS.md` sin archivarla.

### Leyenda del campo `Acceso:` (rellenar ya en ETAPA 3)
Por defecto, una oferta **hereda el `Acceso para el agente:` de su plataforma**. Solo se pone un
valor distinto si esa oferta concreta se comporta de otra forma (p. ej. la plataforma es 🟢
pero esa oferta redirige a un ATS con captcha).

| Icono | Significado | Qué pasa en la ETAPA 5 |
|---|---|---|
| 🟢 Libre | Se puede ver y aplicar sin cuenta | el agente aplica directamente |
| 🟡 Requiere cuenta | Necesita registro o inicio de sesión (indicar siempre la URL) | el agente pide al usuario que se registre/inicie sesión y luego aplica |
| 🔴 Bloqueado | Protección anti-bot activa (Cloudflare, captcha…) | El usuario aplica manualmente desde el navegador |

### PROCESOS_ACTIVOS.md — seguimiento de procesos de selección
Cuando el usuario comunique una respuesta, entrevista, prueba o cualquier avance de una oferta
aplicada, el agente crea o actualiza su bloque en `PROCESOS_ACTIVOS.md` con la plantilla
comentada del propio archivo: historial (✅), etapas pendientes (⏳) y `📅 EVENTOS_CALENDARIO`
con **fechas absolutas** y zona horaria. Actualizar también la tabla de fechas clave y la fecha
de "Hoy". Si el proceso termina, marcarlo como cerrado en su título.

---

## 7. LIMPIEZA PERIÓDICA DE ARCHIVOS

Al inicio de cada sesión, o cuando el usuario lo pida, el agente revisa la carpeta y elimina
archivos que ya no sean útiles:

| Tipo de archivo | Condición para eliminar |
|---|---|
| Informes de perfil de cualquier plataforma (LinkedIn, X, GitHub…) | Si el usuario ya aplicó los cambios al perfil (ETAPA 2) |
| Resúmenes o métricas de búsquedas antiguas | Si la info ya está en `OFERTAS.md` o `PERFIL_CANDIDATO.md` |
| Carpetas de trabajo `unpack_<tag>/` | Una vez generado el PDF |
| CVs en `CVs_OFERTAS/` | **Conservar siempre** |
| `PERFIL_CANDIDATO.md`, `INSTRUCCIONES_PROYECTO.md`, `PLATAFORMAS.md`, `OFERTAS.md`, `OFERTAS_APLICADAS.md`, `PROCESOS_ACTIVOS.md`, `README.md`, `AGENTS.md`, `grafo_dependencias.md` | **Conservar siempre** |
| Foto e imágenes de CV | **Conservar siempre** |
| `CV_GENERICO.docx` base | **Conservar siempre** |

**Regla general:** si un archivo fue un paso intermedio y su contenido ya está en un archivo
permanente, puede eliminarse. Ante la duda, preguntar al usuario antes de borrar.
