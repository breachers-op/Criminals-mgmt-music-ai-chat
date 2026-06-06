import logging
from hydrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_STRING

logger = logging.getLogger(__name__)

app = Client(
    "CriminalsBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Criminals.modules"),
    workdir="./"
)

logger.info("✅ Bot client initialized")

assistant = None
if SESSION_STRING:
    assistant = Client(
        "CriminalsAssistant",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION_STRING,
        workdir="./"
    )
    logger.info("✅ Music bot initialized")
else:
    logger.warning("⚠️ Music bot disabled (no SESSION_STRING)")

__all__ = ["app", "assistant"]
