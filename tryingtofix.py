import json
test = open("data.json", encoding="utf8")
data = json.load(test)
playerteam = []
pokemonmoves = []
global p
p = True
def pickpokemon():
    while p == True:
        pokemon = input("Type pokemon here ")
        for i in range(len(data)):
            if pokemon == (data[i]["Name"]):
                playerteam.append(pokemon)
                p = False
global m
m = True
def pickmove():
    while m == True:
        moves = input("")

