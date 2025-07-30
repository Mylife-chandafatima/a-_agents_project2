# tools.py
import random

# --- Tool Functions ---
def roll_dice(sides: int = 20, count: int = 1) -> int:
    """Simulates rolling one or more dice with a specific number of sides."""
    return sum(random.randint(1, sides) for _ in range(count))

def generate_event() -> str:
    """Generates a random event to advance the story dynamically."""
    events = [
        "You find a hidden chest containing a mysterious map.",
        "A monster jumps out from the shadows! Prepare for combat.",
        "A goblin appears from behind a tree! Battle begins.",
        "You discover an ancient, moss-covered ruin. It seems quiet.",
        "A traveling merchant offers to sell you a health potion.",
        "The path ahead is blocked by a raging river.",
        "A mysterious fog rolls in, obscuring your vision.",
        "You hear strange sounds coming from the darkness."
    ]
    return random.choice(events)

def get_reward() -> str:
    """Generates a reward after winning a combat."""
    rewards = [
        "Health Potion",
        "Sword of Light", 
        "Shield of Resilience",
        "Magic Ring",
        "Golden Coin",
        "Mysterious Scroll",
        "Enchanted Amulet",
        "Crystal Shard"
    ]
    return random.choice(rewards)

# --- Tool Schemas for OpenAI ---
ROLL_DICE_TOOL_SCHEMA = {
    "type": "function",
    "function": {
        "name": "roll_dice",
        "description": "Rolls one or more dice with a given number of sides to determine an outcome.",
        "parameters": {
            "type": "object",
            "properties": {
                "sides": {"type": "integer", "description": "The number of sides on the die (e.g., 6, 20)."},
                "count": {"type": "integer", "description": "The number of dice to roll."},
            },
            "required": ["sides", "count"],
        },
    },
}

GENERATE_EVENT_TOOL_SCHEMA = {
    "type": "function",
    "function": {
        "name": "generate_event",
        "description": "Generates a random event when the player explores or moves to a new area. Use this to decide what happens next in the story.",
        "parameters": {"type": "object", "properties": {}},
    },
}

GET_REWARD_TOOL_SCHEMA = {
    "type": "function",
    "function": {
        "name": "get_reward",
        "description": "Generates a random reward item after winning a combat encounter.",
        "parameters": {"type": "object", "properties": {}},
    },
}