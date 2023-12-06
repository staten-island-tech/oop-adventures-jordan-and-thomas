import json
import os
combinedname = input("Type here ")
gang = combinedname.split(",")
with open("playerteaminfo.json", "r") as f:
    data = json.load(f) # append to data!!!
    data.append([gang])
new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data, indent=4)
    f.write(json_string)
os.remove("playerteaminfo.json")
os.rename(new_file, "playerteaminfo.json")