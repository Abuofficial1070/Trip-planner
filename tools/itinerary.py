from tools.places import find_places

def create_itinerary(city: str, days: int):

    places = find_places(city)

    # If find_places returns a dictionary
    if isinstance(places, dict):
        place_list = places.get("places", [])
    else:
        place_list = places

    if not place_list:
        return {
            "destination": city,
            "itinerary": ["No tourist places found."]
        }

    itinerary = {}

    index = 0

    for day in range(1, days + 1):

        today = []

        for _ in range(3):
            if index < len(place_list):
                today.append(place_list[index])
                index += 1

        # Restart from beginning if places are fewer than days
        if not today:
            index = 0
            for _ in range(min(3, len(place_list))):
                today.append(place_list[index])
                index += 1

        itinerary[f"Day {day}"] = today

    return itinerary