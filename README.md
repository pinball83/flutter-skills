# Flutter Skills Pack

A repository of Flutter-focused `SKILL.md` packages in a `skills.sh`-compatible layout.

## Included Skills
- `flutter-architecture-guard`
- `flutter-design-pattern-review`
- `flutter-simplify`

## Repository Structure
```text
flutter-skills/
├── CHANGELOG.md
├── README.md
├── SKILL_INDEX.md
└── skills/
    ├── flutter-architecture-guard/
    │   └── SKILL.md
    ├── flutter-design-pattern-review/
    │   └── SKILL.md
    └── flutter-simplify/
        └── SKILL.md
```

## Install From GitHub (skills.sh)
```bash
# list available skills in repo
npx skills add <owner>/flutter-skills --list

# install one skill
npx skills add <owner>/flutter-skills --skill flutter-simplify

# install all skills
npx skills add <owner>/flutter-skills --skill '*'
```

## Local Validation
Each skill file contains YAML frontmatter with required fields:
- `name`
- `description`

Paths:
- `skills/flutter-architecture-guard/SKILL.md`
- `skills/flutter-design-pattern-review/SKILL.md`
- `skills/flutter-simplify/SKILL.md`
