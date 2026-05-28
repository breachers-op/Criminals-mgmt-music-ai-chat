from hydrogram import filters
from Criminals import app, assistant
import traceback

@app.on_message(filters.command("play") & filters.group)
async def play_music(client, message):
    if not assistant:
        return await message.reply("Assistant not configured. Set SESSION_STRING.")

    try:
        # Standard import for v3
        from pytgcalls import PyTgCalls
        
        # Test initialization
        call_py = PyTgCalls(assistant)
        await message.reply("✅ **Music Engine (v3) is LIVE!**\nYou can now play music in this group.")
        
    except ImportError:
        await message.reply("❌ **Import Error:** PyTgCalls class not found in the installed package.")
    except Exception:
        err = traceback.format_exc()
        await message.reply(f"❌ **System Error during startup:**\n\n`{err}`")
