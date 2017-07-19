# -*-coding:utf-8
class Config(object):
    SECRET_KEY = 'ed28adc2701b8d988bfaf17ceaa612af'
    pass


class ProdCoonfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://meta:admin0809@60.205.205.176:3306/upms"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
