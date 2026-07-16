nomeCliente = str(input("Digite o nome do cliente: "))
quantEquipamentos = int(input("Digite a quantidade de equipamentos: "))
valorDiaria = float(input("Digite o valor da diária: "))
diasAlugados = int(input("Digite a quantidade de dias alugados: "))

valorTotal = valorDiaria * diasAlugados * quantEquipamentos

if valorTotal < 500:
    print("não há desconto, o valor total é R$" + str(valorTotal))
elif valorTotal >= 500 and valorTotal < 1000:
    print("há desconto de 5%, o valor original é R$" + str(valorTotal) + " e o valor total é R$" + str(valorTotal * 0.95))
else:
    print("há desconto de 10%,o valor original é R$" + str(valorTotal) + " e o valor total é R$" + str(valorTotal * 0.90))


