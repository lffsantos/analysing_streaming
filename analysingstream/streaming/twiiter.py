import json
import logging

from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

import config
from analysingstream.database.mongo import MongoService

logger = logging.getLogger(__name__)


def authenticate_twitter_app() -> object:
    auth = OAuthHandler(config.API_KEY, config.API_SECRET_KEY)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    return auth


def stream_tweets(hash_tag_list: list):
    listener = TwitterListener()
    auth = authenticate_twitter_app()
    stream = Stream(auth, listener)
    stream.filter(track=hash_tag_list, languages=["pt"])


class TwitterListener(StreamListener):
    def __init__(self):
        self.database = MongoService()
        self.collection = self.database.collection(config.COLLECTION)

    def on_data(self, raw_data):
        data = json.loads(raw_data)
        self.database.insert(self.collection, data)
        logger.info(raw_data)

    def on_error(self, status_code):
        print("Error detected")


if __name__ == "__main__":
    stream_tweets(["covid", "covid-19"])
