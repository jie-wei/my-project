# Quality Report: Merge to Main -- 2026-04-16

## Summary
Added theory mode to write-summary and review-summary skills. Both now auto-detect empirics vs theory and load the appropriate workflow, templates, and review criteria.

## Files Modified
| File | Type | Quality Score |
|------|------|---|
| `.claude/skills/write-summary/SKILL.md` | Skill config | N/A |
| `.claude/skills/write-summary/references/workflow-empirics.md` | Reference (new) | N/A |
| `.claude/skills/write-summary/references/workflow-theory.md` | Reference (new) | N/A |
| `.claude/skills/write-summary/references/template-latex-empirics.tex` | Template (renamed) | N/A |
| `.claude/skills/write-summary/references/template-latex-theory.tex` | Template (new) | N/A |
| `.claude/skills/review-summary/SKILL.md` | Skill config | N/A |
| `.claude/skills/review-summary/references/workflow-empirics.md` | Reference (new) | N/A |
| `.claude/skills/review-summary/references/workflow-theory.md` | Reference (new) | N/A |
| `.claude/skills/review-code/SKILL.md` | Skill config | N/A |
| `.claude/skills/write-code/SKILL.md` | Skill config | N/A |
| `.claude/skills/write-code/references/*` | References | N/A |
| `.claude/skills/review-literature-comparison/*` | Skill config + template | N/A |
| `.claude/skills/review-literature-synoptic/*` | Skill config + template | N/A |
| `.claude/rules/protocol-orchestrator.md` | Rule | N/A |
| `.claude/rules/standalone-conventions.md` | Rule | N/A |

## Verification
- [x] All new reference files exist at expected paths
- [x] Old files properly removed/renamed
- [x] Quality gates >= 80 (N/A — no scored file types)

## Status
MERGED
