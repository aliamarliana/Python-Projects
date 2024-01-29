import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  # Read data from file
  df = pd.read_csv("epa-sea-level.csv")

  # Create scatter plot
  plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

  # Calculate line of best fit for all data (once for efficiency)
  slope, intercept, r_value, p_value, std_err = linregress(
      df["Year"], df["CSIRO Adjusted Sea Level"])

  # Plot first line of best fit (all data)
  x1 = df["Year"]
  y1 = intercept + slope * x1
  plt.plot(x1, y1, color="red", label="Line of Best Fit (All Data)")

  # Plot extension of first line to 2050
  x2 = 2050
  y2 = intercept + slope * x2
  plt.plot(x2, y2, color="red", linestyle="--")

  # Plot second line of best fit (since 2000)
  df_recent = df[df["Year"] >= 2000]
  x3 = df_recent["Year"]
  y3 = intercept + slope * x3
  plt.plot(x3, y3, color="blue", label="Line of Best Fit (Since 2000)")

  # Plot extension of second line to 2050
  x4 = 2050
  y4 = intercept + slope * x4
  plt.plot(x4, y4, color="blue", linestyle="--")

  # Add labels and title
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  plt.title("Rise in Sea Level")
  plt.legend()
  plt.grid(True)
  plt.show()

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
