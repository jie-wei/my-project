---
name: commit
description: Commit the requested changes. Push, open a pull request, or merge only when the user's request includes those actions.
disable-model-invocation: true
argument-hint: "[optional commit message or requested Git actions]"
allowed-tools: ["Bash", "Read", "Glob", "Write"]
---

# Commit Requested Changes

Match the Git operations to the user's request and any authorization already established in the conversation.

## Determine the Scope

| Request | Actions |
| --- | --- |
| `/commit`, with or without a commit message | Stage the requested changes and create a local commit, then stop. |
| Commit and push | Commit, then push the intended branch. |
| Open a pull request | Prepare any necessary commit, push the branch, and open the PR; leave it unmerged. |
| Merge an identified PR | Check and merge that PR; do not create another branch, commit, or PR unless needed and requested. |
| Commit, open a PR, and merge | Complete that sequence within the requested scope. |

A commit message is content, not an instruction to perform additional Git actions. Honor explicit requests to use an existing commit or branch.

Do not request confirmation again for actions already authorized. Ask only when the intended changes, repository, branch, or PR cannot be determined safely from context.

## Prepare and Commit

1. **Inspect the working tree and index.**

   ```bash
   git status --short
   git diff --stat
   git diff --cached
   git log --oneline -5
   ```

   Identify the changes belonging to the request. Preserve unrelated work, including pre-existing staged changes; do not include it in the commit without authorization. Use selective staging for files containing both requested and unrelated edits, and an isolated index when needed to preserve unrelated staging.

2. **Choose the branch.** Reuse the appropriate existing feature branch. If committing from the repository's default branch, create a descriptive feature branch unless the user requested otherwise. Determine the actual default branch rather than assuming it is named `main`.

3. **Stage the intended paths or hunks.** Use specific paths, never a blanket `git add -A`. Exclude local settings and secrets. Inspect the staged diff to confirm the commit contains only the intended changes, and check the relevant verification results.

4. **Commit.** Use a supplied commit message exactly. Otherwise, write a concise message explaining the change and its purpose. Write multiline text to a temporary file and use `git commit -F <message-file>`; keep user text out of shell interpolation.

For a commit-only request, report the commit hash, branch, and what changed. The workflow ends here.

## Push or Open a PR When Requested

Push the intended branch to its appropriate remote when the request includes pushing or opening a PR. Do not force-push unless explicitly requested.

Reuse an existing PR for the branch when appropriate. For a new PR, describe the concrete problem, resulting behavior, and relevant validation. Write the body to a temporary file and pass it with `gh pr create --body-file <body-file>`. Attribute the work accurately; do not add a hard-coded client signature.

Report the PR URL when a PR is requested. Opening a PR does not imply merging it.

## Merge When Requested

Confirm the intended PR and target branch, review the diff and required check status, then merge using the repository's permitted method. Prefer a merge commit when no other method is requested or required. Do not bypass required checks.

Report the merged PR and result. Delete branches or switch the local checkout only when that cleanup is requested or already authorized.
