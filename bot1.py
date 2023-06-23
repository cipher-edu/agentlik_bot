from telegram.ext import Updater, CommandHandler
def subscribe(update, context):
    chat_id = update.effective_chat.id
    # Add your subscription logic here
    context.bot.send_message(chat_id=chat_id, text='You have successfully subscribed!')

def main():
    updater = Updater(token='5304967823:AAGUWKnofSfuEeQ7D3Hm6voK1O9bTWh_Y3s', use_context=True)
    dispatcher = updater.dispatcher

    # Register the command handler
    dispatcher.add_handler(CommandHandler('subscribe', subscribe))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
