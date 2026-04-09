# Flutter Architecture Guard

## Summary
A review skill for enforcing architecture boundaries in Flutter projects so code stays modular, testable, and predictable as it grows.

## Problem It Solves
Teams often lose architecture clarity over time: UI classes absorb domain logic, repositories become catch-all classes, and dependencies start flowing in the wrong direction. This skill provides a consistent way to detect and correct that drift.

## When to Use
- You are reviewing a Flutter codebase for clean architecture alignment.
- A feature has become hard to evolve because responsibilities are mixed.
- You need to verify layer boundaries (presentation, domain/application, data/infrastructure).
- You want to propose incremental architecture corrections without changing product behavior.

## When Not to Use
- You are implementing a new feature from scratch.
- The goal is purely visual/UI polish.
- You need a full architecture rewrite rather than a boundary-focused review.

## Inputs
- Existing Flutter/Dart source files.
- Current architecture style and project conventions.
- A target scope (module, feature, or pull request).

## Outputs
- A boundary review with concrete findings.
- A list of dependency-direction or ownership violations.
- Minimal, practical refactor recommendations.
- Clear risk notes when behavior could change.

## Step-by-Step Usage
1. Identify the current architecture style used by the project.
2. Map responsibilities across layers and feature modules.
3. Check dependency direction and cross-layer imports.
4. Locate side-effect ownership (navigation, analytics, storage, network).
5. Flag architecture smells with examples.
6. Propose the smallest high-value corrections.
7. Confirm recommendations preserve behavior unless change is explicitly requested.

## Examples
- A widget triggers API calls and maps DTOs directly. Recommendation: move integration and mapping into repository/application layer; keep widget focused on rendering and interaction.
- A notifier manages UI state, business policy, navigation, and analytics. Recommendation: split policy and integrations into dedicated collaborators; keep notifier UI-facing.
- A shared `utils` module contains unrelated feature rules. Recommendation: move logic back into feature-owned modules unless it is truly stable and cross-feature.

## Edge Cases / Caveats
- Some projects intentionally use lighter architecture; avoid dogmatic enforcement.
- A theoretical violation may be acceptable if local ownership and maintainability remain strong.
- Refactors should stay incremental to reduce regression risk.

## Related Skills
- [Flutter Design Pattern Review](./flutter-design-pattern-review.md)
- [Flutter Simplify](./flutter-simplify.md)

## Status
`ready`
