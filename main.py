import telebot

API_TOKEN = '5379884147:AAEQyzq5lLZZhkURDET0IzYN5G-VOP6d_wI'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    user_info = f'Hi, <u>{message.from_user.username}</u>'
    print(message)
    bot.send_message(message.chat.id, user_info, parse_mode='html')


bot.polling(none_stop=True)
