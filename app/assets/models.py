from typing import Any

from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import JSON
from sqlmodel import Field, SQLModel

from app.assets.enums import AssetType


class AssetBase(SQLModel):
    name: str
    description: str
    asset_type: AssetType
    image: str
    service_id: int = Field(foreign_key="service.id")
    price: float
    meta: Any = Field(default={}, sa_column=Column(JSON, nullable=True))

    class Config:
        arbitrary_types_allowed = True


class AssetCreate(AssetBase):
    pass


class AssetRead(AssetBase):
    id: int
