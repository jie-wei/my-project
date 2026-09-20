# Compiling the Paper

This directory uses `latexmk` with a local `.latexmkrc`. Read this file before running any LaTeX command.

## Always

- **Run from `paper/`, or from `paper/sections/` / `paper/appendices/`.** The `.latexmkrc` here sets `TEXINPUTS`, the aux directory (`.build/`), and the cleanup command. Forwarding `.latexmkrc` files in `sections/` and `appendices/` (`do "../.latexmkrc";`) load this same config when invoked from those subdirectories — do not delete them. Running from the project root dumps aux files in the wrong place and fails to find template classes.
- **Use `latexmk -xelatex`, never raw `xelatex`/`pdflatex`/`bibtex`.** `latexmk` handles multi-pass compilation (bib, refs, toc) automatically. Raw commands leave the bibliography half-built.
- **Recompile after every edit to a `.tex` or `.bib` file.** Don't wait to be asked.
- **Recompile the touched subfile after `main.pdf`.** When editing a section or appendix file, also rebuild that file's standalone PDF (e.g., `sections/02-model.pdf`) so the user can preview the section in isolation. Citations resolve in subfile PDFs because `main.tex` hooks `\bibliography{references}` into `\AtEndDocument` whenever the `subfiles` class is loaded — the subfile's PDF gets its own References list. Cross-references to other subfiles use labels imported from `main.aux`; rebuild `main.tex` first to keep them current.
- **Keep `paper/paper-structure.md` current.** It is a one-line-per-file index of what each `.tex` file contains. Update it whenever a section is added, renamed, split, merged, or substantially repurposed. Read it before navigating an unfamiliar paper layout — it's faster than grepping `\section{}` headers.

## Three Modes

This paper is split with the `subfiles` package: `main.tex` holds the preamble and a chain of `\subfile{...}` includes; section bodies live in `sections/*.tex` and `appendices/*.tex`. Each section file starts with `\documentclass[../main.tex]{subfiles}` so it can compile either as part of the full paper or on its own.

### Full paper

```
cd paper
latexmk -xelatex main.tex
```

Produces `main.pdf` and preserves `main.aux` for cross-references in standalone subfile builds. This mode assembles all sections, appendices, and the bibliography.

For an untouched template with an empty `references.bib` and no citations, add `-bibtex-` to preview the scaffold. Remove that flag once bibliography entries and citations have been added.

### Single subfile from `paper/`

```
cd paper
latexmk -xelatex sections/01-introduction.tex
```

Produces `sections/01-introduction.pdf`. `$do_cd = 1` makes `latexmk` cd into the subfile's directory before compiling, so `\documentclass[../main.tex]{subfiles}` resolves correctly. Citations resolve through the subfile's own References list; cross-references to other subfiles resolve when `main.aux` is present and current.

### Single subfile from its own directory

```
cd paper/sections
latexmk -xelatex 01-introduction.tex
```

Same output. Useful when working interactively in `sections/` or when an IDE compiles the active file from its own directory.

## After a Successful Compile

`.latexmkrc`'s `$success_cmd` preserves `paper/main.aux`, then deletes `.build/` and the other build files (`.bbl`, `.blg`, `.brf`, `.fdb_latexmk`, `.fls`, `.log`, `.out`, `.synctex.gz`, `.toc`) automatically. `main.aux` supplies labels to standalone subfile builds and is an expected local artifact. Verify that `.build/` is gone and each requested PDF exists. If other build files linger, check the log for a failed run.

## When Compilation Fails

`latexmk` exits non-zero and leaves `.build/` in place so the log survives. To diagnose:

1. Read `.build/<jobname>.log` — search for the first line beginning with `!` (that's the actual error; everything after it is fallout).
2. Common causes:
   - Undefined `\cite{...}` — bib entry missing. `references.bib` is protected, so report the title/authors/year and ask the user to add it.
   - Inline citation without `\citet`/`\citep`/`\citealt` — use the proper command.
   - Missing package — install via `tlmgr`.
   - Typo in a `\subfile{...}` path.
   - Missing `\begin{document}`/`\end{document}` in a subfile.
3. Fix, recompile, verify `.build/` is cleaned up.

Don't run raw `xelatex` to "see the error" — the log from `latexmk` has the same information and keeps your build state coherent.

## Adding a New Section

1. Create `sections/NN-name.tex` (or `appendices/L-name.tex`) with:
   ```latex
   \documentclass[../main.tex]{subfiles}
   \begin{document}
   \section{...}
   \end{document}
   ```
2. Add `\subfile{sections/NN-name}` to `main.tex` in the right place in the chain.
3. Recompile the full paper to confirm it's wired in, and recompile the new subfile's standalone PDF as a preview.
