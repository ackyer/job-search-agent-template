# PROJECT INSTRUCTIONS — AUTOMATED JOB SEARCH

> Reference file for the agent. It holds the CV rules and the full 5-stage workflow.
> The candidate's data and preferences live in `CANDIDATE_PROFILE.md`.

---

## 0. THE «Start the project» COMMAND — ONBOARDING

When the user says **«Start the project»** (or anything equivalent: "let's go", "set it up",
"begin"), the agent runs this flow **before anything else**. The point is that the user never
has to fill anything in by hand: the agent asks for what it needs and writes the files itself.

### Step 0.1 — Check whether the project is already configured
Look for missing information:
- `CANDIDATE_PROFILE.md` still has unfilled gaps (text inside `[...]`).
- There is no `GENERIC_CV.docx` in the folder.
- There is no `profile_photo_circular.png` in the folder.
- `PLATFORMS.md` has no platform registered (still the empty template).

If **everything is there** → skip to Step 0.3. If **something is missing** → Step 0.2.

### Step 0.2 — Setup interview (fill the structure automatically)
The agent interviews the user, asking **only for what is missing**, in blocks and
conversationally (never dump a giant form at once). After each block, **write to
`CANDIDATE_PROFILE.md` immediately** — don't wait until the end. Blocks:

1. **Contact details** → name, email, phone, LinkedIn, GitHub, location, availability,
   mobility, age (optional).
2. **Headline and professional summary** → a one-line headline + 2-3 paragraphs "about me".
3. **Education** → degrees, institutions, dates, thesis/projects.
4. **Work experience** → per job: company, role, dates, achievements, stack.
5. **Flagship project** → description, measurable impact, stack, whether an NDA applies.
6. **Technical skills** → grouped by category, with the private level S / M+ / M / B.
   Ask as well which technologies they only know at a basic level (for the "mention only if
   the job ad asks for it" rule).
7. **Languages and certifications**.
8. **Search preferences** → target roles (in priority order), geographic areas (in priority
   order), work mode, and locations ruled out up front → `CANDIDATE_PROFILE.md` §Preferences.
9. **Privacy rules** → confirm what must never go out in public channels (phone, salary, NDAs).
10. **Base CV and photo** → ask the user to drop into the project folder:
    - their CV in Word, with the design they want to keep → the agent renames it to
      `GENERIC_CV.docx`. If they only have a PDF or another format, help them get an
      editable `.docx`.
    - their profile photo → the agent crops it into a circle if needed and saves it as
      `profile_photo_circular.png`.

> Do not ask here which platforms to search on: that is **STAGE 1** (§4), which runs later and
> has its own state file, `PLATFORMS.md`.

When done, **show a summary** of everything collected and ask the user to confirm it is
correct before continuing.

### Step 0.3 — Choose which stages the agent handles
Ask the user **which stage(s) of the flow they want the agent to take on**. They can pick one,
several or all of them (details in §4):
1. **STAGE 1 — Choose where to search (platforms)** — *prerequisite*: if `PLATFORMS.md` is
   empty it always runs before searching, even if the user didn't ask for it.
2. **STAGE 2 — Prepare your profiles on those platforms** — *optional*, and only for
   platforms where the user already has an account.
3. **STAGE 3 — Job search**
4. **STAGE 4 — CV generation**
5. **STAGE 5 — Apply** (if they don't pick it, the user applies on their own)

### Step 0.4 — Choose the execution mode: sequential or parallel
Ask whether they want the work done **sequentially** or in **parallel**:

- **Sequential** — the agent handles one job/task after another. Slower, but easier to
  supervise and cheaper. Recommended when there are few jobs or the user wants to review as
  things go.
- **Parallel** — the agent launches several **helpers at once** (e.g. one CV per helper, or
  several searches across different job boards at the same time). Far faster with many jobs.
  **Only if your tool can launch agents in parallel**; otherwise go sequential. Helpers cannot
  talk to the user: **ask every question before launching them** and include the answers in
  their brief. The **model strategy** below applies.

> ⚠️ `JOBS.md`, `JOBS_APPLIED.md` and `PLATFORMS.md` are **state files**: helpers propose,
> but **only the orchestrator writes**. Two agents writing at once corrupt the tracking.

### Model strategy in parallel mode
If your tool lets you pick a model per task, assign it by **complexity and importance**. If it
only has one model, skip this section: the division of work still holds, everything is just
done by the same model.

- **Your most capable model** → important decisions and complex or creative work:
  - Judging whether a job is a real fit (geographic relevance rule, §2).
  - Deciding which platforms to recommend and on what grounds (STAGE 1).
  - Writing the profile copy for each platform: headline, "about", bio (STAGE 2).
  - Writing and adapting the CV's PROFESSIONAL SUMMARY for each job.
  - Deciding which skills to highlight and what subtitle to use.
  - Reviewing/updating the candidate's platform profile before applying (STAGE 5).
  - Writing personalised messages to recruiters.
- **Your fastest and cheapest model** (or a mid-tier one, if your tool has several) →
  mechanical, low-risk work:
  - Text replacements in the `.docx` XML (unpack/edit/repack).
  - `.docx` → PDF conversion and moving files into `CVs_JOBS/`.
  - Updating state fields in `JOBS.md` and `PLATFORMS.md`, and applying the archive/delete
    rules.
  - Simple lookups and data extraction from a job ad that has already been found.

> Rule of thumb: **judgement and writing → the capable model; repetitive execution → the cheap
> one**. When in doubt about whether a task is "important", use the capable model.

### Step 0.5 — Run
With the stages and the mode chosen, run the flow in §4 respecting every rule in this
document. When finished, report the outcome to the user (jobs found, CVs generated,
applications sent) and the next steps that need action from them.

---

## 1. THE CANDIDATE'S PROFILE

> ⚠️ **The candidate's information lives in `CANDIDATE_PROFILE.md`.**
> The agent must read that file before generating any CV or filling in any form. Never use
> hardcoded data; `CANDIDATE_PROFILE.md` is the single source of truth.

---

## 2. GEOGRAPHIC RELEVANCE RULE (MANDATORY)

The preferred roles, areas and work modes live in `CANDIDATE_PROFILE.md` §Search preferences.

Jobs **inside the preferred areas** are **high priority and always registered**, even when the
technical fit is merely reasonable.

Jobs **outside those areas** are only registered in `JOBS.md` if the candidate is a **very
good fit for the role**. "Good fit" means **all** of these hold at once:

- **Junior level** or little experience required (intern, working student, "0–1 years", "first
  job", trainee). Rule out up front anything asking for 2+ years, "senior", "mid", "expert",
  or experience in something the candidate doesn't have yet.
- **A stack that matches what the candidate is strong in** according to
  `CANDIDATE_PROFILE.md` (the ones marked S or M+ in their private level table). If the core
  requirements are technologies marked only M, B or absent, it isn't a real fit.
- **The role is among the candidate's top priorities.**
- **A location reasonably close** to the ideal area, or a workable hybrid/remote arrangement,
  and not on the list of locations ruled out up front.

If an out-of-area job fails **any** of those points, **discard it in STAGE 3** and do not add
it to `JOBS.md`. When in doubt, ask the user before registering it. A prestigious company, a
high salary or an "interesting" project **are not reasons enough** on their own — technical
and geographic fit rule.

---

## 3. CV RULES

| Rule | Detail |
|---|---|
| **Template and structure** | Use `GENERIC_CV.docx` as the base template and replicate its structure exactly (sections, order, formatting, typography) |
| **No home address** | Don't put a home address on the CV (optional exception: jobs in the candidate's own area) |
| **Mobility** | State willingness to relocate / mobility if it applies |
| **Regional language** | Include a regional language **ONLY** for jobs in that region; remove it everywhere else |
| **ATS** | Optimise for ATS engines using keywords from the job ad |
| **No false information** | Never invent experience or skills |
| **Profile photo** | Always include the photo. Use `profile_photo_circular.png` (circular crop) as the main image |
| **One page maximum** | The CV must fit on one A4 page. If it doesn't, **cut content**; never touch margins, font or spacing |
| **Personalisation** | Ask the user about additional relevant skills before generating each CV |
| **Basic skills** | Technologies marked as "basic knowledge, no experience" in `CANDIDATE_PROFILE.md` are **only mentioned if the job ad explicitly asks for them**, and always as "familiar with X", NEVER as experience |
| **Subtitle under the name** | ⚠️ **CRITICAL RULE.** The text under the name **must never be the exact job title from the ad**. Use a generic description of the candidate's professional identity + key technologies separated by `·`. **Example:** an ad for "Working Student Data Analyst" → subtitle "Data Analyst \| Python · SQL · Power BI". The subtitle should read as the candidate's stable identity, not as the ad's headline |

### ⚠️ Mandatory CV generation process (DOCX → PDF)

**NEVER build the PDF from scratch with libraries like reportlab.** The visual design of the
generic CV must be preserved exactly. The correct flow is:

1. **Decide the CV's language** before starting: if the ad is published in English or the
   working language is English → the whole CV in English; in another language or unspecified →
   the CV in that language. When in doubt, ask the user.
2. Copy `GENERIC_CV.docx` under a new name:
   `CV_[Surname]_[Company]_[Role]_[Area].docx`
3. Open and edit the copied `.docx` with the **unpack → edit XML → repack** technique:
   - Unzip the `.docx` into a working folder (`unpack_<tag>/`).
   - Edit `word/document.xml` by replacing text inside the XML nodes
     (pattern: `>old text<` → `>new text<`).
   - Change the role subtitle, adapt the PROFESSIONAL SUMMARY to the job, adjust the SKILLS to
     highlight the relevant ones, add or remove the regional language depending on the area,
     adjust the location.
   - If the CV is in another language, translate every editable text.
   - Zip it back up (repack).
4. Convert the edited `.docx` to PDF. Two equivalent routes depending on the machine:
   - **With LibreOffice installed (Linux/Mac/Windows):**
     ```bash
     soffice --headless --convert-to pdf --outdir CVs_JOBS CVs_JOBS/CV_[...].docx
     ```
   - **Windows with MS Word (no LibreOffice):** use **MS Word COM** via PowerShell — Word
     renders its own docx, so the PDF is identical. Word COM needs **absolute paths**:
     ```powershell
     Get-Process WINWORD -ErrorAction SilentlyContinue | Stop-Process -Force
     Start-Sleep -Seconds 2
     $docx = (Resolve-Path "CVs_JOBS\CV_[...].docx").Path
     $w = New-Object -ComObject Word.Application
     $w.Visible = $false
     $d = $null
     try {
         $d = $w.Documents.Open($docx)
         $d.SaveAs2([IO.Path]::ChangeExtension($docx, ".pdf"), 17)  # wdFormatPDF = 17
     } finally {
         if ($d) { $d.Close($false) }
         $w.Quit()
     }
     ```
     The `finally` closes Word even if the conversion fails, so no instances are left
     hanging. `Stop-Process` at the start clears any left over from earlier runs. Retry up
     to 3 times with a 5s wait if Word is busy (e.g. helpers running in parallel).
5. Check that the PDF is **exactly one page** (if not, cut content and repeat).
6. Leave **both the `.docx` and the PDF** in `CVs_JOBS/` (create the folder if it doesn't
   exist). Nothing intermediate should be left in the project root.

---

## 4. WORKFLOW — 5 STAGES

### ▶ STAGE 1 — CHOOSE WHERE TO SEARCH (PLATFORMS)

**Goal:** leave in `PLATFORMS.md` the approved list of places where jobs will be searched for,
with the state of each one. Without that list there is no searching: STAGE 3 walks it.

**When it runs:** when the project starts, whenever the user asks ("add X", "drop Y", "where
else could I look") and **always when a search is about to happen with `PLATFORMS.md` empty**,
even if the user didn't ask for it.

**Process:**

1. **Ask the user first**, before proposing anything:
   - which platforms they already search on, or want to;
   - where they already have an account;
   - which ones they don't want to use, and why (so they're never proposed again).
2. **Recommend after that.** Read `CANDIDATE_PROFILE.md` (target roles, areas, work mode,
   languages, seniority) and pick from the §5 catalogue the platforms that fit **that**
   specific profile. Rules for recommending:
   - Every suggestion carries **a one-line reason tied to a real fact in the profile**
     ("your region runs its own employment portal", "it concentrates remote roles in English").
   - **Don't dump the whole catalogue**: between 3 and 6 new suggestions is plenty.
   - **Check that the platform is still alive** and has jobs matching the profile before
     suggesting it. If that can't be checked, say so rather than assuming.
   - Never propose anything sitting in the DISCARDED section of `PLATFORMS.md`.
   - If a platform is paid, say so when proposing it.
3. **Decide with the user:** they approve, remove or add. When in doubt, ask.
4. **Write `PLATFORMS.md`**: one entry per approved platform using the §6 format, filling in
   `Type`, `Priority`, `Account` and `Agent access` right away. Rejected ones go to the
   DISCARDED section with a reason and a date.
5. If an approved platform needs an account the user doesn't have, leave it as
   `Account: 🟡 To create — [URL]`: they create it when it's needed (STAGE 2 or STAGE 5),
   never the agent — full rule in STAGE 2.
6. When finished, offer STAGE 2 for the platforms that have an account.

**Not in this stage:** searching for jobs, touching profiles or generating CVs.

---

### ▶ STAGE 2 — PREPARE YOUR PROFILES (OPTIONAL)

**Goal:** make sure the candidate's profile on each chosen platform is complete, current and
consistent with `CANDIDATE_PROFILE.md` **before** applying, because on most job boards the
recruiter looks at the profile, not just the CV.

**Which platforms:** only those in `PLATFORMS.md` with `Account: ✅` and `Profile ready: ⏳`.
Aggregators and company sites have no profile: mark them `—` and skip.

**Mandatory rules for this stage:**

- **The user does the logging in.** If the platform asks for a login or a sign-up, give them
  the URL, ask them to do it right then and **wait for their confirmation**. The agent never
  creates accounts and never handles credentials in any form.
- **No change without approval.** Present changes **one at a time**, with the exact text that
  would go in, and apply only the approved ones. A "yes" to one change is not a yes to the rest.
- **Privacy** (`CANDIDATE_PROFILE.md` §Hard rules):
  - The **phone number never goes on a public profile** (LinkedIn, X, GitHub, personal site).
    It only goes on delivered CVs and on specific application forms.
  - **Salary:** if the expected-salary field is optional, leave it **empty**. If it is required
    to save the profile, **ask the user what figure to use** and use it only there. Never infer
    or invent it.
  - Anything under an NDA is mentioned only at a high level, with no internal detail.
- **Nothing invented:** everything written must exist in `CANDIDATE_PROFILE.md`. If a fact is
  missing, ask the user and add it to the profile **first**.

**Process, per platform:**

1. Open the user's profile on the platform, with the session already logged in.
2. Compare it **section by section** against `CANDIDATE_PROFILE.md`, using the checklist for
   that type of platform (§5.2).
3. Write a short report with the proposed changes: what is there now, what would go in, and
   why. Grouped by section and ordered by impact.
4. Show it to the user and apply **only** what they approve. Whatever they'd rather do by
   hand, leave them step-by-step instructions.
5. Update `PLATFORMS.md`: `Profile ready: ✅ [date]` and, under `Notes:`, whatever is still on
   their plate.
6. Delete the interim report once the changes are applied (§7).

**In parallel mode:** a helper can analyse each platform and hand back its report, but
**only the orchestrator writes to `PLATFORMS.md`**: it is a state file.

---

### ▶ STAGE 3 — JOB SEARCH

**Goal:** find relevant jobs and register them in `JOBS.md`.

**Where to search:** the platforms in `PLATFORMS.md`, **in priority order** (High → Medium →
Low). That list rules; the §5 catalogue only exists to recommend new platforms in STAGE 1. If
`PLATFORMS.md` is empty, run STAGE 1 first.

**Process:**
1. Walk the approved platforms by priority, searching with the preferences in
   `CANDIDATE_PROFILE.md` and applying the relevance rule in §2. Depending on `Agent access`:
   - **🟢 Open** — search directly.
   - **🟡 Needs you logged in** — ask the user to log in right then and wait, same as STAGE 5.
   - **🔴 Blocked** — don't push: hand the search to the user and move on to the next platform.
   - On **social · visibility** platforms (X, communities), look for job posts and roles shared
     by recruiters, not a conventional job search engine.
2. For each job, add an entry to `JOBS.md` using the §6 format (including `Platform:` and
   `Access:`) with the state fields empty.
3. After finishing each platform, update its `Last search:` in `PLATFORMS.md`.
4. Do not generate CVs in this stage. Only register jobs.

---

### ▶ STAGE 4 — CV GENERATION

**Goal:** generate a tailored PDF CV for every job in `JOBS.md` that doesn't have one.

**Process:**
1. Read `JOBS.md` and filter jobs with `CV generated:` empty.
2. Ask the user whether they have extra skills relevant to each job (in parallel mode, ask
   everything before launching the helpers).
3. For each job: read the ad (and the link if needed) and generate the CV applying every rule
   and the process in §3.
4. Update `JOBS.md`: `CV generated: ✅ [PDF file name]`.

---

### ▶ STAGE 5 — APPLY

**Goal:** apply to the jobs that already have a CV but haven't been submitted.

If the user has **not** handed this stage to the agent (Step 0.3), the agent gives them each
job's link plus their CV PDF, and the user fills in `Applied manually:` when they apply.

**⚠️ Login / sign-up rule — MANDATORY:**
If the platform requires a login or a new account, **ask the user to do it right then** (give
them the URL) and wait for confirmation; the agent applies afterwards. Only if the user says
they can't do it now, mark `Applied: ⚠️ Waiting on user — [URL]`. Update that platform's
`Account:` field in `PLATFORMS.md` as well.

**⚠️ Profile review rule — MANDATORY:**
Before applying on a platform where the user is registered:
1. If `PLATFORMS.md` shows `Profile ready: ✅` with a recent date, just check it is still
   consistent with `CANDIDATE_PROFILE.md`.
2. If it doesn't, run the **STAGE 2** review (checklist in §5.2) before signing up.
3. If anything is out of date, update it before submitting, **asking the user to confirm**
   each change.
4. Only then, go ahead and apply.

**Process:**
1. Read `JOBS.md` and filter jobs with `CV generated: ✅` and `Applied:` empty.
2. For each one, try in this order:
   a. If it has a LinkedIn link → try **LinkedIn Easy Apply**.
   b. If not → open the direct link and try to apply from there.
   c. Upload the PDF CV generated for that job whenever the form allows it.
3. Record the outcome:
   - **Success:** `Applied: ✅ [site] — [date]`
   - **Failure — technical blocker:** `Applied: 🚫 Blocked — [reason: Cloudflare, captcha, etc.]`
   - **Expired ad:** `Expired / Invalid: Yes — detected by the agent [date]`
   - **Never retry** the same job after a failure; record it and move on.

**Extra action — contacting recruiters:**
- For each job applied to, look up the company's HR person or recruiter on LinkedIn.
- Try to connect and send a personalised message expressing interest in the role.
  **Ask the user to confirm before sending the message.**

---

## 5. PLATFORMS — RECOMMENDATION CATALOGUE AND PROFILE CHECKLISTS

Reference material for STAGES 1 and 2. **This is not the user's platform list**: that lives in
`PLATFORMS.md` and is the only one that rules when searching.

### 5.1 Catalogue to recommend from (STAGE 1)

Filter by the candidate's profile: role, areas, work mode, languages and seniority. Recommend
few and justified, never the whole table.

| Category | When it fits | Examples |
|---|---|---|
| **General job boards** | Always; they're the backbone of any search | LinkedIn Jobs, Indeed, and the dominant board in the candidate's country |
| **Tech-specific boards** | Technical profiles: less noise, better stack filters | Wellfound, Otta, Hacker News "Who is hiring", regional tech boards |
| **Public employment services** | When the preferred area runs its own service; many of those ads never reach private boards | The regional or national employment service, city and county portals |
| **Remote and international** | If remote is acceptable, or the candidate can work in English | Remote OK, We Work Remotely, Welcome to the Jungle, Europe Language Jobs |
| **Internships, grants, first job** | Junior profiles, recent graduates or little experience | The university's careers portal, graduate schemes, trainee programmes |
| **Aggregators** | To sweep several sources quickly; watch out for duplicates and stale ads | Jooble, Talent.com, Glassdoor |
| **Company sites and ATS** | When specific companies are of interest: the ad is usually there before the boards | The company's "Careers" page, Greenhouse, Lever, Workday |
| **Social · visibility** | So that jobs and recruiters come to you; you don't apply from here | X, LinkedIn as a network, GitHub, sector Discord/Telegram communities |

Criteria when choosing:
- **Real geographic coverage:** a board with no jobs in the profile's areas is useless, however
  big its name.
- **Language:** if the platform demands a level the candidate doesn't have, say so.
- **Accessibility:** if the site blocks automated browsing (captcha, Cloudflare), it still
  counts, but it gets registered as 🔴 and the user applies.
- **Maintenance effort:** more platforms means more work per session. Better a few well
  tended than fifteen abandoned.

### 5.2 Profile preparation checklists (STAGE 2)

Common to all: a professional photo consistent with `profile_photo_circular.png`, the name
spelled correctly, the location from `CANDIDATE_PROFILE.md` (the profile one, not the postal
address), **no phone number on a public profile**, and nothing that isn't in
`CANDIDATE_PROFILE.md`.

**LinkedIn** (board + network):
- Headline: the one in `CANDIDATE_PROFILE.md`; never a specific job's title.
- "About": a short version of the professional summary, with the key technologies.
- Experience and education: same dates and same names as in the profile.
- Skills: pin the three marked **S** at the top; don't list the basic ones.
- Languages and certifications up to date.
- A custom profile URL, the same one that appears on the CV.
- "Open to work" set the way the user wants: recruiters only, or public.
- Job alerts created for the priority roles and areas.

**X** (visibility, not applications):
- Bio with the professional identity and key technologies; location; link to GitHub or site.
- A pinned post about the flagship project, if the user wants one.
- Follow accounts and lists that post jobs in the sector and the area.
- **No phone number, no private data:** it is a public account.
- **Never post in their name without explicit confirmation.**

**GitHub**:
- A profile README with the headline, the stack and how to get in touch (public email, never
  the phone).
- Pinned repos with a description and a readable README; the flagship project first.
- Real photo and name; a link to LinkedIn.

**Job boards with their own CV** (Indeed, national boards, company portals):
- Fill in the platform's own CV with the profile data: that is what recruiters filter on.
- Upload `GENERIC_CV.docx` (or its PDF) as the default attachment.
- Role, working-hours and area preferences as per `CANDIDATE_PROFILE.md`.
- Expected salary: empty if possible; if it is required, ask the user.

**Public employment services**:
- Check the jobseeker registration is active and up to date.
- Update the requested occupations and the search area.
- These usually need a digital certificate or a government login: **the user does that**.

**Aggregators and company sites**: no profile to prepare. Mark `Profile ready: —` and, at
most, create the corresponding job alert.

---

## 6. TRACKING FILES

### PLATFORMS.md — structure
`PLATFORMS.md` is the single source of truth for **where** searching happens. STAGE 1 fills it
and STAGES 2, 3 and 5 maintain it. Each entry follows this format:

```markdown
## [N]. [Platform name]

- **Type:** General board / Tech board / Public service / Social · visibility / Aggregator / Company site
- **URL:** [home page or an already-filtered search URL]
- **Priority:** High / Medium / Low
- **Source:** User / Recommended by the agent — [reason]
- **Account:** ✅ Have one / 🟡 To create — [sign-up URL] / ❌ N/A
- **Agent access:** 🟢 Open / 🟡 Needs you logged in / 🔴 Blocked — [reason]
- **Profile ready:** ⏳ Pending / ✅ [YYYY-MM-DD] / — (no profile)
- **Applies from agent:** Yes — [kind of application] / No — link only
- **Last search:** YYYY-MM-DD
- **Notes:** 
```

State rules:
- **Priority** sets the order STAGE 3 walks them in.
- **Discarded:** platforms the user rejected go to the `DISCARDED` section at the end, with a
  reason and a date. The agent **never proposes them again** while they sit there.
- A platform is never deleted: it is either active or in DISCARDED.

### JOBS.md — structure
`JOBS.md` is the source of truth for each job's state. Each entry follows this format:

```markdown
## [N]. [Role] — [Company]

- **Platform:** [name exactly as it appears in `PLATFORMS.md`]
- **Links:** [LinkedIn URL if any] / [platform URL] / [company site URL]
- **Description:** Short description of the role and key requirements.
- **Location:** [City / Remote / Hybrid]
- **Work mode:** [On-site / Hybrid / Remote]
- **Date found:** YYYY-MM-DD
- **Access:** 🟢 Open / 🟡 Account needed on [platform] — [URL] / 🔴 Blocked — [reason]
- **CV generated:** 
- **Applied:** 
- **Applied manually:** 
- **Expired / Invalid:** 
```

### The `Applied manually:` field
Reserved for **the user** to fill in when they apply on their own.
- The agent **never** fills it in automatically.
- Format: `✅ [platform] — YYYY-MM-DD`. A plain `Yes` is enough.
- **Archive rule:** when reviewing `JOBS.md`, the agent must **move the whole entry** to
  `JOBS_APPLIED.md` and remove it from `JOBS.md` if:
  1. `Applied manually:` has content, **or**
  2. `Applied:` contains `✅`.
  - Entries in `⚠️ Waiting on user` or `🚫 Blocked` state are **not** archived.

### The `Expired / Invalid:` field
Filled in by the user when a job is no longer valid (expired, not a fit, etc.), or by the agent
if it finds in STAGE 5 that the ad has expired.
- A plain `Yes` or an explanatory note is enough.
- **Delete rule:** if it has content, the agent **removes the entry outright** from `JOBS.md`
  without archiving it.

### Legend for the `Access:` field (fill it in during STAGE 3)
By default a job **inherits its platform's `Agent access:`**. Only set a different value if
that specific job behaves differently (e.g. the platform is 🟢 but this ad redirects to an ATS
with a captcha).

| Icon | Meaning | What happens in STAGE 5 |
|---|---|---|
| 🟢 Open | Can be viewed and applied to without an account | The agent applies directly |
| 🟡 Account needed | Requires sign-up or login (always note the URL) | The agent asks the user to register/log in, then applies |
| 🔴 Blocked | Anti-bot protection (Cloudflare, captcha…) | The user applies by hand from the browser |

### ACTIVE_PROCESSES.md — tracking selection processes
When the user reports a reply, an interview, a test or any progress on a job they applied to,
the agent creates or updates its block in `ACTIVE_PROCESSES.md` using the commented template in
that file: history (✅), pending steps (⏳) and a `📅 CALENDAR_EVENTS` block with **absolute
dates** and a time zone. Update the key-dates table and the "Today" line as well. If a process
ends, mark it closed in its heading.

---

## 7. PERIODIC CLEANUP

At the start of each session, or whenever the user asks, the agent reviews the folder and
deletes files that are no longer useful:

| Type of file | Condition for deleting |
|---|---|
| Profile reports for any platform (LinkedIn, X, GitHub…) | The user already applied the changes to the profile (STAGE 2) |
| Summaries or metrics from old searches | The information is already in `JOBS.md` or `CANDIDATE_PROFILE.md` |
| `unpack_<tag>/` working folders | Once the PDF has been generated |
| CVs in `CVs_JOBS/` | **Always keep** |
| `CANDIDATE_PROFILE.md`, `PROJECT_INSTRUCTIONS.md`, `PLATFORMS.md`, `JOBS.md`, `JOBS_APPLIED.md`, `ACTIVE_PROCESSES.md`, `README.md`, `AGENTS.md`, `INSTALL.md`, `REQUIREMENTS.md`, `dependency_graph.md` | **Always keep** |
| The photo and CV images | **Always keep** |
| The base `GENERIC_CV.docx` | **Always keep** |

**General rule:** if a file was an intermediate step and its content already lives in a
permanent file, it can go. When in doubt, ask the user before deleting.
