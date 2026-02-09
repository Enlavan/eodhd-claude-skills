# Live/Real-Time Price Data API

Status: draft
Source: financial-apis (Live Stock Prices API)
Docs: https://eodhd.com/financial-apis/live-realtime-stocks-api
Provider: EODHD
Base URL: https://eodhd.com/api
Path: /real-time/{SYMBOL}
Method: GET
Auth: api_token (query)

## Purpose
Return real-time (delayed 15-20 minutes for most exchanges) quote data
for a symbol including last price, change, volume, and trading range.

## Parameters
- Required:
  - api_token: EODHD API key
  - {SYMBOL}: Symbol with exchange suffix (e.g., AAPL.US)
- Optional:
  - fmt: csv or json (default csv)
  - s: Additional symbols for batch request (comma-separated)

## Response (shape)
Single quote object or array for batch requests:

```json
{
  "code": "AAPL",
  "timestamp": 1609459200,
  "gmtoffset": -18000,
  "open": 132.43,
  "high": 134.50,
  "low": 131.80,
  "close": 133.72,
  "volume": 98425000,
  "previousClose": 131.96,
  "change": 1.76,
  "change_p": 1.33
}
```

For batch requests with `s` parameter:
```json
[
  {"code": "AAPL", "close": 133.72, ...},
  {"code": "MSFT", "close": 222.42, ...}
]
```

## Example request
```bash
# Single symbol real-time quote
curl "https://eodhd.com/api/real-time/AAPL.US?api_token=demo&fmt=json"

# Batch request for multiple symbols
curl "https://eodhd.com/api/real-time/AAPL.US?s=MSFT.US,GOOGL.US&api_token=demo&fmt=json"

# Using the helper client
python eodhd_client.py --endpoint real-time --symbol AAPL.US
```

## Notes
- Data is delayed 15-20 minutes for most exchanges (real-time requires premium)
- `change` is absolute price change from previous close
- `change_p` is percentage change from previous close
- Timestamp is Unix epoch in seconds
- During market hours, data updates frequently; after hours shows last traded
- Batch requests support up to 15-20 symbols per call
- Works for stocks, ETFs, indices, forex, and crypto (exchange-dependent)
- API call consumption: 1 call per request (batch or single)
