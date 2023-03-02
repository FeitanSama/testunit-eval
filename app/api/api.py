from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder
from api.mongo.mongo import (
    add_car,
    delete_car,
    retrieve_car,
    retrieve_cars,
    update_car,
)
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class carSchema(BaseModel):
    brand: str = Field(...)
    model: str = Field(...)
    price: int = Field(...)
    color: str = Field(...)
    year: int = Field(...)
    weight: str = Field(...)
    motor_type: str = Field(...)
    horse_power: str = Field(...)

    class Config:
        schema_extra = {
            "example":     {
                "brand": "Tesla",
                "model": "Model S",
                "price": 89900,
                "color": "red",
                "year": 2022,
                "weight": "2069-2162",
                "motor_type": "electric",
                "horse_power": "493-750"
            }
        }


class UpdatecarModel(BaseModel):
    brand: Optional[str]
    model: Optional[str]
    price: Optional[int]
    color: Optional[str]
    year : Optional[int]
    weight: Optional[str]
    motor_type: Optional[str]
    horse_power: Optional[str]

    class Config:
        schema_extra = {
            "example":     {
                "brand": "Tesla",
                "model": "Model S",
                "price": 89900,
                "color": "red",
                "year": 2022,
                "weight": "2069-2162",
                "motor_type": "electric",
                "horse_power": "493-750"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}


app = FastAPI()


@app.post("/", response_description="car data added into the database")
async def add_car_data(car: carSchema = Body(...)):
    car = jsonable_encoder(car)
    new_car = await add_car(car)
    return ResponseModel(new_car, "car added successfully.")


@app.get("/", response_description="cars retrieved")
async def get_cars():
    cars = await retrieve_cars()
    if cars:
        return ResponseModel(cars, "cars data retrieved successfully")
    return ResponseModel(cars, "Empty list returned")


@app.get("/{id}", response_description="car data retrieved")
async def get_car_data(id):
    car = await retrieve_car(id)
    if car:
        return ResponseModel(car, "car data retrieved successfully")
    return ErrorResponseModel("An error occurred", 404, "car doesn't exist.")


@app.put("/{id}")
async def update_car_data(id: str, req: UpdatecarModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_car = await update_car(id, req)
    if updated_car:
        return ResponseModel(
            "car with ID: {} update is successful".format(id),
            "car data updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the car data.",
    )


@app.delete("/{id}", response_description="car data deleted from the database")
async def delete_car_data(id: str):
    deleted_car = await delete_car(id)
    if deleted_car:
        return ResponseModel(
            "car with ID: {} removed".format(
                id), "car deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "car with id {0} doesn't exist".format(
            id)
    )  
