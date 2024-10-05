import blueprints
from flask import Flask

if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(blueprints.home)
    app.register_blueprint(blueprints.systemview)
    app.register_blueprint(blueprints.about)
    app.run(debug=True)
