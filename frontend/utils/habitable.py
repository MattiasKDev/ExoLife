import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")


def get_habitability(**kwargs):
    try:
        response = requests.post(f"{API_URL}/habitability", json=kwargs)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
