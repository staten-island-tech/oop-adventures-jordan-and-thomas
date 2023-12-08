import json
test = open("data.json", encoding="utf8")
data = json.load(test)
playerteam = []
global x
x = True
while x == True:
    firstpokemon = input("Type pokemon here ")
    for i in range(len(data)):
        if firstpokemon == (data[i]["Name"]):
            playerteam.append(firstpokemon)
            x = False
print(playerteam)