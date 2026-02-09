# Exchange Symbol List API

Status: complete
Source: financial-apis (Exchanges API)
Docs: https://eodhd.com/financial-apis/exchanges-api-list-of-tickers-and-trading-hours
Provider: EODHD
Base URL: https://eodhd.com/api
Path: /exchange-symbol-list/{EXCHANGE}
Method: GET
Auth: api_token (query)

## Purpose

Fetches the complete list of ticker symbols available on a specific exchange, including
symbol codes, names, countries, exchanges, currencies, and instrument types. Useful for
discovering tradable instruments and building symbol universes.

## Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| {EXCHANGE} | Yes | path | Exchange code (e.g., 'US', 'LSE', 'XETRA') |
| api_token | Yes | string | Your API key for authentication |
| fmt | No | string | Output format: 'json' or 'csv'. Defaults to 'json' |

## Response (shape)

```json
[
  {
    "Code": "AAPL",
    "Name": "Apple Inc",
    "Country": "USA",
    "Exchange": "NASDAQ",
    "Currency": "USD",
    "Type": "Common Stock",
    "Isin": "US0378331005"
  },
  {
    "Code": "MSFT",
    "Name": "Microsoft Corporation",
    "Country": "USA",
    "Exchange": "NASDAQ",
    "Currency": "USD",
    "Type": "Common Stock",
    "Isin": "US5949181045"
  },
  {
    "Code": "SPY",
    "Name": "SPDR S&P 500 ETF Trust",
    "Country": "USA",
    "Exchange": "NYSE ARCA",
    "Currency": "USD",
    "Type": "ETF",
    "Isin": "US78462F1030"
  }
]
```

### Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| Code | string | Ticker symbol |
| Name | string | Company or instrument name |
| Country | string | Country of incorporation/listing |
| Exchange | string | Specific exchange within the market |
| Currency | string | Trading currency |
| Type | string | Instrument type (see below) |
| Isin | string/null | International Securities Identification Number |

### Instrument Types

| Type | Description |
|------|-------------|
| Common Stock | Regular equity shares |
| ETF | Exchange Traded Fund |
| FUND | Mutual fund |
| Preferred Stock | Preferred equity shares |
| REIT | Real Estate Investment Trust |
| Bond | Fixed income security |
| Index | Market index |
| Currency | Foreign exchange pair |
| Cryptocurrency | Digital currency |

## Example Requests

```bash
# All US tickers
curl "https://eodhd.com/api/exchange-symbol-list/US?api_token=demo&fmt=json"

# London Stock Exchange tickers
curl "https://eodhd.com/api/exchange-symbol-list/LSE?api_token=demo&fmt=json"

# Frankfurt (XETRA) tickers
curl "https://eodhd.com/api/exchange-symbol-list/XETRA?api_token=demo&fmt=json"

# Using the helper client
python eodhd_client.py --endpoint exchange-symbol-list --symbol US
```

## Notes

- Full symbol format: `{Code}.{EXCHANGE}` (e.g., `AAPL.US`, `BMW.XETRA`)
- US exchange includes NYSE, NASDAQ, and AMEX (8000+ symbols)
- Large exchanges may return thousands of symbols
- `Type` field helps filter by instrument category
- `Isin` provides cross-reference to international databases
- Some symbols may be delisted but still in historical data
- API call consumption: 1 call per request
- Consider caching results as symbol lists don't change frequently
