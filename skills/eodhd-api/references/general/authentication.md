# EODHD API Authentication

This document explains how to authenticate with the EODHD API.

## Overview

EODHD uses API token-based authentication for all API requests. Authentication is simple and consistent across all endpoints.

## Authentication Method

### API Token

All API requests require an API token passed as a query parameter:

```
?api_token=YOUR_API_TOKEN
```

**Example**:
```bash
curl "https://eodhd.com/api/eod/AAPL.US?api_token=demo&fmt=json"
```

### No Headers Required

Unlike many APIs, EODHD does not require authentication headers. The token is passed directly in the URL query string.

**Not Required**:
- ❌ `Authorization: Bearer TOKEN`
- ❌ `X-API-Key: TOKEN`
- ❌ HTTP Basic Auth

**Required**:
- ✅ Query parameter: `?api_token=YOUR_TOKEN`

## Getting Your API Token

### Step 1: Sign Up

Register for an account at:
- **Website**: https://eodhd.com/register

Choose a plan:
- **Free Tier**: Limited API calls, delayed data
- **Paid Plans**: Increased limits, real-time data, extended history

### Step 2: Access Your Token

After registration:
1. Log in to your EODHD account
2. Navigate to "Settings" or "API" section
3. Copy your API token

**Token Format**:
- Length: 16-32 characters
- Contains: Alphanumeric characters and dots
- Example: `demo` (demo token), `6123abc456def789.12345678` (real token)

### Step 3: Secure Your Token

**Important Security Practices**:
- ✅ Store in environment variables
- ✅ Use secrets management (AWS Secrets Manager, Azure Key Vault, etc.)
- ✅ Rotate tokens periodically
- ❌ Never commit tokens to version control
- ❌ Don't share tokens publicly
- ❌ Avoid embedding in client-side code

## Using the API Token

### Command Line (curl)

```bash
# Basic request
curl "https://eodhd.com/api/eod/AAPL.US?api_token=YOUR_TOKEN&fmt=json"

# With environment variable
export EODHD_API_TOKEN="your_token_here"
curl "https://eodhd.com/api/eod/AAPL.US?api_token=${EODHD_API_TOKEN}&fmt=json"
```

### Python

#### Using requests library

```python
import os
import requests

# Store token in environment variable
api_token = os.environ.get('EODHD_API_TOKEN')

# Make request
url = "https://eodhd.com/api/eod/AAPL.US"
params = {
    'api_token': api_token,
    'fmt': 'json'
}
response = requests.get(url, params=params)
data = response.json()
```

#### Using the provided client

```python
import os
# Set environment variable
os.environ['EODHD_API_TOKEN'] = 'your_token_here'

# Use the client (it reads from environment)
# The client automatically includes the token
```

```bash
# Command line with client
export EODHD_API_TOKEN="your_token_here"
python eodhd_client.py --endpoint eod --symbol AAPL.US
```

### JavaScript/Node.js

```javascript
// Using environment variable
const apiToken = process.env.EODHD_API_TOKEN;

// Using fetch
const url = `https://eodhd.com/api/eod/AAPL.US?api_token=${apiToken}&fmt=json`;
fetch(url)
  .then(response => response.json())
  .then(data => console.log(data));

// Using axios
const axios = require('axios');
axios.get('https://eodhd.com/api/eod/AAPL.US', {
  params: {
    api_token: apiToken,
    fmt: 'json'
  }
})
.then(response => console.log(response.data));
```

### PHP

```php
<?php
// Store token in environment
$api_token = getenv('EODHD_API_TOKEN');

// Build URL
$url = "https://eodhd.com/api/eod/AAPL.US?api_token=" . $api_token . "&fmt=json";

// Make request
$response = file_get_contents($url);
$data = json_decode($response, true);
?>
```

### R

```r
# Store token
api_token <- Sys.getenv("EODHD_API_TOKEN")

# Using httr
library(httr)
library(jsonlite)

url <- "https://eodhd.com/api/eod/AAPL.US"
response <- GET(url, query = list(
  api_token = api_token,
  fmt = "json"
))
data <- fromJSON(content(response, "text"))
```

## Demo Token

EODHD provides a demo token for testing:

**Demo Token**: `demo`

**Example**:
```bash
curl "https://eodhd.com/api/eod/AAPL.US?api_token=demo&fmt=json"
```

**Limitations**:
- Restricted to specific symbols (AAPL.US, MSFT.US, etc.)
- Limited to recent data only
- Rate-limited (low request quota)
- 15-20 minute delayed data
- Not suitable for production use

**Use Cases**:
- Testing API endpoints
- Learning the API structure
- Prototyping applications
- Documentation examples

## Environment Variables

### Recommended Setup

**Linux/macOS**:
```bash
# Temporary (current session only)
export EODHD_API_TOKEN="your_token_here"

# Permanent (add to ~/.bashrc or ~/.zshrc)
echo 'export EODHD_API_TOKEN="your_token_here"' >> ~/.bashrc
source ~/.bashrc
```

**Windows (Command Prompt)**:
```cmd
# Temporary
set EODHD_API_TOKEN=your_token_here

# Permanent
setx EODHD_API_TOKEN "your_token_here"
```

**Windows (PowerShell)**:
```powershell
# Temporary
$env:EODHD_API_TOKEN = "your_token_here"

# Permanent
[System.Environment]::SetEnvironmentVariable('EODHD_API_TOKEN', 'your_token_here', 'User')
```

### Docker

```dockerfile
# Dockerfile
ENV EODHD_API_TOKEN=${EODHD_API_TOKEN}

# Or at runtime
docker run -e EODHD_API_TOKEN=your_token_here your_image
```

### Environment Files

**.env file** (for local development):
```ini
EODHD_API_TOKEN=your_token_here
```

**Load in Python**:
```python
from dotenv import load_dotenv
load_dotenv()

import os
api_token = os.environ.get('EODHD_API_TOKEN')
```

**Load in Node.js**:
```javascript
require('dotenv').config();
const apiToken = process.env.EODHD_API_TOKEN;
```

## Security Best Practices

### 1. Never Hardcode Tokens

❌ **Bad**:
```python
api_token = "6123abc456def789.12345678"  # Never do this!
```

✅ **Good**:
```python
api_token = os.environ.get('EODHD_API_TOKEN')
if not api_token:
    raise ValueError("EODHD_API_TOKEN not set")
```

### 2. Use .gitignore

Add to your `.gitignore`:
```
# Environment files
.env
.env.local
.env.*.local

# Token files
*token*
*secret*
*credential*

# IDE files that might contain tokens
.vscode/settings.json
.idea/
```

### 3. Rotate Tokens Regularly

- Change tokens every 3-6 months
- Immediately rotate if token is exposed
- Keep old token active briefly during rotation
- Update all services using the token

### 4. Limit Token Exposure

- Don't log tokens in application logs
- Redact tokens in error messages
- Don't send tokens to client-side code
- Use server-side proxies for web apps

**Example - Log Redaction**:
```python
def log_url(url, token):
    safe_url = url.replace(token, "***REDACTED***")
    print(f"Request: {safe_url}")
```

### 5. Implement Token Validation

```python
def validate_token(token):
    """Validate token format before use."""
    if not token:
        raise ValueError("Token is empty")
    if len(token) < 4:
        raise ValueError("Token too short")
    # Add more validation as needed
    return token
```

### 6. Use Secrets Management

**AWS Secrets Manager**:
```python
import boto3
import json

def get_token():
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId='eodhd-api-token')
    secret = json.loads(response['SecretString'])
    return secret['EODHD_API_TOKEN']
```

**Azure Key Vault**:
```python
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

def get_token():
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url="https://myvault.vault.azure.net/", credential=credential)
    secret = client.get_secret("eodhd-api-token")
    return secret.value
```

**HashiCorp Vault**:
```python
import hvac

def get_token():
    client = hvac.Client(url='http://localhost:8200')
    secret = client.secrets.kv.v2.read_secret_version(path='eodhd')
    return secret['data']['data']['api_token']
```

## Authentication Errors

### Invalid Token

**Error Response**:
```json
{
  "error": "Invalid API token"
}
```

**HTTP Status**: 401 Unauthorized

**Solutions**:
- Verify token is correct
- Check for typos or extra spaces
- Ensure token hasn't expired
- Try with demo token to confirm API is working

### Missing Token

**Error Response**:
```json
{
  "error": "API token is required"
}
```

**HTTP Status**: 401 Unauthorized

**Solutions**:
- Add `?api_token=YOUR_TOKEN` to URL
- Check environment variable is set
- Verify token is passed in request

### Rate Limit Exceeded

**Error Response**:
```json
{
  "error": "API rate limit exceeded"
}
```

**HTTP Status**: 429 Too Many Requests

**Solutions**:
- Wait and retry after rate limit resets
- Upgrade to a higher plan
- Implement request throttling
- Use bulk endpoints for large datasets

## Checking Token Status

### User Details Endpoint

Verify your token and check account limits:

```bash
curl "https://eodhd.com/api/user?api_token=YOUR_TOKEN"
```

**Response**:
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "plan": "All-In-One",
  "apiRequests": 50000,
  "apiRequestsUsed": 1234,
  "apiRequestsRemaining": 48766,
  "dailyRateLimit": 100000,
  "dailyRateLimitUsed": 5678
}
```

**Use Cases**:
- Verify token is valid
- Check remaining API calls
- Monitor usage
- Validate plan features

## Multiple Tokens

### Using Different Tokens

If you have multiple EODHD accounts:

```python
# Token per environment
dev_token = os.environ.get('EODHD_DEV_TOKEN')
prod_token = os.environ.get('EODHD_PROD_TOKEN')

# Select based on environment
if os.environ.get('ENV') == 'production':
    api_token = prod_token
else:
    api_token = dev_token
```

### Token Rotation

Implement seamless token rotation:

```python
class TokenManager:
    def __init__(self):
        self.primary = os.environ.get('EODHD_TOKEN_PRIMARY')
        self.secondary = os.environ.get('EODHD_TOKEN_SECONDARY')
        self.current = self.primary

    def get_token(self):
        return self.current

    def rotate(self):
        """Switch to secondary token if primary fails."""
        self.current = self.secondary if self.current == self.primary else self.primary
```

## Troubleshooting

### Issue: Token Not Working

**Checklist**:
1. Token is correct (copy-paste from account)
2. No extra spaces or newlines
3. Environment variable is set correctly
4. Account is active and not suspended
5. Token hasn't been revoked

**Test**:
```bash
# Echo token to verify (be careful with this!)
echo $EODHD_API_TOKEN

# Test with demo token
curl "https://eodhd.com/api/eod/AAPL.US?api_token=demo&fmt=json"

# Test with your token
curl "https://eodhd.com/api/user?api_token=$EODHD_API_TOKEN"
```

### Issue: Token in Version Control

**If token was committed**:
1. Immediately revoke the token in EODHD dashboard
2. Generate a new token
3. Update environment variables everywhere
4. Rewrite git history (if public repo):
   ```bash
   # Use git filter-branch or BFG Repo-Cleaner
   # This is advanced - seek help if unsure
   ```

### Issue: Token Exposed Publicly

**Immediate Actions**:
1. Revoke token immediately in EODHD dashboard
2. Generate new token
3. Check account for unusual activity
4. Change password if account security is compromised
5. Review where token was exposed and remove

## Related Resources

- **API Documentation**: https://eodhd.com/financial-apis/
- **Account Settings**: https://eodhd.com/cp/settings
- **Support**: https://eodhd.com/contact
- **Rate Limits**: See `rate-limits.md` in this directory
