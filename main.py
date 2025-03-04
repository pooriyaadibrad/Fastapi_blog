from fastapi import FastAPI
from db.engine import engine, Base
from routing.users import router as users_router

app = FastAPI()


@app.on_event("startup")
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(users_router, prefix="/api/users")
