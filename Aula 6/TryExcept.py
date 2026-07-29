def listarClientes(): #Adicionando try e except 

    try:
        with open("clientes.txt", "r") as clientes:
            texto = clientes.read()

            print("\nClientes Cadastrados:")

            if texto == "":
                print("Nenhum cliente cadastrado!")
            else:
                print(texto)

    except FileNotFoundError:
        print("O arquivo de clientes ainda não existe.")