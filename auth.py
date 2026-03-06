import bcrypt
from database import users_collection

def register_user(username, password):

    existing = users_collection.find_one({"username": username})

    if existing:
        return False

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    users_collection.insert_one({
        "username": username,
        "password": hashed_password
    })

    return True


def login_user(username, password):

    user = users_collection.find_one({"username": username})

    if not user:
        return False

    if bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        return True

    return False
