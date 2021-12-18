import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types.bots_and_keyboards.reply_keyboard_markup import ReplyKeyboardMarkup

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

Tellybots = Client("Anonymous Sender", bot_token = BOT_TOKEN, api_id = API_ID, api_hash = API_HASH)


@Tellybots.on_message(filters.caption & filters.private)
async def addorno(client, message):
    msg = message.message._id
    await message.reply_text('start bot go to the option', quote=True,
    reply_markup=InlineKeyboardMarkup([InlineKeyboardButton(text="yes",
    callback_data=f"yes-{msg}"),
    InlineKeyboardButton(text="No",
    callback_data=f"no-{msg}")])
    )

@Tellybots.on_message(filters.private & filters.text | filters.media)
async def SDBot(client, message):
    await message.copy(message.chat.id)

print("Bot is Started")
print("Join @Tellybots.")
Tellybots.run()
