# -*-coding:utf-8
class Config(object):
    pass


class ProdCoonfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://meta:admin0809@60.205.205.176:3306/upms"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
