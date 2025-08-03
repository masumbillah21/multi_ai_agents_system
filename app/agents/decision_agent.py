from .base_agent import BaseAgent
from ..services.groq_service import GroqLLM

class DecisionAgent(BaseAgent):
    def __init__(self):
        self.llm = GroqLLM()

    async def run(self, cleaned_data: str):
        prompt = f"Based on this data, make a decision: {cleaned_data}"
        result = await self.llm.ask(prompt)
        return {"decision": result}
