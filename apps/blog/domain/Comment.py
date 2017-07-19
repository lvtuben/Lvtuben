# -*-coding:utf-8
from apps.base.model import db, Common


class Comment(Common):
    name = db.Column(db.String(200))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))

    def __repr__(self):
        return "<Comment `{}`>".format(self.text[:15])
