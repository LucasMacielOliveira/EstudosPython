produtos = []

produtosCadastrados = 0;


while True:

    print("\n MENU ")
    print(" opção 1 - cadastrar produto")
    print(" opção 2 - listar produtos")
    print(" opção 3 - Realizar Venda")
    print(" opção 4 - Consultar produto")
    print(" opção 0 - sair")
    print("---------------------------------")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":

        nome_produto = input("Digite o nome do produto: ")
        preco_produto = float(input("Digite o preço do produto: "))
        estoque_produto = int(input("Digite a quantidade em estoque: "))
        quantidade_vendida = 0

        produto = {
        "nome": nome_produto,
        "preco": preco_produto,
        "estoque": estoque_produto,
        "quantidade_vendida": quantidade_vendida
        }

        produtos.append(produto)
        produtosCadastrados += 1

        print("\n=== PRODUTO CADASTRADO ===")
        print(f"Nome: {nome_produto}")
        print(f"Preço: R$ {preco_produto:.2f}")
        print(f"Estoque: {estoque_produto}")
    
    elif opcao == "2":
        # Listar produtos
        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            print("\n -- Produtos Cadastrados -- ")
            for numero, produto in enumerate(produtos, start = 1):

                print(f"\nProduto {numero}")
                print(f"nome: {produto['nome']}")
                print(f"Preço R$: {produto['preco']}")
                print(f"Estoque: {produto['estoque']}")

    elif opcao == "3":
        # Realizar venda
        produtoVenda = input("Digite o produto a ser vendido: ").strip().lower()

        disponivel = False

        for produto in produtos: 

            if produtoVenda == produto['nome'].strip().lower():
                disponivel = True

                quantidadeVenda = int(input("Digite a quantidade desejada: "))

                if quantidadeVenda <= produto['estoque']:
                   produto['estoque'] -= quantidadeVenda
                   produto['quantidade_vendida'] += quantidadeVenda
                   valorVenda = quantidadeVenda * produto['preco']

                   print(f" o valor da venda foi de {valorVenda:.2f}")

                else: 
                    print("estoque insuficiente!!")

        if not disponivel:
            print("produto não disponível")


    elif opcao == "4":   

        nomeProduto_pesquisado = input("Digite o nome do produto: ").strip().lower()

        encontrado = False

        for numero, produto in enumerate(produtos, start=1):

            if produto['nome'].strip().lower() == nomeProduto_pesquisado:
                encontrado = True

                print(f"\n -- PRODUTO {numero} -- ")
                print(f"Nome: {produto['nome']}")
                print(f"Estoque: {produto['estoque']}")
                print(f"Quantidade Vendida: {produto['quantidade_vendida']}")

        if not encontrado: 
            print("produto não encontrado")

    elif opcao == "0":
        print("Saindo do programa")
        break

    else:
        print("Opção inválida")