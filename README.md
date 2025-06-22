# 📄 Website & PDF Summarizer

A full-stack application to **summarize articles from a website URL or uploaded PDF**.  
Built with **React (Vite) + FastAPI + LangChain + Groq API**.

---

## 🚀 Features

- 🔗 **Summarize Website** — Enter any URL (e.g., a Wikipedia page)
- 📄 **Summarize PDF** — Upload a PDF file
- 🧠 Uses **LLM (LLaMA 3 from Groq)** to generate summaries
- 🎨 Clean, responsive UI with gradient background
- 🌐 Deployed on **GitHub Pages** (frontend) & **Render** (backend)

---

## 🖼️ Live Demo

- **Frontend:** [https://solanki505.github.io/site-pdf-summarizer/](https://solanki505.github.io/site-pdf-summarizer/)
- **Backend:** [https://summarizer-backend-kc6t.onrender.com](https://summarizer-backend-kc6t.onrender.com)

---

## 📁 Project Structure

site-pdf-summarizer/
│
├── frontend/ # Vite + React app
│ ├── App.jsx
│ ├── main.jsx
│ ├── style.css
│ └── vite.config.js
│
├── backend/ # FastAPI backend
│ ├── main.py # API endpoints
│ └── summarizer.py # Summarization logic
│
├── requirements.txt # Backend dependencies
└── README.md
#2. Setup Frontend
```bash
cd frontend
npm install
npm run dev

```
# Setup Backend
```bash
Copy
Edit
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
create .env
GROQ_API_KEY=your_groq_key

