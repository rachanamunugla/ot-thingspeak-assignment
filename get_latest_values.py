import requests

CHANNEL_ID = "2894769"  # this line is fine

url = f"https://api.thingspeak.com/channels/2894769/feeds/last.json"

response = requests.get(url)

try:
    data = response.json()

    # If it's an int, it means there's no JSON data yet
    if isinstance(data, dict) and "field1" in data:
        print("📡 Latest Sensor Readings:")
        print(f"Temperature: {data['field1']} °C")
        print(f"Humidity: {data['field2']} %")
        print(f"CO2: {data['field3']} ppm")
        print(f"Timestamp: {data['created_at']}")
    else:
        print("⚠️ No recent sensor data found in ThingSpeak.")
except Exception as e:
    print("❌ Failed to decode response:", e)

