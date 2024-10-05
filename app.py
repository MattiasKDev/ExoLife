from flask import Flask

import blueprints

if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(blueprints.home)
    app.run(debug=True)
