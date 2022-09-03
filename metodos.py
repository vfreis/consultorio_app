# bibliotecas
import pyodbc
from datetime import date

# para conversão e visualização de consultas
import json

#variaveis de ambiente
from env_var import env_var

## atribue as variaveis de ambiente
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

class Metodos:

    def __init__(self, nome, dt_nasc, email, celular, telefone, sexo, cpf):
        self.nome = nome
        self.data_nasc = dt_nasc
        self.email = email
        self.celular = celular
        self.telefone = telefone
        self.sexo = sexo
        self.cpf = cpf

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

    def selecionar_todos_pacientes():
        query = cursor.execute(f"SELECT * FROM pacientes WHERE STATUS = 'True'")
        columns = [column[0] for column in cursor.description]
        results = []
        for row in cursor.fetchall(): 
            results.append(dict(zip(columns, row)))
        jsonstr = json.dumps(results, indent=4, sort_keys=False)
        jsonobj = json.loads(jsonstr)
        # print(jsonobj) # apenas para teste
        return jsonobj

    def inserir_paciente(nome, dt_nasc, email, celular, telefone, sexo, cpf):
        timestamp = date.today()
        sql = f'''insert into pacientes (status, nome, dt_nasc, email, celular, telefone, sexo, cpf, data_criacao) values('True' , '{nome}', '{dt_nasc}', '{email}', '{celular}', '{telefone}', '{sexo}', '{cpf}', '{timestamp}')'''
        cursor.execute(sql)
        cnxn.commit()
        temp = Metodos.paciente_por_cpf(cpf)[0]['nome']
        print(f'paciente {temp} adicionado com sucesso')
        return(Metodos.paciente_por_cpf(cpf))

    def deletar_paciente(cpf):
        sql = f'''UPDATE pacientes SET Status = 'False' WHERE CPF =  {cpf}'''
        cursor.execute(sql)
        cnxn.commit()
        return(Metodos.paciente_por_cpf(cpf))

    def altera_paciente(campo, alteracao, cpf):
        sql = f'''UPDATE pacientes SET {campo} = '{alteracao}' WHERE CPF =  {cpf}'''
        cursor.execute(sql)
        cnxn.commit()
        return(Metodos.paciente_por_cpf(cpf))

# print(altera_paciente('nome', 'edher', '0000000004'))

# inserir_paciente('debouas', '01/01/1989', 'gabidavila@bla.com.br'," 1199999999", "1100000000", 'f', "0000000008")

# print(selecionar_todos_pacientes()) # seleciona todos os clientes

# print(paciente_por_cpf('0000000001'))

# deletar_paciente('0000000005')

# temp = paciente_por_id(1)

# print(temp[0]['cpf'])

