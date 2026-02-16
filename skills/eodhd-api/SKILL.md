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
- US Treasury interest rates (bill rates, long-term rates, yield curves, real yield curves)

Supports equities, ETFs, indices, forex, crypto, and bonds across 70+ exchanges worldwide.

## Trigger

Use this skill when the user asks for any of the following:
- End-of-day or historical stock/ETF/index prices
- Intraday price bars (1m, 5m, 1h intervals)
- Real-time quotes (delayed 15-20 minutes) or extended US stock quotes with bid/ask
- Company fundamentals, financials, or valuation metrics
- Options chains, Greeks, or options analytics
- Technical indicators (SMA, EMA, RSI, MACD, Bollinger Bands, etc.)
- Company news or market sentiment
- Stock screening by fundamental/technical criteria
- Exchange listings or market metadata
- Macro-economic indicators (GDP, inflation, unemployment)
- Corporate calendar events (earnings, dividends, splits, IPOs)
- Insider trading activity (executive purchases, sales)
- Bulk data exports for an exchange
- US Treasury interest rates, bill rates, yield curves, or real yield curves

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
| `news` | Financial news with sentiment | `--symbol`, `--limit`, `--from-date` |
| `sentiment` | Daily sentiment scores | `--symbol`, `--from-date`, `--to-date` |
| `news-word-weights` | Trending topics in news | `--symbol`, `--from-date`, `--to-date`, `--limit` |
| `technical` | Technical indicators | `--symbol`, `--function`, `--period` |
| `options` | Options chains | `--symbol` |
| `dividends` | Dividend history | `--symbol` |
| `splits` | Stock splits | `--symbol` |
| `macro-indicator` | Macro data | `--symbol` (country code), `--indicator` |
| `screener` | Stock screener | `--limit`, `--offset` |
| `calendar/earnings` | Earnings calendar | `--from-date`, `--to-date` or `--symbol` |
| `calendar/trends` | Earnings trends | `--symbol` (comma-separated) |
| `calendar/ipos` | IPO calendar | `--from-date`, `--to-date` |
| `calendar/splits` | Stock splits calendar | `--from-date`, `--to-date` or `--symbol` |
| `calendar/dividends` | Dividends calendar | `--symbol` |
| `economic-events` | Economic events | `--from-date`, `--to-date` |
| `insider-transactions` | Insider trading activity | `--symbol`, `--from-date`, `--to-date`, `--limit` |
| `exchange-symbol-list` | Exchange tickers | `--symbol` (exchange code) |
| `exchanges-list` | All exchanges | (no symbol needed) |
| `eod-bulk-last-day` | Bulk EOD data | `--symbol` (exchange code) |
| `bulk-fundamentals` | Bulk fundamentals for exchange | `--symbol` (exchange code), `--symbols`, `--limit`, `--offset`, `--version` |
| `user` | Account details and API usage | (no parameters needed) |
| `us-quote-delayed` | US extended quotes (Live v2) | `--symbol` (comma-separated for batch) |
| `ust/bill-rates` | US Treasury Bill Rates | `--filter-year` |
| `ust/long-term-rates` | US Treasury Long-Term Rates | `--filter-year` |
| `ust/yield-rates` | US Treasury Par Yield Curve Rates | `--filter-year` |
| `ust/real-yield-rates` | US Treasury Par Real Yield Curve Rates | `--filter-year` |

**API call costs**: Most endpoints cost 1 call. `technical` and `intraday` cost 5 calls. `fundamentals` and `options` cost 10 calls. News-related endpoints (`news`, `sentiment`, `news-word-weights`) cost 5 calls + 5 per ticker. Bulk endpoints cost 100 calls (+ N symbols if `--symbols` used). See `references/general/rate-limits.md` for full details.

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

# Company news with sentiment
python eodhd_client.py --endpoint news --symbol TSLA.US --limit 10

# Daily sentiment scores
python eodhd_client.py --endpoint sentiment --symbol AAPL.US --from-date 2025-01-01 --to-date 2025-01-31

# Trending topics in news (word weights)
python eodhd_client.py --endpoint news-word-weights --symbol AAPL.US --from-date 2025-01-01 --to-date 2025-01-15 --limit 20

# US inflation data
python eodhd_client.py --endpoint macro-indicator --symbol USA --indicator inflation_consumer_prices_annual

# Stock screener
python eodhd_client.py --endpoint screener --limit 20

# Insider transactions
python eodhd_client.py --endpoint insider-transactions --symbol AAPL.US --from-date 2025-01-01 --limit 50

# Upcoming IPOs
python eodhd_client.py --endpoint calendar/ipos --from-date 2025-01-01 --to-date 2025-03-31

# Stock splits calendar
python eodhd_client.py --endpoint calendar/splits --from-date 2025-01-01 --to-date 2025-01-31

# Bulk fundamentals for an exchange (first 100)
python eodhd_client.py --endpoint bulk-fundamentals --symbol NASDAQ --limit 100

# Bulk fundamentals for specific symbols
python eodhd_client.py --endpoint bulk-fundamentals --symbol NASDAQ --symbols AAPL.US,MSFT.US

# User account details and API usage
python eodhd_client.py --endpoint user

# US extended quote (Live v2)
python eodhd_client.py --endpoint us-quote-delayed --symbol AAPL.US,TSLA.US

# US Treasury Bill Rates for 2012
python eodhd_client.py --endpoint ust/bill-rates --filter-year 2012 --limit 100

# US Treasury Long-Term Rates for 2020
python eodhd_client.py --endpoint ust/long-term-rates --filter-year 2020

# US Treasury Yield Curve for 2023
python eodhd_client.py --endpoint ust/yield-rates --filter-year 2023

# US Treasury Real Yield Curve for 2024
python eodhd_client.py --endpoint ust/real-yield-rates --filter-year 2024
```

## References

### General Documentation
- **Getting Started**: `references/general/README.md` - Start here for setup and basics
- **Authentication**: `references/general/authentication.md` - API tokens, protocols (HTTPS/HTTP), CORS, security
- **Symbol Format**: `references/general/symbol-format.md` - How to format tickers correctly
- **Exchanges**: `references/general/exchanges.md` - Complete list of 70+ exchanges, coverage gaps
- **Update Times**: `references/general/update-times.md` - When data is refreshed
- **Rate Limits**: `references/general/rate-limits.md` - Quotas (~17 req/sec), optimization, error codes
- **Fundamentals API**: `references/general/fundamentals-api.md` - Complete guide to company fundamentals, ETFs, funds, and indices
- **Pricing & Plans**: `references/general/pricing-and-plans.md` - Subscription tiers, WebSocket limits, marketplace
- **SDKs & Integrations**: `references/general/sdks-and-integrations.md` - Official Python/.NET/R SDKs, MCP Server, tools
- **Versioning**: `references/general/versioning.md` - API stability guarantees, backwards-compatibility
- **Glossary**: `references/general/glossary.md` - Financial, technical, and EODHD-specific terms

### Endpoint Documentation
- **Endpoint catalog**: `references/endpoints.md` - Overview of all endpoints
- **Individual endpoint docs**: `references/endpoints/*.md` - Detailed specs per endpoint
- **Analysis workflows**: `references/workflows.md` - Common usage patterns
- **Output template**: `templates/analysis_report.md` - Structured report format
