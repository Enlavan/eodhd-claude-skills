#!/usr/bin/env python3
"""Minimal EODHD API client helper (stdlib-only).

Examples:
  # End-of-day prices
  python eodhd_client.py --endpoint eod --symbol AAPL.US --from-date 2025-01-01 --to-date 2025-01-31

  # Fundamentals
  python eodhd_client.py --endpoint fundamentals --symbol AAPL.US

  # Intraday data
  python eodhd_client.py --endpoint intraday --symbol AAPL.US --interval 5m --from-date 2025-01-15

  # Real-time quote
  python eodhd_client.py --endpoint real-time --symbol AAPL.US

  # Company news
  python eodhd_client.py --endpoint news --symbol AAPL.US --limit 10

  # Dividends
  python eodhd_client.py --endpoint dividends --symbol AAPL.US --from-date 2020-01-01

  # Earnings
  python eodhd_client.py --endpoint calendar/earnings --from-date 2025-01-01 --to-date 2025-01-31

  # Technical indicators
  python eodhd_client.py --endpoint technical --symbol AAPL.US --function sma --period 50

  # Macro indicators
  python eodhd_client.py --endpoint macro-indicator --symbol USA --indicator inflation_consumer_prices_annual

  # Options data
  python eodhd_client.py --endpoint options --symbol AAPL.US

  # Exchanges list
  python eodhd_client.py --endpoint exchanges-list

  # Bulk EOD data for exchange
  python eodhd_client.py --endpoint eod-bulk-last-day --symbol US
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request

BASE_URL = "https://eodhd.com/api"

# Endpoints that don't require a symbol
NO_SYMBOL_ENDPOINTS = {
    "screener",
    "exchanges-list",
    "calendar/earnings",
    "calendar/ipos",
    "calendar/splits",
    "economic-events",
}

# Endpoints where --symbol means exchange code, not ticker
EXCHANGE_CODE_ENDPOINTS = {
    "exchange-symbol-list",
    "eod-bulk-last-day",
}


class ClientError(RuntimeError):
    """Raised when user input or API response is invalid."""


def build_path(endpoint: str, symbol: str | None, function: str | None = None) -> str:
    """Build the API path for the given endpoint."""

    # Endpoints that don't need a symbol
    if endpoint in NO_SYMBOL_ENDPOINTS:
        if endpoint == "exchanges-list":
            return "/exchanges-list"
        if endpoint == "calendar/earnings":
            return "/calendar/earnings"
        if endpoint == "calendar/ipos":
            return "/calendar/ipos"
        if endpoint == "calendar/splits":
            return "/calendar/splits"
        if endpoint == "economic-events":
            return "/economic-events"
        if endpoint == "screener":
            return "/screener"
        return f"/{endpoint}"

    # Require symbol for all other endpoints
    if not symbol:
        raise ClientError(f"--symbol is required for endpoint={endpoint}")

    # Simple symbol-based endpoints
    if endpoint == "eod":
        return f"/eod/{symbol}"
    if endpoint == "intraday":
        return f"/intraday/{symbol}"
    if endpoint == "fundamentals":
        return f"/fundamentals/{symbol}"
    if endpoint == "real-time":
        return f"/real-time/{symbol}"
    if endpoint == "dividends":
        return f"/div/{symbol}"
    if endpoint == "splits":
        return f"/splits/{symbol}"
    if endpoint == "news":
        return f"/news"  # news uses 's' param, not path
    if endpoint == "sentiment":
        return f"/sentiments"  # sentiments uses 's' param
    if endpoint == "insider-transactions":
        return f"/insider-transactions"  # uses 'code' param
    if endpoint == "technical":
        if not function:
            raise ClientError("--function is required for endpoint=technical (e.g., sma, ema, rsi)")
        return f"/technical/{symbol}"
    if endpoint == "options":
        return f"/options/{symbol}"
    if endpoint == "macro-indicator":
        return f"/macro-indicator/{symbol}"

    # Exchange code endpoints
    if endpoint == "exchange-symbol-list":
        return f"/exchange-symbol-list/{symbol}"
    if endpoint == "eod-bulk-last-day":
        return f"/eod-bulk-last-day/{symbol}"

    # Index/exchange related
    if endpoint == "exchanges-details":
        return f"/exchanges/{symbol}"
    if endpoint == "index-components":
        return f"/fundamentals/{symbol}"  # index components via fundamentals

    raise ClientError(f"Unsupported endpoint: {endpoint}")


SUPPORTED_ENDPOINTS = [
    # Core market data
    "eod",
    "intraday",
    "real-time",
    "eod-bulk-last-day",
    # Fundamentals & company data
    "fundamentals",
    "news",
    "sentiment",
    "insider-transactions",
    "dividends",
    "splits",
    # Technical analysis
    "technical",
    # Options
    "options",
    # Macro & economic
    "macro-indicator",
    "economic-events",
    # Calendar events
    "calendar/earnings",
    "calendar/ipos",
    "calendar/splits",
    # Exchange/listing
    "exchange-symbol-list",
    "exchanges-list",
    "exchanges-details",
    "index-components",
    # Screening
    "screener",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Query EODHD API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Supported endpoints:
  Market Data:    eod, intraday, real-time, eod-bulk-last-day
  Fundamentals:   fundamentals, news, sentiment, insider-transactions
  Corporate:      dividends, splits
  Technical:      technical (requires --function)
  Options:        options
  Macro:          macro-indicator, economic-events
  Calendar:       calendar/earnings, calendar/ipos, calendar/splits
  Exchange:       exchange-symbol-list, exchanges-list, exchanges-details
  Screening:      screener

Symbol format: {TICKER}.{EXCHANGE} (e.g., AAPL.US, MSFT.US, BMW.XETRA)
For exchange-symbol-list and eod-bulk-last-day, use exchange code (e.g., US, LSE)
        """,
    )
    parser.add_argument(
        "--endpoint",
        required=True,
        choices=SUPPORTED_ENDPOINTS,
        help="API endpoint to query",
    )
    parser.add_argument(
        "--symbol",
        help="Ticker with exchange suffix (e.g., AAPL.US) or exchange code for bulk endpoints",
    )
    parser.add_argument("--from-date", help="Start date YYYY-MM-DD")
    parser.add_argument("--to-date", help="End date YYYY-MM-DD")
    parser.add_argument("--interval", help="Intraday interval: 1m, 5m, 1h")
    parser.add_argument("--limit", type=int, help="Limit results")
    parser.add_argument("--offset", type=int, help="Offset for pagination")
    parser.add_argument(
        "--function",
        help="Technical indicator function (sma, ema, wma, rsi, macd, stoch, cci, adx, atr, bbands)",
    )
    parser.add_argument("--period", type=int, help="Period for technical indicators")
    parser.add_argument(
        "--indicator",
        help="Macro indicator code (e.g., inflation_consumer_prices_annual, gdp_current_usd)",
    )
    parser.add_argument(
        "--filter",
        help="Filter for specific fields (e.g., last_close, extended for earnings)",
    )
    parser.add_argument("--base-url", default=BASE_URL, help="Override base URL")
    parser.add_argument("--timeout", type=int, default=30, help="HTTP timeout seconds")
    parser.add_argument(
        "--raw",
        action="store_true",
        help="Output raw response without JSON formatting",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    token = os.getenv("EODHD_API_TOKEN")
    if not token:
        print("Error: EODHD_API_TOKEN environment variable is not set", file=sys.stderr)
        print("Get your API token at https://eodhd.com/", file=sys.stderr)
        return 2

    try:
        path = build_path(args.endpoint, args.symbol, args.function)
    except ClientError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    # Build query parameters
    params: dict[str, str | int] = {
        "api_token": token,
        "fmt": "json",
    }

    # Date range
    if args.from_date:
        params["from"] = args.from_date
    if args.to_date:
        params["to"] = args.to_date

    # Pagination
    if args.limit is not None:
        params["limit"] = args.limit
    if args.offset is not None:
        params["offset"] = args.offset

    # Intraday interval
    if args.interval:
        params["interval"] = args.interval

    # Technical indicators
    if args.function:
        params["function"] = args.function
    if args.period is not None:
        params["period"] = args.period

    # Macro indicator
    if args.indicator:
        params["indicator"] = args.indicator

    # Filter
    if args.filter:
        params["filter"] = args.filter

    # Special handling for news endpoint (uses 's' parameter)
    if args.endpoint == "news" and args.symbol:
        params["s"] = args.symbol

    # Special handling for sentiment endpoint
    if args.endpoint == "sentiment" and args.symbol:
        params["s"] = args.symbol

    # Special handling for insider-transactions endpoint
    if args.endpoint == "insider-transactions" and args.symbol:
        params["code"] = args.symbol

    query = urllib.parse.urlencode(params)
    url = args.base_url.rstrip("/") + path + "?" + query

    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            payload = response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        print(f"HTTP Error {exc.code}: {exc.reason}", file=sys.stderr)
        print(f"URL: {url.replace(token, '***')}", file=sys.stderr)
        try:
            error_body = exc.read().decode("utf-8", errors="replace")
            print(f"Response: {error_body}", file=sys.stderr)
        except Exception:
            pass
        return 1
    except urllib.error.URLError as exc:
        print(f"Request failed: {exc.reason}", file=sys.stderr)
        print(f"URL: {url.replace(token, '***')}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"Request failed: {exc}", file=sys.stderr)
        print(f"URL: {url.replace(token, '***')}", file=sys.stderr)
        return 1

    if args.raw:
        print(payload)
        return 0

    try:
        parsed = json.loads(payload)
    except json.JSONDecodeError:
        # Not JSON, print raw
        print(payload)
        return 0

    print(json.dumps(parsed, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
