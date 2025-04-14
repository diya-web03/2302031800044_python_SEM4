import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Fetch historical data
def fetch_stock_data(ticker, start, end):
    stock_data = yf.download(ticker, start=start, end=end)
    return stock_data

# Step 2: Calculate indicators
def calculate_indicators(data):
    data['MA20'] = data['Close'].rolling(window=20).mean()
    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['Daily Return'] = data['Close'].pct_change()
    data['Volatility'] = data['Daily Return'].rolling(window=20).std()
    return data

# Step 3: Plotting
def plot_data(data, ticker):
    plt.figure(figsize=(14, 7))

    # Price with moving averages
    plt.subplot(2, 1, 1)
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['MA20'], label='20-day MA', color='red')
    plt.plot(data['MA50'], label='50-day MA', color='green')
    plt.title(f'{ticker} Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()

    # Daily returns and volatility
    plt.subplot(2, 1, 2)
    plt.plot(data['Daily Return'], label='Daily Return', color='purple')
    plt.plot(data['Volatility'], label='20-day Volatility', color='orange')
    plt.title(f'{ticker} Daily Return and Volatility')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Main function
if __name__ == "__main__":
    ticker = "AAPL"
    start_date = "2020-01-01"
    end_date = "2024-12-31"

    stock_data = fetch_stock_data(ticker, start_date, end_date)
    stock_data = calculate_indicators(stock_data)
    plot_data(stock_data, ticker)
