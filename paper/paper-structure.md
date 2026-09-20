# Paper Structure

One-line description of what each `.tex` file holds. **Update this file whenever a section is added, renamed, split, merged, or substantially repurposed.** Keep entries terse — the goal is a fast index, not a TOC.

## Body

| File | Contents |
|------|----------|
| `main.tex` | Preamble, title/author/abstract, `\subfile{}` chain, bibliography hook |
| `sections/01-introduction.tex` | Introduction (TBD) |
| `sections/02-next-section.tex` | (Rename and describe — e.g., "§2 Model. Setup, primitives, equilibrium concept.") |

## Appendix

| File | Contents |
|------|----------|
| `appendices/A-proofs.tex` | Proofs of results stated in the body |
| `appendices/B-extensions.tex` | Extensions and robustness checks |

## Archive

`archive/` holds previous drafts and obsolete stubs. Not part of the compile chain. Do not edit.

## References

- `references.bib` — protected; do not edit. Report missing entries to the user.
