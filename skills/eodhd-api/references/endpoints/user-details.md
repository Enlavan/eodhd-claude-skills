# User Details API

Status: complete
Source: financial-apis (User API)
Docs: https://eodhd.com/financial-apis/user-api
Provider: EODHD
Base URL: https://eodhd.com/api
Path: /user
Method: GET
Auth: api_token (query)

## Purpose

Returns account details for the subscriber associated with the given API token. Use this endpoint to verify authentication, check remaining API quota, monitor daily usage, and retrieve subscription information. No symbol or additional parameters are required.

## Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| api_token | Yes | string | Your API access token |

## Response (shape)

```json
{
  "name": "Moomoo LLC",
  "email": "user@example.com",
  "subscriptionType": "commercial",
  "paymentMethod": "Wire",
  "apiRequests": 74535,
  "apiRequestsDate": "2026-02-16",
  "dailyRateLimit": 100000,
  "extraLimit": 137909,
  "inviteToken": "X6MKGMGM",
  "inviteTokenClicked": 7,
  "subscriptionMode": "paid",
  "canManageOrganizations": false
}
```

### Output Format

| Field | Type | Description |
|-------|------|-------------|
| name | string | Name of the subscriber associated with the API token |
| email | string | Email of the subscriber associated with the API token |
| subscriptionType | string | Subscription type (e.g., monthly, yearly, commercial) |
| paymentMethod | string | Payment method (e.g., PayPal, Stripe, Wire) |
| apiRequests | integer | Number of API calls on the latest day of API usage. Resets at midnight GMT, but shows the previous day's count until a new request is made after reset |
| apiRequestsDate | string (YYYY-MM-DD) | Date of the latest API request |
| dailyRateLimit | integer | Maximum number of API calls allowed per day |
| extraLimit | integer | Remaining amount of additionally purchased API calls |
| inviteToken | string | Invitation token for the affiliate program |
| inviteTokenClicked | integer | Number of invite token clicks |
| subscriptionMode | string | Subscription mode (e.g., paid) |
| canManageOrganizations | boolean | Whether the user can manage organizations |

## Example Requests

```bash
# Get user details
curl "https://eodhd.com/api/user?api_token=YOUR_TOKEN"

# Using the demo key
curl "https://eodhd.com/api/user?api_token=demo"

# Using the helper client
python eodhd_client.py --endpoint user
```

## Notes

- No symbol or date parameters are required
- The `apiRequests` counter resets at midnight GMT each day
- The count shown reflects the latest day any request was made; it does not update until a new request occurs after the midnight reset
- API calls vs API requests: some endpoints consume more than 1 API call per request (see EODHD documentation for details)
- Useful for verifying that your API token is valid and checking remaining quota before making data requests
- API call consumption: 1 call per request

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
