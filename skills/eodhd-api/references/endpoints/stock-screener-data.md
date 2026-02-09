# Stock Screener API

Status: draft
Source: financial-apis (Stock Market Screener API)
Docs: https://eodhd.com/financial-apis/stock-market-screener-api
Provider: EODHD
Base URL: https://eodhd.com/api
Path: /screener
Method: GET
Auth: api_token (query)

## Purpose
Screen and filter stocks based on fundamental metrics, market cap, sector, exchange,
and other criteria. Returns a list of matching symbols with key metrics.

## Parameters
- Required:
  - api_token: EODHD API key
- Optional:
  - sort: Field to sort by (e.g., market_capitalization, name)
  - order: Sort order: a (ascending) or d (descending)
  - limit: Number of results (default 50, max 100)
  - offset: Pagination offset
  - filters: JSON array of filter conditions (see below)

## Filter Syntax
Filters are passed as a JSON array with field, operation, and value:

```json
[
  ["market_capitalization", ">", 1000000000],
  ["sector", "=", "Technology"],
  ["exchange", "=", "us"]
]
```

### Supported Filter Fields
| Field | Description | Type |
|-------|-------------|------|
| market_capitalization | Market cap in USD | number |
| earnings_share | EPS | number |
| dividend_yield | Dividend yield % | number |
| sector | Industry sector | string |
| industry | Specific industry | string |
| exchange | Exchange code (us, uk, etc.) | string |
| name | Company name (partial match) | string |
| code | Ticker symbol | string |
| refund_1d_p | 1-day return % | number |
| refund_5d_p | 5-day return % | number |
| refund_ytd_p | Year-to-date return % | number |
| avgvol_50d | 50-day avg volume | number |
| pe | P/E ratio | number |
| peg | PEG ratio | number |
| pb | Price/Book ratio | number |
| ps | Price/Sales ratio | number |
| revenue | Revenue | number |
| ebitda | EBITDA | number |
| roe | Return on equity % | number |
| roa | Return on assets % | number |
| beta | Beta coefficient | number |

### Filter Operations
- `=` : equals (exact match for strings)
- `!=` : not equals
- `>` : greater than
- `>=` : greater than or equal
- `<` : less than
- `<=` : less than or equal
- `match` : partial string match

## Response (shape)
Array of matching stocks with key metrics:

```json
{
  "count": 150,
  "data": [
    {
      "code": "AAPL",
      "name": "Apple Inc",
      "exchange": "NASDAQ",
      "sector": "Technology",
      "industry": "Consumer Electronics",
      "market_capitalization": 2500000000000,
      "earnings_share": 6.15,
      "dividend_yield": 0.005,
      "pe": 28.5,
      "peg": 2.1,
      "pb": 41.5,
      "ps": 6.5,
      "roe": 147.5,
      "roa": 21.5,
      "beta": 1.25,
      "refund_1d_p": 0.5,
      "refund_5d_p": 2.1,
      "refund_ytd_p": 15.3
    }
  ]
}
```

## Example request
```bash
# Large-cap tech stocks
curl 'https://eodhd.com/api/screener?api_token=demo&fmt=json&filters=[["market_capitalization",">",100000000000],["sector","=","Technology"]]'

# High dividend yield stocks
curl 'https://eodhd.com/api/screener?api_token=demo&fmt=json&filters=[["dividend_yield",">",0.04]]&sort=dividend_yield&order=d'

# Low P/E stocks in US market
curl 'https://eodhd.com/api/screener?api_token=demo&fmt=json&filters=[["exchange","=","us"],["pe",">",0],["pe","<",15]]&limit=20'

# Using the helper client (basic)
python eodhd_client.py --endpoint screener --limit 20
```

## Notes
- Filters must be URL-encoded when passed as query parameters
- Maximum 100 results per request; use offset for pagination
- Sorting by metrics helps prioritize results
- Null values may exist for stocks missing certain metrics
- Screener data is updated daily
- API call consumption: 1 call per request
