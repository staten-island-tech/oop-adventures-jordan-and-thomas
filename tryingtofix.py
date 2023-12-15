import json
test = open("data.json", encoding="utf8")
data = json.load(test)
pknumber = [1]
playerteam = []
pokemonmoves = []
allpokemon = []
for i in range(len(data)):
            allpokemon.append(data[i]["Name"])
global p
global m
global m2
global m3
global m4
class Teambuilder():
    def pickpokemon(playerpokemon):
        p = True
        while p == True:
            for i in range(len(data)):
                if playerpokemon == data[i]["Name"]:
                    playerteam.append(playerpokemon)
                    pokemonnumber = i
                    pknumber[0] = (pokemonnumber)
                    p = False
    def pickmove(move):
        currentpkmoves = []
        m = True
        while m == True:
            for i in range(len(data[pknumber[0]]["Learnable Moves"])):
                if move == data[pknumber[0]]["Learnable Moves"][i]:
                    currentpkmoves.append(move)
                    m = False
        m2 = True
        move2 = input("Type move here ")
        while m2 == True:
            for i in range(len(data[pknumber[0]]["Learnable Moves"])):
                if move2 == data[pknumber[0]]["Learnable Moves"][i]:
                    currentpkmoves.append(move2)
                    m2 = False
        m3 = True
        move3 = input("Type move here ")
        while m3 == True:
            for i in range(len(data[pknumber[0]]["Learnable Moves"])):
                if move3 == data[pknumber[0]]["Learnable Moves"][i]:
                    currentpkmoves.append(move3)
                    m3 = False
        m4= True
        move4 = input("Type move here ")
        while m4 == True:
            for i in range(len(data[pknumber[0]]["Learnable Moves"])):
                if move4 == data[pknumber[0]]["Learnable Moves"][i]:
                    currentpkmoves.append(move4)
                    m4 = False
        pokemonmoves.append(currentpkmoves)
    def teambuilder(self):
            print(allpokemon)
            inputpokemon = input("Type pokemon here ")
            Teambuilder.pickpokemon(inputpokemon)
            print(data[pknumber[0]]["Learnable Moves"])
            inputmove = input("Type move here ")
            Teambuilder.pickmove(inputmove)

tb = Teambuilder()
tb.teambuilder()


print(playerteam)
print(pokemonmoves)



