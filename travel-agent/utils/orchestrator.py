from agents import Agent
from agents import RunContextWrapper
import chainlit as cl

def orchestrator_handoff(agent: Agent):
    async def _on_handoff(context: RunContextWrapper[None]):
        # Notify user about the handoff
        await cl.message(
            content=f"handing off to '{agent.name}'..."
        ).send
        # Update the user session with the new agent
        cl.user_session.set("agent", agent)
    return _on_handoff