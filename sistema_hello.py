# Desenha tela GUI
import tkinter as tk
from tkinter import messagebox 

# Exibir o nome da Pessoa 
def mostrar_mensagem():
    nome = entrada_nome.get()
    messagebox.showinfo("Saudaçao", f"Ola, {nome} Bem Vindo !")

# Criar uma Janela
janela = tk.Tk()

# Dar o nome e o Tamanho 
janela.title("Ola Tkinter")
janela.geometry("300x150") # 300 Pixels por 150 Pixels 

# Criar o label do input 
rotulo_nome = tk.Label(janela, text="Digite o seu nome :", bg="lightblue")  
rotulo_nome.pack(pady=5) # Configurando estilo de texto 

# Criando Campo de Texto
entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5)
botao = tk.Button(janela, text="Cliquue Aqui", command=mostrar_mensagem, bg="green")    

botao.pack(pady=20)

# Inicia O Tk
janela.mainloop() 