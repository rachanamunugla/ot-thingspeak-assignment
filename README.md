# IoT Sensor System with ThingSpeak Integration

This project simulates an environmental monitoring system using virtual sensors that generate random values for temperature, humidity, and CO2 levels. The data is published to a ThingSpeak channel via HTTP.

---

## 🧪 Project Features

- Simulates real-time sensor readings
- Sends data to ThingSpeak using HTTP POST
- Displays:
  - Latest sensor readings
  - Last 5 hours of field data using ThingSpeak API

---

## 📁 Files

| File Name               | Description                                      |
|------------------------|--------------------------------------------------|
| `final_http_sensor.py` | Sends sensor data (Temp, Humidity, CO2) to ThingSpeak |
| `get_latest_values.py` | Fetches the most recent sensor values from ThingSpeak |
| `get_last_5_hours.py`  | Retrieves the last 5 hours of data for any one sensor |
| `screenshots/`         | Contains output screenshots of system behavior   |

---

## 📡 ThingSpeak Channel Info

- **Channel ID**: `2894769`
- **Fields**:
  - Field 1: Temperature (°C)
  - Field 2: Humidity (%)
  - Field 3: CO2 (ppm)

---

## 📝 How to Run

1. Install dependencies:
   ```bash
   pip install requests

