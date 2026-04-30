import requests
import time

TOKEN = "8791981573:AAGgxK1iJCiqVPRdf4Xo1__7pbUUTg9ZmOc"
CHAT_ID = "875446465"

def send_msg(text):
    url = f"https://api.telegram.org/bot{8791981573:AAGgxK1iJCiqVPRdf4Xo1__7pbUUTg9ZmOc}/sendMessage"
    requests.get(url, params={"chat_id": CHAT_ID, "text": text})

def coinbase_price():
    data = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot").json()
    return float(data["data"]["amount"])

def kraken_price():
    url = "https://api.kraken.com/0/public/Ticker?pair=XBTUSD"
    data = requests.get(url).json()
    return float(data["result"]["XXBTZUSD"]["c"][0])

while True:
    try:
        c1 = coinbase_price()
        c2 = kraken_price()

        diff = c1 - c2
        percent = (diff / c2) * 100

        print("Coinbase:", c1)
        print("Kraken:", c2)
        print(f"Diff: {diff} ({percent:.4f}%)")

        # 🔥 현실 필터
        if abs(percent) > 0.5:
            msg = f"""
🚨 REAL ARBITRAGE

Coinbase: {c1}
Kraken: {c2}

Diff: {diff}
Percent: {percent:.4f}%
"""
            send_msg(msg)

    except Exception as e:
        print("error:", e)

    time.sleep(10)
