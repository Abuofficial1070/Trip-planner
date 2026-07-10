import os



from google.adk.agents import LlmAgent
import prompt

from tools import weather, hotel, places, itinerary, budget

travel_agent = LlmAgent(
    name="TravelAgent",
    model="gemini-2.5-flash",
    description="AI Travel Planner",
    instruction=prompt.SYSTEM_PROMPT,
    tools=[
        weather.get_weather,
        hotel.find_hotels,
        places.find_places,
        itinerary.create_itinerary,
        budget.calculate_budget,
    ],
)