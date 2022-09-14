# Bibliotecas
from datetime import date
import json
from flask import Flask
from flaskext.mysql import MySQL

# Importa variaveis de ambiente
from env_var import env_var_mysql

app = Flask(__name__)
mysql = MySQL()

# Atribui variaveis de ambiente
app.config['MYSQL_DATABASE_HOST'] = env_var_mysql['server']
app.config['MYSQL_DATABASE_PORT'] = env_var_mysql['porta']
app.config['MYSQL_DATABASE_USER'] = env_var_mysql['username']
app.config['MYSQL_DATABASE_PASSWORD'] = env_var_mysql['password']
app.config['MYSQL_DATABASE_DB'] = env_var_mysql['database']
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql.init_app(app)

class Conexao_DB():
    
    def test_conn():
        conn = mysql.connect()
        cursor = conn.cursor()              
        consulta_nome_db = '''SELECT DATABASE() as 'DB_NAME' '''
        cursor.execute(consulta_nome_db)
        colunas = [coluna[0] for coluna in cursor.description]
        resultados = []
        for linha in cursor.fetchall():
            resultados.append(dict(zip(colunas, linha)))
        json_str = json.dumps(resultados, indent=4, sort_keys=False)
        json_obj = json.loads(json_str)
        return json_obj
    

    def realizar_consulta(consulta):
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            resultado_dic = list(resultado)
            resultado_json = str(resultado_dic)
            rf = json.dumps(resultado_json)
            rf_json = json.loads(rf)
            return type(rf_json)


    def inserir_agente(nome, dt_nasc, email, celular, telefone, sexo, cpf, senha, agente):
        conn = mysql.connect()
        cursor = conn.cursor()
        timestamp = date.today()
        insert = f'''insert into {agente} (status, nome, dt_nasc, email, celular, telefone, sexo, cpf, senha, data_criacao) values('True' , '{nome}', '{dt_nasc}', '{email}', '{celular}', '{telefone}', '{sexo}', '{cpf}','{senha}', '{timestamp}')'''
        cursor.execute(insert)
        conn.commit()
        return nome + ' adicionado'

    # def selecionar_agente_cpf(cpf, agente = 'pacientes'):
    #     consulta = f'''SELECT * FROM {agente} WHERE CPF = {cpf}'''
    #     resultado = Conexao_DB.realizar_consulta(consulta)
    #     return resultado

consulta = '''select * from pacientes'''
print(Conexao_DB.realizar_consulta(consulta))

# consulta = ''' insert into pacientes (status, nome, dt_nasc, email, celular, telefone, sexo, cpf, senha, data_criacao ) values (true,'Edherzito', '01-01-1929', 'edherzito@blaaa.com.br',"1195866325", "11495464987", 'm', "000005900", "senha", curdate()) '''
# print(Conexao_DB.realizar_consulta(consulta))
# print(Conexao_DB.inserir_agente('Gabi', '01/01/1929', 'gabi@blaa.com',"1195866325", "11495464989", 'm', "0000059812", "senha", 'pacientes'))
#consulta = 'select * from pacientes'
#print(Conexao_DB.realizar_consulta(consulta))
#print(Conexao_DB.test_conn())



