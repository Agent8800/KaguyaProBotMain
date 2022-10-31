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

def hneko(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/nsfw/neko").json()
    url = api["url"]
    m.reply_photo(url)

hneko_handler = CommandHandler("hneko", hneko)
dispatcher.add_handler(hneko_handler)

def kiss(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/kiss").json()
    url = api["url"]
    m.reply_animation(animation=url)

kiss_handler = CommandHandler("kiss", kiss)
dispatcher.add_handler(kiss_handler)

def bully(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/bully").json()
    url = api["url"]
    m.reply_animation(animation=url)

bully_handler = CommandHandler("bully", bully)
dispatcher.add_handler(bully_handler)

def cuddle(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/cuddle").json()
    url = api["url"]
    m.reply_animation(animation=url)

cuddle_handler = CommandHandler("cuddle", cuddle)
dispatcher.add_handler(cuddle_handler)

def hug(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/hug").json()
    url = api["url"]
    m.reply_animation(animation=url)

hug_handler = CommandHandler("hug", hug)
dispatcher.add_handler(hug_handler)

def cry(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/cry").json()
    url = api["url"]
    m.reply_animation(animation=url)

cry_handler = CommandHandler("cry", cry)
dispatcher.add_handler(cry_handler)

def awoo(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/awoo").json()
    url = api["url"]
    m.reply_animation(animation=url)

awoo_handler = CommandHandler("awoo", awoo)
dispatcher.add_handler(awoo_handler)

