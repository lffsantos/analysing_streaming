import os

DB_URI = os.environ.get("DB_URI")
DB_NAME = os.environ.get("DB_NAME", "stream")
COLLECTION = os.environ.get("COLLECTION", "twitter")
API_KEY = os.environ.get("TWITTER_API_KEY")
API_SECRET_KEY = os.environ.get("TWITTER_SECRET_KEY")
ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
