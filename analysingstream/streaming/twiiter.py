import os

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

API_KEY = os.environ.get("TWITTER_API_KEY")
API_SECRET_KEY = os.environ.get("TWITTER_SECRET_KEY")
ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")


def authenticate_twitter_app() -> object:
    auth = OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return auth


def stream_tweets(hash_tag_list: list):
    listener = TwitterListener()
    auth = authenticate_twitter_app()
    stream = Stream(auth, listener)
    stream.filter(track=hash_tag_list, languages=["pt"])


class TwitterListener(StreamListener):
    def on_data(self, raw_data):
        print(raw_data)

    def on_error(self, status_code):
        print("Error detected")


if __name__ == "__main__":
    stream_tweets(["covid", "covid-19"])
