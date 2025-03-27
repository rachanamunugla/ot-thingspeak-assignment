import requests
import random
import time

WRITE_API_KEY = "NN2DLD8PXV8KEA2V"
url = "https://api.thingspeak.com/update"

while True:
    temp = round(random.uniform(10, 40), 2)
    humidity = round(random.uniform(30, 80), 2)
    co2 = round(random.uniform(400, 1500), 2)

    payload = {
        "api_key": WRITE_API_KEY,
        "field1": temp,
        "field2": humidity,
        "field3": co2
    }

    response = requests.post(url, params=payload)

    print(f"✅ Sent → Temp={temp}C, Hum={humidity}%, CO2={co2}ppm | Response: {response.text}")
    time.sleep(15)

