
"""Stock analysis class - contains all stock analysis functions"""

import pandas as pd
import talib


class StockAnalysis:
    """Class containing all stock analysis functions"""

    def __init__(self):
        pass

    def load_stock_data(self, stock_name):
        """
        Load stock data
        """
        file_path = f'../data/{stock_name}_historical_data.csv'
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'])
        return df

    def calculate_moving_averages(self, df, short_window=20, long_window=50):
        """
        Calculate moving averages
        """
        df['SMA_20'] = talib.SMA(df['Close'], timeperiod=short_window)
        df['EMA_50'] = talib.EMA(df['Close'], timeperiod=long_window)
        return df
    
    def calculate_rsi(self, df, period=14):
        """
        Calculate relative strength index
        """
        df['RSI'] = talib.RSI(df['Close'], timeperiod=period)
        return df
    
    def calculate_macd(self, df, fastperiod=12, slowperiod=26, signalperiod=9):
        """
        Calculate moving average convergence divergence
        """
        df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(df['Close'],
                                                      fastperiod=fastperiod,
                                                      slowperiod=slowperiod,
                                                      signalperiod=signalperiod)
        return df
    

    
