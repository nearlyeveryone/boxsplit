from datetime import datetime

from fastapi import FastAPI
from models import Split, Box, User
from pydantic import BaseModel

# uvicorn main:app --reload
# class Split(BaseModel):
#     split_id: int
#     name: str = 'TestSplit'
#     description: str = 'I have no description'
#     price_cents: condecimal(decimal_places=2) = 19.99
#     creation_date: datetime = datetime.now()
#
#
# class Box(BaseModel):
#     box_id: int
#     name: str
#     description: str
#     state: int = 0
#     creation_date: datetime
#
#     splits: List[Split]

app = FastAPI()


class Test(BaseModel):
    id: int = None
    name: str = "Kimi no na wa?"
    creation_date: datetime = datetime.now()


@app.get("/splits")
def create_split():
    return Split(id="asd")


@app.get("/boxes")
def create_box():
    return Box(splits=[Split(id="nest", description='I am stuck in here', name="Nest Uno"),
                       Split(id="nest2", description="Its dark in here", name="Nest Dos")])


@app.get("/user/{user_id}")
async def get_user(user_id: str):
    return User(id=user_id)


@app.get("/")
def read_root():
    return {"This is": "the root"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


'''
@app.get("/user_test")
def user_test():
    user = svc.find_user_by_email("poog@split.box")
    return user.to_json()
'''
