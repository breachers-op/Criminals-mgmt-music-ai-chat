import datetime
import time
from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
from Criminals import app # Ensure this matches your bot's app initialization
from config import OWNER_ID, SUDO_USERS

# --- ANTI-SPAM LOGIC ---
SPAM_DATA = {}
SPAM_THRESHOLD = 5  # Max messages
SPAM_WINDOW = 10    # Seconds

@app.on_message(filters.group & ~filters.service, group=-1)
async def anti_spam_logic(_, message: Message):
    if not message.from_user:
        return
    
    chat_id = message.chat.id
    user_id = message.from_user.id
    now = time.time()

    if chat_id not in SPAM_DATA:
        SPAM_DATA[chat_id] = {}
    if user_id not in SPAM_DATA[chat_id]:
        SPAM_DATA[chat_id][user_id] = []

    # Clean old timestamps
    SPAM_DATA[chat_id][user_id] = [t for t in SPAM_DATA[chat_id][user_id] if now - t < SPAM_WINDOW]
    SPAM_DATA[chat_id][user_id].append(now)

    if len(SPAM_DATA[chat_id][user_id]) > SPAM_THRESHOLD:
        try:
            await message.delete() # Deletes even if sender is admin
        except:
            pass

# --- PURGE LOGIC ---
@app.on_message(filters.command("purge") & filters.group)
async def purge_msgs(client, message: Message):
    # Check permissions (Only admins can purge)
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not user.privileges and message.from_user.id not in SUDO_USERS:
        return

    if not message.reply_to_message:
        return await message.reply_text("Reply to a message to start purge.")
    
    chat_id = message.chat.id
    message_ids = []
    for m_id in range(message.reply_to_message.id, message.id):
        message_ids.append(m_id)
        if len(message_ids) == 100:
            await client.delete_messages(chat_id, message_ids)
            message_ids = []
    
    if message_ids:
        await client.delete_messages(chat_id, message_ids)
    
    await message.reply_text("✨ Purge Complete.")

# --- TIMELY MUTE LOGIC ---
def parse_time(time_str):
    unit = time_str[-1].lower()
    try:
        value = int(time_str[:-1])
        if unit == 'm': return datetime.timedelta(minutes=value)
        if unit == 'h': return datetime.timedelta(hours=value)
        if unit == 'd': return datetime.timedelta(days=value)
    except:
        return None

@app.on_message(filters.command("tmute") & filters.group)
async def timely_mute(client, message: Message):
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not user.privileges and message.from_user.id not in SUDO_USERS:
        return

    if not message.reply_to_message:
        return await message.reply_text("Reply to a user to mute them.")
    
    args = message.text.split()
    if len(args) < 2:
        return await message.reply_text("Usage: `/tmute 1h` (m/h/d)")

    duration = parse_time(args[1])
    if not duration:
        return await message.reply_text("Invalid time format. Use 10m, 1h, or 1d.")

    until_date = datetime.datetime.now() + duration
    try:
        await client.restrict_chat_member(
            message.chat.id,
            message.reply_to_message.from_user.id,
            permissions=ChatPermissions(can_send_messages=False),
            until_date=until_date
        )
        await message.reply_text(f"🔇 Muted for {args[1]}.")
    except Exception as e:
        await message.reply_text(f"Error: {e}")
