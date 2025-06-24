from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from summarizer import summarize_url, summarize_pdf_file

app = FastAPI()

class URLPayload(BaseModel):
    html: str

@app.post("/summarize-url")
def summarize_html_url(payload: URLPayload):
    try:
        summary = summarize_url(payload.html)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}

@app.post("/summarize-pdf")
def summarize_uploaded_pdf(file: UploadFile = File(...)):
    try:
        summary = summarize_pdf_file(file)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}
