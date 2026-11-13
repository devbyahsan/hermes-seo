# Getting Started with hermes-seo

## Your first audit

```bash
# 1. Start Hermes
hermes

# 2. In the chat, run
/seo audit https://example.com
```

The skill spins up parallel sub-skills and returns a scored, prioritized report.

## Understanding the report

The report includes:
- **SEO Health Score** (0–100) with weighted category scores
- **Critical / High / Medium / Low** findings by priority
- **Dependency-sequenced** action plan with falsifiability checks
- **Leading indicators** you can monitor without re-running

## Next steps

1. Read the `README.md` for the full command reference
2. Run `/seo setup` to prepare the isolated Python runtime
3. Try `/seo doctor` to check runtime readiness
