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
global pcheck
global m
global mcheck
global m2
global m2check
global m3
global m3check
global m4
global m4check
class Teambuilder():
    def pickpokemon():
        p = True
        pcheck = True
        while p == True:
                playerpokemon = input("Type pokemon here ")
                for i in range(len(data)):
                    if playerpokemon == data[i]["Name"]:
                        if len(playerteam) == 0:
                            playerteam.append(playerpokemon)
                            pokemonnumber = i
                            pknumber[0] = (pokemonnumber)
                            p = False
                        if len(playerteam) != 0 or len(playerteam) != 1:
                            for i in range(len(playerteam)):
                                playerteam.append(playerpokemon)
                                pokemonnumber = i
                                pknumber[0] = pokemonnumber
                                if playerpokemon == playerteam[i]:
                                    pcheck = False
                            if pcheck == True:
                                p = False
    def pickmove():
        currentpkmoves = []
        m = True
        while m == True:
            move = input("Type move here ")
            for i in range(len(data[pknumber[0]]["Learnable Moves"])):
                if move == data[pknumber[0]]["Learnable Moves"][i]:
                    currentpkmoves.append(move)
                    m = False
        m2 = True
        while m2 == True:
            move2 = input("Type move here ")
            for i in range(len(data[pknumber[0]]["Learnable Moves"])):
                if move2 == data[pknumber[0]]["Learnable Moves"][i]:
                    currentpkmoves.append(move2)
                    m2 = False
        m3 = True
        while m3 == True:
            move3 = input("Type move here ")
            for i in range(len(data[pknumber[0]]["Learnable Moves"])):
                if move3 == data[pknumber[0]]["Learnable Moves"][i]:
                    currentpkmoves.append(move3)
                    m3 = False
        m4 = True
        while m4 == True:
            move4 = input("Type move here ")
            for i in range(len(data[pknumber[0]]["Learnable Moves"])):
                if move4 == data[pknumber[0]]["Learnable Moves"][i]:
                    currentpkmoves.append(move4)
                    m4 = False
        pokemonmoves.append(currentpkmoves)
    def teambuilder(self):
        for i in range(5):
            print(allpokemon)
            Teambuilder.pickpokemon()
            print(data[pknumber[0]]["Learnable Moves"])
            Teambuilder.pickmove()

tb = Teambuilder()
tb.teambuilder()


print(playerteam)
print(pokemonmoves)



