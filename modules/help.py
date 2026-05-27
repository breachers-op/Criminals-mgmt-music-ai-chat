from hydrogram import filters
from Criminals import app

@app.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply("**Criminals Bot**\n/ai - Chat\n/mute /ban - Admin\n/setflood - Security\n/purge - Delete\nInline: @botname text")
