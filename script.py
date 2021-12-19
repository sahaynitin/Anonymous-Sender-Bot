from pyrogram import Client as Tellybots
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
class Script(object):



    START_TEXT = """
Hey {} 

I am Telegram Anonymous Sender Bot

Just Send me a post, I will send you back with anonymous sender

Use Help Command to Know How to Use me

Made With 💕 By @Tellybots_4u
"""
    HELP_TEXT = """
Recommended
➠ Just Forward Me any post or Media to get started

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



