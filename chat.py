from database import messages_collection
import datetime

def save_message(username, message):

    messages_collection.insert_one({
        "user": username,
        "message": message,
        "time": datetime.datetime.now()
    })


def get_messages():

    return messages_collection.find().sort("time", 1)
