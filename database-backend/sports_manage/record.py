from account_manage.account_models import User, Bodydata
from sports_manage.sports_models import Sports_record
from db_manage.sql import db
from sqlalchemy import and_
from flask import Blueprint, jsonify, request
import sys

sys.path.append("..")

record_app = Blueprint('record', __name__)

@record_app.route('/api/single_record', methods=['POST'])
def single_plan():
    '''
    查找单一运动记录
    '''
    data = []
    msg = ''
    record_id = request.form['record_id']
    account = request.form['account']
    user = User.query.filter(User.account == account).first()
    sports_record = Sports_record.query.filter(and_(Sports_record.user_id == user.user_id, Sports_record.record_id==record_id)).first()
    data.append(sports_record.to_json())
    msg = "查找单一记录成功！"
    return jsonify(code=200, data=data, msg=msg)

@record_app.route('/api/add_record', methods=['POST'])
def add_record():
    '''
    添加运动记录
    '''
    data = []
    msg = ''
    account = request.form['account']
    user = User.query.filter(User.account == account).first()
    sports_records = Sports_record.query.all()
    sports_record = Sports_record(record_id=len(sports_records) + 1,
                                  type=request.form['type'],
                                  time_len=request.form['time_len'],
                                  place=request.form['place'],
                                  len=request.form['len'],
                                  user_id=user.user_id)
    db.session.add(sports_record)
    db.session.commit()
    data.append(sports_record.to_json())
    msg = "添加记录成功！"
    return jsonify(code=200, data=data, msg=msg)

@record_app.route('/api/del_record', methods=['POST'])
def del_record():
    '''
    删除运动记录
    '''
    data = []
    msg = ''
    record_del_id = request.form['record_id']
    record_del = Sports_record.query.filter(Sports_record.record_id == record_del_id).first()
    db.session.delete(record_del)
    db.session.commit()
    msg = "删除记录成功！"
    return jsonify(code=200, data=data, msg=msg)

@record_app.route('/api/modify_record', methods=['POST'])
def modify_prod():
    '''
    修改运动记录
    '''
    data = []
    msg = ''
    record_modify = Sports_record.query.filter(Sports_record.record_id == request.form['record_id']).first()
    if not record_modify:
        msg = "不存在的运动记录"
        return jsonify(code=150, data=data, msg=msg)  
    record_modify.type = request.form['type']
    record_modify.time_len = request.form['time_len']
    record_modify.place = request.form['place']
    record_modify.len = request.form['len']
    db.session.commit()
    data.append(record_modify.to_json())
    msg = "记录修改成功"
    return jsonify(code=200, data=data, msg=msg)
    
@record_app.route('/api/search_record', methods=['POST'])
def search_record():
    '''
    搜索运动记录
    '''
    data = []
    msg = ''
    account = request.form['account']
    user = User.query.filter(User.account == account).first()
    if request.form['content']:
        type = request.form['content']
        sports_records = Sports_record.query.filter(and_(Sports_record.user_id == user.user_id, Sports_record.type==type)).all()
    else:
        sports_records = Sports_record.query.filter(Sports_record.user_id == user.user_id).all()
    for sports_record in sports_records:
        data.append(sports_record.to_json())
    msg = "搜索记录成功"
    return jsonify(code=200, data=data, msg=msg)

@record_app.route('/api/data_stat', methods=['POST'])
def data_stat():
    '''
    数据统计
    '''
    data = []
    times = ['时间']
    msg = ''
    account = request.form['account']
    user = User.query.filter(User.account == account).first()
    sports_records = Sports_record.query.filter(Sports_record.user_id == user.user_id).all()
    bodydatas = Bodydata.query.filter(Bodydata.user_id == user.user_id).all()
    time_lens, lens, bmis, heart_rates = [], [], [], []
    num = 1
    for sports_record in sports_records:
        times.append(str(num))
        num += 1
        time_lens.append(sports_record.time_len)
        lens.append(sports_record.len)
    for bodydata in bodydatas:
        bmis.append(bodydata.bmi / 2)
        heart_rates.append(bodydata.heart_rate / 10)
    data.append(times)
    time_lens.append("运动时长")
    lens.append("运动距离")
    bmis.append('BMI/2')
    heart_rates.append("心率/10")
    time_lens.reverse()
    lens.reverse()
    bmis.reverse()
    heart_rates.reverse()
    data.append(time_lens)
    data.append(lens)
    data.append(bmis)
    data.append(heart_rates)
    msg = "数据统计成功"
    return jsonify(code=200, data=data, msg=msg)
