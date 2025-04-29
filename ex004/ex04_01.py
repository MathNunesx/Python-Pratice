opcao = 0
while opcao != 3:
    print("1 - Receber um elogio")
    print("2 - Calcular o fatorial de um número")
    print("3 - Sair")
    opcao = int(input("Informe o número da opção desejada e depois tecle ENTER: "))
    if opcao == 1:
        #instruções para o caso de o usuário ter escolhido a opção 1
        print("Você é uma pessoa muito inteligente!")
    elif opcao == 2:
        #instruções para o caso de o usuário ter escolhido a opção 2
        numero = int(input("Informe o número do qual deseja obter o fatorial "))
        fat = numero
        for valor in range(1, numero, 1):
            fat = fat * valor
        print(f"O fatorial do número informado é: {fat} ")
    elif opcao == 3:
        #Instruções para o caso de o usuário ter escolhido a opção 3
        print("Saindo do sistema...")
        break
    else:
        #Instruções para o caso de o usuário não ter escolhido nenhuma opção válida
        print("Você não selecionou nenhuma opção válida. Tente novamente: ")