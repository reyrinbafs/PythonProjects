
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data["Primary Fur Color"])


gray_squ_count = len(data[data["Primary Fur Color"] == "Gray"])
cin_squ_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
bl_squ_count = len(data[data["Primary Fur Color"] == "Black"])

dict = {
    "fur color": ["grey", "Cinnamon", "black"],
    "count": [gray_squ_count, cin_squ_count, bl_squ_count]
}

df = pandas.DataFrame(dict)
df.to_csv("squirrel_count")
