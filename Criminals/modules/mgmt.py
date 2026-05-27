from hydrogram import filters
from hydrogram.types import ChatPermissions
from Criminals import app
from Criminals.utils.decorators import admin_only

@app.on_message(filters.command(["mute", "unmute", "ban", "unban"]) & filters.group)
@admin_only
async def mgmt_cmds(client, message):
    if not message.reply_to_message: return await message.reply("Reply to a user.")
    cmd, uid = message.command[0], message.reply_to_message.from_user.id
    if cmd == "mute":
        await client.restrict_chat_member(message.chat.id, uid, ChatPermissions(can_send_messages=False))
    elif cmd == "unmute":
        await client.restrict_chat_member(message.chat.id, uid, ChatPermissions(can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True))
    elif cmd == "ban":
        await client.ban_chat_member(message.chat.id, uid)
    elif cmd == "unban":
        await client.unban_chat_member(message.chat.id, uid)
    await message.reply(f"Successfully {cmd}ed.")
