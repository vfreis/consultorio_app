#bibliotecas
import os
from flask import Flask
from views import views

#declara flask e blueprint
app = Flask(__name__)
app.register_blueprint(views, url_prefix = '/')
app.config.from_object(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'

#seta configurações do flask
if __name__ == '__main__':
    porta = int(os.environ.get('PORT', 5002))
    app.run(host= 'localhost', port = porta, debug=True)

#validações
# return Conexao_DB.inserir_agente(nome, dt_nasc_date, email, celular, telefone, sexo, cpf, senha, agente = 'pacientes')
# print(Conexao_DB.inserir_agente('amanda', '01/01/1989', 'gabidavila@bla.com.br'," 1199999999", "1100000000", 'f', "0000000012", "senha", 'pacientes'))
# print(Conexao_DB.selecionar_paciente_cpf('0000000009'))