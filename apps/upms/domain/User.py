# -*-coding:utf-8
from apps.base.model import db, Common


class User(Common):
    username = db.Column(db.String(100))
    password = db.Column(db.String(200))
    posts = db.relationship(
        'Post',
        backref='user',
        lazy='dynamic'
    )

    def __repr__(self):
        return "<User `{}`>".format(self.username)
