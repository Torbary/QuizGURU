from flask import Flask
from models import storage
from flask_cors import CORS
from api.v0.views import app_views
from waitress import serve
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("API_SECRET_KEY")
app.config["WTF_CSRF_ENABLED"] = False
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app)


@app.teardown_appcontext
def closeDB(arg):
    """
    method to close the storage connection
    """
    storage.close()


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5500"
    serve(app, host=host, port=port)
