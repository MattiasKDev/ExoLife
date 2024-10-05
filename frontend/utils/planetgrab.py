import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")


def get_data():
    response = requests.get(API_URL)
    return response.text


print(get_data())
