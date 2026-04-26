# V1 Scope

## For / Who / Unlike

For a **PhD student revising a single paper across many rounds of feedback** (advisor, co-authors, reviewers), DraftGit is a **Git-native manuscript workflow** (a small CLI + repo templates on top of Git and GitHub) that **makes each revision a reviewable, inspectable, reversible unit of work** — unlike **Overleaf** (which compresses author edits into a single linear history) or **Google Docs** (which isn't text-first and doesn't fit Typst, LaTeX, or Markdown).

ResearchGit is the parent brand; **DraftGit** is the v1 product and the name of the CLI itself.

## The One User We're Building For

One PhD student, writing one paper, with one advisor and maybe one co-author. Every v1 decision is filtered through this person.

If a feature only matters when there are 5+ co-authors, 3+ papers, cross-lab sharing, or hosted infrastructure — it's v2 or later.

## Current Increment: v0.1

DraftGit is **a thin CLI on top of Git + GitHub, not a replacement for either.** You keep using VS Code, `git`, `gh`, and GitHub's web UI. DraftGit adds academic-specific verbs where vanilla Git is awkward.

The current implementation target is **v0.1**, not the full v1. v0.1 exists to prove that DraftGit can create a useful, private-by-default manuscript repository with a clean starter structure.

v0.1 ships:

1. **A CLI called `draftgit`** with one implemented verb:
    - `draftgit new <paper-name> [--format typst|latex|markdown]` — scaffold a paper directory, initialize Git, and optionally create a **private** GitHub repo
2. **Starter paper templates for Typst, LaTeX, and Markdown**
3. **A Typst GitHub Action template** for the primary reference workflow
4. **Private-by-default repo creation** via `gh`, with explicit `--public` opt-in
5. **Discovery stubs** for planned verbs:
    - `draftgit build`
    - `draftgit cite add <doi-or-url>`
    - `draftgit submit <name>`

The stubs are intentional. They reserve the product vocabulary without pretending the workflow is already complete.

## What V1 Ships

V1 ships:

1. **A CLI called `draftgit`** with exactly four verbs:
    - `draftgit new <paper-name> [--format typst|latex|markdown]` — scaffold a paper directory and create a **private** GitHub repo
    - `draftgit build` — detect format, compile to PDF locally
    - `draftgit cite add <doi-or-url>` — fetch metadata from CrossRef and append to `references.bib`
    - `draftgit submit <name>` — create an annotated Git tag `submit/<name>` for submission tracking (signed if the user has a GPG key configured)
2. **Paper templates for Typst, LaTeX, and Markdown** — `draftgit new` scaffolds from these
3. **GitHub Action templates for each format** — auto-build PDF on push and attach as an artifact
4. **Private-by-default repos** — `draftgit new` always creates `--private`; going public is an explicit `--public` flag
5. **A plain-language workflow guide** for co-authors who don't know Git

Everything else — branching, PRs, conflict resolution, issue tracking — is vanilla Git and GitHub. DraftGit **sits alongside** the existing ecosystem, it does not try to replace it.

## Milestone Path To V1

The implementation should grow in order of academic workflow risk, not in order of how easy the code looks.

1. **v0.1: scaffold** — `draftgit new` creates a usable manuscript repo and sets the private-by-default habit.
2. **v0.2: build** — `draftgit build` detects the paper format and compiles to `paper.pdf` locally.
3. **v0.3: submit** — `draftgit submit <name>` creates an annotated `submit/<name>` tag after checking the manuscript state.
4. **v0.4: cite** — `draftgit cite add <doi-or-url>` adds conservative CrossRef-backed BibTeX entries with duplicate protection.
5. **v1.0: dogfood release** — the full four-verb workflow has been used on at least one real paper cycle and documented for a non-Git co-author.

`cite add` comes after `build` and `submit` because citation automation is deceptively messy in real academic work: DOI metadata can be incomplete, preprints and journal versions collide, BibTeX keys need to stay stable, and duplicate detection must be trustworthy.

## Naming Decisions

- **Parent brand:** ResearchGit
- **Product/CLI brand:** DraftGit
- **PyPI package:** `draftgit`
- **Installed binary:** `draftgit`
- **Docs primary form:** `draftgit new thesis`

We do **not** ship a `git-draft` subcommand alias: although Git supports external `git-*` commands on PATH, the `git-draft` slug on PyPI is already taken by an unrelated code-assistant tool, and reusing that name would reintroduce the collision problem we chose `draftgit` to avoid. Users who want a Git-style shorthand can set a local alias themselves (`git config alias.draft '!draftgit'`) — that's their choice, not a shipped default.

## The CLI Discipline Rule

**No fifth verb ships until `docs/pain-log.md` has at least three independent entries justifying it.** The CLI stays small and composable on purpose. Features that sound useful but can already be done with one-line Git aliases stay as documentation, not code.

## A Day In The Life (V1)

1. `draftgit new my-paper --format typst`. A private GitHub repo appears with scaffolding and CI. Student clones it in VS Code.
2. Student writes the first draft in `paper.typ`, using VS Code's Typst extension. `draftgit build` gives a local PDF preview. Push.
3. CI compiles the PDF and attaches it as a downloadable artifact on the commit.
4. `draftgit cite add 10.1234/foo` → CrossRef metadata lands in `references.bib`. Push. PDF rebuilds.
5. Advisor (invited via GitHub) opens a PR titled "Methods section feedback." Student reviews each change inline, merges.
6. At submission: `draftgit submit iclr-2026`. Annotated tag `submit/iclr-2026` is created with date + message. The tagged PDF is archived by CI.
7. Six months later when a reviewer asks "which version did we submit?", `git checkout submit/iclr-2026` returns the exact paper bit-for-bit.

## In Scope (V1)

- `draftgit` CLI with four verbs: `new`, `build`, `cite add`, `submit`
- Paper templates for Typst, LaTeX, and Markdown
- GitHub Action templates for each format
- Private-by-default repo creation via `gh` under the hood
- `draftgit cite add` backed by the public CrossRef API (no API key required)
- Plain-language workflow guide for non-Git co-authors
- Works alongside VS Code / JetBrains / command-line Git without custom plugins

## In Scope (v0.1)

- `draftgit new`
- Typst, LaTeX, and Markdown starter files
- Git initialization and initial commit
- Optional GitHub repo creation through `gh`
- Private-by-default repo creation
- Clear stubs for `build`, `cite add`, and `submit`

## Out Of Scope (V1)

- **A fifth CLI verb.** Any proposed expansion waits on the pain log.
- **A `git-draft` subcommand alias.** See "Naming Decisions" above.
- Custom VS Code / JetBrains extensions — existing Git integrations are sufficient
- GitLab / Bitbucket / self-hosted Git support — GitHub only in v1; multi-host is v1.1+
- Peer review rebuttal tooling — v2
- Journal submission automation — v3+
- AI writing / citation recommendation — v2+
- Reference-manager parity with Zotero / Mendeley — not a goal
- Multi-paper / lab-wide shared libraries — v2
- DOCX round-tripping — never
- Custom Git server or hosted DraftGit platform — use GitHub

## How We'll Know V1 Works

The author writes a real paper using v1 (the dogfood test). v1 is done when:

1. Writing a paper start-to-finish feels less chaotic than the prior Overleaf/Dropbox workflow.
2. A co-author who doesn't know Git can leave comments and suggest edits via GitHub's PR UI with under 15 minutes of onboarding.
3. Answering "what did the paper look like on date X?" takes under 10 seconds via `git log` or `git checkout`.
4. `docs/pain-log.md` has at least 10 entries — real friction discovered by using the tool, which becomes the v1.1 backlog.
5. At least one external PhD student (not the author) completes a paper cycle with DraftGit and would recommend it to their advisor.

## Implementation Choices

- **CLI language: Python.** Fastest path from zero to shipping for a new engineer, huge ecosystem, `click` makes argument parsing trivial, `requests` makes the CrossRef call trivial, `pipx install draftgit` is a one-line install for users. Rust or Go can come later if performance matters (it won't for v1).
- **GitHub operations via `gh` CLI.** `draftgit new` shells out to `gh repo create --private`. Keeps DraftGit thin and avoids reimplementing GitHub's auth. Auth is **not** inherited magically — it flows only because we explicitly shell out to `gh` and read `git config`.
- **Build dispatch via filesystem detection.** `draftgit build` looks for `paper.typ`, `main.tex`, or `paper.md` and picks a compiler accordingly. No format config file needed in v1.
- **Privacy: private-by-default, explicit opt-in to public.** Protects pre-publication work by default.
- **Signing: optional.** `draftgit submit` checks `git config user.signingkey`. If set, tag is GPG-signed. If not, plain annotated tag. No new crypto dependencies in v1.

## Supported Formats

All three ship at v1 launch:

- **Typst** — fastest builds (milliseconds), cleanest errors, best for new authors. Primary reference implementation.
- **LaTeX** — still the dominant academic format. Shipping without it would cut off most of the target audience.
- **Markdown** (via Pandoc) — lowest barrier to entry, familiar to anyone who's written a README.

The cost of three formats is three templates + three CI workflows to maintain. That's acceptable because templates are static, CI configs are ~15 lines each, and the `draftgit build` dispatcher is a single switch statement.
