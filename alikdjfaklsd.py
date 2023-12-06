import json
import os
test = open("data.json", encoding="utf8")
data = json.load(test)
test2 = open("playerteaminfo.json", encoding="utf8")
data2 = json.load(test2)
allpokemon = []
playerteam = []
firstpokemonmoves = []
secondpokemonmoves = []
thirdpokemonmoves = []
fourthpokemonmoves = []
fifthpokemonmoves = []
sixthpokemonmoves = []
pokemonfound1 = 0
pokemonfound2 = 0
pokemonfound3 = 0
pokemonfound4 = 0
pokemonfound5 = 0
pokemonfound6 = 0
firstpokemonnumber = 0
secondpokemonnumber = 0
thirdpokemonnumber = 0
fourthpokemonnumber = 0
fifthpokemonnumber = 0
sixthpokemonnumber = 0
move11found = 0
move12found = 0
move13found = 0
move14found = 0
move21found = 0
move22found = 0
move23found = 0
move24found = 0
move31found = 0
move32found = 0
move33found = 0
move34found = 0
move41found = 0
move42found = 0
move43found = 0
move44found = 0
move51found = 0
move52found = 0
move53found = 0
move54found = 0
move61found = 0
move62found = 0
move63found = 0
move64found = 0
findnewpokemon1 = 1
findnewpokemon2 = 1
findnewpokemon3 = 1
findnewpokemon4 = 1
findnewpokemon5 = 1
findnewpokemon6 = 1
findmove11 = 1
findmove12 = 1
findmove13 = 1
findmove14 = 1
findmove21 = 1
findmove22 = 1
findmove23 = 1
findmove24 = 1
findmove31 = 1
findmove32 = 1
findmove33 = 1
findmove34 = 1
findmove41 = 1
findmove42 = 1
findmove43 = 1
findmove44 = 1
findmove51 = 1
findmove52 = 1
findmove53 = 1
findmove54 = 1
findmove61 = 1
findmove62 = 1
findmove63 = 1
findmove64 = 1
findnewmove1 = 1
findnewmove2 = 1
findnewmove3 = 1
findnewmove4 = 1
findnewmove5 = 1
findnewmove6 = 1
findnewmove7 = 1
findnewmove8 = 1
findnewmove9 = 1
findnewmove10 = 1
findnewmove11 = 1
findnewmove12 = 1
findnewmove13 = 1
findnewmove14 = 1
findnewmove15 = 1
findnewmove16 = 1
findnewmove17 = 1
findnewmove18 = 1
differentsecondpokemon = 1
differentthirdpokemon = 1
differentfourthpokemon = 1
differentfifthpokemon = 1
differentsixthpokemon = 1
for i in range(len(data)):
    allpokemon.append(data[i]["Name"])
print(allpokemon)
firstpokemon = input("\nWhat pokemon do you want on your team? ")
for i in range(len(data)):
    if firstpokemon == (data[i]["Name"]):
        playerteam.append(firstpokemon)
        firstpokemonnumber = i
        pokemonfound1 = 1
        break
if pokemonfound1 == 0:
    while pokemonfound1 == 0:
        firstpokemon = input("Try again ")
        for i in range(len(data)):
            if firstpokemon == (data[i]["Name"]):
                playerteam.append(firstpokemon)
                pokemonfound1 == 1
for i in range(len(data)):
    if firstpokemon == (data[i]["Name"]):
        print(data[i]["Learnable Moves"])
        move11 = input("Choose a learnable move ")
        for i in range(len(data[firstpokemonnumber]["Learnable Moves"])):
            if move11 in (data[firstpokemonnumber]["Learnable Moves"][i]):
                firstpokemonmoves.append(move11)
                move11found = 1
                break
        if move11found == 0:
            while move11found == 0:
                move11 = input("Try again ")
                for i in range(len(data)):
                    if move11 in (data[firstpokemonnumber]["Learnable Moves"]):
                        firstpokemonmoves.append(move11)
                        findmove11 == 1
for i in range(len(data)):
    if firstpokemon == (data[i]["Name"]):
        move12 = input("Choose a learnable move ")
        for i in range(len(data[firstpokemonnumber]["Learnable Moves"])):
            if move12 in (data[firstpokemonnumber]["Learnable Moves"][i]):
                firstpokemonmoves.append(move12)
                move12found = 1
                break
        if move12found == 0:
            while move12found == 0:
                    move12 = input("Try again ")
                    for i in range(len(data[firstpokemonnumber]["Learnable Moves"])):
                        if move12 in (data[firstpokemonnumber]["Learnable Moves"][i]):
                            firstpokemonmoves.append(move12)
                            move12found == 1 
if move12 == move11:
    firstpokemonmoves.remove(move12)
    move12found = 0
    for i in range(findnewmove1):
        move12 = input("Choose a move that you haven't chosen yet ")
        for i in range(len(data[firstpokemonnumber]["Learnable Moves"])):
            if move12 in (data[firstpokemonnumber]["Learnable Moves"][i]):
                firstpokemonmoves.append(move12)
                move12found = 1
                break
        if move12found == 0:
            for i in range(findmove12):
                move12 = input("Try again ")
            for i in range(len(data[firstpokemonnumber]["Learnable Moves"])):
                if move12 in (data[firstpokemonnumber]["Learnable Moves"][i]):
                    firstpokemonmoves.append(move12)
                    break
                else:
                    findmove12 += 1
        if move12 == move11: 
            findnewmove1 += 1
for i in range(len(data)):
    if firstpokemon == (data[i]["Name"]):
        move13 = input("Choose a learnable move ")
        for i in range(len(data[firstpokemonnumber]["Learnable Moves"])):
            if move13 in (data[firstpokemonnumber]["Learnable Moves"][i]):
                firstpokemonmoves.append(move13)
                move13found = 1
                break
        if move13found == 0:
            while move13found == 0:
                    move13 = input("Try again ")
                    for i in range(len(data[firstpokemonnumber]["Learnable Moves"])):
                        if move13 in (data[firstpokemonnumber]["Learnable Moves"][i]):
                            firstpokemonmoves.append(move13)
                            move13found == 1
if move13 == move11 or move13 == move12:
    firstpokemonmoves.remove(move13)
    move13found = 0
    for i in range(findnewmove2):
        move13 = input("Choose a move that you haven't chosen yet ")
        for i in range(len(data[firstpokemonnumber]["Learnable Moves"])):
            if move13 in (data[firstpokemonnumber]["Learnable Moves"][i]):
                firstpokemonmoves.append(move13)
                move13found = 1
                break
        if move13found == 0:
            for i in range(findmove13):
                move13 = input("Try again ")
            for i in range(len(data[firstpokemonnumber]["Learnable Moves"])):
                if move13 in (data[firstpokemonnumber]["Learnable Moves"][i]):
                    firstpokemonmoves.append(move13)
                    break
                else:
                    findmove13 += 1
        if move13 == move11 or move13 == move11: 
            findnewmove2 += 1
for i in range(len(data)):
    if firstpokemon == (data[i]["Name"]):
        move14 = input("Choose a learnable move ")
        for i in range(len(data[firstpokemonnumber]["Learnable Moves"])):
            if move14 in (data[firstpokemonnumber]["Learnable Moves"][i]):
                firstpokemonmoves.append(move14)
                move14found = 1
                break
        if move14found == 0:
            while move14found == 0:
                move14 = input("Try again ")
            for i in range(len(data[firstpokemonnumber]["Learnable Moves"])):
                if move14 in (data[firstpokemonnumber]["Learnable Moves"][i]):
                    firstpokemonmoves.append(move14)
                    move14found = 0
if move14 == move11 or move14 == move12 or move14 == move13:
    firstpokemonmoves.remove(move14)
    move14found = 0
    for i in range(findnewmove3):
        move14 = input("Choose a move that you haven't chosen yet ")
        for i in range(len(data[firstpokemonnumber]["Learnable Moves"])):
            if move14 in (data[firstpokemonnumber]["Learnable Moves"][i]):
                firstpokemonmoves.append(move14)
                move14found = 1
                break
        if move14found == 0:
            for i in range(findmove14):
                move14 = input("Try again ")
                for i in range(len(data[firstpokemonnumber]["Learnable Moves"])):
                    if move14 in (data[firstpokemonnumber]["Learnable Moves"][i]):
                        firstpokemonmoves.append(move14)
                        break
                    else:
                        findmove14 += 1
        if move14 == move11 or move14 == move12 or move14 == move13: 
            findnewmove3 += 1
with open("playerteaminfo.json", "r") as f:
    playerteamjson = json.load(f) # append to data!!!
    playerteamjson.append({"First Pokemon":playerteam[0], "First Pokemon's Moves":firstpokemonmoves})
    new_file = "updated.json"
    with open(new_file, "w") as f:
        json_string = json.dumps(data2, indent=4)
        f.write(json_string)
    os.remove("playerteaminfo.json")
    os.rename(new_file, "playerteaminfo.json")

