import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls
from config import *

app = Client("Bot", API_ID, API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="modules"))
userbot = Client("Assistant", API_ID, API_HASH, session_string=SESSION_STRING)
call_py = PyTgCalls(userbot)

async def start_bot():
    await app.start()
    await userbot.start()
    await call_py.start()
    print("✅ Bot is live and stylish!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
