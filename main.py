import os
import threading
from flask import Flask

# 1. START WEB SERVER FIRST (INSTANTLY)
# We do this before any other imports to ensure the port opens immediately.
web = Flask(__name__)

@web.route('/')
def home():
    return "Criminals Bot is Online"

def run_web():
    # Use the PORT Render gives us, or default to 10000
    port = int(os.environ.get("PORT", 10000))
    print(f"--- Starting Health Check Server on Port {port} ---")
    web.run(host='0.0.0.0', port=port)

# Start the thread immediately
thread = threading.Thread(target=run_web)
thread.daemon = True
thread.start()

# 2. NOW IMPORT THE HEAVY STUFF
import asyncio
from hydrogram import idle
from Criminals import app, assistant

async def start_bot():
    print("--- Connecting to Telegram... ---")
    try:
        await app.start()
        if assistant:
            await assistant.start()
        print("--- Criminals Bot & Assistant Online ---")
        await idle()
    except Exception as e:
        print(f"CRITICAL STARTUP ERROR: {e}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
