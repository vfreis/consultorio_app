import pyodbc

# para conversão e visualização de consultas
import json

from datetime import date


#variaveis de ambiente
from env_var import env_var

## variaveis de ambiente
server = env_var['server']
porta = env_var['porta']
database = env_var['database']
username = env_var['username']
password = env_var['password']

# setup connection
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
print('conectado com ' + database)

#metodos para aplicação
def paciente_por_id(id):
    query = cursor.execute(f"SELECT * FROM pacientes WHERE id = {id}")
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall(): 
        results.append(dict(zip(columns, row)))
    jsonstr = json.dumps(results, indent=4, sort_keys=False)
    jsonobj = json.loads(jsonstr)
    # print(jsonobj) # apenas para teste
    return jsonobj

def paciente_por_cpf(cpf):
    query = cursor.execute(f"SELECT * FROM pacientes WHERE CPF = {cpf}")
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall(): 
        results.append(dict(zip(columns, row)))
    jsonstr = json.dumps(results, indent=4, sort_keys=False)
    jsonobj = json.loads(jsonstr)
    # print(jsonobj) # apenas para teste
    return jsonobj

def select_todos_pacientes():
    query = cursor.execute("SELECT * FROM pacientes WHERE status = 'True'")
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    jsonstr = json.dumps(results, indent=4, sort_keys=False)
    jsonobj = json.loads(jsonstr)
    # print(jsonobj) # apenas para teste
    return jsonobj

def inserir_paciente(status, nome, dt_nasc, email, celular, telefone, sexo, cpf):
    timestamp = date.today()
    sql = f'''insert into pacientes (status, nome, dt_nasc, email, celular, telefone, sexo, cpf, data_criacao) values('{status}' , '{nome}', '{dt_nasc}', '{email}', '{celular}', '{telefone}', '{sexo}', '{cpf}', '{timestamp}')'''
    cursor.execute(sql)
    cnxn.commit()
    print(f'cliente {nome} adicionado com sucesso')
    print(paciente_por_id(id))

def deletar_paciente(id):
    sql = f'''UPDATE pacientes SET Status = 'False' WHERE ID =  {id}'''
    cursor.execute(sql)
    cnxn.commit()
    print(paciente_por_id(id))

# insert_cliente('true', 'tiuzin', '24/24/1989', 'willdavila@bla.com.br', " 1199999999", "1100000000", '?', "0000000001") # não sabemos pq nao funciona

# inserir_paciente('true', 'tiuzin', '01/01/1989', 'willdavila@bla.com.br'," 1199999999", "1100000000", '?', "0000000001")

# select_todos_clientes() # seleciona todos os clientes

# delete_cliente(4)

temp = paciente_por_id(1)

print(temp[0]['cpf'])

