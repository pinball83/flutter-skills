---
name: jira-branch-starter
description: Start work from a Jira issue or subtask by loading parent and subtask context, then create a feature or fix git branch named with the Jira key prefix.
compatibility: Requires git, Python 3, and Atlassian Rovo access in Codex.
---

# Jira Branch Starter

Use this skill when the user wants to begin work from a Jira ticket and needs:

- the ticket opened and summarized
- parent and subtask context loaded
- a feature or fix branch created locally
- the branch name to include the Jira task key prefix

## Outcome

Produce a branch name that is tied to the active Jira work item, for example:

- `feature/ABC-123-add-login`
- `fix/ABC-123-null-guard`

Use the leaf work item key that is actually being implemented. If the work item is a subtask, use the subtask key in the branch name and load the parent for context.

## Workflow

1. Resolve the Jira issue key from the user's request.
2. Fetch the issue with `mcp__codex_apps__atlassian_rovo._getjiraissue`.
3. If the issue has a parent, fetch the parent too.
4. If the issue has subtasks, fetch the relevant subtask or subtasks.
5. Read summary, description, issue type, status, labels, components, parent, and subtask text before deciding the branch name.
6. Classify the branch as:
   - `fix` for Bug, Defect, Incident, Hotfix, or regression work
   - `feature` for Story, Task, Improvement, or new behavior
   - the user's explicit instruction wins if it conflicts with issue type
7. Build the branch name with `scripts/branch_name.py` so slug generation stays deterministic.
8. Create the branch from the current HEAD unless the user names a different base branch.
9. Report the Jira key, the context used from the parent/subtask chain, and the final branch name.

## Context Rules

- If the ticket is a parent issue with subtasks, load the subtask context before naming the branch when the subtask is the actual work item.
- If the user only gives a parent ticket, do not invent a subtask; use the parent key and the parent summary.
- If the user asks for a feature branch but the ticket is clearly a bug fix, follow the user unless they explicitly want type inference.
- If the issue key cannot be resolved, ask for the Jira key once instead of guessing.

## Branch Rules

- Prefer `feature/` or `fix/` as the branch prefix.
- Always include the Jira issue key right after the prefix.
- Keep the branch based on the active repository's branch workflow.
- If the branch already exists locally, reuse it rather than inventing a duplicate.

## Commands To Use

- `mcp__codex_apps__atlassian_rovo._getaccessibleatlassianresources` to resolve the Jira cloud/site if needed.
- `mcp__codex_apps__atlassian_rovo._getjiraissue` to load issue data.
- `bash skill.sh --kind <feature|fix> --issue-key <ISSUE-KEY> --summary <summary>` to derive the branch name.
- `bash skill.sh --kind <feature|fix> --issue-key <ISSUE-KEY> --summary <summary> --create` to create it with git.
