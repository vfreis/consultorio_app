#bibliotecas
from flask import (
    render_template, request, Blueprint, session, redirect, url_for
)
from methods import Conexao_DB
from datetime import datetime

from models.user import Usuario

#declara views com Blueprint
views = Blueprint(__name__, 'views')


#gestao de login
# gestao_login = LoginManager()
# gestao_login.init_app(views)

# @gestao_login.user_loader
# def carrgar_usuario(user_id):
#     return User.get(user_id)

#exceções
class Abort(Exception):
    pass

#rotas
@views.route('/')
def teste():
    return render_template('index.html')

@views.route('/home')
def home():
    return render_template('index.html')

@views.route('/cadastrar', methods = ['POST', 'GET'])
def cadastrarAgente():

    if request.method == 'POST':
        nome = request.form['nome']
        dt_nasc = request.form['dt_nasc']
        email = request.form['email']
        celular = request.form['celular']
        telefone = request.form['telefone']
        sexo = request.form['sexo']
        cpf = request.form['cpf']
        senha = request.form['senha']
        #converte, pois no banco parametro 'dt_nasc' é date; necessário?!
        try:
            dt_nasc_date = datetime.strptime(dt_nasc, '%d/%m/%Y').date()
        except ValueError:
            Abort(404)
        return Conexao_DB.inserir_agente(nome, dt_nasc_date, email, celular, telefone, sexo, cpf, senha, agente = 'pacientes')
    else:
        return render_template('cadastro.html')

@views.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST' and 'user' not in session:
        email = request.form['email']
        senha = request.form['senha']
        if email and senha and Conexao_DB.autenticar_usuario(email, senha, 'pacientes'):
            usuario = Conexao_DB.selecionar_agente_email(email)
            session['user'] = usuario['nome']
            return redirect(url_for('views.usuario'))
        else:
            return render_template('login.html')
    else:
        return redirect(url_for('views.usuario'))

@views.route('/usuario', methods = ['POST', 'GET'])
def usuario():
    if 'user' in session:
        usuario = session['user']
        return render_template('usuario.html')
    else:
        return render_template('login.html')

@views.route('/agendamento', methods = ['POST', 'GET'])
def agendamento():
    if request.method == "POST" and 'user' in session:
        paciente = session['user']
        data = request.form['data']
        hora = request.form['hora']
        local = request. form['local']
        especialidade = request.form['especialidade']
        medico = request.form['medico']
        return (Conexao_DB.agendar_consulta(paciente, data, hora, local, especialidade, medico) + '''<a class="nav-link" href="usuario"> Clique aqui para Voltar</a>''') 
    if 'user' in session:
        return render_template('agendamento.html')
    else:
        return redirect(url_for('views.login'))

@views.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
        return redirect(url_for('views.home'))
    else:
        return redirect(url_for('views.home'))
    