import requests

CHANNEL_ID = "2894769"
FIELD = "1"

url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/{FIELD}.json?results=5"

try:
    response = requests.get(url)
    data = response.json()

    if isinstance(data, dict) and "feeds" in data and len(data["feeds"]) > 0:
        print(f"\n📊 Last Entries for Field {FIELD}:")
        for feed in data["feeds"]:
            print(f"{feed['created_at']} → {feed[f'field{FIELD}']} units")
    else:
        print("⚠️ No data found for this field.")
except Exception as e:
    print("❌ Error fetching data:", e)

