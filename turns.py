import json
from effects import effect
from effects import Using
import time

times = 1.5

turn = 0
#going = "You"

test = open("move.json", encoding="utf8")
moves = json.load(test)
movelist = len(moves)

quiz = open("pokemon.json", encoding="utf8")
data = json.load(quiz)
pokemonlist = len(data)

firstpokemon = "Bulbasaur"
secondpokemon = "Weedle"
thirdpokemon = "Beedrill"
fourthpokemon = "Poliwrath"
fifthpokemon = "Arbok"
sixthpokemon = "Fearow"
userparty =[firstpokemon, secondpokemon, thirdpokemon, fourthpokemon, fifthpokemon, sixthpokemon]


move1 = "Cut"
move2 = "Razor Leaf"
move3 = "Tackle"
move4 = "Vine Whip"
firstpokemonmoves = [move1, move2, move3, move4]

enemyhealth = 200
currenthealth = 100
enemyspeed = 100
currentspeed = 50

global stab
stab = True
global meffective1
meffective1 = normal
global meffective2
meffective2 = normal
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



currentpokemon = firstpokemon




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
    def damagecalc(move, attackingpk, enemypk):
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
        if moves[move]["category"] == "Physical":
            attackingpower = userattack
            defendingpower = enemydefense
        if moves[move]["category"] == "Special":
            attackingpower = userspecial
            defendingpower = enemyspecial
        math1 = 40 * movepower
        math2 = attackingpower // defendingpower
        math3 = math2 * math1
        math4 = math3 // 50
        math5 = math4 + 2
        if moves[movenumber]["type"] in data[attacknumber]["Types"]:
            stab = True
        f = functionality()
        if len(data[enemynumber]["Types"]) > 1:
            enemytype1 = (data[enemynumber]["Types"])[0]
            enemytype2 = (data[enemynumber]["Types"])[1]
            f.supereffective(move, enemytype1)
            if effective == "super":
                meffective1 = True
            f.supereffective(move, enemytype2)
            if effective == 



        if len(data[enemynumber]["Types"]) < 1:
            enemytype
        f.supereffective(move, enemytype1)
        if 
        
        



        

        
 

        

    


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
                functionality.oppositehealththing(going, enemyhealth, currenthealth)
            
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
    




    def turnone(playerpokemon1, enemypokemon1, enemy):
   

        #endorturn = "no"
        #pokemonin = "same"

        

        print("You are challenged by", enemy)
        time.sleep(times)
        print("You threw out", playerpokemon1)
        time.sleep(0.5)
        print(enemy, "threw out", enemypokemon1)
        time.sleep(times)
        global going
    

        print("Switch Out Or Attack")
        userdo = input("What would you like to do: ")
        if userdo == "Switch" or userdo == "switch" or userdo == "Switch Out" or userdo == "switch out" or userdo == "Switch out":
            global currentpokemon
            print(userparty)
            switchin = input("Pick a Pokemon to Switch into: ")
            print("You switched into", switchin)
            currentpokemon = switchin
            
            going = "Enemy"
            time.sleep(times)
            Mike.Raichudoing()
           


            

        if userdo == "Attack" or userdo == "attack":
            print(firstpokemonmoves)
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
            




        
      


#Turns.turnone(firstpokemon, enemypokemon1, "Elite Four Member Mike M.")

        





#Tims team
#Pikachu - Toxic, Thunderbolt, Double Team, Surf
#Gyarados - 
#Moltres
#Articuno
#Venusaur
#Mewtwo