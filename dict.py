Colors = {"Sam": "Blue", "Amy": "Red", "Sarah": "Yellow"}
letter = {}
stings = "test string"

print(Colors["Sarah"])

print(Colors.keys())

for Item in Colors.keys():
    print("{0} предпочитает цвет {1}.".format(Item, Colors[Item]))
for letters in stings:
    if letter.get(letters, 0) > 0:
        letter[letters] = letter[letters] + 1
    else:
        letter.update({letters: 1})

print(letter)

Colors["Sarah"] = "Purple"
Colors.update({"Harry": "Orange"})

del Colors["Sam"]

print(Colors)