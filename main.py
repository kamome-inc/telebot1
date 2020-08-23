import telebot
bot_token = "1171530088:AAEY9EXzFxBXZm4_Bymzm18hYpm8KZjnpx8"
bot = telebot.TeleBot(bot_token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.from_user.first_name, message.from_user.last_name, message.from_user.id, '  ', message.text)
    if message.text == "Привет":
        ans = "Привет! Купи слона!"
        bot.send_message(message.from_user.id, ans)
    elif message.text == "/start":
        ans = "Представьтесь пожалуйста"
        bot.send_message(message.from_user.id, ans)
    else:
        ans = "Все говорят \'" + message.text + "\', а ты купи слона!"
        bot.send_message(message.from_user.id, ans)
    print("bot to:", message.from_user.first_name, message.from_user.last_name, message.from_user.id, '  ', ans)

bot.polling(none_stop=True, interval=0)

