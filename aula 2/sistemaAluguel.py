''''
Quando o usuário escolher 1, peça:

Nome do cliente;
quantidade de equipamentos;
valor da diária;
quantidade de dias.

Depois, utilize a mesma regra:

Abaixo de R$500: sem desconto;
de R$500 até R$999,99: 5%;
a partir de R$1.000: 10%.

Após mostrar o resultado, o menu deve aparecer novamente.

Quando o usuário digitar 0, apresente:

Quantidade total de aluguéis cadastrados;
faturamento total, considerando os descontos;
mensagem de encerramento.
'''


quantidade_alugueis = 0
faturamento_total = 0.0

while True:

    print("\n MENU")
    print(" opção 1 - cadastrar")
    print(" opção 2 - consultar")
    print(" opção 0 - sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        nome_cliente = input("Digite o nome do cliente: ")
        quantidade_equipamentos = int(input("Digite a quantidade de equipamentos: "))
        valor_diaria = float(input("Digite o valor da diária: "))
        quantidade_dias = int(input("Digite a quantidade de dias: "))

        total = quantidade_equipamentos * valor_diaria * quantidade_dias


        if total < 500:
            print(f"Total a pagar: R${total:.2f} (sem desconto)")
        elif total < 1000:
            desconto = total * 0.95
            print(f"Total a pagar: R${desconto:.2f} (5% de desconto) - o valor original era R${total:.2f}")
        else: 
            desconto = total * 0.90
            print(f"Total a pagar: R${desconto:.2f} (10% de desconto) - o valor original era R${total:.2f}")
            
        quantidade_alugueis += 1
        faturamento_total += desconto

    elif opcao == "2":
        print(f"Quantidade total de aluguéis cadastrados: {quantidade_alugueis}")
        print(f"Faturamento total: R${faturamento_total:.2f}")

    elif opcao == "0":
        print(f"Quantidade total de aluguéis cadastrados: {quantidade_alugueis}")
        print(f"Faturamento total: R${faturamento_total:.2f}")
        print("Encerrando o programa...")
        break

    else: 
        print("Opção inválida. Tente novamente.")
            

