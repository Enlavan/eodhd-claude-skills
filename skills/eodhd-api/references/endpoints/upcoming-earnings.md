# Upcoming Earnings API

Status: complete
Source: financial-apis (Calendar Earnings API)
Docs: https://eodhd.com/financial-apis/calendar-upcoming-earnings-ipos-and-splits
Provider: EODHD
Base URL: https://eodhd.com/api
Path: /calendar/earnings
Method: GET
Auth: api_token (query)

## Purpose

Fetches upcoming and historical earnings data, including report dates, actual vs estimated EPS,
and beat/miss percentages. Useful for earnings calendars, event-driven trading, and fundamental analysis.

## Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| api_token | Yes | string | Your API key for authentication |
| from | No | string (YYYY-MM-DD) | Start date for earnings data. Defaults to today |
| to | No | string (YYYY-MM-DD) | End date for earnings data. Defaults to 7 days from today |
| symbols | No | string | Specific symbols (comma-separated, e.g., 'AAPL.US,MSFT.US'). Overrides from/to if used |
| fmt | No | string | Output format: 'csv' or 'json'. Defaults to 'csv' |

## Response (shape)

```json
{
  "type": "Earnings",
  "description": "Historical and upcoming Earnings",
  "from": "2025-01-01",
  "to": "2025-01-07",
  "earnings": [
    {
      "code": "AAPL.US",
      "report_date": "2025-02-02",
      "date": "2024-12-31",
      "before_after_market": "AfterMarket",
      "currency": "USD",
      "actual": 1.88,
      "estimate": 1.94,
      "difference": -0.06,
      "percent": -3.0928
    }
  ]
}
```

### Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| code | string | Ticker symbol |
| report_date | string (date) | Date the earnings report was released |
| date | string (date) | End date of the fiscal period |
| before_after_market | string | 'BeforeMarket' or 'AfterMarket' timing |
| currency | string | Currency of earnings values |
| actual | number | Actual reported EPS (null if not yet reported) |
| estimate | number | Consensus EPS estimate |
| difference | number | Actual minus estimate |
| percent | number | Percentage difference (beat/miss) |

## Example Requests

```bash
# Earnings for the next 7 days
curl "https://eodhd.com/api/calendar/earnings?api_token=demo&fmt=json"

# Earnings for specific date range
curl "https://eodhd.com/api/calendar/earnings?from=2025-01-01&to=2025-01-31&api_token=demo&fmt=json"

# Earnings for specific symbols
curl "https://eodhd.com/api/calendar/earnings?symbols=AAPL.US,MSFT.US&api_token=demo&fmt=json"

# Using the helper client
python eodhd_client.py --endpoint calendar/earnings --from-date 2025-01-01 --to-date 2025-01-31
```

## Notes

- `before_after_market` indicates when earnings are released relative to market hours
- `actual` will be null for upcoming (not yet reported) earnings
- `percent` shows earnings surprise: positive = beat, negative = miss
- When using `symbols` parameter, `from` and `to` are ignored
- Required fields: code, report_date, date, currency
- API call consumption: 1 call per request
