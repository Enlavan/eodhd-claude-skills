# EODHD Endpoint Reference (Starter)

> Base URL commonly used: `https://eodhd.com/api`

## 1) Historical EOD OHLCV
- Path: `/eod/{SYMBOL}`
- Typical params:
  - `api_token` (required)
  - `from`, `to` (`YYYY-MM-DD`)
  - `period` (commonly `d`, also weekly/monthly variants where available)
  - `fmt=json`
- Use for: daily (or higher aggregation) price history.

## 2) Intraday
- Path: `/intraday/{SYMBOL}`
- Typical params:
  - `api_token`
  - `interval` (e.g., `1m`, `5m`, `1h` depending on support)
  - `from`, `to` (date/time constraints)
  - `fmt=json`
- Use for: short-horizon trading analysis and event windows.

## 3) Fundamentals
- Path: `/fundamentals/{SYMBOL}`
- Typical params:
  - `api_token`
  - `fmt=json`
- Use for: company profile, financial statements, valuation metrics, dividends/splits metadata.

## 4) Exchange Symbol List
- Path: `/exchange-symbol-list/{EXCHANGE_CODE}`
- Typical params:
  - `api_token`
  - `fmt=json`
- Use for: universe construction and exchange-level discovery.

## 5) Screener
- Path: `/screener`
- Typical params:
  - `api_token`
  - filter/sort payload (implementation-specific)
  - `limit`, `offset`
- Use for: quantitative candidate generation.

## 6) Real-time / delayed quote (availability varies by plan)
- Path patterns may include quote-specific endpoints.
- Use for: latest snapshot pricing for watchlists.

## Request pattern examples

```bash
# EOD candles
python skills/eodhd-api/scripts/eodhd_client.py \
  --endpoint eod \
  --symbol MSFT.US \
  --from-date 2025-01-01 \
  --to-date 2025-02-01

# Fundamentals
python skills/eodhd-api/scripts/eodhd_client.py \
  --endpoint fundamentals \
  --symbol MSFT.US
```

## Notes
- Endpoint availability and fields vary by subscription level.
- Keep calls narrow first, then scale to larger universes.
