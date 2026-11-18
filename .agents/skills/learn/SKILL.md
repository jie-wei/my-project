---
name: learn
description: |
  Extract reusable knowledge from the current session into a persistent skill.
  Use when you discover something non-obvious, create a workaround, or develop
  a multi-step workflow that future sessions would benefit from.
disable-model-invocation: true
argument-hint: "[skill-name (kebab-case)]"
allowed-tools: ["Read", "Grep", "Glob", "Write"]
---

# /learn -- Skill Extraction Workflow

Extract non-obvious discoveries into reusable skills that persist across sessions.

## When to Use This Skill

Invoke `/learn` when you encounter:

- **Non-obvious debugging** -- Investigation that took significant effort, not in docs
- **Misleading errors** -- Error message was wrong, found the real cause
- **Workarounds** -- Found a limitation with a creative solution
- **Tool integration** -- Undocumented API usage or configuration
- **Trial-and-error** -- Multiple attempts before success
- **Repeatable workflows** -- Multi-step task you'd do again
- **User-facing automation** -- Reports, checks, or processes users will request

## Workflow Phases

### PHASE 1: Evaluate (Self-Assessment)

Before creating a skill, answer these questions:

1. "What did I just learn that wasn't obvious before starting?"
2. "Would future-me benefit from this being documented?"
3. "Was the solution non-obvious from documentation alone?"
4. "Is this a multi-step workflow I'd repeat?"

**Continue only if YES to at least one question.**

### PHASE 2: Check Existing Skills

Search for related skills to avoid duplication:

```bash
# Check project skills
ls .agents/skills/ 2>/dev/null

# Search for keywords
rg -n -i "KEYWORD" .agents/skills/
```

**Outcomes:**
- Nothing related -- Create new skill (continue to Phase 3)
- Same trigger & fix -- Update existing skill
- Partial overlap -- Update existing skill with new variant

### PHASE 3: Create Skill

Create the skill file at `.agents/skills/[skill-name]/SKILL.md`:

````markdown
---
name: descriptive-kebab-case-name
description: |
  [CRITICAL: Include specific triggers in the description]
  - What the skill does
  - Specific trigger conditions (exact error messages, symptoms)
  - When to use it (contexts, scenarios)
disable-model-invocation: true
argument-hint: "[expected arguments]"
allowed-tools: ["Read", "Grep", "Glob", "Write"]
---

# Skill Name

## Problem
[Clear problem description -- what situation triggers this skill]

## Context / Trigger Conditions
[When to use -- exact error messages, symptoms, scenarios]
[Be specific enough that you'd recognize it again]

## Solution
[Step-by-step solution]
[Include commands, code snippets, or workflows]

## Verification
[How to verify it worked]
[Expected output or state]

## Example
[Concrete example of the skill in action]

## References
[Documentation links, related files, or prior discussions]
````

For the explicit-only scaffold above, also create `.agents/skills/[skill-name]/agents/openai.yaml`:

```yaml
policy:
  allow_implicit_invocation: false
```

These two settings express the same choice: Claude uses `disable-model-invocation: true`, while Codex uses `policy.allow_implicit_invocation: false`. Both clients still discover the shared skill for explicit invocation.

When updating an existing skill, preserve its invocation mode and unrelated metadata. If the user requests automatic selection, set Claude's `disable-model-invocation` to `false` and Codex's `allow_implicit_invocation` to `true`. Keep the pair consistent; do not regenerate an existing metadata file in a way that discards its other fields.

### PHASE 4: Quality Gates

Before finalizing, verify:

- [ ] Description has specific trigger conditions (not vague)
- [ ] Solution was verified to work (tested)
- [ ] Content is specific enough to be actionable
- [ ] Content is general enough to be reusable
- [ ] No sensitive information (credentials, personal data)
- [ ] Skill name is descriptive and uses kebab-case
- [ ] Claude's frontmatter and Codex's `agents/openai.yaml` express the same invocation mode; existing unrelated metadata is preserved

## Output

After creating the skill, report:

```
Skill created: .agents/skills/[name]/
  Invocation: [explicit-only or automatic, consistent across both clients]
  Trigger: [when to use]
  Problem: [what it solves]
```

## Example: Creating a Skill

User discovers that pandas silently coerces types when merging:

````markdown
---
name: pandas-merge-type-coercion
description: |
  Handle silent type coercion in pandas merge operations.
  Use when: merged DataFrame has unexpected types, integer columns
  become float after merge, or comparison operations fail post-merge.
disable-model-invocation: true
allowed-tools: ["Read", "Grep", "Glob", "Write"]
---

# pandas Merge Type Coercion

## Problem
pandas silently converts integer columns to float when merging DataFrames
that have missing values in the join key, which can cause downstream
comparison failures and unexpected behavior.

## Context / Trigger Conditions
- Integer column becomes float64 after merge
- Comparison operations fail (e.g., df['id'] == 42 returns unexpected results)
- Merged DataFrame has NaN in integer columns
- Results differ between inner and left/outer merge

## Solution
1. Check dtypes before and after merge:
   ```python
   print(df1.dtypes)
   print(df2.dtypes)
   merged = df1.merge(df2, on='key', how='left')
   print(merged.dtypes)  # Check for int -> float conversion
   ```
2. Use nullable integer types to preserve int through NaN:
   ```python
   df['id'] = df['id'].astype('Int64')  # Capital I = nullable
   ```
3. Or explicitly cast back after merge:
   ```python
   merged['id'] = merged['id'].fillna(-1).astype(int)
   ```

## Verification
Compare `merged.dtypes` with expected types. Integer columns should
remain integer (or Int64) after merge.

## References
- pandas documentation on nullable integer types
- [LEARN:python] entry in MEMORY.md if applicable
````

---

## Important

- **Trigger conditions are critical.** Vague descriptions like "handle data issues" won't match future situations. Be specific: exact error messages, symptoms, scenarios.
- **Test before saving.** Only document solutions that actually work.
- **Choose the right destination.** Reusable workflows go in `.agents/skills/`; project-specific corrections go in `MEMORY.md`. Machine-specific or private local notes go in `.claude/state/personal-memory.md`. `AGENTS.md` tells both clients to read these memory files at session start. Do not create a skill for a correction that only needs a short memory entry.
- **Update MEMORY.md** with a `[LEARN:skills]` entry noting the new skill was created.
