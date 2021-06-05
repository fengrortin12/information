from flask import Flask
from flask import session
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_session import Session
from flask_script import  Manager
from flask_migrate import Migrate, MigrateCommand


class Config(object):
    """项目配置"""
    DEBUG = True

    SECRET_KEY = 'gI8RgQt1QbmYCqdSrLKf9laEXeps6HAu5TvSmYUrsVO0tOpLRGpQEH4Cm/MiqL3'

    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information2"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Redis的配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # session 保存配置
    SESSION_TYPE = 'redis'
    # 开启session签名
    SESSION_USE_SIGNER = True
    # 制定session 保存的redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2


app = Flask(__name__)


# 加载配置
app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)
# 初始化 redis 存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启当前项目CSRF 保护,只做服务器验证功能
CSRFProtect(app)

Session(app)


@app.route('/')
def index():
    session['name'] = 'itheima'
    return 'index'


if __name__ == '__main__':
    manager.run()