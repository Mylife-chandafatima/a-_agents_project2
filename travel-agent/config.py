# config.py
import os
from dotenv import load_dotenv, find_dotenv
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletion
from openai.types.chat.chat_completion import Choice
from agents import Agent, Runner, OpenAIChatCompletionsModel

# Load .env
load_dotenv(find_dotenv())

api_key = os.getenv("OPENAI_API_KEY")

# Check API key
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please ensure it is defined in your .env file.")

# ✅ Correct OpenAI Client
external_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://api.openai.com/v1"  # ✅ OpenAI base URL
)

# ✅ Correct model (adjust name if needed)
model_name = "gpt-4o"  # or "gpt-4o-mini" if supported in your setup

# Travel Configuration
DEFAULT_BUDGET = 1000
DEFAULT_TRIP_DURATION = 7  # days
MAX_TRAVELERS = 4
DEFAULT_DEPARTURE_CITY = "New York"
DEFAULT_DESTINATION_CITY = "Paris"

# Agent Configuration
AGENT_TEMPERATURE = 0.7
AGENT_MAX_TOKENS = 2000

# Travel Preferences
DEFAULT_ACCOMMODATION_TYPE = "hotel"
DEFAULT_TRANSPORTATION_TYPE = "flight"
DEFAULT_ACTIVITY_PREFERENCES = ["sightseeing", "food", "culture"]

# API Configuration
FLIGHT_API_ENDPOINT = "https://api.example.com/flights"
HOTEL_API_ENDPOINT = "https://api.example.com/hotels"
WEATHER_API_ENDPOINT = "https://api.example.com/weather"

# OpenAI Configuration
OPENAI_API_KEY = api_key
DEFAULT_MODEL = model_name