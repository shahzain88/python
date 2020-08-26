import tweepy
import time

auth = tweepy.OAuthHandler("IEVaD85orjjwsRMZkSRaCPLX9",
                           "L6OQ0ioz6s1Tcfb3DTESYLjtTaYiimhG0Kc5tLIXk23YKn1fDF")
auth.set_access_token("1298627061490147329-EgQWi6Sa28jz3bVfo9h6S9froW4z6b",
                      "ZipfWrbI4Xxn6uCrxYK08bkPDlBBx0TREttbZb4BRaTH2")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

user_followers = api.followers


def limit_handler(cursor):
    try:

        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


for follower in limit_handler(tweepy.Cursor(user_followers).items()):
    if follower == "porson name":

        follower.follow()
        break
