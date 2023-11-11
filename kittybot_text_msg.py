from telegram import Bot

# Здесь укажите токен,
# который вы получили от @Botfather при создании бот-аккаунта
bot = Bot(token='6343280383:AAFNKMEitLvnscYQkiO_aSHwyLlGEt2mnUo')
# Укажите id своего аккаунта в Telegram
chat_id = 415404984
text = 'А это мой бот))'
# Отправка сообщения
bot.send_message(chat_id, text)
