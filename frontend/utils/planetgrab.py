import math
import os
import random

import requests
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")


def get_data():
    response = requests.get(f"{API_URL}/exohabitdata")
    return add_cords(response.json())


def get_test_data():
    response = requests.get(f"{API_URL}/test")
    return add_cords(response.json())


def add_cords(data):
    for planet in data:
        print(planet)
        planet["x"], planet["y"] = create_x_y(planet["Distance"])
    return data


# create random coords with correct distance from earth using pythagorean theorem
def create_x_y(distance):
    maxX = math.sqrt(distance)
    x = random.uniform(0, maxX)
    y = math.sqrt(distance - x**2)
    return random.choice([x, -x]), random.choice([y, -y])
