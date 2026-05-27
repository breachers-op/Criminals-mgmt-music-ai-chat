import asyncio
from hydrogram import idle
from Criminals import app, assistant
from flask import Flask
from threading import Thread

# Flask for Health Checks on Railway/Koyeb
web = Flask(__name__)
@web.route('/')
def home(): return "Bot is Alive!"

def run_web():
    web.run(host="0.0.0.0", port=8080)

async def start_bot():
    print("Starting Main Bot...")
    await app.start()
    if assistant:
        print("Starting Assistant...")
        await assistant.start()
    print("Everything is Online!")
    await idle()

if __name__ == "__main__":
    Thread(target=run_web).start()
    asyncio.get_event_loop().run_until_complete(start_bot())
