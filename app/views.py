from flask import (Blueprint, render_template, request, redirect, url_for)
from .models import User
from . import db
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash
from .controllers import *

views = Blueprint('views', __name__)

@views.route('/home', methods = ['GET', 'POST'])
@views.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('index.html')

@views.route('/sigin', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        _email = request.form['email']
        _senha = request.form['senha']
        current_user = User.query.filter_by(email = _email).first()
        # print(f'{current_user.password} = {_senha}')
        if current_user:
            if current_user.password == _senha:
                login_user(current_user, remember = True)               
                return redirect(url_for('views.user', user = current_user))
            else:
                return 'wrong email or password'
    else:
        render_template('sigin.html')
    return render_template('sigin.html')

@views.route('/signup', methods = ['GET', 'POST'])
def signup():

    if request.method == 'GET': 
        return render_template('signup.html')
    elif request.method == 'POST':
        # _name, _address, _birthday, _email, _phone, _doc_id, _password
        nome = request.form['nome']
        dt_nasc_date = request.form['dt_nasc']
        email = request.form['email']
        celular = request.form['celular']
        endereco = request.form['endereco']
        sexo = request.form['sexo']
        cpf = request.form['cpf']
        senha = request.form['senha']
        add_user(nome, endereco, dt_nasc_date, email, celular, cpf, senha)
        return f'{nome}, adicionado! <a href="/">Clique aqui</a> para voltar'

@views.route('/user', methods = ['GET'])
def user():
    return render_template('user.html')

@views.route('/schedule', methods = ['POST', 'GET'])
def schedule():
    if request.method == 'GET' and current_user:
        return render_template('schedule.html')
    if request.method == 'POST' and current_user:
        return render_template('schedule.html')
    else:
        return render_template('sigin.html')

@views.route('/signout')
def sigout():
    logout_user()
    return(redirect(url_for('views.home')))

@views.route('my_schedule')
def my_schedule():
    return render_template('my_schedule.html', user = current_user)
# @views.route('/schedule', methods = ['GET', 'POST'], )
# def schedule():
#     return render_template('schedule.html')

# @views.route('/my_schedule', methods = ['GET', 'POST'])
# def schedule():
#     return render_template('my_schedule.html')

# @views.route('/user', methods = ['GET', 'POST'])
# def schedule():
#     return render_template('user.html')