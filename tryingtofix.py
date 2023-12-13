import json
test = open("data.json", encoding="utf8")
data = json.load(test)
pknumber = [1]
playerteam = []
pokemonmoves = []
global p
global m
class Teambuilder():
    def pickpokemon(self, playerpokemon):
        self.playerpokemon = playerpokemon
        p = True
        while p == True:
            playerpokemon = input("Type pokemon here ")
            for i in range(len(data)):
                if playerpokemon == data[i]["Name"]:
                    playerteam.append(playerpokemon)
                    pokemonnumber = i
                    pknumber.replace(pokemonnumber)
                    p = False
    pickpokemon()
    def pickmove():
        m = True
        while m == True:
            move = input("Type moves here ")
            for i in range(len(data[pknumber[0]]["Learnable Moves"])):
                if move == data[pknumber[0]]["Learnable Moves"][i]:
                    pokemonmoves.append(move)
                    m = False
Teambuilder.pickpokemon()
print(playerteam)
print(pokemonmoves)



