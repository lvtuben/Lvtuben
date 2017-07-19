import os

from apps import create_app

if __name__ == '__main__':
    env = os.environ.get('ENV', 'dev')
    app = create_app('config.%sConfig' % env.capitalize())
    app.run()
