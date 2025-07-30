# 🎮 Game Master Agent (Fantasy Adventure Game)

## What It Does
This AI-powered Chainlit app runs a **fun and fast** fantasy role-playing game using multiple specialized agents:
- **NarratorAgent**: Gives short, exciting story updates with emojis
- **MonsterAgent**: Manages fun combat with silly goblin responses
- **ItemAgent**: Announces rewards in an exciting way

## 🏗️ Project Structure
```
game_changer/
├── agents/                 # Agent modules
│   ├── __init__.py        # Package initialization with compatibility classes
│   ├── base_agent.py      # Base agent class
│   ├── narrator_agent.py  # Story narration agent (SHORT & FUN)
│   ├── monster_agent.py   # Combat management agent (SILLY)
│   └── item_agent.py      # Reward distribution agent (EXCITING)
├── main.py                # Chainlit app entry point
├── config.py              # Game configuration and OpenAI client setup
├── tools.py               # Game utilities and functions
├── assistants.py          # OpenAI assistants configuration
├── requirements.txt       # Dependencies
├── chainlit.md           # Chainlit app description
└── .gitignore            # Git ignore rules
```

## 🧠 Agent Architecture
- **Base Agent Class**: Common functionality for all agents
- **Specialized Agents**: Each agent has specific responsibilities
- **Modular Design**: Easy to add new agents or modify existing ones
- **Clean Separation**: Each agent is in its own file for better organization
- **Configuration Management**: Centralized settings and OpenAI client in config.py
- **Compatibility Classes**: Runner and OpenAIChatCompletionsModel for compatibility
- **Fun Responses**: All agents give short, exciting responses with emojis

## 🎯 Game Style
- **Short & Sweet**: Responses are 1-3 sentences max
- **Fun & Playful**: Not serious, lots of emojis and excitement
- **Fast Paced**: Quick turns and reduced delays
- **Engaging**: Keeps players interested with quick feedback

## 🔧 Configuration
The `config.py` file handles:
- **OpenAI Client Setup**: AsyncOpenAI client with proper configuration
- **Environment Variables**: Automatic .env file loading
- **API Key Validation**: Ensures OPENAI_API_KEY is properly set
- **Game Settings**: All game parameters in one place
- **Agent Imports**: Imports Agent, Runner, OpenAIChatCompletionsModel

## 📦 Available Imports
```python
from agents import (
    Agent,                    # Base agent class
    Runner,                   # Compatibility class
    OpenAIChatCompletionsModel, # Compatibility class
    NarratorAgent,            # Story narration (FUN)
    MonsterAgent,             # Combat management (SILLY)
    ItemAgent                 # Reward distribution (EXCITING)
)
```

## How to Run
```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables
# Create .env file with: OPENAI_API_KEY=your_api_key_here

# Run the game
chainlit run main.py
```

## 🎯 Game Flow
1. **Start**: Player begins in the Whispering Woods
2. **Explore**: Choose actions (e.g., "go to castle", "walk into forest")
3. **Combat**: Fight enemies with dice-based mechanics (FAST)
4. **Rewards**: Win items and continue the adventure
5. **Progress**: Track HP and inventory throughout the journey

## 🔧 Features
- **Dynamic Storytelling**: AI-generated narrative progression (SHORT)
- **Turn-based Combat**: Dice-rolling combat system (FAST)
- **Random Events**: Procedural event generation
- **Inventory System**: Collect and manage items
- **Modular Agents**: Clean, organized code structure
- **Configurable Settings**: Easy to modify game parameters
- **Async OpenAI Client**: Modern async/await pattern
- **Compatibility**: Support for Agent, Runner, OpenAIChatCompletionsModel imports
- **Fun Responses**: Short, exciting responses with emojis
