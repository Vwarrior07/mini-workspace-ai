# Mini Workspace AI – Private Knowledge Q&A

A production-ready Django web application that allows users to upload documents (TXT/PDF), ask AI-powered questions, view answer sources, and track recent query history.

This project was built as part of a build task to demonstrate backend architecture, LLM integration, clean deployment practices, and structured development workflow.

---

## 🚀 Live Demo

🔗 Live URL: (Add your Render link here after deployment)

---

## 📌 Features

### 1. Document Upload
- Supports `.txt` and `.pdf` files
- Extracts and stores document content
- View uploaded document list
- Admin panel support

### 2. AI-Powered Q&A
- Ask questions based on uploaded documents
- Uses keyword-based relevance matching
- Sends selected document context to LLM
- Returns:
  - AI-generated answer
  - Source document
  - Excerpt used

### 3. Run History
- Stores each question-answer pair
- Displays last 5 runs
- Includes timestamp and source info

### 4. Health Status Endpoint
- `/status/` endpoint checks:
  - Backend status
  - Database connection
  - LLM connectivity
- Live status indicator in bottom footer

### 5. Dashboard UI
- Clean Tailwind-based layout
- Central landing page
- Connected navigation
- Responsive design

---

## 🏗 Architecture

- **Backend:** Django
- **Database (Local):** SQLite
- **Database (Production):** PostgreSQL
- **LLM Provider:** Groq (Llama model)
- **Deployment:** Render
- **Production Server:** Gunicorn

### Project Structure



Clean separation of concerns:
- `documents` → file handling
- `qa` → LLM logic
- `runs` → history storage
- `status` → health checks

---

## 🧠 LLM Integration

The application:
1. Performs keyword-based document relevance scoring.
2. Selects the most relevant document.
3. Sends limited context to LLM.
4. Returns structured answer with source tracking.

Error handling is implemented to prevent crashes during LLM failures.

---

## ⚙️ Local Setup

### 1. Clone repository
---
git clone <your-repo-link>
cd mini-workspace-ai
---


### 2. Create virtual environment
---
python -m venv venv
venv\Scripts\activate # Windows
---


### 3. Install dependencies
---
pip install -r requirements.txt
---