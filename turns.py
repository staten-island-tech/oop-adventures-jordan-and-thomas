import json
from effects import effect
from effects import Using
import time

times = 1.5

turn = 0
going = "You"

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


move1 = "Leech Seed"
move2 = "Absorb"
move3 = "Growl"
move4 = "Vine Whip"
firstpokemonmoves = [move1, move2, move3, move4]

enemyhealth = 200
currenthealth = 100
enemyspeed = 100
currentspeed = 50


#enemyhealth = 200
#Pokemon.teambuilder()

class functionality():
    def oppositehealththing(going, enemyhealth, currenthealth):
        if going == "You":
            oppositehealth = enemyhealth
        if going == "Enemy":
            oppositehealth = currenthealth

class Ai():
    def supereffectivecheck(usermovetype):
        print("placeholder")


class Mike(functionality):
    def Raichudoing():
        if turn == 0:
            print("Raichu used Toxic")
            enemyuse = "Toxic"
            functionality.oppositehealththing(going, enemyhealth, currenthealth)
            Using.usemove("placeholder", enemyuse, oppositehealth)





goingfirst = [1]
class Turns(Mike):
    def speedcheck(enemyspeed, currentspeed):
        if enemyspeed > currentspeed:
            goingfirst.append("Enemy")
        if currentspeed > enemyspeed:
            goingfirst.append("User")
    




    def turnone(playerpokemon1, enemypokemon1, enemy):
   

        endorturn = "no"
        pokemonin = "same"

        

        print("You are challenged by", enemy)
        time.sleep(times)
        print("You threw out", playerpokemon1)
        time.sleep(0.5)
        print(enemy, "threw out", enemypokemon1)
        time.sleep(times)
     
        print("Switch Out Or Attack")
        userdo = input("What would you like to do: ")
        if userdo == "Switch" or userdo == "switch" or userdo == "Switch Out" or userdo == "switch out" or userdo == "Switch out":
            print(userparty)
            switchin = input("Pick a Pokemon to Switch into: ")
            print("You switched into", switchin)
            userpokemon = switchin


            

        if userdo == "Attack" or userdo == "attack":
            print(firstpokemonmoves)
            use = input("Pick a move to use: ")
            time.sleep(times)
            Turns.speedcheck(enemyspeed, currentspeed)
            
            if "User" in goingfirst:
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
            if "Enemy" in goingfirst:
                going = "Enemy"
                Mike.Raichudoing()
                
            




        
      


Turns.turnone(firstpokemon, "Raichu", "Elite Four Member Mike M.")

        

#Turns.turnone(playerpokemon1, "Charizard","Adam")



#Tims team
#Pikachu - Toxic, Thunderbolt, Double Team, Surf
#Gyarados - 
#Moltres
#Articuno
#Venusaur
#Mewtwo