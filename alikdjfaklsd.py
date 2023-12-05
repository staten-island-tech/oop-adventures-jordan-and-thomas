import json

test = open("playerteaminfo.json", encoding="utf8")
data = json.load(test)

print(data)