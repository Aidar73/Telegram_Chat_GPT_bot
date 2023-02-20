import os
import openai
import telebot
from dotenv import load_dotenv
from telebot import types

# Загрузка токена
load_dotenv()
token = os.getenv('TELEGRAM_TOKEN')
key = os.getenv('key_openai')
# Подключение бота
bot = telebot.TeleBot(token)
# OpenAI key
openai.api_key = key


# Функция для обработки ввода сообщений
@bot.message_handler(content_types=['text'])
def func(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f'{message.text}',
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    bot.send_message(message.chat.id, response.choices[0].text)
    print(message.from_user.username, message.from_user.first_name)
    print(message.text)
    print(response.choices[0].text)
    print('_______________________________________________')


# Запускаем бота
if __name__ == '__main__':
    bot.polling(none_stop=True)









