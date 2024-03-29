# bibliotecas
import pyodbc
from datetime import date
import json

#importa variaveis de ambiente
from env_var import env_var

#atribue as variaveis de ambiente
server_endpoint = env_var['server']
porta = env_var['porta']
db_name = env_var['database']
db_username = env_var['username']
db_password = env_var['password']
driver = 'SQL Server'

#setup de conexão com db
def_conn = f'DRIVER={driver};SERVER={server_endpoint};DATABASE={db_name};UID={db_username};PWD={db_password}'
cnn = pyodbc.connect(def_conn)
cursor = cnn.cursor()

class Conexao_DB():

    def test_conn():
        def_conn = f'DRIVER={driver};SERVER={server_endpoint};DATABASE={db_name};UID={db_username};PWD={db_password}'
        cnn = pyodbc.connect(def_conn)
        consulta_nome_db = '''SELECT DB_NAME() as [DB_NAME]'''
        cursor.execute(consulta_nome_db)
        colunas = [coluna[0] for coluna in cursor.description]
        resultados = []
        for linha in cursor.fetchall():
            resultados.append(dict(zip(colunas, linha)))
        json_str = json.dumps(resultados, indent=4, sort_keys=False)
        json_obj = json.loads(json_str)
        return json_obj

    def realizar_consulta(consulta):
        def_conn = f'DRIVER={driver};SERVER={server_endpoint};DATABASE={db_name};UID={db_username};PWD={db_password}'
        cnn = pyodbc.connect(def_conn)
        cursor.execute(consulta)
        colunas = [coluna[0] for coluna in cursor.description]
        resultados = []
        for linha in cursor.fetchall():
            resultados.append(dict(zip(colunas, linha)))
        json_str = json.dumps(resultados, indent=4, sort_keys=False)
        json_obj = json.loads(json_str)
        return json_obj

    def inserir_agente(nome, dt_nasc, email, celular, telefone, sexo, cpf, senha, agente):
        timestamp = date.today()
        insert = f'''insert into {agente} (status, nome, dt_nasc, email, celular, telefone, sexo, cpf, senha, data_criacao) values('True' , '{nome}', '{dt_nasc}', '{email}', '{celular}', '{telefone}', '{sexo}', '{cpf}','{senha}', '{timestamp}')'''
        cursor.execute(insert)
        cnn.commit()
        return Conexao_DB.selecionar_agente_cpf(cpf, agente)[0]['nome'] + ' adicionado'

    def selecionar_agente_cpf(cpf, agente = 'pacientes'):
        consulta = f'''SELECT * FROM {agente} WHERE CPF = {cpf}'''
        resultado = Conexao_DB.realizar_consulta(consulta)
        return resultado
    
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
        # cursor.execute(insert)
        # cnn.commit()
        # return f'Consulta agendadada para: {paciente}, em {data} ás {hora}, com Dr. {medico} para {especialidade}'        
        try:
            cursor.execute(insert)
            cnn.commit()
            return f'Consulta agendadada para: {paciente}, em {data} ás {hora}, com Dr. {medico} para {especialidade}'
        except:
            return 'N/D'
    
    def meus_agendamentos(cpf):
        consulta = f'''SELECT paciente, data_consulta as Dia, left(hora_consulta, 5) as Horário, especialidade as Especialidade, medico as Medico, consultorio as Local from agendamentos where cpf_paciente = {cpf} order by data_consulta asc '''
        return (Conexao_DB.realizar_consulta(consulta))

# testes
# print(Conexao_DB.test_conn())
# print(Conexao_DB.agendar_consulta('Vinicios','222222222' , '01/01/2022', '12:00', 'Consultorio', 'Chico', 'Odonto'))
# print(Conexao_DB.meus_agendamentos('222222222'))
# print(Conexao_DB.autenticar_usuario('testes@teste', 'teste'))
# consulta = '''select * from pacientes where email = 'testes@teste' '''
# Conexao_DB.realizar_consulta(consulta)
# print(Conexao_DB.inserir_agente('willzito', '01/01/1989', 'gabidavila@bla.com.br'," 1199999999", "1100000000", 'f', "0000000020", "senha", 'pacientes'))