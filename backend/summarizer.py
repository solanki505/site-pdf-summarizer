import os
os.environ["USER_AGENT"] = "summarizer-app/1.0"
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from tempfile import NamedTemporaryFile
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(model_name="llama3-8b-8192", groq_api_key=api_key)

prompt = PromptTemplate.from_template('''
# Analyze and summarize the following content:
{page_data}

# Provide a summary in 50 to 100 words.
''')

chain = prompt | model
MAX_CHARS = 12000

def summarize_url(url: str) -> str:
    try:
        loader = WebBaseLoader(url)
        docs = loader.load()
        text = docs[0].page_content[:MAX_CHARS]
        result = chain.invoke({"page_data": text})
        return result.content
    except Exception as e:
        return f"Error: {str(e)}"

def summarize_pdf_file(file) -> str:
    try:
        with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file.file.read())
            path = tmp.name

        loader = PyPDFLoader(path)
        docs = loader.load()
        text = " ".join([doc.page_content for doc in docs])[:MAX_CHARS]
        result = chain.invoke({"page_data": text})
        os.remove(path)
        return result.content
    except Exception as e:
        return f"Error: {str(e)}"
