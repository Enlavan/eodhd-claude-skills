# US Options EOD API

Status: complete
Source: financial-apis (Options Data API)
Docs: https://eodhd.com/financial-apis/stock-options-data-api
Provider: EODHD
Base URL: https://eodhd.com/api
Path: /options/{SYMBOL}
Method: GET
Auth: api_token (query)

## Purpose
Retrieve end-of-day options data for US stocks including all available strikes,
expirations, Greeks, and volume/open interest data for both calls and puts.

## Parameters
- Required:
  - api_token: EODHD API key
  - {SYMBOL}: Underlying symbol with exchange suffix (e.g., AAPL.US)
- Optional:
  - from: Start date YYYY-MM-DD
  - to: End date YYYY-MM-DD
  - trade_date_from: Filter by trade date start
  - trade_date_to: Filter by trade date end
  - contract_name: Specific contract (e.g., AAPL230120C00150000)

## Response (shape)
Nested structure with metadata and options chain:

```json
{
  "code": "AAPL.US",
  "exchange": "US",
  "lastTradeDate": "2024-01-15",
  "data": [
    {
      "expirationDate": "2024-02-16",
      "impliedVolatility": 0.25,
      "putCallRatio": 0.85,
      "options": {
        "CALL": [
          {
            "contractName": "AAPL240216C00185000",
            "contractSize": "REGULAR",
            "currency": "USD",
            "type": "CALL",
            "inTheMoney": "TRUE",
            "lastTradeDateTime": "2024-01-15 16:00:00",
            "expirationDate": "2024-02-16",
            "strike": 185.0,
            "lastPrice": 8.50,
            "bid": 8.45,
            "ask": 8.55,
            "change": 0.35,
            "changePercent": 4.3,
            "volume": 15234,
            "openInterest": 45678,
            "impliedVolatility": 0.28,
            "delta": 0.65,
            "gamma": 0.025,
            "theta": -0.15,
            "vega": 0.32,
            "rho": 0.08,
            "theoretical": 8.52,
            "intrinsicValue": 7.50,
            "timeValue": 1.00,
            "updatedAt": "2024-01-15T21:00:00Z"
          }
        ],
        "PUT": [
          {
            "contractName": "AAPL240216P00185000",
            "type": "PUT",
            "strike": 185.0,
            ...
          }
        ]
      }
    }
  ]
}
```

## Example request
```bash
# All options for AAPL
curl "https://eodhd.com/api/options/AAPL.US?api_token=demo&fmt=json"

# Options with date filter
curl "https://eodhd.com/api/options/AAPL.US?api_token=demo&fmt=json&from=2024-01-01&to=2024-01-31"

# Specific contract
curl "https://eodhd.com/api/options/AAPL.US?api_token=demo&fmt=json&contract_name=AAPL240216C00185000"

# Using the helper client
python eodhd_client.py --endpoint options --symbol AAPL.US
```

## Notes
- Options data is available for US equities with listed options
- Greeks (delta, gamma, theta, vega, rho) are calculated end-of-day
- Contract naming follows OCC format: SYMBOL + YYMMDD + C/P + strike*1000
- Implied volatility is per-contract; expiration-level IV is aggregate
- Volume and open interest are as of market close
- Historical options data availability varies by plan
- Options can have many strikes/expirations; response may be large
- API call consumption: 1 call per request
