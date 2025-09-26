import os
import requests

# Create icons directory if it doesn't exist
os.makedirs("icons", exist_ok=True)

# Dictionary mapping weather conditions to icon URLs
icons = {
    "sun": "https://cdn-icons-png.flaticon.com/512/869/869869.png",
    "cloud": "https://cdn-icons-png.flaticon.com/512/1163/1163624.png",
    "rain": "https://cdn-icons-png.flaticon.com/512/1163/1163657.png",
    "storm": "https://cdn-icons-png.flaticon.com/512/1146/1146860.png",
    "snow": "https://cdn-icons-png.flaticon.com/512/642/642102.png",
    "mist": "https://cdn-icons-png.flaticon.com/512/4005/4005901.png",
    "temperature": "https://cdn-icons-png.flaticon.com/512/1116/1116459.png",
    "feels_like": "https://cdn-icons-png.flaticon.com/512/742/742751.png",
    "humidity": "https://cdn-icons-png.flaticon.com/512/728/728093.png",
    "wind": "https://cdn-icons-png.flaticon.com/512/61/61088.png",
    "pressure": "https://cdn-icons-png.flaticon.com/512/3039/3039431.png",
    "visibility": "https://cdn-icons-png.flaticon.com/512/565/565547.png",
    "sunrise": "https://cdn-icons-png.flaticon.com/512/169/169367.png",
    "sunset": "https://cdn-icons-png.flaticon.com/512/169/169354.png",
    "weather_condition": "https://cdn-icons-png.flaticon.com/512/1163/1163630.png"
}

# Download each icon
for name, url in icons.items():
    filepath = f"icons/{name}.png"
    if not os.path.exists(filepath):
        print(f"⬇️ Downloading {name} icon...")
        response = requests.get(url)
        if response.status_code == 200:
            with open(filepath, "wb") as f:
                f.write(response.content)
            print(f"✅ {name}.png saved!")
        else:
            print(f"❌ Failed to download {name} icon.")
    else:
        print(f"✔️ {name}.png already exists.")
