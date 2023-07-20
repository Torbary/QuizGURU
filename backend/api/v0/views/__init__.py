from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v0/")
from .quiz import *
from .user import *
from .score import *
