# 🤖 Búsqueda de Empleo Automática con un Agente de IA

Esta es una **plantilla de proyecto** para automatizar tu búsqueda de empleo con el agente de
IA que ya uses. La idea es sencilla: tú apenas tocas nada; **el agente hace el trabajo** (busca
ofertas, genera un CV personalizado para cada una y aplica por ti), guiado por los archivos de
instrucciones que hay en esta carpeta.

> Este proyecto **no es software**: es un conjunto de archivos de texto (markdown) que
> le dicen al agente cómo comportarse, más un CV base en Word que se personaliza para
> cada oferta.

---

## 🧩 Con qué funciona

Cualquier agente de IA que sepa **leer y escribir archivos** en esta carpeta: Claude Code,
Codex, Cursor, Gemini CLI, Copilot… Las reglas viven en `AGENTS.md`, que es el archivo que
casi todos buscan; `CLAUDE.md` y `GEMINI.md` solo apuntan ahí. Si el tuyo no lee ninguno de
los tres, dile al empezar: «lee `AGENTS.md` y sigue esas instrucciones».

Qué necesita tu agente para cada parte:

| Para… | Necesita |
|---|---|
| Buscar ofertas y aplicar | Poder **navegar por internet**. Si el tuyo no navega, le pasas tú las ofertas y él hace el resto |
| Generar los CVs | Poder **ejecutar comandos** y tener **LibreOffice** o **Microsoft Word** instalado |
| Llevar el seguimiento | Nada especial: son archivos de texto |

---

## 🚀 Puesta en marcha (solo di «Inicia el proyecto»)

No tienes que rellenar los archivos a mano. El arranque es automático:

1. **Copia esta carpeta** a donde quieras tener tu proyecto y ábrela con tu agente (Claude Code, Codex, Cursor, Gemini CLI…).
2. **Ten a mano tu CV** (en Word, con el diseño que te guste) y una **foto de perfil**.
3. Escríbele a tu agente: **«Inicia el proyecto»**.

A partir de ahí, **el agente se encarga de todo**:

- Detecta que el proyecto está vacío y **te entrevista** preguntándote, por bloques, todo lo
  que necesita: contacto, formación, experiencia, habilidades, idiomas, certificaciones y tus
  **preferencias** de puesto y zona. Con tus respuestas **rellena él mismo**
  `PERFIL_CANDIDATO.md`.
- Te **pide tu CV y tu foto**, los renombra a `CV_GENERICO.docx` y `foto_perfil_circular.png`
  y los deja listos. El agente **nunca** rehace el diseño de tu CV: lo copia y solo cambia los
  textos para cada oferta, así que el resultado siempre conserva tu diseño.
- Te pregunta **dónde quieres buscar**: tú le dices las webs que ya usas y **él te recomienda
  otras** que encajen con tu perfil y tu zona, con el motivo de cada una. La lista aprobada
  queda en `PLATAFORMAS.md`.
- Si quieres, **te prepara el perfil** en esas plataformas (LinkedIn, X, GitHub, InfoJobs…):
  lo compara con tus datos, te propone los cambios uno a uno y aplica solo los que apruebes.
  Es opcional y nunca toca nada sin tu visto bueno.
- Te pregunta **de qué fases quieres que se encargue** (las 5 o solo algunas) y **si quieres
  ejecutarlas en paralelo o de una en una**.
- Se pone a trabajar.

> ✍️ Si prefieres rellenar los archivos tú mismo antes de empezar, también puedes: edita
> `PERFIL_CANDIDATO.md` y pon tu `CV_GENERICO.docx` y `foto_perfil_circular.png` en la
> carpeta. Pero no hace falta: con «Inicia el proyecto» el agente te guía.

### ⚡ Secuencial vs. Paralelo

Cuando el agente te pregunte el modo de ejecución:

- **Secuencial** — procesa una oferta tras otra. Más lento, más fácil de supervisar, más
  barato. Ideal si hay pocas ofertas o quieres revisar sobre la marcha.
- **Paralelo** — lanza varios ayudantes a la vez, p. ej. un CV por ayudante, si tu herramienta
  sabe hacerlo. Mucho más rápido con muchas ofertas. Si además puedes elegir modelo, usará
  **el más capaz para las decisiones importantes** (valorar si una oferta encaja, redactar el
  perfil del CV, mensajes a reclutadores…) y **uno más rápido para lo mecánico** (convertir a
  PDF, mover archivos, actualizar estados). Así vas rápido sin disparar el coste.

---

## 📂 Qué es cada archivo

| Archivo | Para qué sirve | ¿Lo edito yo? |
|---|---|---|
| `README.md` | Este archivo: guía de uso. | No |
| `PERFIL_CANDIDATO.md` | **Tus datos** (contacto, experiencia, skills…) y **preferencias** de búsqueda. Fuente de verdad para los CVs. | Lo rellena el agente al iniciar (o tú, si prefieres) |
| `INSTRUCCIONES_PROYECTO.md` | Manual completo de cómo trabaja el agente: **§0 arranque automático**, flujo en 5 etapas, reglas de CV, limpieza. | No |
| `AGENTS.md` | **Las reglas que lee tu agente.** Es el archivo canónico: resumen del arranque, reglas críticas y checklist de sesión. | No |
| `CLAUDE.md` · `GEMINI.md` | Punteros de una línea a `AGENTS.md`, para las herramientas que buscan su propio nombre de archivo. | No |
| `PLATAFORMAS.md` | **Dónde buscar**: la lista de webs aprobada por ti, con el estado de cada una (¿tengo cuenta?, ¿perfil preparado?). La rellenáis entre los dos en la ETAPA 1. | Lo gestiona el agente contigo |
| `OFERTAS.md` | Lista **viva** de ofertas encontradas y su estado. La rellena el agente. | Lo gestiona el agente |
| `OFERTAS_APLICADAS.md` | Archivo histórico de ofertas ya aplicadas. El agente mueve aquí las terminadas. | Lo gestiona el agente |
| `PROCESOS_ACTIVOS.md` | Seguimiento de entrevistas y procesos de selección en curso. | Lo gestiona el agente / tú |

---

## 🔄 Cómo trabaja el agente (flujo en 5 etapas)

1. **Elegir dónde buscar** — tú le dices en qué webs buscas ya y él te recomienda otras según
   tu perfil, tu zona y tu idioma, explicando por qué cada una. Lo aprobado queda en
   `PLATAFORMAS.md`; lo que descartes no te lo vuelve a proponer. Sin esta lista no se busca.
2. **Preparar tu perfil** *(opcional)* — repasa tu perfil en cada plataforma (LinkedIn, X,
   GitHub, InfoJobs…) contra tus datos y te propone mejoras **una a una**. Solo aplica las que
   apruebes, nunca crea cuentas ni te pide contraseñas, y jamás pone tu teléfono en un perfil
   público.
3. **Búsqueda** — el agente recorre tus plataformas por orden de prioridad y apunta las ofertas
   en `OFERTAS.md`. Todavía no genera CVs.
4. **Generación de CVs** — para cada oferta sin CV, el agente copia tu `CV_GENERICO.docx`,
   adapta los textos a la oferta (idioma, habilidades, subtítulo…) y lo convierte a PDF
   en la carpeta `CVs_OFERTAS/`.
5. **Aplicar** — el agente intenta inscribirte (LinkedIn "Solicitud sencilla" primero, luego
   el enlace directo) y marca el resultado en `OFERTAS.md`. Si una web pide iniciar sesión o
   registrarte, te pedirá que lo hagas en ese momento y seguirá él. Si no le encargas esta
   fase, te da el enlace y el PDF para que apliques tú.

Tú puedes pedirle cualquier etapa por separado, o dejar que las haga todas seguidas.

---

## ✍️ Cosas que tienes que tener a mano (una sola vez)

Con «Inicia el proyecto» el agente te lo pregunta y lo rellena por ti, pero ten preparado:

- [ ] Tu **CV** en Word con el diseño que quieras conservar (el agente lo llamará `CV_GENERICO.docx`).
- [ ] Una **foto de perfil** (el agente la recorta en círculo → `foto_perfil_circular.png`).
- [ ] Tus datos: contacto, formación, experiencia, habilidades, idiomas, certificaciones.
- [ ] Tus **preferencias**: qué puestos y qué zonas te interesan.
- [ ] Saber **en qué webs de empleo tienes cuenta** ya creada (LinkedIn, InfoJobs…). No hace
      falta la contraseña: el agente nunca te la pide; cuando haga falta entrar, te avisa para que
      inicies sesión tú.

---

## 💡 Consejos

- **Habla con tu agente en tu idioma normal.** No hacen falta comandos: "genera los CVs que
  falten", "aplica a las ofertas que ya tengan CV", "búscame más ofertas de Data Engineer".
- **Tú tienes la última palabra.** El agente aplica a las ofertas por sí solo, pero te pide
  confirmación antes de enviar mensajes a reclutadores o hacer cambios importantes en tus
  perfiles (LinkedIn, InfoJobs…).
- **Mantén `PERFIL_CANDIDATO.md` actualizado.** Si cambias de nivel en una skill o añades
  experiencia, edítalo ahí y todos los CVs futuros lo reflejarán.
- **Requisito para pasar de Word a PDF:** el equipo necesita tener **Microsoft Word** o
  **LibreOffice** instalado (el agente usa uno de los dos para exportar el PDF conservando el
  diseño). Está explicado en `INSTRUCCIONES_PROYECTO.md`, sección 3.

---

## 🔒 Un aviso sobre tus datos

`PERFIL_CANDIDATO.md` va a contener tu nombre, tu teléfono y tu historial profesional. El
`.gitignore` ya evita que se suban tu CV, tu foto y los CVs generados, **pero ese archivo sí
se sube** si publicas tu copia. Si vas a trabajar en un repositorio público, quítalo del
control de versiones antes:

```bash
git rm --cached PERFIL_CANDIDATO.md && echo "PERFIL_CANDIDATO.md" >> .gitignore
```

---

¡Suerte con la búsqueda! 🍀
