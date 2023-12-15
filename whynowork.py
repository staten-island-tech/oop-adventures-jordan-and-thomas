import json
test = open("data.json", encoding="utf8")
data = json.load(test)
pknumber = []
playerteam = []
pokemonmoves = []
global p
def pickpokemon():
    p = True
    while p == True:
        pokemon = input("Type pokemon here ")
        for i in range(len(data)):
            if pokemon == (data[i]["Name"]):
                playerteam.append(pokemon)
                pokemonnumber = i
                pknumber.append(pokemonnumber)
                p = False
pickpokemon()
print(data[pknumber[0]]["Learnable Moves"])