from langchain_groq import ChatGroq
from ..config import GROQ_API_KEY

class GroqLLM:
    def __init__(self):
        if not GROQ_API_KEY:
            raise ValueError("Missing GROQ_API_KEY in environment variables or .env file")
        
        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=GROQ_API_KEY
        )

    async def ask(self, prompt: str):
        return self.llm.predict(prompt)
