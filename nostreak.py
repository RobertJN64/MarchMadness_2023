import json

with open("schoolmasterdata2021.json") as f:
    d = json.load(f)

for item in d.values():
    if 'streak' in item:
        item.pop("streak")

with open("schoolmasterdata2021.json", "w+") as f:
    json.dump(d, f, indent=4)