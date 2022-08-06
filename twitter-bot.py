import tweepy
import logging

logging.basicConfig(filename='backlog.log', level=logging.DEBUG,
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Everything works")

except:
    print("Something went wrong.. :(")
