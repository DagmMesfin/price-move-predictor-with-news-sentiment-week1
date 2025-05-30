"""
Visualization class - contains all visualization functions
Extracted directly from the notebook cells
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class Visualization:
    """
    Class containing all visualization functions
    Each method replicates exact functionality from notebook cells
    """
    
    def __init__(self):
        """Initialize the Visualization class"""
        pass
    
    def plot_headline_length_distribution(self, df):
        """
        Plot headline length distribution
        Exact copy from notebook cell
        """
        # Plot headline length distribution
        plt.figure(figsize=(8, 5))
        sns.histplot(df['headline_length'], bins=30, kde=True)
        plt.title('Distribution of Headline Lengths')
        plt.xlabel('Headline Length')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()
    
    def plot_publisher_frequency(self, df, top_n=10):
        """
        Plot top publishers by frequency
        Exact copy from notebook cell
        """
        # Top publishers
        top_publishers = df['publisher'].value_counts().head(top_n)
        
        plt.figure(figsize=(12, 8))
        sns.barplot(x=top_publishers.values, y=top_publishers.index, palette='viridis')
        plt.title(f'Top {top_n} Publishers by Article Count')
        plt.xlabel('Number of Articles')
        plt.ylabel('Publisher')
        plt.tight_layout()
        plt.show()
    
    def plot_daily_publication_count(self, df):
        """
        Plot daily publication count
        Exact copy from notebook cell
        """
        # Daily publication count
        daily_counts = df.groupby('publish_day').size()
        
        plt.figure(figsize=(15, 6))
        daily_counts.plot(kind='line')
        plt.title('Articles Published Per Day')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    def plot_hourly_publication_pattern(self, df):
        """
        Plot hourly publication pattern
        Exact copy from notebook cell
        """
        # Hourly publication pattern
        plt.figure(figsize=(12, 6))
        sns.histplot(df['hour'], bins=24, kde=False)
        plt.title('Distribution of Publishing Hours')
        plt.xlabel('Hour of Day')
        plt.ylabel('Number of Articles')
        plt.xticks(range(0, 24))
        plt.tight_layout()
        plt.show()
    
    def display_keyword_frequency_chart(self, word_freq, top_n=20):
        """
        Display keyword frequency as a horizontal bar chart
        Exact copy from notebook cell
        """
        # Plot top keywords
        plt.figure(figsize=(10, 8))
        top_keywords = word_freq.head(top_n)
        sns.barplot(x=top_keywords.values, y=top_keywords.index, palette='coolwarm')
        plt.title(f'Top {top_n} Keywords in Headlines')
        plt.xlabel('Frequency')
        plt.ylabel('Keywords')
        plt.tight_layout()
        plt.show()
    
    def plot_organizational_domains(self, org_domain_counts, top_n=10):
        """
        Plot organizational email domains
        Exact copy from notebook cell
        """
        top_domains = org_domain_counts.head(top_n)
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_domains.values, y=top_domains.index, palette='coolwarm')
        plt.title('Top Organizational Email Domains Among Publishers')
        plt.xlabel('Count')
        plt.ylabel('Domain')
        plt.tight_layout()
        plt.show()
