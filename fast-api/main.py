from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel, condecimal
from typing import List
import datetime


class Split(BaseModel):
    split_id: int
    name: str
    description: str
    price_cents: condecimal(decimal_places=2)
    creation_date: datetime


class Box(BaseModel):
    box_id: int
    name: str
    description: str
    state: int = 0
    creation_date: datetime

    splits: List[Split]


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}





