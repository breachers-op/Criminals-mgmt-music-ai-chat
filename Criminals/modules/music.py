import traceback
from hydrogram import filters
from Criminals import app, assistant

@app.on_message(filters.command("play") & filters.group)
async def play_music(client, message):
    if not assistant:
        return await message.reply("Assistant not configured. Set SESSION_STRING.")

    try:
        # We try to import and initialize inside the command
        from pytgcalls import PyTgCalls
        from pytgcalls.types import AudioPiped
        
        # Test if it can initialize
        call_py = PyTgCalls(assistant)
        await message.reply("✅ **Music Engine is Ready!**\nYou can now stream in this voice chat.")
        
    except ImportError:
        # Show the actual system error in the chat
        err = traceback.format_exc()
        await message.reply(f"❌ **Library Missing:**\n\n`{err}`")
    except Exception as e:
        await message.reply(f"❌ **Startup Error:**\n\n`{e}`")
