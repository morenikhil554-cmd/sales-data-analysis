"""
Sales Data Analysis & Cleaning Project
----------------------------------------
Author: [Your Name]
Description: Cleans and analyzes a retail sales dataset using Python (pandas),
             identifies category-wise sales/profit trends, and visualizes insights.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Load the data
# -----------------------------
df = pd.read_csv('sales_data.csv')
print("Shape before cleaning:", df.shape)
print(df.head())
print(df.info())

# -----------------------------
# 2. Clean the data
# -----------------------------
# Check missing values
print("\nMissing values per column:\n", df.isnull().sum())

# Drop duplicate rows
df = df.drop_duplicates()

# Fill missing 'Profit' values with the column median (safer than dropping rows)
df['Profit'] = df['Profit'].fillna(df['Profit'].median())

# Convert date column to proper datetime type
df['Order Date'] = pd.to_datetime(df['Order Date'])

print("\nShape after cleaning:", df.shape)

# -----------------------------
# 3. Basic Analysis
# -----------------------------
print("\nTotal Sales: ", round(df['Sales'].sum(), 2))
print("Total Profit:", round(df['Profit'].sum(), 2))

category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print("\nSales by Category:\n", category_sales)

region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print("\nSales by Region:\n", region_sales)

top_products = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Most Profitable Products:\n", top_products)

segment_profit = df.groupby('Segment')['Profit'].sum().sort_values(ascending=False)
print("\nProfit by Segment:\n", segment_profit)

# -----------------------------
# 4. Visualizations
# -----------------------------
sns.set_style("whitegrid")

# Chart 1: Sales by Category
plt.figure(figsize=(8, 5))
sns.barplot(x=category_sales.index, y=category_sales.values, palette="viridis")
plt.title('Total Sales by Category')
plt.ylabel('Total Sales ($)')
plt.xlabel('Category')
plt.tight_layout()
plt.savefig('chart1_sales_by_category.png')
plt.show()

# Chart 2: Monthly Sales Trend
df['Month'] = df['Order Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['Sales'].sum()
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trend')
plt.ylabel('Total Sales ($)')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart2_monthly_trend.png')
plt.show()

# Chart 3: Profit by Region
plt.figure(figsize=(8, 5))
sns.barplot(x=region_sales.index, y=df.groupby('Region')['Profit'].sum().values, palette="magma")
plt.title('Total Profit by Region')
plt.ylabel('Total Profit ($)')
plt.xlabel('Region')
plt.tight_layout()
plt.savefig('chart3_profit_by_region.png')
plt.show()

# -----------------------------
# 5. Save cleaned data
# -----------------------------
df.to_csv('cleaned_sales_data.csv', index=False)
print("\nCleaned data saved as 'cleaned_sales_data.csv'")
print("Charts saved as PNG files in the same folder.")
