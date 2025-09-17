from datetime import datetime, timedelta
from db import mongo

def current_local_time_plus_offset():
    now = datetime.utcnow()
    offset = timedelta(hours=5, minutes=30)  # +5:30 IST offset
    return now + offset

class UserModel:
    collection = mongo.db.users   # like mongoose.model("user")

    @staticmethod
    def create_user(data):
        data["createdAt"] = current_local_time_plus_offset()
        data["updatedAt"] = current_local_time_plus_offset()
        return UserModel.collection.insert_one(data)

    @staticmethod
    def find_by_email(email):
        return UserModel.collection.find_one({"email": email})

    @staticmethod
    def update_user(query, new_data):
        new_data["updatedAt"] = current_local_time_plus_offset()
        return UserModel.collection.find_one_and_update(
            query, {"$set": new_data}, return_document=True
        )
