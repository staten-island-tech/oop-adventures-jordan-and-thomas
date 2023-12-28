import json
from effects import effect
from effects import Using
import time
import decimal
from decimal import Decimal
from random import sample

from tryingtofix import Teambuilder

times = 1.5

turn = 0
#going = "You"
multiplehits = [2, 3, 4, 5]
test = open("move.json", encoding="utf8")
moves = json.load(test)
movelist = len(moves)

quiz = open("pokemon.json", encoding="utf8")
data = json.load(quiz)
pokemonlist = len(data)

pluh = open("playerteaminfo.json", encoding="utf8")
inputteam = json.load(pluh)
inputteamlist = len(inputteam)



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
userparty = [inputteam[0], inputteam[2], inputteam[4], inputteam[6], inputteam[8], inputteam[10]]
userpartystatus = [inputteam[0], "none", inputteam[2], "none", inputteam[4], "none", inputteam[6], "none", inputteam[8], "none", inputteam[10], "none"]
eliteteamstatus = [data[25]["Name"], "none"]
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
    
    def supereffective(use, oppositepokemon):
        global effective
        effective = "normal"
        for i in range(pokemonlist):
            if (data[i]["Name"]) == oppositepokemon:
                ptype = (data[i]["Types"])
        for i in range(movelist):
            if (moves[i]["name"]) == use:
                usetype = (moves[i]["type"])

        if usetype == "Normal" and "Rock" in ptype:
            effective = "half"
        if usetype == "Normal" and "Ghost" in ptype:
            effective = "zero"

        if usetype == "Fire" and "Fire" in ptype:
            effective = "half"
        if usetype == "Fire" and "Water" in ptype:
            effective = "half"
        if usetype == "Fire" and "Grass" in ptype:
            effective = "super"
        if usetype == "Fire" and "Ice" in ptype:
            effective = "super"
        if usetype == "Fire" and "Bug" in ptype:
            effective = "super"
        if usetype == "Fire" and "Rock" in ptype:
            effective = "half"
        if usetype == "Fire" and "Dragon" in ptype:
            effective = "half"
        
        if usetype == "Water" and "Fire" in ptype:
            effective = "super"
        if usetype == "Water" and "Water" in ptype:
            effective = "half"
        if usetype == "Water" and "Grass" in ptype:
            effective = "half"
        if usetype == "Water" and "Ground" in ptype:
            effective = "super"
        if usetype == "Water" and "Rock" in ptype:
            effective = "super"
        if usetype == "Water" and "Dragon" in ptype:
            effective = "half"
        
        if usetype == "Electric" and "Water" in ptype:
            effective = "super"
        if usetype == "Electic" and "Electirc" in ptype:
            effective = "half"
        if usetype == "Electric" and "Grass" in ptype:
            effective = "half"
        if usetype == "Electric" and "Ground" in ptype:
            effective = "zero"
        if usetype == "Electric" and "Flying" in ptype:
            effective = "super"
        if usetype == "Electric" and "Dragon" in ptype:
            effective = "half"

        if usetype == "Grass" and "Fire" in ptype:
            effective = "half"
        if usetype == "Grass" and "Water" in ptype:
            effective = "super"
        if usetype == "Grass" and "Grass" in ptype:
            effective = "half"
        if usetype == "Grass" and "Poison" in ptype:
            effective = "half"
        if usetype == "Grass" and "Ground" in ptype:
            effective = "super"
        if usetype == "Grass" and "Flying" in ptype:
            effective = "half"
        if usetype == "Grass" and "Bug" in ptype:
            effective = "half"
        if usetype == "Grass" and "Rock" in ptype:
            effective = "super"
        if usetype == "Grass" and "Dragon" in ptype:
            effective = "half"
        
        if usetype == "Ice" and "Fire" in ptype:
            effective = "half"
        if usetype == "Ice" and "Water" in ptype:
            effective = "half"
        if usetype == "Ice" and "Grass" in ptype:
            effective = "super"
        if usetype == "Ice" and "Ice" in ptype:
            effective = "half"
        if usetype == "Ice" and "Ground" in ptype:
            effective = "super"
        if usetype == "Ice" and "Flying" in ptype:
            effective = "super"
        if usetype == "Ice" and "Dragon" in ptype:
            effective = "super"
        
        if usetype == "Fighting" and "Normal" in ptype:
            effective = "super"
        if usetype == "Fighting" and "Ice" in ptype:
            effective = "super"
        if usetype == "Fighting" and "Poison" in ptype:
            effective = "half"
        if usetype == "Fighting" and "Flying" in ptype:
            effective = "half"
        if usetype == "Fighting" and "Psychic" in ptype:
            effective = "half"
        if usetype == "Fighting" and "Bug" in ptype:
            effective = "half"
        if usetype == "Fighting" and "Rock" in ptype:
            effective = "super"
        if usetype == "Fighting" and "Ghost" in ptype:
            effective = "zero"
        
        if usetype == "Poison" and "Grass" in ptype:
            effective = "super"
        if usetype == "Poison" and "Poison" in ptype:
            effective = "half"
        if usetype == "Poison" and "Ground" in ptype:
            effective = "half"
        if usetype == "Poison" and "Rock" in ptype:
            effective = "half"
        if usetype == "Poison" and "Ghost" in ptype:
            effective = "half"

        if usetype == "Ground" and "Fire" in ptype:
            effective = "super"
        if usetype == "Ground" and "Electric" in ptype:
            effective = "super"
        if usetype == "Ground" and "Grass" in ptype:
            effective = "half"
        if usetype == "Ground" and "Poison" in ptype:
            effective == "super"
        if usetype == "Ground" and "Flying" in ptype:
            effective == "zero"
        if usetype == "Ground" and "Bug" in ptype:
            effective == "half"
        if usetype == "Ground" and "Rock" in ptype:
            effective = "super"

        if usetype == "Flying" and "Electric" in ptype:
            effective = "half"
        if usetype == "Flying" and "Grass" in ptype:
            effective = "super"
        if usetype == "Flying" and "Fighting" in ptype:
            effective = "super"
        if usetype == "Flying" and "Bug" in ptype:
            effective = "Bug"
        if usetype == "Flying" and "Rock" in ptype:
            effective = "half"
        
        if usetype == "Psychic" and "Fighting" in ptype:
            effective = "super"
        if usetype == "Psychic" and "Poison" in ptype:
            effective = "super"
        if usetype == "Psychic" and "Psychic" in ptype:
            effective = "half"
        
        if usetype == "Bug" and "Fire" in ptype:
            effective = "half"
        if usetype == "Bug" and "Grass" in ptype:
            effective = "super"
        if usetype == "Bug" and "Fighting" in ptype:
            effective = "half"
        if usetype == "Bug" and "Poison" in ptype:
            effective = "half"
        if usetype == "Bug" and "Flying" in ptype:
            effective = "half"
        if usetype == "Bug" and "Psychic" in ptype:
            effective = "super"
        if usetype == "Bug" and "Ghost" in ptype:
            effective = "half"

        if usetype == "Rock" and "Fire" in ptype:
            effective = "super"
        if usetype == "Rock" and "Ice" in ptype:
            effective = "super"
        if usetype == "Rock" and "Fighting" in ptype:
            effective = "half"
        if usetype == "Rock" and "Ground" in ptype:
            effective = "half"
        if usetype == "Rock" and "Flying" in ptype:
            effective = "super"
        if usetype == "Rock" and "Bug" in ptype:
            effective = "super"
        
        if usetype == "Ghost" and "Normal" in ptype:
            effective = "zero"
        if usetype == "Ghost" and "Psychic" in ptype:
            effective = "super"
        if usetype == "Ghost" and "Ghost" in ptype:
            effective = "super"
        
        if usetype == "Dragon" and "Dragon" in ptype:
            effective = "super"
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
            global nodamage
            nodamage = True
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
        f = functionality()
        if len(data[enemynumber]["Types"]) > 1:
            enemytype1 = (data[enemynumber]["Types"])[0]
            enemytype2 = (data[enemynumber]["Types"])[1]
            f.supereffective(move, enemytype1)
            if effective == "super":
                meffective1 = 2
            if effective == "half":
                meffective1 = 0.5
            if effective == "zero":
                meffective1 = 0
            f.supereffective(move, enemytype2)
            if effective == "super":
                meffective2 = 2
            if effective == "half":
                meffective2 = 0.5
            if effective == "zero":
                meffective2 = 0
            global twotype
            twotype = True
        if len(data[enemynumber]["Types"]) < 1:
            enemytype = (data[enemynumber]["Types"])[0]
            f.supereffective(move, enemytype)
            if effective == "super":
                meffective = 2
            if effective == "half":
                meffective = 0.5
            if effective == "zero":
                meffective = 0
            global onetype
            onetype = True
        if stab == True:
            math5 *=  decimal.Decimal(1.5)
        if onetype == True:
            math5 *= decimal.Decimal(meffective)
        if twotype == True:
            meffective = decimal.Decimal(meffective1) * decimal.Decimal(meffective2)
            math5 *= decimal.Decimal(meffective)
        global movedamage
        movedamage = round(math5)
        if nodamage == True:
            movedamage = 0
    def specialeffect(specialeffect, move, damage, enemyspeed, enemypk):
        for i in range(movelist):
            if move == moves[i]["name"]:
                movenumber = i
        for i in range(pokemonlist):
            if enemypk == data[i]["Name"]:
                enemynumber = i
        if "HealHalfD" in moves[movenumber]["effect"]:
            global heal
            global healamount
            heal == True
            healamount = damage / 2
        if "Hits2To5" in moves[movenumber]["effect"]:
            hitamount = sample(multiplehits, 1)[0]
            global again
            global moveagain
            again = True
            moveagain = hitamount - 1
        if "SpeedDown" in moves[movenumber]["effect"]:
            onestage = decimal.Decimal(2) / decimal.Decimal(3)
            enemyspeed *= onestage 
        if "HitsTwice" in moves[movenumber]["effect"]:
            again = True
            moveagain = 1
        if "Poison" in moves[movenumber]["effect"]:
            if not "Poison" in data[enemynumber]["Types"]:
                enemypk = "afflicted"




        






            
        
        



        

        
 

        

    


class Ai():
    def supereffectivecheck(usermovetype):
        print("placeholder")


class Mike(functionality):
    def Raichudoing():


        if turn == 0:
            for i in range(pokemonlist):
                if (data[i]["Name"]) == currentpokemon:
                    ptype = (data[i]["Types"])
            if "Poison" not in ptype:
                print("Raichu used Toxic")
                time.sleep(times)
                enemyuse = "Toxic"
                #functionality.oppositehealththing(going, enemyhealth, currenthealth)
            
                #functionality.oppositepokemon(going, currentpokemon, enemypokemon)
            
                Using.usemove("placeholder", enemyuse, oppositepokemon, oppositehealth, pokemonin, endofturn, turn)
            else:
                print("Raichu used Double Team")





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
    def turn(playerpokemon1, enemypokemon1):
   

        #endorturn = "no"
        #pokemonin = "same"

        


    

        print("Switch Out Or Attack")
        userdo = input("What would you like to do: ")
        if userdo == "Switch" or userdo == "switch" or userdo == "Switch Out" or userdo == "switch out" or userdo == "Switch out":
            global currentpokemon
            currentpokemon = playerpokemon1
            print(userparty)
            switchin = input("Pick a Pokemon to Switch into: ")
            print("You switched into", switchin)
            currentpokemon = switchin
            
            going = "Enemy"
            time.sleep(times)
            Mike.Raichudoing()
           


            

        if userdo == "Attack" or userdo == "attack":
            print(inputteam[1])
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
                for i in range(len(inputteam[1])):
                    if inputteam[1][i]== use:
                        f.damagecalc(use, currentpokemon, enemypokemon1)
                        damage = movedamage
                        print("It did", damage, "damage")
                        enemyhealth = enemyhealth - damage
                        time.sleep(times)
                        print(enemypokemon1, "has", enemyhealth, "health left")
                going = "Enemy"
                time.sleep(times)
                Mike.Raichudoing()
                
               

            if "Enemy" in goingfirst:
                going = "Enemy"
                Mike.Raichudoing()
                time.sleep(times)
                going = "You"
                print("You used", use)
                time.sleep(times)
                # if move effect != None
                #Do effect
                f = functionality()
                for i in range(len(inputteam[1])):
                    if inputteam[1][i] == use:
                        f.damagecalc(use, currentpokemon, enemypokemon1)
                        damage = movedamage
                        print("It did", damage, "damage")
                        enemyhealth = enemyhealth - damage
                        time.sleep(times)
                        print(enemypokemon1, "has", enemyhealth, "health left")
            




        
      

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
