# ResearchGit

ResearchGit is a Git-native workflow for academic manuscripts. The goal is to make research writing more reproducible, collaborative, and automation-friendly by combining manuscript versioning, citation management, and structured review workflows.

## Why ResearchGit

Academic writing still depends heavily on ad hoc file sharing, manual revision tracking, and fragmented feedback loops. ResearchGit is intended to improve that by treating papers more like modern engineering artifacts:

- Track manuscript revisions with clear history
- Support collaborative writing through branching and merging
- Manage citations in a structured, versioned workflow
- Enable reproducible review and revision cycles
- Create a foundation for AI-assisted research automation

## Initial Scope

The first implementation should stay narrow:

- text-first manuscript workflows
- Git-friendly version history and collaboration
- structured citation handling
- support for `LaTeX`, `Markdown`, and `Typst`

`Typst` is in scope from the start because it is text-based, diffable, and well aligned with version-control workflows.

## Vision

ResearchGit is aimed at an end-to-end workflow for research teams:

- Manuscript version control for papers, figures, and references
- Collaboration workflows inspired by pull requests and code review
- Citation-aware project structure with BibTeX-style interoperability
- Automation hooks for literature review, writing assistance, and reporting
- A future submission pipeline for journals and conferences

## Current Status

This repository is currently in the definition stage. The immediate focus is to build the project structure and documentation before implementation begins.

## Non-Goals For V1

- Not a full journal submission platform
- Not a replacement for every reference manager
- Not a WYSIWYG collaborative word processor
- Not an AI-first writing system before core manuscript state is reliable

## Repository Structure

```text
docs/                  project definition and technical planning
sharing/               presentations and external communication materials
```

The documentation entry point is [docs/README.md](docs/README.md).

## Roadmap

1. Define the repository structure and project scope.
2. Design the core manuscript versioning workflow.
3. Add citation management concepts and data model.
4. Explore collaborative review and remote sync workflows.
5. Prototype AI-assisted research automation features.

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE).
