[English](dependency_graph.md) · [Español](../es/grafo_dependencias.md)

# Dependency graph of the files

> A map of which file rules what, who reads whom, and what each stage of the flow writes.
> Handy when you want to adapt the template, and for avoiding the same rule written twice.

## 1. Who reads whom

![Structure of the template: PROJECT_INSTRUCTIONS.md at the centre as the authority, surrounded by AGENTS.md, README.md and the five state files, with CLAUDE.md and GEMINI.md as pointers](structure_graph.svg)

At the centre, `PROJECT_INSTRUCTIONS.md`, drawn with a double circle: it is the authority and
everything else references it instead of repeating its content. The thick-stroked vertex is
`AGENTS.md`, what the agent reads when it starts. The grey-filled ones are the state files it
writes by itself as it works. The dashed ones are yours: `CANDIDATE_PROFILE.md`, which you fill
in at the start, and `README.md`, which is for you and not for the agent. The two small dotted
ones are `/CLAUDE.md` and `/GEMINI.md`, which sit **at the repository root**: one line each,
redirecting to `AGENTS.md` so every tool finds its own filename.

The thick edges are the path the work takes: your data feeds the platforms, the platforms feed
the jobs, and the jobs feed the archive and the open processes. The thin ones are references:
who mentions whom.

**The golden rule:** `PROJECT_INSTRUCTIONS.md` rules and `CANDIDATE_PROFILE.md` is the only
source of the candidate's data. If you add a rule, put it in one place and have the rest
reference it.

## 2. What each stage writes

![The five stages in a row, with arrows to the files each one writes](stages_graph.svg)

Stages 1 and 2 are preparation: without `PLATFORMS.md` there is no searching, and stage 2 is
optional. Stages 3 to 5 are the cycle you repeat whenever you want more jobs. Dashed arrows
are fields a stage updates along the way, like the last-search date.

## 3. What isn't in the repository and you need anyway

| File | You provide it | What for |
|---|---|---|
| `GENERIC_CV.docx` | Yes, at setup | The CV template that gets copied and personalised for each job. Its design is never touched |
| `profile_photo_circular.png` | Yes, at setup | The photo on the CV |
| `CVs_JOBS/` | The agent creates it | Where the `.docx` and `.pdf` for each job end up |

All three are in `.gitignore`: they're yours and shouldn't end up in a public repository.
