from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Location(BaseModel):
    id: int
    longitude: float
    latitude: float
    name: str
    category: str
    calification: Optional[str]

@app.get("/")
def index():
    return {"message" : "Bienvenidos al API Map My World'"}

@app.get("/locations/{id}")
def show_location(id: int):
    return {"data" : id}

@app.post("/locations")
def insert_location(location: Location):
    return {"message" : f"Location {location:name} inserted"}