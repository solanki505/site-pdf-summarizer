import os
from bs4 import BeautifulSoup
from pdfminer.high_level import extract_text
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Initialize model
model = ChatGroq(model_name="llama3-8b-8192", groq_api_key=os.getenv("GROQ_API_KEY"))

def summarize_content(html_text: str) -> str:
    soup = BeautifulSoup(html_text, "html.parser")
    text = soup.get_text()
    prompt = f"Summarize this content:\n{text}"
    return model.invoke(prompt).content

def summarize_pdf_file(file) -> str:
    content = extract_text(file.file)
    prompt = f"Summarize the following PDF content:\n{content}"
    return model.invoke(prompt).content
