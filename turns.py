import json
import time
from teambuilder import Pokemon


import json
test = open("pokemon.json", encoding="utf8")
data = json.load(test)


#test = open("data.json", encoding="utf8")
#data = json.load(test)
#movelist = len(data)

#quiz = open("pokemon.json", encoding="utf8")
#pokemon = json.load(quiz)
#pokemonlist = len(pokemon)

#firstpokemon = "Bulbasuar"
#secondpokemon = "Weedle"
#thirdpokemon = "Beedrill"
#fourthpokemon = "Poliwrath"
#fifthpokemon = "Arbok"
#sixthpokemon = "Fearow"

#move1 = "Leech Seed"
#move2 = "Absorb"
#move3 = "Growl"
#move4 = "Vine Whip"
#firstpokemonmoves = [move1, move2, move3, move4]

Pokemon.teambuilder()

playerpokemon1 = firstpokemon
playerpokemon2 = secondpokemon
playerpokemon3 = thirdpokemon
playerpokemon4 = fourthpokemon
playerpokemon5 = fifthpokemon
playerpokemon6 = sixthpokemon

pokemon1move1 = move1


class Turns():
    def turnone(playerpokemon1, enemypokemon1, enemy):
        print("You are challenged by", enemy)
        time.sleep(1)
        print("You threw out", playerpokemon1)
        time.sleep(0.5)
        print(enemy, "threw out", enemypokemon1)
        time.sleep(1.5)
        print(firstpokemonmoves)
        use = input("Pick a move to use: ")
        time.sleep(1)
        print("You used", use)
        time.sleep(1)
        for i in range(b):
            if data[i]["name"] == use:
                damage = data[i]["power"]
                print("It did", damage, "damage")
      


#Turns.turnone(playerpokemon1, "Pikachu", "Elite Four Member Mike M.")

        

#Turns.turnone(playerpokemon1, "Charizard","Adam")



#Tims team
#Pikachu - Toxic, Thunderbolt, Double Team, Surf
#Gyarados - 
#Moltres
#Articuno
#Venusaur
#Mewtwo