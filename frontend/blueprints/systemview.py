import utils.planetgrab as pg
from flask import Blueprint, render_template

systemview = Blueprint("systemview", __name__, url_prefix="/systemview")


@systemview.route("/")
def index():
    data = pg.get_data()
    return render_template("systemview.html", data=data)


blueprint = systemview
