import requests


def find_places(city: str):

    geo = requests.get(
        f"https://api.geoapify.com/v1/geocode/search?text={city}&apiKey={API_KEY}"
    ).json()

    lat = geo["features"][0]["properties"]["lat"]
    lon = geo["features"][0]["properties"]["lon"]

    url = (
    f"https://api.geoapify.com/v2/places"
    f"?categories=tourism.attraction"
    f"&filter=circle:{lon},{lat},50000"
    f"&limit=30"
    f"&apiKey={API_KEY}"
)
    data = requests.get(url).json()

    places = []

    for item in data.get("features", []):
        props = item.get("properties", {})

        name = (
        props.get("name")
        or props.get("formatted")
        or props.get("address_line1")
            )

        if name and name not in places:
            places.append(name)

    return places
