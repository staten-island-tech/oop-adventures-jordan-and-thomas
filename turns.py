import json
from effects import effect
from effects import Using
import time
from tryingtofix import Teambuilder
from tryingtofix import *
times = 1.5

turn = 0
#going = "You"

test = open("move.json", encoding="utf8")
moves = json.load(test)
movelist = len(moves)

quiz = open("data.json", encoding="utf8")
data = json.load(quiz)
pokemonlist = len(data)


pknumber = [1]
playerteam = []
pokemonmoves = []
allpokemon = []
for i in range(len(data)):
            allpokemon.append(data[i]["Name"])





currentpokemon = teaminfo[0]    


endofturn = "no"
global pokemonin
pokemonin = "same"
global enemyin
enemyin = "same"


#enemyhealth = 200
#Pokemon.teambuilder()

global enemypokemon
enemypokemon1 = "Raichu"
enemypokemon = enemypokemon1






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
    
    def dead(oppositehealth):
        if oppositehealth == 0:
            global currentpokemon
            print(oppositepokemon, "has fainted")
            dead = oppositepokemon
            print(teaminfo)
            switchin = input("Pick a Pokemon to switch in: ")
            if switchin == dead:
                print(switchin, "has already fainted")
                switchin = input("Pick a Pokemon to switch in to:")
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
        print(effective)

    def pokemoninmoves(currentpokemon):
        global currentmoves

        if currentpokemon == teaminfo[0]:
            currentmoves = teaminfo[1]
        if currentpokemon == teaminfo[2]:
            currentmoves = teaminfo[3]
        if currentpokemon == teaminfo[4]:
            currentmoves = teaminfo[5]
        if currentpokemon == teaminfo[6]:
            currentmoves = teaminfo[7]
        if currentpokemon == teaminfo[8]:
            currentmoves = teaminfo[9]
        if currentpokemon == teaminfo[10]:
            currentmoves = teaminfo[11]
 

        

    


class Ai():
    def supereffectivecheck(usermovetype):
        print("placeholder")


class Mike(functionality):
    def Raichudoing():
        global enemypokemon

        if turn == 0:
            enemypokemon = "Raichu"
            for i in range(pokemonlist):
                if (data[i]["Name"]) == currentpokemon:
                    ptype = (data[i]["Types"])
            if "Poison" not in ptype:
                print("Raichu used Toxic")
                time.sleep(times)
                enemyuse = "Toxic"
                functionality.oppositehealththing(going, enemyhealth, "currenthealth")
            
                functionality.oppositepokemon(going, currentpokemon, enemypokemon)
            
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



    def turnone(playerpokemon1, enemypokemon1, enemy):
   

        #endorturn = "no"
        #pokemonin = "same"

        currentpokemon = teaminfo[0]    

        print("You are challenged by", enemy)
        time.sleep(times)
        print("You threw out", playerpokemon1)
        time.sleep(0.5)
        print(enemy, "threw out", enemypokemon1)
        time.sleep(times)
        global going
        Turns.enemyspeed(enemypokemon)
        Turns.speedstat(currentpokemon)
    

        print("Switch Out Or Attack")
        userdo = input("What would you like to do: ")
        if userdo == "Switch" or userdo == "switch" or userdo == "Switch Out" or userdo == "switch out" or userdo == "Switch out":
            
            print("userparty")
            switchin = input("Pick a Pokemon to Switch into: ")
            print("You switched into", switchin)
            currentpokemon = switchin
            
            going = "Enemy"
            time.sleep(times)
            Mike.Raichudoing()
           


            

        if userdo == "Attack" or userdo == "attack":
            functionality.pokemoninmoves(currentpokemon)
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
                #Do effect
                for i in range(movelist):
                    if moves[i]["name"] == use:
                        damage = moves[i]["power"]
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
                for i in range(movelist):
                    if moves[i]["name"] == use:
                        damage = moves[i]["power"]
                        print("It did", damage, "damage")
                        enemyhealth = enemyhealth - damage
                        time.sleep(times)
                        print(enemypokemon1, "has", enemyhealth, "health left")
            




          
time.sleep(2)

Turns.turnone(currentpokemon, enemypokemon, "Elite Four Member Mike M.")

        





#Tims team
#Pikachu - Toxic, Thunderbolt, Double Team, Surf
#Gyarados - 
#Moltres
#Articuno
#Venusaur
#Mewtwo