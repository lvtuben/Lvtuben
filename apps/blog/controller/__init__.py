from flask import Blueprint

blog_blueprint = Blueprint('blog', __name__, url_prefix='/blog')
from . import CommentController
