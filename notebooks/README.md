# notebooks/

This directory contains Jupyter notebooks used for data exploration, analysis, and visualization.

## Key Notebooks

### financial_news_eda.ipynb

This notebook contains the exploratory data analysis (EDA) for the financial news dataset. It includes:
- Loading and preprocessing the dataset.
- Analyzing headline lengths, publisher frequencies, and temporal patterns.
- Extracting and visualizing keywords from headlines.
- Investigating email publishers and their domains.

### sentiment_analysis.ipynb

This notebook focuses on sentiment analysis of financial news headlines. It includes:
- Loading and preprocessing the dataset.
- Assigning sentiment polarity scores to headlines.
- Aggregating sentiment scores daily and aligning with stock return data.
- Computing daily stock returns from closing prices.
- Merging news sentiment and stock return datasets by date and ticker.
- Performing Pearson correlation analysis to evaluate the relationship between sentiment and returns.
- Visualizing the correlation through scatter plots and heatmaps.

### stock_eda.ipynb

This notebook deals with the analysis of stock price data. It includes:
- Loading and preprocessing the stock price dataset.
- Calculating technical indicators such as moving averages, RSI, and MACD.
- Visualizing stock price movements and technical indicators.

## Notes
- All notebooks rely on the datasets found in the `data/` directory.

