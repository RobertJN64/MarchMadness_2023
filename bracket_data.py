from bs4 import BeautifulSoup
from time import sleep
import requests
import json


def get_team_data(school, year):
    url = "https://www.sports-reference.com/cbb/schools/" + school + "/" + year + '.html'
    text = requests.get(url).text
    page = BeautifulSoup(text)
    table = page.find('table', {'id': 'season-total_per_game'}) #Find the table
    header = table.thead
    row = table.tbody.find_all('tr')[0]

    team_data = {}
    for key, value in zip(header.find_all('th')[1:], row.find_all('td')): #zip is an easy method to iterate through 2 lists at the same time
        if key.text != 'G': #ignore total number of games
            team_data[key.text] = float(value.text)
    return team_data

def main():

    with open('bracket.txt') as f:
        out = {}
        for team in f.readlines():
            team = team.strip()
            print(team)
            year = '2023'
            d = get_team_data(team, year)
            sleep(5)
            out[team] = d

        with open("schooldata_2023.json", 'w+') as g:
            json.dump(out, g, indent=4)


main()