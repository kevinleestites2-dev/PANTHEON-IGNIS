import asyncio
from core.ignis.strike import IgnisStrike
from core.safla.bridge import SAFLABridge
from core.swarm.prime_swarm import PrimeSwarm

async def main():
    print("🔱 PANTHEON IGNIS v1.0: UNIFIED STRIKE ENGINE ACTIVE")
    intelligence = SAFLABridge("IgnisCore")
    strike = IgnisStrike(intensity=1.0)
    print("🔥 EXECUTING SWARM STRIKE...")
    await strike.swarm_strike(count=5)

if __name__ == "__main__":
    asyncio.run(main())
