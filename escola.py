# ESCOLA SENAI 
#nota1 = 7
#nota2 = 3
#nota3 = 8
#nota4 = 10

# QUAL a média ?

nota1 = float(input(" Digite a nota1 : "))
nota2 = float(input(" Digite a nota2 : "))
nota3 = float(input(" Digite a nota3 : ")) 
nota4 = float(input(" Digite a nota4 : "))

media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 5:
    print("\033[31mA Media do Aluno é :\033[m ", media)
    print(" \033[31mParabens voce foi aprovado !\033[0m")
else:
    print("\033[31mA Media do Aluno é :\033[m ", media)
    print(" \033[31mSORRY voce foi Reprovado !\033[0m")