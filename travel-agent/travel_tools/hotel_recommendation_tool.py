import os
from dotenv import load_dotenv, find_dotenv
from agents import function_tool, RunContextWrapper, AsyncOpenAI

load_dotenv(find_dotenv())

api_key = os.getenv("OPENAI_API_KEY")

client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

@function_tool
async def suggest_hotels():
    try:
        prompt = (
            f"Suggest hotels in {input['location']} for {input['dates']}.\n"
            f"Budget: {input['budget']}\n"
            f"Preferences: {input['preferences']}\n"
            "Provide hotel options with name, rating, price range, and key amenities.\n"
            "Format the response clearly with bullet points."
        )
        
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        
        output = response.choices[0].message.content
        
        return {
            "hotel_suggestions": output.strip()
        }
        
    except Exception as e:
        print("❌ Exception in suggest_hotels tool:", str(e))
        return {
            "error": f"❌ Exception in suggest_hotels tool: {str(e)}"
        } 