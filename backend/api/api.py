import json
import os

import functions.algorithm as alg
from flask import Blueprint, jsonify, request

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


@api.route("/exohabitdata")
def exohabitdata():
    with open(f"{base_filepath}/data/potential_planets.json") as f:
        data = json.load(f)
    return data


@api.route("/habitability", methods=["POST"])
def habitability():
    input_data = request.get_json()
    if not input_data:
        return jsonify({"error": "Invalid input"}), 400

    try:
        for key, value in input_data.items():
            if key != "spectral_type":
                input_data[key] = float(value)
        habitability_score = alg.calc_habitability_prob(**input_data)
        return jsonify({"habitability_score": habitability_score})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
