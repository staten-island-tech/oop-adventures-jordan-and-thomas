import json
test = open("data.json", encoding="utf8")
data = json.load(test)
class Pokemon():
    def pokemonteam(self, firstpokemon, firstpokemonmoves, secondpokemon, secondpokemonmoves, thirdpokemon, thirdpokemonmoves, fourthpokemon, fourthpokemonmoves, fifthpokemon, fifthpokemonmoves, sixthpokemon, sixthpokemonmoves):
        self.firstpokemon = firstpokemon
        self.firstpokemonmoves = firstpokemonmoves
        self.secondpokemon = secondpokemon
        self.secondpokemonmoves = secondpokemonmoves
        self.thirdpokemon