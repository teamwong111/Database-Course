from account_manage.account_models import User
from sports_manage.sports_models import Sports_plan
from db_manage.sql import db
from sqlalchemy import and_
from flask import Blueprint, jsonify, request
import sys

sys.path.append("..")

plan_app = Blueprint('plan', __name__)

@plan_app.route('/api/single_plan', methods=['POST'])
def single_plan():
    '''
    查看单一运动计划
    '''
    data = []
    msg = ''
    plan_id = request.form['plan_id']
    account = request.form['account']
    user = User.query.filter(User.account == account).first()
    sports_plan = Sports_plan.query.filter(and_(Sports_plan.user_id == user.user_id, Sports_plan.plan_id==plan_id)).first()
    data.append(sports_plan.to_json())
    msg = "查找单一计划成功！"
    return jsonify(code=200, data=data, msg=msg)

@plan_app.route('/api/add_plan', methods=['POST'])
def add_plan():
    '''
    添加运动计划
    '''
    data = []
    msg = ''
    account = request.form['account']
    user = User.query.filter(User.account == account).first()
    sports_plans = Sports_plan.query.all()
    sports_plan = Sports_plan(plan_id=len(sports_plans)+1,
                              name=request.form['name'],
                              frequency=request.form['frequency'],
                              sports_time=request.form['sports_time'],
                              user_id=user.user_id)
    db.session.add(sports_plan)
    db.session.commit()
    data.append(sports_plan.to_json())
    msg = "添加计划成功！"
    return jsonify(code=200, data=data, msg=msg)

@plan_app.route('/api/del_plan', methods=['POST'])
def del_plan():
    '''
    删除运动计划
    '''
    data = []
    msg = ''
    plan_del_id = request.form['plan_id']
    plan_del = Sports_plan.query.filter(Sports_plan.plan_id == plan_del_id).first()
    db.session.delete(plan_del)
    db.session.commit()
    msg = "删除计划成功！"
    return jsonify(code=200, data=data, msg=msg)

@plan_app.route('/api/modify_plan', methods=['POST'])
def modify_plan():
    '''
    修改运动计划
    '''
    data = []
    msg = ''
    plan_modify = Sports_plan.query.filter(Sports_plan.plan_id == request.form['plan_id']).first()
    if not plan_modify:
        msg = "不存在的运动计划"
        return jsonify(code=150, data=data, msg=msg)
    plan_modify.name = request.form['name']
    plan_modify.frequency = request.form['frequency']
    plan_modify.sports_time = request.form['sports_time']
    db.session.commit()
    data.append(plan_modify.to_json())
    msg = "计划修改成功"
    return jsonify(code=200, data=data, msg=msg)

@plan_app.route('/api/search_plan', methods=['POST'])
def search_plan():
    '''
    搜索运动计划
    '''
    data = []
    msg = ''
    account = request.form['account']
    user = User.query.filter(User.account == account).first()
    if request.form['content']:
        name = request.form['content']
        sports_records = Sports_plan.query.filter(and_(Sports_plan.user_id == user.user_id, Sports_plan.name==name)).all()
    else:
        sports_records = Sports_plan.query.filter(Sports_plan.user_id == user.user_id).all()
    for sports_record in sports_records:
        data.append(sports_record.to_json())
    msg = "搜索记录成功"
    return jsonify(code=200, data=data, msg=msg)
    