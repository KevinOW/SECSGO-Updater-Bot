import tweepy
import logging

#consumer_key = 'fTx4UnNpno2qXW0TiuPw72mgW'
#consumer_secret = 'EEEGl8Rrq4z0GAAJvXUv1dCPfeMh35GimTDuSX6hjTkNCulgoO'
#key = '1490181790014836737-IJqqU5twh0tVtqqNBnrt63nj8NNfA'
#secret = 'oHMfkfx2kYGPtYUdNwS7n64gGFCXIPGHyOREfKgLKM0in'

logging.basicConfig(filename='backlog.log', level=logging.DEBUG,
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Everything works")

except:
    print("Something went wrong.. :(")
