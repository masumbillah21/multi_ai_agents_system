from .data_agent import DataAgent
from .decision_agent import DecisionAgent
from .communication_agent import CommunicationAgent

class CoordinatorAgent:
    def __init__(self):
        self.data_agent = DataAgent()
        self.decision_agent = DecisionAgent()
        self.comm_agent = CommunicationAgent()

    async def handle_request(self, user_input: str):
        data_result = await self.data_agent.run(user_input)
        decision_result = await self.decision_agent.run(data_result["cleaned_data"])
        response = await self.comm_agent.run(decision_result)
        return response
