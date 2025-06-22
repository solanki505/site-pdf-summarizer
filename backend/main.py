from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from summarizer import summarize_url, summarize_pdf_file

app = FastAPI()

# Allow all CORS origins for dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/summarize/url")
async def summarize_url_api(url: str = Form(...)):
    return {"summary": summarize_url(url)}

@app.post("/summarize/pdf")
async def summarize_pdf_api(file: UploadFile = File(...)):
    return {"summary": summarize_pdf_file(file)}
