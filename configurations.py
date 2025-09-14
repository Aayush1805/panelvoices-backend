
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')


client = MongoClient(
    MONGO_URI,
    tls=True,
    server_api=ServerApi('1')
)

db = client.voice_db
collection = db["voice_data"]