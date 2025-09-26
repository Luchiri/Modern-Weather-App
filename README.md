🌤️ Modern Weather App

A sleek, modern weather application built with Python and CustomTkinter. Fetches live weather data for any city using the OpenWeatherMap API and displays it in a clean, dynamic interface.

Features

Search any city and get real-time weather information.

Displays all major weather details:

Temperature & Feels Like

Condition (description)

Humidity, Wind Speed, Pressure, Visibility

Sunrise & Sunset

Rain, Clouds, Sun status

Modern GUI with rounded frames, icons, and colors.

Weather info appears only after searching, keeping the interface clean.

Screenshots

https://raw.githubusercontent.com/Luchiri/Modern-Weather-App/da68c901df69103b3841c0c9dfe6438e078d3285/weather%20app%20screenshot.png

Installation

Clone the repository:

git clone https://github.com/yourusername/weather-app.git


Navigate into the project folder:

cd weather-app


Create a virtual environment:

python -m venv venv


Activate the virtual environment:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Install dependencies:

pip install -r requirements.txt


Add your OpenWeatherMap API key to a .env file:

API_KEY=your_api_key_here


Run the app:

python main.py

Dependencies

Python 3.10+

CustomTkinter

Requests

Pillow (PIL)

Usage

Open the app.

Enter the name of a city.

Click Get Weather.

The weather information will appear dynamically in the app window.
