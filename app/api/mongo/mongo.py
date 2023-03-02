import motor.motor_asyncio
from bson.objectid import ObjectId
import json

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
car_collection = client.cars.get_collection("cars_collection")
car_collection.insert_many(json.load(open("cars_data.json")))

# helpers
def car_checker(car) -> dict:
    return {    
        "id"         : str(car["_id"]),
        "brand"      : car["brand"],
        "model"      : car["model"],
        "color"      : car["color"],
        "price"      : car["price"],
        "year"       : car["year"],
        "weight"     : car["weight"],
        "motor_type" : car["motor_type"],
        "horse_power": car["horse_power"],
    }

# CRUD

# CREATE
async def add_car(car_data: dict) -> dict:
    car = await car_collection.insert_one(car_data)
    new_car = await car_collection.find_one({"_id": car.inserted_id})
    return car_checker(new_car)

# READ ALL
async def retrieve_cars():
    cars = []
    async for car in car_collection.find():
        cars.append(car_checker(car))
    return cars

# READ ID
async def retrieve_car(id: str) -> dict:
    car = await car_collection.find_one({"_id": ObjectId(id)})
    if car:
        return car_checker(car)

# UPDATE BY ID
async def update_car(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    car = await car_collection.find_one({"_id": ObjectId(id)})
    if car:
        updated_car = await car_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_car:
            return True
        return False

# DELETE
async def delete_car(id: str):
    car = await car_collection.find_one({"_id": ObjectId(id)})
    if car:
        await car_collection.delete_one({"_id": ObjectId(id)})
        return True