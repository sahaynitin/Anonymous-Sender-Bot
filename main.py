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
async def _calls(main, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    if callback_query.data.lower() == "home":
        user = await main.get_me()
        mention = user["mention"]
        await main.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Script.START_TEXT.format(callback_query.from_user.mention, mention),
            reply_markup=InlineKeyboardMarkup(Script.START_BUTTONS),
        )
    if callback_query.data.lower() == "about":
        await main.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Script.ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Script.home_button),
        )
    if callback_query.data.lower() == "remove":
        caption = ""
        await main.edit_message_caption(
            chat_id=chat_id, message_id=message_id, caption=caption, reply_markup=InlineKeyboardMarkup([Script.add_button])
        )
    if callback_query.data.lower() == "add":
        caption = callback_query.message.reply_to_message.caption
        if caption:
            await main.edit_message_caption(
                chat_id=chat_id, message_id=message_id, caption=caption, reply_markup=InlineKeyboardMarkup([Script.remove_button])
            )
        else:
            await callback_query.answer("The original message has been deleted or their is no previous caption.", show_alert=True)

@Tellybots.on_message(filters.private & ~filters.edited & ~filters.command(["start"]))
async def copy(_, msg):
    if msg.caption:
        await msg.copy(msg.chat.id, reply_markup=InlineKeyboardMarkup([Script.remove_button]), disable_notification=True, reply_to_message_id=msg.message_id)
    else:
        await msg.copy(msg.chat.id)

print("Bot is Started")
print("Join @Tellybots.")
Tellybots.run()
