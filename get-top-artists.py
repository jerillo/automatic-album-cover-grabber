import json

with open('./top-artist-data.json') as f:
    data = json.load(f)

for item in data.get("items"):
    print(item.get("name"))
