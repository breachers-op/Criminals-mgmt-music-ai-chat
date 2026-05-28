import os
import threading
import asyncio
from flask import Flask
from hydrogram import idle

# --- 1. IMMEDIATE WEB SERVER ---
web = Flask(__name__)
@web.route('/')
def home(): return "Bot is Alive"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    print(f"[DEBUG] Flask starting on port {port}")
    web.run(host='0.0.0.0', port=port)

threading.Thread(target=run_web, daemon=True).start()

# --- 2. DELAYED IMPORTS ---
print("[DEBUG] Loading Bot Modules...")
from Criminals import app, assistant

async def start_bot():
    print("[DEBUG] Attempting to start Main Bot...")
    try:
        await app.start()
        print(f"[DEBUG] Main Bot started as @{(await app.get_me()).username}")
        
        if assistant:
            print("[DEBUG] Attempting to start Assistant...")
            try:
                await assistant.start()
                print(f"[DEBUG] Assistant started as @{(await assistant.get_me()).username}")
            except Exception as e:
                print(f"[ERROR] Assistant failed to start: {e}")
        
        print("--- ALL SYSTEMS ONLINE: SEND A MESSAGE TO THE BOT ---")
        await idle()
    except Exception as e:
        print(f"[CRITICAL] Bot failed to start: {e}")

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start_bot())
    except KeyboardInterrupt:
        pass
