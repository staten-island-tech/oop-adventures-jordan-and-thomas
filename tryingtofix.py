import json
test = open("data.json", encoding="utf8")
data = json.load(test)
pknumber = []
playerteam = []
pokemonmoves = []
global p
def pickpokemon():
    p = True
    pokemonnumber = 1
    while p == True:
        pokemon = input("Type pokemon here ")
        for i in range(len(data)):
            if pokemon == (data[i]["Name"]):
                playerteam.append(pokemon)
                pokemonnumber == i
                pknumber.append(pokemonnumber)
                p = False
pickpokemon()
global m
def pickmove():
    m = True
    while m == True:
        move = input("Type moves here ")
        for i in range(len(data)[pknumber[0]]["Learnable Moves"]):
            if move == (data[pknumber[0]]["Learnable Moves"]):
                pokemonmoves.append(move)
                m = False
pickmove()
print(playerteam)
print(pokemonmoves)




