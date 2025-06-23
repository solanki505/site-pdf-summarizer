from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from summarizer import summarize_url, summarize_pdf_file
import os

app = FastAPI()

# ✅ CORS Setup for frontend (localhost:5173 or GitHub Pages)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev; change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Health check route (useful for monitoring and Render deployment)
@app.get("/health")
def health_check():
    return {"status": "ok"}

# ✅ Favicon handler to avoid 404 noise
@app.get("/favicon.ico")
def favicon():
    # If you want to serve a real icon, place it in backend/static/favicon.ico
    icon_path = "static/favicon.ico"
    if os.path.exists(icon_path):
        return FileResponse(icon_path)
    return {}  # fallback empty response

# ✅ API to summarize a website URL
@app.post("/summarize/url")
async def summarize_url_api(url: str = Form(...)):
    return {"summary": summarize_url(url)}

# ✅ API to summarize a PDF file
@app.post("/summarize/pdf")
async def summarize_pdf_api(file: UploadFile = File(...)):
    return {"summary": summarize_pdf_file(file)}
