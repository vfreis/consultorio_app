from flask import (Blueprint, render_template, request, redirect, url_for, flash)
from .models import User, Schedule
from . import db
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash
from .controllers import *

views = Blueprint('views', __name__)

@views.route('/home', methods = ['GET', 'POST'])
@views.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('index.html', _user = current_user)

@views.route('/signin', methods = ['GET', 'POST'])
def signin():
    if request.method == 'POST':
        _email = request.form['email']
        _senha = request.form['senha']
        _user = User.query.filter_by(email = _email).first()
        print(f'{_user.password}')
        if _user:
            if (_user.password == _senha):
                flash('Logged in successfully!', category='success')
                login_user(_user, remember=True)
                return redirect(url_for('views.user'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("signin.html", _user=current_user)

@views.route('/signup', methods = ['GET', 'POST'])
def signup():

    if request.method == 'GET' and current_user.is_authenticated : 
        return redirect(url_for('views.user'))
    
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
    else:
        return render_template('signup.html', _user = current_user)

@views.route('/user', methods = ['GET', 'POST'])
@login_required
def user():
    if request.method == 'POST':
        nome = request.form['nome']
        dt_nasc_date = request.form['dt_nasc']
        email = request.form['email']
        celular = request.form['celular']
        endereco = request.form['endereco']
        sexo = request.form['sexo']
        # cpf = request.form['cpf']
        senha = request.form['senha']
        return update_user(nome, dt_nasc_date, email, celular, endereco, sexo, senha)
    else:
        return render_template('user.html', _user = current_user)


@views.route('/schedule', methods = ['POST', 'GET'])
def schedule():
    
    # return render_template('schedule.html', _user = current_user)
    # add_schedule('vinicios', '29/09/2022', 'sao paulo', 'mario', 'odonto', 1)
    # resposta = add_schedule('vinicios', '29/09/2022', 'sao paulo', 'mario', 'odonto', 1)
    # resposta = add_schedule('vinicios')

    # _patient_name, _scheduled_to, _clinic_address, _doctor, _type_of_doctor, _user_id

    # schedule_var = Schedule('current_user.name', '29/09/2022', 'sao paulo', 'mario', 'odonto', current_user.id, 1)
    # db.session.add(schedule_var)
    # resposta = db.session.commit()
    # return resposta

    if request.method == 'GET' and current_user.is_authenticated:
        return render_template('schedule.html', _user = current_user)
    
    if request.method == 'POST' and current_user.is_authenticated:
        _data = request.form['data']
        _hora = request.form['hora']
        _local = request.form['local']
        _especialidade = request.form['especialidade']
        _nome_medico = request.form['medico']
        _data_hora = f'{_data} {_hora}'

        add_schedule(current_user.name, _data, _local, _nome_medico, _especialidade, current_user.id)
        return f'consulta agendada para {current_user.name}, na clinica {_local} com {_nome_medico} no dia {_data}  as {_hora}. <a href="/">Clique aqui</a> para voltar'
        # try:
        # # add_schedule(_user, _date, _clinic, _doctor, type_of_doctor, _user_id)
        #     add_schedule(current_user.name, _data, _local, _nome_medico, _especialidade, current_user.user_id)
        # except:
        #     return '''<h1>Erro<h1><a href='user'>Voltar<a/>'''
    else:
        return redirect(url_for('views.home'))

@views.route('/signout')
def sigout():
    logout_user()
    return(redirect(url_for('views.home')))

@views.route('my_schedule')
def my_schedule():
    if request.method == 'POST' and current_user.is_authenticated:
        pass
    elif current_user.is_authenticated:
        return render_template('my_schedule.html', _user = current_user)
    else:
        return redirect(url_for('views.signin'))





@views.route('/editar')
def editar():
     
    return (delete_user(current_user.doc_id))
    # return render_template(editar, _user =current_user)


# @views.route('/medicos')
# def medicos():   
#      return (add_medicos('Thomaz', 'Mas', '001882345', 'dentsta', 'rua 12d3','wamrr@ghl.com', '1023430','0012386', '03774')) 


@views.route('/cadastro_medicos', methods = ['GET', 'POST'])
def medicos():

    if request.method == 'GET' and current_user.is_authenticated : 
        return redirect(url_for('views.medicos'))
    
    elif request.method == 'POST':
        nome = request.form['nome']
        sexo = request.form['sexo']
        crm = request.form['crm']
        especialidade = request.form['especialidade']
        endereco = request.form['endereco']
        email = request.form['email']
        celular = request.form['celular']
        cpf = request.form['cpf']
        senha = request.form['senha']
        add_medicos(nome,sexo, crm, especialidade, endereco, email, celular, cpf, senha)
        return f'{nome}, adicionado! <a href="/">Clique aqui</a> para voltar'

    else:
        return render_template('cadastro_medicos.html', _user = current_user)    
