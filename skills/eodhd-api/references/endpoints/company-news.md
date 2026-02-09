# Company News API

Status: draft
Source: financial-apis (Financial News API)
Docs: https://eodhd.com/financial-apis/financial-news-api
Provider: EODHD
Base URL: https://eodhd.com/api
Path: /news
Method: GET
Auth: api_token (query)

## Purpose
Retrieve financial news articles related to a specific symbol, topic, or general market news.
Useful for sentiment analysis, event detection, and market context.

## Parameters
- Required:
  - api_token: EODHD API key
- Optional:
  - s: Symbol(s) to filter news (e.g., AAPL.US or AAPL.US,MSFT.US)
  - t: Topic tag to filter (e.g., technology, finance, crypto)
  - from: Start date YYYY-MM-DD
  - to: End date YYYY-MM-DD
  - limit: Number of articles to return (default 50, max 1000)
  - offset: Pagination offset

## Response (shape)
Array of news article objects:

```json
[
  {
    "date": "2024-01-15 14:30:00",
    "title": "Apple Announces New Product Launch",
    "content": "Full article text...",
    "link": "https://example.com/article",
    "symbols": ["AAPL.US"],
    "tags": ["technology", "product launch"],
    "sentiment": {
      "polarity": 0.15,
      "neg": 0.05,
      "neu": 0.75,
      "pos": 0.20
    }
  }
]
```

## Example request
```bash
# News for a specific symbol
curl "https://eodhd.com/api/news?s=AAPL.US&api_token=demo&fmt=json&limit=10"

# News for multiple symbols
curl "https://eodhd.com/api/news?s=AAPL.US,MSFT.US&api_token=demo&fmt=json"

# News by date range
curl "https://eodhd.com/api/news?s=AAPL.US&from=2024-01-01&to=2024-01-31&api_token=demo&fmt=json"

# General market news (no symbol filter)
curl "https://eodhd.com/api/news?api_token=demo&fmt=json&limit=20"

# Using the helper client
python eodhd_client.py --endpoint news --symbol AAPL.US --limit 10
```

## Notes
- Sentiment scores range from -1 (negative) to +1 (positive)
- `polarity` is the overall sentiment score
- `neg`, `neu`, `pos` are component probabilities (sum to ~1.0)
- News is aggregated from multiple sources
- Content may be truncated; full text available for some sources
- Historical news available depending on plan
- API call consumption: 1 call per request
