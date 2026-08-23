# ============================================================
# SALES DATA ANALYSIS - BUSINESS CASE
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------
# 1. CREATE DATASET
# ------------------------------------------------------------

np.random.seed(42)

# Generate dates
dates = pd.date_range(
    start="2024-01-01",
    end="2025-12-31",
    freq="D"
)

# Categories
products = ["Laptop", "Mobile", "Tablet", "Headphones"]
regions = ["North", "South", "East", "West"]

# Create dataset
n = 500

df = pd.DataFrame({
    "Date": np.random.choice(dates, n),
    "Product": np.random.choice(products, n),
    "Sales": np.random.randint(500, 20000, n),
    "Region": np.random.choice(regions, n)
})

# Add missing dates for demonstration
df.loc[[10, 25, 100], "Date"] = pd.NaT

# Add incorrect sales values for demonstration
df.loc[[50, 75, 150], "Sales"] = [-500, -1000, 0]

# Save raw dataset
df.to_csv("sales_data_raw.csv", index=False)

print("Original Dataset")
print(df.head())
print("\nShape:", df.shape)


# ------------------------------------------------------------
# 2. DATA CLEANING
# ------------------------------------------------------------

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Handle missing dates
# Rows with missing dates are removed because we cannot
# determine which month they belong to.
df = df.dropna(subset=["Date"])

# Remove incorrect sales values
# Sales must be greater than zero.
df = df[df["Sales"] > 0]

# Reset index
df.reset_index(drop=True, inplace=True)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nCleaned Dataset")
print(df.head())

print("\nCleaned Dataset Shape:", df.shape)


# ------------------------------------------------------------
# 3. CREATE MONTH COLUMN
# ------------------------------------------------------------

df["Month"] = df["Date"].dt.to_period("M").dt.to_timestamp()

# Group sales by month
monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
    .reset_index()
)

print("\nMonthly Sales")
print(monthly_sales)


# ------------------------------------------------------------
# 4. SALES BY REGION
# ------------------------------------------------------------

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Sales", ascending=False)
)

print("\nSales by Region")
print(region_sales)

# Find best region
best_region = region_sales.iloc[0]

print("\nBest Performing Region:")
print(best_region["Region"])

print("Sales:",
      f"${best_region['Sales']:,.2f}")


# ------------------------------------------------------------
# 5. SALES BY PRODUCT
# ------------------------------------------------------------

product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Sales", ascending=False)
)

print("\nSales by Product")
print(product_sales)

# Find best product
best_product = product_sales.iloc[0]

print("\nProduct Driving Most Revenue:")
print(best_product["Product"])

print("Sales:",
      f"${best_product['Sales']:,.2f}")


# ============================================================
# VISUALIZATION
# ============================================================

# Seaborn style
sns.set_theme(style="whitegrid")


# ------------------------------------------------------------
# 6. SEABORN LINEPLOT
# Monthly Sales Trend
# ------------------------------------------------------------

plt.figure(figsize=(12, 6))

sns.lineplot(
    data=monthly_sales,
    x="Month",
    y="Sales",
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 7. SEABORN BARPLOT
# Sales by Region
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

# hue + legend=False avoids compatibility problems
# with newer Seaborn versions.
sns.barplot(
    data=region_sales,
    x="Region",
    y="Sales",
    hue="Region",
    legend=False
)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 8. SEABORN BOXPLOT
# Sales Distribution
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="Product",
    y="Sales",
    hue="Product",
    legend=False
)

plt.title("Sales Distribution by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 9. MATPLOTLIB PIE CHART
# Product Share
# ------------------------------------------------------------

plt.figure(figsize=(8, 8))

plt.pie(
    product_sales["Sales"],
    labels=product_sales["Product"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Product Share of Total Sales")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 10. MATPLOTLIB MULTI-LINE PLOT
# Region-wise Monthly Trends
# ------------------------------------------------------------

region_monthly = (
    df.groupby(["Month", "Region"])["Sales"]
    .sum()
    .reset_index()
)

plt.figure(figsize=(12, 6))

for region in regions:

    region_data = region_monthly[
        region_monthly["Region"] == region
    ]

    plt.plot(
        region_data["Month"],
        region_data["Sales"],
        marker="o",
        label=region
    )

plt.title("Region-wise Monthly Sales Trends")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend(title="Region")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ============================================================
# 11. SEASONAL TREND ANALYSIS
# ============================================================

df["Month_Number"] = df["Date"].dt.month
df["Month_Name"] = df["Date"].dt.month_name()

seasonal_sales = (
    df.groupby(
        ["Month_Number", "Month_Name"]
    )["Sales"]
    .sum()
    .reset_index()
    .sort_values("Month_Number")
)

print("\nSeasonal Sales")
print(seasonal_sales)


# Find highest sales month
best_month = seasonal_sales.loc[
    seasonal_sales["Sales"].idxmax()
]

print("\nHighest Sales Month:")
print(best_month["Month_Name"])

print("Sales:",
      f"${best_month['Sales']:,.2f}")


# ------------------------------------------------------------
# 12. SEASONAL SALES GRAPH
# ------------------------------------------------------------

plt.figure(figsize=(12, 6))

sns.lineplot(
    data=seasonal_sales,
    x="Month_Name",
    y="Sales",
    marker="o"
)

plt.title("Seasonal Monthly Sales Pattern")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ============================================================
# 13. BUSINESS ANALYSIS
# ============================================================

total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()

print("\n")
print("=" * 60)
print("SALES DATA ANALYSIS - BUSINESS SUMMARY")
print("=" * 60)

print("\nTotal Revenue:")
print(f"${total_sales:,.2f}")

print("\nAverage Sale:")
print(f"${average_sales:,.2f}")


# ------------------------------------------------------------
# QUESTION 1: WHICH REGION PERFORMS BEST?
# ------------------------------------------------------------

print("\n1. Which region performs best?")

print(
    f"The {best_region['Region']} region performs best "
    f"with total sales of "
    f"${best_region['Sales']:,.2f}."
)


# ------------------------------------------------------------
# QUESTION 2: SEASONAL TRENDS?
# ------------------------------------------------------------

print("\n2. What are the seasonal trends?")

print(
    f"The highest sales were recorded in "
    f"{best_month['Month_Name']} with sales of "
    f"${best_month['Sales']:,.2f}."
)


# ------------------------------------------------------------
# QUESTION 3: WHICH PRODUCT DRIVES REVENUE?
# ------------------------------------------------------------

print("\n3. Which product drives revenue?")

print(
    f"{best_product['Product']} is the highest "
    f"revenue-generating product with total sales of "
    f"${best_product['Sales']:,.2f}."
)


# ============================================================
# 14. PRODUCT REVENUE SHARE
# ============================================================

product_share = (
    product_sales.copy()
)

product_share["Percentage"] = (
    product_share["Sales"] /
    product_share["Sales"].sum()
) * 100

print("\nProduct Revenue Share")
print(product_share)


# ============================================================
# 15. SAVE CLEANED DATA AND RESULTS
# ============================================================

df.to_csv(
    "sales_data_cleaned.csv",
    index=False
)

monthly_sales.to_csv(
    "monthly_sales.csv",
    index=False
)

region_sales.to_csv(
    "region_sales.csv",
    index=False
)

product_sales.to_csv(
    "product_sales.csv",
    index=False
)

seasonal_sales.to_csv(
    "seasonal_sales.csv",
    index=False
)

print("\n")
print("=" * 60)
print("FILES SAVED SUCCESSFULLY")
print("=" * 60)

print("1. sales_data_raw.csv")
print("2. sales_data_cleaned.csv")
print("3. monthly_sales.csv")
print("4. region_sales.csv")
print("5. product_sales.csv")
print("6. seasonal_sales.csv")

print("\nAnalysis Completed Successfully!")