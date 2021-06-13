from db_manage.sql import db
import sys
from account_manage.account_models import User

sys.path.append("..")

class Share(db.Model):
    '''
    分享
    '''
    __tablename__ = 'Share'  

    share_id = db.Column(db.Integer, primary_key=True, nullable=False)
    message = db.Column(db.String(120), nullable=False)
    liking = db.Column(db.Integer)
    name = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict
    
    def __repr__(self):
        return '<Share %r>' % (self.message)


class Comment(db.Model):
    '''
    评论
    '''
    comment_id = db.Column(db.Integer, primary_key=True, nullable=False)
    content = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)
    share_id = db.Column(db.Integer, db.ForeignKey('Share.share_id'), nullable=False)
    
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

    def __repr__(self):
        return '<Comment %r>' % (self.content)
