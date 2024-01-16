import json
import os
test = open("data.json", encoding="utf8")
data = json.load(test)
moveamount = [4]
pknumber = [0]
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
global twomove
global onemove
global threemove
class Teambuilder():
    def pickpokemon():
        p = True
        pcheck = True
        twomove = False
        onemove = False
        threemove = False
        while p == True:
            playerpokemon = input("Type pokemon here ")
            if playerpokemon == "Magikarp":
                moveamount[0] = 2
                twomove = True
            if playerpokemon == "Caterpie":
                moveamount[0] = 2
                twomove = True
            if playerpokemon == "Metapod":
                moveamount[0] = 3
                threemove = True
            if playerpokemon == "Weedle":
                moveamount[0] = 2
                twomove = True
            if playerpokemon == "Kakuna":
                moveamount[0] = 3
                threemove = True
            if playerpokemon == "Ditto":
                moveamount[0] = 1
                onemove = True
            if twomove == False and onemove == False and threemove == False:
                moveamount[0] = 4
            for i in range(len(data)):
                if playerpokemon == data[i]["Name"]:
                    if len(playerteam) != 0:
                        pcheck = not playerpokemon in playerteam
                        if pcheck == True:
                            playerteam.append(playerpokemon)
                            pokemonnumber = i
                            pknumber[0] = (pokemonnumber)
                            p = False
                    if len(playerteam) == 0:
                        playerteam.append(playerpokemon)
                        pokemonnumber = i
                        pknumber[0] = (pokemonnumber)
                        p = False
    def pickmove():
        currentpkmoves = []
        if moveamount[0] == 4:
            m = True
            m2 = True
            m3 = True
            m4 = True
        if moveamount[0] == 3:
            m = True
            m2 = True
            m3 = True
            m4 = False
        if moveamount[0] == 2:
            m = True
            m2 = True
            m3 = False
            m4 = False
        if moveamount[0] == 1:
            m = True
            m2 = False
            m3 = False
            m4 = False
        while m == True:
            move = input("Type move here ")
            for i in range(len(data[pknumber[0]]["Learnable Moves"])):
                if move == data[pknumber[0]]["Learnable Moves"][i]:
                    currentpkmoves.append(move)
                    m = False

        while m2 == True:
            move2 = input("Type move here ")
            for i in range(len(data[pknumber[0]]["Learnable Moves"])):
                if move2 == data[pknumber[0]]["Learnable Moves"][i]:
                    m2check = not move2 in currentpkmoves
                    if m2check == True:
                        currentpkmoves.append(move2)
                        m2 = False

        while m3 == True:
            move3 = input("Type move here ")
            for i in range(len(data[pknumber[0]]["Learnable Moves"])):
                if move3 == data[pknumber[0]]["Learnable Moves"][i]:
                    m3check = not move3 in currentpkmoves
                    if m3check == True:
                        currentpkmoves.append(move3)
                        m3 = False

        while m4 == True:
            move4 = input("Type move here ")
            for i in range(len(data[pknumber[0]]["Learnable Moves"])):
                if move4 == data[pknumber[0]]["Learnable Moves"][i]:
                    m4check = not move4 in currentpkmoves
                    if m4check == True:
                        currentpkmoves.append(move4)
                        m4 = False
        pokemonmoves.append(currentpkmoves)
    def teambuilder(self):
        for i in range(6):
            print(allpokemon)
            Teambuilder.pickpokemon()
            print(data[pknumber[0]]["Learnable Moves"])
            Teambuilder.pickmove()
        with open("playerteaminfo.json", "r") as f:
            playerteamjson = json.load(f)
            teaminfo = (playerteam[0], pokemonmoves[0], playerteam[1], pokemonmoves[1], playerteam[2], pokemonmoves[2], playerteam[3], pokemonmoves[3], playerteam[4], pokemonmoves[4], playerteam[5], pokemonmoves[5])
            playerteamjson.append({"First Pokemon":playerteam[0], "First Pokemon's Moves":pokemonmoves[0], "Second Pokemon":playerteam[1], "Second Pokemon's Moves":pokemonmoves[1], "Third Pokemon":playerteam[2], "Third Pokemon's Moves":pokemonmoves[2], "Fourth Pokemon":playerteam[3], "Fourth Pokemon's Moves":pokemonmoves[3], "Fifth Pokemon":playerteam[4], "Fifth's Pokemon's Moves":pokemonmoves[4], "Sixth Pokemon":playerteam[5], "Sixth Pokemon's Moves":pokemonmoves[5]})
        new_file = "playerteaminfo.json"
        with open(new_file, "w") as f:
            json_string = json.dumps(teaminfo, indent=4)
            f.write(json_string)






