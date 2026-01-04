import requests, json, os

URL = "https://api.alternative.me/fng/?limit=1"

resp = requests.get(URL, timeout=10)
resp.raise_for_status()
new_data = resp.json()["data"][0]

FILE = "fear_greed.json"
history = []

if os.path.exists(FILE):
    try:
        history = json.load(open(FILE))
        if isinstance(history, dict):
            history = [history]
    except:
        history = []

if not history or history[-1]["timestamp"] != new_data["timestamp"]:
    history.append(new_data)

json.dump(history, open(FILE, "w"), indent=2)
