# Codex Adapter: eodhd-api

Use this adapter in Codex environments that support tool-assisted or script-assisted workflows.

## Suggested registration
- Skill folder: `skills/eodhd-api`
- Primary guide: `skills/eodhd-api/SKILL.md`
- Helper script: `skills/eodhd-api/scripts/eodhd_client.py`
- Token env var: `EODHD_API_TOKEN`

## Recommended execution flow
1. Read `SKILL.md`.
2. Select endpoint recipe from `references/endpoints.md`.
3. Run helper script for API pull.
4. Format output using `templates/analysis_report.md`.

## Example
```bash
export EODHD_API_TOKEN="<token>"
python skills/eodhd-api/scripts/eodhd_client.py \
  --endpoint eod \
  --symbol NVDA.US \
  --from-date 2025-01-01 \
  --to-date 2025-01-31
```
