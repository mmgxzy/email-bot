import schedule
import time
import requests

def test():
    print("d")
    print(time.ctime())

def get_bts_price():
    print("======BTC======")
    url = 'https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    response = requests.get(url=url).json()
    price = response.get('price')

    print(f' стоимость биткоина на текущее время: {time.ctime()}, цена: {price}')

# schedule.every(2).seconds.do(test)
# schedule.every(1).minutes.do(test)
# schedule.every().day.at("15:33").do(test)
# schedule.every().monday.at("15:35").do(test)
# schedule.every().day.at("15:37", 'Europe/Amsterdam').do(test)
# schedule.every().hour.at(":39").do(test)
schedule.every(1).seconds.do(get_bts_price)

while True:
    schedule.run_pending()