# 🧠 AI-Therapist GenAI ChatBot

An AI-powered mental health support chatbot built with **Python, FastAPI, LangChain, LangGraph, Qwen, and MedGemma**.

> ⚠️ For educational/support purposes only. It is not a replacement for a licensed mental health professional or emergency service.

## 🚀 Live Demo

👉 **[Try the AI-Therapist ChatBot](https://ai-therapist-genai-chatbot-2.onrender.com)**

## ✨ Features

* 💬 AI mental-health conversation
* 🛡️ Safety/risk-aware workflow
* 🤖 Qwen via Groq
* 🧠 MedGemma via Ollama
* 🔄 LangGraph workflow orchestration
* 🧩 Function/tool calling
* 📞 Emergency calling with Twilio/Exotel
* 📍 Nearby therapist discovery
* 🖥️ Streamlit frontend
* ⚡ FastAPI backend

## 🏗️ Architecture

```text
User
 ↓
Streamlit
 ↓
FastAPI
 ↓
LangGraph
 ↓
LLM / Tools
 ├── Qwen → Groq
 ├── MedGemma → Ollama
 ├── Calling → Twilio/Exotel
 └── Location → Maps API
 ↓
Response
```

## 🛠️ Tech Stack

**Python • FastAPI • Streamlit • LangChain • LangGraph • Qwen • MedGemma • Groq • Ollama • Twilio • Exotel**

## 📂 Project Structure

```text
AI-Therapist-GenAI-ChatBot/
├── backend/
├── frontend/
├── screenshots/
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

## ⚙️ Run Locally

```bash
git clone https://github.com/vitthalkarole/AI-Therapist-GenAI-ChatBot.git
cd AI-Therapist-GenAI-ChatBot

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

### Backend

```bash
uvicorn backend.main:app --reload
```

### Frontend

```bash
streamlit run frontend/frontend.py
```

Create a `.env` file using `.env.example` and add the required API credentials.

## 🔐 Security

* Never commit `.env` or API keys.
* Store production secrets in environment variables.
* Keep telephony and AI provider credentials on the backend.

## 👨‍💻 Author

**Vitthal Kharole**
Computer Science Engineering Student

⭐ If you find the project useful, consider giving it a star.
