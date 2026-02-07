#!/usr/bin/env python3
"""Minimal EODHD API client helper (stdlib-only).

Examples:
  python skills/eodhd-api/scripts/eodhd_client.py --endpoint eod --symbol AAPL.US --from-date 2025-01-01 --to-date 2025-01-31
  python skills/eodhd-api/scripts/eodhd_client.py --endpoint fundamentals --symbol AAPL.US
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request

BASE_URL = "https://eodhd.com/api"


class ClientError(RuntimeError):
    """Raised when user input or API response is invalid."""


def build_path(endpoint: str, symbol: str | None) -> str:
    if endpoint == "eod":
        if not symbol:
            raise ClientError("--symbol is required for endpoint=eod")
        return f"/eod/{symbol}"
    if endpoint == "intraday":
        if not symbol:
            raise ClientError("--symbol is required for endpoint=intraday")
        return f"/intraday/{symbol}"
    if endpoint == "fundamentals":
        if not symbol:
            raise ClientError("--symbol is required for endpoint=fundamentals")
        return f"/fundamentals/{symbol}"
    if endpoint == "exchange-symbol-list":
        if not symbol:
            raise ClientError("--symbol is required for endpoint=exchange-symbol-list (use exchange code)")
        return f"/exchange-symbol-list/{symbol}"
    if endpoint == "screener":
        return "/screener"
    raise ClientError(f"Unsupported endpoint: {endpoint}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Query EODHD API")
    parser.add_argument("--endpoint", required=True, choices=["eod", "intraday", "fundamentals", "exchange-symbol-list", "screener"])
    parser.add_argument("--symbol", help="Ticker with exchange suffix (e.g., AAPL.US) or exchange code for exchange-symbol-list")
    parser.add_argument("--from-date", help="Start date YYYY-MM-DD")
    parser.add_argument("--to-date", help="End date YYYY-MM-DD")
    parser.add_argument("--interval", help="Intraday interval, e.g., 1m, 5m, 1h")
    parser.add_argument("--limit", type=int, help="Limit for screener/other endpoints")
    parser.add_argument("--offset", type=int, help="Offset for screener/other endpoints")
    parser.add_argument("--base-url", default=BASE_URL, help="Override base URL")
    parser.add_argument("--timeout", type=int, default=30, help="HTTP timeout seconds")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    token = os.getenv("EODHD_API_TOKEN")
    if not token:
        print("EODHD_API_TOKEN is not set", file=sys.stderr)
        return 2

    try:
        path = build_path(args.endpoint, args.symbol)
    except ClientError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    params: dict[str, str | int] = {
        "api_token": token,
        "fmt": "json",
    }
    if args.from_date:
        params["from"] = args.from_date
    if args.to_date:
        params["to"] = args.to_date
    if args.interval:
        params["interval"] = args.interval
    if args.limit is not None:
        params["limit"] = args.limit
    if args.offset is not None:
        params["offset"] = args.offset

    query = urllib.parse.urlencode(params)
    url = args.base_url.rstrip("/") + path + "?" + query

    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            payload = response.read().decode("utf-8", errors="replace")
    except Exception as exc:  # noqa: BLE001
        print(f"Request failed: {exc}", file=sys.stderr)
        print(f"URL: {url}", file=sys.stderr)
        return 1

    try:
        parsed = json.loads(payload)
    except json.JSONDecodeError:
        print(payload)
        return 0

    print(json.dumps(parsed, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
