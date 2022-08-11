import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM, Message

@Client.on_chat_join_request()
async def join_request_manage(client:Client, message:Message):
    
    user = message.from_user.id 
    chat = message.chat.id
    text = 'Want to join this group'
    await client.send_message(message.chat.id, text, reply_markup=IKM([[IKB('Approve', f'wlcm_approve-{message.from_user.id}'), IKB('Decline', f'wlcm_decline-{message.from_user.id}')]]))
     
     
@Client.on_callback_query(filters.regex('wlcm'))
async def start_quer(client, callback_query):
    if 'approve' in callback_query.data:
        user=callback_query.data.split('-', 1)[1]
        get_admin = await client.get_chat_member(chat_id=callback_query.message.chat.id, user_id=callback_query.from_user.id)
        if get_admin.status == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
            request_stats = await client.approve_chat_join_request(chat_id=int(callback_query.message.chat.id), user_id=int(user))
            if request_stats is True: 
                await callback_query.answer('Approved Request')
                await asyncio.sleep(5)
                await callback_query.message.delete()
            else:
                await callback_query.answer('Error While Processing Request')    
        else:
            await callback_query.answer('Yamete Senpai')      
             
    elif 'decline' in callback_query.data:
        user=callback_query.data.split('-', 1)[1]
        get_admin = await client.get_chat_member(chat_id=callback_query.message.chat.id, user_id=callback_query.from_user.id)
        if get_admin.status == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
            request_stats = await client.decline_chat_join_request(chat_id=int(callback_query.message.chat.id), user_id=int(user))
            if request_stats is True: 
                await callback_query.answer('Rejected Request')
                await asyncio.sleep(5)
                await callback_query.message.delete()
            else:
                await callback_query.answer('Error While Processing Request')    
        else:
            await callback_query.answer('Yamete Senpai')
