from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UrlInput(BaseModel):
    url: str

@app.post("/summarize-url")
def summarize_url(data: UrlInput):
    try:
        response = requests.get(data.url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=" ", strip=True)
        max_chars = 5000
        trimmed_text = text[:max_chars]
        return {"summary": trimmed_text[:500] + "..." if len(trimmed_text) > 500 else trimmed_text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/summarize-pdf")
def summarize_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDFs are allowed.")
    return {"summary": f"✅ Summary of uploaded PDF: {file.filename}"}
