from dotenv import load_dotenv
import os 
import telebot

# from main import main


load_dotenv()
token = os.environ.get('TELEGRAM_TOKEN')
# print(token)

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Привет. Я бот. Введите валюту')

@bot.message_handler(content_types=["text"])
def show_valut(message):
	try:
		new_str, valuts = valut(message_text)
		bot.send_message(message.chat.id, 'Ваша валюта' + message.text + str(new_str))

	except TypeError:
		bot.send_message(message.chat_id, "Ошибка")

bot.polling()
