# -*-coding:utf-8
from apps.base.model import Common, db


class User(Common):
    username = db.Column(db.String(100))
    password = db.Column(db.String(200))

    # posts = db.relationship(
    #     'Post',
    #     backref='user',
    #     lazy='dynamic'
    # )

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User `{}`>".format(self.username)
