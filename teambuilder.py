import json
import os 
test = open("data.json", encoding="utf8")
data = json.load(test)
class Teambuilder():
    def teambuilder():
        with open("playerteaminfo.json", "r") as f:
            playerteamjson = json.load(f)
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
        print(allpokemon)
        secondpokemon = input("\nWhat pokemon do you want on your team? ")
        for i in range(len(data)):
            if secondpokemon == (data[i]["Name"]):
                playerteam.append(secondpokemon)
                secondpokemonnumber = i
                pokemonfound2 = 1
                break
        if pokemonfound2 == 0:
            while pokemonfound2 == 0:
                secondpokemon = input("Try again ")
                for i in range(len(data)):
                    if secondpokemon == (data[i]["Name"]):
                        playerteam.append(secondpokemon)
                        pokemonfound2 == 1
        if secondpokemon == firstpokemon:
            playerteam.remove(secondpokemon)
            pokemonfound2 = 0
            for i in range(len(data)):
                secondpokemon = input("Choose a pokemon you haven't chosen yet ")
                if secondpokemon == (data[i]["Name"]):
                    playerteam.append(secondpokemon)
                    secondpokemonnumber = i
                    pokemonfound2 = 1
                    break
            if pokemonfound2 == 0:
                while pokemonfound2 == 0:
                    secondpokemon = input("Try again ")
                    for i in range(len(data)):
                        if secondpokemon == (data[i]["Name"]):
                            playerteam.append(secondpokemon)
                            pokemonfound2 == 1
        for i in range(len(data)):
            if secondpokemon == (data[i]["Name"]):
                print(data[i]["Learnable Moves"])
                move21 = input("Choose a learnable move ")
                for i in range(len(data[secondpokemonnumber]["Learnable Moves"])):
                    if move21 in (data[secondpokemonnumber]["Learnable Moves"][i]):
                        secondpokemonmoves.append(move21)
                        move21found = 1
                        break
                if move21found == 0:
                    while move21found == 0:
                        move21 = input("Try again ")
                        for i in range(len(data)):
                            if move21 in (data[secondpokemonnumber]["Learnable Moves"]):
                                secondpokemonmoves.append(move21)
                                move21found = 1
        for i in range(len(data)):
            if secondpokemon == (data[i]["Name"]):
                move22 = input("Choose a learnable move ")
                for i in range(len(data[secondpokemonnumber]["Learnable Moves"])):
                    if move22 in (data[secondpokemonnumber]["Learnable Moves"][i]):
                        secondpokemonmoves.append(move22)
                        move22found = 1
                        break
                if move22found == 0:
                    while move22found == 0:
                        move22 = input("Try again ")
                    for i in range(len(data[secondpokemonnumber]["Learnable Moves"])):
                        if move22 in (data[secondpokemonnumber]["Learnable Moves"][i]):
                            secondpokemonmoves.append(move22)
                            move22found == 1
        if move22 == move21:
            secondpokemonmoves.remove(move22)
            move22found = 0
            for i in range(findnewmove4):
                move22 = input("Choose a move that you haven't chosen yet ")
                for i in range(len(data[secondpokemonnumber]["Learnable Moves"])):
                    if move22 in (data[secondpokemonnumber]["Learnable Moves"][i]):
                        secondpokemonmoves.append(move22)
                        move22found = 1
                        break
                if move22found == 0:
                    for i in range(findmove22):
                        move22 = input("Try again ")
                    for i in range(len(data[secondpokemonnumber]["Learnable Moves"])):
                        if move22 in (data[secondpokemonnumber]["Learnable Moves"][i]):
                            secondpokemonmoves.append(move22)
                            break
                        else:
                            findmove22 += 1
                if move22 == move21: 
                    findnewmove4 += 1
        for i in range(len(data)):
            if secondpokemon == (data[i]["Name"]):
                move23 = input("Choose a learnable move ")
                for i in range(len(data[secondpokemonnumber]["Learnable Moves"])):
                    if move23 in (data[secondpokemonnumber]["Learnable Moves"][i]):
                        secondpokemonmoves.append(move23)
                        move23found = 1
                        break
                if move23found == 0:
                    while move23found == 0:
                        move23 = input("Try again ")
                    for i in range(len(data[secondpokemonnumber]["Learnable Moves"])):
                        if move23 in (data[secondpokemonnumber]["Learnable Moves"][i]):
                            secondpokemonmoves.append(move23)
                            move23found == 1
        if move23 == move21 or move23 == move22:
            secondpokemonmoves.remove(move23)
            move23found = 0
            for i in range(findnewmove5):
                move23 = input("Choose a move that you haven't chosen yet ")
                for i in range(len(data[secondpokemonnumber]["Learnable Moves"])):
                    if move23 in (data[secondpokemonnumber]["Learnable Moves"][i]):
                        secondpokemonmoves.append(move23)
                        move23found = 1
                        break
                if move23found == 0:
                    for i in range(findmove23):
                        move23 = input("Try again ")
                    for i in range(len(data[secondpokemonnumber]["Learnable Moves"])):
                        if move23 in (data[secondpokemonnumber]["Learnable Moves"][i]):
                            secondpokemonmoves.append(move23)
                            break
                        else:
                            findmove23 += 1
                if move23 == move21 or move23 == move22: 
                    findnewmove5 += 1
        for i in range(len(data)):
            if secondpokemon == (data[i]["Name"]):
                move24 = input("Choose a learnable move ")
                for i in range(len(data[secondpokemonnumber]["Learnable Moves"])):
                    if move24 in (data[secondpokemonnumber]["Learnable Moves"][i]):
                        secondpokemonmoves.append(move24)
                        move24found = 1
                        break
                if move24found == 0:
                    while move24found == 0:
                        move24 = input("Try again ")
                    for i in range(len(data[secondpokemonnumber]["Learnable Moves"])):
                        if move24 in (data[secondpokemonnumber]["Learnable Moves"][i]):
                            secondpokemonmoves.append(move24)
                            move24found == 1
        if move24 == move21 or move24 == move22 or move24 == move23:
            secondpokemonmoves.remove(move24)
            move24found = 0
            for i in range(findnewmove6):
                move24 = input("Choose a move that you haven't chosen yet ")
                for i in range(len(data[secondpokemonnumber]["Learnable Moves"])):
                    if move24 in (data[secondpokemonnumber]["Learnable Moves"][i]):
                        secondpokemonmoves.append(move24)
                        move24found = 1
                        break
                if move24found == 0:
                    for i in range(findmove24):
                        move24 = input("Try again ")
                    for i in range(len(data[secondpokemonnumber]["Learnable Moves"])):
                        if move24 in (data[secondpokemonnumber]["Learnable Moves"][i]):
                            secondpokemonmoves.append(move24)
                            break
                        else:
                            findmove24 += 1
                if move24 == move21 or move24 == move22 or move24 == move23: 
                    findnewmove6 += 1
        print(allpokemon)
        thirdpokemon = input("\nWhat pokemon do you want on your team? ")
        for i in range(len(data)):
            if thirdpokemon == (data[i]["Name"]):
                playerteam.append(thirdpokemon)
                thirdpokemonnumber = i
                pokemonfound3 = 1
                break
        if pokemonfound3 == 0:
            while pokemonfound3 == 0:
                thirdpokemon = input("Try again ")
                for i in range(len(data)):
                    if thirdpokemon == (data[i]["Name"]):
                        playerteam.append(thirdpokemon)
                        pokemonfound3 == 1
        if thirdpokemon == firstpokemon or thirdpokemon == secondpokemon:
            playerteam.remove(thirdpokemon)
            pokemonfound3 = 0
            for i in range(len(data)):
                thirdpokemon = input("CHoose a pokemon you haven't chosen yet ")
                if thirdpokemon == (data[i]["Name"]):
                    playerteam.append(thirdpokemon)
                    thirdpokemonnumber = i
                    pokemonfound3 = 1
                    break
            if pokemonfound3 == 0:
                while pokemonfound3 == 0:
                    thirdpokemon = input("Try again ")
                    for i in range(len(data)):
                        if thirdpokemon == (data[i]["Name"]):
                            playerteam.append(thirdpokemon)
                            pokemonfound3 == 1
        for i in range(len(data)):
            if thirdpokemon == (data[i]["Name"]):
                print(data[i]["Learnable Moves"])
                move31 = input("Choose a learnable move ")
                for i in range(len(data[thirdpokemonnumber]["Learnable Moves"])):
                    if move31 in (data[thirdpokemonnumber]["Learnable Moves"][i]):
                        thirdpokemonmoves.append(move31)
                        move31found = 1
                        break
                if move31found == 0:
                    while move31found == 0:
                        move31 = input("Try again ")
                        for i in range(len(data)):
                            if move31 in (data[thirdpokemonnumber]["Learnable Moves"]):
                                thirdpokemonmoves.append(move31)
                                move31found == 1
        for i in range(len(data)):
            if thirdpokemon == (data[i]["Name"]):
                move32 = input("Choose a learnable move ")
                for i in range(len(data[thirdpokemonnumber]["Learnable Moves"])):
                    if move32 in (data[thirdpokemonnumber]["Learnable Moves"][i]):
                        thirdpokemonmoves.append(move32)
                        move32found = 1
                        break
                if move32found == 0:
                    while move32found == 0:
                        move32 = input("Try again ")
                    for i in range(len(data[thirdpokemonnumber]["Learnable Moves"])):
                        if move32 in (data[thirdpokemonnumber]["Learnable Moves"][i]):
                            thirdpokemonmoves.append(move32)
                            move32found == 1
        if move32 == move31:
            thirdpokemonmoves.remove(move32)
            move32found = 0
            for i in range(findnewmove7):
                move32 = input("Choose a move that you haven't chosen yet ")
                for i in range(len(data[thirdpokemonnumber]["Learnable Moves"])):
                    if move32 in (data[thirdpokemonnumber]["Learnable Moves"][i]):
                        thirdpokemonmoves.append(move32)
                        move32found = 1
                        break
                if move32found == 0:
                    while move32found == 0:
                        move32 = input("Try again ")
                    for i in range(len(data[thirdpokemonnumber]["Learnable Moves"])):
                        if move32 in (data[thirdpokemonnumber]["Learnable Moves"][i]):
                            thirdpokemonmoves.append(move32)
                            move32found == 1
                if move32 == move31: 
                    findnewmove7 += 1
        for i in range(len(data)):
            if thirdpokemon == (data[i]["Name"]):
                move33 = input("Choose a learnable move ")
                for i in range(len(data[thirdpokemonnumber]["Learnable Moves"])):
                    if move33 in (data[thirdpokemonnumber]["Learnable Moves"][i]):
                        thirdpokemonmoves.append(move33)
                        move33found = 1
                        break
                if move33found == 0:
                    while move33found == 0:
                        move33 = input("Try again ")
                    for i in range(len(data[thirdpokemonnumber]["Learnable Moves"])):
                        if move33 in (data[thirdpokemonnumber]["Learnable Moves"][i]):
                            thirdpokemonmoves.append(move33)
                            move33found == 1
        if move33 == move31 or move33 == move32:
            thirdpokemonmoves.remove(move33)
            move33found = 0
            for i in range(findnewmove8):
                move33 = input("Choose a move that you haven't chosen yet ")
                for i in range(len(data[thirdpokemonnumber]["Learnable Moves"])):
                    if move33 in (data[thirdpokemonnumber]["Learnable Moves"][i]):
                        thirdpokemonmoves.append(move33)
                        move33found = 1
                        break
                if move33found == 0:
                    while move33found == 0:
                        move33 = input("Try again ")
                    for i in range(len(data[thirdpokemonnumber]["Learnable Moves"])):
                        if move33 in (data[thirdpokemonnumber]["Learnable Moves"][i]):
                            thirdpokemonmoves.append(move33)
                            move33found == 1
                if move33 == move31 or move33 == move32: 
                    findnewmove8 += 1
        for i in range(len(data)):
            if thirdpokemon == (data[i]["Name"]):
                move34 = input("Choose a learnable move ")
                for i in range(len(data[thirdpokemonnumber]["Learnable Moves"])):
                    if move34 in (data[thirdpokemonnumber]["Learnable Moves"][i]):
                        thirdpokemonmoves.append(move34)
                        move34found = 1
                        break
                if move34found == 0:
                    while move34found == 0:
                        move34 = input("Try again ")
                    for i in range(len(data[thirdpokemonnumber]["Learnable Moves"])):
                        if move34 in (data[thirdpokemonnumber]["Learnable Moves"][i]):
                            thirdpokemonmoves.append(move34)
                            move34found == 1
        if move34 == move31 or move34 == move32 or move34 == move33:
            thirdpokemonmoves.remove(move34)
            move34found = 0
            for i in range(findnewmove9):
                move34 = input("Choose a move that you haven't chosen yet ")
                for i in range(len(data[thirdpokemonnumber]["Learnable Moves"])):
                    if move34 in (data[thirdpokemonnumber]["Learnable Moves"][i]):
                        thirdpokemonmoves.append(move34)
                        move34found = 1
                        break
                if move34found == 0:
                    while move34found == 0:
                        move34 = input("Try again ")
                    for i in range(len(data[thirdpokemonnumber]["Learnable Moves"])):
                        if move34 in (data[thirdpokemonnumber]["Learnable Moves"][i]):
                            thirdpokemonmoves.append(move34)
                            move34found == 1
                if move34 == move31 or move34 == move32 or move34 == move33: 
                    findnewmove9 += 1
        print(allpokemon)
        fourthpokemon = input("\nWhat pokemon do you want on your team? ")
        for i in range(len(data)):
            if fourthpokemon == (data[i]["Name"]):
                playerteam.append(fourthpokemon)
                fourthpokemonnumber = i
                pokemonfound4 = 1
                break
        if pokemonfound4 == 0:
            while pokemonfound4 == 0:
                firstpokemon = input("Try again ")
                for i in range(len(data)):
                    if fourthpokemon == (data[i]["Name"]):
                        playerteam.append(fourthpokemon)
                        pokemonfound4 == 1
        if fourthpokemon == firstpokemon or fourthpokemon == secondpokemon or fourthpokemon == thirdpokemon:
            playerteam.remove(fourthpokemon)
            pokemonfound4 = 0
            for i in range(len(data)):
                fourthpokemon = input("Choose a pokemon you haven't chosen yet ")
                if fourthpokemon == (data[i]["Name"]):
                    playerteam.append(fourthpokemon)
                    fourthpokemonnumber = i
                    pokemonfound4 = 1
                    break
            if pokemonfound4 == 0:
                while pokemonfound4 == 0:
                    fourthpokemon = input("Try again ")
                    for i in range(len(data)):
                        if fourthpokemon == (data[i]["Name"]):
                            playerteam.append(fourthpokemon)
                            pokemonfound4 == 1
        for i in range(len(data)):
            if fourthpokemon == (data[i]["Name"]):
                print(data[i]["Learnable Moves"])
                move41 = input("Choose a learnable move ")
                for i in range(len(data[fourthpokemonnumber]["Learnable Moves"])):
                    if move41 in (data[fourthpokemonnumber]["Learnable Moves"][i]):
                        fourthpokemonmoves.append(move41)
                        move41found = 1
                        break
                if move41found == 0:
                    while move41found == 0:
                        move41 = input("Try again ")
                        for i in range(len(data)):
                            if move41 in (data[fourthpokemonnumber]["Learnable Moves"]):
                                fourthpokemonmoves.append(move41)
                                move41found == 1
        for i in range(len(data)):
            if fourthpokemon == (data[i]["Name"]):
                move42 = input("Choose a learnable move ")
                for i in range(len(data[fourthpokemonnumber]["Learnable Moves"])):
                    if move42 in (data[fourthpokemonnumber]["Learnable Moves"][i]):
                        fourthpokemonmoves.append(move42)
                        move42found = 1
                        break
                if move42found == 0:
                    while move42found == 0:
                        move42 = input("Try again ")
                    for i in range(len(data[fourthpokemonnumber]["Learnable Moves"])):
                        if move12 in (data[fourthpokemonnumber]["Learnable Moves"][i]):
                            fourthpokemonmoves.append(move42)
                            move42found == 1
        if move42 == move41:
            fourthpokemonmoves.remove(move42)
            move42found = 0
            for i in range(findnewmove10):
                move42 = input("Choose a move that you haven't chosen yet ")
                for i in range(len(data[fourthpokemonnumber]["Learnable Moves"])):
                    if move42 in (data[fourthpokemonnumber]["Learnable Moves"][i]):
                        fourthpokemonmoves.append(move42)
                        move42found = 1
                        break
                if move42found == 0:
                    while move42found == 0:
                        move42 = input("Try again ")
                    for i in range(len(data[fourthpokemonnumber]["Learnable Moves"])):
                        if move42 in (data[fourthpokemonnumber]["Learnable Moves"][i]):
                            fourthpokemonmoves.append(move42)
                            move42found == 1
                if move42 == move41: 
                    findnewmove10 += 1
        for i in range(len(data)):
            if fourthpokemon == (data[i]["Name"]):
                move43 = input("Choose a learnable move ")
                for i in range(len(data[fourthpokemonnumber]["Learnable Moves"])):
                    if move43 in (data[fourthpokemonnumber]["Learnable Moves"][i]):
                        fourthpokemonmoves.append(move43)
                        move43found = 1
                        break
                if move43found == 0:
                    while move43found == 0:
                        move43 = input("Try again ")
                    for i in range(len(data[fourthpokemonnumber]["Learnable Moves"])):
                        if move43 in (data[fourthpokemonnumber]["Learnable Moves"][i]):
                            fourthpokemonmoves.append(move43)
                            move43found == 1
        if move43 == move41 or move43 == move42:
            fourthpokemonmoves.remove(move43)
            move43found = 0
            for i in range(findnewmove11):
                move43 = input("Choose a move that you haven't chosen yet ")
                for i in range(len(data[fourthpokemonnumber]["Learnable Moves"])):
                    if move43 in (data[fourthpokemonnumber]["Learnable Moves"][i]):
                        fourthpokemonmoves.append(move43)
                        move43found = 1
                        break
                if move43found == 0:
                    while move43found == 0:
                        move43 = input("Try again ")
                    for i in range(len(data[fourthpokemonnumber]["Learnable Moves"])):
                        if move43 in (data[fourthpokemonnumber]["Learnable Moves"][i]):
                            fourthpokemonmoves.append(move43)
                            move43found == 1
                if move43 == move41 or move43 == move42: 
                    findnewmove11 += 1
        for i in range(len(data)):
            if fourthpokemon == (data[i]["Name"]):
                move44 = input("Choose a learnable move ")
                for i in range(len(data[fourthpokemonnumber]["Learnable Moves"])):
                    if move44 in (data[fourthpokemonnumber]["Learnable Moves"][i]):
                        fourthpokemonmoves.append(move44)
                        move44found = 1
                        break
                if move44found == 0:
                    while move44found == 0:
                        move44 = input("Try again ")
                    for i in range(len(data[fourthpokemonnumber]["Learnable Moves"])):
                        if move44 in (data[fourthpokemonnumber]["Learnable Moves"][i]):
                            fourthpokemonmoves.append(move44)
                            move44found == 1
        if move44 == move41 or move44 == move42 or move44 == move43:
            fourthpokemonmoves.remove(move44)
            move44found = 0
            for i in range(findnewmove12):
                move44 = input("Choose a move that you haven't chosen yet ")
                for i in range(len(data[fourthpokemonnumber]["Learnable Moves"])):
                    if move44 in (data[fourthpokemonnumber]["Learnable Moves"][i]):
                        fourthpokemonmoves.append(move44)
                        move44found = 1
                        break
                if move44found == 0:
                    while move44found == 0:
                        move44 = input("Try again ")
                    for i in range(len(data[fourthpokemonnumber]["Learnable Moves"])):
                        if move44 in (data[fourthpokemonnumber]["Learnable Moves"][i]):
                            fourthpokemonmoves.append(move44)
                            move44found == 1
                if move44 == move41 or move44 == move42 or move44 == move43: 
                    findnewmove12 += 1
        print(allpokemon)
        fifthpokemon = input("\nWhat pokemon do you want on your team? ")
        for i in range(len(data)):
            if fifthpokemon == (data[i]["Name"]):
                playerteam.append(fifthpokemon)
                fifthpokemonnumber = i
                pokemonfound5 = 1
                break
        if pokemonfound5 == 0:
            while pokemonfound5 == 0:
                fifthpokemon = input("Try again ")
                for i in range(len(data)):
                    if fifthpokemon == (data[i]["Name"]):
                        playerteam.append(fifthpokemon)
                        pokemonfound5 == 1
        if fifthpokemon == firstpokemon or fifthpokemon == secondpokemon or fifthpokemon == thirdpokemon or fifthpokemon == fourthpokemon:
            playerteam.remove(fifthpokemon)
            pokemonfound5 = 0
            for i in range(len(data)):
                fifthpokemon = input("Choose a pokemon you haven't chosen yet ")
                if fifthpokemon == (data[i]["Name"]):
                    playerteam.append(fifthpokemon)
                    fifthpokemonnumber = i
                    pokemonfound5 = 1
                    break
            if pokemonfound5 == 0:
                while pokemonfound5 == 0:
                    fifthpokemon = input("Try again ")
                    for i in range(len(data)):
                        if fifthpokemon == (data[i]["Name"]):
                            playerteam.append(fifthpokemon)
                            pokemonfound5 == 1
        for i in range(len(data)):
            if fifthpokemon == (data[i]["Name"]):
                print(data[i]["Learnable Moves"])
                move51 = input("Choose a learnable move ")
                for i in range(len(data[fifthpokemonnumber]["Learnable Moves"])):
                    if move51 in (data[fifthpokemonnumber]["Learnable Moves"][i]):
                        fifthpokemonmoves.append(move51)
                        move51found = 1
                        break
                if move51found == 0:
                    while move51found == 0:
                        move51 = input("Try again ")
                        for i in range(len(data)):
                            if move51 in (data[fifthpokemonnumber]["Learnable Moves"]):
                                fifthpokemonmoves.append(move51)
                                move51found == 1
        for i in range(len(data)):
            if fifthpokemon == (data[i]["Name"]):
                move52 = input("Choose a learnable move ")
                for i in range(len(data[fifthpokemonnumber]["Learnable Moves"])):
                    if move52 in (data[fifthpokemonnumber]["Learnable Moves"][i]):
                        fifthpokemonmoves.append(move52)
                        move52found = 1
                        break
                if move52found == 0:
                    while move52found == 0:
                        move52 = input("Try again ")
                        for i in range(len(data[fifthpokemonnumber]["Learnable Moves"])):
                            if move12 in (data[fifthpokemonnumber]["Learnable Moves"][i]):
                                fifthpokemonmoves.append(move52)
                                move52found == 1
        if move52 == move51:
            fifthpokemonmoves.remove(move52)
            move52found = 0
            for i in range(findnewmove13):
                move52 = input("Choose a move that you haven't chosen yet ")
                for i in range(len(data[fifthpokemonnumber]["Learnable Moves"])):
                    if move52 in (data[fifthpokemonnumber]["Learnable Moves"][i]):
                        fifthpokemonmoves.append(move52)
                        move52found = 1
                        break
                if move52found == 0:
                    while move52found == 0:
                        move52 = input("Try again ")
                    for i in range(len(data[fifthpokemonnumber]["Learnable Moves"])):
                        if move52 in (data[fifthpokemonnumber]["Learnable Moves"][i]):
                            fifthpokemonmoves.append(move52)
                            move52found == 1
                if move52 == move51: 
                    findnewmove13 += 1
        for i in range(len(data)):
            if fifthpokemon == (data[i]["Name"]):
                move53 = input("Choose a learnable move ")
                for i in range(len(data[fifthpokemonnumber]["Learnable Moves"])):
                    if move53 in (data[fifthpokemonnumber]["Learnable Moves"][i]):
                        fifthpokemonmoves.append(move53)
                        move53found = 1
                        break
                if move53found == 0:
                    while move53found == 0:
                        move53 = input("Try again ")
                    for i in range(len(data[fifthpokemonnumber]["Learnable Moves"])):
                        if move53 in (data[fifthpokemonnumber]["Learnable Moves"][i]):
                            fifthpokemonmoves.append(move53)
                            move53found == 1
        if move53 == move51 or move53 == move52:
            fifthpokemonmoves.remove(move53)
            move53found = 0
            for i in range(findnewmove14):
                move53 = input("Choose a move that you haven't chosen yet ")
                for i in range(len(data[fifthpokemonnumber]["Learnable Moves"])):
                    if move53 in (data[fifthpokemonnumber]["Learnable Moves"][i]):
                        fifthpokemonmoves.append(move53)
                        move53found = 1
                        break
                if move53found == 0:
                    while move53found == 0:
                        move53 = input("Try again ")
                    for i in range(len(data[fifthpokemonnumber]["Learnable Moves"])):
                        if move53 in (data[fifthpokemonnumber]["Learnable Moves"][i]):
                            fifthpokemonmoves.append(move53)
                            move53found == 1
                if move53 == move51 or move53 == move52: 
                    findnewmove14 += 1
        for i in range(len(data)):
            if fifthpokemon == (data[i]["Name"]):
                move54 = input("Choose a learnable move ")
                for i in range(len(data[fifthpokemonnumber]["Learnable Moves"])):
                    if move54 in (data[fifthpokemonnumber]["Learnable Moves"][i]):
                        fifthpokemonmoves.append(move54)
                        move54found = 1
                        break
                if move54found == 0:
                    while move54found == 0:
                        move54 = input("Try again ")
                    for i in range(len(data[fifthpokemonnumber]["Learnable Moves"])):
                        if move54 in (data[fifthpokemonnumber]["Learnable Moves"][i]):
                            fifthpokemonmoves.append(move54)
                            move54found == 1
        if move54 == move51 or move54 == move52 or move54 == move53:
            fifthpokemonmoves.remove(move54)
            move54found = 0
            for i in range(findnewmove15):
                move54 = input("Choose a move that you haven't chosen yet ")
                for i in range(len(data[fifthpokemonnumber]["Learnable Moves"])):
                    if move54 in (data[fifthpokemonnumber]["Learnable Moves"][i]):
                        fifthpokemonmoves.append(move54)
                        move54found = 1
                        break
                if move54found == 0:
                    while move54found == 0:
                        move54 = input("Try again ")
                    for i in range(len(data[fifthpokemonnumber]["Learnable Moves"])):
                        if move54 in (data[fifthpokemonnumber]["Learnable Moves"][i]):
                            fifthpokemonmoves.append(move54)
                            move54found == 1
                if move54 == move51 or move54 == move52 or move54 == move53: 
                    findnewmove15 += 1
        print(allpokemon)
        sixthpokemon = input("\nWhat pokemon do you want on your team? ")
        for i in range(len(data)):
            if sixthpokemon == (data[i]["Name"]):
                playerteam.append(sixthpokemon)
                sixthpokemonnumber = i
                pokemonfound6 = 1
                break
        if pokemonfound6 == 0:
            while pokemonfound6 == 0:
                sixthpokemon = input("Try again ")
                for i in range(len(data)):
                    if sixthpokemon == (data[i]["Name"]):
                        playerteam.append(sixthpokemon)
                        pokemonfound6 == 1
        if sixthpokemon == firstpokemon or sixthpokemon == secondpokemon or sixthpokemon == thirdpokemon or sixthpokemon == fourthpokemon or sixthpokemon == fifthpokemon:
            playerteam.remove(sixthpokemon)
            pokemonfound6 = 0
            for i in range(len(data)):
                sixthpokemon = input("Choose a pokemon you haven't chosen yet ")
                if sixthpokemon == (data[i]["Name"]):
                    playerteam.append(sixthpokemon)
                    sixthpokemonnumber = i
                    pokemonfound6 = 1
                    break
            if pokemonfound6 == 0:
                while pokemonfound6 == 0:
                    sixthpokemon = input("Try again ")
                    for i in range(len(data)):
                        if sixthpokemon == (data[i]["Name"]):
                            playerteam.append(sixthpokemon)
                            pokemonfound6 == 1
        for i in range(len(data)):
            if sixthpokemon == (data[i]["Name"]):
                print(data[i]["Learnable Moves"])
                move61 = input("Choose a learnable move ")
                for i in range(len(data[sixthpokemonnumber]["Learnable Moves"])):
                    if move61 in (data[sixthpokemonnumber]["Learnable Moves"][i]):
                        sixthpokemonmoves.append(move61)
                        move61found = 1
                        break
                if move61found == 0:
                    while move61found == 0:
                        move61 = input("Try again ")
                        for i in range(len(data)):
                            if move61 in (data[sixthpokemonnumber]["Learnable Moves"]):
                                sixthpokemonmoves.append(move61)
                                move61found == 1
        for i in range(len(data)):
            if sixthpokemon == (data[i]["Name"]):
                move62 = input("Choose a learnable move ")
                for i in range(len(data[sixthpokemonnumber]["Learnable Moves"])):
                    if move62 in (data[sixthpokemonnumber]["Learnable Moves"][i]):
                        sixthpokemonmoves.append(move62)
                        move62found = 1
                        break
                if move62found == 0:
                    while move62found == 0:
                        move62 = input("Try again ")
                    for i in range(len(data[sixthpokemonnumber]["Learnable Moves"])):
                        if move62 in (data[sixthpokemonnumber]["Learnable Moves"][i]):
                            sixthpokemonmoves.append(move62)
                            move62found == 1
        if move62 == move61:
            sixthpokemonmoves.remove(move62)
            move62found = 0
            for i in range(findnewmove16):
                move62 = input("Choose a move that you haven't chosen yet ")
                for i in range(len(data[sixthpokemonnumber]["Learnable Moves"])):
                    if move52 in (data[sixthpokemonnumber]["Learnable Moves"][i]):
                        sixthpokemonmoves.append(move62)
                        move62found = 1
                        break
                if move62found == 0:
                    while move62found == 0:
                        move62 = input("Try again ")
                    for i in range(len(data[sixthpokemonnumber]["Learnable Moves"])):
                        if move62 in (data[sixthpokemonnumber]["Learnable Moves"][i]):
                            sixthpokemonmoves.append(move62)
                            move62found == 1
                if move62 == move61: 
                    findnewmove16 += 1
        for i in range(len(data)):
            if sixthpokemon == (data[i]["Name"]):
                move63 = input("Choose a learnable move ")
                for i in range(len(data[sixthpokemonnumber]["Learnable Moves"])):
                    if move63 in (data[sixthpokemonnumber]["Learnable Moves"][i]):
                        sixthpokemonmoves.append(move63)
                        move63found = 1
                        break
                if move63found == 0:
                    while move63found == 0:
                        move63 = input("Try again ")
                    for i in range(len(data[sixthpokemonnumber]["Learnable Moves"])):
                        if move63 in (data[sixthpokemonnumber]["Learnable Moves"][i]):
                            sixthpokemonmoves.append(move63)
                            move63found == 1
        if move63 == move61 or move63 == move62:
            sixthpokemonmoves.remove(move63)
            move63found = 0
            for i in range(findnewmove17):
                move63 = input("Choose a move that you haven't chosen yet ")
                for i in range(len(data[sixthpokemonnumber]["Learnable Moves"])):
                    if move63 in (data[sixthpokemonnumber]["Learnable Moves"][i]):
                        sixthpokemonmoves.append(move63)
                        move63found = 1
                        break
                if move63found == 0:
                    while move63found == 0:
                        move63 = input("Try again ")
                    for i in range(len(data[sixthpokemonnumber]["Learnable Moves"])):
                        if move63 in (data[sixthpokemonnumber]["Learnable Moves"][i]):
                            sixthpokemonmoves.append(move63)
                            move63found == 1
                if move63 == move61 or move63 == move62: 
                    findnewmove17 += 1
        for i in range(len(data)):
            if sixthpokemon == (data[i]["Name"]):
                move64 = input("Choose a learnable move ")
                for i in range(len(data[sixthpokemonnumber]["Learnable Moves"])):
                    if move64 in (data[sixthpokemonnumber]["Learnable Moves"][i]):
                        sixthpokemonmoves.append(move64)
                        move64found = 1
                        break
                if move64found == 0:
                    while move64found == 0:
                        move64 = input("Try again ")
                    for i in range(len(data[sixthpokemonnumber]["Learnable Moves"])):
                        if move64 in (data[sixthpokemonnumber]["Learnable Moves"][i]):
                            sixthpokemonmoves.append(move64)
                            break
                        else:
                            findmove64 += 1
        if move64 == move61 or move64 == move62 or move64 == move63:
            sixthpokemonmoves.remove(move64)
            move64found = 0
            for i in range(findnewmove18):
                move64 = input("Choose a move that you haven't chosen yet ")
                for i in range(len(data[sixthpokemonnumber]["Learnable Moves"])):
                    if move64 in (data[sixthpokemonnumber]["Learnable Moves"][i]):
                        sixthpokemonmoves.append(move64)
                        move64found = 1
                        break
                if move64found == 0:
                    while move64found == 0:
                        move64 = input("Try again ")
                    for i in range(len(data[sixthpokemonnumber]["Learnable Moves"])):
                        if move64 in (data[sixthpokemonnumber]["Learnable Moves"][i]):
                            sixthpokemonmoves.append(move64)
                            move64found == 1
                if move64 == move61 or move64 == move62 or move64 == move63: 
                    findnewmove18 += 1
        teaminformation = (playerteam[0], firstpokemonmoves, playerteam[1], secondpokemonmoves, playerteam[2], thirdpokemonmoves, playerteam[3], fourthpokemonmoves, playerteam[4], fifthpokemonmoves, playerteam[5], sixthpokemonmoves)
        print(teaminformation)
        playerteamjson.append({"First Pokemon":playerteam[0], "First Pokemon's Moves":firstpokemonmoves, "Second Pokemon":playerteam[1], "Second Pokemon's Moves":secondpokemonmoves, "Third Pokemon":playerteam[2], "Third Pokemon's Moves":thirdpokemonmoves, "Fourth Pokemon":playerteam[3], "Fourth Pokemon's Moves":fourthpokemonmoves, "Fifth Pokemon":playerteam[4], "Fifth's Pokemon's Moves":fifthpokemonmoves, "Sixth Pokemon":playerteam[5], "Sixth Pokemon's Moves":sixthpokemonmoves})
        new_file = "playerteaminfo.json"
        os.remove("playerteaminfo.json")
        with open(new_file, "w") as f:
            json_string = json.dumps(teaminformation, indent=4)
            f.write(json_string)
        os.rename(new_file, "playerteaminfo.json")
    teambuilder()

        