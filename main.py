import os
from pyrogram import Client, filters

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

Tellybots = Client("Anonymous Sender", bot_token = BOT_TOKEN, api_id = API_ID, api_hash = API_HASH)

 
@Tellybots.on_message(filters.private & ~filters.edited & ~filters.command(["start"]))
async def copy(_, msg):
        await msg.copy(msg.chat.id)

print("Bot is Started")
print("Join @Tellybots.")
Tellybots.run()
