import requests
API_KEY = "5417371de3f34e89bda714515ee6929d"

def find_hotels(city: str):

    geo = requests.get(
        f"https://api.geoapify.com/v1/geocode/search?text={city}&apiKey={API_KEY}"
    ).json()

    lat = geo["features"][0]["properties"]["lat"]
    lon = geo["features"][0]["properties"]["lon"]

    url = f"https://api.geoapify.com/v2/places?categories=accommodation.hotel&filter=circle:{lon},{lat},10000&limit=5&apiKey={API_KEY}"

    data = requests.get(url).json()

    hotels = []

    for hotel in data["features"]:
        hotels.append(hotel["properties"]["name"])

    return hotels
