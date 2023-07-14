from flask import Flask
from models import storage
from flask_cors import CORS
from api.v0.views import app_views

app = Flask(__name__)
app.secret_key = 'd628b27b45e7fc856f78e565a20051d5b15e86203830209b38d5612841d9ee58'
app.config['WTF_CSRF_ENABLED'] = False
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app)

@app.teardown_appcontext
def closeDB(arg):
    """
    method to close the storage connection
    """
    storage.close()

if __name__ == '__main__':
    host = '0.0.0.0'
    port = '5500'
    app.run(host=host, port=port, threaded=True, debug=True)
