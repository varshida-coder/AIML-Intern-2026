# NIVA SALES ANALYSIS
# File Name: sales.csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# LOAD DATASET
# =====================================================

df = pd.read_csv("sales.csv")

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== DATASET DESCRIPTION =====")
print(df.describe())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# =====================================================
# NUMPY ANALYSIS
# =====================================================

revenue = df["Revenue"].values
profit = df["Profit"].values

print("\n===== NUMPY ANALYSIS =====")

print("Total Revenue :", np.sum(revenue))

print("Average Revenue :", np.mean(revenue))

print("Maximum Revenue :", np.max(revenue))

print("Minimum Revenue :", np.min(revenue))

print("Revenue Standard Deviation :", np.std(revenue))

print("Total Profit :", np.sum(profit))

print("Average Profit :", np.mean(profit))

# =====================================================
# PRODUCT WISE REVENUE
# =====================================================

print("\n===== PRODUCT WISE REVENUE =====")

product_revenue = df.groupby("Product_Name")["Revenue"].sum()

print(product_revenue)

print("\nTop Revenue Product :")
print(product_revenue.idxmax())

# =====================================================
# PRODUCT WISE PROFIT
# =====================================================

print("\n===== PRODUCT WISE PROFIT =====")

product_profit = df.groupby("Product_Name")["Profit"].sum()

print(product_profit)

print("\nMost Profitable Product :")
print(product_profit.idxmax())

# =====================================================
# CITY WISE SALES
# =====================================================

print("\n===== CITY WISE REVENUE =====")

city_sales = df.groupby("Customer_City")["Revenue"].sum()

print(city_sales)

print("\nBest City :")
print(city_sales.idxmax())

# =====================================================
# SALES CHANNEL ANALYSIS
# =====================================================

print("\n===== SALES CHANNEL REVENUE =====")

channel_sales = df.groupby("Sales_Channel")["Revenue"].sum()

print(channel_sales)

print("\nBest Sales Channel :")
print(channel_sales.idxmax())

# =====================================================
# QUANTITY SOLD ANALYSIS
# =====================================================

print("\n===== PRODUCT WISE QUANTITY SOLD =====")

quantity_sold = df.groupby("Product_Name")["Quantity_Sold"].sum()

print(quantity_sold)

print("\nHighest Quantity Sold Product :")
print(quantity_sold.idxmax())

# =====================================================
# TOP 5 REVENUE RECORDS
# =====================================================

print("\n===== TOP 5 REVENUE RECORDS =====")

top_revenue = df.sort_values(
    by="Revenue",
    ascending=False
)

print(top_revenue.head())

# =====================================================
# BAR CHART - PRODUCT REVENUE
# =====================================================

plt.figure(figsize=(12,5))

product_revenue.plot(kind="bar")

plt.title("NIVA Product Wise Revenue")

plt.xlabel("Products")

plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.show()

# =====================================================
# PIE CHART - CITY REVENUE
# =====================================================

plt.figure(figsize=(8,8))

plt.pie(
    city_sales,
    labels=city_sales.index,
    autopct="%1.1f%%"
)

plt.title("City Wise Revenue Share")

plt.show()

# =====================================================
# HISTOGRAM - REVENUE DISTRIBUTION
# =====================================================

plt.figure(figsize=(8,5))

plt.hist(
    df["Revenue"],
    bins=8
)

plt.title("Revenue Distribution")

plt.xlabel("Revenue")

plt.ylabel("Frequency")

plt.show()

# =====================================================
# BOX PLOT - REVENUE
# =====================================================

plt.figure(figsize=(6,5))

plt.boxplot(
    df["Revenue"],
    notch=False,
    vert=True
)

plt.title("Revenue Box Plot")

plt.ylabel("Revenue")

plt.show()

# =====================================================
# LINE CHART - REVENUE TREND
# =====================================================

plt.figure(figsize=(12,5))

plt.plot(
    df["Date"],
    df["Revenue"],
    marker="o"
)

plt.title("Revenue Trend")

plt.xlabel("Date")

plt.ylabel("Revenue")

plt.xticks(rotation=90)

plt.show()

# =====================================================
# PROFIT HISTOGRAM
# =====================================================

plt.figure(figsize=(8,5))

plt.hist(
    df["Profit"],
    bins=8
)

plt.title("Profit Distribution")

plt.xlabel("Profit")

plt.ylabel("Frequency")

plt.show()

# =====================================================
# FINAL BUSINESS INSIGHTS
# =====================================================

print("\n====================================")
print("NIVA BUSINESS INSIGHTS")
print("====================================")

print("Total Revenue :", np.sum(revenue))

print("Total Profit :", np.sum(profit))

print("Average Revenue :", np.mean(revenue))

print("Average Profit :", np.mean(profit))

print("Top Revenue Product :", product_revenue.idxmax())

print("Most Profitable Product :", product_profit.idxmax())

print("Highest Quantity Product :", quantity_sold.idxmax())

print("Best City :", city_sales.idxmax())

print("Best Sales Channel :", channel_sales.idxmax())

print("====================================")
print("ANALYSIS COMPLETED")
print("====================================")
