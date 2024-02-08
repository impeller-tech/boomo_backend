from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlmodel import Session, select

from app.db import get_session
from app.services.models import ServiceCreate, ServiceRead

from .models import Service

router = APIRouter()


@router.post("/services/", response_model=ServiceRead)
def create_service(*, session: Session = Depends(get_session), service: ServiceCreate):
    db_asset = Service.model_validate(service)
    session.add(db_asset)
    session.commit()
    session.refresh(db_asset)
    return db_asset


@router.get("/services/", response_model=List[ServiceRead])
def read_services(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100),
):
    heroes = session.exec(select(Service).offset(offset).limit(limit)).all()
    return heroes
