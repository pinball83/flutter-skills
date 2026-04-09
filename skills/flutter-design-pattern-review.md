# Flutter Design Pattern Review

## Summary
A pragmatic review skill for identifying useful design patterns, detecting anti-patterns, and improving structure without unnecessary abstraction.

## Problem It Solves
Flutter codebases can become either under-structured (duplication, unclear ownership) or over-structured (layers of indirection with little value). This skill helps apply patterns only where they create measurable improvement.

## When to Use
- You want to understand which patterns are already present.
- You need targeted recommendations for recurring structural problems.
- You suspect anti-patterns (god objects, dumping-ground repositories, scattered side effects).
- You want pattern guidance aligned with practical clean architecture.

## When Not to Use
- You only need minor formatting or naming cleanup.
- The request is feature delivery rather than code review.
- A one-off issue can be solved with a simple local helper.

## Inputs
- Flutter/Dart code under review.
- Problem statements (maintainability, duplication, testability, complexity).
- Team conventions and current architecture style.

## Outputs
- Identified existing patterns with practical explanations.
- Anti-pattern findings with severity and impact.
- Minimal pattern recommendations with rationale.
- A “do not abstract” list for low-value changes.

## Step-by-Step Usage
1. Determine the project’s architecture style and boundaries.
2. Identify repeated logic, branching, and ownership hotspots.
3. Detect current patterns already solving real problems.
4. Flag anti-patterns that increase coupling or cognitive load.
5. Recommend only pattern changes with clear return on complexity.
6. Distinguish high-value changes from overengineering risks.
7. Provide a staged refactor path when implementation is requested.

## Examples
- Repeated conditional pricing logic across screens. Recommendation: use a strategy/policy object to centralize variant behavior.
- Repository class mixes network calls, UI formatting, and navigation decisions. Recommendation: restore repository to data-boundary role; move UI policy out.
- Multiple pass-through use cases add no intent. Recommendation: remove low-value indirection and keep flow explicit.

## Edge Cases / Caveats
- Pattern names matter less than responsibility clarity and maintainability.
- Not every duplication requires a formal pattern.
- Pattern adoption should match team familiarity and project scale.

## Related Skills
- [Flutter Architecture Guard](./flutter-architecture-guard.md)
- [Flutter Simplify](./flutter-simplify.md)

## Status
`ready`
