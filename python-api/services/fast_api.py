import services.data_service as svc
from fastapi import FastAPI, Query
from services.models import Box, Split
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Idiot"}


@app.get("/yeet/{item_id}/{q}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/penis")
def penis():
    user = svc.find_user_by_email("poog@split.box")
    return user.to_json()





app = FastAPI()


@app.get("/splits")
def create_split(split: Split):
    return split
