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

@app.route('/cadastro', methods = ['POST', 'GET'])
def cadastrarWeb():
    valorNome = request.form['usuario']
    valorDataNasc = request.form['data_nascimento']
    valorEmail = request.form['email']
    valorCelular = request.form['celular']
    valorTelefone = request.form['telefone']
    valorSexo = request.form['sexo']
    valorCPF = request.form['cpf']
    novoPaciente = Metodos()
    novoPaciente.inserir_paciente(valorNome, valorDataNasc, valorEmail, valorCelular, valorTelefone, valorSexo, valorCPF)
    return novoPaciente.paciente_por_cpf(valorCPF)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host= 'localhost', port = port)

# print(Metodos.paciente_por_cpf('0000000008'))
# print(Metodos.inserir_paciente('kenshin', '01/01/1989', 'gabidavila@bla.com.br'," 1199999999", "1100000000", 'f', "0000000010"))


