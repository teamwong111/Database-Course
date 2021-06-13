import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = 'abcdefggknmlgb'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True