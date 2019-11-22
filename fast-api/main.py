from enum import Enum
from fastapi import FastAPI, Query
from pydantic import BaseModel, condecimal
from typing import List
from datetime import datetime


class Split(BaseModel):
    split_id: int
    name: str = 'TestSplit'
    description: str = 'I have no description'
    price_cents: condecimal(decimal_places=2) = 19.99
    creation_date: datetime = datetime.now()


class Box(BaseModel):
    box_id: int
    name: str
    description: str
    state: int = 0
    creation_date: datetime

    splits: List[Split]


app = FastAPI()


@app.get("/splits")
def create_split(split: Split):
    return split


@app.get("/")
def read_root():
    return {"This is": "the root"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}