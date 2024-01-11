import json
import time
import decimal
from decimal import Decimal
from random import sample
import random 

from tryingtofix import Teambuilder

times = 1.5

turn = 0
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



#enemyhealth = 200
#Pokemon.teambuilder()

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
firstpokemon = inputteam[0]
global currentpokemon
currentpokemon = firstpokemon
global currentspeed
global currenthealth
for i in range(len(data)):
    if currentpokemon == data[i]["Name"]:
        currentspeed = data[i]["Speed Stat"]
        currenthealth = data[i]["Health Stat"]




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
            hitamount = sample(multiplehits, 1)[0]
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
    def accuracycheck(accuracycheck, move):
        for i in range(movelist):
            if move == moves[i]["name"]:
                accnumber = moves[i]["accuracy"]
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
    def Raichudoing():
        global enemymove
        enemymove = "Thunderbolt"
        return(enemymove)





goingfirst = []
class Turns(Mike):
    def speedcheck(enemyspeed, currentspeed):
        if enemyspeed > currentspeed:
            goingfirst.append("Enemy")
        if currentspeed > enemyspeed:
            goingfirst.append("User")
        if enemyspeed == currentspeed:
            goingfirst.append("Enemy")
    



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
        while fullwipe == False:
            f = functionality()
            print("Switch Out Or Attack")
            userdo = input("What would you like to do: ")
            if userdo == "Switch" or userdo == "switch" or userdo == "Switch Out" or userdo == "switch out" or userdo == "Switch out":
                for i in range(len(userpartyhealth)):
                    if currentpokemon == userpartyhealth[i - 1]:
                        currenthealth = userpartyhealth[i]
                print(userparty)
                switchin = input("Pick a Pokemon to Switch into: ")
                print("You switched into", switchin)
                currentpokemon = switchin
                for i in range(len(userpartyhealth)):
                    if currentpokemon == userpartyhealth[i - 1]:
                        currenthealth = userpartyhealth[i]
                        x = i
                going = "Enemy"
                time.sleep(times)
                Mike.Raichudoing()
                f.damagecalc(enemymove, enemypokemon1, currentpokemon)
                enemydamage = movedamage
                if enemydamage == currenthealth or enemydamage > currenthealth:
                    enemydamage = currenthealth
                print("Raichu used", enemymove)
                print("Raichu did", enemydamage, "damage")
                currenthealth = currenthealth - enemydamage
                print(currentpokemon, "has", currenthealth, "health left")
                userpartyhealth[x] = currenthealth
                if currenthealth == 0:
                    for i in range(len(userparty)):
                        if currentpokemon == userparty[i]:
                            userparty.remove(i)
                    print(userparty)
                    newpk = input("Who will you switch into? ")
                    for i in range(len(userparty)):
                        if newpk == userparty[i]:
                            currentpokemon = newpk
                    for i in range(len(userpartyhealth)):
                        if currentpokemon == userpartyhealth[i - 1]:
                            currenthealth = userpartyhealth[i]
            if userdo == "Attack" or userdo == "attack":
                for i in range(inputteamlist):
                    if currentpokemon == inputteam[i - 1]:
                        currentmoves = inputteam[i]
                        print(currentmoves)
                use = input("Pick a move to use: ")
                time.sleep(times)
                Turns.speedcheck(enemyspeed, currentspeed)
            
                if "User" in goingfirst:
                    f = functionality()
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
                                Weezer = f.accuracycheck(use)
                                if Weezer == True:
                                    f.damagecalc(use, currentpokemon, enemypokemon1)
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
                                        fullwipe = True
                                enemypartyhealth[1] = enemyhealth
                                if Weezer == False:
                                    print(currentpokemon, "missed their attack!")
                    going = "Enemy"
                    Mike.Raichudoing()
                    gomove = f.accuracycheck(enemymove)
                    if gomove == True:
                        f.damagecalc(enemymove, enemypokemon, currentpokemon)
                        enemydamage = movedamage
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
                        userpartyhealth[x] = currenthealth
                        global death
                        death = False
                        if currenthealth == 0:
                            for i in range(len(userparty)):
                                if currentpokemon == userparty[i]:
                                    userparty.remove(userparty[i])
                                    death = True
                                    break
                            print(userparty)
                            print(len(userparty))
                            if len(userparty) > 0:
                                newpk = input("Who will you switch into? ")
                                for i in range(len(userparty)):
                                    if newpk == userparty[i]:
                                        currentpokemon = newpk
                                for i in range(len(userpartyhealth)):
                                    if currentpokemon == userpartyhealth[i - 1]:
                                        currenthealth = userpartyhealth[i]
                            if len(userparty) == 0:
                                fullwipe = True
                                break
                    if gomove == False:
                        print(enemypokemon, "missed their attack!")
                
               

                if "Enemy" in goingfirst:
                    f = functionality()
                    going = "Enemy"
                    Mike.Raichudoing()
                    gomove = f.accuracycheck(enemymove)
                    if gomove == True:
                        f.damagecalc(enemymove, enemypokemon, currentpokemon)
                        enemydamage = movedamage
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
                        userpartyhealth[x] = currenthealth
                        global death
                        death = False
                        if currenthealth == 0:
                            for i in range(len(userparty)):
                                if currentpokemon == userparty[i]:
                                    userparty.remove(userparty[i])
                                    death = True
                                    break
                            print(userparty)
                            print(len(userparty))
                            if len(userparty) > 0:
                                newpk = input("Who will you switch into? ")
                                for i in range(len(userparty)):
                                    if newpk == userparty[i]:
                                        currentpokemon = newpk
                                for i in range(len(userpartyhealth)):
                                    if currentpokemon == userpartyhealth[i - 1]:
                                        currenthealth = userpartyhealth[i]
                            if len(userparty) == 0:
                                fullwipe = True
                                break
                    if gomove == False:
                        print(enemypokemon, "missed their attack!")
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
                                Weezer = f.accuracycheck(use)
                                if Weezer == True:
                                    f.damagecalc(use, currentpokemon, enemypokemon1)
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
                                        fullwipe = True
                                enemypartyhealth[1] = enemyhealth
                                if Weezer == False:
                                    print(currentpokemon, "missed their attack!")
            




        
      

Turns.preturn(firstpokemon, enemypokemon1, "Elite Four Member Mike")
Turns.turn(firstpokemon, enemypokemon1)

        
#Mike's Team
#Charizard
#Dragonite
#Raichu - Toxic, Thunderbolt, Double Team, Surf
#Gengar
#Blastoise
#Machamp




#Tims team
#Pikachu - Toxic, Thunderbolt, Double Team, Surf
#Gyarados - 
#Moltres
#Articuno
#Venusaur
#Mewtwo
