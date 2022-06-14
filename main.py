import requests
from datetime import datetime
import telebot
from auth_data import token


def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]["sell"]
    today_day = datetime.now().strftime('%Y-%m-%d %H:%M')
    print(response)
    print(f"{today_day}\n Sell BTC price: {sell_price}\n")

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["Start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello friend! Write the 'price' to find out the sell price of BTC")


if __name__ == "__main__":
    # get_data()
    telegram_bot(token)

