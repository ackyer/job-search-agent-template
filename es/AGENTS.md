# AGENTS.md

Guidance for any coding agent (Claude Code, Codex, Cursor, Gemini CLI…) working with this
project. **This file is canonical for the Spanish copy**: `/CLAUDE.md` and `/GEMINI.md` at the
repository root point at the language folders. Edit rules here only.

If your tool doesn't read any of these by default, tell it to read this file at the start of
the session.

User-facing language for this copy is **Spanish**. The English copy lives in `/en`. This one,
`/es`, is the reference version: if the two ever disagree, `/es` wins.

## What this project is

Not a software codebase — a **personal job-application workflow**. The agent is the operator.
The "code" is markdown specs that drive the agent's behaviour plus a Word CV template that gets
personalised per job offer.

User-facing language is **Spanish** by default.

## Source-of-truth files — read first

Always read these at session start; they take precedence over this file:

- `INSTRUCCIONES_PROYECTO.md` — the full operating manual (onboarding, 5-stage workflow, CV
  rules, file-state machine, cleanup policy). **Authoritative.**
- `PERFIL_CANDIDATO.md` — candidate data and search preferences. Single source of truth for
  any CV content or form field. Never hardcode candidate info from memory.
- `PLATAFORMAS.md` — the approved list of platforms to search, and their per-platform state.
  Single source of truth for **where** to search; never search somewhere that isn't listed.
- `OFERTAS.md` — active job offers and their state. `OFERTAS_APLICADAS.md` — archive.
- `PROCESOS_ACTIVOS.md` — live state of every open selection process (interviews, tests,
  calendar events). The agent keeps it up to date from what the user reports.

## Entry point — «Inicia el proyecto»

When the user says **«Inicia el proyecto»** (or "empezar", "arranca", "vamos"…), run
`INSTRUCCIONES_PROYECTO.md` §0 before anything else: detect missing configuration, interview
the user and fill the files for them, then ask which stages to run and sequential vs parallel.

## Critical rules (details in the § referenced)

- **CV pipeline (§3):** never build a CV PDF from scratch (reportlab or similar). Copy
  `CV_GENERICO.docx` → unpack → edit `word/document.xml` text nodes → repack → PDF with
  LibreOffice or MS Word COM. Formatting is never touched; 1 page A4; both `.docx` and `.pdf`
  go to `CVs_OFERTAS/`.
- **CV content (§3):** subtitle is never the literal offer title; "basic" skills only if the
  offer asks, phrased as "conocimientos de X"; never invent experience.
- **Platforms (§4 ETAPA 1):** search only what `PLATAFORMAS.md` lists, in priority order.
  Recommendations come from the §5 catalogue filtered by the candidate's own profile, each with
  a one-line reason; rejected platforms go to `DESCARTADAS` and are never proposed again.
- **Profiles (§4 ETAPA 2, optional):** never create accounts or handle credentials — the user
  logs in and confirms. Present profile changes one by one and apply only the approved ones.
  Never put the phone number on a public profile; leave the salary field empty unless it is
  mandatory, and then ask the user for the figure.
- **Applying (§4):** if a platform needs login or sign-up, ask the user to do it now and wait;
  review the platform profile against `PERFIL_CANDIDATO.md` before applying; never retry a
  failed application; confirm with the user before sending any recruiter message.
- **File states (§6):** on every pass over `OFERTAS.md`, archive offers with `Aplicado: ✅` or
  a filled `Aplicado manualmente:`, and delete offers with a filled `Expirada / No válida:`.
  `PLATAFORMAS.md`, `OFERTAS.md`, `OFERTAS_APLICADAS.md`, `PROCESOS_ACTIVOS.md` and
  `PERFIL_CANDIDATO.md` are state files: subagents propose, **only the orchestrator writes**,
  one writer at a time.
- **Privacy (`PERFIL_CANDIDATO.md` §Reglas duras):** phone only on delivered CVs and
  application forms; never disclose salary expectations in initial filters; respect NDAs.

## Session-start checklist

1. Read `INSTRUCCIONES_PROYECTO.md` and `PERFIL_CANDIDATO.md`.
2. If any searching is about to happen and `PLATAFORMAS.md` is empty, run ETAPA 1 first.
3. Sweep `OFERTAS.md` and apply the §6 archive/delete rules before doing any new work.
4. Run the cleanup criteria in `INSTRUCCIONES_PROYECTO.md` §7.
5. If you change the onboarding flow or the file set, update `README.md` (end-user guide).
