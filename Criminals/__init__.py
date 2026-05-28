from hydrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_STRING

# We use "Criminals.modules" as a python package path
app = Client(
    "CriminalsBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Criminals.modules") 
)

assistant = Client(
    "CriminalsAssistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING
) if SESSION_STRING else None
