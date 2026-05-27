from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.fonts import stylish
from config import IMG_URL

@Client.on_message(filters.command("help"))
async def help_cmd(client, message):
    text = (
        f"👋 **ʜᴇʟʟᴏ {message.from_user.first_name}!**\n\n"
        f"ɪ ᴀᴍ ʏᴏᴜʀ **{stylish('ultimate assistant')}**\n"
        f"ᴄʟɪᴄᴋ ᴀ ᴄᴀᴛᴇɢᴏʀʏ ʙᴇʟᴏᴡ ᴛᴏ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀs."
    )
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🛡️ ᴍᴀɴᴀɢᴇ", callback_data="h_mgmt"),
         InlineKeyboardButton("🎵 ᴍᴜsɪᴄ", callback_data="h_music")],
        [InlineKeyboardButton("🤖 ᴀɪ ᴄʜᴀᴛ", callback_data="h_ai"),
         InlineKeyboardButton("⚙️ ᴏᴡɴᴇʀ", callback_data="h_owner")]
    ])
    await message.reply_photo(photo=IMG_URL, caption=text, reply_markup=buttons)
