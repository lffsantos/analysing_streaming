from pymongo import MongoClient, ReadPreference

import config


class MongoService:
    def __init__(self):
        client = MongoClient(config.DB_URI)
        self.db = client[config.DB_NAME]  # pylint: disable=invalid-name

    def collection(self, collection_name):
        return self.db.get_collection(
            collection_name, read_preference=ReadPreference.SECONDARY
        )

    @staticmethod
    def upsert(collection, item, query, field):
        data = collection.find_one(query)
        if data:
            collection.update_one(query, {"$set": {field: item[field]}})
        else:
            collection.insert_one(item)

    @staticmethod
    def insert(collection, item):
        collection.insert_one(item)

    @staticmethod
    def insert_many(collection, items):
        collection.insert_many(items)
