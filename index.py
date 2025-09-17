from flask import Flask,request, jsonify
from flask_cors import CORS
from config import Config
from db import db_connect 
import logging


app = Flask(__name__)
CORS(app,supports_credentials=True)

# Connect to MongoDB
db_connect(app)

# logging (similar morgan)
logging.basicConfig(level=logging.INFO)

# app.before_request
def log_request():
    logging.info(f"{request.remote_addr} {request.method} {request.url}")

# Routes
app.register_blueprint(auth_bp,url_prefix="/api/auth")


# Default error handler
@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    seed_admin()  # similar to Admin() from JS
    app.run(port=Config.PORT, debug=True)