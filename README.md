# Mini Workspace AI – Private Knowledge Q&A

A production-ready Django web application that allows users to upload documents (TXT/PDF), ask AI-powered questions, view answer sources, and track recent query history.

This project was built as part of a build task to demonstrate backend architecture, LLM integration, clean deployment practices, and structured development workflow.

---

## 🚀 Live Demo

🔗 Live URL: https://mini-workspace-ai.onrender.com

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
```bash
git clone <your-repo-link>
cd mini-workspace-ai
```
### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Create `.env`
```bash
DEBUG=True
GROQ_API_KEY=your_groq_key
```
### 5. Run migrations
```bash
python manage.py migrate
```
### 6. Run server
```bash
python manage.py runserver
```
---

## 🌍 Production Deployment (Render)
```bash
https://mini-workspace-ai.onrender.com
```
### Required Environment Variables
```bash
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=5432
GROQ_API_KEY=
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
```
### Build Command
```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput
```
### Start Command
```bash
gunicorn config.wsgi:application
```
---

## 🛡 Security Practices

- No API keys committed
- `.env` excluded via `.gitignore`
- Environment-based configuration
- Production-safe error handling
- DEBUG disabled in production

---

## 📈 Future Improvements

- Semantic search using embeddings
- Chunk-based retrieval
- Richer response formatting
- User authentication
- Multi-document citation

---

## 👤 Author

Vipul Saraswat  
Backend Developer | Python | Django | LLM Integration  