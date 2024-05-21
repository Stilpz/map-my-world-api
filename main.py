from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, timedelta
import random

app = FastAPI()

# Base de datos temporal para almacenar ubicaciones, categorías y revisiones
database = {
    "locations": [],
    "categories": [],
    "location_category_reviews": []
}

class Location(BaseModel):
    #id: int
    longitude: float
    latitude: float
    name: str
    category: str
    calification: Optional[int]

class Category(BaseModel):
    name: str

class LocationCategoryReview(BaseModel):
    location_name: str
    category_name: str
    last_reviewed: datetime=datetime.now()
    
#Rutas para agregar nuevas ubicaciones y categorías
@app.post("/locations/", response_model=Location)
def insert_location(location: Location):
    database["locations"].append(location)
    # return {"message" : f"Location {location.name} inserted"}
    return location

@app.post("/categories/", response_model=Category)
# @app.post("/categories")
def insert_category(category: Category):
    database["categories"].append(category)
    return category


# Función para obtener combinaciones de ubicación-categoría no revisadas en los últimos 30 días
def get_unreviewed_locations_categories():
    today = datetime.now()
    thirty_days_ago = today - timedelta(days=30)
    unreviewed = []
    for loc in database["locations"]:
        for cat in database["categories"]:
            if not any(review.location_name == loc.name and review.category_name == cat.name and review.last_reviewed > thirty_days_ago for review in database["location_category_reviews"]):
                unreviewed.append({"location": loc.name, "category": cat.name})
    return unreviewed

# Ruta para obtener recomendaciones de exploración
@app.get("/exploration_recommendations/", response_model=List[dict])
def get_exploration_recommendations():
    unreviewed_locations_categories = get_unreviewed_locations_categories()
    random.shuffle(unreviewed_locations_categories)
    return unreviewed_locations_categories[:10]

# Ruta para marcar una combinación de ubicación-categoría como revisada
@app.put("/location_category_review/{location_name}/{category_name}/")
def mark_location_category_reviewed(location_name: str, category_name: str):
    for review in database["location_category_reviews"]:
        if review.location_name == location_name and review.category_name == category_name:
            review.last_reviewed = datetime.now()
            return {"message": f"Review for {location_name} in category {category_name} marked as reviewed."}
    raise HTTPException(status_code=404, detail="Location-category combination not found")

# Documentación del API
@app.get("/", include_in_schema=False)
async def read_root():
    return {"message": "Welcome to Map My World API. Please refer to the documentation at /docs."}
