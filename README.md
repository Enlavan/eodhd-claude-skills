# EODHD Skills Adapter for Claude/Codex

Initial release of reusable skills and adapters for using the [EOD Historical Data (EODHD) API](https://eodhd.com/) from Claude- and Codex-style agent workflows.

> **Note:** external network access was restricted in this environment while implementing this release, so this version is designed as a robust starter pack based on public EODHD API conventions and common skill layouts.

## What is included

- `skills/eodhd-api/SKILL.md` — primary skill instructions with trigger conditions, workflow, and output standards.
- `skills/eodhd-api/references/endpoints.md` — endpoint catalog and parameter guidance.
- `skills/eodhd-api/references/workflows.md` — common analysis workflows (OHLCV pull, fundamentals snapshot, screening, and macro overlays).
- `skills/eodhd-api/templates/analysis_report.md` — report template for consistent analyst-ready output.
- `skills/eodhd-api/scripts/eodhd_client.py` — lightweight Python helper client (stdlib only).
- `adapters/claude/eodhd-api.md` — adapter guidance for Claude-oriented environments.
- `adapters/codex/eodhd-api.md` — adapter guidance for Codex-oriented environments.

## Quick start

1. Export your API token:

```bash
export EODHD_API_TOKEN="<your_token>"
```

2. Use the helper client:

```bash
python skills/eodhd-api/scripts/eodhd_client.py \
  --endpoint eod \
  --symbol AAPL.US \
  --from-date 2025-01-01 \
  --to-date 2025-01-31
```

3. In your agent prompt, request usage of the `eodhd-api` skill and desired workflow (e.g., "daily prices + valuation snapshot").

## Scope of this initial release

This release focuses on:
- historical/end-of-day data retrieval,
- intraday retrieval,
- fundamentals/exchange/screener access,
- consistent, auditable agent output format.

Future releases can add:
- richer schema validation,
- higher-level factor libraries,
- caching + retry strategy,
- integrated notebook/report generation.
