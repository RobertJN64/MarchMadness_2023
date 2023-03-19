import json

with open("verified_bracket.txt") as f:
    teams = [team.strip() for team in f.readlines()]

with open("schoolmasterdata2021.json") as f:
    d = json.load(f)



for team in teams:
    if team not in d.keys():
        print("NO MATCH", team)

