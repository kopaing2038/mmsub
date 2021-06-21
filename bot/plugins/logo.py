import os
import shutil
from os import execl
from time import sleep
from sys import executable
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, RPCError
from bot import SUDO_USERS, DOWNLOAD_DIRECTORY, LOGGER, SUPPORT_CHAT_LINK
from bot.config import Messages as tr
from pyrogram import Client, filters
from bot.helpers.sql_helper import chidss
from bot.plugins.vidsearch import download_vid
from bot.plugins.cmdescription import desonly
from bot.config import BotCommands, Messages

@Client.on_message(filters.private & filters.incoming & filters.command(BotCommands.Logo) )
async def _logo(client, message):
    user_id = message.from_user.id
    if len(message.command) > 1:
        chid = message.text.split(' ',maxsplit=1)[1]
        
        chidss._set(user_id, chid)
       
        await message.reply_text(
                text="ခင်ဗျား ချန်နယ်ကို ကျနော် အသိအမှတ်ပြု လိုက်ပါပြီ",
                disable_web_page_preview=True,
            )
       
    else:
        await message.reply_text(
            text="မှားနေတယ် ငါ့လူ ... ချန်နယ် အိုင်ဒီ ထည့်ပေးပါ",
            disable_web_page_preview=True,
        )