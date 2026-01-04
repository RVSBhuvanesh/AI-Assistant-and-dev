import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text
