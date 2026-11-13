# Contributing to hermes-seo

Thank you for your interest in the Hermes port of claude-seo. This guide covers
how to contribute.

## How to contribute

### Reporting issues

- Use GitHub Issues. Include:
  - Hermes version (`hermes --version` or `hermes doctor --json`)
  - Python version (`python --version`)
  - The skill command you ran and the full output
  - Steps to reproduce

### Submitting changes

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-change`)
3. Make your changes
4. Test locally in your Hermes installation
5. Commit with a clear message
6. Open a Pull Request

### Adding a new skill

Each skill is a `SKILL.md` file with YAML frontmatter:

```yaml
---
name: my-skill
description: "What it does and when to use it."
version: "1.0.0"
author: "Your Name"
license: "MIT"
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [seo, my-category]
    homepage: "https://github.com/you/hermes-seo"
    related_skills: [seo-technical]
---
```

Skills follow progressive disclosure: keep `SKILL.md` under 200 lines and move
detail to `references/` and `scripts/`.

### Adding a new extension

Extensions ship in `extensions/<name>/` with:
- `install.sh` / `install.ps1` — setup script
- `README.md` — usage docs
- `skills/` — optional sub-skills
- `references/` — reference docs

## Code style

- Python: `ruff check .` (target `>=3.11`, line length 100)
- Markdown: no Title Case headings, no em dashes, no emojis
- All prose deliverables follow the Hermes style guide

## License

MIT. By contributing you agree to license your contributions under the same.
