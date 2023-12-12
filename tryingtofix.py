import json
test = open("data.json", encoding="utf8")
data = json.load(test)
playerteam = []
pokemonmoves = []
global pokemonnumber
global p
def pickpokemon():
    p = True
    while p == True:
        pokemon = input("Type pokemon here ")
        for i in range(len(data)):
            if pokemon == (data[i]["Name"]):
                playerteam.append(pokemon)
                pokemonnumber = i
                p = False
pickpokemon()
global m
def pickmove():
    m = True
    while m == True:
        move = input("Type moves here")
        for i in range(len(data)[pokemonnumber]["Learnable Moves"]):
            if move == (data[pokemonnumber]["Learnable Moves"]):
                pokemonmoves.append(move)
                m = False
pickmove()
print(playerteam)
print(pokemonmoves)




