import telebot
from telebot import types
import config

bot = telebot.TeleBot("6504161039:AAHAJBKxyMkxeG5fRU5V3HssjDsOqPkk5nk")

@bot.message_handler(commands=['start'])
def phone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text='Raqamni yubormoq', request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, 'Davom etish uchun raqamni kiriting', reply_markup=keyboard)

@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        print(message.contact)
        print(type(message.contact))
        print('Name: ' + str(message.contact.first_name))
        text = 'Пользователь: ' + message.contact.first_name + ': телефон: ' + message.contact.phone_number
        bot.send_message('-4008371539', text)

print('Bot ishlamoqda')
bot.polling()