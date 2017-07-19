# -*-coding:utf-8
from sqlalchemy import func

from apps.base.model import db
from apps.blog.domain.Post import Post, tags
from apps.blog.domain.Tag import Tag


def sidebar_data():
    recent = db.session.query(Post).order_by(
        Post.publish_date.desc()
    ).limit(5).all()

    top_tags = db.session.query(
        Tag, func.count(tags.c.post_id).label('total')
    ).join(
        tags
    ).group_by(Tag).order_by('total DESC').limit(5).all()
    return recent, top_tags
