# Fundamentals Data API

Status: draft
Source: financial-apis (Fundamental Data API)
Docs: https://eodhd.com/financial-apis/stock-etfs-fundamental-data-feeds
Provider: EODHD
Base URL: https://eodhd.com/api
Path: /fundamentals/{SYMBOL}
Method: GET
Auth: api_token (query)

## Purpose
Return comprehensive fundamental data for a company including financial statements,
valuation metrics, earnings history, dividends, and company profile information.

## Parameters
- Required:
  - api_token: EODHD API key
  - {SYMBOL}: Symbol with exchange suffix (e.g., AAPL.US)
- Optional:
  - filter: Comma-separated list of sections to return (e.g., General,Highlights,Valuation)

## Response (shape)
Large nested JSON object containing multiple sections:

```json
{
  "General": {
    "Code": "AAPL",
    "Name": "Apple Inc",
    "Exchange": "NASDAQ",
    "CurrencyCode": "USD",
    "Sector": "Technology",
    "Industry": "Consumer Electronics",
    "Description": "...",
    "FullTimeEmployees": 164000,
    "IPODate": "1980-12-12",
    "WebURL": "https://www.apple.com"
  },
  "Highlights": {
    "MarketCapitalization": 2500000000000,
    "EBITDA": 130000000000,
    "PERatio": 28.5,
    "PEGRatio": 2.1,
    "WallStreetTargetPrice": 195.0,
    "BookValue": 4.25,
    "DividendShare": 0.96,
    "DividendYield": 0.005,
    "EarningsShare": 6.15,
    "EPSEstimateCurrentYear": 6.50,
    "EPSEstimateNextYear": 7.20,
    "MostRecentQuarter": "2024-09-30",
    "ProfitMargin": 0.255,
    "OperatingMarginTTM": 0.302,
    "ReturnOnAssetsTTM": 0.215,
    "ReturnOnEquityTTM": 1.475,
    "RevenueTTM": 385000000000,
    "RevenuePerShareTTM": 24.50,
    "QuarterlyRevenueGrowthYOY": 0.08,
    "GrossProfitTTM": 170000000000,
    "DilutedEpsTTM": 6.15
  },
  "Valuation": {
    "TrailingPE": 28.5,
    "ForwardPE": 26.2,
    "PriceSalesTTM": 6.5,
    "PriceBookMRQ": 41.5,
    "EnterpriseValue": 2600000000000,
    "EnterpriseValueRevenue": 6.75,
    "EnterpriseValueEbitda": 20.0
  },
  "SharesStats": {
    "SharesOutstanding": 15700000000,
    "SharesFloat": 15650000000,
    "PercentInsiders": 0.07,
    "PercentInstitutions": 60.5,
    "SharesShort": 120000000,
    "ShortRatio": 1.5,
    "ShortPercentOfFloat": 0.008
  },
  "Financials": {
    "Balance_Sheet": { "quarterly": [...], "yearly": [...] },
    "Income_Statement": { "quarterly": [...], "yearly": [...] },
    "Cash_Flow": { "quarterly": [...], "yearly": [...] }
  },
  "Earnings": {
    "History": [...],
    "Trend": [...],
    "Annual": [...]
  },
  "outstandingShares": { "annual": [...], "quarterly": [...] }
}
```

## Example request
```bash
# Full fundamentals for AAPL
curl "https://eodhd.com/api/fundamentals/AAPL.US?api_token=demo&fmt=json"

# Only highlights and valuation
curl "https://eodhd.com/api/fundamentals/AAPL.US?api_token=demo&filter=Highlights,Valuation"

# Using the helper client
python eodhd_client.py --endpoint fundamentals --symbol AAPL.US
```

## Notes
- Returns extensive data; use filter parameter to reduce payload size
- Financial statements include quarterly and yearly data going back several years
- Currency is in the company's reporting currency (check CurrencyCode)
- Some fields may be null for companies that don't report certain metrics
- ETFs have different structure focusing on holdings and asset allocation
- Mutual funds have NAV history and expense ratio information
- API call consumption: 1 call per request regardless of sections filtered
