import json
class effect:
    def HealHalfD(damagedone, currentHealth):
        currentHealth = currentHealth + damagedone/2
        print(currentHealth)
    

effect.HealHalfD(50,100)