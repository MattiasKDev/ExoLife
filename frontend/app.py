import blueprints
from flask import Flask, redirect

app = Flask(__name__)
app.register_blueprint(blueprints.home)
app.register_blueprint(blueprints.systemview)
app.register_blueprint(blueprints.about)


@app.errorhandler(404)
def page_not_found(e):
    return redirect("/home")


if __name__ == "__main__":
    app.run(debug=True)
