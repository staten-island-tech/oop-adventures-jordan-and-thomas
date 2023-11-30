import json
with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)

b = len(data)

firstpokemon = "Bulbasuar"
secondpokemon = "Weedle"
thirdpokemon = "Beedrill"
fourthpokemon = "Poliwrath"
fifthpokemon = "Arbok"
sixthpokemon = "Fearow"

move1 = "Leech Seed"
move2 = "Absorb"
move3 = "Growl"
move4 = "Vine Whip"
firstpokemonmoves = [move1, move2, move3, move4]

playerpokemon1 = firstpokemon
playerpokemon2 = secondpokemon
playerpokemon3 = thirdpokemon
playerpokemon4 = fourthpokemon
playerpokemon5 = fifthpokemon
playerpokemon6 = sixthpokemon

class Turns():
    def turnone(playerpokemon1, enemypokemon1, enemy):
        print("You threw out", playerpokemon1)
        print(enemy, "threw out", enemypokemon1)
        print(firstpokemonmoves)
        use = input("Pick a move to use: ")
        print("You used", use)
        for i in range(b):
            if data[i]["name"] == use:
                damage = data[i]["power"]
                print("It did", damage, "damage")
      
                

        

Turns.turnone(playerpokemon1, "Charizard","Adam")
