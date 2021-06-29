import logging

import config
from analysingstream.database.mongo import MongoService
from analysingstream.processors.consumer.service_runner import ServiceRunner

logger = logging.getLogger(__name__)


class StreamDBService(ServiceRunner):
    def __init__(self):
        super().__init__(StreamDBService)
        self.database = MongoService()
        self.collection = self.database.collection(config.COLLECTION)
        self.start(5)

    def parse(self, record):
        print("------------------------------------------")
        print("Save on database")
        data = record.value.payload
        print(
            "%s:%d:%d: key=%s value=%s"
            % (record.topic, record.partition, record.offset, record.key, data)
        )
        try:
            self.database.insert(self.collection, data)
            logger.info(data)
        except InterruptedError as error:
            logger.error(error)
            raise error
        print("Record Save")

    @classmethod
    def get_consumer_group(cls):
        return StreamDBService.__name__

    @classmethod
    def get_topic(cls):
        return config.QUEUE_COLLECT_TWITTER


if __name__ == "__main__":
    stream_service = StreamDBService()
