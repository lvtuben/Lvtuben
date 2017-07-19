# -*-coding:utf-8
from . import upms_blueprint


@upms_blueprint.route('/')
def index():
    return 'hello umps'
