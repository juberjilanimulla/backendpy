import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    PORT = int(os.getenv("PORT", 5000))
    MONGODB_URL = os.getenv("MONGODB_URL")