import json
import time
import decimal
from decimal import Decimal
from random import sample
import random 

from tryingtofix import Teambuilder

times = 1.5

#going = "You"
multiplehits = [1, 2, 3, 4]
accuracynumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
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
global fullwipe
fullwipe = False
words = ["Switch", "switch", "Switch Out", "switch out", "Switch out", "Attack", "attack"]
global turn
turn = 1
global evilturn
evilturn = 1

#enemyhealth = 200
#Pokemon.teambuilder()
global paralyzed
paralyzed = False
global enemypokemon
global enemyspeed
global enemyhealth
tb = Teambuilder()
tb.teambuilder()
pluh = open("playerteaminfo.json", encoding="utf8")
inputteam = json.load(pluh)
inputteamlist = len(inputteam)
enemyteam = ["Raichu", ["Thunderbolt", "Mega Punch", "Submission", "Surf"], "Dragonite", ["Agility", "Slam", "Fire Blast", "Blizzard"], "Charizard", ["Flamethrower", "Mega Punch", "Earthquake", "Strength"], "Gengar", ["Mega Drain", "Mega Punch", "Thunderbolt", "Psychic"], "Blastoise", ["Hydro Pump", "Toxic", "Bite", "Ice Beam"], "Machamp", ["Body Slam", "Earthquake", "Rock Slide", "Submission"]]
enemyparty = [enemyteam[0], enemyteam[2], enemyteam[4], enemyteam[6], enemyteam[8], enemyteam[10]]
userparty = [inputteam[0], inputteam[2], inputteam[4], inputteam[6], inputteam[8], inputteam[10]]
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
enemypartyhealth = ["Raichu", 230, "Dragonite", 292, "Charizard", 266, "Gengar", 230, "Blastoise", 268, "Machamp", 290]
for i in range(pokemonlist):
    if inputteam[0] == data[i]["Name"]:
        global firstpkspeed
        firstpkspeed = data[i]["Speed Stat"]
    if inputteam[2] == data[i]["Name"]:
        global secondpkspeed
        secondpkspeed = data[i]["Speed Stat"]
    if inputteam[4] == data[i]["Name"]:
        global thirdpkspeed
        thirdpkspeed = data[i]["Speed Stat"]
    if inputteam[6] == data[i]["Name"]:
        global fourthpkspeed
        fourthpkspeed = data[i]["Speed Stat"]
    if inputteam[8] == data[i]["Name"]:
        global fifthpkspeed
        fifthpkspeed = data[i]["Speed Stat"]
    if inputteam[10] == data[i]["Name"]:
        global sixthpkspeed
        sixthpkspeed = data[i]["Speed Stat"]
userpartyspeed = [inputteam[0], firstpkspeed, inputteam[2], secondpkspeed, inputteam[4], thirdpkspeed, inputteam[6], fourthpkspeed, inputteam[8], fifthpkspeed, inputteam[10], sixthpkspeed]
enemypartyspeed = ["Raichu", 205, "Dragonite", 165, "Charizard", 205, "Gengar", 225, "Blastoise", 161, "Machamp", 115]
userpartyaccuracy = [inputteam[0], 1, inputteam[2], 1, inputteam[4], 1, inputteam[6], 1, inputteam[8], 1, inputteam[10], 1]
enemypartyaccuracy = ["Raichu", 1, "Dragonite", 1, "Charizard", 1, "Gengar", 1, "Blastoise", 1, "Machamp", 1]
firstpokemon = inputteam[0]
firstenemypokemon = enemyparty[0]
enemypokemon = firstenemypokemon
for i in range(len(data)):
    if enemypokemon == data[i]["Name"]:
        enemyspeed = data[i]["Speed Stat"]
        enemyhealth = data[i]["Health Stat"]
for i in range(len(data)):
    if enemypokemon == data[i]["Name"]:
        enemyspeed = data[i]["Speed Stat"]
        enemyhealth = data[i]["Health Stat"]
global currentpokemon
currentpokemon = firstpokemon
global currentspeed
global currenthealth
for i in range(len(data)):
    if currentpokemon == data[i]["Name"]:
        currentspeed = data[i]["Speed Stat"]
        currenthealth = data[i]["Health Stat"]
goingfirst = ["pluh"]




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
    def switch(switch, newpokemon):
        global enemypokemon
        enemypokemon = newpokemon

    def dead(oppositehealth):
        if oppositehealth == 0:
            global currentpokemon
            
            print(oppositepokemon, "has fainted")
            print(userparty)
            switchin = input("Pick a Pokemon to switch in: ")
            currentpokemon = switchin
    
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

    def damagecalc(damagecalc, move, attackingpk, enemypk):
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
        if len(data[enemynumber]["Types"]) == 2:
            meffective = decimal.Decimal(meffective1) * decimal.Decimal(meffective2)
            math5 *= decimal.Decimal(meffective)
        global movedamage
        movedamage = round(math5)
        if moves[movenumber]["category"] == "None":
            movedamage = 0
        return(movedamage)
    def specialeffect(specialeffect, move, damage, enemyspeed, enemypk, userpk, enemypartystatus, enemymove, enemydamage, movego, userpartyhealth, enemypartyaccuracy):
        f = functionality
        global damageeffect
        damageeffect = False
        global newdamage
        newdamage = False
        global speedeffect
        speedeffect = False
        global newspeed
        newspeed = False
        global effect
        effect = False
        global neweffect
        neweffect = False
        for i in range(movelist):
            if move == moves[i]["name"]:
                movenumber = i
        for i in range(movelist):
            if enemymove == moves[i]["name"]:
                enemymovenumber = i
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
            hitamount = sample(multiplehits, 1)[0]
            for i in range(hitamount):
                print(userpk, "did", setdamage, "damage")
                print("It hit again!")
            setdamage = damage
            global uniquedamage
            uniquedamage = damage
            for i in range(hitamount):
                print(userpk, "did", setdamage, "damage")
                uniquedamage += setdamage
            edamage = uniquedamage
            damageeffect = True
        if "SpeedDown" in moves[movenumber]["effect"]:
            onestage = decimal.Decimal(2) / decimal.Decimal(3)
            enemyspeed *= onestage 
            espeed = enemyspeed
            speedeffect = True
            print(enemypk, "had its speed go down!")
        if "SpeedSharpUp" in moves[movenumber]["effect"]:
            twostage = decimal.Decimal(5) / decimal.Decimal(3)
            enemyspeed *= twostage
            espeed = enemyspeed
            speedeffect = True
            print(userpk, "had its speed sharply raised!")
        if "HitsTwice" in moves[movenumber]["effect"]:
            edamage = damage * 2
            print(userpk, "used", move)
            print(userpk, "did", damage, "damage")
            print("It hit again!")
            damageeffect = True
        if "Poison" in moves[movenumber]["effect"] or " Poison" in moves[movenumber]["effect"]:
            poisonchance = random.randint(0, 100)
            if moves[movenumber]["name"] == "Twineedle":
                prob = 20
            if moves[movenumber]["name"] == "Toxic":
                prob = 100
            if poisonchance < prob or poisonchance == prob:
                for i in range(len(enemypartystatus)):
                    if enemypk == enemypartystatus[i - 1]:
                        if not("Poison" in data[enemynumber]["Types"]):
                            enemypartystatus[i] = "Poisoned"
                            print(enemypk, "got poisoned!")
        if "Paralyze" in moves[movenumber]["effect"]:
            if moves[movenumber]["name"] == "Thunder" or moves[movenumber]["name"] == "Thunder Punch" or moves[movenumber]["name"] == "Thunder Shock" or moves[movenumber]["name"] == "Thunderbolt":
                thunderprob = 10
            paralyzechance = random.randint(0, 100)
            if paralyzechance < thunderprob or paralyzechance == thunderprob:
                for i in range(len(enemypartystatus)):
                    if enemypk == enemypartystatus[i - 1]:
                        if not("Electric" in data[enemynumber]["Types"]):
                            enemypartystatus[i] = "Paralyzed"
                            print(enemypk, "got paralyzed!")
        if "AlwaysParalyze" in moves[movenumber]["effect"]:
            for i in range(len(enemypartystatus)):
                if enemypk == enemypartystatus[i - 1]:
                    if not("Electric" in data[enemynumber]["Types"]):
                        enemypartystatus[i] = "Paralyzed"
                        print(enemypokemon, "got paralyzed!")
        if "ItCounter" in moves[movenumber]["effect"]:
            if "Enemy" in goingfirst:
                if moves[enemymovenumber]["type"] == "Fighting" or moves[enemymovenumber]["type"]:
                    if moves[enemymovenumber]["power"] != 0:
                        edamage = enemydamage * 2
                        damageeffect = True
                    else:
                        edamage = 0
                        damageeffect = True
                        print("The move missed!")
                else:
                    edamage = 0
                    damageeffect = True  
                    print("The move missed!")
            else: 
                edamage = 0
                damageeffect = True
                print("The move missed!")
        if "Flinch13" in moves[movenumber]["effect"]:
            flinchnumber = random.randint(0, 100)
            flinchchance = 30
            if flinchnumber < flinchchance or flinchnumber == flinchchance:
                effect = True
                eeffect = "Flinch"
        if "Seismictoss" in moves[movenumber]["effect"]:
            edamage = enemynumber
            damageeffect = True
        if "AccuracyDown" in moves[movenumber]["effect"]:
            newaccuracy = decimal.Decimal(2) / decimal.Decimal(3)
            for i in range(len(enemypartyaccuracy)):
                if enemypk == enemypartyaccuracy[i - 1]:
                    print(newaccuracy, "newaccuracy")
                    enemypartyaccuracy[i] = enemypartyaccuracy[i] * newaccuracy
        if "ToxicEffect" in moves[movenumber]["effect"]:
            for i in range(len(enemypartystatus)):
                if enemypk == enemypartystatus[i - 1]:
                    if not("Poison" in data[enemynumber]["Types"]):
                        enemypartystatus[i] = "Toxic"
                        print(enemypk, "got badly poisoned!")
        if effect == True:
            neweffect = True
            return(eeffect)
        if damageeffect == True:
            newdamage = True
            return(edamage)
        if speedeffect == True:
            newspeed = True
            return(espeed)
    def accuracycheck(accuracycheck, move, accuracy):
        for i in range(movelist):
            if move == moves[i]["name"]:
                anumber = moves[i]["accuracy"]
                accnumber = anumber * accuracy
        randnumb = random.randint(0,100)
        if randnumb < accnumber:
            movego = True
        if randnumb == accnumber:
            movego = True
        if randnumb > accnumber:
            movego = False
        return(movego)

 

        

    


class Ai():
    def supereffectivecheck(usermovetype):
        print("placeholder")


class Mike(functionality):
    def enemydoing(enemypokemon):
        global enemymove
        if enemypokemon == "Raichu":
            silly = random.randint(0, 4)
            if silly == 1:
                enemymove = "Thunderbolt"
            if silly == 2:
                enemymove = "Mega Punch"
            if silly == 3:
                enemymove = "Submission"
            if silly == 4:
                enemymove = "Surf"
        if enemypokemon == "Dragonite":
            zany = random.randint(0, 4)
            if zany == 1:
                enemymove = "Agility"
            if zany == 2:
                enemymove = "Slam"
            if zany == 3:
                enemymove = "Fire Blast"
            if zany == 4:
                enemymove = "Blizzard"
        if enemypokemon == "Charizard":
            goofy = random.randint(0, 4)
            if goofy == 1:
                enemymove = "Flamethrower"
            if goofy == 2:
                enemymove = "Mega Punch"
            if goofy == 3:
                enemymove = "Earthquake"
            if goofy == 4:
                enemymove = "Strength"
        if enemypokemon == "Gengar":
            tomfoolery = random.randint(0, 4)
            if tomfoolery == 1:
                enemymove = "Mega Drain"
            if tomfoolery == 2:
                enemymove = "Thunderbolt"
            if tomfoolery == 3:
                enemymove = "Mega Punch"
            if tomfoolery == 4:
                enemymove = "Psychic"
        if enemypokemon == "Blastoise":
            buffoonery = random.randint(0, 4)
            if buffoonery == 1:
                enemymove = "Hydro Pump"
            if buffoonery == 2:
                enemymove = "Toxic"
            if buffoonery == 3:
                enemymove = "Bite"
            if buffoonery == 4:
                enemymove = "Ice Beam"
        if enemypokemon == "Machamp":
            lobotomy = random.randint(0, 4)
            if lobotomy == 1:
                enemymove = "Body Slam"
            if lobotomy == 2:
                enemymove = "Earthquake"
            if lobotomy == 3:
                enemymove = "Rock Slide"
            if lobotomy == 4:
                enemymove = "Submission"
        return(enemymove)





class Turns(Mike):
    def speedcheck(enemyspeed, currentspeed):
        if enemyspeed > currentspeed:
            goingfirst[0] = ("Enemy")
        if currentspeed > enemyspeed:
            goingfirst[0] = ("User")
        if enemyspeed == currentspeed:
            goingfirst[0] = ("Enemy")
    



    def preturn(playerpokemon1, enemypokemon1, enemy):
        print("You are challenged by", enemy)
        time.sleep(times)
        print("You threw out", playerpokemon1)
        time.sleep(0.5)
        print(enemy, "threw out", enemypokemon1)
        time.sleep(times)
        global going
    def turn(currentpokemon, enemypokemon1):
        global unique
        global meffective
        global meffective1
        global meffective2
        global onetype
        global twotype
        global movedamage
        global uniquedamage
        global fullwipe
        global enemyhealth
        global crithappen
        global enemyspeed
        global newdamage
        global newspeed
        global paralyzed
        paralyzed = False
        global flinched
        flinched = False
        global enemypokemon
        while fullwipe == False:
            f = functionality()
            print("Switch Out Or Attack")
            userdo = "Haunted by Laufey"
            while not(userdo in words):
                userdo = input("What would you like to do: ")
            if userdo == "Switch" or userdo == "switch" or userdo == "Switch Out" or userdo == "switch out" or userdo == "Switch out":
                for i in range(len(userpartyhealth)):
                    if currentpokemon == userpartyhealth[i - 1]:
                        currenthealth = userpartyhealth[i]
                print(userparty)
                switchin = "Roses by Kanye West"
                while not(switchin in userparty):
                    switchin = input("Pick a Pokemon to Switch into: ")
                print("You switched into", switchin)
                currentpokemon = switchin
                for i in range(len(userpartyhealth)):
                    if currentpokemon == userpartyhealth[i - 1]:
                        currenthealth = userpartyhealth[i]
                        x = i
                for i in range(len(userpartyspeed)):
                    if currentpokemon == userpartyspeed[i-1]:
                        currentspeed = userpartyspeed[i]
                going = "Enemy"
                time.sleep(times)
                enemymove = Mike.enemydoing(enemypokemon)
                for i in range(len(enemypartyaccuracy)):
                    if enemypokemon == enemypartyaccuracy[i - 1]:
                        accuracy = enemypartyaccuracy[i]
                gomove = f.accuracycheck(enemymove, accuracy)
                if gomove == True:
                    for i in range(len(userpartystatus)):
                        if currentpokemon == userpartystatus[i - 1]:
                            if userpartystatus[i] == "Paralyzed":
                                paralyzechance = 25
                                pchance = random.randint(0, 100)
                                if pchance < paralyzechance or pchance == paralyzechance:
                                    paralyzed = True
                                    print(enemypokemon, "couldn't move because he was paralyzed")
                    if paralyzed == False:
                        enemydamage = f.damagecalc(enemymove, enemypokemon, currentpokemon)
                        thing = f.specialeffect(enemymove, enemydamage, currentspeed, currentpokemon, enemypokemon, userpartystatus, "Captain Underpants' Theme Song", "A and W", gomove, enemypartyhealth, userpartyaccuracy)
                        if newdamage == True:
                            enemydamage = thing
                        if newspeed == True:
                            enemyspeed = thing
                            for i in range(len(enemypartyspeed)):
                                if enemypokemon == enemypartyspeed[i - 1]:
                                    enemypartyspeed[i] = enemyspeed 
                        if enemydamage == currenthealth or enemydamage > currenthealth:
                            enemydamage = currenthealth
                        print(enemypokemon, "used", enemymove)
                        print(enemypokemon, "did", enemydamage, "damage")
                        if crithappen == True:
                            print("It was a crit!")
                        currenthealth = currenthealth - enemydamage
                        print(currentpokemon, "has", currenthealth, "health left")
                        userpartyhealth[x] = currenthealth
                        if currenthealth == 0:
                            for i in range(len(userparty)):
                                print(len(userparty))
                                print(userparty[i])
                                if currentpokemon == userparty[i]:
                                    userparty.remove(userparty[i])
                                    break
                            print(userparty)
                            newpk = "Mercury by Steve Lacy"
                            while not(newpk in userparty):
                                newpk = input("Who will you switch into? ")
                            for i in range(len(userparty)):
                                if newpk == userparty[i]:
                                    currentpokemon = newpk
                            for i in range(len(userpartyhealth)):
                                if currentpokemon == userpartyhealth[i - 1]:
                                    currenthealth = userpartyhealth[i]
                                    x = i
                            if enemydamage == currenthealth or enemydamage > currenthealth:
                                enemydamage = currenthealth
                            print(enemypokemon, "used", enemymove, )
                            print(enemypokemon, "did", enemydamage, "damage")
                            currenthealth -= enemydamage
                            print(currentpokemon, "has", currenthealth, "health left")
                            for i in range(len(userpartystatus)):
                                if userpartystatus[i] == "Paralyzed":
                                    for i in range(len(userpartyspeed)):
                                        if currentpokemon == userpartyspeed[i - 1]:
                                            speeddown = decimal.Decimal(1) / decimal.Decimal(4)
                                            currentspeed = userpartyspeed[i]
                                            cs = currentspeed * speeddown
                                            currentspeed = round(cs)
                                            userpartyspeed[i] = currentspeed
                            userpartyhealth[x] = currenthealth
                            if currenthealth == 0:
                                for i in range(len(userparty)):
                                    if currentpokemon == userparty[i]:
                                        userparty.remove(userparty[i])
                                        break
                                if len(userparty) > 0:
                                    newpk = "Drive ME Crazy by Lil Yachty"
                                    while not(newpk in userparty):
                                        newpk = input("Who will you switch into? ")
                                    for i in range(len(userparty)):
                                        if newpk == userparty[i]:
                                            currentpokemon = newpk
                                    for i in range(len(userpartyhealth)):
                                        if currentpokemon == userpartyhealth[i - 1]:
                                            currenthealth = userpartyhealth[i]
                                    for i in range(len(userpartyspeed)):
                                        if currentpokemon == userpartyspeed[i-1]:
                                            currentspeed = userpartyspeed[i]
                                            print(currentspeed)
                                if len(userparty) == 0:
                                    fullwipe = True
                                    break
                if gomove == False:
                    print(enemypokemon, "missed their attack!")
                    if enemymove == "Hi Jump Kick" or enemymove == "Jump Kick":
                        for i in range(len(enemypartyhealth)):
                            if enemypokemon == enemypartyhealth[i - 1]:
                                newhealth = enemypartyhealth[i]
                                newhealth = newhealth - 1
                                enemypartyhealth[i] = newhealth
                                print(enemypokemon, "took damage from missing their move!")
                                print(enemypokemon, "has", newhealth, "health left")
            
            if userdo == "Attack" or userdo == "attack":
                for i in range(inputteamlist):
                    if currentpokemon == inputteam[i - 1]:
                        currentmoves = inputteam[i]
                        print(currentmoves)
                use = "Cactus by the Pixies"
                while not(use in currentmoves):
                    use = input("Pick a move to use: ")
                time.sleep(times)
                for i in range(len(enemypartyspeed)):
                    if enemypokemon == enemypartyspeed[i - 1]:
                        enemyspeed = enemypartyspeed[i]
                for i in range(len(userpartyspeed)):
                    if currentpokemon == userpartyspeed[i - 1]:
                        currentspeed = userpartyspeed[i]
                Turns.speedcheck(enemyspeed, currentspeed)
            
                if "User" in goingfirst:
                    f = functionality()
                    time.sleep(times)
                    going = "You"
                    print("You used", use)
                    for i in range(len(userpartyaccuracy)):
                        if currentpokemon == userpartyaccuracy[i - 1]:
                            accuracy = userpartyaccuracy[i]
                    Weezer = f.accuracycheck(use, accuracy)
                    time.sleep(times)
                    f = functionality()
                    for i in range(len(currentmoves)):
                        if currentmoves[i] == use:
                            if Weezer == True:
                                for i in range(len(userpartystatus)):
                                    if currentpokemon == userpartystatus[i - 1]:
                                        if userpartystatus[i] == "Paralyzed":
                                            paralyzechance = 25
                                            pchance = random.randint(0, 100)
                                            if pchance < paralyzechance or pchance == paralyzechance:
                                                paralyzed = True
                                                print(currentpokemon, "couldn't move because he was paralyzed")
                                if paralyzed == False:
                                    damage = f.damagecalc(use, currentpokemon, enemypokemon1)
                                    thing = f.specialeffect(use, damage, enemyspeed, enemypokemon, currentpokemon, eliteteamstatus, "Heroes", "Christmas Wrapping", Weezer, userpartyhealth, enemypartyaccuracy)
                                    if newdamage == True:
                                        damage = thing
                                    if newspeed == True:
                                        enemyspeed = thing
                                        for i in range(len(enemypartyspeed)):
                                            if enemypokemon == enemypartyspeed[i - 1]:
                                                enemypartyspeed[i] = enemyspeed 
                                    if neweffect == True:
                                        if thing == "Flinch":
                                            flinched = True
                                    if damage == enemyhealth or damage > enemyhealth:
                                        damage = enemyhealth
                                    print(currentpokemon, "did", damage, "damage")
                                    if crithappen == True:
                                        print("It was a crit!")
                                    enemyhealth = enemyhealth - damage
                                    time.sleep(times)
                    if enemyhealth > 0:
                        print(enemypokemon, "has", enemyhealth, "health left")
                        for i in range(len(eliteteamstatus)):
                            if eliteteamstatus[i] == "Paralyzed":
                                for i in range(len(enemypartyspeed)):
                                    if enemypokemon == enemypartyspeed[i - 1]:
                                        speeddown = decimal.Decimal(1) / decimal.Decimal(4)
                                        enemyspeed = enemypartyspeed[i]
                                        cs = enemyspeed * speeddown
                                        enemyspeed = round(cs)
                                        enemypartyspeed[i] = enemyspeed
                    if enemyhealth == 0:
                        print(enemypokemon, "has fainted")
                        for i in range(len(enemyparty)):
                            if enemypokemon == enemyparty[i]:
                                enemyparty.remove(enemypokemon)
                                break
                        pleasemrwhalengivemeagoodgrade = random.randint(0, len(enemyparty))
                        pluh = pleasemrwhalengivemeagoodgrade - 1
                        enemypokemon = enemyparty[pluh]
                        print("Mike switched in to", enemypokemon)
                        for i in range(len(enemypartyhealth)):
                            if enemypokemon == enemypartyhealth[i - 1]:
                                enemyhealth = enemypartyhealth[i]
                        for i in range(len(enemypartyspeed)):
                            if enemypokemon == enemypartyspeed[i-1]:
                                enemyspeed = enemypartyspeed[i]
                    if len(enemyparty) == 0:
                        break



                                
                    enemypartyhealth[1] = enemyhealth
                    if Weezer == False:
                        print(currentpokemon, "missed their attack!")
                        if use == "Hi Jump Kick" or use == "Jump Kick":
                            for i in range(len(userpartyhealth)):
                                if currentpokemon == userpartyhealth[i - 1]:
                                    newhealth = userpartyhealth[i]
                                    newhealth = newhealth - 1
                                    userpartyhealth[i] = newhealth
                                    print(currentpokemon, "took damage from missing their move!")
                                    print(currentpokemon, "has", newhealth, "health left")
                    going = "Enemy"
                    enemymove = Mike.enemydoing(enemypokemon)
                    for i in range(len(enemypartyaccuracy)):
                        if enemypokemon == enemypartyaccuracy[i - 1]:
                            accuracy = enemypartyaccuracy[i]
                    gomove = f.accuracycheck(enemymove, accuracy)
                    if gomove == True and flinched == False:
                        for i in range(len(eliteteamstatus)):
                            if enemypokemon == eliteteamstatus[i - 1]:
                                if eliteteamstatus[i] == "Paralyzed":
                                    paralyzechance = 25
                                    pchance = random.randint(0, 100)
                                    if pchance < paralyzechance or pchance == paralyzechance:
                                        paralyzed = True
                                        print(enemypokemon, "couldn't move because they were paralyzed")
                        if paralyzed == False:
                            enemydamage = f.damagecalc(enemymove, enemypokemon, currentpokemon)
                            thing = f.specialeffect(enemymove, enemydamage, currentspeed, currentpokemon, enemypokemon, userpartystatus, use, damage, gomove, enemypartyhealth, userpartyaccuracy)
                            if newdamage == True:
                                enemydamage = thing
                            if newspeed == True:
                                currentspeed = thing
                                for i in range(len(userpartyspeed)):
                                    if currentpokemon == userpartyspeed[i - 1]:
                                        userpartyspeed[i] = currentspeed 
                            for i in range(len(userpartyhealth)):
                                if currentpokemon == userpartyhealth[i - 1]:
                                    currenthealth = userpartyhealth[i]
                                    x = i
                            if enemydamage == currenthealth or enemydamage > currenthealth:
                                enemydamage = currenthealth
                            print(enemypokemon, "used", enemymove, )
                            print(enemypokemon, "did", enemydamage, "damage")
                            if crithappen == True:
                                print("It was a crit!")
                            currenthealth -= enemydamage
                            print(currentpokemon, "has", currenthealth, "health left")
                            for i in range(len(userpartystatus)):
                                if userpartystatus[i] == "Paralyzed":
                                    for i in range(len(userpartyspeed)):
                                        if currentpokemon == userpartyspeed[i - 1]:
                                            speeddown = decimal.Decimal(1) / decimal.Decimal(4)
                                            currentspeed = userpartyspeed[i]
                                            cs = currentspeed * speeddown
                                            currentspeed = round(cs)
                                            userpartyspeed[i] = currentspeed
                            userpartyhealth[x] = currenthealth
                            if currenthealth == 0:
                                print(currentpokemon, "has fainted")
                                for i in range(len(userparty)):
                                    if currentpokemon == userparty[i]:
                                        userparty.remove(userparty[i])
                                        break
                                print(userparty)
                                if len(userparty) > 0:
                                    newpk = "Dumb by Nirvana"
                                    while not(newpk in userparty):
                                        newpk = input("Who will you switch into? ")
                                    for i in range(len(userparty)):
                                        if newpk == userparty[i]:
                                            currentpokemon = newpk
                                    for i in range(len(userpartyhealth)):
                                        if currentpokemon == userpartyhealth[i - 1]:
                                            currenthealth = userpartyhealth[i]
                                    for i in range(len(userpartyspeed)):
                                        if currentpokemon == userpartyspeed[i-1]:
                                            currentspeed = userpartyspeed[i]
                                if len(userparty) == 0:
                                    fullwipe = True
                                    break
                    if flinched == True:
                        print(enemypokemon, "flinched!")
                    if gomove == False:
                        print(enemypokemon, "missed their attack!")
                        if enemymove == "Hi Jump Kick" or enemymove == "Jump Kick":
                            for i in range(len(enemypartyhealth)):
                                if enemypokemon == enemypartyhealth[i - 1]:
                                    newhealth = enemypartyhealth[i]
                                    newhealth = newhealth - 1
                                    enemypartyhealth[i] = newhealth
                                    print(enemypokemon, "took damage from missing their move!")
                                    print(enemypokemon, "has", newhealth, "health left")
            
                
               

                if "Enemy" in goingfirst:
                    f = functionality()
                    going = "Enemy"
                    enemymove = Mike.enemydoing(enemypokemon)
                    for i in range(len(enemypartyaccuracy)):
                        if enemypokemon == enemypartyaccuracy[i - 1]:
                            accuracy = enemypartyaccuracy[i]
                    gomove = f.accuracycheck(enemymove, accuracy)
                    if gomove == True:
                        for i in range(len(eliteteamstatus)):
                            if enemypokemon == eliteteamstatus[i - 1]:
                                if eliteteamstatus[i] == "Paralyzed":
                                    print(pluh)
                                    paralyzechance = 25
                                    pchance = random.randint(0, 100)
                                    if pchance < paralyzechance or pchance == paralyzechance:
                                        paralyzed = True
                                        print(enemypokemon, "couldn't move because he was paralyzed")
                        if paralyzed == False:
                            enemydamage = f.damagecalc(enemymove, enemypokemon, currentpokemon)
                            thing = f.specialeffect(enemymove, enemydamage, currentspeed, currentpokemon, enemypokemon, userpartystatus, "Barry Bonds", "LOVE.FEAT.ZACARI", gomove, enemypartyhealth, userpartyaccuracy)
                            if newdamage == True:
                                enemydamage = thing
                            if newspeed == True:
                                currentspeed = thing
                                for i in range(len(userpartyspeed)):
                                    if currentpokemon == userpartyspeed[i - 1]:
                                        userpartyspeed[i] = currentspeed 
                            if neweffect == True:
                                if thing == "Flinch":
                                    flinched = True
                            for i in range(len(userpartyhealth)):
                                if currentpokemon == userpartyhealth[i - 1]:
                                    currenthealth = userpartyhealth[i]
                                    x = i
                            if enemydamage == currenthealth or enemydamage > currenthealth:
                                enemydamage = currenthealth
                            print(enemypokemon, "used", enemymove, )
                            print(enemypokemon, "did", enemydamage, "damage")
                            if crithappen == True:
                                print("It was a crit!")
                            currenthealth -= enemydamage
                            print(currentpokemon, "has", currenthealth, "health left")
                            for i in range(len(userpartystatus)):
                                if userpartystatus[i] == "Paralyzed":
                                    for i in range(len(userpartyspeed)):
                                        if currentpokemon == userpartyspeed[i - 1]:
                                            speeddown = decimal.Decimal(1) / decimal.Decimal(4)
                                            currentspeed = userpartyspeed[i]
                                            cs = currentspeed * speeddown
                                            currentspeed = round(cs)
                                            userpartyspeed[i] = currentspeed  
                            userpartyhealth[x] = currenthealth
                    for i in range(len(userpartyhealth)):
                        if currentpokemon == userpartyhealth[i - 1]:
                            currenthealth = userpartyhealth[i]
                    global death
                    death = False
                    if currenthealth == 0:
                        print(currentpokemon, "has fainted")
                        for i in range(len(userparty)):
                            if currentpokemon == userparty[i]:
                                userparty.remove(userparty[i])
                                death = True
                                break
                        print(userparty)
                        if len(userparty) > 0:
                            newpk = "Wesley's Theory by Kendrick Lamar"
                            while not(newpk in userparty):
                                newpk = input("Who will you switch into? ")
                            for i in range(len(userparty)):
                                if newpk == userparty[i]:
                                    currentpokemon = newpk
                            for i in range(len(userpartyhealth)):
                                if currentpokemon == userpartyhealth[i - 1]:
                                    currenthealth = userpartyhealth[i]
                            for i in range(len(userpartyspeed)):
                                if currentpokemon == userpartyspeed[i-1]:
                                    currentspeed = userpartyspeed[i]
                        if len(userparty) == 0:
                            fullwipe = True
                            break
                    if gomove == False:
                        print(enemypokemon, "missed their attack!")
                        if enemymove == "Hi Jump Kick" or enemymove == "Jump Kick":
                            for i in range(len(enemypartyhealth)):
                                if enemypokemon == enemypartyhealth[i - 1]:
                                    newhealth = enemypartyhealth[i]
                                    newhealth = newhealth - 1
                                    enemypartyhealth[i] = newhealth
                                    print(enemypokemon, "took damage from missing their move!")
                                    print(enemypokemon, "has", newhealth, "health left")
            
                    if death == False:
                        time.sleep(times)
                        going = "You"
                        print("You used", use)
                        time.sleep(times)
                        f = functionality()
                        for i in range(len(currentmoves)):
                            if currentmoves[i] == use:
                                for i in range(len(userpartyaccuracy)):
                                    if currentpokemon == userpartyaccuracy[i - 1]:
                                        accuracy = userpartyaccuracy[i]
                                Weezer = f.accuracycheck(use, accuracy)
                                if Weezer == True and flinched == False:
                                    for i in range(len(userpartystatus)):
                                        if currentpokemon == userpartystatus[i - 1]:
                                            if userpartystatus[i] == "Paralyzed":
                                                paralyzechance = 25
                                                pchance = random.randint(0, 100)
                                                if pchance < paralyzechance or pchance == paralyzechance:
                                                    paralyzed = True
                                                    print(currentpokemon, "couldn't move because they were paralyzed")
                                    if paralyzed == False:
                                        damage = f.damagecalc(use, currentpokemon, enemypokemon1)
                                        thing = f.specialeffect(use, damage, enemyspeed, enemypokemon, currentpokemon, eliteteamstatus, enemymove, enemydamage, Weezer, userpartyhealth, enemypartyaccuracy)
                                        if newdamage == True:
                                            damage = thing
                                        if newspeed == True:
                                            enemyspeed = thing
                                            for i in range(len(enemypartyspeed)):
                                                if enemypokemon == enemypartyspeed[i - 1]:
                                                    enemypartyspeed[i] = enemyspeed
                                        if damage == enemyhealth or damage > enemyhealth:
                                            damage = enemyhealth
                                        print(currentpokemon, "did", damage, "damage")
                                        if crithappen == True:
                                            print("It was a crit!")
                                        enemyhealth = enemyhealth - damage
                                        time.sleep(times)
                                        if enemyhealth > 0:
                                            print(enemypokemon, "has", enemyhealth, "health left")
                                            for i in range(len(eliteteamstatus)):
                                                if eliteteamstatus[i] == "Paralyzed":
                                                    for i in range(len(enemypartyspeed)):
                                                        if enemypokemon == enemypartyspeed[i - 1]:
                                                            speeddown = decimal.Decimal(1) / decimal.Decimal(4)
                                                            enemyspeed = enemypartyspeed[i]
                                                            cs = enemyspeed * speeddown
                                                            enemyspeed = round(cs)
                                                            enemypartyspeed[i] = enemyspeed
                                    if enemyhealth == 0:
                                        print(enemypokemon, "has fainted")
                                        for i in range(len(enemyparty)):
                                            if enemypokemon == enemyparty[i]:
                                                enemyparty.remove(enemypokemon)
                                                break
                                        pleasemrwhalengivemeagoodgrade = random.randint(0, len(enemyparty))
                                        pluh = pleasemrwhalengivemeagoodgrade - 1
                                        enemypokemon = enemyparty[pluh]
                                        print("Mike switched into", enemypokemon)
                                        for i in range(len(enemypartyhealth)):
                                                if enemypokemon == enemypartyhealth[i - 1]:
                                                    enemyhealth = enemypartyhealth[i]
                                        for i in range(len(enemypartyspeed)):
                                            if enemypokemon == enemypartyspeed[i-1]:
                                                enemyspeed = enemypartyspeed[i]
                                if flinched == True:
                                    print(currentpokemon, "flinched!")
                                if Weezer == False:
                                    print(currentpokemon, "missed their attack!")
                                    if use == "Hi Jump Kick" or use == "Jump Kick":
                                        for i in range(len(userpartyhealth)):
                                            if currentpokemon == userpartyhealth[i - 1]:
                                                newhealth = userpartyhealth[i]
                                                newhealth = newhealth - 1
                                                userpartyhealth[i] = newhealth
                                                print(currentpokemon, "took damage from missing their move!")
                                                print(currentpokemon, "has", newhealth, "health left")
                    if len(enemyparty) == 0:
                        break
            

            for i in range(len(userpartystatus)):
                if currentpokemon == userpartystatus[i - 1]:
                    if userpartystatus[i] == "Poisoned":
                        for i in range(pokemonlist):
                            if currentpokemon == data[i]["Name"]:
                                fullhealth = data[i]["Health Stat"]
                                poisond = decimal.Decimal(fullhealth) / 16
                                poisondamage = round(poisond)
                                if poisondamage > currenthealth:
                                    poisondamage = currenthealth
                                currenthealth = currenthealth - poisondamage
                                print(currentpokemon, "took", poisondamage, "damage from the poison!")
                                print(currentpokemon, "has", currenthealth, "health left")
                                for i in range(len(userpartyhealth)):
                                    if currentpokemon == userpartyhealth[i - 1]:
                                        userpartyhealth[i] = currenthealth
            for i in range(len(userpartystatus)):
                global turn
                if currentpokemon == userpartystatus[i - 1]:
                    if userpartystatus[i] == "Toxic":
                        for i in range(pokemonlist):
                            if currentpokemon == data[i]["Name"]:
                                fullhealth = data[i]["Health Stat"]
                                poisond = decimal.Decimal(fullhealth) / 16
                                pd = round(poisond)
                                poisondamage = pd * turn
                                if poisondamage > currenthealth:
                                    poisondamage = currenthealth 
                                currenthealth = currenthealth - poisondamage
                                print(currentpokemon, "took", poisondamage, "from the toxic!")
                                print(currentpokemon, "has", currenthealth, "health left")
                                for i in range(len(userpartyhealth)):
                                    if currentpokemon == userpartyhealth[i - 1]:
                                        userpartyhealth[i] = currenthealth
                        turn += 1
                    if userpartystatus[i] != "Toxic":
                        turn = 1
            if currenthealth == 0:
                print(currentpokemon, "has fainted")
                for i in range(len(userparty)):
                    if currentpokemon == userparty[i]:
                        userparty.remove(userparty[i])
                        death = True
                        break
                print(userparty)
                if len(userparty) > 0:
                    newpk = "Wesley's Theory by Kendrick Lamar"
                    while not(newpk in userparty):
                        newpk = input("Who will you switch into? ")
                    for i in range(len(userparty)):
                        if newpk == userparty[i]:
                            currentpokemon = newpk
                    for i in range(len(userpartyhealth)):
                        if currentpokemon == userpartyhealth[i - 1]:
                            currenthealth = userpartyhealth[i]
                    for i in range(len(userpartyspeed)):
                        if currentpokemon == userpartyspeed[i-1]:
                            currentspeed = userpartyspeed[i]
                if len(userparty) == 0:
                    fullwipe = True
                    break


            for i in range(len(eliteteamstatus)):
                if enemypokemon == eliteteamstatus[i - 1]:
                    if eliteteamstatus[i] == "Poisoned":
                        for i in range(pokemonlist):
                            if enemypokemon == data[i]["Name"]:
                                fullhealth = data[i]["Health Stat"]
                                poisond = decimal.Decimal(fullhealth) / 16
                                poisondamage = round(poisond)
                                if poisondamage > enemyhealth:
                                    poisondamage = enemyhealth
                                enemyhealth = enemyhealth - poisondamage
                                print(enemypokemon, "took", poisondamage, "damage from the poison!")
                                print(enemypokemon, "has", enemyhealth, "health left")
                                for i in range(len(enemypartyhealth)):
                                    if enemypokemon == enemypartyhealth[i - 1]:
                                        enemypartyhealth[i] = enemyhealth
            for i in range(len(eliteteamstatus)):
                global evilturn
                if enemypokemon == eliteteamstatus[i - 1]:
                    if eliteteamstatus[i] == "Toxic":
                        for i in range(pokemonlist):
                            if enemypokemon == data[i]["Name"]:
                                fullhealth = data[i]["Health Stat"]
                                poisond = decimal.Decimal(fullhealth) / 16
                                pd = round(poisond)
                                poisondamage = pd * turn
                                if poisondamage > enemyhealth:
                                    poisondamage = enemyhealth 
                                enemyhealth = enemyhealth - poisondamage
                                print(enemypokemon, "took", poisondamage, "from the toxic!")
                                print(enemypokemon, "has", enemyhealth, "health left")
                                for i in range(len(enemypartyhealth)):
                                    if enemypokemon == enemypartyhealth[i - 1]:
                                        enemypartyhealth[i] == enemyhealth
                        evilturn += 1
                    if eliteteamstatus[i] != "Toxic":
                        evilturn = 1
                                    
            if enemyhealth == 0:
                print(enemypokemon, "has fainted")
                break

    


                




        
      

Turns.preturn(firstpokemon, enemypokemon, "Elite Four Member Mike")
Turns.turn(firstpokemon, enemypokemon)

        



        


