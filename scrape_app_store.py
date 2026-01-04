import requests, json, os, time

URL = "https://rss.applemarketingtools.com/api/v2/us/apps/top-free/100/apps.json"
TARGETS = ["Coinbase", "Robinhood"]

today = time.strftime("%Y-%m-%d")
FILE = "app_store_ranks.json"

resp = requests.get(URL, timeout=10)
resp.raise_for_status()
apps = resp.json()["feed"]["results"]

history = []
if os.path.exists(FILE):
    history = json.load(open(FILE))

for name in TARGETS:
    rank = None
    for i, app in enumerate(apps, start=1):
        if name.lower() in app["name"].lower():
            rank = i
            break

    record = {
        "date": today,
        "app": name,
        "platform": "ios",
        "rank": rank
    }

    if not any(
        r["date"] == today and r["app"] == name
        for r in history
    ):
        history.append(record)

json.dump(history, open(FILE, "w"), indent=2)
