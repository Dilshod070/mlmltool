import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DOCKERHOST = os.environ.get('DOCKERHOST') or 'localhost'
    PSQL_PASSWORD = os.environ.get('PSQL_PASSWORD') or ''
    SQLALCHEMY_DATABASE_URI = f'postgresql://dilshod070:{PSQL_PASSWORD}@{DOCKERHOST}:5432/flaskapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') or False
