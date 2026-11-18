# Economics research project

Shared rules, skills, and hook code live in `.agents/`. Edit those source files directly. `CLAUDE.md` imports this file, and `.claude/rules` and `.claude/skills` link to the shared directories. Keep client-specific settings in `.claude/` and `.codex/`.

- At the start of each session, read `MEMORY.md` and, if present, `.claude/state/personal-memory.md`. Both clients use these notes. Apply relevant corrections, giving current user instructions and verified project state precedence over older notes.
- Follow the [project conventions](.agents/rules/standalone-conventions.md) for research discussions, writing, code, data, and math in chat. Apply their paragraph spacing and layered proof guidance to ordinary chat replies as well as saved documents.
- Before changing data loading, saved outputs, or paths, read the [file I/O guide](.agents/rules/standalone-file-io.md).
- For a research variant or a change of tier, follow the [exploration workflow](.agents/rules/workflow-exploration.md).
- For presentations, follow the [slides guide](slides/README.md) for editing, shared research inputs, and independent compilation.
- When reading a paper or inspecting a generated PDF, follow the [PDF guide](.agents/rules/standalone-pdf.md).
- Ask questions in plain text when a research choice needs the user's input. Present a plan when requested.
- Keep exploratory discussion in chat until writing or edits are requested. Carry out authorized changes without reconfirming, and preserve user-authored content outside the requested scope.
- Verify changes by running the affected code or compiling the document. Follow the [verification guide](.agents/rules/protocol-verification.md).
- Save project-specific corrections in `MEMORY.md` using `[LEARN:category] wrong → right`. Keep responses concise.

For work on the manuscript, read the [LaTeX build instructions](.agents/rules/standalone-latex-compile.md) before compiling. Rebuild after each edit to a `.tex` or `.bib` file. For a section or appendix edit, compile the full paper first and then the standalone subfile.
