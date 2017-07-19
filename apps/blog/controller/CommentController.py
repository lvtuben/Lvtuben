# -*-coding:utf-8
from . import blog_blueprint


@blog_blueprint.route('/')
def index():
    return 'hello blog'
