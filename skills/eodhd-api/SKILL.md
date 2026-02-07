# Skill: eodhd-api

## Purpose
Use EODHD market data APIs to fetch, normalize, and summarize prices, fundamentals, and screening results for equities, ETFs, indices, FX, and crypto symbols where supported.

## Trigger
Use this skill when the user asks for any of the following:
- end-of-day/historical prices,
- intraday bars,
- symbol fundamentals,
- exchange listings or market metadata,
- screening/filtering by fundamentals or technical fields,
- macro/indicator context via EODHD datasets.

## Required inputs
- `EODHD_API_TOKEN` (environment variable preferred)
- instrument identifier in EODHD style where applicable (e.g., `AAPL.US`)
- date range and interval (if time-series data is requested)

## Workflow
1. Clarify objective, universe, and time horizon.
2. Select minimal endpoint set from `references/endpoints.md`.
3. Pull raw JSON via `scripts/eodhd_client.py` or equivalent HTTP call.
4. Validate assumptions:
   - symbol exists on exchange,
   - date coverage is adequate,
   - fields requested are present.
5. Produce concise analyst output using `templates/analysis_report.md`.
6. Include reproducible request examples and caveats.

## Output requirements
- State the exact symbols and date ranges used.
- Distinguish factual API output from interpretation.
- Mention any missing fields, null values, or endpoint constraints.
- Prefer tables for comparatives and bullet points for conclusions.

## Guardrails
- Never fabricate market data values.
- If data cannot be retrieved, provide exact command/call attempted and what failed.
- Ask for confirmation before broad, multi-exchange pulls that may generate very large output.

## Minimal endpoint mapping
- Historical EOD OHLCV: `eod/{SYMBOL}`
- Intraday bars: `intraday/{SYMBOL}`
- Fundamentals: `fundamentals/{SYMBOL}`
- Exchange symbols list: `exchange-symbol-list/{EXCHANGE_CODE}`
- Screener: `screener`
