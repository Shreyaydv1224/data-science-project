import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("intraday.csv")

# -----------------------------
# Returns Calculation
# -----------------------------
df['Return'] = df['Close'].pct_change()

# -----------------------------
# Volatility Clustering (Rolling Std)
# -----------------------------
df['Volatility'] = df['Return'].rolling(window=3).std()

# -----------------------------
# Moving Averages
# -----------------------------
df['SMA_3'] = df['Close'].rolling(3).mean()
df['SMA_5'] = df['Close'].rolling(5).mean()

# -----------------------------
# Drawdown Calculation
# -----------------------------
df['Cumulative_Max'] = df['Close'].cummax()
df['Drawdown'] = (df['Close'] - df['Cumulative_Max']) / df['Cumulative_Max']

# -----------------------------
# PRICE + MOVING AVERAGE PLOT
# -----------------------------
plt.figure()
plt.plot(df['Close'], label='Price')
plt.plot(df['SMA_3'], label='SMA 3')
plt.plot(df['SMA_5'], label='SMA 5')
plt.title("Price & Moving Average Analysis")
plt.legend()
plt.show()

# -----------------------------
# VOLATILITY PLOT
# -----------------------------
plt.figure()
plt.plot(df['Volatility'])
plt.title("Volatility Clustering")
plt.show()

# -----------------------------
# VOLUME SPIKE ANALYSIS
# -----------------------------
plt.figure()
plt.bar(df.index, df['Volume'])
plt.title("Intraday Volume Spikes")
plt.show()

# -----------------------------
# RETURN DISTRIBUTION
# -----------------------------
plt.figure()
plt.hist(df['Return'].dropna(), bins=10)
plt.title("Intraday Return Distribution")
plt.show()

# -----------------------------
# DRAWDOWN PLOT
# -----------------------------
plt.figure()
plt.plot(df['Drawdown'])
plt.title("Drawdown Analysis")
plt.show()

# -----------------------------
# Final Outputs
# -----------------------------
print("Maximum Drawdown:", df['Drawdown'].min())
print("Price-Volume Correlation:",
      df['Return'].corr(df['Volume']))
