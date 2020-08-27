

import tweepy
import time

auth = tweepy.OAuthHandler("",
                           "")
auth.set_access_token("",
                      "")

api = tweepy.API(auth)


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


search_string = "python"
numbersofTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersofTweets):
    try:

        tweet.favorite()
        print("i liked that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# for follower in limit_handler(tweepy.Cursor(user_followers).items()):
#     if follower == "porson name":

#         follower.follow()
#         break
