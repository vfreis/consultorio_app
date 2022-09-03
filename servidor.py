# library
import os
from flask import Flask, request, jsonify, render_template, url_for
import pyodbc
# metodos
from metodos import Metodos

app = Flask(__name__)

@app.route('/')
def init():
    return render_template('index.html')

@app.route('/cadastro', methods = ['POST', 'GET',])
def cadastrarWeb():
    nome = request.form['usuario']
    dt_nasc = request.form['data_nascimento']
    email = request.form['email']
    celular = request.form['celular']
    telefone = request.form['telefone']
    sexo = request.form['sexo']
    cpf = request.form['cpf']
    novoPaciente = Metodos(nome, dt_nasc, email, celular, telefone, sexo, cpf)
    novoPaciente.inserir_paciente()
    return novoPaciente.paciente_por_cpf(cpf)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host= 'localhost', port = port)

# print(Metodos.paciente_por_cpf('0000000008'))
# print(Metodos.inserir_paciente('kenshin', '01/01/1989', 'gabidavila@bla.com.br'," 1199999999", "1100000000", 'f', "0000000010"))


