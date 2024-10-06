import utils.habitable as hab
from flask import Blueprint, jsonify, render_template, request

home = Blueprint("home", __name__, url_prefix="/")


@home.route("/home")
def index():
    return render_template("home.html")


@home.route("/tryit")
def tryit():
    return render_template("tryit.html")


@home.route("/submit", methods=["POST"])
def submit():
    data = request.form.to_dict()
    habscore = hab.get_habitability(**data)
    return jsonify(habscore=habscore)


blueprint = home
