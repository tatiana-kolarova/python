import json

alice = []
characters = []
dictionary = {}
count = 0

with open("alice.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        alice.append(line)

for line in alice:
    for character in line:
        if character.isalpha():
            character = character.lower()
        if character != " ":
            characters.append(character)

for i in characters:
    if i not in dictionary.keys():
        count = characters.count(i)
        dictionary[i] = count

dictionary = dict(sorted(dictionary.items()))

with open("hw01_output.json", mode="w", encoding="utf-8") as file:
    json.dump(dictionary, file, ensure_ascii=False, indent=4)
