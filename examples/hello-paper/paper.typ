#set document(title: "ResearchGit Hello Paper", author: "Mei Chern")
#set page(paper: "a4", margin: 2.5cm)
#set text(size: 11pt)
#set par(justify: true, leading: 0.7em)
#set heading(numbering: "1.")

#align(center)[
  #text(size: 18pt, weight: "bold")[Hello, ResearchGit]

  #v(0.5em)
  Mei Chern \
  #link("mailto:meichern.nhrs@gmail.com") \
  #datetime.today().display()
]

#v(1em)

#align(center)[
  #set par(justify: false)
  #block(width: 80%)[
    #text(weight: "bold")[Abstract.]
    This is a minimal Typst paper used to verify the ResearchGit build
    pipeline. Every push to the repository rebuilds this document as a
    downloadable PDF artifact, so each commit has a compiled manuscript
    attached to it.
  ]
]

= Introduction

ResearchGit treats manuscripts the way software engineers treat code:
text-first, version-controlled, and reviewable through pull requests.
This example paper exists so the author (and anyone cloning the
template) can confirm end-to-end that the pipeline works before writing
real content.

= How to use this example

1. Edit this file (`examples/hello-paper/paper.typ`).
2. Commit and push.
3. Open the *Actions* tab on GitHub — the *Build paper PDF* workflow
   should run and produce `hello-paper-pdf` as a downloadable artifact.
4. For a new paper, copy this directory to a fresh repository and
   rename as appropriate.

= Citations

Citations use a standard BibTeX file at `references.bib`. Once you add
entries to that file, you can cite them like this: @example-key.

#pagebreak()
#bibliography("references.bib", style: "ieee")
