import json

data = []

with open("netflix_titles.tsv", mode="r", encoding="utf-8") as file:
    for line in file:
        data.append(line.strip().split("\t"))

header = data[0]
data = data[1:]

primary_title_index = header.index("PRIMARYTITLE")
director_index = header.index("DIRECTOR")
cast_index = header.index("CAST")
genre_index = header.index("GENRES")
startyear_index = header.index("STARTYEAR")

keys = ["title", "directors", "cast", "genres", "decade"]
values = [primary_title_index, director_index,
          cast_index, genre_index, startyear_index]
list = []

for line in data:
    slovnik = {}
    for i in range(len(keys)):
        if line[values[i]]:
            if keys[i] == "title":
                slovnik[keys[i]] = "".join(line[values[i]])
            elif keys[i] == "decade":
                slovnik[keys[i]] = line[values[i]][:3]+'0'
            else:
                slovnik[keys[i]] = line[values[i]].split(", ")
        else:
            slovnik[keys[i]] = []
    list.append(slovnik)

with open("hw02_output.json", mode="w", encoding="utf-8") as output_file:
    json.dump(list, output_file, indent=4, ensure_ascii=False)

