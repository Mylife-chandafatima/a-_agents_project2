# import os
# from dotenv import load_dotenv, find_dotenv
# from openai import AsyncOpenAI
# from openai.types.chat import ChatCompletion
# from openai.types.chat.chat_completion import Choice
# from agents import OpenAIChatCompletionsModel, RunConfig

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
# model = OpenAIChatCompletionsModel(
#     model="gpt-4o",  # or "gpt-4o-mini" if supported in your setup
#     openai_client=external_client
# )

# # ✅ Final config
# openai_config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )



# # config_gemini.py
# import os
# from dotenv import load_dotenv, find_dotenv
# import google.generativeai as genai
# from agents import RunConfig  # Assuming your code uses a custom RunConfig

# # Load .env
# load_dotenv(find_dotenv())

# google_api_key = os.getenv("GOOGLE_API_KEY")

# if not google_api_key:
#     raise ValueError("GOOGLE_API_KEY is not set. Please check your .env file.")

# # Configure Gemini
# genai.configure(api_key=google_api_key)

# # Wrapper class to simulate OpenAI-like behavior
# class GeminiModelWrapper:
#     def __init__(self, model_name="gemini-pro"):
#         self.model = genai.GenerativeModel(model_name)

#     async def acompletion(self, prompt: str):
#         response = self.model.generate_content(prompt)
#         return {"choices": [{"message": {"content": response.text}}]}

# # Final config for Gemini
# model = GeminiModelWrapper()

# openai_config = RunConfig(
#     model=model,
#     model_provider=None,  # Gemini doesn't need OpenAI client
#     tracing_disabled=True
# )



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