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

def neko(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/neko").json()
    url = api["url"]
    m.reply_photo(url)

neko_handler = CommandHandler("neko", neko)
dispatcher.add_handler(neko_handler)

def waifu(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/waifu").json()
    url = api["url"]
    m.reply_photo(url)

waifu_handler = CommandHandler("waifu", waifu)
dispatcher.add_handler(waifu_handler)

def shinobu(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/shinobu").json()
    url = api["url"]
    m.reply_photo(url)

shinobu_handler = CommandHandler("shinobu", shinobu)
dispatcher.add_handler(shinobu_handler)

def megumin(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/megumin").json()
    url = api["url"]
    m.reply_photo(url)

megumin_handler = CommandHandler("megumin", megumin)
dispatcher.add_handler(megumin_handler)

def awoo(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/awoo").json()
    url = api["url"]
    m.reply_photo(url)

awoo_handler = CommandHandler("awoo", awoo)
dispatcher.add_handler(awoo_handler)

#Gif




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


def kiss(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/kiss").json()
    url = api["url"]
    m.reply_animation(animation=url)

kiss_handler = CommandHandler("kiss", kiss)
dispatcher.add_handler(kiss_handler)

def lick(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/lick").json()
    url = api["url"]
    m.reply_animation(animation=url)

lick_handler = CommandHandler("lick", lick)
dispatcher.add_handler(lick_handler)

def pat(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/pat").json()
    url = api["url"]
    m.reply_animation(animation=url)

pat_handler = CommandHandler("pat", pat)
dispatcher.add_handler(pat_handler)

def smug(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/smug").json()
    url = api["url"]
    m.reply_animation(animation=url)

smug_handler = CommandHandler("smug", smug)
dispatcher.add_handler(smug_handler)

def bonk(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/bonk").json()
    url = api["url"]
    m.reply_animation(animation=url)

bonk_handler = CommandHandler("bonk", bonk)
dispatcher.add_handler(bonk_handler)

def yeet(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/yeet").json()
    url = api["url"]
    m.reply_animation(animation=url)

yeet_handler = CommandHandler("yeet", yeet)
dispatcher.add_handler(yeet_handler)

def blush(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/blush").json()
    url = api["url"]
    m.reply_animation(animation=url)

blush_handler = CommandHandler("blush", blush)
dispatcher.add_handler(blush_handler)

def smile(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/smile").json()
    url = api["url"]
    m.reply_animation(animation=url)

smile_handler = CommandHandler("smile", smile)
dispatcher.add_handler(smile_handler)

def wave(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/wave").json()
    url = api["url"]
    m.reply_animation(animation=url)

wave_handler = CommandHandler("wave", wave)
dispatcher.add_handler(wave_handler)

def highfive(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/highfive").json()
    url = api["url"]
    m.reply_animation(animation=url)

highfive_handler = CommandHandler("highfive", highfive)
dispatcher.add_handler(highfive_handler)

def handhold(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/handhold").json()
    url = api["url"]
    m.reply_animation(animation=url)

handhold_handler = CommandHandler("handhold", handhold)
dispatcher.add_handler(handhold_handler)

def nom(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/nom").json()
    url = api["url"]
    m.reply_animation(animation=url)

nom_handler = CommandHandler("nom", nom)
dispatcher.add_handler(nom_handler)

def bite(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/bite").json()
    url = api["url"]
    m.reply_animation(animation=url)

bite_handler = CommandHandler("bite", bite)
dispatcher.add_handler(bite_handler)

def glomp(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/glomp").json()
    url = api["url"]
    m.reply_animation(animation=url)

glomp_handler = CommandHandler("glomp", glomp)
dispatcher.add_handler(glomp_handler)

def slap(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/slap").json()
    url = api["url"]
    m.reply_animation(animation=url)

slap_handler = CommandHandler("slap", slap)
dispatcher.add_handler(slap_handler)

def kill(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/kill").json()
    url = api["url"]
    m.reply_animation(animation=url)

kill_handler = CommandHandler("kill", kill)
dispatcher.add_handler(kill_handler)

def kick(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/kick").json()
    url = api["url"]
    m.reply_animation(animation=url)

kick_handler = CommandHandler("kick", kick)
dispatcher.add_handler(kick_handler)

def happy(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/happy").json()
    url = api["url"]
    m.reply_animation(animation=url)

happy_handler = CommandHandler("happy", happy)
dispatcher.add_handler(happy_handler)

def wink(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/wink").json()
    url = api["url"]
    m.reply_animation(animation=url)

wink_handler = CommandHandler("wink", wink)
dispatcher.add_handler(wink_handler)

def poke(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/poke").json()
    url = api["url"]
    m.reply_animation(animation=url)

poke_handler = CommandHandler("poke", poke)
dispatcher.add_handler(poke_handler)

def dance(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/dance").json()
    url = api["url"]
    m.reply_animation(animation=url)

dance_handler = CommandHandler("dance", dance)
dispatcher.add_handler(dance_handler)

def cringe(update: Update, context: CallbackContext):
    m = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/cringe").json()
    url = api["url"]
    m.reply_animation(animation=url)

cringe_handler = CommandHandler("cringe", cringe)
dispatcher.add_handler(cringe_handler)
