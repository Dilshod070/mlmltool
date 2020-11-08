import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://dilshod070:12345@89.223.120.79:5432/flaskapp'  # <- Should work in ubuntu
    # SQLALCHEMY_DATABASE_URI = 'postgresql://dilshod070:12345@host.docker.internal:5432/flaskapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
