# -*-coding:utf-8
class Config(object):
    SECRET_KEY = 'ed28adc2701b8d988bfaf17ceaa612af'
    pass


class ProdCoonfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://your name:your password@your db host:your db port/db name"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
