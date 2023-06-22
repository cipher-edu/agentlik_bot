# from telegram.ext import Updater, CommandHandler

# TOKEN = '5304967823:AAGUWKnofSfuEeQ7D3Hm6voK1O9bTWh_Y3s'
# CHANNEL_ID = '1513797200'

# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text='Bot started!')

# def check_user(update, context):
#     user_id = update.effective_user.id
#     channel_member = context.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
    
#     if channel_member.status == 'member' or channel_member.status == 'creator':
#         message = 'User is available in the channel.'
#     else:
#         message = 'User is not available in the channel.'
    
#     context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# def main():
#     updater = Updater(bot_token=TOKEN, use_context=True)
#     dispatcher = updater.dispatcher

#     start_handler = CommandHandler('start', start)
#     check_user_handler = CommandHandler('check_user', check_user)

#     dispatcher.add_handler(start_handler)
#     dispatcher.add_handler(check_user_handler)

#     updater.start_polling()

# if __name__ == '__main__':
#     main()
