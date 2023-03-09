from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from KaguyaRobot import dispatcher
from telegram import Bot

def tinvitelink(update: Update, context: CallbackContext):
    """Generate a group invite link with a maximum number of users."""
    try:
        # Get the maximum number of users from the command argument
        max_users = int(context.args[0])
    except (IndexError, ValueError):
        # Handle errors if no argument or invalid argument is provided
        update.message.reply_text("Please provide a valid maximum number of users.")
        return

    # Generate a new invite link with the Telegram Bot API
    chat_id = update.message.chat_id
    invite_link = context.bot.export_chat_invite_link(chat_id)

    # Set the maximum number of users allowed in the group
    context.bot.set_chat_member_maximum_ban_count(chat_id, max_users)

    # Send the invite link back to the user who requested it
    message = f"Here's a new invite link that can accept up to {max_users} users: {invite_link}"
    update.message.reply_text(message)

# Register the command handler with the dispatcher
tinvitelink_handler = CommandHandler("tinvitelink", tinvitelink)
dispatcher.add_handler(tinvitelink_handler)
