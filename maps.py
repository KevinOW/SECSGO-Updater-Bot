from cffi import VerificationMissing
import requests
import logging

#LOGGING DATE & TIME
logging.basicConfig(filename='maps.log', level=logging.DEBUG,
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

url = "https://esportal.com/api/maps"

querystring = {"_":"1654620522466"}

payload = ""
headers = {
    'authority': "esportal.com",
    'accept': "*/*",
    'accept-language': "sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7",
    'cookie': "auth=119651_RGhmOmJMQkcvKFpUWEZTVQ; CookieConsent=^{stamp:^%^27S1tclZ9cac924/e5+cVbwmtzsOnhkLESNQqA//99speVzaRHPQRlgw==^%^27^%^2Cnecessary:true^%^2Cpreferences:true^%^2Cstatistics:true^%^2Cmarketing:true^%^2Cver:1^%^2Cutc:1646504466233^%^2Cregion:^%^27se^%^27^}; __cf_bm=FH2sz1HstjyUdVrgbpT8TNFG6S414HwA6EqrbqZAWDE-1654620514-0-AXywdZnrc7ku/WfsHe987VtVLpkol1fA825TVmn8yUFUGU8ryKo9hIaaoB6CFbEWnnaxjUDy57C4RqdExtAVK39paqfTxD11gga2LXo5zmYfjClapBqp2e9mm6ZB/jqmiQ==",
    'referer': "https://esportal.com/sv/secsgo",
    'sec-ch-ua': "^\^"
    }
r = requests.request("GET", url, data=payload, headers=headers, params=querystring).json()

dust = r[1]['name']
inferno = r[2]['name']
nuke = r[3]['name']
overpass = r[4]['name']
mirage = r[5]['name']
vertigo = r[18]['name']
ancient = r[34]['name']

print(dust, inferno, nuke, overpass, mirage, vertigo, ancient)
