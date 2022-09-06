#bibliotecas
import os
from flask import Flask
from views import views


app = Flask(__name__)
app.register_blueprint(views, url_prefix = '/')

# #tratativa de exceções
# class ErrCnn(Exception):
#     pass


#rota da home
# @app.route('/')
# def init():
#     return render_template('index.html')


#rota cadastrar
# @app.route('/cadastrar', methods = ['POST', 'GET'])
# def cadastrarAgente():
#     nome = request.form['nome']
#     dt_nasc = request.form['dt_nasc']
#     email = request.form['email']
#     celular = request.form['celular']
#     telefone = request.form['telefone']
#     sexo = request.form['sexo']
#     cpf = request.form['cpf']
#     senha = request.form['senha']

#     #converte, pois no banco parametro 'dt_nasc' é date; necessário?!
#     try:
#         dt_nasc_date = datetime.strptime(dt_nasc, '%d/%m/%Y').date()
#     except ValueError:
#         Abort(404)

#     return Conexao_DB.inserir_agente(nome, dt_nasc_date, email, celular, telefone, sexo, cpf, senha, agente = 'pacientes')
    

if __name__ == '__main__':
    porta = int(os.environ.get('PORT', 5002))
    app.run(host= 'localhost', port = porta, debug=True)



# print(Conexao_DB.inserir_agente('amanda', '01/01/1989', 'gabidavila@bla.com.br'," 1199999999", "1100000000", 'f', "0000000012", "senha", 'pacientes'))
# print(Conexao_DB.selecionar_paciente_cpf('0000000009'))