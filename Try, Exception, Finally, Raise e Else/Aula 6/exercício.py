def exibirMenu():
    print("====== MENU =====")
    print(" opção 1 - Cadastrar Cliente")
    print(" opção 2 - Listar clientes")
    print(" opção 3 - Consultar por Nome")
    print(" opção 0 - Sair")
    return input("Digite a opção desejada: ")


def cadastrarCliente():
    nome = input("Digite o nome: ")
    telefone = input("Digite o número de celular: ")

    with open("clientes.txt", "a") as clientes:
        clientes.write(f"{nome};{telefone}\n")

    print("\nCliente cadastrado com sucesso!\n")


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


def listarPorNome():

    clientePesquisado = input("Digite o nome do cliente: ").strip().lower()
    encontrado = False

    with open("clientes.txt", "r") as clientes:

        for numero, linha in enumerate(clientes, start=1):

            dados = linha.strip().split(";")

            nome = dados[0]
            telefone = dados[1]

            if nome.strip().lower() == clientePesquisado:

                encontrado = True

                print(f"\n=== CLIENTE {numero} ===")
                print(f"Nome: {nome}")
                print(f"Telefone: {telefone}")

                break

        if not encontrado:
            print("\nCliente não encontrado.\n")


while True:

    opcao = exibirMenu()

    if opcao == "1":
        cadastrarCliente()

    elif opcao == "2":
        listarClientes()

    elif opcao == "3":
        listarPorNome()

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!\n")