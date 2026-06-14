import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# ==========================
# LOAD DATASET
# ==========================
df = pd.read_csv("ecommerce.csv")

# ==========================
# DISPLAY DATASET AS TABLE
# ==========================
print("\nE-COMMERCE DATASET\n")
print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))

# ==========================
# BASIC INFORMATION
# ==========================
print("\nDATASET INFORMATION")
print(df.info())

print("\nSUMMARY STATISTICS")
print(tabulate(df.describe(), headers='keys', tablefmt='grid'))

# ==========================
# TOTAL SALES
# ==========================
total_sales = df['Total_Amount'].sum()

print("\nTOTAL SALES")
print(f"₹{total_sales:,.2f}")

# ==========================
# CATEGORY WISE SALES
# ==========================
category_sales = df.groupby('Category')['Total_Amount'].sum()

print("\nCATEGORY WISE SALES")
print(tabulate(
    category_sales.reset_index(),
    headers=['Category', 'Sales'],
    tablefmt='grid',
    showindex=False
))

# ==========================
# CITY WISE ORDERS
# ==========================
city_orders = df['City'].value_counts()

print("\nCITY WISE ORDERS")
print(tabulate(
    city_orders.reset_index(),
    headers=['City', 'Orders'],
    tablefmt='grid',
    showindex=False
))

# ==========================
# PAYMENT MODE ANALYSIS
# ==========================
payment_analysis = df['Payment_Mode'].value_counts()

print("\nPAYMENT MODE ANALYSIS")
print(tabulate(
    payment_analysis.reset_index(),
    headers=['Payment Mode', 'Count'],
    tablefmt='grid',
    showindex=False
))

# ==========================
# TOP SELLING PRODUCTS
# ==========================
top_products = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)

print("\nTOP SELLING PRODUCTS")
print(tabulate(
    top_products.reset_index(),
    headers=['Product', 'Quantity Sold'],
    tablefmt='grid',
    showindex=False
))

# ==========================
# VISUALIZATION
# ALL GRAPHS IN ONE WINDOW
# ==========================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# --------------------------------
# 1. Category Wise Sales
# --------------------------------
category_sales.plot(
    kind='bar',
    ax=axes[0, 0]
)

axes[0, 0].set_title("Category Wise Sales")
axes[0, 0].set_xlabel("Category")
axes[0, 0].set_ylabel("Sales Amount")

# --------------------------------
# 2. Payment Mode Distribution
# --------------------------------
payment_analysis.plot(
    kind='pie',
    autopct='%1.1f%%',
    ax=axes[0, 1]
)

axes[0, 1].set_title("Payment Mode Distribution")
axes[0, 1].set_ylabel("")

# --------------------------------
# 3. City Wise Orders
# --------------------------------
city_orders.plot(
    kind='bar',
    ax=axes[1, 0]
)

axes[1, 0].set_title("City Wise Orders")
axes[1, 0].set_xlabel("City")
axes[1, 0].set_ylabel("Number of Orders")

# --------------------------------
# 4. Quantity vs Total Amount
# --------------------------------
axes[1, 1].scatter(
    df['Quantity'],
    df['Total_Amount']
)

axes[1, 1].set_title("Quantity vs Total Amount")
axes[1, 1].set_xlabel("Quantity")
axes[1, 1].set_ylabel("Total Amount")

# ==========================
# SHOW ALL GRAPHS TOGETHER
# ==========================
plt.tight_layout()
plt.show()

# ==========================
# FINAL REPORT
# ==========================
print("\n========== E-COMMERCE REPORT ==========")
print(f"Total Orders      : {len(df)}")
print(f"Total Revenue     : ₹{total_sales:,.2f}")
print(f"Top Category      : {category_sales.idxmax()}")
print(f"Top City          : {city_orders.idxmax()}")
print(f"Most Used Payment : {payment_analysis.idxmax()}")
print("=======================================")
