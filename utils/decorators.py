from pyrogram import filters
from config import OWNER_ID, SUDO_USERS

def sudo_only(func):
    async def wrapper(client, message):
        if message.from_user.id not in SUDO_USERS:
            return await message.reply("❌ **sᴜᴅᴏ ᴘʀɪᴠɪʟᴇɢᴇs ʀᴇǫᴜɪʀᴇᴅ**")
        return await func(client, message)
    return wrapper

def owner_only(func):
    async def wrapper(client, message):
        if message.from_user.id != OWNER_ID:
            return await message.reply("❌ **ᴏᴡɴᴇʀ ᴏɴʟʏ ᴄᴏᴍᴍᴀɴᴅ**")
        return await func(client, message)
    return wrapper
