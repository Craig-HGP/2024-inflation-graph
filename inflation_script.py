import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Year": [i for i in range(1929, 2024)],
    "Inflation Rate YOY": [0.6, -6.4, -9.3, -10.3, 0.8, 1.5, 3.0, 1.4, 2.9, -2.8, 0.0, 0.7, 9.9, 9.0, 3.0, 2.3, 2.2, 18.1, 8.8, 3.0, -2.1, 5.9, 6.0, 0.8, 0.7, -0.7, 0.4, 3.0, 2.9, 1.8, 1.7, 1.4, 0.7, 1.3, 1.6, 1.0, 1.9, 3.5, 3.0, 4.7, 6.2, 5.6, 3.3, 3.4, 8.7, 12.3, 6.9, 4.9, 6.7, 9.0, 13.3, 12.5, 8.9, 3.8, 3.8, 3.9, 3.8, 1.1, 4.4, 4.4, 4.6, 6.1, 3.1, 2.9, 2.7, 2.7, 2.5, 3.3, 1.7, 1.6, 2.7, 3.4, 1.6, 2.4, 1.9, 3.3, 3.4, 2.5, 4.1, 0.1, 2.7, 1.5, 3.0, 1.7, 1.5, 0.8, 0.7, 2.1, 2.1, 1.9, 2.3, 1.4, 7.0, 6.5, 3.4],
    "Federal Funds Rate": [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 1.25, 2.5, 3.0, 3.0, 3.0, 3.75, 4.25, 5.5, 4.5, 6.0, 9.0, 5.0, 5.75, 9.0, 8.0, 4.75, 4.75, 6.5, 10.0, 12.0, 18.0, 12.0, 8.5, 9.25, 8.25, 7.75, 6.0, 6.75, 9.75, 8.25, 7.0, 4.0, 3.0, 3.0, 5.5, 5.5, 5.25, 6.5, 1.75, 1.25, 1.0, 2.25, 4.25, 5.25, 4.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.75, 1.5, 2.5, 1.75, 0.25, 0.25, 4.5, 5.5],
}

# Verify that all lists are of the same length
min_length = min(len(data["Year"]), len(data["Inflation Rate YOY"]), len(data["Federal Funds Rate"]))
data["Year"] = data["Year"][:min_length]
data["Inflation Rate YOY"] = data["Inflation Rate YOY"][:min_length]
data["Federal Funds Rate"] = data["Federal Funds Rate"][:min_length]

# Create a DataFrame
df = pd.DataFrame(data)

# Plot the data
fig, ax1 = plt.subplots(figsize=(16, 9))

# Plot Inflation Rate YOY
ax1.plot(df["Year"], df["Inflation Rate YOY"], color="red", label="Inflation Rate YOY")
ax1.set_ylabel("Inflation Rate YOY (%)", color="red")
ax1.tick_params(axis="y", labelcolor="red")
ax1.set_xlabel("Year")

# Plot Federal Funds Rate on secondary y-axis
ax2 = ax1.twinx()
ax2.plot(df["Year"], df["Federal Funds Rate"], color="blue", label="Federal Funds Rate")
ax2.set_ylabel("Federal Funds Rate (%)", color="blue")
ax2.tick_params(axis="y", labelcolor="blue")

# Add title and grid
plt.title("U.S. Inflation Rate and Federal Funds Rate (1929-2023)", fontsize=16)
ax1.grid(alpha=0.3)

# Add a legend
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))

# Show the plot
plt.tight_layout()
plt.show()
