from telegram import Bot

bot = Bot(token='6343280383:AAFNKMEitLvnscYQkiO_aSHwyLlGEt2mnUo')

URL = 'https://cdn2.thecatapi.com/images/3dl.jpg'

chat_id = 415404984
text = 'Вам телеграмма!'
# Отправка сообщения
bot.send_message(chat_id, text)
# Отправка изображения
bot.send_photo(chat_id, URL)
