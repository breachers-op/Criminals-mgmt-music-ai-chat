import traceback
from hydrogram import filters
from Criminals import app, assistant

@app.on_message(filters.command("play") & filters.group)
async def play_music(client, message):
    if not assistant:
        return await message.reply("Assistant not configured. Set SESSION_STRING.")

    try:
        # UNIVERSAL IMPORT LOGIC
        try:
            from pytgcalls import PyTgCalls
        except ImportError:
            # Fallback for some specific builds
            from pytgcalls.pytgcalls import PyTgCalls
        
        # Test initialization
        call_py = PyTgCalls(assistant)
        await message.reply("✅ **Music Engine successfully loaded!**\nYour server now supports voice chat streaming.")
        
    except ImportError as e:
        await message.reply(
            f"❌ **Import Error:** `{e}`\n\n"
            "This usually means the audio libraries (libopus) were missing during deployment."
        )
    except Exception:
        err = traceback.format_exc()
        await message.reply(f"❌ **Startup Error:**\n\n`{err}`")
