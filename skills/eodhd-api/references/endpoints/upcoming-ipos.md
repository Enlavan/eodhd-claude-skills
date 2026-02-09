# Upcoming IPOs API

Status: complete
Source: financial-apis (Calendar Upcoming Earnings, IPOs, and Splits API)
Docs: https://eodhd.com/financial-apis/calendar-upcoming-earnings-ipos-and-splits
Provider: EODHD
Base URL: https://eodhd.com/api
Path: /calendar/ipos
Method: GET
Auth: api_token (query)

## Purpose

Fetches upcoming and recent IPO (Initial Public Offering) data including expected pricing,
share offerings, and deal details. Useful for tracking new market listings and IPO investment
opportunities.

## Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| api_token | Yes | string | Your API key for authentication |
| from | No | string (YYYY-MM-DD) | Start date for IPO data. Defaults to today |
| to | No | string (YYYY-MM-DD) | End date for IPO data. Defaults to 7 days from today |
| fmt | No | string | Output format: 'csv' or 'json'. Defaults to 'csv' |

## Response (shape)

```json
{
  "type": "IPOs",
  "description": "Upcoming and historical IPOs",
  "from": "2025-01-01",
  "to": "2025-01-31",
  "ipos": [
    {
      "code": "NEWCO",
      "exchange": "US",
      "name": "NewCo Technologies Inc",
      "currency": "USD",
      "start_date": "2025-01-15",
      "filing_date": "2024-12-01",
      "amended_date": "2024-12-20",
      "price_from": 18.00,
      "price_to": 21.00,
      "offer_price": 19.50,
      "shares": 10000000,
      "deal_type": "IPO"
    }
  ]
}
```

### Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| code | string | Ticker symbol for the new listing |
| exchange | string | Exchange code where IPO will list (e.g., 'US', 'LSE') |
| name | string | Company name |
| currency | string | Currency for pricing (e.g., 'USD') |
| start_date | string (date) | Expected or actual IPO date |
| filing_date | string (date) | SEC/regulatory filing date |
| amended_date | string (date)/null | Date of any amended filings |
| price_from | number/null | Low end of expected price range |
| price_to | number/null | High end of expected price range |
| offer_price | number/null | Final offer price (null until priced) |
| shares | number/null | Number of shares being offered |
| deal_type | string | Type of offering (e.g., 'IPO', 'SPAC', 'Direct Listing') |

### Deal Types

- **IPO**: Traditional initial public offering
- **SPAC**: Special Purpose Acquisition Company merger
- **Direct Listing**: Direct listing without traditional underwriting
- **Spin-off**: Corporate spin-off from parent company

## Example Requests

```bash
# IPOs for the next 7 days
curl "https://eodhd.com/api/calendar/ipos?api_token=demo&fmt=json"

# IPOs for specific date range
curl "https://eodhd.com/api/calendar/ipos?from=2025-01-01&to=2025-01-31&api_token=demo&fmt=json"

# IPOs for next quarter
curl "https://eodhd.com/api/calendar/ipos?from=2025-01-01&to=2025-03-31&api_token=demo&fmt=json"

# Using the helper client
python eodhd_client.py --endpoint calendar/ipos --from-date 2025-01-01 --to-date 2025-01-31
```

## Notes

- `offer_price` is null until the IPO is priced (usually day before or day of listing)
- `price_from` and `price_to` represent the expected pricing range from prospectus
- `shares` represents total shares in the offering (not including overallotment)
- `filing_date` is when initial S-1/prospectus was filed
- `amended_date` updates when pricing or terms change
- Required fields: code, exchange, name, start_date
- API call consumption: 1 call per request
