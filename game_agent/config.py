# config.py
import os
from dotenv import load_dotenv, find_dotenv
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletion
from openai.types.chat.chat_completion import Choice
from game_agents import Agent, Runner, OpenAIChatCompletionsModel

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

# Game Configuration
PLAYER_STARTING_HP = 10
MONSTER_STARTING_HP = 5
PLAYER_ATTACK_DAMAGE = 2
MONSTER_ATTACK_DAMAGE = 3
PLAYER_HIT_THRESHOLD = 8
MONSTER_HIT_THRESHOLD = 10

# Game State
STARTING_LOCATION = "Whispering Woods"
STARTING_INVENTORY = []

# Agent Configuration
AGENT_TEMPERATURE = 0.7

# Combat Configuration
DICE_SIDES = 20

# OpenAI Configuration
OPENAI_API_KEY = api_key
DEFAULT_MODEL = model_name 