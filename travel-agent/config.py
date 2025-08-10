# # config.py
# import os
# from dotenv import load_dotenv, find_dotenv
# from openai import AsyncOpenAI
# from openai.types.chat import ChatCompletion
# from openai.types.chat.chat_completion import Choice
# from agents import Agent, Runner, OpenAIChatCompletionsModel

# # Load .env
# load_dotenv(find_dotenv())

# api_key = os.getenv("OPENAI_API_KEY")

# # Check API key
# if not api_key:
#     raise ValueError("OPENAI_API_KEY is not set. Please ensure it is defined in your .env file.")

# # ✅ Correct OpenAI Client
# external_client = AsyncOpenAI(
#     api_key=api_key,
#     base_url="https://api.openai.com/v1"  # ✅ OpenAI base URL
# )

# # ✅ Correct model (adjust name if needed)
# model = "gpt-4o-mini"  # or "gpt-4o-mini" if supported in your setup

# # Travel Configuration
# DEFAULT_BUDGET = 1000
# DEFAULT_TRIP_DURATION = 7  # days
# MAX_TRAVELERS = 4
# DEFAULT_DEPARTURE_CITY = "New York"
# DEFAULT_DESTINATION_CITY = "Paris"

# # Agent Configuration
# AGENT_TEMPERATURE = 0.7
# AGENT_MAX_TOKENS = 2000

# # Travel Preferences
# DEFAULT_ACCOMMODATION_TYPE = "hotel"
# DEFAULT_TRANSPORTATION_TYPE = "flight"
# DEFAULT_ACTIVITY_PREFERENCES = ["sightseeing", "food", "culture"]

# # API Configuration
# FLIGHT_API_ENDPOINT = "https://api.example.com/flights"
# HOTEL_API_ENDPOINT = "https://api.example.com/hotels"
# WEATHER_API_ENDPOINT = "https://api.example.com/weather"

# # OpenAI Configuration
# OPENAI_API_KEY = api_key
# DEFAULT_MODEL = model



import os
from dotenv import load_dotenv
from typing import cast
import chainlit as cl
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

# Load the environment variables from the .env file
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")


#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
        api_key=gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )
model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client
    )

config = RunConfig(
        model=model,
        model_provider=external_client,
        tracing_disabled=True
    )