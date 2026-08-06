produtos = []
produtosCadastrados = 0

def exibirMenu():
    print("\nMENU")
    print(" opção 1 - cadastrar produto")
    print(" opção 2 - listar produtos")
    print(" opção 3 - Realizar Venda")
    print(" opção 4 - Consultar produto")
    print(" opção 0 - sair")
    print("---------------------------------")
    return input("Digite a opção desejada: ").strip()

def cadastrarProduto(produtos):
    global produtosCadastrados

    nome_produto = input("Digite o nome do produto: ").strip()
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
    print(f"Total de produtos cadastrados: {produtosCadastrados}")

def listarProduto(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print("\n -- Produtos Cadastrados -- ")
        for numero, produto in enumerate(produtos, start=1):
            print(f"\nProduto {numero}")
            print(f"nome: {produto['nome']}")
            print(f"Preço R$: {produto['preco']:.2f}")
            print(f"Estoque: {produto['estoque']}")

def realizar_venda(produtos):
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

                print(f"o valor da venda foi de {valorVenda:.2f}")
            else:
                print("estoque insuficiente!!")
            break

    if not disponivel:
        print("produto não disponível")

def buscar_produto(produtos):
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

while True:
    opcao = exibirMenu()

    if opcao == "1":
        cadastrarProduto(produtos)
    elif opcao == "2":
        listarProduto(produtos)
    elif opcao == "3":
        realizar_venda(produtos)
    elif opcao == "4":
        buscar_produto(produtos)
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")