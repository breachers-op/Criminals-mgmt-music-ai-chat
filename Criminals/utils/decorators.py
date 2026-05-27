from functools import wraps
from config import OWNER_ID, SUDO_USERS

def admin_only(func):
    @wraps(func)
    async def decorator(client, message):
        if message.chat.type == "private": return await func(client, message)
        user = await client.get_chat_member(message.chat.id, message.from_user.id)
        if user.privileges or message.from_user.id in SUDO_USERS or message.from_user.id == int(OWNER_ID):
            return await func(client, message)
    return decorator
