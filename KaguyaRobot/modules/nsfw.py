import requests

import os
import html
import nekos
import requests
from PIL import Image
from telegram import ParseMode
from KaguyaRobot import dispatcher, updater
import KaguyaRobot.modules.sql.nsfw_sql as sql
from KaguyaRobot.modules.log_channel import gloggable
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram.error import BadRequest, RetryAfter, Unauthorized
from telegram.ext import CommandHandler, run_async, CallbackContext
from KaguyaRobot.modules.helper_funcs.filters import CustomFilters
from KaguyaRobot.modules.helper_funcs.chat_status import user_admin
from telegram.utils.helpers import mention_html, mention_markdown, escape_markdown

def hneko(update: Update):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/nsfw/neko").json()
    url = api["url"]
    m.reply_photo(url)

hneko_handler = CommandHandler("hneko", hneko, run_async=True)
dispatcher.add_handler(hneko_handler)
