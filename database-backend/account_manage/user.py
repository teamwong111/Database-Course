from account_manage.account_models import User, Bodydata
from db_manage.sql import db
from sqlalchemy import and_
from flask import Blueprint, jsonify, request
import sys
import re

sys.path.append("..")

user_app = Blueprint('User', __name__)

def valid_regist(account):
    '''
    注册检验
    '''
    user = User.query.filter(User.account == account).first()
    if user:
        return False
    else:
        return True


@user_app.route('/api/regist', methods=['GET', 'POST'])
def regist():
    '''
    注册：后端接收前端注册信息，进行数据合法性判断，并返回错误信息
    '''
    data = []
    msg = ''
    if len(request.form['name']) == 0 or len(request.form['name']) > 30:
        msg = '用户名长度必须在1-30个字符内'
        return jsonify(code=100, data=data, msg=msg)  # code = 100 : danger
    elif len(request.form['password1']) < 6 or len(request.form['password1']) > 30:
        msg = '密码长度必须在6-30个字符内'
        return jsonify(code=100, data=data, msg=msg)
    elif not re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}(\.edu)?\.[com,cn,net]{1,3}$', request.form['account']):
        msg = '账户(邮箱)格式不正确'
        return jsonify(code=100, data=data, msg=msg)
    elif request.form['password1'] != request.form['password2']:
        msg = '两次密码不相同！'
        return jsonify(code=100, data=data, msg=msg)
    elif not valid_regist(request.form['account']):
        msg = '该邮箱已被注册！'
        return jsonify(code=100, data=data, msg=msg)
    else:
        users = User.query.all()
        user = User(user_id=len(users) + 1,
                    name=request.form['name'],
                    account=request.form['account'],
                    password=request.form['password1']
                    )
        db.session.add(user)
        db.session.commit()
        msg = "注册成功！"
        return jsonify(code=200, data=data, msg=msg)

@user_app.route('/api/login', methods=['POST'])
def login():
    '''
    登录：检验账号密码是否匹配
    '''
    data = []
    msg = ''
    account = request.form['account']
    password = request.form['password']
    user = User.query.filter(and_(User.account == account, User.password == password)).first()
    if user:
        msg = "成功登录！"
        data.append(user.to_json())
        return jsonify(code=200, data=data, msg=msg)
    else:
        msg = '错误的用户名或密码！'
        return jsonify(code=100, data=data, msg=msg)

@user_app.route('/api/modify_password', methods=['POST'])
def modify_password():
    '''
    修改密码：后端接收前端的数据，并进行数据合法性检验
    '''
    data = []
    msg = ''
    account = request.form['account']
    user = User.query.filter(User.account == account).first()
    if user.password != request.form['password1']:
        msg = '原密码错误'
        return jsonify(code=150, data=data, msg=msg)
    elif len(request.form['password2']) < 6 or len(request.form['password2']) > 30:
        msg = '密码长度必须在6-30个字符内'
        return jsonify(code=150, data=data, msg=msg)
    elif request.form['password2'] != request.form['password3']:
        msg = '两次密码输入不相同！'
        return jsonify(code=150, data=data, msg=msg)
    else:
        user.password = request.form['password2']
        db.session.commit()
        msg = "密码修改成功"
        return jsonify(code=200, data=data, msg=msg)

@user_app.route('/api/get_info', methods=['POST'])
def get_info():
    '''
    获取个人信息
    '''
    data = []
    msg = ''
    account = request.form['account']
    user = User.query.filter(User.account == account).first()
    body_datas = Bodydata.query.filter(Bodydata.user_id == user.user_id).all()
    if user:
        data.append(user.to_json())
    if body_datas and body_datas[-1]:
        data.append(body_datas[-1].to_json())
    msg = "获取个人信息成功"
    return jsonify(code=200, data=data, msg=msg)
