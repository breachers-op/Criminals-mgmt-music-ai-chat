from hydrogram import filters
from Criminals import app, assistant

# Defensive Import
try:
    from pytgcalls import PyTgCalls
except ImportError:
    try:
        from pytgcalls.client import PyTgCalls
    except ImportError:
        PyTgCalls = None

# Initialize only if import was successful
call_py = None
if assistant and PyTgCalls:
    try:
        call_py = PyTgCalls(assistant)
    except Exception as e:
        print(f"Music Error: {e}")

@app.on_message(filters.command("play") & filters.group)
async def play_music(client, message):
    if not assistant:
        return await message.reply("Assistant not configured. Set SESSION_STRING.")
    if not call_py:
        return await message.reply("❌ Music library (PyTgCalls) failed to load on the server.")
    
    await message.reply("🎵 **Music Module Active**\nChecking voice chat...")
