import os
import sys
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

required = {
    "API_ID": "Telegram API ID",
    "API_HASH": "Telegram API Hash",
    "BOT_TOKEN": "Bot Token",
    "MONGO_URL": "MongoDB URL",
    "OWNER_ID": "Owner ID",
    "AI_API_KEY": "AI API Key"
}

missing = [k for k in required if not os.getenv(k)]

if missing:
    print("\n" + "="*60)
    print("ERROR: Missing required environment variables:")
    for var in missing:
        print(f"  - {var}: {required[var]}")
    print("\nSetup: cp .env.example .env && nano .env")
    print("="*60 + "\n")
    sys.exit(1)

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_STRING = os.getenv("SESSION_STRING", "")
MONGO_URL = os.getenv("MONGO_URL")
OWNER_ID = int(os.getenv("OWNER_ID"))
SUDO_USERS = [int(x) for x in os.getenv("SUDO_USERS", "").split()] if os.getenv("SUDO_USERS") else []
AI_API_KEY = os.getenv("AI_API_KEY")
PORT = int(os.getenv("PORT", "10000"))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

logger.info("✅ Configuration loaded")
