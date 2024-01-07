import telebot
import wikipedia

bot = telebot.TeleBot("5754196545:AAH-iJtTHHFhdq5BnVqKhVPSzbx_H9zVa5o")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "salom men wiki botman menga sorov tashang va men sizga uni topib beraman")

@bot.message_handler(func=lambda message: True)
def search(message):
    wikipedia.set_lang('uzb') # Установка языка
    query = message.text
    results = wikipedia.search(query)
    if not results:
        bot.send_message(message.chat.id, 'hech nima topilmadi((')

    page = wikipedia.page(results[0])
    bot.send_message(message.chat.id, page.url)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text
    chat_id = message.chat.id
bot.polling()