# Sales Data Analysis & Cleaning

## Overview
This project analyzes a retail sales dataset (1,200+ records) using Python. It covers data cleaning (handling missing values and duplicates), exploratory data analysis, and visualization of sales/profit trends.

## Tools Used
- Python
- Pandas (data cleaning & analysis)
- Matplotlib & Seaborn (visualization)

## What Was Done
1. **Data Cleaning**
   - Removed duplicate records
   - Handled missing values in the `Profit` column using median imputation
   - Converted date fields to proper datetime format

2. **Exploratory Analysis**
   - Total sales and profit calculations
   - Sales breakdown by Category and Region
   - Top 5 most profitable products
   - Profit breakdown by customer Segment

3. **Visualizations**
   - Bar chart: Sales by Category
   - Line chart: Monthly Sales Trend
   - Bar chart: Profit by Region

## Key Insights
- Office Supplies generated the highest total sales among all categories.
- Central region led in total sales, closely followed by West.
- A handful of specific products (e.g., Paper and Art items) drove disproportionately high profit.
- Consumer segment contributed the most profit, ahead of Home Office and Corporate.

## Files
- `sales_data.csv` – raw dataset
- `analysis.py` – full analysis script
- `cleaned_sales_data.csv` – cleaned output dataset
- `chart1_sales_by_category.png`, `chart2_monthly_trend.png`, `chart3_profit_by_region.png` – visual outputs

## How to Run
```bash
pip install pandas matplotlib seaborn
python analysis.py
```
