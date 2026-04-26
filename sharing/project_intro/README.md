# ResearchGit Project Intro

This folder contains a Reveal.js slide deck and a direct PDF export script.

## Files

- `index.html`: slide deck source
- `theme.css`: custom presentation styling
- `vendor/reveal/dist/`: pinned local Reveal.js runtime assets
- `export_pdf.sh`: headless Chrome PDF export command

## Export

From the repository root:

```bash
chmod +x sharing/project_intro/export_pdf.sh
./sharing/project_intro/export_pdf.sh
```

The exported file is:

```text
sharing/project_intro/researchgit_project_intro.pdf
```
