from .base_agent import BaseAgent
from ..services.groq_service import GroqLLM

class DataAgent(BaseAgent):
    def __init__(self):
        self.llm = GroqLLM()

    async def run(self, query: str):
        prompt = f"Extract and clean relevant data from: {query}"
        result = await self.llm.ask(prompt)
        return {"cleaned_data": result}
