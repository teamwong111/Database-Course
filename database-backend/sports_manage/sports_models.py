import sys
from db_manage.sql import db

sys.path.append("..")

class Sports_record(db.Model):
    '''
    运动记录
    '''
    record_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    type = db.Column(db.String(80), nullable=False)
    time_len = db.Column(db.Float, nullable=False)
    place = db.Column(db.String(80), nullable=False)
    len = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

    def __repr__(self):
        return '<Sports_record %r>' % (self.type)


class Sports_plan(db.Model):
    '''
    运动计划
    '''
    plan_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    frequency = db.Column(db.Integer, nullable=False)
    sports_time = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)
    
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

    def __repr__(self):
        return '<Sports_plan %r>' % (self.name)


