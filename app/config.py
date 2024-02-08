from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = Field(
        validation_alias="database_url", default="sqlite:///./sql_app.db"
    )


settings = Settings()
