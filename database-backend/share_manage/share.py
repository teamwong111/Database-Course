from flask.json import dump
from account_manage.account_models import User
from share_manage.share_models import Comment, Share
from db_manage.sql import db
from sqlalchemy import and_
from flask import Blueprint, jsonify, request
import sys
import json

sys.path.append("..")

share_app = Blueprint('Share', __name__)

@share_app.route('/api/search_share', methods=['POST'])
def all_data():
    '''
    搜索分享
    '''
    data = []
    msg = ''
    if request.form['content']:
        name = request.form['content']
        shares = Share.query.filter(Share.name==name).all()
    else:
        shares = Share.query.all()
    for share in shares:
        comments = Comment.query.filter(Comment.share_id==share.share_id).all()
        payload = share.to_json()
        comment_list = []
        for comment in comments:
            comment_list.append(comment.to_json())
        data.append({'share': payload, 'comment': comment_list})

    msg = "搜索分享成功！"
    return jsonify(code=200, data=data, msg=msg)

@share_app.route('/api/single_share', methods=['POST'])
def single_share():
    '''
    查找单一分享
    '''
    data = []
    msg = ''
    share_id = request.form['share_id']
    account = request.form['account']
    user = User.query.filter(User.account == account).first()
    sports_record = Share.query.filter(and_(Share.user_id == user.user_id, Share.share_id==share_id)).first()
    data.append(sports_record.to_json())
    msg = "查找单一分享成功！"
    return jsonify(code=200, data=data, msg=msg)

@share_app.route('/api/add_share', methods=['POST'])
def add_share():
    '''
    添加运动分享
    '''
    data = []
    msg = ''
    account = request.form['account']
    user = User.query.filter(User.account == account).first()
    shares = Share.query.all()
    share = Share(share_id=len(shares)+1,
                  message=request.form['message'],
                  liking=0,
                  name=user.name,
                  user_id=user.user_id)
    db.session.add(share)
    db.session.commit()
    msg = "添加分享成功！"
    return jsonify(code=200, data=data, msg=msg)

@share_app.route('/api/del_share', methods=['GET', 'POST'])
def del_share():
    '''
    删除运动分享
    '''
    data = []
    msg = ''
    data_del_id = request.form['share_id']
    share_del = Share.query.filter(Share.share_id == data_del_id).first()
    db.session.delete(share_del)
    db.session.commit()
    msg = "删除分享成功！"
    return jsonify(code=200, data=data, msg=msg)

@share_app.route('/api/modify_share', methods=['POST'])
def modify_share():
    '''
    修改运动分享
    '''
    data = []
    msg = ''
    share_modify = Share.query.filter(Share.share_id == request.form['share_id']).first()
    if not share_modify:
        msg = "不存在的运动分享"
        return jsonify(code=150, data=data, msg=msg)
    share_modify.message = request.form['message']
    db.session.commit()
    msg = "分享修改成功"
    return jsonify(code=200, data=data, msg=msg)

@share_app.route('/api/add_liking', methods=['POST'])
def add_liking():
    '''
    点赞
    '''
    data = []
    msg = ''
    share_modify = Share.query.filter(Share.share_id == request.form['share_id']).first()
    if not share_modify:
        msg = "不存在的运动分享"
        return jsonify(code=150, data=data, msg=msg)
    share_modify.liking = share_modify.liking + 1
    db.session.commit()
    msg = "点赞成功"
    return jsonify(code=200, data=data, msg=msg)
    
@share_app.route('/api/add_comment', methods=['POST'])
def add_comment():
    '''
    评论
    '''
    data = []
    msg = ''
    share_modify = Share.query.filter(Share.share_id == request.form['share_id']).first()
    if not share_modify:
        msg = "不存在的运动分享"
        return jsonify(code=150, data=data, msg=msg)
    else:
        user = User.query.filter(User.account == request.form['account']).first()
        comments = Comment.query.all()
        comment = Comment(comment_id=len(comments)+1,
                  content=request.form['message'],
                  name=user.name,
                  user_id=user.user_id,
                  share_id=share_modify.share_id)
        db.session.add(comment)
        db.session.commit()
        msg = "评论成功"
        return jsonify(code=200, data=data, msg=msg)