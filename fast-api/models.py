from bson import ObjectId
from pydantic import BaseModel, condecimal
from typing import List
from datetime import datetime
import json

'''
class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise ValueError("Not a valid ObjectId")
        return str(v)
'''


class BaseID(BaseModel):
    id: str = "No ID"


class Split(BaseID):
    name: str = 'TestSplit'
    description: str = 'I have no description'
    price_dollars: condecimal(decimal_places=2) = 19.99
    creation_date: datetime = datetime.now()
    boxid: str = None
    #Need to cheese a reference to the box, cannot do circular references


class Box(BaseID):
    name: str = 'TestBox'
    description: str = 'I also have no description'
    state: int = 0
    creation_date: datetime = datetime.now()

    tags: List[str] = None
    splits: List[Split] = None


class User(BaseID):
    name: str = "I have no name"
    email: str = "jackss@rpi.edu"
    boxes: List[Box] = None #Boxes a
    splits: List[Split] = None