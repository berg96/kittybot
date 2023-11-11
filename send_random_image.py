import requests

from telegram import Bot

bot = Bot(token='6343280383:AAFNKMEitLvnscYQkiO_aSHwyLlGEt2mnUo')
# Адрес API сохраним в константе
URL = 'https://api.thecatapi.com/v1/images/search'
# Сделаем GET-запрос к API
# метод json() преобразует полученный ответ JSON в тип данных, понятный Python
response = requests.get(URL).json()
# Рассмотрим структуру и содержимое переменной response
print(response)

# Посмотрим, какого типа переменная response
print(type(response))

# response - это список. А какой длины?
print(len(response))

# Посмотрим, какого типа первый элемент
print(type(response[0]))

random_cat_url = response[0].get('url')

chat_id = 415404984
text = 'Вам телеграмма!'
# Отправка сообщения
bot.send_message(chat_id, text)
# Отправка изображения
bot.send_photo(chat_id, random_cat_url)
