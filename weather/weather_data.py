from settings import *
import json
import requests

def get_weather(latitude, longitude, units, period):
    full_url = f"{BASE_URL}&lat={latitude}&lon={longitude}&appid={API_KEY}&units={units}"
    response = requests.get(full_url)

    current_data = {}
    forcast_data = {}

    if response.status_code == 200:
        data = response.json()
        for key, value in data.items():
            if key == "list":
                for index, data_entry in enumerate(value):

                    if index == 0: # Current
                        current_data["temp"] = int(round(data_entry["main"]["temp"], 0))
                        current_data["feels_like"] = int(round(data_entry["main"]["feels_like"], 0))
                        current_data["weather"] = data_entry["weather"][0]["main"]
                        today = data_entry["dt_txt"].split(" ")[0]
                    else:
                        if data_entry["dt_txt"].split(" ")[0] != today:
                            start_index = index + 4
                            break
        
        for index in range(start_index, len(data["list"]), 8):
            forcast_entry = data["list"][index]
            # Key -> date
            date = forcast_entry["dt_txt"].split(" ")[0]
            # Value -> {'temp', 'feels_like', 'weather'}
            forcast_data[date] = {
                "temp": int(round(forcast_entry["main"]["temp"])),
                "feels_like": int(round(forcast_entry["main"]["feels_like"])),
                "weather": data_entry["weather"][0]["main"]
            }
    else:
        print(response.status_code)

    if period == "today":
        return current_data
    else: 
        return forcast_data