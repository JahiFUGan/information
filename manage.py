from flask import session
from flask.ext.migrate import Migrate, MigrateCommand
from flask_script import Manager

import redis
from flask_session import Session
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import Config



app = Flask(__name__)
# 配置
app.config.from_object(Config)
# 初始化數據庫
db = SQLAlchemy(app)
# 初始化redis
redis_storp = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 開啓csrf保護,只做保護
CSRFProtect(app)
# 开启session
Session(app)
# 配置manager
manager = Manager(app)
# 数据库迁移
Migrate(app,db)
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    session['name'] = 'itheima'
    return 'index'


if __name__ == '__main__':
    manager.run()