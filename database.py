from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")

client = MongoClient(MONGO_URI)

db = client["chatbot_db"]
conversations = db["conversations"]
