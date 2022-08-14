from KaguyaRobot import telethn as tbot
import os
from KaguyaRobot.events import register
import secureme
from KaguyaRobot.modules.language import gs


@register(pattern="^/encrypt ?(.*)")
async def hmm(event):
    if event.reply_to_msg_id:
        lel = await event.get_reply_message()
        cmd = lel.text
    else:
        cmd = event.pattern_match.group(1)
    Text = cmd
    k = secureme.encrypt(Text)
    await event.reply(k)


@register(pattern="^/decrypt ?(.*)")
async def hmm(event):
    if event.reply_to_msg_id:
        lel = await event.get_reply_message()
        ok = lel.text
    else:
        ok = event.pattern_match.group(1)
    Text = ok
    k = secureme.decrypt(Text)
    await event.reply(k)

def helps(chat):
    return gs(chat, "encrypt_help")
    
__mod_name__ = "Encrypt/Decrypt"
