from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from summarizer import summarize_content, summarize_pdf_file

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class HtmlInput(BaseModel):
    htmlContent: str

@app.post("/summarize/html")
async def summarize_html_api(input: HtmlInput):
    return {"summary": summarize_content(input.htmlContent)}

@app.post("/summarize/pdf")
async def summarize_pdf_api(file: UploadFile = File(...)):
    return {"summary": summarize_pdf_file(file)}
