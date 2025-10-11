import sqlite3

# Criando conexao
conn = sqlite3.connect('escola.db') # DB_URI
# ele vai ntermediar as execucoes no banco 
cursor = conn.cursor()

# Relacionais 
# MYSQL, MariaDb, Postgres, SQL Server, Microsoft SQL
# DDL -> Data Daefinition Language _> Linguagem de Definiao de Dados
# Comandos Estruturais

# Criar uma Tabela 
cursor.execute('CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)')

# DML _> Data Manipulation Language _> Linguagem de Manipulacao de Dados 
cursor.execute('INSERT INTO alunos (nome, idade) VALUES ("Arthur", 46)')
# Executar a consulta 
conn.commit()

print("\n Lista de Alunos: ")
cursor.execute("SELECT * FROM alunos") 
for linha in cursor.fetchall():
    print(linha)

