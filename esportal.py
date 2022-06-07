import requests
import array
import json

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
maps = r['map_pool']

maps = ['1', '2', '3', '4', '5', '18', '34']

for i in range(len(maps)):

    # replace 1 with Dust
    if maps[i] == '1':
        maps[i] = 'Dust'

    # replace 2 with Ancient
    if maps[i] == '2':
        maps[i] = 'Inferno'

    # replace 3 with Ancient
    if maps[i] == '3':
        maps[i] = 'Nuke'

    # replace 4 with Ancient
    if maps[i] == '4':
        maps[i] = 'Overpass'

    # replace 5 with Ancient
    if maps[i] == '5':
        maps[i] = 'Mirage'

    # replace 18 with Ancient
    if maps[i] == '18':
        maps[i] = 'Vertigo'

    # replace 34 with Ancient
    if maps[i] == '34':
        maps[i] = 'Ancient'

print(map_pool)
print(team1 , end=" - ")
print(team1_score)
print(team2 , end=" - ")
print(team2_score)
print(maps)