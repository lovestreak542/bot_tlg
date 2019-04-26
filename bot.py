import parser
import telebot

bot = telebot.TeleBot("")
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "саня набери /sanya")

@bot.message_handler(commands=['list'])
def send_list(message):
	bot.send_message(message.chat.id, '''
	List of commands:
	/sanya
	''')

@bot.message_handler(commands=['sanya'])
def send_emoji(message):
	bot.send_message(message.chat.id, '''
	Саня хуй соси да
	''')
 
bot.polling( none_stop= True)