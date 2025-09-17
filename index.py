from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from db import db_connect, mongo

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
db_connect(app)

# Example route (like Express test route)
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "OK", "db_name": mongo.db.name})

if __name__ == "__main__":
    app.run(port=Config.PORT, debug=True)
