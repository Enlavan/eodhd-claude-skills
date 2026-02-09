# Economic Events API

Status: complete
Source: financial-apis (Economic Events Data API)
Docs: https://eodhd.com/financial-apis/economic-events-data-api
Provider: EODHD
Base URL: https://eodhd.com/api
Path: /economic-events
Method: GET
Auth: api_token (query)

## Purpose

Fetches economic events and indicators by date range, country, and comparison type.
Includes actual values, estimates, and changes for events like GDP releases, employment data,
inflation reports, and central bank decisions. Useful for macro analysis and event-driven trading.

## Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| api_token | Yes | string | Your API key for authentication |
| from | No | string (YYYY-MM-DD) | Start date for data retrieval |
| to | No | string (YYYY-MM-DD) | End date for data retrieval |
| country | No | string | ISO 3166-1 alpha-2 country code (e.g., 'US', 'GB', 'DE') |
| comparison | No | string | Comparison type: 'mom' (month-over-month), 'qoq' (quarter-over-quarter), 'yoy' (year-over-year) |
| offset | No | integer | Data offset (0-1000). Default: 0 |
| limit | No | integer | Number of results (0-1000). Default: 50 |

## Response (shape)

Array of economic event objects:

```json
[
  {
    "type": "Nonfarm Payrolls",
    "comparison": null,
    "period": "May",
    "country": "US",
    "date": "2025-06-03 16:30:00",
    "actual": 275,
    "previous": 256,
    "estimate": 250,
    "change": 19,
    "change_percentage": 7.42
  },
  {
    "type": "CPI",
    "comparison": "yoy",
    "period": "May",
    "country": "US",
    "date": "2025-06-12 12:30:00",
    "actual": 3.2,
    "previous": 3.4,
    "estimate": 3.3,
    "change": -0.2,
    "change_percentage": -5.88
  }
]
```

### Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| type | string | Event type (e.g., 'Nonfarm Payrolls', 'CPI', 'GDP') |
| comparison | string/null | Comparison type: 'mom', 'qoq', 'yoy', or null |
| period | string/null | Period for the data (e.g., 'May', 'Q1') |
| country | string | ISO 3166 country code |
| date | string (datetime) | Event date and time (YYYY-MM-DD HH:MM:SS) |
| actual | number/null | Actual reported value |
| previous | number/null | Previous period's value |
| estimate | number/null | Consensus estimate |
| change | number/null | Change from previous value |
| change_percentage | number/null | Percentage change from previous |

### Common Event Types

- Employment: Nonfarm Payrolls, Unemployment Rate, Initial Jobless Claims
- Inflation: CPI, PPI, PCE Price Index
- Growth: GDP, Industrial Production, Retail Sales
- Manufacturing: ISM Manufacturing PMI, Durable Goods Orders
- Housing: Existing Home Sales, Building Permits, Housing Starts
- Central Bank: Fed Interest Rate Decision, ECB Rate Decision

## Example Requests

```bash
# Economic events for the next week
curl "https://eodhd.com/api/economic-events?api_token=demo&fmt=json"

# US events for specific date range
curl "https://eodhd.com/api/economic-events?country=US&from=2025-01-01&to=2025-01-31&api_token=demo&fmt=json"

# Year-over-year comparisons only
curl "https://eodhd.com/api/economic-events?comparison=yoy&limit=20&api_token=demo&fmt=json"

# German events with pagination
curl "https://eodhd.com/api/economic-events?country=DE&limit=50&offset=0&api_token=demo&fmt=json"

# Using the helper client
python eodhd_client.py --endpoint economic-events --from-date 2025-01-01 --to-date 2025-01-31
```

## Notes

- `actual` is null for upcoming events not yet released
- Times are in the format 'YYYY-MM-DD HH:MM:SS' (typically UTC)
- Country codes use ISO 3166-1 alpha-2 (US, GB, DE, JP, CN, etc.)
- Use `comparison` filter to get only specific comparison types
- Maximum 1000 results per request; use offset for pagination
- API call consumption: 1 call per request
