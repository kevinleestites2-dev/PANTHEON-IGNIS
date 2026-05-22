import asyncio
from brain.metagpt.roles.scout import Scout
from brain.metagpt.roles.scraper_engineer import ScraperEngineer
from brain.metagpt.roles.ignis import Ignis
from metagpt.software_company import SoftwareCompany
class StrikeOrchestrator:
    async def start_strike(self):
        company = SoftwareCompany()
        company.hire([Scout(), ScraperEngineer(), Ignis()])
        await company.run(n_round=3)
