# Research slides

Edit [slides.tex](slides.tex). The starter uses 12pt Beamer in 16:9 widescreen with the adapted Seminar Notes theme. Replace the title and example frame; add only the frames the talk needs. Keep one source file until splitting it helps.

## Visual style

Use the local [Seminar Notes theme](beamerthemeSeminarNotes.sty) for new slides. The theme, fonts, and optional layouts live in this folder; edit them directly when adapting the project.

| Element | Default |
| --- | --- |
| Presentation title and frame headings | Seminar Pen Semibold, the template's handwritten font |
| Body text, subtitles, result labels, captions, diagram labels, author details, and footers | Latin Modern Roman serif, preserving the previous starter's non-heading font |
| Equations | Latin Modern Math |
| Palette | Cream `#FCFAF4` background, ink blue `#233649` text, restrained red `#953B32` emphasis, muted `#535F67` secondary text |
| Layout | Spacious margins, left-aligned headings, flat result blocks, simple frame numbers, and no navigation icons |

Handwritten type is reserved for the presentation title and frame headings. Keep all other text in Latin Modern.

The required Seminar Pen fonts and their license are bundled in [fonts/](fonts/). Latin Modern is supplied by the TeX distribution and loaded by font filename so no separate system-font installation is needed. Compile with XeLaTeX.

Copy a frame from [layouts.tex](layouts.tex) when an equation, result, figure, comparison, or model timeline needs a different layout. These examples are optional and are not automatically included in the deck. Use the supplied `\pennote`, `\penunderline`, and `sn ...` TikZ styles sparingly for meaningful emphasis; non-heading annotations stay serif. Keep proof explanations layered and split crowded material across frames.

## Theory-talk rules of thumb

Use Shengwu Li’s [How to give an economic theory talk](https://zhu-wenbo.github.io/misc/Theory_Presentation_Advice.pdf) (March 4, 2023) as guidance, allowing reasoned exceptions.

- Teach the motivation, model, results, and limitations; aim at a second-year graduate student.

- Introduce the model before reviewing literature. Target minute 3, 7, or 10 for talks lasting 20, 45, or 75 minutes, respectively.

- Slides support speech through reminders, visuals, and precise statements. Keep most spoken explanation off-slide.

- Introduce abstract claims through simple, informative examples.

- Keep active notation near seven items; omit rarely reused symbols and remind listeners of returning ones.

- Make symbols distinguishable both visually and aloud.

- Include only equations worth reading; explain them and allow reading time.

- Distinguish proved statements, informal results, and conjectures.

- Use large type, whitespace, strong contrast, and consistent, accessible colors.

- Rehearse at conversational speed, allowing questions. Budget roughly two minutes per substantive slide; cut material instead of rushing.

These are defaults, not quotas. Apply our existing preferences alongside them: one main idea per frame, visible spacing, and proof arguments presented in layers—first why the major steps establish the result, then their justifications. Split material across frames when needed.

Preserve established project notation. If different talk notation would help, propose the change before using it and make the correspondence explicit. Keep the current Beamer starter; the advice guides content and readability rather than requiring a software change.

## Build and check

From the project root:

```bash
cd slides
latexmk -xelatex -interaction=nonstopmode -halt-on-error slides.tex
```

Run from `slides/` so latexmk loads its local configuration. The PDF appears beside the source; auxiliary files and logs stay in the ignored `.build/` directory. This deck builds independently of `paper/main.tex`.

Rebuild after edits to the deck or its included material. Check `.build/slides.log` for unresolved citations, references, missing glyphs, and overfull boxes; visually inspect affected pages. Keep text and equations readable by splitting crowded frames. Optional cleanup: `latexmk -c slides.tex` keeps the PDF and any cached bibliography.

## Reuse research material

- Use the latest agreed notation and assumptions from the paper or research notes. Preserve existing slides outside the requested edit, especially the author's motivation and narrative.
- Keep slides concise and suited to the audience and stage of the project. Use plain statements and equations by default; avoid decorative boxes around results. Add proof details or backup frames only when useful.
- Read generated figures and tables directly from `output/{tier}/`. For core results, use `\includegraphics[width=\textwidth]{variant/figure.pdf}` or `\input{../output/core/tables/variant/table.tex}`. For exploration or archive material, give the corresponding explicit path. Update these references when a variant moves tiers.
- Create `assets/` only for images made or collected specifically for the presentation. Keep generated research outputs in their canonical output folders.
- Use `\citet{key}` or `\citep{key}` with entries in the shared [paper bibliography](../paper/references.bib). When citations are added, put the following before `\end{document}`. The local build configuration makes `references.bib` available to BibTeX. The uncited starter needs no bibliography frame.

```latex
\begin{frame}[allowframebreaks]{References}
    \bibliographystyle{plainnat}
    \bibliography{references}
\end{frame}
```
