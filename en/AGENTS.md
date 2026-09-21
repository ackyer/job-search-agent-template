# AGENTS.md

Guidance for any coding agent (Claude Code, Codex, Cursor, Gemini CLI…) working with this
project. **This file is canonical for the English copy**: `/CLAUDE.md` and `/GEMINI.md` at the
repository root point at the language folders. Edit rules here only.

If your tool doesn't read any of these by default, tell it to read this file at the start of
the session.

## What this project is

Not a software codebase — a **personal job-application workflow**. The agent is the operator.
The "code" is markdown specs that drive the agent's behaviour plus a Word CV template that gets
personalised per job.

## Source-of-truth files — read first

Always read these at session start; they take precedence over this file:

- `PROJECT_INSTRUCTIONS.md` — the full operating manual (onboarding, 5-stage workflow, CV
  rules, file-state machine, cleanup policy). **Authoritative.**
- `CANDIDATE_PROFILE.md` — candidate data and search preferences. Single source of truth for
  any CV content or form field. Never hardcode candidate info from memory.
- `PLATFORMS.md` — the approved list of platforms to search, and their per-platform state.
  Single source of truth for **where** to search; never search somewhere that isn't listed.
- `JOBS.md` — active jobs and their state. `JOBS_APPLIED.md` — archive.
- `ACTIVE_PROCESSES.md` — live state of every open selection process (interviews, tests,
  calendar events). The agent keeps it up to date from what the user reports.

## Entry point — «Start the project»

When the user says **«Start the project»** (or "let's go", "set it up", "begin"…), run
`PROJECT_INSTRUCTIONS.md` §0 before anything else: detect missing configuration, interview the
user and fill the files for them, then ask which stages to run and sequential vs parallel.

## Critical rules (details in the § referenced)

- **CV pipeline (§3):** never build a CV PDF from scratch (reportlab or similar). Copy
  `GENERIC_CV.docx` → unpack → edit `word/document.xml` text nodes → repack → PDF with
  LibreOffice or MS Word COM. Formatting is never touched; 1 page A4; both `.docx` and `.pdf`
  go to `CVs_JOBS/`.
- **CV content (§3):** the subtitle is never the literal job title; "basic" skills only if the
  ad asks, phrased as "familiar with X"; never invent experience.
- **Platforms (§4 STAGE 1):** search only what `PLATFORMS.md` lists, in priority order.
  Recommendations come from the §5 catalogue filtered by the candidate's own profile, each with
  a one-line reason; rejected platforms go to `DISCARDED` and are never proposed again.
- **Profiles (§4 STAGE 2, optional):** never create accounts or handle credentials — the user
  logs in and confirms. Present profile changes one by one and apply only the approved ones.
  Never put the phone number on a public profile; leave the salary field empty unless it is
  mandatory, and then ask the user for the figure.
- **Applying (§4):** if a platform needs login or sign-up, ask the user to do it now and wait;
  review the platform profile against `CANDIDATE_PROFILE.md` before applying; never retry a
  failed application; confirm with the user before sending any recruiter message.
- **File states (§6):** on every pass over `JOBS.md`, archive jobs with `Applied: ✅` or a
  filled `Applied manually:`, and delete jobs with a filled `Expired / Invalid:`.
  `PLATFORMS.md`, `JOBS.md`, `JOBS_APPLIED.md`, `ACTIVE_PROCESSES.md` and
  `CANDIDATE_PROFILE.md` are state files: helpers propose, **only the orchestrator writes**,
  one writer at a time.
- **Privacy (`CANDIDATE_PROFILE.md` §Hard rules):** phone only on delivered CVs and application
  forms; never disclose salary expectations in initial filters; respect NDAs.

## Session-start checklist

1. Read `PROJECT_INSTRUCTIONS.md` and `CANDIDATE_PROFILE.md`.
2. If any searching is about to happen and `PLATFORMS.md` is empty, run STAGE 1 first.
3. Sweep `JOBS.md` and apply the §6 archive/delete rules before doing any new work.
4. Run the cleanup criteria in `PROJECT_INSTRUCTIONS.md` §7.
5. If you change the onboarding flow or the file set, update `README.md` (end-user guide).

## A note on language

The Spanish copy of this template lives in `/es` and is the reference version: if the two ever
disagree, `/es` wins. Working language with the user is whatever they write in.
