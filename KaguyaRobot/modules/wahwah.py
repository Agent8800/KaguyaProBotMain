from KaguyaRobot import pbot as bot
from pyrogram import filters

def parse_com(com, key):
  try:
    r = com.split(key,1)[1]
  except KeyError:
    return None
  r = (r.split(" ", 1)[1] if len(r.split()) >= 1 else None)
  return r

@bot.on_message(filters.command('id'))
async def ids(_,message):
  if message.reply_to_message:
    user = message.reply_to_message.from_user.id
  else:
    com = parse_com(message.text, "id")
    if com:
      user = com.split()[0]
      if user.isdigit():
        user = int(user)
      else:
        user = user.replace("@","")
    else:
      user = None
  if user:
    reply = await bot.get_users(user)
    await message.reply_text(f"**Your ID**: `{message.from_user.id}`\n**{reply.first_name}'s ID**: `{reply.id}`\n**{message.chat.title}'s ID**: `{message.chat.id}`")
  else:
    await message.reply(f"**Your ID**: `{message.from_user.id}`\n**{message.chat.title}'s ID**: `{message.chat.id}`")

#RyuSenpaiX is op
