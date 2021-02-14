import telebot
from bs4 import BeautifulSoup
import requests



bot = telebot.TeleBot('1542315191:AAFkEShzjlMbT7TIue-y47o0_uasc11tqR8')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(commands=['title'])
def start_message(message):
    url = 'https://quotes.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')

    for i in range(0, len(quotes)):
        print(quotes[i].text)
        print('--' + authors[i].text)
        tagsforquote = tags[i].find_all('a', class_='tag')
        for tagforquote in tagsforquote:
            print(tagforquote.text)
            print(' ')
            bot.send_message(message.chat.id, tagforquote.text + ' ' + quotes[i].text)

bot.polling()
