idade = int(input("Digite sua idade : "))

if idade < 18 :
    print("\033[31mVoce é menor de idade\033[0m")
else:
    print("\033[31mMaior de idade\033[0m")

    if idade >= 18 and idade <= 70:
        print("\033[31mSeu Voto é Obrigatório , BOA SORTE PARA ENCONTRAR ALGUM CANDIDATO QUE PRESTE !!!\033[0m ")
    else:
        print("\033[31mSeu Voto é Facultaivo, MELHOR NAO TEM NENHUM QUE PRESTE !!!\033[0m")

