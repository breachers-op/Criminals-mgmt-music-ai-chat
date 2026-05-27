from pyrogram import filters, Client
from pyrogram.types import ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton
from utils.fonts import stylish
from utils.decorators import sudo_only

@Client.on_message(filters.command("ban") & filters.group)
@sudo_only
async def ban_user(client, message):
    if not message.reply_to_message:
        return await message.reply(f"❗ **{stylish('reply to a user to ban')}**")
    
    user = message.reply_to_message.from_user
    await client.ban_chat_member(message.chat.id, user.id)
    await message.reply(
        f"🚫 **{stylish('user banned')}**\n\n"
        f"👤 **ᴜsᴇʀ:** {user.mention}\n"
        f"🆔 **ɪᴅ:** `{user.id}`\n"
        f"👮 **ᴀᴅᴍɪɴ:** {message.from_user.mention}\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )
