# Flutter Skills Pack

A repository of Flutter-focused `SKILL.md` packages in a `skills.sh`-compatible layout.

## Included Skills
- `flutter-architecture-guard`
- `flutter-design-pattern-review`
- `flutter-simplify`
- `jira-branch-starter`
- `pr-coverage-test-guard`

## Skill Index

See [SKILL_INDEX.md](SKILL_INDEX.md) for the full list of skills and their purpose.

## Repository Structure
```text
flutter-skills/
├── README.md
├── SKILL_INDEX.md
└── skills/
    ├── flutter-architecture-guard/
    │   └── SKILL.md
    ├── flutter-design-pattern-review/
    │   └── SKILL.md
    ├── flutter-simplify/
    │   └── SKILL.md
    ├── jira-branch-starter/
    │   ├── SKILL.md
    │   └── scripts/
    │       └── branch_name.py
    └── pr-coverage-test-guard/
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
- `skills/jira-branch-starter/SKILL.md`
- `skills/pr-coverage-test-guard/SKILL.md`
