# Claude Adapter: eodhd-api

Use this adapter when operating in Claude-style environments with local skills support.

## Suggested registration
- Skill name: `eodhd-api`
- Entry file: `skills/eodhd-api/SKILL.md`
- Token env var: `EODHD_API_TOKEN`

## Prompting pattern
"Use the `eodhd-api` skill. Pull `{SYMBOLS}` from `{FROM}` to `{TO}`, include fundamentals summary, and return a concise analyst report with reproducible calls."

## Operational notes
- Keep initial pull narrow to validate symbol and coverage.
- Prefer deterministic command examples with explicit parameters.
- Include caveats on plan limitations and missing fields.
