[English](../en/REQUIREMENTS.md) · [Español](REQUISITOS.md)

# Requisitos

Este proyecto **no es un programa**: son archivos de texto que le dicen a un agente de IA cómo
llevar tu búsqueda de empleo. No hay nada que compilar ni dependencias que instalar.

## Imprescindible

| | Para qué |
|---|---|
| **Un agente de IA que lea y escriba archivos** | Es quien hace el trabajo. Claude Code, Codex, Cursor, Gemini CLI, Copilot… |
| **Tu CV en Word (`.docx`)** | Se copia y se le cambian los textos para cada oferta. Su diseño no se toca nunca. **¿No tienes, o quieres rehacerlo? Te lo hace el propio proyecto** |
| **Una foto de perfil** | Va en el CV. Cualquier formato de imagen vale |
| **20–30 minutos la primera vez** | La entrevista inicial: tus datos, tu experiencia, tus preferencias |

Si tu CV solo lo tienes en PDF, pídele al agente que te ayude a convertirlo a Word antes de
empezar: necesita un `.docx` editable.

**Y si no tienes CV, o el que tienes se te ha quedado viejo, no lo busques fuera:** díselo al
empezar («no tengo CV, ayúdame a crearlo» o «ayúdame a rehacerlo») y te lo monta con lo que
le cuentes en la entrevista inicial. Ese archivo pasa a ser tu plantilla base.

## Según lo que quieras que haga

| Quiero que… | Necesito además |
|---|---|
| …genere los CV en PDF | **LibreOffice** (gratis, libreoffice.org) o **Microsoft Word** instalado |
| …busque ofertas por su cuenta | Que el agente pueda **navegar por internet** |
| …aplique por mí | Lo anterior + tener **la sesión iniciada** en los portales, en el mismo navegador |
| …me prepare los perfiles | Cuentas en las plataformas donde quieras estar (LinkedIn, portales de empleo…) |
| …lo lleve desde el móvil | Una cuenta de **GitHub** gratuita. Ver `INSTALACION.md`, vía B |

Nada de esto es obligatorio para empezar. Sin navegación, el agente sigue sirviendo para
organizar la búsqueda, escribir los CV y llevar el seguimiento: le pasas tú las ofertas.

## Lo que NO hace falta

- **Saber programar.** Ni una línea.
- **Python, Node ni ninguna dependencia.** No hay `requirements.txt` que instalar porque no
  hay código que ejecutar.
- **Saber usar GitHub**, si descargas el ZIP.
- **Pagar por el proyecto.** Es gratis y libre.

## El coste real

El proyecto no cuesta nada; **el agente que lo mueve, sí**. Trabajar con Claude Code, por
ejemplo, requiere un plan de pago.

Y hay un detalle práctico: generar veinte CV personalizados consume bastante cuota. Si tu plan
es ajustado, ve por tandas de cinco o seis ofertas en vez de lanzarlo todo de golpe. El propio
manual trae un modo secuencial pensado para eso.

## Compatibilidad

Funciona con cualquier agente capaz de leer y escribir archivos en una carpeta. Las reglas
viven en `AGENTS.md`, que es el archivo que casi todos buscan solos; `/CLAUDE.md` y
`/GEMINI.md` apuntan ahí.

Si el tuyo no lee ninguno, empieza la conversación con:

> lee `AGENTS.md` y sigue esas instrucciones

Lo que cambia de un agente a otro no son las reglas, sino **cuánto puede hacer solo**: si el
tuyo no navega, tú le pasas las ofertas; si no ejecuta comandos, tú conviertes los CV a PDF.
El resto funciona igual.

## ¿Dudas?

Abre una *issue* en el repositorio o escríbeme por LinkedIn: [www.linkedin.com/in/anderakierayucar](https://www.linkedin.com/in/anderakierayucar)
