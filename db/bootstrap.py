from sqlalchemy.ext.asyncio import AsyncEngine
from db import Base  # Base = declarative_base() bo'lgan joy
# yoki sende Base qayerda bo'lsa o'shani import qil

async def create_tables(engine: AsyncEngine) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
