import google.generativeai as genai
from pyrogram import filters, Client
from config import AI_API_KEY
from utils.fonts import stylish

genai.configure(api_key=AI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

@Client.on_message((filters.mentioned | filters.private) & ~filters.bot & ~filters.command(["start", "help"]))
async def ai_chat(client, message):
    await client.send_chat_action(message.chat.id, "typing")
    prompt = message.text.replace(f"@{client.me.username}", "").strip()
    
    try:
        res = model.generate_content(f"Be polite and professional. Question: {prompt}")
        await message.reply_text(f"🤖 **{stylish('ai response')}**\n━━━━━━━━━━━━\n{res.text}")
    except:
        await message.reply_text(f"🙏 **{stylish('lets keep it respectful')}**")
