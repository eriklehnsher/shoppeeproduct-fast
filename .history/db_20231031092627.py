from pymongo.mongo_client import MongoClient
import motor.motor_asyncio
from config import settings



client = motor.motor_asyncio.AsyncIOMotorClient(settings.uri)

db = client.Products
Products_db = db["Products"]
images_collection = db["images"]