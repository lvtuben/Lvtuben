# -*-coding:utf-8
from flask import Blueprint

upms_blueprint = Blueprint('upms', __name__)
from . import UserController
