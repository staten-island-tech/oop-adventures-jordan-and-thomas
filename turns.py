import json

import time
from tryingtofix import Teambuilder
times = 1.5
import random
import decimal
from decimal import Decimal
global turn
turn = 1
#going = "You"

test = open("moves.json", encoding="utf8")
moves = json.load(test)
movelist = len(moves)

quiz = open("data.json", encoding="utf8")
data = json.load(quiz)
pokemonlist = len(data)

pluh = open("playerteaminfo.json", encoding="utf8")
inputteam = json.load(pluh)
inputteamlist = len(inputteam)
global unique
unique = ["nah", "id", "win"]
typeeffect = ["Surfer", "Rosa"]
global stab
stab = False
global meffective1
meffective1 = 1
global meffective2
meffective2 = 1
global meffective
meffective = 1
global twotype
twotype = False
global onetype
onetype = False
endofturn = "no"
global pokemonin
pokemonin = "same"
global enemyin
enemyin = "same"
global itch
itch = False
global Kaifat
Kaifat = "very"
global enemytypes
#enemyhealth = 200
#Pokemon.teambuilder()

#global enemypokemon
global enemyspeed
global enemyhealth
enemypokemon = "Raichu"

for i in range(len(data)):
    if enemypokemon == data[i]["Name"]:
        enemyspeed = data[i]["Speed Stat"]
        enemyhealth = data[i]["Health Stat"]
tb = Teambuilder()
tb.teambuilder()
pluh = open("playerteaminfo.json", encoding="utf8")
inputteam = json.load(pluh)
inputteamlist = len(inputteam)
enemyparty = ["Raichu", ["Toxic", "Double Team", "Thunderbolt", "Surf"]]
yourteam = [inputteam[0], inputteam[2], inputteam[4], inputteam[6], inputteam[8], inputteam[10]]
userpartystatus = [inputteam[0], "none", inputteam[2], "none", inputteam[4], "none", inputteam[6], "none", inputteam[8], "none", inputteam[10], "none"]
eliteteamstatus = ["Raichu", "none"]
for i in range(pokemonlist):
    if inputteam[0] == data[i]["Name"]:
        global firstpkhealth
        firstpkhealth = data[i]["Health Stat"]
    if inputteam[2] == data[i]["Name"]:
        global secondpkhealth
        secondpkhealth = data[i]["Health Stat"]
    if inputteam[4] == data[i]["Name"]:
        global thirdpkhealth
        thirdpkhealth = data[i]["Health Stat"]
    if inputteam[6] == data[i]["Name"]:
        global fourthpkhealth
        fourthpkhealth = data[i]["Health Stat"]
    if inputteam[8] == data[i]["Name"]:
        global fifthpkhealth
        fifthpkhealth = data[i]["Health Stat"]
    if inputteam[10] == data[i]["Name"]:
        global sixthpkhealth
        sixthpkhealth = data[i]["Health Stat"]
userpartyhealth = [inputteam[0], firstpkhealth, inputteam[2], secondpkhealth, inputteam[4], thirdpkhealth, inputteam[6], fourthpkhealth, inputteam[8], fifthpkhealth, inputteam[10], sixthpkhealth]
enemypartyhealth = ["Raichu", 230]
firstpokemon = inputteam[0]
global currentpokemon
currentpokemon = firstpokemon
global currentspeed
global currenthealth
for i in range(len(data)):
    if currentpokemon == data[i]["Name"]:
        currentspeed = data[i]["Speed Stat"]
        currenthealth = data[i]["Health Stat"]
pknumber = [1]
playerteam = []
pokemonmoves = []
allpokemon = []
for i in range(len(data)):
            allpokemon.append(data[i]["Name"])



yourdeadguys = []
Mikesdeadguys = []
#yourteam = [teaminfo[0], teaminfo[2], teaminfo[4], teaminfo[6], teaminfo[8], teaminfo[10]]
currentpokemon = yourteam[0]    


endofturn = "no"

pokemonin = "same"

enemyin = "same"


#enemyhealth = 200
#Pokemon.teambuilder()


#enemypokemon = "Raichu"
#enemypokemon = enemypokemon






class functionality():
    def oppositehealththing(going, enemyhealth, currenthealth):
        global oppositehealth
        if going == "You":
            oppositehealth = enemyhealth
        if going == "Enemy":
            oppositehealth = currenthealth


    def oppositepokemon(going, currentpokemon, enemypokemon):
        global oppositepokemon
        if going == "You":
            oppositepokemon = enemypokemon
        if going == "Enemy":
            oppositepokemon = currentpokemon

    def afflicted(oppositepokemon, oppositehealth, pokemonin, endofturn, turn):

        if pokemonin == "afflicted":
            if endofturn == "end":
                N = 1
                damage = N * oppositehealth/16
                if turn + 1:
                    N += 1

    def dead(oppositehealth, oppositepokemon):
        if oppositehealth == 0:
            if going == "Enemy":
                global currentpokemon
                yourdeadguys.append(currentpokemon)

                print(oppositepokemon, "has fainted")

                print(yourteam)
                switchin = input("Pick a Pokemon to switch in: ")
                if switchin in yourdeadguys or switchin not in yourteam:
                    print(switchin, "has already fainted")
                    switchin = input("Pick a Pokemon to switch in to:")
                currentpokemon = switchin
            if going == "You":
                Mikesdeadguys.append(oppositepokemon)
                #switch in good


    def supereffective(supereffective, use, ptype):
        global effective
        effective = "normal"
        for i in range(movelist):
            if (moves[i]["name"]) == use:
                usetype = (moves[i]["type"])



        if usetype == "Normal" and "Rock" == ptype or usetype == "Normal" and " Rock" == ptype:
            effective = "half"
        if usetype == "Normal" and "Ghost" == ptype or usetype == "Normal" and " Ghost" == ptype:
            effective = "zero"

        if usetype == "Fire" and "Fire" == ptype or usetype == "Fire" and " Fire" == ptype:
            effective = "half"
        if usetype == "Fire" and "Water" == ptype or usetype == "Fire" and " Water" == ptype:
            effective = "half"
        if usetype == "Fire" and "Grass" == ptype or usetype == "Fire" and " Grass" == ptype:
            effective = "super"
        if usetype == "Fire" and "Ice" == ptype or usetype == "Fire" and " Ice" == ptype:
            effective = "super"
        if usetype == "Fire" and "Bug" == ptype or usetype == "Fire" and " Bug" == ptype:
            effective = "super"
        if usetype == "Fire" and "Rock" == ptype or usetype == "Fire" and " Rock" == ptype:
            effective = "half"
        if usetype == "Fire" and "Dragon" == ptype or usetype == "Fire" and " Dragon" == ptype:
            effective = "half"

        if usetype == "Water" and "Fire" == ptype or usetype == "Water" and " Fire" == ptype:
            effective = "super"
        if usetype == "Water" and "Water" == ptype or usetype == "Water" and " Water" == ptype:
            effective = "half"
        if usetype == "Water" and "Grass" == ptype or usetype == "Water" and " Grass" == ptype:
            effective = "half"
        if usetype == "Water" and "Ground" == ptype or usetype == "Water" and " Ground" == ptype:
            effective = "super"
        if usetype == "Water" and "Rock" == ptype or usetype == "Water" and " Rock" == ptype:
            effective = "super"
        if usetype == "Water" and "Dragon" == ptype or usetype == "Water" and " Dragon" == ptype:
            effective = "half"

        if usetype == "Electric" and "Water" == ptype or usetype == "Electric" and " Water" == ptype:
            effective = "super"
        if usetype == "Electic" and "Electirc" == ptype or usetype == "Electric" and " Electric" == ptype:
            effective = "half"
        if usetype == "Electric" and "Grass" == ptype or usetype == "Electric" and " Grass" == ptype:
            effective = "half"
        if usetype == "Electric" and "Ground" == ptype or usetype == "Electric" and " Ground" == ptype:
            effective = "zero"
        if usetype == "Electric" and "Flying" == ptype or usetype == "Electric" and " Flying" == ptype:
            effective = "super"
        if usetype == "Electric" and "Dragon" == ptype or usetype == "Electric" and " Dragon" == ptype:
            effective = "half"

        if usetype == "Grass" and "Fire" == ptype or usetype == "Grass" and " Fire" == ptype:
            effective = "half"
        if usetype == "Grass" and "Water" == ptype or usetype == "Grass" and " Water" == ptype:
            effective = "super"
        if usetype == "Grass" and "Grass" == ptype or usetype == "Grass" and " Grass" == ptype:
            effective = "half"
        if usetype == "Grass" and "Poison" == ptype or usetype == "Grass" and " Poison" == ptype:
            effective = "half"
        if usetype == "Grass" and "Ground" == ptype or usetype == "Grass" and " Ground" == ptype:
            effective = "super"
        if usetype == "Grass" and "Flying" == ptype or usetype == "Grass" and " Flying" == ptype:
            effective = "half"
        if usetype == "Grass" and "Bug" == ptype or usetype == "Grass" and " Bug" == ptype:
            effective = "half"
        if usetype == "Grass" and "Rock" == ptype or usetype == "Grass" and " Rock" == ptype:
            effective = "super"
        if usetype == "Grass" and "Dragon" == ptype or usetype == "Grass" and " Dragon" == ptype:
            effective = "half"

        if usetype == "Ice" and "Fire" == ptype or usetype == "Ice" and " Fire" == ptype:
            effective = "half"
        if usetype == "Ice" and "Water" == ptype or usetype == "Ice" and " Water" == ptype:
            effective = "half"
        if usetype == "Ice" and "Grass" == ptype or usetype == "Ice" and " Grass" == ptype:
            effective = "super"
        if usetype == "Ice" and "Ice" == ptype or usetype == "Ice" and " Ice" == ptype:
            effective = "half"
        if usetype == "Ice" and "Ground" == ptype or usetype == "Ice" and " Ground" == ptype:
            effective = "super"
        if usetype == "Ice" and "Flying" == ptype or usetype == "Ice" and " Flying" == ptype:
            effective = "super"
        if usetype == "Ice" and "Dragon" == ptype or usetype == "ICe" and " Dragon" == ptype:
            effective = "super"

        if usetype == "Fighting" and "Normal" == ptype or usetype == "Fighting" and " Normal" == ptype:
            effective = "super"
        if usetype == "Fighting" and "Ice" == ptype or usetype == "Fighting" and " Ice" == ptype:
            effective = "super"
        if usetype == "Fighting" and "Poison" == ptype or usetype == "Fighting" and " Poison" == ptype:
            effective = "half"
        if usetype == "Fighting" and "Flying" == ptype or usetype == "Fighting" and " Flying" == ptype:
            effective = "half"
        if usetype == "Fighting" and "Psychic" == ptype or usetype == "Fighting" and " Psychic" == ptype:
            effective = "half"
        if usetype == "Fighting" and "Bug" == ptype or usetype == "Fighting" and " Flying" == ptype:
            effective = "half"
        if usetype == "Fighting" and "Rock" == ptype or usetype == "Fighting" and " Rock" == ptype:
            effective = "super"
        if usetype == "Fighting" and "Ghost" == ptype or usetype == "Figthing" and " Ghost" == ptype:
            effective = "zero"

        if usetype == "Poison" and "Grass" == ptype or usetype == "Poison" and " Grass" == ptype:
            effective = "super"
        if usetype == "Poison" and "Poison" == ptype or usetype == "Poison" and " Poison" == ptype:
            effective = "half"
        if usetype == "Poison" and "Ground" == ptype or usetype == "Poison" and " Ground" == ptype:
            effective = "half"
        if usetype == "Poison" and "Rock" == ptype or usetype == "Poison" and " Rock" == ptype:
            effective = "half"
        if usetype == "Poison" and "Ghost" == ptype or usetype == "Poison" and " Ghost" == ptype:
            effective = "half"

        if usetype == "Ground" and "Fire" == ptype or usetype == "Ground" and " Fire" == ptype:
            effective = "super"
        if usetype == "Ground" and "Electric" == ptype or usetype == "Ground" and " Electric" == ptype:
            effective = "super"
        if usetype == "Ground" and "Grass" == ptype or usetype == "Ground" and " Grass" == ptype:
            effective = "half"
        if usetype == "Ground" and "Poison" == ptype or usetype == "Ground" and " Poison" == ptype:
            effective == "super"
        if usetype == "Ground" and "Flying" == ptype or usetype == "Ground" and " Flying" == ptype:
            effective == "zero"
        if usetype == "Ground" and "Bug" == ptype or usetype == "Ground" and " Bug" == ptype:
            effective == "half"
        if usetype == "Ground" and "Rock" == ptype or usetype == "Ground" and " Rock" == ptype:
            effective = "super"

        if usetype == "Flying" and "Electric" == ptype or usetype == "Flying" and " Electric" == ptype:
            effective = "half"
        if usetype == "Flying" and "Grass" == ptype or usetype == "Flying" and " Grass" == ptype:
            effective = "super"
        if usetype == "Flying" and "Fighting" == ptype or usetype == "Flying" and " Fighting" == ptype:
            effective = "super"
        if usetype == "Flying" and "Bug" == ptype or usetype == "Flying" and " Bug" == ptype:
            effective = "Bug"
        if usetype == "Flying" and "Rock" == ptype or usetype == "Flying" and " Rock" == ptype:
            effective = "half"

        if usetype == "Psychic" and "Fighting" == ptype or usetype == "Psychic" and " Fighting" == ptype:
            effective = "super"
        if usetype == "Psychic" and "Poison" == ptype or usetype == "Psychic" and " Poison" == ptype:
            effective = "super"
        if usetype == "Psychic" and "Psychic" == ptype or usetype == "Psychic" and " Psychic" == ptype:
            effective = "half"

        if usetype == "Bug" and "Fire" == ptype or usetype == "Bug" and " Fire" == ptype:
            effective = "half"
        if usetype == "Bug" and "Grass" == ptype or usetype == "Bug" and " Grass" == ptype:
            effective = "super"
        if usetype == "Bug" and "Fighting" == ptype or usetype == "Bug" and " Fighting" == ptype:
            effective = "half"
        if usetype == "Bug" and "Poison" == ptype or usetype == "Bug" and " Poison" == ptype:
            effective = "half"
        if usetype == "Bug" and "Flying" == ptype or usetype == "Bug" and " Flying" == ptype:
            effective = "half"
        if usetype == "Bug" and "Psychic" == ptype or usetype == "Bug" and " Psychic" == ptype:
            effective = "super"
        if usetype == "Bug" and "Ghost" == ptype or usetype == "Bug" and " Ghost" == ptype:
            effective = "half"

        if usetype == "Rock" and "Fire" == ptype or usetype == "Rock" and " Fire" == ptype:
            effective = "super"
        if usetype == "Rock" and "Ice" == ptype or usetype == "Rock" and " Ice" == ptype:
            effective = "super"
        if usetype == "Rock" and "Fighting" == ptype or usetype == "Rock" and " Fighting" == ptype:
            effective = "half"
        if usetype == "Rock" and "Ground" == ptype or usetype == "Rock" and " Ground" == ptype:
            effective = "half"
        if usetype == "Rock" and "Flying" == ptype or usetype == "Rock" and " Flying" == ptype:
            effective = "super"
        if usetype == "Rock" and "Bug" == ptype or usetype == "Rock" and " Bug" == ptype:
            effective = "super"

        if usetype == "Ghost" and "Normal" == ptype or usetype == "Ghost" and " Normal" == ptype:
            effective = "zero"
        if usetype == "Ghost" and "Psychic" == ptype or usetype == "Ghost" and " Psychic" == ptype:
            effective = "super"
        if usetype == "Ghost" and "Ghost" == ptype or usetype == "Ghost" and " Ghost" == ptype:
            effective = "super"

        if usetype == "Dragon" and "Dragon" == ptype or usetype == "Dragon" and " Dragon" == ptype:
            effective = "super"
        return(effective)


    def typechart(enemypokemon, oppositepokemon):
        global matchup
        global matchup1
        Doit = "yes"
        matchup = "normal"
        matchup1 = "normal"
        for i in range(pokemonlist):
            if (data[i]["Name"]) == oppositepokemon:
                ptype = (data[i]["Types"])
        for i in range(pokemonlist):
            if (data[i]["Name"]) == enemypokemon:
                enemytypes = (data[i]["Types"])
        enemytype = enemytypes[0]
        if len(enemytypes) == 1:
          Doit = "no"

        if len(enemytypes) == 2:
          enemytype2 = enemytypes[1]
        #if len(types) == 2: 2 variables

        if enemytype == "Normal" and "Rock" in ptype:
            matchup = "half"
        if enemytype == "Normal" and "Ghost" in ptype:
            matchup = "zero"

        if enemytype == "Fire" and "Fire" in ptype:
            matchup = "half"
        if enemytype == "Fire" and "Water" in ptype:
            matchup = "half"
        if enemytype == "Fire" and "Grass" in ptype:
            matchup = "super"
        if enemytype == "Fire" and "Ice" in ptype:
            matchup = "super"
        if enemytype == "Fire" and "Bug" in ptype:
            matchup = "super"
        if enemytype == "Fire" and "Rock" in ptype:
            matchup = "half"
        if enemytype == "Fire" and "Dragon" in ptype:
            matchup = "half"

        if enemytype == "Water" and "Fire" in ptype:
            matchup = "super"
        if enemytype == "Water" and "Water" in ptype:
            matchup = "half"
        if enemytype == "Water" and "Grass" in ptype:
            matchup = "half"
        if enemytype == "Water" and "Ground" in ptype:
            matchup = "super"
        if enemytype == "Water" and "Rock" in ptype:
            matchup = "super"
        if enemytype == "Water" and "Dragon" in ptype:
            matchup = "half"

        if enemytype == "Electric" and "Water" in ptype:
            matchup = "super"
        if enemytype == "Electic" and "Electirc" in ptype:
            matchup = "half"
        if enemytype == "Electric" and "Grass" in ptype:
            matchup = "half"
        if enemytype == "Electric" and "Ground" in ptype:
            matchup = "zero"
        if enemytype == "Electric" and "Flying" in ptype:
            matchup = "super"
        if enemytype == "Electric" and "Dragon" in ptype:
            matchup = "half"

        if enemytype == "Grass" and "Fire" in ptype:
            matchup = "half"
        if enemytype == "Grass" and "Water" in ptype:
            matchup = "super"
        if enemytype == "Grass" and "Grass" in ptype:
            matchup = "half"
        if enemytype == "Grass" and "Poison" in ptype:
            matchup = "half"
        if enemytype == "Grass" and "Ground" in ptype:
            matchup = "super"
        if enemytype == "Grass" and "Flying" in ptype:
            matchup = "half"
        if enemytype == "Grass" and "Bug" in ptype:
            matchup = "half"
        if enemytype == "Grass" and "Rock" in ptype:
            matchup = "super"
        if enemytype == "Grass" and "Dragon" in ptype:
            matchup = "half"

        if enemytype == "Ice" and "Fire" in ptype:
            matchup = "half"
        if enemytype == "Ice" and "Water" in ptype:
            matchup = "half"
        if enemytype == "Ice" and "Grass" in ptype:
            matchup = "super"
        if enemytype == "Ice" and "Ice" in ptype:
            matchup = "half"
        if enemytype == "Ice" and "Ground" in ptype:
            matchup = "super"
        if enemytype == "Ice" and "Flying" in ptype:
            matchup = "super"
        if enemytype == "Ice" and "Dragon" in ptype:
            matchup = "super"

        if enemytype == "Fighting" and "Normal" in ptype:
            matchup = "super"
        if enemytype == "Fighting" and "Ice" in ptype:
            matchup = "super"
        if enemytype == "Fighting" and "Poison" in ptype:
            matchup = "half"
        if enemytype == "Fighting" and "Flying" in ptype:
            matchup = "half"
        if enemytype == "Fighting" and "Psychic" in ptype:
            matchup = "half"
        if enemytype == "Fighting" and "Bug" in ptype:
            matchup = "half"
        if enemytype == "Fighting" and "Rock" in ptype:
            matchup = "super"
        if enemytype == "Fighting" and "Ghost" in ptype:
            matchup = "zero"

        if enemytype == "Poison" and "Grass" in ptype:
            matchup = "super"
        if enemytype == "Poison" and "Poison" in ptype:
            matchup = "half"
        if enemytype == "Poison" and "Ground" in ptype:
            matchup = "half"
        if enemytype == "Poison" and "Rock" in ptype:
            matchup = "half"
        if enemytype == "Poison" and "Ghost" in ptype:
            matchup = "half"

        if enemytype == "Ground" and "Fire" in ptype:
            matchup = "super"
        if enemytype == "Ground" and "Electric" in ptype:
            matchup = "super"
        if enemytype == "Ground" and "Grass" in ptype:
            matchup = "half"
        if enemytype == "Ground" and "Poison" in ptype:
            matchup == "super"
        if enemytype == "Ground" and "Flying" in ptype:
            matchup == "zero"
        if enemytype == "Ground" and "Bug" in ptype:
            matchup == "half"
        if enemytype == "Ground" and "Rock" in ptype:
            matchup = "super"

        if enemytype == "Flying" and "Electric" in ptype:
            matchup = "half"
        if enemytype == "Flying" and "Grass" in ptype:
            matchup = "super"
        if enemytype == "Flying" and "Fighting" in ptype:
            matchup = "super"
        if enemytype == "Flying" and "Bug" in ptype:
            matchup = "Bug"
        if enemytype == "Flying" and "Rock" in ptype:
            matchup = "half"

        if enemytype == "Psychic" and "Fighting" in ptype:
            matchup = "super"
        if enemytype == "Psychic" and "Poison" in ptype:
            matchup = "super"
        if enemytype == "Psychic" and "Psychic" in ptype:
            matchup = "half"

        if enemytype == "Bug" and "Fire" in ptype:
            matchup = "half"
        if enemytype == "Bug" and "Grass" in ptype:
            matchup = "super"
        if enemytype == "Bug" and "Fighting" in ptype:
            matchup = "half"
        if enemytype == "Bug" and "Poison" in ptype:
            matchup = "half"
        if enemytype == "Bug" and "Flying" in ptype:
            matchup = "half"
        if enemytype == "Bug" and "Psychic" in ptype:
            matchup = "super"
        if enemytype == "Bug" and "Ghost" in ptype:
            matchup = "half"

        if enemytype == "Rock" and "Fire" in ptype:
            matchup = "super"
        if enemytype == "Rock" and "Ice" in ptype:
            matchup = "super"
        if enemytype == "Rock" and "Fighting" in ptype:
            matchup = "half"
        if enemytype == "Rock" and "Ground" in ptype:
            matchup = "half"
        if enemytype == "Rock" and "Flying" in ptype:
            matchup = "super"
        if enemytype == "Rock" and "Bug" in ptype:
            matchup = "super"

        if enemytype == "Ghost" and "Normal" in ptype:
            matchup = "zero"
        if enemytype == "Ghost" and "Psychic" in ptype:
            matchup = "super"
        if enemytype == "Ghost" and "Ghost" in ptype:
            matchup = "super"

        if enemytype == "Dragon" and "Dragon" in ptype:
            matchup = "super"
        if Doit == "yes":
          if enemytype2 == "Normal" and "Rock" in ptype:
            matchup1 = "half"
          if enemytype2 == "Normal" and "Ghost" in ptype:
            matchup1 = "zero"

          if enemytype2 == "Fire" and "Fire" in ptype:
            matchup1 = "half"
          if enemytype2 == "Fire" and "Water" in ptype:
            matchup1 = "half"
          if enemytype2 == "Fire" and "Grass" in ptype:
            matchup1 = "super"
          if enemytype2 == "Fire" and "Ice" in ptype:
            matchup1 = "super"
          if enemytype2 == "Fire" and "Bug" in ptype:
            matchup1 = "super"
          if enemytype2 == "Fire" and "Rock" in ptype:
            matchup1 = "half"
          if enemytype2 == "Fire" and "Dragon" in ptype:
            matchup1 = "half"

          if enemytype2 == "Water" and "Fire" in ptype:
            matchup1 = "super"
          if enemytype2 == "Water" and "Water" in ptype:
            matchup1 = "half"
          if enemytype2 == "Water" and "Grass" in ptype:
            matchup1 = "half"
          if enemytype2 == "Water" and "Ground" in ptype:
            matchup1 = "super"
          if enemytype2 == "Water" and "Rock" in ptype:
            matchup1 = "super"
          if enemytype2 == "Water" and "Dragon" in ptype:
            matchup1 = "half"

          if enemytype2 == "Electric" and "Water" in ptype:
            matchup1 = "super"
          if enemytype2 == "Electic" and "Electirc" in ptype:
            matchup1 = "half"
          if enemytype2 == "Electric" and "Grass" in ptype:
            matchup1 = "half"
          if enemytype2 == "Electric" and "Ground" in ptype:
            matchup1 = "zero"
          if enemytype2 == "Electric" and "Flying" in ptype:
            matchup1 = "super"
          if enemytype2 == "Electric" and "Dragon" in ptype:
            matchup1 = "half"

          if enemytype2 == "Grass" and "Fire" in ptype:
            matchup1 = "half"
          if enemytype2 == "Grass" and "Water" in ptype:
            matchup1 = "super"
          if enemytype2 == "Grass" and "Grass" in ptype:
            matchup1 = "half"
          if enemytype2 == "Grass" and "Poison" in ptype:
            matchup1 = "half"
          if enemytype2 == "Grass" and "Ground" in ptype:
            matchup1 = "super"
          if enemytype2 == "Grass" and "Flying" in ptype:
            matchup1 = "half"
          if enemytype2 == "Grass" and "Bug" in ptype:
            matchup1 = "half"
          if enemytype2 == "Grass" and "Rock" in ptype:
            matchup1 = "super"
          if enemytype2 == "Grass" and "Dragon" in ptype:
            matchup1 = "half"

          if enemytype2 == "Ice" and "Fire" in ptype:
            matchup1 = "half"
          if enemytype2 == "Ice" and "Water" in ptype:
            matchup1 = "half"
          if enemytype2 == "Ice" and "Grass" in ptype:
            matchup1 = "super"
          if enemytype2 == "Ice" and "Ice" in ptype:
            matchup1 = "half"
          if enemytype2 == "Ice" and "Ground" in ptype:
            matchup1 = "super"
          if enemytype2 == "Ice" and "Flying" in ptype:
            matchup1 = "super"
          if enemytype2 == "Ice" and "Dragon" in ptype:
            matchup1 = "super"

          if enemytype2 == "Fighting" and "Normal" in ptype:
            matchup1 = "super"
          if enemytype2 == "Fighting" and "Ice" in ptype:
            matchup1 = "super"
          if enemytype2 == "Fighting" and "Poison" in ptype:
            matchup1 = "half"
          if enemytype2 == "Fighting" and "Flying" in ptype:
            matchup1 = "half"
          if enemytype2 == "Fighting" and "Psychic" in ptype:
            matchup1 = "half"
          if enemytype2 == "Fighting" and "Bug" in ptype:
            matchup1 = "half"
          if enemytype2 == "Fighting" and "Rock" in ptype:
            matchup1 = "super"
          if enemytype2 == "Fighting" and "Ghost" in ptype:
            matchup1 = "zero"

          if enemytype2 == "Poison" and "Grass" in ptype:
            matchup1 = "super"
          if enemytype2 == "Poison" and "Poison" in ptype:
            matchup1 = "half"
          if enemytype2 == "Poison" and "Ground" in ptype:
            matchup1 = "half"
          if enemytype2 == "Poison" and "Rock" in ptype:
            matchup1 = "half"
          if enemytype2 == "Poison" and "Ghost" in ptype:
            matchup1 = "half"

          if enemytype2 == "Ground" and "Fire" in ptype:
            matchup1 = "super"
          if enemytype2 == "Ground" and "Electric" in ptype:
            matchup1 = "super"
          if enemytype2 == "Ground" and "Grass" in ptype:
            matchup1 = "half"
          if enemytype2 == "Ground" and "Poison" in ptype:
            matchup1 == "super"
          if enemytype2 == "Ground" and "Flying" in ptype:
            matchup1 == "zero"
          if enemytype2 == "Ground" and "Bug" in ptype:
            matchup1 == "half"
          if enemytype2 == "Ground" and "Rock" in ptype:
            matchup1 = "super"

          if enemytype2 == "Flying" and "Electric" in ptype:
            matchup1 = "half"
          if enemytype2 == "Flying" and "Grass" in ptype:
            matchup1 = "super"
          if enemytype2 == "Flying" and "Fighting" in ptype:
            matchup1 = "super"
          if enemytype2 == "Flying" and "Bug" in ptype:
            matchup1 = "Bug"
          if enemytype2 == "Flying" and "Rock" in ptype:
            matchup1 = "half"

          if enemytype2 == "Psychic" and "Fighting" in ptype:
            matchup1 = "super"
          if enemytype2 == "Psychic" and "Poison" in ptype:
            matchup1 = "super"
          if enemytype2 == "Psychic" and "Psychic" in ptype:
            matchup1 = "half"

          if enemytype2 == "Bug" and "Fire" in ptype:
            matchup1 = "half"
          if enemytype2 == "Bug" and "Grass" in ptype:
            matchup1 = "super"
          if enemytype2 == "Bug" and "Fighting" in ptype:
            matchup1 = "half"
          if enemytype2 == "Bug" and "Poison" in ptype:
            matchup1 = "half"
          if enemytype2 == "Bug" and "Flying" in ptype:
            matchup1 = "half"
          if enemytype2 == "Bug" and "Psychic" in ptype:
            matchup1 = "super"
          if enemytype2 == "Bug" and "Ghost" in ptype:
            matchup1 = "half"

          if enemytype2 == "Rock" and "Fire" in ptype:
            matchup1 = "super"
          if enemytype2 == "Rock" and "Ice" in ptype:
            matchup1 = "super"
          if enemytype2 == "Rock" and "Fighting" in ptype:
            matchup1 = "half"
          if enemytype2 == "Rock" and "Ground" in ptype:
            matchup1 = "half"
          if enemytype2 == "Rock" and "Flying" in ptype:
            matchup1 = "super"
          if enemytype2 == "Rock" and "Bug" in ptype:
            matchup1 = "super"

          if enemytype2 == "Ghost" and "Normal" in ptype:
            matchup1 = "zero"
          if enemytype2 == "Ghost" and "Psychic" in ptype:
            matchup1 = "super"
          if enemytype2 == "Ghost" and "Ghost" in ptype:
            matchup1 = "super"

          if enemytype2 == "Dragon" and "Dragon" in ptype:
            matchup1 = "super"


    def pokemoninmoves(currentpokemon):
        global currentmoves

        #if currentpokemon == teaminfo[0]:
        #    currentmoves = teaminfo[1]
        #if currentpokemon == teaminfo[2]:
        #    currentmoves = teaminfo[3]
        #if currentpokemon == teaminfo[4]:
        #    currentmoves = teaminfo[5]
        #if currentpokemon == teaminfo[6]:
        #    currentmoves = teaminfo[7]
        #if currentpokemon == teaminfo[8]:
        #    currentmoves = teaminfo[9]
        #if currentpokemon == teaminfo[10]:
        #    currentmoves = teaminfo[11]

    def damagecalc(damagecalc, move, attackingpk, enemypk):
      if move != "Nothing":
        for i in range(movelist):
            if move == moves[i]["name"]:
                movenumber = i
        for i in range(pokemonlist):
            if attackingpk == data[i]["Name"]:
                attacknumber = i
        for i in range(pokemonlist):
            if enemypk == data[i]["Name"]:
                enemynumber = i
        movepower = moves[movenumber]["power"]
        userattack = data[attacknumber]["Attack Stat"]
        enemydefense = data[enemynumber]["Defense Stat"]
        userspecial = data[attacknumber]["Special Stat"]
        enemyspecial = data[enemynumber]["Special Stat"]
        if moves[movenumber]["category"] == "Physical":
            global attackingpower
            global defendingpower
            attackingpower = userattack
            defendingpower = enemydefense
        if moves[movenumber]["category"] == "Special":
            attackingpower = userspecial
            defendingpower = enemyspecial
        if moves[movenumber]["category"] == "None":
            attackingpower = userattack
            defendingpower = enemydefense
        userspeed = data[attacknumber]["Speed Stat"]
        threshold = userspeed / decimal.Decimal(8)
        critchance = random.randint(0,255)
        if threshold > critchance:
            attackingpower *= 1.5
            global crithappen
            crithappen = True
        if threshold < critchance or threshold == critchance:
            crithappen = False
        math1 = decimal.Decimal(40) * decimal.Decimal(movepower)
        math2 = decimal.Decimal(attackingpower) / decimal.Decimal(defendingpower)
        math3 = decimal.Decimal(math2) * decimal.Decimal(math1)
        math4 = decimal.Decimal(math3) / decimal.Decimal(50)
        math5 = decimal.Decimal(math4) + decimal.Decimal(2)
        #print(math5)
        if moves[movenumber]["type"] in data[attacknumber]["Types"]:
            global stab
            stab = True
        if not(moves[movenumber]["type"] in data[attacknumber]["Types"]):
            stab = False
        f = functionality()
        if len(data[enemynumber]["Types"]) == 2:
            enemytype1 = (data[enemynumber]["Types"])[0]
            enemytype2 = (data[enemynumber]["Types"])[1]
            typeeffect1 = f.supereffective(move, enemytype1)
            global meffective1
            global typesuper1
            typesuper1 = False
            global typehalf1
            typehalf1 = False
            global typezero1
            typezero1 = False
            if typeeffect1 == "super":
                typesuper1 = True
                meffective1 = 2
            if typeeffect1 == "half":
                typehalf1 = True
                meffective1 = 0.5
            if typeeffect1 == "zero":
                typezero1 = True
                meffective1 = 0
            if typesuper1 != True and typehalf1 != True and typezero1 != True:
                meffective1 = 1
            typeeffect2 = f.supereffective(move, enemytype2)
            global meffective2
            global typesuper2
            typesuper2 = False
            global typehalf2
            typehalf2 = False
            global typezero2
            typezero2 = False
            if typeeffect2 == "super":
                typesuper2 = True
                meffective2 = 2
            if typeeffect2 == "half":
                typehalf2 = True
                meffective2 = 0.5
            if typeeffect2 == "zero":
                typezero2 = True
                meffective2 = 0
            if typesuper2 != True and typehalf2 != True and typezero2 != True:
                meffective2 = 1
            global twotype
            twotype = True
        if len(data[enemynumber]["Types"]) == 1:
            enemytype = (data[enemynumber]["Types"])[0]
            typeeffect = f.supereffective(move, enemytype)
            global meffective
            global typesuper
            typesuper = False
            global typehalf
            typehalf = False
            global typezero
            typezero = False
            if typeeffect == "super":
                typesuper = True
                meffective = 2
            if typeeffect == "half":
                typehalf = True
                meffective = 0.5
            if typeeffect == "zero":
                typezero = True
                meffective = 0
            if typesuper != True and typehalf != True and typezero != True:
                meffective = 1
        if stab == True:
            math5 *=  decimal.Decimal(1.5)
        if len(data[enemynumber]["Types"]) == 1:
            math5 *= decimal.Decimal(meffective)
            #print(meffective)
            #print(math5)
        if len(data[enemynumber]["Types"]) == 2:
            meffective = decimal.Decimal(meffective1) * decimal.Decimal(meffective2)
            #print(meffective1)
            #print(meffective2)
            math5 *= decimal.Decimal(meffective)
            #print(math5)
        global movedamage
        movedamage = round(math5)
        if moves[movenumber]["category"] == "None":
            movedamage = 0
      else:
        movedamage = 0
    def specialeffect(specialeffect, move, damage, enemyspeed, enemypk, userpk):
        f = functionality
        for i in range(movelist):
            if move == moves[i]["name"]:
                movenumber = i
        for i in range(pokemonlist):
            if enemypk == data[i]["Name"]:
                enemynumber = i
        if "HealHalfD" in moves[movenumber]["effect"]:
            for i in range(pokemonlist):
                if userpk == data[i]["Name"]:
                    fullhealth = data[i]["Health Stat"]
            for i in range(len(userpartyhealth)):
                if userpk == userpartyhealth[i - 1]:
                    currenthealth = userpartyhealth[i]
            healamount = damage / 2
            if currenthealth != fullhealth:
                currenthealth += int(healamount)
            if currenthealth == fullhealth or currenthealth > fullhealth:
                currenthealth = fullhealth
            for i in range(len(userpartyhealth)):
                if userpk == userpartyhealth[i - 1]:
                    userpartyhealth[i] = currenthealth
            print(userpk, "healed", healamount)
            print(userpk, "has", currenthealth, "health left")
        if "Hits2to5" in moves[movenumber]["effect"]:
            hitamount = 3 #sample(multiplehits, 1)[0]
            setdamage = damage
            global uniquedamage
            uniquedamage = damage
            for i in range(hitamount):
                print(userpk, "did", setdamage, "damage")
                uniquedamage += setdamage
            damage = uniquedamage
            unique[0] = "Yah"
        if "SpeedDown" in moves[movenumber]["effect"]:
            onestage = decimal.Decimal(2) / decimal.Decimal(3)
            enemyspeed *= onestage 
        if "HitsTwice" in moves[movenumber]["effect"]:
            again = True
            moveagain = 1
        if "Poison" in moves[movenumber]["effect"]:
            if not "Poison" in data[enemynumber]["Types"]:
                enemypk = "afflicted"
        return damage
      


    def checks(oppositepokemon):
        global enemypokemon
        global enemyspeed
        global enemyhealth
        global enemymove
        
        global shouldiswitch
        shouldiswitch = "no"
        for i in range(pokemonlist):
            if data[i]["Name"] == enemypokemon:
                Types = data[i]["Types"]
        functionality.typechart(enemypokemon, oppositepokemon)
       

        for i in range(pokemonlist):
            if data[i]["Name"] == "Raichu":
                RTypes = data[i]["Types"]
        for i in range(pokemonlist):
            if data[i]["Name"] == "Dragonite":
                DTypes = data[i]["Types"]
        for i in range(pokemonlist):
            if data[i]["Name"] == "Charizard":
                CTypes = data[i]["Types"]
        for i in range(pokemonlist):
            if data[i]["Name"] == "Gengar":
                GTypes = data[i]["Types"]
        for i in range(pokemonlist):
            if data[i]["Name"] == "Blastoise":
                BTypes = data[i]["Types"]
        for i in range(pokemonlist):
            if data[i]["Name"] == "Machamp":
                MTypes = data[i]["Types"]

        #type chart code for each, make variable each specific pokemons effectiveness
        #for range of 6 or 5- if variablle equals super, then repeat with normal

        if matchup == "half" or matchup == "zero" or matchup1 == "half" or matchup1 == "zero":
            functionality.typechart("Raichu", oppositepokemon)
            R = matchup
            R1 = matchup1
            functionality.typechart("Dragonite", oppositepokemon)
            D = matchup
            D1 = matchup1
            functionality.typechart("Charizard", oppositepokemon)
            C = matchup
            C1 = matchup1
            functionality.typechart("Gengar", oppositepokemon)
            G = matchup
            G1 = matchup1
            functionality.typechart("Blastoise", oppositepokemon)
            B = matchup
            B1 = matchup1
            functionality.typechart("Machamp", oppositepokemon)
            M = matchup
            M1 = matchup1
            if "Raichu" not in Mikesdeadguys and R != "half" and R != "zero" and R != "normal" or R1 != "normal" and R1 != "half" and R1 != "zero":

                enemypokemon = "Raichu"
                for i in range(pokemonlist):
                  for i in range(len(data)):
                    if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into", enemypokemon)
                shouldiswitch = "yes"
                enemymove = "Nothing"
                return enemypokemon

            elif "Dragonite" not in Mikesdeadguys and D != "half" and D != "zero" and D != "normal" or D1 != "normal" and D1 != "half" and D1 != "zero":
                enemypokemon = "Dragonite"
                for i in range(pokemonlist):
                  if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Dragonite")
                shouldiswitch = "yes"
                enemymove = "Nothing"
                return enemypokemon

            elif "Charizard" not in Mikesdeadguys and C != "half" and C != "zero" and C != "normal" or C1 != "normal" and C1 != "half" and C1 != "zero":
                enemypokemon = "Charizard"
                for i in range(pokemonlist):
                  if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Charizard")
                shouldiswitch = "yes"
                enemymove = "Nothing"
                return enemypokemon

            elif "Gengar" not in Mikesdeadguys and G != "half" and G != "zero" and G != "normal" or G1 != "normal" and G1 != "half" and G1 != "zero":
                enemypokemon = "Gengar"
                for i in range(pokemonlist):
                  if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Gengar")
                shouldiswitch = "yes"
                enemymove = "Nothing"
                return enemypokemon

            elif "Blastoise" not in Mikesdeadguys and B != "half" and B != "zero" and B != "normal" or B1 != "normal" and B1 != "half" and B1 != "zero":
                enemypokemon = "Blastoise"
                
                for i in range(pokemonlist):
                  if enemypokemon == data[i]["Name"]:
                          enemyspeed = data[i]["Speed Stat"]
                          enemyhealth = data[i]["Health Stat"]
                
                print("Mike M switched into Blastoise")
              
                shouldiswitch = "yes"
                enemymove = "Nothing"
                return enemypokemon
                

            elif "Machamp" not in Mikesdeadguys and M != "half" and M != "zero" and M != "normal" or M1 != "normal" and M1 != "half" and M1 != "zero":
                enemypokemon = "Machamp"
                for i in range(pokemonlist):
                  if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Machamp")
                shouldiswitch = "yes"
                enemymove = "Nothing"
                return enemypokemon
            else: 
                caniswitch = "no"
                while caniswitch == "no":
                    p = random.randrange(6)
                    if p == 1 and "Raichu" not in Mikesdeadguys and enemypokemon != "Raichu":
                         enemypokemon = "Raichu"
                         print("Mike M switched into", enemypokemon)
                         shouldiswitch = "yes"
                         caniswitch = "yes"
                    if p == 2 and "Dragonite" not in Mikesdeadguys and enemypokemon != "Dragonite":
                        enemypokemon = "Dragonite"
                        print("Mike M switched into Dragonite")
                        shouldiswitch = "yes"
                        caniswitch = "yes"
                    if p == 3 and "Charizard" not in Mikesdeadguys and enemypokemon != "Charizard":
                        enemypokemon = "Charizard"
                        print("Mike M switched into Charizard")
                        shouldiswitch = "yes"
                        caniswitch = "yes"
                    if p == 4 and "Gengar" not in Mikesdeadguys and enemypokemon != "Gengar":
                        enemypokemon = "Gengar"
                        print("Mike M switched into Gengar")
                        shouldiswitch = "yes"
                        caniswitch = "yes"
                    if p == 5 and "Blastoise" not in Mikesdeadguys and enemypokemon != "Blastoise":
                        enemypokemon = "Blastoise"
                        printM("Mike M switched into Blastoise")
                        shouldiswitch = "yes"
                        caniswitch = "yes"
                    if p == 6 and "Machamp" not in Mikesdeadguys and enemypokemon != "Machamp":
                        enemypokemon = "Machamp"
                        print("Mike M switched into Machamp")
                        shouldiswitch = "yes"
                        caniswitch = "yes"
              

    def Mikesdeadpks(enemyhealth, oppositepokemon):
        global enemypokemon
        if enemyhealth == 0:
            print(enemypokemon, "has fainted")
            Mikesdeadguys.append(enemypokemon)
            
            functionality.typechart("Raichu", oppositepokemon)
            R = matchup
            functionality.typechart("Dragonite", oppositepokemon)
            D = matchup
            functionality.typechart("Charizard", oppositepokemon)
            C = matchup
            functionality.typechart("Gengar", oppositepokemon)
            G = matchup
            functionality.typechart("Blastoise", oppositepokemon)
            B = matchup
            functionality.typechart("Machamp", oppositepokemon)
            M = matchup
            if "Raichu" not in Mikesdeadguys:
                
                enemypokemon = "Raichu"
                for i in range(len(data)):
                  if enemypokemon == (data[i]["Name"]):
                      enemyspeed = (data[i]["Speed Stat"])
                      enemyhealth = (data[i]["Health Stat"])
                print("Mike M switched into", enemypokemon)
                shouldiswitch = "yes"

            elif "Dragonite" not in Mikesdeadguys:
                enemypokemon = "Dragonite"
                for i in range(len(data)):
                  if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Dragonite")
                shouldiswitch = "yes"

            elif "Charizard" not in Mikesdeadguys:
                enemypokemon = "Charizard"
                for i in range(len(data)):
                  if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Charizard")
                shouldiswitch = "yes"

            elif "Gengar" not in Mikesdeadguys:
                enemypokemon = "Gengar"
                for i in range(len(data)):
                  if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Gengar")
                shouldiswitch = "yes"

            elif "Blastoise" not in Mikesdeadguys:
                enemypokemon = "Blastoise"
                for i in range(len(data)):
                  if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Blastoise")
                shouldiswitch = "yes"

            elif "Machamp" not in Mikesdeadguys:
                enemypokemon = "Machamp"
                for i in range(len(data)):
                  if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Machamp")
                shouldiswitch = "yes"
            elif len(Mikesdeadguys) == 6:
              print("Mike has no more pokemon left")
            else: 
                caniswitch = "no"
                while caniswitch == "no":
                    p = random.randrange(6)
                    if p == 1 and "Raichu" not in Mikesdeadguys:
                         enemypokemon = "Raichu"
                         print("Mike M switched into", enemypokemon)
                         shouldiswitch = "yes"
                         caniswitch = "yes"
                    if p == 2 and "Dragonite" not in Mikesdeadguys:
                        enemypokemon = "Dragonite"
                        print("Mike M switched into Dragonite")
                        shouldiswitch = "yes"
                        caniswitch = "yes"
                    if p == 3 and "Charizard" not in Mikesdeadguys:
                        enemypokemon = "Charizard"
                        print("Mike M switched into Charizard")
                        shouldiswitch = "yes"
                        caniswitch = "yes"
                    if p == 4 and "Gengar" not in Mikesdeadguys:
                        enemypokemon = "Gengar"
                        print("Mike M switched into Gengar")
                        shouldiswitch = "yes"
                        caniswitch = "yes"
                    if p == 5 and "Blastoise" not in Mikesdeadguys:
                        enemypokemon = "Blastoise"
                        print("Mike M switched into Blastoise")
                        shouldiswitch = "yes"
                        caniswitch = "yes"
                    if p == 6 and "Machamp" not in Mikesdeadguys:
                        enemypokemon = "Machamp"
                        print("Mike M switched into Machamp")
                        shouldiswitch = "yes"
                        caniswitch = "yes"
              







class Mike(functionality):
    MikeTeam = ["Raichu", "Dragonite", "Charizard", "Gengar", "Blastoise", "Machamp"]










    def Raichudoing(turn, enemypokemon):
        global enemymove
        
        Rmoves = ["Double Team", "Toxic", "Thunderbolt", "Surf"]
        
        
        for i in range(pokemonlist):
          if data[i]["Name"] == currentpokemon:
            oscar = i
        Alek = data[oscar]["Types"][0]
        if turn == 0:
           
            for i in range(pokemonlist):
                if (data[i]["Name"]) == currentpokemon:
                    ptype = (data[i]["Types"])
            if "Poison" not in ptype:
                #print("Raichu used Toxic")
                enemymove = "Toxic"

            else:
                enemymove = "Double Team"
                #print("Raichu used Double Team")


        if turn != 0:
            
        
            enemypokemon = functionality.checks(currentpokemon)
            
            if shouldiswitch == "no":
                functionality.supereffective("why", "Thunderbolt", Alek)
                if effective == "super":
                    enemymove = "Thunderbolt"
                    #print("Raichu used Thunderbolt")

                if effective != "super":
                    functionality.supereffective("why", "Surf", Alek)
                    if effective == "super":
                        enemymove = "Surf"
                        #print("Raichu used Surf")

                        if effective != "super":
                            for i in range(userpartystatus):
                                if currentpokemon == userpartystatus[i - 1]:
                                    x = userpartystatus[i]
                                    if x == "None":
                                        enemymove = "Toxic"
                                    if x != "None":
                                        x = random.randrange(4)
                                        if x == 1 or x == 4:
                                            enemymove = "Double Team"
                                            #print("Raichu used Double Team")

                                        if x == 2:
                                            enemymove = "Thunderbolt"
                                            #print("Raichu used Thunderbolt")

                                        if x == 3:
                                            enemymove = "Surf"
                                            #print("Raichu used Surf")
            return enemypokemon


    def DragoniteDoing(turn):
        global enemymove
        global enemypokemon
        Dmoves = ["Agility", "Slam", "Fire Blast", "Blizzard"]
        for i in range(pokemonlist):
          if data[i]["Name"] == currentpokemon:
            oscar = i
        Alek = data[oscar]["Types"][0]

        functionality.checks(currentpokemon)
        if shouldiswitch != "yes":
            functionality.supereffective("why", "Fire Blast", Alek)
            if effective == "super":
                enemymove = "Fire Blast"
                #print("Raichu used Fire Blast")

            if effective != "super":
                functionality.supereffective("why", "Blizzard", Alek)
                if effective == "super":
                    enemymove = "Blizzard"
                    #print("Raichu used Surf")

                if effective != "super":
                    x = random.randrange(5)
                    if x == 1 or x == 4:
                        enemymove = "Agility"
                        #print("Raichu used Agility")

                    if x == 2:
                        enemymove = "Slam"
                        #print("Raichu used Thunderbolt")

                    if x == 3:
                        enemymove = "Fire Blast"
                        #print("Raichu used Surf")

                    if x == 5:
                        enemymove = "Blizzard"

    def Charizarddoing(turn):
        global enemymove
        global enemypokemon
        Cmoves = ["Swords Dance", "Mega Punch", "Earthquake", "Strength"]
        for i in range(pokemonlist):
          if data[i]["Name"] == currentpokemon:
            oscar = i
        Alek = data[oscar]["Types"][0]
        y = turn
        Joel = turn - y
        if Joel < 2:
            enemymove = "Swords Dance"
        if Joel == 2 or Joel > 2:
            functionality.checks(currentpokemon)
            if shouldiswitch != "yes":
                functionality.supereffective("why", "Mega Punch", Alek)
                if effective == "super":
                    enemymove = "Mega Punch"
                    #print("Raichu used Fire Blast")

                if effective != "super":
                    functionality.supereffective("why", "Earthquake", Alek)
                    if effective == "super":
                        enemymove = "Earthquake"
                        #print("Raichu used Surf")

                    if effective != "super":
                        functionality.supereffective("why", "Strength", Alek)
                        if effective == "super":
                                enemymove = "Strength"

                        if effective != "super":
                            x = random.randrange(3)
                            if x == 1:
                                enemymove = "Mega Punch"
                                #print("Raichu used Agility")

                            if x == 2:
                                enemymove = "Earthquake"
                                #print("Raichu used Thunderbolt")

                            if x == 3:
                                enemymove = "Strength"
                                #print("Raichu used Surf")

    def Gengardoing():
        global enemymove
        global enemypokemon
        Gmoves = ["Mega Drain", "Hypnosis", "Dream Eater", "Psychic"]
        for i in range(pokemonlist):
          if data[i]["Name"] == currentpokemon:
            oscar = i
        Alek = data[oscar]["Types"][0]

        functionality.checks(currentpokemon)
        if shouldiswitch != "yes":
            functionality.supereffective("why", "Psychic", Alek)
            if effective == "super":
                enemymove = "Psychic"
                #print("Raichu used Fire Blast")

            if effective != "super":
                functionality.supereffective("why", "Mega Drain", Alek)
                if effective == "super":
                    enemymove = "Mega Drain"
                if effective != "super":
                    for i in range(userpartystatus):
                        if currentpokemon == userpartystatus[i - 1]:
                            x = userpartystatus[i]
                            if x == "asleep":
                                enemymove = "Dream Eater"
                            if x != "asleep":
                                enemymove = "Hypnosis"

                            else:
                                v = random.randrange(2)
                                if v == 1:
                                    enemymove = "Mega Drain"
                                if v == 2:
                                    enemymove = "Psychic"
                                #print("Raichu used Agility")

    def Blastoisedoing(turn):
        global enemymove
        global enemypokemon
        
        Gmoves = ["Hydro Pump", "Toxic", "Bite", "Ice Beam"]
        for i in range(pokemonlist):
          if data[i]["Name"] == currentpokemon:
            oscar = i
        Alek = data[oscar]["Types"][0]
        functionality.checks(currentpokemon)
        if shouldiswitch != "yes":
                functionality.supereffective("why", "Hydro Pump", Alek)
                if effective == "super":
                    enemymove = "Hydro Pump"
                    #print("Raichu used Fire Blast")

                if effective != "super":
                    functionality.supereffective("why", "Bite", Alek)
                    if effective == "super":
                        enemymove = "Bite"
                        #print("Raichu used Surf")

                    if effective != "super":
                        functionality.supereffective("why", "Ice Beam", Alek)
                        if effective == "super":
                                enemymove = "Ice Beam"

                        if effective != "super":
                            for i in range(userpartystatus):
                                if currentpokemon == userpartystatus[i - 1]:
                                    x = userpartystatus[i]
                                    if x != "Poisoned":
                                        enemymove = "Toxic"
                                    if x == "Poisoned":

                                        x = random.randrange(3)
                                        if x == 1:
                                            enemymove = "Hydro Pump"
                                            #print("Raichu used Agility")

                                        if x == 2:
                                            enemymove = "Bite"
                                            #print("Raichu used Thunderbolt")

                                        if x == 3:
                                            enemymove = "Ice Beam"
                                        #print("Raichu used Surf")
    def Machampdoing():
        global enemymove
        global enemypokemon
        Gmoves = ["Body Slam", "Earthquake", "Rock Slide", "Submission"]
        for i in range(pokemonlist):
          if data[i]["Name"] == currentpokemon:
            oscar = i
        Alek = data[oscar]["Types"][0]
        functionality.checks(currentpokemon)
        if shouldiswitch != "yes":
                functionality.supereffective("why", "Body Slam", Alek)
                if effective == "super":
                    enemymove = "Body Slam"
                    #print("Raichu used Fire Blast")

                if effective != "super":
                    functionality.supereffective("why", "Earthquake", Alek)
                    if effective == "super":
                        enemymove = "Earthquake"
                        #print("Raichu used Surf")

                    if effective != "super":
                        functionality.supereffective("why", "Rock Slide", Alek)
                        if effective == "super":
                                enemymove = "Rock Slide"

                        if effective != "super":
                            functionality.supereffective("why","Submission", Alek)
                            if effective == "super":
                                enemymove = "Submission"
                            if effective != "super":
                                x = random.randrange(4)
                                if x == 1:
                                    enemymove = "Body Slam"
                                    #print("Raichu used Agility")

                                if x == 2:
                                    enemymove = "Earthquake"
                                    #print("Raichu used Thunderbolt")

                                if x == 3:
                                    enemymove = "Rock Slide"
                                    #print("Raichu used Surf")

                                if x == 4:
                                    enemymove = "Submission"










class Schmovin(Mike):
    def Whosmovin(enemypokemon):
      
      if enemypokemon == "Raichu":
          Mike.Raichudoing(turn, enemypokemon)
      if enemypokemon == "Dragonite":
          Mike.DragoniteDoing(turn)
      if enemypokemon == "Charizard":
          Mike.Charizarddoing(turn)
      if enemypokemon == "Gengar":
          Mike.Gengardoing()
      if enemypokemon == "Blastoise":
          Mike.Blastoisedoing(turn)
      if enemypokemon == "Machamp":
          Mike.Machampdoing()











goingfirst = []
class Turns(Mike):

    def speedcheck(enemyspeed, currentspeed):
        if enemyspeed > currentspeed or enemyspeed == currentspeed:
            goingfirst.append("Enemy")
        if currentspeed > enemyspeed:
            goingfirst.append("User")

    def speedstat(currentpokemon):
        global currentspeed
        for i in range(pokemonlist):
            if data[i]["Name"] == currentpokemon:
                currentspeed = data[i]["Speed Stat"]

    def enemyspeed(enemypokemon):
        global enemyspeed
        for i in range(pokemonlist):
            if data[i]["Name"] == enemypokemon:
                enemyspeed = data[i]["Speed Stat"]
                print("placeholder")



    def preturn(playerpokemon1, enemypokemon, enemy):
        print("You are challenged by", enemy)
        time.sleep(times)
        print("You threw out", playerpokemon1)
        time.sleep(0.5)
        print(enemy, "threw out", enemypokemon)
        time.sleep(times)
        global going
    def turn(currentpokemon, Kaifat):
        global unique
        global meffective
        global meffective1
        global meffective2
        global onetype
        global twotype
        global movedamage
        global uniquedamage
        while Kaifat == "very":
            global turn
            f = functionality()
            print("Switch Out Or Attack")
            userdo = input("What would you like to do: ")
            if userdo == "Switch" or userdo == "switch" or userdo == "Switch Out" or userdo == "switch out" or userdo == "Switch out":
                for i in range(len(userpartyhealth)):
                    if currentpokemon == userpartyhealth[i - 1]:
                        currenthealth = userpartyhealth[i]
                print(yourteam)
                switchin = input("Pick a Pokemon to Switch into: ")
                print("You switched into", switchin)
                currentpokemon = switchin
                for i in range(len(userpartyhealth)):
                    if currentpokemon == userpartyhealth[i - 1]:
                        currenthealth = userpartyhealth[i]
                        x = i
                going = "Enemy"
                time.sleep(times)
                Schmovin.Whosmovin(enemypokemon)
                
                f.damagecalc(enemymove, enemypokemon, currentpokemon)
                enemydamage = movedamage
                if enemydamage == currenthealth or enemydamage > currenthealth:
                    enemydamage = currenthealth
                print(enemypokemon, "used", enemymove)
                print(enemypokemon, "did", enemydamage, "damage")
                currenthealth = currenthealth - enemydamage
                print(currentpokemon, "has", currenthealth, "health left")
                userpartyhealth[x] = currenthealth
                if currenthealth == 0:
                    for i in range(len(yourteam)):
                        if currentpokemon == yourteam.index(i):
                            yourteam.remove(i)
                    print(yourteam)
                    newpk = input("Who will you switch into? ")
                    for i in range(len(yourteam)):
                        if newpk == yourteam[i]:
                            currentpokemon = newpk
                    for i in range(len(userpartyhealth)):
                        if currentpokemon == userpartyhealth[i - 1]:
                            currenthealth = userpartyhealth[i]
            if len(yourteam) == 0:
              Kaifat = "no"
            if userdo == "Attack" or userdo == "attack":
                for i in range(inputteamlist):
                    if currentpokemon == inputteam[i - 1]:
                        currentmoves = inputteam[i]
                        print(currentmoves)
                use = input("Pick a move to use: ")
                time.sleep(times)
                Turns.speedcheck(enemyspeed, currentspeed)

                if "User" in goingfirst:

                    global enemyhealth
                    going = "You"
                    print("You used", use)
                    time.sleep(times)
                    # if move effect != None
                    #Do effect\
                    f = functionality()
                    for i in range(len(currentmoves)):
                        if currentmoves[i]== use:
                            f.damagecalc(use, currentpokemon, enemypokemon)
                            damage = movedamage
                            f.specialeffect(use, damage, enemyspeed, enemypokemon, currentpokemon)
                            if damage == enemyhealth or damage > enemyhealth:
                                damage = enemyhealth
                            print("It did", damage, "damage")
                            enemyhealth = enemyhealth - damage
                            time.sleep(times)
                            if enemyhealth > 0:
                                print(enemypokemon, "has", enemyhealth, "health left")
                            #print(enemypokemon)
                            if enemyhealth == 0:
                                print(enemypokemon, "fainted")
                    enemypartyhealth[1] = enemyhealth
                    
                    functionality.Mikesdeadpks(enemyhealth, currentpokemon)
                    if len(Mikesdeadguys) == 6:
                      Kaifat = "no"
                    going = "Enemy"
                    time.sleep(times)
                    Schmovin.Whosmovin(enemypokemon)
                    #Mike.Raichudoing(turn)
                    f.damagecalc(enemymove, enemypokemon, currentpokemon)
                    enemydamage = movedamage
                    for i in range(len(userpartyhealth)):
                        if currentpokemon == userpartyhealth[i - 1]:
                            currenthealth = userpartyhealth[i]
                    if enemydamage == currenthealth or enemydamage > currenthealth:
                        enemydamage = currenthealth
                    print(enemypokemon, "used", enemymove)
                    print(enemypokemon, "did", enemydamage, "damage")
                    
                    currenthealth -= enemydamage
                    print(currentpokemon, "has", currenthealth, "health left")
                    #here down = deaD
                    userpartyhealth[i] = currenthealth
                    if currenthealth == 0:
                        for i in range(len(yourteam)):
                            if currentpokemon == yourteam[i]:
                                yourteam.remove[i]
                        print(yourteam)
                        newpk = input("Who will you switch into? ")
                        for i in range(len(yourteam)):
                            if newpk == yourteam[i]:
                                currentpokemon = newpk
                        for i in range(len(userpartyhealth)):
                            if currentpokemon == userpartyhealth[i - 1]:
                                currenthealth = userpartyhealth[i]
                    if len(yourteam) == 0:
                      Kaifat = "no"
                    turn =+1



                if "Enemy" in goingfirst:
                    f = functionality()
                    going = "Enemy"
                    Schmovin.Whosmovin(enemypokemon)
                    
                    f.damagecalc(enemymove, enemypokemon, currentpokemon)
                    enemydamage = movedamage
                    for i in range(len(userpartyhealth)):
                        if currentpokemon == userpartyhealth[i - 1]:
                            currenthealth = userpartyhealth[i]
                            x = i
                    if enemydamage == currenthealth or enemydamage > currenthealth:
                        enemydamage = currenthealth
                    print(enemypokemon, "used", enemymove,)
                    print(enemypokemon, "did", enemydamage, "damage")
                    currenthealth -= enemydamage
                    print(currentpokemon, "has", currenthealth, "health left")
                    userpartyhealth[x] = currenthealth
                    global death
                    death = False
                    if currenthealth == 0:
                        for i in range(len(yourteam)):
                            if currentpokemon == yourteam[i]:
                                yourteam.remove(yourteam[i])
                                death = True
                                break
                        print(yourteam)
                        newpk = input("Who will you switch into? ")
                        for i in range(len(yourteam)):
                            if newpk == yourteam[i]:
                                currentpokemon = newpk
                        for i in range(len(userpartyhealth)):
                            if currentpokemon == userpartyhealth[i - 1]:
                                currenthealth = userpartyhealth[i]
                    if len(yourteam) == 0:
                      Kaifat = "no"
                    if death == False:
                        time.sleep(times)
                        going = "You"
                        print("You used", use)
                        time.sleep(times)
                        # if move effect != None
                        #Do effect
                        f = functionality()
                        for i in range(len(currentmoves)):
                            if currentmoves[i] == use:
                                f.damagecalc(use, currentpokemon, enemypokemon)
                                damage = movedamage
                                damage = f.specialeffect(use, damage, enemyspeed, enemypokemon, currentpokemon)
                                if damage == enemyhealth or damage > enemyhealth:
                                    damage = enemyhealth
                                print(currentpokemon, "did", damage, "damage")
                                enemyhealth = enemyhealth - damage
                                time.sleep(times)
                                if enemyhealth > 0:
                                    print(enemypokemon, "has", enemyhealth, "health left")
                                if enemyhealth == 0:
                                    print(enemypokemon, "fainted")
                    enemypartyhealth[1] = enemyhealth
                    functionality.Mikesdeadpks(enemyhealth, currentpokemon)
                    if len(Mikesdeadguys) == 6:
                      Kaifat = "no"
                    turn =+1




time.sleep(2)        


Turns.preturn(firstpokemon, enemypokemon, "Elite Four Member Mike")
Turns.turn(firstpokemon, Kaifat)
time.sleep(2)

if len(Mikesdeadguys) == 6:
  print("Congratulations! You have defeated Elite For Member Mike!")

if len(yourteam) == 0:
  print("You have no more pokemon left to battle with\n You have lost the battle\n GAME OVER")















#Tims team
#Pikachu - Toxic, Thunderbolt, Double Team, Surf
#Gyarados - 
#Moltres
#Articuno
#Venusaur
#Mewtwo#Mewtwo#Mewtwo#Mewtwo