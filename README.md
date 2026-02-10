# EODHD Skills Adapter for Claude/Codex

Reusable skills and adapters for using the [EOD Historical Data (EODHD) API](https://eodhd.com/) from Claude- and Codex-style agent workflows.

## Table of Contents

- [Installation](#installation)
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Repository Structure](#repository-structure)
- [Quick Start](#quick-start)
- [Supported Endpoints](#supported-endpoints)
- [Usage Examples](#usage-examples)
- [Workflows](#workflows)
- [Development Status](#development-status)
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
- **Endpoint documentation** for 50+ EODHD API endpoints
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
│       │   ├── endpoints.md      # Endpoint catalog overview
│       │   ├── endpoints/        # Individual endpoint docs (57 files)
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

## Supported Endpoints

### Python Client (Built-in)

| Endpoint | Description | Symbol Required |
|----------|-------------|-----------------|
| `eod` | End-of-day historical OHLCV | Yes (e.g., AAPL.US) |
| `intraday` | Intraday price bars | Yes |
| `fundamentals` | Company fundamentals | Yes |
| `exchange-symbol-list` | List symbols on exchange | Yes (exchange code, e.g., US) |
| `screener` | Stock screener | No |

### Documented Endpoints (57 total)

The `skills/eodhd-api/references/endpoints/` directory contains documentation for:

| Category | Endpoints |
|----------|-----------|
| Market Data | Historical prices, intraday, live data, technical indicators |
| Fundamentals | Company data, news, insider transactions, sentiment |
| Options | US options contracts, EOD data, underlyings |
| Economic | Events, earnings, IPOs, splits, dividends |
| ESG | Investverte ESG data by company/country/sector |
| Banking/Bonds | Praams bank data, bond analysis, risk scoring |
| Exchange/Index | Exchange listings, index components, CBOE data |
| Advanced Analytics | Illio market insights, performance, risk analysis |

See `skills/eodhd-api/references/endpoints/README.md` for the complete index.

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

## Development Status

### Current Release (v0.0.3)

- Historical/end-of-day data retrieval
- Intraday data retrieval
- Fundamentals/exchange/screener access
- Consistent, auditable output format
- 57 endpoint documentation stubs

### Roadmap

- [ ] Complete documentation for all endpoint stubs
- [ ] Add more endpoints to Python client
- [ ] Schema validation for API responses
- [ ] Factor libraries for common calculations
- [ ] Caching and retry strategies
- [ ] Notebook/report generation

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
