# Skill: eodhd-api

## Purpose

Use EODHD market data APIs to fetch, normalize, and summarize financial data including:
- Prices (historical, intraday, real-time)
- Company fundamentals and financial statements
- Options data with Greeks
- Technical indicators
- News and sentiment
- Macro-economic indicators
- Corporate events (dividends, splits, earnings, IPOs)

Supports equities, ETFs, indices, forex, crypto, and bonds across 70+ exchanges worldwide.

## Trigger

Use this skill when the user asks for any of the following:
- End-of-day or historical stock/ETF/index prices
- Intraday price bars (1m, 5m, 1h intervals)
- Real-time quotes (delayed 15-20 minutes)
- Company fundamentals, financials, or valuation metrics
- Options chains, Greeks, or options analytics
- Technical indicators (SMA, EMA, RSI, MACD, Bollinger Bands, etc.)
- Company news or market sentiment
- Stock screening by fundamental/technical criteria
- Exchange listings or market metadata
- Macro-economic indicators (GDP, inflation, unemployment)
- Corporate calendar events (earnings, dividends, splits, IPOs)
- Bulk data exports for an exchange

## Required inputs

- `EODHD_API_TOKEN` — environment variable containing your API key
- Instrument identifier in EODHD format: `{TICKER}.{EXCHANGE}` (e.g., `AAPL.US`, `BMW.XETRA`)
- Date range (`--from-date`, `--to-date`) for time-series requests
- Endpoint-specific parameters (e.g., `--function` for technical indicators)

## Workflow

1. **Clarify the request**
   - Identify objective: price analysis, screening, fundamentals, event study, etc.
   - Confirm symbol(s), date range, and specific metrics needed
   - Determine output format (tables, charts, summary)

2. **Select endpoint(s)**
   - Reference `references/endpoints.md` or `references/endpoints/` for endpoint specs
   - Choose minimal set of endpoints to satisfy the request
   - Consider endpoint-specific parameters

3. **Execute API calls**
   - Use `scripts/eodhd_client.py` for supported endpoints
   - For unsupported endpoints, construct curl commands per endpoint docs
   - Handle pagination for large result sets

4. **Validate response**
   - Confirm symbol exists and has data for requested range
   - Check for null/missing fields
   - Verify date coverage is adequate

5. **Process and present**
   - Transform data as needed (calculate returns, ratios, etc.)
   - Use `templates/analysis_report.md` for structured output
   - Include tables for comparisons, bullet points for conclusions

6. **Document reproducibility**
   - Include exact commands used
   - Note any data limitations or caveats
   - Provide token-redacted curl examples

## Supported endpoints (Python client)

| Endpoint | Description | Key Parameters |
|----------|-------------|----------------|
| `eod` | Historical OHLCV | `--symbol`, `--from-date`, `--to-date` |
| `intraday` | Intraday bars | `--symbol`, `--interval` (1m/5m/1h) |
| `real-time` | Live quotes | `--symbol` |
| `fundamentals` | Company data | `--symbol` |
| `news` | Financial news | `--symbol`, `--limit` |
| `technical` | Technical indicators | `--symbol`, `--function`, `--period` |
| `options` | Options chains | `--symbol` |
| `dividends` | Dividend history | `--symbol` |
| `splits` | Stock splits | `--symbol` |
| `macro-indicator` | Macro data | `--symbol` (country code), `--indicator` |
| `screener` | Stock screener | `--limit`, `--offset` |
| `calendar/earnings` | Earnings calendar | `--from-date`, `--to-date` |
| `calendar/ipos` | IPO calendar | `--from-date`, `--to-date` |
| `economic-events` | Economic events | `--from-date`, `--to-date` |
| `exchange-symbol-list` | Exchange tickers | `--symbol` (exchange code) |
| `exchanges-list` | All exchanges | (no symbol needed) |
| `eod-bulk-last-day` | Bulk EOD data | `--symbol` (exchange code) |

## Output requirements

- **State exact parameters**: symbols, date ranges, endpoints used
- **Separate facts from interpretation**: clearly distinguish API data from analysis
- **Note limitations**: mention missing fields, null values, date gaps
- **Use appropriate formats**:
  - Tables for multi-symbol comparisons
  - Bullet points for conclusions and insights
  - JSON/code blocks for raw data samples
- **Include reproducible commands**: token-redacted curl or client commands

## Guardrails

- **Never fabricate data**: if retrieval fails, report the error and command attempted
- **Validate before acting**: confirm symbol exists before making multiple calls
- **Respect rate limits**: avoid unnecessary duplicate requests
- **Handle errors gracefully**: provide actionable error messages
- **Warn on large requests**: ask for confirmation before broad multi-exchange pulls

## Common patterns

See `references/workflows.md` for detailed recipes:

1. **Single-ticker deep dive**: EOD + fundamentals + news
2. **Peer comparison**: Screener + fundamentals for multiple symbols
3. **Event study**: Intraday bars around earnings/announcements
4. **Macro context**: Stock performance vs. economic indicators
5. **Technical analysis**: Price data + indicators (SMA, RSI, MACD)
6. **Options analysis**: Options chains + Greeks for strategy evaluation

## Example commands

```bash
# Historical prices
python eodhd_client.py --endpoint eod --symbol AAPL.US --from-date 2025-01-01 --to-date 2025-01-31

# Company fundamentals
python eodhd_client.py --endpoint fundamentals --symbol MSFT.US

# 50-day SMA
python eodhd_client.py --endpoint technical --symbol NVDA.US --function sma --period 50

# Company news
python eodhd_client.py --endpoint news --symbol TSLA.US --limit 10

# US inflation data
python eodhd_client.py --endpoint macro-indicator --symbol USA --indicator inflation_consumer_prices_annual

# Stock screener
python eodhd_client.py --endpoint screener --limit 20
```

## References

- Endpoint catalog: `references/endpoints.md`
- Individual endpoint docs: `references/endpoints/*.md`
- Analysis workflows: `references/workflows.md`
- Output template: `templates/analysis_report.md`
