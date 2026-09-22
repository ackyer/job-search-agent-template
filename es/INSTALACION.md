[English](../en/INSTALL.md) · [Español](INSTALACION.md)

# Cómo poner esto en marcha

No hace falta saber programar ni haber usado GitHub nunca. Hay **dos formas**: la del
ordenador, que es la recomendada, y una alternativa para llevarlo desde el móvil.

## ¿Cuál elijo?

| | **A. En el ordenador** ⭐ | **B. Desde el móvil (con GitHub)** |
|---|---|---|
| Lo que necesitas | Un ordenador y 15 minutos | Una cuenta de GitHub, gratis |
| Entrevista inicial y tu perfil | ✅ | ✅ |
| Elegir dónde buscar | ✅ | ✅ |
| Generar los CV en PDF | ✅ instalando LibreOffice o con Word | ✅ ya viene todo puesto |
| Buscar ofertas | ✅ | ⚠️ solo las que se ven sin iniciar sesión |
| **Que aplique por ti** | ✅ con tus sesiones abiertas | ❌ no tiene tus sesiones iniciadas |
| Seguimiento de procesos | ✅ | ✅ |

> ### ⭐ Ve por la vía A
>
> En el ordenador funciona **todo**: busca con tus sesiones abiertas, genera los CV y se
> inscribe por ti. Es la que está probada de principio a fin.
>
> **La vía B es la alternativa** para quien no tenga ordenador a mano o necesite trabajar
> desde el móvil. Hace casi todo, pero las candidaturas acabas enviándolas tú.

---

# A. En el ordenador ⭐ (recomendada)

## Paso 1 — Descargar el proyecto

1. Abre la página del proyecto en GitHub.
2. Busca el botón verde que pone **`Code`**, arriba a la derecha de la lista de archivos.
3. Púlsalo y elige **`Download ZIP`**. Se te descargará un archivo comprimido.
4. Descomprímelo donde quieras tenerlo (el Escritorio vale):
   - **Windows:** clic derecho sobre el archivo → *Extraer todo…* → *Extraer*.
   - **Mac:** doble clic sobre el archivo y se descomprime solo.

Te queda una carpeta con todo dentro.

## Paso 2 — Quedarte con un solo idioma

Dentro verás dos carpetas, `es` y `en`. **Borra la que no vayas a usar.** No es obligatorio,
pero si dejas las dos el agente tiene que preguntarte cada vez cuál usar.

La carpeta que te quedes **es tu proyecto**: ahí dentro trabajarás.

## Paso 3 — Instalar Claude

La forma más sencilla, sin tocar ninguna terminal:

1. Entra en **claude.ai/download** e instala la aplicación de escritorio.
2. Ábrela e inicia sesión con tu cuenta de Claude.
3. Dile que abra la carpeta de tu proyecto (la del paso 2).

> Necesitas un plan de pago de Claude. El proyecto es gratis, pero el agente que lo mueve no.

<details>
<summary>Si prefieres la terminal</summary>

Con Node.js instalado:

```bash
npm install -g @anthropic-ai/claude-code
cd ruta/a/tu/carpeta
claude
```

Los comandos de instalación cambian de vez en cuando; la fuente fiable es la documentación
oficial de Claude Code.
</details>

> ¿Usas otro agente (Codex, Cursor, Gemini CLI, Copilot…)? Vale igual: ábrelo en esa carpeta.
> Lo único imprescindible es que pueda **leer y escribir archivos** en ella.

## Paso 4 — ¿No tienes CV, o el que tienes no te convence?

No pasa nada: **el propio proyecto te lo hace**. Cuando llegue el momento de pedirte el CV,
dile una de estas dos cosas:

> **No tengo CV, ayúdame a crearlo**
>
> **Mi CV está anticuado, ayúdame a rehacerlo**

Con lo que le has contado en la entrevista te monta uno en Word desde cero, o reescribe el que
ya tienes. Ese archivo pasa a ser tu plantilla base, y a partir de ahí el proyecto funciona
igual: la copia y la adapta a cada oferta sin tocar el diseño.

> Un CV hecho así sale correcto y limpio, pero sobrio. Si quieres un diseño más trabajado,
> puedes partir de una plantilla de Word que te guste y pedirle que rellene los textos.

## Paso 5 — Para los PDF: LibreOffice

El proyecto coge tu CV de Word, le cambia los textos y lo convierte a PDF sin tocar el diseño.
Para esa conversión hace falta **Microsoft Word** o **LibreOffice** en el ordenador.

Si no tienes Word: entra en **libreoffice.org/download**, descárgalo e instálalo. Es gratis y
no hay que configurar nada: con tenerlo instalado basta.

## Paso 6 — Arrancar

Con la carpeta abierta en Claude, escribe:

> **Inicia el proyecto**

Y ya está. Te irá preguntando por tus datos, te pedirá tu CV y tu foto, y se pondrá a trabajar.

---

# B. Desde el móvil, con GitHub (segunda opción)

Esta vía es para cuando **no tienes ordenador disponible** o necesitas llevar la búsqueda
desde el móvil. El proyecto vive en tu propia cuenta de GitHub y Claude trabaja sobre él desde
internet, sin que tengas nada encendido.

## Paso 1 — Cuenta de GitHub

Si no tienes: entra en **github.com**, pulsa *Sign up* y sigue los pasos. Es gratis y solo
pide un correo.

## Paso 2 — Hacer tu copia del proyecto

En la página del proyecto verás arriba a la derecha uno de estos dos botones:

- **`Use this template`** → *Create a new repository*. Es el mejor: te da una copia limpia.
- Si no aparece, usa **`Fork`**, que hace lo mismo con otro nombre.

Te pedirá un nombre para tu copia. Ponle el que quieras.

> ### ⚠️ Ponlo en **privado**
>
> En esa pantalla hay una opción **Public / Private**: elige **Private**.
>
> Tu copia va a contener tu nombre, tu teléfono, tu historial laboral y tu CV. En público, eso
> lo ve cualquiera. Con `Fork` no siempre se puede elegir: si tu copia sale pública y vas a
> meter datos personales, bórrala y usa `Use this template` en privado.

## Paso 3 — Abrir Claude sobre tu copia

1. Entra en **claude.ai/code** desde el navegador del móvil, o abre la app de Claude y ve a la
   sección **Code**.
2. Conecta tu cuenta de GitHub cuando te lo pida y dale permiso sobre tu copia del proyecto.
3. Crea una sesión eligiendo ese repositorio.

## Paso 4 — Arrancar

Escribe en el chat:

> **Inicia el proyecto**

Te entrevistará, rellenará los archivos y trabajará dentro de tu repositorio.

## Paso 5 — Que no se pierda nada

Las sesiones en la nube son temporales: **lo que no se guarde en tu repositorio se pierde.**
Cuando termines una tanda, dile:

> **Guarda los cambios en GitHub**

Así tus ofertas, tu perfil y tus CV quedan a salvo en tu copia, y la siguiente sesión sigue
donde lo dejaste.

## Lo que no podrá hacer por esta vía

Aplicar por ti. Para inscribirte en LinkedIn o InfoJobs hace falta tu sesión iniciada en esas
webs, y ahí Claude no la tiene. Lo que hará es dejarte **el enlace de la oferta y el CV
generado** listos para que apliques tú en dos minutos.

---

## Si algo falla

| Lo que ves | Qué pasa |
|---|---|
| «No encuentro el CV» | El archivo tiene que llamarse `CV_GENERICO.docx` y estar en la carpeta del idioma. Si tu CV es un PDF, pídele a Claude que te ayude a pasarlo a Word |
| El PDF no se genera | Falta LibreOffice o Word. Paso 4 de la vía A |
| Abre pero no sabe qué hacer | Dile: «lee `AGENTS.md` y sigue esas instrucciones» |
| Una web no le deja aplicar | Normal: algunas bloquean los envíos automáticos. Te dará el enlace para que lo hagas tú |

### ¿Sigue sin funcionar?

Dos vías, la que te sea más cómoda:

- **Abre una *issue*** en el repositorio (pestaña *Issues* → *New issue*) contando qué has
  hecho y qué te sale. Así queda público y le sirve al siguiente que se atasque.
- **Escríbeme directamente** por LinkedIn: [www.linkedin.com/in/anderakierayucar](https://www.linkedin.com/in/anderakierayucar)

No hace falta que sepas explicarlo en términos técnicos: cuéntalo como lo dirías por teléfono,
con una captura si puedes.
