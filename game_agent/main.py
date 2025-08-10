# main.py
import chainlit as cl
import asyncio
from experts.game_base_agent import base_agent
from experts.game_narrator_agent import narrator_agent
from experts.enemy_monster_agent import monster_agent
from experts.game_item_agent import item_agent

from agents import  Agent, Runner, OpenAIChatCompletionsModel
import tools
import config

# Initialize agents
narrator_agent = narrator_agent
monster_agent = monster_agent
item_agent = item_agent

# Game state
player_hp = config.PLAYER_STARTING_HP
monster_hp = config.MONSTER_STARTING_HP

@cl.on_chat_start
async def start_chat():
    """Initialize the chat session with an immersive game intro."""
    await cl.Message(
        content="""⚔️ **Greetings, Adventurer!**

You find yourself at the edge of the **Whispering Woods**, a place of ancient magic and forgotten secrets. Local legends speak of a lost artifact, the 'Sunstone', hidden deep within. It is said to have the power to heal the blighted lands.

Before you lies a fork in the path. 
- To your **left**, a narrow trail disappears into the dark, gnarled trees. 
- To your **right**, the path follows a murmuring stream.

**What do you do?** (e.g., "Go left into the trees" or "Follow the stream to the right")
"""
    ).send()

@cl.on_message
async def main(message: cl.Message):
    """Main message handler that coordinates all agents."""
    global player_hp, monster_hp
    
    try:
        workflow_results = []
        
        # 1. NarratorAgent generates an event and narrates
        event = tools.generate_event()
        narrator_response = await narrator_agent.narrate_event(event)
        workflow_results.append({
            "agent": "NarratorAgent",
            "description": "Narrates the story progress.",
            "response": narrator_response
        })

        # 2. Combat Logic (if monster encounter)
        if "monster" in event.lower() or "goblin" in event.lower():
            combat_log = "⚔️ Battle begins!\n"
            
            while player_hp > 0 and monster_hp > 0:
                # Player attacks
                player_roll = tools.roll_dice(config.DICE_SIDES)
                if player_roll > config.PLAYER_HIT_THRESHOLD:
                    monster_hp -= config.PLAYER_ATTACK_DAMAGE
                    combat_log += f"⚔️ You hit! (Monster HP: {monster_hp})\n"
                else:
                    combat_log += "⚔️ You missed!\n"

                if monster_hp <= 0: 
                    break

                # Monster attacks
                monster_roll = tools.roll_dice(config.DICE_SIDES)
                if monster_roll > config.MONSTER_HIT_THRESHOLD:
                    player_hp -= config.MONSTER_ATTACK_DAMAGE
                    monster_action = await monster_agent.describe_attack(True, config.MONSTER_ATTACK_DAMAGE)
                    combat_log += f"👹 {monster_action} (Your HP: {player_hp})\n"
                else:
                    monster_action = await monster_agent.describe_attack(False)
                    combat_log += f"👹 {monster_action}\n"
            
            # Add combat log as MonsterAgent's response
            workflow_results.append({
                "agent": "MonsterAgent",
                "description": "Manages the combat phase.",
                "response": combat_log
            })

            # 3. Reward Logic (if player won)
            if monster_hp <= 0:
                reward = tools.get_reward()
                reward_response = await item_agent.announce_reward(reward)
                workflow_results.append({
                    "agent": "ItemAgent",
                    "description": "Grants rewards to the player.",
                    "response": reward_response
                })
            else:
                workflow_results.append({
                    "agent": "GameMaster",
                    "description": "Game Over.",
                    "response": "💀 You have been defeated. Game Over!"
                })
        
        # Display each agent's result
        for i, result in enumerate(workflow_results):
            await cl.Message(
                author=result["agent"],
                content=f"*{result['description']}*\n\n{result['response']}"
            ).send()
            
            # Shorter delay between agents
            if i < len(workflow_results) - 1:
                await cl.Message(content="**🔄 Next phase...**").send()
                await asyncio.sleep(0.5)  # Reduced delay
        
        await cl.Message(content="\n---\n✅ **Turn Complete!** Type your next action to continue the adventure.").send()
        
    except Exception as e:
        await cl.Message(content=f"❌ An error occurred: {e}").send()