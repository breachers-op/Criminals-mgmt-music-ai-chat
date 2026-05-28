import os
import threading
import asyncio
from flask import Flask
from hydrogram import idle
from Criminals import app, assistant
from config import OWNER_ID

web = Flask(__name__)
@web.route('/')
def home(): return "Bot is Online"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.run(host='0.0.0.0', port=port)

# Start web server immediately
threading.Thread(target=run_web, daemon=True).start()

async def start_bot():
    print("Connecting to Telegram...")
    await app.start()
    
    # PROOF OF LIFE: This will message you directly
    try:
        await app.send_message(OWNER_ID, "🚀 **Bot is now Online and Connected!**\nIf you see this, the bot can hear you.")
        print("Startup message sent to Owner!")
    except Exception as e:
        print(f"Could not send startup message: {e}")

    if assistant:
        await assistant.start()
    
    print("--- CRIMINALS BOT ACTIVE ---")
    await idle()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
