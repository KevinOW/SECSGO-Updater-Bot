import tweepy


auth = tweepy.OAuth1UserHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Everything works")

except:
    print("Something went wrong.. :(")
