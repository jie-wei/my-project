---
name: review-literature-synoptic
description: Build a neutral understanding of a literature by decomposing it into three levels — ingredients (what papers assume about the world), questions (what they ask), and answers (what they find). Produces an ingredient tree, thematic question sections, and an ingredient-by-question matrix. Use this skill when the user asks to "map the literature", "build an ingredient tree", "what does the literature assume", "synoptic review", "decompose the literature", "what questions does the literature ask", "understand the literature", or wants to see the landscape of a field on its own terms. This is the UNDERSTANDING skill — it describes what the literature contains and how papers connect to each other. For positioning our paper against the literature, use /review-literature-comparison instead.
disable-model-invocation: true
argument-hint: "[topic or literature to map]"
---

# Synoptic Literature Review

Build a structured understanding of an entire literature by decomposing papers into three levels:

1. **Ingredients** — what facts about the world each paper takes as given (model building blocks)
2. **Questions** — what each paper asks about that world
3. **Answers** — what each paper finds for a given (ingredient, question) pair

This skill understands the literature on its own terms. It traces how papers connect to each other — who introduced what, who extended whom, what the field has collectively learned. It does not read the literature through the lens of any particular new paper or thesis.

**Input:** `$ARGUMENTS` — a topic, field, or set of papers to map.

---

## Mode Detection

Parse `$ARGUMENTS`:
- **`deepen`** → run the Deepen workflow (enriches existing entries from paper summaries or original full text)
- **`merge`** → run the Merge workflow (integrates newly read papers into an existing synoptic review)
- **Anything else** → standard synoptic review (Steps 1-3 below)

---

## Sources

Build on existing work rather than starting from scratch:

1. **Read individual paper summaries or original sources** in `docs/literature/` and any user-supplied locations. Summaries can contain model details, key findings, and core assessments; when absent, read the relevant paper directly. Do NOT read `summary-literature-comparison*.md` — that is a comparison review written through the lens of our paper, and importing its framing would contaminate the synoptic review's neutrality.
2. **Read the paper body** for any features/ingredients section — it may already contain an ingredient tree. The body lives in `paper/sections/*.tex` and `paper/appendices/*.tex`; `paper/main.tex` only holds the preamble and `\subfile{...}` chain, so reading `main.tex` alone is not enough.
3. **Check `paper/references.bib`** for papers already in the project.
4. **Use `WebSearch`** to find recent publications that may be missing from local files.
5. **Use `WebFetch`** to access working paper repositories and abstracts.

Use an existing individual paper summary when available. Otherwise read the original PDF or full text directly, following the [PDF guide](../../rules/standalone-pdf.md). Match the paper and version, read the sections supporting each substantive claim, and retain page, section, or result references. A separate summary file is optional.

Use the available search and page/PDF-reading tools in either client; `WebSearch` and `WebFetch` below name Claude's equivalents. If only an abstract is accessible, label the entry as preliminary and retain `[UNSUMMARIZED]`. Do not infer detailed assumptions or theorems from an abstract. Report unavailable sources without blocking work on accessible papers.

---

## Output Format

Read the bundled template at `templates/template-summary-literature-synoptic.md` (relative to this skill's directory) as the starting structure. The template has 10 sections:

1. **Thesis** — what the entire literature is trying to understand, and an overview of what it has collectively found
2. **Framework** — what these papers have in common; the ingredient tree is the core of this section
3. **Scope** — what literature is covered, what's excluded
4. **Literature by Question Theme** — organized by common questions, tracing intellectual evolution, synthesis at end of each theme
5. **Ingredient x Question Matrix** — compact glance at the whole literature
6. **Most Important Papers** — landmarks, what they settled, what remains open
7. **Combination Papers** — papers that combine existing ingredients
8. **Formal Tools** — methodology papers
9. **Gaps and Open Questions** — empty cells in the matrix + unexplored territory
10. **Key Papers Index** — question-theme-organized reference list

**Why this structure matters.** The 10-section structure separates three things that are easy to conflate: (a) what the world looks like in these models (Section 2 — ingredients), (b) what questions people ask about it (Section 4 — themes), and (c) what they find (Section 5 — matrix). It also prevents a common failure mode: drifting into comparison with our own paper. If you find yourself writing "connection to our thesis" or "what they miss relative to us," stop — you are writing a comparison review. Use `/review-literature-comparison` for that.

---

## Step 1: Thesis and Framework (Sections 1-3)

**Thesis (Section 1).** One paragraph: what unites this literature? What is it collectively trying to understand? What has it found? This is the literature's thesis, not any single paper's.

**Framework (Section 2).** What do these papers share? The ingredient tree is the heart of this section. Build it following these lessons from experience:

- **Start with plain language.** "They may observe all prices, or only some" — not "Price observability heterogeneity across buyers." Technical terms should emerge naturally from the plain descriptions, not replace them. Every ingredient should be understandable by someone who has never studied the field.
- **Use nesting for sub-cases.** When an ingredient has variants, list the variants as sub-points with citations showing which paper introduced each variant.
- **Order by generality.** More general/foundational ingredients first, specialized ones later. Within a level, order by publication date when natural.
- **Cite one primary paper per leaf.** The paper that *introduced* this specific ingredient as its main contribution. Papers that *combine* existing ingredients don't get cited here — they appear in Sections 5 and 7.
- **Separate what the world looks like from what we ask about it.** "Sellers might collude" is a question, not an ingredient. "Sellers might not know what other sellers are charging" is an ingredient.
- **Group by agent or role.** Organize the tree by who the ingredient describes — the natural groupings depend on the literature (e.g., in a two-sided market it might be demand side vs. supply side vs. intermediary; in a macro literature it might be households vs. firms vs. government).

**Scope (Section 3).** What literature is surveyed? What falls outside? If there is a natural partition, state the criterion.

---

## Step 2: Literature by Question Theme (Section 4)

Organize the literature by the common questions it asks. Questions fall into recurring themes — discover these themes from the papers rather than imposing them. Read what each paper actually asks, group similar questions together, and name the themes in the language the literature itself uses. Do not start from a predetermined list of theme categories — the themes should emerge from the papers. Different literatures ask different questions; the themes should reflect what *this* literature cares about.

**Each question theme sub-section should:**
1. Define the question (1-2 sentences, plain language)
2. List key papers tracing the intellectual evolution — who asked it first, who extended it, how the answer changed over time
3. For each paper entry, include a **Connection** sub-bullet that traces how this paper relates to the seminal paper or the paper that came before it on this question. This is about intellectual genealogy — how understanding evolved — not about comparison to our work.
4. End with a **"What the literature has learned"** synthesis paragraph — what has this line of work collectively established? What remains debated?

**Key paper entry format** (used in Sections 4 and 10):
```
- **Author (Year, Journal)** — [Summary](summary-year-author.md)
    - **Model:** [setting]
    - **Main contribution:** [what the paper does]
    - **Key finding:** [specific result, with theorem/proposition number]
    - **Connection:** [how it relates to earlier papers on this question — the evolution]
```

Use bullet points and sub-bullets for factual content. Reserve prose paragraphs for synthesis ("What the literature has learned"). The reason: bullet-point structure makes factual content scannable, while synthesis reads better as connected prose.

---

## Step 3: Matrix, Landmarks, and Remaining Sections (Sections 5-10)

**Ingredient x Question Matrix (Section 5).** The matrix is the compact map of the entire literature. Each cell answers: "what does the literature say about [ingredient] in the context of [question]?" Getting these answers right matters — a vague or generic cell defeats the purpose.

**Building the matrix (three-step process):**

1. **Map papers to cells.** For each (ingredient, question theme) pair, identify which papers address it. A paper belongs in a cell if it takes the ingredient as a modeling primitive and asks a question in that theme. Write this mapping to a temp file — it is the input for step 2.

2. **Fill cells in parallel.** For each non-empty cell, spawn a sub-agent that reads the summaries or original full text for the papers in that cell and writes a one-phrase answer + citation. The sub-agent's prompt: "Read [summary or original-source paths]. In one phrase, what does this literature find about [ingredient] in the context of [question theme]? Include the key citation." Each sub-agent sees only its own papers and produces one cell entry. This parallelization is the reason the matrix can be both concise and accurate — each cell gets focused attention grounded in the actual sources, not LLM memory.

3. **Assemble sub-matrices.** Collect all cell entries and arrange them into sub-matrices. **Split into multiple sub-matrices** when there are more than 3-4 question columns — a single wide table is unreadable in markdown and PDF. Group related question themes into each sub-matrix. Each sub-matrix shares the same ingredient rows but covers a different subset of question columns. Add a brief heading above each sub-matrix indicating which themes it covers. Use `—` for empty cells.

**Most Important Papers (Section 6).** The 5-10 landmark papers. For each: what question they settled or opened, what they established (specific results), what remains open after them. This is from the field's perspective. Include an assessment summary table.

**Combination Papers (Section 7).** Papers that don't introduce new ingredients but combine existing ones. Format: "combines [A] + [B]. Asks: [Q]. Finds: [answer]."

**Formal Tools (Section 8).** Methodology papers. One sentence each: what it provides.

**Gaps (Section 9).** Empty cells in the matrix + open questions nobody has asked. Reference specific cells.

**Key Papers Index (Section 10).** Question-theme-organized reference list with summary links. Must mirror the structure of Section 4 — same theme names, same ordering.

---

## Deepen Workflow

Use this mode to improve existing synoptic entries with a detailed reading of summaries or original papers.

1. **Find the requested review and entries.** Look in `docs/literature/summary-literature-synoptic*.md`.

2. **Find usable sources.** Look for matching `summary-*.md` files, local PDFs, supplied links, or accessible full text. Check paper identity and version. Read the original paper when a summary is absent or insufficient.

3. **Proceed within the requested scope.** Read available sources directly; no separate paper-reading command or additional approval is required. Report unavailable sources and retain preliminary tags for those entries.

4. **Update each entry from the evidence.**
    - Describe the model ingredients, contribution, and findings with the assumptions and source locations that support them.
    - Ground the connection to earlier work in the actual papers.
    - Link an existing summary, or link the original paper and identify its relevant pages or results.
    - Remove `[UNSUMMARIZED]` only after enriching the entry. Keep `[UNVERIFIED]` until the citation details are checked.

5. **Update the map.** Revisit the ingredient tree, theme syntheses, matrix, and index when the reading changes the field's picture. Keep repeated entries' links and tags consistent.

### Entry format after deepening

```markdown
- **Author (Year, Journal)** — [Paper](actual-source-url-or-relative-path)
    - **Model:** [Setting and necessary assumptions]
    - **Main contribution:** [Supported claim]
    - **Key finding:** [Result with section, page, or proposition reference]
    - **Connection:** [How this advances or changes earlier work on the question]
```

Use a `Summary` link instead when a summary file exists. Retain any unverified-citation tag.

---

## Merge Workflow

When the user says `merge`, "add new papers", "integrate these into the synoptic review", or similar — this mode integrates newly read papers into an existing synoptic review. Unlike `deepen` (which enriches *existing* entries), merge handles papers that are *not yet in the review at all*.

### Why this is different from `deepen`

`Deepen` assumes the entry already exists with `[UNSUMMARIZED]` tags. `Merge` handles a harder problem: new papers need to be *classified* (ingredient paper? question-answering paper? combination? tool?), *placed* in the right sections, and may trigger *cascading updates* across multiple sections. The failure modes are: (a) putting a paper under the wrong question theme, (b) forgetting to update the matrix, (c) adding a paper to Section 4 but not Section 10, (d) adding a new ingredient without updating the tree.

### Steps

1. **Identify new papers.** Start with the papers the user supplied or requested. If asked to scan the local collection, check summaries and original papers in `docs/literature/`. Compare paper identities and versions against existing review entries, rather than treating a missing summary link as a new paper.

2. **Triage each paper.** For each new paper, read its summary or original full text and classify it:
   - **Ingredient paper** → introduces a new building block (update ingredient tree in Section 2 + relevant question themes in Section 4 + matrix in Section 5)
   - **Question-answering paper** → answers an existing question with existing ingredients (add to question theme in Section 4 + matrix in Section 5)
   - **Combination paper** → combines existing ingredients (Section 7 + matrix in Section 5)
   - **Formal tool** → provides methodology (Section 8)
   - **Needs a new question theme** → if the paper asks a question not covered by existing themes, consider creating a new 4.N subsection. Ask the user before creating new themes.

3. **Plan the merge.** Before editing, produce a merge plan listing:
   - Which section(s) each paper will be added to
   - Whether any new question themes are needed
   - Whether any "What the literature has learned" synthesis paragraphs need updating
   - Whether the ingredient tree needs new entries

   Present the plan to the user for approval.

4. **Execute the merge.** For each paper, update ALL relevant sections:

   **Checklist per paper:**
   - [ ] Section 2: update ingredient tree if new ingredient
   - [ ] Section 4: add to appropriate question theme (with Model, Main contribution, Key finding, Connection sub-bullets)
   - [ ] Section 4: update "What the literature has learned" paragraph if the new paper changes the synthesis
   - [ ] Section 5: add cell to matrix
   - [ ] Section 6: add to landmark assessment if this is a major paper
   - [ ] Section 7: add if combination paper
   - [ ] Section 10: add to index (must mirror Section 4 structure)

   **Parallelization guidance.** As the review grows large (>300 lines), a single agent may struggle with context. Use sub-agents, but split by *section*, not by paper:
   - One agent for Section 2 + 4 edits (needs: the new papers or summaries + current sections to know where to place entries)
   - One agent for Section 5 + 10 edits (needs: list of new papers + which question theme each belongs to — provide this as input, don't make the agent figure it out)

   Each agent edits *different lines* of the same file, so they won't conflict. But do NOT run two agents on the same section. And if using cloud sync (Dropbox), run agents sequentially or write to temp files first, then merge.

   The key context each agent needs: (a) the summary or original-source file(s) for its papers, (b) the specific section it's editing, (c) the merge plan (which papers go where). Provide the merge plan explicitly — don't make sub-agents rediscover the classification.

5. **Revisit Sections 1-3.** After merging new papers, re-read Sections 1 (Thesis), 2 (Framework/Ingredient Tree), and 3 (Scope). These are high-level summaries that can only be written well after understanding the full literature. New papers may introduce ingredients that reshape the tree, open new question themes that change the thesis, or extend the scope. Update as needed.

6. **Verify consistency.** After all edits, run through this checklist. These checks catch the most common failure mode — sections drifting out of sync after incremental additions:
   - Every theme in Section 10 should correspond to a theme in Section 4 (same names, same ordering). If you added a new 4.N, Section 10 must have a matching subsection.
   - Every paper in Section 4 should appear in Section 10, and vice versa
   - Ingredient tree (Section 2) includes all ingredients referenced in the matrix (Section 5)
   - Remove `[UNSUMMARIZED]` only after reading the relevant source and incorporating its evidence; the mere existence of a summary file is insufficient
   - New "What the literature has learned" paragraphs exist for any new question themes
   - The matrix (Section 5) has cells for all new papers

### When to create new question themes

Create a new theme (4.N) when:
- 2+ new papers ask a question not covered by existing themes
- A single paper opens a fundamentally new line of inquiry (not just a variant of an existing question)
- The user explicitly requests it

Label cross-cutting themes explicitly (e.g., "4.N [Theme Name] (Cross-Cutting)") to distinguish them from the core themes.

---

## Output Location

Save to `docs/literature/`:

| Type | Filename |
|------|----------|
| Overall synoptic review | `summary-literature-synoptic.md` |
| Topic-specific synoptic | `summary-literature-synoptic-[short-description].md` |

If the project has `paper/references.bib`, offer to append new BibTeX entries. Note: `references.bib` is a protected file — the user must confirm before editing.

---

## Parallelization Guidance (Standard Review)

For a literature with 30+ papers, building the synoptic review in a single pass may exceed context. The work has a natural dependency structure — some parts can run in parallel, others must wait. Think in terms of *information independence*, not section numbers.

**Step 1 — Parallel: Per-paper extraction.** Spawn one agent per paper (or per batch of 5-10 papers). Each agent reads one paper's summary or original full text and extracts: what ingredients does this paper assume? What question does it ask? What does it find? These are completely independent — no agent needs to see another paper's summary. Each agent writes its output to a temp file.

**Step 2 — Sequential: Assembly.** The main agent reads all extraction outputs and assembles: build the ingredient tree (group and nest ingredients), discover question themes (what common questions emerge from the extracted questions), and assign each paper to its theme. This step requires seeing all papers together to find the right groupings — it cannot be parallelized.

**Step 3 — Parallel: Write question theme sections.** Once themes are identified and papers assigned, spawn one agent per question theme. Each agent gets: (a) the theme definition, (b) the papers assigned to it with their extracted ingredients/questions/answers, (c) the ingredient tree for reference. Each theme section is independent — the agent writes the paper entries, traces the intellectual evolution, and writes the "What the literature has learned" synthesis. Each agent writes to a temp file.

**Step 4 — Sequential: Final assembly.** The main agent merges all theme sections and writes the remaining parts: thesis, framework (with ingredient tree from Step 2), scope, matrix, most important papers, combination papers, formal tools, gaps, and key papers index. These require the full picture.

**Summary:** parallel → sequential → parallel → sequential. If using cloud sync (Dropbox), all agents should write to temp files; the main agent merges at the end.

---

## Anti-patterns

- Do NOT organize Section 4 by ingredient alone — the question themes are the organizing principle, not the ingredients. The ingredient tree lives in Section 2; Section 4 is organized by *what questions people ask*.
- Do NOT write synthesis paragraphs that compare to our paper — "What the literature has learned" is about the field's collective understanding, not about how it relates to us.
- Do NOT put combination papers in the ingredient tree — the tree is for papers that *introduce* ingredients. Papers that combine existing ingredients go in Section 7.
- Do NOT let the matrix grow beyond what fits on a page — split into multiple sub-matrices by grouping related question columns (max 3-4 question columns per table). Also aggregate related ingredients into groups for the matrix rows if there are too many.
- Do NOT omit summary links on paper entries when the summary file exists — every entry must link to its summary.

---

## PDF Export When Requested

Use ordinary local compilation tools; no conversion skill is required. With Pandoc and XeLaTeX available, run from the review's directory, substituting its actual filename:

```bash
pandoc "review.md" --from=markdown+tex_math_dollars+raw_tex --pdf-engine=xelatex -V fontsize=12pt -V geometry:margin=1in -V linestretch=1.1 -o "review.pdf"
```

If Pandoc is unavailable, create an equivalent LaTeX source in a temporary build directory and compile it with `latexmk -xelatex -interaction=nonstopmode -halt-on-error review.tex`. Preserve the text, nested lists, math, tables, and links. Resolve relative source and image paths from the original review's directory.

Use 12pt serif text, comfortable paragraph and list spacing, and a new page for each major section. For Pandoc, put `\newpage` before major sections in the export source and use a temporary LaTeX header via `--include-in-header` when needed for spacing. Keep figures with their explanations and split wide tables. Inspect the resulting PDF using the [PDF guide](../../rules/standalone-pdf.md). Report a missing compiler or failed build rather than claiming a PDF was produced.

---

## Important

- **This is NOT a comparison review.** Do not read papers through the lens of any thesis. Do not write "connection to our paper" or "relevance to our argument." The "Connection" field traces how papers relate to *each other* (intellectual evolution), not to our work. If you find yourself comparing to our paper, stop — use `/review-literature-comparison` for that.
- **Plain language first.** Every ingredient should be understandable by someone outside the field. Technical terms can appear in parentheses, but the plain statement comes first.
- **The ingredient tree is the core.** Spend the most effort making it clear, well-nested, and well-cited. It is the framework that organizes everything else.
- **Citation format.** Always include the journal abbreviation: **Author (Year, Journal)**. Standard abbreviations: AER, Ecma, JPE, QJE, REStud, RAND, JIE, TE, JET, AEJ:Micro, MS. For working papers, use "WP." This lets the reader gauge venue without clicking through.
- **Summary links are mandatory.** Every paper entry must include a `[Summary](summary-year-author.md)` link if the summary file exists. Before writing entries, scan `docs/literature/summary-*.md` to build a list of available summaries. When no summary file exists, link the original paper as `[Paper](...)` with relevant page or result references. Reading status depends on the evidence incorporated, not on the presence of a summary file.
- **Tags.** Use `[UNSUMMARIZED]` until a substantive summary or original paper has been read and the entry updated with supported claims and source locations. This may occur during review, deepening, or merging. Use `[UNVERIFIED]` until citation details have been checked against a reliable bibliographic source or verified project entry. A file's existence alone does not clear either tag.
- **Use 4-space indentation for nested lists.** Use 4 spaces per nesting level for reliable Pandoc output. Also add a blank line between a bold header (like `**Buyers**`) and the list that follows it, so pandoc treats them as separate blocks.
- **Write math for PDF compatibility.** Use explicit LaTeX math delimiters, including single symbols: `$\beta$`, `$\mu \to 1$`, `$N_{eff}$`. Brace multi-character subscripts. Do not rely on a custom Unicode preprocessor.
- **Use bullet points and sub-bullets** for factual content (paper descriptions, gap lists, index entries). Reserve prose for synthesis paragraphs ("What the literature has learned") and landmark assessments. Each bullet should make one claim or state one fact.
- **Do NOT fabricate citations.** If unsure about a paper's details, flag it for the user. Getting a citation wrong is worse than omitting it.
- **BibTeX fields from memory are unreliable.** Mark unverifiable fields with `% UNVERIFIED` comments.
- **Prioritize recent work** (last 5-10 years) unless seminal papers are older.
- **Note working papers vs published papers** — working papers may change before publication.
- **Handle web tool failures gracefully.** If WebSearch or WebFetch fail, analyze only local files and note what could not be searched.
- **Verify URLs.** Use WebSearch to find real, clickable URLs. Prefer stable links: journal pages, EconPapers/IDEAS/RePEC, SSRN, NBER. Never guess URLs.
- **Consistency checks.** After any edit, verify: Section 10 mirrors Section 4 theme structure. Every paper in Section 4 appears in Section 10. Ingredient tree covers all ingredients in the matrix. No stale tags.
