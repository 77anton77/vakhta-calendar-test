import telebot
from telebot.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "8335146818:AAEyYl0bkVIWZ4m99O-VBx4sMVkpOav38Uk"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(
        "📅 Тест календарь", 
        web_app=WebAppInfo(url="https://77anton77.github.io/vakhta-calendar/")
    ))
    
    bot.send_message(
        message.chat.id,
        "🤖 ТЕСТОВЫЙ БОТ\n\n🔥 АВТОДЕПЛОЙ!",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "🚀 ВЕРСИЯ 2")

if __name__ == "__main__":
    print("🚀 Тестовый бот запущен!")
    bot.infinity_polling()
