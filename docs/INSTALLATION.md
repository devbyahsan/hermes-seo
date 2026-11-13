# Installation Guide

This guide covers installing hermes-seo in different Hermes setups.

## Prerequisites

- Python 3.11 – 3.14
- Hermes Agent CLI or desktop app
- SSH/Git access to the repo

## Method 1: Plugin registry (recommended)

```bash
hermes plugin install hermes-seo
```

The plugin manager fetches the latest release and enables it.

## Method 2: Local dev install

```bash
git clone https://github.com/AgriciDaniel/claude-seo.git
cd claude-seo
hermes plugin link .
```

## Method 3: Bare skills directory

Copy `skills/` to `~/.hermes/skills/`:

```bash
cp -r skills ~/.hermes/skills/
```

The agent loads skills from `~/.hermes/skills/` on startup.

## Verification

```bash
hermes skills list
# Should show: seo, seo-technical, seo-content, ...
```

## Upgrading

```bash
hermes plugin update hermes-seo
# or
cd claude-seo && git pull && hermes plugin link .
```
