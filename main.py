import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types.bots_and_keyboards.reply_keyboard_markup import ReplyKeyboardMarkup
from script import Script
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
@Tellybots.on_callback_query()
async def button(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=Script.START_TEXT.format(update.from_user.mention),
            reply_markup=Script.START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=Script.HELP_TEXT,
            reply_markup=Script.HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=Script.ABOUT_TEXT.format((await bot.get_me()).username),
            reply_markup=Script.ABOUT_BUTTONS,
            disable_web_page_preview=True
        )

        else:
            await update.message.delete()

@Tellybots.on_message(filters.private & ~filters.edited & ~filters.command(["start"]))
async def copy(_, msg):
    if msg.caption:
        await msg.copy(msg.chat.id, reply_markup=InlineKeyboardMarkup([Script.remove_button]), disable_notification=True, reply_to_message_id=msg.message_id)
    else:
        await msg.copy(msg.chat.id)

print("Bot is Started")
print("Join @Tellybots.")
Tellybots.run()
