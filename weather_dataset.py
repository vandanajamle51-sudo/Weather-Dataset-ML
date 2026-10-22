import statistics

data = {
    "Temperature": [25, 28, 30, 22, 27, 31, 24, 29],
    "Humidity": [60, 55, 50, 75, 65, 45, 80, 58],
    "Wind_Speed": [10, 12, 8, 15, 11, 9, 14, 7],
    "Weather": ["Sunny", "Sunny", "Sunny", "Rainy", "Cloudy", "Sunny", "Rainy", "Cloudy"]
}

print("Weather Dataset")
for i in range(len(data["Temperature"])):
    print(data["Temperature"][i], data["Humidity"][i],
          data["Wind_Speed"][i], data["Weather"][i])

print("\nAverage Temperature:", statistics.mean(data["Temperature"]))
print("Average Humidity:", statistics.mean(data["Humidity"]))
print("Average Wind Speed:", statistics.mean(data["Wind_Speed"]))

print("\nWeather Distribution")
for condition in set(data["Weather"]):
    print(condition, ":", data["Weather"].count(condition))
