import telebot
from time import sleep
import requests

bot = telebot.TeleBot('')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True) 
keyboard1.row('Show portfolio', 'Show contacts', 'How do you work?')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'We start', reply_markup=keyboard1)

@bot.message_handler(content_types = ['text'])
def main(message):
    if message.text == 'Show portfolio':
        bot.send_message(message.chat.id, '"It was necessary to collect the data (title and unicode of each free icon) from dynamic web page - catalog of web site FontAwesome and to output it into CSV file."\n\nUpWork: https://www.upwork.com/freelancers/~018dd2b1f222cf42f5?p=1357018100471742464\n\nGitHub: https://github.com/santaCoding/Parsing/tree/master/dynamic')
        bot.send_message(message.chat.id, '"Task was to collect static data about each university of my city and to display it in tablesheet view from website, but just with one label of phone (there are many labels)."\n\nUpWork: https://www.upwork.com/freelancers/~018dd2b1f222cf42f5?p=1357070523058319360\n\nGitHub: https://github.com/santaCoding/Parsing/tree/master/static')
        bot.send_message(message.chat.id, '"I was given the list of 5 instagram profiles, where I needed to collect posting date, caption, link and comments count of each post. Then to output it in Excel file for ceperate file for account."\n\nUpWork: https://www.upwork.com/freelancers/~018dd2b1f222cf42f5?p=1357709104770588672\n\nGitHub: https://github.com/santaCoding/Parsing/tree/master/instagram')
        bot.send_message(message.chat.id, '"Bot scraping data from my private Telegram channel was screated with telethone module. It collects all messages + all data about each message and all available info about each channel member. All data outputted into JSON format which can easile be imported into future batabase."\n\nUpWork: https://www.upwork.com/freelancers/~018dd2b1f222cf42f5?p=1359502049102405632\n\nGitHub: https://github.com/santaCoding/Bots/tree/master/telegram_parser')
    elif message.text == 'Show contacts':
        bot.send_message(message.chat.id, 'Telegram: @santaCoding\nInstagram: @santacoding\nGitHub: https://github.com/santaCoding\nEmail: landreax100@gmail.com')
    elif message.text == 'How do you work?':
        bot.send_message(message.chat.id, 'I work on telebot basis (module in Python) which allows to create from simple to hard functionality Telegram Bot. I\'m just an example of portfolio and bot, that can be developed for you. I will have brothers from Discord and Facebook soon.\nI will be more then happy for Alex if you start working with him.❤️')
    else:
        bot.send_message(message.chat.id, 'Repeat please?')


bot.polling()