# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#
#
#     for row in data:
#         if row[1] != ("temp"):
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
# print(type(data["temp"]))

# data_dict = data.to_dict() # DataFrame operasyonu
# print(data_dict)

# temp_list = data["temp"].to_list() # Series operasyonu
# mean_temp = data["temp"].mean()
# max_temp = data["temp"].max()


# get data in columns
# print(data.condition)


# get data in rows
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
#
# print((monday.temp)*1.8+32)

# Create a DataFrame from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251205.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels)
print(red_squirrels)
print(black_squirrels)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon, "Black"]",
    "Count" : [grey_squirrels, red_squirrels, black_squirrels]
}

df = pd.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")


