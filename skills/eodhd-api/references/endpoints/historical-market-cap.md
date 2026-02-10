# Historical Market Capitalization API - Complete Reference

**Status**: Complete
**Source**: EODHD Historical Market Capitalization API
**Docs**: https://eodhd.com/financial-apis/historical-market-capitalization-api
**Provider**: EODHD
**Base URL**: https://eodhd.com/api
**Path**: /historical-market-cap/{TICKER_CODE}
**Method**: GET
**Auth**: api_token (query parameter)

---

## Overview

The Historical Market Capitalization API provides weekly market capitalization data for all US stocks traded on NYSE and NASDAQ, starting from 2019. This API is particularly useful for:

- **Historical trend analysis** - Track how company valuations change over time
- **Portfolio management** - Analyze market cap changes across your holdings
- **Research and backtesting** - Historical market cap data for quantitative analysis
- **Comparative analysis** - Compare market cap trends across companies or sectors

**Key Features**:
- **Weekly frequency** - Data points for each week
- **US stock coverage** - All NYSE and NASDAQ listed stocks
- **Historical depth** - Data available from 2019 onwards
- **Large cap companies** - Essential for tracking mega-cap and large-cap stocks

---

## Plan Availability

**Available Packages**:
- **All-In-One Package**
- **Fundamentals Data Feed Package**

**API Consumption**: Each request consumes **10 API calls**.

**Rate Limits**: Default limit is 100,000 API calls per day across all EODHD APIs.

---

## When to Use This API

### Use This API When:
- You need **weekly market cap data** for trend analysis
- You're tracking **historical valuation changes**
- You need **time-series market cap data** for backtesting
- You want to analyze **market cap growth rates** over time

### Use Fundamentals API Instead When:
- You need **current/real-time** market capitalization
- You need **quarterly market cap** synchronized with earnings
- You need **more precise point-in-time** values
- You're doing fundamental analysis requiring other financial metrics

**Note**: The Fundamentals API provides quarterly market cap updates that are considered more precise for specific points in time, while this API provides weekly frequency for trend analysis.

---

## API Endpoint

### Base URL Format

```
https://eodhd.com/api/historical-market-cap/{TICKER_CODE}?api_token={API_TOKEN}
```

### Ticker Code Format

**Standard Format**: `{SYMBOL_NAME}.{EXCHANGE_ID}`

**Examples**:
- `AAPL.US` - Apple Inc. on NASDAQ
- `MSFT.US` - Microsoft Corporation
- `TSLA.US` - Tesla Inc.

**US Ticker Shorthand**: For US stocks, you can omit the exchange suffix:
- `AAPL` (equivalent to `AAPL.US`)
- `MSFT` (equivalent to `MSFT.US`)
- `GOOGL` (equivalent to `GOOGL.US`)

**Supported Exchanges**:
- NYSE (New York Stock Exchange)
- NASDAQ (NASDAQ Stock Market)

---

## API Parameters

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `{TICKER_CODE}` | string | Stock ticker with exchange suffix (e.g., `AAPL.US`) or without for US stocks (e.g., `AAPL`) |
| `api_token` | string | Your EODHD API key for authentication |

### Optional Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `from` | date | 2019-01-01 | Start date in YYYY-MM-DD format. Earliest available data if omitted. |
| `to` | date | Latest | End date in YYYY-MM-DD format. Latest available data if omitted. |
| `fmt` | string | `json` | Output format: `json` or `csv` |

---

## Request Examples

### Basic Request (All Available Data)

```bash
# Get all historical market cap data for Apple
curl "https://eodhd.com/api/historical-market-cap/AAPL.US?api_token=demo"
```

### Date Range Request

```bash
# Get market cap data for Apple from Jan 5, 2020 to Mar 10, 2020
curl "https://eodhd.com/api/historical-market-cap/AAPL.US?api_token=demo&from=2020-01-05&to=2020-03-10&fmt=json"
```

### US Ticker Shorthand

```bash
# Omit .US for US stocks
curl "https://eodhd.com/api/historical-market-cap/AAPL?api_token=demo&from=2023-01-01&to=2023-12-31"
```

### CSV Format

```bash
# Get data in CSV format for spreadsheet import
curl "https://eodhd.com/api/historical-market-cap/MSFT.US?api_token=demo&from=2023-01-01&fmt=csv"
```

### Multiple Companies

```bash
# Fetch data for multiple tickers (requires separate requests)
curl "https://eodhd.com/api/historical-market-cap/AAPL.US?api_token=demo&from=2023-01-01"
curl "https://eodhd.com/api/historical-market-cap/MSFT.US?api_token=demo&from=2023-01-01"
curl "https://eodhd.com/api/historical-market-cap/GOOGL.US?api_token=demo&from=2023-01-01"
```

---

## Response Format

### JSON Response Structure

The API returns a JSON object with numeric keys (array-like structure), where each entry contains a date and market cap value.

**Example Response**:
```json
{
  "0": {
    "date": "2020-01-09",
    "value": 1357426280000
  },
  "1": {
    "date": "2020-01-16",
    "value": 1382020671500
  },
  "2": {
    "date": "2020-01-23",
    "value": 1396784480400
  },
  "3": {
    "date": "2020-01-30",
    "value": 1417086707600
  },
  "4": {
    "date": "2020-02-06",
    "value": 1422949850800
  },
  "5": {
    "date": "2020-02-13",
    "value": 1421462187600
  },
  "6": {
    "date": "2020-02-20",
    "value": 1401466244000
  },
  "7": {
    "date": "2020-02-27",
    "value": 1196781289600
  },
  "8": {
    "date": "2020-03-05",
    "value": 1281665601600
  }
}
```

### Response Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `date` | string | Weekly date in YYYY-MM-DD format | "2020-01-09" |
| `value` | number | Market capitalization in base currency (USD for US stocks) | 1357426280000 |

**Important**: The `value` field is in **raw dollars**, not millions or billions.

**Example Conversions**:
- `1357426280000` = $1.357 trillion
- `1382020671500` = $1.382 trillion

---

## CSV Response Format

When using `fmt=csv`, the response is returned in comma-separated values format:

**Example CSV Response**:
```csv
date,value
2020-01-09,1357426280000
2020-01-16,1382020671500
2020-01-23,1396784480400
2020-01-30,1417086707600
2020-02-06,1422949850800
2020-02-13,1421462187600
2020-02-20,1401466244000
2020-02-27,1196781289600
2020-03-05,1281665601600
```

**Use Case**: Direct import into Excel, Google Sheets, or data analysis tools.

---

## Data Characteristics

### Frequency

- **Weekly data points** - One value per week
- **Specific weekly dates** - Typically Thursday or Friday
- **Consistent intervals** - Regular weekly spacing

### Coverage

- **Geographic**: US stocks only (NYSE, NASDAQ)
- **Historical depth**: Data available from 2019 onwards
- **Company coverage**: All US stocks traded on NYSE/NASDAQ
- **Asset types**: Common stocks (equities only, no ETFs, funds, or bonds)

### Data Quality

- **Source**: Calculated from stock price × shares outstanding
- **Accuracy**: Weekly snapshot values
- **Updates**: Data updated weekly
- **Precision**: Raw dollar values (not rounded)

---

## Use Cases and Examples

### 1. Track Market Cap Growth Over Time

**Objective**: Analyze how Apple's market capitalization changed during 2020.

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_historical_market_cap(ticker, api_token, from_date, to_date):
    """Fetch historical market cap data."""
    url = f"https://eodhd.com/api/historical-market-cap/{ticker}"
    params = {
        "api_token": api_token,
        "from": from_date,
        "to": to_date,
        "fmt": "json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame.from_dict(data, orient='index')
    df['date'] = pd.to_datetime(df['date'])
    df['value_billions'] = df['value'] / 1e9  # Convert to billions
    df = df.sort_values('date')

    return df

# Usage
df = get_historical_market_cap('AAPL.US', 'your_api_token', '2020-01-01', '2020-12-31')

# Plot
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['value_billions'], linewidth=2)
plt.title('Apple Inc. - Historical Market Capitalization (2020)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Market Cap (Billions USD)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Statistics
print(f"Starting Market Cap: ${df['value_billions'].iloc[0]:.2f}B")
print(f"Ending Market Cap: ${df['value_billions'].iloc[-1]:.2f}B")
print(f"Growth: {((df['value_billions'].iloc[-1] / df['value_billions'].iloc[0]) - 1) * 100:.2f}%")
print(f"Peak: ${df['value_billions'].max():.2f}B")
print(f"Trough: ${df['value_billions'].min():.2f}B")
```

---

### 2. Compare Market Cap Trends Across Companies

**Objective**: Compare market cap trends of FAANG stocks.

```python
def compare_market_caps(tickers, api_token, from_date, to_date):
    """Compare market cap trends across multiple companies."""
    all_data = {}

    for ticker in tickers:
        df = get_historical_market_cap(ticker, api_token, from_date, to_date)
        all_data[ticker] = df.set_index('date')['value_billions']

    # Combine into single DataFrame
    comparison_df = pd.DataFrame(all_data)

    return comparison_df

# Usage
tickers = ['AAPL.US', 'MSFT.US', 'GOOGL.US', 'AMZN.US', 'META.US']
comparison = compare_market_caps(tickers, 'your_api_token', '2023-01-01', '2023-12-31')

# Plot comparison
plt.figure(figsize=(14, 8))
for ticker in comparison.columns:
    plt.plot(comparison.index, comparison[ticker], label=ticker, linewidth=2)

plt.title('FAANG Market Capitalization Comparison (2023)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Market Cap (Billions USD)', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Rankings
print("\nCurrent Market Cap Rankings:")
latest = comparison.iloc[-1].sort_values(ascending=False)
for i, (ticker, value) in enumerate(latest.items(), 1):
    print(f"{i}. {ticker}: ${value:.2f}B")
```

---

### 3. Calculate Growth Rates

**Objective**: Calculate week-over-week and year-over-year growth rates.

```python
def calculate_growth_rates(ticker, api_token, from_date, to_date):
    """Calculate various growth rate metrics."""
    df = get_historical_market_cap(ticker, api_token, from_date, to_date)

    # Week-over-week growth
    df['wow_growth_pct'] = df['value'].pct_change() * 100

    # Year-over-year growth (52 weeks)
    df['yoy_growth_pct'] = df['value'].pct_change(periods=52) * 100

    # Cumulative growth from start
    df['cumulative_growth_pct'] = ((df['value'] / df['value'].iloc[0]) - 1) * 100

    return df

# Usage
df = calculate_growth_rates('AAPL.US', 'your_api_token', '2020-01-01', '2023-12-31')

# Summary statistics
print("Growth Rate Statistics:")
print(f"Average Weekly Growth: {df['wow_growth_pct'].mean():.2f}%")
print(f"Weekly Growth Volatility: {df['wow_growth_pct'].std():.2f}%")
print(f"Best Week: {df['wow_growth_pct'].max():.2f}%")
print(f"Worst Week: {df['wow_growth_pct'].min():.2f}%")
print(f"Total Cumulative Growth: {df['cumulative_growth_pct'].iloc[-1]:.2f}%")

# Plot growth rates
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# Market Cap
ax1.plot(df['date'], df['value_billions'], linewidth=2, color='blue')
ax1.set_title('Market Capitalization', fontsize=14)
ax1.set_ylabel('Market Cap (Billions USD)', fontsize=12)
ax1.grid(True, alpha=0.3)

# Week-over-week growth
ax2.plot(df['date'], df['wow_growth_pct'], linewidth=1, color='green', alpha=0.6)
ax2.axhline(y=0, color='black', linestyle='--', alpha=0.3)
ax2.set_title('Week-over-Week Growth Rate', fontsize=14)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.set_xlabel('Date', fontsize=12)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

### 4. Identify Market Cap Milestones

**Objective**: Find when a company crossed significant market cap milestones.

```python
def find_market_cap_milestones(ticker, api_token, milestones):
    """
    Find dates when company crossed market cap milestones.

    Args:
        milestones: List of milestone values in billions (e.g., [1000, 1500, 2000])
    """
    df = get_historical_market_cap(ticker, api_token, '2019-01-01', '2024-12-31')

    results = []
    for milestone in milestones:
        milestone_value = milestone * 1e9  # Convert billions to raw value

        # Find first date crossing milestone
        crossed = df[df['value'] >= milestone_value]

        if not crossed.empty:
            first_date = crossed.iloc[0]['date']
            first_value = crossed.iloc[0]['value'] / 1e9
            results.append({
                'milestone_billions': milestone,
                'first_crossed': first_date,
                'value_at_cross': first_value
            })

    return pd.DataFrame(results)

# Usage
milestones_df = find_market_cap_milestones(
    'AAPL.US',
    'your_api_token',
    [1000, 1500, 2000, 2500, 3000]
)

print("Market Cap Milestones:")
print(milestones_df.to_string(index=False))

# Example Output:
# milestone_billions  first_crossed  value_at_cross
#               1000     2020-08-13         1999.66
#               1500     2020-12-17         2244.02
#               2000     2021-08-19         2474.97
#               2500     2021-11-11         2564.22
#               3000     2022-01-06         3019.48
```

---

### 5. Sector Market Cap Analysis

**Objective**: Compare total market cap across sectors.

```python
def sector_market_cap_analysis(sector_tickers, api_token, date):
    """
    Analyze total market cap for a sector on a specific date.

    Args:
        sector_tickers: Dict mapping ticker to company name
        date: Analysis date in YYYY-MM-DD format
    """
    sector_data = []

    for ticker, name in sector_tickers.items():
        df = get_historical_market_cap(
            ticker,
            api_token,
            from_date=date,
            to_date=date
        )

        if not df.empty:
            sector_data.append({
                'ticker': ticker,
                'company': name,
                'market_cap_billions': df['value_billions'].iloc[0]
            })

    sector_df = pd.DataFrame(sector_data)
    sector_df = sector_df.sort_values('market_cap_billions', ascending=False)

    # Calculate statistics
    total_market_cap = sector_df['market_cap_billions'].sum()
    sector_df['sector_share_pct'] = (sector_df['market_cap_billions'] / total_market_cap) * 100

    return sector_df

# Usage - Tech Sector Example
tech_sector = {
    'AAPL.US': 'Apple Inc.',
    'MSFT.US': 'Microsoft Corporation',
    'GOOGL.US': 'Alphabet Inc.',
    'AMZN.US': 'Amazon.com Inc.',
    'META.US': 'Meta Platforms Inc.',
    'NVDA.US': 'NVIDIA Corporation',
    'TSLA.US': 'Tesla Inc.'
}

sector_analysis = sector_market_cap_analysis(tech_sector, 'your_api_token', '2023-12-31')

print("\nTech Sector Market Cap Analysis (2023-12-31):")
print(sector_analysis.to_string(index=False))
print(f"\nTotal Tech Sector Market Cap: ${sector_analysis['market_cap_billions'].sum():.2f}B")
```

---

### 6. Volatility Analysis

**Objective**: Measure market cap volatility as risk indicator.

```python
def market_cap_volatility(ticker, api_token, from_date, to_date):
    """Calculate market cap volatility metrics."""
    df = get_historical_market_cap(ticker, api_token, from_date, to_date)

    # Calculate returns
    df['returns'] = df['value'].pct_change()

    # Volatility metrics
    volatility_weekly = df['returns'].std()
    volatility_annualized = volatility_weekly * (52 ** 0.5)  # Annualize weekly vol

    # Drawdown analysis
    df['cummax'] = df['value'].cummax()
    df['drawdown'] = (df['value'] - df['cummax']) / df['cummax']
    max_drawdown = df['drawdown'].min()

    # Recovery time
    max_dd_date = df.loc[df['drawdown'].idxmin(), 'date']
    recovery_date = df[df['date'] > max_dd_date][df['value'] >= df['cummax']].iloc[0]['date'] if len(df[df['date'] > max_dd_date][df['value'] >= df['cummax']]) > 0 else None

    results = {
        'weekly_volatility': volatility_weekly * 100,
        'annualized_volatility': volatility_annualized * 100,
        'max_drawdown_pct': max_drawdown * 100,
        'max_drawdown_date': max_dd_date,
        'recovery_date': recovery_date
    }

    return results, df

# Usage
vol_stats, df = market_cap_volatility('AAPL.US', 'your_api_token', '2020-01-01', '2023-12-31')

print("Market Cap Volatility Analysis:")
print(f"Weekly Volatility: {vol_stats['weekly_volatility']:.2f}%")
print(f"Annualized Volatility: {vol_stats['annualized_volatility']:.2f}%")
print(f"Maximum Drawdown: {vol_stats['max_drawdown_pct']:.2f}%")
print(f"Max Drawdown Date: {vol_stats['max_drawdown_date']}")
print(f"Recovery Date: {vol_stats['recovery_date']}")
```

---

## Important Notes

### 1. Ticker Format

- **Required Format**: `{SYMBOL}.{EXCHANGE}` for explicit exchange specification
- **US Shorthand**: For US stocks, exchange suffix can be omitted (e.g., `AAPL` instead of `AAPL.US`)
- **Case Sensitivity**: Ticker codes are case-insensitive

### 2. API Call Consumption

- **10 API calls per request** regardless of date range
- Counts toward your daily limit of 100,000 calls across all EODHD APIs
- Plan accordingly when fetching data for multiple tickers

**Example**:
- 1 ticker = 10 calls
- 10 tickers = 100 calls
- 100 tickers = 1,000 calls

### 3. Data Frequency

- **Weekly intervals** - Data points typically on Thursdays or Fridays
- Not daily data - gaps between data points
- Consistent weekly spacing for time-series analysis

### 4. Historical Depth

- **Earliest data**: 2019
- **Latest data**: Current week
- No intraday or daily market cap data

### 5. Geographic Coverage

- **US stocks only** - NYSE and NASDAQ
- International stocks not currently supported
- Cryptocurrencies not supported (may be added in future)

### 6. Data Precision

- Values in **raw dollars** (not millions or billions)
- Convert for readability: `value / 1e9` for billions, `value / 1e12` for trillions
- High precision for large numbers

### 7. Alternative Data Source

- **Fundamentals API** provides quarterly market cap
- More precise for specific quarterly periods
- Updated with financial statements
- Use Fundamentals API for:
  - Current market cap
  - Quarterly snapshots
  - Integration with other fundamental metrics

### 8. Test Access

- API token `demo` works for `AAPL.US` only
- Limited to Apple data for testing
- Sign up for full access to all US stocks

---

## Error Handling

### Common Errors

**1. Invalid Ticker**
```json
{
  "error": "Ticker not found"
}
```
**Solution**: Verify ticker format includes exchange suffix (e.g., `AAPL.US`)

**2. Invalid Date Range**
```json
{
  "error": "Invalid date format"
}
```
**Solution**: Use YYYY-MM-DD format for `from` and `to` parameters

**3. No Data Available**
```json
{}
```
**Solution**:
- Check if ticker has data from 2019
- Verify ticker is US-listed stock
- Try broader date range

**4. API Rate Limit**
```json
{
  "error": "Rate limit exceeded"
}
```
**Solution**:
- Monitor your daily API call usage
- Consider caching historical data
- Upgrade plan if needed

### Python Error Handling Example

```python
import requests

def safe_get_market_cap(ticker, api_token, from_date=None, to_date=None):
    """Fetch market cap data with error handling."""
    url = f"https://eodhd.com/api/historical-market-cap/{ticker}"
    params = {"api_token": api_token, "fmt": "json"}

    if from_date:
        params["from"] = from_date
    if to_date:
        params["to"] = to_date

    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()

        if not data:
            print(f"Warning: No data available for {ticker}")
            return None

        if "error" in data:
            print(f"API Error: {data['error']}")
            return None

        return data

    except requests.exceptions.Timeout:
        print(f"Timeout error for {ticker}")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

    except ValueError:
        print(f"Invalid JSON response for {ticker}")
        return None

# Usage
data = safe_get_market_cap('AAPL.US', 'your_api_token', '2023-01-01', '2023-12-31')
if data:
    print(f"Retrieved {len(data)} data points")
```

---

## Best Practices

### 1. Caching Historical Data

Historical data doesn't change, so cache it to save API calls:

```python
import os
import json
from datetime import datetime

def get_cached_market_cap(ticker, api_token, from_date, to_date, cache_dir='cache'):
    """Fetch with caching to save API calls."""
    os.makedirs(cache_dir, exist_ok=True)

    cache_file = f"{cache_dir}/{ticker}_{from_date}_{to_date}.json"

    # Check cache
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            print(f"Loading from cache: {cache_file}")
            return json.load(f)

    # Fetch from API
    data = safe_get_market_cap(ticker, api_token, from_date, to_date)

    if data:
        # Save to cache
        with open(cache_file, 'w') as f:
            json.dump(data, f)
        print(f"Saved to cache: {cache_file}")

    return data
```

### 2. Batch Processing

When analyzing multiple tickers, process efficiently:

```python
import time

def batch_fetch_market_caps(tickers, api_token, from_date, to_date, delay=0.1):
    """Fetch market cap for multiple tickers with rate limiting."""
    results = {}

    for i, ticker in enumerate(tickers, 1):
        print(f"Fetching {i}/{len(tickers)}: {ticker}")

        data = get_cached_market_cap(ticker, api_token, from_date, to_date)
        results[ticker] = data

        # Rate limiting
        if i < len(tickers):
            time.sleep(delay)

    return results
```

### 3. Data Validation

Always validate data before analysis:

```python
def validate_market_cap_data(data):
    """Validate market cap data quality."""
    if not data:
        return False, "No data received"

    if isinstance(data, dict) and "error" in data:
        return False, f"API error: {data['error']}"

    # Check for reasonable values
    df = pd.DataFrame.from_dict(data, orient='index')

    if df.empty:
        return False, "Empty dataframe"

    if df['value'].min() <= 0:
        return False, "Contains non-positive values"

    # Check for unreasonable jumps (>50% week-over-week)
    returns = df['value'].pct_change()
    if returns.abs().max() > 0.5:
        return False, "Unrealistic weekly changes detected"

    return True, "Data validated successfully"
```

### 4. Convert to Standard Units

Always convert to billions or trillions for readability:

```python
def format_market_cap(value):
    """Format market cap value with appropriate units."""
    if value >= 1e12:
        return f"${value/1e12:.2f}T"
    elif value >= 1e9:
        return f"${value/1e9:.2f}B"
    elif value >= 1e6:
        return f"${value/1e6:.2f}M"
    else:
        return f"${value:,.0f}"

# Usage
print(format_market_cap(1357426280000))  # Output: $1.36T
```

### 5. Combine with Other APIs

Combine market cap with price data for comprehensive analysis:

```python
def enhanced_analysis(ticker, api_token):
    """Combine market cap with price data."""
    # Get market cap
    market_cap = get_historical_market_cap(ticker, api_token, '2023-01-01', '2023-12-31')

    # Get price data (from EOD Historical API)
    prices = requests.get(
        f"https://eodhd.com/api/eod/{ticker}",
        params={"api_token": api_token, "from": "2023-01-01", "to": "2023-12-31", "fmt": "json"}
    ).json()

    # Merge and analyze
    # ... combine datasets for price vs market cap analysis
```

---

## Related APIs

Enhance your analysis by combining with other EODHD endpoints:

1. **Fundamentals API** - Quarterly market cap, financial statements, ratios
2. **End-of-Day Historical Data API** - Price data to calculate shares outstanding
3. **Live Stock Prices API** - Real-time price for current market cap estimation
4. **Calendar API** - Earnings dates to correlate with market cap changes
5. **Technical Indicators API** - Technical analysis on market cap as time series

---

## Frequently Asked Questions

**Q: Why weekly data instead of daily?**
A: Weekly frequency provides sufficient granularity for long-term trend analysis while keeping data volume manageable. For daily market cap, calculate from price × shares outstanding using EOD price API and Fundamentals API.

**Q: How is market cap calculated?**
A: Market Cap = Stock Price × Total Shares Outstanding. This API provides pre-calculated weekly snapshots.

**Q: Can I get data before 2019?**
A: No, historical depth starts from 2019. For earlier data, use Fundamentals API quarterly data or calculate from historical prices and shares outstanding.

**Q: Why use this instead of Fundamentals API?**
A:
- **This API**: Weekly frequency, optimized for trend analysis
- **Fundamentals API**: Quarterly, more precise, includes other financial metrics
- **Use both**: Weekly trends + quarterly precision = comprehensive analysis

**Q: Does this include all US stocks?**
A: Yes, all stocks listed on NYSE and NASDAQ with available data from 2019 onwards.

**Q: How often is data updated?**
A: Weekly. New data points added each week for the previous week.

**Q: Can I get international stocks?**
A: Currently US only (NYSE/NASDAQ). International coverage may be added in future.

---

## Support and Documentation

- **API Documentation**: https://eodhd.com/financial-apis/historical-market-capitalization-api
- **Support**: Contact EODHD support for technical issues
- **Community**: Join EODHD community forums for discussions
- **Rate Limits**: Monitor usage in your dashboard

---

**Last Updated**: 2024-11-27
**API Version**: EODHD Historical Market Capitalization API v1
**Data Coverage**: US Stocks (NYSE, NASDAQ) from 2019 onwards

## HTTP Status Codes

The API returns standard HTTP status codes to indicate success or failure:

| Status Code | Meaning | Description |
|-------------|---------|-------------|
| **200** | OK | Request succeeded. Data returned successfully. |
| **402** | Payment Required | API limit used up. Upgrade plan or wait for limit reset. |
| **403** | Unauthorized | Invalid API key. Check your `api_token` parameter. |
| **429** | Too Many Requests | Exceeded rate limit (requests per minute). Slow down requests. |

### Error Response Format

When an error occurs, the API returns a JSON response with error details:

```json
{
  "error": "Error message description",
  "code": 403
}
```

### Handling Errors

**Python Example**:
```python
import requests

def make_api_request(url, params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises HTTPError for bad status codes
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 402:
            print("Error: API limit exceeded. Please upgrade your plan.")
        elif e.response.status_code == 403:
            print("Error: Invalid API key. Check your credentials.")
        elif e.response.status_code == 429:
            print("Error: Rate limit exceeded. Please slow down your requests.")
        else:
            print(f"HTTP Error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
```

**Best Practices**:
- Always check status codes before processing response data
- Implement exponential backoff for 429 errors
- Cache responses to reduce API calls
- Monitor your API usage in the user dashboard
