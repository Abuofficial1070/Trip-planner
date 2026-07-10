import requests

API_KEY = "5417371de3f34e89bda714515ee6929d"

hotel_prices = {
    "dubai": 12000,
    "paris": 18000,
    "london": 17000,
    "singapore": 10000,
    "tokyo": 14000,
    "new york": 19000,
    "goa": 3500,
    "kerala": 3000,
    "ooty": 2500,
    "chennai": 2800,
    "mumbai": 6000,
    "bangalore": 4000,
    "hyderabad": 3500,
    "delhi": 4500,
}

DEFAULT_HOTEL_PRICE = 5000


def calculate_budget(destination: str, days: int, people: int):

    # Verify that the place exists
    url = (
        f"https://api.geoapify.com/v1/geocode/search"
        f"?text={destination}"
        f"&apiKey={API_KEY}"
    )

    data = requests.get(url).json()

    if not data.get("features"):
        return {"error": "Destination not found"}

    city = destination.lower()

    hotel_per_night = hotel_prices.get(city, DEFAULT_HOTEL_PRICE)

    hotel = hotel_per_night * days

    food = int(hotel * 0.45)

    transport = int(hotel * 0.25)

    sightseeing = int(hotel * 0.30)

    total = hotel + food + transport + sightseeing

    return {
        "Destination": destination.title(),
        "Days": days,
        "People": people,
        "Hotel Cost": hotel,
        "Food Cost": food,
        "Transport Cost": transport,
        "Sightseeing Cost": sightseeing,
        "Total Estimated Budget": total
    }
