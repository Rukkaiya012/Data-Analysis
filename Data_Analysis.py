
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print("\n🔹 First 5 rows of the data:")
print(df.head())

print("\n🔹 Data Info:")
print(df.info())

print("\n🔹 Summary Statistics:")
print(df.describe())

total_sales = df['Sales'].sum()
print(f"\n💰 Total Sales: {total_sales}")

sales_by_category = df.groupby('Category')['Sales'].sum()
print("\n📊 Sales by Category:")
print(sales_by_category)

plt.figure(figsize=(8,5))
sales_by_category.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Sales by Category", fontsize=14)
plt.ylabel("Total Sales", fontsize=12)
plt.xlabel("Category", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  
    monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Sales'].sum()

    plt.figure(figsize=(8,5))
    monthly_sales.plot(kind='line', marker='o', color='green')
    plt.title("Monthly Sales Trend", fontsize=14)
    plt.ylabel("Sales", fontsize=12)
    plt.xlabel("Month", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
else:
    print("\n⚠ No 'Date' column found. Skipping monthly sales trend chart.")
