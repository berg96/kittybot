import logging
import os

import requests

from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from dotenv import load_dotenv

load_dotenv()
secret_token = os.getenv('TOKEN')
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
# Взяли переменную TOKEN из пространства переменных окружения
# Шпионы печальны, шпионы ушли с пустыми руками
CAT_URL = 'https://api.thecatapi.com/v1/images/search'
DOG_URL = 'https://api.thedogapi.com/v1/images/search'


def get_new_image(url):
    try:
        response = requests.get(url)
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        if url == DOG_URL:
            new_url = CAT_URL
        else:
            new_url = DOG_URL
        response = requests.get(new_url)

    response = response.json()
    return response[0].get('url')


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image(CAT_URL))


def new_dog(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image(DOG_URL))


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Привет, я KittyBot!')


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    # Вот она, наша кнопка.
    # Обратите внимание: в класс передаётся список, вложенный в список,
    # даже если кнопка всего одна.
    # Каждый вложенный список определяет
    # новый ряд кнопок в интерфейсе бота.
    # Здесь описаны две кнопки в первом ряду и одна - во втором.
    # buttons = ReplyKeyboardMarkup([
    #     ['Который час?', 'Определи мой ip'],
    #     ['/random_digit']
    # ])
    # За счёт параметра resize_keyboard=True сделаем кнопки поменьше
    buttons = ReplyKeyboardMarkup(
        [
            ['/newcat', '/newdog']
        ],
        resize_keyboard=True
    )
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Посмотри, какого котика я тебе нашёл'.format(name),
        reply_markup=buttons
    )
    context.bot.send_photo(chat.id, get_new_image(CAT_URL))


def main():
    updater = Updater(token=secret_token)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))
    updater.dispatcher.add_handler(CommandHandler('newdog', new_dog))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
