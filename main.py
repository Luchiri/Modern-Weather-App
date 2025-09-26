import os
import requests
import customtkinter as ctk
from datetime import datetime
from PIL import Image

API_KEY = "b9da68923deb60879e0982d659f1f98d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# ---- ROOT WINDOW ----
app = ctk.CTk()
app.title("🌤️ Modern Weather App")
app.geometry("800x700")

# ---- TOP FRAME: SEARCH BAR ----
top_frame = ctk.CTkFrame(app, corner_radius=0, fg_color="#e0f7fa")
top_frame.pack(side="top", fill="x", padx=20, pady=20)

city_entry = ctk.CTkEntry(top_frame, width=400, height=35, placeholder_text="Enter City")
city_entry.pack(side="left", padx=(0,10))

search_btn = ctk.CTkButton(top_frame, text="🔍 Get Weather")
search_btn.pack(side="left")

# ---- CENTER FRAME: WEATHER RESULT ----
center_frame = ctk.CTkFrame(app, corner_radius=25, fg_color="#ffffff")
center_frame.pack(fill="both", expand=True, padx=20, pady=20)
center_frame.pack_propagate(False)

# ---- ICON LOADER ----
def load_icon(path, size=(40,40)):
    if os.path.exists(path):
        return ctk.CTkImage(light_image=Image.open(path), size=size)
    return None

icons = {
    "temp": load_icon("icons/temperature.png"),
    "feels": load_icon("icons/feels_like.png"),
    "description": load_icon("icons/weather_condition.png"),
    "humidity": load_icon("icons/humidity.png"),
    "wind": load_icon("icons/wind.png"),
    "pressure": load_icon("icons/pressure.png"),
    "visibility": load_icon("icons/visibility.png"),
    "sunrise": load_icon("icons/sunrise.png"),
    "sunset": load_icon("icons/sunset.png"),
    "rain": load_icon("icons/rain.png"),
    "clouds": load_icon("icons/cloud.png"),
    "sun": load_icon("icons/sun.png"),
}

# ---- CREATE LABELS DYNAMICALLY ----
result_labels = {}
info_order = ["temp","feels","description","humidity","wind","pressure","visibility","sunrise","sunset","rain","clouds","sun"]

def create_label_row(frame, icon, text, row):
    if icons[icon]:
        lbl_icon = ctk.CTkLabel(frame, image=icons[icon], text="")
        lbl_icon.grid(row=row, column=0, padx=10, pady=6)
    lbl_text = ctk.CTkLabel(frame, text=text, font=("Arial", 14), anchor="w", justify="left")
    lbl_text.grid(row=row, column=1, sticky="w")
    return lbl_text

for i, key in enumerate(info_order):
    result_labels[key] = create_label_row(center_frame, key, "", i)

# ---- FETCH WEATHER FUNCTION ----
def get_weather():
    city = city_entry.get()
    if city == "":
        return

    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        for lbl in result_labels.values():
            lbl.configure(text="❌ City not found")
        return

    data = response
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"].capitalize()
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    pressure = data["main"]["pressure"]
    visibility = data.get("visibility", 0)/1000
    clouds = data["clouds"]["all"]
    sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M:%S")
    sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M:%S")
    rain = data.get("rain", {}).get("1h", 0)
    sun_status = "☀️ Clear" if clouds < 30 else "⛅ Partly Cloudy" if clouds < 70 else "☁️ Cloudy"

    # Update labels
    result_labels["temp"].configure(text=f"🌡️ Temperature: {temp}°C")
    result_labels["feels"].configure(text=f"🤔 Feels Like: {feels_like}°C")
    result_labels["description"].configure(text=f"🌥️ Condition: {description}")
    result_labels["humidity"].configure(text=f"💧 Humidity: {humidity}%")
    result_labels["wind"].configure(text=f"🌬️ Wind Speed: {wind} m/s")
    result_labels["pressure"].configure(text=f"📊 Pressure: {pressure} hPa")
    result_labels["visibility"].configure(text=f"👁️ Visibility: {visibility} km")
    result_labels["sunrise"].configure(text=f"🌅 Sunrise: {sunrise}")
    result_labels["sunset"].configure(text=f"🌇 Sunset: {sunset}")
    result_labels["rain"].configure(text=f"🌧️ Rain: {rain} mm")
    result_labels["clouds"].configure(text=f"☁️ Cloudiness: {clouds}%")
    result_labels["sun"].configure(text=f"{sun_status}")

search_btn.configure(command=get_weather)
app.mainloop()
