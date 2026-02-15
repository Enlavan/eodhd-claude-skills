# Stocks From Search API

Status: stub
Source: TBD (financial-apis or marketplace)
Provider: TBD
Base URL: TBD
Path: TBD
Method: TBD
Auth: TBD

## Purpose
TBD.

## Parameters
- Required: TBD
- Optional: TBD

## Response (shape)
TBD.

## Example request
```bash
# TBD
```

## Notes
- **Search engine**: EODHD uses a professional search engine ([SphinxSearch](http://sphinxsearch.com/)) with sophisticated search rules that take into account market capitalization (converted to USD) and average trading volume over the past 10 days. The ticker code is the primary ranking parameter. For example, searching "VISA" returns that ticker first because it is a valid ticker code on some markets, even though Visa Inc.'s primary ticker is `V`.
- **Search by ISIN**: Tickers are searchable by their ISINs via the Search API and the main page search tool. However, ISINs are not unique — the same ISIN can exist on different exchanges (e.g., `AAPL.US` and `AAPL.MX`). EODHD uses `TICKER + EXCHANGE` as the unique identifier, consistent with other data providers.
- **Special characters in names**: Some company names contain characters that are difficult for the search engine to interpret (e.g., the apostrophe in "Lowe's Companies"). In most cases the search works perfectly, but such names may produce unexpected results.
- **Multiple tickers**: The search input is a single string. It returns results relevant to that string as a whole. Entering two different ticker codes will not return two separate results — it will likely return no results. Search is one query at a time.

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
