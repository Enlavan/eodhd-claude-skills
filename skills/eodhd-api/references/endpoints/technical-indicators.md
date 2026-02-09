# Technical Indicators API

Status: complete
Source: financial-apis (Technical Indicator API)
Docs: https://eodhd.com/financial-apis/technical-indicators-api
Provider: EODHD
Base URL: https://eodhd.com/api
Path: /technical/{SYMBOL}
Method: GET
Auth: api_token (query)

## Purpose
Calculate common technical indicators (SMA, EMA, RSI, MACD, etc.) for a symbol
without needing to compute them locally from raw price data.

## Parameters
- Required:
  - api_token: EODHD API key
  - {SYMBOL}: Symbol with exchange suffix (e.g., AAPL.US)
  - function: Indicator function name (see list below)
- Optional:
  - period: Lookback period (default varies by indicator)
  - from: Start date YYYY-MM-DD
  - to: End date YYYY-MM-DD
  - order: a (ascending) or d (descending)
  - splitadjusted_only: 1 for split-adjusted data only

## Supported Functions
| Function | Description | Default Period |
|----------|-------------|----------------|
| sma | Simple Moving Average | 50 |
| ema | Exponential Moving Average | 50 |
| wma | Weighted Moving Average | 50 |
| volatility | Historical Volatility | 50 |
| stochastic | Stochastic Oscillator | 14 |
| rsi | Relative Strength Index | 14 |
| stddev | Standard Deviation | 50 |
| avgvol | Average Volume | 50 |
| avgvolccy | Avg Volume Currency | 50 |
| macd | MACD | (12,26,9) |
| atr | Average True Range | 14 |
| cci | Commodity Channel Index | 20 |
| adx | Average Directional Index | 14 |
| slope | Linear Regression Slope | 50 |
| bbands | Bollinger Bands | 20 |
| dmi | Directional Movement Index | 14 |
| williamsr | Williams %R | 14 |
| sar | Parabolic SAR | (0.02,0.2) |
| splitadjusted | Split-Adjusted Prices | N/A |

## Response (shape)
Array of data points with date and indicator value(s):

```json
[
  {
    "date": "2024-01-15",
    "sma": 185.42
  }
]
```

For multi-value indicators like MACD:
```json
[
  {
    "date": "2024-01-15",
    "macd": 2.35,
    "macd_signal": 1.89,
    "macd_hist": 0.46
  }
]
```

For Bollinger Bands:
```json
[
  {
    "date": "2024-01-15",
    "bbands_upper": 195.50,
    "bbands_middle": 185.42,
    "bbands_lower": 175.34
  }
]
```

## Example request
```bash
# 50-period SMA
curl "https://eodhd.com/api/technical/AAPL.US?function=sma&period=50&api_token=demo&fmt=json"

# 14-period RSI
curl "https://eodhd.com/api/technical/AAPL.US?function=rsi&period=14&api_token=demo&fmt=json"

# MACD with date range
curl "https://eodhd.com/api/technical/AAPL.US?function=macd&from=2024-01-01&to=2024-01-31&api_token=demo&fmt=json"

# Bollinger Bands
curl "https://eodhd.com/api/technical/AAPL.US?function=bbands&period=20&api_token=demo&fmt=json"

# Using the helper client
python eodhd_client.py --endpoint technical --symbol AAPL.US --function sma --period 50
```

## Notes
- Technical indicators require sufficient historical data for the lookback period
- First N values (where N = period) will be NaN as insufficient data for calculation
- MACD uses standard (12, 26, 9) parameters by default
- Bollinger Bands use 2 standard deviations by default
- All calculations are based on adjusted close prices
- API call consumption: 1 call per request
