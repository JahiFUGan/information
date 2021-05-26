from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


class Config(object):
    DEBUG = True
    # 數據庫的配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/information3'
    SQLALCHEMY_TRACK_MODIFICATIONS = Flask
    # redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = '6379'

app = Flask(__name__)
# 配置
app.config.from_object(Config)
# 初始化數據庫
db = SQLAlchemy(app)
# 初始化redis
redis_storp = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 開啓csrf保護,只做保護
CSRFProtect(app)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)