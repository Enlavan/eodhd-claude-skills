# Historical Stock Prices API

Status: draft
Source: financial-apis (End-Of-Day Historical Stock Market Data API)
Docs: https://eodhd.com/financial-apis/api-for-historical-data-and-volumes
Provider: EODHD
Base URL: https://eodhd.com/api
Path: /eod/{SYMBOL}
Method: GET
Auth: api_token (query)

## Purpose
Return end-of-day historical OHLCV data for a symbol, with optional date range,
period aggregation, and output format controls.

## Parameters
- Required:
  - api_token: EODHD API key.
- Optional:
  - fmt: csv or json (default csv).
  - period: d (daily), w (weekly), m (monthly). Default d.
  - order: a (ascending), d (descending). Default a.
  - from: YYYY-MM-DD.
  - to: YYYY-MM-DD.
  - filter: last_close or last_volume (requires fmt=json).

## Response (shape)
- json: array of bars with date, open, high, low, close, adjusted_close, volume.
- csv: header row with Date,Open,High,Low,Close,Adjusted_close,Volume.

## Example request
```bash
curl "https://eodhd.com/api/eod/MCD.US?api_token=demo&fmt=json"
curl "https://eodhd.com/api/eod/MCD.US?from=2020-01-05&to=2020-02-10&period=d&api_token=demo&fmt=json"
curl "https://eodhd.com/api/eod/MCD.US?filter=last_close&api_token=demo&fmt=json"
```

## Notes
- API call consumption: 1 call per request (any length of history).
- Symbol format: {SYMBOL}.{EXCHANGE} (e.g., MCD.US).
- Free plan: 1 year historical depth for EOD data only.
- OHLC is raw (not split/dividend adjusted). Adjusted_close is adjusted to splits
  and dividends; volume is adjusted to splits.
- Yahoo-style dates supported via /api/table.csv with s/a/b/c/d/e/f/g params
  (month is 0-based). JSON output not supported for Yahoo-style.
