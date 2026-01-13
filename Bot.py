import g4f.Provider
import g4f.Provider.Chatgpt4Online
import telebot
from telebot import types 
import requests
from bs4 import BeautifulSoup as bs
import time
import json
import g4f
import asyncio
import test,test2,test3,test4,test5,test6,test7,test8
from telegram import Update 
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
bot = telebot.TeleBot('ВАШ_ТОКЕН_БОТА', skip_pending=True)
id_channel = "@SuperFastNewsBot"
_providers = [
    
]
with open('data/news_dict.json', 'r', encoding='utf-8') as f:
    news_data = json.load(f)
with open('data/world_news_dict.json', 'r', encoding='utf-8') as f:
    news_data2 = json.load(f)
with open('data/BBC_news_dict.json', 'r', encoding='utf-8') as f:
    news_data3 = json.load(f)
waiting_for_response = False 
async def generate_response(message_text: str):
    try:
        messages = [
            {"role": "content", "content": "Ты чат-бот который отвечает на вопросы пользователей, отвечай на русском. Указывай источники. Не добовляй в сообщения звездочки и дургие подобные знаки для обозночения переменных. Давай ёмкие, но информативные по воему содержанию ответы"},
            {"role": "content", "content": news_data},
            {"role": "content", "content": news_data2},
            {"role": "content", "content": message_text}
        ]
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=messages,
            provider=_providers[0] 
        )
        return response
    except Exception as e:
        print("OpenAI GPT Error:", e)
        return None
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Новости")
    btn2 = types.KeyboardButton("Помощь")
    btn3 = types.KeyboardButton("Чат-Бот")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Добро Пожаловать!",reply_markup=markup)
def commands(message):
    back_post_id = 0
    while True:
        post_text = Since.Since_News2,Since.Since_News,Space.Space_News,Space.Rambler_Space_News,World.World_News,World.BBC_World_News,Kazakstan.Kz_News,Kazakstan.Kz_News_Sputnik(back_post_id)
        back_post_id = post_text[1]
        if post_text[0] != None:
            bot.send_message(id_channel, message)
            time.sleep(1800)
@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Новости":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("Мировые Новости")
        btn4 = types.KeyboardButton("Новости Казахстана")
        btn5 = types.KeyboardButton("Космические Новости")
        btn6 = types.KeyboardButton("Новости Науки")
        back1 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn3, btn4, btn5, btn6, back1)
        bot.send_message(message.chat.id, text="Выберите, что вы сегодня хотите узнать.", reply_markup=markup)
    elif message.text == "Помощь":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Что ты?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    elif message.text == "Чат-Бот":
        global waiting_for_response
        waiting_for_response = True
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Чат-бот активирован. Напиши мне что-нибудь, и я отвечу!", reply_markup=markup)  
    elif waiting_for_response and message.text != "Вернуться в главное меню":
        user_message = message
        message_list = [user_message]
        ai_conversation(message_list[-1])

    #Мировые новости
    elif(message.text == "Мировые Новости"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Lenta.ru")
        btn2 = types.KeyboardButton("BBC News")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выберите источник", reply_markup=markup)  
    elif(message.text == "Lenta.ru"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Последняя новость из Lenta.ru")
        btn2 = types.KeyboardButton("Последние 5 новостей из Lenta.ru")
        btn3 = types.KeyboardButton("Все последние новости из Lenta.ru")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите сколько новостей вы хотите видеть", reply_markup=markup)   
    elif(message.text == "Последняя новость из Lenta.ru"):
        test2.main()
        news_messages = World.World_News(message, world_num = 1)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Последние 5 новостей из Lenta.ru"):
        test2.main()
        news_messages = World.World_News(message, world_num = 2)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Все последние новости из Lenta.ru"):
        test2.main()
        news_messages = World.World_News(message, world_num = 3)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Lenta.ru"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Последняя новость из Lenta.ru")
        btn2 = types.KeyboardButton("Последние 5 новостей из Lenta.ru")
        btn3 = types.KeyboardButton("Все последние новости из Lenta.ru")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите сколько новостей вы хотите видеть", reply_markup=markup)   
    elif(message.text == "BBC News"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Последняя новость из BBC News")
        btn2 = types.KeyboardButton("Последние 5 новостей из BBC News")
        btn3 = types.KeyboardButton("Все последние новости из BBC News")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите сколько новостей вы хотите видеть", reply_markup=markup)   
    elif(message.text == "Последняя новость из BBC News"):
        test6.main()
        news_messages = World.BBC_World_News(message, bbc_world_num = 1)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Последние 5 новостей из BBC News"):
        test6.main()
        news_messages = World.BBC_World_News(message, bbc_world_num = 2)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Все последние новости из BBC News"):
        test6.main()
        news_messages = World.BBC_World_News(message, bbc_world_num = 3)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    #Казахстанские Новости
    elif(message.text == "Новости Казахстана"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Tengri News")
        btn2 = types.KeyboardButton("Sputnik KZ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выберите источник", reply_markup=markup)   
    elif(message.text == "Tengri News"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Последняя новость из Tengri")
        btn2 = types.KeyboardButton("Последние 5 новостей из Tengri")
        btn3 = types.KeyboardButton("Все последние новости из Tengri")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите сколько новостей вы хотите видеть", reply_markup=markup)   
    elif(message.text == "Sputnik KZ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Последняя новость из Sputnik")
        btn2 = types.KeyboardButton("Последние 5 новостей из Sputnik")
        btn3 = types.KeyboardButton("Все последние новости из Sputnik")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите сколько новостей вы хотите видеть", reply_markup=markup)   
    elif(message.text == "Последняя новость из Tengri"):
        test.main()
        news_messages = Kazakstan.Kz_News(message, num = 1)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Последние 5 новостей из Tengri"):
        test.main()
        news_messages = Kazakstan.Kz_News(message, num = 2)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Все последние новости из Tengri"):
        test.main()
        news_messages = Kazakstan.Kz_News(message, num = 3)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Последняя новость из Sputnik"):
        test5.main()
        news_messages = Kazakstan.Kz_News_Sputnik(message, sputnik_num = 1)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Последние 5 новостей из Sputnik"):
        test5.main()
        news_messages = Kazakstan.Kz_News_Sputnik(message, sputnik_num = 2)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Все последние новости из Sputnik"):
        test5.main()
        news_messages = Kazakstan.Kz_News_Sputnik(message, sputnik_num = 3)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    #Космо новости
    elif message.text == "Космические Новости":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Tengri News Space")
        btn2 = types.KeyboardButton("Rambler News")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выберите источник", reply_markup=markup)
    elif(message.text == "Tengri News Space"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Последняя новость из Tengri Space")
        btn2 = types.KeyboardButton("Последние 5 новостей из Tengri Space")
        btn3 = types.KeyboardButton("Все последние новости из Tengri Space")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите сколько новостей вы хотите видеть", reply_markup=markup)   
    elif(message.text == "Последняя новость из Tengri Space"):
        test3.main()
        news_messages = Space.Space_News(message, space_num = 1)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Последние 5 новостей из Tengri Space"):
        test3.main()
        news_messages = Space.Space_News(message, space_num = 2)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Все последние новости из Tengri Space"):
        test3.main()
        news_messages = Space.Space_News(message, space_num = 3)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Rambler News"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Последняя новость из Rambler News")
        btn2 = types.KeyboardButton("Последние 5 новостей из Rambler News")
        btn3 = types.KeyboardButton("Все последние новости из Rambler News")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите сколько новостей вы хотите видеть", reply_markup=markup)   
    elif(message.text == "Последняя новость из Rambler News"):
        test7.main()
        news_messages = Space.Rambler_Space_News(message, rambler_space_num = 1)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Последние 5 новостей из Rambler News"):
        test7.main()
        news_messages = Space.Rambler_Space_News(message, rambler_space_num = 2)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Все последние новости из Rambler News"):
        test7.main()
        news_messages = Space.Rambler_Space_News(message, rambler_space_num = 3)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    #Новости науки
    elif message.text == "Новости Науки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Playground")
        btn2 = types.KeyboardButton("New-science")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back) 
        bot.send_message(message.chat.id, text="Выберите источник", reply_markup=markup) 
    elif(message.text == "Playground"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Последняя новость из Playground")
        btn2 = types.KeyboardButton("Последние 5 новостей из Playground")
        btn3 = types.KeyboardButton("Все последние новости из Playground")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите сколько новостей вы хотите видеть", reply_markup=markup) 
    elif(message.text == "New-science"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Последняя новость из New-science")
        btn2 = types.KeyboardButton("Последние 5 новостей из New-science")
        btn3 = types.KeyboardButton("Все последние новости из New-science")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите сколько новостей вы хотите видеть", reply_markup=markup) 
    elif(message.text == "Последняя новость из Playground"):
        test4.main()
        news_messages = Since.Since_News(message, since_num = 1)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Последние 5 новостей из Playground"):
        test4.main()
        news_messages = Since.Since_News(message, since_num = 2)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Все последние новости из Playground"):
        test4.main()
        news_messages = Since.Since_News(message, since_num = 3)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Последняя новость из New-science"):
        test8.main()
        news_messages = Since.Since_News2(message, second_since_num = 1)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Последние 5 новостей из New-science"):
        test8.main()
        news_messages = Since.Since_News2(message, second_since_num = 2)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    elif(message.text == "Все последние новости из New-science"):
        test8.main()
        news_messages = Since.Since_News2(message, second_since_num = 3)
        for news_message in news_messages:
            bot.send_message(message.chat.id, news_message)
    #Помощь
    elif(message.text == "Что ты?"):
        bot.send_message(message.chat.id, "Я чат бот для предостовления информации")
    elif message.text == "Что ты можешь?":
        bot.send_message(message.chat.id,text="Расказать тебе о том что происходит в мире")
    elif (message.text == "Вернуться в главное меню"):
        controler = True
        waiting_for_response = False
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Новости")
        button2 = types.KeyboardButton("Помощь")
        button3 = types.KeyboardButton("Чат-Бот")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)  
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован")
#Функия обработчик чат Бота.
def ai_conversation(message):
    user_message = message.text
    message_list = [user_message]
    print(message_list)
    # Generate response using OpenAI's GPT model
    response = asyncio.run(generate_response(message_list[-1]))
    # Send response to user
    bot.send_message(message.chat.id, text=response)
#Объявление классов обработки сообщений
class Kazakstan:
    def Kz_News(message, num):
        with open('data/news_dict.json', 'r', encoding='utf-8') as f:
            news_data = json.load(f)
        if (num == 1):
            last_news = list(news_data.values())[:1]
        elif (num == 2):
            last_news = list(news_data.values())[:5]
        elif (num == 3):
            last_news = list(news_data.values())[:-1]
        # Формируем список сообщений новостей
        news_messages = []
        for news_item in last_news:
            news_message = f"{news_item['Заголовок']}\n\n{news_item['Текст']}\n\n{news_item['Ссылка']}"
            news_messages.append(news_message)
        return news_messages
    def Kz_News_Sputnik(message, sputnik_num):
        with open('data/sputnik_news_dict.json', 'r', encoding='utf-8') as f:
            news_data = json.load(f)
        if (sputnik_num == 1):
            last_news = list(news_data.values())[:1]
        elif (sputnik_num == 2):
            last_news = list(news_data.values())[:5]
        elif (sputnik_num == 3):
            last_news = list(news_data.values())[:-1]
        # Формируем список сообщений новостей
        news_messages = []
        for news_item in last_news:
            news_message = f"{news_item['Заголовок']}\n\n{news_item['Ссылка']}"
            news_messages.append(news_message)
        return news_messages
class World:
    def World_News(message, world_num):
        with open('data/world_news_dict.json', 'r', encoding='utf-8') as f:
            news_data = json.load(f)
        if (world_num == 1):
            last_news = list(news_data.values())[:1]
        elif (world_num == 2):
            last_news = list(news_data.values())[:5]
        elif (world_num == 3):
            last_news = list(news_data.values())[:-1]
        # Формируем список сообщений новостей
        news_messages = []
        for news_item in last_news:
            news_message = f"{news_item['Заголовок']}\n\n{news_item['Ссылка']}"
            news_messages.append(news_message)
        return news_messages
    def BBC_World_News(message, bbc_world_num):
        with open('data/BBC_news_dict.json', 'r', encoding='utf-8') as f:
            news_data = json.load(f)
        if (bbc_world_num == 1):
            last_news = list(news_data.values())[:1]
        elif (bbc_world_num == 2):
            last_news = list(news_data.values())[:5]
        elif (bbc_world_num == 3):
            last_news = list(news_data.values())[:-1]
        # Формируем список сообщений новостей
        news_messages = []
        for news_item in last_news:
            news_message = f"{news_item['Заголовок']}\n\n{news_item['Ссылка']}"
            news_messages.append(news_message)
        return news_messages
class Space:
    def Space_News(message, space_num):
        with open('data/space_news_dict.json', 'r', encoding='utf-8') as f:
            news_data = json.load(f)
        if (space_num == 1):
            last_news = list(news_data.values())[:1]
        elif (space_num == 2):
            last_news = list(news_data.values())[:5]
        elif (space_num == 3):
            last_news = list(news_data.values())[:-1]
        # Формируем список сообщений новостей
        news_messages = []
        for news_item in last_news:
            news_message = f"{news_item['Заголовок']}\n\n{news_item['Текст']}\n\n{news_item['Ссылка']}"
            news_messages.append(news_message)
        return news_messages
    def Rambler_Space_News(message, rambler_space_num):
        with open('data/Rambler_space__news_dict.json', 'r', encoding='utf-8') as f:
            news_data = json.load(f)
        if (rambler_space_num == 1):
            last_news = list(news_data.values())[:1]
        elif (rambler_space_num == 2):
            last_news = list(news_data.values())[:5]
        elif (rambler_space_num == 3):
            last_news = list(news_data.values())[:-1]
        # Формируем список сообщений новостей
        news_messages = []
        for news_item in last_news:
            news_message = f"{news_item['Заголовок']}\n\n{news_item['Ссылка']}"
            news_messages.append(news_message)
        return news_messages
class Since:
    def Since_News(messeage, since_num):
        with open('data/since_news_dict.json', 'r', encoding='utf-8') as f:
            news_data = json.load(f)
        if (since_num == 1):
            last_news = list(news_data.values())[:1]
        elif (since_num == 2):
            last_news = list(news_data.values())[:5]
        elif (since_num == 3):
            last_news = list(news_data.values())[:-1]
        # Формируем список сообщений новостей
        news_messages = []
        for news_item in last_news:
            news_message = f"{news_item['Заголовок']}\n\n{news_item['Ссылка']}"
            news_messages.append(news_message)
        return news_messages
    def Since_News2(message, second_since_num):
        with open('data/second_since_news_dict.json', 'r', encoding='utf-8') as f:
            news_data = json.load(f)
        if (second_since_num == 1):
            last_news = list(news_data.values())[:1]
        elif (second_since_num == 2):
            last_news = list(news_data.values())[:5]
        elif (second_since_num == 3):
            last_news = list(news_data.values())[:-1]
        # Формируем список сообщений новостей
        news_messages = []
        for news_item in last_news:
            news_message = f"{news_item['Заголовок']}\n\n{news_item['Ссылка']}"
            news_messages.append(news_message)
        return news_messages
# Пример использования asyncio.run():
if __name__ == '__main__': 
    bot.polling(none_stop=True)