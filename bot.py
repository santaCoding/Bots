import telebot

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет привет')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока пока')

bot.polling()