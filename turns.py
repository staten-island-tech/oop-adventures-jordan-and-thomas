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
    
    def supereffective():
        for i in range(pokemonlist):
            if (data[i]["Name"]) == oppositepokemon:
                ptype = (data[i]["Types"])
            




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
            




        
      


Turns.turnone(firstpokemon, enemypokemon1, "Elite Four Member Mike M.")

        

#Turns.turnone(playerpokemon1, "Charizard","Adam")



#Tims team
#Pikachu - Toxic, Thunderbolt, Double Team, Surf
#Gyarados - 
#Moltres
#Articuno
#Venusaur
#Mewtwo