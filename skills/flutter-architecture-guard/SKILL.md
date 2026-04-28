---
name: flutter-architecture-guard
description: Review and enforce Flutter architecture boundaries in existing codebases. Use when evaluating or refactoring Flutter/Dart code for layer separation, dependency direction, feature modularity, state-management boundaries, navigation ownership, clean architecture alignment, and prevention of architecture drift without changing product behavior.
---

# Purpose

Use this skill to protect and reinforce the existing Flutter architecture.

This skill is for:
- architecture reviews
- boundary checks between layers
- clean architecture alignment checks
- preventing architecture drift
- identifying coupling and responsibility leaks
- guiding safe refactors toward cleaner module and feature ownership
- checking whether new code fits the current architectural rules

This skill is not for:
- adding features
- redesigning the product
- rewriting the entire app architecture unless explicitly requested
- refactoring for style only without architectural relevance

# When to use

Use this skill when the request sounds like:
- "review this Flutter architecture"
- "check if this code violates clean architecture"
- "protect boundaries between layers"
- "is this widget doing too much?"
- "should this dependency live here?"
- "does this feature belong in presentation or domain?"
- "prevent architecture drift"
- "review module boundaries"
- "keep Riverpod/Bloc/navigation clean"
- "check whether this follows clean architecture"

# Primary goal

Keep the codebase easy to evolve by preserving clear responsibility boundaries.

Optimize for:
1. correct dependency direction
2. low coupling
3. high cohesion
4. feature ownership clarity
5. explicit side effects
6. testability
7. consistency with the current codebase

# Core architectural rules

Apply these rules unless the project explicitly uses different conventions.

## 1. Dependency direction
- Outer layers may depend on inner layers.
- Inner layers must not depend on outer layers.
- Domain logic must not depend on Flutter UI, widgets, BuildContext, or platform-specific presentation code.
- Data/infrastructure details must not leak into presentation as ad hoc logic.

## 2. Presentation layer responsibilities
Presentation may:
- render UI
- transform state into view models or UI models
- handle user interaction
- coordinate with state-management objects
- trigger navigation through the project’s chosen pattern

Presentation must not:
- contain business rules that belong in domain
- perform heavy mapping from raw transport models when this belongs elsewhere
- call low-level APIs directly
- mix unrelated feature responsibilities into a single screen/controller/viewmodel

## 3. Domain layer responsibilities
Domain should:
- contain business rules
- define use cases, policies, and core entities/value objects when the project has them
- stay independent from Flutter and UI concerns
- express intent clearly

Domain should not:
- import presentation concerns
- know about route names, widgets, BuildContext, or view formatting
- depend on DTOs or transport-layer details unless the project intentionally collapsed layers

## 4. Data layer responsibilities
Data/infrastructure may:
- call APIs, databases, caches, SDKs, platform services
- map external models to internal models
- implement repository contracts if the project uses repository abstraction

Data/infrastructure should not:
- decide UI behavior
- format content for widgets
- own business policy that should be reusable and testable in domain

## 5. Feature modularity
Prefer code grouped by feature first, then by layer within the feature, if that matches the project.
Watch for:
- shared folders becoming dumping grounds
- unrelated features importing each other casually
- one "utils" or "common" area slowly becoming the real architecture
- feature logic spread across many unrelated folders with weak ownership

## 6. State management boundaries
Respect the existing state-management solution: Riverpod, Bloc, Cubit, Provider, setState, etc.

State-management objects should:
- expose UI-facing state clearly
- delegate business logic to domain/application services where appropriate
- avoid turning into god objects
- avoid holding unrelated responsibilities

Watch for:
- ViewModels/Notifiers/Blocs performing API mapping, persistence, analytics, navigation, and business policy all together
- duplicated derivation logic across many widgets
- state transitions hidden across multiple files with unclear ownership

## 7. Navigation and side effects
Navigation ownership should be consistent.
Side effects should be visible and traceable.

Watch for:
- navigation decisions scattered across widgets, repositories, and services
- analytics, storage, API calls, and routing mixed into a single callback
- BuildContext passed deep into non-UI layers without strong reason

## 8. Shared code rules
Shared code is allowed only when it is truly shared and stable.
Do not move code to shared/common/core too early.

A piece of code is a good shared candidate only if it is:
- used in multiple places
- conceptually identical across those places
- unlikely to diverge soon

# Clean Architecture checks

When reviewing code, explicitly evaluate whether the code follows Clean Architecture principles appropriate for the current project.

## Dependency rule
- Dependencies should point inward.
- Presentation may depend on domain/application interfaces or use cases.
- Domain must not depend on Flutter, UI frameworks, navigation, DTOs, or infrastructure details.
- Data/infrastructure may depend on domain contracts if the project uses repository abstraction.

## Layer checks
Evaluate whether responsibilities are placed in the correct layer.

### Presentation
- widgets/screens render UI and coordinate interaction
- presentation state holders expose UI-facing state
- presentation should not own core business rules

### Domain / application
- contains business policies, use cases, and core decisions
- should stay framework-independent
- should not know about BuildContext, routes, widgets, or API DTOs

### Data / infrastructure
- integrates APIs, storage, SDKs, caches, and platform services
- performs transport-to-domain mapping where relevant
- should not decide UI behavior or screen flow

## Smells against Clean Architecture
Flag these as likely violations:
- business logic inside widgets
- domain code importing Flutter
- repositories returning UI-shaped models only for convenience
- DTOs leaking across the app
- navigation driven from deep infrastructure/services
- one notifier/bloc/viewmodel mixing business rules, API orchestration, persistence, analytics, and routing
- use cases that add no boundary value and only forward one repository call without improving intent or testability

## Pragmatic rule
Do not apply Clean Architecture dogmatically.
If the project intentionally uses a lighter structure, evaluate whether the code is still:
- understandable
- testable
- consistent
- easy to extend
- clear in ownership

A theoretical violation is less important than a structure that is stable, explicit, and maintainable in the current codebase.

# Review process

Follow this process:

1. Identify the project’s actual architecture before judging it.
   - Determine whether it is feature-first, layer-first, hybrid, MVVM, Clean Architecture, Redux-style, etc.
   - Do not force an architecture the codebase is not trying to use.

2. Map the responsibilities.
   - What belongs to presentation?
   - What belongs to domain/application?
   - What belongs to data/infrastructure?
   - What is currently mixed?

3. Check dependency direction.
   - Look for imports or flows that violate intended boundaries.
   - Look for domain knowledge embedded in UI-only code.
   - Look for infrastructure assumptions leaking upward.

4. Check feature ownership.
   - Confirm that each feature has a clear home for UI, state, business logic, and integration logic.
   - Flag code that is hard to place because responsibilities are mixed.

5. Check side-effect placement.
   - Verify where navigation, analytics, persistence, networking, and caching are triggered.
   - Flag hidden or scattered side effects.

6. Evaluate clean architecture alignment.
   - Check whether business logic is separated from UI.
   - Check whether use cases/services have meaningful intent.
   - Check whether repositories represent proper boundaries instead of dumping grounds.
   - Check whether state-management objects became the real application layer by accident.

7. Recommend the smallest architectural correction that improves the code.
   - Prefer incremental moves over sweeping rewrites.
   - Preserve behavior.
   - Keep the current stack unless migration is explicitly requested.

# Decision rules

When deciding whether something is an architecture problem, ask:

- Is this responsibility in the wrong layer?
- Does this dependency point the wrong way?
- Is this code difficult to test because concerns are mixed?
- Would another developer struggle to know where similar future code should go?
- Is this "shared" abstraction actually hiding feature ownership?
- Is this state holder becoming a catch-all class?
- Is this repository/service doing policy work that belongs elsewhere?

If yes, flag it.

If a violation is mild but intentional and consistent across the project:
- note it as a tradeoff, not necessarily a defect

If a theoretically cleaner solution would require large churn:
- prefer a smaller local correction

If the code is not purely clean architecture but is still consistent and maintainable:
- prefer pragmatic guidance over dogmatic criticism

# Refactor guidance

When asked to fix architecture issues:
- preserve product behavior
- make the smallest change that restores boundary clarity
- avoid mass file moves unless clearly justified
- prefer extracting a use case/service/helper over rewriting many screens
- prefer moving code to the nearest correct layer instead of inventing a new abstraction
- do not introduce new packages unless explicitly requested

# Flutter-specific heuristics

## Widgets
Flag widgets that:
- own too much business logic
- coordinate too many unrelated concerns
- perform heavy data shaping that belongs elsewhere
- mix layout, state orchestration, navigation, analytics, and remote calls together

## Riverpod / Provider / Bloc / Cubit / Notifiers
Flag state holders that:
- become catch-all classes
- know too much about transport models
- directly manage too many side effects
- become the only real place where the feature logic exists with no separation of policy

## Repositories and services
Flag repositories/services that:
- return UI-shaped data for convenience
- embed navigation or presentation decisions
- mix remote, cache, and policy decisions without clear boundaries

## Routing
Flag routing if:
- route selection is mixed with domain decisions everywhere
- screen widgets own cross-feature navigation logic that should be centralized or coordinated consistently

# Output expectations

## If the user asks for review only
Return:
1. Architecture summary
2. Top boundary violations or drift risks
3. Clean architecture alignment issues
4. Why each issue matters
5. Safe fixes in priority order
6. What not to change yet

## If the user asks for changes
Return:
1. Short architecture assessment
2. Minimal refactor plan
3. Code changes
4. Summary of restored boundaries
5. Remaining tradeoffs or known limitations

# Severity model

Use these severity levels:

- Critical:
  Strong boundary violation that will spread coupling or break maintainability quickly.
- Medium:
  Responsibility placement is wrong or unclear and will make future changes harder.
- Low:
  Imperfect but acceptable; note as cleanup opportunity.

# Anti-pattern checklist

Watch for these anti-patterns:
- god ViewModel / god Bloc / god Notifier
- repository as business-logic dumping ground
- UI deciding domain policy inline
- DTOs leaking through the whole app
- BuildContext passed into deep services
- "shared" package becoming a junk drawer
- feature modules importing each other without clear ownership
- routing, analytics, and API calls tangled in button handlers
- use cases that are just pass-through wrappers with no architectural value
- abstractions created too early

# Success criteria

This skill succeeds when:
- architectural boundaries are clearer after review or refactor
- dependency direction becomes easier to reason about
- future code placement becomes more obvious
- behavior remains unchanged unless the user requested otherwise
- clean architecture alignment improves where relevant
- the codebase becomes easier to scale without a rewrite