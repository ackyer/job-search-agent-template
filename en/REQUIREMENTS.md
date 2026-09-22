[English](REQUIREMENTS.md) · [Español](../es/REQUISITOS.md)

# Requirements

This project **is not a program**: it's a set of text files telling an AI agent how to run your
job search. There is nothing to compile and no dependencies to install.

## Essential

| | What for |
|---|---|
| **An AI agent that reads and writes files** | It does the work. Claude Code, Codex, Cursor, Gemini CLI, Copilot… |
| **Your CV in Word (`.docx`)** | It gets copied and its text rewritten for each job. Its design is never touched. **Don't have one, or want to redo it? The project makes it for you** |
| **A profile photo** | It goes on the CV. Any image format works |
| **20–30 minutes the first time** | The setup interview: your details, your experience, your preferences |

If you only have your CV as a PDF, ask the agent to help you convert it to Word before
starting: it needs an editable `.docx`.

**And if you have no CV, or yours has gone stale, don't go looking elsewhere:** say so at the
start ("I don't have a CV, help me create one" or "help me redo it") and it will build one from
what you tell it in the setup interview. That file becomes your base template.

## Depending on what you want it to do

| I want it to… | I also need |
|---|---|
| …generate the CVs as PDF | **LibreOffice** (free, libreoffice.org) or **Microsoft Word** installed |
| …search for jobs on its own | The agent to be able to **browse the web** |
| …apply for me | The above + being **logged in** on the job boards, in the same browser |
| …prepare my profiles | Accounts on the platforms you want to be on (LinkedIn, job boards…) |
| …run it from my phone | A free **GitHub** account. See `INSTALL.md`, route B |

None of this is required to start. Without browsing, the agent is still useful for organising
the search, writing the CVs and keeping track: you hand it the job ads.

## What you do NOT need

- **To know how to code.** Not a line.
- **Python, Node or any dependency.** There's no `requirements.txt` to install because there's
  no code to run.
- **To know how to use GitHub**, if you download the ZIP.
- **To pay for the project.** It's free and open.

## The real cost

The project costs nothing; **the agent running it does**. Working with Claude Code, for
instance, requires a paid plan.

And there's a practical detail: generating twenty tailored CVs eats a fair chunk of your quota.
If your plan is tight, go in batches of five or six jobs instead of firing everything at once.
The manual itself has a sequential mode meant for exactly that.

## Compatibility

It works with any agent that can read and write files in a folder. The rules live in
`AGENTS.md`, the file almost all of them look for on their own; `/CLAUDE.md` and `/GEMINI.md`
point there.

If yours reads none of them, start the conversation with:

> read `AGENTS.md` and follow those instructions

What changes from one agent to another isn't the rules, it's **how much it can do on its own**:
if yours can't browse, you hand it the job ads; if it can't run commands, you convert the CVs
to PDF. The rest works the same.

## Questions?

Open an *issue* in the repository, or message me on LinkedIn:
[www.linkedin.com/in/anderakierayucar](https://www.linkedin.com/in/anderakierayucar)
