import datetime

from sqlmodel import Field, SQLModel


class ReservationBase(SQLModel):
    asset_id: int
    user_id: int
    start_date: datetime.datetime
    end_date: datetime.datetime

    class Config:
        arbitrary_types_allowed = True


class ReservationCreate(ReservationBase):
    pass


class ReservationRead(ReservationBase):
    id: int


class Reservation(ReservationBase, table=True):
    id: int = Field(default=None, primary_key=True)
