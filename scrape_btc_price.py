import requests, json, os, time

URL = "https://api.coindesk.com/v1/bpi/historical/close.json?for=yesterday"

resp = requests.get(URL, timeout=10)
resp.raise_for_status()
data = resp.json()["bpi"]

FILE = "btc_price.json"
history = []

if os.path.exists(FILE):
    history = json.load(open(FILE))

for date, price in data.items():
    if not any(d["date"] == date for d in history):
        history.append({"date": date, "price": price})

json.dump(history, open(FILE, "w"), indent=2)
