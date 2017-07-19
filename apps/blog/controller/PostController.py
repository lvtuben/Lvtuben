# -*-coding:utf-8
import uuid

import datetime
from flask import render_template
from apps.base.model import db

from apps.blog.domain.Comment import Comment
from apps.blog.domain.Post import Post
from apps.blog.forms.CommentForm import CommentForm
from apps.blog.utils.SiderBarTools import sidebar_data
from . import blog_blueprint


@blog_blueprint.route('/')
@blog_blueprint.route('/<int:page>')
def index(page=1):
    posts = Post.query.order_by(
        Post.publish_date.desc()
    ).paginate(page, 10)
    recent, top_tags = sidebar_data()

    return render_template('blog/index.html',
                           posts=posts,
                           recent=recent,
                           top_tags=top_tags)



@blog_blueprint.route('/post/<int:post_sid>', methods=('GET', 'POST'))
def post(post_sid):
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment()
        new_comment.name = form.name.data
        new_comment.text = form.text.data
        new_comment.date = datetime.datetime.now()
        new_comment.post_sid = post_sid
        db.session.add(new_comment)
        db.session.commit()

    post = Post.query.get_or_404(post_sid)
    tags = post.tags
    comments = post.comments.order_by(Comment.date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template('blog/post/index.html',
                           post=post,
                           tags=tags,
                           comments=comments,
                           form=form,
                           recent=recent,
                           top_tags=top_tags)
