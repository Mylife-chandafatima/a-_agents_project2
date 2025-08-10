import chainlit as cl
from agents import Runner
from experts.destination_planning_agent import destination_agent
from experts.travel_exploration_agent import explore_agent
from experts.travel_booking_agent import booking_agent

# Event handler for chat start
@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("history", [])
    welcome_message = "🌟 Hello! Welcome to your AI Travel Designer. Ready to discover your next adventure? Ask me anything about destinations, flights, or hotels! 🌍✈️"
    await cl.Message(welcome_message).send()

# Event handler for incoming messages
@cl.on_message
async def on_message(message: cl.Message):
    session_history = cl.user_session.get("history") or []
    session_history.append({"role": "user", "content": message.content})

    loading_message = await cl.Message("🔎 Planning your perfect trip... Please wait!").send()

    try:
        # Use the OpenAI Agents SDK Runner to run the destination agent
        agent_result = await Runner.run(
            destination_agent,
            session_history
        )
        final_output = agent_result.final_output

        loading_message.content = final_output
        await loading_message.update()

        # Update session history
        session_history = agent_result.to_input_list()
        cl.user_session.set("history", session_history)

    except Exception as error:
        loading_message.content = f"❌ Oops! Something went wrong: {error}"
        await loading_message.update()
