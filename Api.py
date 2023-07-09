
import tweepy

# Authenticate to Twitter using the API key and secret
auth = tweepy.OAuth1UserHandler("", "")
auth.set_access_token("-4vxRxOJ9UaNaKxXiS2nh7", "")

# Create API object
api = tweepy.API(auth)

# Post a tweet
api.update_status("Hello, Tweepy!")
