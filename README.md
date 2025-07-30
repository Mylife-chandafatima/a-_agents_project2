# 🤖 AI Agents SDK - Multi-Project Collection

A comprehensive collection of AI-powered applications built with OpenAI Agents SDK and Chainlit, featuring specialized agents for career guidance, gaming, and travel planning.

## 📋 Project Overview

This repository contains three distinct AI applications, each designed to solve specific real-world problems using advanced AI agent technology:

### 🎓 **Career Agent** - Professional Development Assistant
### ⚔️ **Game Agent** - Interactive Adventure Game
### 🌍 **Travel Agent** - Intelligent Travel Planner

---

## 🎓 Career Agent

**Location:** `career_agent/`

An AI-powered career guidance system that helps users explore career paths, develop skills, and find job opportunities.

### ✨ Features
- **Career Guidance** - Discover suitable career paths based on interests and skills
- **Skill Development** - Get personalized learning roadmaps for career advancement
- **Job Search** - Find relevant job opportunities in chosen fields
- **Interactive Planning** - Step-by-step career development guidance

### 🏗️ Structure
```
career_agent/
├── agents/                           # AI agents for career tasks
│   ├── career_guidance_agent.py      # Main career advisor
│   ├── skill_development_agent.py    # Learning roadmap creator
│   └── job_search_agent.py           # Job opportunity finder
├── tools/                           # Career planning tools
│   └── skill_roadmap_generator.py   # Skill development tool
├── utils/                           # Utility functions
├── main.py                          # Chainlit application
└── config.py                        # Configuration
```

### 🚀 Quick Start
```bash
cd career_agent
pip install -r requirements.txt
chainlit run main.py
```

---

## ⚔️ Game Agent

**Location:** `game_agent/`

An immersive text-based adventure game powered by AI agents that create dynamic storytelling and interactive gameplay.

### ✨ Features
- **Dynamic Storytelling** - AI-generated narrative with branching storylines
- **Combat System** - Turn-based combat with dice mechanics
- **Item Management** - Collect and use items throughout the adventure
- **Multiple AI Agents** - Specialized agents for narration, combat, and rewards

### 🏗️ Structure
```
game_agent/
├── game_agents/                      # Game AI agents
│   ├── game_narrator_agent.py        # Story narrator
│   ├── enemy_monster_agent.py        # Combat controller
│   ├── game_item_agent.py            # Item manager
│   └── game_base_agent.py            # Core game logic
├── game_assistants_manager.py        # Assistant management
├── tools.py                          # Game tools (dice, events)
├── main.py                           # Game application
└── config.py                         # Game configuration
```

### 🚀 Quick Start
```bash
cd game_agent
pip install -r requirements.txt
chainlit run main.py
```

---

## 🌍 Travel Agent

**Location:** `travel-agent/`

An intelligent travel planning assistant that helps users discover destinations, plan itineraries, and book travel arrangements.

### ✨ Features
- **Destination Discovery** - Find perfect travel destinations
- **Itinerary Planning** - Create detailed day-by-day travel plans
- **Flight Search** - Find and compare flight options
- **Hotel Recommendations** - Get personalized accommodation suggestions

### 🏗️ Structure
```
travel-agent/
├── travel_agents/                    # Travel AI agents
│   ├── travel_exploration_agent.py   # Destination discoverer
│   ├── destination_planning_agent.py # Itinerary planner
│   └── travel_booking_agent.py       # Booking assistant
├── travel_tools/                     # Travel tools
│   ├── flight_search_tool.py         # Flight finder
│   └── hotel_recommendation_tool.py  # Hotel recommender
├── utils/                           # Utility functions
├── main.py                          # Travel application
└── config.py                        # Configuration
```

### 🚀 Quick Start
```bash
cd travel-agent
pip install -r requirements.txt
chainlit run main.py
```

---

## 🛠️ Technology Stack

### Core Technologies
- **OpenAI Agents SDK** - AI agent orchestration and management
- **Chainlit** - Interactive chat interface for all applications
- **Python 3.8+** - Backend logic and processing
- **Async/Await** - Concurrent operation handling

### AI & ML
- **OpenAI GPT Models** - Natural language processing
- **Function Tools** - Custom tool integration
- **Agent Handoffs** - Seamless agent transitions

### Development Tools
- **Environment Variables** - Secure API key management
- **Modular Architecture** - Clean, maintainable code structure
- **Error Handling** - Robust error management

---

## 📋 Prerequisites

### System Requirements
- Python 3.8 or higher
- OpenAI API key
- Internet connection for API access

### Required Packages
Each project has its own `requirements.txt` file with specific dependencies.

---

## 🔧 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd agent-sdk-3
```

### 2. Set Up Environment
```bash
# Create .env file in each project directory
echo "OPENAI_API_KEY=your_api_key_here" > career_agent/.env
echo "OPENAI_API_KEY=your_api_key_here" > game_agent/.env
echo "OPENAI_API_KEY=your_api_key_here" > travel-agent/.env
```

### 3. Install Dependencies
```bash
# Career Agent
cd career_agent
pip install -r requirements.txt

# Game Agent
cd ../game_agent
pip install -r requirements.txt

# Travel Agent
cd ../travel-agent
pip install -r requirements.txt
```

---

## 🚀 Running the Applications

### Career Agent
```bash
cd career_agent
chainlit run main.py
```
**Use Case:** Ask about career paths, skill development, or job opportunities

### Game Agent
```bash
cd game_agent
chainlit run main.py
```
**Use Case:** Start an adventure game and interact with AI-driven storytelling

### Travel Agent
```bash
cd travel-agent
chainlit run main.py
```
**Use Case:** Plan trips, find flights, or get hotel recommendations

---

## 🎯 Use Cases & Examples

### Career Agent Examples
- "I'm interested in data science, what skills should I learn?"
- "Help me find jobs in software development"
- "Create a learning roadmap for becoming a UX designer"

### Game Agent Examples
- "I want to explore the dark forest"
- "Attack the goblin with my sword"
- "Check my inventory"

### Travel Agent Examples
- "I want to visit Paris for 5 days"
- "Find flights from New York to London"
- "Recommend hotels in Tokyo under $200/night"

---

## 🔒 Security & Best Practices

### API Key Management
- Store API keys in `.env` files (not in version control)
- Use environment variables for sensitive data
- Never commit API keys to the repository

### Error Handling
- Comprehensive error handling in all applications
- User-friendly error messages
- Graceful degradation when services are unavailable

### Data Privacy
- No sensitive user data is stored
- All conversations are processed in real-time
- Secure communication with OpenAI APIs

---

## 🤝 Contributing

We welcome contributions to improve any of the three projects!

### How to Contribute
1. **Fork the repository**
2. **Choose a project** - Career, Game, or Travel agent
3. **Create a feature branch**
4. **Make your changes**
5. **Test thoroughly**
6. **Submit a pull request**

### Development Guidelines
- Follow Python PEP 8 style guidelines
- Add comprehensive error handling
- Include docstrings for new functions
- Test your changes before submitting

---

## 📊 Project Statistics

| Project | Agents | Tools | Lines of Code | Complexity |
|---------|--------|-------|---------------|------------|
| Career Agent | 3 | 1 | ~500 | Medium |
| Game Agent | 4 | 3 | ~800 | High |
| Travel Agent | 3 | 2 | ~600 | Medium |

---

## 🆘 Support & Documentation

### Getting Help
- **Documentation** - Each project has its own README
- **Issues** - Open GitHub issues for bugs or feature requests
- **Discussions** - Use GitHub Discussions for questions

### Troubleshooting
- Check API key configuration
- Verify Python version compatibility
- Ensure all dependencies are installed
- Check network connectivity for API access

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **OpenAI** - For providing the Agents SDK
- **Chainlit** - For the excellent chat interface framework
- **Contributors** - Everyone who has helped improve these projects

---

## 🌟 Future Enhancements

### Planned Features
- **Voice Integration** - Add voice input/output capabilities
- **Multi-language Support** - Support for multiple languages
- **Advanced Analytics** - Usage analytics and insights
- **Mobile Apps** - Native mobile applications
- **API Endpoints** - RESTful APIs for integration

### Roadmap
- **Q1 2024** - Enhanced error handling and logging
- **Q2 2024** - Performance optimizations
- **Q3 2024** - New agent types and capabilities
- **Q4 2024** - Advanced UI/UX improvements

---

**Happy Coding! 🚀🤖✨**

*Choose your adventure: Build careers, play games, or plan travels with AI!*
