from flask import Flask
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis


class Config(object):
    """项目配置"""
    DEBUG = True

    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information2"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Redis的配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6397


app = Flask(__name__)
# 加载配置
app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
# 初始化 redis 存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启当前项目CSRF 保护,只做服务器验证功能
CSRFProtect(app)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()
