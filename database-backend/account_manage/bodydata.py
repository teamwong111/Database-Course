from account_manage.account_models import User, Bodydata
from db_manage.sql import db
from sqlalchemy import and_
from flask import request, jsonify, Blueprint
import sys
sys.path.append("..")

bodydata_app = Blueprint('Bodydata', __name__)

@bodydata_app.route('/api/single_bodydata', methods=['POST'])
def single_bodydata():
    '''
    查找单一健康数据
    '''
    data = []
    msg = ''
    bodydata_id = request.form['bodydata_id']
    account = request.form['account']
    user = User.query.filter(User.account == account).first()
    body_data = Bodydata.query.filter(and_(Bodydata.user_id == user.user_id, Bodydata.bodydata_id==bodydata_id)).first()
    data.append(body_data.to_json())
    msg = "查找单一健康数据成功！"
    return jsonify(code=200, data=data, msg=msg)

@bodydata_app.route('/api/all_bodydata', methods=['POST'])
def all_bodydata():
    '''
    查看健康数据
    '''
    data = []
    msg = ''
    account = request.form['account']
    user = User.query.filter(User.account == account).first()
    body_datas = Bodydata.query.filter(Bodydata.user_id == user.user_id).all()
    for body_data in body_datas:
        data.append(body_data.to_json())
    msg = "查看健康数据成功！"
    return jsonify(code=200, data=data, msg=msg)

@bodydata_app.route('/api/add_bodydata', methods=['POST'])
def add_bodydata():
    '''
    添加健康数据
    '''
    data = []
    msg = ''
    account = request.form['account']
    user = User.query.filter(User.account == account).first()
    body_datas = Bodydata.query.all()
    body_data = Bodydata(bodydata_id=len(body_datas)+1,
                         height=request.form['height'],
                         weight=request.form['weight'],
                         bmi=request.form['bmi'],
                         heart_rate=request.form['heart_rate'],
                         user_id=user.user_id)
    db.session.add(body_data)
    db.session.commit()
    data.append(body_data.to_json())
    msg = "添加健康数据成功！"
    return jsonify(code=200, data=data, msg=msg)

@bodydata_app.route('/api/del_bodydata', methods=['POST'])
def del_bodydata():
    '''
    删除健康数据
    '''
    data = []
    msg = ''
    data_del_id = request.form['bodydata_id']
    data_del = Bodydata.query.filter(Bodydata.bodydata_id == data_del_id).first()
    db.session.delete(data_del)
    db.session.commit()
    msg = "删除健康数据成功！"
    return jsonify(code=200, data=data, msg=msg)

@bodydata_app.route('/api/modify_bodydata', methods=['POST'])
def modify_bodydata():
    '''
    修改健康数据
    '''
    data = []
    msg = ''
    data_modify = Bodydata.query.filter(Bodydata.bodydata_id == request.form['bodydata_id']).first()
    if not data_modify:
        msg = "不存在的健康数据"
        return jsonify(code=150, data=data, msg=msg)
    data_modify.height = request.form['height']
    data_modify.weight = request.form['weight']
    data_modify.bmi = request.form['bmi']
    data_modify.heart_rate = request.form['heart_rate']
    db.session.commit()
    data.append(data_modify.to_json())
    msg = "健康数据修改成功"
    return jsonify(code=200, data=data, msg=msg)
