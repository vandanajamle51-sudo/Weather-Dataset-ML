import pandas as pd

data = pd.read_csv("weather.csv")

print("Weather Dataset")
print(data.head())

print("\nDataset Information:")
print(data.info())

print("\nStatistical Summary:")
print(data.describe())
