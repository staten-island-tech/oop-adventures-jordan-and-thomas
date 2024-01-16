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
test = open("move.json", encoding="utf8")
moves = json.load(test)
movelist = len(moves)

quiz = open("pokemon.json", encoding="utf8")
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
enemypokemon1 = "Raichu"
enemypokemon = enemypokemon1
for i in range(len(data)):
    if enemypokemon == data[i]["Name"]:
        enemyspeed = data[i]["Speed Stat"]
        enemyhealth = data[i]["Health Stat"]
tb = Teambuilder()
tb.teambuilder()
pluh = open("playerteaminfo.json", encoding="utf8")
inputteam = json.load(pluh)
inputteamlist = len(inputteam)
enemyparty = ["Raichu", ["Thunderbolt", "Thunder Wave", "Submission", "Surf"]]
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
enemypartyhealth = ["Raichu", 230]
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
enemypartyspeed = ["Raichu", 205]
userpartyaccuracy = [inputteam[0], 1, inputteam[2], 1, inputteam[4], 1, inputteam[6], 1, inputteam[8], 1, inputteam[10], 1]
enemypartyaccuracy = ["Raichu", 1]
firstpokemon = inputteam[0]
global currentpokemon
currentpokemon = firstpokemon
global currentspeed
global currenthealth
for i in range(len(data)):
    if currentpokemon == data[i]["Name"]:
        currentspeed = data[i]["Speed Stat"]
        currenthealth = data[i]["Health Stat"]
global enemyasleep
global youasleep
enemyasleep = "no" 
youasleep = "no"
Mikesdeadguys = []




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

    def dead(dead, oppositehealth, oppositepokemon):
        if going == "You":
            Mikesdeadguys.append(oppositepokemon)
    
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
    def specialeffect(specialeffect, move, damage, enemyspeed, enemypk, userpk, enemypartystatus, enemymove, enemydamage, movego, userpartyhealth, enemypartyaccuracy, userpartyspeed):
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
                twostag = enemyspeed / 100
                twostage = twostag * 20
                enemyspeed += twostage
                espeed = enemyspeed
                speedeffect = True
                print(enemypk, "had its speed sharply raised!")
        if "AttackSharpUp" in moves[movenumber]["effect"]:
            global enemyattack
            for i in range(pokemonlist):
                if data[i]["Name"] == enemypokemon:
                    enemyattack = data[i]["Attack Stat"]
            twostag = enemyattack / 100
            twostage = twostag * 20
            enemyattack += twostage
            print(enemypk, "had its attack sharply raised!")

        if "Sleep" in moves[movenumber]["effect"]:
            for i in range(len(enemypartystatus)):
                if enemypk == enemypartystatus[i - 1]:
                    enemypartystatus[i] = "Sleep"
                    print(enemypk, "fell asleep!")
                    if enemypk == enemypokemon:
                        enemyasleep = "yes"
                    if enemypk == currentpokemon:
                        youasleep = "yes" 
        if "DreamEatEffect" in moves[movenumber]["effect"]:  
            global damage
            if going == "Enemy":
                if youasleep == "no":
                    damage = 0
                    print("Nothing Happened")
            if going == "User":
                if enemyasleep == "no"
                damage = 0
                print("Nothing Happened")
 
        if "HitsTwice" in moves[movenumber]["effect"]:
            edamage = damage * 2
            print(userpk, "used", move)
            print(userpk, "did", damage, "damage")
            print("It hit again!")
            damageeffect = True
        if "Poison" in moves[movenumber]["effect"] or " Poison" in moves[movenumber]["effect"]:
            if moves[movenumber]["name"] == "Twineedle":
                poisonchance = random.randint(0, 100)
                twineedleprob = 20
                if poisonchance < twineedleprob or poisonchance == twineedleprob:
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
            print(edamage)
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
    def accuracycheck(accuracycheck, move, accuracy, userpk, userpartyaccuracy):
        for i in range(movelist):
            if move == moves[i]["name"]:
                anumber = moves[i]["accuracy"]
                accnumber = anumber * accuracy
                print(accuracy, "accuracy")
                print(accnumber, "accnumber")
        randnumb = random.randint(0,100)
        print(randnumb)
        if randnumb < accnumber:
            movego = True
        if randnumb == accnumber:
            movego = True
        if randnumb > accnumber:
            movego = False
        return(movego)

 

        

    
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
def checks(enemypokemo, oppositepokemon):
    global enemypokemon
    global enemyspeed
    global enemyhealth
    enemypokemon = enemypokemo
    global shouldiswitch
    shouldiswitch = "no"
    for i in range(pokemonlist):
        if data[i]["Name"] == enemypokemon:
            Types = data[i]["Types"]
    functionality.typechart(enemypokemon, oppositepokemon)
    print(matchup)

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

    if matchup == "half" or "zero" or matchup1 == "half" or "zero":
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
        if R != "half" and R != "zero" and R != "normal" and R1 != "normal" and R1 != "half" and R1 != "zero" and "Raichu" not in Mikesdeadguys:

            enemypokemon = "Raichu"
            for i in range(len(data)):
                if enemypokemon == data[i]["Name"]:
                    enemyspeed = data[i]["Speed Stat"]
                    enemyhealth = data[i]["Health Stat"]
            print("Mike M switched into", enemypokemon)
            shouldiswitch = "yes"

        elif D != "half" and D != "zero" and D != "normal" and D1 != "normal" and D1 != "half" and D1 != "zero" and "Dragonite" not in Mikesdeadguys:
            enemypokemon = "Dragonite"
            if enemypokemon == data[i]["Name"]:
                    enemyspeed = data[i]["Speed Stat"]
                    enemyhealth = data[i]["Health Stat"]
            print("Mike M switched into Dragonite")
            shouldiswitch = "yes"

        elif C != "half" and C != "zero" and C != "normal" and C1 != "normal" and C1 != "half" and C1 != "zero" and "Charizard" not in Mikesdeadguys:
            enemypokemon = "Charizard"
            if enemypokemon == data[i]["Name"]:
                    enemyspeed = data[i]["Speed Stat"]
                    enemyhealth = data[i]["Health Stat"]
            print("Mike M switched into Charizard")
            shouldiswitch = "yes"

        elif G != "half" and G != "zero" and G != "normal" and G1 != "normal" and G1 != "half" and G1 != "zero" and "Gengar" not in Mikesdeadguys:
            enemypokemon = "Gengar"
            if enemypokemon == data[i]["Name"]:
                    enemyspeed = data[i]["Speed Stat"]
                    enemyhealth = data[i]["Health Stat"]
            print("Mike M switched into Gengar")
            shouldiswitch = "yes"

        elif B != "half" and B != "zero" and B != "normal" and B1 != "normal" and B1 != "half" and B1 != "zero" and "Blastoise" not in Mikesdeadguys:
            enemypokemon = "Blastoise"
            if enemypokemon == data[i]["Name"]:
                    enemyspeed = data[i]["Speed Stat"]
                    enemyhealth = data[i]["Health Stat"]
            print("Mike M switched into Blastoise")
            shouldiswitch = "yes"

        elif M != "half" and M != "zero" and M != "normal" and M1 != "normal" and M1 != "half" and M1 != "zero"and "Machamp" not in Mikesdeadguys:
            enemypokemon = "Machamp"
            if enemypokemon == data[i]["Name"]:
                    enemyspeed = data[i]["Speed Stat"]
                    enemyhealth = data[i]["Health Stat"]
            print("Mike M switched into Machamp")
            shouldiswitch = "yes"
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
            if R != "half" or "none" and "Raichu" not in Mikesdeadguys:

                enemypokemon = "Raichu"
                for i in range(len(data)):
                    if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into", enemypokemon)
                shouldiswitch = "yes"

            elif D != "half" or "none" and "Dragonite" not in Mikesdeadguys:
                enemypokemon = "Dragonite"
                if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Dragonite")
                shouldiswitch = "yes"

            elif C != "half" or "none" and "Charizard" not in Mikesdeadguys:
                enemypokemon = "Charizard"
                if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Charizard")
                shouldiswitch = "yes"

            elif G != "half" or "none" and "Gengar" not in Mikesdeadguys:
                enemypokemon = "Gengar"
                if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Gengar")
                shouldiswitch = "yes"

            elif B != "half" or "none" and "Blastoise" not in Mikesdeadguys:
                enemypokemon = "Blastoise"
                if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Blastoise")
                shouldiswitch = "yes"

            elif M != "half" or "none" and "Machamp" not in Mikesdeadguys:
                enemypokemon = "Machamp"
                if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Machamp")
                shouldiswitch = "yes"
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










    def Raichudoing(raichudoing, turn):
        global enemymove
        global enemypokemon
        Rmoves = ["Double Team", "Toxic", "Thunderbolt", "Surf"]
        if turn == 0:
            enemypokemon = "Raichu"
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
            functionality.checks(enemypokemon, currentpokemon)
            if shouldiswitch != "yes":
                functionality.supereffective("Thunderbolt", currentpokemon)
                if effective == "super":
                    enemymove = "Thunderbolt"
                    #print("Raichu used Thunderbolt")

                if effective != "super":
                    functionality.supereffective("Surf", currentpokemon)
                    if effective == "super":
                        enemymove = "Surf"
                        #print("Raichu used Surf")

                    if effective != "super":
                        for i in range(userpartystatus):
                            if currentpokemon == userpartystatus[i - 1]:
                                x = userpartystatus[i]
                                if x != "Poisoned":
                                    enemymove = "Toxic"
                                if x == "Poisoned":
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



    def DragoniteDoing(turn):
        global enemymove
        global enemypokemon
        Dmoves = ["Agility", "Slam", "Fire Blast", "Blizzard"]

        functionality.checks(enemypokemon, currentpokemon)
        if shouldiswitch != "yes":
            functionality.supereffective("Fire Blast", currentpokemon)
            if effective == "super":
                enemymove = "Fire Blast"
                #print("Raichu used Fire Blast")

            if effective != "super":
                functionality.supereffective("Blizzard", currentpokemon)
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
        y = turn
        Joel = turn - y
        if Joel < 2:
            enemymove = "Swords Dance"
        if Joel == 2 or Joel > 2:
            functionality.checks(enemypokemon, currentpokemon)
            if shouldiswitch != "yes":
                functionality.supereffective("Mega Punch", currentpokemon)
                if effective == "super":
                    enemymove = "Mega Punch"
                    #print("Raichu used Fire Blast")

                if effective != "super":
                    functionality.supereffective("Earthquake", currentpokemon)
                    if effective == "super":
                        enemymove = "Earthquake"
                        #print("Raichu used Surf")

                    if effective != "super":
                        functionality.supereffective("Fly", currentpokemon)
                        if effective == "super":
                                enemymove = "Fly"

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

        functionality.checks(enemypokemon, currentpokemon)
        if shouldiswitch != "yes":
            functionality.supereffective("Psychic", currentpokemon)
            if effective == "super":
                enemymove = "Psychic"
                #print("Raichu used Fire Blast")

            if effective != "super":
                functionality.supereffective("Mega Drain", currentpokemon)
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
        functionality.checks(enemypokemon, currentpokemon)
        if shouldiswitch != "yes":
                functionality.supereffective("Hydro Pump", currentpokemon)
                if effective == "super":
                    enemymove = "Hydro Pump"
                    #print("Raichu used Fire Blast")

                if effective != "super":
                    functionality.supereffective("Bite", currentpokemon)
                    if effective == "super":
                        enemymove = "Bite"
                        #print("Raichu used Surf")

                    if effective != "super":
                        functionality.supereffective("Ice Beam", currentpokemon)
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
        functionality.checks(enemypokemon, currentpokemon)
        if shouldiswitch != "yes":
                functionality.supereffective("Body Slam", currentpokemon)
                if effective == "super":
                    enemymove = "Body Slam"
                    #print("Raichu used Fire Blast")

                if effective != "super":
                    functionality.supereffective("Earthquake", currentpokemon)
                    if effective == "super":
                        enemymove = "Earthquake"
                        #print("Raichu used Surf")

                    if effective != "super":
                        functionality.supereffective("Rock Slide", currentpokemon)
                        if effective == "super":
                                enemymove = "Rock Slide"

                        if effective != "super":
                            functionality.supereffective("Submission", currentpokemon)
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
            Mike.Raichudoing(turn)
        if enemypokemon == "Dragonite":
            Mike.DragoniteDoing(turn)
        if enemypokemon == "Charizard":
            Mike.Charizarddoing(turn)
        if enemypokemon == "Gengar":
            Mike.Gengardoing()
        if enemypokemon == "Blastoise":
            Mike.Blastoisedoing()
        if enemypokemon == "Machamp":
            Mike.Machampdoing()
class Ai():
    def supereffectivecheck(usermovetype):
        print("placeholder")







goingfirst = ["pluh"]
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
        global enemyasleep
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
                Mike.Raichudoing(turn)
                for i in range(len(enemypartyaccuracy)):
                    if enemypokemon == enemypartyaccuracy[i - 1]:
                        accuracy = enemypartyaccuracy[i]
                gomove = f.accuracycheck(enemymove, accuracy, enemypokemon, enemypartyaccuracy)
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
                        f.damagecalc(enemymove, enemypokemon, currentpokemon)
                        enemydamage = movedamage
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
                        print("Raichu used", enemymove)
                        print("Raichu did", enemydamage, "damage")
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
                            print("Raichu used", enemymove, )
                            print("Raichu did", enemydamage, "damage")
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
                    if youasleep == "yes":
                        snore = random.randrange(4)
                        if snore == 1:
                            for i in range(len(userpartystatus)):
                                if userpartystatus[i - 1] == currentpokemon:
                                    userpartystatus[i] == "none"
                            print(currentpokemon, "woke up!")
                            youasleep == "no"
                        else:
                            print(currentpokemon, "is fast asleep")
                    if youasleep != "yes":
                        f = functionality()
                        time.sleep(times)
                        going = "You"
                        print("You used", use)
                        for i in range(len(userpartyaccuracy)):
                            if currentpokemon == userpartyaccuracy[i - 1]:
                                accuracy = userpartyaccuracy[i]
                        Weezer = f.accuracycheck(use, accuracy, currentpokemon, userpartyaccuracy)
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
                                        f.damagecalc(use, currentpokemon, enemypokemon1)
                                        damage = movedamage
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
                            print(enemypokemon, "fainted")
                            fullwipe = True
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
                    if enemyasleep == "yes":
                        snore = random.randrange(4)
                        if snore == 1:
                            for i in range(len(eliteteamstatus)):
                                if eliteteamstatus[i - 1] == enemypokemon:
                                    eliteteamstatus[i] == "none"
                            print(enemypokemon, "woke up!")
                            enemyasleep == "no"
                        else:
                            print(enemypokemon, "is fast asleep")
                    if enemyasleep != "yes":
                        Mike.Raichudoing(turn)
                        for i in range(len(enemypartyaccuracy)):
                            if enemypokemon == enemypartyaccuracy[i - 1]:
                                accuracy = enemypartyaccuracy[i]
                        gomove = f.accuracycheck(enemymove, accuracy, enemypokemon, enemypartyaccuracy)
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
                                f.damagecalc(enemymove, enemypokemon, currentpokemon)
                                enemydamage = movedamage
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
                                print("Raichu used", enemymove, )
                                print("Raichu did", enemydamage, "damage")
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
                    if enemyasleep == "yes":
                        snore = random.randrange(4)
                        if snore == 1:
                            for i in range(len(eliteteamstatus)):
                                if eliteteamstatus[i - 1] == enemypokemon:
                                    eliteteamstatus[i] == "none"
                            print(enemypokemon, "woke up!")
                            enemyasleep == "no"
                        else:
                            print(enemypokemon, "is fast asleep")
                    if enemyasleep != "yes":
                        f = functionality()
                        going = "Enemy"
                        Mike.Raichudoing(turn)
                        for i in range(len(enemypartyaccuracy)):
                            if enemypokemon == enemypartyaccuracy[i - 1]:
                                accuracy = enemypartyaccuracy[i]
                        gomove = f.accuracycheck(enemymove, accuracy, enemypokemon, enemypartyaccuracy)
                        print(eliteteamstatus)
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
                                f.damagecalc(enemymove, enemypokemon, currentpokemon)
                                enemydamage = movedamage
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
                                print("Raichu used", enemymove, )
                                print("Raichu did", enemydamage, "damage")
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
                        if youasleep == "yes":
                            snore = random.randrange(4)
                        if snore == 1:
                            for i in range(len(userpartystatus)):
                                if userpartystatus[i - 1] == currentpokemon:
                                    userpartystatus[i] == "none"
                            print(currentpokemon, "woke up!")
                            youasleep == "no"
                        else:
                            print(currentpokemon, "is fast asleep")
                        if youasleep != "yes":
                            print("You used", use)
                            time.sleep(times)
                            f = functionality()
                            for i in range(len(currentmoves)):
                                if currentmoves[i] == use:
                                    for i in range(len(userpartyaccuracy)):
                                        if currentpokemon == userpartyaccuracy[i - 1]:
                                            accuracy = userpartyaccuracy[i]
                                    Weezer = f.accuracycheck(use, accuracy, currentpokemon, userpartyaccuracy)
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
                                            f.damagecalc(use, currentpokemon, enemypokemon1)
                                            damage = movedamage
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
                                            print(enemypokemon, "fainted")
                                            fullwipe = True
                                    enemypartyhealth[1] = enemyhealth
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

    


                




        
      

Turns.preturn(firstpokemon, enemypokemon1, "Elite Four Member Mike")
Turns.turn(firstpokemon, enemypokemon1)

        

