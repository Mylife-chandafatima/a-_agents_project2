🤖 AI Agents SDK - Multi-Project Collection (Gemini + UV)
A comprehensive collection of AI-powered applications built with Google Gemini API and Chainlit, featuring specialized agents for career guidance, gaming, and travel planning.
This version is optimized for UV-based project setup.

📋 Project Overview
This repository contains three distinct AI applications:

🎓 Career Agent – Professional Development Assistant

⚔️ Game Agent – Interactive Adventure Game

🌍 Travel Agent – Intelligent Travel Planner

🎓 Career Agent
Location: career_agent/
Helps users explore career paths, develop skills, and find job opportunities.

✨ Features

Career Guidance – Discover paths based on interests and skills

Skill Development – Personalized learning roadmaps

Job Search – Find relevant job openings

Interactive Planning – Step-by-step guidance

⚔️ Game Agent
Location: game_agent/
An immersive text-based AI-powered adventure game with dynamic storytelling, combat mechanics, and item management.

🌍 Travel Agent
Location: travel-agent/
An AI travel assistant for destination discovery, itinerary planning, and travel bookings.

🛠️ Technology Stack
Google Gemini API (google-generativeai)

Chainlit – Interactive chat interface

Python 3.8+

Async/Await for concurrency

📋 Prerequisites
Python 3.8 or higher

Gemini API Key

Internet connection for API calls

🔧 Installation & Setup (UV Version)
1. Clone the Repository
bash
Copy
Edit
git clone <repository-url>
cd ai-agents-sdk
2. Create .env Files for Each Project
bash
Copy
Edit
echo "GEMINI_API_KEY=your_api_key_here" > career_agent/.env
echo "GEMINI_API_KEY=your_api_key_here" > game_agent/.env
echo "GEMINI_API_KEY=your_api_key_here" > travel-agent/.env
3. Install Dependencies with UV
Career Agent

bash
Copy
Edit
cd career_agent
uv sync
Game Agent

bash
Copy
Edit
cd ../game_agent
uv sync
Travel Agent

bash
Copy
Edit
cd ../travel-agent
uv sync
🚀 Running the Applications with UV
Career Agent

bash
Copy
Edit
cd career_agent
uv run chainlit run main.py
Game Agent

bash
Copy
Edit
cd ../game_agent
uv run chainlit run main.py
Travel Agent

bash
Copy
Edit
cd ../travel-agent
uv run chainlit run main.py
🔒 Security
Store API keys in .env

Never commit .env files

Use environment variables for security
