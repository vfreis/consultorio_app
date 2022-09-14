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
mysql.init_app(app)

# Conexão com o DB
conn = mysql.connect()
cursor =conn.cursor()

cursor.execute("SELECT * from pacientes")
data = cursor.fetchone()
print(data)


