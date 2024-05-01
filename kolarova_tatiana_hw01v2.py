import json

alice = []
dictionary = {}

with open("alice.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        alice.append(line)

for line in alice:
    for character in line:
        if character.isalpha():
            character = character.lower()
        if character != " ":
            if character in dictionary:
                dictionary[character] += 1
            else:
                dictionary[character] = 1

dictionary = dict(sorted(dictionary.items()))

with open("hw01_output.json", mode="w", encoding="utf-8") as file:
    json.dump(dictionary, file, ensure_ascii=False, indent=4)
