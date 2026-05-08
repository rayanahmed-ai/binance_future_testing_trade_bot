# Binance Futures Testnet Trading Bot

A simplified Python trading bot for Binance Futures Testnet (USDT-M) built using Python.

The application allows users to place MARKET and LIMIT orders through a command-line interface (CLI) with proper validation, logging, and exception handling.

This project was developed as part of the Primetrade.ai Python Developer application task.

---

# Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL
- Binance Futures Testnet integration
- Command-line interface using argparse
- Input validation
- Structured modular code
- Logging to file
- Exception handling
- Colored CLI output using Colorama

---

# Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

# Technologies Used

- Python 3.x
- python-binance
- python-dotenv
- colorama

---

# Requirements

- Python 3.x
- Binance Futures Testnet account
- Binance API Key and Secret

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/rayanahmed-ai/binance_future_testing_trade_bot
cd trading_bot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Binance Futures Testnet Setup

1. Open Binance Futures Testnet:

https://testnet.binancefuture.com

2. Login and open API Management

3. Generate:
- API Key
- Secret Key

4. Create a `.env` file in the project root:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

# CLI Arguments

| Argument | Type | Required | Description | Example |
|---|---|---|---|---|
| `--symbol` | string | Yes | Trading pair symbol | BTCUSDT |
| `--side` | string | Yes | Order side | BUY / SELL |
| `--type` | string | Yes | Order type | MARKET / LIMIT |
| `--quantity` | float | Yes | Order quantity | 0.001 |
| `--price` | float | Only for LIMIT | Limit order price | 95000 |

---

# Input Constraints

- `side` must be:
  - BUY
  - SELL

- `type` must be:
  - MARKET
  - LIMIT

- `quantity` must be greater than 0

- `price` is required for LIMIT orders

- Symbol format should match Binance Futures symbols:
  - BTCUSDT
  - ETHUSDT
  - BNBUSDT

---

# Running the Application

## MARKET BUY Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

## MARKET SELL Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

---

## LIMIT BUY Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 90000
```

---

## LIMIT SELL Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 95000
```

---

# Example Successful Output

```text
Connecting to Binance Futures Testnet...

========== ORDER SUMMARY ==========
Symbol      : BTCUSDT
Side        : BUY
Type        : MARKET
Quantity    : 0.001
==================================

========== RESPONSE ==========
Order ID     : 123456
Status       : FILLED
Executed Qty : 0.001
Avg Price    : N/A
================================

✓ Order placed successfully
```

---

# Example Error Output

## Missing Price for LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001
```

Output:

```text
Error: LIMIT orders require a price
```

---

## Invalid Side

```bash
python cli.py --symbol BTCUSDT --side HOLD --type MARKET --quantity 0.001
```

Output:

```text
Error: Invalid side. Use BUY or SELL.
```

---

## Invalid Quantity

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity -1
```

Output:

```text
Error: Quantity must be greater than 0.
```

---

# Logging

Logs are stored in:

```text
logs/trading.log
```

Logs include:

- API requests
- API responses
- validation errors
- exceptions

---

# Example Log Entry

```text
2026-05-08 15:10:22 - INFO - CLI started
2026-05-08 15:10:23 - INFO - Order Request -> Symbol=BTCUSDT, Side=BUY, Type=MARKET, Quantity=0.001
2026-05-08 15:10:24 - INFO - Order Response -> {'orderId': 123456}
```

---

# Error Handling

The application handles:

- invalid user input
- Binance API errors
- network failures
- timestamp synchronization errors
- missing LIMIT price

---

# Assumptions

- Binance Futures Testnet account is active
- API keys are valid
- User has testnet USDT balance
- Internet connection is available

---

# Dependencies

```text
python-binance
python-dotenv
colorama
```

