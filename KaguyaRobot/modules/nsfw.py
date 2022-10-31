import requests

from telegram import Update
from import dispatcher

def hneko(update: Update):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/nsfw/neko").json()
    url = api["url"]
    m.reply_photo(url)

hneko_handler = CommandHandler("hneko", hneko)
dispatcher.add_handler(hneko_handler)
