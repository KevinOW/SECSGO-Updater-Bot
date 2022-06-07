import requests

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

r = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(r.json())