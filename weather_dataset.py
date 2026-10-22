import pandas as pd

data = {
    "Temperature": [25, 28, 30, 22, 27, 31, 24, 29],
    "Humidity": [60, 55, 50, 75, 65, 45, 80, 58],
    "Wind_Speed": [10, 12, 8, 15, 11, 9, 14, 7],
    "Weather": ["Sunny", "Sunny", "Sunny", "Rainy", "Cloudy", "Sunny", "Rainy", "Cloudy"]
}

df = pd.DataFrame(data)

print("Weather Dataset")
print(df)

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

print("\nWeather Distribution")
print(df["Weather"].value_counts())
