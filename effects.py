import json
import random

test = open("move.json", encoding="utf8")
moves = json.load(test)
movelist = len(moves)



class effect():
   

    def Toxic(oppositepokemon, oppositehealth, pokemonin, endofturn, turn):
        print(oppositepokemon, "has been Poisoned")
        afflicted = pokemonin
        while afflicted == pokemonin:
            if endofturn == "end":
                N = 1
                damage = N * oppositehealth/16
                if turn + 1:
                    N += 1




    def HealHalfD(damagedone, targetHealth):
        targetHealth = targetHealth + damagedone/2
        
    def Hits2to5(movedamage):
        times = random.randrange(5)
        if times == 1 or times == 2:
            damagedoneb = movedamage * 2
        if times == 3:
            damagedoneb = movedamage * 3
        if times == 4:
            damagedoneb = movedamage * 4 
        if times == 5:
            damagedoneb = movedamage * 5
        
    def SpeedDown(speedstat):
        x = 1
        percent = speedstat/100
        if x == 1:
            targetspeedstat = percent * 67
        if x == 2:
            targetspeedstat = percent * 50
        if x == 3:
            targetspeedstat = percent * 40
        if x == 4:
            targetspeedstat = percent * 33
        if x == 5:
            targetspeedstat = percent * 29
        if x == 6 or x > 6:
            targetspeedstat = percent * 25
        x += 1

    def HitsTwice(movedamage):
        damagedoneb = movedamage * 2
    
    def Poison(targetpokemontype):
        if targetpokemontype != "Poison":
            skull = random.randrange(5)
            if skull == 1:
                targetpokemonstatus = "Poison"
    
    def Always40():
        damagedone = 40
    
    def Paralyze(targetpokemontype):
        if targetpokemontype != "Electric":
            zap = random.randrange(5)
            print(zap)
            if zap == 1:
                targetpokemonstatus = "Paralyze"
                print("Pokemon has been paralyzed")
            
    
    def AlwaysParalyze(targetpokemontype):
        if targetpokemontype != "Electric":
            targetpokemonstatus = "Paralyze"
    
    def ItCounter(damagedealt, movecat):
        if movecat == "physical":
            damagedone = damagedealt * 2
    
    def MissDoD(hit, targethealth):
        if hit == "no":
            smaack = targethealth/8
            targethealth = smaack * 7


    def MissDoLessD(hit, targethealth):
        if hit == "no":
            targethealth = targethealth - 1

    def Flinch13():
        chance = random.randrange(3)
        if chance == 1:
            Flinch = "yes"
    
    def Seismictoss(defensestat):
        damagedone = defensestat/4
    
    def Recoil14(damagedone, targethealth):
        back = damagedone/4
        targethealth = targethealth - back
    
    def Burn(targetpokemontype):
        if targetpokemontype != "Fire":
            fuego = random.randrange(10)
            if fuego == 1:
                    targetpokemonstatus = "Burn"
    
    def FireSpin():
        turns = random.randrange(4)
        #pokemonescape = trapped
        if turns == 1:
            TurnsHitsfor = 2
        if turns == 2:
            TurnsHitsfor = 3
        if turns == 3:
            TurnsHitsfor = 4
        if turns == 4:
            TurnsHitsfor = 5
    
    def Flygimmick():
        immune = "yes"





    


class Using(effect):
    def usemove(use, enemyuse, oppositepokemon, oppositehealth, pokemonin, endofturn, turn):
        for i in range(movelist):
            if use == "Toxic" or enemyuse == "Toxic":
                effect.Toxic(oppositepokemon, oppositehealth, pokemonin, endofturn, turn)
            



            
    
    



        

    

