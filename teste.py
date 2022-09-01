# teste library
import pyodbc
# engine = create_engine('sqlite:///clientes.db', echo = True)

## infos do banco
server = 'consultorio-app-alpha.ciofokjqok2t.us-east-1.rds.amazonaws.com'
porta = 1433
database = 'consulta_app_alpha'
username = 'admin'
password = '123456789'

# setup connection
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
print('conectado com ' + database)


#metodos para aplicação
def select_cliente_id(id):
    try:
        sql = "SELECT * FROM [clientes] WHERE ID = " + str(id)
        cursor.execute(sql)
        for r in cursor:
            print(r) # para teste apenas
            return(r)
    except:
        return('N/D')

def select_todos_clientes():
    sql = "SELECT * FROM [clientes]"
    cursor.execute(sql)
    for r in cursor:
        return(r)



def insert_cliente(status, nome, dt_nasc, email, celular, telefone, sexo, cpf):
    # sql = f'''insert into clientes (status, nome, dt_nasc, email, celular, telefone, sexo, cpf) values({status} , {nome}, {dt_nasc}, {email}, {celular}, {telefone}, {sexo}, {cpf} )'''
    sql = '''insert into clientes (status, nome, dt_nasc, email, celular, telefone, sexo, cpf) values( 'true', 'william', '01/01/1989', 'willdavila@bla.com.br', '1199999999', '1100000000', '?', '0000000001')'''
    cursor.execute(sql)
    cnxn.commit()
    print(f'cliente {nome} adicionado com sucesso')

insert_cliente('true', 'william2', '01/01/1989', 'willdavila@bla.com.br'," 1199999999", "1100000000", '?', "0000000001")

# insert_teste = '''insert into clientes (status, nome, dt_nasc, email, celular, telefone, sexo, cpf) values( 'true', 'william', '01/01/1989', 'willdavila@bla.com.br', '1199999999', '1100000000', '?', '0000000001')'''

