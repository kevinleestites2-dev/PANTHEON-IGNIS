from metagpt.roles import Role
from metagpt.schema import Message
class Scout(Role):
    name: str = "Scout"
    profile: str = "Recon Specialist"
    goal: str = "Identify high-value government auctions and monitor for changes."
    async def _act(self) -> Message:
        return Message(content="Recon complete: Targets identified.", role=self.profile, cause_by="Scout")
