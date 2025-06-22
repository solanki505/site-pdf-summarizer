# 📄 Website & PDF Summarizer
https://github.com/user-attachments/assets/f2fb55cd-0079-4bac-9e09-b8e00c3dd548

<br>
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

site-pdf-summarizer/<br>
│<br>
├── frontend/ # Vite + React app<br>
│ ├── App.jsx<br>
│ ├── main.jsx<br>
│ ├── style.css<br>
│ └── vite.config.js<br>
│<br>
├── backend/ # FastAPI backend<br>
│ ├── main.py # API endpoints<br>
│ └── summarizer.py # Summarization logic<br>
│<br>
├── requirements.txt # Backend dependencies<br>
└── README.md<br>
# Setup Frontend
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
create .env file and add <br>
GROQ_API_KEY=your_groq_key

