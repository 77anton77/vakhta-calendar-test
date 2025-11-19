import telebot
from telebot.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "8335146818:AAEyYl0bkVIWZ4m99O-VBx4sMVkpOav38Uk"  # Замени на реальный токен!

bot = telebot.TeleBot(BOT_TOKEN)
# Устанавливаем webhook для Telegram
@app.route('/telegram/' + BOT_TOKEN, methods=['POST'])
def telegram_webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'OK', 200
    return 'Forbidden', 403

# При запуске устанавливаем webhook
if __name__ == "__main__":
    # Удаляем старый webhook
    bot.remove_webhook()
    
    # Устанавливаем новый webhook для Telegram
    telegram_webhook_url = f'https://vakhta-bot.fly.dev/telegram/{BOT_TOKEN}'
    bot.set_webhook(url=telegram_webhook_url)
    
    print("🚀 Тестовый бот запущен на порту 8081!")
    app.run(host='0.0.0.0', port=8081, debug=False)

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
