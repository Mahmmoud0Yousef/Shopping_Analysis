# 🛍️ Shopping Trends Data Analysis Project

## 📊 Project Overview

This comprehensive data analysis project explores e-commerce shopping trends and customer behavior patterns. The project combines SQL Server database integration with advanced data visualization techniques to uncover valuable business insights from a large-scale retail dataset.

## 🎯 Key Features

- **Database Integration**: Direct connection to SQL Server for real-time data access
- **Advanced Analytics**: Comprehensive analysis of customer demographics, purchasing patterns, and seasonal trends
- **Interactive Visualizations**: Dynamic charts and graphs using Plotly and Seaborn
- **Business Intelligence**: Actionable insights for e-commerce optimization
- **Power BI Integration**: Professional dashboard creation for stakeholder presentations

## 📁 Project Structure

```
Training Month/
├── Analysis Project.ipynb          # Main analysis notebook
├── Connect to sql server .ipynb    # Database connection utilities
├── shopping_trends.csv             # Raw dataset (3,900+ records)
├── Project.pbix                    # Power BI dashboard
└── README.md                       # This file
```

## 🗃️ Dataset Information

The project analyzes a comprehensive shopping trends dataset containing **3,900+ customer records** with the following key dimensions:

### 📈 Data Features
- **Customer Demographics**: Age, Gender, Location
- **Purchase Behavior**: Item categories, amounts, payment methods
- **Shopping Patterns**: Seasonality, frequency, subscription status
- **Customer Experience**: Review ratings, shipping preferences, discount usage

### 📊 Key Metrics Analyzed
- Purchase amounts and frequency patterns
- Category performance across demographics
- Seasonal shopping trends
- Payment method preferences
- Customer satisfaction metrics

## 🛠️ Technical Stack

### Core Technologies
- **Python 3.x** - Primary programming language
- **Jupyter Notebooks** - Interactive development environment
- **SQL Server** - Database management system
- **Power BI** - Business intelligence and visualization

### Data Science Libraries
```python
import pandas as pd          # Data manipulation
import numpy as np           # Numerical computing
import matplotlib.pyplot as plt  # Static visualizations
import seaborn as sns        # Statistical visualizations
import plotly.express as px  # Interactive visualizations
import pyodbc               # Database connectivity
```

## 🚀 Getting Started

### Prerequisites
1. **Python Environment**: Python 3.7+ with required packages
2. **SQL Server**: Local or remote SQL Server instance
3. **ODBC Driver**: SQL Server ODBC Driver 17
4. **Power BI Desktop**: For dashboard viewing (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Training-Month
   ```

2. **Install required packages**
   ```bash
   pip install pandas numpy matplotlib seaborn plotly pyodbc
   ```

3. **Configure database connection**
   - Update connection string in `Connect to sql server .ipynb`
   - Ensure SQL Server is running and accessible

4. **Run the analysis**
   ```bash
   jupyter notebook "Analysis Project.ipynb"
   ```

## 📊 Analysis Highlights

### 🔍 Key Insights Discovered
- **Demographic Patterns**: Age and gender-based purchasing preferences
- **Seasonal Trends**: Peak shopping periods and category performance
- **Payment Preferences**: Popular payment methods by customer segment
- **Customer Satisfaction**: Review rating correlations with purchase behavior
- **Geographic Analysis**: Regional shopping patterns and preferences

### 📈 Visualization Examples
- Interactive customer demographic charts
- Seasonal purchase trend analysis
- Category performance heatmaps
- Payment method distribution plots
- Customer satisfaction correlation matrices

## 🎨 Power BI Dashboard

The project includes a comprehensive Power BI dashboard (`Project.pbix`) featuring:
- **Executive Summary**: Key performance indicators
- **Customer Analytics**: Demographics and behavior insights
- **Sales Performance**: Revenue and category analysis
- **Geographic Insights**: Regional performance mapping
- **Trend Analysis**: Time-series visualizations

## 📚 Learning Outcomes

This project demonstrates proficiency in:
- **Data Engineering**: SQL Server integration and data pipeline development
- **Statistical Analysis**: Advanced analytics and pattern recognition
- **Data Visualization**: Multi-platform visualization techniques
- **Business Intelligence**: Actionable insight generation
- **Project Management**: End-to-end analytics project execution


