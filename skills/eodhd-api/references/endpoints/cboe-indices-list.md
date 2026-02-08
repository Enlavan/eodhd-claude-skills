# Cboe Indices List API

Status: draft
Source: financial-apis (CBOE Europe Indices API beta)
Docs: https://eodhd.com/financial-apis/cboe-europe-indices-api-beta
Provider: EODHD
Base URL: https://eodhd.com/api
Path: /cboe/indices
Method: GET
Auth: api_token (query)

## Purpose
Return the full list of CBOE indices available via EODHD, including the latest
close and divisor plus basic metadata needed to select an index code for the
feed endpoint.

## Parameters
- Required:
  - api_token: EODHD API key.
- Optional:
  - fmt: json or xml (default json).
  - pagination: follow the URL in links.next until null (no manual params).

## Response (shape)
- meta.total: integer total returned in this response.
- data[]: array of index entries.
  - data[].id: EODHD index identifier (often same as index_code).
  - data[].type: "cboe-index".
  - data[].attributes.region: country/region.
  - data[].attributes.index_code: CBOE index code.
  - data[].attributes.feed_type: latest feed type.
  - data[].attributes.date: YYYY-MM-DD.
  - data[].attributes.index_close: number.
  - data[].attributes.index_divisor: number.
- links.next: string or null pagination URL.

## Example request
```bash
curl "https://eodhd.com/api/cboe/indices?api_token=YOUR_API_KEY&fmt=json"
```

## Notes
- API call consumption: 10 calls per request.
- Use this endpoint to discover supported indices and the index_code for
  the detailed feed endpoint.
