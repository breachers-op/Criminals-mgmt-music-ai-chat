import traceback
from hydrogram import filters
from Criminals import app, assistant

@app.on_message(filters.command("play") & filters.group)
async def play_music(client, message):
    if not assistant:
        return await message.reply("Assistant not configured. Set SESSION_STRING.")

    try:
        # DEEP IMPORT STRATEGY
        try:
            from pytgcalls import PyTgCalls
        except ImportError:
            # Try loading from the internal client folder
            from pytgcalls.pytgcalls import PyTgCalls
        
        # Try to initialize
        call_py = PyTgCalls(assistant)
        await message.reply("✅ **Music Engine v3 (Dev24) Connected!**\nYou are ready to play.")
        
    except Exception:
        # This will show us the EXACT system error (e.g., missing .so file)
        err = traceback.format_exc()
        await message.reply(f"❌ **Detailed System Error:**\n\n`{err}`")
