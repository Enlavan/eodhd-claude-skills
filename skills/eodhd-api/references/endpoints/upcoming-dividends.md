# Historical Dividends API

Status: complete
Source: financial-apis (Dividends API)
Docs: https://eodhd.com/financial-apis/api-splits-dividends
Provider: EODHD
Base URL: https://eodhd.com/api
Path: /div/{SYMBOL}
Method: GET
Auth: api_token (query)

## Purpose

Fetches historical dividend data for a specified stock symbol, including key dividend dates
(declaration, record, ex-dividend, payment) and values. Useful for income analysis, dividend
tracking, and yield calculations.

## Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| {SYMBOL} | Yes | path | Ticker symbol (e.g., 'AAPL.US', 'AAPL.MX') |
| api_token | Yes | string | Your API key for authentication |
| from | No | string (YYYY-MM-DD) | Start date. Defaults to earliest available |
| to | No | string (YYYY-MM-DD) | End date. Defaults to latest available |
| fmt | No | string | Output format: 'json' or 'csv'. Defaults to 'json' |

## Response (shape)

Array of dividend records:

```json
[
  {
    "date": "2024-08-09",
    "declarationDate": "2024-07-24",
    "recordDate": "2024-08-13",
    "paymentDate": "2024-08-16",
    "period": "Quarterly",
    "value": 0.25,
    "unadjustedValue": 0.25,
    "currency": "USD"
  }
]
```

### Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| date | string (date) | Ex-dividend date |
| declarationDate | string (date) | Date dividend was declared |
| recordDate | string (date) | Record date for dividend eligibility |
| paymentDate | string (date) | Dividend payment date |
| period | string | Dividend period (e.g., 'Quarterly', 'Annual') |
| value | number | Dividend value per share (split-adjusted) |
| unadjustedValue | number | Unadjusted dividend value (before splits) |
| currency | string | Currency (e.g., 'USD') |

### Key Dates Explained

- **Declaration Date**: When the company announces the dividend
- **Ex-Dividend Date**: First day stock trades without dividend rights
- **Record Date**: Cutoff date for determining eligible shareholders
- **Payment Date**: When dividends are actually paid

## Example Requests

```bash
# All dividend history for AAPL
curl "https://eodhd.com/api/div/AAPL.US?api_token=demo&fmt=json"

# Dividends for specific date range
curl "https://eodhd.com/api/div/AAPL.US?from=2020-01-01&to=2024-12-31&api_token=demo&fmt=json"

# Dividends for international stock
curl "https://eodhd.com/api/div/BMW.XETRA?api_token=demo&fmt=json"

# Using the helper client
python eodhd_client.py --endpoint dividends --symbol AAPL.US --from-date 2020-01-01
```

## Notes

- `value` is split-adjusted; use `unadjustedValue` for historical accuracy
- Ex-dividend date (`date`) is the key date for most trading purposes
- Must own shares before ex-dividend date to receive the dividend
- Period values include: 'Quarterly', 'Semi-Annual', 'Annual', 'Monthly', 'Special'
- Required fields: date, value, currency
- API call consumption: 1 call per request
