from hydrogram import filters
from Criminals import app, assistant

# Delayed import to prevent startup crashes
@app.on_message(filters.command("play") & filters.group)
async def play_music(client, message):
    if not assistant:
        return await message.reply("Assistant not configured. Set SESSION_STRING.")
    
    try:
        from pytgcalls import PyTgCalls
        # In 3.x, initialization is simpler
        call_py = PyTgCalls(assistant)
        await message.reply("🎵 **Music Engine Ready (v3.0.0)**\nChecking voice chat...")
    except ImportError:
        return await message.reply("❌ Music library not installed correctly on server.")
    except Exception as e:
        return await message.reply(f"❌ Error: {e}")
