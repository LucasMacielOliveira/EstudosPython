alugueis = []

quantidade_alugueis = 0
faturamento_total = 0.0

while True:

    print("\n=== MENU ===")
    print("Opção 1 - Cadastrar")
    print("Opção 2 - Listar todos")
    print("Opção 3 - Consultar por cliente")
    print("Opção 0 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        nome_cliente = input("Digite o nome do cliente: ")
        quantidade_equipamentos = int(input("Digite a quantidade de equipamentos: "))
        valor_diaria = float(input("Digite o valor da diária: "))
        quantidade_dias = int(input("Digite a quantidade de dias: "))

        total = quantidade_equipamentos * valor_diaria * quantidade_dias

        if total < 500:
            percentual_desconto = 0

        elif total < 1000:
            percentual_desconto = 0.05

        else:
            percentual_desconto = 0.10

        valor_desconto = total * percentual_desconto
        valor_final = total - valor_desconto

        novo_aluguel = {
            "cliente": nome_cliente,
            "quantidade_equipamentos": quantidade_equipamentos,
            "valor_diaria": valor_diaria,
            "quantidade_dias": quantidade_dias,
            "valor_original": total,
            "percentual_desconto": percentual_desconto,
            "valor_desconto": valor_desconto,
            "valor_final": valor_final
        }

        alugueis.append(novo_aluguel)

        quantidade_alugueis += 1
        faturamento_total += valor_final

        print("\n=== ALUGUEL CADASTRADO ===")
        print(f"Cliente: {nome_cliente}")
        print(f"Valor original: R$ {total:.2f}")
        print(f"Desconto: R$ {valor_desconto:.2f}")
        print(f"Valor final: R$ {valor_final:.2f}")

    elif opcao == "2":

        if len(alugueis) == 0:
            print("Nenhum aluguel cadastrado.")

        else:
            print("\n=== ALUGUÉIS CADASTRADOS ===")

            for numero, aluguel in enumerate(alugueis, start=1):
                print(f"\nAluguel {numero}")
                print(f"Cliente: {aluguel['cliente']}")
                print(
                    f"Equipamentos: "
                    f"{aluguel['quantidade_equipamentos']}"
                )
                print(f"Valor da diária: R$ {aluguel['valor_diaria']:.2f}")
                print(f"Dias: {aluguel['quantidade_dias']}")
                print(f"Valor original: R$ {aluguel['valor_original']:.2f}")
                print(f"Desconto: R$ {aluguel['valor_desconto']:.2f}")
                print(f"Valor final: R$ {aluguel['valor_final']:.2f}")
                print("-" * 30)

            print(f"\nFaturamento total: R$ {faturamento_total:.2f}")

    elif opcao == "3":
        nome_pesquisado = input("Digite o nome do cliente: ").strip().lower()

        encontrado = False

        for numero, aluguel in enumerate(alugueis, start=1):

            if aluguel["cliente"].strip().lower() == nome_pesquisado:
                encontrado = True

                print(f"\n=== ALUGUEL {numero} ===")
                print(f"Cliente: {aluguel['cliente']}")
                print(
                    f"Equipamentos: "
                    f"{aluguel['quantidade_equipamentos']}"
                )
                print(f"Dias: {aluguel['quantidade_dias']}")
                print(f"Valor final: R$ {aluguel['valor_final']:.2f}")

        if not encontrado:
            print(f"Cliente '{nome_pesquisado}' não encontrado.")

    elif opcao == "0":
        print("\n=== RESUMO FINAL ===")
        print(f"Aluguéis cadastrados: {quantidade_alugueis}")
        print(f"Faturamento total: R$ {faturamento_total:.2f}")
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")