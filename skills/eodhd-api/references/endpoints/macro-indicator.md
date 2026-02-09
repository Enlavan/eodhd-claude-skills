# Macro Indicator API

Status: complete
Source: financial-apis (Macroeconomics Data API)
Docs: https://eodhd.com/financial-apis/macroeconomics-data-and-macro-indicators-api
Provider: EODHD
Base URL: https://eodhd.com/api
Path: /macro-indicator/{COUNTRY}
Method: GET
Auth: api_token (query)

## Purpose
Retrieve macroeconomic indicators for countries including GDP, inflation, unemployment,
interest rates, trade balance, and other economic metrics from sources like the World Bank.

## Parameters
- Required:
  - api_token: EODHD API key
  - {COUNTRY}: ISO 3166-1 alpha-3 country code (e.g., USA, GBR, DEU, JPN, CHN)
- Optional:
  - indicator: Specific indicator code (see list below)
  - fmt: csv or json (default csv)

## Common Indicators
| Code | Description |
|------|-------------|
| gdp_current_usd | GDP (current US$) |
| gdp_growth_annual | GDP growth (annual %) |
| inflation_consumer_prices_annual | Inflation, consumer prices (annual %) |
| unemployment_total_percent | Unemployment, total (% of labor force) |
| interest_rate | Central bank interest rate |
| population_total | Total population |
| population_growth_annual | Population growth (annual %) |
| real_interest_rate | Real interest rate (%) |
| trade_percent_gdp | Trade (% of GDP) |
| government_debt_percent_gdp | Government debt (% of GDP) |
| current_account_percent_gdp | Current account balance (% of GDP) |

## Response (shape)
Array of time-series data points:

```json
[
  {
    "CountryCode": "USA",
    "CountryName": "United States",
    "Indicator": "gdp_current_usd",
    "Date": "2023-12-31",
    "Period": "2023",
    "Value": 25462700000000
  }
]
```

When no specific indicator is provided, returns all available indicators:
```json
{
  "CountryCode": "USA",
  "CountryName": "United States",
  "gdp_current_usd": [...],
  "inflation_consumer_prices_annual": [...],
  ...
}
```

## Example request
```bash
# All macro indicators for USA
curl "https://eodhd.com/api/macro-indicator/USA?api_token=demo&fmt=json"

# Specific indicator: GDP growth
curl "https://eodhd.com/api/macro-indicator/USA?api_token=demo&fmt=json&indicator=gdp_growth_annual"

# Inflation for Germany
curl "https://eodhd.com/api/macro-indicator/DEU?api_token=demo&fmt=json&indicator=inflation_consumer_prices_annual"

# Using the helper client
python eodhd_client.py --endpoint macro-indicator --symbol USA --indicator gdp_current_usd
```

## Notes
- Country codes use ISO 3166-1 alpha-3 format (USA, GBR, DEU, JPN, CHN, etc.)
- Data is typically annual, with varying historical depth by indicator
- Some indicators may have gaps or missing years
- Values are in the units specified by the indicator (%, USD, count, etc.)
- Data sourced from World Bank and other official sources
- API call consumption: 1 call per request
