import json
import os
## Create Class for creating new dictionaries here
class moves():
    def __init__(self, name, movetype, cat, power, acc, pp, effect):
       self.name = name
       self.movetype = movetype
       self.cat = cat
       self.power = power
       self.acc = acc
       self.pp = pp
       self.effect = effect

name = input("Name of move: ")
movetype = input("Move type: ")
cat = input("Move category: ")
power = input("Move power: ")
acc = input("Move accuracy: ")
pp = input("pp: ")
effect = input("Move effect: ")


 
    
  
        


  

    

    
    
    


        


    
#dat.append(variable, variable)
#Variable = title


with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    data.append({"name": name, "type": movetype, "category": cat, "power": power, "accuracy": acc, "PP": pp, "effect": effect})
    ##Call classes in here
    
    
   
       







#No code needed below this line
# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data, indent=4)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("data.json")
os.rename(new_file, "data.json")