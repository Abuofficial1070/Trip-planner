import requests
API_KEY = "8955ec43fccf1fbb6538f435d7c9276a"
def get_weather(city: str):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    data = requests.get(url).json()

    if data.get("cod") != 200:
        return {"error": "City not found"}

    return {
        "City": city,
        "Temperature": f"{data['main']['temp']} °C",
        "Weather": data["weather"][0]["description"],
        "Humidity": data["main"]["humidity"]
    }
