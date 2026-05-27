from hydrogram import Client, filters
from hydrogram.types import InlineQueryResultArticle, InputMessageContent
import uuid

F_MAP = str.maketrans("abcdefghijklmnopqrstuvwxyz", "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ")

@Client.on_inline_query()
async def inline_fonts(client, query):
    txt = query.query or "Type..."
    results = [
        InlineQueryResultArticle(id=str(uuid.uuid4()), title="Small Caps", input_message_content=InputMessageContent(txt.translate(F_MAP))),
        InlineQueryResultArticle(id=str(uuid.uuid4()), title="Magic ✨", input_message_content=InputMessageContent(f"✨ {txt} ✨")),
        InlineQueryResultArticle(id=str(uuid.uuid4()), title="Fire 🔥", input_message_content=InputMessageContent(f"🔥 {txt} 🔥"))
    ]
    await query.answer(results, cache_time=1)
