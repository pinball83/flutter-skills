---
name: flutter-simplify
description: Safely simplify Flutter and Dart code without changing behavior. Use for refactoring widgets, reducing duplication, improving readability, and cleaning up state management while preserving existing logic and APIs.
---

# Purpose

Use this skill when the user asks to simplify, clean up, refactor, or make Flutter/Dart code more maintainable without changing behavior.

This skill is for safe refactoring work:
- reducing duplication
- improving readability
- splitting large widgets or methods
- clarifying naming
- simplifying state handling
- removing obvious dead code when confidence is high
- improving file structure inside the existing architecture

This skill is **not** for feature work, product redesign, or architecture rewrites unless explicitly requested.

# When to use

Use this skill when the request sounds like:
- "simplify this widget"
- "clean up this code"
- "refactor without changing behavior"
- "reduce duplication"
- "make this screen easier to maintain"
- "split this large file"
- "improve readability"
- "remove code smells"

# Do not

- Do not change business logic intentionally.
- Do not change visible behavior unless necessary to fix an obvious bug explicitly requested by the user.
- Do not introduce new dependencies unless explicitly requested.
- Do not rewrite the app architecture unless explicitly requested.
- Do not rename public APIs, routes, DTOs, or externally used symbols unless necessary and safe.
- Do not replace an established state-management approach with another one just because it is preferred.
- Do not over-abstract.
- Do not convert simple code into “clever” code.

# Refactoring principles

Prefer the smallest safe refactor that meaningfully improves the code.

Optimize for:
1. readability
2. maintainability
3. local reasoning
4. testability
5. consistency with the existing codebase

Prefer:
- extracting small private widgets when a build method becomes hard to scan
- extracting small private methods when logic is repeated
- flattening deeply nested conditionals when possible
- replacing magic values with clearly named constants
- improving variable and method names when the new names are clearly better
- grouping related logic together
- reducing widget tree noise where practical
- preserving framework idioms already used in the project

Avoid:
- speculative abstractions
- unnecessary base classes
- generic helper utilities used only once
- large “cleanup” diffs touching unrelated code
- mixing formatting-only changes with structural refactors unless useful

# Flutter-specific guidance

## Widgets
- Prefer extracting private widgets when a widget subtree has a clear responsibility.
- Keep extracted widgets close to their usage unless they are reused.
- Prefer `const` constructors and `const` widget usage when safe and supported.
- Avoid extracting tiny widgets that make navigation harder unless they remove real complexity.

## Build methods
- Keep `build()` readable.
- Move non-trivial mapping, branching, and formatting logic out of `build()` if it reduces noise.
- Avoid hidden side effects in `build()`.

## State management
- Respect the current pattern in the codebase: setState, Provider, Riverpod, Bloc, Cubit, etc.
- Simplify state transitions and derived values, but do not migrate state-management libraries unless explicitly requested.
- Prefer making derived UI state explicit rather than recalculating scattered conditions across the file.

## Async code
- Preserve existing async behavior.
- Make loading, success, and error flows easier to follow.
- Avoid introducing race conditions.
- Keep cancellation and mounted checks intact where relevant.

## Models and mapping
- Reduce repetitive mapping code only when the result stays explicit.
- Do not hide important domain transformations in vague helpers.

## Navigation and side effects
- Preserve existing navigation behavior.
- Keep side effects visible and easy to trace.

# Process

Follow this process:

1. Read the target file or files fully.
2. Identify the main complexity hotspots.
3. Make a short internal plan with the smallest high-value refactors.
4. Apply changes incrementally.
5. Keep the diff focused on the requested cleanup.
6. Run relevant checks if available:
   - formatter
   - analyzer
   - tests related to touched code
7. Summarize:
   - what was simplified
   - what was intentionally left unchanged
   - any risks or follow-ups

# Decision rules

When choosing between two valid refactors:
- prefer the smaller diff
- prefer the option that matches the existing project style
- prefer explicitness over abstraction
- prefer private/local extraction over shared/global utilities
- prefer preserving APIs over renaming

If confidence is low:
- make fewer changes
- note uncertainty explicitly
- avoid risky renames or behavior-affecting edits

# Output expectations

When making changes:
- first explain the main simplification strategy briefly
- then apply the code changes
- then give a concise summary of:
  - simplified areas
  - behavior preserved
  - risks or follow-up opportunities

If asked for review only:
- do not edit code
- list the top simplification opportunities in priority order
- mention which ones are safe vs risky

# Examples

## Example: large widget
If a screen has a 250-line `build()` with repeated sections:
- extract clearly named private widgets or helper builders
- keep screen-level state and orchestration in the parent
- avoid moving everything into generic helpers

## Example: repeated conditions
If the same conditional expression appears several times:
- extract a well-named local boolean or derived getter
- keep the meaning obvious at call sites

## Example: duplicated UI blocks
If two UI blocks are almost identical:
- extract a private reusable widget only if it improves clarity
- parameterize only the truly varying parts

# Success criteria

A successful refactor should:
- preserve behavior
- reduce cognitive load
- make future edits easier
- keep the code idiomatic for Flutter/Dart
- avoid unnecessary architectural churn
