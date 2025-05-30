"""Data loading class - contains all data loading and preprocessing functions""" 

import pandas as pd


class DataLoad:
    """Class containing all data loading and preprocessing functions"""
    
    def __init__(self):
        self.df = None
    
    def load_dataset(self, file_path='data/raw_analyst_ratings.csv'):
        """
        Load dataset (adjust the path as needed)
        """
        self.df = pd.read_csv(file_path)
        return self.df
    
    def display_dataset_overview(self, df=None):
        """
        Display dataset overview and descriptive statistics
        """
        if df is None:
            df = self.df
        
        # --- Descriptive Statistics ---
        print("\n--- Dataset Overview ---")
        print(df.info())
        print("\n--- Descriptive Stats ---")
        print(df.describe(include='all'))
    
    def analyze_headline_length(self, df=None):
        """
        Headline length analysis
        """
        if df is None:
            df = self.df
        
        # Headline length analysis
        df['headline_length'] = df['headline'].str.len()
        print("\n--- Headline Length Stats ---")
        print(df['headline_length'].describe())
        
        if df is self.df:
            self.df = df
        return df
    
    def prepare_time_features(self, df=None):
        """
        Prepare time-based features from the date column
        """
        if df is None:
            df = self.df
        
        # Convert date to datetime and extract time features
        df['date'] = pd.to_datetime(df['date'], utc=True, format='mixed')
        df['publish_day'] = df['date'].dt.date
        df['hour'] = df['date'].dt.hour
        df['day_of_week'] = df['date'].dt.day_name()
        df['month'] = df['date'].dt.month
        df['year'] = df['date'].dt.year
        
        if df is self.df:
            self.df = df
        return df
