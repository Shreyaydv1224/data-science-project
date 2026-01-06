import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
df = pd.read_csv("sales.csv")

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract month name
df['Month'] = df['Date'].dt.month_name()

# Group by month and sum sales
monthly_sales = df.groupby('Month')['Sales'].sum()

# Output
print("Monthly Sales:")
print(monthly_sales)
print("\nBest Month:", monthly_sales.idxmax())
print("Worst Month:", monthly_sales.idxmin())

# Plot
monthly_sales.plot(marker='o')
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Trend")
plt.show()
