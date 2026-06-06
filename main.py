#!/usr/bin/env python3
import os, sys, threading, asyncio, logging
from flask import Flask, jsonify
from hydrogram import idle

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', 
                   handlers=[logging.StreamHandler(), logging.FileHandler('bot.log')])
logger = logging.getLogger(__name__)

try:
    from Criminals import app, assistant
    from config import OWNER_ID, PORT
except Exception as e:
    logger.error(f"❌ Import failed: {e}")
    sys.exit(1)

web = Flask(__name__)

@web.route('/')
def home():
    return jsonify({"status": "online", "bot": "Criminals"}), 200

@web.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

def run_web():
    try:
        web.run(host='0.0.0.0', port=PORT, debug=False, use_reloader=False)
    except Exception as e:
        logger.error(f"❌ Web server error: {e}")

threading.Thread(target=run_web, daemon=True).start()
logger.info(f"✅ Web server started on port {PORT}")

async def start_bot():
    try:
        logger.info("\n" + "="*60)
        logger.info("🤖 CRIMINALS BOT STARTING")
        logger.info("="*60)
        
        await app.start()
        logger.info("✅ Bot connected")
        
        try:
            await app.send_message(OWNER_ID, "🚀 **Criminals Bot Online!**")
            logger.info("✅ Notification sent")
        except:
            pass
        
        if assistant:
            try:
                await assistant.start()
                logger.info("✅ Music bot connected")
            except Exception as e:
                logger.warning(f"⚠️ Music bot error: {e}")
        
        logger.info("\n" + "="*60)
        logger.info("🎯 BOT FULLY ACTIVE")
        logger.info("="*60 + "\n")
        
        await idle()
        
    except Exception as e:
        logger.error(f"❌ Bot error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        logger.info("\n⛔ Bot stopped")
    except Exception as e:
        logger.error(f"❌ {e}")
        sys.exit(1)
