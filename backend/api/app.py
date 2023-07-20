from flask import Blueprint, Flask
from models import storage
from flask_cors import CORS
import api.v0.views as v0
from waitress import serve
from dotenv import load_dotenv
import os

load_dotenv()

app_view = Blueprint("main_app_blueprint", __name__, url_prefix="/api/")
app_view.register_blueprint(v0.app_views)

app = Flask(__name__)
app.secret_key = os.getenv("API_SECRET_KEY")
app.config["WTF_CSRF_ENABLED"] = False
app.url_map.strict_slashes = False
app.register_blueprint(app_view)
CORS(app, supports_credentials=True)


@app.teardown_appcontext
def closeDB(arg):
    """
    method to close the storage connection
    """
    storage.close()


@app.get("/status")
def app_status():
    return "Alive!", 200


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5500"
    serve(app, host=host, port=port)
