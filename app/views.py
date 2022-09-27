from flask import (Flask, Blueprint, render_template, request)
from .controllers import *

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('base.html')

@views.route('/login', methods = ['GET', 'POST'])
def login():
    return '<h1>Login Page<h1>'

@views.route('/new_user', methods = ['GET', 'POST'])
def new_user():
    try:
        add_user('vinicios', 'rua 123', '01/01/2021', 'teste@gmail6', '11993408348', '22972425819', '123456')
    except:
        return 'add_user not posible'
    return 'user added'