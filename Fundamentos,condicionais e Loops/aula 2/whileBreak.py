while True: 
    print("\n MENU ")
    print(" opção 1 - cadastrar")
    print(" opção 2 - consultar")
    print(" opção 0 - sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        print("Cadastrando...")
    elif opcao == "2":
        print("Consultando...")
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")   
