from flask import Flask
from flask_cors import CORS

from account_manage.account_models import User
import config.config as config
from db_manage.sql import db
from account_manage.user import user_app
from account_manage.bodydata import bodydata_app
from share_manage.share import share_app
from sports_manage.record import record_app
from sports_manage.plan import plan_app

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config.from_object(config.Config)
db.init_app(app)

@app.before_first_request
def create_db():
    db.create_all()

# 注册蓝图
app.register_blueprint(user_app)
app.register_blueprint(bodydata_app)
app.register_blueprint(share_app)
app.register_blueprint(record_app)
app.register_blueprint(plan_app)

if __name__ == '__main__':
    app.run(debug=True)