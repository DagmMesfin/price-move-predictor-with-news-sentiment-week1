
"""Stock visualization class - contains all stock visualization functions"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import yfinance as yf

class StockVisualization:
    """Class containing all stock visualization functions"""

    def __init__(self):
        pass

    def plot_stock_price(self, df, stock_name):
        """
        Plot stock price with moving averages
        """
        plt.figure(figsize=(14, 6))
        plt.plot(df['Date'], df['Close'], label='Close Price')
        plt.plot(df['Date'], df['SMA_20'], label='SMA 20', linestyle='--')
        plt.plot(df['Date'], df['EMA_50'], label='EMA 50', linestyle=':')
        plt.xticks(df['Date'].iloc[::365])
        plt.title(f'Close Price with SMA & EMA for {stock_name}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_rsi(self, df, stock_name):
        """
        Plot relative strength index
        """
        plt.figure(figsize=(12, 5))
        plt.plot(df['Date'],df['RSI'], label='RSI', color='purple')
        plt.xticks(df['Date'].iloc[::365*3])
        plt.yticks(range(0,101,10))

        plt.axhline(70, color='red', linestyle='--')
        plt.axhline(30, color='green', linestyle='--')
        #45 degree dates
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.title(f"Relative Strength Index (RSI) - {stock_name}")
        plt.show()

    
    def plot_macd(self, df, stock_name):
        """
        Plot moving average convergence divergence
        """
        plt.figure(figsize=(12, 5))
        plt.plot(df['Date'], df['MACD'], label='MACD')
        plt.plot(df['Date'], df['MACD_signal'], label='Signal')
        plt.bar(df['Date'], df['MACD_hist'], label='Histogram', alpha=0.4)
        plt.xticks(df['Date'].iloc[::365*3])
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.title(f"MACD & Signal Line - {stock_name}")
        plt.legend()
        plt.show()
    
    def plot_stock_returns(self, stock_name):
        """
        Plot stock returns
        """
        stock = yf.Ticker(stock_name)
        returns = stock.history(period="max")['Close'].pct_change()
        returns.plot(title=f"Daily Returns - {stock_name}", figsize=(12, 5))
    





