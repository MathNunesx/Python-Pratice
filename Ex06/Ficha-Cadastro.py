option = 0
ficha = {} #empty dictionary

while option != 4:
    print("\n ----- FICHA CADASTRAL -----")
    print("1 - Incluir informações na ficha")
    print("2 - Recuperar informação da ficha")
    print("3 - Exibir a ficha completa")
    print("4 - Sair")
    option = int(input("infomre a opção desejada: "))
    if option == 1:
        key = input("\n Em qual campo deseja inserir os dados? ")
        valor = input(f" Qual é o dado que deseja incluir no campo {key}? ")
        ficha.update({key:valor})

    elif option == 2:
        print(f"\n Os campos disponiveis na ficha são: {ficha.keys()}")
        key = input("Você deseja opter dados de qual campo? ")
        if key in ficha.keys():
            print(f"{key} --> {ficha.get(key)}")
        else:
            print("O campo informado não existe na ficha =(.")

    elif option == 3:
        print("\n ---FICHA---")
        for campo, dado in ficha.items():
            print(f"{campo.upper()} --> {dado}")
            print("----------------------------------------------")

    elif option == 4:
        print("Saindo do sistema....")
        break
    else:
        print("Favor escolha uma opção valida!!!")