from pydantic import BaseModel, condecimal
from typing import List
from datetime import datetime
from bson import ObjectId


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise ValueError("Not a valid ObjectId")
        return str(v)


class BaseID(BaseModel):
    _id: ObjectIdStr = None


class Split(BaseID):
    name: str = 'TestSplit'
    description: str = 'I have no description'
    price_cents: condecimal(decimal_places=2) = 19.99
    creation_date: datetime = datetime.now()


class Box(BaseID):
    name: str
    description: str
    state: int = 0
    creation_date: datetime

    splits: List[Split]
