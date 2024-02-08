from enum import Enum


class ServiceType(str, Enum):
    HOTEL = "hotel"
    RESTAURANT = "restaurant"
    STORE = "store"
    TOUR = "tour"
    TRANSPORT = "transport"

    class Config:
        use_enum_values = True
