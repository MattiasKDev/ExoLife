from api.api import api
from flask import Flask

app = Flask(__name__)
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
