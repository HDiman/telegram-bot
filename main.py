import requests
from datetime import datetime

def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]["sell"]
    today_day = datetime.now().strftime('%Y-%m-%d %H:%M')
    print(response)
    print(f"{today_day}\n Sell BTC price: {sell_price}\n")


if __name__ == "__main__":
    get_data()

