# Flutter Simplify

## Summary
A safe refactoring skill for reducing complexity in Flutter/Dart code while preserving behavior, APIs, and existing project conventions.

## Problem It Solves
Large widgets, duplicated logic, and unclear state flows increase maintenance cost and bug risk. This skill streamlines code with focused, low-risk refactors.

## When to Use
- You need behavior-preserving cleanup.
- A widget tree or method is too large to read efficiently.
- Repeated conditions or UI blocks should be consolidated.
- State transitions are correct but hard to follow.

## When Not to Use
- You are changing product behavior or business rules.
- You plan to migrate state-management libraries.
- The task requires broad architecture redesign.

## Inputs
- Target Flutter/Dart files.
- Current behavior expectations and API constraints.
- Relevant tests or acceptance scenarios.

## Outputs
- Smaller, clearer code with preserved behavior.
- Reduced duplication and improved local readability.
- Safer state and async flow clarity.
- A concise summary of what changed and what stayed intentionally unchanged.

## Step-by-Step Usage
1. Read the full target scope before editing.
2. Mark the highest-impact complexity hotspots.
3. Choose the smallest set of safe refactors.
4. Apply changes incrementally (extractions, naming, duplication removal).
5. Preserve existing state-management and navigation behavior.
6. Run formatter, analyzer, and relevant tests where available.
7. Report simplifications, preserved behavior, and residual risks.

## Examples
- A 250-line `build()` method is split into focused private widgets with clear names and unchanged behavior.
- Repeated conditional expressions are replaced with explicit derived booleans.
- Similar UI blocks are merged into a private reusable widget with only meaningful parameters.

## Edge Cases / Caveats
- Over-extraction can reduce readability; keep abstractions local and purposeful.
- Async refactors must preserve cancellation and mounted checks.
- Dead code removal should happen only when confidence is high.

## Related Skills
- [Flutter Architecture Guard](./flutter-architecture-guard.md)
- [Flutter Design Pattern Review](./flutter-design-pattern-review.md)

## Status
`ready`
