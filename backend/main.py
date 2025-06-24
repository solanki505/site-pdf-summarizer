from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ✅ CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ For HTML summarization
class HtmlInput(BaseModel):
    html: str

@app.post("/summarize-url")
def summarize_url(data: HtmlInput):
    html_content = data.html
    # replace with your actual summary logic
    return {"summary": "✅ Summary of the provided HTML content."}

# ✅ For PDF summarization
@app.post("/summarize-pdf")
def summarize_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDFs are allowed.")
    # replace with your actual PDF summary logic
    return {"summary": f"✅ Summary of uploaded PDF: {file.filename}"}
