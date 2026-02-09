# Upcoming Splits API

Status: complete
Source: financial-apis (Calendar Upcoming Earnings, IPOs, and Splits API)
Docs: https://eodhd.com/financial-apis/calendar-upcoming-earnings-ipos-and-splits
Provider: EODHD
Base URL: https://eodhd.com/api
Path: /calendar/splits
Method: GET
Auth: api_token (query)

## Purpose

Fetches upcoming and historical stock split data including split ratios and effective dates.
Useful for portfolio adjustments, historical price analysis, and corporate action tracking.

## Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| api_token | Yes | string | Your API key for authentication |
| from | No | string (YYYY-MM-DD) | Start date for splits data. Defaults to today |
| to | No | string (YYYY-MM-DD) | End date for splits data. Defaults to 7 days from today |
| fmt | No | string | Output format: 'csv' or 'json'. Defaults to 'csv' |

## Response (shape)

```json
{
  "type": "Splits",
  "description": "Upcoming and historical Stock Splits",
  "from": "2025-01-01",
  "to": "2025-01-31",
  "splits": [
    {
      "code": "NVDA.US",
      "exchange": "US",
      "date": "2025-01-15",
      "split": "10/1",
      "old_shares": 1,
      "new_shares": 10,
      "optionable": "Y"
    },
    {
      "code": "SHOP.US",
      "exchange": "US",
      "date": "2025-01-20",
      "split": "1/5",
      "old_shares": 5,
      "new_shares": 1,
      "optionable": "Y"
    }
  ]
}
```

### Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| code | string | Ticker symbol with exchange suffix |
| exchange | string | Exchange code (e.g., 'US', 'LSE') |
| date | string (date) | Effective date of the split |
| split | string | Split ratio as "new/old" (e.g., "10/1" for 10-for-1) |
| old_shares | number | Number of shares before split |
| new_shares | number | Number of shares after split |
| optionable | string | Whether options are available ('Y' or 'N') |

### Understanding Split Ratios

- **Forward split (e.g., "10/1")**: Each share becomes 10 shares, price divides by 10
  - old_shares: 1, new_shares: 10
  - Example: $1000 stock becomes $100 after 10-for-1 split

- **Reverse split (e.g., "1/5")**: 5 shares become 1 share, price multiplies by 5
  - old_shares: 5, new_shares: 1
  - Example: $2 stock becomes $10 after 1-for-5 reverse split

## Example Requests

```bash
# Splits for the next 7 days
curl "https://eodhd.com/api/calendar/splits?api_token=demo&fmt=json"

# Splits for specific date range
curl "https://eodhd.com/api/calendar/splits?from=2025-01-01&to=2025-01-31&api_token=demo&fmt=json"

# Splits for next month
curl "https://eodhd.com/api/calendar/splits?from=2025-02-01&to=2025-02-28&api_token=demo&fmt=json"

# Using the helper client
python eodhd_client.py --endpoint calendar/splits --from-date 2025-01-01 --to-date 2025-01-31
```

## Notes

- Forward splits (new_shares > old_shares) are more common for high-priced stocks
- Reverse splits (new_shares < old_shares) often indicate struggling companies trying to meet exchange listing requirements
- Historical prices are typically split-adjusted automatically in EOD data
- Use `split` string for display; use `old_shares`/`new_shares` for calculations
- Required fields: code, exchange, date, split
- API call consumption: 1 call per request
