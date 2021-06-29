import json

from analysingstream.processors.message import Message


class MessageSerializer:
    @staticmethod
    def serialize(msg):
        content = {
            "payload": msg.payload,
            "correlationId": msg.id.__dict__,
        }
        return json.dumps(content).encode()

    @staticmethod
    def deserialize(msg):
        msg = json.loads(msg.decode())
        return Message(msg["correlationId"], msg["payload"])
