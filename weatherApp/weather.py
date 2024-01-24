import tkinter as tk
import requests
import json

API_KEY = "de46fcb2772c80be26891eaa727e7aca"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def get_weather_info():
    city = entry.get()
    weather_data = get_weather(city)
    if weather_data.get("cod") == "404":
        result_label.config(text="City not found!")
    else:
        try:
            temperature = weather_data["main"]["temp"]
            weather_description = weather_data["weather"][0]["description"]
            result_label.config(text=f"The temperature in {city} is {temperature}°C.\nThe weather is {weather_description}.")
        except KeyError as e:
            result_label.config(text="Error: Invalid API response format.")


window = tk.Tk()
window.title("Weather App")
label = tk.Label(window, text="Enter the name of the city:")
label.pack()
entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text="Get Weather", command=get_weather_info)
button.pack()
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()


