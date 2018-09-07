# -*-coding:utf-8
class Config(object):
    SECRET_KEY = 'ed28adc2701b8d988bfaf17ceaa612af'
    pass


class ProdCoonfig(Config):
    pass


class DevConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@10.0.3.16:3306/upms"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
