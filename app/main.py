from fastapi import FastAPI
from .agents.coordinator_agent import CoordinatorAgent

app = FastAPI(title="Multi-Agent AI System", version="1.0.0")

@app.post("/process")
async def process_request(user_input: str):
    coordinator = CoordinatorAgent()
    result = await coordinator.handle_request(user_input)
    return {"result": result}
