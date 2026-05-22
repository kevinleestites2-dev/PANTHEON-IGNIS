from metagpt.roles import Role
from metagpt.schema import Message
class ScraperEngineer(Role):
    name: str = "ScraperEngineer"
    profile: str = "Bypass Engineer"
    goal: str = "Generate code to bypass 403 blocks and extract auction data."
    async def _act(self) -> Message:
        return Message(content="Scraper logic generated.", role=self.profile, cause_by="ScraperEngineer")
