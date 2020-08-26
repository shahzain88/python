import tweepy

auth = tweepy.OAuthHandler("",
                           "")
auth.set_access_token("",
                      "")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

user = api.me()
print(user.name)
print(user.screen_name)
print(user.followers_count)
