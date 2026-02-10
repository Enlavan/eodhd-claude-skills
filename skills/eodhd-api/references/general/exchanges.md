# EODHD Supported Exchanges

This document provides a comprehensive list of exchanges supported by EODHD, including those that may not appear in the `/exchanges-list` endpoint.

## Overview

EODHD provides data for 70+ exchanges worldwide covering:
- **Equities** - Stocks, ETFs, preferred shares
- **Indices** - Major market indices
- **Forex** - Currency pairs
- **Cryptocurrencies** - Digital assets
- **Bonds** - Government and corporate bonds
- **Commodities** - Futures and spot prices

**Note**: Not all exchanges appear in the `/exchanges-list` endpoint. Some specialized exchanges (e.g., MONEY, FOREX, CC, COMM) are accessed directly using their exchange codes.

## Exchange Code Format

Symbol format: `{TICKER}.{EXCHANGE_CODE}`

Examples:
- `AAPL.US` - Apple Inc. on NYSE/NASDAQ (US stocks)
- `BMW.XETRA` - BMW on XETRA (Germany)
- `EURUSD.FOREX` - EUR/USD currency pair
- `BTC-USD.CC` - Bitcoin/USD on cryptocurrency exchanges
- `US10Y.MONEY` - US 10-year Treasury yield

## Major Exchanges by Region

### North America

| Code | Exchange Name | Country | Asset Types | Trading Hours (Local) |
|------|---------------|---------|-------------|---------------------|
| US | NYSE/NASDAQ/AMEX | United States | Stocks, ETFs, Indices | 09:30-16:00 EST |
| TO | Toronto Stock Exchange | Canada | Stocks, ETFs | 09:30-16:00 EST |
| V | TSX Venture Exchange | Canada | Stocks | 09:30-16:00 EST |
| CN | Canadian Securities Exchange | Canada | Stocks | 09:30-16:00 EST |
| NE | NEO Exchange | Canada | Stocks, ETFs | 09:30-16:00 EST |
| MX | Mexican Stock Exchange | Mexico | Stocks | 08:30-15:00 CST |

### Europe

| Code | Exchange Name | Country | Asset Types | Trading Hours (Local) |
|------|---------------|---------|-------------|---------------------|
| LSE | London Stock Exchange | United Kingdom | Stocks, ETFs, Bonds | 08:00-16:30 GMT |
| XETRA | Deutsche Börse XETRA | Germany | Stocks, ETFs | 09:00-17:30 CET |
| F | Frankfurt Stock Exchange | Germany | Stocks | 08:00-20:00 CET |
| PA | Euronext Paris | France | Stocks, ETFs | 09:00-17:30 CET |
| AS | Euronext Amsterdam | Netherlands | Stocks, ETFs | 09:00-17:30 CET |
| BR | Euronext Brussels | Belgium | Stocks | 09:00-17:30 CET |
| LS | Euronext Lisbon | Portugal | Stocks | 09:00-17:30 CET |
| MC | Madrid Stock Exchange | Spain | Stocks | 09:00-17:30 CET |
| MI | Borsa Italiana | Italy | Stocks, ETFs | 09:00-17:30 CET |
| SW | SIX Swiss Exchange | Switzerland | Stocks | 09:00-17:30 CET |
| VI | Vienna Stock Exchange | Austria | Stocks | 09:00-17:30 CET |
| CO | Copenhagen Stock Exchange | Denmark | Stocks | 09:00-17:00 CET |
| ST | Stockholm Stock Exchange | Sweden | Stocks | 09:00-17:30 CET |
| HE | Helsinki Stock Exchange | Finland | Stocks | 10:00-18:30 EET |
| OL | Oslo Stock Exchange | Norway | Stocks | 09:00-16:20 CET |
| IC | Iceland Stock Exchange | Iceland | Stocks | 09:30-15:30 GMT |
| IR | Irish Stock Exchange | Ireland | Stocks | 08:00-16:28 GMT |
| WAR | Warsaw Stock Exchange | Poland | Stocks | 09:00-17:00 CET |
| PR | Prague Stock Exchange | Czech Republic | Stocks | 09:00-16:25 CET |
| BUD | Budapest Stock Exchange | Hungary | Stocks | 09:00-17:00 CET |
| ATH | Athens Stock Exchange | Greece | Stocks | 10:00-17:20 EET |
| IST | Borsa Istanbul | Turkey | Stocks | 09:40-18:10 TRT |
| MCX | Moscow Exchange | Russia | Stocks | 10:00-18:50 MSK |

### Asia-Pacific

| Code | Exchange Name | Country | Asset Types | Trading Hours (Local) |
|------|---------------|---------|-------------|---------------------|
| T | Tokyo Stock Exchange | Japan | Stocks | 09:00-15:00 JST |
| HK | Hong Kong Stock Exchange | Hong Kong | Stocks | 09:30-16:00 HKT |
| SHG | Shanghai Stock Exchange | China | Stocks (A-shares) | 09:30-15:00 CST |
| SHE | Shenzhen Stock Exchange | China | Stocks (A-shares) | 09:30-15:00 CST |
| NSE | National Stock Exchange of India | India | Stocks, ETFs | 09:15-15:30 IST |
| BSE | Bombay Stock Exchange | India | Stocks | 09:15-15:30 IST |
| KO | Korea Stock Exchange | South Korea | Stocks | 09:00-15:30 KST |
| KQ | KOSDAQ | South Korea | Stocks | 09:00-15:30 KST |
| SI | Singapore Exchange | Singapore | Stocks, REITs | 09:00-17:00 SGT |
| KLSE | Bursa Malaysia | Malaysia | Stocks | 09:00-17:00 MYT |
| BK | Stock Exchange of Thailand | Thailand | Stocks | 10:00-16:40 ICT |
| JK | Indonesia Stock Exchange | Indonesia | Stocks | 09:00-16:00 WIB |
| TW | Taiwan Stock Exchange | Taiwan | Stocks | 09:00-13:30 CST |
| PSE | Philippine Stock Exchange | Philippines | Stocks | 09:30-15:30 PHT |
| AU | Australian Securities Exchange | Australia | Stocks, ETFs | 10:00-16:00 AEST |
| NZ | New Zealand Stock Exchange | New Zealand | Stocks | 10:00-16:45 NZST |

### Middle East & Africa

| Code | Exchange Name | Country | Asset Types | Trading Hours (Local) |
|------|---------------|---------|-------------|---------------------|
| TADAWUL | Saudi Stock Exchange (Tadawul) | Saudi Arabia | Stocks | 10:00-15:00 AST |
| DU | Dubai Financial Market | UAE | Stocks | 10:00-14:00 GST |
| QSE | Qatar Stock Exchange | Qatar | Stocks | 09:30-13:20 AST |
| DFMG | Dubai Gold & Commodities Exchange | UAE | Commodities | 24/5 trading |
| TA | Tel Aviv Stock Exchange | Israel | Stocks | 09:30-17:25 IST |
| JSE | Johannesburg Stock Exchange | South Africa | Stocks | 09:00-17:00 SAST |
| EGX | Egyptian Exchange | Egypt | Stocks | 10:00-14:30 EET |

### Latin America

| Code | Exchange Name | Country | Asset Types | Trading Hours (Local) |
|------|---------------|---------|-------------|---------------------|
| SA | São Paulo Stock Exchange (B3) | Brazil | Stocks | 10:00-17:00 BRT |
| BA | Buenos Aires Stock Exchange | Argentina | Stocks | 11:00-17:00 ART |
| SN | Santiago Stock Exchange | Chile | Stocks | 09:30-16:00 CLT |
| CO | Colombia Stock Exchange | Colombia | Stocks | 09:30-16:00 COT |

## Special Exchange Codes

### Forex (FOREX)

Currency pairs use the `.FOREX` suffix:

Examples:
- `EURUSD.FOREX` - Euro/US Dollar
- `GBPUSD.FOREX` - British Pound/US Dollar
- `USDJPY.FOREX` - US Dollar/Japanese Yen
- `AUDUSD.FOREX` - Australian Dollar/US Dollar

**Format**: `{BASE}{QUOTE}.FOREX` (no separator between currencies)

### Cryptocurrencies (CC)

Cryptocurrency pairs use the `.CC` suffix:

Examples:
- `BTC-USD.CC` - Bitcoin/US Dollar
- `ETH-USD.CC` - Ethereum/US Dollar
- `BNB-USD.CC` - Binance Coin/US Dollar
- `XRP-USD.CC` - Ripple/US Dollar

**Format**: `{CRYPTO}-{QUOTE}.CC` (hyphen separator)

### Money Markets & Bonds (MONEY)

Government bonds and interest rates use the `.MONEY` suffix:

Examples:
- `US10Y.MONEY` - US 10-year Treasury yield
- `US2Y.MONEY` - US 2-year Treasury yield
- `DE10Y.MONEY` - German 10-year Bund yield
- `GB10Y.MONEY` - UK 10-year Gilt yield

### Commodities (COMM)

Commodity futures use the `.COMM` suffix:

Examples:
- `CL.COMM` - Crude Oil (WTI)
- `GC.COMM` - Gold
- `SI.COMM` - Silver
- `NG.COMM` - Natural Gas

### Indices (INDX)

Major indices use the `.INDX` suffix:

Examples:
- `SPX.INDX` - S&P 500 Index
- `DJI.INDX` - Dow Jones Industrial Average
- `IXIC.INDX` - NASDAQ Composite
- `FTSE.INDX` - FTSE 100
- `GDAXI.INDX` - DAX
- `N225.INDX` - Nikkei 225

## Exchange Status & Data Availability

### Real-Time Data
Some exchanges provide real-time data, while others have a 15-20 minute delay:
- **Real-time**: US (with appropriate subscription), major European exchanges
- **15-minute delay**: Most exchanges in standard plans
- **End-of-day only**: Some smaller exchanges

### Historical Data Coverage

| Region | Start Date | Notes |
|--------|-----------|-------|
| US exchanges | 1980s+ | Most liquid stocks have data from 1980s |
| Major European | 1990s+ | Varies by exchange |
| Asian markets | 1990s+ | Varies by exchange |
| Cryptocurrencies | 2010+ | Bitcoin from ~2010, others vary |
| Forex | 1990s+ | Major pairs have extensive history |

## Finding the Right Exchange Code

### Method 1: Symbol Search API
Use the `/search/{QUERY}` endpoint to find the correct symbol:

```bash
curl "https://eodhd.com/api/search/Apple?api_token=YOUR_TOKEN"
```

Returns symbols across all exchanges.

### Method 2: Exchange Symbol List
Get all symbols for a specific exchange:

```bash
curl "https://eodhd.com/api/exchange-symbol-list/US?api_token=YOUR_TOKEN"
```

### Method 3: Exchanges List API
List all available exchanges:

```bash
curl "https://eodhd.com/api/exchanges-list?api_token=YOUR_TOKEN"
```

**Note**: This endpoint may not list FOREX, CC, MONEY, COMM, or INDX "exchanges" as they are virtual groupings.

## Common Issues & Solutions

### Issue: Symbol not found
- **Solution**: Verify exchange code is correct
- Try searching for the company name using the search endpoint
- Some symbols require specific exchange codes (e.g., `AAPL.US`, not just `AAPL`)

### Issue: No data returned
- **Solution**: Check if the exchange is supported for the asset type
- Verify trading hours and market holidays
- Some instruments may have limited historical data

### Issue: Incorrect exchange code
- **Solution**: Use the exchange symbol list to verify correct ticker format
- Check if the symbol has been delisted or merged

## Additional Resources

- **Exchange Details API**: `/exchanges/{EXCHANGE_CODE}` - Get detailed information about a specific exchange
- **Exchange Symbol List API**: `/exchange-symbol-list/{EXCHANGE_CODE}` - List all symbols on an exchange
- **Symbol Search API**: `/search/{QUERY}` - Search for symbols by name or ticker

## Notes

1. Exchange codes are case-sensitive in some contexts
2. Always use the full symbol format: `TICKER.EXCHANGE`
3. Some exchanges trade multiple sessions (pre-market, regular, post-market)
4. Holiday schedules vary by exchange and country
5. Corporate actions (splits, dividends) are automatically adjusted in historical data
