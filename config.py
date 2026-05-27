import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "12345"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
SESSION_STRING = os.getenv("SESSION_STRING", "") # For Music Assistant
MONGO_URL = os.getenv("MONGO_URL", "")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
SUDO_USERS = [int(x) for x in os.getenv("SUDO_USERS", "").split()] if os.getenv("SUDO_USERS") else []
AI_API_KEY = os.getenv("AI_API_KEY", "")
