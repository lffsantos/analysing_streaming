import json
import logging

from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

import config
from analysingstream.processors.correlation_id import CorrelationId
from analysingstream.processors.dispatcher.kafka_dispatcher import KafkaDispatcher

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
        self.dispatcher = KafkaDispatcher()

    def on_data(self, raw_data):
        data = json.loads(raw_data)
        correlation_id = CorrelationId(TwitterListener.__name__)
        self.dispatcher.send(
            config.QUEUE_COLLECT_TWITTER, data["id_str"], correlation_id, data
        )
        logger.info(raw_data)

    def on_error(self, status_code):
        print("Error detected")


if __name__ == "__main__":
    stream_tweets(["covid", "covid-19", "flamengo"])
