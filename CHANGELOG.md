# Changelog – hermes-seo

All notable changes to the hermes-seo Hermes port will be documented here.

## [2.6.0] – 2026-11-13

### Added
- Hermes-native port of claude-seo v2.6.0
- 26 Hermes skills converted from Claude Code format
- Cross-platform launcher (`scripts/claude-seo` as Python)
- `.hermes-plugin/manifest.json` plugin entry point
- Hermes-compatible `HOOK.yaml` + `handler.py` for JSON-LD validation
- Extension skeletons for 9 optional integrations (ahrefs, banana, bing-webmaster, dataforseo, firecrawl, matomo, profound, seranking, unlighthouse)
- Documentation for Hermes installation and usage

### Changed
- `CLAUDE_PLUGIN_ROOT` replaced with `HERMES_PLUGIN_ROOT`
- Claude Code plugin manifest replaced with Hermes plugin manifest
- Skill frontmatter converted to Hermes format (removed `user-invocable`, `argument-hint`)
- Bash launcher converted to Python (cross-platform, no Bash dependency)

### Fixed
- Portability: launcher and scripts are now platform-agnostic
- Skill paths updated to use Hermes-relative paths

---

## Upstream

This port is based on **claude-seo v2.6.0** by **AgriciDaniel**.
Original repo: https://github.com/AgriciDaniel/claude-seo (MIT license).
