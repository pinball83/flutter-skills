---
name: pr-coverage-test-guard
description: Analyze PR coverage comments and changed files, identify touched source files with 0-70% coverage, and create or update focused tests for the affected code in the current repository.
---

# Purpose

Use this skill to turn low-coverage PR changes into targeted tests.

# Outcome

For each changed source file with low coverage, produce the smallest useful test change that covers the new or changed behavior.

# Workflow

1. Read the PR coverage comment and extract every changed file with coverage between 0% and 70%.
2. Cross-check that each file is part of the PR diff and ignore generated, config-only, and non-source files.
3. Read the changed code and infer the user-visible or business behavior that needs coverage.
4. Search for the nearest existing tests by basename, module, feature, symbol, or behavior.
5. Update the closest relevant test file when one exists.
6. Create a new test file only when there is no suitable existing place.
7. Keep the diff focused on meaningful behavior, not implementation details.
8. Run the smallest relevant test set first, then expand only if needed.

# Coverage Rules

- Prefer files with the lowest coverage first.
- Skip files already covered by stronger adjacent tests unless the PR introduced a new branch or regression risk.
- If the coverage comment and the diff disagree, trust the actual changed files and note the mismatch in the final summary.
- Do not invent coverage numbers or claim improvements you did not verify.

# Test Selection

Prefer tests that cover:
- public behavior
- branching logic
- error handling
- null, empty, and boundary states
- state transitions
- output changes that matter to users

Avoid:
- private implementation details
- broad refactors unrelated to the changed file
- unnecessary mocks
- behavior changes in production code unless testability requires it and the reason is clear

# Output

When finished, report:
1. the low-coverage changed files you found
2. whether each one was updated, added, or skipped
3. what behavior is now covered
4. the exact test files changed

# Final Check

Stop once you have the smallest valid change set that meaningfully improves coverage.
