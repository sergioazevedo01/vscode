import sqlite3

conn = sqlite3.connect("livors.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        autor TEXT,
        ano INTEGER
    )
''')

# LOOP PRINCIPAL 
while True:
    print("=== CADASTRO DE LIVROS ===")
    print("1 - Cadastrar Novo Livro")
    print("2 - Listar Livros")
    print("3 - Sair")

    opcao = input("Escolha uma opcao...")

    if opcao == "1":
        titulo = input("Titulo do Livro: ")
        autor = input("Autor: ")
        ano = int(input("Ano da publicacao: "))

        cursor.execute("INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)",
        (titulo, autor, ano))

        conn.commit() # confirmar insersao de dados
        print(f'Livro (titulo) criado com sucesso!')

    elif opcao == "2":
        print("Livros cadastrados")
        for linha in cursor.execute("SELECT * FROM livros"):
            print(f'ID: {linha[0]} | {linha[1]} | autor {linha[2]} | Ano {linha[3]}')

    elif opcao == "3":
        print("Ecerrando o Programa...")
        break
        
    else:
        print("Opcao Invalida, tente novamente ... ")