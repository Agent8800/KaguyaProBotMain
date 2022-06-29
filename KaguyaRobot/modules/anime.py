import datetime
import html
import textwrap

import bs4
import jikanpy
import requests
from telegram.utils.helpers import mention_html
from KaguyaRobot import OWNER_ID, DRAGONS, REDIS, dispatcher
from KaguyaRobot.modules.disable import DisableAbleCommandHandler
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, ParseMode,
                      Update)
from telegram.ext import CallbackContext, CallbackQueryHandler, run_async
#HEADERS
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

info_btn = "More Information"
kaizoku_btn = "Kaizoku ☠️"
kayo_btn = "Kayo 🏴‍☠️"
indi_btn = "Indi"
prequel_btn = "⬅️ Prequel"
sequel_btn = "Sequel ➡️"
close_btn = "❌"


def shorten(description, info='anilist.co'):
    msg = ""
    if len(description) > 700:
        description = description[0:500] + '....'
        msg += f"\n*Description*:\n_{description}_[Read More]({info})"
    else:
        msg += f"\n*Description*:\n_{description}_"
    return msg


#time formatter from uniborg
def t(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " Days, ") if days else "") + \
        ((str(hours) + " Hours, ") if hours else "") + \
        ((str(minutes) + " Minutes, ") if minutes else "") + \
        ((str(seconds) + " Seconds, ") if seconds else "") + \
        ((str(milliseconds) + " ms, ") if milliseconds else "")
    return tmp[:-2]


def site_search(update: Update, context: CallbackContext, site: str):
    message = update.effective_message
    args = message.text.strip().split(" ", 1)
    more_results = True

    try:
        search_query = args[1]
    except IndexError:
        message.reply_text("Give something to search")
        return

    if site == "kaizoku":
        search_url = f"https://animekaizoku.com/?s={search_query}"
        html_text = requests.get(search_url , headers=headers).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "post-title"})

        if search_result:
            result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>AnimeKaizoku</code>: \n"
            for entry in search_result:
                post_link = "https://animekaizoku.com/" + entry.a['href']
                post_name = html.escape(entry.text)
                result += f"• <a href='{post_link}'>{post_name}</a>\n"
        else:
            more_results = False
            result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>AnimeKaizoku</code>"

    elif site == "kayo":
        search_url = f"https://kayoanime.com/?s={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "post-title"})

        result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>KayoAnime</code>: \n"
        for entry in search_result:

            if entry.text.strip() == "Nothing Found":
                result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>KayoAnime</code>"
                more_results = False
                break

            post_link = entry.a['href']
            post_name = html.escape(entry.text.strip())
            result += f"• <a href='{post_link}'>{post_name}</a>\n"
           
    elif site == "indi":
        search_url = f"https://indianime.com/?s={search_query}"
        html_text = requests.get(search_url , headers=headers).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {"class": "post-title"})

        result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>indianime</code>: \n"
        for entry in search_result:

            if entry.text.strip() == "Nothing Found":
                result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>indianime</code>"
                more_results = False
                break

            post_link = entry.a['href']
            post_name = html.escape(entry.text.strip())
            result += f"• <a href='{post_link}'>{post_name}</a>\n"

    elif site == "anidl":
        search_url = f"https://anidl.org/?s={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "post-title"})

        result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>anidl</code>: \n"
        for entry in search_result:

            if entry.text.strip() == "Nothing Found":
                result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>anidl</code>"
                more_results = False
                break

            post_link = entry.a['href']
            post_name = html.escape(entry.text.strip())
            result += f"• <a href='{post_link}'>{post_name}</a>\n"

    buttons = [[InlineKeyboardButton("See all results", url=search_url)]]

    if more_results:
        message.reply_text(
            result,
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True)
    else:
        message.reply_text(
            result, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


@run_async
def kaizoku(update: Update, context: CallbackContext):
    site_search(update, context, "kaizoku")


@run_async
def kayo(update: Update, context: CallbackContext):
    site_search(update, context, "kayo")
    
@run_async
def indi(update: Update, context: CallbackContext):
    site_search(update, context, "indi")

@run_async
def anidl(update: Update, context: CallbackContext):
    site_search(update, context, "anidl")    
    
    
#plugin by t.me/RCage
@run_async
def meme(update: Update, context: CallbackContext):
    msg = update.effective_message
    meme = requests.get("https://meme-api.herokuapp.com/gimme/Animemes/").json()
    image = meme.get("url")
    caption = meme.get("title")
    if not image:
        msg.reply_text("No URL was received from the API!")
        return
    msg.reply_photo(
                photo=image, caption=caption)
                
                
                
__help__ = """
  ◆/anime - Fetches info on single anime (includes
           buttons to look up for prequels and
           sequels)
  ◆/anilist - Fetches info on multiple possible
             animes related to query
  ◆/character - Fetches info on multiple possible
               characters related to query
  ◆/manga - Fetches info on multiple possible
           mangas related to query
  ◆/airing - Fetches info on airing data for anime
  ◆/browse - get popular, trending or upcoming
            animes
  ◆/whatanime - search any anime media powered by
               tracemoepy
  ◆/watchorder - Fetches watch order for anime
                series
  ◆/fillers - To get list of anime fillers
  ◆/top - to retrieve top animes for a genre or
          tags
  ◆/gettags - Get list of available Tags
  ◆/getgenres - Get list of available Genres
  
                **Anilist Account Help🈚 :**
                
  ◆/auth - Fetches info on how to authorize
           anilist account                
  ◆/flex - Fetches anilist info of an authorised
           user
  ◆/user - Fetches anilist info as per query
  ◆/schedule - Fetches scheduled animes
  ◆/logout - removes authorization
  ◆/favourites - Get Anilist favourites
  ◆/me or /activity - Get Anilist recent activity
   
     **NSFW lock , Anime News and aniCommand disabling☮️ :**
 
  ◆/anisettings - To toggle nsfw lock and airing
                  notifications in groups
  ◆/anidisable - To disable a command in group
  ◆/anienable - To enable a command in group
  ◆/anidisabled - To list disabled commands in a grou
  
          **Anime  Sites Help♐ :**
          
  ◆/kayo*:* Find anime from animekayo website.
  ◆/kaizoku*:* Find anime from kaizoku website.
  ◆/indi*:* Find anime from indianime.com 
  ◆/anidl*:* search an anime on anidl.org
 """
     
 __mod_name__ = "Anime"
 

KAIZOKU_SEARCH_HANDLER = DisableAbleCommandHandler("kaizoku", kaizoku)
KAYO_SEARCH_HANDLER = DisableAbleCommandHandler("kayo", kayo)
INDI_SEARCH_HANDLER = DisableAbleCommandHandler("indi", indi)
ANIDL_SEARCH_HANDLER = DisableAbleCommandHandler("anidl", anidl)
MEME_HANDLER = DisableAbleCommandHandler("meme", meme)


dispatcher.add_handler(KAIZOKU_SEARCH_HANDLER)
dispatcher.add_handler(KAYO_SEARCH_HANDLER)
dispatcher.add_handler(INDI_SEARCH_HANDLER)
dispatcher.add_handler(ANIDL_SEARCH_HANDLER)
dispatcher.add_handler(MEME_HANDLER)
