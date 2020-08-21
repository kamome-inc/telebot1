import telebot
bot_token = "1171530088:AAEY9EXzFxBXZm4_Bymzm18hYpm8KZjnpx8"
bot = telebot.TeleBot(bot_token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Представьтесь пожалуйста")
    print(message.from_user.first_name, message.from_user.last_name, message.from_user.id, '  ', message.text)
    bot.send_message(message.from_user.id, message.text)

bot.polling(none_stop=True, interval=0)

