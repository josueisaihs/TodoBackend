from pymongo import MongoClient
import certifi

from config.settings import Settings

settings = Settings()

mogodb_client = MongoClient(
    settings.mongodb_connection,
    tlsCAFile=certifi.where()
)

db_client = mogodb_client.fastapi