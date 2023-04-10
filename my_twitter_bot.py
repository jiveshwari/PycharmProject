import tweepy
import time

auth = tweepy.OAuthHandler('9KIBMPHMgRdFYGqFc0iczCIo5','jnKQNlOeM8oDhaOg896GhoV76MyX85J5QRb3If5cu4wofWBbfy')
auth.set_access_token('1292377854605266945-SikTtdVnN4xGMkQuFGHbtGMzmvi7n8','tXVKFETlxOCqEYPpE2axt6LMMT6MXePN0NFi1OIWaJ9aE')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search1 = "Women in engineering"
search2 = "Women in STEM"
search3 = "python"
search4 = "#girlwhocode"
search5 = "coding"
nrtweets = 500

for tweet in tweepy.Cursor(api.search, search1, search2, search4).items(nrtweets):
    try:
        print("Tweet liked and retweeted")
        tweet.retweet()
        time.sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search2, search3, search5).items(nrtweets):
    try:
        print("Tweet liked and retweeted")
        tweet.favorite()
        time.sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
