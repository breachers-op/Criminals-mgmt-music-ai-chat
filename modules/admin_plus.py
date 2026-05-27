import time
from hydrogram import Client, filters
from hydrogram.types import ChatPermissions
from Criminals import app
from Criminals.utils.decorators import admin_only
from Criminals.database.flood_db import get_flood_limit, set_flood_limit_db

FLOOD_DATA = {}

@app.on_message(filters.group & ~filters.service, group=-1)
async def antiflood_handler(client, message):
    if not message.from_user: return
    chat_id, user_id, now = message.chat.id, message.from_user.id, time.time()
    limit = await get_flood_limit(chat_id)
    
    if chat_id not in FLOOD_DATA: FLOOD_DATA[chat_id] = {}
    if user_id not in FLOOD_DATA[chat_id]: FLOOD_DATA[chat_id][user_id] = []
    FLOOD_DATA[chat_id][user_id] = [t for t in FLOOD_DATA[chat_id][user_id] if now - t < 10]
    FLOOD_DATA[chat_id][user_id].append(now)

    if len(FLOOD_DATA[chat_id][user_id]) > limit:
        try:
            await message.delete() # Affects everyone
            user = await client.get_chat_member(chat_id, user_id)
            if not user.privileges:
                await client.restrict_chat_member(chat_id, user_id, ChatPermissions(can_send_messages=False))
        except: pass

@app.on_message(filters.command("setflood"))
@admin_only
async def set_flood(client, message):
    if len(message.command) < 2: return await message.reply("Usage: /setflood 7")
    limit = int(message.command[1])
    await set_flood_limit_db(message.chat.id, limit)
    await message.reply(f"Flood limit updated to {limit}")

@app.on_message(filters.command("purge"))
@admin_only
async def purge(client, message):
    if not message.reply_to_message: return
    m_ids = list(range(message.reply_to_message.id, message.id))
    for i in range(0, len(m_ids), 100):
        await client.delete_messages(message.chat.id, m_ids[i:i+100])
