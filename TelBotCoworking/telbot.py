import telebot
from telebot import types

token = "1038002086:AAH7PVaLhrtwjhyf7RmB-VtbREfDLWOzwaw"

bot = telebot.TeleBot(token)



@bot.message_handler(commands=["geo"])
def geo(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и передай мне свое местоположение", reply_markup=keyboard)

@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        print(message.location)
        print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
        bot.send_location(message.chat.id, 55.7527698, 37.6213976)

bot.polling()