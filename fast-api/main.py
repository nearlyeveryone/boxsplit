from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel


class Shape(str, Enum):
    square = "square"
    circle = "circle"
    triangle = "triangle"
    rectangle = "triangle"
    dodecahedron = "dodecahedron"


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/shape/{shape_name}")
async def get_shape(shape_name: Shape):
    """
    - **shape_name**: What shape are you using?
    """
    if shape_name == Shape.circle:
        return {"shape_name": shape_name, "message": "I have infinite vertices!"}
    if shape_name == Shape.square:
        return {"shape_name": shape_name, "message": "I have 4 vertices."}
    if shape_name == Shape.rectangle:
        return {"shape_name": shape_name, "message": "I have 4 vertices and L E N G T H!"}
    if shape_name == Shape.triangle:
        return {"shape_name": shape_name, "message": "I have 3 vertices."}
    return {"shape_name": shape_name, "message": "Who am I, why am I here? :("}
