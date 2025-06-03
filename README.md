# 📊 Predicting Price Moves with News Sentiment - Week 1 Challenge

This repository contains my submission for the **Week 1 Challenge** of the **10 Academy Artificial Intelligence Mastery (AIM)** program. The project focuses on predicting stock price movements by analyzing financial news sentiment and integrating it with technical indicators using Python.

---

## 🎯 Project Objective

The goal is to help **Nova Financial Solutions** enhance its predictive analytics by:

- Performing **sentiment analysis** on financial news headlines.
- Computing **technical indicators** using historical stock data.
- Analyzing correlations between sentiment scores and stock price **returns**.
- Providing data-driven investment insights based on observed patterns.

---

## ✅ Tasks & Deliverables

### Task 1: Git & Environment Setup

- Initialized a GitHub repository with the recommended folder structure.
- Created a Python virtual environment and tracked dependencies in `requirements.txt`.
- Configured GitHub Actions for Continuous Integration (CI).
- Set up branches (`task-1`, `main`) with regular commits and pull requests.
- Performed initial EDA:
  - Headline length distributions
  - Publisher activity patterns
  - News volume over time
  - Topic modeling and named entity extraction

### Task 2: Quantitative Analysis Using PyNance

- Fetched stock price data using `yfinance`.
- Switched from TA-Lib to **PyNance** due to system dependency issues.
- Calculated technical indicators such as:
  - Simple and exponential moving averages
  - Relative Strength Index (RSI)
  - Moving Average Convergence Divergence (MACD)
- Visualized indicators in relation to stock price movement (saved in `outputs/` folder).
- Organized work on the `task-2` branch with commits and PR.

### Task 3: Correlation Between Sentiment and Stock Movement

- Used `NLTK` to assign sentiment polarity scores to headlines.
- Aggregated sentiment scores daily and aligned with stock return data.
- Computed daily stock returns from closing prices.
- Merged news sentiment and stock return datasets by date and ticker.
- Performed Pearson correlation analysis to evaluate the relationship between sentiment and returns.
- Prepared visualizations such as scatter plots and correlation heatmaps.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/DagmMesfin/price-move-predictor-with-news-sentiment-week1.git
cd price-move-predictor-with-news-sentiment-week1
````

### 2. Create and Activate a Virtual Environment

🔁 For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

🔁 For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📂 Folder Structure

```plaintext
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── notebooks/
│   ├── __init__.py
│   └── EDA.ipynb
├── src/
│   └── __init__.py
├── scripts/
│   ├── __init__.py
│   └── README.md
├── tests/
│   └── __init__.py
├── requirements.txt
├── README.md
├── .gitignore
```