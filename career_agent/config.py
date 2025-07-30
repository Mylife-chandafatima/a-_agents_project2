import os
from dotenv import load_dotenv, find_dotenv
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletion
from openai.types.chat.chat_completion import Choice
from agents import OpenAIChatCompletionsModel, RunConfig

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
model = OpenAIChatCompletionsModel(
    model="gpt-4o",  # or "gpt-4o-mini" if supported in your setup
    openai_client=external_client
)

# ✅ Final config
openai_config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
