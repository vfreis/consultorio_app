from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .env import mysql_var

db = SQLAlchemy()
# DB_NAME = mysql_var['database']
# DB_HOST = 'mysql+pymysql://admin:123456789@meu-consultorio-app-mysql.ciofokjqok2t.us-east-1.rds.amazonaws.com:3306/consulta_app_alpha'

def create_app():

    from .models import User, Schedule
    from .views import views

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'''{mysql_var['driver']}://{mysql_var['host']}:{mysql_var['port']}/{mysql_var['database']}'''
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'{DB_HOST}'
    app.config['SECRET_KEY'] = mysql_var['secret_key']
    db.init_app(app)

    app.register_blueprint(views, url_prefix = '/')

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'view.sigin'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    try:
        db.create_all(app = app)
        print('\nDB  : OK')
        print('TBL : OK \n')
    except:
        print('\n Acessing DB or Creating Tables failed. \n')


