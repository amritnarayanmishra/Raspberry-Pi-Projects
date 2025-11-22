import Adafruit_DHT
import requests
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 17
THINGSPEAK_API_KEY = "YOUR_API_KEY"

url = f"https://api.thingspeak.com/update?api_key={THINGSPEAK_API_KEY}"

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            data = f"{url}&field1={temperature}&field2={humidity}"
            response = requests.get(data)
            print(f"Temp={temperature}C Humidity={humidity}% Sent. Response={response.status_code}")
        else:
            print("Failed to get reading.")
        time.sleep(15)
except KeyboardInterrupt:
    print("Program stopped")
