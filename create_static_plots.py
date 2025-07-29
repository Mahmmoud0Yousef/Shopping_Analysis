import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Load the data
data = pd.read_csv('shopping_trends.csv')

# Create a directory for static plots
import os
if not os.path.exists('static_plots'):
    os.makedirs('static_plots')

print("Creating static HTML plots for GitHub...")

# 1. Scatter Plot - Previous Purchases vs Purchase Amount
fig1 = px.scatter(data, x='Previous Purchases', y='Purchase Amount (USD)', 
                  title='Previous Purchases vs Purchase Amount (USD)',
                  color='Gender', size='Review Rating',
                  hover_data=['Age', 'Category', 'Location'])
fig1.write_html('static_plots/01_scatter_previous_purchases.html')

# 2. Box Plot - Purchase Amount by Gender
fig2 = px.box(data, x="Purchase Amount (USD)", y="Previous Purchases", 
              color="Gender", title="Purchase Amount Distribution by Gender")
fig2.write_html('static_plots/02_box_purchase_amount_gender.html')

# 3. Box Plot - Purchase Amount by Discount Applied
fig3 = px.box(data, x="Purchase Amount (USD)", y="Discount Applied", 
              color="Gender", title="Purchase Amount by Discount Status")
fig3.write_html('static_plots/03_box_purchase_amount_discount.html')

# 4. Histogram - Purchase Amount Distribution by Gender
fig4 = px.histogram(data, x="Purchase Amount (USD)", color="Gender", 
                   title="Purchase Amount Distribution by Gender",
                   nbins=30)
fig4.write_html('static_plots/04_histogram_purchase_amount_gender.html')

# 5. Histogram - Purchase Amount by Age and Size
fig5 = px.histogram(data, x="Purchase Amount (USD)", y="Age", color="Size", 
                   title="Purchase Amount by Age and Size")
fig5.write_html('static_plots/05_histogram_purchase_amount_age_size.html')

# 6. Histogram - Purchase Amount by Payment Method
fig6 = px.histogram(data, x="Purchase Amount (USD)", color="Preferred Payment Method", 
                   title="Purchase Amount by Preferred Payment Method")
fig6.write_html('static_plots/06_histogram_purchase_amount_payment.html')

# 7. Histogram - Purchase Amount by Purchase Frequency
fig7 = px.histogram(data, x="Purchase Amount (USD)", color="Frequency of Purchases", 
                   title="Purchase Amount by Purchase Frequency")
fig7.write_html('static_plots/07_histogram_purchase_amount_frequency.html')

# 8. Histogram - Purchase Amount by Season
fig8 = px.histogram(data, x="Purchase Amount (USD)", color="Season", 
                   title="Purchase Amount by Season")
fig8.write_html('static_plots/08_histogram_purchase_amount_season.html')

# 9. Histogram - Review Rating by Shipping Type
fig9 = px.histogram(data, x="Review Rating", color="Shipping Type", 
                   title="Review Rating by Shipping Type")
fig9.write_html('static_plots/09_histogram_review_rating_shipping.html')

# 10. Histogram - Purchase Amount by Discount Applied
fig10 = px.histogram(data, x="Purchase Amount (USD)", color="Discount Applied", 
                    title="Purchase Amount by Discount Applied")
fig10.write_html('static_plots/10_histogram_purchase_amount_discount.html')

# 11. Pie Chart - Shipping Type Distribution
fig11 = px.pie(data, values="Purchase Amount (USD)", names="Shipping Type", 
               title="Purchase Amount Distribution by Shipping Type")
fig11.write_html('static_plots/11_pie_shipping_type.html')

# 12. Pie Chart - Subscription Status by Review Rating
fig12 = px.pie(data, values="Review Rating", names="Subscription Status", 
               title="Review Rating Distribution by Subscription Status")
fig12.write_html('static_plots/12_pie_subscription_status.html')

# 13. Pie Chart - Shipping Type by Review Rating
fig13 = px.pie(data, values="Review Rating", names="Shipping Type", 
               title="Review Rating Distribution by Shipping Type")
fig13.write_html('static_plots/13_pie_shipping_type_review.html')

# 14. Bar Chart - Category Performance
category_performance = data.groupby('Category')['Purchase Amount (USD)'].sum().sort_values(ascending=False)
fig14 = px.bar(x=category_performance.index, y=category_performance.values,
               title="Total Purchase Amount by Category",
               labels={'x': 'Category', 'y': 'Total Purchase Amount (USD)'})
fig14.write_html('static_plots/14_bar_category_performance.html')

# 15. Bar Chart - Age Group Analysis
data['Age_Group'] = pd.cut(data['Age'], bins=[0, 25, 35, 45, 55, 100], 
                           labels=['18-25', '26-35', '36-45', '46-55', '55+'])
age_group_performance = data.groupby('Age_Group')['Purchase Amount (USD)'].mean()
fig15 = px.bar(x=age_group_performance.index, y=age_group_performance.values,
               title="Average Purchase Amount by Age Group",
               labels={'x': 'Age Group', 'y': 'Average Purchase Amount (USD)'})
fig15.write_html('static_plots/15_bar_age_group_performance.html')

# 16. Heatmap - Correlation Matrix
data_num = data.select_dtypes(include='number')
correlation_matrix = data_num.corr()
fig16 = px.imshow(correlation_matrix, 
                  title="Correlation Matrix of Numerical Variables",
                  color_continuous_scale='RdBu')
fig16.write_html('static_plots/16_heatmap_correlation.html')

# 17. Scatter Matrix
fig17 = px.scatter_matrix(data[['Age', 'Purchase Amount (USD)', 'Previous Purchases', 'Review Rating']],
                         title="Scatter Matrix of Key Variables")
fig17.write_html('static_plots/17_scatter_matrix.html')

# 18. 3D Scatter Plot
fig18 = px.scatter_3d(data, x='Age', y='Purchase Amount (USD)', z='Previous Purchases',
                      color='Gender', title="3D Scatter Plot: Age vs Purchase Amount vs Previous Purchases")
fig18.write_html('static_plots/18_3d_scatter.html')

# 19. Sunburst Chart
fig19 = px.sunburst(data, path=['Category', 'Gender', 'Season'], 
                    values='Purchase Amount (USD)',
                    title="Purchase Amount Distribution by Category, Gender, and Season")
fig19.write_html('static_plots/19_sunburst_category_gender_season.html')

# 20. Treemap
fig20 = px.treemap(data, path=['Category', 'Gender'], values='Purchase Amount (USD)',
                   title="Purchase Amount Treemap by Category and Gender")
fig20.write_html('static_plots/20_treemap_category_gender.html')

print("✅ All static HTML plots have been created in the 'static_plots' directory!")
print("📁 You can now upload these HTML files to GitHub and view them directly in the browser.")
print("🔗 Each HTML file contains an interactive Plotly visualization that works without running code.") 