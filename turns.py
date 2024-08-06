import json

import time
from tryingtofix import Teambuilder
times = 1.5
import random
import decimal
from decimal import Decimal
#global turn
#turn = 1
#going = "You"

test = open("moves.json", encoding="utf8")
moves = json.load(test)
movelist = len(moves)

quiz = open("data.json", encoding="utf8")
data = json.load(quiz)
pokemonlist = len(data)

pluh = open("playerteaminfo.json", encoding="utf8")
inputteam = json.load(pluh)
inputteamlist = len(inputteam)
global unique
unique = ["nah", "id", "win"]
typeeffect = ["Surfer", "Rosa"]
global stab
stab = False
global meffective1
meffective1 = 1
global meffective2
meffective2 = 1
global meffective
meffective = 1
global twotype
twotype = False
global onetype
onetype = False

global pokemonin
pokemonin = "same"
global enemyin
enemyin = "same"
global itch
itch = False
global Kaifat
Kaifat = "very"
global enemytypes

global N
N = 1
global M
M = 1

global evasive
evasive = 0
global enemyevasive
enemyevasive = 0

#enemyhealth = 200
#Pokemon.teambuilder()

#global enemypokemon
global enemyspeed
global enemyhealth
enemypokemon = "Raichu"

for i in range(len(data)):
    if enemypokemon == data[i]["Name"]:
        enemyspeed = data[i]["Speed Stat"]
        enemyhealth = data[i]["Health Stat"]
tb = Teambuilder()
tb.teambuilder()
pluh = open("playerteaminfo.json", encoding="utf8")
inputteam = json.load(pluh)
inputteamlist = len(inputteam)
enemyparty = ["Raichu", ["Toxic", "Double Team", "Thunderbolt", "Surf"]]
yourteam = [inputteam[0], inputteam[2], inputteam[4], inputteam[6], inputteam[8], inputteam[10]]
userpartystatus = [inputteam[0], "none", inputteam[2], "none", inputteam[4], "none", inputteam[6], "none", inputteam[8], "none", inputteam[10], "none"]
eliteteamstatus = ["Raichu", "none", "Dragonite", "none", "Charizard", "none", "Gengar", "none", "Blastoise", "none", "Machamp", "none"]
for i in range(pokemonlist):
    if inputteam[0] == data[i]["Name"]:
        global firstpkhealth
        firstpkhealth = data[i]["Health Stat"]
    if inputteam[2] == data[i]["Name"]:
        global secondpkhealth
        secondpkhealth = data[i]["Health Stat"]
    if inputteam[4] == data[i]["Name"]:
        global thirdpkhealth
        thirdpkhealth = data[i]["Health Stat"]
    if inputteam[6] == data[i]["Name"]:
        global fourthpkhealth
        fourthpkhealth = data[i]["Health Stat"]
    if inputteam[8] == data[i]["Name"]:
        global fifthpkhealth
        fifthpkhealth = data[i]["Health Stat"]
    if inputteam[10] == data[i]["Name"]:
        global sixthpkhealth
        sixthpkhealth = data[i]["Health Stat"]
userpartyhealth = [inputteam[0], firstpkhealth, inputteam[2], secondpkhealth, inputteam[4], thirdpkhealth, inputteam[6], fourthpkhealth, inputteam[8], fifthpkhealth, inputteam[10], sixthpkhealth]
enemypartyhealth = ["Raichu", 230]
firstpokemon = inputteam[0]
global currentpokemon
currentpokemon = firstpokemon
global currentspeed
global currenthealth
for i in range(len(data)):
    if currentpokemon == data[i]["Name"]:
        currentspeed = data[i]["Speed Stat"]
        currenthealth = data[i]["Health Stat"]
pknumber = [1]
playerteam = []
pokemonmoves = []
allpokemon = []
for i in range(len(data)):
            allpokemon.append(data[i]["Name"])



yourdeadguys = []
Mikesdeadguys = []
#yourteam = [teaminfo[0], teaminfo[2], teaminfo[4], teaminfo[6], teaminfo[8], teaminfo[10]]
currentpokemon = yourteam[0]    




pokemonin = "same"

enemyin = "same"


#enemyhealth = 200
#Pokemon.teambuilder()


#enemypokemon = "Raichu"
#enemypokemon = enemypokemon






class functionality():
    def oppositehealththing(going, enemyhealth, currenthealth):
        global oppositehealth
        if going == "User":
            oppositehealth = enemyhealth
        if going == "Enemy":
            oppositehealth = currenthealth


    def oppositepokemon(going, currentpokemon, enemypokemon):
        global oppositepokemon
        if going == "User":
            oppositepokemon = enemypokemon
        if going == "Enemy":
            oppositepokemon = currentpokemon

    def afflicted(Near, Mello, currenthealth, currentpokemon):
        global enemyhealth
        global Afterhealth

        global N
        global M

        #10% chance to wear off
        cure = random.randrange(10)
        enemycure = random.randrange(10)
        print(cure, enemycure, "cure, enemycure")
        
        
        Afterhealth = currenthealth
        for i in range(len(userpartystatus)):
            if currentpokemon == userpartystatus[i - 1]:

                if userpartystatus[i] == "Poison":
                    if cure != 1:
                        
                        for i in range(pokemonlist):
                            if currentpokemon == data[i]["Name"]:
                                startinghealth = data[i]["Health Stat"]
                        BigD = Near * startinghealth/16
                        damage = round(BigD)
                        if damage == currenthealth or damage > currenthealth:
                            damage = currenthealth
                        Afterhealth -= damage
                        time.sleep(1)
                        print(currentpokemon, "took", damage, "damage due to Poison")
                        time.sleep(1)
                        print(currentpokemon, "has", Afterhealth, "health left")
                        Near += 1
                        N = Near
                        #print(N)
                        
                        time.sleep(1)
                        #return Afterhealth
                    if cure == 1:
                        for i in range(len(userpartystatus)):
                            if currentpokemon == userpartystatus[i - 1]:
                                userpartystatus[i] = "None"
                                print(currentpokemon, "was cured of its poison!")
                                N = 1

        
        for i in range(len(eliteteamstatus)):
                
            if enemypokemon == eliteteamstatus[i - 1]:
                    
                if eliteteamstatus[i] == "Poison":
                    if enemycure != 1:

                        for i in range(pokemonlist):
                            if enemypokemon == data[i]["Name"]:
                                enemystartinghealth = data[i]["Health Stat"]
                        BigE = Mello * enemystartinghealth/16
                        damage = round(BigE)
                        if damage == enemyhealth or damage > enemyhealth:
                            damage = enemyhealth
                        enemyhealth = enemyhealth - damage
                        time.sleep(1)
                        print(enemypokemon, "took", damage, "damage due to Poison")
                        time.sleep(1)
                        print(enemypokemon, "has", enemyhealth, "health left")
                        Mello += 1
                        M = Mello
                        time.sleep(1)
                    if enemycure == 1:
                        for i in range(len(eliteteamstatus)):
                            if enemypokemon == eliteteamstatus[i - 1]:
                                eliteteamstatus[i] = "None"
                                print(enemypokemon, "was cured of its poison!")
                                M = 1
    
    def Paralyze(persongoing):
        pchance = random.randrange(3)
        clickclak = random.randrange(4)

        

        global youPAR
        global enemyPAR
        youPAR = "no"
        enemyPAR = "no"
        for i in range(len(userpartystatus)):
            if currentpokemon == userpartystatus[i-1]:
                if userpartystatus[i] == "Paralyzed":
                    if pchance == 1:
                         youPAR = "yes"
                    
        for i in range(len(eliteteamstatus)):
            if enemypokemon == eliteteamstatus[i-1]:
                if eliteteamstatus[i] == "Paralyzed":
                    print(clickclak, "p number")
                    if clickclak == 1:
                        enemyPAR = "yes"
    def Imatired(going):
        global yousleep
        global enemysleep
        print("running")

        memememe = random.randrange(4)
        monke = random.randrange(2)

        for i in range(len(userpartystatus)):
            if currentpokemon == userpartystatus[i-1]:
                if userpartystatus[i] != "Asleep":
                    yousleep = "no"
        for i in range(len(eliteteamstatus)):
            if enemypokemon == eliteteamstatus[i-1]:
                if eliteteamstatus[i] != "Asleep":
                    enemysleep = "no"
        
        if going == "User":
            for i in range(len(userpartystatus)):
                if currentpokemon == userpartystatus[i-1]:
                    if userpartystatus[i] == "Asleep":
                        if memememe != 1:
                            yousleep = "yes"
                        if memememe == 1:
                            yousleep = "no"
                            for i in range(len(userpartystatus)):
                                if currentpokemon == userpartystatus[i-1]:
                                    userpartystatus[i] = "None"
                            print(currentpokemon,"woke up!")

        if going == "Enemy":            
            for i in range(len(eliteteamstatus)):
                if enemypokemon == eliteteamstatus[i-1]:
                    if eliteteamstatus[i] == "Asleep":
                        print(monke, "sleep number")
                        if monke != 1:
                            enemysleep = "yes"
                        if monke == 1:
                            enemysleep = "no"
                            for i in range(len(eliteteamstatus)):
                                if enemypokemon == eliteteamstatus[i-1]:
                                    eliteteamstatus[i] = "None"
                            print(enemypokemon,"woke up!")

    def coldgaming(going):
        global youcold
        global enemycold
        print("cold running")

        brrr = random.randrange(4)
        uk = random.randrange(2)

        for i in range(len(userpartystatus)):
            if currentpokemon == userpartystatus[i-1]:
                if userpartystatus[i] != "Frozen":
                    youcold = "no"
        for i in range(len(eliteteamstatus)):
            if enemypokemon == eliteteamstatus[i-1]:
                if eliteteamstatus[i] != "Frozen":
                    enemycold = "no"
        
        if going == "User":
            for i in range(len(userpartystatus)):
                if currentpokemon == userpartystatus[i-1]:
                    if userpartystatus[i] == "Frozen":
                        if brrr != 1:
                            youcold = "yes"
                        if brrr == 1:
                            youcold = "no"
                            for i in range(len(userpartystatus)):
                                if currentpokemon == userpartystatus[i-1]:
                                    userpartystatus[i] = "None"
                            print(currentpokemon,"thawed out!")
        if going == "Enemy":            
            for i in range(len(eliteteamstatus)):
                if enemypokemon == eliteteamstatus[i-1]:
                    if eliteteamstatus[i] == "Frozen":
                        print(uk, "freeze number")
                        if uk != 1:
                            enemycold = "yes"
                        if uk == 1:
                            enemycold = "no"
                            for i in range(len(eliteteamstatus)):
                                if enemypokemon == eliteteamstatus[i-1]:
                                    eliteteamstatus[i] = "None"
                            print(enemypokemon,"thawed out!")                
            
                    
    def Confuse(persongoing, goingsdamage):
        global currenthealth
        global enemyhealth

        global hityourself
        global enemyhititself
        print("bruh")
        print(persongoing, "person going")
        bruh = random.randrange(2)
        uh = random.randrange(2)

        lost = random.randrange(6)
        found = random.randrange(3)

        if persongoing == currentpokemon:
            for i in range(len(userpartystatus)):
                if currentpokemon == userpartystatus[i -1]:
                    if userpartystatus[i] == "Confused":
                        if lost != 1:
                        
                            print("uh")
                            if uh == 1 or uh == 0:
                                hityourself = "yes"
                                print(currentpokemon,"hit itself in its confusion!")
                                time.sleep(1)
                                print("Plus L")
                                time.sleep(0.5)
                                print("Plus Ratio")
                                time.sleep(times)
                                print(currentpokemon,"took", goingsdamage, "damage")
                                time.sleep(0.5)
                        if lost == 1:
                            for i in range(len(userpartystatus)):
                                if currentpokemon == userpartystatus[i -1]:
                                    userpartystatus[i] = "None"
                            print(currentpokemon, "snapped out of its confusion!")

        if persongoing == enemypokemon:
            for i in range(len(eliteteamstatus)):
                if enemypokemon == eliteteamstatus[i - 1]:
                    if eliteteamstatus[i] == "Confused":
                        if found != 1:
                        
                            print(bruh)
                            if bruh == 1:
                                enemyhititself = "yes"
                                print(enemypokemon,"hit itself in its confusion!")
                            
                                time.sleep(times)
                                print(enemypokemon,"took", goingsdamage, "damage")
                                time.sleep(0.5)
                        if found == 1:
                            for i in range(len(eliteteamstatus)):
                                if enemypokemon == eliteteamstatus[i - 1]:
                                    eliteteamstatus[i] = "None"
                            print(enemypokemon,"snapped out of its confusion!")

                                
        
        

    def Flinch(chance, going, goingfirst):
        global Flinching
        Flinching = "no"
        Laith = random.randrange(chance)
        
        if Laith == 1:
            if going == "User":
                if goingfirst == "User":
                    Flinching = "yes"

    def hedobetrapped(startingturntrapped,Trappedturns,turn):
        global Trapped
        if Trapped == "yes":
            sofar = turn - startingturntrapped
            print(sofar, turn, startingturntrapped, "sofar, turn, startingturn")
            print(Trappedturns, "trapped turns")

            if sofar == Trappedturns or sofar > Trappedturns:
                
                Trapped = "no"
                print(enemypokemon, "is no longer trapped")

    def FlyandDiggimmick(currentpokemon):
        global Kaifat
        global awaybeforehit
        if awaybeforehit == "yes":
            if turn - 1 == leavingturn:
                global itsfly
                global itsdig

                if itsfly == "yes":
                    use = "Fly"
                if itsdig == "yes":
                    use = "Dig"

                global unique
                global meffective
                global meffective1
                global meffective2
                global onetype
                global twotype
                global movedamage
                global uniquedamage
                

                global Diditmiss
                Diditmiss = "no"
                global runspecial
                runspecial = "yes"

                global PrintPoison
                global DoDamage
                global EnemyPoisoned

                PrintPoison = "no"
                DoDamage = "yes"
                EnemyPoisoned = "no"

                global Afterhealth
                Afterhealth = 0
                
                global shouldiswitch
                shouldiswitch = "no"
                global goingfirst
                goingfirst = "ABBA"

                global Diduniquedamagehappen
                Diduniquedamagehappen = "no"

                global Didithittwice
                Didithittwice = "no"

                global fourtydamagetrue
                fourtydamagetrue = "no"

                global itcounter
                global counterdamage
                itcounter = "no"

                global Flinching
                Flinching = "no"

                global PrintBurn
                PrintBurn = "no"
                global EnemyBurn
                EnemyBurn = "no"

                global Trappedturns
                global Trapped
                Trapped = "no"
                global startingturntrapped
                Trappedturns = 0
                startingturntrapped = 0
                awaybeforehit = "no"
                Turns.speedcheck(enemyspeed, currentspeed)
                if goingfirst == "User":
                    global enemyhealth
                    
                    going = "User"
                    print(currentpokemon,"used", use)
                    functionality.damagecalc("bruh",use, currentpokemon, enemypokemon)
                    damage = movedamage
                    functionality.Miss(use,evasive, enemyevasive, going)
                    if damage == enemyhealth or damage > enemyhealth:
                        damage = enemyhealth

                    if Diditmiss != "no":
                        damage = 0
                        if DoDamage == "yes":
                            print("But it missed!")
                        DoDamage = "no"
                        

                    time.sleep(1)
                    if typesuper1 == True or typesuper2 == True or typesuper == True:
                        print("It was supereffective!")
                        time.sleep(0.5)
                        print("It did", damage, "damage")
                    if crithappen == True:
                        print("It was a critical hit!")
                        time.sleep(0.5)

                    
                    enemyhealth = enemyhealth - damage
                    print("It did", damage, "damage")
                    time.sleep(times)
                    if enemyhealth > 0:
                        print(enemypokemon, "has", enemyhealth, "health left")
                                #print(enemypokemon)
                    if enemyhealth == 0:
                        print(enemypokemon, "fainted")
                    enemypartyhealth[1] = enemyhealth
                        
                    functionality.Mikesdeadpks(enemyhealth, currentpokemon)
                        #print(enemypokemon)
                    if len(Mikesdeadguys) == 6:
                        Kaifat = "no"
                    going = "Enemy"
                    Schmovin.Whosmovin(enemypokemon,currentpokemon)
                            #Mike.Raichudoing(turn)
                    functionality.damagecalc("bruh",enemymove, enemypokemon, currentpokemon)
                    functionality.Miss(enemymove,evasive, enemyevasive, going)
                    if runspecial == "yes":
                        functionality.specialeffect("bruh",enemymove,damage,enemyspeed,currentspeed,enemypokemon,currentpokemon, going, "placeholder", turn, enemyhealth)
                    if Diduniquedamagehappen != "no":
                        movedamage = uniquedamage

                    if Didithittwice != "no":
                        movedamage = TwoHitDamage

                    if fourtydamagetrue != "no":
                        movedamage = 40

                    if itcounter != "no":
                        movedamage = counterdamage


                            #effects end here

                    enemydamage = movedamage
                    for i in range(len(userpartyhealth)):
                        if currentpokemon == userpartyhealth[i - 1]:
                            currenthealth = userpartyhealth[i]
                            #print(currenthealth, "after calc")
                            #for i in range(len(userpartyhealth)):
                            #   if currentpokemon == userpartyhealth[i - 1]:
                            #      currenthealth = userpartyhealth[i]
                            #print(enemydamage, "enemydamage after damage calc")
                    if enemydamage == currenthealth or enemydamage > currenthealth:
                        enemydamage = currenthealth
                                #print(enemydamage, "enemydamage after == or > than")
                    print(enemypokemon, "used", enemymove)
                    time.sleep(times)

                    if Diditmiss != "no":
                        enemydamage = 0
                        if DoDamage == "yes":
                            print("But it missed!")
                        DoDamage = "no"
                        
                        if enemymove == "Hi Jump Kick" or use == "Jump Kick":
                            functionality.damagecalc(enemymove, enemypokemon, currentpokemon)
                            enemydamage = movedamage
                            enemyhealth = enemyhealth - enemydamage
                            print(enemypokemon, "took", enemydamage, "damage due to recoil")
                            print(enemypokemon, "has", enemyhealth, "health left")
                        enemydamage = 0
                    time.sleep(1)
                    if typesuper1 == True or typesuper2 == True or typesuper == True:
                        print("It was supereffective!")
                        time.sleep(0.5)
                    print(enemypokemon, "did", enemydamage, "damage")
                    if crithappen == True:
                        print("It was a critical hit!")
                        time.sleep(0.5)
                                
                            #health already reset at this point
                    currenthealth -= enemydamage
                            #print(currenthealth, "after")

                    if Flinching != "no":
                        print(enemypokemon, "flinched and couldn't move")
                    time.sleep(times)
                    print(currentpokemon, "has", currenthealth, "health left")
                    #here down = deaD
                    userpartyhealth[i] = currenthealth
                    if currenthealth == 0:
                        for i in range(len(yourteam)-1):
                            if currentpokemon == yourteam[i]:
                                yourteam.remove(currentpokemon)
                        print(yourteam)
                        newpk = input("Who will you switch into? ")
                        for i in range(len(yourteam)):
                            if newpk == yourteam[i]:
                                currentpokemon = newpk
                        for i in range(len(userpartyhealth)):
                            if currentpokemon == userpartyhealth[i - 1]:
                                currenthealth = userpartyhealth[i]

                    #print(currenthealth, "before afflicted")
                    functionality.afflicted(N,M, currenthealth, currentpokemon)
                    functionality.Crispy(currentpokemon)

                    functionality.Mikesdeadpks(enemyhealth, currentpokemon)

                    for i in range(len(userpartystatus)):
                        if currentpokemon == userpartystatus[i - 1]:
                            if userpartystatus[i] == "Poison":
                                currenthealth = Afterhealth
                    
                                #print(currenthealth, "after afflicted")
                                #print(Afterhealth, "after afflicted")
                                #dead below
                                for i in range(len(userpartyhealth)):
                                    if currentpokemon == userpartyhealth[i - 1]:
                                        userpartyhealth[i] = Afterhealth
                if goingfirst == "Enemy":
                    
                    
                    time.sleep(times)

                    going = "User"

                    if itcounter == "yes":
                        for i in range(pokemonlist):
                            if data[i]["Name"] == currentpokemon:
                                currentspeed == data[i]["Speed Stat"]


                    PrintPoison = "no"
                    DoDamage = "yes"
                    EnemyPoisoned = "no"
                    shouldiswitch = "no"
                    goingfirst = "ABBA"
                    Diduniquedamagehappen = "no"
                    Didithittwice = "no"
                    fourtydamagetrue = "no"
                    itcounter = "no"
                    Diditmiss = "no"
                    runspecial = "yes"
                    Flinching = "no"
                    PrintBurn = "no"
                    EnemyBurn = "no"
                    

                    print("You used", use)
                    time.sleep(times)
                    # if move effect != None
                    #Do effect
                    f = functionality()
                    
                    functionality.damagecalc("bruh",use, currentpokemon, enemypokemon)
                    damage = movedamage
                    functionality.Miss(use,evasive, enemyevasive, going)
                        
                    
                        

                    if damage == enemyhealth or damage > enemyhealth:
                        damage = enemyhealth

                    if Diditmiss != "no":
                        damage = 0
                        if DoDamage == "yes":
                            print("But it missed!")
                        DoDamage = "no"
                        
                        if use == "Hi Jump Kick" or use == "Jump Kick":
                            functionality.damagecalc("bruh",use, currentpokemon, enemypokemon)
                            damage = movedamage
                            currenthealth = currenthealth - damage
                            print(currentpokemon, "took", damage, "damage due to recoil")
                            print(currentpokemon, "has", currenthealth, "health left")
                        damage = 0
                    
                    

                    if DoDamage == "yes":
                        functionality.Confuse(currentpokemon, damage)
                        if hityourself == "no":
                            time.sleep(1)
                            if typesuper1 == True or typesuper2 == True or typesuper == True:
                                print("It was supereffective!")
                                time.sleep(0.5)
                            print(currentpokemon, "did", damage, "damage")
                            if crithappen == True:
                                print("It was a critical hit!")
                                time.sleep(0.5)

                            enemyhealth = enemyhealth - damage
                    time.sleep(times)
                    if enemyhealth > 0:
                        print(enemypokemon, "has", enemyhealth, "health left")
                    if enemyhealth == 0:
                        print(enemypokemon, "fainted")
                    enemypartyhealth[1] = enemyhealth
                    functionality.Mikesdeadpks(enemyhealth, currentpokemon)
                    #print(enemypokemon)

                    for i in range(len(userpartyhealth)):
                        if currentpokemon == userpartyhealth[i - 1]:
                            currenthealth = userpartyhealth[i]

                    functionality.afflicted(N,M, currenthealth, currentpokemon)
                    functionality.Crispy(currentpokemon)

                    functionality.Mikesdeadpks(enemyhealth, currentpokemon)

                    for i in range(len(userpartystatus)):
                        if currentpokemon == userpartystatus[i - 1]:
                            if userpartystatus[i] == "Poison":
                                
                                currenthealth = Afterhealth
                    
                                #print(currenthealth, "after afflicted")
                                #print(Afterhealth, "after afflicted")
                                #dead below
                                for i in range(len(userpartyhealth)):
                                    if currentpokemon == userpartyhealth[i - 1]:
                                        userpartyhealth[i] = Afterhealth
                                

                    PrintPoison = "no"
                    DoDamage = "yes"
                    EnemyPoisoned = "no"
                    shouldiswitch = "no"
                    goingfirst = "ABBA"
                    Diduniquedamagehappen = "no"
                    Didithittwice = "no"
                    fourtydamagetrue = "no"
                    itcounter = "no"
                    Diditmiss = "no"
                    runspecial = "yes"
                    Flinching = "no"
                    PrintBurn = "no"
                    EnemyBurn = "no"
                    

                    if currenthealth == 0:
                        for i in range(len(yourteam)):
                            if currentpokemon == yourteam[i]:
                                yourteam.remove(i)
                        print(yourteam)
                        newpk = input("Who will you switch into? ")
                        for i in range(len(yourteam)):
                            if newpk == yourteam[i]:
                                currentpokemon = newpk
                        for i in range(len(userpartyhealth)):
                            if currentpokemon == userpartyhealth[i - 1]:
                                currenthealth = userpartyhealth[i]

                    functionality.hedobetrapped(startingturntrapped,Trappedturns,turn)

                    if len(Mikesdeadguys) == 6:
                        Kaifat = "no"

                itsfly = "no"
                itsdig = "no"
                
    def keepusing(usingturn, gooblie):
        global lockedin
        global usedturn
        
        if lockedin == "yes" or enemylockedin == "yes":
            if turn - gooblie == usedturn:
                if lockedin == "yes":
                    for i in range(len(userpartystatus)):
                        if currentpokemon == userpartystatus[i-1]:
                            userpartystatus[i] == "Confused"
                    lockedin = "no"
                    usedturn = 0
                    print(currentpokemon,"has become confused")
                if enemylockedin == "yes":
                    for i in range(len(eliteteamstatus)):
                        if enemypokemon == eliteteamstatus[i-1]:
                            eliteteamstatus[i] == "Confused"
                    enemylockedin == "no"
                    print(enemypokemon,"has become confused!")
                

            
            
            

    def Crispy(currentpokemon):
        global enemyhealth
        

        # burn also decreases attack stat so we gotta make something hapem
        #To the above, but what if we didnt?
      
        # 1 in 6 chance to cure
        cooloff = random.randrange(6)
        enemycool = random.randrange(6)


        for i in range(len(userpartystatus)):
            if currentpokemon == userpartystatus[i - 1]:

                if userpartystatus[i] == "Burn":
                    if cooloff != 1:
                    
                        for i in range(pokemonlist):
                            if currentpokemon == data[i]["Name"]:
                                currentpkstartinghp = data[i]["Health Stat"]

                        for i in range(len(userpartyhealth)):
                            if currentpokemon == userpartyhealth[i - 1]:
                                currenthealth = userpartyhealth[i]

                        ahhthatshot = currentpkstartinghp/8

                        damage = round(ahhthatshot)
                        if damage == currenthealth or damage > currenthealth:
                            damage = currenthealth
                        currenthealth -= damage

                        time.sleep(1)
                        print(currentpokemon, "took", damage, "damage due to its burn")
                        time.sleep(1)
                        print(currentpokemon, "has", currenthealth, "health left")
                        for i in range(len(userpartyhealth)):
                            if currentpokemon == userpartyhealth[i - 1]:
                                userpartyhealth[i] = currenthealth
                        #print(N)
                        
                        time.sleep(1)
                        #return Afterhealth
                    if cooloff == 1:
                        for i in range(len(userpartystatus)):
                            if currentpokemon == userpartystatus[i-1]:
                                userpartystatus[i] = "None"
                                print(currentpokemon, "healed its burn!")


        for i in range(len(eliteteamstatus)):
            
            if enemypokemon == eliteteamstatus[i - 1]:
                
                if eliteteamstatus[i] == "Burn":
                    if enemycool != 1:
                        for i in range(pokemonlist):
                            if enemypokemon == data[i]["Name"]:
                                enemystartinghealth = data[i]["Health Stat"]
                        BigEburn = enemystartinghealth/16
                        damage = round(BigEburn)
                        if damage == enemyhealth or damage > enemyhealth:
                            damage = enemyhealth
                        enemyhealth = enemyhealth - damage
                        time.sleep(1)
                        print(enemypokemon, "took", damage, "damage due to its Burn")
                        time.sleep(1)
                        print(enemypokemon, "has", enemyhealth, "health left")
                        
                        time.sleep(1)
                    if enemycool == 1:
                        for i in range(len(eliteteamstatus)):
                                if enemypokemon == eliteteamstatus[i-1]:
                                    eliteteamstatus[i] = "None"
                                    print(enemypokemon, "healed its burn!")



    def speedstages(moveused, speed):
        global used
        global currentspeed
        currentspeed = speed
        used = moveused
        
        
        

        if used == "Counter":
            currentspeed = 10
            



    def dead(oppositehealth, oppositepokemon):
        if oppositehealth == 0:
            if going == "Enemy":
                global currentpokemon
                yourdeadguys.append(currentpokemon)

                print(oppositepokemon, "has fainted")

                print(yourteam)
                switchin = input("Pick a Pokemon to switch in: ")
                if switchin in yourdeadguys or switchin not in yourteam:
                    print(switchin, "has already fainted")
                    switchin = input("Pick a Pokemon to switch in to:")
                currentpokemon = switchin
            if going == "User":
                Mikesdeadguys.append(enemypokemon)
                #switch in good


    def supereffective(supereffective, use, ptype):
        global effective
        effective = "normal"
        for i in range(movelist):
            if (moves[i]["name"]) == use:
                usetype = (moves[i]["type"])
        #print(usetype, effective, "usetype effective in supereffective")
        #print(ptype, "ptype")



        if usetype == "Normal" and "Rock" == ptype or usetype == "Normal" and " Rock" == ptype:
            effective = "half"
        if usetype == "Normal" and "Ghost" == ptype or usetype == "Normal" and " Ghost" == ptype:
            effective = "zero"

        if usetype == "Fire" and "Fire" == ptype or usetype == "Fire" and " Fire" == ptype:
            effective = "half"
        if usetype == "Fire" and "Water" == ptype or usetype == "Fire" and " Water" == ptype:
            effective = "half"
        if usetype == "Fire" and "Grass" == ptype or usetype == "Fire" and " Grass" == ptype:
            effective = "super"
        if usetype == "Fire" and "Ice" == ptype or usetype == "Fire" and " Ice" == ptype:
            effective = "super"
        if usetype == "Fire" and "Bug" == ptype or usetype == "Fire" and " Bug" == ptype:
            effective = "super"
        if usetype == "Fire" and "Rock" == ptype or usetype == "Fire" and " Rock" == ptype:
            effective = "half"
        if usetype == "Fire" and "Dragon" == ptype or usetype == "Fire" and " Dragon" == ptype:
            effective = "half"

        if usetype == "Water" and "Fire" == ptype or usetype == "Water" and " Fire" == ptype:
            effective = "super"
        if usetype == "Water" and "Water" == ptype or usetype == "Water" and " Water" == ptype:
            effective = "half"
        if usetype == "Water" and "Grass" == ptype or usetype == "Water" and " Grass" == ptype:
            effective = "half"
        if usetype == "Water" and "Ground" == ptype or usetype == "Water" and " Ground" == ptype:
            effective = "super"
        if usetype == "Water" and "Rock" == ptype or usetype == "Water" and " Rock" == ptype:
            effective = "super"
        if usetype == "Water" and "Dragon" == ptype or usetype == "Water" and " Dragon" == ptype:
            effective = "half"

        if usetype == "Electric" and "Water" == ptype or usetype == "Electric" and " Water" == ptype:
            effective = "super"
        if usetype == "Electic" and "Electirc" == ptype or usetype == "Electric" and " Electric" == ptype:
            effective = "half"
        if usetype == "Electric" and "Grass" == ptype or usetype == "Electric" and " Grass" == ptype:
            effective = "half"
        if usetype == "Electric" and "Ground" == ptype or usetype == "Electric" and " Ground" == ptype:
            effective = "zero"
        if usetype == "Electric" and "Flying" == ptype or usetype == "Electric" and " Flying" == ptype:
            effective = "super"
        if usetype == "Electric" and "Dragon" == ptype or usetype == "Electric" and " Dragon" == ptype:
            effective = "half"

        if usetype == "Grass" and "Fire" == ptype or usetype == "Grass" and " Fire" == ptype:
            effective = "half"
        if usetype == "Grass" and "Water" == ptype or usetype == "Grass" and " Water" == ptype:
            effective = "super"
        if usetype == "Grass" and "Grass" == ptype or usetype == "Grass" and " Grass" == ptype:
            effective = "half"
        if usetype == "Grass" and "Poison" == ptype or usetype == "Grass" and " Poison" == ptype:
            effective = "half"
        if usetype == "Grass" and "Ground" == ptype or usetype == "Grass" and " Ground" == ptype:
            effective = "super"
        if usetype == "Grass" and "Flying" == ptype or usetype == "Grass" and " Flying" == ptype:
            effective = "half"
        if usetype == "Grass" and "Bug" == ptype or usetype == "Grass" and " Bug" == ptype:
            effective = "half"
        if usetype == "Grass" and "Rock" == ptype or usetype == "Grass" and " Rock" == ptype:
            effective = "super"
        if usetype == "Grass" and "Dragon" == ptype or usetype == "Grass" and " Dragon" == ptype:
            effective = "half"

        if usetype == "Ice" and "Fire" == ptype or usetype == "Ice" and " Fire" == ptype:
            effective = "half"
        if usetype == "Ice" and "Water" == ptype or usetype == "Ice" and " Water" == ptype:
            effective = "half"
        if usetype == "Ice" and "Grass" == ptype or usetype == "Ice" and " Grass" == ptype:
            effective = "super"
        if usetype == "Ice" and "Ice" == ptype or usetype == "Ice" and " Ice" == ptype:
            effective = "half"
        if usetype == "Ice" and "Ground" == ptype or usetype == "Ice" and " Ground" == ptype:
            effective = "super"
        if usetype == "Ice" and "Flying" == ptype or usetype == "Ice" and " Flying" == ptype:
            effective = "super"
        if usetype == "Ice" and "Dragon" == ptype or usetype == "ICe" and " Dragon" == ptype:
            effective = "super"

        if usetype == "Fighting" and "Normal" == ptype or usetype == "Fighting" and " Normal" == ptype:
            effective = "super"
        if usetype == "Fighting" and "Ice" == ptype or usetype == "Fighting" and " Ice" == ptype:
            effective = "super"
        if usetype == "Fighting" and "Poison" == ptype or usetype == "Fighting" and " Poison" == ptype:
            effective = "half"
        if usetype == "Fighting" and "Flying" == ptype or usetype == "Fighting" and " Flying" == ptype:
            effective = "half"
        if usetype == "Fighting" and "Psychic" == ptype or usetype == "Fighting" and " Psychic" == ptype:
            effective = "half"
        if usetype == "Fighting" and "Bug" == ptype or usetype == "Fighting" and " Flying" == ptype:
            effective = "half"
        if usetype == "Fighting" and "Rock" == ptype or usetype == "Fighting" and " Rock" == ptype:
            effective = "super"
        if usetype == "Fighting" and "Ghost" == ptype or usetype == "Figthing" and " Ghost" == ptype:
            effective = "zero"

        if usetype == "Poison" and "Grass" == ptype or usetype == "Poison" and " Grass" == ptype:
            effective = "super"
        if usetype == "Poison" and "Poison" == ptype or usetype == "Poison" and " Poison" == ptype:
            effective = "half"
        if usetype == "Poison" and "Ground" == ptype or usetype == "Poison" and " Ground" == ptype:
            effective = "half"
        if usetype == "Poison" and "Rock" == ptype or usetype == "Poison" and " Rock" == ptype:
            effective = "half"
        if usetype == "Poison" and "Ghost" == ptype or usetype == "Poison" and " Ghost" == ptype:
            effective = "half"

        if usetype == "Ground" and "Fire" == ptype or usetype == "Ground" and " Fire" == ptype:
            effective = "super"
        if usetype == "Ground" and "Electric" == ptype or usetype == "Ground" and " Electric" == ptype:
            effective = "super"
        if usetype == "Ground" and "Grass" == ptype or usetype == "Ground" and " Grass" == ptype:
            effective = "half"
        if usetype == "Ground" and "Poison" == ptype or usetype == "Ground" and " Poison" == ptype:
            effective == "super"
        if usetype == "Ground" and "Flying" == ptype or usetype == "Ground" and " Flying" == ptype:
            effective == "zero"
        if usetype == "Ground" and "Bug" == ptype or usetype == "Ground" and " Bug" == ptype:
            effective == "half"
        if usetype == "Ground" and "Rock" == ptype or usetype == "Ground" and " Rock" == ptype:
            effective = "super"

        if usetype == "Flying" and "Electric" == ptype or usetype == "Flying" and " Electric" == ptype:
            effective = "half"
        if usetype == "Flying" and "Grass" == ptype or usetype == "Flying" and " Grass" == ptype:
            effective = "super"
        if usetype == "Flying" and "Fighting" == ptype or usetype == "Flying" and " Fighting" == ptype:
            effective = "super"
        if usetype == "Flying" and "Bug" == ptype or usetype == "Flying" and " Bug" == ptype:
            effective = "Bug"
        if usetype == "Flying" and "Rock" == ptype or usetype == "Flying" and " Rock" == ptype:
            effective = "half"

        if usetype == "Psychic" and "Fighting" == ptype or usetype == "Psychic" and " Fighting" == ptype:
            effective = "super"
        if usetype == "Psychic" and "Poison" == ptype or usetype == "Psychic" and " Poison" == ptype:
            effective = "super"
        if usetype == "Psychic" and "Psychic" == ptype or usetype == "Psychic" and " Psychic" == ptype:
            effective = "half"

        if usetype == "Bug" and "Fire" == ptype or usetype == "Bug" and " Fire" == ptype:
            effective = "half"
        if usetype == "Bug" and "Grass" == ptype or usetype == "Bug" and " Grass" == ptype:
            effective = "super"
        if usetype == "Bug" and "Fighting" == ptype or usetype == "Bug" and " Fighting" == ptype:
            effective = "half"
        if usetype == "Bug" and "Poison" == ptype or usetype == "Bug" and " Poison" == ptype:
            effective = "half"
        if usetype == "Bug" and "Flying" == ptype or usetype == "Bug" and " Flying" == ptype:
            effective = "half"
        if usetype == "Bug" and "Psychic" == ptype or usetype == "Bug" and " Psychic" == ptype:
            effective = "super"
        if usetype == "Bug" and "Ghost" == ptype or usetype == "Bug" and " Ghost" == ptype:
            effective = "half"

        if usetype == "Rock" and "Fire" == ptype or usetype == "Rock" and " Fire" == ptype:
            effective = "super"
        if usetype == "Rock" and "Ice" == ptype or usetype == "Rock" and " Ice" == ptype:
            effective = "super"
        if usetype == "Rock" and "Fighting" == ptype or usetype == "Rock" and " Fighting" == ptype:
            effective = "half"
        if usetype == "Rock" and "Ground" == ptype or usetype == "Rock" and " Ground" == ptype:
            effective = "half"
        if usetype == "Rock" and "Flying" == ptype or usetype == "Rock" and " Flying" == ptype:
            effective = "super"
        if usetype == "Rock" and "Bug" == ptype or usetype == "Rock" and " Bug" == ptype:
            effective = "super"

        if usetype == "Ghost" and "Normal" == ptype or usetype == "Ghost" and " Normal" == ptype:
            effective = "zero"
        if usetype == "Ghost" and "Psychic" == ptype or usetype == "Ghost" and " Psychic" == ptype:
            effective = "super"
        if usetype == "Ghost" and "Ghost" == ptype or usetype == "Ghost" and " Ghost" == ptype:
            effective = "super"

        if usetype == "Dragon" and "Dragon" == ptype or usetype == "Dragon" and " Dragon" == ptype:
            effective = "super"
        #print(effective, "effective at end")
        return(effective)


    def typechart(enemypokemon, oppositepokemon):
        global matchup
        global matchup1
        Doit = "yes"
        matchup = "normal"
        matchup1 = "normal"
        for i in range(pokemonlist):
            if (data[i]["Name"]) == oppositepokemon:
                ptype = (data[i]["Types"])
        for i in range(pokemonlist):
            if (data[i]["Name"]) == enemypokemon:
                enemytypes = (data[i]["Types"])
        enemytype = enemytypes[0]
        if len(enemytypes) == 1:
          Doit = "no"

        if len(enemytypes) == 2:
          enemytype2 = enemytypes[1]
          
        #if len(types) == 2: 2 variables
        

        if enemytype == "Normal" and "Rock" in ptype:
            matchup = "half"
        if enemytype == "Normal" and "Ghost" in ptype:
            matchup = "zero"

        if enemytype == "Fire" and "Fire" in ptype:
            matchup = "half"
        if enemytype == "Fire" and "Water" in ptype:
            matchup = "half"
        if enemytype == "Fire" and "Grass" in ptype:
            matchup = "super"
        if enemytype == "Fire" and "Ice" in ptype:
            matchup = "super"
        if enemytype == "Fire" and "Bug" in ptype:
            matchup = "super"
        if enemytype == "Fire" and "Rock" in ptype:
            matchup = "half"
        if enemytype == "Fire" and "Dragon" in ptype:
            matchup = "half"

        if enemytype == "Water" and "Fire" in ptype:
            matchup = "super"
        if enemytype == "Water" and "Water" in ptype:
            matchup = "half"
        if enemytype == "Water" and "Grass" in ptype:
            matchup = "half"
        if enemytype == "Water" and "Ground" in ptype:
            matchup = "super"
        if enemytype == "Water" and "Rock" in ptype:
            matchup = "super"
        if enemytype == "Water" and "Dragon" in ptype:
            matchup = "half"

        if enemytype == "Electric" and "Water" in ptype:
            matchup = "super"
        if enemytype == "Electic" and "Electirc" in ptype:
            matchup = "half"
        if enemytype == "Electric" and "Grass" in ptype:
            matchup = "half"
        if enemytype == "Electric" and "Ground" in ptype:
            matchup = "zero"
        if enemytype == "Electric" and "Flying" in ptype:
            matchup = "super"
        if enemytype == "Electric" and "Dragon" in ptype:
            matchup = "half"

        if enemytype == "Grass" and "Fire" in ptype:
            matchup = "half"
        if enemytype == "Grass" and "Water" in ptype:
            matchup = "super"
        if enemytype == "Grass" and "Grass" in ptype:
            matchup = "half"
        if enemytype == "Grass" and "Poison" in ptype:
            matchup = "half"
        if enemytype == "Grass" and "Ground" in ptype:
            matchup = "super"
        if enemytype == "Grass" and "Flying" in ptype:
            matchup = "half"
        if enemytype == "Grass" and "Bug" in ptype:
            matchup = "half"
        if enemytype == "Grass" and "Rock" in ptype:
            matchup = "super"
        if enemytype == "Grass" and "Dragon" in ptype:
            matchup = "half"

        if enemytype == "Ice" and "Fire" in ptype:
            matchup = "half"
        if enemytype == "Ice" and "Water" in ptype:
            matchup = "half"
        if enemytype == "Ice" and "Grass" in ptype:
            matchup = "super"
        if enemytype == "Ice" and "Ice" in ptype:
            matchup = "half"
        if enemytype == "Ice" and "Ground" in ptype:
            matchup = "super"
        if enemytype == "Ice" and "Flying" in ptype:
            matchup = "super"
        if enemytype == "Ice" and "Dragon" in ptype:
            matchup = "super"

        if enemytype == "Fighting" and "Normal" in ptype:
            matchup = "super"
        if enemytype == "Fighting" and "Ice" in ptype:
            matchup = "super"
        if enemytype == "Fighting" and "Poison" in ptype:
            matchup = "half"
        if enemytype == "Fighting" and "Flying" in ptype:
            matchup = "half"
        if enemytype == "Fighting" and "Psychic" in ptype:
            matchup = "half"
        if enemytype == "Fighting" and "Bug" in ptype:
            matchup = "half"
        if enemytype == "Fighting" and "Rock" in ptype:
            matchup = "super"
        if enemytype == "Fighting" and "Ghost" in ptype:
            matchup = "zero"

        if enemytype == "Poison" and "Grass" in ptype:
            matchup = "super"
        if enemytype == "Poison" and "Poison" in ptype:
            matchup = "half"
        if enemytype == "Poison" and "Ground" in ptype:
            matchup = "half"
        if enemytype == "Poison" and "Rock" in ptype:
            matchup = "half"
        if enemytype == "Poison" and "Ghost" in ptype:
            matchup = "half"

        if enemytype == "Ground" and "Fire" in ptype:
            matchup = "super"
        if enemytype == "Ground" and "Electric" in ptype:
            matchup = "super"
        if enemytype == "Ground" and "Grass" in ptype:
            matchup = "half"
        if enemytype == "Ground" and "Poison" in ptype:
            matchup == "super"
        if enemytype == "Ground" and "Flying" in ptype:
            matchup == "zero"
        if enemytype == "Ground" and "Bug" in ptype:
            matchup == "half"
        if enemytype == "Ground" and "Rock" in ptype:
            matchup = "super"

        if enemytype == "Flying" and "Electric" in ptype:
            matchup = "half"
        if enemytype == "Flying" and "Grass" in ptype:
            matchup = "super"
        if enemytype == "Flying" and "Fighting" in ptype:
            matchup = "super"
        if enemytype == "Flying" and "Bug" in ptype:
            matchup = "Bug"
        if enemytype == "Flying" and "Rock" in ptype:
            matchup = "half"

        if enemytype == "Psychic" and "Fighting" in ptype:
            matchup = "super"
        if enemytype == "Psychic" and "Poison" in ptype:
            matchup = "super"
        if enemytype == "Psychic" and "Psychic" in ptype:
            matchup = "half"

        if enemytype == "Bug" and "Fire" in ptype:
            matchup = "half"
        if enemytype == "Bug" and "Grass" in ptype:
            matchup = "super"
        if enemytype == "Bug" and "Fighting" in ptype:
            matchup = "half"
        if enemytype == "Bug" and "Poison" in ptype:
            matchup = "half"
        if enemytype == "Bug" and "Flying" in ptype:
            matchup = "half"
        if enemytype == "Bug" and "Psychic" in ptype:
            matchup = "super"
        if enemytype == "Bug" and "Ghost" in ptype:
            matchup = "half"

        if enemytype == "Rock" and "Fire" in ptype:
            matchup = "super"
        if enemytype == "Rock" and "Ice" in ptype:
            matchup = "super"
        if enemytype == "Rock" and "Fighting" in ptype:
            matchup = "half"
        if enemytype == "Rock" and "Ground" in ptype:
            matchup = "half"
        if enemytype == "Rock" and "Flying" in ptype:
            matchup = "super"
        if enemytype == "Rock" and "Bug" in ptype:
            matchup = "super"

        if enemytype == "Ghost" and "Normal" in ptype:
            matchup = "zero"
        if enemytype == "Ghost" and "Psychic" in ptype:
            matchup = "super"
        if enemytype == "Ghost" and "Ghost" in ptype:
            matchup = "super"

        if enemytype == "Dragon" and "Dragon" in ptype:
            matchup = "super"
        if Doit == "yes":
          if enemytype2 == "Normal" and "Rock" in ptype:
            matchup1 = "half"
          if enemytype2 == "Normal" and "Ghost" in ptype:
            matchup1 = "zero"

          if enemytype2 == "Fire" and "Fire" in ptype:
            matchup1 = "half"
          if enemytype2 == "Fire" and "Water" in ptype:
            matchup1 = "half"
          if enemytype2 == "Fire" and "Grass" in ptype:
            matchup1 = "super"
          if enemytype2 == "Fire" and "Ice" in ptype:
            matchup1 = "super"
          if enemytype2 == "Fire" and "Bug" in ptype:
            matchup1 = "super"
          if enemytype2 == "Fire" and "Rock" in ptype:
            matchup1 = "half"
          if enemytype2 == "Fire" and "Dragon" in ptype:
            matchup1 = "half"

          if enemytype2 == "Water" and "Fire" in ptype:
            matchup1 = "super"
          if enemytype2 == "Water" and "Water" in ptype:
            matchup1 = "half"
          if enemytype2 == "Water" and "Grass" in ptype:
            matchup1 = "half"
          if enemytype2 == "Water" and "Ground" in ptype:
            matchup1 = "super"
          if enemytype2 == "Water" and "Rock" in ptype:
            matchup1 = "super"
          if enemytype2 == "Water" and "Dragon" in ptype:
            matchup1 = "half"

          if enemytype2 == "Electric" and "Water" in ptype:
            matchup1 = "super"
          if enemytype2 == "Electic" and "Electirc" in ptype:
            matchup1 = "half"
          if enemytype2 == "Electric" and "Grass" in ptype:
            matchup1 = "half"
          if enemytype2 == "Electric" and "Ground" in ptype:
            matchup1 = "zero"
          if enemytype2 == "Electric" and "Flying" in ptype:
            matchup1 = "super"
          if enemytype2 == "Electric" and "Dragon" in ptype:
            matchup1 = "half"

          if enemytype2 == "Grass" and "Fire" in ptype:
            matchup1 = "half"
          if enemytype2 == "Grass" and "Water" in ptype:
            matchup1 = "super"
          if enemytype2 == "Grass" and "Grass" in ptype:
            matchup1 = "half"
          if enemytype2 == "Grass" and "Poison" in ptype:
            matchup1 = "half"
          if enemytype2 == "Grass" and "Ground" in ptype:
            matchup1 = "super"
          if enemytype2 == "Grass" and "Flying" in ptype:
            matchup1 = "half"
          if enemytype2 == "Grass" and "Bug" in ptype:
            matchup1 = "half"
          if enemytype2 == "Grass" and "Rock" in ptype:
            matchup1 = "super"
          if enemytype2 == "Grass" and "Dragon" in ptype:
            matchup1 = "half"

          if enemytype2 == "Ice" and "Fire" in ptype:
            matchup1 = "half"
          if enemytype2 == "Ice" and "Water" in ptype:
            matchup1 = "half"
          if enemytype2 == "Ice" and "Grass" in ptype:
            matchup1 = "super"
          if enemytype2 == "Ice" and "Ice" in ptype:
            matchup1 = "half"
          if enemytype2 == "Ice" and "Ground" in ptype:
            matchup1 = "super"
          if enemytype2 == "Ice" and "Flying" in ptype:
            matchup1 = "super"
          if enemytype2 == "Ice" and "Dragon" in ptype:
            matchup1 = "super"

          if enemytype2 == "Fighting" and "Normal" in ptype:
            matchup1 = "super"
          if enemytype2 == "Fighting" and "Ice" in ptype:
            matchup1 = "super"
          if enemytype2 == "Fighting" and "Poison" in ptype:
            matchup1 = "half"
          if enemytype2 == "Fighting" and "Flying" in ptype:
            matchup1 = "half"
          if enemytype2 == "Fighting" and "Psychic" in ptype:
            matchup1 = "half"
          if enemytype2 == "Fighting" and "Bug" in ptype:
            matchup1 = "half"
          if enemytype2 == "Fighting" and "Rock" in ptype:
            matchup1 = "super"
          if enemytype2 == "Fighting" and "Ghost" in ptype:
            matchup1 = "zero"

          if enemytype2 == "Poison" and "Grass" in ptype:
            matchup1 = "super"
          if enemytype2 == "Poison" and "Poison" in ptype:
            matchup1 = "half"
          if enemytype2 == "Poison" and "Ground" in ptype:
            matchup1 = "half"
          if enemytype2 == "Poison" and "Rock" in ptype:
            matchup1 = "half"
          if enemytype2 == "Poison" and "Ghost" in ptype:
            matchup1 = "half"

          if enemytype2 == "Ground" and "Fire" in ptype:
            matchup1 = "super"
          if enemytype2 == "Ground" and "Electric" in ptype:
            matchup1 = "super"
          if enemytype2 == "Ground" and "Grass" in ptype:
            matchup1 = "half"
          if enemytype2 == "Ground" and "Poison" in ptype:
            matchup1 == "super"
          if enemytype2 == "Ground" and "Flying" in ptype:
            matchup1 == "zero"
          if enemytype2 == "Ground" and "Bug" in ptype:
            matchup1 == "half"
          if enemytype2 == "Ground" and "Rock" in ptype:
            matchup1 = "super"

          if enemytype2 == "Flying" and "Electric" in ptype:
            matchup1 = "half"
          if enemytype2 == "Flying" and "Grass" in ptype:
            matchup1 = "super"
          if enemytype2 == "Flying" and "Fighting" in ptype:
            matchup1 = "super"
          if enemytype2 == "Flying" and "Bug" in ptype:
            matchup1 = "Bug"
          if enemytype2 == "Flying" and "Rock" in ptype:
            matchup1 = "half"

          if enemytype2 == "Psychic" and "Fighting" in ptype:
            matchup1 = "super"
          if enemytype2 == "Psychic" and "Poison" in ptype:
            matchup1 = "super"
          if enemytype2 == "Psychic" and "Psychic" in ptype:
            matchup1 = "half"

          if enemytype2 == "Bug" and "Fire" in ptype:
            matchup1 = "half"
          if enemytype2 == "Bug" and "Grass" in ptype:
            matchup1 = "super"
          if enemytype2 == "Bug" and "Fighting" in ptype:
            matchup1 = "half"
          if enemytype2 == "Bug" and "Poison" in ptype:
            matchup1 = "half"
          if enemytype2 == "Bug" and "Flying" in ptype:
            matchup1 = "half"
          if enemytype2 == "Bug" and "Psychic" in ptype:
            matchup1 = "super"
          if enemytype2 == "Bug" and "Ghost" in ptype:
            matchup1 = "half"

          if enemytype2 == "Rock" and "Fire" in ptype:
            matchup1 = "super"
          if enemytype2 == "Rock" and "Ice" in ptype:
            matchup1 = "super"
          if enemytype2 == "Rock" and "Fighting" in ptype:
            matchup1 = "half"
          if enemytype2 == "Rock" and "Ground" in ptype:
            matchup1 = "half"
          if enemytype2 == "Rock" and "Flying" in ptype:
            matchup1 = "super"
          if enemytype2 == "Rock" and "Bug" in ptype:
            matchup1 = "super"

          if enemytype2 == "Ghost" and "Normal" in ptype:
            matchup1 = "zero"
          if enemytype2 == "Ghost" and "Psychic" in ptype:
            matchup1 = "super"
          if enemytype2 == "Ghost" and "Ghost" in ptype:
            matchup1 = "super"

          if enemytype2 == "Dragon" and "Dragon" in ptype:
            matchup1 = "super"


    def pokemoninmoves(currentpokemon):
        global currentmoves

        #if currentpokemon == teaminfo[0]:
        #    currentmoves = teaminfo[1]
        #if currentpokemon == teaminfo[2]:
        #    currentmoves = teaminfo[3]
        #if currentpokemon == teaminfo[4]:
        #    currentmoves = teaminfo[5]
        #if currentpokemon == teaminfo[6]:
        #    currentmoves = teaminfo[7]
        #if currentpokemon == teaminfo[8]:
        #    currentmoves = teaminfo[9]
        #if currentpokemon == teaminfo[10]:
        #    currentmoves = teaminfo[11]

    def damagecalc(damagecalc, move, attackingpk, enemypk):
        
      if move != "Nothing":
        global typesuper1
        typesuper1 = False
        global typesuper2
        typesuper2 = False
        global typesuper
        typesuper = False

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
        if currentpokemon == attackingpk:
            userattack = userattack * userattackup
        if currentpokemon == attackingpk:
            userattack = userattack / userattackdown
            userattack = round(userattack)

        if enemypokemon == attackingpk:
            userattack = userattack * enemyattackup
        if enemypokemon == attackingpk:
            userattack = userattack / enemyattackdown
            userattack = round(userattack)

        enemydefense = data[enemynumber]["Defense Stat"]
        userspecial = data[attacknumber]["Special Stat"]
        
        

        userspecial = userspecial / userspecialdown

        enemyspecial = data[enemynumber]["Special Stat"]

        if attackingpk == enemypokemon:
            if Lightscreen == "yes":
                enemyspecial = enemyspecial * 2
            if Reflect == "yes":
                enemydefense = enemydefense * 2
            userspecial = userspecial / enemyspecialdown
            enemyspecial = enemyspecial / userspecialdown
            enemydefense = enemydefense * userdefenseup
            enemyspecial = enemyspecial * userspecialup
            userspecial = userspecial * enemyspecialup


        if attackingpk == currentpokemon:
            userspecial = userspecial / userspecialdown
            enemyspecial = enemyspecial / enemyspecialdown
            enemyspecial = enemyspecial * enemyspecialup
            userspecial = userspecial * userspecialup

        if moves[movenumber]["category"] == "Physical":
            global attackingpower
            global defendingpower
            attackingpower = userattack
            defendingpower = enemydefense
        if moves[movenumber]["category"] == "Special":
            attackingpower = userspecial
            defendingpower = enemyspecial
        if moves[movenumber]["category"] == "None":
            attackingpower = userattack
            defendingpower = enemydefense
        userspeed = data[attacknumber]["Speed Stat"]
        threshold = userspeed / decimal.Decimal(8)
        donut = 255
        for i in range(movelist):
            if "HighCrit" in moves[movenumber]["effect"]:
                donut = 180
        critchance = random.randint(0,donut)
        if threshold > critchance:
            attackingpower *= 1.5
            global crithappen
            crithappen = True
        if threshold < critchance or threshold == critchance:
            crithappen = False
        math1 = decimal.Decimal(40) * decimal.Decimal(movepower)
        math2 = decimal.Decimal(attackingpower) / decimal.Decimal(defendingpower)
        math3 = decimal.Decimal(math2) * decimal.Decimal(math1)
        math4 = decimal.Decimal(math3) / decimal.Decimal(50)
        math5 = decimal.Decimal(math4) + decimal.Decimal(2)
        #print(math5)
        if moves[movenumber]["type"] in data[attacknumber]["Types"]:
            global stab
            stab = True
        if not(moves[movenumber]["type"] in data[attacknumber]["Types"]):
            stab = False
        f = functionality()
        if len(data[enemynumber]["Types"]) == 2:
            enemytype1 = (data[enemynumber]["Types"])[0]
            enemytype2 = (data[enemynumber]["Types"])[1]
            typeeffect1 = f.supereffective(move, enemytype1)
            global meffective1
            
            global typehalf1
            typehalf1 = False
            global typezero1
            typezero1 = False
            if typeeffect1 == "super":
                typesuper1 = True
                meffective1 = 2
            if typeeffect1 == "half":
                typehalf1 = True
                meffective1 = 0.5
            if typeeffect1 == "zero":
                typezero1 = True
                meffective1 = 0
            if typesuper1 != True and typehalf1 != True and typezero1 != True:
                meffective1 = 1
            typeeffect2 = f.supereffective(move, enemytype2)
            global meffective2
            
            global typehalf2
            typehalf2 = False
            global typezero2
            typezero2 = False
            if typeeffect2 == "super":
                typesuper2 = True
                meffective2 = 2
            if typeeffect2 == "half":
                typehalf2 = True
                meffective2 = 0.5
            if typeeffect2 == "zero":
                typezero2 = True
                meffective2 = 0
            if typesuper2 != True and typehalf2 != True and typezero2 != True:
                meffective2 = 1
            global twotype
            twotype = True
        if len(data[enemynumber]["Types"]) == 1:
            enemytype = (data[enemynumber]["Types"])[0]
            typeeffect = f.supereffective(move, enemytype)
            global meffective
            
            global typehalf
            typehalf = False
            global typezero
            typezero = False
            if typeeffect == "super":
                typesuper = True
                meffective = 2
            if typeeffect == "half":
                typehalf = True
                meffective = 0.5
            if typeeffect == "zero":
                typezero = True
                meffective = 0
            if typesuper != True and typehalf != True and typezero != True:
                meffective = 1
        if stab == True:
            math5 *=  decimal.Decimal(1.5)
        if len(data[enemynumber]["Types"]) == 1:
            math5 *= decimal.Decimal(meffective)
            #print(meffective)
            #print(math5)
        if len(data[enemynumber]["Types"]) == 2:
            meffective = decimal.Decimal(meffective1) * decimal.Decimal(meffective2)
            #print(meffective1)
            #print(meffective2)
            math5 *= decimal.Decimal(meffective)
            #print(math5)
        global movedamage
        movedamage = round(math5)
        if moves[movenumber]["category"] == "None":
            movedamage = 0
      else:
        movedamage = 0
        #if typesuper == True or typesuper2 == True or typesuper1 == True:
            #print("It was supereffective!")
    def specialeffect(specialeffect, move, damage, enemyspeedph, currentspeedph, enemypk, userpk, going, previousdamage, turn,enemyheat):
        global PrintPoison
        global DoDamage
        global EnemyPoisoned

        global uniquedamage
        global Diduniquedamagehappen
        Diduniquedamagehappen = "no"

        global enemyspeed
        global currentspeed

        global TwoHitDamage
        global Didithittwice
        Didithittwice = "no"

        global fourtydamagetrue
        fourtydamagetrue = "no"

        global itcounter
        global counterdamage
        itcounter = "no"

        global Flinching
        Flinching = "no"

        global PrintBurn
        PrintBurn = "no"
        global EnemyBurn
        EnemyBurn = "no"

        global Trapped
        
        global Trappedturns
        global startingturntrapped

        global awaybeforehit
        global leavingturn

        global itsfly
        #itsfly = "no"
        global itsdig
        #itsdig = "no"

        global hitsnextturn

        global PrintConfuse
        global EnemyConfuse

        global PrintParalyzed
        global EnemyParalyzed

        global evasive
        global enemyevasive

        global enemyattackup
        global userattackup

        global enemyhealth

        global lockedin
        global usedturn
        global gooblie
        global enemylockedin
        global enemyusedturn
        global fdd

        global enemyattackdown
        global userattackdown

        global mistactive

        global Lightscreen
        global Reflect

        global userspecialdown
        global enemyspecialdown

        global userdefenseup

        global userspecialup
        global enemyspecialup

        global Recharging
        global previousturn

        print(going, "going at beginning of special effect")
        print(move, "move in special effect")
        movenumber = 6

        f = functionality
        if move != "Nothing":
            for i in range(movelist):
                if move == moves[i]["name"]:
                    movenumber = i
        for i in range(pokemonlist):
            if enemypk == data[i]["Name"]:
                enemynumber = i
        for i in range(pokemonlist):
            if userpk == data[i]["Name"]:
                usernumber = i

        if "HealHalfD" in moves[movenumber]["effect"]:
            for i in range(pokemonlist):
                if userpk == data[i]["Name"]:
                    fullhealth = data[i]["Health Stat"]
            for i in range(len(userpartyhealth)):
                if userpk == userpartyhealth[i - 1]:
                    currenthealth = userpartyhealth[i]
            heal = damage / 2
            healamount = round(heal)
            if currenthealth != fullhealth:
                currenthealth += int(healamount)
            if currenthealth == fullhealth or currenthealth > fullhealth:
                currenthealth = fullhealth
            for i in range(len(userpartyhealth)):
                if userpk == userpartyhealth[i - 1]:
                    userpartyhealth[i] = currenthealth
            print(userpk, "healed", healamount)
            print(userpk, "has", currenthealth, "health left")

        if "Hits2to5" in moves[movenumber]["effect"]:
            hitamount = random.randrange(5)
            if hitamount == 1 or hitamount == 0:
                hitamount = 2
            setdamage = damage
            global uniquedamage
            uniquedamage = damage
            for i in range(hitamount):
                print(userpk, "did", setdamage, "damage")
                uniquedamage += setdamage
            uniquedamage -= setdamage
            Diduniquedamagehappen = "yes"
            DoDamage = "no"
            print("It hit", hitamount, "times!")
            #damage = uniquedamage
            unique[0] = "Yah"

        if "SpeedDown" in moves[movenumber]["effect"]:
            if going == "User":
                onestage = decimal.Decimal(2) / decimal.Decimal(3)
                enemyspeedph *= onestage 
                enemyspeed = round(enemyspeedph)
                print(enemypokemon,"'s speed fell!")
                print(enemyspeed)
            if going == "Enemy":
                Eonestage = decimal.Decimal(2) / decimal.Decimal(3)
                currentspeedph *= Eonestage 
                currentspeed = round(currentspeedph)
                print(currentpokemon,"'s speed fell!")
                print(currentspeed)
            
        if "HitsTwice" in moves[movenumber]["effect"]:
            for i in range(2):
                print(userpk, "did", damage, "damage")
            startdamage = damage
            TwoHitDamage = startdamage *2
            DoDamage = "no"
            Didithittwice = "yes"
            
        if "Always40D" in moves[movenumber]["effect"]:
            fourtydamagetrue = "yes"

        if "ItCounter" in moves[movenumber]["effect"]:
            # goes last
            # only works if move being countered is normal or fighting
            # deals double the damage
            countertypes = moves[movenumber]["type"]
            if "Normal" or "Fighting" in countertypes:
                counterdamage = previousdamage * 2
                itcounter = "yes"

        if "Flinch13" in moves[movenumber]["effect"]:
            functionality.Flinch(3, going, goingfirst)
        
        if "Seismictoss" in moves[movenumber]["effect"]:
            print("Boy i ain't coding all that")

        if "Recoil14" in moves[movenumber]["effect"]:
            for i in range(len(userpartyhealth)):
                if userpk == userpartyhealth[i - 1]:
                    currenthealth = userpartyhealth[i]
            recoil = damage/4
            recoil = round(recoil)
            currenthealth = currenthealth - recoil
            print(currenthealth, "currenthealth")
            print(currentpokemon, "took", recoil, "damage due to recoil")
            for i in range(len(userpartyhealth)):
                if userpk == userpartyhealth[i - 1]:
                    userpartyhealth[i] = currenthealth
        
        if "Burn13" in moves[movenumber]["effect"]:
            allentown = random.randrange(3)
            if allentown == 1:
                if going == "Enemy":
                    if not "Fire" in data[usernumber]["Types"]:
                        for i in range(len(userpartystatus)):
                            if currentpokemon == userpartystatus[i - 1]:
                                if userpartystatus[i] != "Burn":
                                    userpartystatus[i] = "Burn"
                                    PrintBurn = "yes"
                                    DoDamage = "no"
                                if userpartystatus[i] == "Burn":
                                    print(currentpokemon, "is already burned")
                            
                    
                if going == "User":
                    if not 'Fire' in data[enemynumber]["Types"]:
                        for i in range(len(eliteteamstatus)):
                            if enemypokemon == eliteteamstatus[i - 1]:
                                if eliteteamstatus[i] != "Burn":
                                    eliteteamstatus[i] = "Burn"
                                    EnemyBurn = "yes"
                                    DoDamage = "no"
                                if eliteteamstatus[i] == "Burn":
                                    print(enemypokemon,"is already burned")
        
        if "Firespin" in moves[movenumber]["effect"]:
            #gonna be a bit different. Just burns and traps
            
            Trapped = "yes"
            Trappedturns = random.randrange(5)
            if Trappedturns == 0 or Trappedturns == 1:
                Trappedturns = 2
            startingturntrapped = turn
            print(enemypokemon, "is trapped!")
            if not 'Fire' in data[enemynumber]["Types"]:
                for i in range(len(eliteteamstatus)):
                    if enemypokemon == eliteteamstatus[i - 1]:
                        if eliteteamstatus[i] == "Burn":
                            print(enemypokemon,"is already burned")
                        if eliteteamstatus[i] != "Burn":
                            eliteteamstatus[i] = "Burn"
                            EnemyBurn = "yes"
                            DoDamage = "no"
        
        if "Flygimmick" in moves[movenumber]["effect"]:
            awaybeforehit = "yes"
            itsfly = "yes"
            print(currentpokemon, "flew up high")
            DoDamage = "no"
            leavingturn = turn
            
        if "Digs" in moves[movenumber]["effect"]:
            awaybeforehit = "yes"
            itsdig = "yes"
            print(currentpokemon, "dug down")
            DoDamage = "no"
            leavingturn = turn
            
        if "HitsNextTurn" in moves[movenumber]["effect"]:
            
            if hitsnextturn == "no":
                hitsnextturn = "yes"
                DoDamage = "no"
            elif hitsnextturn == "yes":
                hitsnextturn = "no"

        if "LeechSeed" in moves[movenumber]["effect"]:
            global seeded
            seeded = "yes"
            DoDamage = "no"
        
        if "AccuracyDown" in moves[movenumber]["effect"]:
            if going == "Enemy":
                if mistactive == "no":
                    evasive += 1
                    DoDamage = "no"
                    print(currentpokemon,"'s accuracy fell!")
                if mistactive == "yes":
                    print(currentpokemon, "did not have its accuracy decreased due to Mist")
            if going == "User":
                enemyevasive += 1
                DoDamage = "no"
                print(enemypokemon,"'s accuracy fell")

        if "SpeedSharpUp" in moves[movenumber]["effect"]:
            DoDamage = "no"
            if going == "Enemy":
                enemyspeed = enemyspeed * 2
                print(enemypokemon,"'s speed rose sharply")
            if going == "User":
                currentspeed = currentspeed * 2
                print(currentpokemon,"'s speed rose sharply")
        
        if "AttackSharpUp" in moves[movenumber]["effect"]:
            DoDamage = "no"
            if going == "Enemy":
                enemyattackup += 2
                print(enemypokemon,"'s attack rose sharply")
            if going == "User":
                userattackup += 2
                print(currentpokemon,"'s attack rose sharply")

        if "DreamEatEffect" in moves[movenumber]["effect"]:
            if going == "Enemy":
                for i in range(len(userpartystatus)):
                    if currentpokemon == userpartystatus[i-1]:
                        if userpartystatus[i] == "Asleep":
                            healing = damage/2
                            healing = round(healing)
                            for i in range(pokemonlist):
                                if currentpokemon == data[i]["Name"]:
                                    korok = data[i]["Health Stat"]
                            currenthealth = currenthealth + healing
                            if healing == korok or healing > korok:
                                currenthealth = korok
                            for i in range(len(userpartyhealth)):
                                if currentpokemon == userpartyhealth[i-1]:
                                    userpartyhealth[i] = currenthealth
                        if userpartystatus[i] != "Asleep":
                            DoDamage = "no"
                            print("But it failed")
                            
            if going == "User":
                for i in range(len(eliteteamstatus)):
                    if enemypokemon == eliteteamstatus[i-1]:
                        if eliteteamstatus[i] == "Asleep":
                            healing = damage/2
                            healing = round(healing)
                            for i in range(pokemonlist):
                                if enemypokemon == data[i]["Name"]:
                                    korok = data[i]["Health Stat"]
                            enemyhealth = enemyheat + healing
                            if healing == korok or healing > korok:
                                enemyhealth = korok
                            #for i in range(len(eliteteamstatus)):
                             #   if currentpokemon == eliteteamstatus[i-1]:
                              #      enemypartyhealth[i] = enemyhealth
                        else:
                            DoDamage = "no"
                            print("But it failed")
                            
        if "PetalDance" in moves[movenumber]["effect"]:
            
            if going == "User":
                if lockedin == "no":
                    gooblie = random.randrange(3)
                    if gooblie == 0 or gooblie == 1:
                        gooblie = 2
                    usedturn = turn
                    lockedin = "yes"

            if going == "Enemy":
                if enemylockedin == "no":
                    fdd = random.randrange(3)
                    if fdd == 0 or fdd == 1:
                        fdd = 2
                    enemyusedturn = turn
                    enemylockedin = "yes"

        if "MayFlinch" in moves[movenumber]["effect"]:
            functionality.Flinch(5, going, goingfirst)  
        
        if "OHKO" in moves[movenumber]["effect"]:
            damage = 1000
            print("Its a one-hit KO!")
        
        if "13AttackDown" in moves[movenumber]["effect"]:
            fork = random.randrange(3)
            if fork == 1:
                if going == "User":
                    enemyattackdown += 1
                    print(enemypokemon,"'s attack fell")
                if going == "Enemy":
                    if mistactive == "no":
                        userattackdown += 1
                        print(currentpokemon,"'s attack fell")
                    if mistactive == "yes":
                        print(currentpokemon, "did not have its attack decreased due to Mist")
        
        if "HazeEffect" in moves[movenumber]["effect"]:
            enemyevasive = 0
            enemyattackup = 0
            enemyattackdown = 0
            for i in range(pokemonlist):
                if enemypokemon == data[i]["Name"]:
                    enemyspeed = data[i]["Speed Stat"]
            DoDamage = "no"
            print(enemypokemon,"was cleared of all stat changes")
        
        if "MistEffect" in moves[movenumber]["effect"]:
            mistactive = "yes"
            
        if "BideEffect" in moves[movenumber]["effect"]:
            print("Why on earth are you using this move. I refuse to code this")
            time.sleep(times)
        if "BindEffect" in moves[movenumber]["effect"]:
            print("it did 1000000 damage!")
            time.sleep(1)
            print("did you believe it?")
            time.sleep(1)
            print("hopefully not :)")

        if "1in3SpeedDown" in moves[movenumber]["effect"]:
            if going == "User":
                enemyspeed = enemyspeed / 2
                print(enemypokemon,"'s speed fell")
            if going == "Enemy":
                currentspeed = currentspeed / 2
                print(currentpokemon,"'s speed fell")
        
        if "LightScreenEffect" in moves[movenumber]["effect"]:
            DoDamage = "no"
            Lightscreen = "yes"

        if "ReflectEffect" in moves[movenumber]["effect"]:
            DoDamage = "no"
            Reflect = "yes"
        
        if "AttackUp" in moves[movenumber]["effect"]:
            if going == "Enemy":
                enemyattackup += 1
                print(enemypokemon,"'s attack rose sharply")
            if going == "User":
                userattackup += 1
                print(currentpokemon,"'s attack rose sharply")
        
        if "1in10Confuse" in moves[movenumber]["effect"]:
            find = random.randrange(10)
            if find == 1:
                if going == "Enemy":
                
                    for i in range(len(userpartystatus)):
                        if currentpokemon == userpartystatus[i - 1]:
                            if userpartystatus[i] == "Confused":
                                print(currentpokemon, "is already confused")
                            if userpartystatus[i] != "Confused":
                                userpartystatus[i] = "Confused"
                                PrintConfuse = "yes"
                                
                                
                                
                        
                if going == "User":
                    
                    for i in range(len(eliteteamstatus)):
                        if enemypokemon == eliteteamstatus[i - 1]:
                            if eliteteamstatus[i] == "Confused":
                                print(enemypokemon,"is already confused")
                            if eliteteamstatus[i] != "Confused":
                                eliteteamstatus[i] = "Confused"
                                EnemyConfuse = "yes"
        
        if "1in3SpecialDown" in moves[movenumber]["effect"]:
            annbalin = random.randrange(3)
            if annbalin == 1:
                if going == "Enemy":
                    userspecialdown += 1
                if going == "User":
                    enemyspecialdown += 1
        
        if "FullRestore" in moves[movenumber]["effect"]:
            for i in range(pokemonlist):
                if currentpokemon == data[i]["Name"]:
                    fullhealth = data[i]["Health Stat"]
            for i in range(len(userpartyhealth)):
                if currentpokemon == userpartyhealth[i - 1]:
                    currenthealth = userpartyhealth[i]
            currenthealth = fullhealth
            for i in range(len(userpartyhealth)):
                if currentpokemon == userpartyhealth[i-1]:
                    userpartyhealth[i] = currenthealth            
            print(currentpokemon, "healed all of its health!")
            time.sleep(1)
            for i in range(len(userpartystatus)):
                    if currentpokemon == userpartystatus[i-1]:
                        if userpartystatus[i] == "Asleep":
                            print(currentpokemon,"is already asleep")
                        if userpartystatus[i] != "Asleep":
                            userpartystatus[i] = "Asleep"
                            print(currentpokemon,"fell asleep!")

        if "WrapEffect" in moves[movenumber]["effect"]:
            print("this effect way too broken.\n no handouts\n be better")
            time.sleep(times)
        
        if "SwitchTypetoTarget" in moves[movenumber]["effect"]:
            for i in range(pokemonlist):
                if enemypokemon == data[i]["Name"]:
                    datypes = data[i]["Types"]
            print(currentpokemon, "now identifies as", datypes)
        
        if "DefenseUp" in moves[movenumber]["effect"]:
            
            if going == "User":
                userdefenseup += 1
        
        if "DisableMove" in moves[movenumber]["effect"]:
            print(currentpokemon,"disabled", enemymove)
            time.sleep(1)
            print("But Mike used his mystic powers to counter it!")
        
        if "AttackDown" in moves[movenumber]["effect"]:
            if going == "User":
                    enemyattackdown += 1
                    print(enemypokemon,"'s attack fell")
            if going == "Enemy":
                if mistactive == "no":
                    userattackdown += 1
                    print(currentpokemon,"'s attack fell")
                if mistactive == "yes":
                    print(currentpokemon, "did not have its attack decreased due to Mist")
        
        if "SpecialUp" in moves[movenumber]["effect"]:
            if going == "Enemy":
                userspecialup += 1
            if going == "User":
                enemyspecialup += 1
        
        if "Recharge" in moves[movenumber]["effect"]:
            Recharging = "yes"
            print("recharging runnin")
            previousturn = turn
            if turn - previousturn == 1:
                Recharging = "no"

        

        
        


            
        if "Sleep" in moves[movenumber]["effect"]:
            if going == "Enemy":
                for i in range(len(userpartystatus)):
                    if currentpokemon == userpartystatus[i-1]:
                        if userpartystatus[i] == "Asleep":
                            print(currentpokemon,"is already asleep")
                        if userpartystatus[i] != "Asleep":
                            userpartystatus[i] = "Asleep"
                            print(currentpokemon,"fell asleep!")
                            
            if going == "User":
                for i in range(len(eliteteamstatus)):
                    if enemypokemon == eliteteamstatus[i-1]:
                        if eliteteamstatus[i] == "Asleep":
                            print(enemypokemon,"is already asleep")
                        if eliteteamstatus[i] != "Asleep":
                            eliteteamstatus[i] = "Asleep"
                            print(enemypokemon,"fell asleep!")
                            
        
        if "Freeze" in moves[movenumber]["effect"]:
            if going == "Enemy":
                for i in range(len(userpartystatus)):
                    if currentpokemon == userpartystatus[i-1]:
                        if userpartystatus[i] == "Frozen":
                            print(currentpokemon,"is already frozen")
                        if userpartystatus[i] != "Frozen":
                            userpartystatus[i] = "Frozen"
                            print(currentpokemon,"is frozen!")
                            
            if going == "User":
                for i in range(len(eliteteamstatus)):
                    if enemypokemon == eliteteamstatus[i-1]:
                        if eliteteamstatus[i] == "Frozen":
                            print(enemypokemon,"is already frozen")
                        if eliteteamstatus[i] != "Frozen":
                            eliteteamstatus[i] = "Frozen"
                            print(enemypokemon,"is frozen!")
                            

        if "Poison" in moves[movenumber]["effect"]:
            if going == "Enemy":
                if not "Poison" in data[usernumber]["Types"]:
                    for i in range(len(userpartystatus)):
                        if currentpokemon == userpartystatus[i - 1]:
                            if userpartystatus[i] == "Poison":
                                print(currentpokemon, "is already poisoned")
                            if userpartystatus[i] != "Poison":
                                userpartystatus[i] = "Poison"
                                PrintPoison = "yes"
                                
                            
            if going == "User":
                if not 'Poison' in data[enemynumber]["Types"]:
                    for i in range(len(eliteteamstatus)):
                        if enemypokemon == eliteteamstatus[i - 1]:
                            if eliteteamstatus[i] == "Poison":
                                print(enemypokemon,"is already poisoned")
                            if eliteteamstatus[i] != "Poison":
                                eliteteamstatus[i] = "Poison"
                                EnemyPoisoned = "yes"
                                
                            

        if "Burn" in moves[movenumber]["effect"]:
            if going == "Enemy":
                if not "Fire" in data[usernumber]["Types"]:
                    for i in range(len(userpartystatus)):
                        if currentpokemon == userpartystatus[i - 1]:
                            if userpartystatus[i] == "Burn":
                                print(currentpokemon, "is already burned")
                            if userpartystatus[i] != "Burn":
                                userpartystatus[i] = "Burn"
                                PrintBurn = "yes"
                                
                            
                            
                    
            if going == "User":
                if not 'Fire' in data[enemynumber]["Types"]:
                    for i in range(len(eliteteamstatus)):
                        if enemypokemon == eliteteamstatus[i - 1]:
                            if eliteteamstatus[i] == "Burn":
                                print(enemypokemon,"is already burned")
                            if eliteteamstatus[i] != "Burn":
                                eliteteamstatus[i] = "Burn"
                                EnemyBurn = "yes"
                                
                            
        if "Confuses" in moves[movenumber]["effect"]:
            if going == "Enemy":
                
                for i in range(len(userpartystatus)):
                    if currentpokemon == userpartystatus[i - 1]:
                        if userpartystatus[i] == "Confused":
                            print(currentpokemon, "is already confused")
                        if userpartystatus[i] != "Confused":
                            userpartystatus[i] = "Confused"
                            PrintConfuse = "yes"
                            
                            
                            
                    
            if going == "User":
                
                for i in range(len(eliteteamstatus)):
                    if enemypokemon == eliteteamstatus[i - 1]:
                        if eliteteamstatus[i] == "Confused":
                            print(enemypokemon,"is already confused")
                        if eliteteamstatus[i] != "Confused":
                            eliteteamstatus[i] = "Confused"
                            EnemyConfuse = "yes"
                            
        
        if "Paralyze" in moves[movenumber]["effect"]:
            if going == "Enemy":
                
                for i in range(len(userpartystatus)):
                    if currentpokemon == userpartystatus[i - 1]:
                        if userpartystatus[i] == "Paralyzed":
                            print(currentpokemon, "is already paralyzed")
                        if userpartystatus[i] != "Paralyzed":
                            oneting = currentspeedph / 100
                            currentspeed = oneting * 25
                            currentspeed = round(currentspeed)
                            userpartystatus[i] = "Paralyzed"
                            PrintParalyzed = "yes"
                            
                            
                            
                    
            if going == "User":
                
                for i in range(len(eliteteamstatus)):
                    if enemypokemon == eliteteamstatus[i - 1]:
                        if eliteteamstatus[i] == "Paralyzed":
                            print(enemypokemon,"is already paralyzed")
                        if eliteteamstatus[i] != "Paralyzed":
                            baker = enemyspeedph / 100
                            enemyspeed = baker * 25
                            enemyspeed = round(enemyspeed)
                            eliteteamstatus[i] = "Paralyzed"
                            EnemyParalyzed = "yes"
                            

        if "1in3Paralyze" in moves[movenumber]["effect"]:
            cheese = random.randrange(3)
            if cheese == 1:
                if going == "Enemy":
                
                    for i in range(len(userpartystatus)):
                        if currentpokemon == userpartystatus[i - 1]:
                            if userpartystatus[i] == "Paralyzed":
                                print(currentpokemon, "is already paralyzed")
                            if userpartystatus[i] != "Paralyzed":
                                oneting = currentspeedph / 100
                                currentspeed = oneting * 25
                                currentspeed = round(currentspeed)
                                userpartystatus[i] = "Paralyzed"
                                PrintParalyzed = "yes"
                                
                            
                            
                    
                if going == "User":
                    
                    for i in range(len(eliteteamstatus)):
                        if enemypokemon == eliteteamstatus[i - 1]:
                            if eliteteamstatus[i] == "Paralyzed":
                                print(enemypokemon,"is already paralyzed")
                            if eliteteamstatus[i] != "Paralyzed":
                                baker = enemyspeedph / 100
                                enemyspeed = baker * 25
                                enemyspeed = round(enemyspeed)
                                eliteteamstatus[i] = "Paralyzed"
                                EnemyParalyzed = "yes"
                            
            
        return damage
      
    def Miss(move, evasive, enemyevasive, going):
        
        global Diditmiss
        Diditmiss = "no"
        global runspecial
        runspecial = "yes"

        mistynumber = 110
        if going == "Enemy":
            if enemyevasive == 1:
                mistynumber = 140
            if enemyevasive == 2:
                mistynumber = 160
            if enemyevasive == 3:
                mistynumber = 180
            if enemyevasive == 4:
                mistynumber = 200
            if enemyevasive > 4:
                mistynumber = 220
            
            

        if going == "User":
            if evasive == 1:
                mistynumber = 140
            if evasive == 2:
                mistynumber = 160
            if evasive == 3:
                mistynumber = 180
            if evasive == 4:
                mistynumber = 200
            if evasive > 4:
                mistynumber = 220

        
        
        if move != "Nothing":
            for i in range(movelist):
                if move == moves[i]["name"]:
                    accuracy = moves[i]["accuracy"]
            Misty = random.randrange(mistynumber)
            print(Misty, "misty")
            if Misty > accuracy:
                Diditmiss = "yes"
                runspecial = "no"
                


    def checks(oppositepokemon):
        global enemypokemon
        global enemyspeed
        global enemyhealth
        global enemymove
        global shouldiswitch
        global evasive
        global enemyattackup
        global enemyattackdown
        if Trapped != "yes":
            print("checks is running")
            for i in range(pokemonlist):
                if data[i]["Name"] == enemypokemon:
                    Types = data[i]["Types"]
            functionality.typechart(enemypokemon, oppositepokemon)
            print(matchup, matchup1)
            print("matchup")
            

            for i in range(pokemonlist):
                if data[i]["Name"] == "Raichu":
                    RTypes = data[i]["Types"]
            for i in range(pokemonlist):
                if data[i]["Name"] == "Dragonite":
                    DTypes = data[i]["Types"]
            for i in range(pokemonlist):
                if data[i]["Name"] == "Charizard":
                    CTypes = data[i]["Types"]
            for i in range(pokemonlist):
                if data[i]["Name"] == "Gengar":
                    GTypes = data[i]["Types"]
            for i in range(pokemonlist):
                if data[i]["Name"] == "Blastoise":
                    BTypes = data[i]["Types"]
            for i in range(pokemonlist):
                if data[i]["Name"] == "Machamp":
                    MTypes = data[i]["Types"]

            #type chart code for each, make variable each specific pokemons effectiveness
            #for range of 6 or 5- if variablle equals super, then repeat with normal

            if matchup == "half" or matchup == "zero" or matchup1 == "half" or matchup1 == "zero":
                functionality.typechart("Raichu", oppositepokemon)
                R = matchup
                R1 = matchup1
                
                functionality.typechart("Dragonite", oppositepokemon)
                D = matchup
                D1 = matchup1
                
                functionality.typechart("Charizard", oppositepokemon)
                C = matchup
                C1 = matchup1
                
                functionality.typechart("Gengar", oppositepokemon)
                G = matchup
                G1 = matchup1
            
                functionality.typechart("Blastoise", oppositepokemon)
                B = matchup
                B1 = matchup1
                
                functionality.typechart("Machamp", oppositepokemon)
                M = matchup
                M1 = matchup1
                print("Raichu",R,R1,"Dragonite",D,D1,"Charizard",C,C1,"Genhar",G,G1,"Blastoise",B,B1,"Machamp",M,M1)
                if "Raichu" not in Mikesdeadguys:
                    if R != "half" and R != "zero" and R != "normal" or R1 != "normal" and R1 != "half" and R1 != "zero" and enemypokemon != "Raichu":
                        enemypokemon = "Raichu"
                        for i in range(pokemonlist):
                            for i in range(len(data)):
                                if enemypokemon == data[i]["Name"]:
                                    enemyspeed = data[i]["Speed Stat"]
                                    enemyhealth = data[i]["Health Stat"]
                        print("Mike M switched into", enemypokemon)
                        shouldiswitch = "yes"
                        enemymove = "Nothing"
                        evasive = 0
                        enemyattackup = 1
                        enemyattackdown = 1
                        return enemypokemon

                elif "Dragonite" not in Mikesdeadguys:
                    if D != "half" and D != "zero" and D != "normal" or D1 != "normal" and D1 != "half" and D1 != "zero":
                        enemypokemon = "Dragonite"
                        for i in range(pokemonlist):
                            if enemypokemon == data[i]["Name"]:
                                enemyspeed = data[i]["Speed Stat"]
                                enemyhealth = data[i]["Health Stat"]
                        print("Mike M switched into Dragonite")
                        print(Mikesdeadguys)
                        shouldiswitch = "yes"
                        enemymove = "Nothing"
                        evasive = 0
                        enemyattackup = 1
                        enemyattackdown = 1
                        return enemypokemon

                elif "Charizard" not in Mikesdeadguys:
                    if C != "half" and C != "zero" and C != "normal" or C1 != "normal" and C1 != "half" and C1 != "zero":
                        enemypokemon = "Charizard"
                        for i in range(pokemonlist):
                            if enemypokemon == data[i]["Name"]:
                                enemyspeed = data[i]["Speed Stat"]
                                enemyhealth = data[i]["Health Stat"]
                        print("Mike M switched into Charizard")
                        shouldiswitch = "yes"
                        enemymove = "Nothing"
                        evasive = 0
                        enemyattackup = 1
                        enemyattackdown = 1
                        return enemypokemon

                elif "Gengar" not in Mikesdeadguys:
                    if G != "half" and G != "zero" and G != "normal" or G1 != "normal" and G1 != "half" and G1 != "zero":
                        enemypokemon = "Gengar"
                        for i in range(pokemonlist):
                            if enemypokemon == data[i]["Name"]:
                                enemyspeed = data[i]["Speed Stat"]
                                enemyhealth = data[i]["Health Stat"]
                        print("Mike M switched into Gengar")
                        shouldiswitch = "yes"
                        enemymove = "Nothing"
                        evasive = 0
                        enemyattackup = 1
                        enemyattackdown = 1
                        return enemypokemon

                elif "Blastoise" not in Mikesdeadguys:
                    if B != "half" and B != "zero" and B != "normal" or B1 != "normal" and B1 != "half" and B1 != "zero":
                        enemypokemon = "Blastoise"
                    
                        for i in range(pokemonlist):
                            if enemypokemon == data[i]["Name"]:
                                enemyspeed = data[i]["Speed Stat"]
                                enemyhealth = data[i]["Health Stat"]
                    
                        print("Mike M switched into Blastoise")
                
                        shouldiswitch = "yes"
                        enemymove = "Nothing"
                        evasive = 0
                        enemyattackup = 1
                        enemyattackdown = 1
                        return enemypokemon
                    

                elif "Machamp" not in Mikesdeadguys:
                    if M != "half" and M != "zero" and M != "normal" or M1 != "normal" and M1 != "half" and M1 != "zero":
                        enemypokemon = "Machamp"
                        for i in range(pokemonlist):
                            if enemypokemon == data[i]["Name"]:
                                enemyspeed = data[i]["Speed Stat"]
                                enemyhealth = data[i]["Health Stat"]
                        print("Mike M switched into Machamp")
                        shouldiswitch = "yes"
                        enemymove = "Nothing"
                        evasive = 0
                        enemyattackup = 1
                        enemyattackdown = 1
                        return enemypokemon
        if Trapped == "yes":
            shouldiswitch = "no"
            #else: 
                #caniswitch = "no"
                #while caniswitch == "no":
                 #   p = random.randrange(6)
                  #  if p == 1 and "Raichu" not in Mikesdeadguys and enemypokemon != "Raichu":
                   #      enemypokemon = "Raichu"
                    #     print("Mike M switched into", enemypokemon)
                     #    shouldiswitch = "yes"
                      #   caniswitch = "yes"
                    #if p == 2 and "Dragonite" not in Mikesdeadguys and enemypokemon != "Dragonite":
                     #   enemypokemon = "Dragonite"
                      #  print("Mike M switched into Dragonite")
                       # shouldiswitch = "yes"
                        #caniswitch = "yes"
                    #if p == 3 and "Charizard" not in Mikesdeadguys and enemypokemon != "Charizard":
                     #   enemypokemon = "Charizard"
                      #  print("Mike M switched into Charizard")
                       # shouldiswitch = "yes"
                        #caniswitch = "yes"
                    #if p == 4 and "Gengar" not in Mikesdeadguys and enemypokemon != "Gengar":
                     #   enemypokemon = "Gengar"
                      #  print("Mike M switched into Gengar")
                       # shouldiswitch = "yes"
                        #caniswitch = "yes"
                    #if p == 5 and "Blastoise" not in Mikesdeadguys and enemypokemon != "Blastoise":
                     #   enemypokemon = "Blastoise"
                      #  print("Mike M switched into Blastoise")
                       # shouldiswitch = "yes"
                        #caniswitch = "yes"
                    #if p == 6 and "Machamp" not in Mikesdeadguys and enemypokemon != "Machamp":
                     #   enemypokemon = "Machamp"
                      #  print("Mike M switched into Machamp")
                       # shouldiswitch = "yes"
                        #caniswitch = "yes"
              

    def Mikesdeadpks(enemyhealt, oppositepokemon):
        global enemypokemon
        global enemyhealth
        global enemyspeed
        if enemyhealt == 0:
            print(enemypokemon, "has fainted")
            Mikesdeadguys.append(enemypokemon)
            print(Mikesdeadguys)
            
            functionality.typechart("Raichu", oppositepokemon)
            R = matchup
            functionality.typechart("Dragonite", oppositepokemon)
            D = matchup
            functionality.typechart("Charizard", oppositepokemon)
            C = matchup
            functionality.typechart("Gengar", oppositepokemon)
            G = matchup
            functionality.typechart("Blastoise", oppositepokemon)
            B = matchup
            functionality.typechart("Machamp", oppositepokemon)
            M = matchup
            if "Raichu" not in Mikesdeadguys:
                
                enemypokemon = "Raichu"
                for i in range(len(data)):
                  if enemypokemon == (data[i]["Name"]):
                      enemyspeed = (data[i]["Speed Stat"])
                      enemyhealth = (data[i]["Health Stat"])
                print("Mike M switched into", enemypokemon)
                shouldiswitch = "yes"
                return enemypokemon

            elif "Dragonite" not in Mikesdeadguys:
                enemypokemon = "Dragonite"
                for i in range(len(data)):
                  if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Dragonite")
                shouldiswitch = "yes"
                return enemypokemon

            elif "Charizard" not in Mikesdeadguys:
                enemypokemon = "Charizard"
                for i in range(len(data)):
                  if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Charizard")
                shouldiswitch = "yes"
                return enemypokemon

            elif "Gengar" not in Mikesdeadguys:
                enemypokemon = "Gengar"
                for i in range(len(data)):
                  if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Gengar")
                shouldiswitch = "yes"
                return enemypokemon

            elif "Blastoise" not in Mikesdeadguys:
                enemypokemon = "Blastoise"
                for i in range(len(data)):
                  if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Blastoise")
                shouldiswitch = "yes"
                return enemypokemon

            elif "Machamp" not in Mikesdeadguys:
                enemypokemon = "Machamp"
                for i in range(len(data)):
                  if enemypokemon == data[i]["Name"]:
                        enemyspeed = data[i]["Speed Stat"]
                        enemyhealth = data[i]["Health Stat"]
                print("Mike M switched into Machamp")
                shouldiswitch = "yes"
                return enemypokemon

            elif len(Mikesdeadguys) == 6:
              print("Mike has no more pokemon left")
            else: 
                caniswitch = "no"
                while caniswitch == "no":
                    p = random.randrange(6)
                    if p == 1 and "Raichu" not in Mikesdeadguys:
                         enemypokemon = "Raichu"
                         print("Mike M switched into", enemypokemon)
                         shouldiswitch = "yes"
                         caniswitch = "yes"
                    if p == 2 and "Dragonite" not in Mikesdeadguys:
                        enemypokemon = "Dragonite"
                        print("Mike M switched into Dragonite")
                        shouldiswitch = "yes"
                        caniswitch = "yes"
                    if p == 3 and "Charizard" not in Mikesdeadguys:
                        enemypokemon = "Charizard"
                        print("Mike M switched into Charizard")
                        shouldiswitch = "yes"
                        caniswitch = "yes"
                    if p == 4 and "Gengar" not in Mikesdeadguys:
                        enemypokemon = "Gengar"
                        print("Mike M switched into Gengar")
                        shouldiswitch = "yes"
                        caniswitch = "yes"
                    if p == 5 and "Blastoise" not in Mikesdeadguys:
                        enemypokemon = "Blastoise"
                        print("Mike M switched into Blastoise")
                        shouldiswitch = "yes"
                        caniswitch = "yes"
                    if p == 6 and "Machamp" not in Mikesdeadguys:
                        enemypokemon = "Machamp"
                        print("Mike M switched into Machamp")
                        shouldiswitch = "yes"
                        caniswitch = "yes"
              







class Mike(functionality):
    MikeTeam = ["Raichu", "Dragonite", "Charizard", "Gengar", "Blastoise", "Machamp"]










    def Raichudoing(turn, enemypokemon,currentpokemon):
        global enemymove
        #print(turn,"turn at start of raichu doing")
        Rmoves = ["Double Team", "Toxic", "Thunderbolt", "Surf"]
        
        
        for i in range(pokemonlist):
            if data[i]["Name"] == currentpokemon:
                oscar = i
        Alek = data[oscar]["Types"][0]
        if turn == 1:
           
            for i in range(pokemonlist):
                if (data[i]["Name"]) == currentpokemon:
                    ptype = (data[i]["Types"])
            if "Poison" not in ptype:
                #print("Raichu used Toxic")
                enemymove = "Toxic"

            else:
                enemymove = "Double Team"
                #print("Raichu used Double Team")
            

        if turn != 1:
            
        
            enemypokemon = functionality.checks(currentpokemon)
            
            if shouldiswitch != "yes":
                functionality.supereffective("why", "Thunderbolt", Alek)
                if effective == "super":
                    enemymove = "Thunderbolt"
                    #print("Raichu used Thunderbolt")

                if effective != "super":
                    functionality.supereffective("why", "Surf", Alek)
                    if effective == "super":
                        enemymove = "Surf"
                        #print("Raichu used Surf")

                    if effective != "super":
                        for i in range(len(userpartystatus)):
                            if currentpokemon == userpartystatus[i - 1]:
                                z = userpartystatus[i]
                                print(z)
                                if z == "None":
                                    enemymove = "Toxic"
                        
                                if z != "None":
                                    e = random.randrange(4)
                                    print(e,"random number")
                                    if e == 1 or e == 4:
                                        enemymove = "Double Team"
                                            #print("Raichu used Double Team")

                                    if e == 2 or e == 0:
                                        enemymove = "Thunderbolt"
                                            #print("Raichu used Thunderbolt")

                                    if e == 3:
                                        enemymove = "Surf"
                                            #print("Raichu used Surf")
            
            return enemypokemon
            


    def DragoniteDoing(turn,currentpokemon):
        global enemymove
        global enemypokemon
        Dmoves = ["Agility", "Slam", "Fire Blast", "Blizzard"]
        for i in range(pokemonlist):
          if data[i]["Name"] == currentpokemon:
            oscar = i
        Alek = data[oscar]["Types"][0]

        functionality.checks(currentpokemon)
        print(shouldiswitch,"\n shouldiswitch after Ddoing")
        if shouldiswitch != "yes":
            functionality.supereffective("why", "Fire Blast", Alek)
            if effective == "super":
                enemymove = "Fire Blast"
                #print("Raichu used Fire Blast")

            elif effective != "super":
                functionality.supereffective("why", "Blizzard", Alek)
                if effective == "super":
                    enemymove = "Blizzard"
                    #print("Raichu used Surf")

                elif effective != "super":
                    d = random.randrange(5)
                    print(d)
                    if d == 1 or d == 4:
                        enemymove = "Agility"
                        #print("Raichu used Agility")

                    if d == 2:
                        enemymove = "Slam"
                        #print("Raichu used Thunderbolt")

                    if d == 3 or d == 0:
                        enemymove = "Fire Blast"
                        #print("Raichu used Surf")

                    if d == 5:
                        enemymove = "Blizzard"

    def Charizarddoing(turn,currentpokemon):
        global enemymove
        global enemypokemon
        Cmoves = ["Swords Dance", "Mega Punch", "Earthquake", "Strength"]
        for i in range(pokemonlist):
          if data[i]["Name"] == currentpokemon:
            oscar = i
        Alek = data[oscar]["Types"][0]
        
        functionality.checks(currentpokemon)
        if shouldiswitch != "yes":
            functionality.supereffective("why", "Mega Punch", Alek)
            if effective == "super":
                enemymove = "Mega Punch"
                    #print("Raichu used Fire Blast")

            if effective != "super":
                functionality.supereffective("why", "Earthquake", Alek)
                if effective == "super":
                    enemymove = "Earthquake"
                        #print("Raichu used Surf")

                if effective != "super":
                    functionality.supereffective("why", "Strength", Alek)
                    if effective == "super":
                            enemymove = "Strength"

                    if effective != "super":
                        c = random.randrange(5)
                        print(c)
                        if c == 1:
                            enemymove = "Mega Punch"
                                #print("Raichu used Agility")

                        if c == 2:
                            enemymove = "Earthquake"
                                #print("Raichu used Thunderbolt")

                        if c == 3:
                            enemymove = "Strength"
                                #print("Raichu used Surf")
                            
                        if c == 4 or c == 5 or c == 0:
                            enemymove = "Swords Dance"

    def Gengardoing(currentpokemon):
        global enemymove
        global enemypokemon
        Gmoves = ["Mega Drain", "Hypnosis", "Dream Eater", "Psychic"]
        for i in range(pokemonlist):
          if data[i]["Name"] == currentpokemon:
            oscar = i
        Alek = data[oscar]["Types"][0]

        functionality.checks(currentpokemon)
        if shouldiswitch != "yes":
            functionality.supereffective("why", "Psychic", Alek)
            if effective == "super":
                enemymove = "Psychic"
                #print("Raichu used Fire Blast")

            if effective != "super":
                functionality.supereffective("why", "Mega Drain", Alek)
                if effective == "super":
                    enemymove = "Mega Drain"
                if effective != "super":
                    for i in range(len(userpartystatus)-1):
                        if currentpokemon == userpartystatus[i - 1]:
                            y = userpartystatus[i]
                            if y == "Asleep":
                                enemymove = "Dream Eater"
                            if y != "Asleep":
                                enemymove = "Hypnosis"

                            else:
                                v = random.randrange(2)
                                print(v)
                                if v == 1:
                                    enemymove = "Mega Drain"
                                if v == 2 or v == 0:
                                    enemymove = "Psychic"
                                #print("Raichu used Agility")

    def Blastoisedoing(turn,currentpokemon):
        global enemymove
        global enemypokemon
        #print(currentpokemon, "currentpokemon at start of blastoise doing")
        Bmoves = ["Hydro Pump", "Toxic", "Bite", "Ice Beam"]
        for i in range(pokemonlist):
          if data[i]["Name"] == currentpokemon:
            oscar = i
        Alek = data[oscar]["Types"][0]
        functionality.checks(currentpokemon)
        if shouldiswitch != "yes":
                functionality.supereffective("why", "Hydro Pump", Alek)
                #print(effective, "effective in balstoise doing after supereffective")
                if effective == "super":
                    enemymove = "Hydro Pump"
                    #print("Raichu used Fire Blast")

                if effective != "super":
                    functionality.supereffective("why", "Bite", Alek)
                    if effective == "super":
                        enemymove = "Bite"
                        #print("Raichu used Surf")

                    if effective != "super":
                        functionality.supereffective("why", "Ice Beam", Alek)
                        if effective == "super":
                                enemymove = "Ice Beam"

                        if effective != "super":
                            #print("not super")
                            for i in range(len(userpartystatus)-1):
                                if currentpokemon == userpartystatus[i - 1]:
                                    x = userpartystatus[i]
                                    if x == "None":
                                        enemymove = "Toxic"
                                    if x != "None":

                                        b = random.randrange(3)
                                        #print(b,"Pleses beee here")
                                        if b == 1 or b == 0:
                                            enemymove = "Hydro Pump"
                                            #print("Raichu used Agility")

                                        if b == 2:
                                            enemymove = "Bite"
                                            #print("Raichu used Thunderbolt")

                                        if b == 3:
                                            enemymove = "Ice Beam"
                                        #print("Raichu used Surf")
    def Machampdoing(currentpokemon):
        global enemymove
        global enemypokemon
        Mmoves = ["Body Slam", "Earthquake", "Rock Slide", "Hyper Beam"]
        for i in range(pokemonlist):
          if data[i]["Name"] == currentpokemon:
            oscar = i
        Alek = data[oscar]["Types"][0]
        functionality.checks(currentpokemon)
        if shouldiswitch != "yes":
                functionality.supereffective("why", "Body Slam", Alek)
                if effective == "super":
                    enemymove = "Body Slam"
                    #print("Raichu used Fire Blast")

                if effective != "super":
                    functionality.supereffective("why", "Earthquake", Alek)
                    if effective == "super":
                        enemymove = "Earthquake"
                        #print("Raichu used Surf")

                    if effective != "super":
                        functionality.supereffective("why", "Rock Slide", Alek)
                        if effective == "super":
                            enemymove = "Rock Slide"

                        if effective != "super":
                            functionality.supereffective("why","Hyper Beam", Alek)
                            if effective == "super":
                                enemymove = "Hyper Beam"
                            if effective != "super":
                                m = random.randrange(4)
                                if m == 1 or m == 0:
                                    enemymove = "Body Slam"
                                    #print("Raichu used Agility")

                                if m == 2:
                                    enemymove = "Earthquake"
                                    #print("Raichu used Thunderbolt")

                                if m == 3:
                                    enemymove = "Rock Slide"
                                    #print("Raichu used Surf")

                                if m == 4:
                                    enemymove = "Hyper Beam"










class Schmovin(Mike):
    def Whosmovin(pokemon, currentpokemon):
        
        
      
        if pokemon == "Raichu":
            Mike.Raichudoing(turn, enemypokemon,currentpokemon)
        if pokemon == "Dragonite":
            Mike.DragoniteDoing(turn,currentpokemon)
        if pokemon == "Charizard":
            Mike.Charizarddoing(turn,currentpokemon)
        if pokemon == "Gengar":
            Mike.Gengardoing(currentpokemon)
        if pokemon == "Blastoise":
            Mike.Blastoisedoing(turn,currentpokemon)
        if pokemon == "Machamp":
            Mike.Machampdoing(currentpokemon)











#goingfirst = []
class Turns(Mike):

    def speedcheck(enemyspeed, currentspeed):
        global goingfirst
        if enemyspeed > currentspeed or enemyspeed == currentspeed:
            goingfirst = "Enemy"
        if currentspeed > enemyspeed:
            goingfirst = "User"

        print(goingfirst, "goingfirst after speedcheck")

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
                print("placeholder")



    def preturn(playerpokemon1, enemypokemon, enemy):
        print("You are challenged by", enemy)
        time.sleep(times)
        print("You threw out", playerpokemon1)
        time.sleep(0.5)
        print(enemy, "threw out", enemypokemon)
        time.sleep(times)
        global going
    def turn(currentpokemon, Kaifat):
        global unique
        global meffective
        global meffective1
        global meffective2
        global onetype
        global twotype
        global movedamage
        global uniquedamage
        global turn
        turn = 0

        global Diditmiss
        Diditmiss = "no"
        global runspecial
        runspecial = "yes"

        global PrintPoison
        global DoDamage
        global EnemyPoisoned

        PrintPoison = "no"
        DoDamage = "yes"
        EnemyPoisoned = "no"

        global Afterhealth
        Afterhealth = 0
        
        global shouldiswitch
        shouldiswitch = "no"
        global goingfirst
        goingfirst = "ABBA"

        global Diduniquedamagehappen
        Diduniquedamagehappen = "no"

        global Didithittwice
        Didithittwice = "no"

        global fourtydamagetrue
        fourtydamagetrue = "no"

        global itcounter
        global counterdamage
        itcounter = "no"

        global Flinching
        Flinching = "no"

        global PrintBurn
        PrintBurn = "no"
        global EnemyBurn
        EnemyBurn = "no"

        global Trappedturns
        global Trapped
        Trapped = "no"
        global startingturntrapped
        Trappedturns = 0
        startingturntrapped = 0

        global awaybeforehit
        awaybeforehit = "no"

        global itsfly
        itsfly = "no"
        global itsdig
        itsdig = "no"

        global hitsnextturn
        hitsnextturn = "no"

        global hityourself
        global enemyhititself
        hityourself = "no"
        enemyhititself = "no"
        global PrintConfuse
        global EnemyConfuse
        PrintConfuse = "no"
        EnemyConfuse = "no"

        global youPAR
        global enemyPAR
        youPAR = "no"
        enemyPAR = "no"
        global PrintParalyzed
        global EnemyParalyzed
        PrintParalyzed = "no"
        EnemyParalyzed = "no"

        global seeded
        seeded = "no"

        global evasive
        global enemyevasive
        evasive = 0
        enemyevasive = 0

        global enemyattackup
        enemyattackup = 1
        global userattackup
        userattackup = 1

        global enemyattackdown
        enemyattackdown = 1
        global userattackdown
        userattackdown = 1

        global yousleep
        global enemysleep
        yousleep = "no"
        enemysleep = "no"

        global lockedin
        global usedturn
        global gooblie
        global enemylockedin
        global enemyusedturn
        global fdd
        lockedin = "no"
        usedturn = 0
        gooblie = 0
        enemylockedin = "no"
        enemyusedturn = 0
        fdd = 0

        global enemycold
        enemycold = "no"
        global youcold
        youcold = "no"

        global mistactive
        mistactive = "no"

        global Lightscreen
        Lightscreen = "no"
        global Reflect
        Reflect = "no"

        global userspecialdown
        userspecialdown = 1
        global enemyspecialdown
        enemyspecialdown = 1

        global userdefenseup
        userdefenseup = 1

        global userspecialup
        global enemyspecialup
        userspecialup = 1
        enemyspecialup = 1

        global Recharging
        Recharging = "no"
        global previousturn
        previousturn = 0

        

        while Kaifat == "very":
            turn += 1
            #print(turn, "turn before")
            f = functionality()

            functionality.FlyandDiggimmick(currentpokemon)
            

            if awaybeforehit == "no":
                if hitsnextturn == "no":
                    
                    if Recharging == "no":
                        global enemyhealth
                        if lockedin == "no":
                            print("Switch Out Or Attack")
                            userdo = input("What would you like to do: ")
                        if lockedin == "yes":
                            userdo = "Attack"
                        if userdo == "Switch" or userdo == "switch" or userdo == "Switch Out" or userdo == "switch out" or userdo == "Switch out":
                            for i in range(len(userpartyhealth)):
                                if currentpokemon == userpartyhealth[i - 1]:
                                    currenthealth = userpartyhealth[i]
                            print(yourteam)
                            switchin = input("Pick a Pokemon to Switch into: ")
                            print("You switched into", switchin)
                            currentpokemon = switchin
                            enemyevasive = 0
                            userattackup = 1
                            userattackdown = 1
                            mistactive = "no"
                            Lightscreen = "no"
                            userspecialdown = 1
                            userspecialup = 1
                            for i in range(len(userpartyhealth)):
                                if currentpokemon == userpartyhealth[i - 1]:
                                    currenthealth = userpartyhealth[i]
                                    x = i
                                    
                            going = "Enemy"

                            functionality.Paralyze(enemypokemon)
                            functionality.Imatired(going)
                            functionality.coldgaming(going)


                            time.sleep(times)
                            #print(currentpokemon, "before whosmovin")
                            Schmovin.Whosmovin(enemypokemon, currentpokemon)
                            
                            
                            f.damagecalc(enemymove, enemypokemon, currentpokemon)
                            damage = movedamage

                            functionality.Miss(enemymove,evasive, enemyevasive, going)
                            if shouldiswitch == "no":
                                if enemyPAR != "no":
                                    DoDamage = "no"
                                    print(enemypokemon,"was unable to move due to its paralysis")
                                    runspecial = "no"
                                if enemysleep != "no":
                                    DoDamage = "no"
                                    print(enemypokemon,"is fast asleep")
                                    runspecial = "no"
                                if enemycold != "no":
                                    DoDamage ="no"
                                    print(enemypokemon, "is frozen solid")
                                    runspecial = "no"
                            if runspecial == "yes":
                                
                                f.specialeffect(enemymove,damage,enemyspeed,currentspeed, enemypokemon,currentpokemon, going, "placeholder", turn, enemyhealth)
                            
                            if Diduniquedamagehappen != "no":
                                movedamage = uniquedamage

                            if Didithittwice != "no":
                                movedamage = TwoHitDamage

                            if fourtydamagetrue != "no":
                                movedamage = 40

                            if itcounter != "no":
                                movedamage = counterdamage


                            #move effects end here

                            enemydamage = movedamage
                            
                            if enemydamage == currenthealth or enemydamage > currenthealth:
                                enemydamage = currenthealth
                            


                            if enemyPAR == "no" and enemysleep == "no" and enemycold == "no":
                                print(enemypokemon, "used", enemymove)
                                time.sleep(1)
                            
                            
                            if Diditmiss != "no":
                                enemydamage = 0
                                if DoDamage == "yes":
                                    print("But it missed!")
                                DoDamage = "no"
                                
                                
                            
                                    



                            if PrintPoison != "no":
                                    print(currentpokemon, "has been poisoned!")

                            if PrintBurn != "no":
                                print(currentpokemon, "was burned!" )
                            if PrintConfuse != "no":
                                print(currentpokemon, "is confused!")
                            if PrintParalyzed != "no":
                                print(currentpokemon, "was paralyzed")

                            if DoDamage == "yes":
                                functionality.Confuse(enemypokemon, enemydamage)
                                if enemyhititself == "no":
                                    time.sleep(1)
                                    
                                    if typesuper1 == True or typesuper2 == True or typesuper == True:
                                        print("It was supereffective!")
                                        time.sleep(0.5)
                                    print(enemypokemon, "did", enemydamage, "damage")
                                    if crithappen == True:
                                        print("It was a critical hit!")
                                        time.sleep(0.5)
                            
                                    currenthealth = currenthealth - enemydamage
                            print(currentpokemon, "has", currenthealth, "health left")
                            userpartyhealth[x] = currenthealth
                            if currenthealth == 0:
                                
                                for i in range(len(yourteam)-1):
                                    if currentpokemon == yourteam[i]:
                                        yourteam.remove(currentpokemon)
                                    
                                print(yourteam)
                                newpk = input("Who will you switch into? ")
                                for i in range(len(yourteam)):
                                    if newpk == yourteam[i]:
                                        currentpokemon = newpk
                                for i in range(len(userpartyhealth)):
                                    if currentpokemon == userpartyhealth[i - 1]:
                                        currenthealth = userpartyhealth[i]

                            functionality.hedobetrapped(startingturntrapped,Trappedturns,turn)

                            if seeded == "yes":
                                for i in range(pokemonlist):
                                    if enemypokemon == data[i]["Name"]:
                                        start = data[i]["Health Stat"]
                                seedgaming = start/16
                                damage = round(seedgaming)
                                if damage == enemyhealth or damage > enemyhealth:
                                    damage = enemyhealth
                                enemyhealth = enemyhealth - damage
                                
                                print(enemypokemon, "had its health sapped by Leech Seed")
                                time.sleep(times)
                                print(enemypokemon,"has", enemyhealth, "health left")

                                for i in range(pokemonlist):
                                    if currentpokemon == data[i]["Name"]:
                                        fail = data[i]["Health Stat"]
                                if currenthealth != fail:
                                    currenthealth += damage
                                    if currenthealth == fail or currenthealth > fail:
                                        currenthealth = fail
                                print(currentpokemon, "recovered", damage,"health")
                                time.sleep(times)
                                print(currentpokemon, "has", currenthealth,"health")
                                for i in range(len(userpartyhealth)):
                                    if currentpokemon == userpartyhealth[i-1]:
                                        userpartyhealth[i] = currenthealth
                                        

                            PrintPoison = "no"
                            EnemyPoisoned = "no"
                            shouldiswitch = "no"
                            DoDamage = "yes"
                            Diduniquedamagehappen = "no"
                            Didithittwice = "no"
                            fourtydamagetrue = "no"
                            itcounter = "no"
                            Diditmiss = "no"
                            runspecial = "yes"
                            Flinching = "no"
                            PrintBurn = "no"
                            EnemyBurn = "no"
                            hityourself = "no"
                            enemyhititself = "no"
                            PrintConfuse = "no"
                            EnemyConfuse = "no"
                            PrintParalyzed = "no"
                            EnemyParalyzed = "no"
                            
                            
                            

                        if len(yourteam) == 0:
                            Kaifat = "no"
                    

                if hitsnextturn != "no":
                    userdo = "Attack"
                if Recharging == "yes":
                        
                    userdo = "Atatck"
                    print(currentpokemon,"has to recharge")
                
                if userdo == "Attack" or userdo == "attack":
                    for i in range(len(userpartyhealth)):
                        if currentpokemon == userpartyhealth[i - 1]:
                            currenthealth = userpartyhealth[i]
                    #print(currenthealth, "start")
                    if hitsnextturn == "no":
                        if Recharging == "no":
                            if lockedin == "no":
                                for i in range(inputteamlist):
                                    if currentpokemon == inputteam[i - 1]:
                                        currentmoves = inputteam[i]
                                        print(currentmoves)
                            
                                use = input("Pick a move to use: ")
                                functionality.speedstages(use,currentspeed)
                        if Recharging == "yes":
                            DoDamage = "no"
                        

                    time.sleep(times)
                    print(enemyspeed, currentspeed, "enemyspeed and current speed before check")
                    Turns.speedcheck(enemyspeed, currentspeed)

                    if goingfirst == 'User':
                        going = "User"

                        functionality.Paralyze(currentpokemon)
                        functionality.Imatired(going)
                        functionality.coldgaming(going)
                        
                        
                        if youPAR == "no" and yousleep == "no" and youcold == "no":
                            going = "User"
                            print("You used", use)

                        if youPAR != "no":
                            DoDamage = "no"
                            print(currentpokemon,"was unable to move due to its paralysis")
                            runspecial = "no"
                        
                        if yousleep != "no":
                            DoDamage = "no"
                            print(currentpokemon,"is fast asleep")
                            runspecial = "no"
                        
                        if youcold != "no":
                            DoDamage = "no"
                            print(currentpokemon, "is frozen solid")
                            runspecial = "no"

                        time.sleep(times)
                        # if move effect != None
                        #Do effect\
                        f = functionality()
                        for i in range(len(currentmoves)):
                            if currentmoves[i]== use:
                            
                                f.damagecalc(use, currentpokemon, enemypokemon)
                                damage = movedamage
                                functionality.Miss(use,evasive, enemyevasive, going)
                                if youPAR != "no":
                                    DoDamage = "no"
                                    print(currentpokemon,"was unable to move due to its paralysis")
                                    runspecial = "no"
                                
                                if yousleep != "no":
                                    DoDamage = "no"
                                    print(currentpokemon,"is fast asleep")
                                    runspecial = "no"
                                
                                if youcold != "no":
                                    DoDamage = "no"
                                    print(currentpokemon, "is frozen solid")
                                    runspecial = "no"

                                if runspecial == "yes":
                                    
                                    f.specialeffect(use, damage, enemyspeed,currentspeed,enemypokemon, currentpokemon, going, "placeholder", turn, enemyhealth)
                                
                                if Diduniquedamagehappen != "no":
                                    damage = uniquedamage

                                if Didithittwice != "no":
                                    damage = TwoHitDamage

                                if fourtydamagetrue != "no":
                                    damage = 40

                                if itcounter != "no":
                                    damage = counterdamage

                                if awaybeforehit == "yes":
                                    damage = 0
                                
                                if use == "Mirror Move":
                                    f.damagecalc(enemymove, currentpokemon, enemypokemon)
                                    damage = movedamage
                                    print(currentpokemon, "mirrored", enemymove)
                                    use = enemymove
                                    f.specialeffect(use, damage, enemyspeed,currentspeed, enemypokemon, currentpokemon, going, enemydamage, turn, enemyhealth)
                                    
                                    
                                if hitsnextturn == "yes":
                                    if use == "Sky Attack":
                                        print(currentpokemon, "started to glow!")
                                    if use == "Solar Beam":
                                        print(currentpokemon,"is absorbing sunlight")

                                #effects end here

                                if damage == enemyhealth or damage > enemyhealth:
                                    damage = enemyhealth

                                if Diditmiss != "no":
                                    damage = 0
                                    if DoDamage == "yes":
                                        print("But it missed!")
                                    DoDamage = "no"
                                    
                                    if use == "Hi Jump Kick" or use == "Jump Kick":
                                        f.damagecalc(use, currentpokemon, enemypokemon)
                                        damage = movedamage
                                        currenthealth = currenthealth - damage
                                        print(currentpokemon, "took", damage, "damage due to recoil")
                                        print(currentpokemon, "has", currenthealth, "health left")
                                    damage = 0


                                if EnemyPoisoned != "no":
                                    print(enemypokemon, "was poisoned!")
                                if EnemyBurn != "no":
                                    print(enemypokemon, "was burned!")
                                if EnemyConfuse != "no":
                                    print(enemypokemon, "is confused!")
                                if EnemyParalyzed != "no":
                                    print(enemypokemon, "was paralyzed")

                                if DoDamage == "yes":
                                    functionality.Confuse(currentpokemon, damage)
                                    if hityourself == "no":
                                        time.sleep(1)
                                        if typesuper1 == True or typesuper2 == True or typesuper == True:
                                            print("It was supereffective!")
                                            time.sleep(0.5)
                                        print("It did", damage, "damage")
                                        if crithappen == True:
                                            print("It was a critical hit!")
                                            time.sleep(0.5)
                                        
                                        enemyhealth = enemyhealth - damage
                                        if use == "Explosion":
                                            currenthealth = 0
                                            print(currentpokemon,"died because it exploded")
                                            time.sleep(1)
                                            if currenthealth == 0:
                                                for i in range(len(yourteam)-1):
                                                    if currentpokemon == yourteam[i]:
                                                        yourteam.remove(currentpokemon)
                                                print(yourteam)
                                                newpk = input("Who will you switch into? ")
                                                for i in range(len(yourteam)):
                                                    if newpk == yourteam[i]:
                                                        currentpokemon = newpk
                                                for i in range(len(userpartyhealth)):
                                                    if currentpokemon == userpartyhealth[i - 1]:
                                                        currenthealth = userpartyhealth[i]

                                time.sleep(times)
                                if enemyhealth > 0:
                                    print(enemypokemon, "has", enemyhealth, "health left")
                                #print(enemypokemon)
                                if enemyhealth == 0:
                                    print(enemypokemon, "fainted")
                        enemypartyhealth[1] = enemyhealth
                        
                        functionality.Mikesdeadpks(enemyhealth, currentpokemon)
                        #print(enemypokemon)
                        if len(Mikesdeadguys) == 6:
                            Kaifat = "no"
                        functionality.keepusing(usedturn, gooblie)
                        going = "Enemy"

                        PrintPoison = "no"
                        DoDamage = "yes"
                        EnemyPoisoned = "no"
                        shouldiswitch = "no"
                        goingfirst = "ABBA"
                        Diduniquedamagehappen = "no"
                        Didithittwice = "no"
                        fourtydamagetrue = "no"
                        itcounter = "no"
                        Diditmiss = "no"
                        runspecial = "yes"
                        PrintBurn = "no"
                        EnemyBurn = "no"
                        PrintConfuse = "no"
                        EnemyConfuse = "no"
                        PrintParalyzed = "no"
                        EnemyParalyzed = "no"
                        #Flinching = "no"

                        functionality.Paralyze(enemypokemon)
                        functionality.Imatired(going)
                        functionality.coldgaming(going)

                        time.sleep(times)
                        if Flinching == "no":
                            Schmovin.Whosmovin(enemypokemon,currentpokemon)
                            
                            #Mike.Raichudoing(turn)
                            f.damagecalc(enemymove, enemypokemon, currentpokemon)
                            functionality.Miss(enemymove,evasive, enemyevasive, going)
                            if shouldiswitch == "no":
                                if enemyPAR != "no":
                                    DoDamage = "no"
                                    print(enemypokemon,"was unable to move due to its paralysis")
                                    runspecial = "no"
                                if enemysleep != "no":
                                    DoDamage = "no"
                                    print(enemypokemon,"is fast asleep")
                                    runspecial = "no"
                                if enemycold != "no":
                                    DoDamage = "no"
                                    print(enemypokemon, "is frozen solid")
                                    runspecial = "no"

                            if runspecial == "yes":
                                
                                f.specialeffect(enemymove,damage,enemyspeed,currentspeed,enemypokemon,currentpokemon, going, "placeholder", turn, enemyhealth)
                            
                            if Diduniquedamagehappen != "no":
                                movedamage = uniquedamage

                            if Didithittwice != "no":
                                movedamage = TwoHitDamage

                            if fourtydamagetrue != "no":
                                movedamage = 40

                            if itcounter != "no":
                                movedamage = counterdamage

                            if awaybeforehit == "no":
                                #effects end here

                                enemydamage = movedamage
                                #print(currenthealth, "after calc")
                                #for i in range(len(userpartyhealth)):
                                #   if currentpokemon == userpartyhealth[i - 1]:
                                #      currenthealth = userpartyhealth[i]
                                #print(enemydamage, "enemydamage after damage calc")
                                if enemydamage == currenthealth or enemydamage > currenthealth:
                                    enemydamage = currenthealth
                                    #print(enemydamage, "enemydamage after == or > than")
                                
                                if enemyPAR == "no" and enemysleep == "no" and enemycold == "no":
                                    print(enemypokemon, "used", enemymove)
                                    time.sleep(times)

                                if Diditmiss != "no":
                                    enemydamage = 0
                                    if DoDamage == "yes":
                                        print("But it missed!")
                                    DoDamage = "no"
                                    
                                    if enemymove == "Hi Jump Kick" or use == "Jump Kick":
                                        f.damagecalc(enemymove, enemypokemon, currentpokemon)
                                        enemydamage = movedamage
                                        enemyhealth = enemyhealth - enemydamage
                                        print(enemypokemon, "took", enemydamage, "damage due to recoil")
                                        print(enemypokemon, "has", enemyhealth, "health left")
                                    enemydamage = 0
                

                                if PrintPoison != "no":
                                    print(currentpokemon, "has been poisoned!")
                                if PrintBurn != "no":
                                    print(currentpokemon, "was burned!" )
                                if PrintConfuse != "no":
                                    print(currentpokemon, "is confused!")
                                if PrintParalyzed != "no":
                                    print(currentpokemon, "was paralyzed")
                                if DoDamage == "yes":
                                    functionality.Confuse(enemypokemon, enemydamage)
                                    if enemyhititself == "no":
                                        time.sleep(1)
                                        if typesuper1 == True or typesuper2 == True or typesuper == True:
                                            print("It was supereffective!")
                                            time.sleep(0.5)
                                        print(enemypokemon, "did", enemydamage, "damage")
                                        if crithappen == True:
                                            print("It was a critical hit!")
                                            time.sleep(0.5)
                                        
                                        #health already reset at this point
                                        currenthealth -= enemydamage
                                #print(currenthealth, "after")
                            if awaybeforehit != "no":
                                print(enemypokemon, "used", enemymove)
                                time.sleep(times)
                                if DoDamage == "yes":
                                    print("But it missed!")


                        if Flinching != "no":
                            print(enemypokemon, "flinched and couldn't move")
                        time.sleep(times)
                        print(currentpokemon, "has", currenthealth, "health left")
                        #here down = deaD
                        userpartyhealth[i] = currenthealth
                        if currenthealth == 0:
                            for i in range(len(yourteam)-1):
                                if currentpokemon == yourteam[i]:
                                    yourteam.remove(currentpokemon)
                            print(yourteam)
                            newpk = input("Who will you switch into? ")
                            for i in range(len(yourteam)):
                                if newpk == yourteam[i]:
                                    currentpokemon = newpk
                            for i in range(len(userpartyhealth)):
                                if currentpokemon == userpartyhealth[i - 1]:
                                    currenthealth = userpartyhealth[i]

                        #print(currenthealth, "before afflicted")
                        functionality.afflicted(N,M, currenthealth, currentpokemon)
                        functionality.Crispy(currentpokemon)

                        functionality.Mikesdeadpks(enemyhealth, currentpokemon)

                        for i in range(len(userpartystatus)):
                            if currentpokemon == userpartystatus[i - 1]:
                                if userpartystatus[i] == "Poison":
                                    currenthealth = Afterhealth
                        
                                    #print(currenthealth, "after afflicted")
                                    #print(Afterhealth, "after afflicted")
                                    #dead below
                                    for i in range(len(userpartyhealth)):
                                        if currentpokemon == userpartyhealth[i - 1]:
                                            userpartyhealth[i] = Afterhealth
                                    

                        PrintPoison = "no"
                        DoDamage = "yes"
                        EnemyPoisoned = "no"
                        shouldiswitch = "no"
                        goingfirst = "ABBA"
                        Diduniquedamagehappen = "no"
                        Didithittwice = "no"
                        fourtydamagetrue = "no"
                        itcounter = "no"
                        Diditmiss = "no"
                        runspecial = "yes"
                        Flinching = "no"
                        PrintBurn = "no"
                        EnemyBurn = "no"
                        hityourself = "no"
                        enemyhititself = "no"
                        PrintConfuse = "no"
                        EnemyConfuse = "no"
                        PrintParalyzed = "no"
                        EnemyParalyzed = "no"

                        if seeded == "yes":
                            for i in range(pokemonlist):
                                if enemypokemon == data[i]["Name"]:
                                    start = data[i]["Health Stat"]
                            seedgaming = start/16
                            damage = round(seedgaming)
                            if damage == enemyhealth or damage > enemyhealth:
                                damage = enemyhealth
                            enemyhealth = enemyhealth - damage
                            
                            print(enemypokemon, "had its health sapped by Leech Seed")
                            time.sleep(times)
                            print(enemypokemon,"has", enemyhealth, "health left")

                            for i in range(pokemonlist):
                                if currentpokemon == data[i]["Name"]:
                                    fail = data[i]["Health Stat"]
                            if currenthealth != fail:
                                currenthealth += damage
                                if currenthealth == fail or currenthealth > fail:
                                    currenthealth = fail
                            print(currentpokemon, "recovered", damage,"health")
                            time.sleep(times)
                            print(currentpokemon, "has", currenthealth,"health")
                            for i in range(len(userpartyhealth)):
                                if currentpokemon == userpartyhealth[i-1]:
                                    userpartyhealth[i] = currenthealth
                        

                        if currenthealth == 0:
                            for i in range(len(yourteam)-1):
                                if currentpokemon == yourteam[i]:
                                    yourteam.remove(currentpokemon)
                            print(yourteam)
                            newpk = input("Who will you switch into? ")
                            for i in range(len(yourteam)):
                                if newpk == yourteam[i]:
                                    currentpokemon = newpk
                            for i in range(len(userpartyhealth)):
                                if currentpokemon == userpartyhealth[i - 1]:
                                    currenthealth = userpartyhealth[i]
                        #print(currenthealth, "end")
                        if len(yourteam) == 0:
                            Kaifat = "no"
                        

                    functionality.hedobetrapped(startingturntrapped,Trappedturns,turn)

                    if goingfirst == "Enemy":
                        f = functionality()
                        going = "Enemy"
                        
                        #print("Before")
                        Schmovin.Whosmovin(enemypokemon,currentpokemon)
                        functionality.Paralyze(enemypokemon)
                        functionality.Imatired(going)
                        functionality.coldgaming(going)

                        
                    
                        #if he switches out he shouldnt also attack which is why
                        #enemymove isnt updating after the switch.
                        #Since he no attack, enemymove doesn't change but damage calc is still pulling the enemymove variable
                        global death
                        death = False
                        #print(shouldiswitch)
                        if shouldiswitch != "yes":
                            f.damagecalc(enemymove, enemypokemon, currentpokemon)
                            enemydamage = movedamage
                            functionality.Miss(enemymove,evasive, enemyevasive, going)
                            if shouldiswitch == "no":
                                if enemyPAR != "no":
                                    DoDamage = "no"
                                    print(enemypokemon,"was unable to move due to its paralysis")
                                    runspecial = "no"
                                if enemysleep != "no":
                                    DoDamage = "no"
                                    print(enemypokemon,"is fast asleep")
                                    runspecial = "no"
                                if enemycold != "no":
                                    DoDamage = "no"
                                    print(enemypokemon,"is frozen solid")
                                    runspecial = "no"

                            if runspecial == "yes":
                                
                                f.specialeffect(enemymove,enemydamage,enemyspeed,currentspeed,enemypokemon,currentpokemon, going, "placeholder", turn, enemyhealth)
                            
                            if Diduniquedamagehappen != "no":
                                enemydamage = uniquedamage

                            if Didithittwice != "no":
                                enemydamage = TwoHitDamage

                            if fourtydamagetrue != "no":
                                enemydamage = 40

                            if itcounter != "no":
                                enemydamage = counterdamage

                            #enemydamage = movedamage
                            for i in range(len(userpartyhealth)):
                                if currentpokemon == userpartyhealth[i - 1]:
                                    currenthealth = userpartyhealth[i]
                                    x = i
                            if enemydamage == currenthealth or enemydamage > currenthealth:
                                enemydamage = currenthealth
                            if enemyPAR == "no" and enemysleep == "no" and enemycold == "no":
                                print(enemypokemon, "used", enemymove)
                                time.sleep(times)

                            if Diditmiss != "no":
                                enemydamage = 0
                                if DoDamage == "yes":
                                    print("But it missed!")
                                DoDamage = "no"
                                
                                if enemymove == "Hi Jump Kick" or use == "Jump Kick":
                                    f.damagecalc(enemymove, enemypokemon, currentpokemon)
                                    enemydamage = movedamage
                                    enemyhealth = enemyhealth - enemydamage
                                    print(enemypokemon, "took", enemydamage, "damage due to recoil")
                                    print(enemypokemon, "has", enemyhealth, "health left")
                                enemydamage = 0


                            if PrintPoison != "no":
                                print(currentpokemon, "has been poisoned!")
                            if PrintBurn != "no":
                                print(currentpokemon, "was burned!" )
                            if PrintConfuse != "no":
                                print(currentpokemon, "is confused!")
                            if PrintParalyzed != "no":
                                print(currentpokemon, "was paralyzed")
                            
                            if DoDamage == "yes":
                                functionality.Confuse(enemypokemon, enemydamage)
                                if enemyhititself == "no":
                                    time.sleep(1)
                                    if typesuper1 == True or typesuper2 == True or typesuper == True:
                                        print("It was supereffective!")
                                        time.sleep(0.5)
                                    print(enemypokemon, "did", enemydamage, "damage")
                                    if crithappen == True:
                                        print("It was a critical hit!")
                                        time.sleep(0.5)
                                
                                    currenthealth -= enemydamage
                            time.sleep(1)
                            print(currentpokemon, "has", currenthealth, "health left")
                            userpartyhealth[x] = currenthealth
                            #global Death
                            #death = False
                            if currenthealth == 0:
                                for i in range(len(yourteam)):
                                    if currentpokemon == yourteam[i]:
                                        yourteam.remove(yourteam[i])
                                        death = True
                                        break
                                print(yourteam)
                                newpk = input("Who will you switch into? ")
                                for i in range(len(yourteam)):
                                    if newpk == yourteam[i]:
                                        currentpokemon = newpk
                                for i in range(len(userpartyhealth)):
                                    if currentpokemon == userpartyhealth[i - 1]:
                                        currenthealth = userpartyhealth[i]
                            if len(yourteam) == 0:
                                Kaifat = "no"
                        if death == False:
                            time.sleep(times)

                            going = "User"

                            if itcounter == "yes":
                                for i in range(pokemonlist):
                                    if data[i]["Name"] == currentpokemon:
                                        currentspeed == data[i]["Speed Stat"]


                            PrintPoison = "no"
                            DoDamage = "yes"
                            EnemyPoisoned = "no"
                            shouldiswitch = "no"
                            goingfirst = "ABBA"
                            Diduniquedamagehappen = "no"
                            Didithittwice = "no"
                            fourtydamagetrue = "no"
                            itcounter = "no"
                            Diditmiss = "no"
                            runspecial = "yes"
                            Flinching = "no"
                            PrintBurn = "no"
                            EnemyBurn = "no"
                            PrintConfuse = "no"
                            EnemyConfuse = "no"
                            PrintParalyzed = "no"
                            EnemyParalyzed = "no"
                            
                            functionality.Paralyze(currentpokemon)
                            functionality.Imatired(going)
                            functionality.coldgaming(going)
                            if youPAR == "no" and yousleep == "no" and youcold == "no":
                                print("You used", use)
                                time.sleep(times)
                            
                            # if move effect != None
                            #Do effect
                            f = functionality()
                            for i in range(len(currentmoves)):
                                if currentmoves[i] == use:
                                    f.damagecalc(use, currentpokemon, enemypokemon)
                                    damage = movedamage
                                    functionality.Miss(use, evasive, enemyevasive, going)
                                    if youPAR != "no":
                                        DoDamage = "no"
                                        print(currentpokemon,"was unable to move due to its paralysis")
                                        runspecial = "no"

                                    if yousleep != "no":
                                        DoDamage = "no"
                                        print(currentpokemon,"is fast asleep")
                                        runspecial = "no"
                                    if youcold != "no":
                                        DoDamage = "no"
                                        print(currentpokemon, "is frozen solid")
                                        runspecial = "no"

                                    if runspecial == "yes":
                                        
                                        f.specialeffect(use, damage, enemyspeed,currentspeed, enemypokemon, currentpokemon, going, enemydamage, turn, enemyhealth)
                                    
                                    if Diduniquedamagehappen != "no":
                                        damage = uniquedamage

                                    if Didithittwice != "no":
                                        damage = TwoHitDamage

                                    if fourtydamagetrue != "no":
                                        damage = 40

                                    if itcounter != "no":
                                        damage = counterdamage

                                    if awaybeforehit == "yes":
                                        damage = 0
                                    if use == "Mirror Move":
                                        f.damagecalc(enemymove, currentpokemon, enemypokemon)
                                        damage = movedamage
                                        print(currentpokemon, "mirrored", enemymove)
                                        use = enemymove
                                        f.specialeffect(use, damage, enemyspeed,currentspeed, enemypokemon, currentpokemon, going, enemydamage, turn, enemyhealth)
                                        

                                    if hitsnextturn == "yes":
                                        if use == "Sky Attack":
                                            print(currentpokemon, "started to glow!")
                                        if use == "Solar Beam":
                                            print(currentpokemon,"is absorbing sunlight")

                                    #effect stuff ends here

                                    if damage == enemyhealth or damage > enemyhealth:
                                        damage = enemyhealth

                                    if Diditmiss != "no":
                                        damage = 0
                                        if DoDamage == "yes":
                                            print("But it missed!")
                                        DoDamage = "no"
                                        
                                        if use == "Hi Jump Kick" or use == "Jump Kick":
                                            f.damagecalc(use, currentpokemon, enemypokemon)
                                            damage = movedamage
                                            currenthealth = currenthealth - damage
                                            print(currentpokemon, "took", damage, "damage due to recoil")
                                            print(currentpokemon, "has", currenthealth, "health left")
                                        damage = 0
                            
                                    if EnemyPoisoned != "no":
                                        print(enemypokemon,"was poisoned!")
                                    if EnemyBurn != "no":
                                        print(enemypokemon, "was burned!")
                                    if EnemyConfuse != "no":
                                        print(enemypokemon, "is confused!")
                                    if EnemyParalyzed != "no":
                                        print(enemypokemon, "was paralyzed")


                                    if DoDamage == "yes":
                                        functionality.Confuse(currentpokemon, damage)
                                        if hityourself == "no":
                                            time.sleep(1)
                                            if typesuper1 == True or typesuper2 == True or typesuper == True:
                                                print("It was supereffective!")
                                                time.sleep(0.5)
                                            print(currentpokemon, "did", damage, "damage")
                                            if crithappen == True:
                                                print("It was a critical hit!")
                                                time.sleep(0.5)
                                            if use == "Explosion":
                                                
                                                currenthealth = 0
                                                print(currentpokemon,"died because it exploded")
                                                if currenthealth == 0:
                                                    for i in range(len(yourteam)):
                                                        if currentpokemon == yourteam[i]:
                                                            yourteam.remove(i)
                                                    print(yourteam)
                                                    newpk = input("Who will you switch into? ")
                                                    for i in range(len(yourteam)):
                                                        if newpk == yourteam[i]:
                                                            currentpokemon = newpk
                                                    for i in range(len(userpartyhealth)):
                                                        if currentpokemon == userpartyhealth[i - 1]:
                                                            currenthealth = userpartyhealth[i]

                                            enemyhealth = enemyhealth - damage
                                    time.sleep(times)
                                    if enemyhealth > 0:
                                        print(enemypokemon, "has", enemyhealth, "health left")
                                    if enemyhealth == 0:
                                        print(enemypokemon, "fainted")
                        enemypartyhealth[1] = enemyhealth
                        functionality.Mikesdeadpks(enemyhealth, currentpokemon)
                        #print(enemypokemon)

                        for i in range(len(userpartyhealth)):
                            if currentpokemon == userpartyhealth[i - 1]:
                                currenthealth = userpartyhealth[i]

                        functionality.afflicted(N,M, currenthealth, currentpokemon)
                        functionality.Crispy(currentpokemon)

                        functionality.keepusing(usedturn, gooblie)

                        functionality.Mikesdeadpks(enemyhealth, currentpokemon)

                        for i in range(len(userpartystatus)):
                            if currentpokemon == userpartystatus[i - 1]:
                                if userpartystatus[i] == "Poison":
                                    
                                    currenthealth = Afterhealth
                        
                                    #print(currenthealth, "after afflicted")
                                    #print(Afterhealth, "after afflicted")
                                    #dead below
                                    for i in range(len(userpartyhealth)):
                                        if currentpokemon == userpartyhealth[i - 1]:
                                            userpartyhealth[i] = Afterhealth
                                    

                        PrintPoison = "no"
                        DoDamage = "yes"
                        EnemyPoisoned = "no"
                        shouldiswitch = "no"
                        goingfirst = "ABBA"
                        Diduniquedamagehappen = "no"
                        Didithittwice = "no"
                        fourtydamagetrue = "no"
                        itcounter = "no"
                        Diditmiss = "no"
                        runspecial = "yes"
                        Flinching = "no"
                        PrintBurn = "no"
                        EnemyBurn = "no"
                        hityourself = "no"
                        enemyhititself = "no"
                        PrintConfuse = "no"
                        EnemyConfuse = "no"
                        PrintParalyzed = "no"
                        EnemyParalyzed = "no"
                        
                        if seeded == "yes":
                            for i in range(pokemonlist):
                                if enemypokemon == data[i]["Name"]:
                                    start = data[i]["Health Stat"]
                            seedgaming = start/16
                            damage = round(seedgaming)
                            if damage == enemyhealth or damage > enemyhealth:
                                damage = enemyhealth
                            enemyhealth = enemyhealth - damage
                            
                            print(enemypokemon, "had its health sapped by Leech Seed")
                            time.sleep(times)
                            print(enemypokemon,"has", enemyhealth, "health left")

                            for i in range(pokemonlist):
                                if currentpokemon == data[i]["Name"]:
                                    fail = data[i]["Health Stat"]
                            if currenthealth != fail:
                                currenthealth += damage
                                if currenthealth == fail or currenthealth > fail:
                                    currenthealth = fail
                            print(currentpokemon, "recovered", damage,"health")
                            time.sleep(times)
                            print(currentpokemon, "has", currenthealth,"health")
                            for i in range(len(userpartyhealth)):
                                if currentpokemon == userpartyhealth[i-1]:
                                    userpartyhealth[i] = currenthealth

                        if currenthealth == 0:
                            for i in range(len(yourteam)):
                                if currentpokemon == yourteam[i]:
                                    yourteam.remove(i)
                            print(yourteam)
                            newpk = input("Who will you switch into? ")
                            for i in range(len(yourteam)):
                                if newpk == yourteam[i]:
                                    currentpokemon = newpk
                            for i in range(len(userpartyhealth)):
                                if currentpokemon == userpartyhealth[i - 1]:
                                    currenthealth = userpartyhealth[i]

                        functionality.hedobetrapped(startingturntrapped,Trappedturns,turn)

                        if len(Mikesdeadguys) == 6:
                            Kaifat = "no"
                        #turn += 1
                        if awaybeforehit != "no":
                            time.sleep(2)
                            Schmovin.Whosmovin(enemypokemon,currentpokemon)
                            print(enemypokemon,"used", enemymove)
                            if DoDamage == "yes":

                                time.sleep(times)
                                print("But it missed")




time.sleep(2)        


Turns.preturn(firstpokemon, enemypokemon, "Elite Four Member Mike")
Turns.turn(firstpokemon, Kaifat)
time.sleep(2)

if len(Mikesdeadguys) > 5:
  print("Congratulations!\nYou have defeated Elite Four Member Mike!")

if len(yourteam) == 0:
  print("You have no more pokemon left to battle with\n You have lost the battle\n GAME OVER")















#Tims team
#Pikachu - Toxic, Thunderbolt, Double Team, Surf
#Gyarados - 
#Moltres
#Articuno
#Venusaur
#Mewtwo#Mewtwo#Mewtwo#Mewtwo