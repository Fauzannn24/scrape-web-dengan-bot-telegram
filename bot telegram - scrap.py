import telebot
import requests
from bs4 import BeautifulSoup

api = '6594995717:AAGiMrwKQXGxlo2KVPKq1ocs3RsQx6VhwPs'
data = telebot.TeleBot(api)
@data.message_handler(commands=['start'])
def balas_start(message):
    data.reply_to(message,'Selamat Datang di Bot AAF')
@data.message_handler(commands=['scrap'])
def scrap(message):
    page = requests.get("https://plniconplus.co.id/e-proc/")
    after_bs = BeautifulSoup(page.content, 'html.parser')
    find_data = after_bs.find_all('div',class_="post__detail")
    output = 'Assalamualaikum ww, berikut update E-Proc'
    b = '--------------------------------------------------'
    for x in find_data:      
        output = output + '\n' + x.text + b
    data.reply_to(message, output)
print('Bot Berjalan')
data.polling()