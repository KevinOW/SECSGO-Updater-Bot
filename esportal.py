import requests
import json
import logging
import re

logging.basicConfig(filename='backlog.log', level=logging.DEBUG,
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


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


team1 = r['matches'][0]['team1']['name']
team2 = r['matches'][0]['team2']['name']
team1_score = r['matches'][0]['team1_score']
team2_score = r['matches'][0]['team2_score']
map_pool = r['matches'][0]['map_id']
#maps = ['Dust', 'Inferno', 'Nuke', 'Overpass', 'Mirage', 'Vertigo', 'Ancient']
#maps_change = ['map_id'.replace([0],[1],[2],[3],[4],[5],[6]) for item in ]

for item in ['matches']:
    for row in ['map_id']:
        print("Map is",map_pool)



print(map_pool)
print(team1 , end=" - ")
print(team1_score)
print(team2 , end=" - ")
print(team2_score)

logging.info(team1)
logging.info(team2)
logging.info(team1_score)
logging.info(team2_score)
