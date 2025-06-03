# src/

This project is a modular Python-based data processing and analysis pipeline.

## Folder Structure

```
src/
├── __init__.py
├── financial_news/
│   ├── data_load.py
│   ├── analysis.py
│   └── visualization.py
└── stock/
    ├── analysis.py
    └── visualization.py
```

## Key Classes

### financial_news/data_load.py

The `DataLoad` class contains methods for loading and preprocessing the financial news dataset.

### financial_news/analysis.py

The `Analysis` class contains methods for analyzing the financial news dataset.

### financial_news/visualization.py

The `Visualization` class contains methods for visualizing the financial news dataset.

### stock/analysis.py

The `StockAnalysis` class contains methods for analyzing stock price data.

### stock/visualization.py

The `StockVisualization` class contains methods for visualizing stock price data.


## Benefits of Class-Based Structure

### Organization by Functionality
- All data loading methods in one class
- All analysis methods in one class
- All visualization methods in one class

### Easy to Extend
- Add new methods to appropriate class
- Maintain clear separation of concerns
- Simple inheritance if needed

### Intuitive Usage
- Clear class names indicate functionality
- Methods grouped logically
- Easy to remember and use

### Exact Notebook Preservation
- Each method is an exact copy of notebook cells
- No abstraction or modification of original logic
- Preserves all original outputs and behavior

## Notes

- All methods preserve the exact logic from the notebook
- Data path defaults to 'data/raw_analyst_ratings.csv'
- Visualizations will display using matplotlib/seaborn
- Methods print results to console just like the notebook cells
- Classes can be used independently or together
