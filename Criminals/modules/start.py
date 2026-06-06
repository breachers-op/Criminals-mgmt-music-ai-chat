import logging
from hydrogram import Client, filters
from hydrogram.types import Message

logger = logging.getLogger(__name__)

@Client.on_message(filters.private & filters.command("start"))
async def start(client: Client, message: Message):
    user = message.from_user
    text = f"""
🤖 **Welcome to Criminals Bot!**

Hello {user.mention}!

✨ **Features:**
  • 🛡️ Group Management (ban, kick, mute)
  • 🎵 Music Streaming
  • 🤖 AI Chat

📝 **Commands:**
  /help - Show commands
  /ai - Chat with AI

Made by @breachers_op ❤️
"""
    try:
        await message.reply_text(text, quote=True)
        logger.info(f"Start sent to {user.id}")
    except Exception as e:
        logger.error(f"Error: {e}")

logger.info("✅ Start module loaded")
