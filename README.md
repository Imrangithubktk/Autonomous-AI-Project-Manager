# 🤖 Autonomous AI Project Manager

An AI-powered Project Management System built using **FastAPI, PostgreSQL, LangGraph, Groq LLM, RAG, and Streamlit**. The system automates project monitoring, analytics, AI recommendations, and intelligent conversations with persistent memory.

---

# 📌 Project Overview

Autonomous AI Project Manager is an intelligent platform that helps engineering teams manage projects efficiently. It combines traditional project management features with AI agents that can analyze project data, answer user queries, provide recommendations, and retrieve knowledge from documents using Retrieval-Augmented Generation (RAG).

The system also stores conversation history in PostgreSQL so the AI can remember previous interactions within a session.

---

# 🚀 Features

## Project Management

* Create Projects
* Update Projects
* Delete Projects
* View Projects

## Task Management

* Create Tasks
* Update Tasks
* Delete Tasks
* Track Task Status
* Track Task Priority

## Dashboard

* Total Projects
* Active Projects
* Completed Projects
* Total Tasks
* Pending Tasks
* Completed Tasks

## Analytics

* Project Status Analytics
* Task Status Analytics
* Task Priority Analytics
* Upcoming Deadlines
* Dashboard Summary

## AI Features

* Supervisor Agent
* Analytics Agent
* Recommendation Agent
* Reporter Agent
* General Chat Agent
* RAG Agent

## AI Capabilities

* Intelligent Project Recommendations
* General Question Answering
* Document Question Answering (RAG)
* Conversation Memory
* Session-based Chat History

---

# 🧠 AI Workflow

User Query

↓

Supervisor Agent

↓

Intent Detection

↓

Depending on Intent:

* Analytics Agent
* Recommendation Agent
* Reporter Agent
* General Agent
* RAG Agent

↓

Final AI Response

---

# 🏗️ Tech Stack

## Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic

## AI

* Groq LLM
* LangChain
* LangGraph
* RAG

## Frontend

* Streamlit
* Plotly

## Database

* PostgreSQL

---

# 📂 Project Structure

```text
Autonomous_project_manager_system/

│── app/
│   ├── ai/
│   ├── agents/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── graph/
│   ├── models/
│   ├── rag/
│   ├── services/
│   ├── monitoring/
│   └── main.py
│
├── dashboard/
│   ├── app.py
│   ├── api_client.py
│   ├── pages/
│   │   ├── dashboard.py
│   │   ├── analytics.py
│   │   ├── recommendations.py
│   │   └── chat.py
│   └── utils.py
│
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure environment variables in the `.env` file.

Run FastAPI

```bash
uvicorn app.main:app --reload
```

Run Streamlit

```bash
streamlit run dashboard/app.py
```

---

# 📡 API Endpoints

## Projects

* GET /projects/
* POST /projects/
* PUT /projects/{id}
* DELETE /projects/{id}

## Tasks

* GET /tasks/
* POST /tasks/
* PUT /tasks/{id}
* DELETE /tasks/{id}

## Dashboard

* GET /dashboard/summary

## Analytics

* GET /analytics/dashboard
* GET /analytics/project-status
* GET /analytics/task-status
* GET /analytics/task-priority
* GET /analytics/upcoming-deadlines

## AI

* POST /ai/chat
* GET /ai/recommendations

---

# 💬 Conversation Memory

The application stores user conversations in PostgreSQL using session IDs.

Features include:

* Session-based memory
* Conversation history
* Context-aware responses
* Persistent storage

---

# 📈 Future Improvements

* User Authentication
* Multi-user Support
* Role-based Access Control
* Email Notifications
* Docker Deployment
* CI/CD Pipeline
* Cloud Deployment
* File Upload for RAG
* Advanced AI Agents

## 🚀 Live Demo
Check out the live API here:
[https://autonomous-ai-project-manager.onrender.com/docs](https://autonomous-ai-project-manager.onrender.com/docs)

---

# 👨‍💻 Author

**Imran Ullah**

Bachelor's in Data Science

---

# 📄 License

This project is created for educational and portfolio purposes.
