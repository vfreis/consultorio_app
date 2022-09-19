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
            resultados =[]
            colunas = [coluna[0] for coluna in cursor.description]
            for linha in cursor.fetchall():
                resultados.append(dict(zip(colunas, linha)))
            return resultados
            
    def inserir_agente(nome, dt_nasc, email, celular, telefone, sexo, cpf, senha, agente = 'pacientes'):
        conn = mysql.connect()
        cursor = conn.cursor()
        timestamp = date.today()
        insert = f'''insert into {agente} (status, nome, dt_nasc, email, celular, telefone, sexo, cpf, senha, data_criacao) values('True' , '{nome}', '{dt_nasc}', '{email}', '{celular}', '{telefone}', '{sexo}', '{cpf}','{senha}', '{timestamp}')'''
        cursor.execute(insert)
        conn.commit()
        return Conexao_DB.selecionar_agente_cpf(cpf, agente)[0]['nome'] + ' adicionado'

    def selecionar_agente_cpf(cpf, agente = 'pacientes'):
        consulta = f'''SELECT * FROM {agente} WHERE CPF = {cpf}'''
        resultado = Conexao_DB.realizar_consulta(consulta)
        return resultado


    #NECESSITA VALIDAR \/

    def selecionar_agente_email(email, agente = 'pacientes'):
        consulta = f'''SELECT * FROM {agente} WHERE email = '{email}' '''
        resultado = Conexao_DB.realizar_consulta(consulta)
        return resultado[0]

    def selecionar_todos_agentes(agente):
        consulta = f'''SELECT * FROM {agente}'''
        Conexao_DB.realizar_consulta(consulta)

    def autenticar_usuario(email, senha, agente = 'pacientes'):
        consulta = f'''SELECT email, senha FROM {agente} WHERE email = '{email}' AND senha = '{senha}' '''
        resposta = Conexao_DB.realizar_consulta(consulta)
        if resposta and email == resposta[0]['email'] and senha == resposta[0]['senha']:
            return True
        else:
            return False

    def agendar_consulta(paciente, cpf, data, hora, local, especialidade, medico):
        insert = f'''INSERT INTO agendamentos (status, paciente, cpf_paciente, data_consulta, hora_consulta, consultorio, medico, especialidade) values ('True','{paciente}', '{cpf}', '{data}', '{hora}', '{local}', '{especialidade}', '{medico}') '''
        conn = mysql.connect()
        cursor = conn.cursor()
        # return f'Consulta agendadada para: {paciente}, em {data} ás {hora}, com Dr. {medico} para {especialidade}'        
        try:
            cursor.execute(insert)
            conn.commit()
            return f'Consulta agendadada para: {paciente}, em {data} ás {hora}, com Dr. {medico} para {especialidade}'
        except:
            return 'N/D'
    
    def meus_agendamentos(cpf):
        consulta = f'''SELECT paciente, data_consulta as Dia, left(hora_consulta, 5) as Horário, especialidade as Especialidade, medico as Medico, consultorio as Local from agendamentos where cpf_paciente = {cpf} order by data_consulta asc '''
        return (Conexao_DB.realizar_consulta(consulta))





# TESTE
# consulta = '''select * from pacientes'''
# print(Conexao_DB.realizar_consulta(consulta))
# consulta = ''' insert into pacientes (status, nome, dt_nasc, email, celular, telefone, sexo, cpf, senha, data_criacao ) values (true,'Edherzito', '01-01-1929', 'edherzito@blaaa.com.br',"1195866325", "11495464987", 'm', "000005900", "senha", curdate()) '''
# print(Conexao_DB.realizar_consulta(consulta))
# print(Conexao_DB.inserir_agente('Teste', '01/01/1929', 'teste',"1195866325", "11495464989", 'm', "11111111111", "senha", 'pacientes'))
#consulta = 'select * from pacientes'
#print(Conexao_DB.realizar_consulta(consulta))
#print(Conexao_DB.test_conn())



