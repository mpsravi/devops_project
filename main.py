import yfinance as yf
import pandas as pd
import talib

def calculate_moving_average(symbol, period):
    stock_data = yf.download(symbol)
    close_prices = stock_data['Close']
    moving_average = close_prices.rolling(window=period).mean()
    return moving_average

def calculate_rsi(symbol, period):
    stock_data = yf.download(symbol)
    close_prices = stock_data['Close']
    rsi = talib.RSI(close_prices, timeperiod=period)
    return rsi

def main():
    symbol = input("Enter the stock symbol: ")
    period = int(input("Enter the period for moving average and RSI calculation: "))

    moving_average = calculate_moving_average(symbol, period)
    rsi = calculate_rsi(symbol, period)

    print(f"Moving Average for {symbol}:")
    print(moving_average.tail())

    print(f"RSI for {symbol}:")
    print(rsi.tail())

if __name__ == '__main__':
    main()
