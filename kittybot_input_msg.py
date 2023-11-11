from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

updater = Updater(token='6343280383:AAFNKMEitLvnscYQkiO_aSHwyLlGEt2mnUo')


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Привет, я KittyBot!')


def wake_up(update, context):
    # В ответ на команду /start 
    # будет отправлено сообщение 'Спасибо, что включили меня'
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, 
                             text='Спасибо, что включили меня')


# Регистрируется обработчик CommandHandler;
# он будет отфильтровывать только сообщения с содержимым '/start'
# и передавать их в функцию wake_up()
updater.dispatcher.add_handler(CommandHandler('start', wake_up))

updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
updater.start_polling()
updater.idle()
