# Manuscript Lifecycle

## Core Workflow

ResearchGit should support a paper workflow that looks closer to software delivery than to file exchange.

1. Initialize a manuscript project.
2. Create or import manuscript source files and references.
3. Make isolated changes to sections, figures, or bibliography data.
4. Save revisions with meaningful history.
5. Review, compare, and merge edits from collaborators.
6. Prepare revision rounds and response changes.
7. Produce submission-ready artifacts.

## Key Entities

- manuscript files
- figures and tables
- bibliography and citation records
- revision messages
- branches or parallel editing tracks
- review comments and decision history

## Important User Scenarios

### Solo Author

Needs reliable version history, rollback, and citation consistency without heavy collaboration features.

### Co-Author Team

Needs parallel editing, merge-safe workflows, and clear attribution for changes.

### Revision Round

Needs explicit comparison between submission versions, reviewer responses, and resulting manuscript edits.

## First Implementation Focus

The initial workflow support should prioritize:

- creating a project
- tracking manuscript revisions
- basic branch-oriented collaboration concepts
- keeping citation data attached to the paper lifecycle

## Open Questions

- Which manuscript source formats should be first-class in v1: Markdown, LaTeX, DOCX, or a combination?
- How opinionated should the project layout be?
- Should citations be stored as BibTeX only, or through an internal normalized model?
- What is the minimum viable remote collaboration model?
