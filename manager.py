from flask import session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from info import app, db

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    session['name'] = 'itheima'
    return 'index'


if __name__ == '__main__':
    manager.run()
