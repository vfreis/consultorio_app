# library
from ast import Import
import os
from flask import Flask, request, jsonify, render_template, url_for
import pyodbc
# metodos
from metodos import Metodos

app = Flask(__name__)

@app.route('/')
def init():
    return render_template('index.html')


# print(Metodos.paciente_por_cpf('0000000008'))
# print(Metodos.inserir_paciente('kenshin', '01/01/1989', 'gabidavila@bla.com.br'," 1199999999", "1100000000", 'f', "0000000010"))


