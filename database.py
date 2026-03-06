from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["chat_application"]

users_collection = db["users"]
messages_collection = db["messages"]
