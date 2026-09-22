[English](INSTALL.md) · [Español](../es/INSTALACION.md)

# How to get this running

You don't need to know how to code, and you don't need to have used GitHub before. There are
**two routes**: the computer one, which is the recommended one, and an alternative for running
it from your phone.

## Which one do I pick?

| | **A. On a computer** ⭐ | **B. From your phone (via GitHub)** |
|---|---|---|
| What you need | A computer and 15 minutes | A free GitHub account |
| Setup interview and your profile | ✅ | ✅ |
| Choosing where to search | ✅ | ✅ |
| Generating the CVs as PDF | ✅ with LibreOffice or Word installed | ✅ everything is already set up |
| Searching for jobs | ✅ | ⚠️ only what's visible without logging in |
| **Applying on your behalf** | ✅ with your sessions logged in | ❌ it doesn't have your logins |
| Tracking your processes | ✅ | ✅ |

> ### ⭐ Go with route A
>
> On a computer **everything** works: it searches with your sessions logged in, generates the
> CVs and submits applications for you. It's the route that has been tested end to end.
>
> **Route B is the alternative** for anyone without a computer at hand or who needs to work
> from their phone. It does almost everything, but you end up sending the applications
> yourself.

---

# A. On a computer ⭐ (recommended)

## Step 1 — Download the project

1. Open the project's page on GitHub.
2. Find the green **`Code`** button, above the file list on the right.
3. Click it and choose **`Download ZIP`**. A compressed file downloads.
4. Unzip it wherever you want to keep it (the Desktop is fine):
   - **Windows:** right-click the file → *Extract All…* → *Extract*.
   - **Mac:** double-click the file and it unzips itself.

You end up with a folder containing everything.

## Step 2 — Keep one language only

Inside you'll see two folders, `es` and `en`. **Delete the one you won't use.** It isn't
mandatory, but if you keep both the agent has to ask you which one every time.

The folder you keep **is your project**: that's where you'll work.

## Step 3 — Install Claude

The simplest way, with no terminal involved:

1. Go to **claude.ai/download** and install the desktop app.
2. Open it and sign in with your Claude account.
3. Point it at your project folder (the one from step 2).

> You need a paid Claude plan. The project is free, but the agent running it isn't.

<details>
<summary>If you'd rather use the terminal</summary>

With Node.js installed:

```bash
npm install -g @anthropic-ai/claude-code
cd path/to/your/folder
claude
```

Install commands change every now and then; the reliable source is the official Claude Code
documentation.
</details>

> Using a different agent (Codex, Cursor, Gemini CLI, Copilot…)? That works too: open it in
> that folder. The only hard requirement is that it can **read and write files** there.

## Step 4 — No CV yet, or not happy with the one you have?

Not a problem: **the project makes it for you**. When it asks you for your CV, tell it one of
these:

> **I don't have a CV, help me create one**
>
> **My CV is out of date, help me redo it**

With what you told it in the interview it builds one in Word from scratch, or rewrites the one
you have. That file becomes your base template, and from there the project works the same: it
copies it and adapts it to each job without touching the design.

> A CV built this way comes out correct and clean, but plain. If you want a more polished
> design, start from a Word template you like and ask it to fill in the text.

## Step 5 — For the PDFs: LibreOffice

The project takes your Word CV, changes the text and converts it to PDF without touching the
design. That conversion needs **Microsoft Word** or **LibreOffice** on your computer.

If you don't have Word: go to **libreoffice.org/download**, download it and install it. It's
free and there's nothing to configure — having it installed is enough.

## Step 6 — Start

With the folder open in Claude, type:

> **Start the project**

That's it. It will ask you for your details, request your CV and photo, and get to work.

---

# B. From your phone, via GitHub (second option)

This route is for when you **don't have a computer available** or you need to run your search
from your phone. The project lives in your own GitHub account and Claude works on it over the
internet, with nothing of yours switched on.

## Step 1 — A GitHub account

If you don't have one: go to **github.com**, hit *Sign up* and follow the steps. It's free and
only asks for an email.

## Step 2 — Make your own copy of the project

On the project's page you'll see one of these two buttons at the top right:

- **`Use this template`** → *Create a new repository*. This is the better one: you get a clean
  copy.
- If it isn't there, use **`Fork`**, which does the same thing under another name.

It will ask for a name for your copy. Call it whatever you like.

> ### ⚠️ Make it **private**
>
> On that screen there's a **Public / Private** option: choose **Private**.
>
> Your copy will end up holding your name, your phone number, your work history and your CV.
> In public, anyone can read that. With `Fork` you can't always choose: if your copy comes out
> public and you're about to put personal data in it, delete it and use `Use this template`
> set to private.

## Step 3 — Open Claude on your copy

1. Go to **claude.ai/code** in your phone's browser, or open the Claude app and go to the
   **Code** section.
2. Connect your GitHub account when asked and give it access to your copy of the project.
3. Create a session pointing at that repository.

## Step 4 — Start

Type in the chat:

> **Start the project**

It will interview you, fill in the files and work inside your repository.

## Step 5 — Don't lose anything

Cloud sessions are temporary: **whatever isn't saved to your repository is lost.** When you
finish a stretch of work, tell it:

> **Save the changes to GitHub**

That way your jobs, your profile and your CVs are safe in your copy, and the next session picks
up where you left off.

## What it won't be able to do this way

Apply for you. Signing you up on LinkedIn or a job board needs your session logged in on those
sites, and Claude doesn't have it there. What it will do is leave you **the job link and the
generated CV** ready so you can apply yourself in two minutes.

---

## If something goes wrong

| What you see | What's happening |
|---|---|
| "I can't find the CV" | The file has to be called `GENERIC_CV.docx` and sit in the language folder. If your CV is a PDF, ask Claude to help you turn it into Word |
| The PDF isn't generated | LibreOffice or Word is missing. Step 5 of route A |
| It opens but doesn't know what to do | Tell it: "read `AGENTS.md` and follow those instructions" |
| A site won't let it apply | Normal: some block automated submissions. It'll give you the link so you can do it |

### Still stuck?

Two ways, whichever suits you:

- **Open an *issue*** in the repository (*Issues* tab → *New issue*) describing what you did
  and what you got. That way it's public and helps the next person who gets stuck.
- **Message me directly** on LinkedIn:
  [www.linkedin.com/in/anderakierayucar](https://www.linkedin.com/in/anderakierayucar)

You don't need to explain it in technical terms: describe it the way you'd say it out loud,
with a screenshot if you can.
