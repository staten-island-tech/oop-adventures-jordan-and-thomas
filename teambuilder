import json
test = open("data.json", encoding="utf8")
data = json.load(test)

class Pokemon():
    def teambuilder():
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
        firstpokemon = input("What pokemon do you want on your team? ")
        for i in range(len(data)):
            if firstpokemon == (data[i]["Name"]):
                playerteam.append(firstpokemon)
                firstpokemonnumber = i
                pokemonfound1 = 1
                break
        if pokemonfound1 == 0:
            for i in range(findnewpokemon1):
                firstpokemon = input("Try again ")
                for i in range(len(data)):
                    if firstpokemon == (data[i]["Name"]):
                        playerteam.append(firstpokemon)
                    else:
                        findnewpokemon1 += 1
        print(firstpokemonnumber)
        for i in range(len(data)):
            if firstpokemon == (data[i]["Name"]):
                print(data[i]["Learnable Moves"])
                move11 = input("Choose a learnable move ")
                for i in range(len(data[firstpokemonnumber]["Learnable Moves"])):
                    if move11 in (data[firstpokemonnumber]["Learnable Moves"]):
                        firstpokemonmoves.append(move11)
                        move11found = 1
                        break
                if move11found == 0:
                    for i in range(findmove11):
                        move11 = input("Try again ")
                        for i in range(len(data)):
                            if move11 in (data[firstpokemonnumber]["Learnable Moves"]):
                                firstpokemonmoves.append(move11)
                                break
                            else:
                                findmove11 += 1
        for i in range(len(data)):
            if firstpokemon == (data[i]["Name"]):
                move12 = input("Choose a learnable move ")
                for i in range(len(data[firstpokemonnumber]["Learnable Moves"])):
                    if move12 in (data[firstpokemonnumber]["Learnable Moves"]):
                        firstpokemonmoves.append(move12)
                        move12found = 1
                        break
                if move12found == 0:
                    for i in range(findmove12):
                        move12 = input("Try again ")
                    for i in range(len(data)):
                        if move12 in (data[firstpokemonnumber]["Learnable Moves"]):
                            firstpokemonmoves.append(move12)
                            break
                    else:
                        findmove12 += 1
        if move12 in firstpokemonmoves:
            firstpokemonmoves.remove(move12)
            for i in range(findnewmove1):
                move12 = input("Choose a move that you haven't chosen yet ")
                if move12 in firstpokemonmoves: 
                    findnewmove1 += 1
                firstpokemonmoves.append(move12)
        for i in range(len(data)):
            if firstpokemon == (data[i]["Name"]):
                move13 = input("Choose a learnable move ")
                for i in range(len(data[firstpokemonnumber]["Learnable Moves"])):
                    if move13 in (data[firstpokemonnumber]["Learnable Moves"]):
                        firstpokemonmoves.append(move13)
                        move13found = 1
                        break
                if move13found == 0:
                    for i in range(findmove13):
                        move13 = input("Try again ")
                    for i in range(len(data)):
                        if move13 in (data[firstpokemonnumber]["Learnable Moves"]):
                            firstpokemonmoves.append(move13)
                            break
                    else:
                        findmove13 += 1
        if move13 in firstpokemonmoves:
            firstpokemonmoves.remove(move13)
            for i in range(findnewmove2):
                move13 = input("Choose a move that you haven't chosen yet ")
                if move13 in firstpokemonmoves: 
                    findnewmove2 += 1
                firstpokemonmoves.append(move13)
        for i in range(len(data)):
            if firstpokemon == (data[i]["Name"]):
                move14 = input("Choose a learnable move ")
                for i in range(len(data[firstpokemonnumber]["Learnable Moves"])):
                    if move14 in (data[firstpokemonnumber]["Learnable Moves"]):
                        firstpokemonmoves.append(move14)
                        move14found = 1
                        break
                if move14found == 0:
                    for i in range(findmove14):
                        move14 = input("Try again ")
                    for i in range(len(data)):
                        if move14 in (data[firstpokemonnumber]["Learnable Moves"]):
                            firstpokemonmoves.append(move14)
                            break
                    else:
                        findmove14 += 1
        if move14 in firstpokemonmoves:
            firstpokemonmoves.remove(move14)
            for i in range(findnewmove3):
                move14 = input("Choose a move that you haven't chosen yet ")
                if move14 in firstpokemonmoves: 
                    findnewmove3 += 1
                firstpokemonmoves.append(move14)
        print(firstpokemonmoves)
        secondpokemon = input("What pokemon do you want on your team? ")
        for i in range(len(data)):
            if secondpokemon == (data[i]["Name"]):
                playerteam.append(secondpokemon)
                pokemonfound2 = 1
                break
        if pokemonfound2 == 0:
            for i in range(findnewpokemon2):
                secondpokemon = input("try again ")
                for i in range(len(data)):
                    if secondpokemon == (data[i]["Name"]):
                        playerteam.append(secondpokemon)
                    else:
                        findnewpokemon2 += 1
        for i in range(len(data)):
            if secondpokemon == (data[i]["Name"]):
                print(data[i]["Learnable Moves"])
                move21 = input("Choose a learnable move ")
                secondpokemonmoves.append(move21)
                move22 = input("Choose a learnable move ")
                if move22 in secondpokemonmoves:
                    for i in range(findnewmove4):
                        move22 = input("Choose a move that you haven't chosen yet ")
                        if move22 in secondpokemonmoves: 
                            findnewmove4 += 1
                secondpokemonmoves.append(move22)
                move23 = input("Choose a learnable move ")
                if move23 in secondpokemonmoves:
                    for i in range(findnewmove5):
                        move23 = input("Choose a move that you haven't chosen yet ")
                        if move23 in secondpokemonmoves: 
                            findnewmove5 += 1
                secondpokemonmoves.append(move23)
                move24 = input("Choose a learnable move ")
                if move24 in secondpokemonmoves:
                    for i in range(findnewmove6):
                        move24 = input("Choose a move that you haven't chosen yet ")
                        if move24 in secondpokemonmoves: 
                            findnewmove6 += 1
                secondpokemonmoves.append(move24)
        print(secondpokemonmoves)
        thirdpokemon = input("What pokemon do you want on your team? ")
        for i in range(len(data)):
            if thirdpokemon == (data[i]["Name"]):
                playerteam.append(thirdpokemon)
                pokemonfound3 = 1
                break
        if pokemonfound3 == 0:
            for i in range(findnewpokemon3):
                thirdpokemon = input("try again ")
                for i in range(len(data)):
                    if thirdpokemon == (data[i]["Name"]):
                        playerteam.append(thirdpokemon)
                    else:
                        findnewpokemon3 += 1
        for i in range(len(data)):
            if thirdpokemon == (data[i]["Name"]):
                print(data[i]["Learnable Moves"])
                move31 = input("Choose a learnable move ")
                thirdpokemonmoves.append(move31)
                move32 = input("Choose a learnable move ")
                if move32 in thirdpokemonmoves:
                    for i in range(findnewmove7):
                        move32 = input("Choose a move that you haven't chosen yet ")
                        if move32 in thirdpokemonmoves: 
                            findnewmove7 += 1
                thirdpokemonmoves.append(move12)
                move33 = input("Choose a learnable move ")
                if move33 in thirdpokemonmoves:
                    for i in range(findnewmove8):
                        move33 = input("Choose a move that you haven't chosen yet ")
                        if move33 in thirdpokemonmoves: 
                            findnewmove8 += 1
                thirdpokemonmoves.append(move33)
                move34 = input("Choose a learnable move ")
                if move34 in thirdpokemonmoves:
                    for i in range(findnewmove9):
                        move34 = input("Choose a move that you haven't chosen yet ")
                        if move34 in thirdpokemonmoves: 
                            findnewmove9 += 1
                thirdpokemonmoves.append(move34)
        print(thirdpokemonmoves)
        fourthpokemon = input("What pokemon do you want on your team? ")
        for i in range(len(data)):
            if fourthpokemon == (data[i]["Name"]):
                playerteam.append(fourthpokemon)
                pokemonfound4 = 1
                break
        if pokemonfound4 == 0:
            for i in range(findnewpokemon4):
                fourthpokemon = input("try again ")
                for i in range(len(data)):
                    if fourthpokemon == (data[i]["Name"]):
                        playerteam.append(fourthpokemon)
                    else:
                        findnewpokemon4 += 1
        for i in range(len(data)):
            if fourthpokemon == (data[i]["Name"]):
                print(data[i]["Learnable Moves"])
                move41 = input("Choose a learnable move ")
                fourthpokemonmoves.append(move41)
                move42 = input("Choose a learnable move ")
                if move42 in fourthpokemonmoves:
                    for i in range(findnewmove10):
                        move42 = input("Choose a move that you haven't chosen yet ")
                        if move42 in fourthpokemonmoves: 
                            findnewmove10 += 1
                fourthpokemonmoves.append(move42)
                move43 = input("Choose a learnable move ")
                if move43 in fourthpokemonmoves:
                    for i in range(findnewmove11):
                        move43 = input("Choose a move that you haven't chosen yet ")
                        if move43 in fourthpokemonmoves: 
                            findnewmove11 += 1
                fourthpokemonmoves.append(move43)
                move44 = input("Choose a learnable move ")
                if move44 in fourthpokemonmoves:
                    for i in range(findnewmove12):
                        move44 = input("Choose a move that you haven't chosen yet ")
                        if move44 in fourthpokemonmoves: 
                            findnewmove12 += 1
                fourthpokemonmoves.append(move44)
        print(fourthpokemonmoves)
        fifthpokemon = input("What pokemon do you want on your team? ")
        for i in range(len(data)):
            if fifthpokemon == (data[i]["Name"]):
                playerteam.append(fifthpokemon)
                pokemonfound5 = 1
                break
        if pokemonfound5 == 0:
            for i in range(findnewpokemon5):
                fifthpokemon = input("try again ")
                for i in range(len(data)):
                    if fifthpokemon == (data[i]["Name"]):
                        playerteam.append(fifthpokemon)
                    else:
                        findnewpokemon5 += 1
        for i in range(len(data)):
            if fifthpokemon == (data[i]["Name"]):
                print(data[i]["Learnable Moves"])
                move51 = input("Choose a learnable move ")
                fifthpokemonmoves.append(move51)
                move52 = input("Choose a learnable move ")
                if move52 in fifthpokemonmoves:
                    for i in range(findnewmove13):
                        move52 = input("Choose a move that you haven't chosen yet ")
                        if move52 in fifthpokemonmoves: 
                            findnewmove13 += 1
                fifthpokemonmoves.append(move52)
                move53 = input("Choose a learnable move ")
                if move53 in fifthpokemonmoves:
                    for i in range(findnewmove14):
                        move53 = input("Choose a move that you haven't chosen yet ")
                        if move53 in fifthpokemonmoves: 
                            findnewmove14 += 1
                fifthpokemonmoves.append(move43)
                move54 = input("Choose a learnable move ")
                if move54 in fifthpokemonmoves:
                    for i in range(findnewmove15):
                        move54 = input("Choose a move that you haven't chosen yet ")
                        if move54 in fifthpokemonmoves: 
                            findnewmove15 += 1
                fifthpokemonmoves.append(move54)
        print(fifthpokemonmoves)
        sixthpokemon = input("What pokemon do you want on your team? ")
        for i in range(len(data)):
            if sixthpokemon == (data[i]["Name"]):
                playerteam.append(sixthpokemon)
                pokemonfound6 = 1
                break
        if pokemonfound6 == 0:
            for i in range(findnewpokemon6):
                sixthpokemon = input("try again ")
                for i in range(len(data)):
                    if sixthpokemon == (data[i]["Name"]):
                        playerteam.append(sixthpokemon)
                    else:
                        findnewpokemon6 += 1
        for i in range(len(data)):
            if sixthpokemon == (data[i]["Name"]):
                print(data[i]["Learnable Moves"])
                move61 = input("Choose a learnable move ")
                sixthpokemonmoves.append(move61)
                move62 = input("Choose a learnable move ")
                if move62 in sixthpokemonmoves:
                    for i in range(findnewmove16):
                        move62 = input("Choose a move that you haven't chosen yet ")
                        if move62 in sixthpokemonmoves: 
                            findnewmove16 += 1
                sixthpokemonmoves.append(move62)
                move63 = input("Choose a learnable move ")
                if move63 in sixthpokemonmoves:
                    for i in range(findnewmove17):
                        move63 = input("Choose a move that you haven't chosen yet ")
                        if move63 in sixthpokemonmoves: 
                            findnewmove17 += 1
                sixthpokemonmoves.append(move63)
                move64 = input("Choose a learnable move ")
                if move64 in sixthpokemonmoves:
                    for i in range(findnewmove18):
                        move64 = input("Choose a move that you haven't chosen yet ")
                        if move64 in sixthpokemonmoves: 
                            findnewmove18 += 1
                sixthpokemonmoves.append(move64)
        print(sixthpokemonmoves)
        teamandmoves = (playerteam[0], firstpokemonmoves, playerteam[1], secondpokemonmoves, playerteam[2], thirdpokemonmoves, playerteam[3], fourthpokemonmoves, playerteam[4], fifthpokemonmoves, playerteam[5], sixthpokemon)
        print(teamandmoves)
    teambuilder()
            
