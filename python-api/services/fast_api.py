import services.data_service as svc
from fastapi import FastAPI, Query
from services.models import Box, Split
app = FastAPI()

#uvicorn main:app --reload

@app.get("/")
def read_root():
    return {"Hello": "Idiot"}


@app.get("/yeet/{item_id}/{q}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/user_test")
def user_test():
    user = svc.find_user_by_email("poog@split.box")
    print(user.to_json())
    return user.to_json()

@app.get("/splits")
def create_split(split: Split):
    return split
