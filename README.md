🧠 AI-Therapist GenAI ChatBot

An AI-powered mental health support application built with Python, FastAPI, LangGraph, LangChain, Qwen, and MedGemma. It provides conversational support, safety-aware workflows, emergency calling, and nearby therapist discovery.

⚠️ This project is for educational/support purposes and is not a replacement for a licensed mental health professional or emergency service.

✨ Features

💬 AI mental-health conversation

🛡️ Safety / risk-aware workflow

🤖 Two LLM options:

Qwen via Groq — fast cloud inference

MedGemma via Ollama — local LLM inference

🧩 Function/tool calling

📞 Emergency contact calling via Twilio / Exotel

📍 Nearby therapist discovery using a location/maps service

🔄 LangGraph-based workflow orchestration

🏗️ Architecture

User
 ↓
Frontend
 ↓
FastAPI
 ↓
LangGraph
 ↓
Safety / LLM Decision
 ├── Qwen → Groq
 ├── MedGemma → Ollama
 ├── Calling Tool → Twilio / Exotel
 └── Location Tool → Maps / Location Service
 ↓
Response / Tool Result
 ↓
User

🛠️ Tech Stack

Category

Technologies

Language

Python

Backend

FastAPI, Uvicorn

AI Workflow

LangChain, LangGraph

LLMs

Qwen, MedGemma

LLM Runtime/Providers

Groq, Ollama

Calling

Twilio, Exotel

Location

Maps / Location API

Frontend

Streamlit / configured frontend

Version Control

Git, GitHub

🧩 Function Calling

The application can invoke backend tools when an action is required.

User Request
    ↓
LangGraph
    ↓
LLM
    ↓
Function Call
 ┌──┴──────────────┐
 ↓                 ↓
Calling          Location
 ↓                 ↓
Twilio/Exotel    Maps API

📞 Emergency Calling

For configured high-risk workflows:

User Message
 ↓
Safety Workflow
 ↓
Calling Function
 ↓
Twilio / Exotel
 ↓
Configured Emergency Contact

Telephony features require valid provider credentials, verified numbers, and applicable compliance.

📍 Therapist Location

Users can request nearby professional support:

"Find therapists near me"
          ↓
   Location Function
          ↓
    Maps / Location API
          ↓
 Nearby Therapist Results

📂 Project Structure

AI-Therapist-GenAI-ChatBot/
├── backend/
├── frontend/
├── screenshots/
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

⚙️ Setup

git clone https://github.com/vitthalkarole/AI-Therapist-GenAI-ChatBot.git
cd AI-Therapist-GenAI-ChatBot

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/macOS

pip install -r requirements.txt

Create a .env file from .env.example and add only the credentials required by your configuration.

Run Backend

uvicorn backend.main:app --reload

Run Streamlit Frontend

streamlit run frontend/app.py

Update the entry-point paths above if your actual filenames are different.

🔐 Security

Keep API keys and credentials in .env

Never commit .env to GitHub

Use .env.example for required variable names

📸 Screenshots

Add application screenshots to the screenshots/ folder.

🔮 Future Improvements

Conversation memory

Human therapist handoff

Appointment booking

Voice interaction

Multilingual support

Improved safety evaluation

Production deployment

👨‍💻 Author

Vitthal Kharole
Computer Science Engineering Student

GitHub

⭐ If you find the project useful, consider giving it a star.
