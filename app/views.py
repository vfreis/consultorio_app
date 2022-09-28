from flask import (Blueprint, render_template, request, redirect, url_for)
from .models import User
from . import db
from flask_login import login_required, login_user
from werkzeug.security import check_password_hash
from .controllers import *

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('index.html')

@views.route('/sigin', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        _email = request.form['email']
        _senha = request.form['senha']
        current_user = User.query.filter_by(email = _email).first()
        if current_user:
            if check_password_hash(current_user.password, _senha):
                login_user(current_user, remember = True)                
                return redirect(url_for('views.schedule'))
            else:
                return 'wrong email or password'
    else:
        render_template('sigin.html')
    return render_template('sigin.html')

@views.route('/new_user', methods = ['GET', 'POST'])
def new_user():
    if request.method == 'GET': 
        return render_template('new_user.html')
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

@login_required
@views.route('/schedule', methods = ['GET', 'POST'])
def schedule():
    return render_template('schedule.html')
        