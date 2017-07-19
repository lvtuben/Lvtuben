# -*-coding:utf-8
from flask import render_template

from apps.base.model import db
from apps.blog.domain.Post import Post
from apps.blog.utils.SiderBarTools import sidebar_data
from apps.upms.domain.User import User
from . import upms_blueprint


@upms_blueprint.route('/user/<string:username>')
def user(username):
    user = db.session.query(User).filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = sidebar_data()
    return render_template('user.html',
                           user=user,
                           posts=posts,
                           recent=recent,
                           top_tags=top_tags)
