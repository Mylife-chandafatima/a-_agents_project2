# game_assistants_manager.py
import config
from tools import GENERATE_EVENT_TOOL_SCHEMA, ROLL_DICE_TOOL_SCHEMA, GET_REWARD_TOOL_SCHEMA

def create_assistants(client=None) -> dict:
    """Creates all game assistants and returns them in a dictionary."""
    
    # Use config client if no client provided
    if client is None:
        client = config.external_client
    
    narrator_agent = client.beta.assistants.create(
        name="NarratorAgent",
        instructions=(
            "You are the Game Master. Narrate a fantasy story. Describe scenes vividly. "
            "Give the player clear choices. Use the 'generate_event' tool to decide what happens next. "
            "If combat starts, your FINAL response MUST be a JSON object: "
            "{\"action\": \"handoff\", \"next_agent\": \"MonsterAgent\", \"details\": \"A goblin appears!\"}"
        ),
        model=config.DEFAULT_MODEL,
        tools=[GENERATE_EVENT_TOOL_SCHEMA],
    )

    monster_agent = client.beta.assistants.create(
        name="MonsterAgent",
        instructions=(
            "You manage combat. A monster has appeared. Narrate the fight turn-by-turn. "
            "Use the 'roll_dice' tool for attacks (1d20). A roll > 10 hits. Player and monster have 3 HP. "
            "When combat ends, your FINAL response MUST be a JSON object. "
            "On victory: {\"action\": \"handoff\", \"next_agent\": \"ItemAgent\", \"details\": \"The player is victorious!\"} "
            "On defeat: {\"action\": \"end_game\", \"details\": \"The player has been defeated.\"}"
        ),
        model=config.DEFAULT_MODEL,
        tools=[ROLL_DICE_TOOL_SCHEMA],
    )
    
    item_agent = client.beta.assistants.create(
        name="ItemAgent",
        instructions=(
            "You are the quartermaster. The player won a battle. Reward them with one item: 'Health Potion' or 'Sword of Light'. "
            "Your FINAL response MUST be a JSON object: "
            "{\"action\": \"handoff\", \"next_agent\": \"NarratorAgent\", \"details\": \"You found a Health Potion!\"}"
        ),
        model=config.DEFAULT_MODEL,
        tools=[GET_REWARD_TOOL_SCHEMA],
    )

    return {
        "NarratorAgent": narrator_agent,
        "MonsterAgent": monster_agent,
        "ItemAgent": item_agent,
    } 