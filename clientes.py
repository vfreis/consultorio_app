from sqlalchemy import create_engine, insert
from sqlalchemy.sql import text

engine = create_engine('sqlite:///clientes.db', echo = True)


## infos do banco
endpoint = 'consultorio-app-alpha.ciofokjqok2t.us-east-1.rds.amazonaws.com'
porta = 1433
nome_db = 'dbo.clientes'




## devera ser alterado para um usuário apenas para o servidor
usuario = 'admin'
senha = '123456789'


# def adicionar_cliente(name,	birth,	gender,	mail,	phone,	password,	ss_number,	stat):
#     with engine.connect() as con:
#         statement = text("""INSERT INTO 
#         clientes (nome, nascimento, idade, sexo, email, telefone, senha, cpf, status)
#         VALUES (:nome, :nascimento, :idade, :sexo, :email, :telefone, :senha, :cpf, :status )
#          """)
#         rs = con.execute(statement, 
#         nome = name,
#         nascimento = birth,
#         sexo = gender,
#         email = mail,
#         telefone = phone,
#         senha = password,
#         cpf = ss_number,
#         status = stat
#         )
#         return rs

def adicionar_cliente(nome_1, cpf):
    with engine.connect() as con:



def retorna_clientes():
    with engine.connect() as con:
        statement = text("""SELECT * FROM clientes""")
        rs = con.execute(statement)
        clientes = rs.fetchall()
        return clientes