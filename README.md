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

## Tasks & Deliverables

### Task 1: Git & Environment Setup

- Initialized a GitHub repository with the recommended folder structure.
- Created a Python virtual environment and tracked dependencies in `requirements.txt`.
- Configured GitHub Actions for Continuous Integration (CI).
- Set up branches (`task-1`, `main`) with regular commits and pull requests.
- Performed initial EDA:
  - Headline length distributions
  - Publisher activity patterns
  - News volume over time
  - Early keyword exploration (topic modeling)

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
│       └── unittests.yml
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