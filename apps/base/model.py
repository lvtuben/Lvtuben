# -*-coding:utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Common(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    status = db.Column(db.Integer(), default=1)
    create_time = db.Column(db.DateTime(), default=db.func.now())
    update_time = db.Column(db.DateTime(), default=db.func.now(), server_onupdate=db.func.now())
