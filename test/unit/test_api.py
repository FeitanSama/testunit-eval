import requests
import unittest

url = 'http://localhost:8000/'

data = {
    "brand": "TEST",
    "model": "TEST",
    "price": 99999,
    "color": "TEST",
    "year": 9999,
    "weight": "TEST",
    "motor_type": "TEST",
    "horse_power": "TEST"
}

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.car_data = data

    def test_00_add_car(self):
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        car = response.json()
        self.assertIsInstance(car, dict)
        self.assertEqual(car["data"][0]["brand"], self.car_data["brand"])
        self.assertEqual(car["data"][0]["model"], self.car_data["model"])
        self.assertEqual(car["data"][0]["price"], self.car_data["price"])
        self.assertEqual(car["data"][0]["color"], self.car_data["color"])
        self.assertEqual(car["data"][0]["year"], self.car_data["year"])
        self.assertEqual(car["data"][0]["weight"], self.car_data["weight"])
        self.assertEqual(car["data"][0]["motor_type"], self.car_data["motor_type"])
        self.assertEqual(car["data"][0]["horse_power"], self.car_data["horse_power"])
        self.assertEqual(car["message"], "car added successfully.")
    
    def test_01_update_car(self):
        self.car_data["year"] = 9998
        response = requests.get(url)
        old_car = response.json()
        for i in range(0, len(old_car["data"][0])):
            if old_car["data"][0][i]["brand"] == "TEST":
                id_car = old_car["data"][0][i]["id"]
                break
        response = requests.put(f"{url}{id_car}", json=data)
        self.assertEqual(response.status_code, 200)
        car = response.json()
        self.assertIsInstance(car, dict)
        self.assertEqual(car["data"][0], f"car with ID: {id_car} update is successful")
        self.assertEqual(car["message"], "car data updated successfully")

    def test_02_update_nonexistent_car(self):
        id_car = "63fa0d6af9f464bdf1303b88"
        response = requests.put(f"{url}{id_car}", json=data)
        self.assertEqual(response.status_code, 200)
        error = response.json()
        self.assertIsInstance(error, dict)
        self.assertEqual(error["error"], "An error occurred")
        self.assertEqual(error["code"], 404)
        self.assertEqual(error["message"], "There was an error updating the car data.")

    def test_03_retrieve_cars(self):
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        cars = response.json()
        self.assertIsInstance(cars, dict)
        self.assertGreater(len(cars), 0)
        self.assertEqual(cars["message"], "cars data retrieved successfully")
    
    def test_04_retrieve_car(self):
        response = requests.get(url)
        old_car = response.json()
        for i in range(0, len(old_car["data"][0])):
            if old_car["data"][0][i]["brand"] == "TEST":
                id_car = old_car["data"][0][i]["id"]
                break
        response = requests.get(f"{url}{id_car}")
        self.assertEqual(response.status_code, 200)
        car = response.json()
        self.assertIsInstance(car, dict)
        self.assertEqual(car["message"], "car data retrieved successfully")

    def test_05_get_nonexistent_car(self):
        id_car = "63fa0d6af9f464bdf1303b88"
        response = requests.get(f"{url}{id_car}")
        self.assertEqual(response.status_code, 200)
        error = response.json()
        self.assertIsInstance(error, dict)
        self.assertEqual(error["error"], "An error occurred")
        self.assertEqual(error["code"], 404)
        self.assertEqual(error["message"], "car doesn't exist.")

    def test_06_delete_car(self):
        response = requests.get(url)
        old_car = response.json()
        for i in range(0, len(old_car["data"][0])):
            if old_car["data"][0][i]["brand"] == "TEST":
                id_car = old_car["data"][0][i]["id"]
                break
        response = requests.delete(f"{url}{id_car}")
        self.assertEqual(response.status_code, 200)
        car = response.json()
        self.assertIsInstance(car, dict)
        self.assertEqual(car["message"], "car deleted successfully")
    
    def test_07_delete_nonexistent_car(self):
        id_car = "63fa0d6af9f464bdf1303b88"
        response = requests.delete(f"{url}{id_car}")
        self.assertEqual(response.status_code, 200)
        error = response.json()
        self.assertIsInstance(error, dict)
        self.assertEqual(error["error"], "An error occurred")
        self.assertEqual(error["code"], 404)
        self.assertEqual(error["message"], f"car with id {id_car} doesn't exist")

if __name__ == '__main__':
    unittest.main()