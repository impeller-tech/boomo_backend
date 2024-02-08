from sqlmodel import Session, SQLModel, create_engine

from .config import settings

connect_args = {"check_same_thread": False}

if settings.db_url.startswith("postgres"):
    connect_args = {}

engine = create_engine(
    settings.db_url,
)


def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)


def get_session():
    with Session(engine) as session:
        yield session
