from flask import Blueprint

api_v1_blueprint = Blueprint('APIv1', __name__)
from . import UserController
