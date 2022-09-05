from flask import render_template, request, Blueprint
from methods import Conexao_DB
from datetime import datetime

views = Blueprint(__name__, 'views')

class Abort(Exception):
    pass

@views.route('/views')
@views.route('/')
def home():
    return render_template('cadastro.html')

@views.route('/cadastrar')
def cadastro():
    return render_template('cadastro.html')


@views.route('/cadastrar', methods = ['POST', 'GET'])
def cadastrarAgente():
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
    