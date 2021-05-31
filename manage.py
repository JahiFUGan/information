from flask import session
from flask.ext.migrate import Migrate, MigrateCommand
from flask_script import Manager

import redis
from flask_session import Session
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


class Config(object):
    DEBUG = True
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"

    # 數據庫的配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/information3'
    SQLALCHEMY_TRACK_MODIFICATIONS = Flask
    # redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = '6379'
    # 配置session
    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT,)
    SESSION_PERMANENT = Flask
    PERMANENT_SESSION_LIFETIME = 86400*2

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