from enum import Enum


class AssetType(str, Enum):
    ROOM = "room"
    TABLE = "table"
    PRODUCT = "product"
    VEHICLE = "vehicle"
    TICKET = "ticket"

    class Config:
        use_enum_values = True
