# Scraper, output data


# IMPORTS
from pip import main
import requests
import json
import logging

# LOGGING DATE & TIME
logging.basicConfig(filename='backlog.log', level=logging.DEBUG,
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# SCRAPER
url = "https://esportal.com/api/tournament/get"
querystring = {"_":"1654563653130","id":"2511"}

payload = ""
headers = {
    'authority': "esportal.com",
    'accept': "*/*",
    'accept-language': "sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7",
    'cookie': "auth=119651_RGhmOmJMQkcvKFpUWEZTVQ; CookieConsent=^{stamp:^%^27S1tclZ9cac924/e5+cVbwmtzsOnhkLESNQqA//99speVzaRHPQRlgw==^%^27^%^2Cnecessary:true^%^2Cpreferences:true^%^2Cstatistics:true^%^2Cmarketing:true^%^2Cver:1^%^2Cutc:1646504466233^%^2Cregion:^%^27se^%^27^}; __cf_bm=nre6JaTDI0I823F7MbZh2VfoeYexUWRd8KeLzSkPAt8-1654563393-0-Ac8L1IN2ew9vggYGnfAfp7IW5k9FEnWoajelomu0G3QgHbCcSK5yumPKRVVRR8Sk+nVeAFCmFXWpg/S2v7/SezQKI4PGGL4E2B1YrmTSmaCWZYqe1hUIQTVxAhspai2NRw==",
    'referer': "https://esportal.com/sv/secsgo",
    'sec-ch-ua': "^\^"
    }

r = requests.request("GET", url, data=payload, headers=headers, params=querystring).json()

match_id = r['matches'][0]['id']
team1 = r['matches'][0]['team1']['name']
team2 = r['matches'][0]['team2']['name']
team1_score = r['matches'][0]['team1_score']
team2_score = r['matches'][0]['team2_score']
map_pool = r['matches'][0]['map_id']


# VARIABLES

# FUNCTIONS

def displayWinner():
    if team1_score >= team2_score:
        print("Winner:", team1)
    else:
        print("Winner:", team2)
    return

def displayMatchID():
    print(match_id)
    return

def displayTeam_1():
    print(team1 , end=" - ")
    return

def displayTeam_1_score():
    print(team1_score)
    return

def displayTeam_2():
    print(team2 , end=" - ")
    return

def displayTeam_2_score():
    print(team2_score)
    return

def displayMaps():
    if map_pool == 0:
        print('No map')
    elif map_pool == 34:
        print('Map is: Ancient')
    elif map_pool == 18:
        print('Map is: Vertigo')
    elif map_pool == 5:
        print('Map is: Mirage')
    elif map_pool == 4:
        print('Map is: Overpass')
    elif map_pool == 3:
        print('Map is: Nuke')
    elif map_pool == 2:
        print('Map is: Inferno')
    elif map_pool == 1:
        print('Map is: Dust')
    return


# OUTPUTS
displayMatchID()
displayTeam_1()
displayTeam_1_score()
displayTeam_2()
displayTeam_2_score()
displayMaps()
displayWinner()

# LOGGING INFORMATION
logging.info(match_id)
logging.info(team1)
logging.info(team2)
logging.info(team1_score)
logging.info(team2_score)
logging.info(map_pool)