import os
## see https://habr.com/post/346344/
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	## see https://habr.com/post/346342/
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-it'

    ## see https://habr.com/post/346344/
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False