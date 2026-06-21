# Ra.One AI — Behavior Correction Chatbot

An AI-powered conversational chatbot that analyzes user-described behaviors and traits, then provides empathetic, psychology-grounded guidance to help users reflect on and improve them — inspired by the villain character "Ra.One" from the 2011 film of the same name.

**Live demo:** [ra-one-ai.onrender.com](https://ra-one-ai.onrender.com)

## Overview

Ra.One AI lets a user describe a behavior or trait (e.g. "I get angry easily" or "I lie to avoid conflict"), and responds with root-cause analysis, practical coping strategies, and follow-up questions — similar to a structured self-reflection conversation. It maintains context across the full conversation and responds fluently in both English and Hindi.

## Features

- **Persona-driven responses** — custom system prompt gives the AI a consistent, intense "Ra.One" voice while keeping guidance genuinely constructive
- **Multi-turn conversation memory** — the AI remembers prior messages in the session for coherent, contextual replies
- **Bilingual support** — responds naturally in English or Hindi depending on user input
- **Crisis-aware responses** — recognizes signs of serious distress and surfaces relevant helpline information
- **Custom dark-themed UI** — villain-inspired interface built with vanilla HTML/CSS/JS
- **Live deployment** — fully hosted and publicly accessible, with a CI/CD pipeline from GitHub to Render

## Tech Stack

- **Backend:** Python, Flask, Flask-CORS
- **AI/LLM:** Groq API (`llama-3.3-70b-versatile`)
- **Frontend:** HTML, CSS, JavaScript (vanilla, no framework)
- **Deployment:** Render (with Gunicorn as the production WSGI server)
- **Environment management:** `python-dotenv`

## How It Works

1. The frontend sends the full conversation history (including a system prompt defining Ra.One's persona) to a Flask backend via a `/chat` endpoint.
2. The backend forwards this to the Groq API, which generates a response using the Llama 3.3 70B model.
3. The response is returned to the frontend and appended to the conversation, preserving context for future turns.
4. The entire app is deployed on Render, with the Flask server also serving the static frontend files.

## Getting Started

### Prerequisites
- Python 3.x
- A free [Groq API key](https://console.groq.com)

### Setup

```bash
git clone https://github.com/sid0053/Ra-one-AI.git
cd Ra-one-AI
pip install -r requirements.txt
```

Create a `.env` file in the project root:
```
GROQ_API_KEY=your_api_key_here
```

### Run locally

```bash
python server.py
```

Then open `http://localhost:5000` in your browser.

## What I Learned

- Integrating a third-party LLM API into a real application (prompt design, conversation state management)
- Designing system prompts to shape a consistent AI persona and tone
- Building a Flask backend that serves both an API and static frontend
- Managing secrets safely using environment variables (including recovering from accidentally exposed API keys early in development)
- Debugging and deploying a full-stack app to a live production environment (Render), including fixing localhost-vs-production URL issues

## Future Improvements

- Persistent conversation history (per-user, saved to a database)
- User authentication
- Voice input/output support
- Expanded multilingual support beyond English/Hindi