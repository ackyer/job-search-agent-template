# AGENTS.md — language router

This repository ships **two complete copies** of the same template, one per language:

- `es/` — Spanish. **The reference version**: if the two ever disagree, `es/` wins.
- `en/` — English.

## What to do when you open this repository

1. **Pick the language** the user writes in, or ask them if it isn't obvious.
2. **Read `es/AGENTS.md` or `en/AGENTS.md`** and follow it. That file points at the operating
   manual and the state files for that language.
3. **Work inside that folder only.** The state files (jobs, platforms, profile) live there.
4. Suggest to the user, once, that they **delete the folder they don't use**: two copies of
   the rules are two things to keep in sync, and only one of them is being updated.

Never mix files across the two folders: the field names inside them (`Applied:` vs
`Aplicado:`) are literals the manual depends on.

`CLAUDE.md` and `GEMINI.md` at the root point here, so tools that look for their own filename
land in the same place.
