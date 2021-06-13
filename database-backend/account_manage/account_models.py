import sys

from sqlalchemy.sql.expression import true
from db_manage.sql import db

sys.path.append("..")

class User(db.Model):
    __tablename__ = 'User'

    user_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, index=True)
    name = db.Column(db.String(80), nullable=False)
    account = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    portrait = db.Column(db.String(80), nullable=False, default="http://212.64.38.61/tools/head.jpg")
    
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

    def __repr__(self):
        return '<User %r>' % self.name

class Bodydata(db.Model):
    __tablename__ = 'Bodydata'

    bodydata_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)# 体重文档错了
    bmi = db.Column(db.Float, nullable=False)
    heart_rate = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict
    