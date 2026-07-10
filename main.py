import asyncio
import os

# Google API Key

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agent_code import travel_agent

APP_NAME = "travel_planner_agent"
USER_ID = "user1"
SESSION_ID = "session1"


async def main():

    session_service = InMemorySessionService()

    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    runner = Runner(
        app_name=APP_NAME,
        agent=travel_agent.travel_agent,
        session_service=session_service,
    )

    print("=" * 60)
    print("      Welcome to the AI Travel Planner Agent!")
    print("Type 'exit' to quit.")
    print("=" * 60)

    while True:

        prompt = input("\nYou: ")

        if prompt.lower() in ["exit", "quit"]:
            print("\nThank you for using Travel Planner Agent!")
            break

        message = types.Content(
            role="user",
            parts=[types.Part(text=prompt)],
        )

        print("\nAgent:\n")

        try:

            async for event in runner.run_async(
                user_id=USER_ID,
                session_id=SESSION_ID,
                new_message=message,
            ):

                if event.is_final_response():

                    if (
                        event.content
                        and event.content.parts
                        and event.content.parts[0].text
                    ):
                        print(event.content.parts[0].text)

        except Exception as e:

            print("\nError:", e)

            if "503" in str(e):
                print("\nGemini server is busy. Please try again in a few seconds.")

            elif "429" in str(e):
                print("\nAPI quota exceeded. Try again later.")

            else:
                print("\nSomething went wrong while generating the travel plan.")


if __name__ == "__main__":
    asyncio.run(main())