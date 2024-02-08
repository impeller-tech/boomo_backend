from fastapi import FastAPI
from sqlmodel import Session, SQLModel

from app.db import engine
from app.services.routers import router as services_router


def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI()
app.include_router(services_router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
