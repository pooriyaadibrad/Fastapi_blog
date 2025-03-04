from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

engine = create_async_engine('sqlite+aiosqlite:///fastapi.db')
Session = async_sessionmaker(bind=engine)


class Base(DeclarativeBase, MappedAsDataclass):
    pass


async def get_session():
    session = Session()
    try:
        yield session
    finally:
        await session.close()
