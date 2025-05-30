"""
Financial News EDA Package

This package contains modularized classes extracted directly from the
financial_news_eda.ipynb notebook. Each class contains methods that
replicate the exact functionality from the notebook cells.

Classes:
- DataLoad: Load and preprocess data
- Analysis: Analyze publisher patterns, text, and temporal data
- Visualization: Create plots and charts
"""

# Import key classes for easy access
from .data_load import DataLoad
from .analysis import Analysis
from .visualization import Visualization

__all__ = [
    'DataLoad',
    'Analysis',
    'Visualization'
]
