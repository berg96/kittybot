from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from telegram import ReplyKeyboardMarkup

updater = Updater(token='6343280383:AAFNKMEitLvnscYQkiO_aSHwyLlGEt2mnUo')


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,text='Привет, я KittyBot!')


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    # Вот она, наша кнопка.
    # Обратите внимание: в класс передаётся список, вложенный в список,
    # даже если кнопка всего одна.
    # Каждый вложенный список определяет
    # новый ряд кнопок в интерфейсе бота.
    # Здесь описаны две кнопки в первом ряду и одна - во втором.
    buttons = ReplyKeyboardMarkup([
        ['Который час?', 'Определи мой ip'],
        ['/random_digit']
    ])
    context.bot.send_message(
        chat_id=chat.id,
        text='Спасибо, что вы включили меня, {}!'.format(name),
        # Добавим кнопку в содержимое отправляемого сообщения
        reply_markup=buttons
        )


updater.dispatcher.add_handler(CommandHandler('start', wake_up))

updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

updater.start_polling()
updater.idle()
