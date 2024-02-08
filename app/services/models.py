from typing import Any

from sqlmodel import JSON, Column, Field, SQLModel

from app.services.enums import ServiceType


class ServiceBase(SQLModel):
    ref: str = Field(index=True)
    name: str
    description: str
    image: str
    service_type: ServiceType
    meta: Any = Field(default={}, sa_column=Column(JSON, nullable=True))

    model_config = {
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "example": {
                "ref": "service-ref",
                "name": "Hostal Santander",
                "description": "Hostal Santander",
                "image": "https://via.placeholder.com/150",
                "service_type": "hotel",
                "meta": {
                    "address": "Calle 5 # 7-50",
                    "phone": "1234567890",
                    "email": "",
                },
            }
        },
    }


class Service(ServiceBase, table=True):
    id: int = Field(default=None, primary_key=True)


class ServiceCreate(ServiceBase):
    pass


class ServiceRead(ServiceBase):
    id: int
