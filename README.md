# EODHD Skills Adapter for Claude/Codex

Reusable skills and adapters for using the [EOD Historical Data (EODHD) API](https://eodhd.com/) from Claude- and Codex-style agent workflows.

> **Disclaimer**: This skill set may differ from actual EODHD API endpoints and behavior, both due to possible errors and contradictions in the documentation and because the API is constantly changing and evolving. Furthermore, Claude and the Codex may interpret the information provided incorrectly. Some data, such as update times, is empirical in nature and is provided for guidance only. For any questions, please email supportlevel1@eodhistoricaldata.com

## Table of Contents

- [Installation](#installation)
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Repository Structure](#repository-structure)
- [Quick Start](#quick-start)
- [Usage Tips](#usage-tips)
- [Supported Endpoints](#supported-endpoints)
- [General Reference Documentation](#general-reference-documentation)
- [Usage Examples](#usage-examples)
- [Workflows](#workflows)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Claude Code (Plugin System)

```bash
# Register the marketplace
/plugin marketplace add Enlavan/eodhd-claude-skills

# Install the plugin
/plugin install eodhd-api@eodhd-claude-skills
```

**Manage the plugin:**

```bash
/plugin update eodhd-api@eodhd-claude-skills      # Update to latest version
/plugin enable eodhd-api@eodhd-claude-skills       # Enable
/plugin disable eodhd-api@eodhd-claude-skills      # Disable
/plugin uninstall eodhd-api@eodhd-claude-skills    # Uninstall
```

### Manual Setup

Clone the repository and set your API token:

```bash
git clone https://github.com/Enlavan/eodhd-claude-skills.git
export EODHD_API_TOKEN="your_token_here"
```

## Overview

This repository provides a skill adapter that enables AI agents (Claude, Codex, etc.) to interact with the EODHD financial data API. It includes:

- **Skill definitions** with trigger conditions, workflows, and output standards
- **Endpoint documentation** for 72 EODHD API endpoints
- **General reference guides** covering 28 topics (exchanges, symbol format, rate limits, fundamentals, etc.)
- **A lightweight Python client** (stdlib-only, no external dependencies)
- **Analysis templates** for consistent, auditable output
- **Adapter guides** for different AI environments

## Prerequisites

1. **EODHD API Token**: Get one at [eodhd.com](https://eodhd.com/)
2. **Python 3.8+** (for the helper client)
3. No external Python packages required (stdlib-only)

## Repository Structure

```
eodhd-claude-skills/
├── .claude-plugin/
│   └── marketplace.json          # Plugin manifest for Claude Code
├── .github/
│   └── workflows/
│       └── release.yml           # Auto-release on version bump
├── skills/
│   └── eodhd-api/
│       ├── SKILL.md              # Primary skill definition
│       ├── references/
│       │   ├── general/          # General reference guides (28 files)
│       │   ├── endpoints/        # Individual endpoint docs (72 files)
│       │   └── workflows.md      # Common analysis patterns
│       ├── scripts/
│       │   └── eodhd_client.py   # Lightweight Python API client
│       └── templates/
│           └── analysis_report.md
├── adapters/
│   ├── claude/
│   │   └── eodhd-api.md          # Claude environment adapter
│   └── codex/
│       └── eodhd-api.md          # Codex environment adapter
├── CLAUDE.md                     # Claude Code project context
└── README.md
```

## Quick Start

### 1. Set your API token

```bash
export EODHD_API_TOKEN="your_token_here"
```

> If you installed via the plugin system, the skill is already available in Claude Code. Just set the token and start asking for financial data.

### 2. Use the helper client

```bash
# Get historical prices
python skills/eodhd-api/scripts/eodhd_client.py \
  --endpoint eod \
  --symbol AAPL.US \
  --from-date 2025-01-01 \
  --to-date 2025-01-31

# Get company fundamentals
python skills/eodhd-api/scripts/eodhd_client.py \
  --endpoint fundamentals \
  --symbol MSFT.US

# Get intraday data
python skills/eodhd-api/scripts/eodhd_client.py \
  --endpoint intraday \
  --symbol TSLA.US \
  --interval 5m \
  --from-date 2025-01-15

# List exchange symbols
python skills/eodhd-api/scripts/eodhd_client.py \
  --endpoint exchange-symbol-list \
  --symbol US
```

### 3. Use in agent prompts

```
Use the `eodhd-api` skill. Pull daily prices for NVDA.US from 2025-01-01 to 2025-01-31,
include fundamentals summary, and return a concise analyst report with reproducible calls.
```

## Usage Tips

After installing the skill, Claude Code won't always use it automatically — you may need to nudge it. Here are a few ways to make sure the skill gets picked up:

### Prompt prefix

Start your message with a line like:

```
Use available skills you have access to whenever possible.
Get me AAPL.US daily prices for the last 30 days and summarize the trend.
```

Or reference the skill explicitly:

```
Use the eodhd-api skill. Show me fundamentals for MSFT.US.
```

### Add a project-level instruction

Create or edit a `CLAUDE.md` in your project root and add:

```markdown
Always use available skills (especially `eodhd-api`) when handling financial data requests.
```

Claude Code reads `CLAUDE.md` at the start of every session, so this acts as a persistent hint.

### Add a global instruction

To apply the hint across all projects, add the following to your `~/.claude/CLAUDE.md`:

```markdown
Use available skills whenever they match the task at hand.
```

### Why is this needed?

Claude Code currently treats installed skills as optional context. It will use them when it recognizes a strong match, but for broad or ambiguous requests it may fall back to general knowledge. An explicit mention — either in the prompt or in `CLAUDE.md` — makes the match unambiguous.

## Supported Endpoints

### Python Client (Built-in)

| Endpoint | Description | Symbol Required |
|----------|-------------|-----------------|
| `eod` | End-of-day historical OHLCV | Yes (e.g., AAPL.US) |
| `intraday` | Intraday price bars | Yes |
| `fundamentals` | Company fundamentals | Yes |
| `exchange-symbol-list` | List symbols on exchange | Yes (exchange code, e.g., US) |
| `screener` | Stock screener | No |

See `skills/eodhd-api/SKILL.md` for the full list of client-supported endpoints.

### Documented Endpoints (72 total)

The `skills/eodhd-api/references/endpoints/` directory contains documentation for each endpoint. See `skills/eodhd-api/references/endpoints/README.md` for the complete index.

#### Market Data

| Endpoint | File |
|----------|------|
| Historical Stock Prices (EOD) | `historical-stock-prices.md` |
| Intraday Historical Data | `intraday-historical-data.md` |
| Live Price Data | `live-price-data.md` |
| US Live Extended Quotes | `us-live-extended-quotes.md` |
| WebSockets Real-Time Data | `websockets-realtime.md` |
| Technical Indicators | `technical-indicators.md` |
| Stock Screener Data | `stock-screener-data.md` |
| Stocks From Search | `stocks-from-search.md` |
| Stock Market Logos (PNG) | `stock-market-logos.md` |
| Stock Market Logos (SVG) | `stock-market-logos-svg.md` |
| Historical Market Cap | `historical-market-cap.md` |
| Symbol Change History | `symbol-change-history.md` |

#### Fundamentals & Company Data

| Endpoint | File |
|----------|------|
| Fundamentals Data | `fundamentals-data.md` |
| Bulk Fundamentals | `bulk-fundamentals.md` |
| Company News | `company-news.md` |
| Sentiment Data | `sentiment-data.md` |
| News Word Weights | `news-word-weights.md` |
| Insider Transactions | `insider-transactions.md` |

#### Calendar & Events

| Endpoint | File |
|----------|------|
| Upcoming Earnings | `upcoming-earnings.md` |
| Earnings Trends | `earnings-trends.md` |
| Upcoming Dividends | `upcoming-dividends.md` |
| Upcoming Splits | `upcoming-splits.md` |
| Upcoming IPOs | `upcoming-ipos.md` |
| Economic Events | `economic-events.md` |

#### Exchange & Index Data

| Endpoint | File |
|----------|------|
| Exchanges List | `exchanges-list.md` |
| Exchange Details | `exchange-details.md` |
| Exchange Tickers | `exchange-tickers.md` |
| Index Components | `index-components.md` |
| Indices List | `indices-list.md` |
| CBOE Index Data | `cboe-index-data.md` |
| CBOE Indices List | `cboe-indices-list.md` |

#### Macro & Treasury

| Endpoint | File |
|----------|------|
| Macro Indicator | `macro-indicator.md` |
| US Treasury Bill Rates | `ust-bill-rates.md` |
| US Treasury Long-Term Rates | `ust-long-term-rates.md` |
| US Treasury Yield Rates | `ust-yield-rates.md` |
| US Treasury Real Yield Rates | `ust-real-yield-rates.md` |

#### User & Account

| Endpoint | File |
|----------|------|
| User Details | `user-details.md` |

#### Marketplace: Options

| Endpoint | File |
|----------|------|
| US Options EOD | `us-options-eod.md` |
| US Options Contracts | `us-options-contracts.md` |
| US Options Underlyings | `us-options-underlyings.md` |

#### Marketplace: Tick Data

| Endpoint | File |
|----------|------|
| US Tick Data | `us-tick-data.md` |
| Marketplace Tick Data | `marketplace-tick-data.md` |

#### Marketplace: TradingHours

| Endpoint | File |
|----------|------|
| List All Markets | `tradinghours-list-markets.md` |
| Lookup Markets | `tradinghours-lookup-markets.md` |
| Get Market Details | `tradinghours-market-details.md` |
| Market Status Details | `tradinghours-market-status.md` |

#### Marketplace: Illio Analytics

| Endpoint | File |
|----------|------|
| Market Insights — Best/Worst | `illio-market-insights-best-worst.md` |
| Market Insights — Beta Bands | `illio-market-insights-beta-bands.md` |
| Market Insights — Largest Volatility | `illio-market-insights-largest-volatility.md` |
| Market Insights — Performance | `illio-market-insights-performance.md` |
| Market Insights — Risk Return | `illio-market-insights-risk-return.md` |
| Market Insights — Volatility | `illio-market-insights-volatility.md` |
| Performance Insights | `illio-performance-insights.md` |
| Risk Insights | `illio-risk-insights.md` |

#### Marketplace: Investverte ESG

| Endpoint | File |
|----------|------|
| List Companies | `investverte-esg-list-companies.md` |
| List Countries | `investverte-esg-list-countries.md` |
| List Sectors | `investverte-esg-list-sectors.md` |
| View Company | `investverte-esg-view-company.md` |
| View Country | `investverte-esg-view-country.md` |
| View Sector | `investverte-esg-view-sector.md` |

#### Marketplace: PRAAMS

| Endpoint | File |
|----------|------|
| Bank Balance Sheet (by ISIN) | `praams-bank-balance-sheet-by-isin.md` |
| Bank Balance Sheet (by Ticker) | `praams-bank-balance-sheet-by-ticker.md` |
| Bank Income Statement (by ISIN) | `praams-bank-income-statement-by-isin.md` |
| Bank Income Statement (by Ticker) | `praams-bank-income-statement-by-ticker.md` |
| Bond Analyze (by ISIN) | `praams-bond-analyze-by-isin.md` |
| Multi-Factor Bond Report (by ISIN) | `praams-report-bond-by-isin.md` |
| Multi-Factor Equity Report (by ISIN) | `praams-report-equity-by-isin.md` |
| Multi-Factor Equity Report (by Ticker) | `praams-report-equity-by-ticker.md` |
| Risk Scoring (by ISIN) | `praams-risk-scoring-by-isin.md` |
| Risk Scoring (by Ticker) | `praams-risk-scoring-by-ticker.md` |
| Smart Investment Screener — Bond | `praams-smart-investment-screener-bond.md` |
| Smart Investment Screener — Equity | `praams-smart-investment-screener-equity.md` |

## General Reference Documentation

The `skills/eodhd-api/references/general/` directory contains 28 reference guides:

### Essential

| Guide | Description |
|-------|-------------|
| `authentication.md` | API tokens, security, protocols, CORS, environment setup |
| `symbol-format.md` | Ticker format rules, exchange codes, special characters |
| `exchanges.md` | Supported exchanges (70+), trading hours, coverage |
| `rate-limits.md` | API quotas, rate limiting, Marketplace limits, optimization |
| `update-times.md` | Data refresh schedules by data type and exchange |

### Fundamentals

| Guide | Description |
|-------|-------------|
| `fundamentals-api.md` | Complete guide to fundamentals, ETFs, funds, indices |
| `fundamentals-common-stock.md` | Common stock fundamentals structure |
| `fundamentals-etf.md` | ETF fundamentals and holdings |
| `fundamentals-etf-metrics.md` | ETF-specific metrics and calculations |
| `fundamentals-fund.md` | Mutual fund data structure |
| `fundamentals-crypto-currency.md` | Cryptocurrency and forex fundamentals |
| `fundamentals-ratios.md` | Financial ratios documentation |
| `fundamentals-faq.md` | Common fundamentals questions and answers |

### Asset Class Notes

| Guide | Description |
|-------|-------------|
| `forex-data-notes.md` | Forex market hours, EOD definition, volume |
| `crypto-data-notes.md` | Crypto data sources, volume, price discrepancies |
| `indices-data-notes.md` | Index access, live data, historical components |

### Ticker & Exchange Guides

| Guide | Description |
|-------|-------------|
| `stock-types-ticker-suffixes-guide.md` | Ticker suffixes, share classes, preferred shares |
| `special-exchanges-guide.md` | Special exchange codes (FOREX, CC, GBOND, INDX, etc.) |
| `primary-tickers-guide.md` | Primary ticker identification for ADRs and dual listings |
| `delisted-tickers-guide.md` | Working with delisted and historical tickers |

### Data & Calculations

| Guide | Description |
|-------|-------------|
| `data-adjustment-guide.md` | Split/dividend adjustments for price data |
| `financial-ratios-calculation-guide.md` | How financial ratios are calculated |
| `general-data-faq.md` | ISINs, data formats, adjusted close, error codes, etc. |

### Platform

| Guide | Description |
|-------|-------------|
| `pricing-and-plans.md` | Subscription tiers, WebSocket limits, Marketplace |
| `sdks-and-integrations.md` | Official SDKs, MCP Server, third-party tools |
| `versioning.md` | API stability guarantees, backwards compatibility |
| `api-authentication-demo-access.md` | Demo token access and limitations |
| `glossary.md` | Financial, technical, and EODHD-specific terms |

## Usage Examples

### Historical Price Analysis

```bash
# Get AAPL prices for Q1 2025
python skills/eodhd-api/scripts/eodhd_client.py \
  --endpoint eod \
  --symbol AAPL.US \
  --from-date 2025-01-01 \
  --to-date 2025-03-31
```

### Compare Multiple Symbols

```bash
# Pull data for comparison (run separately, combine in analysis)
for symbol in AAPL.US MSFT.US GOOGL.US; do
  python skills/eodhd-api/scripts/eodhd_client.py \
    --endpoint eod \
    --symbol $symbol \
    --from-date 2025-01-01 \
    --to-date 2025-01-31 > "${symbol}.json"
done
```

### Fundamentals Snapshot

```bash
python skills/eodhd-api/scripts/eodhd_client.py \
  --endpoint fundamentals \
  --symbol NVDA.US | jq '.Highlights'
```

## Workflows

The skill supports four primary analysis patterns (see `skills/eodhd-api/references/workflows.md`):

1. **Historical + Fundamentals Snapshot**: Single-ticker deep dive with valuation metrics
2. **Cross-sectional Screener**: Filter universe, rank by criteria, present shortlist
3. **Event Window Analysis**: Intraday bars around specific events (earnings, announcements)
4. **Macro Overlay**: Align instrument data with macro indicators for co-movement analysis

## Contributing

Contributions are welcome! Priority areas:

1. **Fill in TBD endpoint stubs** in `skills/eodhd-api/references/endpoints/`
2. **Expand Python client** with additional endpoint support
3. **Add example workflows** for specific use cases
4. **Improve documentation** with real-world examples

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

TBD - License information to be added.

---

**Note**: This project is not officially affiliated with EODHD. Use the EODHD API in accordance with their [terms of service](https://eodhd.com/terms-of-use).
