from metagpt.roles import Role
from metagpt.schema import Message
class Ignis(Role):
    name: str = "Ignis"
    profile: str = "Strike Executioner"
    goal: str = "Perform high-intensity hardware-mediated strikes on targets."
    async def _act(self) -> Message:
        return Message(content="Strike executed via Red Magic.", role=self.profile, cause_by="Ignis")
