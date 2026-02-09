# Intraday Historical Data API

Status: draft
Source: financial-apis (Intraday Historical Data API)
Docs: https://eodhd.com/financial-apis/intraday-historical-data-api
Provider: EODHD
Base URL: https://eodhd.com/api
Path: /intraday/{SYMBOL}
Method: GET
Auth: api_token (query)

## Purpose
Return intraday historical OHLCV data for a symbol with configurable intervals (1m, 5m, 1h).
Useful for short-term analysis, event studies, and high-frequency patterns.

## Parameters
- Required:
  - api_token: EODHD API key
  - {SYMBOL}: Symbol with exchange suffix (e.g., AAPL.US)
- Optional:
  - fmt: csv or json (default csv)
  - interval: 1m, 5m, or 1h (default 5m)
  - from: Unix timestamp (seconds) for start
  - to: Unix timestamp (seconds) for end

## Response (shape)
- json: array of bars with timestamp, gmtoffset, datetime, open, high, low, close, volume
- csv: header row with corresponding fields

```json
[
  {
    "timestamp": 1609459200,
    "gmtoffset": -18000,
    "datetime": "2021-01-01 00:00:00",
    "open": 132.43,
    "high": 132.63,
    "low": 132.35,
    "close": 132.59,
    "volume": 143523
  }
]
```

## Example request
```bash
# 5-minute bars for AAPL
curl "https://eodhd.com/api/intraday/AAPL.US?api_token=demo&fmt=json&interval=5m"

# 1-hour bars with date range (Unix timestamps)
curl "https://eodhd.com/api/intraday/AAPL.US?api_token=demo&fmt=json&interval=1h&from=1609459200&to=1609545600"

# Using the helper client
python eodhd_client.py --endpoint intraday --symbol AAPL.US --interval 5m
```

## Notes
- Intraday data is available for US stocks, major ETFs, and indices
- Historical depth varies by plan (typically 120 days for free tier)
- Timestamps are in UTC; gmtoffset indicates the local exchange offset
- Volume is the actual traded volume for that interval
- Data may have gaps for low-volume periods or market closures
- API call consumption: 1 call per request
