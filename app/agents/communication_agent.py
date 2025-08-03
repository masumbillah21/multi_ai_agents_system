from .base_agent import BaseAgent
from ..services.groq_service import GroqLLM

class CommunicationAgent(BaseAgent):
    def __init__(self):
        self.llm = GroqLLM()

    async def run(self, decision: dict):
        # Instead of asking for long explanations, just extract the final answer
        prompt = f"Only give the direct final answer for: {decision['decision']}"
        result = await self.llm.ask(prompt)
        return {"message": result.strip()}
