from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytgcalls.types import AudioPiped
from utils.fonts import stylish

@Client.on_message(filters.command("play") & filters.group)
async def play_audio(client, message):
    from main import call_py
    if not message.reply_to_message or not message.reply_to_message.audio:
        return await message.reply(f"🎵 **{stylish('reply to audio to stream')}**")
    
    m = await message.reply(f"⏳ **{stylish('processing stream')}...**")
    file_path = await message.reply_to_message.download()
    
    await call_py.join_group_call(message.chat.id, AudioPiped(file_path))
    
    buttons = InlineKeyboardMarkup([[
        InlineKeyboardButton("⏸ ᴘᴀᴜsᴇ", callback_data="pause"),
        InlineKeyboardButton("⏹ sᴛᴏᴘ", callback_data="stop")
    ]])
    
    await m.edit(
        f"🎶 **{stylish('now streaming on vc')}**\n\n"
        f"📌 **ᴛɪᴛʟᴇ:** `{message.reply_to_message.audio.file_name}`\n"
        f"👤 **ʀᴇǫᴜᴇsᴛ:** {message.from_user.mention}\n"
        f"⏳ **ᴘʀᴏɢʀᴇss:** ━━🌑━━━━━━━\n"
        "━━━━━━━━━━━━━━━━━━━━",
        reply_markup=buttons
    )
