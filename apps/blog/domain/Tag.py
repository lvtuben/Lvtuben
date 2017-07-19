# -*-coding:utf-8
from apps.base.model import db, Common


class Tag(Common):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return "<Tag `{}`>".format(self.name)
