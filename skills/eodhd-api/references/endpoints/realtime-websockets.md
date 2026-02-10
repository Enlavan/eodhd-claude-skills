# Realtime Websockets API

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
- TBD

## Error Handling

### WebSocket Error Messages

When an error occurs, the WebSocket connection sends error messages in JSON format:

```json
{
  "status": 422,
  "message": "Server error"
}
```

### Common Error Codes

| Status Code | Meaning | Description | Solution |
|-------------|---------|-------------|----------|
| **401** | Unauthorized | Invalid API token | Check your `api_token` parameter in the connection URL |
| **403** | Forbidden | No access to real-time data | Upgrade to a plan with WebSocket access |
| **422** | Unprocessable Entity | Server error or invalid request | Verify subscribe message format and symbol syntax |
| **429** | Too Many Requests | Rate limit from rapid reconnection attempts | Implement exponential backoff for reconnections |
| **500** | Internal Server Error | Server-side error | Retry connection after delay |

### WebSocket Close Codes

| Close Code | Meaning | Description |
|------------|---------|-------------|
| **1000** | Normal Closure | Connection closed normally |
| **1006** | Abnormal Closure | Connection lost without close frame |
| **1008** | Policy Violation | Invalid symbols or message format |
| **1011** | Internal Error | Server error |

### Python Error Handling Example

```python
import asyncio
import websockets
import json

async def connect_with_error_handling(url):
    """Connect with comprehensive error handling"""
    try:
        async with websockets.connect(url) as ws:
            print("✅ Connected")

            # Subscribe
            await ws.send(json.dumps({"action": "subscribe", "symbols": "AAPL"}))

            # Receive messages
            async for message in ws:
                data = json.loads(message)

                # Check for error messages
                if "status" in data and "message" in data:
                    status = data["status"]
                    msg = data["message"]

                    if status == 422:
                        print(f"⚠️ Server error (422): {msg}")
                    elif status == 429:
                        print(f"⚠️ Rate limit (429): {msg}")
                    else:
                        print(f"⚠️ Error {status}: {msg}")
                    continue

                # Process valid data
                if "s" in data and "p" in data:
                    print(f"{data['s']}: ${data['p']}")

    except websockets.exceptions.InvalidStatusCode as e:
        if e.status_code == 401:
            print("❌ Error 401: Invalid API token")
        elif e.status_code == 403:
            print("❌ Error 403: No access to real-time data")
        elif e.status_code == 429:
            print("⚠️ Error 429: Rate limit exceeded")

    except websockets.exceptions.ConnectionClosed as e:
        print(f"⚠️ Connection closed: code={e.code}")

        if e.code == 1000:
            print("Normal closure")
        elif e.code == 1008:
            print("Policy violation - check symbols")
        else:
            print("Reconnecting...")

# Usage
url = "wss://ws.eodhistoricaldata.com/ws/crypto?api_token=demo"
asyncio.run(connect_with_error_handling(url))
```

### Best Practices

- **Exponential Backoff**: Use increasing delays for reconnection attempts (1s, 2s, 4s, 8s, ...)
- **Rate Limit Handling**: For 429 errors, wait at least 60 seconds before retrying
- **Validate Messages**: Check for `"status"` field before processing as market data
- **Monitor Health**: Track time since last message; reconnect if connection appears stale
- **Graceful Shutdown**: Unsubscribe before closing connection
