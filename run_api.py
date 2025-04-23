# run_api.py

from flask import Flask
from app.api import api

app = Flask(__name__)
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
