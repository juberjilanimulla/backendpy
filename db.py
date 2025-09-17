from flask_pymongo import PyMongo
from config import Config

mongo = PyMongo()

def db_connect(app):
    try:
        # Configure MongoDB
        app.config["MONGO_URI"] = Config.MONGODB_URL
        mongo.init_app(app)
        print("Database connected successfully")
    except Exception as e:
        print("Unable to connect to database:", e)
