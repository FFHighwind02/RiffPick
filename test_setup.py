import os
from dotenv import load_dotenv
from llama_index.llms.google_genai import GoogleGenAI

load_dotenv()

llm = GoogleGenAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

response = llm.complete("In one sentence, why is the album Paranoid by Black Sabbath significant?")
print(response)
