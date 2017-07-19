# -*-coding:utf-8
from flask import render_template

from apps.blog.domain.Post import Post
from apps.blog.domain.Tag import Tag
from apps.blog.utils.SiderBarTools import sidebar_data
from . import blog_blueprint


@blog_blueprint.route('/tag/<string:tag_name>')
def tag(tag_name):
    tag = Tag.query.filter_by(name=tag_name).first_or_404()
    posts = tag.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template('tag.html',
                           tag=tag,
                           posts=posts,
                           recent=recent,
                           top_tags=top_tags)
