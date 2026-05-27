from hydrogram import filters
from Criminals import app
from config import AI_API_KEY
import google.generativeai as genai

if AI_API_KEY:
    genai.configure(api_key=AI_API_KEY)
    ai_model = genai.GenerativeModel('gemini-pro')

@app.on_message(filters.command("ai"))
async def chat_ai(client, message):
    if not AI_API_KEY or len(message.command) < 2: return
    res = ai_model.generate_content(message.text.split(None, 1)[1])
    await message.reply(res.text)
