# DraftGit CLI

A Git-native manuscript workflow for academic papers. The v1.0 CLI
implements `draftgit new`; the other three verbs (`build`, `cite add`,
`submit`) are defined in the scope but stubbed in code pending pain-log
evidence that they're worth building.

## Requirements

- Python 3.9+
- `git` on PATH
- `gh` (GitHub CLI) on PATH, authenticated with `gh auth login` (only
  needed for repo creation; skip with `--no-remote`)

## Install (development / editable)

From the repo root:

```
pipx install -e cli/
```

Verify:

```
draftgit --help
```

If you don't have `pipx`, use `pip install -e cli/` inside a virtual
environment instead.

## Usage

Create a new paper — Typst, private GitHub repo, default settings:

```
draftgit new my-thesis
```

Other formats:

```
draftgit new my-thesis --format latex
draftgit new my-thesis --format markdown
```

Create a **public** repo (explicit opt-out of the private default):

```
draftgit new my-thesis --public
```

Scaffold locally without creating a remote (useful for offline work or
when you want to push to a remote you configure yourself later):

```
draftgit new my-thesis --no-remote
```

## What `draftgit new` does

1. Creates a directory called `my-thesis/` in the current working
   directory.
2. Writes starter files for the selected format: `paper.typ`,
   `main.tex`, or `paper.md`, plus `references.bib`, `.gitignore`, and
   `README.md`. Typst projects also get a `.github/workflows/build-paper.yml`
   that compiles the PDF on push.
3. Runs `git init -b main`, `git add .`, and `git commit -m "Initial
   scaffold (<format>)"`.
4. Unless `--no-remote` is set, runs `gh repo create <name> --private
   --source . --remote origin --push` to create and push to a private
   GitHub repo.

## What's intentionally not in v1.0

- **`draftgit build`** — compile locally. Stubbed. Use `typst compile
  paper.typ paper.pdf` or `pdflatex main.tex` directly until the pain
  log justifies a wrapper.
- **`draftgit cite add <doi>`** — fetch CrossRef metadata. Stubbed.
  Paste BibTeX manually for now.
- **`draftgit submit <name>`** — create a submission tag. Stubbed. Use
  `git tag -a submit/<name> -m "Submitted"` for now.

These stubs print a one-line message pointing to the vanilla-Git
equivalent, so users discover the planned surface without the CLI
over-promising on functionality it doesn't yet have.

## Uninstall

```
pipx uninstall draftgit
```
