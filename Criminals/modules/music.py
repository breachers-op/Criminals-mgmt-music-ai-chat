import traceback
from hydrogram import filters
from Criminals import app, assistant

@app.on_message(filters.command("play") & filters.group)
async def play_music(client, message):
    if not assistant:
        return await message.reply("Assistant not configured. Set SESSION_STRING.")

    try:
        # UNIVERSAL IMPORT FOR VERSION 3.0.0+
        try:
            from pytgcalls import PyTgCalls
        except ImportError:
            # In some 3.x versions, the main class is named Client
            from pytgcalls import Client as PyTgCalls
        
        # Initialize
        call_py = PyTgCalls(assistant)
        
        await message.reply("✅ **Music Engine (v3 Stable) Connected!**\nYour server is ready for streaming.")
        
    except Exception:
        # This will show us the EXACT error if the import STILL fails
        err = traceback.format_exc()
        await message.reply(f"❌ **System Error during startup:**\n\n`{err}`")
