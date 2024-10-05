from flask import Blueprint, render_template

systemview = Blueprint("systemview", __name__, url_prefix="/systemview")


@systemview.route("/")
def index():
    return render_template("systemview.html")


blueprint = systemview
