# Fix matplotlib backend issue (prevents Tkinter errors)
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
print("\nLoading dataset...")

df = pd.read_csv("Cannabis_Retail_Sales_by_Week_Ending.csv")

print("\nPreview of dataset:")
print(df.head())

# -----------------------------
# Data Cleaning
# -----------------------------
print("\nCleaning data...")

# Convert date column
df["Week Ending"] = pd.to_datetime(df["Week Ending"])

# Sort data by date
df = df.sort_values("Week Ending")

# -----------------------------
# Total Sales Trend
# -----------------------------
print("\nGenerating Total Sales Trend graph...")

plt.figure(figsize=(10,5))

plt.plot(df["Week Ending"], df["Total Adult-Use and Medical Sales"])

plt.title("Total Cannabis Sales Over Time")
plt.xlabel("Week")
plt.ylabel("Total Sales")

plt.grid(True)

plt.tight_layout()
plt.savefig("total_sales_trend.png")
plt.close()

# -----------------------------
# Adult vs Medical Sales
# -----------------------------
print("Generating Adult vs Medical Sales graph...")

plt.figure(figsize=(10,5))

plt.plot(df["Week Ending"], df["Adult-Use Retail Sales"], label="Adult Use")
plt.plot(df["Week Ending"], df["Medical Marijuana Retail Sales"], label="Medical")

plt.title("Adult vs Medical Cannabis Sales")
plt.xlabel("Week")
plt.ylabel("Sales")

plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("adult_vs_medical_sales.png")
plt.close()

# -----------------------------
# Product Sales Trend
# -----------------------------
print("Generating Product Sales Trend graph...")

plt.figure(figsize=(10,5))

plt.plot(df["Week Ending"], df["Total Products Sold"])

plt.title("Total Cannabis Products Sold Over Time")
plt.xlabel("Week")
plt.ylabel("Products Sold")

plt.grid(True)

plt.tight_layout()
plt.savefig("product_sales_trend.png")
plt.close()

# -----------------------------
# Average Price Trend
# -----------------------------
print("Generating Price Trend graph...")

plt.figure(figsize=(10,5))

plt.plot(df["Week Ending"], df["Adult-Use Average Product Price"], label="Adult Price")
plt.plot(df["Week Ending"], df["Medical Average Product Price"], label="Medical Price")

plt.title("Average Cannabis Product Price Trend")
plt.xlabel("Week")
plt.ylabel("Price")

plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("price_trend.png")
plt.close()

# -----------------------------
# Summary Statistics
# -----------------------------
print("\nSummary Statistics:")
print(df.describe())

# -----------------------------
# Basic Insights
# -----------------------------
print("\nKey Insights:")

avg_adult_sales = df["Adult-Use Retail Sales"].mean()
avg_medical_sales = df["Medical Marijuana Retail Sales"].mean()

print(f"Average Adult-Use Sales: ${avg_adult_sales:,.2f}")
print(f"Average Medical Sales: ${avg_medical_sales:,.2f}")

if avg_adult_sales > avg_medical_sales:
    print("Adult-use cannabis sales dominate the market compared to medical sales.")

avg_products = df["Total Products Sold"].mean()
print(f"Average Weekly Products Sold: {avg_products:,.0f}")

print("\nGraphs saved successfully!")
print("Check your project folder for the generated PNG files.")