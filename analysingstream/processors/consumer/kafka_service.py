import re
import uuid

from kafka import KafkaConsumer

import config
from analysingstream.processors.serializer import MessageSerializer


class KafkaService:
    consumer = None
    parse = None

    def __init__(self, topic: str or re, parse: any = None, group_id: str = None):
        self.parse = parse
        self.consumer = KafkaConsumer(**self.properties(group_id))
        if isinstance(topic, str):
            self.consumer.subscribe(topic)
        else:
            self.consumer.subscribe(pattern=topic)

    def run(self):
        while True:
            print("starting the consumer")
            self.consumer.poll(2)
            for message in self.consumer:
                self.parse(message)

    @staticmethod
    def properties(group_id):
        conf = {
            "bootstrap_servers": config.BROKER_URL,
            # 'key_deserializer': str.encode,
            "value_deserializer": lambda m: MessageSerializer.deserialize(m),  # noqa
            "group_id": group_id,
            "client_id": str(uuid.uuid4()),
            "max_poll_records": 1,
            "auto_offset_reset": "earliest",
        }
        return conf


if __name__ == "__main__":
    service = KafkaService("ECOMMERCE_NEW_ORDER")
    service.run()
