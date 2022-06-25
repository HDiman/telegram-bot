import requests
import telebot
from auth_data import token, key
import time


def get_data():
    s_city = "Moscow,RU"
    city_id = 524901
    appid = key
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        weather = data['main']['temp']
        cond = data['weather'][0]['description']
        min_t = data['main']['temp_min']
        max_t = data['main']['temp_max']

        print("conditions:", data['weather'][0]['description'])
        print("temp:", data['main']['temp'])
        print("temp_min:", data['main']['temp_min'])
        print("temp_max:", data['main']['temp_max'])
        return [weather, cond, min_t, max_t]
    except Exception as e:
        print("Exception (weather):", e)
        pass

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Have a good day!")

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == 't':
            try:
                bot.send_message(message.chat.id, f"temp: {get_data()[0]}\n"
                                                  f"condition: {get_data()[1]}\n"
                                                  f"temp_max: {get_data()[3]}\n"
                                                  f"temp_min: {get_data()[2]}\n")
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Disconnection!!!")
        else:
            bot.send_message(message.chat.id, "Wrong command")

    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)  # или просто print(e) если у вас логгера нет
            time.sleep(15)


if __name__ == "__main__":
    telegram_bot(token)
    # get_data()


