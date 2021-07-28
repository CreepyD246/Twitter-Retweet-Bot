# Importing all modules/packages/libraries
import tweepy

# Initialization
auth = tweepy.OAuthHandler("API KEY", "API SECRET KEY")
auth.set_access_token("ACCESS TOKEN", "SECRET ACCESS TOKEN")
api = tweepy.API(auth)

# Getting Bot ID
bot_id = int(api.me().id_str)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        print("Tweet Found!")
        print(f"TWEET: {tweet.author.screen_name} - {tweet.text}")
        if tweet.author.id != bot_id and tweet.in_reply_to_status_id is None:
            if not tweet.retweeted:
                try:
                    print("Attempting Retweet...")
                    api.retweet(tweet.id)
                    print("Tweet successfully retweeted :)")
                except Exception as err:
                    print(err)

stream_listener = MyStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["Python"], languages=["en"])
