
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Script(object):



    START_TEXT = """
Hey {} 

I am Telegram Anonymous Sender Bot

I can help you to remove caption and tag from media

Use Help Command to Know How to Use me

Made With 💕 By @Tellybots_4u
"""
    HELP_TEXT = """
Recommended
➠ Just Send media To Remove Caption

Recommended
➠ Just readd a Caption to add Caption

Made With 💕 By @Tellybots_4u
"""
    ABOUT_TEXT = """
 **🤖 Bot :** Anonymous-Sender\n
 **👲 Developer :** [Tellybots_4u](https://telegram.me/tellybots_4u)\n
 **👥 Channel :** [Tellybots_4u](https://telegram.me/tellybots_4u)\n
 **❄️ Credits :** Everyone in this journey\n
 **🍴 Source :** [Click here](https://t.me/tellybots_digital)\n
 **📝 Language :** [Python3](https://python.org)\n
 **📚 Library :** [Pyrogram v1.2.0](https://pyrogram.org)\n
 **🌟 Server :** [Heroku](https://heroku.com)\n
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 Update Channel', url='https://telegram.me/tellybots_4u'),
        InlineKeyboardButton('💬 Support Group', url='https://telegram.me/tellybots_support')
        ],[
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    # Home Button
    home_button = [[InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]]

    # Remove Caption Button
    remove_button = [InlineKeyboardButton("� Remove Caption �", callback_data="remove")]

    # Add caption button
    add_button = [InlineKeyboardButton("💬 Re-Add Caption 💬", callback_data="add")]

@Client.on_callback_query()
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
            reply_markup=InlineKeyboardMarkup(Data.home_button),
        )
    if callback_query.data.lower() == "remove":
        caption = ""
        await main.edit_message_caption(
            chat_id=chat_id, message_id=message_id, caption=caption, reply_markup=InlineKeyboardMarkup([Data.add_button])
        )
    if callback_query.data.lower() == "add":
        caption = callback_query.message.reply_to_message.caption
        if caption:
            await main.edit_message_caption(
                chat_id=chat_id, message_id=message_id, caption=caption, reply_markup=InlineKeyboardMarkup([Data.remove_button])
            )
        else:
            await callback_query.answer("The original message has been deleted or their is no previous caption.", show_alert=True)
