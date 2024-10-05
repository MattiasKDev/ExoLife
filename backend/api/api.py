import json
import os

from flask import Blueprint

base_filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/")
def index():
    return "Hello, World!"


@api.route("/test")
def test():
    with open(f"{base_filepath}/data/sampledata.json") as f:
        data = json.load(f)
    return data
