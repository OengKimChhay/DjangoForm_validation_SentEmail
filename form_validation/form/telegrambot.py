from django.conf import settings
import telebot
import requests
from telebot import types

chat_id = -1001573381440
token = '1978973317:AAGlbP7vSXn_n0XWQ5khT3nFUbqJJqY7jcM'
parse_mode = 'HTML'
bot = telebot.TeleBot(token, parse_mode=parse_mode)


# sendMessage
@bot.message_handler(content_types=['text'])
def sent_message(text):
    bot.send_message(chat_id, text)


# send photo
@bot.message_handler(content_types=['photo'])
def sent_photo(photo):
    bot.send_photo(chat_id, photo)
    bot.send_photo(chat_id, "FILEID")


# sendLocation
@bot.message_handler(content_types=['location'])
def send_location(lat, lon):
    bot.send_location(chat_id, lat, lon)


# sendDocument
def send_document(doc):
    bot.send_document(chat_id, doc)
    bot.send_document(chat_id, "FILEID")


# sendChatAction
@bot.message_handler(content_types=['location'])
def send_chat_action():
    print(bot.send_chat_action(chat_id, 'find_location'))


bot.polling()
