from pytgcalls import PyTgCalls
from Criminals import assistant
from hydrogram import filters

# In version 3.0.0+, initialization is simpler
if assistant:
    call_py = PyTgCalls(assistant)

@assistant.on_message(filters.command("play") & filters.group)
async def play_music(client, message):
    # Music logic here...
    await message.reply("🎵 Music Player Ready.")
