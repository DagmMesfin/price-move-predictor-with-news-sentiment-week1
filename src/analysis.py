"""Analysis class - contains all analysis functions"""

import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer


class Analysis:
    """Class containing all analysis functions"""

    def __init__(self):
        pass

    # Publisher Analysis Methods
    def analyze_publisher_frequency(self, df, top_n=10):
        """
        Analyze publisher frequency
        """
        # Publisher frequency analysis
        publisher_counts = df['publisher'].value_counts()
        print(f"\n--- Top {top_n} Publishers ---")
        print(publisher_counts.head(top_n))
        return publisher_counts

    def extract_email_publishers(self, df):
        """
        Extract publishers that appear to be email addresses
        """
        # Filter publishers that look like email addresses
        email_publishers = df['publisher'].dropna().astype(str)
        email_publishers = email_publishers[email_publishers.str.contains('@', na=False)]

        print(f"\n--- Email Publishers ---")
        print(f"Number of email publishers: {len(email_publishers)}")
        print(f"Unique email publishers: {email_publishers.nunique()}")
        print("\nSample email publishers:")
        print(email_publishers.head(10).tolist())

        return email_publishers

    def extract_email_domains(self, email_publishers):
        """
        Extract domains from email publishers
        """
        # Extract domains using regex
        email_domains = email_publishers.str.extract(r'@([A-Za-z0-9.-]+)', expand=False).dropna()

        print(f"\n--- Email Domains ---")
        print(f"Total domains: {len(email_domains)}")
        print(f"Unique domains: {email_domains.nunique()}")

        return email_domains

    def get_organizational_domains(self, email_domains, top_n=10):
        """
        Get organizational email domains (excluding personal domains)
        """
        # Define personal email domains to filter out
        personal_domains = {
            'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com',
            'aol.com', 'icloud.com', 'protonmail.com', 'msn.com',
            'live.com', 'mail.com', 'yandex.com', 'zoho.com'
        }

        # Filter out personal domains
        org_domains = email_domains[~email_domains.isin(personal_domains)]
        org_domain_counts = org_domains.value_counts()

        print(f"\n--- Top {top_n} Organizational Email Domains ---")
        print(org_domain_counts.head(top_n))

        return org_domain_counts

    # Text Analysis Methods
    def analyze_keyword_frequency(self, df, ngram_range=(2, 3), max_features=30, stop_words='english'):
        """
        Analyze keyword frequency using n-grams
        """
        # Keyword frequency analysis using n-grams
        headlines = df['headline'].fillna("")

        vectorizer = CountVectorizer(
            ngram_range=ngram_range,
            stop_words=stop_words,
            max_features=max_features
        )

        X = vectorizer.fit_transform(headlines)
        feature_names = vectorizer.get_feature_names_out()

        # Calculate frequencies
        word_freq = pd.Series(
            X.toarray().sum(axis=0),
            index=feature_names
        ).sort_values(ascending=False)

        print(f"\n--- Top {max_features} Keywords (n-grams {ngram_range}) ---")
        print(word_freq)

        return word_freq

    def analyze_headline_patterns(self, df):
        """
        Analyze patterns in headlines
        """
        headlines = df['headline'].fillna("").astype(str)

        print("\n--- Headline Pattern Analysis ---")
        print(f"Total headlines: {len(headlines)}")
        print(f"Empty headlines: {(headlines == '').sum()}")
        print(f"Average headline length: {headlines.str.len().mean():.2f} characters")
        print(f"Median headline length: {headlines.str.len().median():.2f} characters")
        print(f"Max headline length: {headlines.str.len().max()} characters")
        print(f"Min headline length: {headlines.str.len().min()} characters")

        # Additional pattern analysis
        print(f"Headlines with numbers: {headlines.str.contains(r'\d', na=False).sum()}")
        print(f"Headlines with special characters: {headlines.str.contains(r'[^a-zA-Z0-9\s]', na=False).sum()}")
        print(f"Headlines with all caps words: {headlines.str.count(r'\b[A-Z]{2,}\b').sum()}")
        print(f"Headlines with question marks: {headlines.str.count(r'\?').sum()}")
        print(f"Headlines with exclamation marks: {headlines.str.count(r'!').sum()}")

        return headlines

    # Time Analysis Methods
    def analyze_daily_patterns(self, df):
        """
        Analyze daily publication patterns
        """
        # Daily publication count analysis
        daily_counts = df.groupby('publish_day').size()

        print("\n--- Daily Publication Patterns ---")
        print(f"Total days with publications: {len(daily_counts)}")
        print(f"Date range: {daily_counts.index.min()} to {daily_counts.index.max()}")
        print(f"Average articles per day: {daily_counts.mean():.2f}")
        print(f"Median articles per day: {daily_counts.median():.2f}")
        print(f"Max articles in a day: {daily_counts.max()}")
        print(f"Min articles in a day: {daily_counts.min()}")

        print("\nTop 10 busiest days:")
        print(daily_counts.nlargest(10))

        return daily_counts

    def analyze_hourly_patterns(self, df):
        """
        Analyze hourly publication patterns
        """
        # Hourly publication pattern analysis
        hourly_counts = df['hour'].value_counts().sort_index()

        print("\n--- Hourly Publication Patterns ---")
        print("Articles published by hour:")
        print(hourly_counts)

        # Business hours vs after hours
        business_hours = hourly_counts[9:17].sum()  # 9 AM to 5 PM
        after_hours = hourly_counts.sum() - business_hours

        print(f"\nBusiness hours (9 AM - 5 PM): {business_hours} articles")
        print(f"After hours: {after_hours} articles")
        print(f"Business hours percentage: {business_hours/hourly_counts.sum()*100:.1f}%")

        return hourly_counts

    def analyze_weekly_patterns(self, df):
        """
        Analyze weekly publication patterns (day of week)
        """
        # Weekly pattern analysis
        weekly_counts = df['day_of_week'].value_counts()

        # Reorder by actual day of week
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekly_counts = weekly_counts.reindex(day_order, fill_value=0)

        print("\n--- Weekly Publication Patterns ---")
        print("Articles published by day of week:")
        print(weekly_counts)

        # Weekday vs weekend
        weekday_articles = weekly_counts[['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']].sum()
        weekend_articles = weekly_counts[['Saturday', 'Sunday']].sum()

        print(f"\nWeekday articles: {weekday_articles}")
        print(f"Weekend articles: {weekend_articles}")
        print(f"Weekday percentage: {weekday_articles/(weekday_articles + weekend_articles)*100:.1f}%")

        return weekly_counts
