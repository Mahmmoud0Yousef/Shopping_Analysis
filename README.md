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
├── interactive_dashboard.html      # Interactive web dashboard
├── create_static_plots.py          # Static HTML plot generator
├── static_plots/                   # Generated interactive charts (20 HTML files)
├── SETUP_INSTRUCTIONS.md           # Setup guide (Arabic)
├── .gitignore                      # Git ignore file
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
2. **SQL Server**: Local or remote SQL Server instance (optional for static plots)
3. **ODBC Driver**: SQL Server ODBC Driver 17 (optional for static plots)
4. **Power BI Desktop**: For dashboard viewing (optional)

### Quick Start (Static Visualizations)

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/shopping-trends-analysis.git
   cd shopping-trends-analysis
   ```

2. **Install required packages**
   ```bash
   pip install pandas numpy matplotlib seaborn plotly pyodbc
   ```

3. **Generate static HTML plots**
   ```bash
   python create_static_plots.py
   ```

4. **Open the interactive dashboard**
   - Open `interactive_dashboard.html` in your web browser
   - Or view individual plots in the `static_plots/` directory

### Full Analysis Setup

1. **Configure database connection**
   - Update connection string in `Connect to sql server .ipynb`
   - Ensure SQL Server is running and accessible

2. **Run the complete analysis**
   ```bash
   jupyter notebook "Analysis Project.ipynb"
   ```

### 🎯 GitHub Deployment

The project is ready for GitHub deployment with:
- **Static HTML files** that work without running code
- **Interactive dashboard** accessible via web browser
- **Professional README** with setup instructions
- **Git configuration** with proper `.gitignore`

## 📊 Analysis Highlights

### 🔍 Key Insights Discovered
- **Demographic Patterns**: Age and gender-based purchasing preferences
- **Seasonal Trends**: Peak shopping periods and category performance
- **Payment Preferences**: Popular payment methods by customer segment
- **Customer Satisfaction**: Review rating correlations with purchase behavior
- **Geographic Analysis**: Regional shopping patterns and preferences

### 📈 Interactive Visualizations
- **20 Interactive Charts**: Scatter plots, histograms, box plots, pie charts
- **3D Visualizations**: Multi-dimensional data exploration
- **Advanced Charts**: Sunburst, treemap, correlation heatmaps
- **Real-time Interactivity**: Zoom, hover, filter capabilities
- **Mobile Responsive**: Works on all devices and browsers

### 🎨 Dashboard Features
- **Professional Web Interface**: Modern, responsive design
- **Easy Navigation**: One-click access to all visualizations
- **Quick Statistics**: Project overview with key metrics
- **No Code Required**: View all charts without running Python

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
- **Web Development**: Interactive HTML dashboard creation
- **Git Version Control**: Professional repository management
- **Documentation**: Comprehensive setup and usage guides

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Submit bug reports and feature requests
- Contribute additional analysis notebooks
- Enhance visualizations and dashboards
- Improve documentation and code quality
- Add new interactive visualizations
- Enhance the web dashboard design

## 🚀 Deployment Status

- ✅ **Git Repository**: Initialized and ready for GitHub
- ✅ **Static HTML Files**: 20 interactive visualizations generated
- ✅ **Interactive Dashboard**: Professional web interface created
- ✅ **Documentation**: Comprehensive setup guides included
- ✅ **Git Configuration**: Proper `.gitignore` and commit structure

