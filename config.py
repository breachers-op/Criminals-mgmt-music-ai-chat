import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
SESSION_STRING = os.getenv("SESSION_STRING", "")
MONGO_URL = os.getenv("MONGO_URL", "")
AI_API_KEY = os.getenv("AI_API_KEY", "")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
SUDO_USERS = [int(x) for x in os.getenv("SUDO_USERS", "").split()]
SUDO_USERS.append(OWNER_ID)

# UI Settings
IMG_URL = "https://telegra.ph/file/0c32f8319688001d93198.jpg" # Replace with your banner
