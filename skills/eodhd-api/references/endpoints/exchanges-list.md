# Exchanges List API

Status: complete
Source: financial-apis (Exchanges API)
Docs: https://eodhd.com/financial-apis/exchanges-api-list-of-tickers-and-டrading-hours
Provider: EODHD
Base URL: https://eodhd.com/api
Path: /exchanges-list
Method: GET
Auth: api_token (query)

## Purpose

Fetches a list of all supported stock exchanges with their codes, names, countries,
currencies, and operating hours. Useful for discovering available markets and understanding
exchange metadata before querying market data.

## Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| api_token | Yes | string | Your API key for authentication |
| fmt | No | string | Output format: 'json' or 'csv'. Defaults to 'json' |

## Response (shape)

```json
[
  {
    "Name": "New York Stock Exchange",
    "Code": "NYSE",
    "OperatingMIC": "XNYS",
    "Country": "USA",
    "Currency": "USD",
    "CountryISO2": "US",
    "CountryISO3": "USA"
  },
  {
    "Name": "NASDAQ Stock Exchange",
    "Code": "NASDAQ",
    "OperatingMIC": "XNAS",
    "Country": "USA",
    "Currency": "USD",
    "CountryISO2": "US",
    "CountryISO3": "USA"
  },
  {
    "Name": "London Stock Exchange",
    "Code": "LSE",
    "OperatingMIC": "XLON",
    "Country": "UK",
    "Currency": "GBP",
    "CountryISO2": "GB",
    "CountryISO3": "GBR"
  }
]
```

### Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| Name | string | Full name of the exchange |
| Code | string | EODHD exchange code (used in symbol suffix) |
| OperatingMIC | string | ISO 10383 Market Identifier Code |
| Country | string | Country name |
| Currency | string | Primary trading currency |
| CountryISO2 | string | ISO 3166-1 alpha-2 country code |
| CountryISO3 | string | ISO 3166-1 alpha-3 country code |

### Common Exchange Codes

| Code | Exchange |
|------|----------|
| US | United States (NYSE, NASDAQ, AMEX combined) |
| LSE | London Stock Exchange |
| XETRA | Frankfurt (Deutsche Börse) |
| PA | Euronext Paris |
| TO | Toronto Stock Exchange |
| HK | Hong Kong Stock Exchange |
| TW | Taiwan Stock Exchange |
| KO | Korea Stock Exchange |
| SHG | Shanghai Stock Exchange |
| SHE | Shenzhen Stock Exchange |
| AU | Australian Securities Exchange |
| TSE | Tokyo Stock Exchange |
| NSE | National Stock Exchange of India |
| SA | Sao Paulo Stock Exchange (B3) |
| MC | Madrid Stock Exchange |
| AS | Euronext Amsterdam |

## Example Requests

```bash
# List all exchanges
curl "https://eodhd.com/api/exchanges-list?api_token=demo&fmt=json"

# Using the helper client
python eodhd_client.py --endpoint exchanges-list
```

## Notes

- Exchange codes are used as suffixes in symbol identifiers (e.g., `AAPL.US`, `BMW.XETRA`)
- The `US` code combines NYSE, NASDAQ, and AMEX into a single virtual exchange
- MIC codes follow ISO 10383 standard for market identification
- Exchange list is relatively static; cache results when appropriate
- Use exchange codes with `exchange-symbol-list` endpoint to get tickers
- API call consumption: 1 call per request
