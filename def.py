import json
import random
class effect:
    def HealHalfD(damagedone, currentHealth):
        currentHealth = currentHealth + damagedone/2
        
    def Hits2to5(movedamage):
        times = randrange(5)
        if times == 1 or times == 2:
            damagedoneb = movedamage * 2
        if times == 3:
            damagedoneb = movedamage * 3
        if times == 4:
            damagedoneb = movedamage * 4
        if times == 5:
            damagedoneb = movedamage * 5
        
    def SpeedDown():
        a

    def HitsTwice(movedamage):
        damagedoneb = movedamage * 2
    
    def Poison():
        a
    
    def Always40():
        damagedone = 40
    
    def Paralyze():
        a
    
    def AlwaysParalyze():
        a
    
    def ItCounter(damagedealt, movecat):
        if movecat == "physical":
            damagedone = damagedealt
    
    def MissDoD():
        b

    def MissDoLessD():
        b

    def Flinch13():
        chance = random.randrange(3)
        if chance == 1:
            
    
    



        

    

