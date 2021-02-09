import telebot
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Начинаем')

@bot.message_handler(content_types = ['text'])
def main(message):
    if message.text.lower() == 'секрет':
        bot.send_photo(message.chat.id, photo=open('photka.jpg', 'rb'))


bot.polling()