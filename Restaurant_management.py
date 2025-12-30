import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Creating restaurant order data 
data = {
    "Order_ID":[101, 102, 103, 104, 105],
    "Item":["Pizza", "Burger", "Pasta", "Pizza","Burger"],
} 
df = pd.DataFrame(data)
df
df["Total_Bill"] = df["Quantity"]*df["Price"]
df
#Total revenue using NumPy
total_revenue = np.sum(df["Total_Bill"])
print("Total Revenue:₹",total_revenue)
menu_sales = df.groupby("Item")
["Total_Bill"].sum()
print(menu_sales)
plt.figure()
menu_sales.plot(kind='bar')
plt.title("Menu Item Revenue")
plt.xlabel("Found Item")
plt.ylabel("Revenue(₹)")
plt.show()
quantity_sold = df.groupby("Item")
["Quantity"].sum()

plt.figure()
plt.pie(quantity_sold,
labels=quantity_sold.index,autopct='%1.1f%%')
plt.title("Customer Prefernce by Quantity")
plt.show()