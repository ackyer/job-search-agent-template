[English](README.md) · [Español](../es/README.md)

# 🤖 Automated Job Search with an AI Agent

This is a **project template** for automating your job search with whichever AI agent you
already use. The idea is simple: you barely touch anything; **the agent does the work** (finds
jobs, generates a tailored CV for each one and applies for you), guided by the instruction
files in this folder.

> This project **is not software**: it's a set of text files (markdown) telling the agent how
> to behave, plus a base CV in Word that gets personalised for each job.

---

## 🧩 What it works with

Any AI agent that can **read and write files** in this folder: Claude Code, Codex, Cursor,
Gemini CLI, Copilot… The rules live in `AGENTS.md`, the file almost all of them look for. If
yours reads none of them, just say at the start: "read `AGENTS.md` and follow those
instructions".

What your agent needs for each part:

| For… | It needs |
|---|---|
| Finding jobs and applying | To be able to **browse the web**. If yours can't browse, you hand it the ads and it does the rest |
| Generating the CVs | To be able to **run commands**, with **LibreOffice** or **Microsoft Word** installed |
| Keeping track | Nothing special: they're text files |

---

## 🚀 Getting started (just say «Start the project»)

You don't have to fill the files in by hand. Setup is automatic:

1. **Copy this folder** wherever you want your project and open it with your agent (Claude
   Code, Codex, Cursor, Gemini CLI…).
2. **Have your CV handy** (in Word, with the design you like) and a **profile photo**.
3. Tell your agent: **«Start the project»**.

From there, **the agent handles everything**:

- It notices the project is empty and **interviews you**, block by block, for everything it
  needs: contact details, education, experience, skills, languages, certifications and your
  **preferences** on roles and areas. With your answers it **fills in**
  `CANDIDATE_PROFILE.md` itself.
- It **asks for your CV and photo**, renames them to `GENERIC_CV.docx` and
  `profile_photo_circular.png` and gets them ready. The agent **never** redesigns your CV: it
  copies it and only changes the text for each job, so the result always keeps your design.
- It asks **where you want to search**: you name the sites you already use and **it recommends
  others** that fit your profile and your area, with a reason for each. The approved list ends
  up in `PLATFORMS.md`.
- If you want, it **prepares your profiles** on those platforms (LinkedIn, X, GitHub, job
  boards…): it compares them against your data, proposes changes one by one and applies only
  the ones you approve. It's optional and it never touches anything without your say-so.
- It asks **which stages you want it to handle** (all five or just some) and **whether to run
  them in parallel or one at a time**.
- It gets to work.

> ✍️ If you'd rather fill the files in yourself before starting, you can: edit
> `CANDIDATE_PROFILE.md` and drop your `GENERIC_CV.docx` and `profile_photo_circular.png` into
> the folder. But you don't have to: «Start the project» walks you through it.

### ⚡ Sequential vs. parallel

When the agent asks about the execution mode:

- **Sequential** — one job after another. Slower, easier to supervise, cheaper. Ideal when
  there are few jobs or you want to review as you go.
- **Parallel** — it launches several helpers at once, e.g. one CV per helper, if your tool can
  do that. Much faster with many jobs. If you can also pick a model, it will use **the most
  capable one for the important decisions** (judging whether a job fits, writing the CV
  summary, messages to recruiters…) and **a faster one for the mechanical parts** (converting
  to PDF, moving files, updating state). Fast without blowing up the cost.

---

## 📂 What each file is for

| File | What it's for | Do I edit it? |
|---|---|---|
| `README.md` | This file: the usage guide. | No |
| `CANDIDATE_PROFILE.md` | **Your data** (contact, experience, skills…) and search **preferences**. Source of truth for the CVs. | The agent fills it in at setup (or you, if you prefer) |
| `PROJECT_INSTRUCTIONS.md` | The full manual of how the agent works: **§0 automatic setup**, the 5-stage flow, CV rules, cleanup. | No |
| `AGENTS.md` | **The rules your agent reads.** The canonical file: setup summary, critical rules and session checklist. | No |
| `PLATFORMS.md` | **Where to search**: the list of sites you approved, with the state of each (do I have an account? is the profile ready?). You both fill it in during STAGE 1. | The agent manages it with you |
| `JOBS.md` | The **living** list of jobs found and their state. The agent fills it in. | The agent manages it |
| `JOBS_APPLIED.md` | Archive of jobs already applied to. The agent moves the finished ones here. | The agent manages it |
| `ACTIVE_PROCESSES.md` | Tracking of interviews and selection processes under way. | The agent manages it / you |
| `dependency_graph.md` | A map of which file rules what and what each stage writes, with diagrams. For when you want to adapt the template. | No |

---

## 🔄 How the agent works (the 5-stage flow)

1. **Choose where to search** — you tell it which sites you already use and it recommends
   others based on your profile, your area and your languages, explaining why for each one.
   What you approve goes to `PLATFORMS.md`; what you drop is never proposed again. Without
   this list there is no searching.
2. **Prepare your profiles** *(optional)* — it goes through your profile on each platform
   (LinkedIn, X, GitHub, job boards…) against your data and proposes improvements **one by
   one**. It only applies what you approve, it never creates accounts or asks for passwords,
   and it never puts your phone number on a public profile.
3. **Search** — the agent walks your platforms in priority order and records the jobs in
   `JOBS.md`. No CVs yet.
4. **CV generation** — for each job without a CV, the agent copies your `GENERIC_CV.docx`,
   adapts the text to the job (language, skills, subtitle…) and converts it to PDF in the
   `CVs_JOBS/` folder.
5. **Apply** — the agent tries to submit your application (LinkedIn Easy Apply first, then the
   direct link) and records the result in `JOBS.md`. If a site asks you to log in or sign up,
   it will ask you to do it right then and carry on. If you don't hand it this stage, it gives
   you the link and the PDF so you can apply yourself.

You can ask for any stage on its own, or let it run them all back to back.

---

## ✍️ What to have handy (once)

With «Start the project» the agent asks for all of this and fills it in for you, but have it
ready:

- [ ] Your **CV** in Word with the design you want to keep (the agent will call it
      `GENERIC_CV.docx`).
- [ ] A **profile photo** (the agent crops it into a circle → `profile_photo_circular.png`).
- [ ] Your details: contact, education, experience, skills, languages, certifications.
- [ ] Your **preferences**: which roles and which areas interest you.
- [ ] Knowing **which job sites you already have an account on** (LinkedIn, Indeed…). No
      password needed: the agent never asks for one; when a login is required it tells you so
      you can sign in yourself.

---

## 💡 Tips

- **Talk to your agent in plain language.** No commands needed: "generate the CVs that are
  missing", "apply to the jobs that already have a CV", "find me more Data Engineer roles".
- **You have the final word.** The agent applies to jobs on its own, but it asks for
  confirmation before messaging recruiters or making significant changes to your profiles.
- **Keep `CANDIDATE_PROFILE.md` up to date.** If your level in a skill changes or you add
  experience, edit it there and every future CV will reflect it.
- **Requirement for Word → PDF:** the machine needs **Microsoft Word** or **LibreOffice**
  installed (the agent uses one of them to export the PDF keeping the design). It's explained
  in `PROJECT_INSTRUCTIONS.md`, section 3.

---

## 🔒 A note about your data

`CANDIDATE_PROFILE.md` will end up holding your name, your phone number and your work history.
The `.gitignore` already keeps your CV, your photo and the generated CVs out, **but that file
does get committed** if you publish your copy. If you're going to work in a public repository,
take it out of version control first:

```bash
git rm --cached en/CANDIDATE_PROFILE.md && echo "CANDIDATE_PROFILE.md" >> .gitignore
```

---

Good luck with the search! 🍀
