# -*-coding:utf-8
import os

from flask import Flask, redirect, url_for

from api.v1.controller import api_v1_blueprint
from apps.base.model import db
from apps.blog.controller import blog_blueprint
from apps.upms.controllers import upms_blueprint


def create_app(object_name):
    """
    oop 创建app对象
    :param object_name:app默认加载的配置
    :return:flask app对象
    """
    app = Flask(__name__, template_folder=os.path.join(os.path.pardir, 'templates'),
                static_folder=os.path.join(os.path.pardir, 'static'))
    app.config.from_object(object_name)
    db.init_app(app)

    @app.route('/')
    def index():
        return redirect(url_for('blog.index'))

    # 注册蓝图
    app.register_blueprint(upms_blueprint, url_prefix='/upms')
    app.register_blueprint(blog_blueprint, url_prefix='/blog')
    app.register_blueprint(api_v1_blueprint, url_prefix='/%s/api' % api_v1_blueprint.name)
    return app
