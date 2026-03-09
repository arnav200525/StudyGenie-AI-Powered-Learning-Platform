import pdfplumber
import io
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="models/gemma-3-27b-it")

def extractpdf(file_stream):
    text = ""
    with pdfplumber.open(io.BytesIO(file_stream.read())) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
            text += "\n"
    return text.strip()