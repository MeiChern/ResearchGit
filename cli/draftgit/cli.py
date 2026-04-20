"""DraftGit command-line interface.

V1 implements a single verb: `draftgit new`. It scaffolds a paper
directory, initializes a Git repo with an initial commit, and (unless
--no-remote is passed) creates a private GitHub repo via `gh`.

The other three verbs from the v1 scope (`build`, `cite add`, `submit`)
are declared here as stubs so users discover the planned surface, but
they exit with a clear "not implemented in v1.0" message until the
corresponding pain-log evidence justifies building them.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import click


FORMATS = ("typst", "latex", "markdown")

TYPST_PAPER = '''\
#set document(title: "TITLE_PLACEHOLDER")
#set page(paper: "a4", margin: 2.5cm)
#set text(size: 11pt)
#set par(justify: true, leading: 0.7em)
#set heading(numbering: "1.")

#align(center)[
  #text(size: 18pt, weight: "bold")[TITLE_PLACEHOLDER]

  #v(0.5em)
  Your name \\
  _Your affiliation_ \\
  #datetime.today().display()
]

#v(1em)

#align(center)[
  #set par(justify: false)
  #block(width: 80%)[
    #text(weight: "bold")[Abstract.] Write your abstract here.
  ]
]

= Introduction

Write your paper here.

#pagebreak()
#bibliography("references.bib", style: "ieee")
'''

LATEX_PAPER = r'''\documentclass[11pt]{article}
\usepackage[margin=2.5cm]{geometry}
\usepackage{hyperref}

\title{TITLE_PLACEHOLDER}
\author{Your name}
\date{\today}

\begin{document}
\maketitle

\begin{abstract}
Write your abstract here.
\end{abstract}

\section{Introduction}

Write your paper here.

\bibliographystyle{ieeetr}
\bibliography{references}

\end{document}
'''

MARKDOWN_PAPER = '''\
---
title: "TITLE_PLACEHOLDER"
author: Your name
date: \\today
bibliography: references.bib
---

# Abstract

Write your abstract here.

# Introduction

Write your paper here.
'''

STARTER_BIB = '''\
@article{example-key,
  author  = {Last, First},
  title   = {An Example Reference},
  journal = {Journal of Example Studies},
  year    = {2026}
}
'''

GITIGNORE = '''\
# Compiled PDF output
*.pdf

# Typst cache
.typst-cache/

# LaTeX auxiliary files
*.aux
*.log
*.out
*.toc
*.bbl
*.blg
*.synctex.gz
*.fls
*.fdb_latexmk

# Editor / OS
.vscode/
.idea/
*.swp
.DS_Store
'''

BUILD_WORKFLOW_TYPST = '''\
name: Build paper PDF

on:
  push:
    branches: [main]
  pull_request:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: typst-community/setup-typst@v3
      - run: typst compile paper.typ paper.pdf
      - uses: actions/upload-artifact@v4
        with:
          name: paper-pdf
          path: paper.pdf
'''


def _run(cmd: list[str], cwd: Path | None = None) -> None:
    """Run a subprocess command, streaming output; exit on failure."""
    click.echo(f"$ {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd)
    if result.returncode != 0:
        click.echo(f"Command failed (exit {result.returncode}): {' '.join(cmd)}", err=True)
        sys.exit(result.returncode)


def _require_tool(name: str, install_hint: str) -> None:
    """Fail early if a required external tool is missing from PATH."""
    try:
        subprocess.run([name, "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        click.echo(
            f"Error: `{name}` is not installed or not on PATH.\n"
            f"Install it: {install_hint}",
            err=True,
        )
        sys.exit(1)


def _scaffold(title: str, fmt: str, target: Path) -> None:
    """Write template files into target for the given format."""
    target.mkdir(parents=True, exist_ok=False)

    if fmt == "typst":
        (target / "paper.typ").write_text(
            TYPST_PAPER.replace("TITLE_PLACEHOLDER", title)
        )
        workflows = target / ".github" / "workflows"
        workflows.mkdir(parents=True)
        (workflows / "build-paper.yml").write_text(BUILD_WORKFLOW_TYPST)
    elif fmt == "latex":
        (target / "main.tex").write_text(
            LATEX_PAPER.replace("TITLE_PLACEHOLDER", title)
        )
    elif fmt == "markdown":
        (target / "paper.md").write_text(
            MARKDOWN_PAPER.replace("TITLE_PLACEHOLDER", title)
        )

    (target / "references.bib").write_text(STARTER_BIB)
    (target / ".gitignore").write_text(GITIGNORE)
    (target / "README.md").write_text(
        f"# {title}\n\nA manuscript managed with [DraftGit](https://github.com/MeiChern/ResearchGit).\n"
    )


@click.group()
@click.version_option()
def main() -> None:
    """DraftGit: a Git-native manuscript workflow for academic papers."""


@main.command()
@click.argument("name")
@click.option(
    "--format",
    "fmt",
    type=click.Choice(FORMATS),
    default="typst",
    show_default=True,
    help="Manuscript format.",
)
@click.option(
    "--public",
    is_flag=True,
    default=False,
    help="Create a public GitHub repo (default: private).",
)
@click.option(
    "--no-remote",
    is_flag=True,
    default=False,
    help="Skip creating a GitHub repo; just scaffold and git init locally.",
)
def new(name: str, fmt: str, public: bool, no_remote: bool) -> None:
    """Scaffold a new paper: NAME is used as both the directory and repo name."""
    target = Path.cwd() / name
    if target.exists():
        click.echo(f"Error: {target} already exists.", err=True)
        sys.exit(1)

    _require_tool("git", "https://git-scm.com/downloads")
    if not no_remote:
        _require_tool("gh", "https://cli.github.com/")

    click.echo(f"Scaffolding {fmt} paper in {target}")
    _scaffold(name, fmt, target)

    _run(["git", "init", "-b", "main"], cwd=target)
    _run(["git", "add", "."], cwd=target)
    _run(["git", "commit", "-m", f"Initial scaffold ({fmt})"], cwd=target)

    if no_remote:
        click.echo(
            f"\nDone. Local repo at {target}. No GitHub remote created (--no-remote)."
        )
        return

    visibility = "--public" if public else "--private"
    _run(
        [
            "gh", "repo", "create", name,
            visibility,
            "--source", ".",
            "--remote", "origin",
            "--push",
        ],
        cwd=target,
    )
    click.echo(
        f"\nDone. GitHub repo created ({'public' if public else 'private'}). "
        f"Open it with: gh repo view --web"
    )


@main.command()
def build() -> None:
    """Compile the paper to PDF. (Not implemented in v1.0.)"""
    click.echo(
        "draftgit build is not implemented in v1.0.\n"
        "For now: `typst compile paper.typ paper.pdf` or `pdflatex main.tex` directly.",
        err=True,
    )
    sys.exit(2)


@main.group()
def cite() -> None:
    """Manage citations. (Not implemented in v1.0.)"""


@cite.command("add")
@click.argument("doi_or_url")
def cite_add(doi_or_url: str) -> None:
    """Fetch CrossRef metadata for a DOI/URL and append to references.bib. (Not implemented in v1.0.)"""
    click.echo(
        f"draftgit cite add {doi_or_url!r} is not implemented in v1.0.\n"
        "For now: look up the BibTeX entry manually and paste into references.bib.",
        err=True,
    )
    sys.exit(2)


@main.command()
@click.argument("name")
def submit(name: str) -> None:
    """Create an annotated `submit/NAME` tag marking a submission. (Not implemented in v1.0.)"""
    click.echo(
        f"draftgit submit {name!r} is not implemented in v1.0.\n"
        f"For now: `git tag -a submit/{name} -m 'Submitted'` does the same thing.",
        err=True,
    )
    sys.exit(2)


if __name__ == "__main__":
    main()
