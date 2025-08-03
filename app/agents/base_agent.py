from abc import ABC, abstractmethod

class BaseAgent(ABC):
    @abstractmethod
    async def run(self, **kwargs):
        pass
