import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types.bots_and_keyboards.reply_keyboard_markup import ReplyKeyboardMarkup

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

Tellybots = Client("Anonymous Sender", bot_token = BOT_TOKEN, api_id = API_ID, api_hash = API_HASH)



@Tellybots.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    await update.reply_text(
        text=Script.START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=Script.START_BUTTONS
    )


@Tellybots.on_message(filters.private & ~filters.edited & ~filters.command(["start"]))
async def copy(_, msg):
    if msg.caption:
        await msg.copy(msg.chat.id, reply_markup=InlineKeyboardMarkup([Script.remove_button]), disable_notification=True, reply_to_message_id=msg.message_id)
    else:
        await msg.copy(msg.chat.id)

print("Bot is Started")
print("Join @Tellybots.")
Tellybots.run()
