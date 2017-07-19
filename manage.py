# -*-coding:utf-8
import os

from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager, Server

from apps import create_app, db
from apps.blog.domain.Comment import Comment
from apps.blog.domain.Post import Post
from apps.blog.domain.Tag import Tag
from apps.upms.domain.User import User

env = os.environ.get('ENV', 'dev')
app = create_app('config.%sConfig' % env.capitalize())
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("server", Server())
manager.add_command("db", MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, Server=Server, User=User, Post=Post, Tag=Tag, Comment=Comment)


if __name__ == '__main__':
    manager.run()
