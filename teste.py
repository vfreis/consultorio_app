# teste library
import pymssql
import pyodbc 
from os import getenv
import pymssql
from sqlalchemy import create_engine, insert
from sqlalchemy.sql import text

# engine = create_engine('sqlite:///clientes.db', echo = True)



## infos do banco
server = 'consultorio-app-alpha.ciofokjqok2t.us-east-1.rds.amazonaws.com'
porta = 1433
database = 'consulta_app_alpha'

username = 'admin'
password = '123456789'


# setup connection

try:
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    print('conectado com ' + database)
except: 
        print('não foi possivel conectar')
