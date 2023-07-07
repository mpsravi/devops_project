import yfinance as yf
import pandas as pd

def calculate_rsi(data, period=14):
    close_delta = data['Close'].diff()
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)
    avg_gain = up.rolling(window=period).mean()
    avg_loss = down.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_ma(data, period=50):
    ma = data['Close'].rolling(window=period).mean()
    return ma

# Fetch stock data using yfinance
ticker = 'AAPL'  # Replace with your desired stock symbol
stock_data = yf.download(ticker, start='2021-01-01', end='2023-07-06')

# Calculate RSI
rsi = calculate_rsi(stock_data)

# Calculate Moving Average (MA)
ma = calculate_ma(stock_data)

# Print the RSI and MA values
print("RSI:")
print(rsi)

print("\nMoving Average:")
print(ma)
