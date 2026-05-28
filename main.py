import os
import asyncio
from flask import Flask
from threading import Thread
from hydrogram import idle
from Criminals import app, assistant

# 1. SETUP WEB SERVER IMMEDIATELY
web = Flask(__name__)

@web.route('/')
def home():
    return "Bot is Online"

def run_web():
    # Render and Railway provide 'PORT'. Default to 8080 if not found.
    port = int(os.environ.get("PORT", 10000))
    # '0.0.0.0' is REQUIRED for Render/Railway
    web.run(host="0.0.0.0", port=port)

# 2. BOT STARTUP LOGIC
async def start_bot():
    try:
        await app.start()
        if assistant:
            await assistant.start()
        print("--- Criminals Bot & Assistant Online ---")
        await idle()
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")

if __name__ == "__main__":
    # START WEB SERVER IN BACKGROUND FIRST
    # This tells Render "I am alive" immediately
    t = Thread(target=run_web)
    t.daemon = True
    t.start()
    
    # NOW START THE BOT
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
