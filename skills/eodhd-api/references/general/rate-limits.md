# EODHD API Rate Limits & Quotas

This document explains the rate limits, API call quotas, and consumption rules for the EODHD API.

## Overview

EODHD implements rate limits and API call quotas to ensure fair usage and system stability. Limits vary by subscription plan and endpoint type.

## API Call Consumption

### How API Calls are Counted

Each successful API request consumes a certain number of API calls from your quota:

| Endpoint Type | Calls Consumed                     | Example |
|---------------|------------------------------------|---------|
| Most endpoints | 1 call                             | EOD prices, fundamentals, splits |
| News endpoints | 5 + (5 × tickers)                  | News for 2 tickers = 5 + 10 = 15 calls |
| Sentiment | 5 + (5 × tickers)                  | Sentiment for 1 ticker = 5 + 5 = 10 calls |
| News word weights | 5 + (5 × tickers)                  | Word weights for 3 tickers = 5 + 15 = 20 calls |
| Bulk downloads | 100 call (EOD)  | Entire exchange data in one call |
| Failed requests (HTTP errors) | 0 calls                            | Server errors don't count against quota |
| Invalid symbol requests | 1 call                             | Wrong symbols still return a response and count |

### Standard Endpoints 

The following endpoints consume **1 API call** per request:

**Market Data**:
- End-of-day prices (`/eod/{TICKER}`)
- Intraday data (`/intraday/{TICKER}`)
- Live (delayed) quotes (`/real-time/{TICKER}`)
- Technical indicators (`/technical/{TICKER}`)

**Fundamentals**:
- Company fundamentals (`/fundamentals/{TICKER}`)
- Dividends (`/div/{TICKER}`)
- Splits (`/splits/{TICKER}`)
- Insider transactions (`/insider-transactions`)

**Calendar & Events**:
- Earnings calendar (`/calendar/earnings`)
- Earnings trends (`/calendar/trends`)
- IPOs calendar (`/calendar/ipos`)
- Splits calendar (`/calendar/splits`)
- Dividends calendar (`/calendar/dividends`)
- Economic events (`/economic-events`)

**Exchange Data**:
- Exchange list (`/exchanges-list`)
- Exchange details (`/exchanges/{CODE}`)
- Exchange symbols (`/exchange-symbol-list/{CODE}`)
- Symbol search (`/search/{QUERY}`)

**Screening**:
- Stock screener (`/screener`)

**Bulk Data**:
- Bulk EOD (`/eod-bulk-last-day/{EXCHANGE}`)

### News & Sentiment Endpoints (5 + 5×N Calls)

These endpoints have higher consumption due to AI processing:

**Formula**: `5 + (5 × number_of_tickers)`

**Examples**:

| Request | Tickers | Calculation | Total Calls |
|---------|---------|-------------|-------------|
| `/news?s=AAPL.US` | 1 | 5 + (5 × 1) | 10 calls |
| `/news?s=AAPL.US,MSFT.US` | 2 | 5 + (5 × 2) | 15 calls |
| `/sentiment?s=AAPL.US` | 1 | 5 + (5 × 1) | 10 calls |
| `/news-word-weights?s=AAPL.US,MSFT.US,GOOGL.US` | 3 | 5 + (5 × 3) | 20 calls |

**Affected Endpoints**:
- Company news (`/news`)
- Sentiment data (`/sentiments`)
- News word weights (`/news-word-weights`)

## Plan-Based Quotas


**Note**: Actual limits depend on your specific subscription. Check your account dashboard for exact quotas.

### Daily Rate Limits

In addition to monthly quotas, there are daily rate limits:

**Purpose**: Prevent burst usage that could exhaust monthly quota too quickly

**Typical Limits**:
- Free: 20-50 requests/day
- Paid plans: 1,000-10,000+ requests/day

**Reset Time**: Daily limits reset at **midnight GMT (00:00 GMT)**

**Important**: The counter is refreshed on **the first API request made after midnight GMT**. Until that first request is sent, the counter may still display the number of API calls from the last active day. There is no manual or on-demand reset option.

### Per-Second Rate Limits

Rate limits are enforced at the API gateway level:

| Limit Type | Rate | Burst | Description |
|------------|------|-------|-------------|
| REST API requests | ~17 requests/sec (~1,000/min) | 400 | General API endpoint rate limit |

Requests exceeding the rate limit receive an **HTTP 429 (Too Many Requests)** response. Excess requests are rejected immediately (not queued).

**Note**: The per-minute rate limit does **not** increase when you purchase additional daily API calls. Doubling your daily call quota does not double the per-minute limit.

### Symbols Per Request

| Request Type | Recommended | Maximum | Notes |
|-------------|-------------|---------|-------|
| **Bulk download** | Entire exchange | Entire exchange | 1 call (EOD) or 100 calls (live). US = 45,000+ tickers |
| **Standard request with `s` parameter** | 15-20 symbols | ~100 symbols | URL becomes extremely long at high counts |
| **Batch real-time** | 15-20 symbols | ~100 symbols | Same URL length constraint |

### No Push API

EODHD provides a **REST API only** (pull-based). There is no push API that sends data to your endpoints. For real-time streaming, use the WebSocket API.

### API Request History

EODHD does **not** keep user request history data — only the latest usage counters. With hundreds of millions of requests per day across all users, storing per-request history is not feasible.

### 502 Error During Maintenance

EODHD performs technical maintenance between **5:30 and 6:00 GMT** daily. Requests during this window have an increased risk of encountering **502 errors**. Avoid scheduling automated data fetches during this period.

### X-RateLimit Headers

The `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `X-RateLimit-Reset` fields are **HTTP response headers** — they are included in the HTTP response, not in the WebSocket data stream or response body. Access them through your HTTP client's header-reading mechanism.

### WebSocket Limits

WebSocket streaming does **not** have per-request rate limits. Instead, limits apply to:

- **Concurrent connections** — Based on subscription tier
- **Symbols per connection** — Based on subscription tier (default 50, upgradeable)

See `pricing-and-plans.md` for WebSocket tier details.

## Rate Limit Headers

EODHD may include rate limit information in response headers:

```
X-RateLimit-Limit: 100000
X-RateLimit-Remaining: 95432
X-RateLimit-Reset: 1640995200
```

**Headers**:
- `X-RateLimit-Limit`: Total monthly quota
- `X-RateLimit-Remaining`: Remaining calls this month
- `X-RateLimit-Reset`: Unix timestamp when quota resets

**Note**: Header availability depends on endpoint and plan.

## Checking Your Usage

### User Details Endpoint

Check remaining quota:

```bash
curl "https://eodhd.com/api/user?api_token=YOUR_TOKEN"
```

**Response**:
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "plan": "All-In-One",
  "apiRequests": 100000,
  "apiRequestsUsed": 5432,
  "apiRequestsRemaining": 94568,
  "dailyRateLimit": 5000,
  "dailyRateLimitUsed": 123,
  "monthlyResetDate": "2024-01-01T00:00:00Z"
}
```

### Dashboard

Monitor usage through your account dashboard:
- Real-time usage statistics
- Historical usage graphs
- Usage alerts and notifications
- Breakdown by endpoint type

## Rate Limit Errors

### Exceeded Monthly Quota

**Error Response**:
```json
{
  "error": "API rate limit exceeded. Your monthly quota is exhausted."
}
```

**HTTP Status**: 429 Too Many Requests

**Solutions**:
1. Wait until quota resets (1st of next month)
2. Upgrade to higher plan
3. Purchase additional API calls (if available)
4. Optimize requests to use fewer calls

### Exceeded Daily Limit

**Error Response**:
```json
{
  "error": "Daily rate limit exceeded. Please try again tomorrow."
}
```

**HTTP Status**: 429 Too Many Requests

**Solutions**:
1. Wait until 00:00 UTC (daily reset)
2. Upgrade to plan with higher daily limit
3. Spread requests throughout the day

### Exceeded Per-Second Limit

**Error Response**:
```json
{
  "error": "Too many requests. Please slow down."
}
```

**HTTP Status**: 429 Too Many Requests

**Retry-After Header**: May include suggested wait time
```
Retry-After: 5
```

**Solutions**:
1. Implement rate limiting in your code
2. Add delays between requests
3. Use exponential backoff for retries
4. Consider batch/bulk endpoints

## Optimization Strategies

### 1. Use Bulk Endpoints

Instead of fetching EOD data for 100 symbols individually:

❌ **Inefficient** (100 calls):
```bash
for symbol in AAPL.US MSFT.US GOOGL.US ...; do
  curl "https://eodhd.com/api/eod/${symbol}?api_token=TOKEN"
done
```

✅ **Efficient** (1 call):
```bash
curl "https://eodhd.com/api/eod-bulk-last-day/US?api_token=TOKEN"
```

### 2. Cache Responses

Cache data that doesn't change frequently:

**EOD Data**: Cache until next trading day
```python
from datetime import datetime, time

def should_refresh_eod():
    """Refresh EOD cache after 5 PM EST."""
    now = datetime.now()
    return now.time() > time(17, 0)  # After 5 PM
```

**Fundamentals**: Cache for 24 hours
```python
import time

class FundamentalsCache:
    def __init__(self):
        self.cache = {}
        self.ttl = 86400  # 24 hours

    def get(self, symbol):
        if symbol in self.cache:
            data, timestamp = self.cache[symbol]
            if time.time() - timestamp < self.ttl:
                return data
        return None

    def set(self, symbol, data):
        self.cache[symbol] = (data, time.time())
```

### 3. Batch Requests

For calendar endpoints, request ranges instead of individual dates:

❌ **Inefficient** (7 calls):
```python
for date in date_range:
    get_earnings(date)
```

✅ **Efficient** (1 call):
```python
get_earnings(from_date, to_date)
```

### 4. Use Appropriate Intervals

For intraday data, choose the interval that matches your needs:

- **1-minute**: Most granular, largest response
- **5-minute**: Good balance for intraday analysis
- **1-hour**: Sufficient for daily patterns

### 5. Limit Historical Range

Only request the date range you actually need:

❌ **Excessive**:
```python
# Getting 20 years when you only need 1 year
get_eod("AAPL.US", from_date="2004-01-01", to_date="2024-01-01")
```

✅ **Appropriate**:
```python
# Only request what you need
get_eod("AAPL.US", from_date="2023-01-01", to_date="2024-01-01")
```

### 6. Minimize News API Usage

News endpoints are expensive (5 + 5×N calls):

**Strategies**:
- Request news for multiple symbols in one call
- Use longer date ranges to get more articles per request
- Cache news results for several hours
- Consider if you really need sentiment analysis

## Implementing Rate Limiting

### Python Example

```python
import time
from functools import wraps

class RateLimiter:
    def __init__(self, calls_per_second=5):
        self.min_interval = 1.0 / calls_per_second
        self.last_call = 0

    def wait(self):
        """Wait if necessary to respect rate limit."""
        elapsed = time.time() - self.last_call
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self.last_call = time.time()

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.wait()
            return func(*args, **kwargs)
        return wrapper

# Usage
limiter = RateLimiter(calls_per_second=5)

@limiter
def fetch_data(symbol):
    # Your API call here
    pass
```

### Exponential Backoff

Handle 429 errors with exponential backoff:

```python
import time
import requests

def fetch_with_retry(url, max_retries=5):
    """Fetch with exponential backoff on rate limit."""
    for attempt in range(max_retries):
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 429:
            # Rate limited
            retry_after = int(response.headers.get('Retry-After', 2 ** attempt))
            print(f"Rate limited. Waiting {retry_after} seconds...")
            time.sleep(retry_after)
            continue

        # Other error
        response.raise_for_status()

    raise Exception(f"Max retries ({max_retries}) exceeded")
```

### Request Queue

Implement a request queue for multiple operations:

```python
import queue
import threading
import time

class RequestQueue:
    def __init__(self, requests_per_second=5):
        self.queue = queue.Queue()
        self.interval = 1.0 / requests_per_second
        self.worker = threading.Thread(target=self._process_queue, daemon=True)
        self.worker.start()

    def add_request(self, func, *args, **kwargs):
        """Add request to queue."""
        future = queue.Queue()
        self.queue.put((func, args, kwargs, future))
        return future

    def _process_queue(self):
        """Process queued requests at controlled rate."""
        while True:
            func, args, kwargs, future = self.queue.get()
            try:
                result = func(*args, **kwargs)
                future.put(('success', result))
            except Exception as e:
                future.put(('error', e))
            time.sleep(self.interval)
            self.queue.task_done()

# Usage
request_queue = RequestQueue(requests_per_second=5)

def fetch_symbol(symbol):
    # Your fetch logic
    pass

# Queue requests
futures = []
for symbol in symbols:
    future = request_queue.add_request(fetch_symbol, symbol)
    futures.append(future)

# Collect results
results = [f.get() for f in futures]
```

## Monitoring & Alerts

### Track Usage

Implement usage tracking:

```python
class UsageTracker:
    def __init__(self):
        self.daily_count = 0
        self.monthly_count = 0
        self.last_reset = time.time()

    def increment(self, calls=1):
        """Increment usage counters."""
        self.daily_count += calls
        self.monthly_count += calls

    def check_limits(self, daily_limit, monthly_limit):
        """Check if approaching limits."""
        daily_pct = (self.daily_count / daily_limit) * 100
        monthly_pct = (self.monthly_count / monthly_limit) * 100

        if daily_pct > 90:
            print(f"Warning: {daily_pct:.1f}% of daily limit used")

        if monthly_pct > 90:
            print(f"Warning: {monthly_pct:.1f}% of monthly limit used")

        return daily_pct, monthly_pct
```

### Set Up Alerts

Configure alerts when approaching limits:

```python
def send_alert(message):
    """Send alert (email, Slack, etc.)."""
    # Implement your alert mechanism
    print(f"ALERT: {message}")

def check_quota():
    """Check quota and alert if necessary."""
    response = requests.get(f"https://eodhd.com/api/user?api_token={token}")
    data = response.json()

    remaining = data.get('apiRequestsRemaining', 0)
    limit = data.get('apiRequests', 0)
    pct_remaining = (remaining / limit) * 100

    if pct_remaining < 10:
        send_alert(f"Only {pct_remaining:.1f}% of API quota remaining!")
```

## Best Practices

1. **Monitor usage regularly**: Check dashboard or use `/user` endpoint
2. **Implement caching**: Reduce redundant API calls
3. **Use bulk endpoints**: When fetching data for multiple symbols
4. **Rate limit your requests**: Don't exceed per-second limits
5. **Handle 429 errors gracefully**: Implement retry logic with backoff
6. **Request only what you need**: Avoid over-fetching data
7. **Cache expensive endpoints**: Especially news/sentiment
8. **Set up alerts**: Know when approaching limits
9. **Plan for scale**: Choose appropriate subscription tier
10. **Optimize queries**: Use date ranges efficiently

## Upgrading Plans

If you consistently hit rate limits:

### Signs You Need to Upgrade

- Regularly hitting monthly quota
- Frequently receiving 429 errors
- Need faster request rates
- Require real-time data
- Need longer historical data

### What to Consider

- **Monthly call volume**: Current usage + growth
- **Daily patterns**: Peak usage times
- **Feature requirements**: Real-time vs delayed
- **Data retention**: Historical data needs
- **Support level**: Priority support for higher tiers

### How to Upgrade

1. Visit EODHD pricing page
2. Compare plan features
3. Select appropriate plan
4. Upgrade through dashboard
5. New limits apply immediately

## HTTP Error Codes

| HTTP Code | Meaning |
|-----------|---------|
| 200 | Success |
| 401 | Unauthorized — invalid or missing API key |
| 403 | Forbidden — endpoint not available for your plan |
| 429 | Too Many Requests — rate limit exceeded |
| 500 | Server Error — retry after a short delay |

## SDK Quota Management

Some official SDKs include built-in quota management:

- **R package (eodhdR2)**: Local caching and quota tracking
- **MCP Server**: Rate limiting and retry logic built in

See `sdks-and-integrations.md` for full SDK details.

## Related Resources

- **Authentication**: See `authentication.md`
- **Pricing & Plans**: See `pricing-and-plans.md` for quota details per plan
- **User endpoint**: `/api/user` for quota checking
- **Account dashboard**: Monitor usage in real-time
- **Support**: Contact for custom enterprise limits
