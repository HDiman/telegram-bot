import requests
from datetime import datetime
import telebot
from auth_data import token, key
import time


# def get_data():
#     req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
#     response = req.json()
#     sell_price = response["btc_usd"]["sell"]
#     today_day = datetime.now().strftime('%Y-%m-%d %H:%M')
#     print(f"{today_day}\n Sell BTC price: {sell_price}\n")
#     return f"{today_day}\n Sell BTC price: {round(sell_price)}\n"

def get_data():
    s_city = "Petersburg,RU"
    city_id = 0
    appid = "буквенно-цифровой APPID"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        print("city:", cities)
        city_id = data['list'][0]['id']
        print('city_id=', city_id)
    except Exception as e:
        print("Exception (find):", e)
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
                bot.send_message(message.chat.id, get_data())
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Disconnection!!!")
        else:
            bot.send_message(message.chat.id, "Wrong command")

    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)  # или просто print(e) если у вас логгера нет,
            # или import traceback; traceback.print_exc() для печати полной инфы
            time.sleep(15)


if __name__ == "__main__":
    telegram_bot(token)


