---
name: review-literature
description: Structured literature search and synthesis with citation extraction and gap identification. Use when the user asks to survey literature, find related work, check novelty of results, or says "do a literature review", "extended search", "what's the related literature on X". Also triggers when the user wants to compare their paper's results against existing work. Has a "deepen" mode that enriches existing literature review entries using summary files from /read-paper — triggers on "deepen the lit review", "enrich entries", "update with summaries".
disable-model-invocation: true
argument-hint: "[topic, paper title, or research question]"
---

# Literature Review

Conduct a structured literature search and synthesis on the given topic.

**Input:** `$ARGUMENTS` — a topic, paper title, research question, or phenomenon to investigate. If `$ARGUMENTS` is `deepen`, run the Deepen workflow instead (see below).

---

## Mode Detection

Parse `$ARGUMENTS`:
- **`deepen`** → run the Deepen workflow (enriches existing entries using `/read-paper` summaries)
- **Anything else** → standard literature review (Steps 1-7 below)

---

## Steps (Standard Review)

1. **Parse the topic** from `$ARGUMENTS`. If a specific paper is named, use it as the anchor.

2. **Establish the comparison target.** The review should position literature findings against *our* work. What counts as "our work" depends on the project stage:
   - If the conversation already makes the target clear (e.g., the user just discussed a result, or pointed to a file), use that context directly — no need to ask.
   - If `paper/main.tex` (or `paper/main.pdf`) exists and hasn't been read this session, read its introduction, main results, and related literature sections as the default anchor.
   - If no draft exists yet, check `docs/core/` and `docs/exploration/` for analysis notes that capture the project's current thinking.
   - If none of the above applies — or if the topic is narrow enough that the general draft isn't the right comparator — ask the user what to compare against before proceeding.

3. **Search for related work** using available tools:
   - Check `docs/literature/` for existing literature review files
   - Check `docs/core/` and `docs/exploration/` for existing analysis notes
   - Check `paper/references.bib` for papers already in the project
   - Use `WebSearch` to find recent publications
   - Use `WebFetch` to access working paper repositories and abstracts

4. **Organize findings** into these categories:
   - **Theoretical contributions** — models, frameworks, mechanisms
   - **Empirical findings** — key results, effect sizes, data sources
   - **Methodological innovations** — new techniques, research designs, analytical tools
   - **Open debates** — unresolved disagreements in the literature

5. **Identify gaps and opportunities:**
   - What questions remain unanswered?
   - What data or methods could address them?
   - Where do findings conflict?
   - How do our results fill these gaps?

6. **Extract citations** in BibTeX format for all papers discussed.

7. **Save the report** — see Output Location below.

---

## Output Format

Read the bundled template at `templates/summary-literature.md` (relative to this skill's directory) as the starting structure. The key sections are:

### Summary
2-3 paragraph overview positioning the state of the literature relative to our paper's contribution.

### Key Papers

For each paper, use this format:

```markdown
### [Author (Year)](URL) — Short Title `[UNSUMMARIZED]` `[UNVERIFIED]`

- **Publication:** *Journal Name*, vol. X(Y), pp. Z
- **Main contribution:** [1-2 sentences]
- **Method:** [Research design / data]
- **Key finding:** [Result with effect size if available]
- **Relevance to our paper:** [How it relates to our specific results — compare, contrast, complement]
```

### Tags

Every paper entry starts with **two tags** by default:

- **`[UNSUMMARIZED]`** — the literature review entry has not been enriched with a deep reading. Removed only by `/review-literature deepen` after it reads the corresponding `summary-*.md` file produced by `/read-paper` and updates the entry.
- **`[UNVERIFIED]`** — citation details come from LLM memory, not a verified source. Remove only after confirming via WebSearch/WebFetch (verified URL, correct journal/volume/pages) or if the entry already exists in `paper/references.bib`.

**Tag lifecycle for `[UNSUMMARIZED]`:**
1. `/review-literature` adds the tag when creating the entry
2. User downloads the PDF and runs `/read-paper` → produces a `summary-*.md` file (tag stays)
3. User runs `/review-literature deepen` → reads the summary, enriches the entry, replaces `[UNSUMMARIZED]` with a clickable link to the summary file

Papers already in `paper/references.bib` can drop `[UNVERIFIED]`. Papers with a verified URL from WebSearch can drop `[UNVERIFIED]`. Neither tag should be removed just because the information *seems* correct.

### Thematic Organization

Group papers into themes relevant to the paper's contribution. Themes should be driven by the content, not by a fixed template. Common patterns:
- Organize around the paper's main results and how existing work relates to each
- Group by mechanism, method, or debate
- Include a theme for empirical evidence if relevant

Within each theme, discuss how existing papers relate to each other *and* to our paper. The value is in the synthesis and positioning, not just the listing.

### Gaps and Opportunities, Suggested Next Steps, BibTeX Entries

See template for structure.

---

## Deepen Workflow

When the user says `deepen`, "enrich the lit review", "update entries with summaries", or similar — this mode upgrades literature review entries using the deep summaries produced by `/read-paper`.

The idea: initial entries are written from abstracts and LLM memory (shallow). After `/read-paper` produces a `summary-*.md` file, you can go back and enrich the entry with real understanding — better descriptions, more accurate "Relevance to our paper" assessments, and updated thematic synthesis.

### Steps

1. **Find literature review files** — scan for entries with `[UNSUMMARIZED]` tags in:
   - `docs/literature/summary-literature*.md`
   - `docs/literature/review-literature*.md` (legacy naming)
   - `docs/core/lit_review_*.md`
   - `docs/exploration/**/lit_review_*.md`

2. **Find matching summary files** — for each `[UNSUMMARIZED]` entry, search for a corresponding `summary-{year}-{author}.md` file (match by author name and year). Check these locations:
   - The directory where the paper's PDF lives (most common — `/read-paper` places summaries alongside PDFs)
   - `docs/literature/` and its subdirectories
   - The project root's `paper/` directory

3. **Report what's available** — show the user which `[UNSUMMARIZED]` entries have summary files ready, and which don't (those need `/read-paper` first). Let the user confirm which entries to deepen, or proceed with all that have summaries.

4. **For each entry with a summary file:**
   a. Read the `summary-*.md` file — focus on the story summary, narrative tree, and core assessment.
   b. Re-read the comparison target (Step 2 of the standard review) if not already in context.
   c. **Update the entry:**
      - Rewrite **Main contribution** and **Key finding** based on actual paper content, not abstract-level guesses.
      - Rewrite **Relevance to our paper** with specific, grounded comparisons — now that you've read the actual arguments, you can say precisely how they relate.
      - Add a **Summary** field with a link to the summary file: `**Summary:** [Full summary](relative/path/to/summary-year-author.md)`
   d. **Remove `[UNSUMMARIZED]`** from the entry heading.

5. **Update thematic sections** — with deeper understanding of several papers, the thematic groupings and synthesis paragraphs may need revision. Re-read the themes and update if the deep readings reveal connections or tensions the shallow pass missed.

6. **Update gaps and next steps** — deep readings often reveal new gaps or close ones that seemed open from the abstract.

### Entry format after deepening

```markdown
### [Author (Year)](URL) — Short Title `[UNVERIFIED]`

- **Summary:** [Full summary](relative/path/to/summary-year-author.md)
- **Publication:** *Journal Name*, vol. X(Y), pp. Z
- **Main contribution:** [Updated with deep understanding]
- **Method:** [Updated if needed]
- **Key finding:** [Updated — specific, grounded in actual reading]
- **Relevance to our paper:** [Updated — names specific results, precise comparison]
```

Note: `[UNSUMMARIZED]` is gone, replaced by the clickable Summary link. `[UNVERIFIED]` stays until citation details are independently confirmed.

---

## Output Location

All literature reviews go in `docs/literature/`:

| Type | Filename | When |
|------|----------|------|
| Overall literature review | `summary-literature.md` | Comprehensive survey of all related work for the paper |
| Topic-specific review | `summary-literature-[short-description].md` | Focused review on a specific question, result, or sub-topic |

Examples of topic-specific naming:
- `summary-literature-search-technology-collusion.md`
- `summary-literature-optimal-punishments.md`
- `summary-literature-empirical-price-dispersion.md`

If `docs/literature/` doesn't exist, create it.

If the project has `paper/references.bib`, offer to append new BibTeX entries there. Note: `references.bib` is a protected file — the user must confirm before editing.

---

## Important

- **All papers get `[UNSUMMARIZED]` and `[UNVERIFIED]` tags by default.** `[UNSUMMARIZED]` is removed only by the `deepen` workflow after reading the summary file and enriching the entry. `[UNVERIFIED]` is removed after citation verification. Neither tag is removed by judgment alone.
- **Do NOT fabricate citations.** If you are unsure about a paper's details (authors, year, journal, title), flag it for the user to verify. Getting a citation wrong is worse than omitting it.
- **BibTeX fields from memory are unreliable.** Even when a paper is real, LLM-recalled volume, pages, and DOI are often wrong. Mark individual fields you cannot verify with `% UNVERIFIED` comments in the BibTeX entry.
- **Compare against our paper.** The "Relevance to our paper" field in each entry should be specific: name which of our results the paper relates to, whether it's a predecessor, competitor, complement, or something we extend.
- **Prioritize recent work** (last 5-10 years) unless seminal papers are older.
- **Note working papers vs published papers** — working papers may change before publication.
- **Handle web tool failures gracefully.** If WebSearch or WebFetch are unavailable or fail, analyze only local files and note what could not be searched.
- **Verify URLs.** Use WebSearch to find real, clickable URLs for each paper. Prefer stable links: journal publisher pages, EconPapers/IDEAS/RePEC, SSRN, NBER. Never guess URLs.
