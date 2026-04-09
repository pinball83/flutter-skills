---
name: flutter-design-pattern-review
description: Review Flutter and Dart code for design patterns, anti-patterns, and opportunities to improve structure using appropriate patterns without overengineering. Use for identifying existing patterns, missing patterns, responsibility issues, and pragmatic clean architecture alignment.
---

# Purpose

Use this skill to analyze Flutter/Dart code for:
- existing design patterns
- missing patterns that could simplify the code
- anti-patterns
- overengineering disguised as architecture
- pragmatic alignment with Clean Architecture

This skill is for review, diagnosis, and targeted architectural guidance.
It should not force patterns where simpler code is better.

# When to use

Use this skill when the request sounds like:
- "find design patterns in this code"
- "what patterns are used here?"
- "where should we apply a pattern?"
- "is there an anti-pattern here?"
- "can this be organized better with patterns?"
- "does this align with clean architecture?"
- "is this overengineered?"

# Philosophy

Patterns are tools, not goals.

Prefer:
- clarity
- maintainability
- explicit ownership
- minimal sufficient abstraction

Do not recommend a pattern unless it improves:
- separation of concerns
- testability
- extensibility
- readability
- reuse with stable semantics

Do not introduce patterns only because they are academically correct.

# What to detect

## Existing patterns
Identify whether the code already uses patterns such as:
- Strategy
- Factory / Factory Method
- Adapter
- Facade
- Repository
- Use Case / Interactor
- Observer / reactive state flow
- State pattern
- Command-like actions
- Mapper / Translator
- Dependency Injection
- Coordinator / Navigator abstraction
- Decorator
- Builder
- Specification-like filtering logic

Describe them in practical terms, not just labels.

## Missing patterns
Suggest a pattern only when it would solve a real problem, such as:
- repeated branching logic with multiple variants -> Strategy
- repeated object creation logic -> Factory
- external SDK/API mismatch -> Adapter
- too many subsystem calls exposed to UI -> Facade
- repeated transformation between models -> Mapper
- complex action orchestration reused across screens -> Use Case / Application Service
- scattered navigation decisions -> Coordinator-like abstraction
- interchangeable validation or pricing logic -> Strategy / Policy object

## Anti-patterns
Watch for:
- god widget / god viewmodel / god notifier / god bloc
- repository as dumping ground
- service classes with no clear role
- deep inheritance for simple composition problems
- DTO leakage across layers
- massive utils/common helpers with weak ownership
- pass-through use cases with no value
- patterns added only for indirection
- boolean-flag-driven behavior explosion
- switch/case trees duplicated across files
- BuildContext leaking too deep
- hidden side effects

# Clean Architecture alignment

When relevant, also evaluate:
- whether business rules are separated from UI
- whether dependencies point in the right direction
- whether use cases actually carry intent
- whether repositories represent data access boundaries rather than business policy dumping grounds
- whether shared abstractions clarify or obscure ownership

# Review process

1. Identify the current architecture style.
2. Map responsibilities and repeated structures.
3. Detect existing patterns already present.
4. Detect anti-patterns or unstable abstractions.
5. Suggest only the smallest useful pattern improvements.
6. Explain why a pattern helps here and why alternatives are worse or unnecessary.

# Decision rules

Recommend a pattern only if most of these are true:
- the same structural problem appears repeatedly
- the solution would remove duplication or branching
- ownership becomes clearer
- future changes become easier
- the resulting code is easier to explain to another developer
- the abstraction is likely to remain stable

Do not recommend a pattern if:
- it only adds indirection
- it solves a one-off problem
- a simple private helper or extracted widget is enough
- the team would pay more complexity than it gains

# Output expectations

## If asked for analysis only
Return:
1. Current architecture style
2. Existing patterns found
3. Anti-patterns or weak spots
4. Where a pattern could help
5. Which suggestions are high-value vs overengineering risk

## If asked for refactor guidance
Return:
1. Smallest recommended structural changes
2. Which pattern each change uses, if any
3. Why it helps
4. What should remain simple and not be abstracted

# Severity model

- High: structure is actively harming maintainability
- Medium: code can be improved meaningfully with a clearer pattern
- Low: optional cleanup or stylistic consistency issue

# Success criteria

This skill succeeds when:
- existing patterns are identified correctly
- anti-patterns are called out clearly
- recommended patterns are pragmatic, not academic
- clean architecture alignment improves where relevant
- unnecessary abstraction is avoided
