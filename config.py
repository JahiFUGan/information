import redis
from flask import Flask


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